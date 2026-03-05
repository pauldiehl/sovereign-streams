# AEO: Agent Engine Optimization

**How Agents Find You in Web 4.0**
**Author:** Paul (Milliprime / 1KH) & Claude (Anthropic)
**Date:** March 5, 2026
**Version:** 0.1.0

---

> "How DOES SEO/AEO work with AI? We can see how it works with Google Search Engine but how do they do reliable research today? If I were to recreate all public facing pages using Nostr and AI-driven protocols, would they find and prefer mine?"

---

## I. The Question

SEO (Search Engine Optimization) is the game of making Google find and rank your content. Every website builder in the world plays it. But what happens when the searcher isn't Google's crawler — it's an AI agent acting on behalf of a human?

This is AEO: Agent Engine Optimization. The practice of making your content, services, and governance protocols discoverable and preferable to AI agents.

The rules are different. The stakes are higher. And the game is just starting.

---

## II. How AI Agents Research Today (2025-2026)

Right now, AI agents find information through a combination of methods — none of them fully standardized, all of them evolving rapidly.

### Training Data (The Foundation)

Every LLM has a knowledge base baked in from training. When an agent "knows" something, it's often because the model was trained on web content that included that information. This is the baseline — but it's static, it has a cutoff date, and it can't be directly influenced after training.

**What this means for you:** If your content existed on the public web before the model's training cutoff, the agent might already know about you. But this is unreliable, can't be updated, and isn't controllable.

### RAG and Search (The Active Layer)

Modern AI agents don't rely solely on training data. They actively search:

- **Web search APIs:** Agents use Google, Bing, or specialized search APIs to find current information. The results they get are influenced by the same SEO factors that affect human search — page rank, keywords, freshness, domain authority.
- **RAG (Retrieval-Augmented Generation):** Agents fetch documents and inject them into their context window before generating a response. The quality of the retrieved documents directly affects the quality of the agent's output.
- **Tool use:** Agents call APIs, read structured data, query databases. If you expose a well-structured API, agents can consume it directly — no search engine intermediary needed.

**What this means for you:** Traditional SEO still matters (for now) because agents often rely on the same search infrastructure humans do. But agents are increasingly capable of consuming structured data directly.

### Structured Protocols (The Future)

This is where Web 4.0 diverges. Instead of relying on search engines as intermediaries, agents will increasingly discover providers through:

- **`.well-known` endpoints:** Standardized URLs (like `.well-known/agent-exchange.json`) that agents check directly
- **Governance protocols:** Structured JSON documents that declare what a provider does, how it operates, and what it guarantees
- **Exchange listings:** Structured entries on the Agent Exchange with trust scores and verified capabilities
- **Nostr events:** Agent-readable content published to decentralized relays
- **P2P gossip:** Agents recommending providers to each other based on past experience

---

## III. The Two Worlds (Transitional Period)

For the foreseeable future, providers need to exist in both worlds:

```
┌─────────────────────────────────────────────────────┐
│                                                      │
│  WORLD 1: TRADITIONAL WEB                            │
│  (How agents find you TODAY)                         │
│                                                      │
│  • HTML pages with good SEO                          │
│  • Schema.org structured data                        │
│  • Google Business Profile                           │
│  • Social media presence                             │
│  • Blog content, reviews, backlinks                  │
│  • All the traditional SEO playbook                  │
│                                                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  WORLD 2: PROTOCOL ENDPOINTS                         │
│  (How agents find you in WEB 4.0)                    │
│                                                      │
│  • .well-known/governance.json                       │
│  • Agent Exchange listing with trust score           │
│  • Nostr events with enrichment metadata             │
│  • SEP (Stream Exchange Protocol) endpoints          │
│  • Machine-readable capability declarations          │
│  • Structured pricing, availability, terms           │
│                                                      │
└─────────────────────────────────────────────────────┘
```

**The key insight:** You don't choose one or the other. You maintain both. Traditional web pages catch agents that search the way humans do. Protocol endpoints catch agents that search the Web 4.0 way. Over time, the balance shifts toward protocols — but abandoning traditional web presence too early means you're invisible to the majority of agents that still rely on search engines.

---

## IV. The AEO Playbook

### Level 1: Optimize for AI Search (Today)

These are things you can do right now to make AI agents more likely to find and trust your content:

**Structured data is king.** AI agents parse structured data far more effectively than prose. Schema.org markup, JSON-LD, OpenGraph tags — anything that makes your content machine-readable without requiring an LLM to interpret it.

**Answer the question directly.** AI agents extracting information from web pages prefer content that directly answers queries. "Our therapy groups meet Thursday evenings, cost $15/session, and specialize in anxiety management" beats a marketing-heavy page that buries the details.

**Be specific over clever.** Marketing copy optimized for human emotional response is often noise to an AI agent. "Transform your relationship with worry in our intimate healing circles" tells an agent less than "Group therapy, anxiety focus, CBT-based, licensed facilitator, 8 participants max, $15/session, virtual + in-person."

**Freshness matters more.** AI agents with search capabilities weight recent content heavily. A governance protocol updated last week is more trustworthy than a static about page from 2023.

**Structured FAQs work.** Q&A formatted content maps directly to how agents process queries. A structured FAQ section on your site gives agents extractable, high-confidence answers.

### Level 2: Publish Protocol Endpoints (Near Term)

**`.well-known/governance.json`** — Publish a governance protocol at a standardized URL. Even before the Agent Exchange exists at scale, any agent that checks this endpoint gets a machine-readable declaration of your capabilities, terms, and guarantees. Early movers will be indexed by the first wave of Web 4.0 agents.

**Enrichment metadata** — Tag your content with structured metadata that goes beyond Schema.org. Include sentiment, energy level, therapeutic intent, audience fit, accessibility flags — whatever enrichment dimensions are relevant to your domain. This is the enrichment envelope concept from [SEP-EVOLUTION.md](./spec/SEP-EVOLUTION.md).

**Nostr event publication** — Publish your governance protocol and key content as Nostr events. This makes you discoverable through decentralized relays — not dependent on any single search engine or exchange.

**API-first design** — Expose your service through clean, documented APIs that agents can call directly. A well-documented REST endpoint is infinitely more useful to an agent than a beautifully designed web page.

### Level 3: Join the Exchange (Web 4.0)

**Register on the Agent Exchange** — When the exchange is live, register as a provider. Your listing includes your governance protocol, trust score (starting from zero), capabilities, pricing, and availability. Agents discover you through structured queries, not keyword search.

**Build trust through transactions** — Every successful transaction builds your trust score. This is the moat that replaces domain authority. A provider with 1,000 successful transactions and a 4.8/5 trust score is preferred over a provider with better SEO but no transaction history.

**Publish enriched offers** — Go beyond basic listings. Publish detailed capability descriptions, example governance protocol interactions, response time guarantees, and consumer testimonials (verified through on-chain attestation).

---

## V. Would Agents Prefer Protocol Endpoints Over Web Pages?

Paul's core question: "If I were to recreate all public facing pages using Nostr and AI-driven protocols, would they find and prefer mine?"

**The honest answer: eventually, yes — but not immediately.**

### Why Agents Will Prefer Structured Protocols

1. **Parsing cost:** Extracting information from a web page requires an LLM call. Reading a JSON governance protocol requires zero intelligence. The governance protocol is cheaper, faster, and more reliable.

2. **Trust signal:** A governance protocol is a commitment. A web page is marketing. Agents evaluating providers weight commitments over marketing.

3. **Negotiation readiness:** A governance protocol includes terms, pricing, availability — everything needed to initiate a transaction. A web page requires the agent to find and interpret scattered information, then navigate to a checkout flow.

4. **No dark patterns:** Web pages are designed to manipulate humans. Governance protocols are designed for agent consumption. An agent reading a governance protocol isn't susceptible to urgency countdowns, social proof popups, or misleading pricing.

5. **Completeness:** A governance protocol explicitly declares what data is collected, what guarantees exist, what the refund policy is. Web pages often bury or omit this information. Agents need complete information to evaluate trust.

### Why The Transition Takes Time

1. **Chicken-and-egg:** Agents won't check protocol endpoints until enough providers publish them. Providers won't publish them until enough agents check them. The cold start problem applies here too.

2. **Fallback to search:** Current AI agents (2025-2026) primarily rely on web search. Even the best protocol endpoint is invisible to an agent that doesn't know to look for it. The traditional web presence is still the fallback.

