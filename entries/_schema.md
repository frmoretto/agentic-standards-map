# Entry fields (schema v2)

One YAML file per entry. `python tools/build_map.py --check entries/<id>.yaml` validates a file.

```yaml
id: short-kebab-id             # unique, used in `overlaps`
name: Human-readable name
org: W3C | IETF | GS1 | UN/CEFACT | Other standards bodies | AAIF | Linux Foundation | Independent | Industry
kind: venue | charter | specification | work-item | event | position
tier: core | context           # core: on the path of a seller, a product or a service; context: touches it
status: Two sentences at most. What the item is now. Dated by status_as_of.
status_as_of: YYYY-MM-DD
relevance: >                   # core: 3-5 sentences on where commerce, products or sellers enter.
  context: 1-2 sentences. Statements by a participant or a third party say so in the sentence.
committed_next:                # core: 1-3 items. ONLY declared deliverables, scheduled events or
  - what: ...                  # intentions of the responsible body. Not a participant's estimate.
    when: YYYY-MM-DD | "approx. YYYY-MM-DD" | undated
    source: URL
    class: normative | decision | statement | third-party
boundary: One sentence: what the item declares out of scope (core).
participation: Optional. "The author of this map took part in ...; see Disclosure."
sources:                       # primary URLs, and every other page quoted in the entry
  - url: ...
    read: YYYY-MM-DD
    class: normative | decision | statement | third-party
overlaps: [other-id, ...]      # optional
seams: [S1, S3]                # optional: the seams of notes/seams.md that name this entry (S1 to S4). Both sides must agree:
                               # an id listed in the first line of a seam has that seam here, and the other way round
                               # (python tools/build_map.py checks it). Not rendered in MAP.md or the bundles; the site shows it.
verified: YYYY-MM-DD
evidence:                      # optional; rendered as one line per entry in the appendix "Evidence and coverage"
  read: the corpus read (window, criterion), in full
  not_read: what was not read, in full
  not_found: optional; the negatives, each as "Not found in [corpus, date]: ..."
open_proposals:                # optional; rendered in the appendix "Open proposals"
  - what: ...
    author: login or organisation
    date: YYYY-MM-DD
    state: open | closed | merged | draft
    url: ...
matrix:                        # only the payment protocols of the comparison table
  governance: ...
  version_state: ...
  signs: ...
  signer: ...
  record: ...
  dispute: ...
  source: URL
```

Source classes, shown in the text: **normative** = normative text (specification, charter, schema, README rule);
**decision** = official decision or commitment (merged change, press release, ballot, announcement);
**statement** = maintainer or chair statement; **third-party** = participant or third party.

Dates: `status_as_of` is the date of the readings behind `status`; `verified` is the date of the most recent reading of any part of
the entry, and is not earlier than `status_as_of` or than any `read` date of a source (`python tools/build_map.py --check` fails otherwise).
`evidence.read` says which part was read on which date. `when` is one date, `approx.` plus one date, or `undated`: a week or a range
(for example the IETF meeting week) is written in `what`. `open_proposals[].state` is one word of the enum; the reason or the date
of a closure goes in `what`.

Negatives are always "not found in [corpus, date]". Numbers in entries are only dates, versions and identifiers; counts that
define coverage go in `evidence`.
