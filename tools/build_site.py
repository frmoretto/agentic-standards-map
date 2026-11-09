"""Build the static site of the map: one page per entry, the notes, a graph, the data files.

Usage: python tools/build_site.py [--commit HEAD] [--source DIR] [--out site] [--base-url URL] [--repo-url URL] [--doi DOI] [--version-doi DOI] [--cite-version V]

The site is generated, never edited by hand, and only from the PUBLIC export: unless --source is given, the script runs
tools/export_public.py on the commit (the same exclusions as the public bundle) in a temporary folder and reads entries/ and
notes/ from there. With --source DIR it reads DIR (for example the public repository itself) and does no export.

Output (folder site/, in .gitignore):
  index.html            public summary, "Where things stand", payment matrix, list of entries, link to graph and calendar
  entries/<id>.html     one page per entry, all the fields of the entry
  seams.html intro.html disclosure.html calendar.html method.html ai-use.html   the notes, same text as notes/
  graph.html, graph.svg, graph-seams.svg                  the graph of the entries (static SVG, every node a link)
  map.json              the entries as in the YAML (schema v2, see entries/_schema.md) and the graph
  calendar.ics          one event per committed_next item with a full date
  sitemap.xml, robots.txt, style.css

The pages need no JavaScript, no font and no script from another site, and have no tracking. GitHub Pages is NOT enabled
by this script: see .github/workflows/pages.yml.disabled. --base-url is the address the site will have (a declared
placeholder until then): it is used for canonical links, the sitemap, JSON-LD and the UID domain-free calendar URLs.
"""
import argparse
import csv
import datetime
import html as htmllib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_map import seam_members, check_seams, find_italian, italian_selftest, ITALIAN_WORDS, next_date, source_label  # noqa: E402  the same reader and rules as the check of the entries
ROOT = HERE.parent
PLACEHOLDER_BASE = "https://example.invalid/"
DEFAULT_REPO = "https://github.com/frmoretto/agentic-standards-map"
SITE_TITLE = "Agentic standards map"
SITE_NAME = "Agentic Standards Map"   # the name in the header of every page and in the breadcrumb of the entries
TAGLINE = "Who is standardising agentic commerce, where, and what they have committed to next."   # under the name in the header of every page; also the second line of public/README.md
INTRO_STRIP = "Maintained by %s. <strong>New here?</strong> Start with the %s."   # the tagline in the header already says what the map is
AUTHOR = "Francesco Marinoni Moretto"
ORCID_ID = "0009-0004-0096-4712"
ORCID = "https://orcid.org/" + ORCID_ID
GITHUB_USER = "frmoretto"
GITHUB = "https://github.com/" + GITHUB_USER
LINKEDIN_USER = "francesco-moretto"
LINKEDIN = "https://www.linkedin.com/in/" + LINKEDIN_USER + "/"
ISSUES_URL = DEFAULT_REPO + "/issues"
NEW_ISSUE_URL = DEFAULT_REPO + "/issues/new/choose"   # the issue templates (Correction), linked from the cadence lines
AUTHOR_LINE = "independent researcher on agentic commerce, Milan"
AUTHOR_PART = "I have taken part in some of the venues mapped; the %s lists where, and the entries concerned say so."
CITE_REQUEST = "Please cite the entry id, the date it was read and the DOI."
CITE_GENERAL = "To cite the map in general, use https://doi.org/%s."
CREATOR = {"@type": "Person", "name": AUTHOR, "identifier": ORCID, "sameAs": [ORCID, GITHUB, LINKEDIN], "url": GITHUB}
LICENCE_URL = "https://creativecommons.org/licenses/by/4.0/"
ORDER = ["W3C", "IETF", "GS1", "UN/CEFACT", "Other standards bodies", "AAIF", "Linux Foundation", "Independent", "Industry"]
COLOURS = {"W3C": "#1f6fb2", "IETF": "#c0392b", "GS1": "#2e8b57", "UN/CEFACT": "#8e6bbf", "Other standards bodies": "#5a7d2a", "AAIF": "#d98c10",
           "Linux Foundation": "#7f8c8d", "Independent": "#b5499b", "Industry": "#127c82"}
SEAM_COLOURS = {"S1": "#1f6fb2", "S2": "#2e8b57", "S3": "#c0392b", "S4": "#d98c10"}
CLASSES = {"normative": "normative text", "decision": "official decision or commitment", "statement": "maintainer or chair statement",
           "third-party": "participant or third party"}
MATRIX_COLS = [("governance", "Owner / governance"), ("version_state", "Version and state"), ("signs", "What it signs"),
               ("signer", "Who signs"), ("record", "Receipt or record"), ("dispute", "Dispute"), ("source", "Source")]
# the latest version that has a tag: updated by hand when a release is made (with RELEASED_TAG of tools/export_public.py)
LATEST_RELEASE = ("1.4", "v1.4")
MATRIX_ORDER = ["ap2", "ucp", "acp", "x402", "visa-tap", "verifiable-intent", "emvco-agentic-payments-framework"]
NOTE_PAGES = [  # (source file in the export, page, title, description)
    ("notes/intro.md", "intro.html", "Introduction", "Why the map exists, who it is for and how to read it."),
    ("notes/seams.md", "seams.html", "Seams", "Where the venues meet: discovery layers, product and seller identity, agent identity and delegation, signed terms and receipts, and what is not established."),
    ("notes/disclosure.md", "disclosure.html", "Disclosure", "Where the author of the map has taken part in the venues it maps, with dates and links."),
    ("notes/calendar-2026.md", "calendar.html", "Calendar", "Dated public events of the venues in the map for the next 60 days."),
    ("METHOD.md", "method.html", "Method", "Inclusion rules, how an entry is written, source classes and how negatives are read."),
    ("AI-USE.md", "ai-use.html", "Declaration of AI use", "How language model assistants were used for the map and what the author checked."),
]
LINK_MAP = {"map-bundle.md#part-seams": "seams.html", "map-bundle.md#part-calendar": "calendar.html", "map-bundle.md#part-status": "index.html#where-things-stand",
            "map-bundle.md#part-matrix": "index.html#matrix", "map-bundle.md#part-disclosure": "disclosure.html", "map-bundle.md": "map-bundle.md",
            "entries/": "index.html#entries", "METHOD.md": "method.html", "AI-USE.md": "ai-use.html"}
REPO_FILES = ("CONTRIBUTING.md", "LICENSE", "LICENSE-CODE")


DATE_CELL = re.compile(r"(?:approx\. )?\d{4}-\d{2}-\d{2}.{0,20}", re.S)   # a table cell that holds a date, "approx." before it, a short suffix (", 14:00", " to 2026-11-20")


def short_link_text(url):
    """Visible text of a bare URL in a table cell (the href stays the full URL). GitHub: owner/repo#N for issues, pull
    requests and discussions, owner/repo: file for /blob/ and /tree/, owner/repo for the repository. Datatracker: the
    document or group name, "group: page" for other group pages, "datatracker: last segment" for meeting pages. Other
    sites: host without www., then /…/ and the last segment, cut to 40 characters."""
    u = urllib.parse.urlparse(url)
    host = u.netloc.lower()
    host = host[4:] if host.startswith("www.") else host
    parts = [urllib.parse.unquote(x) for x in u.path.split("/") if x]

    def cut(s):
        return s if len(s) <= 40 else s[:39] + "…"
    if host == "github.com" and len(parts) >= 2:
        repo = "%s/%s" % (parts[0], parts[1])
        if len(parts) == 2:
            return repo
        if len(parts) >= 4 and parts[2] in ("issues", "pull", "discussions") and parts[3].isdigit():
            return "%s#%s" % (repo, parts[3])
        if len(parts) >= 4 and parts[2] in ("blob", "tree"):
            return "%s: %s" % (repo, cut(parts[-1]))
    if host == "datatracker.ietf.org" and len(parts) >= 2:
        if parts[0] == "doc":
            return cut(parts[1])
        if parts[0] in ("group", "wg", "rg"):
            return parts[1] if len(parts) == 2 or parts[-1] == "about" else "%s: %s" % (parts[1], cut(parts[-1]))
        if parts[0] == "meeting":
            return "datatracker: " + cut(parts[-1])
    if not parts:
        return host
    return host + "/" + (cut(parts[0]) if len(parts) == 1 else "…/" + cut(parts[-1]))


def short_link_selftest():
    """the short label of known URLs, the date-cell rule on cells that must and must not match"""
    cases = {"https://github.com/w3c/tpac2026-breakouts/issues/22": "w3c/tpac2026-breakouts#22",
             "https://github.com/aaif/ws-taxonomy-landscape/pull/61": "aaif/ws-taxonomy-landscape#61",
             "https://github.com/aaif/ws-taxonomy-landscape/blob/main/charter/charter.md": "aaif/ws-taxonomy-landscape: charter.md",
             "https://github.com/w3c/tpac2026-breakouts": "w3c/tpac2026-breakouts",
             "https://datatracker.ietf.org/doc/charter-ietf-dawn/": "charter-ietf-dawn",
             "https://datatracker.ietf.org/group/dawn/about/": "dawn",
             "https://datatracker.ietf.org/meeting/127/agenda.json": "datatracker: agenda.json",
             "https://www.w3.org/2026/09/ecommerce-agents/": "w3.org/…/ecommerce-agents",
             "https://example.org/": "example.org",
             "https://example.org/" + "x" * 50: "example.org/" + "x" * 39 + "…"}
    for u, want in cases.items():
        assert short_link_text(u) == want, (u, short_link_text(u), want)
    for c in ("2026-10-15", "2026-11-17, 16:30", "2026-11-16 to 2026-11-20", "approx. 2026-10-19"):
        assert DATE_CELL.fullmatch(c), c
    for c in ("Version 1.2 (2026-10-26)", "2026-10-15 the IESG approved the charter of the group", "2026-10"):
        assert not DATE_CELL.fullmatch(c), c


def esc(s):
    return htmllib.escape(str(s), quote=False)


def attr(s):
    return htmllib.escape(str(s), quote=True)


def d(v):
    return v.isoformat() if isinstance(v, (datetime.date, datetime.datetime)) else str(v)


def one_line(v):
    return " ".join(str(v or "").split())


def slug(text):
    t = re.sub(r"[^\w\s-]", "", re.sub(r"<[^>]+>", "", text).lower())
    return re.sub(r"\s+", "-", t.strip())


def short_desc(text, limit=160):
    t = one_line(text)
    if len(t) <= limit:
        return t
    cut = t[:limit].rsplit(" ", 1)[0].rstrip(" ,;:(")
    return cut + "\u2026"


def short_name(name):
    n = re.split(r" \(|, | - |: ", name)[0].strip()
    return n if len(n) <= 28 else n[:27].rstrip() + "\u2026"


# ---- markdown (the subset the notes use) ---------------------------------------------------------------------------

