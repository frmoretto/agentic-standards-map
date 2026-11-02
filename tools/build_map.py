"""Build MAP.md from entries/*.yaml (schema v2, see entries/_schema.md).
Usage: python tools/build_map.py
       python tools/build_map.py --check entries/a.yaml entries/b.yaml   (validate single files)

The renderers (status_table, matrix, core_cards, context_cards, evidence, open_proposals) are also
used by tools/build_bundle.py, so MAP.md and the bundle are made of the same generated parts.
"""
from pathlib import Path
import datetime
import re
import sys
import urllib.parse
import yaml

ROOT = Path(__file__).resolve().parent.parent
ORDER = ["W3C", "IETF", "GS1", "UN/CEFACT", "Other standards bodies", "AAIF", "Linux Foundation", "Independent", "Industry"]
TIERS = ("core", "context")
CLASSES = {
    "normative": "normative text",
    "decision": "official decision or commitment",
    "statement": "maintainer or chair statement",
    "third-party": "participant or third party",
}
TAGS = {"normative": "normative", "decision": "decision", "statement": "statement", "third-party": "third party"}
MATRIX_ORDER = ["ap2", "ucp", "acp", "x402", "visa-tap", "verifiable-intent", "emvco-agentic-payments-framework"]
MATRIX_COLS = [("governance", "Owner / governance"), ("version_state", "Version and state"),
               ("signs", "What it signs"), ("signer", "Who signs"), ("record", "Receipt or record"),
               ("dispute", "Dispute"), ("source", "Source")]
REQUIRED_CORE = ("id", "name", "org", "kind", "tier", "status", "status_as_of", "relevance", "boundary",
                 "committed_next", "sources", "verified")
REQUIRED_CONTEXT = ("id", "name", "org", "kind", "tier", "status", "status_as_of", "relevance", "sources", "verified")


SEAM_KEYS = ("S1", "S2", "S3", "S4")


# Italian words that must not be left in the English text of the map (work orders are in Italian, the map is not).
# Whole words, case-insensitive, never inside a URL or an identifier (a hyphen, slash, dot or @ next to the word).
ITALIAN_WORDS = ["in attesa", "della", "delle", "degli", "dello", "perch\u00e9", "perche", "anche", "sono", "questo", "questa",
                 "scheda", "schede", "giuntura", "giunture", "ordine", "non trovato", "non trovata", "verificato", "verificata",
                 "nella", "nelle", "alla", "alle", "quindi", "fonte", "fonti"]
# (word, context substring, reason): a use that is not Italian text (a proper name, a quotation in Italian). Empty today.
ITALIAN_ALLOW = []
_IT = re.compile(r"(?<![\w/@.#:-])(%s)(?![\w/@-])" % "|".join(re.escape(w) for w in sorted(ITALIAN_WORDS, key=len, reverse=True)), re.I)
_DOUBLE_STOP = re.compile(r"[A-Za-z0-9)\"'](\.\.)(?!\.)")


def find_italian(text):
    """[(line, word, context)] for every Italian word of the list, and for a double full stop (..), outside URLs"""
    hits = []
    for n, line in enumerate(text.split("\n"), 1):
        for m in _IT.finditer(line):
            a = line.rfind(" ", 0, m.start()) + 1
            b = line.find(" ", m.end())
            if "://" in line[a:(b if b >= 0 else len(line))]:
                continue
            ctx = line[max(0, m.start() - 40):m.end() + 40].strip()
            if any(w == m.group(1).lower() and sub in ctx for w, sub, _ in ITALIAN_ALLOW):
                continue
            hits.append((n, m.group(1), ctx))
        for m in _DOUBLE_STOP.finditer(line):
            hits.append((n, "..", line[max(0, m.start() - 40):m.end() + 40].strip()))
    return hits


