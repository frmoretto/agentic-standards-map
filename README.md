# Agentic Standards Map

**Who is standardising agentic commerce, where, and what they have committed to next.**

W3C, IETF, GS1, UN/CEFACT, the Linux Foundation, AAIF, and the industry protocols (UCP, ACP, AP2, x402, Visa, Mastercard) are all working on how an AI agent finds a seller, trusts a product, proves who it acts for and pays. They do it at the same time, at different speeds and with different rules. This map puts them on one page.

Every statement is dated and points to a public source. The map makes no predictions or recommendations of its own and does not rank approaches. Third-party proposals are recorded with attribution and their stated status.

This map documents public standardisation activity, specifications and declared commitments. It does not measure market adoption, transaction volume, cross-protocol interoperability or the reliability of deployed implementations. Implementation claims are reported only where supported by dated public evidence and are not treated as evidence of interoperability.

*Version 1.3 (2026-11-02) · site updated 2026-11-02. The map is updated as venues move; each entry carries its own read date.*

DOI (all versions): [10.5281/zenodo.23357361](https://doi.org/10.5281/zenodo.23357361)

---

## Four things you see only when you look across venues

**1. The map identifies at least nine discovery mechanisms or publication paths.** `/.well-known/ucp`, A2A's `agent-card.json`, schema.org, ARD, AI Catalog, MCP Server Cards, DNS-AID, the `/.well-known/poppy.json` of the Personal Agent Protocol, and `/.well-known/x402`, under discussion in the Domain Discovery working group of the x402 Foundation. Of these nine, two are in the IANA well-known registry: `agent-card.json` (permanent) and `/.well-known/ucp` (provisional, registered 2026-10-26) (registry updated 2026-10-26, read 2026-10-27). Two venues have discovery-charter work in progress: IETF DAWN became a working group on 2026-10-22 (approved charter charter-ietf-dawn-01), and the W3C Agentic Web WG charter is in refinement. [Seam S1](map-bundle.md#part-seams)

**2. Product identity: one ratified route and one route marked at risk.** GS1 Digital Link gives a ratified route to product identifiers; the DID route cited for Digital Product Passports rests on a feature that the DID Resolution Candidate Recommendation Draft marks at risk. One workshop position statement (#31, Sven Böckelmann) frames the open question as three checks: "Where. Who signed. Who may." [Seam S2](map-bundle.md#part-seams)

**3. Agent identity: several protocols reference HTTP Message Signatures or Web Bot Auth.** Visa TAP, Mastercard Agent Pay, UCP and x402 build on RFC 9421 or Web Bot Auth. The IETF agentproto charter names webbotauth among the groups to coordinate with, and the draft W3C Agentic Web charter lists it for coordination too. ACP's texts do not mention it (not found in the ACP repository, 2026-10-03). [Seam S3](map-bundle.md#part-seams)

**4. Checkout: what each protocol defines differs between the checkout and the events after it.** Native AP2 chains a merchant-signed checkout, the user's mandate and a Checkout Receipt that the merchant must return once it accepts or rejects the mandate (docs/ap2/specification.md at commit e1ea56d, read 2026-10-13). The words refund and cancel are not found in the seven AP2 documents of docs/ap2; the goods-return term occurs only as the field return_policy ("30-day returns") in two example checkouts of checkout_mandate.md, and fulfil(l) only as a generic verb, never for the fulfilment of an order (2026-10-14). UCP signs the delivery of order webhooks (RFC 9421) and ACP signs its webhooks with HMAC: those are signatures on a delivery. Poppy, PACT and Shopify/shop each state in writing what their own record does not prove. A confirmation to the consumer on a durable medium is not found in the Poppy specification and operations pages, the PACT specification page or the Shopify/shop README, SKILL.md and transactions.md (2026-10-13). [Seam S4](map-bundle.md#part-seams)

## Next on the calendar

- **approx. 2 Nov** Charter refinement of the Digital Policy WG ends
- **5 Nov** Public comments on the proposed maintenance charter of the Decentralized Identifier
- **approx. 10 Nov** Charter refinement of the Agentic Web WG ends
- **14 to 20 Nov** IETF 127, San Francisco
- **16 Nov** IETF 127: agentproto session, 14:00 to 16:00 San Francisco time, room Continental 5

Full 60-day calendar: [Calendar](map-bundle.md#part-calendar)

## Start here

| If you want | Go to |
|---|---|
| The cross-venue picture | [Seams S1 to S4](map-bundle.md#part-seams) |
| How the payment protocols compare | [Payment protocols compared](map-bundle.md#part-matrix) |
| Where each venue stands, in one table | [Status](map-bundle.md#part-status) |
| Everything in one file | [`map-bundle.md`](map-bundle.md) |
| The site, one page per venue | [frmoretto.github.io/agentic-standards-map](https://frmoretto.github.io/agentic-standards-map/) |
| One venue in detail | [`entries/`](entries/) |

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

Marinoni Moretto, F. (2026). Agentic Standards Map (Version 1.3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.23882108

Please cite the entry id, the date it was read and the DOI. To cite the map in general, use https://doi.org/10.5281/zenodo.23357361.

## Contributing

Corrections and additions based on public sources are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md). Each change is dated.

## Licence

Content (entries, notes, `MAP.md`, `map.json`, the per-entry JSON files, `map-bundle.md`): [CC BY 4.0](LICENSE). Code (`tools/`): [MIT](LICENSE-CODE). Quotations from third-party texts remain under their own terms; CC BY 4.0 applies to the author's text and data.