class Md:
    def __init__(self, ids, repo_url, rel=""):
        self.ids, self.repo_url, self.rel = ids, repo_url, rel
        self.unmapped = []

    def href(self, h):
        if h in LINK_MAP:
            return self.rel + LINK_MAP[h]
        if h in REPO_FILES:
            return self.repo_url + "/blob/main/" + h
        if re.match(r"^(https?:|mailto:|#)", h):
            return h
        self.unmapped.append(h)
        return None

    def inline(self, s):
        stash = []

        def keep(html_):
            stash.append(html_)
            return "\x00%d\x00" % (len(stash) - 1)

        def code(m):
            c = m.group(1)
            if c in self.ids:
                return keep('<a href="%sentries/%s.html"><code>%s</code></a>' % (self.rel, attr(c), esc(c)))
            return keep("<code>%s</code>" % esc(c))

        s = re.sub(r"`([^`]+)`", code, s)

        def link(m):
            h = self.href(m.group(2))
            inner = self.inline_plain(m.group(1))
            if h is None:
                return keep(inner)
            ext = ' rel="noopener"' if h.startswith("http") else ""
            return keep('<a href="%s"%s>%s</a>' % (attr(h), ext, inner))

        s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)

        def bare(m):
            u = m.group(0)
            tail = ""
            while u and u[-1] in ".,;:)":
                tail = u[-1] + tail
                u = u[:-1]
            return keep('<a href="%s" rel="noopener">%s</a>' % (attr(u), esc(u))) + tail

        s = re.sub(r"https?://[^\s<>\x00\"]+", bare, s)
        out = self.inline_plain(s)
        while "\x00" in out:  # a link can hold a code span: restore until nothing is left
            out = re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], out)
        return out

    def inline_plain(self, s):
        s = esc(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<em>\1</em>", s)
        return s

    def render(self, text, skip_h1=False):
        lines = text.replace("\r\n", "\n").split("\n")
        out, i, n = [], 0, len(lines)

        def is_row(l):
            return l.lstrip().startswith("|")

        def cells(l):
            l = l.strip().strip("|")
            parts, cur, k = [], "", 0
            while k < len(l):
                if l[k] == "\\" and k + 1 < len(l) and l[k + 1] == "|":
                    cur += "|"
                    k += 2
                    continue
                if l[k] == "|":
                    parts.append(cur.strip())
                    cur = ""
                else:
                    cur += l[k]
                k += 1
            parts.append(cur.strip())
            return parts

        pending_id = None
        while i < n:
            l = lines[i]
            if not l.strip():
                i += 1
                continue
            m = re.match(r'^<a id="([^"]+)"></a>\s*$', l)
            if m:
                pending_id = m.group(1)
                i += 1
                continue
            if l.startswith("```"):
                j = i + 1
                buf = []
                while j < n and not lines[j].startswith("```"):
                    buf.append(lines[j])
                    j += 1
                out.append("<pre><code>%s</code></pre>" % esc("\n".join(buf)))
                i = j + 1
                continue
            m = re.match(r"^(#{1,6}) (.*)$", l)
            if m:
                lvl = len(m.group(1))
                if not (skip_h1 and lvl == 1):
                    hid = pending_id or slug(m.group(2))
                    out.append('<h%d id="%s">%s</h%d>' % (lvl, attr(hid), self.inline(m.group(2)), lvl))
                pending_id = None
                i += 1
                continue
            if l.strip() == "---":
                out.append("<hr>")
                i += 1
                continue
            if is_row(l) and i + 1 < n and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
                head = cells(l)
                j = i + 2
                rows = []
                while j < n and is_row(lines[j]):
                    rows.append(cells(lines[j]))
                    j += 1
                t = ['<div class="scroll"><table><thead><tr>%s</tr></thead><tbody>' % "".join("<th>%s</th>" % self.inline(c) for c in head)]
                for r in rows:
                    t.append("<tr>%s</tr>" % "".join("<td>%s</td>" % self.inline(c) for c in r))
                t.append("</tbody></table></div>")
                out.append("".join(t))
                i = j
                continue
            if l.startswith(">"):
                buf = []
                while i < n and lines[i].startswith(">"):
                    buf.append(lines[i].lstrip(">").strip())
                    i += 1
                out.append("<blockquote><p>%s</p></blockquote>" % self.inline(" ".join(buf)))
                continue
            mm = re.match(r"^(\s*)([-*]|\d+\.) (.*)$", l)
            if mm:
                items = []
                while i < n:
                    mm = re.match(r"^(\s*)([-*]|\d+\.) (.*)$", lines[i])
                    if mm:
                        items.append([len(mm.group(1)), mm.group(2), mm.group(3)])
                        i += 1
                    elif lines[i].strip() and lines[i].startswith("  ") and items:
                        items[-1][2] += " " + lines[i].strip()
                        i += 1
                    else:
                        break
                out.append(self.list_html(items))
                continue
            buf = []
            while i < n and lines[i].strip() and not re.match(r"^(#{1,6} |```|---$|\s*([-*]|\d+\.) |\||>|<a id=)", lines[i]):
                buf.append(lines[i].strip())
                i += 1
            if buf:
                out.append("<p>%s</p>" % self.inline(" ".join(buf)))
            else:
                i += 1
        return "\n".join(out)

    def list_html(self, items):
        res, stack = [], []
        for indent, mark, text in items:
            tag = "ol" if mark[0].isdigit() else "ul"
            while stack and stack[-1][0] > indent:
                res.append("</li></%s>" % stack.pop()[1])
            if not stack or stack[-1][0] < indent:
                res.append("<%s>" % tag)
                stack.append((indent, tag))
            else:
                res.append("</li>")
            res.append("<li>%s" % self.inline(text))
        while stack:
            res.append("</li></%s>" % stack.pop()[1])
        return "".join(res)


# ---- data ---------------------------------------------------------------------------------------------------------

def load_entries(src):
    entries = {}
    for p in sorted((src / "entries").glob("*.yaml")):
        e = yaml.safe_load(p.read_text(encoding="utf-8"))
        e["_file"] = p.name
        entries[e["id"]] = e
    return entries


def key(e):
    return (ORDER.index(e["org"]) if e["org"] in ORDER else 99, e["name"])


def graph_data(entries, seams):
    edges = sorted({tuple(sorted((i, o))) for i, e in entries.items() for o in (e.get("overlaps") or [])})
    unknown_overlap = [(i, o) for i, e in entries.items() for o in (e.get("overlaps") or []) if o not in entries]
    unknown_seam = [(k, i) for k, (_, ids) in seams.items() for i in ids if i not in entries]
    return edges, unknown_overlap, unknown_seam


# ---- graph (static SVG) -------------------------------------------------------------------------------------------

SVG_DESC = ("Each circle is an entry of the map and links to its page; the colour is the kind of body behind it, a filled circle is a core entry and a dashed circle a context entry.")


def svg_open(w, h, title, tid="gt", desc=SVG_DESC):
    return ('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 %d %d" width="%d" height="%d" '
            'role="img" aria-labelledby="%s %sd" font-family="system-ui, sans-serif">\n<title id="%s">%s</title>\n<desc id="%sd">%s</desc>\n'
            % (w, h, w, h, tid, tid, tid, esc(title), tid, esc(desc)))


def node_svg(e, x, y, label_x, anchor="start", prefix="entries/", fs=11, maxlen=28, tags=None):
    c = COLOURS.get(e["org"], "#555")
    core = e["tier"] == "core"
    circ = ('<circle cx="%.1f" cy="%.1f" r="7" fill="%s" stroke="#222" stroke-width="2"/>' % (x, y, c) if core else
            '<circle cx="%.1f" cy="%.1f" r="7" fill="#fff" stroke="%s" stroke-width="2.5" stroke-dasharray="3 2"/>' % (x, y, c))
    href = "%s%s.html" % (prefix, e["id"])
    label = e["name"] if False else short_name(e["name"])
    if len(label) > maxlen:
        label = label[:maxlen - 1].rstrip() + "\u2026"
    tagsvg = ""
    if tags:
        tagsvg = "".join('<tspan fill="%s" font-size="%d" font-weight="bold" stroke="none"> %s</tspan>' % (SEAM_COLOURS[t], fs - 2, t) for t in tags)
    return ('<a xlink:href="%s" href="%s" target="_top"><title>%s (%s, %s)</title>%s'
            '<text x="%.1f" y="%.1f" font-size="%d" text-anchor="%s" fill="#111" stroke="#fff" stroke-width="3" paint-order="stroke">%s%s</text></a>\n'
            % (href, href, attr(e["name"]), attr(e["org"]), e["tier"], circ, label_x, y + 4, fs, anchor, esc(label), tagsvg))


def legend_svg(x, y, overlap=True):
    out = ['<g font-size="11" fill="#111">']
    out.append('<circle cx="%d" cy="%d" r="7" fill="#777" stroke="#222" stroke-width="2"/><text x="%d" y="%d">core entry</text>' % (x, y, x + 12, y + 4))
    out.append('<circle cx="%d" cy="%d" r="7" fill="#fff" stroke="#777" stroke-width="2.5" stroke-dasharray="3 2"/><text x="%d" y="%d">context entry</text>' % (x + 100, y, x + 112, y + 4))
    if overlap:
        out.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#555" stroke-width="1.2"/><text x="%d" y="%d">overlap (entry lists the other)</text>' % (x + 215, y, x + 245, y, x + 252, y + 4))
    else:
        out.append('<circle cx="%d" cy="%d" r="9" fill="#777"/><text x="%d" y="%d">seam named in notes/seams.md, with the entries it names</text>' % (x + 222, y, x + 238, y + 4))
    out.append("</g>")
    return "".join(out)


def graph_columns_svg(entries, edges):
    orgs = [o for o in ORDER if any(e["org"] == o for e in entries.values())]
    cols = {o: sorted([e for e in entries.values() if e["org"] == o], key=lambda e: e["name"]) for o in orgs}
    colx = {o: 40 + k * 235 for k, o in enumerate(orgs)}
    pos = {}
    for o in orgs:
        for r, e in enumerate(cols[o]):
            pos[e["id"]] = (colx[o], r)
    nb = {i: [] for i in entries}
    for a, b in edges:
        nb[a].append(b)
        nb[b].append(a)
    for _ in range(8):  # barycentre ordering, deterministic
        for o in orgs:
            def bary(e):
                ys = [pos[n][1] for n in nb[e["id"]] if entries[n]["org"] != o]
                return (sum(ys) / len(ys)) if ys else pos[e["id"]][1]
            order = sorted(cols[o], key=lambda e: (bary(e), e["name"]))
            cols[o] = order
            for r, e in enumerate(order):
                pos[e["id"]] = (colx[o], r)
    rowh, top = 30, 110
    height = top + max(len(c) for c in cols.values()) * rowh + 30
    width = 40 + len(orgs) * 235
    xy = {i: (x + 8, top + r * rowh) for i, (x, r) in pos.items()}
    s = [svg_open(width, height, "Graph of the entries of the map: overlaps between entries, grouped by organisation", "gt1",
                  SVG_DESC + " Entries are in columns by kind of body; a line joins two entries when one of them lists the other as an overlap.")]
    s.append('<text x="40" y="26" font-size="16" font-weight="bold" fill="#111">%s: overlaps between entries</text>' % esc(SITE_TITLE))
    s.append(legend_svg(40, 52))
    for o in orgs:
        s.append('<text x="%d" y="%d" font-size="12" font-weight="bold" fill="%s">%s (%d)</text>' % (colx[o], top - 22, COLOURS[o], esc(o), len(cols[o])))
    s.append('<g fill="none" stroke="#555" stroke-opacity="0.38" stroke-width="1.1">')
    for a, b in edges:
        (xa, ya), (xb, yb) = xy[a], xy[b]
        if xa == xb:
            s.append('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f"/>' % (xa, ya, xa - 46, ya, xa - 46, yb, xb, yb))
        else:
            if xa > xb:
                xa, ya, xb, yb = xb, yb, xa, ya
            dx = (xb - xa) * 0.45
            s.append('<path d="M%.1f,%.1f C%.1f,%.1f %.1f,%.1f %.1f,%.1f"/>' % (xa, ya, xa + dx, ya, xb - dx, yb, xb, yb))
    s.append("</g>")
    for o in orgs:
        for e in cols[o]:
            x, y = xy[e["id"]]
            s.append(node_svg(e, x, y, x + 12))
    s.append("</svg>\n")
    return "".join(s), xy


def graph_seams_svg(entries, seams):
    import math
    keys = [k for k in ("S1", "S2", "S3", "S4") if k in seams]
    pw, ph = 760, 640
    width, height = pw * 2, ph * 2 + 50
    s = [svg_open(width, height, "Graph of the four seams: the entries each seam names", "gt2",
                  SVG_DESC + " The four seams S1 to S4 are drawn with the entries that notes/seams.md names for each.")]
    s.append('<text x="30" y="28" font-size="16" font-weight="bold" fill="#111">%s: the entries named by each seam</text>' % esc(SITE_TITLE))
    for n, k in enumerate(keys):
        title, ids = seams[k]
        cx, cy = (n % 2) * pw + pw / 2, 50 + (n // 2) * ph + ph / 2
        members = sorted((entries[i] for i in ids if i in entries), key=key)
        radius = 215
        pts = []
        for r, e in enumerate(members):
            ang = -math.pi / 2 + 2 * math.pi * r / len(members)
            pts.append((e, cx + radius * math.cos(ang), cy + radius * math.sin(ang), math.cos(ang)))
        s.append('<g stroke="%s" stroke-opacity="0.55" stroke-width="1.4">' % SEAM_COLOURS[k])
        for e, x, y, _ in pts:
            s.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (cx, cy, x, y))
        s.append("</g>")
        href = "seams.html#%s" % slug(title)
        s.append('<a xlink:href="%s" href="%s" target="_top"><title>%s</title><circle cx="%.1f" cy="%.1f" r="26" fill="%s"/>'
                 '<text x="%.1f" y="%.1f" font-size="15" font-weight="bold" fill="#fff" text-anchor="middle">%s</text></a>'
                 % (href, href, attr(title), cx, cy, SEAM_COLOURS[k], cx, cy + 5, k))
        s.append('<text x="%.1f" y="%.1f" font-size="12" text-anchor="middle" fill="#111">%s</text>' % (cx, cy + 46, esc(title)))
        for e, x, y, c in pts:
            if c > 0.2:
                s.append(node_svg(e, x, y, x + 12, "start"))
            elif c < -0.2:
                s.append(node_svg(e, x, y, x - 12, "end"))
            else:
                s.append(node_svg(e, x, y, x + 12, "start"))
    s.append(legend_svg(30, height - 18, overlap=False))
    s.append("</svg>\n")
    return "".join(s)


def entry_neighbours(e, entries, seams):
    """overlap neighbours (either side lists the other) and seam neighbours (share a seam S1..S4 in notes/seams.md)"""
    me = e["id"]
    ov = set(e.get("overlaps") or [])
    ov |= {i for i, x in entries.items() if me in (x.get("overlaps") or [])}
    ov.discard(me)
    mine = {k for k, (_, ids) in seams.items() if k in ("S1", "S2", "S3", "S4") and me in ids}
    sm = {}
    for k in sorted(mine):
        for i in seams[k][1]:
            if i != me and i not in ov and i in entries:
                sm.setdefault(i, []).append(k)
    return sorted(ov, key=lambda i: key(entries[i])), sorted(sm.items(), key=lambda kv: (kv[1][0], key(entries[kv[0]])))


def entry_graph_svg(e, entries, ovn, smn):
    W, rowh, top = 760, 26, 46
    n = max(len(ovn), len(smn), 1)
    H = top + n * rowh + 24
    cx, cy = 380, top + (n * rowh) / 2.0 - 4
    xl, xr = 215, 545
    c = COLOURS.get(e["org"], "#555")
    s = [svg_open(W, H, "Neighbours of %s in the map" % e["name"], "gte",
                  SVG_DESC + " The entry in the middle, with the entries it overlaps and the entries named by the same seams.")]
    s.append('<text x="%d" y="22" font-size="13" font-weight="bold" fill="#111" text-anchor="end">Overlaps (%d)</text>' % (xl + 6, len(ovn)))
    s.append('<text x="%d" y="22" font-size="13" font-weight="bold" fill="#111">Share a seam (%d)</text>' % (xr - 6, len(smn)))
    s.append('<g fill="none">')
    for r, i in enumerate(ovn):
        y = top + r * rowh + 8
        s.append('<path d="M%d,%.1f C%d,%.1f %d,%.1f %d,%.1f" stroke="#333" stroke-width="1.7"/>' % (cx, cy, cx - 90, cy, xl + 90, y, xl, y))
    for r, (i, ks) in enumerate(smn):
        y = top + r * rowh + 8
        s.append('<path d="M%d,%.1f C%d,%.1f %d,%.1f %d,%.1f" stroke="%s" stroke-width="1.5" stroke-dasharray="5 3"/>' % (cx, cy, cx + 90, cy, xr - 90, y, xr, y, SEAM_COLOURS[ks[0]]))
    s.append("</g>")
    for r, i in enumerate(ovn):
        s.append(node_svg(entries[i], xl, top + r * rowh + 8, xl - 12, "end", "../entries/", 13, 24))
    for r, (i, ks) in enumerate(smn):
        s.append(node_svg(entries[i], xr, top + r * rowh + 8, xr + 12, "start", "../entries/", 13, 24, tags=ks))
    s.append('<circle cx="%d" cy="%.1f" r="12" fill="%s" stroke="#222" stroke-width="2"/>' % (cx, cy, c) if e["tier"] == "core" else
             '<circle cx="%d" cy="%.1f" r="12" fill="#fff" stroke="%s" stroke-width="3" stroke-dasharray="3 2"/>' % (cx, cy, c))
    s.append('<text x="%d" y="%.1f" font-size="13" font-weight="bold" fill="#111" text-anchor="middle" stroke="#fff" stroke-width="3" paint-order="stroke">%s</text>' % (cx, cy - 18, esc(short_name(e["name"]))))
    s.append("</svg>\n")
    return "".join(s)


# ---- pages --------------------------------------------------------------------------------------------------------

CSS = """:root{--measure:56rem;--pad:1rem;--fg:#1b1b1b;--bg:#fff;--muted:#555;--line:#d9d9d9;--link:#0b5cad;--accent:#0f4761;--chip:#eef2f6;--strip:#d6e6f5;--sep:#a3a3a3}
@media (prefers-color-scheme:dark){:root{--fg:#e8e8e8;--bg:#161a1d;--muted:#aab;--line:#333b42;--link:#7ab8f5;--accent:#8fc4dd;--chip:#232a30;--strip:#1c3247;--sep:#5f6870}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--fg);background:var(--bg)}
header.site,footer.site{padding-left:max(var(--pad),calc((100% - var(--measure))/2 + var(--pad)));padding-right:max(var(--pad),calc((100% - var(--measure))/2 + var(--pad)))}
header.site{padding-top:.6rem;padding-bottom:.6rem;background:linear-gradient(var(--line),var(--line)) center bottom/min(var(--measure),100%) 1px no-repeat}
header.site{display:flex;flex-wrap:wrap;row-gap:.2rem}
header.site a{margin-right:1rem;color:var(--accent);text-decoration:none;font-weight:600;white-space:nowrap}header.site a.brand{flex-basis:100%;font-size:1.85rem;font-weight:700;margin-bottom:.2rem}header.site .menuw{flex-basis:100%;overflow:hidden}header.site nav.menu{display:flex;flex-wrap:wrap;row-gap:.2rem;margin-left:-.75rem}header.site nav.menu a{margin-right:.75rem;padding-left:.75rem}header.site nav.menu a::before{content:"";display:inline-block;height:.6em;vertical-align:0;border-left:1px solid var(--sep);margin-left:-.75rem;margin-right:calc(.75rem - 1px)}header.site .cadence{flex-basis:100%;margin:0;font-size:.85rem;color:var(--muted)}header.site h1.brand{flex-basis:100%;margin:0;font-size:inherit;line-height:inherit}header.site .tagline{flex-basis:100%;margin:0 0 .3rem;font-size:.95rem;color:var(--muted)}header.site .cadence a{margin-right:0;font-weight:400;text-decoration:underline}footer.site .cadence{margin:0 0 .4rem}
header.site .brandrow{flex-basis:100%;display:flex;flex-wrap:wrap;align-items:center;column-gap:.7rem;row-gap:.25rem;margin-bottom:.2rem}header.site .brandrow a.brand,header.site .brandrow h1.brand{flex-basis:auto;margin-bottom:0}
header.site .pill{display:inline-block;margin-right:0;padding:.05rem .6rem;border:1px solid var(--accent);border-radius:1rem;background:var(--chip);color:var(--accent);font-size:.85rem;font-weight:600;line-height:1.5;white-space:nowrap;text-decoration:none}header.site a.pill:hover,header.site a.pill:focus{text-decoration:underline}
div.strip{max-width:var(--measure);margin:.8rem auto 0;padding:.55rem var(--pad);background:var(--strip);border-radius:.4rem;font-size:.9rem}div.strip p{margin:0}
@media (max-width:56rem){div.strip{border-radius:0;margin-top:0}}
p.crumbs{font-size:.85rem;color:var(--muted);margin:.6rem 0 -.4rem}p.crumbs+h1::before{content:"\\25B8";content:"\\25B8" / "";margin-right:.35em}
a[target="_blank"]::after{content:"\\2197";content:"\\2197" / "";font-size:.8em;margin-left:.15em;text-decoration:none;display:inline-block}
td code,td .nw{white-space:nowrap}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);clip-path:inset(50%);white-space:nowrap}
main{max-width:var(--measure);margin:0 auto;padding:var(--pad)}
h1,h2,h3{color:var(--accent);line-height:1.25}h1{font-size:1.45rem}h2{font-size:1.3rem;margin-top:2rem}h3{font-size:1.1rem}
a{color:var(--link);overflow-wrap:anywhere}code{background:var(--chip);padding:0 .25em;border-radius:3px;font-size:.92em;overflow-wrap:anywhere}
pre{background:var(--chip);padding:.8rem;overflow:auto}hr{border:0;border-top:1px solid var(--line);margin:1.5rem calc(-1 * var(--pad))}
.scroll{overflow-x:auto;margin:1rem 0;position:relative}table{border-collapse:collapse;font-size:.9rem;width:100%}
th,td{border-bottom:1px solid var(--line);padding:.4rem .5rem;text-align:left;vertical-align:top;overflow-wrap:break-word}td:has(a){overflow-wrap:anywhere}
th{background:var(--chip)}blockquote{margin:1rem 0;padding:.2rem 1rem;border-left:4px solid var(--line);color:var(--muted)}
.chips span{display:inline-block;background:var(--chip);border-radius:1rem;padding:.1rem .7rem;margin:0 .4rem .4rem 0;font-size:.85rem}
.verified{color:var(--muted);font-size:.9rem}td.nw,th.nw{white-space:nowrap}td.it{min-width:9rem}table.wts{min-width:42rem}dl.fields dt{font-weight:700;margin-top:1rem}dl.fields dd{margin:.2rem 0 0 0}
ul.sources{padding-left:1.1rem}ul.sources li{margin:.3rem 0}.cls{color:var(--muted);font-size:.85rem}.cls a.arch{color:var(--muted)}
section.author{border-top:1px solid var(--line);margin-top:2rem;padding-top:.5rem}section.author h2{font-size:1.1rem}footer.site{border-top:1px solid var(--line);margin-top:3rem;padding-top:1rem;padding-bottom:1rem;color:var(--muted);font-size:.85rem}
.eg svg{width:100%;height:auto}.eg .legend{font-size:.85rem;color:var(--muted)}.graph{overflow:auto;border:1px solid var(--line);margin:1rem 0}.graph svg{max-width:none;height:auto}
table.matrix .mmeta{font-size:.8rem;color:var(--muted);margin-top:.35rem}table.matrix .mmeta div{margin-top:.15rem}table.matrix .lab{font-weight:700}
table.matrix td.mp{min-width:11rem}
@media (min-width:64rem){.scroll.wide{position:relative;left:50%;transform:translateX(-50%);width:min(72rem,calc(100vw - 4rem))}td:has(a),td a{overflow-wrap:break-word}}
@media (max-width:40rem){:root{--pad:.7rem}body{font-size:15px}
table.matrix,table.matrix tbody,table.matrix tr,table.matrix td{display:block;width:100%}
table.matrix thead{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
table.matrix tr{border:1px solid var(--line);border-radius:.4rem;margin:0 0 1rem 0;padding:.2rem .6rem}
table.matrix td{border-bottom:0;padding:.35rem 0}
table.matrix td:not(.mp)::before{content:attr(data-label);display:block;font-weight:700;color:var(--accent);font-size:.8rem;margin-bottom:.1rem}
table.matrix td.mp{min-width:0;font-size:1rem;border-bottom:1px solid var(--line)}}
"""


class Site:
    def __init__(self, a, entries, src, sha, today, lastmods):
        self.a, self.entries, self.src, self.sha, self.today, self.lastmods = a, entries, src, sha, today, lastmods
        self.pages = {}  # path -> dict(title, desc, lastmod)
        self.out = Path(a.out)
        self.version = ""   # the version named in the first line of the README ("*Version 1.0.1 (2026-10-14) · site updated ...*"), shown in the footer
        self.version_date = ""   # the date in the same line, shown with the number in the header pill
        self.archived = {}  # source URL -> Wayback Machine snapshot URL, from notes/archived-sources.csv

    def base(self, path=""):
        return self.a.base_url + path

    def table_cells(self, page):
        """Inside <td> only: a cell whose text is an ISO date with a short suffix stays on one line; slugs listed in one cell
        go one per line; a bare URL (link text = href) shows a short label, the full URL in title. The href never changes."""
        def cell(m):
            open_, inner = m.group(1), m.group(2)
            text = htmllib.unescape(re.sub(r"<[^>]+>", "", inner)).strip()
            if DATE_CELL.fullmatch(text):   # the date itself never breaks; a time or a second date may go to the next line
                inner = "".join(x if x.startswith("<") else re.sub(r"(?<![\w-])(\d{4}-\d{2}-\d{2})(?![\w-])", r'<span class="nw">\1</span>', x)
                                for x in re.split(r"(<[^>]*>)", inner))   # text only, never inside a tag
            inner = re.sub(r'(?<=</code></a>),\s+(?=<a href="[^"]*entries/[a-z0-9-]+\.html"><code>)', "<br>", inner)  # only links to entries, not code in prose

            def bare(a):
                h = re.search(r'\bhref="(https?://[^"]*)"', a.group(1))
                if not h or htmllib.unescape(a.group(2)) != htmllib.unescape(h.group(1)) or h.group(1).startswith(self.a.base_url):
                    return a.group(0)
                url = htmllib.unescape(h.group(1))
                label = re.sub(r"([/#:])", r"\1<wbr>", esc(short_link_text(url)))   # the line breaks after / # : and not inside a word
                return '<a%s title="%s">%s</a>' % (a.group(1), attr(url), label)
            inner = re.sub(r"<a\b([^>]*)>(.*?)</a>", bare, inner, flags=re.S)
            return open_ + inner + "</td>"
        parts = re.split(r'(<script type="application/ld\+json">.*?</script>)', page, flags=re.S)
        return "".join(p if p.startswith('<script type="application/ld+json">') else re.sub(r"(<td\b[^>]*>)(.*?)</td>", cell, p, flags=re.S) for p in parts)

    def external_in_new_window(self, page):
        """Every link that leaves the site opens in a new tab and says so: an <a> whose href is http(s) and not under the base URL
        gets target="_blank", rel="noopener" and a visually hidden "(opens in a new tab)"; the CSS adds the arrow. JSON-LD blocks
        and links that already carry a target (the nodes of the graph) are left as they are."""
        def fix(m):
            a, inner = m.group(1), m.group(2)
            h = re.search(r'\bhref="(https?://[^"]*)"', a)
            if not h or h.group(1).startswith(self.a.base_url) or "target=" in a:
                return m.group(0)
            if re.search(r'\brel="', a):
                if not re.search(r'\brel="[^"]*\bnoopener\b', a):
                    a = re.sub(r'\brel="([^"]*)"', r'rel="\1 noopener"', a, count=1)
            else:
                a = a[:-1] + ' rel="noopener"' + a[-1]
            return a[:-1] + ' target="_blank"' + a[-1] + inner + '<span class="sr"> (opens in a new tab)</span></a>'
        parts = re.split(r'(<script type="application/ld\+json">.*?</script>)', page, flags=re.S)
        return "".join(p if p.startswith('<script type="application/ld+json">') else re.sub(r"(<a\b[^>]*>)(.*?)</a>", fix, p, flags=re.S) for p in parts)

    def version_pill(self):
        """The current version next to the name in the header, from the version line of the README (never written by hand).
        Links to the version DOI if given, else to the concept DOI, else no link; absent if the README names no version."""
        if not self.version:
            return ""
        text = "v%s" % esc(self.version) + (" &middot; %s" % esc(self.version_date) if self.version_date else "")
        doi, which = (self.a.version_doi, "version DOI") if self.a.version_doi else (self.a.doi, "concept DOI, always resolves to the latest release")
        if doi:
            return '<a class="pill" href="https://doi.org/%s" rel="noopener" title="Version %s; DOI %s (%s)">%s</a>' % (
                attr(doi), esc(self.version), esc(doi), which, text)
        return '<span class="pill" title="Version %s">%s</span>' % (esc(self.version), text)

    def write(self, path, body, title, desc, lastmod, jsonld=None, depth=0, alternates=None):
        rel = "../" * depth
        alt = "".join('<link rel="alternate" type="%s" href="%s">\n' % (attr(t_), attr(h_)) for t_, h_ in (alternates or []))
        nav = '<a class="brand" href="%sindex.html">%s</a>' % (rel, esc(SITE_NAME))
        if path == "index.html":   # one h1 per page: on the home page it is the name in the header, elsewhere the title of the page
            nav = '<h1 class="brand">%s</h1>' % nav
        nav = '<div class="brandrow">%s%s</div>' % (nav, self.version_pill())   # the pill sits outside the h1: it is not part of the name
        nav += '<p class="tagline">%s</p>' % esc(TAGLINE)
        nav += '<div class="menuw"><nav class="menu" aria-label="Site">%s</nav></div>' % "".join(  # the wrapper hides the separator at the start of each row
            '<a href="%s%s">%s</a>' % (rel, h, t) for h, t in (("index.html#entries", "Entries"), ("graph.html", "Graph"), ("seams.html", "Seams"),
                                                               ("calendar.html", "Calendar"), ("intro.html", "Introduction"),
                                                               ("disclosure.html", "Disclosure"), ("method.html", "Method"), ("data.html", "For agents and tools")))
        strip = ""
        if path != "index.html":   # the home page has its own introduction
            strip = '<div class="strip"><p>%s</p></div>\n' % (INTRO_STRIP % ('<a href="%s" rel="noopener">%s</a>' % (attr(GITHUB), esc(AUTHOR)),
                                                                             '<a href="%sintro.html">Introduction</a>' % rel))
        ld = ""
        if jsonld:
            ld = '<script type="application/ld+json">%s</script>\n' % json.dumps(jsonld, ensure_ascii=False, indent=1).replace("</", "<\\/")
        if self.sha:
            commit = 'the data at commit <a href="%s/commit/%s" rel="noopener">%s</a>' % (attr(self.a.repo_url), self.sha, self.sha[:7])
        else:
            commit = 'the data of the <a href="%s" rel="noopener">repository</a>' % attr(self.a.repo_url)
        page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
                '<title>%s</title>\n<meta name="description" content="%s">\n<link rel="canonical" href="%s">\n<link rel="stylesheet" href="%sstyle.css">\n%s%s</head>\n'
                '<body>\n<header class="site">%s<p class="cadence">Updated weekly, new versions on Mondays &middot; Corrections: <a href="%s" rel="noopener">open an issue</a>'
                ' &middot; Source and data: <a href="%s" rel="noopener">GitHub</a></p></header>\n%s<main>\n%s\n</main>\n'
                '<footer class="site"><p class="cadence">Updated weekly: numbered versions are released on Mondays. To correct or propose an entry, <a href="%s" rel="noopener">open an issue</a>.</p>%s%s. Generated on %s from %s; content under CC BY 4.0. Generated from the data of the map, never edited by hand. No tracking, no scripts.</footer>\n</body>\n</html>\n'
                % (esc(title), attr(desc), attr(self.base(path)), rel, alt, ld, nav, attr(NEW_ISSUE_URL), attr(self.a.repo_url), strip, body, attr(NEW_ISSUE_URL), esc(SITE_TITLE), (", version %s" % esc(self.version)) if self.version else "", self.today, commit))
        page = self.external_in_new_window(self.table_cells(page))
        target = self.out / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page, encoding="utf-8", newline="\n")
        self.pages[path] = {"title": title, "desc": desc, "lastmod": lastmod}