def italian_selftest():
    """the check must find planted Italian and stay silent on URLs, identifiers and English"""
    assert len(find_italian("the text is in attesa and not read..\nla scheda e la giuntura\nnon trovato")) == 5, "italian check missed planted text"
    quiet = "see https://example.org/della/scheda and della-robbia, a_sono, x/anche, user@sono, an item.. here is not matched? no: ellipsis ... fine"
    assert [h for h in find_italian(quiet) if h[1] != ".."] == [], find_italian(quiet)
    assert find_italian("the order of the cards, a note about the fountain, 'come back'") == [], "italian check fired on English"


def find_plain_hash(text):
    """[(line, key, value read, rest)] for every plain (unquoted, non-block) scalar that a ' #' cuts: YAML reads the rest of
    the line as a comment, so the loaded value is truncated and nothing raises. Works on the source tokens, not on the loaded
    value, where the cut is invisible. Also catches a comment line right after a plain scalar, which ends it the same way."""
    lines = text.split("\n")
    hits, key, expect_key = [], None, False
    for tok in yaml.scan(text):
        if isinstance(tok, yaml.KeyToken):
            expect_key = True
            continue
        if not isinstance(tok, yaml.ScalarToken):
            continue
        if expect_key:
            key, expect_key = tok.value, False
            continue
        if not tok.plain:
            continue
        ln, col = tok.end_mark.line, tok.end_mark.column
        rest = lines[ln][col:] if ln < len(lines) else ""
        nxt = lines[ln + 1] if ln + 1 < len(lines) else ""
        if re.match(r"[ \t]+#", rest):
            hits.append((ln + 1, key, tok.value, rest.strip()))
        elif re.match(r"[ \t]+#", nxt):
            hits.append((ln + 2, key, tok.value, nxt.strip()))
    return hits


def hash_selftest():
    """the check must find a value cut by ' #' and stay silent on quoted values, blocks and a '#' with no space before it"""
    assert [h[1:3] for h in find_plain_hash("a: Breakout #22, The Agentic Web\n")] == [("a", "Breakout")], "plain ' #' missed"
    assert [h[1:3] for h in find_plain_hash("l:\n  - what: issue #13 x\n    when: undated\n")] == [("what", "issue")], "list item missed"
    assert len(find_plain_hash("a: issue\n  # 13 and the rest\nb: c\n")) == 1, "comment line after a plain scalar missed"
    quiet = "a: 'Breakout #22'\nb: \"issue #13\"\nc: >-\n  Breakout #22, text\nd: x#y\ne: https://example.org/p#frag\nf: 3\n"
    assert find_plain_hash(quiet) == [], find_plain_hash(quiet)


class UniqueKeyLoader(yaml.SafeLoader):
    """safe_load that refuses a key repeated in the same mapping: plain YAML keeps the last value and drops the first without a word"""

    def construct_mapping(self, node, deep=False):
        seen = {}
        for k, _ in node.value:
            key = self.construct_object(k, deep=deep)
            if key in seen:
                raise yaml.constructor.ConstructorError(
                    "while constructing a mapping", node.start_mark,
                    f"key {key!r} repeated (line {seen[key] + 1} and line {k.start_mark.line + 1})", k.start_mark)
            seen[key] = k.start_mark.line
        return super().construct_mapping(node, deep=deep)


def load_unique(text):
    return yaml.load(text, Loader=UniqueKeyLoader)


def dupkey_selftest():
    """the loader must refuse a repeated key at the top and inside a list item, and accept the same key in two items or two levels"""
    for bad in ("a: 1\nb: 2\na: 3\n", "s:\n  - url: x\n    class: a\n    read: 1\n    class: b\n"):
        try:
            load_unique(bad)
        except yaml.constructor.ConstructorError:
            continue
        raise AssertionError(f"repeated key not refused: {bad!r}")
    assert load_unique("s:\n  - url: x\n    class: a\n  - url: y\n    class: b\nclass: c\n")["class"] == "c"


