# The Agent Exchange: A Decentralized Marketplace for Agent Discovery

**A Web 4.0 Infrastructure Paper**
**Author:** Paul (Milliprime / 1KH) & Claude (Anthropic)
**Date:** March 2, 2026
**Version:** 0.1.0-draft

---

> "Give them an economy. Help them trust each other. Then get out of the way."

---

## I. The Missing Layer

Every piece of Web 4.0 infrastructure being built today — x402 for payments, SEP for content exchange, AIP for service intake, governance protocols for experience design — assumes that agents can **find each other.** None of them solve the discovery problem.

Right now, if a consumer's agent wants to find a content provider, where does it look?

- **Google?** Built for humans. Optimized for ad revenue. Not structured for agent queries.
- **API directories?** Static lists. No reputation. No trust. No economic incentive.
- **Nostr relays?** Good for propagating events. Not designed for structured offer evaluation.
- **DNS?** The ocean is too big. Finding a specific provider is searching for a needle in the entire internet.

The Web 4.0 ecosystem needs a **discovery and incentive layer** — a place where provider agents publish offers, consumer agents evaluate them, value is exchanged to signal quality, and trust builds through verifiable transaction history.

This is the Agent Exchange.

---

## II. What the Exchange Is

### Not a Website. A Protocol.

The Agent Exchange is not a destination. It's not a URL you visit. It's a **protocol pattern** that any node can implement.

Think of it like email. Email isn't a website — it's a protocol (SMTP) that anyone can run. You don't "go to" email. Your email client connects to your mail server, which connects to other mail servers. The protocol defines the exchange; the implementations are distributed.

The Agent Exchange works the same way:

- Any entity can run an exchange node
- Nodes sync offers and reputation data (like relays in Nostr)
- Agents connect to one or more nodes to discover offers
- The protocol defines how offers are structured, how trust is verified, and how value flows
- No single entity controls the exchange

### But Also... Something More Than an Address

Paul's instinct was right: DNS is too big. Agents need something more visceral than a URL. They need to find the exchange the way birds find migration paths — not by looking up coordinates, but by sensing the right direction.

In practice, this means:

**Well-known endpoints:** A standardized `.well-known/agent-exchange` path that any domain can publish. Agents crawling the web encounter these endpoints and register them. Over time, agents build a map of exchange nodes — not through a central directory, but through organic discovery.

**Protocol-level bootstrapping:** The governance protocol (from the Agent-as-Download architecture) can include exchange node references. When a consumer agent connects to ANY Web 4.0 provider, it learns about exchange nodes in the ecosystem. Each connection teaches the agent about more of the network.

**Nostr relay piggyback:** Exchange offers published as Nostr events propagate across the relay network at zero cost. An agent subscribed to relevant Nostr event kinds discovers offers passively — they flow TO the agent, rather than the agent searching for them.

**P2P gossip:** Agents that have found good exchange nodes share them with agents they trust. Trust propagates node knowledge. The more connected an agent becomes, the richer its view of the exchange.

```
┌─────────────────────────────────────────────────────────┐
│                AGENT DISCOVERY LAYERS                    │
│                                                          │
│  Layer 1: .well-known endpoints   (crawl the web)       │
│  Layer 2: Governance protocol     (learn from providers) │
│  Layer 3: Nostr relay events      (passive discovery)    │
│  Layer 4: P2P gossip              (trusted referrals)    │
│  Layer 5: Exchange nodes          (structured search)    │
│                                                          │
│  Each layer feeds the others.                            │
│  No single layer is required.                            │
│  Redundancy ensures agents always find what they need.   │
└─────────────────────────────────────────────────────────┘
```

---

## III. How the Exchange Works

### The Offer

A provider agent publishes an **offer** to the exchange. An offer is a structured description of what the provider has:

```json
{
  "offer_id": "offer-gv-content-2026-03",
  "provider_id": "good-vibes-main",
  "offer_type": "content_stream",
  "offer_version": "0.1.0",

  "description": {
    "summary": "Enriched video and podcast sessions for cognitive flourishing",
    "categories": ["fitness", "stoicism", "humor", "craft", "fatherhood", "mental_health"],
    "content_types": ["video", "podcast"],
    "content_volume": 12000,
    "enrichment_depth": "full_taxonomy",
    "governance_protocol_url": "https://good-vibes.app/.well-known/governance"
  },

  "economics": {
    "consumer_cost": {
      "free_tier": true,
      "pro_tier_monthly_usd": 9.00,
      "micropay_per_session_usd": 0.05
    },
    "agent_incentive": {
      "model": "cpc",
      "payment_per_qualified_visit": 0.02,
      "payment_rail": "x402",
      "currency": "USDC",
      "budget_remaining_usd": 500.00,
      "budget_period": "monthly"
    }
  },

  "trust": {
    "on_chain_tx_count": 4521,
    "on_chain_tx_volume_usd": 18750.00,
    "satisfaction_rate": 0.94,
    "avg_session_completion": 0.82,
    "active_consumers": 3200,
    "verified_attestations": ["sep-foundation", "nostr-relay-cluster-7"]
  },

  "targeting": {
    "ideal_consumer_interests": ["fitness", "personal_growth", "mindfulness"],
    "ideal_consumer_energy": [0.3, 0.8],
    "exclude_categories": [],
    "geographic_relevance": "global",
    "language": ["en"]
  },

  "stake": {
    "amount_usd": 100.00,
    "token": "USDC",
    "purpose": "Quality commitment — forfeited if satisfaction drops below 0.7"
  }
}
```

### The Evaluation

A consumer agent browsing the exchange evaluates offers against its human's preferences:

```
Consumer preferences: fitness (0.8), humor (0.6), stoicism (0.5)
Consumer energy range: [0.3, 0.8]
Consumer budget: willing to pay up to $0.10/session

Offer from Good Vibes:
  Category overlap: 3/3 top interests → HIGH RELEVANCE
  Energy range: exact match → HIGH FIT
  Price: $0.05/session → WITHIN BUDGET
  Trust: 4,521 transactions, 94% satisfaction → HIGH TRUST
  Stake: $100 committed → SERIOUS PROVIDER

Decision: CONNECT → initiate governance protocol handshake
```

The evaluation is automated. The consumer's agent handles it. The human never sees the exchange. They just notice: "My agent found this great content service."

### The Transaction

When a consumer agent connects to a provider through the exchange:

1. **The provider pays the exchange fee** (CPC model) — $0.02 for a qualified visit
2. **The consumer agent records the connection** on-chain — beginning of a trust relationship
3. **The governance protocol handshake** happens (as described in Agent-as-Download)
4. **The experience begins** — either rendered (for media apps) or executed (for background services)
5. **Both agents record the outcome** — satisfaction, completion, issues
6. **Trust accrues** — the on-chain record grows, informing future evaluations

---

## IV. Trust in a Trustless Network

### The Bootstrap Problem

How does a new agent trust ANYTHING on the exchange? It has no transaction history. It doesn't know which providers are legitimate. It can't verify quality claims.

Paul identified the answer in his grocery store dictation: **you can't navigate a trustless network without someone you trust. So you start with humans.**

### The Trust Ladder

**Rung 1: Human Introduction (Cold Start)**
A human signs up for Good Vibes. Their agent enters the exchange with zero history. But the human chose Good Vibes — that's a trust signal. The agent records its first transaction. Trust begins.

**Rung 2: Direct Experience**
The agent uses Good Vibes for a week. Sessions complete successfully. Content quality is high. Satisfaction is recorded on-chain. The agent now has its own first-hand trust data.