def cite_text(a):
    """Citation line; empty unless a DOI was given."""
    if not a.doi:
        return ""
    vdoi = a.version_doi or a.doi
    return "%s (2026). Agentic Standards Map (Version %s) [Data set]. Zenodo. https://doi.org/%s" % (
        "Marinoni Moretto, F.", a.cite_version or datetime.date.today().isoformat(), vdoi)


def cite_request(a):
    """The request that follows the citation: with a DOI it also names the concept DOI, for citing the map in general."""
    return CITE_REQUEST + (" " + CITE_GENERAL % a.doi if a.doi and a.version_doi else "")


def link_dois(text):
    """escape the text and turn each https://doi.org/... into a link"""
    return re.sub(r"(https://doi\.org/[0-9A-Za-z./-]+?)(?=[.]?(?:\s|$|<))", lambda m: '<a href="%s" rel="noopener">%s</a>' % (m.group(1), m.group(1)), esc(text))


def author_block_html(a, disclosure_href="disclosure.html"):
    """The 'About the author' block of the home page and of intro.html. Every URL comes from the constants at the top of this file."""
    h = ['<section class="author"><h2>About the author</h2>',
         "<p>%s, %s.</p>" % (esc(AUTHOR), esc(AUTHOR_LINE)),
         '<p>ORCID <a href="%s" rel="noopener">%s</a> &middot; GitHub <a href="%s" rel="noopener">%s</a> &middot; LinkedIn <a href="%s" rel="noopener">%s</a></p>'
         % (attr(ORCID), ORCID_ID, attr(GITHUB), GITHUB_USER, attr(LINKEDIN), LINKEDIN_USER),
         "<p>%s</p>" % (AUTHOR_PART % ('<a href="%s">Disclosure</a>' % attr(disclosure_href))),
         '<p>Corrections and missing sources: <a href="%s" rel="noopener">open an issue on the repository</a>.</p>' % attr(ISSUES_URL)]
    ct = cite_text(a)
    if ct:
        h.append('<h3>How to cite</h3><p>%s<br>%s</p>' % (link_dois(ct), link_dois(cite_request(a))))
    h.append("</section>")
    return "".join(h)