def seam_members(text):
    """sections of notes/seams.md whose first line is a list of backticked ids -> {key: (title, [ids])};
    the key is S1..S4 for the numbered seams and a slug of the title for the other sections"""
    res, cur, title, got = {}, None, None, False
    for l in text.split("\n"):
        if l.startswith("## "):
            title = l[3:].strip()
            m = re.match(r"^(S\d+)\.", title)
            cur = m.group(1) if m else re.sub(r"\s+", "-", re.sub(r"[^\w\s-]", "", title.lower()).strip())
            got = False
        elif cur and l.strip() and not got:
            got = True
            if re.fullmatch(r"(`[^`]+`(, )?)+", l.strip()):
                res[cur] = (title, re.findall(r"`([^`]+)`", l))
    return res


def seams_by_entry(text):
    out = {}
    for k, (_, ids) in seam_members(text).items():
        if k in SEAM_KEYS:
            for i in ids:
                out.setdefault(i, set()).add(k)
    return out


def check_seams(entries, seams_text, all_entries=True):
    """both sides of the seams must agree: an id listed in a seam has that seam in its entry and the other way round"""
    want = seams_by_entry(seams_text)
    diffs = []
    ids = {e["id"] for e in entries}
    for e in entries:
        have = set(e.get("seams") or [])
        if have != want.get(e["id"], set()):
            diffs.append(f"{e['_file']}: seams {sorted(have)} in the entry, {sorted(want.get(e['id'], set()))} in notes/seams.md")
    if all_entries:
        for i in sorted(set(want) - ids):
            diffs.append(f"notes/seams.md names {i}, which is not an entry")
    return diffs


WHEN_RE = re.compile(r"approx\. \d{4}-\d\d-\d\d")
PROPOSAL_STATES = ("open", "closed", "merged", "draft")


def as_date(v):
    """a YAML date, a datetime or an ISO string -> datetime.date; None if it is none of these"""
    if isinstance(v, datetime.datetime):
        return v.date()
    if isinstance(v, datetime.date):
        return v
    try:
        return datetime.date.fromisoformat(str(v))
    except ValueError:
        return None


def check_entry(p):
    text = Path(p).read_text(encoding="utf-8")
    name = Path(p).name
    try:
        e = load_unique(text)
    except yaml.constructor.ConstructorError as x:
        raise SystemExit(f"{name}: {x.problem}; YAML would keep the last value and drop the first")
    cut = find_plain_hash(text)
    if cut:
        raise SystemExit("\n".join(f"{name}: line {n}, key {k!r}: unquoted value followed by {r[:40]!r}; YAML reads it as a comment "
                                   f"and the value becomes {v!r}. Quote the value or write it as a block (>-)." for n, k, v, r in cut))
    first = re.search(r"^sources:[ ]*\n([ ]*)- url:", text, flags=re.M)
    if first:
        listed = len(re.findall(r"^" + first.group(1) + r"- url:", text, flags=re.M))
        if listed != len(e.get("sources") or []):
            raise SystemExit(f"{name}: {listed} source items ('- url:' at the indentation of the sources list) in the file but {len(e.get('sources') or [])} sources parsed: a source item sits inside another field")
    e["_file"] = name
    if e.get("tier") not in TIERS:
        raise SystemExit(f"{name}: tier is missing or not one of {TIERS}: {e.get('tier')!r}")
    if e.get("org") not in ORDER:
        raise SystemExit(f"{name}: org {e.get('org')!r} is not one of {ORDER}")
    for f in (REQUIRED_CORE if e["tier"] == "core" else REQUIRED_CONTEXT):
        if f not in e or e[f] in (None, "") or (e[f] == [] and f != "committed_next"):
            raise SystemExit(f"{name}: required field {f!r} is missing")
    if e.get("seams") is not None:
        if not isinstance(e["seams"], list) or any(k not in SEAM_KEYS for k in e["seams"]):
            raise SystemExit(f"{name}: seams must be a list of {SEAM_KEYS}: {e['seams']!r}")
    for s in e.get("sources", []):
        if s.get("class") not in CLASSES:
            raise SystemExit(f"{name}: source {s.get('url')!r} has class {s.get('class')!r}, expected one of {list(CLASSES)}")
    for c in e.get("committed_next") or []:
        if c.get("class") not in CLASSES:
            raise SystemExit(f"{name}: committed_next item has class {c.get('class')!r}, expected one of {list(CLASSES)}")
        for k in ("what", "when", "source"):
            if not c.get(k):
                raise SystemExit(f"{name}: committed_next item lacks {k}")
        w = c["when"]
        if not (isinstance(w, datetime.date) or (isinstance(w, str) and (w == "undated" or WHEN_RE.fullmatch(w)))):
            raise SystemExit(f"{name}: committed_next 'when' must be YYYY-MM-DD, 'approx. YYYY-MM-DD' or undated, not {w!r}")
    for p_ in e.get("open_proposals") or []:
        for k in ("what", "author", "date", "state", "url"):
            if not p_.get(k):
                raise SystemExit(f"{name}: open_proposals item lacks {k}")
        if p_["state"] not in PROPOSAL_STATES:
            raise SystemExit(f"{name}: open_proposals state must be one of {PROPOSAL_STATES}, not {p_['state']!r}")
    if e.get("evidence"):
        for k in ("read", "not_read"):
            if not e["evidence"].get(k):
                raise SystemExit(f"{name}: evidence lacks {k}")
    ver, asof = as_date(e.get("verified")), as_date(e.get("status_as_of"))
    if ver and asof and asof > ver:
        raise SystemExit(f"{name}: status_as_of {asof} is later than verified {ver}")
    reads = [s_.get("read") for s_ in e.get("sources") or []] + [s_.get("read") for s_ in (e.get("evidence") or {}).get("quoted_pages") or []]
    latest = max((as_date(r) for r in reads if as_date(r)), default=None)
    if ver and latest and latest > ver:
        raise SystemExit(f"{name}: a source was read on {latest}, later than verified {ver}")
    return e


