# Method

## Note on the use of AI assistance

The author used large language model assistants for source retrieval, for checking quotes, dates and states against the original pages where these could be read in full (partial readings are declared in the Evidence appendix), for drafting entries under the author's direction and for editing. Drafts were also reviewed by separate model passes acting as adversarial reviewers. The author reviewed every statement and its source before publication. Work files and the change log are retained. No pass to remove traces of machine assistance was applied to this text. The version covered by this note is the one stated in the header and in AI-USE.md. The tools, uses and version covered are declared in full in [AI-USE.md](AI-USE.md).

## Inclusion

An item is included if its public texts define or discuss how an agent finds, identifies, pays or transacts with a seller, a product or a service. Items that touch the subject without being on that path are listed as context entries.

Entries are grouped by the kind of body behind them: W3C, IETF, GS1, UN/CEFACT, other standards bodies (CEN/CENELEC and IEEE), AAIF, the Linux Foundation (with the projects of its Joint Development Foundation, such as DIF), independent projects (for example schema.org, ARD, the OpenID Foundation and the positions of browser vendors) and industry. Industry groups the protocols and programmes published by companies or industry consortia; EMVCo and the FIDO Alliance are consortia.

Not covered: 3GPP (its agent discovery work is surveyed in draft-jimenez-dawn-discovery-landscape-00), ETSI, ITU-T and ISO/IEC JTC 1/SC 42.

## Scope

This map documents public standardisation activity, specifications and declared commitments. It does not measure market adoption, transaction volume, cross-protocol interoperability or the reliability of deployed implementations. Implementation claims are reported only where supported by dated public evidence and are not treated as evidence of interoperability.

llms.txt is cited in the entry ard (a Lighthouse audit) and is not assessed in this version.

## Rules

1. **Public sources only.** Every statement points to a public URL and the date it was read. No private correspondence, paraphrased or not.
2. **Committed, not predicted.** "Committed next" means a deliverable, a scheduled event or an intention declared by the responsible body, with a date where one was given. Estimates by individual participants are not listed.
3. **No proposals.** Gaps and overlaps are recorded as facts. What to do about them belongs elsewhere.
4. **Dated.** Each entry carries `as of` and `verified` dates.
5. **Existing surveys are cited, not redone.** Where a survey covers ground (for example draft-jimenez-dawn-discovery-landscape), the map links it and covers only what it leaves out.

## How an entry is written

Each core entry has the same fields: Status (two sentences at most, with its "as of" date); Relevance to commerce; Committed next (declared items only); Boundary (what the item declares out of scope); Author participation (only where the author of this map took part, see Disclosure); Sources (primary URLs). Context entries have a short status, a line of relevance and sources.

## Source classes

Every source is tagged with one of four classes, shown in the text: **normative text** (specification, charter, schema, repository rule); **official decision or commitment** (merged change, press release, ballot, announcement); **maintainer or chair statement**; **participant or third party**. A statement of a participant or a third party is never presented as the position of the venue. Open proposals by third parties are in their own appendix, with author, date and state.

## How to read the negatives

A negative is always written as "not found in [corpus, date]": it describes the texts that were searched, not the world. What was read and what was not is in the appendix "Evidence and coverage".

## Internet-Drafts at the IETF

An Internet-Draft is not an IETF decision, and the map says which kind of draft it names. A **working group document** is a draft a working group has adopted; its name begins `draft-ietf-` followed by the group. An **individual Internet-Draft** has no working group: the datatracker lists it under "Individual Submissions" and shows no stream. Wherever the map names an individual draft it calls it individual, and an entry that exists only to list such drafts says so in its status. The datatracker states the standing of an individual draft in these words, copied on 2026-10-16 from the page https://datatracker.ietf.org/doc/draft-ranjbar-dane-did/: "This document is an Internet-Draft (I-D). Anyone may submit an I-D to the IETF. This I-D is not endorsed by the IETF and has no formal standing in the IETF standards process." The sentence holds for every individual draft in the map, including those named inside an entry whose organisation is IETF: that field names the venue of the work item (a charter, a list, a BoF), not an endorsement of the drafts the entry mentions. The group and the date of each draft named in the map were read on the datatracker (2026-10-13 to 2026-10-16).