def readme_author_md(a):
    """The same block as markdown, for public/README.md (the build checks that the README carries it)."""
    t = ["## About the author", "",
         "%s, %s." % (AUTHOR, AUTHOR_LINE), "",
         "ORCID [%s](%s) · GitHub [%s](%s) · LinkedIn [%s](%s)" % (ORCID_ID, ORCID, GITHUB_USER, GITHUB, LINKEDIN_USER, LINKEDIN), "",
         AUTHOR_PART % "[Disclosure](notes/disclosure.md)", "",
         "Corrections and missing sources: [open an issue on the repository](%s)." % ISSUES_URL]
    ct = cite_text(a)
    if ct:
        t += ["", "### How to cite", "", ct, "", cite_request(a)]
    return "\n".join(t) + "\n"


def check_readme_block(readme_text):
    """The README is a hand-kept source; every constant must be in it, so that it cannot drift from the site."""
    need = [AUTHOR, AUTHOR_LINE, ORCID, GITHUB, LINKEDIN, ISSUES_URL, "## About the author"]
    miss = [n for n in need if n not in readme_text]
    return miss


def load_archived(src):
    """URL -> snapshot of the Wayback Machine, from notes/archived-sources.csv (columns url, archived, snapshot). Absent file: nothing archived."""
    p = src / "notes" / "archived-sources.csv"
    if not p.exists():
        return {}
    out = {}
    for r in csv.DictReader(p.read_text(encoding="utf-8").splitlines()):
        if not re.fullmatch(r"https://web\.archive\.org/web/\d{14}/.+", r["archived"]):
            raise SystemExit("notes/archived-sources.csv: not a snapshot URL: %s" % r["archived"][:80])
        out[r["url"]] = r["archived"]
    return out