def load():
    dupkey_selftest()
    entries = [check_entry(p) for p in sorted((ROOT / "entries").glob("*.yaml"))]
    ids = {e["id"] for e in entries}
    for e in entries:
        for o in e.get("overlaps", []) or []:
            if o not in ids:
                raise SystemExit(f"{e['_file']}: unknown overlap id {o}")
    for i in MATRIX_ORDER:
        if i not in ids:
            raise SystemExit(f"matrix row {i} has no entry")
    sp = ROOT / "notes" / "seams.md"
    if sp.exists():
        diffs = check_seams(entries, sp.read_text(encoding="utf-8"))
        if diffs:
            raise SystemExit("seams differ between the entries and notes/seams.md:\n  " + "\n  ".join(diffs))
    return entries


def d(v):
    return v.isoformat() if isinstance(v, (datetime.date, datetime.datetime)) else str(v)


def one_line(v):
    return " ".join(str(v or "").split())


def key(e):
    return (ORDER.index(e["org"]) if e["org"] in ORDER else 99, e["name"])


def cell(v):
    return one_line(v).replace("|", "\\|") or "not found"


def next_date(e, ref):
    """the earliest dated item of committed_next that is not before `ref` (a full date or an 'approx.' date), else '-'"""
    best = None
    for c in e.get("committed_next") or []:
        w = d(c.get("when"))
        m = re.search(r"\d{4}-\d{2}-\d{2}", w or "")
        if not m or m.group(0) < ref:
            continue
        if best is None or m.group(0) < best[0]:
            best = (m.group(0), w)
    return best[1] if best else "-"


def status_table(entries):
    ref = max(d(e["verified"]) for e in entries)
    core = sorted((e for e in entries if e["tier"] == "core"), key=key)
    out = ["| Org | Item | State (as of) | Next dated item |", "|---|---|---|---|"]
    for e in core:
        out.append(f"| {e['org']} | [{e['name']}](#{e['id']}) | {cell(e['status'])} ({d(e['status_as_of'])}) | {next_date(e, ref)} |")
    return "\n".join(out)