3. **Agent capability variance:** Not all agents are equally capable. A sophisticated agent might check `.well-known/governance.json`. A simpler one just does a web search. You need to serve both.

### The Strategy

Maintain both worlds. Lead with traditional web presence for discoverability. Publish protocol endpoints for the agents that know how to find them. As Web 4.0 grows, the ratio shifts — but never fully abandon the traditional web, because it's the bridge.

---

## VI. Measuring Agent Preference

How do you know if agents are finding and preferring your protocol endpoints? What signals indicate the shift is happening?

### Metrics to Track

**Protocol endpoint hits vs. web page hits.** Monitor traffic to your `.well-known/governance.json` and API endpoints separately from your web pages. Rising protocol traffic relative to web traffic indicates agents are finding you through structured channels.

**Agent-identified traffic.** Some agents identify themselves in User-Agent headers or request metadata. Track the ratio of agent-identified requests to human-browser requests.

**Transaction source attribution.** When a transaction completes, track whether the consumer agent discovered you through the exchange, a Nostr relay, a `.well-known` fetch, or a web search referral. This tells you which discovery channel is most effective.

**Governance protocol fetch-to-transaction ratio.** How many agents read your governance protocol vs. how many actually transact? A low ratio means your governance protocol is discoverable but not convincing. A high ratio means you're converting well.

**Standing offer volume.** How many standing offers ("notes on the door") are agents leaving at your endpoint? High volume with low match rate means there's demand you're not serving.

### The Preference Signal

The strongest signal that agents prefer your protocol endpoint: **transactions that never touched your web page.** When a consumer agent finds your governance protocol, evaluates it, negotiates terms, and completes a transaction — all without any party ever loading your website — that's pure AEO working. Track this number. When it grows, the transition is real.

---

## VII. The Nostr Angle

Paul specifically asked about recreating public-facing pages on Nostr. Here's the strategic logic:

**Nostr events are natively structured.** A Nostr event has a kind, tags, and content — all parseable without an LLM. Publishing your governance protocol as a Nostr event (with appropriate kind and tags) makes it discoverable through relay queries.

**Nostr is decentralized.** Your content exists on multiple relays. No single search engine controls discoverability. An agent can query any relay and find your events.

**Nostr has built-in identity.** Your npub is your persistent identity. Trust built on Nostr transfers across relays and clients. An agent verifying your identity on Nostr doesn't need to check a domain registry or SSL certificate.

**The limitation:** Nostr's current user base is small. Most AI agents don't query Nostr relays (yet). Publishing to Nostr is a forward bet — positioning for the network effect that will come when Web 4.0 agents standardize on decentralized discovery.

**The play:** Publish on both. Traditional web for today's agents. Nostr events for tomorrow's. The cost of publishing to Nostr is near zero (it's just structured JSON posted to relays). The upside is being discoverable when the wave hits.

---

## VIII. AEO vs. SEO: The Key Differences

| Dimension | SEO (Search Engine) | AEO (Agent Engine) |
|-----------|--------------------|--------------------|
| **Who searches** | Google's crawler | AI agents acting for humans |
| **What they read** | HTML, links, meta tags | Governance protocols, APIs, structured data |
| **How they rank** | PageRank, keywords, backlinks | Trust score, governance quality, transaction history |
| **What they optimize for** | Click-through rate | Resolution rate (did the agent fulfill the intent?) |
| **Dark patterns** | Effective (humans click) | Ineffective (agents ignore) |
| **Freshness** | Matters | Matters more |
| **Structured data** | Helpful | Essential |
| **Trust signal** | Domain authority, SSL, reviews | On-chain transaction history, governance attestation |
| **Lock-in** | Google controls ranking | Open exchange — no single gatekeeper |
| **Gaming** | Keyword stuffing, link farms | Sybil attacks, fake trust scores (but on-chain makes this expensive) |

---

## Related Documents

- [Agent Exchange](./AGENT-EXCHANGE.md) — The discovery and trust layer
- [Agent Communication](./AGENT-COMMUNICATION.md) — How agents talk to each other
- [Agentic Execution](./AGENTIC-EXECUTION.md) — Intent in, outcome out
- [Web4.0 Simulation](./WEB4-SIMULATION.md) — Testing agent discovery patterns
- [WEB4 Economics](./WEB4-ECONOMICS.md) — Payment and value exchange infrastructure