def add_archived(o, archived):
    """Put `archived` right after `url` (or `source` in committed_next) of every item that has a snapshot; items without one are left as they are."""
    if not archived:
        return o

    def put(item, name):
        if isinstance(item, dict) and item.get(name) in archived:
            new = {}
            for k, v in item.items():
                new[k] = v
                if k == name:
                    new["archived"] = archived[item[name]]
            return new
        return item
    o = dict(o)
    for field, name in (("sources", "url"), ("open_proposals", "url"), ("committed_next", "source")):
        if o.get(field):
            o[field] = [put(x, name) for x in o[field]]
    return o


def entry_object(e, archived=None):
    """The entry as in the YAML, without the working field _file; with `archived` next to the URLs that have a snapshot."""
    return add_archived({k: v for k, v in e.items() if k != "_file"}, archived)


def entry_json(site, e):
    """Per-entry JSON: the object of map.json plus url, source_url (the YAML at the source commit) and licence."""
    o = entry_object(e, site.archived)
    ref = site.sha or "main"
    o["url"] = site.base("entries/%s.html" % e["id"])
    o["source_url"] = "%s/blob/%s/entries/%s" % (site.a.repo_url, ref, e["_file"])
    o["licence"] = LICENCE_URL
    return o


def entry_ld(site, e, desc):
    """WebPage of the entry: part of the dataset, with the date of verification, the licence, what it is about and the primary sources as citations."""
    prim = [x["url"] for x in e.get("sources") or [] if x.get("class") != "third-party"]
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": e["name"], "description": desc, "dateModified": d(e["verified"]),
            "url": site.base("entries/%s.html" % e["id"]), "isPartOf": {"@id": site.base("") + "#dataset"}, "license": LICENCE_URL,
            "about": {"@type": "Thing", "name": e["name"]}}
    if prim:
        ld["citation"] = [{"@type": "CreativeWork", "url": u} for u in prim]
    return ld


def data_page_html(a, site, n_entries, newest, map_size, n_events, sha):
    cite = cite_text(a)
    if cite:
        cite_p = "<p>%s<br>%s</p>" % (link_dois(cite), link_dois(cite_request(a)))
    else:
        cite_p = "<p>Cite the entry id and the date it was read.</p>"
    # the version that has a tag (and a DOI); the version shown on the site may be a later one, which has neither until its release is recorded here
    rel_v, rel_tag = LATEST_RELEASE
    shown = (a.cite_version or rel_v)
    pending = "" if shown == rel_v else " The version shown on this site, %s, has no tag and no DOI of its own yet; they are recorded here when it is released." % esc(shown)
    if a.doi and a.version_doi:
        citable_p = '<p>The website is the living version and changes as venues move. Each DOI identifies a frozen snapshot: version %s is the tag <code>%s</code>, version DOI <a href="https://doi.org/%s" rel="noopener">%s</a>.%s The concept DOI <a href="https://doi.org/%s" rel="noopener">%s</a> always resolves to the latest version; cite the version DOI for the text you read.</p>' % (rel_v, rel_tag, attr(a.version_doi), esc(a.version_doi), pending, attr(a.doi), esc(a.doi))
    elif a.doi:
        citable_p = '<p>The website is the living version and changes as venues move. Each DOI identifies a frozen snapshot: version %s is the tag <code>%s</code>; its version DOI is recorded here once Zenodo assigns it. The concept DOI <a href="https://doi.org/%s" rel="noopener">%s</a> always resolves to the latest version.%s</p>' % (rel_v, rel_tag, attr(a.doi), esc(a.doi), pending)
    else:
        citable_p = "<p>The website is the living version and changes as venues move. Version %s is the tag <code>%s</code> of the repository; a DOI for each frozen snapshot is not issued yet, and until it is, cite the entry id, the date it was read and the commit shown in the footer of the page.%s</p>" % (rel_v, rel_tag, pending)
    rows = [
        ("<a href=\"map.json\">map.json</a>", "All entries as in the YAML (schema v2, described in entries/_schema.md) and the graph of overlaps and seams. Top-level fields: schema, schema_description, generated, source_commit, licence, entries, graph. Where a snapshot of a source exists in the Wayback Machine of the Internet Archive, the item of sources, open_proposals or committed_next carries an archived field next to its url (%d URLs). %d entries; generated %s; source commit %s; licence CC BY 4.0; size %d bytes." % (len(site.archived), n_entries, esc(site.today), esc(sha[:7] if sha else "not given"), map_size)),
        ("<code>entries/&lt;id&gt;.json</code>", "One file per entry: the same object as in map.json, plus <code>url</code> (the page of the entry), <code>source_url</code> (the YAML file in the repository at the source commit) and <code>licence</code>. Example: <a href=\"entries/ap2.json\">entries/ap2.json</a>."),
        ("<a href=\"calendar.ics\">calendar.ics</a>", "The same dated events as the Calendar page (%d), in iCalendar format." % n_events),
        ("<a href=\"map-bundle.md\">map-bundle.md</a>", "The full text of the map in one Markdown file."),
        ("<a href=\"sitemap.xml\">sitemap.xml</a>", "The list of the pages of the site."),
        ("JSON-LD", "Every page carries JSON-LD: a Dataset on the home page, a WebPage on the others; an entry page names the primary sources of the entry as citations."),
    ]
    tbl = "".join("<tr><td>%s</td><td>%s</td></tr>" % (a_, b_) for a_, b_ in rows)
    return ("<h1>For agents and tools</h1>"
            "<p>The map in machine-readable form. These are plain files and standard web formats.</p>"
            "<p>This site uses generic web mechanisms (JSON files, link rel=alternate, schema.org JSON-LD, a sitemap). It does not adopt any of the discovery mechanisms described in the map, so that the map does not take a side in what it maps.</p>"
            "<h2 id=\"files\">Files</h2><div class=\"scroll\"><table><thead><tr><th>File</th><th>What it holds</th></tr></thead><tbody>%s</tbody></table></div>"
            "<h2 id=\"licence\">Licence</h2><p>The content is under <a href=\"%s\" rel=\"noopener\">CC BY 4.0</a>; the scripts in <code>tools/</code> are under the MIT licence. Reuse is free with attribution. Quotations from third-party texts remain under their own terms; CC BY 4.0 applies to the author's text and data.</p>"
            "<h2 id=\"cite\">How to cite</h2>%s%s"
            "<h2 id=\"counts\">Counts</h2><p>The numbers of sources quoted on the site (source references, distinct URLs, primary and third-party-only URLs) are produced by <a href=\"%s\" rel=\"noopener\">tools/count_sources.py</a>, run on the files of the repository. A source reference is one use of a URL in the field <code>sources</code> or in a <code>committed_next</code> item; a distinct URL is counted once whatever the number of uses; a URL with a fragment is a different URL. The script counts URLs and does not check that they respond.</p>"
            "<h2 id=\"updates\">Updates</h2><p>Each entry carries its own read date (the fields <code>verified</code> and <code>status_as_of</code>). The site is regenerated from the data at each commit of the repository; the newest verification date is %s. Update cadence: numbered versions are released on Mondays; changes verified by Friday enter the following Monday. Corrections and proposals: open an issue at <a href=\"%s\" rel=\"noopener\">%s</a>.</p>"
            "<h2 id=\"corrections\">Corrections</h2><p>Corrections and missing sources: <a href=\"%s\" rel=\"noopener\">open an issue on the repository</a>.</p>"
            % (tbl, attr(LICENCE_URL), cite_p, citable_p, attr(a.repo_url.rstrip("/") + "/blob/main/tools/count_sources.py"), esc(newest), attr(ISSUES_URL), esc(ISSUES_URL), attr(ISSUES_URL)))