## Versions and citation

The website is the living version and changes as venues move. Each DOI identifies a frozen snapshot: version 1.4 (2026-11-09) is the tag v1.4 of the repository and has the version DOI 10.5281/zenodo.24073152; version 1.3 (2026-11-02) is the tag v1.3 of the repository and has the version DOI 10.5281/zenodo.23882108; version 1.2 (2026-10-26) is the tag v1.2 of the repository and has the version DOI 10.5281/zenodo.23655852; version 1.1 (2026-10-19) is the tag v1.1 of the repository and has the version DOI 10.5281/zenodo.23464332; version 1.0.1 (2026-10-14) is the tag v1.0.1 and has the version DOI 10.5281/zenodo.23377309; version 1.0.0 is the tag v1.0.0 and has the version DOI 10.5281/zenodo.23357362. The concept DOI 10.5281/zenodo.23357361 always resolves to the latest version; cite the version DOI for the text you read.

Changes verified by Friday evening enter the following Monday's release; a Monday with no change to citable content produces no new version. Corrections and proposals go through issues on the repository, one per entry, so that each change has a public trail.

Archive copies: snapshots of the cited sources were requested on 2026-10-14 from the Wayback Machine of the Internet Archive, and the failed ones were requested again, in part, on 2026-10-15. Of 576 distinct URLs of the entries and notes, 357 now have a snapshot (291 saved on request, 66 that already had a copy from 2026-10-01 or later), 211 failed (206 of them with an error of the service) and 8 were not requested (a login, a token, a placeholder or a Google Doc). Where a snapshot exists, `map.json` and the JSON of the entry carry it in an `archived` field next to the URL, and the entry page links it. A snapshot is a copy kept by a third party, taken at the time shown in its address; it is not the text read on the date of reading.

**Changelog.**

**Since 1.4 (not a numbered version).** Corrections to the living version, for the next numbered version.

- `gs1-web-vocabulary`: the status in 1.4 gave the reading date of the GS1 Web Vocabulary change log, 2026-11-09, in parentheses after its newest entry, 1.17.0, so that it read as the date of that version; the change log gives no dates and does not yet list 1.18 (read again on 2026-11-09).
- `ietf-wimse-aims`: the status in 1.4 gave revision 00 as the latest, from a reading on the morning of 2026-11-02; revision 01 was posted at 18:20 UTC the same day and expires 2027-05-06. The status now gives -01 and what it changes (read on 2026-11-09).

**1.4 (2026-11-09).** Two entries added (`gs1-epcis`, `gs1-web-vocabulary`); corrections and additions to the living version. Facts dated after Friday 2026-11-06 are deferred to 1.5, except corrections of the state of a source already cited (the move of the agentproto use cases draft to the working group stream on 2026-11-07) and contributions of the author of this map.

Between 1.3 and 1.4, on the living version:

- Site header: the one-line description of the map is shown under its name on every page; the home page no longer repeats the name and the tagline above its text, and each page has one h1 (presentation only, no change to the data).

Corrections:

- `x402` and seam S1: pull request #8 of the Domain Discovery working group and pull request #2979 of the core repository, which version 1.3 called no longer reachable (404 on 2026-11-02), are reachable and open again on 2026-11-09; the two open proposals are open again.
- `ietf-agentproto`: draft-agentic-ai-usecases-requirements is at -07, published on 2026-11-02, and on 2026-11-07 it moved to the IETF stream in the agentproto group as "Candidate for WG Adoption".
- `kyapay`: kyapay-token-03 and using-kyapay-tokens-02 (2026-11-02), still individual submissions; the -03 text replaces the -02 as source.
- `ietf-vcon`: draft-ietf-vcon-vcon-core is at -05 (2026-10-31).
- `w3c-did-resolution`: Candidate Recommendation Draft of 2026-11-03.
- `lf-ai-catalog`: pull request #117 merged on 2026-10-28 and pull request #91 closed without merge on 2026-10-29, both out of the open proposals.
- `a2a-core`: the Technical Steering Committee has nine seats since 2026-10-20, with Bloomberg.
- `ucp`: the status is rewritten as the state at 2026-11-06; the readings of 1.3 are kept word for word in the evidence. The passed target of issue #682 is replaced by the lodging milestone of 2026-12-08.
- `w3c-tpac-2026`: breakouts #22, #34, #69, #71 and #84 are recorded as held, on their published draft minutes; breakout #95 was not held.
- `w3c-digital-policy-wg`: the draft charter of the entry is unchanged since 2026-10-05; a second draft charter, Digital Policy Platform Working Group, sits next to it.

