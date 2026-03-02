# Web 4.0 — Seamless Sovereignty

> Protocol-mediated streams between sovereign consumers and sovereign providers, coordinated by intelligent agents.

**Web 4.0** is an open vision and protocol ecosystem for user-owned algorithms, agent-mediated services, and invisible decentralization. It builds on the technical infrastructure of Web3 while eliminating the friction that prevented adoption.

## What's Here

- **[MANIFESTO.md](./MANIFESTO.md)** — The full Web 4.0 vision: why Web3 failed, what agents change, the architecture, use cases, and transition strategy.
- **[spec/](./spec/)** — The **Stream Exchange Protocol (SEP)** — an open protocol defining how Stream Providers and Stream Consumers exchange metadata-driven content through structured negotiation.

## The Protocol: SEP (Stream Exchange Protocol)

SEP defines:

- **Enrichment Envelope** — How content metadata is tagged and structured
- **Consumer Intent** — How consumers express what they want (weights, filters, disclosure level)
- **Provider Response** — How providers return enriched payloads with confidence scores
- **Provider Manifest** — How providers advertise their capabilities
- **Telemetry** — How engagement signals flow back (opt-in only)

SEP is content-agnostic. It works for video, text, audio, images, apps, products, services — any content type that can be described by metadata.

## Implementations

| Project | Content Type | Status |
|---------|-------------|--------|
| [Good Vibes](https://github.com/sovereign-streams/good-vibes) | Short-form video/audio | Active development |
| Stanzas | Text (poems, stories, books) | Planned |
| Sovereign Kids | Parental-controlled media | Planned |
| YOMO | Products/marketplace | Planned |

## Core Principles

1. **Seamless Sovereignty** — Users own their algorithm without managing infrastructure
2. **Invisible Decentralization** — No wallets, gas fees, or seed phrases in the UX
3. **Protocol Over Platform** — Open specs, interoperable implementations
4. **Agent-Mediated Everything** — Agents handle discovery, negotiation, identity, payment
5. **BYOA** — Bring Your Own Algorithm
6. **Meta-First** — Index meaning, not blobs
7. **Value Flows to Creators** — No 30% platform tax

## Organization: Sovereign Streams

This repo is part of the **sovereign-streams** GitHub organization, which houses:

- `web4` — This repo: manifesto, SEP protocol spec
- `good-vibes` — First SEP implementation: cognitive environment designer
- Future implementation repos as the ecosystem grows

## Related Protocols

- **[AIP (Agent Intake Protocol)](https://github.com/agent-intake-protocol/agent-intake-protocol)** — Agent-mediated service intake and onboarding
- SEP and AIP are complementary: AIP handles service discovery/enrollment, SEP handles ongoing content streams

## License

MIT

---

*Own your scroll. Own your mind. Own your future.*
