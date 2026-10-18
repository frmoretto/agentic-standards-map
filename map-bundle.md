<a id="part-readme"></a>

# Agentic Standards Map

**Who is standardising agentic commerce, where, and what they have committed to next.**

W3C, IETF, GS1, UN/CEFACT, the Linux Foundation, AAIF, and the industry protocols (UCP, ACP, AP2, x402, Visa, Mastercard) are all working on how an AI agent finds a seller, trusts a product, proves who it acts for and pays. They do it at the same time, at different speeds and with different rules. This map puts them on one page.

Every statement is dated and points to a public source. The map makes no predictions or recommendations of its own and does not rank approaches. Third-party proposals are recorded with attribution and their stated status.

This map documents public standardisation activity, specifications and declared commitments. It does not measure market adoption, transaction volume, cross-protocol interoperability or the reliability of deployed implementations. Implementation claims are reported only where supported by dated public evidence and are not treated as evidence of interoperability.

*Version 1.0.1 (2026-10-14) · site updated 2026-10-15. The map is updated as venues move; each entry carries its own read date.*

DOI (all versions): [10.5281/zenodo.23357361](https://doi.org/10.5281/zenodo.23357361)

---

## Four things you see only when you look across venues

**1. The map identifies at least eight discovery mechanisms or publication paths.** `/.well-known/ucp`, A2A's `agent-card.json`, schema.org, ARD, AI Catalog, MCP Server Cards, DNS-AID and the `/.well-known/poppy.json` of the Personal Agent Protocol. Of these eight, only `agent-card.json` is in the IANA well-known registry (updated 2026-10-07, read 2026-10-14). Two venues have discovery-charter work in progress: the IETF DAWN charter is in external review, with comments to the IESG due by 2026-10-19 and an IESG telechat listed for 2026-10-22, and the W3C Agentic Web WG charter is in refinement. [Seam S1](map-bundle.md#part-seams)

**2. Product identity: one ratified route and one route marked at risk.** GS1 Digital Link gives a ratified route to product identifiers; the DID route cited for Digital Product Passports rests on a feature that the DID Resolution Candidate Recommendation Draft marks at risk. One workshop position statement (#31, Sven Böckelmann) frames the open question as three checks: "Where. Who signed. Who may." [Seam S2](map-bundle.md#part-seams)

**3. Agent identity: several protocols reference HTTP Message Signatures or Web Bot Auth.** Visa TAP, Mastercard Agent Pay, UCP and x402 build on RFC 9421 or Web Bot Auth. The IETF agentproto charter names webbotauth among the groups to coordinate with, and the draft W3C Agentic Web charter lists it for coordination too. ACP's texts do not mention it (not found in the ACP repository, 2026-10-03). [Seam S3](map-bundle.md#part-seams)

**4. Checkout: what each protocol defines differs between the checkout and the events after it.** Native AP2 chains a merchant-signed checkout, the user's mandate and a Checkout Receipt that the merchant must return once it accepts or rejects the mandate (docs/ap2/specification.md at commit e1ea56d, read 2026-10-13). The words refund and cancel are not found in the seven AP2 documents of docs/ap2; the goods-return term occurs only as the field return_policy ("30-day returns") in two example checkouts of checkout_mandate.md, and fulfil(l) only as a generic verb, never for the fulfilment of an order (2026-10-14). UCP signs the delivery of order webhooks (RFC 9421) and ACP signs its webhooks with HMAC: those are signatures on a delivery. Poppy, PACT and Shopify/shop each state in writing what their own record does not prove. A confirmation to the consumer on a durable medium is not found in the Poppy specification and operations pages, the PACT specification page or the Shopify/shop README, SKILL.md and transactions.md (2026-10-13). [Seam S4](map-bundle.md#part-seams)

## Next on the calendar

- **15 Oct** Accuracy & Reliability of AI Agents: Virtual Summit, 15:00 to 17:00 GMT, online
- **15 Oct** AAIF Taxonomy and Landscape Workstream: Ecosystem Architecture Map v1.0, target in the charter
- **approx. 19 Oct** Schedule of the Monday to Wednesday TPAC breakouts added to the TPAC calendar
- **19 Oct** Comments on the proposed DAWN charter due to the IESG mailing list
- **21 Oct** aipref virtual interim meeting, 20:00 to 21:30 UTC, no agenda submitted on 2026-09-30

Full 60-day calendar: [Calendar](map-bundle.md#part-calendar)

## How the map is built

- **Public sources only.** Every statement links to a public URL and the date it was read.
- **Committed, not predicted.** "Next" means a deliverable or event declared by the responsible body.
- **Facts, not proposals.** Gaps and overlaps are recorded; what to do about them belongs elsewhere.
- **Speaker is explicit.** Each source is tagged: normative text, official decision, maintainer or chair statement, participant or third party. A participant's view is never presented as the venue's position.
- **Negatives are scoped.** "Not found" always says in which texts and on which date.
- **AI assistance is declared.** How language model assistants were used, and what the author checked, is stated in [AI-USE.md](AI-USE.md).

Inclusion, entry format and source classes are described in full in [METHOD.md](METHOD.md).

## About the author

Francesco Marinoni Moretto, independent researcher on agentic commerce, Milan.

ORCID [0009-0004-0096-4712](https://orcid.org/0009-0004-0096-4712) · GitHub [frmoretto](https://github.com/frmoretto) · LinkedIn [francesco-moretto](https://www.linkedin.com/in/francesco-moretto/)

I have taken part in some of the venues mapped; the [Disclosure](notes/disclosure.md) lists where, and the entries concerned say so.

Corrections and missing sources: [open an issue on the repository](https://github.com/frmoretto/agentic-standards-map/issues).

### How to cite

Marinoni Moretto, F. (2026). Agentic Standards Map (Version 1.0.1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.23377309

Please cite the entry id, the date it was read and the DOI. To cite the map in general, use https://doi.org/10.5281/zenodo.23357361.

---

Version 1.0.1 (2026-10-14) · site updated 2026-10-15. Generated by `tools/build_bundle.py` from the repository files. Do not edit by hand.

## Index

1. [README](#part-readme)
2. [Method](#part-method)
3. [Introduction](#part-intro)
4. [Disclosure (short)](#part-disclosure-short)
5. [Core entries: status](#part-status)
6. [Seams](#part-seams)
7. [Payment protocols compared](#part-matrix)
8. [Core entries](#part-core)
9. [Context entries](#part-context)
10. [Appendix: Evidence and coverage](#part-evidence)
11. [Appendix: Open proposals](#part-proposals)
12. [Appendix: Full disclosure](#part-disclosure)
13. [Appendix: Calendar](#part-calendar)

Core entries (33):

- [W3C AI Agent Protocol Community Group](#w3c-ai-agent-protocol-cg)
- [W3C Agentic Web Working Group (draft charter)](#w3c-agenticweb-wg)
- [W3C DID Resolution](#w3c-did-resolution)
- [W3C TPAC 2026 breakouts on agents (Dublin, 2026-10-26/30)](#w3c-tpac-2026)
- [W3C/GS1 Workshop on E-commerce for Humans and AI Agents (Zurich, 8-9 Sep 2026)](#w3c-gs1-ecommerce-workshop)
- [IETF AI Preferences (aipref WG)](#ietf-aipref)
- [IETF AUDIT (BoF preparation)](#ietf-audit)
- [IETF DAWN, Discovery of Agents With Names (proposed WG)](#ietf-dawn)
- [IETF Web Bot Auth (webbotauth WG)](#ietf-webbotauth)
- [IETF agentproto (Agent Communication Protocols WG)](#ietf-agentproto)
- [IETF vcon (Virtualized Conversations WG)](#ietf-vcon)
- [Individual IETF drafts on the seller side](#ietf-individual-seller-drafts)
- [GS1-Conformant Resolver Standard 1.2.1](#gs1-conformant-resolver)
- [UN Transparency Protocol, Identity Resolver](#untp-identity-resolver)
- [CEN/CENELEC JTC 24 Digital Product Passport standards (EN 18216 to EN 18246)](#cen-clc-jtc24-dpp)
- [A2A protocol, agent discovery](#a2a-discovery)
- [AAIF Agentic Commerce Working Group](#aaif-wg-agentic-commerce)
- [MCP Server Cards (ext-server-card, SEP-2127)](#mcp-server-card)
- [AI Catalog (Agent Card Working Group)](#lf-ai-catalog)
- [x402](#x402)
- [Agentic Resource Discovery (ARD)](#ard)
- [Browser vendor positions on WebMCP (WebKit, Mozilla, Chrome, Edge)](#browsers-webmcp)
- [schema.org open issues relevant to agents, bookings, product and establishment identity](#schemaorg-open-agent-commerce-items)
- [Agent Payments Protocol (AP2)](#ap2)
- [Agentic Commerce Protocol (ACP)](#acp)
- [EMV Agentic Payments Framework for Specifications (draft for public feedback)](#emvco-agentic-payments-framework)
- [KYAPay (Skyfire)](#kyapay)
- [Mastercard Agent Pay](#mastercard-agent-pay)
- [Personal Agent Consent & Trust Protocol (PACT), published by Decagon with Instinct](#pact)
- [Personal Agent Protocol (PAP, "Poppy"), published by Sierra with Meta](#pap)
- [Universal Commerce Protocol (UCP)](#ucp)
- [Verifiable Intent](#verifiable-intent)
- [Visa Trusted Agent Protocol (TAP)](#visa-tap)

Context entries (26):

- [W3C Agent Identity Registry Protocol Community Group](#w3c-agent-identity-registry-cg)
- [W3C Agent-Ready Video Community Group](#w3c-agent-ready-video-cg)
- [W3C Agent-to-Web Framework (A2WF) Community Group](#w3c-agent-to-web-framework-cg)
- [W3C DID Methods Working Group (proposed charter)](#w3c-did-methods-wg)
- [W3C Decentralized Identifier Working Group (proposed charter)](#w3c-did-wg)
- [W3C Digital Policy Working Group (ODRL, draft charter)](#w3c-digital-policy-wg)
- [W3C Web Payment Security Interest Group](#w3c-web-payment-security-ig)
- [W3C browser-testing-tools Working Group (charter draft)](#w3c-browser-testing-tools-wg)
- [WebMCP (Draft Community Group Report, Web Machine Learning CG)](#w3c-webmcp-cg-report)
- [DNS for AI Discovery (DNS-AID, draft-mozleywilliams-dnsop-dnsaid)](#ietf-dnsaid)
- [IETF WIMSE, AI Identity Management System (draft-ietf-wimse-aims)](#ietf-wimse-aims)
- [Payment HTTP Authentication Scheme (draft-httpauth-payment, Tempo Labs and Stripe)](#ietf-httpauth-payment)
- [GS1 Digital Link Standard, URI Syntax 1.7.0](#gs1-digital-link)
- [UN Global Trust Register, namespace urn:gtr](#un-gtr-urn)
- [IEEE P3931 Agent Description, Discovery, and Registry (ADDR) Interoperability](#ieee-p3931-addr)
- [AAIF Identity and Trust group, issue](#aaif-identity-trust)
- [AAIF structure, Technical Committee and working groups](#aaif-structure)
- [Agent2Agent (A2A) protocol, core specification](#a2a-core)
- [Model Context Protocol (MCP), core specification](#mcp-core)
- [DIF Trusted AI Agents Working Group](#dif-trusted-ai-agents)
- [TRACE (Trust, Runtime Attestation and Compliance Evidence)](#trace)
- [EMILIA Protocol (individual drafts and open-source gate)](#emilia-protocol)
- [OpenID Foundation AuthZEN Working Group (agent authorization drafts AARP and COAZ)](#oidf-authzen-agents)
- [schema.org vocabulary for products, offers, sellers and lodging (current release)](#schemaorg-baseline)
- [FIDO Alliance agentic authentication and payments work](#fido-agentic-standards)
- [Shopify, MCP surfaces for buyer agents, developers and merchants](#shopify)

---

<a id="part-method"></a>
# Part 2: Method

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

## Versions and citation

The website is the living version and changes as venues move. Each DOI identifies a frozen snapshot: version 1.0.1 (2026-10-14) is the tag v1.0.1 of the repository and has the version DOI 10.5281/zenodo.23377309; version 1.0.0 is the tag v1.0.0 and has the version DOI 10.5281/zenodo.23357362. The concept DOI 10.5281/zenodo.23357361 always resolves to the latest version; cite the version DOI for the text you read.

Changes verified by Friday evening enter the following Monday's release; a Monday with no change to citable content produces no new version. Corrections and proposals go through issues on the repository, one per entry, so that each change has a public trail.

Archive copies: snapshots of the cited sources were requested on 2026-10-14 from the Wayback Machine of the Internet Archive, and the failed ones were requested again, in part, on 2026-10-15. Of 576 distinct URLs of the entries and notes, 357 now have a snapshot (291 saved on request, 66 that already had a copy from 2026-10-01 or later), 211 failed (206 of them with an error of the service) and 8 were not requested (a login, a token, a placeholder or a Google Doc). Where a snapshot exists, `map.json` and the JSON of the entry carry it in an `archived` field next to the URL, and the entry page links it. A snapshot is a copy kept by a third party, taken at the time shown in its address; it is not the text read on the date of reading.

**Changelog.**

**Since 1.0.1 (not a numbered version).**

- 2026-10-18, `a2a-core`, `a2a-discovery`: org corrected from Linux Foundation to AAIF; A2A joined AAIF as a hosted project (AAIF, 2026-08-17).
- 2026-10-18, `mcp-core`, `mcp-server-card`: org corrected from Linux Foundation to AAIF; MCP is listed among AAIF's projects (aaif.io/projects).
- 2026-10-18, `ap2`, `fido-agentic-standards`: AP2 described as donated by Google to the FIDO Alliance (Google, 2026-04-28); governance row of the matrix updated.
- 2026-10-18, `aaif-structure`: hosted projects listed.
- 2026-10-15, `dif-trusted-ai-agents`: org corrected to Linux Foundation, reported by a DIF participant on the AAIF Taxonomy list.
- 2026-10-15, CONTRIBUTING and issue template: proposals now state the proposer's role and any employer or commercial interest.
- 2026-10-15, header: the citable version and the date of the live site are shown separately.

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

---

<a id="part-intro"></a>
# Part 3: Introduction

After the W3C/GS1 workshop in Zurich, the question I kept hearing was not what to build but where it was already being built. Agentic commerce is being standardised in more than a dozen venues at once, at different speeds and with different rules; this map records what each of them has published and committed to, with dates and sources, and nothing else.

It is written for people who work in one or two of these venues and need a reliable picture of the others. It takes no position on which approach is right: where two efforts overlap or leave a gap, the map says so and stops there.

The map is made by a participant in some of the venues it maps. Seams S1 to S4 each touch at least one venue in which the author took part, and S4 in particular follows questions the author has raised in those venues; the Disclosure lists each contribution.

The quickest way in is the four seams. Each follows one question across all venues: how an agent finds a seller, a product or a service; how it knows who stands behind them; how an agent shows who it acts for; and what gets signed, by whom. The payment comparison comes next, and the calendar of the next 60 days is at the end. The entries are reference material, and the appendices show what was read and what was not.

I am an independent researcher, and I have taken part in some of these venues. The Disclosure that follows lists where, and the entries concerned say so. Corrections are welcome and will be dated.

Francesco Marinoni Moretto

---

<a id="part-disclosure-short"></a>
# Part 4: Disclosure (short)

The author of this map, Francesco Marinoni Moretto, has the following public interests and has taken part in several of the venues mapped. The full table of contributions is in the appendix "Full disclosure".

**Interests**

- Book: *Selling to Agents* (Affero Press, ISBN 979-12-82765-00-8), https://sellingtoagents.com/. The Kindle edition is on sale on Amazon since 2026-10-12 (publication date "12 ottobre 2026" on https://www.amazon.it/dp/B0HMS7RZ3N, ASIN B0HMS7RZ3N, read on 2026-10-13).
- Working paper: "Layered Agentic Retrieval" (LAR), SSRN, https://doi.org/10.2139/ssrn.6801118. It is a publisher-side proposal related to seam S1 (discovery layers) and to position statement #14 at the W3C/GS1 workshop.
- Census of agentic surfaces: "Agentic surface census, 19 September 2026", Zenodo, https://doi.org/10.5281/zenodo.22893539; tool: https://github.com/frmoretto/ucp-probe
- Atlas for Agents, a measurement of Italian accommodation (Puglia): https://atlasforagents.com/
- Public repository frmoretto/shopify-dev-mcp-changelog (release notes for @shopify/dev-mcp, see entry `shopify`): https://github.com/frmoretto/shopify-dev-mcp-changelog
- Independent advisory activity.
- Speaker at AGNTCon 2026 (San Jose), 2026-10-23, with the talk "Reading is Free, Spending is Not: What a Minimal Agent Learns Probing Live Ecommerce Endpoints" (program page read on 2026-10-13): https://events.linuxfoundation.org/agntcon-mcpcon-north-america/program/schedule/

**Participation** (entries and seams affected)

- W3C/GS1 workshop, position statement #14 and two pull requests: entry `w3c-gs1-ecommerce-workshop`; seam S2.
- W3C Agentic Web charter draft, PR #888: entry `w3c-agenticweb-wg`.
- W3C DID Resolution, PR #344: entry `w3c-did-resolution`; seam S2.
- Universal Commerce Protocol, issues, discussions and pull requests: entry `ucp`; seams S1, S2 and S4, and the section on free text against structured data.
- schema.org, issue #4928: entry `schemaorg-open-agent-commerce-items`; seam S2.
- A2A, issue #2276: entry `a2a-discovery`; seam S1.
- ARD and Lighthouse (issues #17251 and #17271, PRs #17260 and #17272, ARD PR #100, merged): entry `ard`; seam S1.
- AI Catalog, one comment on PR #117: entry `lf-ai-catalog`; seam S1.
- IETF DAWN list: entry `ietf-dawn`; seam S1.
- IETF Web Bot Auth, crawler best practices (cbcp): entry `ietf-webbotauth`; seam S3.
- IETF AUDIT list and architecture draft issue #35: entry `ietf-audit`; seams S4 and the closing section on what is not established.
- IETF vcon list, two messages, and PR #41 on the charter text: entry `ietf-vcon`; seam S4.
- AAIF Agentic Commerce Working Group, two messages on the working group list (12 October, 06:23 UTC, and 14 October, 15:22 UTC) and a presentation given at the call of 14 October: entry `aaif-wg-agentic-commerce`; seam S4.
- Shopify AI Toolkit, issue #62: entry `shopify`.
- IETF AUDIT: the lead editor of the expected-record draft stated on 2026-10-08 that the author will be named as a contributor for case 7 (see the full disclosure): entry `ietf-audit`.

---

<a id="part-status"></a>
# Part 5: Core entries: status

| Org | Item | State (as of) | Next dated item |
|---|---|---|---|
| W3C | [W3C AI Agent Protocol Community Group](#w3c-ai-agent-protocol-cg) | Active Community Group (created 2025-05-08); agent identity is DID-method-agnostic (did:wba, did:web, did:webvh) since 2026-08-13. Bi-weekly meetings; the meeting of 2026-10-07 was announced as canceled (calendar notice of 2026-10-01) and the October 2026 list archive holds 5 messages, the last of 2026-10-07, none announcing a later meeting (read 2026-10-13); the W3C group data list two chairs. (2026-10-13) | - |
| W3C | [W3C Agentic Web Working Group (draft charter)](#w3c-agenticweb-wg) | Draft charter for a proposed Working Group, in refinement until approx. 2026-11-10 (W3C Team estimate, public-new-work). On 2026-10-13 the last change to the charter text is still the commit of 2026-09-30 (a definition of the term and a simplified scope), and the Strategy issue #576 is open with 4 comments, the last of 2026-10-01. (2026-10-13) | approx. 2026-11-10 |
| W3C | [W3C DID Resolution](#w3c-did-resolution) | Candidate Recommendation Snapshot 2026-08-06; current Candidate Recommendation Draft 2026-10-01 (also 2026-08-28), which marks the Decentralized Identifier (DID) URL dereferencing feature and sections 5, 6, 8 and 10 as at risk. The exclusion opportunity on the Patent Review Draft ended on 2026-10-05. PR #344, "full pass at DID URL dereferencing algorithm (isolated)", was merged into main on 2026-10-13 at 02:10 UTC (merge commit 0956c93). The W3C publication history read on 2026-10-13 still lists the Candidate Recommendation Draft of 1 October 2026 as the latest, so no draft has been published after the merge; the merged text was not read for the at-risk markings. At the DID Working Group (WG) call of 2026-10-08 (minutes at w3.org/2026/10/08-did-minutes.html, read 2026-10-13) a chair ran the poll "PROPOSAL: Merge PR344 and agree that any future improvements to the DID URL Dereferencing Algorithm should be handled as separate issues.": eight participants recorded +1 and one recorded -1, "some technical issues not sufficiently discussed, charter violation, process violation, breaks compatibilty with DID 1.0 and CID". The chair then said "by Chair's decision, we will be merging this PR" and asked that the technical points be raised as separate issues; the merge followed on 2026-10-13. The minutes do not record the poll as a resolution. The PR comments of 2026-10-08 record the same dissent, that the changes violate the WG charter, and the chairs' answer that they do not. The statement of 2026-10-06 that unresolved points of the PR would be run as proposals so that objections can be recorded was followed by this single poll; separate issues for the points of the -1 were not looked for one by one on 2026-10-13. (2026-10-13) | - |
| W3C | [W3C TPAC 2026 breakouts on agents (Dublin, 2026-10-26/30)](#w3c-tpac-2026) | Technical Plenary and Advisory Committee (TPAC) 2026 takes place 2026-10-26 to 2026-10-30 in Dublin (hybrid). The deadline for breakout proposals to be scheduled in advance was 2026-10-08 and has passed; the README (read 2026-10-13) says that "Around 19 October" the schedule of the breakout sessions for Monday to Wednesday is added to the TPAC calendar, and the calendar page of breakout sessions listed no session in its text on 2026-10-13. On 2026-10-14 (09:35 UTC) that page lists 85 sessions, all marked "Tentative", each with a day, a time shown in Greenwich Mean Time and a room. (2026-10-14) | approx. 2026-10-19 |
| W3C | [W3C/GS1 Workshop on E-commerce for Humans and AI Agents (Zurich, 8-9 Sep 2026)](#w3c-gs1-ecommerce-workshop) | Workshop held 2026-09-08/09 at Google Zurich, co-organised by W3C and GS1. A report and follow-up session is proposed for Technical Plenary and Advisory Committee (TPAC) 2026 (breakout #34, open on 2026-10-13 with one comment and no assigned slot). A workshop report: not found in the root of the workshop repository nor in its commits (the last push is of 2026-09-09), read 2026-10-13. (2026-10-13) | - |
| IETF | [IETF AI Preferences (aipref WG)](#ietf-aipref) | The vocabulary draft is at -08 (2026-09-13 in the datatracker history) and the attach draft was last seen at -05 (2026-08-19). A virtual interim meeting is announced for 2026-10-21. On 2026-10-13 the datatracker record gives revision 08 of the vocabulary draft (time 2026-09-14 06:18 UTC) and revision 05 of the attach draft (2026-08-19), no later revision; the interim announcement was not rechecked. (2026-10-13) | 2026-10-21 |
| IETF | [IETF AUDIT (BoF preparation)](#ietf-audit) | Charter text under discussion on the audit list and in mirjak/audit-bof-preparation; the BoF request lists "User e-commerce use case" in its proposed agenda (file updated 2026-09-18). On 2026-10-05 and 2026-10-06 participants agreed in words on the sentence "VCON is considered a suitable record format and the audit group will work with the vcon group to ensure the specified format addresses the auditing"; pull request #61 (one commit, 009b915) was still open on 2026-10-08 and does not contain that sentence. On 2026-10-13 the datatracker group page of audit shows the state Birds of a Feather (BOF) and no charter; a name search for expected-records finds no draft (not found on the datatracker, 2026-10-13), although a list message of 2026-10-10 refers to draft-ahuja-schrock-audit-expected-records-00. On 2026-10-10 a BoF proponent wrote on the list to a participant who had asked for a presentation slot "I am not the chair of the BoF meeting. The chairs will be selected by the ADs." and that the BoF agenda "will not be based on an open call for presentation". Pull request #61 was still open on 2026-10-13 (3 comments, last update 2026-10-06) and the repository mirjak/audit-bof-preparation has no commit after 2026-09-18. (2026-10-13) | - |
| IETF | [IETF DAWN, Discovery of Agents With Names (proposed WG)](#ietf-dawn) | Charter 00-10 has been in external review since 2026-10-09, with comments to the Internet Engineering Steering Group (IESG) due by 2026-10-19 and an IESG telechat listed for 2026-10-22; the Working Group (WG) is "Proposed", and the WG Review announcement of 2026-10-09 says "The IESG has not made any determination yet". The Approve ballot on 00-10, read on the datatracker on 2026-10-14, carries the summary "Has enough positions to pass." with one Yes and one No Objection recorded; the charter has not been recorded as approved, and no WG Action announcement for DAWN is found among the ietf-announce messages up to 2026-10-12 (read 2026-10-13). The announcement names the chairs of the proposed WG: Adrian Farrel and Wes Hardaker. Earlier history: charter 00-09 was on the IESG ballot: on 2026-10-06 one IESG member changed from Block (on 00-08) to No Objection and another voted Yes; on 2026-10-07 one member voted Yes with comments and three recorded No Objection; on 2026-10-08 two more recorded No Objection; the IESG telechat had been set for 2026-10-08. On 2026-10-09 the charter was revised to 00-10 and sent to external review: the datatracker history of that day shows the state changed from "Start Chartering/Rechartering (Internal Steering Group/IAB Review)" to "External Review (Message to Community, Selected by Secretariat)", the "Ready for external review" ballot closed, an "Approve" ballot created and the telechat date changed from 2026-10-08 to 2026-10-22; one IESG member recorded Yes on the new ballot on 2026-10-12. The datatracker pages read on 2026-10-13 show the WG as "Proposed" and charter-ietf-dawn-00-10 in that state, with "On agenda of 2026-10-22 IESG telechat". The Secretariat's announcement "WG Review: Discovery of Agents With Names (dawn)", sent to ietf-announce on 2026-10-09, says "The IESG has not made any determination yet" and asks for comments to the IESG mailing list by 2026-10-19. No WG Action announcement for DAWN is among the ietf-announce messages up to 2026-10-12, the latest of the list on 2026-10-13; a decision on DAWN is not found. (2026-10-14) | 2026-10-19 |
| IETF | [IETF Web Bot Auth (webbotauth WG)](#ietf-webbotauth) | Active Working Group (WG), listed for coordination by the draft W3C Agentic Web charter; the first WG draft, draft-ietf-webbotauth-httpsig-protocol-00, was adopted on 2026-09-01, and a two-hour session was requested for IETF 127 on 2026-09-15. Implementation reports and proposed edits to the draft were on the list between 2026-10-04 and 2026-10-13. On 2026-10-13 the datatracker still lists draft-ietf-webbotauth-httpsig-protocol-00 (2026-09-01) as the only WG draft, and draft-illyes-webbotauth-cbcp-00 (2026-04-21, expires 23 October 2026) with no later revision. In the thread on updates to the crawler best practices draft a participant posted a revised text proposal on 2026-10-12 for a distinct Signature-Agent URL, key and key directory per crawler purpose, with pull requests in the WG draft repository and as PR #23 of garyillyes/cbcp (open, last update 2026-10-12); PR #22 of the same repository is open (3 comments, last update 2026-10-11). The IETF 127 session is still recorded as requested: no scheduling is found in the list subjects to 2026-10-13. (2026-10-13) | - |
| IETF | [IETF agentproto (Agent Communication Protocols WG)](#ietf-agentproto) | The Internet Engineering Steering Group (IESG) announced on 2026-10-08, 16:55 UTC, "A new IETF WG has been formed in the Applications and Real-Time Area" for Agent Communication Protocols (agentproto), chairs Orie Steele and Leslie Daigle, and names the responsible Area Director. The datatracker page read on 2026-10-09 shows charter-ietf-agentproto-01, state "Approved", Working Group (WG) state "Active", area Applications and Real-Time Area (art), last updated 2026-10-08, and its history records "Charter approved, group active" on 2026-10-08. Reading of 2026-10-13: the datatracker charter page is still headed "Agent Communication Protocols (agentproto) Proposed Charter" while its state is Approved and the group is Active (charter-ietf-agentproto-01, last updated 2026-10-08). The related drafts page lists 15 drafts, among them draft-agentic-ai-usecases-requirements-03 (posted 2026-10-10) and draft-rosenberg-agentproto-usecases-00 (2026-07-04); a revision -04 of the first is not found there. The chairs wrote on the list on 2026-10-12 that "Our goal for this topic is to identify candidate starting points for the Use Cases and Requirements document.", that the discussion "identified two drafts for consideration" (those two) and that "We have useful contributions toward a working group document, but have not yet established which draft should be its starting point." In the same thread an author of the -03 draft proposed, for a -04, the requirements B1-7 (checks on resumption) and B1-8 ("If any check in B1-7 fails or cannot be completed, the dialog is not resumed and the protocol is required to signal the reason."), and CMN-12 ("Before accepting a change to a dialog, a participant is required to be able to verify that the change is authorized at that time."); on 2026-10-13 the same author agreed to add to Section 4.2 "If the outcome cannot be determined, the operation remains unresolved, and resuming the dialog alone does not justify resending it." (proposed text read as quoted in the chairs' message and in the reply). On 2026-10-12 a chair answered a thread on implementation evidence with "Please refrain from sending messages regarding implementations at this time." A session request for agentproto at IETF 127 exists in the datatracker (requested duration 2:00:00, last modified 2026-10-08); no timeslot assignment for it is found in the agenda schedule of the meeting (API, 2026-10-13). (2026-10-13) | 2026-12-31 |
| IETF | [IETF vcon (Virtualized Conversations WG)](#ietf-vcon) | Active working group in the Applications and Real-Time Area, charter-ietf-vcon-01 approved (last updated 2026-03-18); its core draft, draft-ietf-vcon-vcon-core-04 (Standards Track), is dated 2026-09-07. The datatracker lists four charter milestones, dated 2023-12-31 (adopt two drafts) and 2024-06-30 (submit them to the Internet Engineering Steering Group (IESG)), and shows no completion state. The virtual interim of 2026-10-08 (14:00 to 16:00 UTC) was held; the editor's message after it is quoted below. Minutes of that interim: not found in the latest 40 messages of the vcon list (to 2026-10-11), read 2026-10-13; the datatracker interim materials were not read. On 2026-10-13 the datatracker still shows draft-ietf-vcon-vcon-core-04 as the current revision and charter-ietf-vcon-01 as approved. The next virtual interim is on 2026-10-22. Recharter state, 2026-10-13: the datatracker history of the charter shows no revision after charter-ietf-vcon-01 (last action 2026-03-18, a change of Area Director); the recharter text exists only in the repository file changed by PR #37 (merged 2026-10-08) and is not an approved charter. PR #41 on that file is open with no comments. Issue #40 of the core draft repository (opened 2026-10-10 by a participant, no comments) quotes section 2.4 of -04, "Objects that refer to a file which is externally stored from the vCon MUST have the parameters: url, content_hash", and says that references to a streaming-service page or to a recording behind a login cannot be hashed; it reports, as its own measurement on a public dataset, that 4,079 of 8,181 containers fail the schema on that one finding (a figure declared by the issue author, not re-run here). (2026-10-13) | 2026-10-22 |
| IETF | [Individual IETF drafts on the seller side](#ietf-individual-seller-drafts) | Three individual Internet-Drafts on the seller side of agent transactions, none adopted by a Working Group (WG): anders merchant-identity-assertions -01, kavian offering-discovery-protocol -01, hood agtp-merchant-identity (-02, an Independent Submission dated 26 May 2026, Informational, expires 27 November 2026; -00 and -02 read). (2026-10-13) | - |
| GS1 | [GS1-Conformant Resolver Standard 1.2.1](#gs1-conformant-resolver) | Release 1.2.1 ratified August 2026 (standards page and PDF print no day); the archive page on ref.gs1.org lists "Published 19 August 2026". (2026-10-13) | - |
| UN/CEFACT | [UN Transparency Protocol, Identity Resolver](#untp-identity-resolver) | Latest stable version 0.7.0 (GitLab tag of 2026-05-04); the 0.7.0 page says the team "expects to release UNTP version 1.0", without a date. (2026-10-13) | - |
| Other standards bodies | [CEN/CENELEC JTC 24 Digital Product Passport standards (EN 18216 to EN 18246)](#cen-clc-jtc24-dpp) | Eight horizontal standards; six cited in the Official Journal of the EU according to the CEN-CENELEC page of 2026-07-15 (page re-read on 2026-10-13, unchanged); the two not cited are EN 18239 and EN 18246, and their status is not read. The Official Journal itself was not read: EUR-Lex answered HTTP 202 without content on 2026-10-13. (2026-10-13) | - |
| AAIF | [A2A protocol, agent discovery](#a2a-discovery) | A2A registers /.well-known/agent-card.json for a single AgentCard; proposals for hosts serving several agents (PR #2240, issues #2276 and #2248) were open on 2026-10-13: PR #2240 and issue #2248 have no comment, and issue #2276 has no comment after 2026-10-02. (2026-10-13) | - |
| AAIF | [AAIF Agentic Commerce Working Group](#aaif-wg-agentic-commerce) | Charter approved 2026-05-15; Capability Map being built from contributed inputs. Charter targets: Capability Map (2026-09-01) and Recommendations to the Technical Committee on hosted projects (2026-10-01); both dates have passed, and no Capability Map or Recommendations document is found in the repository on 2026-10-13 (root: README.md, charter.md, reporting/; commits to 2026-10-12). Chairs per the August report: Ilya Grigorik (Shopify) and Rahul Bansal (OpenAI). The August report (merged by PR #7 on 2026-10-12) says the x402 session "advanced the payment layer of the Capability Map" and lists no decision needed from the Technical Committee; the report for September is opened as issue #9 (2026-10-12), covering deep dives on onX, MPP and the UCP August release. (2026-10-13) | - |
| AAIF | [MCP Server Cards (ext-server-card, SEP-2127)](#mcp-server-card) | Experimental extension of MCP: the README of the extension repository still reads "not an accepted or official MCP extension" (2026-10-13). SEP-2127 (PR #2127, "MCP Server Cards - HTTP Server Discovery", Extensions Track) was merged on 2026-10-06 (14:43 UTC, merge commit 0a11bf6) by a maintainer of the MCP repository; the Specification Enhancement Proposal (SEP) file, read 2026-10-13, carries "Status: Final" and says the full extension specification stays in the extension repository, graduating to a repository named ext-server-card on acceptance. The last commit of the extension repository on main is of 2026-08-12 (PR #47); latest activity read: issue #30 (2026-10-10, 9 comments). (2026-10-13) | - |
| Linux Foundation | [AI Catalog (Agent Card Working Group)](#lf-ai-catalog) | Pre-v1 specification in "a temporary working repo maintained by the Linux Foundation", governed by a Technical Steering Committee with four initial seats. The well-known path is optional by design (ADR-0011). On 2026-10-13 the README of main still says "This is a temporary working repo maintained by the Linux Foundation" and "This project will be moved to a permanent location a later date with a permanent governance model."; the last commit of main is of 2026-10-08 (PR #119, implementation classifications); issue #46 (project location) was closed as completed on 2026-10-03 without a comment. PR #110 (did:web verification of signed Entry Trust Manifests) was merged on 2026-10-01. (2026-10-13) | - |
| Linux Foundation | [x402](#x402) | Open payment protocol under the x402 Foundation (Linux Foundation): intent announced 2026-04-02; operational launch and completed contribution by Coinbase announced 2026-07-14, with 40 member organisations at launch. On 2026-10-13 main is at commit 6c470a8 and the core specification header reads "Protocol Version: 2" (specs/x402-specification-v2.md); no release is listed on GitHub (not found, 2026-10-13). The file ROADMAP.md, which read "(update coming soon)" on 2026-10-03, was removed from main on 2026-10-13 by PR #3789, "chore: remove outdated ROADMAP.md and PROJECT-IDEAS.md". (2026-10-13) | - |
| Independent | [Agentic Resource Discovery (ARD)](#ard) | Specification v0.91 on main (header "Status: Proposal", dated 2026-08-26; header unchanged and last change to spec/ard.md on 2026-10-12, read 2026-10-13); no tag or release in ard-spec (not found, 2026-10-13); Maintainers decide by majority vote; an Oversight Board (Google, Hugging Face, Microsoft, Amazon, Cisco) is published. On 2026-10-11 and 2026-10-12 the maintainers merged PRs #97, #99, #104, #105, #106 and #80 (namespace segments in Appendix C, base URL and search endpoint in section 5.3, ADR 0010, recognized media types in section 3.3, CDDL for explore facets, attestation scopes in section 4.5.2). (2026-10-13) | - |
| Independent | [Browser vendor positions on WebMCP (WebKit, Mozilla, Chrome, Edge)](#browsers-webmcp) | WebKit position issue #670 closed 2026-06-11 as "position: oppose"; Mozilla #1412 closed 2026-08-05 as "position: neutral". Chrome early preview 2026-02-10; Edge blog of 2026-09-21: implementation "is ready for testing". (2026-10-13) | - |
| Independent | [schema.org open issues relevant to agents, bookings, product and establishment identity](#schemaorg-open-agent-commerce-items) | Issues #4824, #4786, #4828, #4774 and #4928 were open on 2026-10-13 (issue #4928, 1 comment, last activity 2026-10-08). The Digital Product Passport vocabulary (PR #4871, merged 2026-08-17) is the file data/ext/pending/issue-4870.ttl on main as read on 2026-10-03; the release notes of V30.1 (2026-09-16) read "Add vocabulary to support discovery of EU Digital Product Passports" and attribute to PR #4871 the class DigitalProductPassport and the property hasDigitalProductPassport for use on Product and Offer (release notes read 2026-10-14), and the term page schema.org/hasDigitalProductPassport exists (2026-10-13). (2026-10-13) | - |
| Industry | [Agent Payments Protocol (AP2)](#ap2) | Donated by Google to the FIDO Alliance on 2026-04-28 (Google: "We’re donating Agent Payments Protocol to the FIDO Alliance"); standardisation continues in the FIDO Payments and Agentic Authentication Technical Working Groups. The reference repository stays in the GitHub organisation google-agentic-commerce (Apache-2.0); latest release v0.2.0 of 2026-04-28, which "focuses on providing Human Not Present flows". (2026-10-18) | - |
| Industry | [Agentic Commerce Protocol (ACP)](#acp) | Specification in beta, maintained by OpenAI and Stripe; MAINTAINERS.md also lists Meta (PR #236 "ADMIN: Add Meta as TSC member", merged 2026-04-24). Last dated version 2026-04-17; on 2026-10-13 main is still at commit 7fdd78d (2026-07-17), README badge "Beta", no tag or release (not found, 2026-10-13), and the directory spec/unreleased holds the changes not yet dated (checkout, cart, delegate, feed schemas and OpenAPI files). (2026-10-13) | - |
| Industry | [EMV Agentic Payments Framework for Specifications (draft for public feedback)](#emvco-agentic-payments-framework) | Draft published for feedback on 2026-09-01; the comment period ended on 2026-09-30. On 2026-10-13 the EMVCo news list has no item on the outcome of the comment period; the newsletter Q3 2026 (2026-10-09) still calls it a draft and says it was published "to provide a foundation for further industry engagement and potential specification development"; no final version or new draft is found (EMVCo news list and resource page, 2026-10-13). (2026-10-13) | - |
| Industry | [KYAPay (Skyfire)](#kyapay) | Individual Internet-Drafts named for the OAuth Working Group (WG) (draft-skyfire-oauth-*); WG stream or adoption: not found on the datatracker, 2026-10-13 (the pages of kyapay-token and using-kyapay-tokens show "(No stream defined)"). On 2026-10-02 the author announced new revisions of five drafts: kyapay-token-02, using-kyapay-tokens-01, amr-values-02, id-verification-02 and aml-methods-01 (datatracker date 2026-10-01 for all five). The datatracker lists two more documents of the family, kyapay-token-exchange-01 (2026-07-19) and kyapayprofile-02 (2026-06-20, replaced by kyapay-token), seven in all. The Technical Plenary and Advisory Committee (TPAC) breakout proposal #39 (KYAPay: Verified Agent Identity and Payments for Ubiquitous Agentic Commerce) is open on 2026-10-13 with one comment and no assigned slot; the datatracker shows no revision of kyapay-token-exchange after -01 of 2026-07-19. (2026-10-13) | - |
| Industry | [Mastercard Agent Pay](#mastercard-agent-pay) | Commercial programme of Mastercard for agent-initiated payments, described on its framework page (read in a browser on 2026-10-14; first read 2026-10-02). Page metadata: datePublished 2025-10-14, dateModified 2025-11-04. The page introduces the Mastercard Agent Pay Acceptance Framework: registration and verification of agents before they transact with agentic tokens, Web Bot Auth at the content delivery network (CDN) layer, and a Dynamic Token Verification Code, an agentic token formatted for standard card payment fields, submitted in existing checkout forms. The page refers to developer.mastercard.com for use cases; that site was not read. (2026-10-14) | - |
| Industry | [Personal Agent Consent & Trust Protocol (PACT), published by Decagon with Instinct](#pact) | Version 1.0 of the specification ("This is PACT 1.0.") is published at openpactprotocol.org (the Decagon announcement is dated 2026-10-06), and the repository openpactprotocol/openpactprotocol (created 2026-10-01, Apache-2.0) holds the documentation, a reference Provider, a demo personal agent and conformance tests; its latest commit on main is 838c6bd (2026-10-06, a dependency update), read 2026-10-13. Decagon, 2026-10-06: it is open-sourcing PACT, "co-developed and supported by Instinct". No standards body or governing organisation is named in the pages of the site read on 2026-10-13. (2026-10-13) | - |
| Industry | [Personal Agent Protocol (PAP, "Poppy"), published by Sierra with Meta](#pap) | Draft 0.1 of the specification is published at personalagentprotocol.org (announced 2026-10-06, draft published 2026-10-09; the pages read on 2026-10-13 are marked "Updated Oct 12, 2026"), under the Apache License 2.0 with the names and the logo excluded; a further 35 design partners were named on 2026-10-09. Governance is worded two ways, not reconciled here. Sierra, 2026-10-06: "an open standard Meta and Sierra are developing along with industry partners at Genesys, Instinct, Rocket, Shopify, Stripe, and Walmart". Decagon, 2026-10-06: "join the Personal Agent Protocol working group announced by the team behind Meta's Muse to help shape an industry standard". No standards body or governing organisation is named in the pages of the site read on 2026-10-13. (2026-10-13) | approx. 2026-11-09 |
| Industry | [Universal Commerce Protocol (UCP)](#ucp) | Latest GitHub release v2026-08-25 (2026-08-25); lodging booking draft merged 2026-09-24 (PR #780); the Common capability `ask` merged 2026-10-07 (PR #538); feed and subscription policy in draft (PR #866, PR #890); the food checkout proposal (PR #897) is under review (open on 2026-10-13). On 2026-10-13 main is at commit 9756aa9 (2026-10-12) and no release is listed after v2026-08-25. Governance and extension items filed 2026-10-09 to 2026-10-11, read 2026-10-13: issue #922 "[DTC Charter]: Local Services" (DTC: Domain Tech Council; labels Triage and gov:needs-gc-review, no comments) proposes a Domain Tech Council for appointments, group sessions, reservations and rentals, defined by "real-time slot computation over staff and resource calendars, with holds", leaves lodging, food, payments and shopping to the councils that own them, and says of three earlier proposals (#317, #303, #479) that "none has a home council"; the platform it lists is "Meta" and the businesses are "Wix, Housecall Pro, Squarespace, Jobber, HoneyBook, Stripe, Shopify". Issue #924 "Domain Working Group (DWG) Charter: Agentic Donations" (same labels, no comments) names the Shopping Tech Council as sponsor and a proposed chair from Stripe, asks for nominations by "October 23, 2026" and targets "November 2, 2026" for the initial package; "Merged PRs and production launches are not required for the DWG to close." It mentions the Donor Agent Protocol of GoFundMe, whose site gofundme.github.io/donor-agent (read 2026-10-13) is headed "Donor Agent Protocol (DAP) v0.1" and "An Evidence-First Donation Layer"; a repository for it is not found (gofundme/donor-agent, HTTP 404, 2026-10-13). Issue #929 (opened 2026-10-11, one comment besides the author's) proposes the extension dev.ucp.common.quote, described as "a one-quotation-at-a-time loop, not a negotiation protocol", with draft PR #930 as reference implementation ("not requesting merge before #929 reaches Provisional"); an accepted quotation appears in totals and on the Order as the quotation id and its subtotal only. A comment of 2026-10-11 calls it "a useful candidate for the narrower case of a Business-issued, price-only quotation accepted by reference into Cart/Checkout". PR #933 (open, one commit, 2026-10-11) says it "spells out which redirect codes are actually banned (301/302/303/307/308) and says 304 is fine, on both the hosting and fetching side"; PR #932, which proposed the same clarification, was closed on 2026-10-11, two minutes after it was opened, by the account that opened it. PR #897 (food) is still open on 2026-10-13 (head 1e2818c). Discussion #931 (2026-10-11, no comments) asks whether ucp.dev could list community implementations and names one open-source implementation, Portage, described there as an MIT-licensed agent command-line interface and a set of merchant-side Ruby gems; it is noted here and not evaluated. The Shopify/hydrogen pull request #4158 on the UCP profile route is open, not merged (2026-10-13), and is not counted. (2026-10-14) | 2026-10-23 |
| Industry | [Verifiable Intent](#verifiable-intent) | Draft v0.1 specification, maintained by Mastercard according to its README (Apache-2.0, tag v0.1.0). The FIDO Alliance release of 2026-04-28 says Mastercard has contributed it to the Payments Technical Working Group. On 2026-10-13 the last commit on main is of 2026-04-20 (356c296, PR #23), v0.1.0 is the only tag, no release is listed, and the README header reads "Draft (v0.1). Maintained by Mastercard; open to multi-stakeholder contribution." (2026-10-13) | - |
| Industry | [Visa Trusted Agent Protocol (TAP)](#visa-tap) | Specification and sample code published by Visa under Visa Product Terms of October 10, 2025; the product page, read in a browser on 2026-10-14, still says "This product is in the process of development and deployment." (2026-10-14) | - |

---

<a id="part-seams"></a>
# Part 6: Seams

# Seams

Four places where the entries meet. Each statement comes from the entries named in brackets; negatives are searches of the corpus named in the entry, not statements about the world. The participation of the author of this map in the threads concerned is in the Disclosure.

## S1. Discovery layers
`ard`, `lf-ai-catalog`, `a2a-core`, `a2a-discovery`, `mcp-core`, `mcp-server-card`, `ucp`, `ietf-dawn`, `ietf-dnsaid`, `schemaorg-baseline`, `w3c-ai-agent-protocol-cg`, `pap`, `pact`, `shopify`

- A2A defines the AgentCard as a message in `specification/a2a.proto` and registers `/.well-known/agent-card.json` for a single card (`a2a-core`, `a2a-discovery`).
- MCP Server Cards are a static metadata document with a recommended location of `<url>/server-card`; the extension's discovery document points clients to `/.well-known/ai-catalog.json` for catalogues (`mcp-server-card`).
- AI Catalog uses `/.well-known/ai-catalog.json`; its ADR-0011 says a well-known URI "is not mandatory" (`lf-ai-catalog`).
- ARD uses `/.well-known/ard.json`: "A consumer resolving a domain's entries MUST fetch /.well-known/ard.json"; the AI Catalog path is its predecessor, which a publisher "SHOULD move" away from (`ard`).
- A loose coupling between ARD and AI Catalog is recorded in AI Catalog's ADR-0017 and in ARD PR #70: "Every ARD entry is a well-formed catalog entry, but not every catalog entry is an ARD entry." (`lf-ai-catalog`, `ard`).
- A2A PR #2240 proposes `ai-catalog.json` as the "Preferred" mechanism and issue #2276 proposes `/.well-known/agent-card-list.json`; on 2026-09-01 a maintainer closed PR #418 with "A2A working group will not be building any kind of registry standard." (`a2a-discovery`).
- UCP serves a merchant profile at `/.well-known/ucp`; the charter of its Bulk Product Discovery working group puts business discovery outside and defers it to a future RFC (`ucp`).
- UCP's overview page says "Profile endpoints MUST NOT use redirects (3xx).", while the Personal Agent Protocol says of its own well-known document that "Personal Agents MUST follow redirects" (`pap`): the two rules differ, and they concern different paths and different readers; issue #904 (a third-party scan, figures declared by its author, not verified by this map) lists 301 answers at the manifest path of two Shopify stores among the 13 without a parsable manifest (`ucp`).
- Version 3 of the reporting frame in UCP Discussion #867 (posted 2026-10-09 by the author of this map, comment 18833761) counts a 3xx at the profile path on its own line, since "a profile reached only via a 3xx is never a positive", and reports a "200 after redirect" apart as row 1a; it ties both to the two rules of the overview page, Hosting item 2 (line 1466) and identity resolution item 2 (line 1514), at commit f2206e6; the author of the census answered the same day (comment 18834311) that this is how he will report his next pass (https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18833761; `ucp`).
- Known Good run in Discussion #867 (2026-10-08, figures declared by the source, not verified by this map): 41,424 endpoints answered tools/list, two tool signatures cover 41,352 of them, and the post gives "Merchant count 41,424; decision count 2" (https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18816164; `ucp`).
- The Personal Agent Protocol (draft 0.1, published 2026-10-09) discovers a company through one well-known document: "A Company MUST publish its poppy.json document at https://{domain}/.well-known/poppy.json over HTTPS"; the URL "MAY redirect", and "Personal Agents MUST follow redirects, and every redirect MUST be to an HTTPS URL" (`pap`).
- PACT (version 1.0, Decagon with Instinct) takes the A2A route and not a document of its own: a business's card is at "https://{brandDomain}/.well-known/agent-card.json", which "serves the card or redirects to" the Provider's URL, and the specification says "This spec does not define a registry." Redirects are therefore allowed on the well-known path of both personal-agent protocols (`pact`, `pap`), while the UCP overview says "Profile endpoints MUST NOT use redirects (3xx)." (`ucp`). A personal agent that reaches a business meets `poppy.json` at a Poppy company and `agent-card.json` at a PACT business; neither document is read by the other protocol in the texts read (not found: poppy.json in the PACT specification page, and A2A, PACT and agent-card.json in the Poppy specification page, 2026-10-13).
- Where discovery finds no agent checkout, the README of Shopify/shop (commit d1e8c7c, read 2026-10-13) says: "Some stores have no agent checkout API (UCP); the agent has to enter a payment credential into the site's checkout form in a browser." (`shopify`).
- IETF DAWN would standardise discovery of "public properties of AI resources", with, for the public Internet, the charter example "discover all agents of example.org, for all its customers/members" ("discover all agents in this shop" is the charter example for the local network, charter 00-10, read on the datatracker on 2026-10-14); catalogues of capabilities beyond a minimum are out of its scope (`ietf-dawn`).
- The individual draft DNS-AID (draft-mozleywilliams-dnsop-dnsaid-02) "standardizes an approach for publishing AI agents in the Domain Name System (DNS) so that other agents can discover them" (`ietf-dnsaid`).
- schema.org V30.1 defines the types Organization, LocalBusiness, Product and Offer (`schemaorg-baseline`).
- In the IANA well-known URIs registry (updated 2026-10-07, read 2026-10-14, https://www.iana.org/assignments/well-known-uris/well-known-uris.xml), of the eight discovery paths listed on the home page (`/.well-known/ucp`, `agent-card.json`, schema.org, ARD, AI Catalog, MCP Server Cards, DNS-AID, `/.well-known/poppy.json`) only `agent-card.json` is registered (status permanent, controller Linux Foundation, `a2a-core`); `ucp`, `ai-catalog.json`, `ard.json` and `poppy.json` are not found in it. A registration request for `ucp` has been open in the registry's repository since 2026-06-06 (issue #92, https://github.com/protocol-registries/well-known-uris/issues/92), labelled "waiting for input" since 2026-07-11, when the designated expert asked for an e-mail address for the change controller; no later comment (read 2026-10-14). A request for `poppy.json`, `ard.json` or `ai-catalog.json` is not found among the 108 issues of that repository, all states (read 2026-10-14). The registry also holds `gs1resolver` (permanent, controller GS1, registered 2020-05-18, the path used by the GS1-Conformant Resolver, `gs1-conformant-resolver`), `vacation-rental.json` (provisional, registered 2026-08-19; the record points to vacationrentalprotocol.com, whose author commented on schema.org issue #4824, `schemaorg-open-agent-commerce-items`) and `api-catalog` (RFC 9727, permanent, 2024-12-23), a general mechanism for publishing API catalogs that this map does not count among the agent-specific approaches.
- KYAPay token-02 (section 7.3) asks IANA to register the well-known URI suffix `jwks.json` (status permanent) for the key set of a token issuer (`kyapay`); `jwks.json` is not found in the registry read on 2026-10-14.
- The draft W3C Agentic Web charter is in refinement; strategy#576 lists four AI-related community groups for outreach, the AI Agent Protocol CG among them (`w3c-agenticweb-wg`, `w3c-ai-agent-protocol-cg`).
- Two individual IETF drafts survey or analyse discovery mechanisms, draft-jimenez-dawn-discovery-landscape-00 (2026-07-03) and draft-moussa-dawn-gap-analysis-01 (2026-06-12); a text search of both finds no occurrence of AI Catalog, ARD, UCP or commerce (2026-10-06). A DAWN use-case draft names ARD as "an illustrative option" (`ietf-dawn`).

## S2. Product and seller identity
`schemaorg-baseline`, `schemaorg-open-agent-commerce-items`, `gs1-digital-link`, `gs1-conformant-resolver`, `untp-identity-resolver`, `un-gtr-urn`, `w3c-gs1-ecommerce-workshop`, `w3c-did-resolution`, `lf-ai-catalog`, `ucp`, `acp`, `x402`

- schema.org V30.1 (2026-09-16) has Product, Offer, Organization, LocalBusiness, LodgingBusiness, MerchantReturnPolicy and the property `gtin` (`schemaorg-baseline`). Open items on agents and commerce are in the Open proposals appendix (`schemaorg-open-agent-commerce-items`).
- A GS1 Digital Link URI carries a primary key such as a GTIN or a GLN and "is a particular form of URL" (`gs1-digital-link`); the GS1-Conformant Resolver 1.2.1 resolves it to information sources (`gs1-conformant-resolver`).
- The UNTP Identity Resolver 0.7.0 specifies a link resolver service with an OpenAPI artefact; the `gtr` URN namespace is described as "IANA registration pending" (`untp-identity-resolver`, `un-gtr-urn`).
- W3C DID Resolution uses the `relativeRef` parameter for product-level references such as Digital Product Passports; PR #344, which rewrites DID URL dereferencing, was merged on 2026-10-13 (02:10 UTC) after a poll of the DID WG on 2026-10-08 (eight +1, one -1, chair's decision to merge), and the latest Candidate Recommendation Draft, of 2026-10-01, marks that feature as at risk; no draft had been published after the merge on 2026-10-13 (`w3c-did-resolution`).
- The W3C/GS1 workshop of 2026-09-08/09 collected position statements; Sven Böckelmann, author of position statement #31, says "Resolution says where the data is; a signature says who signed it. Neither says who may speak for the product." His workshop slides reduce it to three checks: "Where. Who signed. Who may." (slide 6) (`w3c-gs1-ecommerce-workshop`).
- UCP carries barcodes on catalogue variants, and issue #375 declined external place identifiers in the core schema (`ucp`). ACP's product feed (unreleased) has an optional barcode with a type (GTIN, UPC or EAN) and a value (`acp`). A text search of the x402 issues and pull requests (2026-10-03) returns no occurrence of GTIN, GS1, UPC or EAN (`x402`).
- Seller identity: ACP's discovery RFC says "Seller identity is established through authentication (Bearer token), which is unavailable at discovery time."; AI Catalog uses `urn:air` anchored to a domain and `did:web` verification, and says "This establishes publisher-domain control, not publisher reputation." (`acp`, `lf-ai-catalog`).
- UCP pull request #811 (open, 2026-10-09) would let a catalog variant carry `offers[]`, each naming its seller by `seller.domain`, described as "The seller's canonical host: a bare hostname without scheme, path, port, or trailing slash" that "A Platform resolves ... to the seller's UCP profile at `/.well-known/ucp`"; the overview page says "Profile endpoints MUST NOT use redirects (3xx)." (line 1466), and which of the bare and the www host is canonical for a profile is not found in the overview page at f2206e6 nor in the five files of the pull request (2026-10-09; https://github.com/Universal-Commerce-Protocol/ucp/pull/811; `ucp`).

How the two resolver specifications state the "no data" case (`gs1-conformant-resolver`, `untp-identity-resolver`):

| | GS1-Conformant Resolver 1.2.1 | UNTP Identity Resolver 0.7.0 |
|---|---|---|
| Valid URI, no information | "SHALL return a simple 404 Not Found response" | OpenAPI defines 404, "No link resolver entry found for this identifier."; the prose names the case "When there is no data for the requested entity ID." |
| Invalid URI | "SHALL respond with an HTTP response code of 400 (Bad Request)" | OpenAPI defines 400 for a path that does not match the registered scheme patterns |
| 200 for an error | "SHALL NOT use a 200 OK response code" | not found in the pages read, 2026-10-03 |

## S3. Agent identity and delegation
`ietf-webbotauth`, `visa-tap`, `mastercard-agent-pay`, `kyapay`, `ucp`, `x402`, `acp`, `ietf-agentproto`, `w3c-agenticweb-wg`, `browsers-webmcp`, `w3c-webmcp-cg-report`, `oidf-authzen-agents`, `pap`, `pact`

- IETF Web Bot Auth standardises cryptographic authentication of automated clients (HTTP message signatures, key directories); the first WG draft was adopted on 2026-09-01 (`ietf-webbotauth`).
- Web Bot Auth list, 2026-10-04 to 2026-10-08: an implementer withdraws an agent by emptying its key directory and asks that honouring Cache-Control become a normative SHOULD, a verifier proposes the text, and a second participant writes that for a key set passed on as a signed artifact the bound is the signature's expires and not the cache lifetime; another participant proposes distinct Signature-Agent values for distinct purposes, which two others support; a participant's HTTP linter emits signatures only when challenged, and text on Accept-Signature is proposed for section 5.3 (`ietf-webbotauth`).
- The Personal Agent Protocol's session "is built on OAuth" and the customer decides whether the agent has read-only or write access (`pap`).
- Identity and permission are separate objects in the two personal-agent protocols, in different words. Poppy: "A Personal Agent's client_id MUST be an HTTPS URL that returns its metadata document" (identity, section 4.1), while the access token is "signed in with the account scopes the User granted" (`pap`). PACT: the personal-agent JWT proves "That a known personal agent is calling for someone it calls sub. Not that sub owns a Brand account." (section 3.3), the scopes come from the customer's login with the business through OAuth device code (section 5), and the Decagon post says of the protocol "It separates the identity of the personal agent from its authority to act on a customer" (`pact`). Whether the agent identity of either protocol can be carried by Web Bot Auth is not stated: Web Bot Auth is not found in the PACT specification page nor in the Poppy specification page (2026-10-13).
- Visa TAP defines an agent recognition signature based on HTTP Message Signatures (RFC 9421) and aligned with web-bot-auth, a signed consumer or device identity and a signed payment container (`visa-tap`).
- Mastercard's page of 2025-10-14 says merchants "can verify agent authenticity" by implementing Web Bot Auth at the CDN layer, and that Mastercard has partnered with Cloudflare to support it in Agent Pay (`mastercard-agent-pay`).
- UCP merged Web Bot Auth interop on 2026-07-03 (PR #483); its overview page at commit f2206e6 defines the values of the `Signature-Agent` header `type` parameter by reference to draft-meunier-webbotauth-httpsig-directory-00 (section 4.1: `jwks_uri`, `cimd`, `directory`) and, for `cimd`, to draft-ietf-oauth-client-id-metadata-document (read 2026-10-14): a dual-audience signature, the "RECOMMENDED path for integrators", limited to requests (`ucp`).
- x402 specifies an `http-message-signatures` extension (merged 2026-04-15) that identifies the paying agent, and a `sign-in-with-x` extension that authenticates the buyer's wallet (`x402`). A text search of ACP's specification files, issues and pull requests returns no occurrence of Web Bot Auth (`acp`).
- KYAPay is a family of individual drafts for a signed token carrying verified agent and human identity and payment credentials; the datatracker shows no WG stream (`kyapay`).
- The IETF agentproto charter (01, approved 2026-10-08) names Web Authorization Protocol (OAuth), webbotauth and WIMSE for identity, authorization and security; its PR #128 on the user agent and service agent distinction was closed without a merge on 2026-10-08 (`ietf-agentproto`).
- The draft W3C Agentic Web charter lists agent identity, delegation and interaction context among its scope items (`w3c-agenticweb-wg`).
- Browsers on WebMCP: WebKit issue #670 was closed on 2026-06-11 with "position: oppose"; Mozilla issue #1412 on 2026-08-05 with "position: neutral"; Chrome published an early preview on 2026-02-10; the Edge post of 2026-09-21 says its implementation "is ready for testing" (`browsers-webmcp`, `w3c-webmcp-cg-report`).
- An OpenID Foundation whitepaper outlines identity and authorization resources for AI agents and sets a strategic agenda (arXiv 2510.25819) (`oidf-authzen-agents`).

## S4. Signed terms, authorisation and receipts
`ap2`, `verifiable-intent`, `ucp`, `acp`, `x402`, `ietf-httpauth-payment`, `emvco-agentic-payments-framework`, `fido-agentic-standards`, `aaif-wg-agentic-commerce`, `ietf-vcon`, `emilia-protocol`, `browsers-webmcp`, `pap`, `pact`, `shopify`

This seam compares the records the documents describe. It is not an assessment of legal compliance by any protocol, platform or merchant.

What each normative text says is signed, by whom, and what record exists is in the table "Payment protocols compared". By side:

- Buyer authorisation: AP2 mandates are signed Verifiable Digital Credentials, a Checkout Mandate and a Payment Mandate (`ap2`); Verifiable Intent is a layered SD-JWT credential format (`verifiable-intent`); the UCP AP2 extension requires platforms to provide mandates "proving the user explicitly authorized the specific checkout state and funds transfer" (`ucp`). EMVCo's draft framework describes "Intent Services" to "register, reference, retrieve and manage consumer-authorised intent" (`emvco-agentic-payments-framework`).
- Seller terms: UCP carries the seller's rules in `policies[]` (PR #572, merged 2026-07-23) and requires the business to "embed a cryptographic signature in checkout responses, proving the terms" (`ucp`); x402's offer-and-receipt extension lets the server commit to the payment terms of the offer (`x402`); ACP's checkout session carries a required `links` field (`acp`).
- Receipts and records: x402 signs receipts, with the wire shape "not considered stable" (`x402`); the IETF Payment draft defines an optional `Payment-Receipt` header with four fields, and its table has no signature field (`ietf-httpauth-payment`); ACP's order schema has `receipt_url` (`acp`); UCP signs order webhook payloads with an RFC 9421 message signature over the body, a property of the delivery (`ucp`).
- AP2: the merchant provides a merchant-signed Checkout JWT and, after accepting or rejecting the Checkout Mandate, returns a Checkout Receipt (status Success or Error, bound to the hash of the closed mandate); agent_authorization.md defines the Mandate Receipt as a "Verifier-signed JWT" (`ap2`). UCP's AP2 extension requires `ap2.merchant_authorization` in checkout responses and does not mention a receipt (`ucp`).
- AP2 Checkout Receipt, read in the native text on 2026-10-13 (docs/ap2 at commit e1ea56d, the head of main): "Once the Merchant has accepted or rejected the Checkout Mandate, it MUST return a Checkout Receipt." (docs/ap2/specification.md, section Checkout Mandate), returned to the Shopping Agent; the schema checkout_receipt.json requires status, iss, iat and reference (the hash of the closed mandate), with order_id on Success; the flows page calls it the "Merchant-signed Checkout Receipt". The receipt closes the checkout against the mandate. The words refund and cancel are not found in the seven documents of docs/ap2; as a goods-return term "return" occurs only as the field return_policy ("30-day returns") in two example checkouts of checkout_mandate.md; fulfil(l) appears 3 times, only as a generic verb ("fulfill", "fulfilled", "fulfills"), never for the fulfilment of an order (recounted 2026-10-14), and for disputes the specification says that how the mandates and receipts are used is "outside the scope of this specification" (`ap2`).
- Dispute: Verifiable Intent declares dispute resolution out of scope (`verifiable-intent`); the AP2 FAQ says that in a dispute a network adjudicator can use the user-signed Checkout Mandate (`ap2`); x402's `auth-capture` scheme defines void, refund and reclaim (`x402`).
- Standards track: the FIDO Alliance release of 2026-04-28 says the AP2 and Verifiable Intent contributions will be reviewed and further developed in its Payments Technical Working Group, and the AP2 repository says its core specification has been donated to FIDO (`fido-agentic-standards`, `ap2`).
- AAIF Agentic Commerce group, Running Notes of 2026-07-22: "Presentation is not active consent", with the open question of distinguishing required disclosure, active consent, delegated authority and human escalation (`aaif-wg-agentic-commerce`).
- Not found in the files, issues and pull requests of UCP, ACP, AP2, x402, Verifiable Intent and Visa TAP, 2026-10-06: vCon; and not found in the vCon texts read, 2026-10-06: any of those protocols; the IETF vcon group and the AUDIT effort work on a record format for agent conversations, and the individual draft CHEQ proposes a signed object by which a human confirms an action proposed by an AI agent (`ietf-vcon`, `ietf-audit`).
- Approval gate: UCP Discussion #563 proposes an approval gate for unattended buying agents (`ucp`); AAIF Identity and Trust issue #13 compares how MintID and Proofable record authority, decision, dispatch and effect (https://github.com/aaif/wg-identity-and-trust/issues/13, read 2026-10-08).
- In PayPal's WebMCP implementation for Store Sync merchants the agent initiates checkout and "The buyer is then handed off to PayPal to sign in, choose or confirm a funding source, review the transaction, and approve payment" (`browsers-webmcp`). In the EMILIA README example, an MCP payment server "refuses a call without approval, binds approval to the amount, currency, vendor, and destination" and is a local demonstration (`emilia-protocol`).
- Merchant decisions: UCP Discussion #895 asks about signed, portable evidence for merchant accept and refuse decisions; Issue #896 proposes a contingencies extension in which the business "notes on the Order which rule it applied" (`ucp`).
- Reasoning and evidence, side by side (not a finding about either): the proposed vCon AI Agent Extension lists prompts and reasoning together with tool call requests and responses (`ietf-vcon`); the EMILIA architecture draft says "A valid signature, a current credential, a satisfied evidence requirement, and an observed effect remain different facts." (`emilia-protocol`).
- Digests and bytes: in the Proofable docs repository (https://github.com/proofable/docs) an earlier evidence packet (commits 3a45f02 to 4ceb58b, 2026-10-06 to 2026-10-08) had manifest digests computed over CRLF bytes, as its author stated in the message of commit 63fc73b (2026-10-07), "The prior manifest digests were computed over CRLF bytes while git stores LF."; the packet frozen at commit 9851059 (2026-10-08) matches its SHA256SUMS (recomputed 2026-10-13); issue #287 and pull request #288 of agentrust-io/integrations were open on 2026-10-13 (`aaif-identity-trust`).
- Signal versus grant: the A2A specification says "Agents MUST NOT treat the TASK_STATE_AUTH_REQUIRED state transition, by itself, as authorization for any particular operation." (`a2a-core`), and Shopify's Checkout WebMCP documentation says of the permission to place an order that "WBA and ready_for_complete don't grant it." (`browsers-webmcp`); compare the approval items above (UCP #563, #678 with #883, AAIF issue #13).
- Operator-reported until reproduced (AAIF list message 48, 2026-10-08, read by the author on 2026-10-09): "record the new fixes and traces as operator-reported until independently reproduced" and "out_of_scope does not establish veto enforcement at a protected executor" (https://lists.aaif.io/g/wg-identity-trust/message/48; `aaif-identity-trust`).
- Reports and confirmations, three texts read on 2026-10-13. Poppy operations, section 8: a confirmation shows that a Personal Agent "stated that the User approved a specific revision of the terms", and "It doesn't prove that the User saw the terms or approved them." (`pap`). PACT, section 5.6: each reply under a delegation token carries a signed receipt of the grant, scopes used and actions, and "Personal agents SHOULD verify and keep receipts"; section 3.3 says what the identity token does not prove (`pact`). Shopify/shop, transactions.md: the agent's completion of a spend request "records your report, not payment confirmation", an issued credential state "does not establish credential delivery or payment", and cancelling "does not cancel/refund the purchase or revoke an issued credential" (`shopify`). In the three, the record is addressed to the Company, the personal agent or the agent's own report; a confirmation to the consumer on a durable medium is not found in the Poppy specification and operations pages, the PACT specification page or the Shopify/shop README, SKILL.md and transactions.md (2026-10-13).
- Open proposals on records (UCP #515, #629, #895, #896; ACP #231, #265, #303, #304; x402 receipts and reviews) are in the Open proposals appendix.

## Free text against structured data
`ucp`

Where a business may answer in free text and a structured capability defines the same kind of fact as a field, the texts say which one a consumer relies on. One line per source; the author of this map commented on the pull request of the last line (see Disclosure).

- UCP `ask` (Common capability, merged 2026-10-07 in PR #538; docs/specification/common/ask/index.md at commit f2206e6): the answer is free text authored by the business, with plain text required; "An answer is indicative, not authoritative." and where it conflicts with the representation returned by the capability that owns the resource, "that representation is authoritative and the Platform MUST prefer it" (lines 198 to 204; https://github.com/Universal-Commerce-Protocol/ucp/blob/f2206e680f64fe2cc73495acc3557569afd9097a/docs/specification/common/ask/index.md; `ucp`).
- The same page: "A Platform MUST NOT treat an `answer` as the binding disclosure for a safety, allergen, or regulatory claim." (lines 205 and 206); a business should carry such a notice as a warning with presentation disclosure "rather than only in the answer text" (lines 214 and 215), and warnings with that presentation "carry notices the Platform MUST NOT hide or dismiss" (lines 304 and 305) (`ucp`).
- UCP PR #897 (food domain, open; head 4c2c601 on 2026-10-09): the allergen notice is a warning with code `allergens` and presentation disclosure; the example in docs/specification/food/checkout/index.md gives it as a sentence, "Prepared in a kitchen that handles peanuts, tree nuts, sesame, and wheat.", with a link. A structured allergen field is not found in the 35 files of the pull request at that head (all occurrences of the word are in that one documentation file, 2026-10-09). The author of this map commented on 2026-10-09 asking for an optional list of allergen codes beside the free text, with the code list named because the lists differ by jurisdiction (https://github.com/Universal-Commerce-Protocol/ucp/pull/897#issuecomment-6074516498; `ucp`).

## Not established versus negative
`ietf-dawn`, `ietf-audit`, `ietf-agentproto`, `ucp`, `ard`, `aaif-wg-agentic-commerce`

Several venues distinguish a result that could not be established from a negative one, each in its own vocabulary. One line per venue; none of them defines the others' terms.

- DAWN list, 2026-10-07: a reference that does not resolve, one blocked by the discovering entity's retrieval policy and one that resolves with the record absent, which "end as no discovery result, and they have different owners and different retries" (https://mailarchive.ietf.org/arch/msg/dawn/Ce73ar_tEl0XO2FE41sdNKAGjc8/; `ietf-dawn`).
- AUDIT list, 2026-10-06: an unavailable source or incomplete coverage "produces an incomplete audit, never an absence finding", and the claim is only that "no qualifying record was found in the declared sources by the cutoff" (https://mailarchive.ietf.org/arch/msg/audit/u04Utry2tPGRqJ_f-SmRk_EMW88/; `ietf-audit`).
- AAIF Identity and Trust issue #13, 2026-10-04: the labels agreed on the list are *not applicable* (no equivalent), *not emitted* (exists, not published, by design) and *not measured* (https://github.com/aaif/wg-identity-and-trust/issues/13#issuecomment-5981946163).
- UCP Discussion #867, 2026-09-26: the proposed reporting frame counts hosts that refused by robots.txt or could not be reached as their own figures beside the result, and not as a "no" (https://github.com/Universal-Commerce-Protocol/ucp/discussions/867; `ucp`; the author of this map wrote the discussion, see Disclosure).
- agentproto list, thread "Topic: Existing practice, use cases, and deployment models" (the "Topic 1" input set), 2026-10-05: the author of draft-konda-agentproto-evaluation-state wrote "An unestablished input is a different fact from a negative one" and offered to write the bullet for section 3.3.3 or 3.3.5 of the use cases text (https://mailarchive.ietf.org/arch/msg/agentproto/Oaunfd9TaD0GPF8cS3W9J7m8CQ8/); Iman Schrock answered the same day with, for 3.3.5, "If a required authorization input cannot be established, preserve that fact separately from an evaluated refusal, even when both lead to local denial." (https://mailarchive.ietf.org/arch/msg/agentproto/XMpnWAx0K2u_ct-wh0sYFcPAiQ8/; `ietf-agentproto`).
- Lighthouse PR #17295 (merged on 2026-10-09, GitHub merge record read on 2026-10-14): the robots-txt and llms-txt audits treat HTTP 429 as a server error and not as an absent file, following Google's robots.txt specification (https://github.com/GoogleChrome/lighthouse/pull/17295; `ard`).
- draft-krausz-verification-state-03 separates indeterminate from not_evaluated; a commenter on AAIF issue #5 writes that a mapping "would need to preserve the distinction between an inconclusive evaluation and one that did not occur" (https://github.com/aaif/wg-agentic-commerce/issues/5#issuecomment-6052049160; `aaif-wg-agentic-commerce`).
- AUDIT case 8, 2026-10-08: a verified refusal "can make that effect slot not applicable when the declaration names refusal as a terminal condition", while the refusal "should satisfy the decision slot, not fill the downstream effect slot" (https://mailarchive.ietf.org/arch/msg/audit/p_gA6xAzlBBK3DIMl0SFszYUnmE/; `ietf-audit`).
- UCP #904 and #867, 2026-10-08 and 2026-10-09: the first version of the census run listed its 7 responses of 200 that did not parse among the cases it could not ask, and the reply of the author of this map read them as row 1 without row 2, an answer of the site (https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18812160); in the version of 2026-10-09 of the same comment, a re-run, the 6 that answer 200 and do not parse are counted as "row 1 without row 2" and the site-side and prober-side lines of could not ask are separate (https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18810486 and https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18831816; `ucp`).
- Counterexample: UCP PR #691 makes not declared and absent the same thing; its author wrote on 2026-10-07 that "an absent price_treatment and an absent tax now mean the same thing everywhere" (https://github.com/Universal-Commerce-Protocol/ucp/pull/691#issuecomment-6039591246; `ucp`).
- Lodging, Discussion #864, 2026-10-08: a hotel revenue management practitioner writes that a rate restriction such as a minimum stay would "likely return inventory_exhausted, which gives the agent nothing to recover with"; the standard error table lists inventory_exhausted as "The selected accommodation unit or inventory hold is no longer available" and no code for restrictions (https://github.com/Universal-Commerce-Protocol/ucp/discussions/864#discussioncomment-18816854; `ucp`).
- On whether a 404 or a 410 at the profile path means an absence or a decision not to take part, the author of this map commented in UCP issue #904 on 2026-10-07 (https://github.com/Universal-Commerce-Protocol/ucp/issues/904#issuecomment-6032850150; see Disclosure; `ucp`).
- AAIF Identity and Trust, shared runner (agentrust-io/integrations issue #287, 2026-10-07): the scope asks to "Preserve `not_applicable`, `not_emitted` and `not_measured`" as distinct states (https://github.com/agentrust-io/integrations/issues/287; `aaif-identity-trust`).
- AAIF Identity and Trust, list message 45 (a participant who submitted the runner, 2026-10-08, read by the author on 2026-10-09): "all 14 contract fields receive explicit states, with not_applicable, not_emitted and not_measured kept distinct"; the fixes are in an external repository and pull request #288 of agentrust-io/integrations had not been updated on 2026-10-09 (`aaif-identity-trust`).
- AAIF Identity and Trust, list message 46 (a MintID participant, 2026-10-08, read by the author on 2026-10-09): "a verifier's refusal is a decision, not evidence that a relying party enforces the veto"; and a 5xx is "recorded as a service interruption, never as a decision" (`aaif-identity-trust`).
- Evidence named, not only its age (AAIF list message 40, a MintID participant, 2026-10-06, read by the author on 2026-10-09): "name the evidence each decision rested on (for us, the root's epoch and height), not only its age; that is what lets a reader tell" (https://lists.aaif.io/g/wg-identity-trust/message/40; `aaif-identity-trust`).
- Evidence-strength labels, AAIF Identity and Trust issue #5 (opened 2026-08-25 by a participant): the title is "Proposal: evidence-strength labels for agent identity, authorization, and consent claims (declared vs observed)" and the body says "an approval record is an evidence claim that can be self-declared or independently verified"; a comment of the Proofable author (6020760992, 2026-10-06) writes "portable proof/receipt = the verifiable protocol record" and "appraisal = what the relying party established about that record" (https://github.com/aaif/wg-identity-and-trust/issues/5; `aaif-identity-trust`).

---

<a id="part-matrix"></a>
# Part 7: Payment protocols compared

| Protocol | Signatures | Receipt or record | Dispute |
|---|---|---|---|
| [Agent Payments Protocol (AP2)](#ap2)<br><small>Governance: FIDO Alliance (donated by Google, 2026-04-28; Payments and Agentic Authentication TWGs); reference repository in the organisation google-agentic-commerce, Apache-2.0<br>Version: v0.2.0 (2026-04-28), v0.1.0 (2025-09-16); standardisation continues in FIDO working groups<br>Source: [AP2 index.md](https://github.com/google-agentic-commerce/AP2/blob/main/docs/index.md)</small> | What: Mandates (signed Verifiable Digital Credentials): Checkout Mandate (shared with merchant), Payment Mandate (instrument, amount)<br>Who: Closed mandates: the User (Human Present) or an Agent key (Human Not Present), whose trust "is provided by open Mandates that are signed by the User or a trust list of Agent Providers"; the Merchant provides "a merchant-signed JWT containing the Checkout" (docs/ap2/specification.md, Modes and Checkout Mandate, commit e1ea56d, 2026-10-05); FAQ: "user-signed Checkout Mandate" | Checkout Receipt, returned by the Merchant after accepting or rejecting the Checkout Mandate, with fields status (Success or Error), iss, iat, reference (hash of the closed Mandate) and order_id on Success (checkout_receipt.json); a Mandate Receipt is "a Verifier-signed JWT" (agent_authorization.md); a "signed Payment Receipt" is returned by the Merchant Payment Processor (specification.md); all at commit e1ea56d, 2026-10-05; chained mandates give a verifiable audit trail (docs/index.md) | FAQ: in a dispute the network adjudicator can use the user-signed Checkout Mandate; dispute process: "outside the scope of this specification" (docs/ap2/specification.md, section Dispute Evidence, commit e1ea56d, read 2026-10-14) |
| [Universal Commerce Protocol (UCP)](#ucp)<br><small>Governance: Governing Council of five (Google, Shopify permanent; three elected); Tech Councils decide by majority; Council charters Domain Working Groups (DWGs)<br>Version: latest GitHub release v2026-08-25 (2026-08-25); lodging booking draft (PR #780)<br>Source: [ucp ap2-mandates.md @f2206e6](https://github.com/Universal-Commerce-Protocol/ucp/blob/f2206e680f64fe2cc73495acc3557569afd9097a/docs/specification/payment/extensions/ap2-mandates.md)</small> | What: checkout responses: business signature "proving the terms (price, line items) are authentic"; order webhooks: RFC 9421 signature<br>Who: business (checkout responses, order webhooks); mandates provided by the platform | Order entity, "the authoritative latest state of the order at the time of retrieval or delivery" | not found in the UCP pages read on main (2026-10-03); draft PR #890 only (author commented; see Disclosure) |
| [Agentic Commerce Protocol (ACP)](#acp)<br><small>Governance: OpenAI and Stripe maintainers; TSC of up to 7 seats; MAINTAINERS.md lists Meta; PR #236 "ADMIN: Add Meta as TSC member"<br>Version: Beta; dated versions 2025-09-29 to 2026-04-17 plus an unreleased folder; tag or release: not found in the repository, 2026-10-03 (main unchanged at commit 7fdd78d on 2026-10-14)<br>Source: [agentic-commerce-protocol README.md](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/blob/main/README.md)</small> | What: Signature header on requests (required in delegate_authentication); Merchant-Signature HMAC on webhooks<br>Who: The request sender; for webhooks, the merchant side | receipt_url, "URL to the order receipt"; signed receipt: not found in specification and RFC files, 2026-10-03 (main unchanged at commit 7fdd78d on 2026-10-14) | "dispute" is a post-order adjustment type (unreleased schema); dispute process: not found in specification, RFC files, 2026-10-03 (main unchanged at commit 7fdd78d on 2026-10-14) |
| [x402](#x402)<br><small>Governance: x402 Foundation (Linux Foundation); intent 2026-04-02, operational launch 2026-07-14; TSC.md lists Coinbase, Cloudflare, Stripe<br>Version: v1 SDK packages marked "Deprecated (v1)"; offer-and-receipt: "Wire shape and field placement are not considered stable"<br>Source: [x402 extension-offer-and-receipt.md](https://github.com/x402-foundation/x402/blob/main/specs/extensions/extension-offer-and-receipt.md)</small> | What: Payer signs the payment (PAYMENT-SIGNATURE); with offer-and-receipt the server commits to the offer terms and signs a receipt<br>Who: The client for the payment; the server for offer and receipt | Signed receipt (offer-and-receipt), declared use "dispute evidence and auditability"; wire shape not stable | "irreversible once executed" (exact scheme, FAQ); auth-capture: void, refund, reclaim; dispute process: not found in the pages read, 2026-10-03; the repository has changed since (head e95b066 on 2026-10-13) and a text search of 2026-10-14 finds the word dispute in 26 files, among them the offer-and-receipt specification and scheme texts, not read for a dispute process |
| [Visa Trusted Agent Protocol (TAP)](#visa-tap)<br><small>Governance: Published by Visa under Visa Product Terms of October 10, 2025; the licence is "conditioned upon You implementing the most current version of the Specification in its entirety" (Product Terms, read in a browser on 2026-10-14)<br>Version: Product page: "This product is in the process of development and deployment." (read in a browser on 2026-10-14); version number or date on the specifications page: none visible in the saved text (2026-10-14); release: not found, 2026-10-03<br>Source: [developer.visa.com trusted-agent-protocol-specifications](https://developer.visa.com/capabilities/trusted-agent-protocol/trusted-agent-protocol-specifications)</small> | What: Three signatures: agent recognition (header, HTTP Message Signatures), signed consumer/device identity, signed payment container<br>Who: The agent, with a private key; the merchant or site protection provider verifies with the public key from a key store | no record format found in the merchant specification page (read in a browser on 2026-10-14): audit has no match, and receipt appears once, for data a merchant can use "when providing receipt or order updates" to the consumer; sample README: not found, 2026-10-03 | not found in the merchant specification page (dispute, chargeback, liability: no match, read in a browser on 2026-10-14) and sample README, 2026-10-03 |
| [Verifiable Intent](#verifiable-intent)<br><small>Governance: Maintained by Mastercard (README), "open to multi-stakeholder contribution"; Apache-2.0; contributed to the FIDO Payments Technical Working Group<br>Version: Draft v0.1; tag v0.1.0; last commit 2026-04-20<br>Source: [verifiable-intent README.md](https://github.com/agent-intent/verifiable-intent/blob/main/README.md)</small> | What: A delegation chain of SD-JWT credentials carrying mandates and user constraints; checkout-payment integrity binding<br>Who: Layer 1 credential provider; layer 2 user device key; layer 3 (Autonomous mode) agent key | Tamper-evident record of what the user delegated (README); receipt object: not found in README, design rationale, 2026-10-02 | Dispute resolution is declared out of scope in the README |
| [EMV Agentic Payments Framework for Specifications (draft for public feedback)](#emvco-agentic-payments-framework)<br><small>Governance: EMVCo, Agentic Payments Task Force; collaboration with FIDO Alliance, OpenID Foundation, OpenWallet Foundation and W3C<br>Version: Framework for Specifications v1.0 DRAFT; comment period ended 2026-09-30<br>Source: [emvco.com emvco-requests-feedback-on-framework-…](https://www.emvco.com/news/emvco-requests-feedback-on-framework-for-secure-interoperable-and-scalable-card-based-agentic-payments/)</small> | What: not assessed: the public-feedback draft was not read; press release and Insights article only (2026-10-02)<br>Who: not assessed: the public-feedback draft was not read; press release and Insights article only (2026-10-02) | Intent Services register, reference, retrieve and manage consumer-authorised intent (press release); draft not read | not assessed: the public-feedback draft was not read; press release and Insights article only (2026-10-02) |

---

<a id="part-core"></a>
# Part 8: Core entries

### W3C AI Agent Protocol Community Group
<a id="w3c-ai-agent-protocol-cg"></a>

**W3C, venue.** Active Community Group (created 2025-05-08); agent identity is DID-method-agnostic (did:wba, did:web, did:webvh) since 2026-08-13. Bi-weekly meetings; the meeting of 2026-10-07 was announced as canceled (calendar notice of 2026-10-01) and the October 2026 list archive holds 5 messages, the last of 2026-10-07, none announcing a later meeting (read 2026-10-13); the W3C group data list two chairs. (as of 2026-10-13).

**Relevance to commerce.** The protocol draft defines an Agent Discovery Service Protocol in JSON-LD, with active discovery at https://{domain}/.well-known/agent-descriptions and an Agent Description "Information" that covers "products, or services". The use_case.html draft includes a hotel booking scenario (Personal Agent, Search Agent, hotel Service Agent) with the requirement "Agent Transactions". The agent identity draft uses a Decentralized Identifier (DID) URL as the HTTP signature keyid with RFC 9421 and RFC 9530.

**Committed next.**
- Topics "streaming HTTP authentication, mutual DID authentication"; joint Technical Plenary and Advisory Committee (TPAC) session with the WebAgents Community Group (CG) under discussion (undated) [statement] https://lists.w3.org/Archives/Public/public-agentprotocol/2026Sep/0009.html

**Boundary.** On 2026-09-10 the maintainer wrote of a proposal on agent memory "My feeling is that this goes beyond the current scope of our protocol.".

**Sources.**
- [normative] https://w3c-cg.github.io/ai-agent-protocol/protocol.html (2026-10-02)
- [normative] https://github.com/w3c-cg/ai-agent-protocol/blob/main/agent-identity.html (2026-10-02)
- [normative] https://github.com/w3c-cg/ai-agent-protocol/blob/main/use_case.html (2026-10-02)
- [statement] https://lists.w3.org/Archives/Public/public-agentprotocol/2026Oct/0000.html (2026-10-03)
- [statement] https://lists.w3.org/Archives/Public/public-agentprotocol/2026Oct/ (2026-10-13)
- [normative] https://api.w3.org/groups/cg/agentprotocol (2026-10-02)
- [third party] https://github.com/w3c-cg/ai-agent-protocol/issues/36 (2026-10-03)
- [normative] https://lists.w3.org/Archives/Public/public-agentprotocol/2026Sep/0009.html (2026-10-03)

**Overlaps:** [a2a-discovery](#a2a-discovery), [ard](#ard), [ietf-webbotauth](#ietf-webbotauth), [w3c-agenticweb-wg](#w3c-agenticweb-wg)

**Coverage:** see [Evidence](#evidence-w3c-ai-agent-protocol-cg).

### W3C Agentic Web Working Group (draft charter)
<a id="w3c-agenticweb-wg"></a>

**W3C, charter.** Draft charter for a proposed Working Group, in refinement until approx. 2026-11-10 (W3C Team estimate, public-new-work). On 2026-10-13 the last change to the charter text is still the commit of 2026-09-30 (a definition of the term and a simplified scope), and the Strategy issue #576 is open with 4 comments, the last of 2026-10-01. (as of 2026-10-13).

**Relevance to commerce.** The draft charter proposes a Working Group "to develop specifications that facilitate web pages and applications to be leveraged by LLMs and AI agents", scoped to site capabilities and context for agents, agent identity and delegation, and permissions and policies for agent actions. Its one normative deliverable is WebMCP, adopted from the Web Machine Learning Community Group; it lists the Web Payment Security Interest Group (IG), IETF webbotauth and IETF aipref for coordination. On 2026-08-13 a representative of Apple wrote on PR #829 "Expect a formal objection if this is merged.", about the earlier plan to place WebMCP in the Web Machine Learning Working Group (WG). Charter-drafts PR #888 (editorial fixes, opened by the author of this map on 2026-10-02) was merged on 2026-10-13 at 11:06 UTC by one of its reviewers, after approvals by three reviewers: a participant on 2026-10-08 with the review text "LGTM" (review 5463458958) and two on 2026-10-13 (GitHub, read on 2026-10-14).

**Committed next.**
- Charter refinement until approximately 10 November 2026; notices of extension on the Strategy issue (approx. 2026-11-10) [decision] https://lists.w3.org/Archives/Public/public-new-work/2026Oct/0002.html

**Boundary.** Out of scope: model APIs, inference and execution; cryptographic authentication primitives; crawler controls; agent to server communications.

**Author participation.** The author of this map took part in charter-drafts PR #888 (editorial fixes to the draft, no change to scope; merged on 2026-10-13); see Disclosure.

**Sources.**
- [normative] https://w3c.github.io/charter-drafts/2026/agenticweb-wg.html (2026-10-02)
- [statement] https://github.com/w3c/strategy/issues/576 (2026-10-03)
- [decision] https://lists.w3.org/Archives/Public/public-new-work/2026Oct/0002.html (2026-10-03)
- [third party] https://github.com/w3c/charter-drafts/pull/829 (2026-10-02)
- [decision] https://github.com/w3c/charter-drafts/pull/888#pullrequestreview-5463458958 (2026-10-09)
- [decision] https://github.com/w3c/charter-drafts/pull/888 (2026-10-14)

**Overlaps:** [w3c-tpac-2026](#w3c-tpac-2026), [w3c-webmcp-cg-report](#w3c-webmcp-cg-report), [ietf-webbotauth](#ietf-webbotauth), [ietf-aipref](#ietf-aipref)

**Coverage:** see [Evidence](#evidence-w3c-agenticweb-wg).

### W3C DID Resolution
<a id="w3c-did-resolution"></a>

**W3C, specification.** Candidate Recommendation Snapshot 2026-08-06; current Candidate Recommendation Draft 2026-10-01 (also 2026-08-28), which marks the Decentralized Identifier (DID) URL dereferencing feature and sections 5, 6, 8 and 10 as at risk. The exclusion opportunity on the Patent Review Draft ended on 2026-10-05. PR #344, "full pass at DID URL dereferencing algorithm (isolated)", was merged into main on 2026-10-13 at 02:10 UTC (merge commit 0956c93). The W3C publication history read on 2026-10-13 still lists the Candidate Recommendation Draft of 1 October 2026 as the latest, so no draft has been published after the merge; the merged text was not read for the at-risk markings. At the DID Working Group (WG) call of 2026-10-08 (minutes at w3.org/2026/10/08-did-minutes.html, read 2026-10-13) a chair ran the poll "PROPOSAL: Merge PR344 and agree that any future improvements to the DID URL Dereferencing Algorithm should be handled as separate issues.": eight participants recorded +1 and one recorded -1, "some technical issues not sufficiently discussed, charter violation, process violation, breaks compatibilty with DID 1.0 and CID". The chair then said "by Chair's decision, we will be merging this PR" and asked that the technical points be raised as separate issues; the merge followed on 2026-10-13. The minutes do not record the poll as a resolution. The PR comments of 2026-10-08 record the same dissent, that the changes violate the WG charter, and the chairs' answer that they do not. The statement of 2026-10-06 that unresolved points of the PR would be run as proposals so that objections can be recorded was followed by this single poll; separate issues for the points of the -1 were not looked for one by one on 2026-10-13. (as of 2026-10-13).

**Relevance to commerce.** The specification defines how a DID is resolved to a DID document and how DID URLs are dereferenced; the relativeRef parameter is used for product-level references such as Digital Product Passports (issue #332). PR #344 (merged 2026-10-13) was described on 2026-10-02 as replacing the dereferencing algorithm with handlers and dropping built-in processing of relativeRef and serviceType (the latter from GS1); the merged text (38 commits, rebased on 2026-10-11) was not compared with that description; a participant wrote (https://github.com/w3c/did-resolution/pull/344#issuecomment-5611077919) "This breaks various existing deployments and use cases that I have explained on WG calls, e.g. in the area of Digital Product Passports." On 2026-10-05 a chair (Will Abramson) wrote that "the chairs plan to run a proposal to gauge the consensus of the group for merging this PR", and that otherwise "maybe the group has to start seriously considering ripping out dereferencing entirely from the specification." He approved the PR the same day ("Needs a rebase, but other than that looks good to me"). Exclusion opportunity closed 2026-10-05; no patent disclosures or exclusions listed on the DID WG intellectual property rights (IPR) page as of 2026-10-06. On 2026-10-07 a chair (Will Abramson) wrote on PR #344 "The chairs intend to run a proposal to adopt this PR and replace the existing DID URL Dereferencing section."; another participant approved the PR the same day, noting a concern about the MUST on giving the user the choice of resolvers, and a third participant wrote "I support the idea that we run a proposal to merge this PR on Thursday." On 2026-10-08 a participant wrote on the PR "In my opinion, the changes in this PR violate the WG charter" (and, he adds, like the previous "Resolve DID URLs" proposal) (comment 6060762625); the same chair answered the same day "In the chairs view, as has been stated numerous times on the calls, their is no charter violation." (comment 6062369708). On 2026-10-08 the same participant wrote that "The overloading of service type in this algorithm in my opinion requires a Class 4 change in DID 1.1, which is not allowed by the" (comment 6064294182). The same day that chair wrote for the chairs "My sense is the group is faced with two options", the first to "Adopt this PR as the new foundation for the DID URL Dereferencing algorithm" and the second to "Remove DID URL Dereferencing from this version of the specification" (comment 6062369708). In a review comment the chair wrote "This diagram needs to be updated to 2. Resolve the DID" (4220468912) and a participant answered "Ok. I can get that in today." (4221259495); commit 697f09b of 2026-10-08 by that participant, is titled "removed DID URL from dereferencing diagram". Merge: the PR was merged on 2026-10-13, 02:10:47 UTC (GitHub merge record, read 2026-10-14). PR #344 has no comment after 2026-10-08 (read 2026-10-13); the public-did-wg archive for October 2026 held three messages, the last of 2026-10-07, and the outcome of the call of 2026-10-08 is in its minutes (see the status).

**Committed next.**
- None declared in the sources read.

**Boundary.** WG resolved on 2026-09-10 that the specification "will not define an abstract Dereference() function signature" separate from Resolve().

**Author participation.** The author of this map took part in PR #344 with two comments on 2026-10-02 (relativeRef handler, serviceType); see Disclosure.

**Sources.**
- [decision] https://www.w3.org/groups/wg/did/ipr/ (2026-10-06)
- [third party] https://github.com/w3c/did-resolution/pull/344#issuecomment-5998044656 (2026-10-06)
- [third party] https://github.com/w3c/did-resolution/pull/344#pullrequestreview-5417251334 (2026-10-06)
- [normative] https://www.w3.org/TR/did-resolution/ (2026-10-03)
- [decision] https://www.w3.org/standards/history/did-resolution-1.0/ (2026-10-13)
- [third party] https://github.com/w3c/did-resolution/pull/344 (2026-10-13)
- [third party] https://github.com/w3c/did-resolution/issues/332 (2026-10-02)
- [decision] https://lists.w3.org/Archives/Public/public-did-wg/2026Aug/0003.html (2026-10-05)
- [third party] https://github.com/w3c/did-resolution/pull/344#issuecomment-6041520609 (2026-10-08)
- [third party] https://github.com/w3c/did-resolution/pull/344#pullrequestreview-5444597158 (2026-10-08)
- [third party] https://github.com/w3c/did-resolution/pull/344#issuecomment-6043016784 (2026-10-08)
- [third party] https://github.com/w3c/did-resolution/pull/344#issuecomment-6062369708 (2026-10-09)
- [third party] https://github.com/w3c/did-resolution/pull/344#issuecomment-6064294182 (2026-10-09)
- [third party] https://github.com/w3c/did-resolution/pull/344#discussion_r4220468912 (2026-10-09)
- [third party] https://github.com/w3c/did-resolution/pull/344#discussion_r4221259495 (2026-10-09)
- [third party] https://github.com/w3c/did-resolution/commit/697f09b0e0b22ad9354f272201f19ba89c2bfb5f (2026-10-09)
- [statement] https://www.w3.org/groups/wg/did/ (2026-10-13)
- [decision] https://lists.w3.org/Archives/Public/public-did-wg/2026Oct/ (2026-10-13)
- [third party] https://github.com/w3c/did-resolution/pull/344#issuecomment-6060762625 (2026-10-13)
- [decision] https://github.com/w3c/did-resolution/commit/0956c9396acb7897a7e8763d41d76bcc9e7bc0bc (2026-10-13)
- [decision] https://www.w3.org/2026/10/08-did-minutes.html (2026-10-13)
- [third party] https://github.com/w3c/did-resolution/issues/361 (2026-10-03)

**Overlaps:** [gs1-conformant-resolver](#gs1-conformant-resolver), [w3c-did-methods-wg](#w3c-did-methods-wg)

**Coverage:** see [Evidence](#evidence-w3c-did-resolution).

### W3C TPAC 2026 breakouts on agents (Dublin, 2026-10-26/30)
<a id="w3c-tpac-2026"></a>

**W3C, event.** Technical Plenary and Advisory Committee (TPAC) 2026 takes place 2026-10-26 to 2026-10-30 in Dublin (hybrid). The deadline for breakout proposals to be scheduled in advance was 2026-10-08 and has passed; the README (read 2026-10-13) says that "Around 19 October" the schedule of the breakout sessions for Monday to Wednesday is added to the TPAC calendar, and the calendar page of breakout sessions listed no session in its text on 2026-10-13. On 2026-10-14 (09:35 UTC) that page lists 85 sessions, all marked "Tentative", each with a day, a time shown in Greenwich Mean Time and a room. (as of 2026-10-14).

**Relevance to commerce.** Breakouts on agents carry the label agentic web in w3c/tpac2026-breakouts; on 2026-10-13 twelve are open and none is closed or withdrawn: #22 The Agentic Web, #23 AI-friendly webpages, #24 declarative and imperative solutions, #25 permissions, actions and alignment, #31 the future of agentic web experiences, #34 Zurich workshop report, #36 extending WebMCP, #39 KYAPay, #56 agents and developer experience, #69 action semantics for agents, #71 user consent when browsers act, #84 WebMCP in WebExtensions. Two proposals without that label matter to this map: #37 a pre-kickoff meeting for the Decentralized Identifier (DID) Methods Working Group (WG) (opened 2026-09-30) and #17 the proposed Digital Policy Working Group charter. The issues carry no slot (labels session and agentic web only) and the last push to the repository is of 2026-10-07. On the calendar page of 2026-10-14 (09:35 UTC) these proposals appear with provisional slots, matched by title, times as listed in Greenwich Mean Time: #39 KYAPay on 26 Oct 17:00 to 18:00; #69 action semantics for agents on 26 Oct 17:00 to 18:00; #24 declarative and imperative solutions on 27 Oct 15:30 to 16:30; #17 the Digital Policy Working Group charter on 27 Oct 15:30 to 16:30; #36 extending WebMCP on 28 Oct 09:00 to 10:00; #25 permissions, actions and alignment on 28 Oct 10:30 to 11:30; #23 AI-friendly webpages on 28 Oct 10:30 to 11:30; #84 WebMCP in WebExtensions on 28 Oct 14:00 to 15:00; #34 the report and follow-ups from the E-commerce for Humans and AI Agents workshop on 28 Oct 15:15 to 16:15; #56 agents and developer experience on 28 Oct 15:15 to 16:15; #71 user consent when browsers act on 28 Oct 16:30 to 17:30; #31 the future of agentic web experiences on 29 Oct 17:00 to 18:00; #37 the DID Methods WG pre-kickoff meeting on 29 Oct 17:00 to 18:00; #22 The Agentic Web on 30 Oct 08:30 to 09:30. All are marked "Tentative". Issue #22 (opened 2026-09-16, with #24 and #25 on 2026-09-17, all by marcoscaceres) has the goal "Directions for future work at the W3C around enabling the web to work well with AI agents." The repository w3c/tpac2026-miniworkshops hosts mini-workshops on AI and Society, Age Assurance, and Data Governance and Ownership, with submissions on product data discoverable by agents (#32) and agentic payments (#25).

**Committed next.**
- Schedule of the Monday to Wednesday breakouts added to the TPAC calendar ("Around 19 October"); sessions are already listed as "Tentative" on 2026-10-14 (approx. 2026-10-19) [decision] https://github.com/w3c/tpac2026-breakouts
- Deadline, at noon local time, for breakout proposals made once TPAC is under way (Thursday and Friday slots) (2026-10-29) [decision] https://github.com/w3c/tpac2026-breakouts

**Boundary.** Breakouts are sessions proposed by participants, not Working Group work: TPAC has "a series of breakout sessions determined by the attendees."

**Sources.**
- [decision] https://www.w3.org/events/tpac/2026/ (2026-10-03)
- [decision] https://github.com/w3c/tpac2026-breakouts (2026-10-13)
- [third party] https://github.com/w3c/tpac2026-breakouts/issues/22 (2026-10-03)
- [decision] https://www.w3.org/news-events/tpac/ (2026-10-03)
- [third party] https://github.com/w3c/tpac2026-breakouts/issues/37 (2026-10-13)
- [decision] https://www.w3.org/calendar/tpac2026/breakout-sessions/ (2026-10-14)

**Overlaps:** [w3c-agenticweb-wg](#w3c-agenticweb-wg), [w3c-gs1-ecommerce-workshop](#w3c-gs1-ecommerce-workshop), [w3c-webmcp-cg-report](#w3c-webmcp-cg-report), [browsers-webmcp](#browsers-webmcp)

**Coverage:** see [Evidence](#evidence-w3c-tpac-2026).

### W3C/GS1 Workshop on E-commerce for Humans and AI Agents (Zurich, 8-9 Sep 2026)
<a id="w3c-gs1-ecommerce-workshop"></a>

**W3C, event.** Workshop held 2026-09-08/09 at Google Zurich, co-organised by W3C and GS1. A report and follow-up session is proposed for Technical Plenary and Advisory Committee (TPAC) 2026 (breakout #34, open on 2026-10-13 with one comment and no assigned slot). A workshop report: not found in the root of the workshop repository nor in its commits (the last push is of 2026-09-09), read 2026-10-13. (as of 2026-10-13).

**Relevance to commerce.** The workshop covers merchants' context, legal accountability, protocols, trust and ownership, product data, identity and authorisation, and payment; position statements (issues #10 to #34 and #45) are each the statement of its author. On seller authority and product identity, position statement #31 by Sven Böckelmann says "Resolution says where the data is; a signature says who signed it. Neither says who may speak for the product."; #21 (GS1 Digital Link) is related. On agent identity, delegation and consent, statements include #22 (FIDO Alliance Payments Technical Working Group (TWG), which says AP2 and Verifiable Intent are "now under review within the PTWG") and #26 (Skyfire).

**Committed next.**
- TPAC breakout "Report and follow-ups from the E-commerce for Humans and AI Agents" (#34); no slot assigned in the sources read (undated) [statement] https://github.com/w3c/tpac2026-breakouts/issues/34

**Boundary.** The workshop is an event, not a standards group; no scope exclusion found in the workshop repository, 2026-10-03.

**Author participation.** The author of this map took part in the workshop with position statement #14 (issue of 2026-06-25) and PRs #51 and #73; see Disclosure.

**Sources.**
- [decision] https://www.w3.org/2026/ecommerce-agents/ (2026-10-02)
- [third party] https://github.com/w3c/ecommerce-for-humans-and-AI-Agents-workshop/issues/31 (2026-10-03)
- [third party] https://github.com/w3c/ecommerce-for-humans-and-AI-Agents-workshop/issues/22 (2026-10-03)
- [statement] https://github.com/w3c/tpac2026-breakouts/issues/34 (2026-10-02)
- [third party] https://github.com/w3c/ecommerce-for-humans-and-AI-Agents-workshop/blob/main/slides/Sven_Boeckelmann_benelog_trusted-resolution-v1.pptx (2026-10-05)

**Overlaps:** [w3c-tpac-2026](#w3c-tpac-2026), [w3c-agenticweb-wg](#w3c-agenticweb-wg)

**Coverage:** see [Evidence](#evidence-w3c-gs1-ecommerce-workshop).

### IETF AI Preferences (aipref WG)
<a id="ietf-aipref"></a>

**IETF, venue.** The vocabulary draft is at -08 (2026-09-13 in the datatracker history) and the attach draft was last seen at -05 (2026-08-19). A virtual interim meeting is announced for 2026-10-21. On 2026-10-13 the datatracker record gives revision 08 of the vocabulary draft (time 2026-09-14 06:18 UTC) and revision 05 of the attach draft (2026-08-19), no later revision; the interim announcement was not rechecked. (as of 2026-10-13).

**Relevance to commerce.** The Working Group (WG) develops building blocks to express preferences about how content is collected and processed for AI model development, deployment and use, and the draft W3C Agentic Web charter lists it for coordination. For a seller, the vocabulary is the layer in which a publisher states what automated systems may do with its content. The editor copy of the vocabulary draft (main branch of ietf-wg-aipref/drafts, read 2026-10-03) has a section AI Use that reads "where the asset is not directly provided by the user." with a note that issue 249 asks whether referencing an asset by URL counts as direct.

**Committed next.**
- Virtual interim meeting, 20:00 to 21:30 UTC. (2026-10-21) [decision] https://mailarchive.ietf.org/arch/msg/ai-control/H8Gycx8vy4BKierBvIhG8V2JYFQ/
- Two sessions of 1.5 hours at IETF 127 (14 to 20 November 2026), requested by the chair on 2026-09-14. (undated) [statement] https://mailarchive.ietf.org/arch/msg/ai-control/95iDQg7QAejNvt6iJiEhfbpXMbk/

**Boundary.** A participant wrote on 2026-08-26 that caching of any form was agreed to be an implementation detail outside the document.

**Sources.**
- [normative] https://datatracker.ietf.org/wg/aipref/about/ (2026-09-29)
- [normative] https://datatracker.ietf.org/doc/draft-ietf-aipref-vocab (2026-10-03)
- [decision] https://datatracker.ietf.org/doc/draft-ietf-aipref-vocab/history/ (2026-10-03)
- [decision] https://mailarchive.ietf.org/arch/msg/ai-control/H8Gycx8vy4BKierBvIhG8V2JYFQ/ (2026-10-03)
- [third party] https://mailarchive.ietf.org/arch/msg/ai-control/A63f3A3k2a9GjhEtOy7J56aUorM (2026-10-03)

**Coverage:** see [Evidence](#evidence-ietf-aipref).

### IETF AUDIT (BoF preparation)
<a id="ietf-audit"></a>

**IETF, charter.** Charter text under discussion on the audit list and in mirjak/audit-bof-preparation; the BoF request lists "User e-commerce use case" in its proposed agenda (file updated 2026-09-18). On 2026-10-05 and 2026-10-06 participants agreed in words on the sentence "VCON is considered a suitable record format and the audit group will work with the vcon group to ensure the specified format addresses the auditing"; pull request #61 (one commit, 009b915) was still open on 2026-10-08 and does not contain that sentence. On 2026-10-13 the datatracker group page of audit shows the state Birds of a Feather (BOF) and no charter; a name search for expected-records finds no draft (not found on the datatracker, 2026-10-13), although a list message of 2026-10-10 refers to draft-ahuja-schrock-audit-expected-records-00. On 2026-10-10 a BoF proponent wrote on the list to a participant who had asked for a presentation slot "I am not the chair of the BoF meeting. The chairs will be selected by the ADs." and that the BoF agenda "will not be based on an open call for presentation". Pull request #61 was still open on 2026-10-13 (3 comments, last update 2026-10-06) and the repository mirjak/audit-bof-preparation has no commit after 2026-09-18. (as of 2026-10-13).

**Relevance to commerce.** AUDIT concerns audit information about agents and delegated systems, so it touches commerce wherever an agent acts for a buyer and a seller or payer later needs a record of what happened. The charter scope reads "The scope of such auditing is the observable behavior of agents, including user intent, agent or tool interactions, invoked or declined actions, exchanged data, and" Commerce, seller, merchant: not found in the charter text, 2026-10-02; repository example: "booking a hotel room" (issue #16). The BoF request lists under "Architecture overview und use cases (20 mins)" a "User e-commerce use case" and names no presenter; the architecture draft has no "e-commerce" text, and its use cases include a flight booked through a chain of agents and "Financial Transactions by Agents": "Agents may execute financial operations such as payments or procurement actions on behalf of users". The sentence on VCON was proposed on the list on 2026-10-05 by a BoF proponent, Mirja Kuehlewind ("VCON is considered a suitable record format and the audit group will work with the vcon group to ensure the specified format addresses the auditing") and accepted on 2026-10-06 by a participant ("I'm OK with this wording"); another participant proposed a variant in charter style. On 2026-10-06 Sumit Ahuja wrote that he and Iman Schrock are writing an expected-record draft, "We are aiming for the -00 before the IETF 127 cutoff", which "declares which records each participant in a cross-domain chain is expected to produce, what each establishes, and when an absent one becomes a finding"; Schrock listed six conformance cases for it (declaration integrity, all slots filled, bounded observed absence, incomplete observation, wrong or ineligible record, late record) and the claim boundary "no qualifying record was found in the declared sources by the cutoff". No text of that draft was read; it was announced on the list. Case 4 reads "An unavailable source, incomplete pagination or coverage, unresolved participant set, or open window produces an incomplete audit, never an absence finding." On 2026-10-07 the author of this map wrote a seventh case on the list at Schrock's request, "Wrong recipient or holder": a record produced by the right party but held only by another does not fill the slot, and if the declared holder's source cannot be checked the audit is incomplete; the example is the confirmation that an EU trader owes the consumer on a durable medium (Directive 2011/83/EU, Art. 8(7)), held only by the agent platform. a co-author of the draft replied the same day that the case "catches a distinction the six cases do not state clearly" and asked for it to be written in the same shape; the draft text has not been read. The text of PR #61 adds to deliverable 2: "For interaction records - the expectation is that the group will leverage the VCON format. Extensions to VCON to add data needed to model AI" On 2026-10-07 a participant proposed case 8, "Declined action": "A slot for an action that was refused before it ran is filled by the decider's signed refusal bound to that action."; on 2026-10-08 Iman Schrock replied "the refusal should satisfy the decision slot, not fill the downstream effect slot", and that a verified refusal "can make that effect slot not applicable when the declaration names refusal as a terminal condition." On 2026-10-07 Pavel Izmaylov posted the individual draft draft-izmaylov-agent-permission-receipts: the principal signs a permission with a passkey that carries "limits a machine can check" and conditions, and a verifier states for each recorded action whether it stayed within that permission. Schrock replied on 2026-10-08 comparing it with draft-schrock-ep-authorization-receipts-13 and draft-schrock-ep-bounded-capability-receipts-06 and suggested a comparison in Section 11 of the draft. On 2026-09-30 a participant wrote on the list "Let me know if you want me to share some of our practices on EDR and Gateways during any interim or future meetings." (EDR: endpoint detection and response); on 2026-10-08 the lead editor of the expected-record draft answered "thank you for offering text, and yes please." and the participant wrote that the architecture draft and the charter should "identify the necessary PEPs that should be covered first, rather than jumping into defining the record entries directly" (the message does not expand PEPs; policy enforcement points is the usual expansion). On 2026-10-08 the lead editor of the expected-record draft wrote "Both cases go into the -00." (cases 7 and 8), added that the contributors of the two cases "will be named as contributors for these" (see Disclosure for the credit to the author of this map), and wrote "The draft will be draft-ahuja-schrock-audit-expected-records."; the datatracker page of that name returned 404 and the document search found no draft with "expected-record" in its name on 2026-10-09, so the text is pending and its content was not read. On 2026-10-11 a participant wrote a ninth case, "Refusal with an undetermined cause": "The slot is filled by a record that states whether a refusal came from a check that ran and failed, or from a check that", adding "AAE as published collapses both causes into a single DENY, so this case describes a gap in my own specification as much as anywhere else." Iman Schrock answered the same day (his text read as quoted in the lead editor's reply) that where the declaration requires grounds, "a single DENY cannot tell us whether revocation was established or the status check could not finish", and the lead editor of the expected-record draft wrote the same day "This goes into the -00 as Case 9, just like Iman put it. Lars will be named as a contributor for this case." On 2026-10-12 the same participant wrote that the decision receipt format that he publishes "carries Case 9 as fields". The draft itself is still not found on the datatracker (document search for expected-record and audit-expected, and the page and text URLs of draft-ahuja-schrock-audit-expected-records-00, HTTP 404, 2026-10-13), so cases 7, 8 and 9 are announced for the -00 and not read in it.

**Committed next.**
- BoF session at IETF 127 (14 to 20 November 2026): described as a BoF on the list on 2026-10-10 by a BoF proponent and as the upcoming AUDIT session by a participant; slot or date: not found; the datatracker holds a session request for audit at IETF 127 (requested duration 1:30:00, last modified 2026-10-08) and no timeslot assignment for it is found in the agenda schedule of the meeting (API, 2026-10-13). (undated) [third party] https://mailarchive.ietf.org/arch/msg/audit/2rdEx6WWZAzZDnlsrBNQwIhIv3A/
- Expected-record draft -00, aimed "before the IETF 127 cutoff" (lead editor Sumit Ahuja, co-author Iman Schrock). (undated) [statement] https://mailarchive.ietf.org/arch/msg/audit/RveBSBTLmpMzpU0BGHRfyVnoIt8/

**Boundary.** Scope excludes "the auditing of the underlying AI model, training data, or inference mechanisms" and new identity primitives (issue #7).

**Author participation.** The author of this map took part in issue #35 of mirjak/draft-audit-architecture and the AUDIT list (2026-09-28), and wrote two messages on the AUDIT list on 2026-10-07 proposing and writing the seventh case; see Disclosure.

**Sources.**
- [third party] https://mailarchive.ietf.org/arch/msg/audit/EnHWe1Hv_6XNEzgFEWce_Atp4XA/ (2026-10-06)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/9lVzgPbTpQB_T3aqr3rIZhkD4wg/ (2026-10-06)
- [statement] https://github.com/mirjak/audit-bof-preparation/blob/main/bofreq-kuhlewind-agent-use-of-delegation-and-interaction-traceability-audit.md (2026-10-06)
- [normative] https://github.com/jdrosen/audit-bof-preparation/blob/vcon-alignment/audit-charter.md (2026-10-02)
- [decision] https://github.com/mirjak/audit-bof-preparation/pull/44 (2026-10-03)
- [statement] https://mailarchive.ietf.org/arch/msg/audit/wKCya_8u0bz0HDdlnRHLqAx-fkE (2026-10-03)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/2rdEx6WWZAzZDnlsrBNQwIhIv3A (2026-10-03)
- [third party] https://github.com/mirjak/audit-bof-preparation/pull/61/commits/009b915b00607d8b1f22728896bbb75298353205 (2026-10-08)
- [statement] https://mailarchive.ietf.org/arch/msg/audit/N3Km5fC_LNYdbnYu3rZaFF-lwEk/ (2026-10-13)
- [decision] https://datatracker.ietf.org/group/audit/about/ (2026-10-13)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/PZOOBgEFWK2-cDKgR-6xonM-Smk/ (2026-10-13)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/_88TvnAHVLHCPmta0ONh92wKZvs/ (2026-10-13)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/SLbz1E1imbWTgBsW-APZfQwSXho/ (2026-10-13)
- [third party] https://github.com/mirjak/draft-audit-architecture/blob/main/draft-kuehlewind-audit-architecture.md (2026-10-06)
- [third party] https://github.com/mirjak/audit-bof-preparation/pull/61 (2026-10-06)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/RveBSBTLmpMzpU0BGHRfyVnoIt8/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/u04Utry2tPGRqJ_f-SmRk_EMW88/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/5t31W07Ujanu_0nWkXHRM49DxQY/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/XVTaQ0mqjOt4YHjGjpJPUye3vCY/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/xCNd0SiPlas7ROG5mNLCpYveP8U/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/p_gA6xAzlBBK3DIMl0SFszYUnmE/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/VjCzC9xvzX3jJE5E1SOeTMDeiJ0/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/4GtqigrvVUXbejQP1E69KtuSXdg/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/eX2aQkhOhIKNj93X0UimEGPBklI/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/2SPVhn02fHWjqlihsF1yCvv1mNc/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/YTKRHilHNwQ1a3EgZtu6xMd3WlM/ (2026-10-09)
- [third party] https://mailarchive.ietf.org/arch/msg/audit/MtNPlQiyByNtmp2pVjheQenvXRY/ (2026-10-09)

**Coverage:** see [Evidence](#evidence-ietf-audit).

### IETF DAWN, Discovery of Agents With Names (proposed WG)
<a id="ietf-dawn"></a>

**IETF, charter.** Charter 00-10 has been in external review since 2026-10-09, with comments to the Internet Engineering Steering Group (IESG) due by 2026-10-19 and an IESG telechat listed for 2026-10-22; the Working Group (WG) is "Proposed", and the WG Review announcement of 2026-10-09 says "The IESG has not made any determination yet". The Approve ballot on 00-10, read on the datatracker on 2026-10-14, carries the summary "Has enough positions to pass." with one Yes and one No Objection recorded; the charter has not been recorded as approved, and no WG Action announcement for DAWN is found among the ietf-announce messages up to 2026-10-12 (read 2026-10-13). The announcement names the chairs of the proposed WG: Adrian Farrel and Wes Hardaker. Earlier history: charter 00-09 was on the IESG ballot: on 2026-10-06 one IESG member changed from Block (on 00-08) to No Objection and another voted Yes; on 2026-10-07 one member voted Yes with comments and three recorded No Objection; on 2026-10-08 two more recorded No Objection; the IESG telechat had been set for 2026-10-08. On 2026-10-09 the charter was revised to 00-10 and sent to external review: the datatracker history of that day shows the state changed from "Start Chartering/Rechartering (Internal Steering Group/IAB Review)" to "External Review (Message to Community, Selected by Secretariat)", the "Ready for external review" ballot closed, an "Approve" ballot created and the telechat date changed from 2026-10-08 to 2026-10-22; one IESG member recorded Yes on the new ballot on 2026-10-12. The datatracker pages read on 2026-10-13 show the WG as "Proposed" and charter-ietf-dawn-00-10 in that state, with "On agenda of 2026-10-22 IESG telechat". The Secretariat's announcement "WG Review: Discovery of Agents With Names (dawn)", sent to ietf-announce on 2026-10-09, says "The IESG has not made any determination yet" and asks for comments to the IESG mailing list by 2026-10-19. No WG Action announcement for DAWN is among the ietf-announce messages up to 2026-10-12, the latest of the list on 2026-10-13; a decision on DAWN is not found. (as of 2026-10-14).

**Relevance to commerce.** DAWN would standardise how a client discovers "public properties of AI resources", so it is the IETF venue where a seller's agent surface would be found. The charter gives three deployment contexts with one example each (charter 00-10, read on the datatracker on 2026-10-14): for the local network "within the local network, e.g., discover all agents in this shop;", and for the public Internet "between cooperating parties with trust relationships over the public Internet, e.g., discover all agents of example.org, for all its customers/members.". The WG "will also specify the minimum public discovery information (e.g., type, reachability information, communication protocol, services)."; commerce as a scope item: not found in charter 00-10, read 2026-10-13 (commerce, merchant, transaction, payment and purchase do not occur; "shop" occurs once, in the local network example "within the local network, e.g., discover all agents in this shop;"), nor in charter 00-08, 2026-10-03. On 2026-10-05 the INT Area Director wrote, on a request for a non-WG mailing list for DNS records under underscore labels that carry keys, key commitments or references to them, "While a mailing list will be created, I would like to push back on its name as it misses link to DNS"; the requester proposed the name dns-underscore-keys. An individual survey, draft-jimenez-dawn-discovery-landscape-00 (2026-07-03), compares discovery mechanisms from the IETF, AAIF, 3GPP and open-source projects and lists eight gaps, among them "Well-Known Namespace Pressure"; a text search of it finds no occurrence of AI Catalog, Agentic Resource Discovery (ARD), UCP or commerce (2026-10-06). draft-zhang-dawn-agent-discovery-framework-01 (2026-09-06) proposes a two-layer federated architecture. A second individual draft, draft-moussa-dawn-gap-analysis-01 (Moussa, Akhavain, 2026-06-12), is a gap analysis and applicability statement that maps existing discovery mechanisms to the DAWN problem statement and requirements; a text search of it finds no occurrence of AI Catalog, ARD, UCP or commerce (2026-10-06). draft-kay-dawn-use-cases-01 (2026-09-10) names Agentic Resource Discovery as a possible interface to a provider's catalogue in a broadcast use case and adds: "ARD is an illustrative option; protocol choice remains open." The IETF Chair announced on 2026-10-02 that an INT Area Director resigned from the IESG as of 2026-10-01 and that the other co-AD for the INT area is the primary point of contact for the area; the datatracker lists that Area Director as responsible Area Director (AD) for DAWN (2026-10-03). On 2026-10-07 an IESG member entered a Yes with comments on 00-09 that asks the charter to say that the protocol specifications normatively define the minimum discovery information, that the WG is "expected to converge on one mechanism per deployment context", and that "discovering where a catalog is lives in DAWN, and what a catalog contains doesn't"; the member also asks whether DAWN defines how agents are named, and that DNSSD, DNSOP and AgentProto be named in the coordination text. On the list thread "DAWN Coordination: Discovery Information and Trust Artifact Pointers" Girish Konda wrote on 2026-10-07 that a reference that does not resolve, one blocked by the discovering entity's own retrieval policy, and one that resolves with the record absent are three causes: "All three end as no discovery result, and they have different owners and different retries." On 2026-10-12 a participant who states that they are a co-author of three individual drafts in this space wrote to the IESG on the DAWN list in reply to the WG Review thread "I support chartering DAWN as written in charter-ietf-dawn-00-10", and gave as a reason for keeping identity management of agents out of the first phase "Discovery has to work before anyone argues about who the discovered thing is".

**Committed next.**
- Comments on the proposed charter due to the IESG mailing list, per the WG Review announcement. (2026-10-19) [decision] https://mailarchive.ietf.org/arch/msg/ietf-announce/T8B2tMLk8fU-UE8kASlDIIVLgb4/
- IESG telechat with the DAWN charter on the agenda ("On agenda of 2026-10-22 IESG telechat", datatracker, 2026-10-13). (2026-10-22) [decision] https://datatracker.ietf.org/doc/charter-ietf-dawn/
- Proposed charter milestones (00-10, checked 2026-10-13): terminology June 2027 (optional), protocol specification December 2027, architecture January 2028. (2027-12-31) [normative] https://datatracker.ietf.org/doc/charter-ietf-dawn/

**Boundary.** Out of scope in the initial phase, charter 00-10 (read 2026-10-13): catalogs of capabilities, all communication beyond the initial discovery process, "AI resource indexing and searching across the wider Internet", "Identity management of AI agents, tools, and skills." and trust management beyond secure content exchange between DAWN parties. In scope as a discoverable AI resource: "a service such as a catalog that will further the discovery process".

**Author participation.** The author of this map wrote in the DAWN list thread "DAWN Coordination: Discovery Information and Trust Artifact Pointers", the latest messages on 2026-09-29, on 2026-10-08 (replying to Girish Konda) and on 2026-10-10 (accepting Konda's wording on absence and incomplete results); the reply of Konda adds a third case to the author's second requirement; see Disclosure.

**Sources.**
- [third party] https://datatracker.ietf.org/doc/draft-jimenez-dawn-discovery-landscape/ (2026-10-06)
- [third party] https://www.ietf.org/archive/id/draft-zhang-dawn-agent-discovery-framework-01.txt (2026-10-06)
- [third party] https://datatracker.ietf.org/doc/draft-moussa-dawn-gap-analysis/ (2026-10-06)
- [third party] https://datatracker.ietf.org/doc/draft-kay-dawn-use-cases/ (2026-10-06)
- [decision] https://mailarchive.ietf.org/arch/msg/dawn/8JaXo42KXJo4Z_tacrXT_lOT3gQ/ (2026-10-05)
- [decision] https://mailarchive.ietf.org/arch/msg/ietf-announce/qwarn2pmj9fdyTTd1gBv6QbTXfU/ (2026-10-05)
- [normative] https://datatracker.ietf.org/doc/charter-ietf-dawn/ (2026-10-14)
- [decision] https://datatracker.ietf.org/doc/charter-ietf-dawn/ballot/ (2026-10-14)
- [normative] https://datatracker.ietf.org/wg/dawn/about/ (2026-10-13)
- [decision] https://datatracker.ietf.org/wg/dawn/history/ (2026-10-09)
- [decision] https://mailarchive.ietf.org/arch/browse/ietf-announce/ (2026-10-13)
- [decision] https://datatracker.ietf.org/doc/charter-ietf-dawn/history/ (2026-10-13)
- [statement] https://mailarchive.ietf.org/arch/msg/dawn/3kOpxGr-Hiv_vBH-78W3_FSpD1Q/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/dawn/Ce73ar_tEl0XO2FE41sdNKAGjc8/ (2026-10-08)
- [statement] https://mailarchive.ietf.org/arch/msg/dawn/enY7W1mTMPvP9jnsNI5f-S70uPU/ (2026-10-08)
- [statement] https://mailarchive.ietf.org/arch/msg/dawn/OxEhnEzg4SCzL_LLGY2uEPXgzEo/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/dawn/N9cewk1F_OMxNsKlQKNQsZ068Pg/ (2026-10-08)
- [decision] https://mailarchive.ietf.org/arch/msg/ietf-announce/T8B2tMLk8fU-UE8kASlDIIVLgb4/ (2026-10-14)
- [statement] https://mailarchive.ietf.org/arch/msg/dawn/sdH3BGZF-XAv9ijMRE6p5pN4Id4/ (2026-10-13)
- [third party] https://mailarchive.ietf.org/arch/msg/dawn/QAAfQwe2fvMBTonpP6NgeVFXUvE/ (2026-10-05)
- [third party] https://mailarchive.ietf.org/arch/msg/dawn/Xy97Fv9HzbhYGiCSvpefRYdpUmE/ (2026-10-05)
- [third party] https://mailarchive.ietf.org/arch/msg/dawn/C6Rg1eWrIv9tgjNqh6-ZYaqt6qk (2026-10-03)

**Overlaps:** [w3c-agenticweb-wg](#w3c-agenticweb-wg), [ard](#ard), [a2a-discovery](#a2a-discovery)

**Coverage:** see [Evidence](#evidence-ietf-dawn).

### IETF Web Bot Auth (webbotauth WG)
<a id="ietf-webbotauth"></a>

**IETF, venue.** Active Working Group (WG), listed for coordination by the draft W3C Agentic Web charter; the first WG draft, draft-ietf-webbotauth-httpsig-protocol-00, was adopted on 2026-09-01, and a two-hour session was requested for IETF 127 on 2026-09-15. Implementation reports and proposed edits to the draft were on the list between 2026-10-04 and 2026-10-13. On 2026-10-13 the datatracker still lists draft-ietf-webbotauth-httpsig-protocol-00 (2026-09-01) as the only WG draft, and draft-illyes-webbotauth-cbcp-00 (2026-04-21, expires 23 October 2026) with no later revision. In the thread on updates to the crawler best practices draft a participant posted a revised text proposal on 2026-10-12 for a distinct Signature-Agent URL, key and key directory per crawler purpose, with pull requests in the WG draft repository and as PR #23 of garyillyes/cbcp (open, last update 2026-10-12); PR #22 of the same repository is open (3 comments, last update 2026-10-11). The IETF 127 session is still recorded as requested: no scheduling is found in the list subjects to 2026-10-13. (as of 2026-10-13).

**Relevance to commerce.** The WG standardises cryptographic authentication of automated clients (HTTP message signatures, key directories), which a seller or its content delivery network (CDN) can use to tell which agent is calling. The chairs wrote on 2026-09-01 "Based on the feedback on the mailing list, the WG decided to adopt this draft as a WG document." Participants wrote of merchant-side verifiers: "We operate a production merchant-side verifier for automated commerce traffic (Web Bot Auth, Visa TAP, Google AP2)" (2026-08-03) and "We have implemented and use WBA for bot auth at Shopify in production, and we landed WBA interop for UCP" (2026-08-19). On 2026-10-04 a participant from Auth Your Agent reported an implementation in which a user withdraws an agent by serving its key directory with no keys, cut max-age from 3600 to 300 because "an hour is a long time when the agent has just bought something the user disputes", and asked that verifiers respecting Cache-Control become a normative SHOULD in section 5.5.2 (the draft's appendix C.4 says they "should respect Cache-Control"); Thibault Meunier replied on 2026-10-07 "It seems that the simpler solution would be to prevent the agent from making request in the first place." On 2026-10-08 a participant from Akamai, writing as a verifier, supported moving the C.4 guidance into section 5.5.2 as normative text and proposed "Verifiers SHOULD NOT treat a cached directory as fresh beyond its freshness lifetime as defined in Section 4.2 of [HTTP-CACHE], except as permitted by Section", adding that "short signature expires values (Section 6.3) act faster than any directory TTL". The same day a participant, who publishes per-agent keys as a DNSSEC-signed record set and deactivates an agent by removing its key, wrote that "Section 5.5.2 bounds the wrong thing": where the key set reaches a verifier as a signed artifact (section 5.5.3), "the bound is the Appendix B signature's expires rather than any cache lifetime", and he measured on his apex "TTL 300 seconds against a signature window of 14 days and 1 hour". He proposed a sentence for 5.5.2 on the signature's expires and noted that section 6.3 (removal as the only remedy) and appendix C.12 (manual key rotation as the only revocation mechanism, listed as an anti-pattern) read as a contradiction when taken together. that participant answered on 2026-10-08 that his directories sent max-age=300 while the Appendix B proof on each was valid for 7 days, that he had cut the proof to one hour with a re-signature every 15 minutes, and that he supported the text of the participant who publishes per-agent keys. On 2026-10-09 the same participant wrote that "The revocation thread got me reading the rest of the draft" and proposed for Appendix C.1 to replace "or the key is unknown" with "or the resolved directory does not provide the key", because a verifier could read an unknown key as "the key isn't on my list of bots" and so put a new agent that signs correctly in the same "unverified" outcome as a failed fetch; he also asked whether the draft should say anything about an intermediary that signs all its users' requests with one operator key, where removal under section 6.3 withdraws every user at once. On 2026-10-07 a participant asked whether two bots with different purposes from one operator should have distinct Signature-Agent values and proposed a statement "So it's clear different Signature-Agents need to be used for different purposes / use cases."; he wrote that section 4.1 makes the Signature-Agent URL the identifier. A participant from hCaptcha answered that it is similar to an open proposal, pull request #23 of garyillyes/cbcp, and that some crawl operators already do it, and wrote "I would support this proposal." On 2026-10-08 the same participant from Akamai supported a Signature-Agent per crawler purpose on the cbcp thread, citing that section 6.5 of the protocol draft "already says implementations SHOULD NOT reuse a signing key for different purposes and should use distinct keys and directories" and that "A signature that spans several purposes verifies fine but cannot carry that policy."; he asked that the 6.5 example be broadened to "an operator that runs both crawlers and user-directed agents". The crawler best practices draft (draft-illyes-webbotauth-cbcp, individual) was changed on 2026-10-05 (commit cc9942d of garyillyes/cbcp) and announced on the list the same day: a note that the practices "are intended for crawlers" and are "not necessarily appropriate for all automated clients", particularly "user-directed AI agents"; the requirement levels of the recommended practices changed from MUST to SHOULD; the proposal for a central crawler registry removed; and a Security Considerations section written, which says the opt-outs "are voluntary and do not constitute access control or content security measures" and that the User-Agent "is unauthenticated and trivially spoofed". Pull request #22 of garyillyes/cbcp (the author of this map, opened 2026-09-26, 429 and Retry-After in the back-out logic and a 429 on robots.txt read as unreachable) and #23 (opened 2026-10-06 by a participant, distinct subdomains for different crawl types) were both open on 2026-10-09; the only comment on #22 is of 2026-10-06 and reads "Common Crawl has always treated 429 as unreachable.", and in the announcement Gary Illyes wrote "I'm reviewing the pending PR to explicitly cover HTTP 429 and Retry-After". On 2026-10-05 a participant reported that his REDbot implementation emits signatures only when challenged ("the decision to only emit WBA when challenged") and that his agent-census log analyser sees "a reasonable number of bots emitting WBA by default"; he wrote that this is "an interoperability issue" worth highlighting in the document. Thibault Meunier proposed on 2026-10-07 for section 5.3 "An Origin that expects a signature SHOULD request one from clients that did not provide it." in place of "An Origin MAY choose to request signatures from clients that did not initially provide them.", and a paragraph for appendix C, "Signing conditionally", saying that signing only when an origin asks "adds a round trip, and non-idempotent requests may not be safely retried". On 2026-10-08 a participant answered with text under which an origin that refuses unsigned requests "SHOULD include the Accept-Signature field", and "Origins that do not send Accept-Signature in either of these cases SHOULD NOT rely on the presence of signatures in requests unless there is a"

**Committed next.**
- One session of two hours at IETF 127 (14 to 20 November 2026), requested by the chair on 2026-09-15. (undated) [decision] https://mailarchive.ietf.org/arch/msg/web-bot-auth/w0al4_01_6Evh8AI9wXnbKz6Kc0/

**Boundary.** A co-chair wrote on 2026-08-10, on a human-principal layer, "Please keep topics within our charter".

**Author participation.** The author of this map took part in PR #22 and issue #19 of garyillyes/cbcp (crawler best practices), 2026-09-26, and replied on PR #22 on 2026-10-11; see Disclosure.

**Sources.**
- [normative] https://datatracker.ietf.org/wg/webbotauth/about/ (2026-10-02)
- [statement] https://mailarchive.ietf.org/arch/msg/web-bot-auth/IHIsC9v_WDK_fv2SalA4KeMl8GI (2026-10-03)
- [statement] https://mailarchive.ietf.org/arch/msg/web-bot-auth/kLfrqebxXiW6jcu8hd-f1i7Li6s (2026-10-03)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/5SUKkvPEzPD66hwFexDkP1dl7ko (2026-10-03)
- [normative] https://datatracker.ietf.org/wg/webbotauth/documents/ (2026-10-13)
- [normative] https://datatracker.ietf.org/doc/draft-illyes-webbotauth-cbcp/ (2026-10-13)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/fgokf521lCssTm_abTD7TeHf4AI (2026-10-03)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/hUeE12tWdu6z41pUt3NQs_8AxqI/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/YMTTzbc5SBmi2vXasciXm_Pba7Y/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/sypW8aAD-Y2CqzXqjXZzLHWKWmA/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/tyK4_nyLidnDbbtoyfY7OHagsls/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/pGf24PK_ejMjjWMWi_ZJ9ZK1Yaw/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/fDM_deEVKXJLjgbM83YKAgFfEfc/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/_TOn0TUkZS9ueXlAw6RFgeIUyyI/ (2026-10-09)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/gZ4EOXe5ZdObeM6g6tu9LKH7qOE/ (2026-10-09)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/py8ya2GlxJ4795L5z-seO64DneA/ (2026-10-09)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/AUlWNtUHmoHJkUNvaUOQVjz_6MM/ (2026-10-09)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/LL3NG06lp8PV78XgnwNr0FCax98/ (2026-10-09)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/ztouEfUCpRFHYNYheDeHLzAab_0/ (2026-10-09)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/TRblt-SW4rqes2plYkRQfffiYmM/ (2026-10-09)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/Q44PlkIZJJu2j2NdsHwSIjuNi9c/ (2026-10-09)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/zV3F_1tUvVszGsI6M68r9oSttZg/ (2026-10-09)
- [third party] https://mailarchive.ietf.org/arch/msg/web-bot-auth/_g3XB3ks9_EBHF05ZvWsWVxkD9c/ (2026-10-09)
- [third party] https://github.com/garyillyes/cbcp/commit/cc9942dbebf1e0a52134671872d6992af1589906 (2026-10-09)
- [third party] https://github.com/garyillyes/cbcp/pull/22 (2026-10-09)
- [third party] https://github.com/garyillyes/cbcp/pull/23 (2026-10-09)
- [third party] https://github.com/garyillyes/cbcp/blob/cc9942dbebf1e0a52134671872d6992af1589906/draft-illyes-webbotauth-cbcp.md (2026-10-09)

**Overlaps:** [w3c-agenticweb-wg](#w3c-agenticweb-wg), [kyapay](#kyapay), [mastercard-agent-pay](#mastercard-agent-pay)

**Coverage:** see [Evidence](#evidence-ietf-webbotauth).

### IETF agentproto (Agent Communication Protocols WG)
<a id="ietf-agentproto"></a>

**IETF, charter.** The Internet Engineering Steering Group (IESG) announced on 2026-10-08, 16:55 UTC, "A new IETF WG has been formed in the Applications and Real-Time Area" for Agent Communication Protocols (agentproto), chairs Orie Steele and Leslie Daigle, and names the responsible Area Director. The datatracker page read on 2026-10-09 shows charter-ietf-agentproto-01, state "Approved", Working Group (WG) state "Active", area Applications and Real-Time Area (art), last updated 2026-10-08, and its history records "Charter approved, group active" on 2026-10-08. Reading of 2026-10-13: the datatracker charter page is still headed "Agent Communication Protocols (agentproto) Proposed Charter" while its state is Approved and the group is Active (charter-ietf-agentproto-01, last updated 2026-10-08). The related drafts page lists 15 drafts, among them draft-agentic-ai-usecases-requirements-03 (posted 2026-10-10) and draft-rosenberg-agentproto-usecases-00 (2026-07-04); a revision -04 of the first is not found there. The chairs wrote on the list on 2026-10-12 that "Our goal for this topic is to identify candidate starting points for the Use Cases and Requirements document.", that the discussion "identified two drafts for consideration" (those two) and that "We have useful contributions toward a working group document, but have not yet established which draft should be its starting point." In the same thread an author of the -03 draft proposed, for a -04, the requirements B1-7 (checks on resumption) and B1-8 ("If any check in B1-7 fails or cannot be completed, the dialog is not resumed and the protocol is required to signal the reason."), and CMN-12 ("Before accepting a change to a dialog, a participant is required to be able to verify that the change is authorized at that time."); on 2026-10-13 the same author agreed to add to Section 4.2 "If the outcome cannot be determined, the operation remains unresolved, and resuming the dialog alone does not justify resending it." (proposed text read as quoted in the chairs' message and in the reply). On 2026-10-12 a chair answered a thread on implementation evidence with "Please refrain from sending messages regarding implementations at this time." A session request for agentproto at IETF 127 exists in the datatracker (requested duration 2:00:00, last modified 2026-10-08); no timeslot assignment for it is found in the agenda schedule of the meeting (API, 2026-10-13). (as of 2026-10-13).

**Relevance to commerce.** The charter ("Agent Communication Protocols") defines an "agentic dialog management protocol" of dialog identifiers, lifecycle semantics and propagation of dialog context, with bindings over existing IETF protocols; it "neither replaces application-layer agent communication protocols nor defines a new transport protocol". Commerce, payment, merchant and purchase: not found in charter 00-04 (saved 2026-10-03). The text of the charter on the datatracker page is still headed "Agent Communication Protocols (agentproto) Proposed Charter". Commerce, payment, merchant, purchase and seller: not found in the charter text of the page (2026-10-09). The coordination section reads "This working group is expected to closely coordinate with other related IETF working groups on dependencies of the reference architecture and the agentic dialog management", and lists five groups of venues: "Security: Web Authorization Protocol (OAuth), webbotauth, WIMSE - on identity, authorization, and security considerations.", "Transport: WebTransport, MoQ, QUIC, TSVWG, httpbis - on data transport.", "Discovery and Operations: INT area, OPS area - on agent discovery and operational considerations.", "Evidence and transparency: SCITT, RATS, on software and hardware security." and "Conversational data: vCon - on conversation representation and its relationship to dialog context." On the list thread "Topic: Existing practice, use cases, and deployment models" Iman Schrock proposed on 2026-10-05 for section 3.3.5 of the use cases text: "If a required authorization input cannot be established, preserve that fact separately from an evaluated refusal, even when both lead to local denial."; Girish Konda wrote the same day "An unestablished input is a different fact from a negative one" and pointed to his individual draft draft-konda-agentproto-evaluation-state-00. On 2026-10-07 a participant wrote, without asking to change or delay 00-04, that "accurately recording that an authorization answer was unavailable is not the same thing as making that fact available to the decision that admits the continuation." On 2026-10-08 the responsible Area Director answered three participants on the list: "I believe this matter is one for the working group rather than the charter", adding "The use cases and requirements deliverable is the right home for the more detailed discussion of requirements and corresponding text."; the Internet Architecture Board (IAB) reviewer wrote the same day "The new charter looks good to me." Charter PR #128 (Mallory Knodel, opened 2026-10-02) was closed without a merge on 2026-10-08; the responsible Area Director commented "The PR is a substantial change very late in the process, and the concerns it aims to address were already handled by other, more targeted" The milestones of charter 01 read "Dec 2026 - Adopt an informational use cases draft", "Feb 2027 - Adopt an informational architecture draft", "Mar 2027 - Adopt proposed standard agentic dialog management protocol draft(s)" and "Mar 2028 - Submit agentic dialog management protocol draft(s) to the IESG as proposed standard".

**Committed next.**
- Charter milestones: use cases draft adopted December 2026, architecture February 2027, protocol March 2027; protocol to IESG March 2028. (2026-12-31) [normative] https://datatracker.ietf.org/wg/agentproto/about/

**Boundary.** Out of scope: "Audit data structures and their production, validation, or consumption, though dialog identifiers may be used in auditing."

**Sources.**
- [normative] https://datatracker.ietf.org/doc/charter-ietf-agentproto/ (2026-10-03)
- [normative] https://datatracker.ietf.org/doc/charter-ietf-agentproto/withmilestones-00-04.txt (2026-10-03)
- [decision] https://datatracker.ietf.org/doc/charter-ietf-agentproto/ballot/ (2026-10-03)
- [third party] https://mailarchive.ietf.org/arch/msg/agentproto/XMpnWAx0K2u_ct-wh0sYFcPAiQ8/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/agentproto/Oaunfd9TaD0GPF8cS3W9J7m8CQ8/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/agentproto/H0wOi0o6P_ZgM8wxtF4yr58eCzU/ (2026-10-08)
- [statement] https://mailarchive.ietf.org/arch/msg/agentproto/NvwIOROZ6L4D2GEAo31aeUjsmOs/ (2026-10-08)
- [statement] https://mailarchive.ietf.org/arch/msg/agentproto/jPb6inHUPJjYm5gpAs2TepfKDlU/ (2026-10-08)
- [statement] https://mailarchive.ietf.org/arch/msg/agentproto/lsmWc7vs3FZl4F4GHu3SxU5dz0Q/ (2026-10-08)
- [statement] https://mailarchive.ietf.org/arch/msg/agentproto/LwF8iPHLRP1RrSkIMQH2Om46Fw0/ (2026-10-08)
- [statement] https://mailarchive.ietf.org/arch/msg/agentproto/SaTWzl_Kmrfy2QqdLNp7grfY24Y/ (2026-10-08)
- [statement] https://mailarchive.ietf.org/arch/msg/agentproto/rXv38zFeEwDwrj_XQkt98CDVqX8/ (2026-10-08)
- [decision] https://mailarchive.ietf.org/arch/msg/ietf-announce/olnzT0JibK7hkvy4ZgVlF_nmLa0/ (2026-10-09)
- [normative] https://datatracker.ietf.org/doc/charter-ietf-agentproto/withmilestones-01.txt (2026-10-09)
- [normative] https://datatracker.ietf.org/wg/agentproto/about/ (2026-10-09)
- [decision] https://datatracker.ietf.org/wg/agentproto/history/ (2026-10-09)
- [statement] https://github.com/ietf-artarea/charters/pull/128 (2026-10-09)
- [third party] https://mailarchive.ietf.org/arch/msg/agentproto/Oaunfd9TaD0GPF8cS3W9J7m8CQ8/ (2026-10-09)
- [third party] https://mailarchive.ietf.org/arch/msg/agentproto/O1OU6E7eP0a_DPXoufSJ220Ute4/ (2026-10-13)
- [third party] https://mailarchive.ietf.org/arch/msg/agentproto/EYHBmHhDeFCrHpUqkyW-YKXgicY/ (2026-10-13)
- [third party] https://mailarchive.ietf.org/arch/msg/agentproto/CGc5Kt1qm9Ht8oqy40sWLqAq0IQ/ (2026-10-13)
- [normative] https://datatracker.ietf.org/wg/agentproto/documents/ (2026-10-13)

**Overlaps:** [ietf-audit](#ietf-audit), [ietf-dawn](#ietf-dawn), [ietf-webbotauth](#ietf-webbotauth), [ietf-wimse-aims](#ietf-wimse-aims)

**Coverage:** see [Evidence](#evidence-ietf-agentproto).

### IETF vcon (Virtualized Conversations WG)
<a id="ietf-vcon"></a>

**IETF, charter.** Active working group in the Applications and Real-Time Area, charter-ietf-vcon-01 approved (last updated 2026-03-18); its core draft, draft-ietf-vcon-vcon-core-04 (Standards Track), is dated 2026-09-07. The datatracker lists four charter milestones, dated 2023-12-31 (adopt two drafts) and 2024-06-30 (submit them to the Internet Engineering Steering Group (IESG)), and shows no completion state. The virtual interim of 2026-10-08 (14:00 to 16:00 UTC) was held; the editor's message after it is quoted below. Minutes of that interim: not found in the latest 40 messages of the vcon list (to 2026-10-11), read 2026-10-13; the datatracker interim materials were not read. On 2026-10-13 the datatracker still shows draft-ietf-vcon-vcon-core-04 as the current revision and charter-ietf-vcon-01 as approved. The next virtual interim is on 2026-10-22. Recharter state, 2026-10-13: the datatracker history of the charter shows no revision after charter-ietf-vcon-01 (last action 2026-03-18, a change of Area Director); the recharter text exists only in the repository file changed by PR #37 (merged 2026-10-08) and is not an approved charter. PR #41 on that file is open with no comments. Issue #40 of the core draft repository (opened 2026-10-10 by a participant, no comments) quotes section 2.4 of -04, "Objects that refer to a file which is externally stored from the vCon MUST have the parameters: url, content_hash", and says that references to a streaming-service page or to a recording behind a login cannot be hashed; it reports, as its own measurement on a public dataset, that 4,079 of 8,181 containers fail the schema on that one finding (a figure declared by the issue author, not re-run here). (as of 2026-10-13).

**Relevance to commerce.** The charter defines vCon as a JSON container "to contain and/or reference conversational data, including call style metadata, recordings, data exchanged or presented in the conversations, conversation analysis, transcriptions, translations and annotations", so it is the IETF format for the record of a conversation. On 2026-10-06 a participant proposed on the list to recharter the group to finish the core specification and to add an extension for "ai agent interaction record data"; the charter text he points to adds a baseline format and an "AI Agent Extension" for tool call requests and responses, model details, token usage, prompts and reasoning. The AUDIT effort proposes to treat VCON as its record format for interaction records (see ietf-audit); a related individual draft, draft-rosenberg-cheq-00 (dated 2025-07-24, expiry date 2026-01-25), defines a signed object by which a human confirms an action proposed by an AI agent. On 2026-10-06 the author of this map asked on the list whether the extension's list could name "user instructions and approvals, and references to related records in other protocols"; no reply to that message is among the 6 list messages of 2026-10-06 and 2026-10-07 that were read. On 2026-10-07 the editor of the core draft reported an updated editors copy with "elevation of the party_history events to the top level Events Object" and a Session concept, and that the examples are not yet updated. The editor of the core draft wrote on 2026-10-08, "After discussion in the vCon Interim WG Meeting today, this PR has been merged in to the Charter in the repo."; pull request #37 shows the merge at 15:53 UTC (merge commit 5bd8dbf, file vcon_charter.md in ietf-wg-vcon/draft-ietf-vcon-vcon-core). This is a change to the working group's charter file in its repository; no IESG action on a new charter was found. Pull request #39, a typo fix to the charter, was reported merged on the list on 2026-10-08.

**Committed next.**
- One session of 1.5 hours at IETF 127 (14 to 20 November 2026), requested by a chair on 2026-09-23 (requested, not scheduled). (undated) [decision] https://mailarchive.ietf.org/arch/msg/vcon/8X59uFX_MkTU5Sz2Y5bXio4eJd4/
- Virtual interim meeting 14:00 to 16:00 UTC, agenda "Continue discussion on core document leading up to -05 submission before SFO including redaction PR inclusion. Discuss charter draft status." (2026-10-22) [decision] https://mailarchive.ietf.org/arch/msg/vcon/lnWLdI2xZtUWMMBhIB-pjok72dE/

**Boundary.** The charter lists as out of scope "Real-time streaming or updating of conversational data" and "Definition of a new object security model."

**Author participation.** The author of this map wrote on the vcon list on 2026-10-06, asking whether the recharter text could name user instructions and approvals and references to related records, and opened PR #41 on the charter text on 2026-10-11, announced on the list the same day; see Disclosure.

**Sources.**
- [normative] https://datatracker.ietf.org/doc/charter-ietf-vcon/ (2026-10-13)
- [decision] https://datatracker.ietf.org/wg/vcon/about/ (2026-10-13)
- [decision] https://datatracker.ietf.org/doc/draft-ietf-vcon-vcon-core/ (2026-10-13)
- [third party] https://mailarchive.ietf.org/arch/msg/vcon/O-raCMkzhsmHlOY0Hw48awOViGQ/ (2026-10-06)
- [decision] https://github.com/ietf-wg-vcon/draft-ietf-vcon-vcon-core/pull/37 (2026-10-13)
- [statement] https://mailarchive.ietf.org/arch/msg/vcon/5tu645wIp4SyLHxLXh89fEPigPw/ (2026-10-09)
- [decision] https://datatracker.ietf.org/meeting/upcoming.ics?show=vcon (2026-10-09)
- [decision] https://mailarchive.ietf.org/arch/msg/vcon/lnWLdI2xZtUWMMBhIB-pjok72dE/ (2026-10-09)
- [third party] https://datatracker.ietf.org/doc/draft-rosenberg-vcon-restructure/ (2026-10-13)
- [decision] https://mailarchive.ietf.org/arch/browse/vcon/ (2026-10-13)
- [third party] https://github.com/ietf-wg-vcon/draft-ietf-vcon-vcon-core/issues/40 (2026-10-13)
- [third party] https://github.com/ietf-wg-vcon/draft-ietf-vcon-vcon-core/pull/41 (2026-10-13)
- [decision] https://mailarchive.ietf.org/arch/msg/vcon/rEI9Xl-8pRjNE09yMiL3ppEENAc/ (2026-10-06)
- [statement] https://mailarchive.ietf.org/arch/msg/vcon/uiU5e8IUKRO5cVUiLwyg3hYYFJY/ (2026-10-06)
- [third party] https://www.ietf.org/archive/id/draft-rosenberg-cheq-00.txt (2026-10-06)
- [third party] https://www.ietf.org/archive/id/draft-rosenberg-vcon-restructure-00.txt (2026-10-06)
- [third party] https://mailarchive.ietf.org/arch/msg/vcon/oqJ2wLwEwk044RnhpfOwwosNLSA/ (2026-10-08)
- [statement] https://mailarchive.ietf.org/arch/msg/vcon/LlpZX9eFYQXQJ0HmMfNxzJQhlDI/ (2026-10-08)
- [third party] https://mailarchive.ietf.org/arch/msg/vcon/QzELgHpx8fXANqGtgFEEdve-cQw/ (2026-10-08)

**Overlaps:** [ietf-audit](#ietf-audit), [ap2](#ap2), [ucp](#ucp), [verifiable-intent](#verifiable-intent)

**Coverage:** see [Evidence](#evidence-ietf-vcon).

### Individual IETF drafts on the seller side
<a id="ietf-individual-seller-drafts"></a>

**IETF, work-item.** Three individual Internet-Drafts on the seller side of agent transactions, none adopted by a Working Group (WG): anders merchant-identity-assertions -01, kavian offering-discovery-protocol -01, hood agtp-merchant-identity (-02, an Independent Submission dated 26 May 2026, Informational, expires 27 November 2026; -00 and -02 read). (as of 2026-10-13).

**Relevance to commerce.** draft-anders-merchant-identity-assertions defines a Merchant Identity Assertion, a signed JSON document binding a legal identity to the merchant receiving a payment, so that an automated client can verify the merchant before completing it. draft-kavian-offering-discovery-protocol lets an agent discover a Service's Collections and Offerings and find links to subsequent operations, for "catalogs ranging from a few Offerings to large marketplaces without imposing a universal product taxonomy". draft-hood-agtp-merchant-identity states "This is the merchant identity gap." and treats merchant identity as the receiving side of a purchase.

**Committed next.**
- None declared in the sources read.

**Boundary.** draft-kavian-offering-discovery-protocol declines a product identifier scheme: its discovery is "without imposing a universal product taxonomy".

**Sources.**
- [third party] https://datatracker.ietf.org/api/v1/doc/document/?name=draft-anders-merchant-identity-assertions&format=json (2026-10-02)
- [third party] https://datatracker.ietf.org/api/v1/doc/document/?name=draft-kavian-offering-discovery-protocol&format=json (2026-10-02)
- [third party] https://www.ietf.org/archive/id/draft-hood-agtp-merchant-identity-00.txt (2026-10-02)
- [third party] https://www.ietf.org/archive/id/draft-hood-agtp-merchant-identity-02.txt (2026-10-13)

**Overlaps:** [kyapay](#kyapay), [ucp](#ucp), [ard](#ard), [ietf-dawn](#ietf-dawn)

**Coverage:** see [Evidence](#evidence-ietf-individual-seller-drafts).

### GS1-Conformant Resolver Standard 1.2.1
<a id="gs1-conformant-resolver"></a>

**GS1, specification.** Release 1.2.1 ratified August 2026 (standards page and PDF print no day); the archive page on ref.gs1.org lists "Published 19 August 2026". (as of 2026-10-13).

**Relevance to commerce.** The standard defines how a GS1 Digital Link URI, which carries a product or location key such as a GTIN or a Global Location Number (GLN), is resolved to related information sources. The query string "carries attributes of the identified entity and does not form part of the entity's identifier"; for an invalid request URI "the resolver SHALL respond with an HTTP response code of 400 (Bad Request)", and for a valid URI with no information it "SHALL return a simple 404 Not Found response" (sections 2.12, 2.4.1). A conformant resolver publishes a Resolver Description File at /.well-known/gs1resolver.

**Committed next.**
- None declared in the sources read.

**Boundary.** Out of scope: identical targets or linksets across resolvers, and any particular behaviour for query string parameters.

**Sources.**
- [normative] https://ref.gs1.org/standards/resolver/ (2026-10-13)
- [normative] https://ref.gs1.org/standards/resolver/1.2.1/GS1_Conformant_Resolver_standard_i1.2.1-r-2026-08-07 (2026-10-03)
- [decision] https://ref.gs1.org/standards/resolver/archive (2026-10-13)

**Overlaps:** [w3c-did-resolution](#w3c-did-resolution), [untp-identity-resolver](#untp-identity-resolver), [gs1-digital-link](#gs1-digital-link)

**Coverage:** see [Evidence](#evidence-gs1-conformant-resolver).

### UN Transparency Protocol, Identity Resolver
<a id="untp-identity-resolver"></a>

**UN/CEFACT, specification.** Latest stable version 0.7.0 (GitLab tag of 2026-05-04); the 0.7.0 page says the team "expects to release UNTP version 1.0", without a date. (as of 2026-10-13).

**Relevance to commerce.** The Resolver Workflow section lists, among "some common conditions that a link resolver service SHOULD manage consistently", "When there is no data for the requested entity ID."; not found in its prose, 2026-10-02: the response for that case. The 0.7.0 OpenAPI artefact defines 404 ("No link resolver entry found for this identifier.") and 400 for a path that does not match the registered scheme patterns. The specification describes the gtr Uniform Resource Name (URN) namespace of the UN global trust register as "IANA registration pending" (see un-gtr-urn).

**Committed next.**
- release of UNTP version 1.0 (no date given) (undated) [statement] https://untp.unece.org/docs/0.7.0/specification/IdentityResolver

**Boundary.** The internal workflow of an identity resolver is not defined; the specification lists conditions a link resolver should handle consistently.

**Sources.**
- [normative] https://untp.unece.org/docs/0.7.0/specification/IdentityResolver (2026-10-02)
- [normative] https://untp.unece.org/artefacts/schema/v0.7.0/idr/idr-api.html (2026-10-02)
- [decision] https://untp.unece.org/versions (2026-10-13)

**Overlaps:** [gs1-conformant-resolver](#gs1-conformant-resolver), [un-gtr-urn](#un-gtr-urn)

**Coverage:** see [Evidence](#evidence-untp-identity-resolver).

### CEN/CENELEC JTC 24 Digital Product Passport standards (EN 18216 to EN 18246)
<a id="cen-clc-jtc24-dpp"></a>

**Other standards bodies, specification.** Eight horizontal standards; six cited in the Official Journal of the EU according to the CEN-CENELEC page of 2026-07-15 (page re-read on 2026-10-13, unchanged); the two not cited are EN 18239 and EN 18246, and their status is not read. The Official Journal itself was not read: EUR-Lex answered HTTP 202 without content on 2026-10-13. (as of 2026-10-13).

**Relevance to commerce.** The eight standards cover data exchange protocols (EN 18216), unique identifiers (EN 18219), data carriers (EN 18220), data storage (EN 18221), APIs for lifecycle management and searchability (EN 18222), system interoperability (EN 18223), access rights and security (EN 18239) and data authentication and integrity (EN 18246). Two concern how a product is addressed and found: "unique identifiers" (EN 18219) and "searchability" (EN 18222).

**Committed next.**
- additional standards by product-specific Technical Committees under the 5-year ESPR work plan 2025-2030 (undated) [statement] https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-07-15-dpp/

**Boundary.** Horizontal standards only; product-specific requirements are left to product-specific Technical Committees.

**Sources.**
- [statement] https://www.cencenelec.eu/news-events/news/2026/en-in-the-spotlight/2026-07-15-dpp/ (2026-10-02)
- [statement] https://ref.gs1.org/docs/2026/GS1-and-SDOs (2026-10-02)

**Overlaps:** [gs1-conformant-resolver](#gs1-conformant-resolver), [untp-identity-resolver](#untp-identity-resolver)

**Coverage:** see [Evidence](#evidence-cen-clc-jtc24-dpp).

### A2A protocol, agent discovery
<a id="a2a-discovery"></a>

**AAIF, work-item.** A2A registers /.well-known/agent-card.json for a single AgentCard; proposals for hosts serving several agents (PR #2240, issues #2276 and #2248) were open on 2026-10-13: PR #2240 and issue #2248 have no comment, and issue #2276 has no comment after 2026-10-02. (as of 2026-10-13).

**Relevance to commerce.** PR #2240 proposes /.well-known/ai-catalog.json as the "Preferred" discovery mechanism, and issue #2276 proposes /.well-known/agent-card-list.json for providers serving multiple agents. The documentation (docs/topics/agent-discovery.md on main) says "The current A2A specification does not prescribe a standard API for curated registries."; AI Catalog and Agentic Resource Discovery (ARD) not found in that file (2026-10-03). darrelmiller wrote on issue #1807 (2026-05-12) "Rather than layering trust information into the AgentCard, we are attempting to use AI Catalog to contain that kind of trust information." HTTP Archive custom-metrics PR #176, merged on 2026-10-07, adds a metric for "/.well-known/agent-card.json" to track its presence and key metadata.

**Committed next.**
- None declared in the sources read.

**Boundary.** A maintainer wrote on PR #418 that the A2A working group "will not be building any kind of registry standard".

**Author participation.** The author of this map took part in issue #2276 (two comments, 2026-10-02); see Disclosure.

**Sources.**
- [decision] https://aaif.io/blog/a2a-joins-aaif (2026-10-18)
- [third party] https://github.com/a2aproject/A2A/pull/2240 (2026-10-02)
- [statement] https://github.com/a2aproject/A2A/pull/418 (2026-10-03)
- [statement] https://github.com/a2aproject/A2A/issues/1807 (2026-10-03)
- [normative] https://github.com/a2aproject/A2A/blob/main/docs/topics/agent-discovery.md (2026-10-13)
- [decision] https://github.com/HTTPArchive/custom-metrics/pull/176 (2026-10-08)
- [decision] https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents (2026-10-03)

**Overlaps:** [ard](#ard), [lf-ai-catalog](#lf-ai-catalog), [a2a-core](#a2a-core)

**Coverage:** see [Evidence](#evidence-a2a-discovery).

### AAIF Agentic Commerce Working Group
<a id="aaif-wg-agentic-commerce"></a>

**AAIF, venue.** Charter approved 2026-05-15; Capability Map being built from contributed inputs. Charter targets: Capability Map (2026-09-01) and Recommendations to the Technical Committee on hosted projects (2026-10-01); both dates have passed, and no Capability Map or Recommendations document is found in the repository on 2026-10-13 (root: README.md, charter.md, reporting/; commits to 2026-10-12). Chairs per the August report: Ilya Grigorik (Shopify) and Rahul Bansal (OpenAI). The August report (merged by PR #7 on 2026-10-12) says the x402 session "advanced the payment layer of the Capability Map" and lists no decision needed from the Technical Committee; the report for September is opened as issue #9 (2026-10-12), covering deep dives on onX, MPP and the UCP August release. (as of 2026-10-13).

**Relevance to commerce.** The group aligns open specifications for commerce workflows carried out by AI agents; the charter says "The Working Group does not author competing commerce protocols" and lists UCP, ACP, Mastercard Verifiable Intent and Visa TAP as "Source Projects (primary inputs to the Capability Map)". The Running Notes record on product discovery (2026-04-01) "Finding products is different from finding where to search". The charter lists "Open Meetings: No". In issue #5 (Capability Map input: cross-boundary evidence and audit row) the author of draft-krausz-verification-state, who discloses it, wrote on 2026-10-08 that its v_verdict "carries verified, contradicted, indeterminate or not_evaluated" and that "a mapping would need to preserve the distinction between an inconclusive evaluation and one that did not occur."

**Committed next.**
- None declared in the sources read.

**Boundary.** Out of scope: new commerce protocols, internals of any specific commerce system, end-user UI, marketplace design, hardware.

**Author participation.** The author of this map wrote on the public working group mailing list on 2026-10-12, accepting a 30-minute slot, wrote again in the same thread on 2026-10-14, and gave a presentation of the map at the working group call of 2026-10-14; see Disclosure.

**Sources.**
- [normative] https://github.com/aaif/wg-agentic-commerce/blob/main/charter.md (2026-10-02)
- [normative] https://github.com/aaif/wg-agentic-commerce/blob/main/README.md (2026-10-03)
- [statement] https://docs.google.com/document/d/1Xe0R8xP3w2nCVvC8IScMyS_dl5PkBRzRirptBUHyfV0/edit (2026-10-03)
- [statement] https://github.com/aaif/wg-agentic-commerce/pull/7 (2026-10-02)
- [third party] https://github.com/aaif/wg-agentic-commerce/issues/5#issuecomment-6052049160 (2026-10-08)
- [third party] https://datatracker.ietf.org/doc/draft-krausz-verification-state/ (2026-10-08)
- [statement] https://github.com/aaif/wg-agentic-commerce/blob/main/reporting/2026-08-report.md (2026-10-13)
- [statement] https://github.com/aaif/wg-agentic-commerce/issues/9 (2026-10-13)

**Overlaps:** [ucp](#ucp), [aaif-structure](#aaif-structure), [visa-tap](#visa-tap), [verifiable-intent](#verifiable-intent)

**Coverage:** see [Evidence](#evidence-aaif-wg-agentic-commerce).

### MCP Server Cards (ext-server-card, SEP-2127)
<a id="mcp-server-card"></a>

**AAIF, specification.** Experimental extension of MCP: the README of the extension repository still reads "not an accepted or official MCP extension" (2026-10-13). SEP-2127 (PR #2127, "MCP Server Cards - HTTP Server Discovery", Extensions Track) was merged on 2026-10-06 (14:43 UTC, merge commit 0a11bf6) by a maintainer of the MCP repository; the Specification Enhancement Proposal (SEP) file, read 2026-10-13, carries "Status: Final" and says the full extension specification stays in the extension repository, graduating to a repository named ext-server-card on acceptance. The last commit of the extension repository on main is of 2026-08-12 (PR #47); latest activity read: issue #30 (2026-10-10, 9 comments). (as of 2026-10-13).

**Relevance to commerce.** A Server Card is "a static metadata document that describes a remote MCP server enough for clients to discover and connect to it"; cards "intentionally omit primitive listings (tools, resources, prompts)". docs/discovery.md says clients performing domain-level discovery SHOULD attempt to retrieve /.well-known/ai-catalog.json, whose entries of type application/mcp-server-card+json point to the cards. Commerce metadata was kept out of the card: in issue #27 (closed 2026-06-13) a member of the modelcontextprotocol organisation (GitHub author association MEMBER, read 2026-10-13) answered "we do not intend to introduce MCP-specific patterns (like `_meta`) into the MCP Catalog"; SEP-2007 (payment support) was closed 2026-06-24 as "dormant".

**Committed next.**
- Roadmap (PR #47, merged 2026-08-12): graduate the Server Card as an official MCP extension, then static primitives (#30) and authentication (#13). (undated) [statement] https://github.com/modelcontextprotocol/ext-server-card/pull/47
- Notes of 2026-07-20: "Nested catalog and Link header features deferred to after release." (undated) [statement] https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/3115

**Boundary.** The README says a Server Card "describes remote connectivity only"; local installation metadata stays in the MCP Registry server.json.

**Sources.**
- [statement] https://aaif.io/projects (2026-10-18)
- [normative] https://github.com/modelcontextprotocol/ext-server-card (2026-10-13)
- [normative] https://github.com/modelcontextprotocol/ext-server-card/blob/main/docs/discovery.md (2026-10-02)
- [statement] https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2127 (2026-10-13)
- [statement] https://github.com/modelcontextprotocol/ext-server-card/pull/47 (2026-10-13)
- [decision] https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/seps/2127-mcp-server-cards.md (2026-10-13)
- [third party] https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/3115 (2026-10-03)
- [third party] https://github.com/modelcontextprotocol/ext-server-card/issues/27 (2026-10-03)

**Overlaps:** [lf-ai-catalog](#lf-ai-catalog), [a2a-discovery](#a2a-discovery), [ard](#ard), [mcp-core](#mcp-core)

**Coverage:** see [Evidence](#evidence-mcp-server-card).

### AI Catalog (Agent Card Working Group)
<a id="lf-ai-catalog"></a>

**Linux Foundation, specification.** Pre-v1 specification in "a temporary working repo maintained by the Linux Foundation", governed by a Technical Steering Committee with four initial seats. The well-known path is optional by design (ADR-0011). On 2026-10-13 the README of main still says "This is a temporary working repo maintained by the Linux Foundation" and "This project will be moved to a permanent location a later date with a permanent governance model."; the last commit of main is of 2026-10-08 (PR #119, implementation classifications); issue #46 (project location) was closed as completed on 2026-10-03 without a comment. PR #110 (did:web verification of signed Entry Trust Manifests) was merged on 2026-10-01. (as of 2026-10-13).

**Relevance to commerce.** ADR-0011 (accepted 2026-04-02) says a well-known URI "should be registered as a conventional discovery location" but "is not mandatory", so catalogues may be served from any URL. Publisher identity is the most developed theme: urn:air anchored to a domain and did:web verification of signed trust manifests (PR #110, merged 2026-10-01), whose text says "This establishes publisher-domain control, not publisher reputation." Terms of service and privacy policy URLs are fields of the trust manifest (termsOfServiceUrl, privacyPolicyUrl); the maintainers' wording on Agentic Resource Discovery (ARD) is "Documents the decision to loosely couple ARD and AI-Catalog" (PR #77).

**Committed next.**
- Technical Steering Committee (TSC) vote on the urn:air naming (issue #59): "We may require a TSC vote to move forward." (undated) [statement] https://github.com/Agent-Card/ai-catalog/issues/59
- README: "This project will be moved to a permanent location a later date with a permanent governance model." (undated) [normative] https://github.com/Agent-Card/ai-catalog/blob/main/README.md

**Boundary.** Access and monetization signalling is directed to an extension: "I would fully support this as an extension." (issue #83)

**Author participation.** The author of this map commented on PR #117 of the AI Catalog repository on 2026-10-06, on the policy URLs of the extension; see Disclosure.

**Sources.**
- [normative] https://github.com/Agent-Card/ai-catalog/blob/main/README.md (2026-10-13)
- [normative] https://github.com/Agent-Card/ai-catalog/blob/main/GOVERNANCE.md (2026-10-13)
- [normative] https://github.com/Agent-Card/ai-catalog/blob/main/adr/0011-no-well-known-requirement.md (2026-10-02)
- [decision] https://github.com/Agent-Card/ai-catalog/pull/110 (2026-10-13)
- [statement] https://github.com/Agent-Card/ai-catalog/blob/main/adr/0021-separate-artifact-identity-from-registry-coordinates.md (2026-10-13)
- [decision] https://github.com/Agent-Card/ai-catalog/pull/77 (2026-10-03)
- [third party] https://github.com/Agent-Card/ai-catalog/issues/83 (2026-10-03)
- [third party] https://github.com/Agent-Card/ai-catalog/issues/59 (2026-10-03)

**Overlaps:** [ard](#ard), [a2a-discovery](#a2a-discovery), [mcp-server-card](#mcp-server-card)

**Coverage:** see [Evidence](#evidence-lf-ai-catalog).

### x402
<a id="x402"></a>

**Linux Foundation, specification.** Open payment protocol under the x402 Foundation (Linux Foundation): intent announced 2026-04-02; operational launch and completed contribution by Coinbase announced 2026-07-14, with 40 member organisations at launch. On 2026-10-13 main is at commit 6c470a8 and the core specification header reads "Protocol Version: 2" (specs/x402-specification-v2.md); no release is listed on GitHub (not found, 2026-10-13). The file ROADMAP.md, which read "(update coming soon)" on 2026-10-03, was removed from main on 2026-10-13 by PR #3789, "chore: remove outdated ROADMAP.md and PROJECT-IDEAS.md". (as of 2026-10-13).

**Relevance to commerce.** The README says "x402 is an open standard for internet native payments."; the server answers 402 with a PAYMENT-REQUIRED header, the client replies with PAYMENT-SIGNATURE, and an http-message-signatures extension identifies the paying agent. The offer-and-receipt extension lets the server "cryptographically commit to the payment terms it presents in" accepts[] (the payment terms of the offer, not the commercial terms of the sale) and sign a receipt; it says "Wire shape and field placement are not considered stable". The FAQ describes the exact scheme as a push payment, "irreversible once executed".

**Committed next.**
- None declared in the sources read.

**Boundary.** The FAQ answers "Not natively." on credit-card deposits, placing fiat rails outside the protocol.

**Sources.**
- [decision] https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol (2026-10-03)
- [decision] https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications (2026-10-03)
- [normative] https://github.com/x402-foundation/x402/blob/main/TSC.md (2026-10-13)
- [normative] https://github.com/x402-foundation/x402/blob/main/specs/extensions/extension-offer-and-receipt.md (2026-10-13)
- [decision] https://github.com/x402-foundation/x402/pull/3789 (2026-10-13)
- [normative] https://github.com/x402-foundation/x402/blob/main/python/legacy/README.md (2026-10-03)
- [third party] https://github.com/x402-foundation/x402/pull/1311 (2026-10-03)
- [normative] https://github.com/x402-foundation/x402/blob/main/docs/faq.md (2026-10-03)

**Overlaps:** [acp](#acp), [ucp](#ucp), [verifiable-intent](#verifiable-intent), [ietf-httpauth-payment](#ietf-httpauth-payment)

**Coverage:** see [Evidence](#evidence-x402).

### Agentic Resource Discovery (ARD)
<a id="ard"></a>

**Independent, specification.** Specification v0.91 on main (header "Status: Proposal", dated 2026-08-26; header unchanged and last change to spec/ard.md on 2026-10-12, read 2026-10-13); no tag or release in ard-spec (not found, 2026-10-13); Maintainers decide by majority vote; an Oversight Board (Google, Hugging Face, Microsoft, Amazon, Cisco) is published. On 2026-10-11 and 2026-10-12 the maintainers merged PRs #97, #99, #104, #105, #106 and #80 (namespace segments in Appendix C, base URL and search endpoint in section 5.3, ADR 0010, recognized media types in section 3.3, CDDL for explore facets, attestation scopes in section 4.5.2). (as of 2026-10-13).

**Relevance to commerce.** Agentic Resource Discovery (ARD) defines a manifest of typed entries (A2A agent cards, MCP servers, other resources by media type): "A consumer resolving a domain's entries MUST fetch /.well-known/ard.json"; "a publisher on the predecessor path SHOULD move to ard.json". The chair recorded in issue #61 (2026-07-09): "We decided that at least for now, we will only have a loose coupling between ARD entries and ai-catalog entries." The decision is recorded as ADR 0010 (status Accepted, meeting of 2026-07-09, merged by PR #104 on 2026-10-11): "Loose coupling between ARD and `ai-catalog`". Commerce enters through a "local-business storefront" example (PR #60); issue #20 says "Resources discovered via ARD may require payment or have access restrictions." and "Deferred from v0.9." Lighthouse PR #17295 (merged on 2026-10-09) makes the robots-txt and llms-txt audits fail on HTTP 429, because Google's robots.txt specification makes an exception for 429 "to be treated as a server error"; on PR #17260 (ard-schema) a reviewer wrote on 2026-10-07 "status code 200 is too restrictive. See how other audits (robots-txt, llms-txt) handle status codes."

**Committed next.**
- Lookup by identifier (PR #74, still open on 2026-10-13): "We will merge this into main and ensure it gets synced into the v0.91 draft structure as well." (undated) [statement] https://github.com/ards-project/ard-spec/pull/74
- Neutral host: "a decision for **roughly twelve months out**, not now." (undated) [normative] https://agenticresourcediscovery.org/governance/

**Boundary.** Payment and access signalling were "Deferred from v0.9." (issue #20, still open on 2026-10-13). A maintainer wrote there on 2026-10-11 "With v0.91 and #86 merged, the core mechanism for access and monetization signaling is now in place", carried as namespaced JSON-LD terms rather than payment fields in the base entry; on issue #78 (discovery results and referrals must not confer contact or invocation authority, open) a maintainer wrote "discovery is not authorization" and proposed an editorial clarification in section 3.6 without new normative rules (2026-10-11).

**Author participation.** The author of this map took part in Lighthouse audit issue #17251 on ARD support (closed as completed on 2026-10-09), PR #17260, issue #17271 and PR #17272, and opened PR #100 on ard-spec (merged on 2026-10-11, with a comment of the author on 2026-10-10); see Disclosure.

**Sources.**
- [normative] https://github.com/ards-project/ard-spec/blob/main/spec/ard.md (2026-10-13)
- [normative] https://agenticresourcediscovery.org/governance/ (2026-10-13)
- [statement] https://github.com/ards-project/ard-spec/issues/61 (2026-10-03)
- [third party] https://github.com/ards-project/ard-spec/issues/20 (2026-10-13)
- [third party] https://github.com/GoogleChrome/lighthouse/pull/17295 (2026-10-13)
- [third party] https://github.com/GoogleChrome/lighthouse/pull/17260#discussion_r4210867267 (2026-10-08)
- [decision] https://github.com/ards-project/ard-spec/blob/main/adr/0010-ard-and-ai-catalog-loose-coupling.md (2026-10-13)
- [statement] https://github.com/ards-project/ard-spec/issues/78 (2026-10-13)
- [third party] https://github.com/ards-project/ard-spec/pull/60 (2026-10-03)
- [third party] https://github.com/ards-project/ard-spec/pull/74 (2026-10-03)

**Overlaps:** [lf-ai-catalog](#lf-ai-catalog), [a2a-discovery](#a2a-discovery), [ietf-dawn](#ietf-dawn), [ucp](#ucp)

**Coverage:** see [Evidence](#evidence-ard).

### Browser vendor positions on WebMCP (WebKit, Mozilla, Chrome, Edge)
<a id="browsers-webmcp"></a>

**Independent, position.** WebKit position issue #670 closed 2026-06-11 as "position: oppose"; Mozilla #1412 closed 2026-08-05 as "position: neutral". Chrome early preview 2026-02-10; Edge blog of 2026-09-21: implementation "is ready for testing". (as of 2026-10-13).

**Relevance to commerce.** WebMCP lets a page expose tools to browsing agents; Chrome describes it as "a standard way for exposing structured tools, ensuring AI agents can perform actions on your site with increased speed, reliability, and precision". The WebKit reviewer wrote on 2026-06-03 "WebKit is **opposed** to this proposal due to the following concerns:", among them that "it has no consent or reversibility model for consequential actions". The Mozilla reviewer proposed a neutral position, writing that "in an adversarial setting there is a risk that sites will provide tools that do not match the experience of a user on the page". PayPal's blog of 2026-09-16 says it is "extending WebMCP support through the PayPal JavaScript SDK" for Store Sync merchants; the agent can search, prepare the cart and initiate checkout, and "The buyer is then handed off to PayPal to sign in, choose or confirm a funding source, review the transaction, and approve payment." PayPal reports, as its own results of a small sandbox benchmark: "Approximately 4.6 times less costly in model-inference usage", "Approximately twice as fast at the median", and "three structured tool calls via WebMCP instead of more than 30 interface-interaction steps" (self-reported). Shopify's developer changelog of 2026-09-28 says "Browser agents can now read and update Shopify checkouts using WebMCP tools for checkout", with get_checkout, update_checkout and complete_checkout ("Submit checkout after buyer confirmation"); the tools "don't expose a new API or require merchant configuration". The Checkout WebMCP documentation says "Before you call complete_checkout, show the buyer the current order and total, and get their permission to place it. WBA and ready_for_complete don't grant it."

**Committed next.**
- Mozilla reviewer: "willing to come back to revisit it once there is more evidence of how it will be used by sites" (undated) [statement] https://github.com/mozilla/standards-positions/issues/1412#issuecomment-4593221809

**Boundary.** The positions concern WebMCP and not MCP: the Mozilla reviewer's text says "There is no MCP here."

**Sources.**
- [statement] https://github.com/WebKit/standards-positions/issues/670 (2026-10-13)
- [statement] https://github.com/mozilla/standards-positions/issues/1412 (2026-10-13)
- [decision] https://developer.chrome.com/blog/webmcp-epp (2026-10-13)
- [decision] https://blogs.windows.com/msedgedev/2026/09/21/new-in-edge-for-developers-create-better-components-and-make-your-site-agent-ready/ (2026-10-13)
- [statement] https://developer.paypal.com/community/blog/WebMCP_PayPal_Agent_Ready/ (2026-10-08)
- [statement] https://shopify.dev/changelog/posts/webmcp-support-for-checkout (2026-10-08)
- [normative] https://shopify.dev/docs/agents/carts-and-checkout/checkout-webmcp (2026-10-08)

**Overlaps:** [w3c-webmcp-cg-report](#w3c-webmcp-cg-report), [mcp-core](#mcp-core), [w3c-agenticweb-wg](#w3c-agenticweb-wg)

**Coverage:** see [Evidence](#evidence-browsers-webmcp).

### schema.org open issues relevant to agents, bookings, product and establishment identity
<a id="schemaorg-open-agent-commerce-items"></a>

**Independent, work-item.** Issues #4824, #4786, #4828, #4774 and #4928 were open on 2026-10-13 (issue #4928, 1 comment, last activity 2026-10-08). The Digital Product Passport vocabulary (PR #4871, merged 2026-08-17) is the file data/ext/pending/issue-4870.ttl on main as read on 2026-10-03; the release notes of V30.1 (2026-09-16) read "Add vocabulary to support discovery of EU Digital Product Passports" and attribute to PR #4871 the class DigitalProductPassport and the property hasDigitalProductPassport for use on Product and Offer (release notes read 2026-10-14), and the term page schema.org/hasDigitalProductPassport exists (2026-10-13). (as of 2026-10-13).

**Relevance to commerce.** Issue #4824 proposes a direct booking channel for LodgingBusiness; the author of the Vacation Rental Protocol commented on 2026-09-02: "For machine consumers that distinction should be verifiable, not only declared." PR #4871 links Product, and also Offer, to a passport by hasDigitalProductPassport, a sub-property of hasCertification; a reviewer wrote "Privacy will also need some consideration if "product" passports are not to become proxy identifiers for their holders, traders and purchasers." PR #4861 (2026-07-23) says "This puts several pending schema types and properties into GA (General Availability)."

**Committed next.**
- None declared in the sources read.

**Boundary.** Issue #3303 (bed and occupancy on Accommodation) was closed as not_planned on 2026-05-13.

**Author participation.** The author of this map opened issue #4928 (public registration numbers of accommodations); see Disclosure.

**Sources.**
- [third party] https://github.com/schemaorg/schemaorg/issues/4824 (2026-10-02)
- [third party] https://github.com/schemaorg/schemaorg/issues/4774 (2026-10-02)
- [decision] https://github.com/schemaorg/schemaorg/pull/4871 (2026-10-02)
- [decision] https://github.com/schemaorg/schemaorg/pull/4861 (2026-10-03)
- [normative] https://schema.org/docs/releases.html (2026-10-14)
- [third party] https://github.com/schemaorg/schemaorg/issues/4870 (2026-10-03)

**Overlaps:** [w3c-agenticweb-wg](#w3c-agenticweb-wg), [w3c-gs1-ecommerce-workshop](#w3c-gs1-ecommerce-workshop), [gs1-conformant-resolver](#gs1-conformant-resolver), [schemaorg-baseline](#schemaorg-baseline)

**Coverage:** see [Evidence](#evidence-schemaorg-open-agent-commerce-items).

### Agent Payments Protocol (AP2)
<a id="ap2"></a>

**Industry, specification.** Donated by Google to the FIDO Alliance on 2026-04-28 (Google: "We’re donating Agent Payments Protocol to the FIDO Alliance"); standardisation continues in the FIDO Payments and Agentic Authentication Technical Working Groups. The reference repository stays in the GitHub organisation google-agentic-commerce (Apache-2.0); latest release v0.2.0 of 2026-04-28, which "focuses on providing Human Not Present flows". (as of 2026-10-18).

**Relevance to commerce.** AP2 is available as an extension for A2A and for UCP; its objects are mandates, signed Verifiable Digital Credentials, and the FIDO blog of 2026-05-26 names "Checkout Mandate: This captures the details about and conditions on what the user wants to buy." and "Payment Mandate : This captures the details about and conditions on how the user wants to pay (amount, instrument, timing)." The docs say the Checkout Mandate is shared with the merchant, so the seller is a recipient of the user's signed purchase terms. The record the other way, the Mandate Receipt that the Verifier signs, is described with a `result` field in docs/ap2/agent_authorization.md and with a `status` field in the normative schemas, at the same commit e1ea56d (see issue #374 in the open proposals). UCP's AP2 mandates extension has businesses embed a signature over the checkout terms.

**Committed next.**
- Standardisation continues in the FIDO Agentic Authentication and Payments Technical Working Groups (repository docs) (undated) [statement] https://github.com/google-agentic-commerce/AP2/blob/main/docs/index.md
- The FIDO Alliance will provide reports as its agentic workstreams progress (undated) [decision] https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/

**Boundary.** The docs index (docs/index.md at commit e1ea56d, the head of main on 2026-10-13) says the initial version supports pull payment methods such as credit and debit cards and that the roadmap includes e-wallets, push payments such as real-time bank transfers, and digital currencies; docs/index.md describes "the initial version" as supporting these payment methods, and the latest release is v0.2.0 (2026-04-28).

**Sources.**
- [decision] https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/ (2026-10-18)
- [decision] https://github.com/google-agentic-commerce/AP2/releases/tag/v0.2.0 (2026-10-13)
- [normative] https://github.com/google-agentic-commerce/AP2/blob/main/docs/index.md (2026-10-13)
- [decision] https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/ (2026-10-03)
- [statement] https://fidoalliance.org/building-the-trust-layer-for-agentic-payments-with-ap2-and-verifiable-intent/ (2026-10-03)
- [third party] https://github.com/google-agentic-commerce/AP2/issues/374 (2026-10-13)
- [normative] https://github.com/google-agentic-commerce/AP2/blob/e1ea56db72a6385bce3e5c1112b3a56ce60acb43/docs/ap2/specification.md (2026-10-13)
- [normative] https://github.com/google-agentic-commerce/AP2/blob/e1ea56db72a6385bce3e5c1112b3a56ce60acb43/docs/ap2/agent_authorization.md (2026-10-05)
- [normative] https://github.com/google-agentic-commerce/AP2/blob/e1ea56db72a6385bce3e5c1112b3a56ce60acb43/code/sdk/schemas/ap2/checkout_receipt.json (2026-10-05)
- [normative] https://github.com/google-agentic-commerce/AP2/blob/e1ea56db72a6385bce3e5c1112b3a56ce60acb43/docs/ap2/flows.md (2026-10-13)
- [normative] https://github.com/google-agentic-commerce/AP2/blob/e1ea56db72a6385bce3e5c1112b3a56ce60acb43/docs/ap2/checkout_mandate.md (2026-10-14)
- [normative] https://github.com/google-agentic-commerce/AP2/blob/main/CONTRIBUTING.md (2026-10-03)
- [normative] https://github.com/google-agentic-commerce/AP2/blob/main/docs/faq.md (2026-10-03)

**Overlaps:** [ucp](#ucp), [verifiable-intent](#verifiable-intent), [fido-agentic-standards](#fido-agentic-standards), [acp](#acp)

**Coverage:** see [Evidence](#evidence-ap2).

### Agentic Commerce Protocol (ACP)
<a id="acp"></a>

**Industry, specification.** Specification in beta, maintained by OpenAI and Stripe; MAINTAINERS.md also lists Meta (PR #236 "ADMIN: Add Meta as TSC member", merged 2026-04-24). Last dated version 2026-04-17; on 2026-10-13 main is still at commit 7fdd78d (2026-07-17), README badge "Beta", no tag or release (not found, 2026-10-13), and the directory spec/unreleased holds the changes not yet dated (checkout, cart, delegate, feed schemas and OpenAPI files). (as of 2026-10-13).

**Relevance to commerce.** The README says ACP "is an interaction model and open standard for connecting buyers, their AI agents, and businesses to complete purchases seamlessly." and covers agentic checkout and delegated payment over Representational State Transfer (REST) and an MCP binding. The seller enters through the checkout session's required links field (terms, privacy, return, shipping) and the unreleased product feed, whose optional barcode has a type (GTIN, UPC or EAN) and a value; requests carry a Signature header; the order schema has a receipt_url. The discovery RFC says "Seller identity is established through authentication (Bearer token), which is unavailable at discovery time." The OpenAI developer documentation (developers.openai.com/commerce/specs/checkout, read 2026-10-14) is a text separate from the specification in the repository (spec/unreleased). It says "Building with the Agentic Commerce Protocol is open to all." and "Instant Checkout in ChatGPT is currently available to approved partners." It documents a cancel call for a checkout session, which answers 405 when the session is already canceled or completed, and an order object with a list of refunds (types store_credit and original_payment); the cancellation of a checkout session is thus not the cancellation or refund of a completed order. The page /commerce/specs/delegated-payment answered HTTP 404 on 2026-10-14.

**Committed next.**
- README future path: "Neutral foundation stewardship as ecosystem matures"; no date (undated) [statement] https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/blob/main/README.md

**Boundary.** The discovery document states "Agent identity and authorization are separate concerns", leaving catalog discovery and agent registration outside it.

**Sources.**
- [normative] https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/blob/main/README.md (2026-10-03)
- [normative] https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/blob/02672abb230d7fd75b10264fd9a9a8b9b10e0fa6/MAINTAINERS.md#L9 (2026-10-03)
- [decision] https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/pull/236 (2026-10-03)
- [normative] https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/blob/main/rfcs/rfc.discovery.md (2026-10-03)
- [statement] https://developers.openai.com/commerce/specs/checkout (2026-10-14)
- [statement] https://developers.openai.com/commerce/guides/key-concepts (2026-10-14)
- [normative] https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/blob/main/docs/governance.md (2026-10-03)

**Overlaps:** [x402](#x402), [ucp](#ucp), [verifiable-intent](#verifiable-intent), [aaif-wg-agentic-commerce](#aaif-wg-agentic-commerce)

**Coverage:** see [Evidence](#evidence-acp).

### EMV Agentic Payments Framework for Specifications (draft for public feedback)
<a id="emvco-agentic-payments-framework"></a>

**Industry, specification.** Draft published for feedback on 2026-09-01; the comment period ended on 2026-09-30. On 2026-10-13 the EMVCo news list has no item on the outcome of the comment period; the newsletter Q3 2026 (2026-10-09) still calls it a draft and says it was published "to provide a foundation for further industry engagement and potential specification development"; no final version or new draft is found (EMVCo news list and resource page, 2026-10-13). (as of 2026-10-13).

**Relevance to commerce.** The press release of 2026-09-01 says the draft framework for card payments introduces "Intent Services", a shared layer to "register, reference, retrieve and manage consumer-authorised intent before, during and after a transaction", for cases where a consumer delegates authority to an AI agent to buy on their behalf. It says EMVCo has established a dedicated Agentic Payments Task Force and collaborates with the FIDO Alliance, the OpenID Foundation, the OpenWallet Foundation and W3C.

**Committed next.**
- None declared in the sources read.

**Boundary.** EMVCo "may consider capabilities related to Know Your Agent (KYA) and Agentic Transaction Indicators to be included in future publications".

**Sources.**
- [decision] https://www.emvco.com/news/emvco-requests-feedback-on-framework-for-secure-interoperable-and-scalable-card-based-agentic-payments/ (2026-10-02)
- [statement] https://www.emvco.com/resources/emv-agentic-payments-framework-for-specifications-v1-0-draft-comment-period-ends-30-sept-2026/ (2026-10-02)
- [statement] https://www.emvco.com/knowledge-hub/how-emvco-is-working-to-enable-secure-interoperable-and-scalable-card-based-agentic-payments/ (2026-10-02)
- [statement] https://www.emvco.com/news/emvco-newsletter-q3-2026/ (2026-10-13)
- [statement] https://www.emvco.com/news/ (2026-10-13)

**Overlaps:** [verifiable-intent](#verifiable-intent), [fido-agentic-standards](#fido-agentic-standards), [ap2](#ap2)

**Coverage:** see [Evidence](#evidence-emvco-agentic-payments-framework).

### KYAPay (Skyfire)
<a id="kyapay"></a>

**Industry, specification.** Individual Internet-Drafts named for the OAuth Working Group (WG) (draft-skyfire-oauth-*); WG stream or adoption: not found on the datatracker, 2026-10-13 (the pages of kyapay-token and using-kyapay-tokens show "(No stream defined)"). On 2026-10-02 the author announced new revisions of five drafts: kyapay-token-02, using-kyapay-tokens-01, amr-values-02, id-verification-02 and aml-methods-01 (datatracker date 2026-10-01 for all five). The datatracker lists two more documents of the family, kyapay-token-exchange-01 (2026-07-19) and kyapayprofile-02 (2026-06-20, replaced by kyapay-token), seven in all. The Technical Plenary and Advisory Committee (TPAC) breakout proposal #39 (KYAPay: Verified Agent Identity and Payments for Ubiquitous Agentic Commerce) is open on 2026-10-13 with one comment and no assigned slot; the datatracker shows no revision of kyapay-token-exchange after -01 of 2026-07-19. (as of 2026-10-13).

**Relevance to commerce.** KYAPay defines a signed JWT carrying verified agent and human identity (KYA) and payment credentials (PAY), so that merchant security infrastructure can distinguish human-authorised agents from malicious bots. The author's announcement of 2026-10-02 describes the token as a "JWT token providing claims about the person or organization authorizing an agent to act, the agent platform, the agent instance, and optionally a payment method". On the oauth list the token is discussed among bot managers, CDNs and site policy engines.

**Committed next.**
- The author invites review of the updated drafts on the oauth list and at IETF 127 (14 to 20 November 2026). (undated) [third party] https://mailarchive.ietf.org/arch/msg/oauth/h_YQPuYbBQf0TaiNIJQDNcxgGfc/
- Rework of the delegation text of the token-exchange draft, stated by the author on 2026-09-18. (undated) [third party] https://mailarchive.ietf.org/arch/msg/oauth/CbHD0qu_C-7AgMj3OdM7QNmbRjk

**Boundary.** A participant review of 2026-09-23 reads hid, aid and apd as identifying principal, agent and platform, not the authority delegated.

**Sources.**
- [third party] https://mailarchive.ietf.org/arch/msg/oauth/h_YQPuYbBQf0TaiNIJQDNcxgGfc (2026-10-03)
- [third party] https://mailarchive.ietf.org/arch/msg/oauth/xFAGS_R8IsdZAQygs8J0DT5DgN0 (2026-10-03)
- [third party] https://mailarchive.ietf.org/arch/msg/oauth/CbHD0qu_C-7AgMj3OdM7QNmbRjk (2026-10-03)
- [decision] https://datatracker.ietf.org/doc/draft-skyfire-oauth-kyapay-token/ (2026-10-13)
- [decision] https://datatracker.ietf.org/doc/draft-skyfire-oauth-using-kyapay-tokens/ (2026-10-13)
- [third party] https://www.ietf.org/archive/id/draft-skyfire-oauth-kyapay-token-02.txt (2026-10-14)

**Overlaps:** [w3c-agenticweb-wg](#w3c-agenticweb-wg), [ietf-webbotauth](#ietf-webbotauth), [mastercard-agent-pay](#mastercard-agent-pay)

**Coverage:** see [Evidence](#evidence-kyapay).

### Mastercard Agent Pay
<a id="mastercard-agent-pay"></a>

**Industry, specification.** Commercial programme of Mastercard for agent-initiated payments, described on its framework page (read in a browser on 2026-10-14; first read 2026-10-02). Page metadata: datePublished 2025-10-14, dateModified 2025-11-04. The page introduces the Mastercard Agent Pay Acceptance Framework: registration and verification of agents before they transact with agentic tokens, Web Bot Auth at the content delivery network (CDN) layer, and a Dynamic Token Verification Code, an agentic token formatted for standard card payment fields, submitted in existing checkout forms. The page refers to developer.mastercard.com for use cases; that site was not read. (as of 2026-10-14).

**Relevance to commerce.** The framework page (a Mastercard statement) says "By implementing the emerging Web Bot Auth standard (as outlined in the framework) at the Content Delivery Network (CDN) layer, merchants can verify agent authenticity", and that "we’ve partnered with Cloudflare to support Web Bot Auth in Mastercard Agent Pay". Mastercard is the maintainer of Verifiable Intent (see verifiable-intent).

**Committed next.**
- None declared in the sources read.

**Boundary.** not found in the framework page (read in a browser on 2026-10-14)

**Sources.**
- [statement] https://www.mastercard.com/europe/en/news-and-trends/stories/2025/agentic-commerce-framework.html (2026-10-14)
- [decision] https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/ (2026-10-14)
- [normative] https://github.com/agent-intent/verifiable-intent/blob/main/README.md (2026-10-02)

**Overlaps:** [ietf-webbotauth](#ietf-webbotauth), [kyapay](#kyapay), [verifiable-intent](#verifiable-intent)

**Coverage:** see [Evidence](#evidence-mastercard-agent-pay).

### Personal Agent Consent & Trust Protocol (PACT), published by Decagon with Instinct
<a id="pact"></a>

**Industry, specification.** Version 1.0 of the specification ("This is PACT 1.0.") is published at openpactprotocol.org (the Decagon announcement is dated 2026-10-06), and the repository openpactprotocol/openpactprotocol (created 2026-10-01, Apache-2.0) holds the documentation, a reference Provider, a demo personal agent and conformance tests; its latest commit on main is 838c6bd (2026-10-06, a dependency update), read 2026-10-13. Decagon, 2026-10-06: it is open-sourcing PACT, "co-developed and supported by Instinct". No standards body or governing organisation is named in the pages of the site read on 2026-10-13. (as of 2026-10-13).

**Relevance to commerce.** PACT builds on A2A 1.0 and defines how a personal agent identifies itself to a business's support agent and, optionally, which permissions the customer has granted it. The business's Agent Card is found at "https://{brandDomain}/.well-known/agent-card.json", which "serves the card or redirects to" the Provider's URL; the personal agent "never builds it from a Brand ID". The Poppy protocol uses a different well-known document (see pap and seam S1). The personal agent signs every request with a JWT (ES256 or RS256) checked against its published keys, and section 3.3 says what that proves: "That a known personal agent is calling for someone it calls sub. Not that sub owns a Brand account." Delegated authority is optional: the customer logs in with the business, never with the personal agent, and approves scopes that "Each Brand defines" (examples on the card: orders:read, orders:cancel), through OAuth 2.0 device code (RFC 8628). The Decagon post puts it as "It separates the identity of the personal agent from its authority to act on a customer". Section 5.6: every reply under a delegation token carries a signed receipt (grant id, user, scopes used, actions, timestamp), and "Personal agents SHOULD verify and keep receipts". The receipt records what the Provider's agent did; the words consumer, durable medium and confirm are not found in the specification page (2026-10-13).

**Committed next.**
- None declared in the sources read.

**Boundary.** The specification does not define a registry: "This spec does not define a registry." Registration of a personal agent with a Provider is out of scope ("How these are exchanged is out of scope"), and each Brand defines its own scopes, none reserved by PACT.

**Sources.**
- [normative] https://openpactprotocol.org/spec (2026-10-13)
- [statement] https://openpactprotocol.org/ (2026-10-13)
- [normative] https://github.com/openpactprotocol/openpactprotocol (2026-10-13)
- [statement] https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact (2026-10-13)

**Overlaps:** [pap](#pap), [a2a-core](#a2a-core), [a2a-discovery](#a2a-discovery)

**Coverage:** see [Evidence](#evidence-pact).

### Personal Agent Protocol (PAP, "Poppy"), published by Sierra with Meta
<a id="pap"></a>

**Industry, specification.** Draft 0.1 of the specification is published at personalagentprotocol.org (announced 2026-10-06, draft published 2026-10-09; the pages read on 2026-10-13 are marked "Updated Oct 12, 2026"), under the Apache License 2.0 with the names and the logo excluded; a further 35 design partners were named on 2026-10-09. Governance is worded two ways, not reconciled here. Sierra, 2026-10-06: "an open standard Meta and Sierra are developing along with industry partners at Genesys, Instinct, Rocket, Shopify, Stripe, and Walmart". Decagon, 2026-10-06: "join the Personal Agent Protocol working group announced by the team behind Meta's Muse to help shape an industry standard". No standards body or governing organisation is named in the pages of the site read on 2026-10-13. (as of 2026-10-13).

**Relevance to commerce.** Discovery is one well-known document: "A Company MUST publish its poppy.json document at https://{domain}/.well-known/poppy.json over HTTPS". The well-known URL "MAY redirect" to where the document is hosted, and "Personal Agents MUST follow redirects, and every redirect MUST be to an HTTPS URL"; the UCP specification says the opposite for its profile (see seam S1). poppy.json is not in the Internet Assigned Numbers Authority (IANA) well-known URI registry (not found in the registry XML, 2026-10-13). The agent is identified by a URL: "A Personal Agent's client_id MUST be an HTTPS URL that returns its metadata document", which carries a jwks_uri and a token_endpoint_auth_method of private_key_jwt; the Company can register, allow-list, block or revoke client ids. The operations extension, section 8 ("What a confirmation proves"), says what a confirmation does not show: "It doesn't prove that the User saw the terms or approved them." The announcement of 2026-10-06 says the protocol "defines how personal agents interact with businesses": it "starts on the website, where a personal agent can discover what the company offers and how to reach it", the session "is built on OAuth", and the customer decides whether the agent has read-only or write access. Context, not part of the protocol: Retail Insight Network reported on 2026-09-23 that Shopify and Meta partnered so that Meta's assistant Muse can complete purchases across Shopify's merchants through Shop Pay.

**Committed next.**
- Design workshops and a reference implementation "over the next month" (Sierra blog, 2026-10-09). (approx. 2026-11-09) [statement] https://sierra.ai/blog/poppy

**Boundary.** The Path to 1.0 page lists as areas "the draft doesn't cover yet": payments ("How a personal agent makes payments in a way that fits the protocol, including how that works with existing payment protocols."), push notifications and attachments ("such as receipts, return labels, product images, or forms for the user to fill in").

**Sources.**
- [normative] https://personalagentprotocol.org/docs/spec (2026-10-13)
- [normative] https://personalagentprotocol.org/docs/extensions/operations (2026-10-13)
- [statement] https://personalagentprotocol.org/docs/open-topics (2026-10-13)
- [normative] https://personalagentprotocol.org/license (2026-10-13)
- [statement] https://sierra.ai/blog/poppy (2026-10-13)
- [statement] https://sierra.ai/blog/introducing-personal-agent-protocol (2026-10-08)
- [third party] https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact (2026-10-13)
- [decision] https://www.iana.org/assignments/well-known-uris/well-known-uris.xml (2026-10-13)
- [third party] https://www.implicator.ai/meta-sierra-personal-agent-protocol/ (2026-10-08)
- [third party] https://www.retail-insight-network.com/news/shopify-meta-deal-ai-agent-shopping/ (2026-10-08)

**Overlaps:** [ucp](#ucp), [mcp-core](#mcp-core)

**Coverage:** see [Evidence](#evidence-pap).

### Universal Commerce Protocol (UCP)
<a id="ucp"></a>

**Industry, specification.** Latest GitHub release v2026-08-25 (2026-08-25); lodging booking draft merged 2026-09-24 (PR #780); the Common capability `ask` merged 2026-10-07 (PR #538); feed and subscription policy in draft (PR #866, PR #890); the food checkout proposal (PR #897) is under review (open on 2026-10-13). On 2026-10-13 main is at commit 9756aa9 (2026-10-12) and no release is listed after v2026-08-25. Governance and extension items filed 2026-10-09 to 2026-10-11, read 2026-10-13: issue #922 "[DTC Charter]: Local Services" (DTC: Domain Tech Council; labels Triage and gov:needs-gc-review, no comments) proposes a Domain Tech Council for appointments, group sessions, reservations and rentals, defined by "real-time slot computation over staff and resource calendars, with holds", leaves lodging, food, payments and shopping to the councils that own them, and says of three earlier proposals (#317, #303, #479) that "none has a home council"; the platform it lists is "Meta" and the businesses are "Wix, Housecall Pro, Squarespace, Jobber, HoneyBook, Stripe, Shopify". Issue #924 "Domain Working Group (DWG) Charter: Agentic Donations" (same labels, no comments) names the Shopping Tech Council as sponsor and a proposed chair from Stripe, asks for nominations by "October 23, 2026" and targets "November 2, 2026" for the initial package; "Merged PRs and production launches are not required for the DWG to close." It mentions the Donor Agent Protocol of GoFundMe, whose site gofundme.github.io/donor-agent (read 2026-10-13) is headed "Donor Agent Protocol (DAP) v0.1" and "An Evidence-First Donation Layer"; a repository for it is not found (gofundme/donor-agent, HTTP 404, 2026-10-13). Issue #929 (opened 2026-10-11, one comment besides the author's) proposes the extension dev.ucp.common.quote, described as "a one-quotation-at-a-time loop, not a negotiation protocol", with draft PR #930 as reference implementation ("not requesting merge before #929 reaches Provisional"); an accepted quotation appears in totals and on the Order as the quotation id and its subtotal only. A comment of 2026-10-11 calls it "a useful candidate for the narrower case of a Business-issued, price-only quotation accepted by reference into Cart/Checkout". PR #933 (open, one commit, 2026-10-11) says it "spells out which redirect codes are actually banned (301/302/303/307/308) and says 304 is fine, on both the hosting and fetching side"; PR #932, which proposed the same clarification, was closed on 2026-10-11, two minutes after it was opened, by the account that opened it. PR #897 (food) is still open on 2026-10-13 (head 1e2818c). Discussion #931 (2026-10-11, no comments) asks whether ucp.dev could list community implementations and names one open-source implementation, Portage, described there as an MIT-licensed agent command-line interface and a set of merchant-side Ruby gems; it is noted here and not evaluated. The Shopify/hydrogen pull request #4158 on the UCP profile route is open, not merged (2026-10-13), and is not counted. (as of 2026-10-14).

**Relevance to commerce.** The AP2 mandates extension says businesses must "embed a cryptographic signature in checkout responses, proving the terms (price, line items) are authentic" and platforms provide mandates "proving the user explicitly authorized the specific checkout state and funds transfer". The Order page calls the entity "the authoritative latest state of the order at the time of retrieval or delivery", where webhook payloads "be signed by the business and verified by the platform". Terms travel in policies[] (PR #572, merged 2026-07-23), where the business states rules such as a refund window; the PR says "Policies never force display." On agent identity, the signatures page (PR #483, merged 2026-07-03) says a dual-audience signature "is the RECOMMENDED path for integrators" who want interoperability with Web Bot Auth verifiers; that interoperability is request-scoped. A food domain (`dev.ucp.food.checkout`, `food.fulfillment`) was proposed on 2026-10-03 for early feedback (PR #897, opened by a participant "On behalf of the entire Food Domain Tech Council"; its label on 2026-10-05 was status:needs-triage and on 2026-10-09 and 2026-10-13 is status:under-review, with gov:needs-tc-review and 12 comments on 2026-10-13). A proposal to authenticate the platform client through attestation (issue #852, opened 2026-09-22) was described by its author on 2026-10-04 as "now ready for Technical Council review". Issue #375 (2026-05-29) declined external place identifiers in the core schema: "Adding specialized reconciliation mappings to the core schema is a premature optimization." The Common capability `dev.ucp.common.ask` was merged on 2026-10-07 (PR #538; commit a41a2dc). Its page says "The Ask capability provides natural-language Q&A about a Business's resources, policies, and services." and "`ask` is the open-question complement to UCP's structured commerce capabilities". Two rules of its text: "A Business MUST NOT change the state of any resource exposed through another UCP capability or extension in response to an `ask` request." and "An answer is indicative, not authoritative."; where an answer conflicts with the representation returned by the capability that owns the resource, "that representation is authoritative and the Platform MUST prefer it", and "A Platform MUST NOT treat an `answer` as the binding disclosure for a safety, allergen, or regulatory claim." The page lists as typical use cases product questions ("fit, materials, compatibility, comparisons"), policy questions ("returns, shipping, warranty, refunds"), FAQ and how-to ("store hours, shipping timelines, accepted payment methods") and clarification about a specific resource, grounded in an identifier. The description of the pull request, not the specification, lists "policies, fit and suitability, materials, compatibility, amenities, support information, and Business-specific knowledge". The merge adds docs/specification/common/ask/ (index, Representational State Transfer (REST) and MCP bindings), docs/specification/shopping/ask/index.md and source/schemas/common/ask.json; text read at commit f2206e6 (the head of main on 2026-10-09; on 2026-10-13 main is at 9756aa9, and a git diff of the two commits shows no change to the overview, AP2 mandates, signatures, order, ask and lodging pages cited here). Pull request #811 (opened 2026-09-07 by a participant, open; among its labels on 2026-10-09 status:stale-review and gov:needs-tc-review; no comment or review; state and labels unchanged on 2026-10-13) proposes an optional `offers[]` array on the catalog variant "so one catalog can list a product sold by several different merchants and send each to the right seller's checkout". Each offer names its seller by `seller.domain`, the Merchant of Record, with the seller's own `item_id` and an authoritative price; the proposed schema text describes the domain as "The seller's canonical host: a bare hostname without scheme, path, port, or trailing slash" and adds "A Platform resolves this host to the seller's UCP profile at `/.well-known/ucp` and verifies its signing keys via authority binding." The overview page uses "canonical" for the host that serves a schema (lines 158 to 164); which of the bare and the www host is canonical for a profile is not found in the overview page at f2206e6 nor in the five files of the pull request (2026-10-09). The overview page says, in Profile Requirements, Hosting, item 2, "Profile endpoints MUST NOT use redirects (3xx)." (line 1466) and, in the rules for any URL dereferenced during identity resolution, item 2, "Implementations MUST NOT follow redirects (3xx)." (line 1514); line 182 applies the same rule to schema URLs (file at commit f2206e6 of 2026-10-07; unchanged at 9756aa9 on 2026-10-13). Items 3 and 4 of Hosting ask for a Cache-Control with public and a max-age of at least 60 seconds, and for a validator (ETag or Last-Modified). A registration request for `ucp` has been open in the registry's repository since 2026-06-06 (issue #92), labelled "waiting for input" since 2026-07-11, when the designated expert asked for an e-mail address for the change controller (read 2026-10-14). The profile rule first appears in commit 0426800 of 2026-02-17, "feat: signing for UCP requests & responses (#156)". The author of the census reported in issue #904 (2026-10-07, 2026-10-08) and Discussion #867 (comment 18810486, posted 2026-10-08) a census of 225 hosts probed from Seoul, one route and one attempt per host, 3xx not followed. Version of 2026-10-08, read in the edit history of the comment (figures declared by the source, not verified by this map): 62 positives (200, parses as JSON, ucp.version present), of which 58 Shopify and 4 not identified; declared versions 2026-08-25 (58), 2026-04-08 (3), 2026-01-23 (1); signing keys published by 0 of 62; the other rows: 1 refused by robots.txt, 7 responses 200 that did not parse, 12 3xx at the profile path, 65 404, 2 410, 59 403, 3 429/418/503, 14 connect, timeout or TLS failures. The author states "Not a random draw": a hand-built list of well-known storefronts plus the WooCommerce showcase, heavily Shopify-skewed, so the rate is not an adoption estimate; all figures declared by the source, not verified by this map. Four of the 62 positives have a home page answering 403 or 429 while the profile path answers 200 (comment of 2026-10-07, where the hosts are named). The author reports that probing the host as written gave 60 positives and 23 3xx, and that resolving the canonical host first gave 62 and 12. In the frame of #867 the 62 is "row 2 and ucp.version present", that is a floor on row 2 as the frame defines it (parses as JSON), with rows 3 and 4 not measured; the author of this map replied that the 7 non-parsing 200s are row 1 without row 2, whereas the run lists them among the cases it "could not ask". In Discussion #864 (Lodging), a participant who operates a small property asked on 2026-10-07 how a platform finds a property that is not in a global distribution system (GDS), a chain central reservation system (CRS) or a channel manager feed; the author of this map replied on 2026-10-08 that "today a property-hosted profile is necessary but not sufficient", and the same participant asked whether platforms will discover a profile on the property's own domain or receive lodging inventory only through connectivity partners; no maintainer reply was found among the discussion's six comments, the last of 2026-10-08 (read 2026-10-13). The lodging booking page says a platform "MUST supply valid property.id, and either a pre-composed stay.id OR both accommodation_type.id and rate_plan.id identifiers sourced from upper-funnel discovery mechanisms" (lines 426 to 428, commit f2206e6); the location_summary schema describes id as "Stable, opaque, Business-scoped Location identifier." Issue #678 (buyer consent at complete_checkout) was closed on 2026-10-07 with the merge of PR #883, and issue #666 (permalink and authenticated buyer session) the same day with the merge of PR #789, "require explicit buyer action before cart merge". In PR #691 (price_treatment, open) the author wrote on 2026-10-07 that after dropping not_asserted "an absent price_treatment and an absent tax now mean the same thing everywhere". WooCommerce PR #69577 (open, draft on 2026-10-08) adds UCP catalog routes for search, lookup and product, implementing spec version 2026-04-08, off by default behind the woocommerce_ucp_enabled filter. Known Good posted in Discussion #867 on 2026-10-08, with the figures of https://knowngood.sh/standard/ucp, a run of 2026-09-26 to 2026-09-28 from AWS us-east-1 with robots.txt honoured and the user agent KnownGood-Verifier/0.3 (figures declared by the source, not verified by this map). Its population is 92,541 hosts that its crawl was allowed to ask, from its own index, "not a draw from storefronts". Rows of the frame as reported: HTTP 200 on 45,362 hosts (44,118 at the first request and 1,244 after a redirect), parses as JSON on 42,757, row 3 not measured ("Row 3 is empty on purpose."), and a protocol response (tools/list on the MCP endpoint named by the profile) on 41,424. By endpoint domain: myshopify.com 31,568, wixapis.com 9,782 and three singletons; "Merchant count 41,424; decision count 2" (two tool signatures cover 41,352 endpoints). The Known Good page says "Shopify and Wix advertise the MCP endpoint they run for every store through this profile". No page of Wix on UCP support was found (two searches, 2026-10-09), so Wix is a platform observed by Known Good only. The run follows 3xx at the profile path ("3xx followed up to 2 hops, https only, same registrable domain only"): 2,546 3xx, 2,188 followed, 1,244 ended in 200, and 286 cross-domain 3xx not followed; line 1514 of the overview page reads "Implementations MUST NOT follow redirects (3xx)." The 1,244 are reported here apart from the first-request count. Other figures declared by the source, not verified by this map: 42,434 profiles declare a checkout capability (a declaration, not a transaction); ucp.version declared 2026-08-25 on 41,624, 2026-04-08 on 898 and none on 120; 925 of the parsing profiles are on hosts whose home page was not 2xx. Could not ask, site side: robots.txt 102, 401 and 403 1,350, 402 141, 5xx 157, TLS 5, connection refused 12, reset 6 (sum 1,773, computed here); prober side: 429 504, timeouts 104, per-host budget 89 and 31, other 3 (sum 731, computed here). The authors report two defects in their own record: "Our probe stored the profile's top-level version, not ucp.version", with counts re-read from the stored bodies, and, in their words, "on 1,570 hosts the per-host budget ran out inside the capability loop, so 1,147 hosts that answered 200 kept no result beyond row 1", so "row 2 is a floor by that much". The comment was edited on 2026-10-09 as a re-run of that day restructured against the frame, and its author wrote the same day (comment 18831816) that it was updated against the three points. Figures of the 9 October run (declared by the source, not verified by this map): 225 hosts and 675 requests (225 storefront requests to find the host the storefront settles on, 225 profile-path requests and 225 robots.txt requests), user agent string agentbi/0.1 (the prober's own), vantage KR (Seoul, AS45102); row 1 (HTTP 200) 68 hosts, row 2 and ucp.version present 62 (the source counted the two conditions as one figure until its run of 13 Oct, see below), rows 3 and 4 not measured, no validator run. Other outcomes of that run: 404 64, 410 2, 3xx at the profile path 12 (8 same-host protocol or path redirects, 4 cross-host with the Location host recorded), 200 that does not parse 6, which the author counts as "row 1 without row 2"; could not ask, site side: 403 59, robots.txt refusal 1, 5xx 1, TLS failure 1, connection refused or DNS 2, other 4xx (418) 1; prober side: timeouts 10, 429 1 ("Retry-After not recorded; that is a gap on my side"), URLs not sent because of the prober's own server-side request forgery (SSRF) guard 3. On 2026-10-09 the author of this map posted version 3 of the frame in Discussion #867 (comment 18833761), after the two full runs of issue #904 and of Known Good. It adds a run field for the probed host with the counts "seed host as written, www-normalised, other host in the same registrable domain"; a line for 3xx at the profile path, since "a profile reached only via a 3xx is never a positive"; a row 1a, "200 after redirect", counted "only if 3xx were followed; non-conforming, excluded from 2-4"; a prober-side line widened to "anything the prober chose not to send or could not finish"; and an optional hosting row H, "of row 2: Cache-Control public, max-age ≥ 60; ETag or Last-Modified". The comment ties the redirect rows to the two rules of the overview page quoted above (lines 1466 and 1514) and the hosting row to items 3 and 4 of the same Hosting list. The author of the census answered the same day (comment 18834311) "this is how I'll report the next pass." (his figures, declared by the source, not verified by this map): for the 225 seeds the probed host is the seed host as written for 201, www-normalised for 14 and another host of the same registrable domain for 10; 3xx at the profile path are 8 same-host, 3 same registrable domain and 1 other domain, none counted positive; row 1a is 0 "by construction" because the run never follows a 3xx at the profile path; Retry-After is now recorded and the hosting row measurable in the next pass. On 2026-10-10 and 2026-10-11 the thread of Discussion #867 went on. The author of the census re-ran on 2026-10-11 (comment 18860202; figures declared by the source, not verified by this map): 225 hosts, vantage KR, row 2 and ucp.version present on 61 hosts (62 on 9 Oct; one host moved from a 200 to a 403, so from positive to "could not ask, site side"), and none of the three hosts that had settled on an asset host on 9 Oct did so again; the hosting row was first measured, with 58 of the 61 positives sending Cache-Control public with max-age of at least 60 and 4 sending ETag or Last-Modified. He adopted the case "storefront did not settle on a storefront host" (comment 18861115) and will publish beside the headline how many positives depend on the fallback from 2026-10-12. Known Good split its run by row 1a (comment 18866655; declared): of the 1,244 answers of 200 after a redirect, 4 parse and none is among the 41,424 protocol responses, so 0 of them depend on following a redirect; the bucket of hosts that did not settle on a storefront host (a) is 451 hosts, 80 of them protocol responses, all platform-supplied (myshopify.com 62, wixapis.com 18); his later comment gives the vantage as AWS us-east-1, one egress address. The author of this map posted the updated frame on 2026-10-11 (comment 18867673), "the version to copy", with the new case, the probed and the settled host per row, and the vantage as a run field. No run by anyone else was posted after 2026-10-11 in the 11 comments read on 2026-10-13. On 2026-10-14 (03:00 UTC, comment 18913822; figures declared by the source, not verified by this map) the author of the census wrote that "row 2: 61" reads as though 61 were row 2 as the frame defines it (parses as JSON) and that it is not: the figure is 200, parses as JSON and ucp.version declared, so a floor on row 2; the two numbers are reported apart from the run of 13 Oct, and are 61 and 61 on 13 and 14 Oct (difference 0); on 14 Oct 67 hosts answered 200 at the path, 61 parse as JSON, 5 are HTML soft-404s and 1 answers 200 with a body that is neither; row 3 and row 4 are not measured. On 2026-10-08 a participant working in hotel revenue management proposed restrictions on the stay object of the lodging draft and wrote that the current standard errors "would likely return inventory_exhausted, which gives the agent nothing to recover with"; a hotel operator added "+1 from a six-unit property" (comment 18822183). The Standard Errors table of the lodging booking page (lines 384 to 389) lists four codes, inventory_exhausted, occupancy_exceeded_capacity, payment_failed and eligibility_invalid, and describes inventory_exhausted as "The selected accommodation unit or inventory hold is no longer available"; no code for rate or stay restrictions is listed there (main at f2206e6, read 2026-10-09). Google's own developer pages, describing Google's product built on UCP (class statement; distinct from the standard's text): The lodging FAQ (https://developers.google.com/hotels/ucp/faq, "Last updated 2026-09-24 UTC") says "This first milestone unlocks Booking", "The best way to provide feedback is through GitHub, where the protocol is published." and "Over the coming months, Google will adopt this standard to power its hotel booking feature on AI Mode."; on ranking it answers "No. Opting for our booking integration does not influence how we rank your properties or rates in listings." The lodging page (https://developers.google.com/hotels/ucp, no update date shown on the page read) has a waitlist ("Join the waitlist"), "Conceptual mock only." and "Detailed onboarding and specs coming soon." The food ordering page (https://developers.google.com/actions-center/verticals/ordering/ucp, no update date shown on the page read) has a waitlist, "Detailed onboarding and specs coming soon." and "You remain the Merchant of Record."; allergens, dietary information, nutrition, disclosures, notices and alcohol are not mentioned on the page read on 2026-10-09.

**Committed next.**
- DWG charter: "The DWG targets late October 2026 to produce PRs for the Key Deliverables noted above" (approx. 2026-10-31) [statement] https://github.com/Universal-Commerce-Protocol/ucp/issues/682
- Lodging roadmap (PR #860, merged 2026-09-25): "beyond Booking, supporting hotels discovery, room selection, rate options, loyalty, discounts" (undated) [decision] https://github.com/Universal-Commerce-Protocol/ucp/pull/860
- Agentic Donations DWG (proposal #924): nominations to be filed by "October 23, 2026" (2026-10-23) [statement] https://github.com/Universal-Commerce-Protocol/ucp/issues/924
- Agentic Donations DWG (proposal #924): the initial package is targeted for "November 2, 2026" (2026-11-02) [statement] https://github.com/Universal-Commerce-Protocol/ucp/issues/924

**Boundary.** PR #780 declares out of scope "Upstream lodging search/discovery service."

**Author participation.** The author of this map took part in PR #866, issues #550 and #858, Discussions #864 and #867 (opened by the author; replies on 2026-10-10 and 2026-10-11 and the updated reporting frame of 2026-10-11), PR #890, PR #897 (comments from 2026-10-09 to 2026-10-13) and issue #904; see Disclosure.

**Sources.**
- [decision] https://github.com/Universal-Commerce-Protocol/ucp/pull/780 (2026-10-03)
- [normative] https://github.com/Universal-Commerce-Protocol/ucp/blob/f2206e680f64fe2cc73495acc3557569afd9097a/docs/specification/payment/extensions/ap2-mandates.md (2026-10-03)
- [normative] https://github.com/Universal-Commerce-Protocol/ucp/blob/f2206e680f64fe2cc73495acc3557569afd9097a/docs/specification/shopping/order/index.md (2026-10-03)
- [statement] https://github.com/Universal-Commerce-Protocol/ucp/issues/682 (2026-10-03)
- [normative] https://github.com/Universal-Commerce-Protocol/ucp/blob/f2206e680f64fe2cc73495acc3557569afd9097a/docs/specification/overview/index.md (2026-10-08)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/issues/904 (2026-10-08)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/867 (2026-10-08)
- [decision] https://github.com/Universal-Commerce-Protocol/ucp/commit/0426800 (2026-10-08)
- [normative] https://github.com/Universal-Commerce-Protocol/ucp/blob/f2206e680f64fe2cc73495acc3557569afd9097a/docs/specification/lodging/booking/index.md (2026-10-08)
- [normative] https://github.com/Universal-Commerce-Protocol/ucp/blob/f2206e680f64fe2cc73495acc3557569afd9097a/source/schemas/common/types/location_summary.json (2026-10-08)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/issues/904#issuecomment-6057562464 (2026-10-08)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18810486 (2026-10-09)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/864#discussioncomment-18809459 (2026-10-08)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/864#discussioncomment-18809648 (2026-10-08)
- [decision] https://github.com/Universal-Commerce-Protocol/ucp/pull/883 (2026-10-08)
- [decision] https://github.com/Universal-Commerce-Protocol/ucp/pull/789 (2026-10-08)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/pull/691#issuecomment-6039591246 (2026-10-08)
- [third party] https://github.com/woocommerce/woocommerce/pull/69577 (2026-10-08)
- [third party] https://knowngood.sh/standard/ucp (2026-10-09)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18816164 (2026-10-09)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/864#discussioncomment-18816854 (2026-10-09)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/864#discussioncomment-18822183 (2026-10-09)
- [statement] https://developers.google.com/hotels/ucp/faq (2026-10-09)
- [statement] https://developers.google.com/hotels/ucp (2026-10-09)
- [statement] https://developers.google.com/actions-center/verticals/ordering/ucp (2026-10-09)
- [decision] https://github.com/Universal-Commerce-Protocol/ucp/pull/538 (2026-10-09)
- [decision] https://github.com/Universal-Commerce-Protocol/ucp/commit/a41a2dc1679d91da5c09219a376fe59893eb3e09 (2026-10-09)
- [normative] https://github.com/Universal-Commerce-Protocol/ucp/blob/f2206e680f64fe2cc73495acc3557569afd9097a/docs/specification/common/ask/index.md (2026-10-09)
- [normative] https://github.com/Universal-Commerce-Protocol/ucp/blob/f2206e680f64fe2cc73495acc3557569afd9097a/docs/specification/shopping/ask/index.md (2026-10-09)
- [normative] https://github.com/Universal-Commerce-Protocol/ucp/blob/f2206e680f64fe2cc73495acc3557569afd9097a/source/schemas/common/ask.json (2026-10-09)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/pull/811 (2026-10-09)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18831816 (2026-10-09)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18833761 (2026-10-09)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18834311 (2026-10-09)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/pull/897 (2026-10-09)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/pull/897#issuecomment-6074516498 (2026-10-09)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18860202 (2026-10-13)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18861115 (2026-10-13)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18866655 (2026-10-13)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18867673 (2026-10-13)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18913822 (2026-10-14)
- [third party] https://github.com/protocol-registries/well-known-uris/issues/92 (2026-10-14)
- [statement] https://github.com/Universal-Commerce-Protocol/ucp/issues/922 (2026-10-13)
- [statement] https://github.com/Universal-Commerce-Protocol/ucp/issues/924 (2026-10-13)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/issues/929 (2026-10-13)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/pull/930 (2026-10-13)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/pull/933 (2026-10-13)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/pull/932 (2026-10-13)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/931 (2026-10-13)
- [statement] https://gofundme.github.io/donor-agent/ (2026-10-13)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/issues/852 (2026-10-05)
- [decision] https://github.com/Universal-Commerce-Protocol/ucp/releases (2026-10-05)
- [normative] https://github.com/Universal-Commerce-Protocol/ucp/blob/b0e81adecf816a1771b736464f17586d76950f7f/docs/specification/payment/extensions/ap2-mandates.md (2026-10-05)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/issues/375 (2026-10-03)
- [decision] https://github.com/Universal-Commerce-Protocol/ucp/pull/860 (2026-10-03)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/pull/572 (2026-10-03)
- [normative] https://github.com/Universal-Commerce-Protocol/ucp/blob/f2206e680f64fe2cc73495acc3557569afd9097a/docs/specification/signatures.md (2026-10-03)
- [normative] https://github.com/Universal-Commerce-Protocol/.github/blob/main/GOVERNANCE.md (2026-10-03)
- [third party] https://github.com/Universal-Commerce-Protocol/ucp/discussions/864#discussioncomment-18801390 (2026-10-08)

**Overlaps:** [ard](#ard), [verifiable-intent](#verifiable-intent)

**Coverage:** see [Evidence](#evidence-ucp).

### Verifiable Intent
<a id="verifiable-intent"></a>

**Industry, specification.** Draft v0.1 specification, maintained by Mastercard according to its README (Apache-2.0, tag v0.1.0). The FIDO Alliance release of 2026-04-28 says Mastercard has contributed it to the Payments Technical Working Group. On 2026-10-13 the last commit on main is of 2026-04-20 (356c296, PR #23), v0.1.0 is the only tag, no release is listed, and the README header reads "Draft (v0.1). Maintained by Mastercard; open to multi-stakeholder contribution." (as of 2026-10-13).

**Relevance to commerce.** The repository describes it as an "Open specification for cryptographic agent authorization in commerce"; the README defines a "layered SD-JWT credential format" giving cryptographic evidence that an agent's actions stayed within the scope the user delegated. Layers hold mandates (signed claims on checkout details or payment parameters) and user constraints; the merchant receives the checkout mandate (layer 3b, Autonomous mode). The FIDO release says "Mastercard has contributed its Verifiable Intent framework, co-developed with Google and designed to work with AP2"; Google as co-developer: not found in the repository pages read, 2026-10-02.

**Committed next.**
- None declared in the sources read.

**Boundary.** Out of scope in the README: transport, key management, provider enrolment, agent platform APIs, dispute resolution, regulatory compliance mapping.

**Sources.**
- [normative] https://github.com/agent-intent/verifiable-intent/blob/main/README.md (2026-10-13)
- [normative] https://github.com/agent-intent/verifiable-intent/blob/main/spec/design-rationale.md (2026-10-02)
- [decision] https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/ (2026-10-03)

**Overlaps:** [mastercard-agent-pay](#mastercard-agent-pay), [ucp](#ucp), [emvco-agentic-payments-framework](#emvco-agentic-payments-framework), [ap2](#ap2)

**Coverage:** see [Evidence](#evidence-verifiable-intent).

### Visa Trusted Agent Protocol (TAP)
<a id="visa-tap"></a>

**Industry, specification.** Specification and sample code published by Visa under Visa Product Terms of October 10, 2025; the product page, read in a browser on 2026-10-14, still says "This product is in the process of development and deployment." (as of 2026-10-14).

**Relevance to commerce.** The merchant specification says "this protocol is applicable to the scenario when the Agent is initially unknown to the Merchant." It defines three signatures: an agent recognition signature based on HTTP Message Signatures (RFC 9421) and aligned with web-bot-auth, a signed consumer or device identity and a signed payment container. The product page is headed "Enhancing Visa Intelligent Commerce to improve merchant visibility.", so the protocol is presented as the merchant-facing recognition part of a wider Visa programme (read in a browser on 2026-10-14); this version has no entry for Visa Intelligent Commerce. A merchant or its site protection provider verifies them; the sample repository calls the protocol "a standardized, cryptographic method for an AI agent to prove its identity and associated authorization directly to merchants."

**Committed next.**
- None declared in the sources read.

**Boundary.** "Merchants are not required to use this proposal and do not necessarily have to be registered with the Payment Schemes".

**Sources.**
- [statement] https://developer.visa.com/capabilities/trusted-agent-protocol (2026-10-14)
- [normative] https://developer.visa.com/capabilities/trusted-agent-protocol/trusted-agent-protocol-specifications (2026-10-14)
- [normative] https://developer.visa.com/capabilities/trusted-agent-protocol/product-terms (2026-10-14)
- [normative] https://github.com/visa/trusted-agent-protocol (2026-10-03)
- [normative] https://github.com/visa/trusted-agent-protocol/blob/main/README.md (2026-10-03)

**Overlaps:** [ietf-webbotauth](#ietf-webbotauth), [mastercard-agent-pay](#mastercard-agent-pay), [verifiable-intent](#verifiable-intent), [aaif-wg-agentic-commerce](#aaif-wg-agentic-commerce)

**Coverage:** see [Evidence](#evidence-visa-tap).

---

<a id="part-context"></a>
# Part 9: Context entries

### W3C Agent Identity Registry Protocol Community Group
<a id="w3c-agent-identity-registry-cg"></a>

**W3C, venue.** Community group created 2026-04-24; calls every two weeks on Tuesdays at 15:00 UTC; the call of 2026-10-06 had an agenda on the list (message of 2026-10-01) and minutes of 22 September were posted on 2026-10-01; minutes of the call of 2026-10-06 and a later call: not found in the October 2026 list archive (4 messages, the last of 2026-10-02), read 2026-10-13. The W3C group data list one chair. (as of 2026-10-13). Develops specifications to verify an agent's identity, controlling entity and authorization scope; the chair wrote on 2026-08-26 "We'll keep this group focused on the registry and credential layer for now".

**Sources.** [statement] https://api.w3.org/groups/cg/agent-identity (2026-10-02); [statement] https://lists.w3.org/Archives/Public/public-agent-identity/2026Sep/0017.html (2026-10-03); [statement] https://lists.w3.org/Archives/Public/public-agent-identity/2026Oct/ (2026-10-13); [statement] https://lists.w3.org/Archives/Public/public-agent-identity/2026Aug/0008.html (2026-10-03) Coverage: see [Evidence](#evidence-w3c-agent-identity-registry-cg).

### W3C Agent-Ready Video Community Group
<a id="w3c-agent-ready-video-cg"></a>

**W3C, venue.** Created 2026-10-01; chairs not yet selected: the W3C group data list no chair on 2026-10-13, and the group's list holds one message, the call for participation of 2026-10-01. (as of 2026-10-13). Aims to "make it easier for agents to find, cite and play relevant video on the Web", building on the Agent-Ready Video specification with per-moment rights and signed usage receipts.

**Sources.** [decision] https://lists.w3.org/Archives/Public/public-new-work/2026Oct/0000.html (2026-10-02) Coverage: see [Evidence](#evidence-w3c-agent-ready-video-cg).

### W3C Agent-to-Web Framework (A2WF) Community Group
<a id="w3c-agent-to-web-framework-cg"></a>

**W3C, venue.** Community group created 2026-03-29; may publish Specifications; one chair is listed on the W3C group data on 2026-10-13, and the list public-a2wf has no October 2026 archive (HTTP 404 on the index). (as of 2026-10-13). Develops technology for website operators to publish machine-readable governance policies for AI agents; examples of agent actions: "fill forms, book appointments, add items to carts, submit orders".

**Sources.** [statement] https://api.w3.org/groups/cg/a2wf (2026-10-02); [normative] https://w3c.github.io/charter-drafts/2026/agenticweb-wg.html (2026-10-02) Coverage: see [Evidence](#evidence-w3c-agent-to-web-framework-cg).

### W3C DID Methods Working Group (proposed charter)
<a id="w3c-did-methods-wg"></a>

**W3C, charter.** Proposed charter in Advisory Committee review (2026-09-30); public comments invited through 2026-10-28. (as of 2026-10-13). Mission: "to standardize DID Methods that use Web technologies"; a separate maintenance charter for the existing Decentralized Identifier (DID) Working Group (WG), whose mission includes DID Resolution, went into refinement on 2026-08-10 and was sent to the Advisory Committee on 2026-10-07, with public comments invited through 2026-11-05 (see w3c-did-wg).

**Sources.** [normative] https://www.w3.org/2026/09/proposed-did-methods-wg-charter.html (2026-10-02); [decision] https://lists.w3.org/Archives/Public/public-new-work/2026Sep/0011.html (2026-10-13); [decision] https://lists.w3.org/Archives/Public/public-new-work/2026Aug/0003.html (2026-10-13); [decision] https://lists.w3.org/Archives/Public/public-new-work/2026Oct/0008.html (2026-10-13) Coverage: see [Evidence](#evidence-w3c-did-methods-wg).

### W3C Decentralized Identifier Working Group (proposed charter)
<a id="w3c-did-wg"></a>

**W3C, charter.** Proposed maintenance charter sent to the Advisory Committee on 2026-10-07; W3C invites public comments through 2026-11-05, and the Advisory Committee call for review closes at 23:59 UTC on 2026-11-05. The current charter of the group "is hereby extended until 31 January 2027"; the start and end dates in the proposed charter text are placeholders. (as of 2026-10-09). The mission "is to maintain the specifications produced so far by the Working Group": Decentralized Identifiers and Decentralized Identifier (DID) Resolution; the listed chairs are Will Abramson and Otto Mora. Out of scope are class 4 changes to the DID specification, authentication or authorization protocols, and browser APIs; further notes "will not include DID Method specifications and will not address issues regarding any particular DID Methods". The charter text contains no occurrence of agent, payment, product or commerce (2026-10-08). The call for review says "The Controlled Identifiers (CIDs) recommendation, which is foundational to Decentralized Identifiers, is now also maintained by the DID Working Group." and "The Advisory Committee Representatives of current participants will need to have their organizations re-join the group if the revised charter gets approved."

**Sources.** [normative] https://www.w3.org/2026/10/proposed-did-wg-charter.html (2026-10-08); [decision] https://lists.w3.org/Archives/Public/public-new-work/2026Oct/0008.html (2026-10-08); [decision] https://lists.w3.org/Archives/Public/public-did-wg/2026Oct/0002.html (2026-10-09) Coverage: see [Evidence](#evidence-w3c-did-wg).

### W3C Digital Policy Working Group (ODRL, draft charter)
<a id="w3c-digital-policy-wg"></a>

**W3C, charter.** Draft charter in refinement until approx. 2026-11-02 (public-new-work, 2026-09-30); TPAC breakout #17 aims to discuss it. (as of 2026-10-03). Mission: "to develop and maintain the foundational digital policy layer for the digital economy", by extending the two ODRL recommendations.

**Sources.** [decision] https://lists.w3.org/Archives/Public/public-new-work/2026Sep/0012.html (2026-10-03); [normative] https://w3c.github.io/odrl/w3c-wg-draft-charter-2026/dpwg-draft-charter.html (2026-10-02) Coverage: see [Evidence](#evidence-w3c-digital-policy-wg).

### W3C Web Payment Security Interest Group
<a id="w3c-web-payment-security-ig"></a>

**W3C, venue.** Chartered 2025-04-01 to 2027-03-31 (shortname securepay); the draft Agentic Web charter lists the IG for "agentic payments". (as of 2026-10-03). Mission: "enhance the security and interoperability of various Web payments technologies"; a W3C staff member expected the e-commerce workshop to identify future workstreams for this group (webai-roadmap#45, 2026-06-11).

**Sources.** [normative] https://www.w3.org/securepay/charter-2025.html (2026-10-02); [statement] https://github.com/w3c/webai-roadmap/issues/45 (2026-10-03) Coverage: see [Evidence](#evidence-w3c-web-payment-security-ig).

### W3C browser-testing-tools Working Group (charter draft)
<a id="w3c-browser-testing-tools-wg"></a>

**W3C, charter.** Pull request #882 on w3c/charter-drafts, "Update charter-wg-btt.html", was merged on 2026-10-07 at 17:24 UTC. The merge text was read in the pull request only; the charter file was not read. (as of 2026-10-08). The pull request, opened by tantek, says it "Updates to broaden Motivation and Background, Scope sections to include end users and agentic browsing use-cases."

**Sources.** [decision] https://github.com/w3c/charter-drafts/pull/882 (2026-10-08) Coverage: see [Evidence](#evidence-w3c-browser-testing-tools-wg).

### WebMCP (Draft Community Group Report, Web Machine Learning CG)
<a id="w3c-webmcp-cg-report"></a>

**W3C, specification.** Draft Community Group Report, dated 9 October 2026 on the page read on 2026-10-13 (2026-09-30 on 2026-10-03), no numbered version; on 2026-10-08 PR #338, "Remove declarative API from spec", was merged (the specification now focuses on the imperative registerTool() API); the draft Agentic Web Working Group (WG) charter lists WebMCP as its normative deliverable. (as of 2026-10-13). Draft: "The WebMCP API enables web applications to provide JavaScript-based tools to AI agents."; an editor wrote on 2026-09-25 that identity and delegation proposals "are beyond the scope of the simple WebMCP API".

**Sources.** [normative] https://webmachinelearning.github.io/webmcp/ (2026-10-02); [third party] https://github.com/webmachinelearning/webmcp/issues/257 (2026-10-03); [decision] https://github.com/webmachinelearning/webmcp/pull/338 (2026-10-13); [third party] https://github.com/WebKit/standards-positions/issues/670 (2026-10-03) Coverage: see [Evidence](#evidence-w3c-webmcp-cg-report).

### DNS for AI Discovery (DNS-AID, draft-mozleywilliams-dnsop-dnsaid)
<a id="ietf-dnsaid"></a>

**IETF, work-item.** Individual Internet-Draft -02 (2026-05-27), "(No stream defined)", not adopted by a Working Group (WG); expires 2026-11-28. Related individual proposals, none adopted by a WG (datatracker, 2026-10-13): draft-ihsanullah-dnsid-01 (2026-06-29), draft-ferro-dnsop-apertoid-02 (2026-08-12), draft-morrison-mcp-dns-discovery-08 (2026-10-09) and draft-ranjbar-dane-did-01 (2026-08-01); DNS-AID is not among them. The IETF Secretariat announced on 2026-10-09 (15:20 UTC) a non-WG list, dns-underscore-keys (area INT), whose purpose is "To compare existing proposals for publishing keys, or references to them, under underscore labels in DNS" and names those four drafts; its public archive held three messages on 2026-10-13. The first post, by an author of one of the four drafts (2026-10-10), compares them on five axes: who the record is about, where the key sits, what makes the record trustworthy, revocation, and continuity of holding after a domain changes hands; it leaves open the enumeration of names in a zone, record size, and TXT against a new RRTYPE. On 2026-10-12 an author of another of the four wrote that "A 3 1 1 TLSA with SHA-256 is 35 bytes of RDATA" and "The full signed answer with the DO bit set is 271 bytes", measured on one live record (figures declared by the source, not reproduced here). The draft texts were not read for this entry; their content is as the list messages describe it. (as of 2026-10-13). The abstract says the document "standardizes an approach for publishing AI agents in the Domain Name System (DNS) so that other agents can discover them". The draft publishes AI agents in DNS; Section 5.6 reserves SvcParamKeys for "commercial signaling such as cost-per-unit-of-input, unit-of-input definitions, billing tiers, or rate-limit hints".

**Sources.** [third party] https://www.ietf.org/archive/id/draft-mozleywilliams-dnsop-dnsaid-02.txt (2026-10-02); [decision] https://datatracker.ietf.org/wg/dnsop/documents/ (2026-10-02); [third party] https://datatracker.ietf.org/doc/draft-ihsanullah-dnsid/ (2026-10-13); [third party] https://datatracker.ietf.org/doc/draft-ferro-dnsop-apertoid/ (2026-10-13); [third party] https://datatracker.ietf.org/doc/draft-morrison-mcp-dns-discovery/ (2026-10-13); [third party] https://datatracker.ietf.org/doc/draft-ranjbar-dane-did/ (2026-10-13); [third party] https://mailarchive.ietf.org/arch/msg/dns-underscore-keys/Atm6JcPnAlMDGYTfUwksFWi9KO4/ (2026-10-13); [third party] https://mailarchive.ietf.org/arch/msg/dns-underscore-keys/IZ2sMGeSEHr-A16iL6VCwtQWQeY/ (2026-10-13); [third party] https://mailarchive.ietf.org/arch/msg/dns-underscore-keys/9lSuPLAWz8e5aFdcwhYr4cutWYI/ (2026-10-13); [third party] https://datatracker.ietf.org/doc/html/draft-mozleywilliams-dnsop-dnsaid-02 (2026-10-05) Coverage: see [Evidence](#evidence-ietf-dnsaid).

### IETF WIMSE, AI Identity Management System (draft-ietf-wimse-aims)
<a id="ietf-wimse-aims"></a>

**IETF, work-item.** Working Group (WG) document draft-ietf-wimse-aims-00 (2026-09-15), Informational; adopted 2026-09-09, expires 2027-03-19; replaces draft-klrc-aiagent-auth. The datatracker record of 2026-10-13 gives revision 00 (time 2026-09-15 14:40 UTC) and no later revision. (as of 2026-10-13). The draft "proposes best practices for authentication and authorization of AI agent interactions"; commerce, merchant, seller or purchase text: not found in -00, 2026-10-02. ACP and AP2 appear only in the references.

**Sources.** [normative] https://www.ietf.org/archive/id/draft-ietf-wimse-aims-00.txt (2026-10-02); [decision] https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/ (2026-10-02) Coverage: see [Evidence](#evidence-ietf-wimse-aims).

### Payment HTTP Authentication Scheme (draft-httpauth-payment, Tempo Labs and Stripe)
<a id="ietf-httpauth-payment"></a>

**IETF, specification.** Individual draft-httpauth-payment-01 (2026-09-09), Standards Track intended, no Working Group (WG), expires 2027-03-13; authors from Tempo Labs and Stripe. The datatracker record of 2026-10-13 gives revision 01 (time 2026-09-09 16:08 UTC) and no later revision. (as of 2026-10-14). On receipts, -01 reads "Servers SHOULD include a Payment-Receipt header on successful responses"; the receipt table has four fields (status, method, timestamp, reference) and no signature field.

**Sources.** [decision] https://datatracker.ietf.org/doc/draft-httpauth-payment/ (2026-10-03); [third party] https://www.ietf.org/archive/id/draft-httpauth-payment-01.txt (2026-10-03); [statement] https://docs.stripe.com/payments/machine/mpp (2026-10-14) Coverage: see [Evidence](#evidence-ietf-httpauth-payment).

### GS1 Digital Link Standard, URI Syntax 1.7.0
<a id="gs1-digital-link"></a>

**GS1, specification.** Release 1.7.0 ratified August 2026; the archive on ref.gs1.org lists "Published 7 August 2026". (as of 2026-10-13). The syntax "distinguishes between primary identification keys that express simple GS1 identifiers, such as GTIN and GLN" and key qualifiers and attributes; a GS1 Digital Link URI "is a particular form of URL".

**Sources.** [normative] https://ref.gs1.org/standards/digital-link/uri-syntax/ (2026-10-13); [decision] https://ref.gs1.org/standards/digital-link/uri-syntax/archive (2026-10-13) Coverage: see [Evidence](#evidence-gs1-digital-link).

### UN Global Trust Register, namespace urn:gtr
<a id="un-gtr-urn"></a>

**UN/CEFACT, work-item.** Namespace "IANA registration pending" per the UN Transparency Protocol (UNTP) specification. Not found in the Internet Assigned Numbers Authority (IANA) Uniform Resource Name (URN) namespaces registry (updated 2026-10-12, read 2026-10-13): a record named gtr. (as of 2026-10-13). The specification says "Either register your own scheme with IANA or use the UN global trust register gtr URN namespace (IANA registration pending)", pattern urn:gtr:{identifier-scheme}:{identifier-value}.

**Sources.** [normative] https://untp.unece.org/docs/specification/IdentityResolver/ (2026-10-02); [decision] https://www.iana.org/assignments/urn-namespaces/urn-namespaces.xml (2026-10-13) Coverage: see [Evidence](#evidence-un-gtr-urn).

### IEEE P3931 Agent Description, Discovery, and Registry (ADDR) Interoperability
<a id="ieee-p3931-addr"></a>

**Other standards bodies, work-item.** PAR approved 2026-03-26; "Draft Development" on the IEEE SA active PARs page of the AI standards committee read on 2026-10-13. (as of 2026-10-13). The Project Authorization Request (PAR) says the standard will specify "a description model, registry mechanisms, and discovery protocols for intelligent agents operating across platforms, organizations, and ecosystems".

**Sources.** [normative] https://sagroups.ieee.org/ai-sc/active-pars/ (2026-10-13); [decision] https://standards.ieee.org/about/sasb/sba/26mar2026/ (2026-10-02) Coverage: see [Evidence](#evidence-ieee-p3931-addr).

### AAIF Identity and Trust group, issue
<a id="aaif-identity-trust"></a>

**AAIF, work-item.** Issue #13 of aaif/wg-identity-and-trust compares how MintID and Proofable record authority at the point where an agent action is dispatched; it was open with 8 comments on 2026-10-13, the last of 2026-10-09. The shared runner proposed for it, issue #287 and pull request #288 of agentrust-io/integrations, were open on 2026-10-13; the pull request was not merged (head 74fc43c) and had been approved on 2026-10-12 by the project lead of TRACE. TRACE, the format those integrations cite, is a specification (v0.2, Developer Preview) with a released reference package (agentrust-trace 0.11.0, 2026-09-25). The group's Reference Architecture sub-group has a working draft, "Agent Identity Primitives" (Draft, version 0.1, dated 2026-08-27), in a Google Doc readable without a login (read 2026-10-13). Its scope clause reads "The following are out of scope: authorization models (what an agent is permitted to do), evidence, reputation, and security controls or threat modeling.", and its section 3.4 (Delegation) reads "This section is under active discussion." Comments in the document propose changes that are not yet in the text; they are not quoted here. Commerce, merchant, seller and purchase: not found in the document text (2026-10-13). Messages of the group's list after message 48: not read (the archive requires JavaScript and its rules ask for a licence for automated AI access). (as of 2026-10-13). The group's README says "This working group meets every Thursday, alternating between 6:30AM and 9:00AM USA Pacific Time." and points to a public mailing list on lists.aaif.io; the archive of that list was not read, and six messages of it (numbers 40 and 44 to 48, 2026-10-06 to 2026-10-08) were read by the author on 2026-10-09. Proofable (proofable/docs): an earlier evidence packet (commits 3a45f02 to 4ceb58b, 2026-10-06 to 2026-10-08) had manifest digests computed over CRLF bytes, as its author stated on 2026-10-07; the packet frozen at commit 9851059 (2026-10-08) matches its SHA256SUMS (recomputed on 2026-10-13), and its author lists the limit "Author-operated (SELF); no independent witness." MintID publishes tags on GitLab (public-v2026-10-08.1 and public-v2026-10-08.2, 2026-10-08) and has no release objects. List messages: a participant from MintID wrote on 2026-10-08 that "From public-v2026-10-08.1 a 5xx is recorded as a service interruption, never as a decision, and the run completes"; a participant from ALIGN, an organisation preparing an independent run, wrote that ALIGN "will pin public-v2026-10-08.1 or later" and "We will confirm the start date on October 15."; a participant who submitted the runner wrote on 2026-10-08 that results are recorded "as operator-reported until independently reproduced". The runner (issue #287, pull request #288) says "This is a shared evidence-appraisal runner, not a comparative certification." and "No Verified tier or conformance level is requested."; the test counts given at different heads (27 in the pull request, 28, 34) are declared by the sources and not reconciled here. The README of agentrust-io/integrations defines two tiers, Community ("We do not run your code") and Verified, and says the tier "is set by maintainers, never self-declared". TRACE (agentrust-io/trace-spec): "Developer Preview. Launched at Confidential Computing Summit, 23 June 2026. Spec v0.2 is current."; the specification text is under the Community Specification License 1.0 and the code under Apache 2.0; the project lead listed in MAINTAINERS.md is Imran Siddique (AgenTrust-io).

**Sources.** [third party] https://github.com/aaif/wg-identity-and-trust/issues/13 (2026-10-13); [statement] https://github.com/aaif/wg-identity-and-trust/blob/main/README.md (2026-10-09); [third party] https://github.com/agentrust-io/integrations/issues/286 (2026-10-09); [third party] https://github.com/agentrust-io/integrations/issues/287 (2026-10-13); [third party] https://github.com/agentrust-io/integrations/pull/288 (2026-10-13); [third party] https://github.com/agentrust-io/integrations/pull/288#pullrequestreview-5447425825 (2026-10-09); [third party] https://github.com/agentrust-io/integrations/blob/084571bd337ab605219a74ac183604a74f0c3eb5/integrations/alakris-authority-comparison/RESULTS.md (2026-10-09); [statement] https://github.com/agentrust-io/integrations/blob/main/README.md (2026-10-09); [statement] https://github.com/agentrust-io/trace-spec/blob/main/README.md (2026-10-09); [statement] https://github.com/agentrust-io/trace-spec/blob/main/MAINTAINERS.md (2026-10-09); [decision] https://github.com/agentrust-io/trace-spec/releases/tag/v0.11.0 (2026-10-09); [third party] https://github.com/proofable/docs/commit/63fc73ba27e510b4a06e352321820ae0759653c2 (2026-10-09); [third party] https://gitlab.com/mintid/mintid/-/tags (2026-10-09); [statement] https://github.com/agentrust-io (2026-10-09); [statement] https://github.com/agentrust-io/integrations (2026-10-09); [third party] https://lists.aaif.io/g/wg-identity-trust/message/44 (2026-10-09); [third party] https://lists.aaif.io/g/wg-identity-trust/message/45 (2026-10-09); [third party] https://lists.aaif.io/g/wg-identity-trust/message/46 (2026-10-09); [third party] https://lists.aaif.io/g/wg-identity-trust/message/47 (2026-10-09); [third party] https://gitlab.com/mintid/mintid/-/tree/public-v2026-10-08.2/test-harness/trace/records (2026-10-09); [third party] https://lists.aaif.io/g/wg-identity-trust/message/40 (2026-10-09); [third party] https://lists.aaif.io/g/wg-identity-trust/message/48 (2026-10-09); [third party] https://github.com/proofable/docs/commit/3a45f026fd0c06b9d1d411c053597584b6b1c3dd (2026-10-09); [third party] https://github.com/proofable/docs/commit/4ceb58b68784266be73957c0727bbbf1477bf25b (2026-10-09); [third party] https://github.com/agentrust-io/integrations/issues/287#issuecomment-6051738118 (2026-10-09); [third party] https://docs.google.com/document/d/1nu4k_6zBgyEowLphuuaNrn6TnQbgeJm7FMkD7R-EXiA (2026-10-13); [third party] https://github.com/proofable/docs/tree/9851059900e29ba701bb0f4df2bf89a2107f430c/public/evidence/aaif/authority-at-dispatch/2026-10-08 (2026-10-13) Coverage: see [Evidence](#evidence-aaif-identity-trust).

### AAIF structure, Technical Committee and working groups
<a id="aaif-structure"></a>

**AAIF, venue.** AAIF has a Governing Board, a Technical Committee and working groups, each with a repository; Agentic Commerce has its own entry. Hosted projects listed on aaif.io/projects (2026-10-18): Model Context Protocol, goose, AGENTS.md, agentgateway, Agent2Agent (A2A) and Agent Router. (as of 2026-10-18). aaif.io describes AAIF as "a neutral, open foundation under the Linux Foundation". Its Identity and Trust group aims at standards so "agents can be discovered across platforms, prove who they are, who they act for". Taxonomy and Landscape Workstream (repository ws-taxonomy-landscape, read on 2026-10-09 at commit 6ac90f5 of main): its charter lists the deliverables "Shared Taxonomy Explorer (v1.0)" with the date 2026-08-15 and "Ecosystem Architecture Map (v1.0)", `landscape.yml` plus a web application, with the date 2026-10-15; these are dates of a charter table, not a commitment of the workstream. On 2026-10-13 a portal titled "Taxonomy and Landscape Portal" is published at aaif.github.io/ws-taxonomy-landscape (page marked updated 2026-10-11, 8:13 pm) with links to a Shared Taxonomy Explorer and an Ecosystem Landscape Map; neither is called v1.0 on the page, the repository has no release (0) and no tag read, its commits to 2026-10-12 define taxonomy terms, and the date 2026-10-15 of the Ecosystem Architecture Map is still ahead. Its README says "The Landscape remains on the future roadmap, but its contribution and review process has not yet been accepted." and that "pull requests that propose Landscape changes will be closed"; the text was added by PR #61 ("docs: clarify current taxonomy-only contribution scope", merged 2026-09-16). PR #83 ("Clarify taxonomy contribution process", merged 2026-10-07) rewrote CONTRIBUTING.md: a term is raised in a Working Group, a delegate adds it to the taxonomy spreadsheet, the weekly workstream meeting votes KEEP, CULL or DEBATE, and only then does a delegate open a pull request, which needs approval from delegates of two different Working Groups before it is merged and the term is marked FINALIZED; the guide adds "A pull request for a term that has not received a KEEP vote will be closed."

**Sources.** [statement] https://aaif.io/projects (2026-10-18); [statement] https://aaif.io/about (2026-10-03); [normative] https://github.com/aaif/wg-identity-and-trust/blob/main/charter.md (2026-10-03); [normative] https://github.com/aaif/ws-taxonomy-landscape/blob/main/charter/charter.md (2026-10-09); [normative] https://github.com/aaif/ws-taxonomy-landscape/blob/main/README.md (2026-10-09); [normative] https://github.com/aaif/ws-taxonomy-landscape/blob/main/CONTRIBUTING.md (2026-10-09); [decision] https://github.com/aaif/ws-taxonomy-landscape/pull/61 (2026-10-09); [decision] https://github.com/aaif/ws-taxonomy-landscape/pull/83 (2026-10-09); [statement] https://aaif.github.io/ws-taxonomy-landscape/ (2026-10-13); [statement] https://home.mlops.community/public/events/accuracy-and-reliability-of-ai-agents-virtual-summit-77nje0s530 (2026-10-13) Coverage: see [Evidence](#evidence-aaif-structure).

### Agent2Agent (A2A) protocol, core specification
<a id="a2a-core"></a>

**AAIF, specification.** Hosted project of the Agentic AI Foundation (AAIF, under the Linux Foundation): the AAIF announced on 2026-08-17 that A2A "is joining the Agentic AI Foundation (AAIF) as a hosted project", and the A2A blog of 2026-08-27 says it was "accepted as a Growth Stage project". Latest release v1.0.1, 2026-05-28. Technical Steering Committee of eight company seats: Google, Microsoft, Cisco, AWS, Salesforce, ServiceNow, SAP, IBM. (as of 2026-10-18). The AgentCard is defined in specification/a2a.proto as "A self-describing manifest for an agent."; how cards are found is in a2a-discovery. PR #2081, merged on 2026-07-30, added section 7.6.4 to the specification: "Agents MUST NOT treat the TASK_STATE_AUTH_REQUIRED state transition, by itself, as authorization for any particular operation."; the PR description calls the state "a coordination signal, not an authorization grant".

**Sources.** [normative] https://github.com/a2aproject/A2A/blob/main/specification/a2a.proto (2026-10-03); [normative] https://github.com/a2aproject/A2A/blob/main/GOVERNANCE.md (2026-10-03); [decision] https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents (2026-10-03); [decision] https://aaif.io/blog/a2a-joins-aaif (2026-10-18); [statement] https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/ (2026-10-18); [statement] https://aaif.io/projects (2026-10-18); [normative] https://github.com/a2aproject/A2A/blob/main/docs/specification.md (2026-10-08); [third party] https://github.com/a2aproject/A2A/pull/2081 (2026-10-08); [normative] https://www.iana.org/assignments/well-known-uris/well-known-uris.xml (2026-10-05) Coverage: see [Evidence](#evidence-a2a-core).

### Model Context Protocol (MCP), core specification
<a id="mcp-core"></a>

**AAIF, specification.** Specification version 2026-07-28 (the latest release is 2026-07-28; the specification directory holds 2025-03-26, 2025-06-18, 2025-11-25, 2026-07-28 and a draft; no later release, read 2026-10-13); the blog post of 2025-12-09 says "Anthropic is donating MCP to the Agentic AI Foundation". (as of 2026-10-13). The specification describes MCP as "an open protocol that enables seamless integration between LLM applications and external data sources and tools"; discovery is in mcp-server-card and lf-ai-catalog.

**Sources.** [normative] https://modelcontextprotocol.io/specification/latest (2026-10-03); [decision] https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/ (2026-10-03); [statement] https://aaif.io/projects (2026-10-18) Coverage: see [Evidence](#evidence-mcp-core).

### DIF Trusted AI Agents Working Group
<a id="dif-trusted-ai-agents"></a>

**Linux Foundation, venue.** Active; Delegated Authority and KYA-OS task forces; weekly meetings. (as of 2026-10-13). The group defines "an opinionated, interoperable stack to enable trustworthy, privacy-preserving, and secure AI agents"; KYA-OS (donated by Vouched, March 2026) covers agent identity and delegation with DIDs and VCs.

**Sources.** [normative] https://identity.foundation/working-groups/trusted-agents.html (2026-10-13); [statement] https://blog.identity.foundation/kya-os/ (2026-10-02); [statement] https://identity.foundation/faq/ (2026-10-15); [normative] https://github.com/decentralized-identity/org/blob/main/Org%20documents/Membership%20agreements/DIF%20Project%20Charter%20_4.0.3.pdf (2026-10-15) Coverage: see [Evidence](#evidence-dif-trusted-ai-agents).

### TRACE (Trust, Runtime Attestation and Compliance Evidence)
<a id="trace"></a>

**Linux Foundation, specification.** Specification version 0.2, described in its text as "0.2: Draft" with status "RFC: Request for Comments"; the repository README calls it a Developer Preview launched on 23 June 2026, and the Python package agentrust-trace 0.11.0 was released on 2026-09-25. The README states that the specification is hosted at the Linux Foundation as "TRACE Specification, a Series of LF Projects, LLC", and a Linux Foundation press release of 2026-08-25 announces the contribution of TRACE from OPAQUE. Reading of 2026-10-13: the README of the repository now says "a proposal to bring it into the Agentic AI Foundation as a Sandbox project is in progress" and points to aaif/project-proposals issue #42, which is open with the label Under Review, 8 comments and a last update on 2026-10-02; the specification stays at v0.2 ("Spec v0.2 is current"), main is at commit 8562b09 (2026-10-13, 00:33 UTC), and the latest release objects are conformance-v0.6.2 (2026-10-03, the conformance test package) and v0.11.0 (2026-09-25). The folder spec/ also holds a draft named mcp-profile-v0.3-draft.md, not read. (as of 2026-10-13). The specification says "This is the rulebook for TRACE: it defines the Trust Record (a signed receipt describing one AI agent run), how records are anchored in a" The README describes TRACE as "an open format for a signed receipt of an AI agent run: what ran, where, under which rules, on what kind of data, and which" and states its limit: "A v0.2 signature proves who made a record and that it has not changed. It does not prove the hardware claims inside it". The specification text is under the Community Specification License 1.0 and the code under Apache 2.0 (LICENSE and README); GitHub's repository metadata reports the licence as NOASSERTION. MAINTAINERS.md lists as Project Lead Imran Siddique (AgenTrust-io), as spec editors Rishabh Poddar and Aaron Fulkerson (OPAQUE Systems), and two repository maintainers listed in the same file. The Linux Foundation press release says "The Linux Foundation will provide vendor-neutral governance for TRACE to support sustainability and long-term growth." In the AAIF Identity and Trust work TRACE is the format cited by the shared runner of agentrust-io/integrations, which validates "reference shapes" of the released package agentrust-trace 0.11.0, a reference package, not a version of the specification, which is v0.2 (see aaif-identity-trust).

**Sources.** [statement] https://github.com/agentrust-io/trace-spec/blob/main/README.md (2026-10-13); [statement] https://github.com/aaif/project-proposals/issues/42 (2026-10-13); [normative] https://github.com/agentrust-io/trace-spec/blob/main/spec/trace-v0.2.md (2026-10-09); [statement] https://github.com/agentrust-io/trace-spec/blob/main/MAINTAINERS.md (2026-10-09); [normative] https://github.com/agentrust-io/trace-spec/blob/main/LICENSE (2026-10-09); [decision] https://github.com/agentrust-io/trace-spec/releases/tag/v0.11.0 (2026-10-09); [statement] https://www.linuxfoundation.org/press/linux-foundation-welcomes-trace-to-advance-verifiable-runtime-evidence-for-ai-workloads (2026-10-09) Coverage: see [Evidence](#evidence-trace).

### EMILIA Protocol (individual drafts and open-source gate)
<a id="emilia-protocol"></a>

**Independent, work-item.** Two Internet-Drafts by Iman Schrock (EMILIA Protocol, Inc.) were current on 2026-10-08: draft-schrock-ep-architecture-03 (2026-09-06, Informational) and draft-schrock-action-evidence-boundary-07 (2026-09-25, Informational). The Apache-2.0 repository emiliaprotocol/emilia-protocol was created on 2026-03-13. (as of 2026-10-08). The architecture draft "composes the Canonical Action Identifier (CAID), Authorization Evidence Chain (AEC), and Action Evidence Boundary (AEB)" and says "A valid signature, a current credential, a satisfied evidence requirement, and an observed effect remain different facts." The README says "EMILIA Gate checks authority before a protected tool runs"; its example MCP payment server "refuses a call without approval, binds approval to the amount, currency, vendor, and destination", and the README calls the example "a local demonstration" with "a mock payment tool". The boundary draft refers to AP2 repeatedly (counts in the evidence). On the AUDIT list its author and Sumit Ahuja are writing an expected-record draft that cites the boundary draft (see ietf-audit); on the agentproto list the author pointed on 2026-10-03 to the repository's response-loss example. AAIF Identity and Trust issue #13 compares MintID and Proofable; EMILIA does not appear in the comments of that issue read on 2026-10-08.

**Sources.** [third party] https://datatracker.ietf.org/doc/draft-schrock-ep-architecture/ (2026-10-08); [third party] https://datatracker.ietf.org/doc/draft-schrock-action-evidence-boundary/ (2026-10-08); [third party] https://github.com/emiliaprotocol/emilia-protocol (2026-10-08); [third party] https://mailarchive.ietf.org/arch/msg/agentproto/_-7ahBTxuzTScC_1yCTarPXsbzU/ (2026-10-08); [third party] https://github.com/aaif/wg-identity-and-trust/issues/13 (2026-10-08) Coverage: see [Evidence](#evidence-emilia-protocol).

### OpenID Foundation AuthZEN Working Group (agent authorization drafts AARP and COAZ)
<a id="oidf-authzen-agents"></a>

**Independent, work-item.** AARP and COAZ adopted as Working Group Drafts on 2026-06-15; to be refined through community review and interoperability testing. (as of 2026-10-13). AARP covers prerequisites such as approvals, consent or attestations before a policy decision; COAZ, the profile for MCP tool authorization, maps information models into the Subject-Action-Resource-Context structure. The OpenID Foundation published a whitepaper, "Identity Management for Agentic AI" (OpenID Foundation page 2025-10-07, arXiv 2510.25819 v1 2025-10-29), on authentication and authorization for AI agents; it "outlines the resources already available for securing today's agents and presents a strategic agenda". The whitepaper names Web Bot Auth, one IETF proposal described as a "passport for agents", and the Agent Payments Protocol (AP2); it does not name UCP, ACP, x402 or TAP (text search, counts in the evidence).

**Sources.** [third party] https://arxiv.org/abs/2510.25819 (2026-10-06); [third party] https://openid.net/new-whitepaper-tackles-ai-agent-identity-challenges/ (2026-10-06); [decision] https://openid.net/openid-foundation-advances-authorization-for-the-agent-era-with-new-authzen-working-group-drafts/ (2026-10-13); [statement] https://openid.net/wg/ (2026-10-02) Coverage: see [Evidence](#evidence-oidf-authzen-agents).

### schema.org vocabulary for products, offers, sellers and lodging (current release)
<a id="schemaorg-baseline"></a>

**Independent, specification.** Current release V30.1, 2026-09-16 (previous 30.0, 2026-03-19). Term definitions are quoted from schema.org without comment. (as of 2026-10-13). Present: Product ("Any offered product or service."), Offer ("An offer to transfer some rights to an item or to provide a service"), Organization, LocalBusiness, LodgingBusiness, MerchantReturnPolicy, gtin.

**Sources.** [normative] https://schema.org/version/latest (2026-10-03); [normative] https://schema.org/Product (2026-10-03); [normative] https://schema.org/docs/releases.html (2026-10-13) Coverage: see [Evidence](#evidence-schemaorg-baseline).

### FIDO Alliance agentic authentication and payments work
<a id="fido-agentic-standards"></a>

**Industry, work-item.** Announced 2026-04-28: an Agentic Authentication Technical Working Group, and work in the Payments Technical Working Group starting from Google (AP2) and Mastercard (Verifiable Intent) contributions. (as of 2026-10-14). The release says the Payments Technical Working Group is "chaired by members from Mastercard and Visa"; it says contributed; Google's announcement of the same day says "We’re donating Agent Payments Protocol to the FIDO Alliance", and the AP2 repository says its core specification has been donated to FIDO. For the Agentic Authentication Technical Working Group the release says it is "chaired by members from CVS Health, Google and OpenAI and vice-chaired by members from Amazon, Google and Okta" (read in a browser on 2026-10-14); it names companies, not persons.

**Sources.** [decision] https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/ (2026-10-14); [decision] https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/ (2026-10-18); [normative] https://github.com/google-agentic-commerce/AP2/blob/main/CONTRIBUTING.md (2026-10-03) Coverage: see [Evidence](#evidence-fido-agentic-standards).

### Shopify, MCP surfaces for buyer agents, developers and merchants
<a id="shopify"></a>

**Industry, work-item.** Three distinct MCP surfaces are documented or published by Shopify: checkout for buyers' agents (server-side Checkout MCP and, since 2026-09-28, Checkout WebMCP), the local developer package @shopify/dev-mcp (latest version 1.16.0, 2026-09-25), and a remote MCP for merchants at setup.shopify.com/mcp. For the merchant surface the source is Shopify's own toolkit repository; no page on shopify.dev was found for it. A fourth surface is for shoppers' agents: the command-line client @shopify/shop (npm, MIT; version 1.0.3 published 2026-10-08, 01:20 UTC, after 1.0.2 on 2026-10-07), whose repository Shopify/shop has its latest commit d1e8c7c on main (2026-10-08, 01:17 UTC); neither the README, the skill file nor the transactions reference declares a beta or preview status or a list of supported countries (not found, 2026-10-13). (as of 2026-10-13). Buyers' agents: the documentation says "Use Checkout WebMCP when your agent runs in the buyer's browser. If your agent can run on a server, then use Checkout MCP", and that Checkout WebMCP "implements the UCP checkout capability (dev.ucp.shopping.checkout)"; see ucp and browsers-webmcp. Developers: @shopify/dev-mcp is a local npm package (npm registry, read 2026-10-08 and 2026-10-13, version 1.16.0 published 2026-09-25). Merchants: Shopify-AI-Toolkit v2.1.0 (2026-10-01) states "The Cursor plugin, which Grok Bot also installs from the Cursor Marketplace, now connects to Shopify's remote MCP at `setup.shopify.com/mcp`"; the file .cursor-plugin/mcp.json at that tag declares an http server with that URL and an auth block with a client id, and v2.1.1 (2026-10-08) changes the plugin description to "Create and manage your store with Shopify". The toolkit release v2.0.1 says "Regenerated agent skills from @shopify/shopify-dev-tools 1.17.1"; the package @shopify/shopify-dev-tools returns E404 on the npm registry (2026-10-08 and 2026-10-13). Since v2.0.0 the toolkit publishes UCP as a separate skill: the CHANGELOG entry for 2.0.0 reads "UCP ships separately as `ucp`", and the folder skills/ucp at the tag v2.1.1 (commit 26d0623, 2026-10-08, 00:34 UTC) holds a SKILL.md named ucp whose description begins "Use when the user wants to use the UCP CLI to find, compare, buy, or track products from online merchants" and which requires the binary ucp (read 2026-10-13). Shopper's agents: the README of Shopify/shop (commit d1e8c7c, read 2026-10-13) says the command-line interface (CLI) "lets agents search millions of stores, build carts, check out and pay with the shopper's Shop account, and track orders" and is a client of Shop's MCP server at mcp.shop.com. It says: "Some stores have no agent checkout API (UCP); the agent has to enter a payment credential into the site's checkout form in a browser." For that case the shopper approves a "spend request" on Shop and the agent receives a one-time credential up to the approved limit; the skill file says "Prefer Shop/UCP checkout when available". The reference skills/shop/references/transactions.md says of the agent's report on the purchase "This records your report, not payment confirmation.", of a credential state "`consumed` without an `instrument` does not establish credential delivery or payment.", and of cancelling the request "this does not cancel/refund the purchase or revoke an issued credential." The core of the CLI is a compiled binary (lib/shop.wasm, about 1.9 MB), so its logic is not readable as source; the repository holds nine commits, all of 2026-10-07 and 2026-10-08. No call was made to any MCP or OAuth endpoint; only documentation, repositories and listings were read.

**Author participation.** The author of this map opened issue #62 of Shopify/Shopify-AI-Toolkit on 2026-09-26 (release notes and a source link for @shopify/dev-mcp, and two telemetry questions), still without comments on 2026-10-13; see Disclosure.

**Sources.** [statement] https://github.com/Shopify/Shopify-AI-Toolkit/releases/tag/v2.1.0 (2026-10-08); [statement] https://github.com/Shopify/Shopify-AI-Toolkit/releases/tag/v2.1.1 (2026-10-08); [statement] https://github.com/Shopify/Shopify-AI-Toolkit/releases/tag/v2.0.1 (2026-10-08); [normative] https://github.com/Shopify/Shopify-AI-Toolkit/blob/v2.1.0/.cursor-plugin/mcp.json (2026-10-08); [statement] https://github.com/Shopify/Shopify-AI-Toolkit/blob/v2.1.1/.cursor-plugin/plugin.json (2026-10-08); [normative] https://shopify.dev/docs/agents/carts-and-checkout/checkout-webmcp (2026-10-08); [third party] https://github.com/Shopify/Shopify-AI-Toolkit/issues/62 (2026-10-13); [statement] https://github.com/Shopify/Shopify-AI-Toolkit/blob/v2.1.1/CHANGELOG.md (2026-10-13); [statement] https://github.com/Shopify/Shopify-AI-Toolkit/blob/v2.1.1/skills/ucp/SKILL.md (2026-10-13); [statement] https://github.com/Shopify/shop/blob/d1e8c7c/README.md (2026-10-13); [statement] https://github.com/Shopify/shop/blob/d1e8c7c/skills/shop/SKILL.md (2026-10-13); [statement] https://github.com/Shopify/shop/blob/d1e8c7c/skills/shop/references/transactions.md (2026-10-13); [statement] https://registry.npmjs.org/@shopify%2fshop (2026-10-13) Coverage: see [Evidence](#evidence-shopify).

---

<a id="part-evidence"></a>
# Part 10: Appendix: Evidence and coverage

<a id="evidence-w3c-ai-agent-protocol-cg"></a>**W3C AI Agent Protocol Community Group.** Read: On 2026-10-13: the October 2026 index of public-agentprotocol (5 messages, subjects and dates) and the chairs listed on the W3C group data. Not read: Meeting minutes (2026-09-09, 2026-09-23), attachments, Google Docs and slides.

<a id="evidence-w3c-agent-identity-registry-cg"></a>**W3C Agent Identity Registry Protocol Community Group.** Read: On 2026-10-13: the October 2026 index of public-agent-identity (4 messages, subjects and dates) and the chairs listed on the W3C group data. public-agent-identity (August to October 2026) read on 2026-10-03 without quoted replies. Not read: Group description in full, repository w3c-cg/agent-identity, minutes, cross-posted documents. Not found in those messages: agenticweb, webbotauth, kyapay, dif.

<a id="evidence-w3c-agent-ready-video-cg"></a>**W3C Agent-Ready Video Community Group.** Read: On 2026-10-13: the chairs listed on the W3C group data and the October 2026 index of the group's list. Not read: The list of the group, created on 2026-10-01. Not found on 2026-10-03 in w3c/strategy, w3c/charter-drafts or WebKit/standards-positions (from 2026-01-01): Agent-Ready Video, ARV.

<a id="evidence-w3c-agent-to-web-framework-cg"></a>**W3C Agent-to-Web Framework (A2WF) Community Group.** Read: On 2026-10-13: the chairs listed on the W3C group data and the October 2026 index of public-a2wf (404). Not read: Relation to the exclusion of "Agent to Server communications" in the draft Agentic Web charter. Not found on 2026-10-03: a deliverable, repository, charter or meeting of the group.

<a id="evidence-w3c-agenticweb-wg"></a>**W3C Agentic Web Working Group (draft charter).** Read: On 2026-10-14 also: the state, merge time and reviews of PR #888 (GitHub). Not read: Charter HTML in the 2026-10-03 files, list archives, meeting minutes, TPAC breakout slots.

<a id="evidence-w3c-did-methods-wg"></a>**W3C DID Methods Working Group (proposed charter).** Read: Charter read in full on 2026-10-02; announcement of 2026-09-30 read on 2026-10-03 and again on 2026-10-13, with the announcements of 2026-08-10 (start of refinement of the DID WG maintenance charter) and 2026-10-07 (proposed DID WG charter sent to the Advisory Committee). Not read: The public-review-comments list. Not found in the charter text, 2026-10-02: agent, AI, commerce, merchant, payment, delegat (word stem).

<a id="evidence-w3c-did-resolution"></a>**W3C DID Resolution.** Read: On 2026-10-13: the minutes of the DID WG call of 2026-10-08 (w3.org/2026/10/08-did-minutes.html, read in the sections on PR #344 and the poll). Not read: Minutes pages at w3.org other than that of 2026-10-08, Google Docs with the votes and slides of PR #344, the DID WG maintenance charter; the merged text of the specification and its at-risk markings; the repository role of the account that merged the PR.

<a id="evidence-w3c-did-wg"></a>**W3C Decentralized Identifier Working Group (proposed charter).** Read: The proposed charter page in full and the announcement of 2026-10-07, read 2026-10-08. Not read: The charter's GitHub history and issues, the public-review-comments archive, the current charter of the group. Not found, 2026-10-08: agent, payment, product, commerce.

<a id="evidence-w3c-digital-policy-wg"></a>**W3C Digital Policy Working Group (ODRL, draft charter).** Read: Charter read in full as published HTML on 2026-10-02; refinement announcement and breakout #17 read on 2026-10-03. Not read: GitHub source of the charter in w3c/odrl; ODRL lists and repositories. Not found in the charter text, 2026-10-02: agent, commerce, merchant, product.

<a id="evidence-w3c-tpac-2026"></a>**W3C TPAC 2026 breakouts on agents (Dublin, 2026-10-26/30).** Read: Issues of w3c/tpac2026-breakouts and items of w3c/tpac2026-miniworkshops; README of tpac2026-breakouts (last commit 2026-09-30); event and news pages, read on 2026-10-03. Not read: Dates of the mini-workshops (not stated in the items read); the matching of the sessions to issue numbers is by title, not by a link on the calendar page.

<a id="evidence-w3c-web-payment-security-ig"></a>**W3C Web Payment Security Interest Group.** Read: Charter and group page read on 2026-10-02; webai-roadmap and ai-web-impact items read on 2026-10-03. Not read: Member-only mailing list, wiki sub-pages, TPAC 2025 and 2026 minutes of the IG; w3c/wpsig is empty in the files read. Not found in the charter text, 2026-10-02: agent.

<a id="evidence-w3c-browser-testing-tools-wg"></a>**W3C browser-testing-tools Working Group (charter draft).** Read: The description and metadata of pull request #882, read 2026-10-08. Not read: The charter text, the issue it refers to in webdriver-bidi, the current charter of the group.

<a id="evidence-w3c-gs1-ecommerce-workshop"></a>**W3C/GS1 Workshop on E-commerce for Humans and AI Agents (Zurich, 8-9 Sep 2026).** Read: On 2026-10-13: the file listing and the latest commits of the workshop repository and breakout issue #34. Not read: The other slide files (PRs #57 to #85) and the position-statement PDFs in position_statement/ (Fabacus, KYA-OS, P&G); report and agenda pages, pre-recordings.

<a id="evidence-w3c-webmcp-cg-report"></a>**WebMCP (Draft Community Group Report, Web Machine Learning CG).** Read: On 2026-10-13: the draft report page and the latest commits of the repository (to 2026-10-09), PR #338 and issues #65, #192 and #257. Not read: Minutes pages, section 6.2 of the specification, items #165, #204, #255, #272, #273 and #312 in full.

<a id="evidence-ietf-dnsaid"></a>**DNS for AI Discovery (DNS-AID, draft-mozleywilliams-dnsop-dnsaid).** Read: On 2026-10-13 also: the datatracker records (revision number and revision date) of the four related drafts, and the three messages of the archive of dns-underscore-keys. Not read: A DNS-AID thread under another subject on dnsop; the texts of the four related drafts. Not found: Adoption call, objection or dated promise for the draft: not found in the lists read, 2026-10-03.

<a id="evidence-ietf-aipref"></a>**IETF AI Preferences (aipref WG).** Read: On 2026-10-13: the datatracker records of draft-ietf-aipref-vocab and draft-ietf-aipref-attach. ai-control list, 2026-08-01 to 2026-09-30 (137 messages, read without quoted replies); datatracker history of draft-ietf-aipref-vocab; editor copy of the vocabulary and attach drafts, by keyword. Not read: Posted text of -08, WG milestones page, August interim minutes, repository issues and pull requests, use-case wiki. Not found in the ai-control list, 2026-08-01 to 2026-09-30: commerce, merchant, checkout, Know Your Agent (KYA), know your agent, minors, buyer age.

<a id="evidence-ietf-audit"></a>**IETF AUDIT (BoF preparation).** Read: On 2026-10-13 also: the session request data of IETF 127 for audit (API); the three audit list messages of 2026-10-11 and 2026-10-12 on case 9, found among the 40 latest messages of the list page. Not read: The expected-record draft (announced, no text read); diffs of PR #52, #53, #58, #60; issues of mirjak/draft-audit-architecture; the audit list before 2026-09-17 for the e-commerce search. Not found in the items read, 2026-10-02: minors, buyer age, terms of use, Know Your Agent (KYA), product identity. Not found in the 80 audit list messages (2026-09-17 to 2026-10-06): e-commerce, UCP, ACP, AP2, x402, Verifiable Intent, Visa. Not found in the draft-kuehlewind-audit-architecture files and history, 2026-10-06: e-commerce. Not found on the datatracker BoF page (2026-10-02) and in the IETF 127 agenda updated 2026-10-02 (read 2026-10-06): an AUDIT session.

<a id="evidence-ietf-dawn"></a>**IETF DAWN, Discovery of Agents With Names (proposed WG).** Read: On 2026-10-14: the datatracker charter page and the ballot page of charter-ietf-dawn-00-10 (summary, positions) and the WG Review announcement (chairs). Not read: Ballot comments and positions beyond the summary and the count of positions, the ietf-announce messages after 2026-10-12, the DAWN list messages of 2026-10-10 to 2026-10-12 other than the one cited. Not found in the 200 messages, 2026-10-03: AI Catalog.

<a id="evidence-ietf-wimse-aims"></a>**IETF WIMSE, AI Identity Management System (draft-ietf-wimse-aims).** Read: On 2026-10-13: the datatracker record. Not read: Issues of the draft repository; section numbers quoted by participants are from an earlier draft, not checked against -00. Not found in the AIMS threads read, 2026-10-03: commerce or merchant text.

<a id="evidence-ietf-webbotauth"></a>**IETF Web Bot Auth (webbotauth WG).** Read: WG charter and documents pages, read in full 2026-10-02; web-bot-auth list messages, 2026-08-01 to 2026-09-21, read 2026-10-03; the 11 messages of 2026-10-04 to 2026-10-08, read 2026-10-08; on 2026-10-13 the datatracker pages of the WG documents, of draft-ietf-webbotauth-httpsig-protocol and of draft-illyes-webbotauth-cbcp, the subjects and dates of the 26 latest list messages (2026-10-05 to 2026-10-13) and, in part, four messages of 2026-10-10 to 2026-10-13, and the state of cbcp PRs #19, #22 and #23; on 2026-10-09 the messages of the three threads below and the message of 2026-10-09 on Appendix C.1 (revocation and Cache-Control, signing on request, one Signature-Agent per purpose) and the announcement thread of the crawler best practices, read on mailarchive.ietf.org, and the repository garyillyes/cbcp at commit cc9942d with its pull requests #22 and #23. Not read: The list messages of 2026-10-10 to 2026-10-13 beyond their subjects and the first lines of four of them, the list before 2026-08-01, issues of the draft repository. Not found in datatracker and list (2026-08-01 to 2026-09-21): milestone completion, Know Your Agent (KYA), KYAPay, Mastercard Agent Pay.

<a id="evidence-ietf-agentproto"></a>**IETF agentproto (Agent Communication Protocols WG).** Read: On 2026-10-13: the datatracker pages of the group (about, charter, related drafts), the subjects, senders and dates of the 40 latest list messages (2026-10-08 to 2026-10-13), eight of them in full (one of 2026-10-10, three of 2026-10-12 among them the chairs' message and a chair's answer, four of 2026-10-13), and the session request data of IETF 127 (API). Not read: The other list messages of 2026-10-08 to 2026-10-13 (subjects only), the texts of the related drafts; Threads on AGTP, SAMP, DMSC, COSA; messages in Chinese and Persian; IETF 126 minutes and chat log; 00-04 ballot positions on the list. Not found in 00-00 to 00-04: the list-proposed text. Not found in 408 messages, 2026-10-03: consent, Know Your Agent (KYA), AP2, x402.

<a id="evidence-ietf-vcon"></a>**IETF vcon (Virtualized Conversations WG).** Read: On 2026-10-13: issue #40 and PR #41 of the core draft repository (state and text), the history page of the charter, the datatracker pages of the group, its charter, draft-ietf-vcon-vcon-core and draft-rosenberg-vcon-restructure, pull request #37, and the subjects and dates of the latest 40 messages of the vcon list (to 2026-10-11). Not read: The messages of the vcon list before 2026-09-01, the minutes, and the completion state of the milestones. Not found in the 35 vcon list messages (2026-09-01 to 2026-10-06) and in the texts of draft-ietf-vcon-vcon-core-04, draft-ietf-vcon-overview-02, draft-rosenberg-vcon-restructure-00, draft-howe-vcon-agent-session-00 and draft-rosenberg-cheq-00, 2026-10-06: UCP, ACP, AP2, x402, Verifiable Intent, Visa. Not found in the files, issues and pull requests of the repositories of UCP, ACP, AP2, x402, Verifiable Intent and Visa TAP, 2026-10-06: vCon or "virtualized conversation". Not found in charter-ietf-vcon-01, 2026-10-06: commerce, payment, purchase, agent.

<a id="evidence-ietf-individual-seller-drafts"></a>**Individual IETF drafts on the seller side.** Read: On 2026-10-13: the datatracker records of the three drafts (anders -01 of 2026-07-04, kavian -01 of 2026-09-04, hood -02 of 2026-05-26; no later revision) and the text of hood -02. Not read: Full texts of the anders and kavian drafts, authors' next steps, WG agendas, whether the kavian draft names UCP, ACP or GS1. Not found in the DAWN list (2026-08-01 to 2026-10-02) and dnsop list text, 2026-10-03: names of the three drafts.

<a id="evidence-ietf-httpauth-payment"></a>**Payment HTTP Authentication Scheme (draft-httpauth-payment, Tempo Labs and Stripe).** Read: On 2026-10-13: the datatracker record. Not read: Full -01 text, payment method and intent specifications on mpp.dev, software development kit (SDK) licensing, IETF list discussion, Tempo pages. mpp.dev was not read again on 2026-10-14: its robots.txt carries the signal ai-input=no. Not found, 2026-10-03, in -01: agent protocol, card network, AP2, x402, Verifiable Intent; in the eight lists: the draft name. The Stripe page on the Machine Payments Protocol (MPP), read 2026-10-14, describes MPP as "co-authored by Stripe and Tempo" and does not mention this draft; a statement by a primary source that links the draft to MPP: not found there.

<a id="evidence-gs1-digital-link"></a>**GS1 Digital Link Standard, URI Syntax 1.7.0.** Read: The URI Syntax standard page and its archive on ref.gs1.org, read 2026-10-03 and again 2026-10-13 ("Release 1.7.0, Ratified Aug 2026"; archive: "Published 7 August 2026"). Not read: The www.gs1.org standards page.

<a id="evidence-gs1-conformant-resolver"></a>**GS1-Conformant Resolver Standard 1.2.1.** Read: Standards page, PDF (text extracted) and archive page of the Resolver, in full, 2026-10-03; for dates also the URI Syntax standard page and archive. Not read: The www.gs1.org standards page.

<a id="evidence-un-gtr-urn"></a>**UN Global Trust Register, namespace urn:gtr.** Read: On 2026-10-13: the IANA URN namespaces registry XML (updated 2026-10-12): no value gtr and no occurrence of the token. Not read: Drafts under other names not excluded. Not found in the IANA XML, GRID site or Internet-Draft search, 2026-10-02: an operational register.

<a id="evidence-untp-identity-resolver"></a>**UN Transparency Protocol, Identity Resolver.** Read: On 2026-10-13: the versions page of untp.unece.org (0.7.0 still the only stable release listed; the GitLab tag list was not queried again). Not read: The response diagram of the Resolver Workflow (an image). Not found in the prose of either specification page, 2026-10-02: any mention of 404.

<a id="evidence-cen-clc-jtc24-dpp"></a>**CEN/CENELEC JTC 24 Digital Product Passport standards (EN 18216 to EN 18246).** Read: The CEN-CENELEC news page of 2026-07-15 (read 2026-10-02 and 2026-10-13) and the GS1 document on standards development organisations, read 2026-10-02. Not read: The standard texts (paid): whether EN 18219 refers to ISO/IEC 15459 or 18975, and the status of EN 18239 and EN 18246.

<a id="evidence-ieee-p3931-addr"></a>**IEEE P3931 Agent Description, Discovery, and Registry (ADDR) Interoperability.** Read: On 2026-10-13: the active PARs page (P3931 listed as Draft Development; the PAR text adds that identity frameworks, trust scoring systems, collaborative governance policies and domain-specific business semantics are beyond its scope). Not read: Working group membership and chair; whether the work references DAWN or Agentic Resource Discovery (ARD). Not found in the PAR scope text, 2026-10-02: commerce, merchant, product.

<a id="evidence-a2a-discovery"></a>**A2A protocol, agent discovery.** Read: On 2026-10-18: the AAIF announcement of 2026-08-17 (A2A is a hosted project of AAIF). Repository items read (updated 2026-01-01 to 2026-10-02): discovery threads in full, the rest by keyword search; docs/roadmap.md and agent-discovery.md on main, 2026-10-03. Not read: Technical Steering Committee (TSC) minutes and recordings, the diff of PR #2240, the Discord, long identity threads, replies on #2276 after 2026-10-02 (none found: the thread has three comments, the last of 2026-10-02). Not found: On 2026-10-13 (main at commit 7c861a5): the state, comment count and last update of PR #2240 and issues #2276 and #2248, the latest release (v1.0.1, 2026-05-28), docs/topics/agent-discovery.md (the quoted sentence present; AI Catalog not found in it) and the history of GOVERNANCE.md (last change 2026-08-25). Not found in roadmap.md: discovery.

<a id="evidence-aaif-wg-agentic-commerce"></a>**AAIF Agentic Commerce Working Group.** Read: On 2026-10-13: the repository file listing and commits to 2026-10-12, the charter targets, the August report (reporting/2026-08-report.md), issues #5 to #9, and the Running Notes document linked from the README (a Google Document shared by link): its last session heading is of 2026-07-22 and it does not mention a completed Capability Map. Not read: Discord, the meeting record cited in PR #7, per-session Google Documents, the fork of PR #6. Not found, 2026-10-13: Running Notes for a session after 2026-07-22; a Capability Map or Recommendations document. Not found in the product discovery notes, 2026-10-03: GS1, GTIN, schema.org.

<a id="evidence-aaif-identity-trust"></a>**AAIF Identity and Trust group, issue.** Read: On 2026-10-13: the state, comments, commits and reviews of issue #13, issue #287 and pull request #288, the Proofable comments of 2026-10-09, the frozen packet 9851059 (eight files, SHA256SUMS recomputed), and the Reference Architecture working draft in full. Not read: The mailing list archive pages (they require JavaScript, and its published rules ask for a licence for automated AI access; only six messages supplied by the author were used), the TRACE specification text under spec/, the source of any repository (no code was executed), the full Parmana repository. Not found, 2026-10-09: a merge of pull request #288 (also not found on 2026-10-13); a release object or release notes for the MintID tags.

<a id="evidence-aaif-structure"></a>**AAIF structure, Technical Committee and working groups.** Read: On 2026-10-18: aaif.io/projects (six hosted projects). On 2026-10-13: the file listing, the commits to 2026-10-12, the releases and the issue and pull request list of ws-taxonomy-landscape, the portal page at aaif.github.io/ws-taxonomy-landscape, and the README (last changed 2026-09-16, unchanged on the Landscape sentence). Not read: Discord, mailing lists, recordings, Google Documents. Not found in the proposals repositories, 2026-10-03: AI Catalog, Agentic Resource Discovery (ARD), DAWN, UCP, Verifiable Intent.

<a id="evidence-a2a-core"></a>**Agent2Agent (A2A) protocol, core specification.** Read: On 2026-10-18: the AAIF announcement of 2026-08-17, the A2A blog post of 2026-08-27, the AAIF projects page (A2A listed with MCP, goose, AGENTS.md, agentgateway and Agent Router) and the release list (latest still v1.0.1). On 2026-10-13: the release list (latest v1.0.1, 2026-05-28). On 2026-10-03: a2a.proto, docs/specification.md, GOVERNANCE.md, the release list. Not read: Technical Steering Committee (TSC) minutes and recordings, specification chapters beyond the definitions, the project's later announcements. Not found in the repository README on 2026-10-18: AAIF; the README still says "an open source project under the Linux Foundation, contributed by Google".

<a id="evidence-mcp-server-card"></a>**MCP Server Cards (ext-server-card, SEP-2127).** Read: On 2026-10-18: the AAIF projects page (MCP, whose GitHub organisation holds this extension, is an AAIF project). On 2026-10-13: PR #2127 with its labels and files, the SEP file seps/2127-mcp-server-cards.md, the README of the extension repository and the state of PR #47 and issues #13, #30, #43, #44, #48 and #50. ext-server-card: README, discovery.md, all issues and PRs in full; core repository since 2026-01-01: PR #2127, notes, Discussions #2831, #2896. Not read: Issue #1649 comments, Core Maintainer meetings, external links. Not found there (2026-10-03): GTIN, GS1.

<a id="evidence-mcp-core"></a>**Model Context Protocol (MCP), core specification.** Read: On 2026-10-18: the AAIF projects page, which lists Model Context Protocol among the projects AAIF hosts. On 2026-10-13: the list of releases and the specification directory of the repository; the blog post, the governance page and the versioning page were not re-read. Not read: Full text of each specification chapter, the Specification Enhancement Proposal (SEP) process pages, licence texts beyond README and GOVERNANCE.md. Not found on the governance and specification pages: foundation, AAIF, Linux.

<a id="evidence-lf-ai-catalog"></a>**AI Catalog (Agent Card Working Group).** Read: On 2026-10-13: the README and GOVERNANCE.md of main, the head of main, the list of ADR files, the state of PRs #91, #110, #117, #119 and issues #46, #59, #83, #86, #101, #114. Not read: The Google document linked in PR #77, recordings, the Discord, other ADR files, the password-protected meeting page. Not found in the items (2026-10-03): commerce, seller, GTIN.

<a id="evidence-dif-trusted-ai-agents"></a>**DIF Trusted AI Agents Working Group.** Read: On 2026-10-13: the working group page (the Delegated Authority and KYA-OS task forces listed, with a meeting schedule; the blog post was not read again). Not read: Overlaps are inferred from topic. Not found in the working group page, 2026-10-02: discovery, commerce, merchants, products, catalogs.

<a id="evidence-trace"></a>**TRACE (Trust, Runtime Attestation and Compliance Evidence).** Read: On 2026-10-13: the README of trace-spec (status paragraph), the repository metadata, the three latest commits, the release list and the file list of spec/, and the state, labels and description of aaif/project-proposals issue #42 (its comments were not read). Not read: The rest of the specification (980 lines), the schema, the conformance suite, the roadmap and governance files, the limitations file.

<a id="evidence-x402"></a>**x402.** Read: On 2026-10-13 (fetch of the repository, commit 6c470a8): TSC.md, README.md, the core specification header, specs/extensions/extension-offer-and-receipt.md (still "Wire shape and field placement are not considered stable"), docs/faq.md, and the state of PRs #1986, #3220, #3656, #3789 and issues #2887, #2906, #3500. x402-foundation/x402, 2026-10-03: main branch read (README, TSC.md, ROADMAP, specs, docs, Technical Charter), issues and pull requests updated since 2026-03-01, and the two Linux Foundation releases. Not read: Slack, the tsc and wg-identity repositories, x402.org member and calendar pages, older items; usage figures on x402.org (self-reported).

<a id="evidence-ard"></a>**Agentic Resource Discovery (ARD).** Read: On 2026-10-13: spec/ard.md on main (header and sections 5.1 and 3), the governance page, ADR 0010, the head of ard-spec and the state of its pull requests #74, #80, #97 to #106 and issues #20, #43, #61, #78, #79, #86, #88, #92, and the state of Lighthouse #17258 to #17261, #17294, #17295, #17297, #17160 and #17271. Not read: The Discord, Lighthouse files on main, ADR files other than ADR 0010 beyond titles, the comments of ard-spec issues and pull requests other than those named, ard-docs after 2026-09-13. Not found in both repositories: UCP, commerce, merchant, GTIN, Know Your Agent (KYA) (2026-10-03, not repeated). Not found in ard-spec: a tag or release (2026-10-03 and again 2026-10-13).

<a id="evidence-browsers-webmcp"></a>**Browser vendor positions on WebMCP (WebKit, Mozilla, Chrome, Edge).** Read: On 2026-10-13: the Chrome and Edge pages and the issues of WebKit and Mozilla, whose quoted sentences (the Chrome description, the Edge sentence "is ready for testing", and the WebKit and Mozilla statements) were found again in the current texts; the state and labels of both issues (closed 2026-06-11 "position: oppose" and closed 2026-08-05 "position: neutral", unchanged). Not read: Safari or Apple pages outside the issue, Chrome Status, other Mozilla pages, other vendors, implementation documentation.

<a id="evidence-emilia-protocol"></a>**EMILIA Protocol (individual drafts and open-source gate).** Read: The texts of the architecture draft -03 and the boundary draft -07, the README and the repository metadata, and the comments of AAIF issue #13, read 2026-10-08. Not read: The CAID and EP-AEC drafts, the other drafts of the same author, the code of the repository beyond the README. Not found, 2026-10-08: EMILIA in the comments of AAIF issue #13 (7 comments).

<a id="evidence-oidf-authzen-agents"></a>**OpenID Foundation AuthZEN Working Group (agent authorization drafts AARP and COAZ).** Read: The announcement of the drafts (read 2026-10-02 and again 2026-10-13, "Published June 15, 2026") and the working groups page (2026-10-02); the arXiv version and the OpenID whitepaper page, 2026-10-06. Not read: Authorization API 1.0 Final approval seen only in a search result. Not found in the announcement, 2026-10-02: commerce, merchant, product. Counts in the text of the arXiv version, 2026-10-06: Web Bot Auth 8 times (one a reference, one an IETF proposal described as a "passport for agents"), Agent Payments Protocol (AP2) 3, commerce 2 and AuthZEN 1; not found, 2026-10-06: UCP, ACP, x402, TAP.

<a id="evidence-schemaorg-open-agent-commerce-items"></a>**schema.org open issues relevant to agents, bookings, product and establishment identity.** Read: On 2026-10-14: the release notes of V30.1 (the terms attributed to PR #4871). Not read: The well-known files named in #4824; whether the terms of PR #4871 are in release 30.1 (pending on 2026-10-03). Not found in the repository read: a maintainer release date for the five issues.

<a id="evidence-schemaorg-baseline"></a>**schema.org vocabulary for products, offers, sellers and lodging (current release).** Read: On 2026-10-13: schema.org/docs/releases.html (30.1 dated 2026-09-16, 30.0 dated 2026-03-19, nothing later) and the GitHub release list (v30.1 published 2026-09-15 and v30.0 published 2026-03-25, a different instrument from the page; no release after v30.1; last commit on main 2026-10-01). Not read: Properties, expected types and examples on each term page, and the other terms of the vocabulary.

<a id="evidence-ap2"></a>**Agent Payments Protocol (AP2).** Read: On 2026-10-18: the Google blog post of 2026-04-28 ("Google donates Agent Payments Protocol to FIDO Alliance"), the FIDO release of 2026-04-28 and docs/index.md on main. On 2026-10-13: the release list (latest v0.2.0, 2026-04-28), the head of main (commit e1ea56d, 2026-04-29, unchanged since the reading of 2026-10-05), docs/index.md, docs/ap2/agent_authorization.md, checkout_receipt.json and receipt_status.json at that commit, and issue #374,. Also on 2026-10-13, at the same commit: docs/ap2/specification.md (section Checkout Mandate, which holds the sentence "Once the Merchant has accepted or rejected the Checkout Mandate, it MUST return a Checkout Receipt."), flows.md (receipt passages), the Checkout Receipt section of checkout_mandate.md (which holds the schema fields), and a search of the seven documents of docs/ap2 for the words refund, cancel and fulfil(l), recounted on 2026-10-14. google-agentic-commerce/AP2, 2026-10-03: metadata, releases v0.2.0 and v0.1.0, README, CONTRIBUTING.md, docs/index.md, docs/faq.md; FIDO release of 2026-04-28 and blog of 2026-05-26, in full; at commit e1ea56d on 2026-10-05: docs/ap2/specification.md, docs/ap2/agent_authorization.md and code/sdk/schemas/ap2/checkout_receipt.json. Not read: The mandate pages checkout_mandate.md and payment_mandate.md beyond the receipt sections, other code, commits, issues, FIDO working group charters. Not found in the seven documents of docs/ap2 at commit e1ea56d (agent_authorization, checkout_mandate, flows, implementation_considerations, payment_mandate, security_and_privacy_considerations, specification), 2026-10-14: refund and cancel (0 occurrences each).

<a id="evidence-acp"></a>**Agentic Commerce Protocol (ACP).** Read: On 2026-10-13: the head of main and the README and MAINTAINERS.md of a fresh fetch of the repository (commit 7fdd78d), the tag and release lists, spec/unreleased, and the state of issues #231 and #303 and Discussions #265 and #304. Not read: Discord, TSC meetings, GitHub organisation membership. Not found in the repository, 2026-10-03: tag, release, Web Bot Auth, KYA, Verifiable Intent.

<a id="evidence-emvco-agentic-payments-framework"></a>**EMV Agentic Payments Framework for Specifications (draft for public feedback).** Read: On 2026-10-13, as HTML: the news list (71 results, newest the newsletter of 2026-10-09), the newsletter Q3 2026 and the resource page of the draft (title and page text only). Not read: The draft document itself; matrix cells rest on the press release and the Insights article.

<a id="evidence-fido-agentic-standards"></a>**FIDO Alliance agentic authentication and payments work.** Read: Google blog post of 2026-04-28 announcing the donation of AP2 to FIDO, 2026-10-18. FIDO release of 2026-04-28 in full, read again in a browser on 2026-10-14 (page metadata: published and modified 2026-04-28); blog of 2026-05-26 in full, 2026-10-03, not read again; AP2 CONTRIBUTING.md and docs/index.md, 2026-10-03. Not read: Working group charters, membership, specification text. Not found in pages read, 2026-10-03: AAIF coordination; Visa TAP among contributions.

<a id="evidence-kyapay"></a>**KYAPay (Skyfire).** Read: Datatracker search for draft-skyfire and the pages of kyapay-token and using-kyapay-tokens, 2026-10-13 (seven documents: kyapay-token-02, using-kyapay-tokens-01, amr-values-02, id-verification-02, aml-methods-01, kyapay-token-exchange-01, kyapayprofile-02); datatracker listing of 2026-10-02 (it named four, kyapay-token-02, token-exchange-01, using-kyapay-tokens-01, kyapayprofile-02); the announcement of 2026-10-02 on the oauth list names five; oauth list from 2026-08-01, subject filter (142 of 505 messages), KYAPay threads read. Not read: The pages of the other five drafts on the datatracker (stream and state), skyfire-xyz repositories; IETF 126 session; kyapay.org beyond main page; adopters named in the announcement; threads excluded by the subject filter. Not found in the messages read, 2026-10-03: the merchant's own identity, product identity, prices, checkout.

<a id="evidence-mastercard-agent-pay"></a>**Mastercard Agent Pay.** Read: Framework page in full, read in a browser on 2026-10-14 (title "Agentic token framework: Driving trusted AI transactions | Mastercard Europe"; first read 2026-10-02); FIDO release of 2026-04-28 (2026-10-03); Verifiable Intent README (2026-10-02). Not read: Three Mastercard pages of 2026 (Agent Pay for Machines, trust and intelligence services, Verifiable Intent).

<a id="evidence-pact"></a>**Personal Agent Consent & Trust Protocol (PACT), published by Decagon with Instinct.** Read: On 2026-10-13: the specification page and the home page of openpactprotocol.org, the repository metadata (default branch, licence, creation date, latest commit), the LICENSE file header and the README of the repository, and the Decagon announcement of 2026-10-06. Not read: The pages "Build a personal agent integration", "Build a Provider" and "Run the reference stack", the reference code and the conformance tests, the Instinct side of the announcement, any publication of a standards body on PACT. Not found, 2026-10-13: a standards body, foundation or working group in the pages of the site read; consumer, durable medium, confirm, poppy.json and Web Bot Auth in the specification page.

<a id="evidence-pap"></a>**Personal Agent Protocol (PAP, "Poppy"), published by Sierra with Meta.** Read: On 2026-10-13: the specification, the operations extension, the extensions page, the Path to 1.0 page, the home page and the licence page of personalagentprotocol.org (each marked "Updated Oct 12, 2026" where the page carries a date), the Sierra blog of 2026-10-09, the Decagon blog of 2026-10-06 and the IANA well-known URI registry XML. On 2026-10-08: the Sierra announcement of 2026-10-06 in full, one trade article on it and one on the Shopify and Meta agreement. Not read: The sections of the specification beyond the discovery, agent identity and confirmation texts quoted, the PACT specification, any Meta publication on the protocol, the TechRepublic article on Meta's Muse (not retrievable on 2026-10-08). Not found, 2026-10-13: poppy.json in the IANA well-known URI registry XML; a standards body, foundation or working group in the pages of the site read (home, specification, extensions, operations, Path to 1.0, licence); UCP, A2A and Web Bot Auth in the same pages.

<a id="evidence-shopify"></a>**Shopify, MCP surfaces for buyer agents, developers and merchants.** Read: Toolkit releases v2.0.0 to v2.1.1 and the two plugin files, shopify.dev pages on Checkout WebMCP, the developer changelog of 2026-09-28 and the MCP developer page, npm registry metadata, issue #62, read 2026-10-08; on 2026-10-13: the list of toolkit releases (latest v2.1.1, 2026-10-08), the CHANGELOG and the folder skills/ucp at the tag v2.1.1, the npm registry entries of @shopify/dev-mcp (1.16.0) and @shopify/shopify-dev-tools (E404), and issue #62 (open, no comments). Not read: The shopify.dev pages on Checkout WebMCP, the developer changelog of 2026-09-28 and the MCP developer page were not re-read on 2026-10-13 (last read 2026-10-08). help.shopify.com, any merchant-facing page on shopify.com, the telemetry code of the toolkit, the X post of the Shopify product manager on Checkout WebMCP; the compiled binary lib/shop.wasm and the .mjs files of Shop CLI, the server mcp.shop.com (no call made), the plugin files of Shop CLI. Not found, 2026-10-08: setup.shopify.com in the shopify.dev pages read (the MCP developer page and the changelog index); a page of Shopify describing the merchant MCP. Not found in the README, SKILL.md and transactions.md of Shopify/shop at d1e8c7c (2026-10-13): beta, preview, experimental, a list of supported countries, and a confirmation sent to the shopper on a durable medium.

<a id="evidence-ucp"></a>**Universal Commerce Protocol (UCP).** Read: On 2026-10-14 also: Discussion #867 up to the comment of 2026-10-14 (03:00 UTC, comment 18913822). Not read: Draft feed specification of PR #866, DWG and Tech Council minutes (private), external links, items before 2026-01-01; the schema and the 17 examples of PR #930, the nomination form of #924, the other pages of the DAP site. Not found in overview page or the repository read: Agentic Resource Discovery (ARD).

<a id="evidence-verifiable-intent"></a>**Verifiable Intent.** Read: On 2026-10-13: the head, tags and releases of the repository, the README status line, and the state of PR #40 (open, no comment since 2026-09-28) and issues #9, #10, #22 and #41. agent-intent/verifiable-intent: README, specification, landscape pages (2026-10-02); all 40 issues and pull requests with comments (2026-10-03; #10, #9 and #22 partly read); FIDO release. Not read: Mastercard announcement of 2026-03-05. Not found in the 40 items read, 2026-10-03: standards-body submission, EMVCo.

<a id="evidence-visa-tap"></a>**Visa Trusted Agent Protocol (TAP).** Read: developer.visa.com (product page, merchant specifications, product terms), read in a browser on 2026-10-14 from saved copies; docs index and sample code repository (log, tree, README), 2026-10-03; terms grant a "nontransferable, revocable, limited license". Not read: Code, Client Implementation Guide (not public), other Visa documents. Not found: Standards-body submission: not found in Visa pages, repository 2026-10-03.

---

<a id="part-proposals"></a>
# Part 11: Appendix: Open proposals

| Entry | Proposal | Author | Date | State | Link |
|---|---|---|---|---|---|
| [WebMCP (Draft Community Group Report, Web Machine Learning CG)](#w3c-webmcp-cg-report) | Proposes to "Stand up a new community group for agent-assisted user agents (name to be decided)." | a participant (WebKit standards-positions) | 2026-06-17 | closed | https://github.com/WebKit/standards-positions/issues/670#issuecomment-4729132384 |
| [IETF AI Preferences (aipref WG)](#ietf-aipref) | Add a category for embeddings, indexes and cached copies (ai-embed). | Tyler Martin | 2026-08-26 | open | https://mailarchive.ietf.org/arch/msg/ai-control/p9kpjIxFOia7MTYnQnDVrIZH8aw |
| [IETF AUDIT (BoF preparation)](#ietf-audit) | Charter text: data models for interaction records, identities, delegation context; reuse VCON. | Jonathan Rosenberg | 2026-10-02 | open | https://github.com/mirjak/audit-bof-preparation/pull/61 |
| [IETF DAWN, Discovery of Agents With Names (proposed WG)](#ietf-dawn) | First work item: an organisation's agent index, catalogue or registry. Against charter 00-10 (read 2026-10-13): the charter lists "a service such as a catalog that will further the discovery process" as a discoverable AI resource and excludes catalogs of capabilities and "AI resource indexing and searching across the wider Internet"; the proposal is not among its work items. | Jim Mozley | 2026-08-05 | open | https://mailarchive.ietf.org/arch/msg/dawn/fsJ8oAdR8rpNPhCj6LP9sspbxBA |
| [IETF agentproto (Agent Communication Protocols WG)](#ietf-agentproto) | Charter PR #128: distinguish user from service agents; privacy analysis not to assume symmetry (closed without a merge on 2026-10-08). | Mallory Knodel | 2026-10-02 | closed | https://github.com/ietf-artarea/charters/pull/128 |
| [IETF agentproto (Agent Communication Protocols WG)](#ietf-agentproto) | List-proposed charter text: use cases document as informational RFC or working group input (not found in charter 01 as approved, datatracker page, 2026-10-09). | the responsible Area Director (proposal quoted in a message by a participant) | 2026-09-11 | closed | https://mailarchive.ietf.org/arch/msg/agentproto/myfwr_eF4abrR6Ayfff7cAYI0X0 |
| [IETF vcon (Virtualized Conversations WG)](#ietf-vcon) | Recharter: finish the core specification, then an extension for AI agent interaction record data (message and pull request #37, merged on 2026-10-08 into the charter file of the repository; the interim of 2026-10-08 discussed it, a chair's reminder of 2026-10-06 listing "discuss proposed charter updates"). | Jonathan Rosenberg | 2026-10-06 | merged | https://github.com/ietf-wg-vcon/draft-ietf-vcon-vcon-core/pull/37 |
| [IETF vcon (Virtualized Conversations WG)](#ietf-vcon) | Restructure the format with a session concept and an events object to represent AI agent use cases (draft-rosenberg-vcon-restructure-00; on 2026-10-13 the datatracker still shows -00 as the current revision, last updated 2026-09-11; the editors copy of the core draft of 2026-10-07 reports the elevation of party_history events to a top level Events Object and a Session concept, which are parts of this proposal). | Jonathan Rosenberg | 2026-09-11 | open | https://mailarchive.ietf.org/arch/msg/vcon/pSs7uBFPNQI5ZWd0h3zM60F5E0Q/ |
| [A2A protocol, agent discovery](#a2a-discovery) | PR #2240: /.well-known/ai-catalog.json as the Preferred discovery mechanism (base dev-1.1). | a participant | 2026-09-16 | open | https://github.com/a2aproject/A2A/pull/2240 |
| [A2A protocol, agent discovery](#a2a-discovery) | Issue #2276: /.well-known/agent-card-list.json, an array of AgentCards. | a participant | 2026-10-01 | open | https://github.com/a2aproject/A2A/issues/2276 |
| [A2A protocol, agent discovery](#a2a-discovery) | Issue #2248: standard multi-agent aggregation path and a ListAgents remote procedure call (RPC). | a participant | 2026-09-20 | open | https://github.com/a2aproject/A2A/issues/2248 |
| [AAIF Agentic Commerce Working Group](#aaif-wg-agentic-commerce) | Capability Map input on cross-boundary evidence and audit, and post-purchase rows P1 to P7 | a participant | 2026-08-26 | open | https://github.com/aaif/wg-agentic-commerce/issues/5 |
| [AAIF Agentic Commerce Working Group](#aaif-wg-agentic-commerce) | Capability map to add a buyer-capacity attribute and a table of records kept per party | a participant | 2026-09-24 | open | https://github.com/aaif/wg-agentic-commerce/issues/8 |
| [MCP Server Cards (ext-server-card, SEP-2127)](#mcp-server-card) | Issue #27 and Discussion #2831: payment and value metadata in the Server Card (_meta riders). | a participant | 2026-06-09 | closed | https://github.com/modelcontextprotocol/ext-server-card/issues/27 |
| [MCP Server Cards (ext-server-card, SEP-2127)](#mcp-server-card) | Discussion #2896: a commerce discovery extension for the Server Card in _meta. | a participant | 2026-06-09 | closed | https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/2896 |
| [MCP Server Cards (ext-server-card, SEP-2127)](#mcp-server-card) | Issue #3393: payment metadata in the server card or in the response of a call. | a participant | 2026-09-26 | closed | https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3393 |
| [MCP Server Cards (ext-server-card, SEP-2127)](#mcp-server-card) | Issue #30: optional tool metadata in the Server Card for offline discovery. | a participant | 2026-06-17 | open | https://github.com/modelcontextprotocol/ext-server-card/issues/30 |
| [MCP Server Cards (ext-server-card, SEP-2127)](#mcp-server-card) | Schema and discovery issues #48, #50, #43, #44 (capabilities, instructions, links, nested catalogs). | a participant | 2026-08-24 | open | https://github.com/modelcontextprotocol/ext-server-card/issues/48 |
| [AI Catalog (Agent Card Working Group)](#lf-ai-catalog) | Issue #46: move the project under the Agentic AI Foundation (closed as completed on 2026-10-03 without a comment; the README still announces a move to a permanent location). | a participant | 2026-06-19 | closed | https://github.com/Agent-Card/ai-catalog/issues/46 |
| [AI Catalog (Agent Card Working Group)](#lf-ai-catalog) | Issue #59: prefix air-type before the publisher in the urn:air schema. | a participant | 2026-07-01 | open | https://github.com/Agent-Card/ai-catalog/issues/59 |
| [AI Catalog (Agent Card Working Group)](#lf-ai-catalog) | Issue #83: discovery-time access and monetization signalling (accessModel, x402). | a participant | 2026-07-16 | open | https://github.com/Agent-Card/ai-catalog/issues/83 |
| [AI Catalog (Agent Card Working Group)](#lf-ai-catalog) | Issue #86: federation governance metadata, machine-readable alternative to terms URLs. | a participant | 2026-07-17 | open | https://github.com/Agent-Card/ai-catalog/issues/86 |
| [AI Catalog (Agent Card Working Group)](#lf-ai-catalog) | Issue #101: a catalog and registry observe and never grant authority. | a participant | 2026-08-20 | open | https://github.com/Agent-Card/ai-catalog/issues/101 |
| [AI Catalog (Agent Card Working Group)](#lf-ai-catalog) | PR #91: ADR-0021, multiple identities via alsoKnownAs (open, 11 comments; on main the number ADR-0021 is already used by "Separate Artifact Identity from Registry Coordinates", status Proposed, 2026-08-26). | a participant | 2026-07-24 | open | https://github.com/Agent-Card/ai-catalog/pull/91 |
| [AI Catalog (Agent Card Working Group)](#lf-ai-catalog) | Issue #114: measurement of did:web host identifiers. | a participant | 2026-09-13 | open | https://github.com/Agent-Card/ai-catalog/issues/114 |
| [AI Catalog (Agent Card Working Group)](#lf-ai-catalog) | PR #117: trust metadata grouped by contributor, generalized signatures (not a draft on 2026-10-13; open, 6 comments). | a participant | 2026-09-13 | open | https://github.com/Agent-Card/ai-catalog/pull/117 |
| [x402](#x402) | Terms extension specification | a participant | 2026-04-10 | open | https://github.com/x402-foundation/x402/pull/1986 |
| [x402](#x402) | Authority extension: bounded, offline-verifiable spending mandates | a participant | 2026-08-20 | open | https://github.com/x402-foundation/x402/pull/3220 |
| [x402](#x402) | Offer-receipt additions: action-receipt, v2 bindings, delivery proof, conformance (#2906 and others) | a participant | 2026-07-19 | open | https://github.com/x402-foundation/x402/issues/2906 |
| [x402](#x402) | Dispute evidence layer: working-group request (#2887), feature (#3500) | a participant | 2026-07-17 | open | https://github.com/x402-foundation/x402/issues/2887 |
| [x402](#x402) | Reviews extension: links to payment-backed reviews in 402 and settlement responses | a participant | 2026-10-02 | open | https://github.com/x402-foundation/x402/pull/3656 |
| [Agentic Resource Discovery (ARD)](#ard) | Issue #88: field data on ai-catalog.json and ard.json; asks for a fallback to the predecessor path. | a participant | 2026-08-31 | open | https://github.com/ards-project/ard-spec/issues/88 |
| [Agentic Resource Discovery (ARD)](#ard) | Issue #20: access and monetization signalling in ARD entries. | a participant | 2026-06-19 | open | https://github.com/ards-project/ard-spec/issues/20 |
| [Agentic Resource Discovery (ARD)](#ard) | Issue #78: discovery confers no contact authority. | a participant | 2026-08-20 | open | https://github.com/ards-project/ard-spec/issues/78 |
| [Agentic Resource Discovery (ARD)](#ard) | Issue #43: application/install-manifest+json in the AI Catalog (closed as completed on 2026-10-11: ARD v0.91 accepts any valid RFC 6838 media type in `type`). | a participant | 2026-06-23 | closed | https://github.com/ards-project/ard-spec/issues/43 |
| [schema.org open issues relevant to agents, bookings, product and establishment identity](#schemaorg-open-agent-commerce-items) | Issue #4824: BookingChannel for LodgingBusiness, pointing to a well-known manifest. | a participant | 2026-05-23 | open | https://github.com/schemaorg/schemaorg/issues/4824 |
| [schema.org open issues relevant to agents, bookings, product and establishment identity](#schemaorg-open-agent-commerce-items) | Issue #4786: WebPageSemanticRepresentation type for AI agent consumption. | a participant | 2026-03-25 | open | https://github.com/schemaorg/schemaorg/issues/4786 |
| [schema.org open issues relevant to agents, bookings, product and establishment identity](#schemaorg-open-agent-commerce-items) | Issue #4828: SoftwareAgent type (possible subtype of SoftwareApplication). | a participant | 2026-05-25 | open | https://github.com/schemaorg/schemaorg/issues/4828 |
| [schema.org open issues relevant to agents, bookings, product and establishment identity](#schemaorg-open-agent-commerce-items) | Issue #4774: PaymentMethod collections or profiles via @id for acceptedPaymentMethod on Offer. | a participant | 2026-02-27 | open | https://github.com/schemaorg/schemaorg/issues/4774 |
| [schema.org open issues relevant to agents, bookings, product and establishment identity](#schemaorg-open-agent-commerce-items) | Issue #4928: public registration number of establishments (hasCertification or identifier). | the author of this map | 2026-09-26 | open | https://github.com/schemaorg/schemaorg/issues/4928 |
| [schema.org open issues relevant to agents, bookings, product and establishment identity](#schemaorg-open-agent-commerce-items) | Issues #4572 and #4615: cart object and structured payloads for cart and checkout actions. | a participant | 2025-11-10 | open | https://github.com/schemaorg/schemaorg/issues/4572 |
| [schema.org open issues relevant to agents, bookings, product and establishment identity](#schemaorg-open-agent-commerce-items) | Issue #4525: economic operator attribute on Product. | a participant | 2025-10-09 | open | https://github.com/schemaorg/schemaorg/issues/4525 |
| [schema.org open issues relevant to agents, bookings, product and establishment identity](#schemaorg-open-agent-commerce-items) | Discussion #4699: buyer-owned checkout from Demand, Offer and Order. | a participant | 2026-01-24 | open | https://github.com/schemaorg/schemaorg/discussions/4699 |
| [Agent Payments Protocol (AP2)](#ap2) | Issue #374: the Mandate Receipt is described with a `result` field of `["success", "error"]` (docs/ap2/agent_authorization.md, lines 503 to 516) and with a `status` field of `Success` or `Error` (code/sdk/schemas/ap2/checkout_receipt.json and types/receipt_status.json), both read at commit e1ea56d; no comment on the issue on 2026-10-13. | a participant | 2026-10-11 | open | https://github.com/google-agentic-commerce/AP2/issues/374 |
| [Agentic Commerce Protocol (ACP)](#acp) | Governance-layer binding for ACP: authorization, limits, attribution (discussion) | a participant | 2026-04-23 | open | https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/issues/231 |
| [Agentic Commerce Protocol (ACP)](#acp) | Final commit-time authorization evidence in checkout and payment flows (discussion) | a participant | 2026-06-06 | open | https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/discussions/265 |
| [Agentic Commerce Protocol (ACP)](#acp) | SEP for a dispute resolution extension (ATDRP) and the sponsor request for it (#303, #304) | a participant | 2026-09-09 | open | https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/issues/303 |
| [KYAPay (Skyfire)](#kyapay) | TPAC 2026 breakout on KYAPay (agentic commerce on the existing web); no slot assigned yet. | Michael B. Jones and a co-author | 2026-10-01 | open | https://github.com/w3c/tpac2026-breakouts/issues/39 |
| [Universal Commerce Protocol (UCP)](#ucp) | Issue #929 and draft PR #930: dev.ucp.common.quote, a time-bound quotation accepted by id on Cart and Checkout, projected onto the Order as id and subtotal. | a participant | 2026-10-11 | open | https://github.com/Universal-Commerce-Protocol/ucp/issues/929 |
| [Universal Commerce Protocol (UCP)](#ucp) | PR #933: state that a 304 Not Modified is not a forbidden redirect on profile hosting and fetching (301, 302, 303, 307 and 308 are the banned codes). | a participant | 2026-10-11 | open | https://github.com/Universal-Commerce-Protocol/ucp/pull/933 |
| [Universal Commerce Protocol (UCP)](#ucp) | Food domain: dev.ucp.food.checkout and food.fulfillment, for early feedback. | a participant | 2026-10-03 | open | https://github.com/Universal-Commerce-Protocol/ucp/pull/897 |
| [Universal Commerce Protocol (UCP)](#ucp) | Attestation-based platform client authentication for first-contact accelerated IdP chaining. | a participant | 2026-09-22 | open | https://github.com/Universal-Commerce-Protocol/ucp/issues/852 |
| [Universal Commerce Protocol (UCP)](#ucp) | Issue #515 (MerchantStamp): one signed-receipt envelope verified through a single path. | a participant | 2026-06-15 | open | https://github.com/Universal-Commerce-Protocol/ucp/issues/515 |
| [Universal Commerce Protocol (UCP)](#ucp) | Issue #629: business persists the checkout billing_summary as the record of authorized terms. | a participant | 2026-07-23 | open | https://github.com/Universal-Commerce-Protocol/ucp/issues/629 |
| [Universal Commerce Protocol (UCP)](#ucp) | PR #890: subscription policy extension; the Order snapshot as dispute record. | a participant | 2026-10-02 | draft | https://github.com/Universal-Commerce-Protocol/ucp/pull/890 |
| [Universal Commerce Protocol (UCP)](#ucp) | Discussion #895: merchant decisions as signed, portable evidence. | a participant | 2026-10-03 | open | https://github.com/Universal-Commerce-Protocol/ucp/discussions/895 |
| [Universal Commerce Protocol (UCP)](#ucp) | Issue #896: contingencies, buyer-approved handling of surprises after an order. | a participant | 2026-10-03 | open | https://github.com/Universal-Commerce-Protocol/ucp/issues/896 |
| [Universal Commerce Protocol (UCP)](#ucp) | RFC #550 comment: links[] and policies[] on the feed list and manifest, with a usage-policy rule. | a participant | 2026-09-30 | open | https://github.com/Universal-Commerce-Protocol/ucp/issues/550#issuecomment-5914588559 |
| [Universal Commerce Protocol (UCP)](#ucp) | Discussion #563: an approval gate for unattended buying agents, when no human is at the surface. | a participant | 2026-07-05 | open | https://github.com/Universal-Commerce-Protocol/ucp/discussions/563 |
| [Universal Commerce Protocol (UCP)](#ucp) | PR #691: price_treatment on the price type; an absent price_treatment equals an absent tax. | a participant | 2026-09-21 | open | https://github.com/Universal-Commerce-Protocol/ucp/pull/691 |
| [Universal Commerce Protocol (UCP)](#ucp) | Discussion #864: a restrictions object on the stay (minimum and maximum nights, closed to arrival, closed to departure) and an error code stay_restriction_violated. | a participant | 2026-10-08 | open | https://github.com/Universal-Commerce-Protocol/ucp/discussions/864#discussioncomment-18816854 |
| [Universal Commerce Protocol (UCP)](#ucp) | PR #811: optional offers[] on the catalog variant, each offer naming the seller by seller.domain as Merchant of Record, with the seller's own item_id and price. | a participant | 2026-09-07 | open | https://github.com/Universal-Commerce-Protocol/ucp/pull/811 |
| [Verifiable Intent](#verifiable-intent) | Issue #41: question whether the cumulative budget is meant to be tracked per merchant, since the L3a sd_hash includes the merchant disclosure (no comment on 2026-10-13). | a participant | 2026-10-03 | open | https://github.com/agent-intent/verifiable-intent/issues/41 |
| [Verifiable Intent](#verifiable-intent) | Environment-state constraint types for autonomous execution (PRs #9, #11, #22, #32, issue #28) | a participant | 2026-03-17 | open | https://github.com/agent-intent/verifiable-intent/pull/9 |
| [Verifiable Intent](#verifiable-intent) | agent_attestation scheme, an SD-JWT agent passport | a participant | 2026-09-21 | open | https://github.com/agent-intent/verifiable-intent/issues/36 |
| [Verifiable Intent](#verifiable-intent) | VI implementation for an EUDI wallet | a participant | 2026-03-31 | open | https://github.com/agent-intent/verifiable-intent/issues/19 |
| [Verifiable Intent](#verifiable-intent) | Questions on intent standing after authority change (#35) and on purchase-request matching (#37) | a participant | 2026-09-18 | open | https://github.com/agent-intent/verifiable-intent/issues/35 |
| [Verifiable Intent](#verifiable-intent) | Fix for prompt_summary accepted by the SDK but never written to L2 (issue #39, PR #40) | a participant | 2026-09-28 | open | https://github.com/agent-intent/verifiable-intent/issues/39 |

---

<a id="part-disclosure"></a>
# Part 12: Appendix: Full disclosure

The author has contributed publicly to several of the venues mapped here; those contributions are listed below so readers can weigh them.

Read on 2026-10-13 with GitHub search (issues, pull requests and Discussions authored or commented on by the account `frmoretto`, all dates), a comment-by-comment comparison of that account's comments in the repositories of the venues in this map against this table, and the public archives of the IETF lists DAWN, AUDIT, vcon and web-bot-auth (the latest 40 messages of each) and dns-underscore-keys (3 messages). The working group list of the AAIF Agentic Commerce Working Group (groups.io) shows its messages only with JavaScript or a login, so the entry for it below was not read on the list; it is taken from the message as sent. Not searched: Discord, LFX and lists that are not public. Times are UTC unless stated. The list covers the venues in this map and may be incomplete: contributions that those searches do not return, and other archives, were not searched.

| Date | Venue (entry) | Contribution | What it says |
|---|---|---|---|
| 2026-06-25 | W3C/GS1 workshop (`w3c-gs1-ecommerce-workshop`) | [Issue #14](https://github.com/w3c/ecommerce-for-humans-and-AI-Agents-workshop/issues/14) | Position statement "Toward a Shared Convention for the Publisher-Side Agent Surface". |
| 2026-07-24 | W3C/GS1 workshop (`w3c-gs1-ecommerce-workshop`) | [PR #51](https://github.com/w3c/ecommerce-for-humans-and-AI-Agents-workshop/pull/51), merged | Updates broken links to position statements in agenda.html. |
| 2026-09-08 | W3C/GS1 workshop (`w3c-gs1-ecommerce-workshop`) | [PR #73](https://github.com/w3c/ecommerce-for-humans-and-AI-Agents-workshop/pull/73), merged | Adds the slides for the 8 September 12:50 session. |
| 2026-09-22 | Lighthouse ARD audit (`ard`) | [Issue #17251](https://github.com/GoogleChrome/lighthouse/issues/17251) | Reports that the `ard-schema` audit follows ARD as of June 2026, not v0.91: the discovery path it looks for and the schema it validates against. Closed as completed on 2026-10-09 (17:57 UTC), after PR #17258, which references it, was merged. |
| 2026-09-25 | ARD (`ard`) | [PR #100](https://github.com/ards-project/ard-spec/pull/100), merged on 2026-10-11 (19:35 UTC) | Removes a reference to ADR-0003 from the conformance warning about a root `collections` property. |
| 2026-09-25 | IETF DAWN list (`ietf-dawn`) | [Message](https://mailarchive.ietf.org/arch/msg/dawn/s_ePnn_yff9nCiNOHpJ8TYCrFBU/) in the thread "DAWN Coordination: Discovery Information and Trust Artifact Pointers" | Points out that "usability" is a condition for indirect discovery references without a matching requirement, and proposes defining it or replacing it with two verifiable requirements. |
| 2026-09-26 | schema.org (`schemaorg-open-agent-commerce-items`) | [Issue #4928](https://github.com/schemaorg/schemaorg/issues/4928), open | Proposes documenting public registration numbers for accommodations. |
| 2026-09-26 | UCP (`ucp`) | [Comment on #858](https://github.com/Universal-Commerce-Protocol/ucp/issues/858#issuecomment-5845163207) | On the accommodation type taxonomy: cites EU Regulation 2024/1028 and the Italian national identifier, and asks that the property type vocabulary keep hotels, short-term rentals and camping distinguishable. |
| 2026-09-26 | IETF Web Bot Auth, crawler best practices (`ietf-webbotauth`) | [PR #22](https://github.com/garyillyes/cbcp/pull/22), open on 2026-10-13, and [comment on #19](https://github.com/garyillyes/cbcp/issues/19#issuecomment-5845779106) | Proposes text on HTTP 429 in back-out logic and in robots.txt fetches. |
| 2026-09-26, 08:30 | UCP (`ucp`) | [Discussion #867](https://github.com/Universal-Commerce-Protocol/ucp/discussions/867), opened | Compares published measurements of the UCP surface and proposes a common reporting frame. |
| 2026-09-26, 09:29 | UCP (`ucp`) | [Comment on Discussion #864](https://github.com/Universal-Commerce-Protocol/ucp/discussions/864#discussioncomment-18610525) | On the lodging draft: asks how an agent can tell that two offers are the same physical property. |
| 2026-09-26, 10:34 | Shopify AI Toolkit (`shopify`) | [Issue #62](https://github.com/Shopify/Shopify-AI-Toolkit/issues/62), open, no comments on 2026-10-08 | Asks for release notes and a source link for @shopify/dev-mcp, and two questions on telemetry. The author also keeps the public repository https://github.com/frmoretto/shopify-dev-mcp-changelog (release notes for @shopify/dev-mcp). |
| 2026-09-27 | UCP (`ucp`) | [Comment on #866](https://github.com/Universal-Commerce-Protocol/ucp/pull/866#issuecomment-5855173866) | Raises two gaps in the feed draft: terms of use for the feed itself, and an optional record count per file. |
| 2026-09-27/28 | UCP (`ucp`) | Four comments on Discussion #867 ([1](https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18621614), [2](https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18624454), [3](https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18642324), [4](https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18642515)) | Two drafts of the reporting frame and replies to review, including splitting "could not ask" by side. |
| 2026-09-28 | IETF AUDIT (`ietf-audit`) | [Issue #35](https://github.com/mirjak/draft-audit-architecture/issues/35), open | Asks the architecture draft to state the coverage boundary of Service-side corroboration. |
| 2026-09-28, 04:20 | IETF AUDIT list (`ietf-audit`) | [Message](https://mailarchive.ietf.org/arch/msg/audit/k7hOFPmncnLwEWYfL9B2gDabqtw/) in the thread "Records for declined actions" | Relates a participant's point about a declared coverage boundary to Section 8 of the architecture draft -01, and announces issue #35. |
| 2026-09-29, 07:14 | IETF DAWN list (`ietf-dawn`) | [Message](https://mailarchive.ietf.org/arch/msg/dawn/r6M7_ZH2A_6RGt3sIpTyu14Tgt4/) in the same thread | Proposes limits on indirection depth and defined failure behaviour, and keeping the minimum verification material directly available. |
| 2026-10-01 | UCP (`ucp`) | [Comment on #550](https://github.com/Universal-Commerce-Protocol/ucp/issues/550#issuecomment-5929875271) | Supports making the declared policy a condition of consumption, and an optional record count per file. |
| 2026-10-02, 17:51 | W3C DID Resolution (`w3c-did-resolution`) | [Comment on PR #344](https://github.com/w3c/did-resolution/pull/344#issuecomment-5958114211) | Supports registering a `RelativeRefHandler` with the PR, and cites GS1-Conformant Resolver 1.2.1 §2.12 on query-string forwarding. |
| 2026-10-02, 18:13 | W3C Agentic Web WG charter draft (`w3c-agenticweb-wg`) | [PR #888](https://github.com/w3c/charter-drafts/pull/888), merged on 2026-10-13 (11:06 UTC), after approvals by three reviewers (read on GitHub on 2026-10-14) | Editorial fixes to the draft: broken links, a typo and template leftovers, with no change to scope, deliverables or coordination list. |
| 2026-10-02, 18:55 | A2A (`a2a-discovery`) | [Comment on #2276](https://github.com/a2aproject/A2A/issues/2276#issuecomment-5959270760) | Points to #2240 and to ARD §5.1, and asks whether the proposals could converge on one path. |
| 2026-10-02, 19:39 | A2A (`a2a-discovery`) | [Comment on #2276](https://github.com/a2aproject/A2A/issues/2276#issuecomment-5960055886) | Notes that "successor" is how ARD describes itself, and that AI Catalog is still maintained and uses `ai-catalog.json`. |
| 2026-10-02, 20:04 | W3C DID Resolution (`w3c-did-resolution`) | [Comment on PR #344](https://github.com/w3c/did-resolution/pull/344#issuecomment-5960521110) | On removing built-in `serviceType`: says selection by type matters to agents, cites GS1-Conformant Resolver 1.2.1 §2.6.2 on `linkType`, and asks for a shared registered equivalent. |
| 2026-10-03, 08:39 | UCP (`ucp`) | [Comment on PR #890](https://github.com/Universal-Commerce-Protocol/ucp/pull/890#issuecomment-5967260400), open and draft | On the open question of the subscription policy draft: suggests an `id` on the policy and on each schedule, mirroring payment terms, and a distinct cancellation link, citing Article 11a of Directive 2011/83 and §312k of the German Civil Code. |
| 2026-10-06, 11:45 | Lighthouse ARD audit (`ard`) | [Comment on PR #17260](https://github.com/GoogleChrome/lighthouse/pull/17260#issuecomment-6015540489) | Suggests wording for the legacy-discovery message, since `/.well-known/ai-catalog.json` is also the current discovery path of AI Catalog and of MCP Server Card clients. |
| 2026-10-06, 15:47 | AI Catalog (`lf-ai-catalog`) | [Comment on PR #117](https://github.com/Agent-Card/ai-catalog/pull/117#issuecomment-6019988233), open on 2026-10-13 | On the policy URLs of the extension: asks whether it could carry an optional digest of each document, taken when the entry is signed. |
| 2026-10-06, 17:21 | Lighthouse ARD audit (`ard`) | [Comment on issue #17271](https://github.com/GoogleChrome/lighthouse/issues/17271#issuecomment-6021644887), open on 2026-10-13 | Asks that the audit not fail a site that serves `/.well-known/ai-catalog.json` on purpose, for example by failing only when neither an ARD source nor a valid AI Catalog is found. |
| 2026-10-06, 17:32 | Lighthouse (`ard`) | [PR #17272](https://github.com/GoogleChrome/lighthouse/pull/17272), merged on 2026-10-06 (17:34 UTC) | Quotes the name in the front matter of the Agentic Web issue template, which did not parse. |
| 2026-10-06, 18:15 | IETF vcon list (`ietf-vcon`) | [Message](https://mailarchive.ietf.org/arch/msg/vcon/oqJ2wLwEwk044RnhpfOwwosNLSA/) in the thread "Strawman VCON Recharter to work on AI Agent Interaction Record Formats" | Asks whether the extension's list could name user instructions and approvals, and references to related records in other protocols. |
| 2026-10-07, 02:58 | IETF AUDIT list (`ietf-audit`) | [Message](https://mailarchive.ietf.org/arch/msg/audit/0dnQeIFcwQzMezPI1xek7unw4-M/) in the thread "Charter Comments -- more specific on the scope?" | Proposes that a slot of the expected-record declaration may need to state the expected holder or recipient as well as the producer, with an agentic purchase and the EU durable-medium confirmation as the example. |
| 2026-10-07, 06:12 | IETF AUDIT list (`ietf-audit`) | [Message](https://mailarchive.ietf.org/arch/msg/audit/XVTaQ0mqjOt4YHjGjpJPUye3vCY/) in the same thread | Writes the proposal as a seventh case, "Wrong recipient or holder", and qualifies the cross-border sentence. |
| 2026-10-07, 07:07 | UCP (`ucp`) | [Comment on issue #904](https://github.com/Universal-Commerce-Protocol/ucp/issues/904#issuecomment-6032850150) | Answers a census author's question on telling "not enabled" from "enabled but failing" and points to the reporting frame of #867; adds that an implementation can answer 404 at the profile path in order not to take part, so that a census counts it as an absence ("a 410 may be deliberate, a 404 says less"). |
| 2026-10-08, 08:39 | IETF DAWN list (`ietf-dawn`) | [Message](https://mailarchive.ietf.org/arch/msg/dawn/N9cewk1F_OMxNsKlQKNQsZ068Pg/) in the thread "DAWN Coordination: Discovery Information and Trust Artifact Pointers" | Agrees on a third case (reference resolves, record absent) and proposes that the requirement have the discovering entity report which of three outcomes it hit. |
| 2026-10-08, 08:51 | UCP (`ucp`) | [Comment on issue #904](https://github.com/Universal-Commerce-Protocol/ucp/issues/904#issuecomment-6056280310) | Answers two questions on geo-redirects and a second route (server card) in the census run. |
| 2026-10-08, 09:11 | UCP (`ucp`) | [Comment on Discussion #864](https://github.com/Universal-Commerce-Protocol/ucp/discussions/864#discussioncomment-18809459) | Answers a question on how a platform finds an independent lodging property; reads a property-hosted profile as necessary but not sufficient. |
| 2026-10-08, 10:49 | UCP (`ucp`) | [Comment on Discussion #867](https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18812160) | Answers the census run posted against the frame: canonical host, cross-host 3xx, the 7 non-parsing 200s as row 1 without row 2. |
| 2026-10-08, 13:56 | IETF AUDIT list (`ietf-audit`) | [Message](https://mailarchive.ietf.org/arch/msg/audit/YTKRHilHNwQ1a3EgZtu6xMd3WlM/) from the lead editor of the expected-record draft | Says that cases 7 and 8 go into the -00 of the draft and that the author of this map and the proposer of case 8 "will be named as contributors for these" (case 7 is the one the author wrote on 2026-10-07; the draft text was not on the datatracker on 2026-10-13). |
| 2026-10-09, 04:52 | UCP (`ucp`) | [Comment on PR #897](https://github.com/Universal-Commerce-Protocol/ucp/pull/897#issuecomment-6074516498), open | On the allergens disclosure of the food checkout draft: asks for an optional list of allergen codes beside the free text, with the code list named. |
| 2026-10-09, 10:55 | UCP (`ucp`) | [Comment on Discussion #867](https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18833761) | Posts version 3 of the reporting frame: probed host, 3xx at the profile path, row 1a (200 after redirect), prober-side line widened, optional hosting row. |
| 2026-10-10, 08:06 | IETF DAWN list (`ietf-dawn`) | [Message](https://mailarchive.ietf.org/arch/msg/dawn/9fQNdrMYjWWKrlbxVuafb7vdD4E/) in the thread "DAWN Coordination: Discovery Information and Trust Artifact Pointers" | Accepts a participant's wording that a finding of absence must rest on a complete result for the lookup, and proposes it as the closing sentence of the second requirement. |
| 2026-10-10, 14:27 | UCP (`ucp`) | [Comment on Discussion #867](https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18851878) | Replies to a census author: three asset hosts belong under "other domain", and a storefront that settles on an asset host may not have been the storefront; proposes recording "storefront did not settle on a storefront host". |
| 2026-10-10, 14:33 | UCP (`ucp`) | [Comment on Discussion #867](https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18851929) | Invites a participant who checks `/.well-known/ucp` weekly across about 450 restaurant ordering sites to post the next run in the frame, and asks what comes back from the ordering platforms that return nothing. |
| 2026-10-10, 14:36 | UCP (`ucp`) | [Comment on PR #897](https://github.com/Universal-Commerce-Protocol/ucp/pull/897#issuecomment-6098607731), open | Replies to a reviewer on allergens: proposes `code`, `status` and `source` per allergen, and the rule that an allergen not listed means "not recorded", never "free of". |
| 2026-10-10, 18:02 | ARD (`ard`) | [Comment on PR #100](https://github.com/ards-project/ard-spec/pull/100#issuecomment-6100551973) | Notes that Lighthouse, after PR #17258 (merged on 2026-10-09), ports the warning with the wrong ADR-0003 reference, and that merging the PR fixes it at the source. |
| 2026-10-11, 08:27 | UCP (`ucp`) | [Comment on Discussion #867](https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18860671) | Replies to a census author's re-run: fall back and flag, keeping flagged rows out of the headline count or beside it; proposes the case "storefront did not settle on a storefront host" for the frame. |
| 2026-10-11, 08:31 | UCP (`ucp`) | [Comment on PR #897](https://github.com/Universal-Commerce-Protocol/ucp/pull/897#issuecomment-6107155683), open | Accepts a reviewer's small proposal for allergens (three optional fields and one rule), asks for a PR against the branch, and asks that the conflict message say what is known: "No allergen information about peanuts for this dish". |
| 2026-10-11, 08:48 | IETF vcon (`ietf-vcon`) | [PR #41](https://github.com/ietf-wg-vcon/draft-ietf-vcon-vcon-core/pull/41) on the charter text, open on 2026-10-13 | Adds to the AI Agent Extension the instructions and approvals of the person the agent acts for, and references to records in other systems, and a use case for agent-mediated transactions. |
| 2026-10-11, 08:53 | IETF vcon list (`ietf-vcon`) | [Message](https://mailarchive.ietf.org/arch/msg/vcon/_Q35yLVgzRHm5VRe2leNWEs8SWY/) in the thread "Strawman VCON Recharter to work on AI Agent Interaction Record Formats" | Announces PR #41 and offers to adjust the wording. |
| 2026-10-11, 18:19 | UCP (`ucp`) | [Comment on Discussion #867](https://github.com/Universal-Commerce-Protocol/ucp/discussions/867#discussioncomment-18867673) | Posts the updated reporting frame, "the version to copy": the case "storefront did not settle on a storefront host", probed and settled host per row, vantage as a run field, and a table of the runs reported against the frame. |
| 2026-10-11, 18:23 | IETF Web Bot Auth, crawler best practices (`ietf-webbotauth`) | [Comment on PR #22](https://github.com/garyillyes/cbcp/pull/22#issuecomment-6112212839) | Replies to a participant on Retry-After: honouring it means not returning sooner than the server asked, with a maximum that the crawler operator documents publicly. |
| 2026-10-12, 06:23 | AAIF Agentic Commerce Working Group (`aaif-wg-agentic-commerce`) | Message on the public working group mailing list, subject "Re: [wg-agentic-commerce] Call for topics & presenters", addressed to Ilya Grigorik, chair of the working group, with the list in copy | Accepts a 30-minute slot at the call (about 20 minutes of presentation, the rest for questions) and announces that the map will be public before the call and the link shared with the group. |
| 2026-10-13, 04:22 | UCP (`ucp`) | [Review comment on PR #897](https://github.com/Universal-Commerce-Protocol/ucp/pull/897#discussion_r4254706577), open | Asks that the response carry the basis of a percentage tip, not only the computed amount. |
| 2026-10-13, 04:38 | UCP (`ucp`) | [Review comment on PR #897](https://github.com/Universal-Commerce-Protocol/ucp/pull/897#discussion_r4254785229), open | Asks that a changed `allergens` disclosure after review be re-sent, and no completion until the buyer has seen it, on the same terms as a changed total. |
| 2026-10-14, 15:22 | AAIF Agentic Commerce Working Group (`aaif-wg-agentic-commerce`) | Message on the public working group mailing list, in the thread "Call for topics & presenters" | A message of the author in the same thread, sharing the link to the map and its DOI before the call and inviting corrections. |
| 2026-10-14 | AAIF Agentic Commerce Working Group (`aaif-wg-agentic-commerce`) | Presentation of the map to the working group call | The author presented the map at the working group call of 2026-10-14, as announced in the message of 2026-10-12. The slides are not published here. |

---

<a id="part-calendar"></a>
# Part 13: Appendix: Calendar

# Calendar: dated public events in the next 60 days (2026-10-14 to 2026-12-13)

This calendar lists dated public events of the next 60 days declared by the venues; charter milestones beyond 60 days are listed in the entries only, and the individual draft expiries listed here are marked as such: they are not commitments of a venue. Dates declared in public by the venues of `entries/`, read between 2026-10-02 and 2026-10-14. No estimates: a date that a source gives as "approximately" is marked so, and an undated commitment is not listed. Entries are linked by id. Rows already past on 2026-10-13 were removed: the IESG telechat of 2026-10-08 (the agentproto charter, with the WG formed the same day), the TPAC deadline of 2026-10-08 for breakouts scheduled in advance, the TPAC breakout schedule expected on 2026-10-13 (the README now says around 19 October) and the next meeting of the AAIF Security and Privacy group on 2026-10-13.

Events as declared by the venues on 2026-10-14; check the venue for later changes.

| Date | What | Entry | Source |
|---|---|---|---|
| 2026-10-15 | Accuracy & Reliability of AI Agents: Virtual Summit, 15:00 to 17:00 GMT, online, "Organized by Agentic AI Foundation" (event page, read on 2026-10-13) | `aaif-structure` | https://home.mlops.community/public/events/accuracy-and-reliability-of-ai-agents-virtual-summit-77nje0s530 |
| 2026-10-15 | AAIF Taxonomy and Landscape Workstream: Ecosystem Architecture Map v1.0, target in the charter; the README has not accepted Landscape contributions since 2026-09-16 (PR #61) | `aaif-structure` | https://github.com/aaif/ws-taxonomy-landscape/blob/main/charter/charter.md ; https://github.com/aaif/ws-taxonomy-landscape/blob/main/README.md ; https://github.com/aaif/ws-taxonomy-landscape/pull/61 |
| approx. 2026-10-19 | Schedule of the Monday to Wednesday TPAC breakouts added to the TPAC calendar (README: "Around 19 October we will add the schedule"); on 2026-10-14 the calendar page already lists sessions marked "Tentative" | `w3c-tpac-2026` | https://github.com/w3c/tpac2026-breakouts |
| 2026-10-19 | Comments on the proposed DAWN charter due to the IESG mailing list (WG Review announcement of 2026-10-09: "The IESG has not made any determination yet"; external review since 2026-10-09, read on 2026-10-13) | `ietf-dawn` | https://mailarchive.ietf.org/arch/msg/ietf-announce/T8B2tMLk8fU-UE8kASlDIIVLgb4/ |
| 2026-10-21 | aipref virtual interim meeting, 20:00 to 21:30 UTC, no agenda submitted on 2026-09-30 (interim-2026-aipref-15) | `ietf-aipref` | https://mailarchive.ietf.org/arch/msg/ai-control/H8Gycx8vy4BKierBvIhG8V2JYFQ/ |
| 2026-10-22 | IESG telechat with the DAWN charter on the agenda (datatracker, read on 2026-10-13: "On agenda of 2026-10-22 IESG telechat"); no WG Action announced up to 2026-10-12 | `ietf-dawn` | https://datatracker.ietf.org/doc/charter-ietf-dawn/ |
| 2026-10-22 | vCon working group virtual interim meeting, 14:00 to 16:00 UTC (agenda: "Continue discussion on core document leading up to -05 submission before SFO including redaction PR inclusion.  Discuss charter draft status.") | `ietf-vcon` | https://datatracker.ietf.org/meeting/upcoming.ics?show=vcon |
| 2026-10-23 | UCP Agentic Donations DWG proposal (issue #924): nominations due ("October 23, 2026"; read on 2026-10-13) | `ucp` | https://github.com/Universal-Commerce-Protocol/ucp/issues/924 |
| 2026-10-23 | Expiry of draft-illyes-webbotauth-cbcp unless revised (draft expiry, not a WG commitment) | `ietf-webbotauth` | https://datatracker.ietf.org/doc/draft-illyes-webbotauth-cbcp/ |
| 2026-10-26 to 2026-10-30 | TPAC 2026, Dublin. Proposed breakouts on agents (#22 The Agentic Web, opened 2026-09-16; #24 and #25 on the same theme, opened 2026-09-17; #34 Zurich workshop report, #37 DID Methods WG pre-kickoff, #39 KYAPay and others); provisional slots of some of them below, listed as "Tentative" on the TPAC calendar on 2026-10-14 | `w3c-tpac-2026`, `w3c-agenticweb-wg`, `w3c-gs1-ecommerce-workshop`, `w3c-did-methods-wg`, `kyapay` | https://github.com/w3c/tpac2026-breakouts |
| 2026-10-26 | TPAC 2026 breakout #39, KYAPay: Verified Agent Identity and Payments for Ubiquitous Agentic Commerce on the Existing Web: provisional slot, 17:00 to 18:00 GMT as listed (18:00 to 19:00 in Rome, converted), Second Floor - Room 3, marked "Tentative" (TPAC calendar, read on 2026-10-14) | `kyapay`, `w3c-tpac-2026` | https://www.w3.org/calendar/tpac2026/breakout-sessions/ |
| 2026-10-28 | TPAC 2026 breakout #34, Report and follow-ups from the E-commerce for Humans and AI Agents workshop: provisional slot, 15:15 to 16:15 GMT as listed (16:15 to 17:15 in Rome, converted), Second Floor - Room 1 and 2, marked "Tentative" (TPAC calendar, read on 2026-10-14) | `w3c-gs1-ecommerce-workshop`, `w3c-tpac-2026` | https://www.w3.org/calendar/tpac2026/breakout-sessions/ |
| 2026-10-28 | Advisory Committee review of the DID Methods WG charter closes | `w3c-did-methods-wg` | https://lists.w3.org/Archives/Public/public-new-work/2026Sep/0011.html |
| 2026-10-29 | TPAC 2026: deadline, at noon local time, for breakout proposals made once TPAC is under way (Thursday and Friday slots; README of w3c/tpac2026-breakouts, read on 2026-10-13) | `w3c-tpac-2026` | https://github.com/w3c/tpac2026-breakouts |
| 2026-10-29 | AAIF Workflows and Process Integration group: target of the Best Practices deliverable in the charter (charter.md, "Last Updated: 2026-07-23") | `aaif-structure` | https://github.com/aaif/wg-workflows-and-process-integration/blob/main/charter/charter.md |
| 2026-10-30 | TPAC 2026 breakout #22, The Agentic Web: provisional slot, 08:30 to 09:30 GMT as listed (09:30 to 10:30 in Rome, converted), Second Floor - Room 3, marked "Tentative" (TPAC calendar, read on 2026-10-14) | `w3c-agenticweb-wg`, `w3c-tpac-2026` | https://www.w3.org/calendar/tpac2026/breakout-sessions/ |
| 2026-11-02 | UCP Agentic Donations DWG proposal (issue #924): target date for the initial package ("November 2, 2026") | `ucp` | https://github.com/Universal-Commerce-Protocol/ucp/issues/924 |
| approx. 2026-11-02 | Charter refinement of the Digital Policy WG ends | `w3c-digital-policy-wg` | https://lists.w3.org/Archives/Public/public-new-work/2026Sep/0012.html |
| approx. 2026-11-10 | Charter refinement of the Agentic Web WG ends (announcement on public-new-work) | `w3c-agenticweb-wg` | https://lists.w3.org/Archives/Public/public-new-work/2026Oct/0002.html |
| 2026-11-14 to 2026-11-20 | IETF 127, San Francisco (ietf.org/meeting/127, read on 2026-10-13: "14 Nov 2026 - 20 Nov 2026"); a two-hour webbotauth session has been requested, not scheduled (request of 2026-09-15) | `ietf-webbotauth` | https://www.ietf.org/meeting/127/ ; https://datatracker.ietf.org/meeting/upcoming/ ; https://mailarchive.ietf.org/arch/msg/web-bot-auth/w0al4_01_6Evh8AI9wXnbKz6Kc0/ |
| 2026-11-28 | Expiry of draft-mozleywilliams-dnsop-dnsaid -02 unless revised (draft expiry, not a WG commitment) | `ietf-dnsaid` | https://datatracker.ietf.org/doc/draft-mozleywilliams-dnsop-dnsaid/ |