Additions:

- `gs1-epcis` and `gs1-web-vocabulary` (new entries, issues #27 and #29), and the relevance of `gs1-conformant-resolver` and `gs1-digital-link` rewritten from the standards (issues #23 and #25); read on ref.gs1.org on 2026-11-09. The EPCIS archive gives version 2.0.1, while the PDF it serves prints Release 2.0; an ISO/IEC 19987 equivalence is not stated on the pages read. Seam S2 gains both entries.
- `ucp`: governance from GOVERNANCE.md and TC_ELECTIONS.md (four councils, founders and seats, minutes published, the Local Services and B2B Procurement charters approved on 2026-11-04 and 2026-11-05, the domain working groups and two Payments working group charters proposed on 2026-11-05); lodging as a working draft on main, not in a published release, milestone 2026-12-08; identity linking pull request #998 (2026-10-31); a method note on the WooCommerce discovery fixes for censuses of `/.well-known/ucp`.
- `ard` and `ietf-dawn`: the three ARD drafts of 2026-10-30 taken to DAWN and on the IETF 127 agenda; third-party implementations declared in ard-spec issues; the `TrustManifest` key of the entry schema; the DAWN charter sentence on initial discovery only; current revisions of the individual DAWN drafts. The discovery paths counted on the home page are unchanged (ARD was already counted).
- `ietf-audit`: draft-gruszka-audit-decision-receipts-05; the state of the charter text on VCON (a review suggestion, not merged); the vCon AI agent extension draft.
- `ietf-vcon`: draft-birkholz-vcon-ai-agent-extension-00.
- `ietf-wimse-aims`: the AER-1 conformance corpus (issue #19); revisions of draft-hulea-wimse-agent-mandate and draft-zambo-aer1-wimse-mapping.
- `ietf-webbotauth`: agent-census pull request #143 (2026-11-01).
- `ap2`: issue #393, with the fact checked at the source that version 0.2.0 has no Intent Mandate.
- `pap`: versions 0.2 and 0.3; the reference implementation promised for about 2026-11-09 not published by 2026-11-06.
- `w3c-agenticweb-wg`, `w3c-webmcp-cg-report`, `w3c-ai-agent-protocol-cg`, `w3c-web-payment-security-ig`: TPAC minutes and the co-chairs' summary of breakout #22, the WebMCP resolutions of 2026-10-27, the state of the charter at 2026-11-06, the WebKit explainer of a digital credential payment method.
- `shopify`: toolkit release v2.3.0.
- Seams: ARD at DAWN and the Lighthouse `agentmap` directive, GS1 at breakout #22 (S1); schema.org identifiers over http and https (S2).
- Disclosure: contributions and presence of the author of this map from 2026-10-28 to 2026-11-07.
- Site: the current version as a pill next to the name in the header; the blue strip of the entry pages keeps the maintainer and the Introduction link.

Deferred to 1.5:

- An EU Digital Product Passport Registry note for seams S1 and S2: the guidelines were read by the author's chat on 2026-11-03 but their addresses could not be re-read for this version.
- UCP: purchase options (pull request #890, not merged, based on another branch); the lodging council minutes of 2026-11-03 (published 2026-11-07); issue #969; a row on schema.org-shaped attributes and published JSON-LD.
- A2A pull request #2378; the bazatap census; AAIF identity and trust issue #21; vCon pull request #43; WooCommerce agent readiness pull requests #70499 and #70509; KYAPay pull requests merged on 2026-11-02 (their text in the published revision not checked); the AUDIT agenda for IETF 127 (2026-11-08).
- The same status rewrite as `ucp` for nine other entries whose status has piled up readings.

Credit: Sven Böckelmann (issues #23, #25, #27 and #29; his disclosure is in the evidence of the four entries) and zambodotdev (issue #19).


**1.3 (2026-11-02).** No entry added; corrections and additions to the living version. Facts dated after Friday 2026-10-30 are deferred to 1.4 (among them UCP pull request #998 on identity linking, the UCP Governing Council minutes of 2026-10-30, draft-hulea-wimse-agent-mandate-01 and draft-zambo-aer1-wimse-mapping-02), except contributions of the author of this map and proposals made to this map in its own issues.

Corrections:

- `ucp`: pull request #634, the return policy extension, was merged into main on 2026-10-23; the entry said it was open.
- `ucp` and Calendar: the two dates of issue #924 (nominations by 2026-10-23, initial package on 2026-11-02) are removed: the issue was revised on 2026-10-23, nominations were due by 2026-10-30, and no date for a package remains.
- `w3c-agenticweb-wg`: after pull requests #901 and #907 to #910 (2026-10-29 and 2026-10-30) the draft charter has five normative deliverables and a threat model, no longer WebMCP alone, and two more out-of-scope items.
- `w3c-agent-identity-registry-cg`: the minutes the entry said were not found are in the group's repository; the minutes of 2026-10-20 and the next meeting (2026-11-17) are reported.
- `ietf-individual-seller-drafts`: the sentence quoted from draft-hood-agtp-merchant-identity is attributed to -02; it is not in -03.
- `x402` and seam S1: pull request #8 of the Domain Discovery working group and pull request #2979 of the core repository are no longer reachable (404 on 2026-11-02; how they were removed is not known); the entry keeps them among the open proposals, as closed, and says that the discussion on the content of `/.well-known/x402` continues in issue #11 of the working group.
- `w3c-tpac-2026`: TPAC is reported in the past; breakout #25 was canceled; no other session is recorded as held, since no minutes were found.
- Tools: `build_map.py --check` refuses a key repeated in the same mapping, which YAML would otherwise keep once and drop silently; it runs a self-test first.

Additions:

- `aaif-structure`: 305 members as AAIF states it, the AAIF Landscape at landscape.aaif.io, and the date of 2026-10-15 of the Ecosystem Architecture Map, passed with no release.
- `ucp`: the Identity Linking capability and the Loyalty extension; issue #947 (B2B Procurement charter); the release train decided by the Shopping Tech Council on 2026-09-25, with the difference between the dates in the minutes and the linked milestones; pull requests #1017 to #1020 on business identity and seller attribution; lodging booking and cancellation policy on main since 2026-09-24; a census by Kin Lane of 2026-10-30, cited with its licence (CC BY-NC-SA 4.0) and not incorporated; participation and Disclosure.
- Disclosure: contributions of the author of this map from 2026-10-23 to 2026-11-02 (UCP, W3C, Lighthouse, AI Catalog).
- `w3c-agenticweb-wg`: the W3C TAG Group Note "User Agents" (2026-10-22), as a statement; issues #905 and #906 open; participation (charter text proposed by the author of this map and merged with pull request #908).
- `w3c-ai-agent-protocol-cg`: the white paper and what it compares; the WebAgents Community Group meeting at TPAC with a talk by this group's co-chairs.
- `ard`: pull request #111, informative observability guidance; participation.
- `lf-ai-catalog`: participation.
- `ietf-dawn`: overlap with `ietf-dnsaid`; draft-king-dawn-requirements-02; draft-jakab-dawn-agent-discovery-mdns-01 (issue #18); the individual drafts draft-artamokhov-dawn-marketplace-discovery-01, draft-artamokhov-dawn-index-federation-01 and draft-dinuzzo-best-protocol-02, as candidates not counted on the home page.
- `mcp-server-card` and `ietf-dnsaid`: draft-morrison-mcp-dns-discovery-09, DNS discovery of MCP servers, with its author's disclosure (issue #22).
- `ietf-individual-seller-drafts`: draft-hood-agtp-merchant-identity-03 and draft-hood-agtp-commerce-01.
- `ietf-wimse-aims` and seam S4: AER-1, draft-zambo-aer1-26, execution receipts for agent tool calls (issue #19); draft-hulea-wimse-agent-mandate-00.
- Seam S3: the OAuth WG document draft-ietf-oauth-delegate-sd-jwt-00; the individual drafts draft-martinez-itp-agent-mandates-00 and draft-kroehl-agentic-trust-aae-02 (issue #20); prior work on attenuated delegation (SPKI, Macaroons, Biscuit, zcap, UCAN, AAuth).
- Seam S2: product classifications (ETIM, ECLASS, GS1 GPC), as distinct from product identity.
- `gs1-conformant-resolver`: the success path of the standard (redirect, linkType, linkset, default link, 300 Multiple Choices).
- `acp`: pull request #316 (dispute resolution extension) as an open proposal, with the note that its proposer publishes a policy under which it would resolve such disputes; issue #304 is now a Discussion.
- `ap2`: issue #338 (dispute-time evidence file) as an open proposal.
- `aaif-identity-trust`: the brief posted on issue #15 on 2026-10-31 after MintID's presentation to the AAIF Agentic Commerce Working Group, as a statement of the party; MintID stays an open proposal.
- `w3c-gs1-ecommerce-workshop`: the KYA-OS position statement and the three position-statement PDFs (issue #21).
- Home page: at least nine discovery mechanisms or publication paths, with `/.well-known/x402`.
- Repository: an issue template for proposing a new entry.
- Credit: proposals by Marc Molas (issue #15), ljakab (issue #18), zambodotdev (issue #19), MoltyCel (issue #20), H0BB5 (issue #21) and maxchop (issue #22).

Between 1.2 and 1.3, on the living version:

- `ietf-agentproto`: the IETF 127 session is scheduled on 2026-11-16, 14:00 to 16:00 San Francisco time, room Continental 5 (datatracker agenda, read on 2026-10-26).
- `ietf-webbotauth`: the IETF 127 session is scheduled on 2026-11-17, 16:30 to 18:30 San Francisco time, room Continental 4 (datatracker agenda, read on 2026-10-26).
- `ietf-audit`, `ietf-vcon`, `ietf-dawn`, `ietf-wimse-aims`: the IETF 127 sessions with day, time and room: AUDIT BoF and vcon on 2026-11-17, dawn on 2026-11-19, wimse on 2026-11-18 and 2026-11-19 (the second a joint session with OAUTH) (datatracker agenda, read on 2026-10-26).
- Calendar: the IETF 127 sessions of agentproto, AUDIT (BoF), vcon, webbotauth, wimse (two, the second a joint session with OAUTH) and dawn, read on the datatracker agenda on 2026-10-26.
- Site header: map name on every page, link to the repository, short introduction for visitors arriving on an inner page. External links open in a new tab and are marked.
- Site tables: dates kept on one line and long source URLs shown as short link text (the links are unchanged).
- Site layout: tables kept within the text column, header line and intro box aligned to it (links unchanged).
- `ucp`: the well-known URI suffix `ucp` is registered in the IANA Well-Known URIs registry (provisional, registered 2026-10-26); the registration request (issue #92) was closed on 2026-10-27 (registry read on 2026-10-27).
- Seam S1 and the home page: `/.well-known/ucp` is counted among the paths registered with IANA, with `agent-card.json`.
- Home page: IETF DAWN is described as a working group since 2026-10-22 (approved charter charter-ietf-dawn-01), no longer as a charter in external review.

**1.2 (2026-10-26).** One entry added; corrections and additions to the living version.

Corrections:

- `aaif-identity-trust`: the entry said on 2026-10-09 and 2026-10-13 that no release notes were found for the MintID tags; that was a misreading, since CHANGELOG.md is present in the tagged tree since public-v2026-10-06. Corrected on 2026-10-19 after issue #16, which also reported the merge of pull request #288 on 2026-10-13 and the independent run on issue #13; the status was re-read and is dated 2026-10-19.
- `aaif-identity-trust`: issue #16 is named in the text of the evidence instead of linked.
- `aaif-identity-trust`: the name of the entry was cut after "issue" wherever it was shown, including in version 1.1, because the YAML file read the rest as a comment; it is now quoted and shown in full.
- Tools: `build_map.py --check` refuses an unquoted value followed by " #", which YAML reads as a comment, and names file, key and line; it reads the source text, after a self-test.
- `ucp` and Disclosure: after the comments of the author of this map on PR #966, the entry reports what the PR author wrote on 2026-10-22 (an update pushed, then the merge into the branch of PR #634), no longer that the comments were acted on.

Additions:

- `ietf-audit`: adjacent work, the individual Internet-Draft draft-mih-scitt-agent-action-capsule-05 (read on the datatracker on 2026-10-21).
- `aaif-identity-trust`: a context entry for MintID, proposed in issue #15, is recorded under Open proposals; the PyPI records and the AAIF list messages it cites could not be read.
- New entry: `iab-tech-lab-aamp` (context), IAB Tech Lab AAMP 3.0 and OpenProposal, a draft whose public comment period ran until 2026-10-22; its proposals on a well-known manifest and on Web Bot Auth are listed as open proposals.
- `ietf-dawn`: the working group was formed on 2026-10-22 (charter-ietf-dawn-01; chairs Dapeng Liu and Frank Brockners, technical advisor Kehan Yao, Area Director Éric Vyncke); milestones of the approved charter; the entry was reviewed after the formation (no WG document yet, revisions of the individual drafts, the BoF and telechat states in the past tense), and seam S1 follows it.
- `ietf-dawn`: the individual draft draft-jakab-dawn-agent-discovery-mdns-00 (mDNS and DNS-SD on a local link), proposed in issue #18.
- `w3c-ai-agent-protocol-cg`: the meeting of 2026-10-21 and pull request #46 (open, no choice recorded between two approaches); participation and Disclosure.
- `ucp`: pull request #966 merged on 2026-10-22 into the branch of PR #634 (not into main), with the `not_accepted` wording of policy_return.json; #940 merged, #985 open; participation and Disclosure.
- `w3c-tpac-2026`, `w3c-agenticweb-wg`: slots of the breakouts on agents, breakout #22 on 2026-10-30 with a discussion of the Agentic Web charter proposed for it; the charter is still in refinement.
- `w3c-browser-testing-tools-wg`: the new charter of the Browser Testing and Tools Working Group (2026-10-20 or 2026-10-21 to 2028-10-20, as each W3C page states it), whose scope includes agentic browsing.
- `ietf-webbotauth`: draft-illyes-webbotauth-cbcp-01 (2026-10-22), cbcp PR #23 and protocol PR #140 merged, the individual draft draft-kelley-webbotauth-sail-00; participation and Disclosure.
- `ietf-audit`: issue #64 of the BoF preparation repository on an out-of-scope section; still a BoF with no charter on 2026-10-23.
- `ietf-agentproto`: the IETF 127 session is waiting for scheduling.
- `ietf-vcon`: the interim of 2026-10-22 (no minutes yet) and pull request #41 changed after it; participation and Disclosure.
- `ap2`: the AP2 documentation and the FIDO "Agentic AI" page on the FIDO working groups, each attributed to its source (issue #11).
- `a2a-discovery`: pull request #2240 merged on 2026-10-21 into the branch dev-1.1 (not into main): AI Catalog is the preferred discovery mechanism there; seam S1 follows it.
- `x402`: added to seam S1, with the Domain Discovery working group (PR #6 merged; PR #8 and issue #11 open) and PR #2979 open, proposed in issue #17.
- `aaif-structure`: ten hosted projects listed on aaif.io/projects, four of them announced on 2026-10-22.
- Calendar: the events of 2026-10-22 marked as held, the comment deadline of the DID WG charter (2026-11-05) added, and the rows checked again on 2026-10-23.
- `ietf-vcon`: pull request #41 merged on 2026-10-25 into main of the core draft repository; state of the charter on the datatracker re-read.
- Disclosure: the two rows on vCon pull request #41 give its state as merged on 2026-10-25.
- Credit: proposals by Michael Blake (issue #17), Marc Molas (issues #15 and #16), Alan Blount (issue #11) and ljakab (issue #18).

**1.1 (2026-10-19).** Two entries added; corrections and additions to the living version.

- New entries: `anp` (issue #6) and `accord-project` (issue #1).
- `a2a-core`, `a2a-discovery`: org corrected from Linux Foundation to AAIF; A2A joined AAIF as a hosted project (AAIF, 2026-08-17; Growth Stage, A2A blog of 2026-08-27) (issues #7 and #8).
- `mcp-core`, `mcp-server-card`: org corrected from Linux Foundation to AAIF; MCP is listed among AAIF's projects, and the Server Card is the work of an MCP Working Group (issues #9 and #10).
- `aaif-structure`: hosted projects listed from aaif.io/projects (issue #13).
- `ap2`: date of the donation and Google's announcement added, with the FIDO working groups named in the FIDO release; the wording of the status and of the governance row stays open in issue #11.
- `fido-agentic-standards`: Google's "donating" reported next to FIDO's "contributed" (issue #12).
- Proposals: A2A issue #2323 under `a2a-core` (issue #5); A2A issue #2043 under `a2a-discovery` (issue #4); did:dns issue #12 and draft-ranjbar-dane-did under `ietf-dnsaid` (issue #3); draft-ranjbar-dane-anchored-identity added to `ietf-dnsaid` (issue #2).
- IETF: individual Internet-Drafts are now labelled as individual wherever they are named, and the Method gives the Datatracker's wording on their standing; one entry no longer calls an individual submission an "Independent Submission".
- IETF revisions updated: `draft-agentic-ai-usecases-requirements` -04 (`ietf-agentproto`) and `draft-zhang-dawn-agent-discovery-framework` -07 (`ietf-dawn`), read on the datatracker on 2026-10-16.
- `w3c-ai-agent-protocol-cg`: overlap with `anp` added.
- 2026-10-16, update cadence: the header, the footer and the page for agents and tools say the map is updated weekly; Method and CONTRIBUTING state that numbered versions go out on Mondays.
- 2026-10-15, `dif-trusted-ai-agents`: org corrected to Linux Foundation, reported by a DIF participant on the AAIF Taxonomy list.
- 2026-10-15, CONTRIBUTING and issue template: proposals now state the proposer's role and any employer or commercial interest.
- 2026-10-15, header: the citable version and the date of the live site are shown separately.
- Credit: corrections proposed by Alan Blount (zeroasterisk) in issues #7-#13 and PR #14.

**1.0.1 (2026-10-14).** Corrections and additions to the living version; no entry was added or removed.

- DAWN: the example "discover all agents in this shop" is given as the example of the local network, not as a commercial example on the web; the example of the public Internet is "discover all agents of example.org, for all its customers/members".
- Seam S1: the redirect rules of UCP and of the Personal Agent Protocol are said to differ (different paths and different readers), not to be opposite.
- Home and S1: the count of discovery paths is eight (the home page counted seven and left out the poppy.json of the Personal Agent Protocol).
- Disclosure: the pull request on the W3C charter drafts is recorded as merged on 2026-10-13.
- UCP: the census figure called "row 2" is "row 2 and ucp.version present", as its author wrote on 2026-10-14.
- Calendar: three provisional TPAC breakout slots, with their source and the conversion to Rome time.
- AI-USE.md: the hash it carries is that of the bundle of the released version, and the export checks it against the tag.
- Disclosure: the presentation to the AAIF Agentic Commerce Working Group is recorded as given on 2026-10-14, with the list message of that day.
- Disclosure: the time of the DAWN list message of 2026-09-25 is removed; the date stays.
- IANA: a registration request for `ucp` has been open in the registry's repository since 2026-06-06 (issue #92), and is recorded in S1 and in the UCP entry.
- TPAC: the entry follows the breakout calendar of 2026-10-14 (85 sessions, all marked tentative).
- Sources: archive links in `map.json`, in the JSON of each entry and on the entry pages.
- Presentation: the table "Payment protocols compared" has four columns, short labels for the source links, and may be wider than the text column; the text of its cells did not change.