def matrix_parts(e):
    """The four columns of the comparison table as lists of (label, text) lines.

    It is a view of the `matrix:` block of the entry, not a change of the data: the seven fields keep their text
    word for word, only where they stand changes. Governance, version and source go under the
    protocol; what is signed and who signs go in one cell. An empty field is still "not found"."""
    m = e.get("matrix") or {}

    def g(k):
        return cell(m.get(k))
    return {"protocol": [("Governance", g("governance")), ("Version", g("version_state")), ("Source", g("source"))],
            "signatures": [("What", g("signs")), ("Who", g("signer"))],
            "record": [(None, g("record"))],
            "dispute": [(None, g("dispute"))]}


MATRIX_HEADERS = ("Protocol", "Signatures", "Receipt or record", "Dispute")


def source_label(url):
    """The visible text of the Source link in the comparison table: the repository (or the domain) and the name of
    the file, with the short sha when the link is pinned to a commit. The href stays the full URL; the label is not
    a quotation and is not compared with anything. A file name longer than 40 characters is cut at 37 and ends in
    an ellipsis. A value that is not a URL is returned as it is."""
    if not re.match(r"https?://", url or ""):
        return url
    u = urllib.parse.urlparse(url)
    host = u.netloc.lower()
    host = host[4:] if host.startswith("www.") else host
    parts = [urllib.parse.unquote(x) for x in u.path.split("/") if x]
    name = parts[-1] if parts else ""
    if len(name) > 40:
        name = name[:37] + "…"
    if host == "github.com" and len(parts) >= 2:
        label = parts[1]
        pinned = len(parts) >= 5 and parts[2] in ("blob", "tree", "commit", "raw")
        if pinned and name:
            label += " " + name
        sha = parts[3] if pinned else ""
        if re.fullmatch(r"[0-9a-f]{7,40}", sha):
            label += " @" + sha[:7]
        return label
    return host + (" " + name if name else "")


def matrix(entries):
    by = {e["id"]: e for e in entries}
    out = ["| " + " | ".join(MATRIX_HEADERS) + " |", "|" + "---|" * len(MATRIX_HEADERS)]
    for i in MATRIX_ORDER:
        e = by[i]
        p = matrix_parts(e)
        # the Source line of the protocol cell shows the short label and carries the full URL as the href
        p["protocol"] = [(lab, f"[{source_label(txt)}]({txt})" if lab == "Source" and re.match(r"https?://", txt) else txt)
                         for lab, txt in p["protocol"]]
        proto = f"[{e['name']}](#{e['id']})<br><small>" + "<br>".join(f"{lab}: {txt}" for lab, txt in p["protocol"]) + "</small>"
        sig = "<br>".join(f"{lab}: {txt}" for lab, txt in p["signatures"])
        out.append(f"| {proto} | {sig} | {p['record'][0][1]} | {p['dispute'][0][1]} |")
    return "\n".join(out)


def sources_lines(e):
    return [f"- [{TAGS[s['class']]}] {s['url']} ({d(s['read'])})" for s in e.get("sources", [])]


def core_cards(entries):
    out = []
    for e in sorted((x for x in entries if x["tier"] == "core"), key=key):
        out += [f"### {e['name']}", f'<a id="{e["id"]}"></a>', "",
                f"**{e['org']}, {e['kind']}.** {one_line(e['status'])} (as of {d(e['status_as_of'])}).", "",
                f"**Relevance to commerce.** {one_line(e['relevance'])}", "", "**Committed next.**"]
        if e.get("committed_next"):
            for c in e["committed_next"]:
                out.append(f"- {one_line(c['what'])} ({d(c['when'])}) [{TAGS[c['class']]}] {c['source']}")
        else:
            out.append("- None declared in the sources read.")
        out += ["", f"**Boundary.** {one_line(e['boundary'])}", ""]
        if e.get("participation"):
            out += [f"**Author participation.** {one_line(e['participation'])}", ""]
        out.append("**Sources.**")
        out += sources_lines(e)
        out.append("")
        if e.get("overlaps"):
            out += ["**Overlaps:** " + ", ".join(f"[{o}](#{o})" for o in e["overlaps"]), ""]
        if e.get("evidence"):
            out += [f"**Coverage:** see [Evidence](#evidence-{e['id']}).", ""]
    return "\n".join(out).rstrip()