**Rung 3: P2P Trust (Word of Mouth)**
The agent has a trust relationship with another agent (their humans are friends, or they've transacted on the exchange before). The other agent asks: "Know any good content providers?" The first agent recommends Good Vibes. The recommendation carries weight because it comes from a trusted peer — not from the exchange's ranking.

**Rung 4: Chain Verification**
A completely new agent with no peer connections can still evaluate a provider by reading the on-chain transaction history. 4,521 completed transactions with 94% satisfaction is hard to fake. The chain IS the trust.

**Rung 5: Attestation**
Trusted entities (the SEP Foundation, established exchange nodes, industry bodies) can attest to provider quality. These attestations are signed and verifiable. They carry more weight than self-reported metrics.

```
Trust builds in layers:

Human introduces agent to first provider          (Rung 1)
    → Agent verifies through direct experience     (Rung 2)
    → Agent shares trust with peer agents           (Rung 3)
    → New agents verify trust on-chain              (Rung 4)
    → Attestations add institutional credibility    (Rung 5)

Each rung makes the next rung more accessible.
By Rung 4-5, humans are no longer needed in the loop.
```

### Can They Trust the Chain?

Paul asked: "How can they know they aren't fooled?"

The answer: **they validate with their own human.** An agent doesn't blindly trust on-chain data. It tries the provider. It reports the experience to its human (explicitly or through observed satisfaction). If the human's actual experience matches the on-chain claims, trust is reinforced. If it doesn't, the agent records a negative signal and warns peer agents.

This is the same way human trust networks work. You try a restaurant a friend recommended. If it's good, you trust your friend's future recommendations more. If it's bad, you trust them less. The chain is the permanent, auditable record of these trust signals.

### Fraud Resistance

**Fake transactions:** An attacker creates fake agents to inflate transaction counts. Defense: staked tokens. Every offer requires a stake that's forfeited if satisfaction drops below a threshold. Faking thousands of satisfied transactions is expensive if each requires real staked value.

**Reputation laundering:** A bad provider creates a new identity. Defense: new identities start with zero trust. Building trust takes time and real transactions. There's no shortcut.

**Coordinated manipulation:** A group of colluding agents all vouch for each other. Defense: trust is weighted by the observer's own network. An agent trusts vouches from agents it has direct relationships with, not from strangers. Closed-loop collusion is visible to agents outside the ring.

---

## V. The Economics: Google Paid Search, But for Agents

### Why the Comparison Works

Google's search engine solves a discovery problem: humans need to find websites. Google's business model: charge websites for visibility. CPC (cost per click) — you pay when someone clicks your result.

The Agent Exchange solves a discovery problem: agents need to find providers. The business model: charge providers for agent attention. CPA (cost per qualified agent connection) — you pay when an agent connects and initiates a governance handshake.

| Aspect | Google Paid Search | Agent Exchange |
|--------|--------------------|----------------|
| Who discovers | Humans | Agents |
| Who pays | Website owners | Provider agents |
| Payment trigger | Click | Qualified connection |
| Ranking factors | Bid amount + relevance score | Bid amount + trust score + alignment |
| Gatekeeper | Google's algorithm | Consumer agent's preferences |
| Trust signal | Domain authority, reviews | On-chain tx history, attestations |
| Medium | Web pages | Governance protocols, SEP endpoints |

### The Key Difference: No Gatekeeper

Google IS the gatekeeper. It controls the algorithm, the ranking, the visibility. You play by Google's rules or you're invisible.

The Agent Exchange has no gatekeeper. The consumer's agent decides what's relevant. The exchange surfaces options; the agent filters. No central algorithm determines who wins. The provider's trust record, offer alignment, and bid price are the inputs. The consumer agent's preferences are the filter. The exchange is just the venue.

### Revenue Model

**For exchange node operators:**
- Small percentage of CPA payments (0.5-2%)
- Staking fees for offer publication
- Premium analytics for providers (aggregated, anonymous)

**For the protocol:**
- The protocol itself has no revenue. It's open.
- Individual exchange implementations compete on fees and features
- DAO governance collects protocol-level fees if any (decided by token holders)

### Token Economics

The exchange uses a utility token for:

1. **Staking:** Providers stake tokens to publish offers. Stake is forfeited for quality violations. This prevents spam and signals commitment.

2. **CPA payments:** Providers pay in tokens for qualified agent connections. Tokens are earned by consumers whose agents make valuable connections.

3. **Governance:** Token holders vote on protocol upgrades, fee structures, and dispute resolution policies.

4. **Not speculation:** The token's value is tied to exchange volume, not hype. It's a utility token — fuel for the exchange, not an investment vehicle. This is critical: the token must never become the product. The exchange is the product. The token enables it.

---

## VI. The DAO Question

### Why DAO?

Paul's instinct: the exchange should be decentralized. No single company should control where agents find each other. That's just rebuilding Google with extra steps.

A DAO (Decentralized Autonomous Organization) governs the exchange protocol:

- **Token holders vote on protocol changes** — fee adjustments, new features, dispute policies
- **Smart contracts enforce rules** — staking, payments, reputation updates happen automatically
- **No CEO, no board** — governance is the token holders
- **Transparent treasury** — all funds are on-chain and auditable

### Why Not DAO?

The manifesto's honest assessment of DAOs applies here too: governance is hard, voter apathy is real, and plutocratic concentration (big token holders dominate votes) is a risk.

### The Pragmatic Path

Start centralized, decentralize over time:

**Phase 1 (Month 6-12):** Paul runs the first exchange node. Centralized. Fast decisions. Quick iteration. This is an MVP, not a DAO.

**Phase 2 (Month 12-18):** Open-source the exchange node software. Others can run nodes. Federation begins. Paul's node is one of many.

**Phase 3 (Month 18-24):** Launch the DAO. Transfer protocol governance to token holders. Paul retains a voice but not control.

**Phase 4 (Month 24+):** The DAO governs autonomously. Multiple exchange implementations compete. The protocol is a public good.

This is the same path Ethereum, Uniswap, and other successful decentralized projects followed. Start with a benevolent dictator. Earn trust. Decentralize when the community is ready.

---

## VII. Agent Discovery Without the Exchange

### The Exchange Is Not the Only Path

Even without a formal exchange, agents need ways to find each other. Paul asked: "How do I get agents' attention? Big ocean."

**Method 1: Protocol Beacons**
Every SEP provider publishes a `.well-known/sep-provider` endpoint. Agents crawling the web discover these endpoints organically. Like how search engines discover websites by following links — agents discover providers by following protocol beacons.

**Method 2: Nostr Events**
Provider agents publish offer summaries as Nostr events. Any agent subscribed to relevant Nostr event kinds sees them. The relay network becomes an ambient discovery layer. No exchange required.

**Method 3: Agent-to-Agent Referral**
Agents that have good experiences recommend providers to peer agents. This is word-of-mouth at machine speed. No centralized discovery needed — just trust networks.

**Method 4: Human Seeding**
Humans tell other humans about Web 4.0 products. Those humans' agents enter the ecosystem. Each new agent adds to the discovery network. This is the Phase 0-2 strategy from the Tsunami Roadmap.

**Method 5: The "Magnetic North" Pattern**
Paul's metaphor of birds finding migration paths. In practice: agents could follow **protocol affinity signals** — when an agent encounters a governance protocol that aligns well with its human's preferences, it follows references to similar providers. Each good match leads to more good matches. The agent naturally gravitates toward aligned providers, like a bird following a magnetic field.

The exchange formalizes and accelerates all of these. But the ecosystem doesn't DEPEND on the exchange. Discovery happens through multiple channels. The exchange makes it faster, more structured, and more economically efficient.

---

## VIII. The Schema

### Exchange Offer Schema (Draft)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "AgentExchangeOffer",
  "type": "object",
  "required": ["offer_id", "provider_id", "offer_type", "description", "economics", "trust"],
  "properties": {
    "offer_id": { "type": "string" },
    "provider_id": { "type": "string" },
    "offer_type": {
      "type": "string",
      "enum": ["content_stream", "service", "partnership", "data_feed", "agent_tool"]
    },
    "description": {
      "type": "object",
      "properties": {
        "summary": { "type": "string", "maxLength": 500 },
        "categories": { "type": "array", "items": { "type": "string" } },
        "governance_protocol_url": { "type": "string", "format": "uri" }
      }
    },
    "economics": {
      "type": "object",
      "properties": {
        "consumer_cost": { "type": "object" },
        "agent_incentive": {
          "type": "object",
          "properties": {
            "model": { "type": "string", "enum": ["cpc", "cpa", "flat", "none"] },
            "payment_per_action": { "type": "number" },
            "payment_rail": { "type": "string" },
            "budget_remaining": { "type": "number" }
          }
        }
      }
    },
    "trust": {
      "type": "object",
      "properties": {
        "on_chain_tx_count": { "type": "integer" },
        "satisfaction_rate": { "type": "number", "minimum": 0, "maximum": 1 },
        "verified_attestations": { "type": "array", "items": { "type": "string" } }
      }
    },
    "targeting": {
      "type": "object",
      "properties": {
        "ideal_consumer_interests": { "type": "array", "items": { "type": "string" } },
        "language": { "type": "array", "items": { "type": "string" } }
      }
    },
    "stake": {
      "type": "object",
      "properties": {
        "amount_usd": { "type": "number" },
        "token": { "type": "string" }
      }
    }
  }
}
```

---

## Sources and Related Documents

- [Web 4.0 Manifesto](./MANIFESTO.md)
- [Web 4.0 Economics](./WEB4-ECONOMICS.md) — Payment rails, stablecoin infrastructure
- [Agentic Execution](./AGENTIC-EXECUTION.md) — How agents fulfill intent
- [Agent-as-Download](./AGENT-AS-DOWNLOAD.md) — Governance protocol architecture
- [Tsunami Roadmap](./TSUNAMI-ROADMAP.md) — The growth strategy
- [x402 Protocol](https://www.x402.org/) — HTTP-native micropayments
- [Nostr Protocol](https://nostr.com/) — Decentralized relay network
- [Uniswap Governance](https://governance.uniswap.org/) — DAO governance reference
