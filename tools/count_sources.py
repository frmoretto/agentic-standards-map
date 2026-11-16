#!/usr/bin/env python3
"""Counts of the sources of the map, from the files of a folder (the repository or a public export).

Usage: python tools/count_sources.py [FOLDER]      (default: the folder above tools/)

What is counted
  entries            files entries/*.yaml (not the schema file), and their tier (core, context)
  source references  every item of `sources` plus every `source` of `committed_next`, one per use
  distinct URLs      the same references, each URL once (the fragment after # is part of the URL)
  primary            a distinct URL that is cited at least once in class normative, decision or statement
  third-party only   a distinct URL cited only in class third-party
  bundle URLs        the distinct http(s) URLs found in the text of map-bundle.md, after stripping trailing punctuation
  seams              the headings "## Sn. " of notes/seams.md (raises if none, or if an id repeats)

[SCOPE] This counts URLs; it does not check that they respond, and it does not count or check quotations.
A URL cited with and without a fragment counts twice. The bundle count is a text match
and includes the URLs of the repository and the licence."""
import collections
import re
import sys
from pathlib import Path

import yaml

PRIMARY = {"normative", "decision", "statement"}
URL = re.compile(r"https?://[^\s<>\)\]\|`'\"]+")


SEAM = re.compile(r"^## (S\d+)\. ", re.M)


def counts(root):
    """the counts as a dict, read from the files of the folder (also used by build_site.py and release_metadata.py)"""
    entries = []
    for p in sorted((root / "entries").glob("*.yaml")):
        if p.name.startswith("_"):
            continue
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        if isinstance(d, dict) and "id" in d:
            entries.append(d)
    if not entries:
        raise SystemExit("no entry found in %s/entries" % root)
    classes = collections.defaultdict(set)
    refs = 0
    for e in entries:
        items = [(s["url"], s.get("class")) for s in e.get("sources") or []]
        items += [(c["source"], c.get("class")) for c in e.get("committed_next") or [] if c.get("source")]
        for url, cls in items:
            refs += 1
            classes[url].add(cls)
    primary = sum(1 for c in classes.values() if c & PRIMARY)
    bundle = root / "map-bundle.md"
    bundle_urls = None
    if bundle.exists():
        bundle_urls = {u.rstrip(".,;:") for u in URL.findall(bundle.read_text(encoding="utf-8"))}
    seams_md = root / "notes" / "seams.md"
    seams = SEAM.findall(seams_md.read_text(encoding="utf-8")) if seams_md.exists() else None
    if seams is not None and (not seams or len(seams) != len(set(seams))):
        raise SystemExit("notes/seams.md: no seam heading found, or a seam id repeated: %s" % seams)
    return {"entries": len(entries), "core": sum(1 for e in entries if e.get("tier") == "core"),
            "context": sum(1 for e in entries if e.get("tier") == "context"), "references": refs,
            "distinct": len(classes), "primary": primary, "third_party_only": len(classes) - primary,
            "bundle_urls": len(bundle_urls) if bundle_urls is not None else None,
            "seams": len(seams) if seams is not None else None, "seam_ids": seams}


def main(root):
    c = counts(root)
    print("entries                  %d (core %d, context %d)" % (c["entries"], c["core"], c["context"]))
    print("source references        %d" % c["references"])
    print("distinct source URLs     %d" % c["distinct"])
    print("  primary                %d" % c["primary"])
    print("  third-party only       %d" % c["third_party_only"])
    print("distinct URLs in bundle  %s" % (c["bundle_urls"] if c["bundle_urls"] is not None else "map-bundle.md not found"))
    print("seams                    %s" % ("%d (%s, headings '## Sn.' of notes/seams.md)" % (c["seams"], ", ".join(c["seam_ids"])) if c["seams"] is not None else "notes/seams.md not found"))
    print("[SCOPE] URLs are counted, not fetched; a fragment makes a different URL; quotations are not counted here; seams are counted from the headings of notes/seams.md, not from the entries.")

if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent)