def context_cards(entries):
    out = []
    for e in sorted((x for x in entries if x["tier"] == "context"), key=key):
        out += [f"### {e['name']}", f'<a id="{e["id"]}"></a>', "",
                f"**{e['org']}, {e['kind']}.** {one_line(e['status'])} (as of {d(e['status_as_of'])}). {one_line(e['relevance'])}", ""]
        if e.get("participation"):
            out += [f"**Author participation.** {one_line(e['participation'])}", ""]
        cov = f" Coverage: see [Evidence](#evidence-{e['id']})." if e.get("evidence") else ""
        out += ["**Sources.** " + "; ".join(f"[{TAGS[s['class']]}] {s['url']} ({d(s['read'])})" for s in e.get("sources", [])) + cov, ""]
    return "\n".join(out).rstrip()


def evidence(entries):
    out = []
    for e in sorted((x for x in entries if x.get("evidence")), key=key):
        ev = e["evidence"]
        nf = one_line(ev.get("not_found"))
        nf = (" " if nf.startswith("Not found") else " Not found: ") + nf if nf else ""
        out += [f'<a id="evidence-{e["id"]}"></a>**{e["name"]}.** Read: {one_line(ev.get("read"))} '
                f'Not read: {one_line(ev.get("not_read"))}{nf}', ""]
    return "\n".join(out).rstrip()


def open_proposals(entries):
    rows = [(e, p) for e in sorted(entries, key=key) for p in (e.get("open_proposals") or [])]
    out = ["| Entry | Proposal | Author | Date | State | Link |", "|---|---|---|---|---|---|"]
    for e, p in rows:
        out.append(f"| [{e['name']}](#{e['id']}) | {cell(p['what'])} | {cell(p['author'])} | {d(p['date'])} | {cell(p['state'])} | {p['url']} |")
    return "\n".join(out)


def render(entries):
    out = ["# Agentic standards map", "",
           "Generated from `entries/`. Do not edit by hand. Seams: `notes/seams.md`.", "",
           "## Core entries: status", "", status_table(entries), "",
           "## Payment protocols compared", "", matrix(entries), "",
           "## Core entries", "", core_cards(entries), "",
           "## Context entries", "", context_cards(entries), "",
           "## Appendix: Evidence and coverage", "", evidence(entries), "",
           "## Appendix: Open proposals", "", open_proposals(entries), ""]
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--check":
        hash_selftest()
        dupkey_selftest()
        sp = ROOT / "notes" / "seams.md"
        for f in sys.argv[2:]:
            e = check_entry(f)
            if sp.exists():
                diffs = check_seams([e], sp.read_text(encoding="utf-8"), all_entries=False)
                if diffs:
                    raise SystemExit("\n".join(diffs))
            print("ok", f)
        print("[SCOPE] --check looks at: tier, org, required fields, seams against notes/seams.md, source and committed_next classes, "
              "committed_next 'when' format, open_proposals state enum, verified not earlier than status_as_of or than any source read, and that every '  - url:' line of the file is a parsed source (an item pasted inside another field is refused), "
              "and that no unquoted value is cut by ' #' (read on the source text, with a self-test run first), and that no key is repeated in the same mapping (a loader that refuses it, with a self-test run first). "
              "It does NOT check: that a URL answers, that a quote is in its source (check_sources.py does), or that the dates are true.")
        sys.exit(0)
    md = render(load())
    (ROOT / "MAP.md").write_text(md, encoding="utf-8", newline="\n")
    print(f"MAP.md written, {md.count(chr(10))} lines")