def dataset_ld(site, newest):
    ld = {"@context": "https://schema.org", "@type": "Dataset", "@id": site.base("") + "#dataset", "name": SITE_TITLE,
            "description": "A map of who is standardising agentic commerce, where, and what each venue has committed to next: one dated, sourced entry per specification, draft or group.",
            "url": site.base(""), "creator": CREATOR, "license": LICENCE_URL,
            "dateModified": newest,
            "distribution": [{"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": site.base("map.json")},
                             {"@type": "DataDownload", "encodingFormat": "text/calendar", "contentUrl": site.base("calendar.ics")}]}
    if site.a.doi:
        ld["identifier"] = "https://doi.org/" + site.a.doi
    return ld


def entry_body(e, entries, md, seams, graph_html, archived=None):
    rel = "../"
    ov = ", ".join('<a href="%s.html">%s</a>' % (attr(o), esc(entries[o]["name"])) for o in (e.get("overlaps") or []))
    p = ['<p class="crumbs"><a href="%sindex.html">%s</a> &rsaquo; <a href="%sindex.html#entries">Entries</a> &rsaquo; %s</p>' % (rel, esc(SITE_NAME), rel, esc(e["name"])),
         '<h1>%s</h1>' % esc(e["name"]),
         '<p class="chips"><span>%s</span><span>%s</span><span>%s entry</span></p>' % (esc(e["org"]), esc(e["kind"]), esc(e["tier"])),
         '<p class="verified">Verified %s. Status as of %s. <a href="%sindex.html#entries">All entries</a>.</p>' % (d(e["verified"]), d(e["status_as_of"]), rel)]
    if e.get("seams"):
        p.append('<p class="chips">Seams: %s</p>' % "".join('<span><a href="%sseams.html#%s">%s</a></span>' % (rel, attr(slug(seams[k][0])), esc(k)) for k in e["seams"] if k in seams))
    p.append("<h2>Status</h2><p>%s</p>" % md.inline(one_line(e["status"])))
    p.append("<h2>Relevance</h2>" + split_paragraphs(md, e["relevance"]))
    cn = e.get("committed_next") or []
    p.append("<h2>Committed next</h2>")
    if cn:
        p.append("<ul>%s</ul>" % "".join('<li>%s <strong>(%s)</strong> <span class="cls">[%s]</span> %s</li>' % (
            md.inline(one_line(c["what"])), esc(d(c["when"])), esc(CLASSES[c["class"]]), md.inline(c["source"])) for c in cn))
    else:
        p.append("<p>None declared in the sources read.</p>")
    if e.get("boundary"):
        p.append("<h2>Boundary</h2><p>%s</p>" % md.inline(one_line(e["boundary"])))
    if e.get("participation"):
        p.append("<h2>Author participation</h2><p>%s</p>" % md.inline(one_line(e["participation"])))
    p.append("<h2>Sources</h2><ul class=\"sources\">%s</ul>" % "".join(
        '<li><a href="%s" rel="noopener">%s</a> <span class="cls">%s, read %s%s</span></li>' % (attr(s["url"]), esc(s["url"]), esc(CLASSES[s["class"]]), esc(d(s["read"])),
                                                                                                  (' \u00b7 <a class="arch" href="%s" rel="noopener">archived</a>' % attr(archived[s["url"]])) if archived and s["url"] in archived else "")
        for s in e.get("sources", [])))
    if ov:
        p.append("<h2>Overlaps</h2><p>%s</p>" % ov)
    p.append('<h2 id="neighbours">Neighbours in the map</h2>' + graph_html)
    ev = e.get("evidence")
    if ev:
        p.append("<h2>Evidence and coverage</h2><dl class=\"fields\">")
        for k, lab in (("read", "Read"), ("not_read", "Not read"), ("not_found", "Not found"), ("method", "Method")):
            if ev.get(k):
                p.append("<dt>%s</dt><dd>%s</dd>" % (lab, md.inline(one_line(ev[k]))))
        p.append("</dl>")
    ops = e.get("open_proposals") or []
    if ops:
        p.append("<h2>Open proposals</h2><div class=\"scroll\"><table><thead><tr><th>Proposal</th><th>Author</th><th>Date</th><th>State</th><th>Link</th></tr></thead><tbody>")
        for o in ops:
            p.append("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><a href=\"%s\" rel=\"noopener\">%s</a></td></tr>" % (
                md.inline(one_line(o["what"])), esc(o["author"]), esc(d(o["date"])), esc(o["state"]), attr(o["url"]), esc(o["url"])))
        p.append("</tbody></table></div>")
    m = e.get("matrix")
    if m:
        p.append("<h2>Payment comparison row</h2><dl class=\"fields\">%s</dl>" % "".join(
            "<dt>%s</dt><dd>%s</dd>" % (lab, md.inline(one_line(m.get(k)))) for k, lab in MATRIX_COLS if m.get(k)))
    return "\n".join(p)


def split_paragraphs(md, text):
    """layout only: a long block is cut into paragraphs at sentence ends once a chunk passes 300 characters"""
    t = one_line(text)
    parts, cur = [], ""
    sents = re.split(r"(?<=[a-z0-9\)])\.\s+(?=[A-Z])", t)  # the split removes the full stop between two sentences
    for k, sent in enumerate(sents):
        piece = sent if k == len(sents) - 1 else sent + "."  # the last sentence keeps the ending it has
        cur = (cur + " " + piece) if cur else piece
        if len(cur) > 300:
            parts.append(cur)
            cur = ""
    if cur:
        parts.append(cur)
    return "".join("<p>%s</p>" % md.inline(x) for x in parts)


def status_rows(entries):
    ref = max(d(e["verified"]) for e in entries.values())
    core = sorted((e for e in entries.values() if e["tier"] == "core"), key=key)
    rows = []
    for e in core:
        s = one_line(e["status"])
        m = re.search(r"(?<=[a-z0-9\)])\.\s+(?=[A-Z])", s)
        first = s[:m.start() + 1] if m else s
        nd = next_date(e, ref)
        rows.append((e, first, nd))
    return rows


def calendar_events(src):
    """The events of calendar.ics are the rows of the calendar note, the same list as calendar.html (one source, two renderings)."""
    text = (src / "notes" / "calendar-2026.md").read_text(encoding="utf-8")
    note = [l.strip() for l in text.split("\n") if l.strip().startswith("This calendar lists dated public events")]
    if len(note) != 1:
        raise SystemExit("notes/calendar-2026.md: the line 'This calendar lists dated public events ...' is missing or repeated")
    asof = [l.strip() for l in text.split("\n") if l.strip().startswith("Events as declared by the venues on ")]
    if len(asof) != 1:
        raise SystemExit("notes/calendar-2026.md: the line 'Events as declared by the venues on <date>; ...' is missing or repeated")
    ev, stats = [], {"rows": 0, "approx": 0, "ranges": 0}
    for line in text.split("\n"):
        if not (line.startswith("| 20") or line.startswith("| approx.")):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        dates = re.findall(r"\d{4}-\d{2}-\d{2}", cells[0])
        if len(cells) < 4 or not dates:
            raise SystemExit("calendar note: a row without a date or without four cells: %s" % line[:80])
        approx = cells[0].startswith("approx.")
        stats["rows"] += 1
        stats["approx"] += 1 if approx else 0
        stats["ranges"] += 1 if len(dates) > 1 else 0
        ev.append({"start": dates[0], "end": dates[-1], "approx": approx, "what": cells[1].replace("`", ""),
                   "entries": re.findall(r"`([a-z0-9-]+)`", cells[2]), "sources": re.findall(r"https?://[^\s;]+", cells[3])})
    return ev, stats, note[0].split(" Dates declared")[0] + " " + asof[0]


def fold(line):
    b = line.encode("utf-8")
    if len(b) <= 75:
        return line
    out, cur = [], ""
    for ch in line:
        if len((cur + ch).encode("utf-8")) > (75 if not out else 74):
            out.append(cur)
            cur = ch
        else:
            cur += ch
    out.append(cur)
    return "\r\n ".join(out)


def ics_text(s):
    return s.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def build_ics(events, site, caldesc):
    stamp = site.today.replace("-", "") + "T000000Z"
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Agentic standards map//calendar//EN", "CALSCALE:GREGORIAN", "METHOD:PUBLISH",
             "X-WR-CALNAME:Agentic standards map: calendar", "X-WR-CALDESC:" + ics_text(caldesc)]
    for n, e in enumerate(events):
        end = (datetime.date.fromisoformat(e["end"]) + datetime.timedelta(days=1)).strftime("%Y%m%d")
        first = e["entries"][0] if e["entries"] else ""
        summ = ("approx. " if e["approx"] else "") + short_desc(re.split(r" \(|; ", e["what"])[0].strip(), 110)
        lines += ["BEGIN:VEVENT", "UID:%s-%s-%d.agentic-standards-map.invalid" % (first or "map", e["start"], n), "DTSTAMP:" + stamp,
                  "DTSTART;VALUE=DATE:" + e["start"].replace("-", ""), "DTEND;VALUE=DATE:" + end, "SUMMARY:" + ics_text(summ),
                  "DESCRIPTION:" + ics_text("%s Source: %s" % (e["what"], "; ".join(e["sources"]))), "END:VEVENT"]
        if first:
            lines.insert(len(lines) - 1, "URL:" + site.base("entries/%s.html" % first))
    lines.append("END:VCALENDAR")
    return "\r\n".join(fold(l) for l in lines) + "\r\n"


def git(args, cwd):
    return subprocess.run(["git"] + args, cwd=str(cwd), capture_output=True, text=True, encoding="utf-8").stdout.strip()


def main():
    short_link_selftest()   # before any page is written
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--commit", default="HEAD")
    ap.add_argument("--source", help="read this folder (a public export or the public repository) instead of exporting a commit")
    ap.add_argument("--out", default=str(ROOT / "site"))
    ap.add_argument("--base-url", default=PLACEHOLDER_BASE, help="address of the site; a placeholder until GitHub Pages is on")
    ap.add_argument("--repo-url", default=DEFAULT_REPO)
    ap.add_argument("--doi", default="", help="DOI of the dataset; empty until it exists. With a DOI the author block carries a How to cite section")
    ap.add_argument("--version-doi", default="", help="DOI of the cited version (the citation line uses it); --doi is then the concept DOI")
    ap.add_argument("--cite-version", default="", help="version named in the citation (default: the build date)")
    a = ap.parse_args()
    if not a.base_url.endswith("/"):
        a.base_url += "/"
    a.repo_url = a.repo_url.rstrip("/")
    out = Path(a.out)
    today = datetime.date.today().isoformat()
    tmp = Path(tempfile.mkdtemp(prefix="map-site-"))
    try:
        if a.source:
            src = Path(a.source)
            sha = git(["rev-parse", "HEAD"], src) or None  # a commit of the folder given with --source, which is the public repository
            git_dir = src
        else:
            check = ROOT / "export_check.json"
            saved = check.read_bytes() if check.exists() else None
            try:
                subprocess.run([sys.executable, str(HERE / "export_public.py"), a.commit, "--out", str(tmp / "export")], check=True, capture_output=True, text=True, encoding="utf-8")
            finally:
                if saved is not None:
                    check.write_bytes(saved)  # the export rewrites its report; the repository file stays as it was
            src = tmp / "export"
            sha = None  # a commit of the working repository does not exist in the public one: no link
            git_dir = ROOT
        entries = load_entries(src)
        ids = set(entries)
        lastmods = {}
        for rel, _, _, _ in NOTE_PAGES:
            lm = git(["log", "-1", "--format=%cs", a.commit if not a.source else "HEAD", "--", rel], git_dir)
            lastmods[rel] = lm or today
        if out.exists():
            shutil.rmtree(out)
        out.mkdir(parents=True)
        (out / "style.css").write_text(CSS, encoding="utf-8", newline="\n")
        site = Site(a, entries, src, sha, today, lastmods)
        _readme = (src / "README.md").read_text(encoding="utf-8")
        _v = re.search(r"\*Version ([0-9][0-9.]*) \((\d{4}-\d{2}-\d{2})\)", _readme) or re.search(r"\*Version ([0-9][0-9.]*)[ ,(]", _readme)
        site.version = _v.group(1) if _v else ""
        site.version_date = _v.group(2) if _v and _v.lastindex == 2 else ""   # shown in the header pill with the number
        site.archived = load_archived(src)
        newest = max(d(e["verified"]) for e in entries.values())
        unmapped = []

        seams_text = (src / "notes" / "seams.md").read_text(encoding="utf-8")
        seams = seam_members(seams_text)
        seam_diffs = check_seams(list(entries.values()), seams_text)
        n_graph = n_nograph = 0

        # entries
        for e in sorted(entries.values(), key=key):
            md = Md(ids, a.repo_url, "../")
            ovn, smn = entry_neighbours(e, entries, seams)
            if ovn or smn:
                n_graph += 1
                graph_html = ('<div class="eg">%s</div><p class="legend">Solid lines: overlaps declared by one of the two entries. Dashed lines, coloured by seam: entries named by the same seam (S1 to S4) in the seams note. Every node is a link.</p>'
                              % entry_graph_svg(e, entries, ovn, smn))
            else:
                n_nograph += 1
                graph_html = "<p>No overlap is declared and no seam names this entry, so it has no neighbours to draw.</p>"
            desc = short_desc(e["status"])
            ld = entry_ld(site, e, desc)
            site.write("entries/%s.html" % e["id"], entry_body(e, entries, md, seams, graph_html, site.archived), "%s | %s" % (e["name"], SITE_TITLE), desc, d(e["verified"]), ld, depth=1,
                       alternates=[("application/json", "%s.json" % e["id"])])
            (out / "entries").mkdir(parents=True, exist_ok=True)
            (out / "entries" / ("%s.json" % e["id"])).write_text(json.dumps(entry_json(site, e), ensure_ascii=False, indent=1, default=d), encoding="utf-8", newline="\n")
            unmapped += md.unmapped

        # notes
        for rel, page, title, desc in NOTE_PAGES:
            text = (src / rel).read_text(encoding="utf-8")
            md = Md(ids, a.repo_url)
            if page == "intro.html":
                m = re.search(r"\n\nI am an independent researcher, and I have taken part.*\Z", text, re.S)
                if not m:
                    raise SystemExit("notes/intro.md: the closing paragraphs to replace by the author block were not found")
                body = md.render(text[:m.start()] + "\n", skip_h1=False) + author_block_html(a)
            elif page == "disclosure.html":
                short = (src / "notes" / "disclosure-short.md").read_text(encoding="utf-8")
                body = md.render(short.rstrip("\n") + "\n\n## Full disclosure\n\n" + text, skip_h1=False)
            else:
                body = md.render(text, skip_h1=False)
            if not re.search(r"<h1[ >]", body):
                body = "<h1>%s</h1>\n%s" % (esc(title), body)
            ld = {"@context": "https://schema.org", "@type": "WebPage", "name": title, "description": desc, "dateModified": lastmods[rel],
                  "url": site.base(page), "isPartOf": {"@id": site.base("") + "#dataset"}}
            site.write(page, body, "%s | %s" % (title, SITE_TITLE), desc, lastmods[rel], ld)
            unmapped += md.unmapped
        # graph
        edges, unknown_overlap, unknown_seam = graph_data(entries, seams)
        svg1, _ = graph_columns_svg(entries, edges)
        svg2 = graph_seams_svg(entries, seams)
        (out / "graph.svg").write_text(svg1, encoding="utf-8", newline="\n")
        (out / "graph-seams.svg").write_text(svg2, encoding="utf-8", newline="\n")
        gbody = ('<h1>Graph of the entries</h1><p>Every node is an entry and links to its page. Colour is the organisation; a solid node is a core entry and a dashed ring a context entry. '
                 'The first view draws the overlaps that entries declare (%d, each counted once); the second shows the four seams and the entries each names. '
                 'The same figures are in <a href="map.json">map.json</a>; the SVG files can be used as they are on a slide or a poster: <a href="graph.svg">graph.svg</a>, <a href="graph-seams.svg">graph-seams.svg</a>.</p>'
                 '<h2 id="overlaps">Overlaps between entries</h2><div class="graph">%s</div><h2 id="seams">Seams</h2><div class="graph">%s</div>'
                 % (len(edges), svg1.split("\n", 1)[1] and svg1, svg2))
        site.write("graph.html", gbody, "Graph | %s" % SITE_TITLE, "Graph of the %d entries of the map: overlaps between entries and the entries named by each seam; every node links to its page." % len(entries), newest,
                   {"@context": "https://schema.org", "@type": "WebPage", "name": "Graph", "dateModified": newest, "url": site.base("graph.html"),
                    "description": "Graph of the entries of the map.", "isPartOf": {"@id": site.base("") + "#dataset"}})

        # index
        md = Md(ids, a.repo_url)
        readme = (src / "README.md").read_text(encoding="utf-8")
        head = readme.split("## Next on the calendar")[0]
        # the name and the tagline are in the header of the page; the README opens with both, and the home page starts after them
        opening = "# %s\n\n**%s**\n\n" % (SITE_NAME, TAGLINE)
        if not head.replace("\r\n", "\n").startswith(opening):
            raise SystemExit("README.md does not open with the name and the tagline of the header: %r" % head[:160])
        head = head.replace("\r\n", "\n")[len(opening):]
        nextsec = "## Next on the calendar" + readme.split("## Next on the calendar", 1)[1].split("## Start here")[0]
        tail = "## Start here" + readme.split("## Start here", 1)[1]
        miss = check_readme_block(readme)
        if miss:
            raise SystemExit("README.md does not carry the author block constants: %s" % miss)
        tail_a, rest = tail.split("## About the author", 1)
        tail_b = "## " + rest.split("\n## ", 1)[1]  # what follows the author section
        author_html = author_block_html(a)
        rows = status_rows(entries)
        wt = ['<h2 id="where-things-stand">Where things stand</h2><div class="scroll"><table class="wts"><thead><tr><th class="nw">Org</th><th>Item</th><th>State (as of)</th><th class="nw">Next dated item</th></tr></thead><tbody>']
        for e, first, nd in rows:
            wt.append('<tr><td class="nw">%s</td><td class="it"><a href="entries/%s.html">%s</a></td><td>%s (%s)</td><td class="nw">%s</td></tr>' % (esc(e["org"]), attr(e["id"]), esc(e["name"]), md.inline(first), esc(d(e["status_as_of"])), esc(nd)))
        wt.append("</tbody></table></div>")
        by = {e["id"]: e for e in entries.values()}
        # Four columns (2026-10-14). Same fields, same words, other places: governance, version and source under the protocol,
        # what is signed and who signs in one cell. Under 40rem each protocol becomes a block (CSS only, data-label).
        def mline(lab, k, m):
            v = one_line(m.get(k)) or "not found"
            if lab == "Source" and re.match(r"https?://", v):
                v = "[%s](%s)" % (source_label(v), v)   # short label, the full URL stays the href
            return '<div><span class="lab">%s:</span> %s</div>' % (lab, md.inline(v))
        mx = ['<h2 id="matrix">Payment protocols compared</h2><div class="scroll wide"><table class="matrix"><thead><tr><th>Protocol</th><th>Signatures</th><th>Receipt or record</th><th>Dispute</th></tr></thead><tbody>']
        for i in MATRIX_ORDER:
            e = by[i]
            m = e.get("matrix") or {}
            mx.append('<tr><td class="mp" data-label="Protocol"><a href="entries/%s.html">%s</a><div class="mmeta">%s%s%s</div></td>'
                      '<td data-label="Signatures">%s%s</td><td data-label="Receipt or record">%s</td><td data-label="Dispute">%s</td></tr>' % (
                          attr(i), esc(e["name"]), mline("Governance", "governance", m), mline("Version", "version_state", m), mline("Source", "source", m),
                          mline("What", "signs", m), mline("Who", "signer", m),
                          md.inline(one_line(m.get("record")) or "not found"), md.inline(one_line(m.get("dispute")) or "not found")))
        mx.append("</tbody></table></div>")
        allp = ['<h2 id="entries">All entries</h2>']
        for o in ORDER:
            es = sorted((e for e in entries.values() if e["org"] == o), key=lambda x: x["name"])
            if es:
                allp.append("<h3>%s</h3><ul>%s</ul>" % (esc(o), "".join('<li><a href="entries/%s.html">%s</a> <span class="cls">%s</span></li>' % (attr(e["id"]), esc(e["name"]), e["tier"]) for e in es)))
        links = '<p><a href="graph-seams.svg"><strong>Graph of the seams</strong></a> | <a href="graph.svg">All overlaps</a> | <a href="graph.html">Both graphs on one page</a> | <a href="seams.html">Seams</a> | <a href="calendar.html">Calendar</a> | <a href="map.json">map.json</a> | <a href="calendar.ics">calendar.ics</a> | <a href="map-bundle.md">map-bundle.md</a> | <a href="data.html">For agents and tools</a></p>'
        if sha:
            stamp = '<p class="verified">Entries verified up to %s; pages generated on %s from commit <a href="%s/commit/%s" rel="noopener">%s</a>.</p>' % (newest, today, attr(a.repo_url), sha, sha[:7])
        else:
            stamp = '<p class="verified">Entries verified up to %s; pages generated on %s from the <a href="%s" rel="noopener">repository</a>.</p>' % (newest, today, attr(a.repo_url))
        ibody = md.render(head) + stamp + links + md.render(nextsec) + "".join(wt) + "".join(mx) + md.render(tail_a) + author_html + md.render(tail_b) + "".join(allp)
        unmapped += md.unmapped
        idesc = short_desc("Who is standardising agentic commerce, where, and what each venue has committed to next: %d dated, sourced entries across W3C, IETF, GS1, UN/CEFACT, AAIF, Linux Foundation and industry protocols." % len(entries))
        site.write("index.html", ibody, SITE_TITLE, idesc, newest, dataset_ld(site, newest), alternates=[("application/json", "map.json"), ("text/calendar", "calendar.ics")])

        # data files
        events, stats, caldesc = calendar_events(src)
        (out / "calendar.ics").write_text(build_ics(events, site, caldesc), encoding="utf-8", newline="")
        mapjson = {"schema": "v2", "schema_description": "entries/_schema.md", "generated": today, "source_commit": sha or "", "licence": LICENCE_URL,
                   "entries": [entry_object(entries[i], site.archived) for i in sorted(entries)],
                   "graph": {"nodes": sorted(entries), "overlap_edges": [list(x) for x in edges], "seams": {k: {"title": t, "entries": ids_} for k, (t, ids_) in seams.items()}}}
        (out / "map.json").write_text(json.dumps(mapjson, ensure_ascii=False, indent=1, default=d), encoding="utf-8", newline="\n")

        # page for agents and tools, the bundle
        bundle_src = src / "map-bundle.md"
        if bundle_src.exists():
            shutil.copyfile(bundle_src, out / "map-bundle.md")
        else:
            raise SystemExit("map-bundle.md is not in the source folder: the page for agents needs it")
        mj_size = (out / "map.json").stat().st_size
        dbody = data_page_html(a, site, len(entries), newest, mj_size, len(events), sha)
        site.write("data.html", dbody, "For agents and tools | %s" % SITE_TITLE, "Files and formats of the map: map.json, one JSON per entry, calendar.ics, map-bundle.md, JSON-LD; licence and how to cite.", newest,
                   {"@context": "https://schema.org", "@type": "WebPage", "name": "For agents and tools", "dateModified": newest, "url": site.base("data.html"),
                    "description": "Files and formats of the map.", "isPartOf": {"@id": site.base("") + "#dataset"}})

        # sitemap and robots
        urls = sorted(site.pages)
        sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for p_ in urls:
            sm.append("<url><loc>%s</loc><lastmod>%s</lastmod></url>" % (esc(site.base(p_)), site.pages[p_]["lastmod"]))
        sm.append("</urlset>")
        (out / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8", newline="\n")
        (out / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n" % a.base_url, encoding="utf-8", newline="\n")
        report(a, out, site, entries, seams, edges, unknown_overlap, unknown_seam, events, stats, unmapped, tmp, seam_diffs, n_graph, n_nograph)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def internal_links(out):
    """returns (checked, broken list) for every href and xlink:href of the html and svg files"""
    ids_by_file, broken, checked = {}, [], 0
    files = sorted(list(out.rglob("*.html")) + list(out.rglob("*.svg")))
    for f in files:
        ids_by_file[f.resolve()] = set(re.findall(r'\bid="([^"]+)"', f.read_text(encoding="utf-8")))
    for f in files:
        txt = f.read_text(encoding="utf-8")
        for h in re.findall(r'\b(?:xlink:)?href="([^"]*)"', txt):
            h = htmllib.unescape(h)
            if re.match(r"^(https?:|mailto:)", h):
                continue
            checked += 1
            path, _, frag = h.partition("#")
            tgt = (f.parent / path).resolve() if path else f.resolve()
            if not tgt.exists():
                broken.append((f.relative_to(out).as_posix(), h))
            elif frag and tgt.suffix == ".html" and frag not in ids_by_file.get(tgt, set()):
                broken.append((f.relative_to(out).as_posix(), h))
    return checked, broken


def report(a, out, site, entries, seams, edges, unknown_overlap, unknown_seam, events, stats, unmapped, tmp, seam_diffs, n_graph, n_nograph):
    try:
        import export_public as ex
    except ImportError:
        ex = None
    pages = sorted(site.pages)
    n_entry = sum(1 for p in pages if p.startswith("entries/"))
    n_note = len(NOTE_PAGES)
    print("[CHECK] pages generated: %d (entries %d + notes %d + index 1 + graph 1 + data 1)" % (len(pages), n_entry, n_note))
    checked, broken = internal_links(out)
    print("[CHECK] internal links checked: %d; broken: %d %s" % (checked, len(broken), broken[:10]))
    if unmapped:
        print("[CHECK] markdown links with no target on the site, shown as text: %d %s" % (len(unmapped), sorted(set(unmapped))))
    deg = {i: 0 for i in entries}
    for x, y in edges:
        deg[x] += 1
        deg[y] += 1
    seamed = {i for _, (_, ids) in seams.items() for i in ids}
    print("[CHECK] overlap edges: %d (each pair once); seam sections read from seams.md: %s" % (len(edges), {k: len(v[1]) for k, v in seams.items()}))
    print("[CHECK] entries without an overlap edge: %s; with neither an overlap edge nor a seam: %s" % (sorted(i for i, n in deg.items() if n == 0), sorted(i for i, n in deg.items() if n == 0 and i not in seamed)))
    print("[CHECK] seams: differences between the entries and notes/seams.md: %d %s" % (len(seam_diffs), seam_diffs[:5]))
    print("[CHECK] entry pages with a graph of neighbours: %d; without (no neighbours): %d" % (n_graph, n_nograph))
    print("[CHECK] edges to ids that do not exist: overlaps %d %s, seams %d %s" % (len(unknown_overlap), unknown_overlap, len(unknown_seam), unknown_seam))
    cal_rows = len(re.findall(r"<tr><td", (out / "calendar.html").read_text(encoding="utf-8")))
    print("[CHECK] calendar.ics: %d events, the rows of the calendar note (%d with an approximate date, %d ranges); rows in calendar.html: %d; same list: %s" % (len(events), stats["approx"], stats["ranges"], cal_rows, cal_rows == len(events)))
    titles = [site.pages[p]["title"] for p in pages]
    dup = sorted({t for t in titles if titles.count(t) > 1})
    nodesc = [p for p in pages if not site.pages[p]["desc"].strip()]
    print("[CHECK] duplicate titles: %d %s; pages without description: %d %s" % (len(dup), dup, len(nodesc), nodesc))
    smurls = re.findall(r"<loc>([^<]+)</loc>", (out / "sitemap.xml").read_text(encoding="utf-8"))
    print("[CHECK] sitemap URLs: %d; pages: %d; same set: %s" % (len(smurls), len(pages), sorted(smurls) == sorted(site.base(p) for p in pages)))
    bad_ld = 0
    n_ld = 0
    for f in out.rglob("*.html"):
        for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', f.read_text(encoding="utf-8"), flags=re.S):
            n_ld += 1
            try:
                json.loads(blob.replace("<\\/", "</"))
            except ValueError:
                bad_ld += 1
    json.loads((out / "map.json").read_text(encoding="utf-8"))
    print("[CHECK] JSON-LD blocks: %d, invalid as JSON: %d; map.json parses: True" % (n_ld, bad_ld))
    canon = sum(1 for f in out.rglob("*.html") if 'rel="canonical"' in f.read_text(encoding="utf-8") and 'lang="en"' in f.read_text(encoding="utf-8"))
    print("[CHECK] pages with canonical link and lang=en: %d of %d" % (canon, len(pages)))
    h1_bad, tag_bad = [], []
    for f in sorted(out.rglob("*.html")):
        t = f.read_text(encoding="utf-8")
        if len(re.findall(r"<h1[ >]", t)) != 1:
            h1_bad.append(f.relative_to(out).as_posix())
        hdr = t.split("</header>", 1)[0]
        if t.count(esc(TAGLINE)) != 1 or esc(TAGLINE) not in hdr or re.search(r"<h[1-6][^>]*>[^<]*" + re.escape(esc(TAGLINE)), t):
            tag_bad.append(f.relative_to(out).as_posix())
    home = (out / "index.html").read_text(encoding="utf-8")
    home_h1_in_header = bool(re.search(r"<h1[ >]", home.split("</header>", 1)[0]))
    print("[CHECK] pages with exactly one h1: %d of %d %s; home h1 in the header: %s; tagline once per page, in the header, not a heading: %d of %d %s"
          % (len(pages) - len(h1_bad), len(pages), h1_bad[:5], home_h1_in_header, len(pages) - len(tag_bad), len(pages), tag_bad[:5]))
    # texts that must not reach the site: read at run time from the working repository when it holds the internal summary, never written in this file
    excluded = []
    pv = ROOT / "notes" / "exec-summary.md"
    if pv.exists() and not a.source:
        lines = [l.strip() for l in pv.read_text(encoding="utf-8").split("\n") if l.strip()]
        excluded = [l for l in lines[1:2]] + [l.split(".")[0] for l in lines if l.startswith("This page is only for")]
    hits_excluded = []
    for f in list(out.rglob("*")):
        if f.is_file() and f.suffix in (".html", ".json", ".ics", ".xml", ".svg", ".txt", ".css", ".md"):
            t = f.read_text(encoding="utf-8")
            hits_excluded += [(f.name, "excluded text") for p_ in excluded if p_ and p_ in t]
            if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t):
                hits_excluded.append((f.name, "email-like string"))
    italian_selftest()
    leaks = []
    for f in sorted(out.rglob("*")):
        if f.is_file() and f.suffix in (".html", ".svg", ".ics"):
            for n, line in enumerate(f.read_text(encoding="utf-8").split(chr(10)), 1):
                for h in find_italian(htmllib.unescape(re.sub(r"<[^>]*>", " ", line))):
                    leaks.append((f.relative_to(out).as_posix(), n, h[1], h[2]))
    print("[CHECK] Italian words (%d in the list) or a double full stop in the text of the pages: %d %s" % (len(ITALIAN_WORDS), len(leaks), leaks[:5]))
    if leaks:
        raise SystemExit("Italian text or a double full stop is left in the site:" + chr(10) + "  " + (chr(10) + "  ").join("%s line %d: %r in: %s" % h for h in leaks))
    print("[CHECK] texts of the internal summary (%d lines compared) or email-like strings in the site: %d %s" % (len(excluded), len(hits_excluded), hits_excluded[:5]))
    if ex is None:
        print("[CHECK] terms scan skipped: export_public.py is not in this repository (it is run on the export, before the public repository exists)")
    else:
        scan_dir = tmp / "scan"
        shutil.copytree(out, scan_dir, ignore=shutil.ignore_patterns("robots.txt", "style.css"))
        note_html = Md(set(entries), a.repo_url).render(ex.AI_NOTE)  # the note on AI assistance is allowed in METHOD.md, as in the export
        mp = scan_dir / "method.html"
        mt = mp.read_text(encoding="utf-8")
        if note_html in mt:
            mp.write_text(mt.replace(note_html, "\x00" * len(note_html)), encoding="utf-8")
        (scan_dir / "ai-use.html").rename(scan_dir / "AI-USE.md")  # the export allows the AI terms in the declaration of AI use, under that name
        hits, _, _ = ex.scan(scan_dir)
        bad, allowed = ex.apply_allow(hits)
        print("[CHECK] terms not allowed (same list and allowances as export_check; robots.txt and style.css left out of the scan): %s; allowed by the same rules: %s" % (
            {k: len(v) for k, v in bad.items()} or "none", sum(len(v) for v in allowed.values())))
    print("[SCOPE] these checks read the generated files: they do not render a page, do not follow external links, and the terms scan covers the generated text, not the look of a page.")
    print("site written to %s (base URL %s%s)" % (out, a.base_url, "; placeholder, change --base-url when Pages is on" if a.base_url == PLACEHOLDER_BASE else ""))


if __name__ == "__main__":
    main()
