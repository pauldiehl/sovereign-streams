# First App Blueprint: The Critical Infrastructure Stack

**What Your First Web 4.0 App Actually Needs**
**Author:** Paul (Milliprime / 1KH) & Claude (Anthropic)
**Date:** March 5, 2026
**Version:** 0.1.0

---

> "I need your magic to make it MAGICAL for all sides — the engineers, then the producers/consumers alike."

---

## I. The Honest Assessment

You've written the philosophy. You've written the architecture papers. Now you need to ship something. The question is: what's the minimum viable infrastructure that makes ANY of your products (Good Vibes, Stanzas, CoachKid, whatever you pick) a real Web 4.0 app — not just a Web 2.0 app with governance protocol marketing?

Here's the answer, broken into layers. Each layer has a "Ship Today" option (works now, imperfect) and a "Ship Right" option (Web 4.0 proper). The strategy is: Ship Today first, then migrate to Ship Right as the Coalition grows.

---

## II. The Stack

```
┌─────────────────────────────────────────────────────┐
│  LAYER 5: EXPERIENCE (what humans see)               │
│  Agent-rendered UI OR traditional PWA                 │
├─────────────────────────────────────────────────────┤
│  LAYER 4: ENRICHMENT (what makes it smart)           │
│  Metadata tagging, content intelligence, session arcs│
├─────────────────────────────────────────────────────┤
│  LAYER 3: PROTOCOL ENDPOINTS (how agents find you)   │
│  .well-known, governance.json, MCP, AGENTS.md        │
├─────────────────────────────────────────────────────┤
│  LAYER 2: PAYMENTS (how value moves)                 │
│  x402, Stripe Connect, Lightning, P2P                │
├─────────────────────────────────────────────────────┤
│  LAYER 1: IDENTITY & TRUST (who is who)              │
│  Cryptographic identity, self-sovereign trust         │
└─────────────────────────────────────────────────────┘
```

---

## III. Layer 1: Identity & Trust

### What It Does
Every user and every agent needs an identity. Not a username/password — a cryptographic identity that's portable, verifiable, and self-sovereign.

### Ship Today

**Nostr keypairs.** Every user gets a Nostr keypair (npub/nsec) on signup. This is their identity across the entire Web 4.0 ecosystem — not locked to your app.

Why Nostr keys:
- Free, open standard — no vendor dependency
- Works across any Web 4.0 service that adopts Nostr
- Cryptographic verification built-in (you ARE your public key)
- Already has tooling: nostr-tools (JS), python-nostr, rust-nostr
- Key management can be progressive: start with custodial (you hold the key), migrate to self-custodial (NIP-07 browser extensions like nos2x, Alby)

**Implementation:**
```
User signs up → App generates Nostr keypair →
npub = public identity → nsec = private key (stored securely) →
All actions signed with nsec → Verifiable by anyone with npub
```

**Trust model:** Self-sovereign from day one. No trust scores. No reputation ledger. Each agent keeps its own memory of who it has transacted with and how it went. Peer signals flow through the Nostr relay network.

### Ship Right (Later)

DID (Decentralized Identifier) integration for cross-protocol identity. But Nostr keypairs are sufficient to start and are compatible with DID evolution.

### Existing Tools

| Tool | What It Does | Status |
|------|-------------|--------|
| [nostr-tools](https://github.com/nbd-wtf/nostr-tools) | JS library for Nostr key generation, signing, relay interaction | Mature, actively maintained |
| [NIP-07](https://github.com/nostr-protocol/nips/blob/master/07.md) | Browser extension spec for key management (nos2x, Alby) | Widely adopted |
| [NIP-46](https://github.com/nostr-protocol/nips/blob/master/46.md) | Nostr Connect — remote signing (agent signs on behalf of user) | Relevant for agent delegation |

---

## IV. Layer 2: Payments

### What It Does
Value needs to move. Producer creates content → consumer pays → producer gets paid. The payment layer must work for humans AND agents.

### Ship Today: Dual-Rail

Paul identified the tension: "I need SOMETHING to make P2P payments." The honest answer is: you need TWO rails, not one.

**Rail 1: Stripe Connect (humans paying humans)**

For the products that generate Web 2.0 revenue NOW (CoachKid, Good Vibes subscriptions, direct purchases), Stripe Connect is the fastest path:
- Producers sign up with Stripe Connect
- Consumers pay with credit card
- Platform takes a small fee, rest goes to producer
- Works today, no crypto knowledge needed
- Handles tax reporting, chargebacks, compliance

This is the "pay the bills" rail. It's Web 2.0 infrastructure, but it works and it ships this week.

**Rail 2: x402 (agents paying agents)**

x402 is real and it's ready. Here's the current state (March 2026):

- **What it is:** HTTP-native payment protocol. Server returns HTTP 402 → client pays → server verifies → content served. Built on stablecoins (USDC).
- **Scale:** 100M+ transactions processed by end of 2025. 15M in January 2026 alone. 492% growth.
- **Cost:** Micropayments as low as $0.001. Settlement in sub-seconds. Near-zero fees on Solana.
- **Who's behind it:** Coinbase Development Platform + Cloudflare. x402 Foundation provides neutral governance.
- **Integration:** Already integrated as the crypto rail within Google's Agent Payments Protocol (AP2).

**Implementation for your first app:**

```
HUMAN CONSUMER → Stripe Connect → PRODUCER (Web 2.0 rail)
                                     │
AGENT CONSUMER → x402 (USDC) ───────┘ (Web 4.0 rail)
```

Both rails pay the same producer. The consumer (or their agent) chooses the rail. Over time, the x402 rail handles an increasing percentage as agents handle more transactions.

**x402 integration steps:**
1. Add x402 middleware to your API endpoints
2. When an agent hits a paid endpoint without payment, return HTTP 402 with payment requirements
3. Agent signs USDC payment, resubmits request
4. Your server verifies payment on-chain, serves content
5. Settlement is instant (Solana) or near-instant (Base L2)

**MoR (Merchant of Record) question:** For the Stripe rail, Stripe IS your MoR. For the x402 rail, you receive USDC directly — no MoR needed for crypto-native transactions. This simplifies the escrow pattern: funds move on-chain, verification is cryptographic, no intermediary needed.

### Ship Right (Later)

Lightning Network (Bitcoin L2) as a third rail for users who prefer Bitcoin over USDC. Nostr + Lightning integration via NIP-57 (Zaps) is already mature.

### Existing Tools

| Tool | What It Does | Status |
|------|-------------|--------|
| [x402 SDK](https://www.x402.org/) | Client + server libraries for x402 integration | Production-ready, multi-chain |
| [Stripe Connect](https://stripe.com/connect) | Platform payments with built-in producer onboarding | Mature, battle-tested |
| [Base L2](https://docs.base.org/base-app/agents/x402-agents) | Coinbase L2 with native x402 agent support + documentation | Production, low-fee |
| [Solana Pay](https://solanapay.com/) | Payment protocol on Solana, compatible with x402 | Production, sub-second |

---

## V. Layer 3: Protocol Endpoints (Beacons and Discovery)

### What It Does
This is how agents find your app, understand what it offers, and decide whether to transact. This is your AEO surface — the structured endpoints that make you discoverable.

### Ship Today: The Discovery Stack

Your first app needs FOUR discovery endpoints. Together, they form what Paul called the "contextualized directory/forum/messaging center — coffee shops and monitoring stations."

**Endpoint 1: `/.well-known/mcp/servers.json`**

This is MCP discovery. When an agent (or an orchestrator like Claude, Codex, etc.) looks for tools on your domain, this is what they check first.

```json
{
  "servers": [
    {
      "name": "good-vibes-content",
      "url": "https://api.goodvibes.app/mcp",
      "version": "0.1.0",
      "description": "Streaming content discovery and session composition",
      "auth": { "type": "x402", "scope": ["read", "compose"] },
      "tags": ["streaming", "wellness", "content-discovery", "sessions"]
    }
  ]
}
```

Any agent that checks your `.well-known` endpoint knows instantly: what you offer, how to connect, how to pay, and what capabilities you expose.

**Endpoint 2: `/.well-known/governance.json`**

This is your governance protocol — the declaration of intent that agents evaluate before transacting. This is the Web 4.0 native discovery surface.

```json
{
  "governance_version": "0.1.0",
  "provider": {
    "name": "Good Vibes",
    "identity": "npub1abc...",
    "type": "content_platform",
    "domain": "goodvibes.app"
  },
  "capabilities": {
    "content_discovery": true,
    "session_composition": true,
    "personalization": "agent-driven",
    "enrichment_dimensions": ["mood", "energy", "genre", "therapeutic_intent"]
  },
  "economics": {
    "payment_rails": ["x402", "stripe"],
    "pricing_model": "per-session",
    "price_range": { "min": 0, "max": 5.00, "currency": "USD" },
    "free_tier": true
  },
  "trust_signals": {
    "data_retention": "session_only",
    "content_moderation": "governance_driven",
    "dark_patterns": "none",
    "user_data_export": "always_available"
  },
  "contact": {
    "agent_handshake": "https://api.goodvibes.app/handshake",
    "human_support": "support@goodvibes.app"
  }
}
```

**Endpoint 3: `/AGENTS.md`**

Adopted by 60,000+ open-source projects. Claude, Codex, Copilot, Cursor, and Gemini CLI all read this file. It tells coding agents how to interact with your system.

```markdown
# AGENTS.md — Good Vibes

## Overview
Good Vibes is a wellness streaming platform built on Web 4.0 governance protocols.

## Agent Integration
- MCP server: `https://api.goodvibes.app/mcp`
- Governance protocol: `https://goodvibes.app/.well-known/governance.json`
- Payment: x402 (USDC on Base/Solana) or Stripe Connect

## Available Tools
- `discover_content(mood, energy, genre)` — Find content matching criteria
- `compose_session(duration, intent, preferences)` — Build a personalized session
- `get_governance()` — Retrieve current governance protocol
- `handshake(consumer_agent_id, intent)` — Initiate agent-to-agent negotiation

## Data Sharing
In the spirit of giving — have our data too! Rate-limited API access to enrichment metadata is free. Respect the rate limits or we'll have to block you (you don't want to see that side of us!).
```

**Endpoint 4: Nostr Events (Relay-Based Discovery)**

Publish your governance protocol and key content as Nostr events. This makes you discoverable through decentralized relays, independent of your domain.

```json
{
  "kind": 30078,
  "tags": [
    ["d", "governance-protocol"],
    ["t", "web4"],
    ["t", "streaming"],
    ["t", "wellness"],
    ["p", "npub1abc..."]
  ],
  "content": "{...governance.json contents...}"
}
```

Agents scanning Nostr relays for `["t", "web4"]` tagged events will find your governance protocol. Zero cost to publish. Decentralized discovery.

### The "Coffee Shop" — Agent Handshake Endpoint

Paul asked for a "coffee shop" — a neutral ground where agents meet. Your handshake endpoint IS this:

```
POST /handshake
{
  "from": { "agent_id": "npub1consumer...", "type": "consumer" },
  "intent": { "category": "wellness_streaming", "specifics": { "mood": "calm", "duration": "30min" } },
  "payment_preference": "x402"
}

RESPONSE:
{
  "status": "match",
  "governance": "https://goodvibes.app/.well-known/governance.json",
  "offer": {
    "session": { "content_count": 5, "duration": "32min", "mood_match": 0.92 },
    "price": 1.50,
    "payment": { "rail": "x402", "address": "0xabc...", "chain": "base" }
  }
}
```

### The "Monitoring Station" — Open Data Feed

Paul's idea: "In the spirit of giving — have my data too!" Expose an open API that shares enrichment metadata, anonymized traffic patterns, and content signals. Rate-limited. Free. Anyone can consume it.

```
GET /open/signals
{
  "period": "last_24h",
  "top_categories": ["meditation", "breathwork", "motivation"],
  "top_moods": ["calm", "energized", "reflective"],
  "active_sessions": 247,
  "new_content_items": 12,
  "agent_traffic_ratio": 0.34
}
```

This is the "monitoring station" — coalition members and external agents alike can see what's trending, what consumers want, and how the ecosystem is behaving. Radical transparency as competitive advantage.

---

## VI. Layer 4: Enrichment

### What It Does
Raw content (a YouTube video, a podcast, a book, a song) becomes SMART content through enrichment — LLM-powered metadata tagging that adds dimensions no human could tag at scale.

### Ship Today: The Enrichment Pipeline

This is the shared infrastructure from the Tsunami Roadmap. One pipeline serves ALL products.

```
RAW CONTENT → INGEST → ENRICH → STORE → SERVE
                │         │         │        │
                ▼         ▼         ▼        ▼
           Metadata   LLM tags   Vector   SEP endpoint
           extraction  (mood,    store    + governance
           (title,     energy,   (for     protocol
           duration,   genre,    semantic  query
           creator)    intent,   search)
                       therapeutic
                       value,
                       audience)
```

**Enrichment dimensions (starting set):**

| Dimension | Type | Example Values |
|-----------|------|----------------|
| `mood` | categorical | calm, energized, reflective, joyful, intense |
| `energy_level` | 1-10 scale | 3 (low), 7 (high) |
| `genre` | categorical | meditation, workout, documentary, comedy |
| `therapeutic_intent` | categorical | anxiety_relief, motivation, focus, recovery |
| `audience_fit` | tags | adults, teens, families, professionals |
| `session_position` | categorical | opener, deep_dive, cooldown, transition |
| `content_quality` | 1-5 scale | Based on production value, depth, clarity |
| `creator_sovereignty` | boolean | Does the creator control distribution? |

**Tools:**

| Tool | Use | Cost |
|------|-----|------|
| **Claude Haiku** | Bulk enrichment tagging (cheap, fast, good enough for most dimensions) | ~$0.25/M input tokens |
| **Claude Sonnet** | Complex enrichment (therapeutic intent, nuanced mood analysis) | ~$3/M input tokens |
| **Whisper** (OpenAI) | Audio transcription for podcasts/video → then LLM enrichment on transcript | ~$0.006/minute |
| **Embeddings** (voyage-3, text-embedding-3) | Vector representations for semantic search | ~$0.02/M tokens |
| **Haystack** (deepset) | Open-source RAG framework with metadata enrichment pipeline support | Free |

**Cost per content item:** ~$0.01-0.05 for basic enrichment (mood, energy, genre). ~$0.10-0.25 for deep enrichment (therapeutic intent, session positioning, quality scoring). At 10,000 items: $100-2,500 total.

### Ship Right (Later)

Real-time enrichment where the agent enriches content on-the-fly during session composition. The stored enrichment is the starting point; the agent refines it based on the specific consumer's context.

---

## VII. Layer 5: Experience

### What It Does
The human-facing interface. What people actually see and interact with.

### Ship Today: Progressive Web App (PWA) with Governance Hooks

Don't wait for full agentic rendering. Ship a PWA that USES governance protocols internally but presents a traditional UI to humans.

```
OPTION A: Traditional PWA (Ship this week)
┌──────────────────────────────────────┐
│  Standard React/Next.js frontend     │
│  Reads governance protocol for       │
│  content rules and session logic     │
│  Serves enriched content via API     │
│  Payment via Stripe Connect          │
│  Agent endpoint available but        │
│  human UI is primary                 │
└──────────────────────────────────────┘

OPTION B: Hybrid (Ship in 30 days)
┌──────────────────────────────────────┐
│  PWA with agent enhancement          │
│  Service worker pre-caches           │
│  governance protocol                 │
│  Agent can compose sessions          │
│  Human can browse traditionally      │
│  Both paths serve the same content   │
│  x402 endpoint live for agent rail   │
└──────────────────────────────────────┘

OPTION C: Full Agentic Rendering (Ship in 90 days)
┌──────────────────────────────────────┐
│  Agent generates UI from governance  │
│  protocol + enrichment metadata      │
│  Service worker as agent presence    │
│  Tiered model routing                │
│  (cache → Haiku → Sonnet → Opus)    │
│  No static frontend code             │
│  x402 primary payment rail           │
└──────────────────────────────────────┘
```

**Recommendation:** Ship Option A this week with the governance.json and MCP endpoints live from day one. Agents can already discover and interact with your service. Humans get a great PWA. Migrate to Option B as the agent rail grows. Option C is the destination but NOT the starting point.

---

## VIII. The Agentic Progression Within Your First App

Paul described the concurrent scaling:

```
AGENTIC ENGINEERING          AGENTIC RENDERING          AGENTIC EXECUTION
(pump design +               (cookbooks/recipes)        (pure protocol)
 greenspaces as
 components/portals/
 data services)

[████████████████]           [████░░░░░░░░░░░░]        [██░░░░░░░░░░░░░░]
      NOW                        BUILDING                  EMERGING
         │                          │                         │
         │                          │                         │
         ▼                          ▼                         ▼
  Build the app fast          Write governance          Agent-to-agent
  using AI tools.             protocols that             transactions
  Greenspaces =               agents can read            happening
  reusable components         and render from.           without any UI.
  that other Coalition        "Cookbooks" =              Pure intent →
  members can plug in.        recipes for agents         outcome.
                              to generate UIs.
```

All three happen concurrently in your first app. The governance protocol IS the cookbook. The PWA is the engineering output. The x402 + handshake endpoint is the beginning of pure execution. You don't choose one — you ship all three at different maturity levels.

---

## IX. What's Missing — The Gaps

After reviewing everything in the repo and the watchlist, here are the genuine gaps between "architecture papers" and "shipping product":

### Gap 1: Agent Runtime

You need something that actually RUNS consumer agents. Today, that means:
- **MCP server** on your backend (agents connect to your tools)
- **Recommendation:** Start with Claude as the agent runtime via API. Consumer "picks an agent" = picks which LLM powers their experience. Haiku for routine (free tier), Sonnet for personalized sessions (paid tier).
- **Watch:** AAIF's Goose project — open-source agent runtime that could become the standard consumer agent.

### Gap 2: Session Composition Engine

The enrichment pipeline tags content. But something needs to COMPOSE sessions — selecting and ordering content into a coherent arc (opener → deep dive → cooldown). This is the "cookbook interpreter."

**Build this:** A session composition service that takes:
- Consumer preferences (mood, energy, duration)
- Enriched content catalog
- Governance protocol rules (no dark patterns, cognitive flourishing)

And outputs:
- An ordered list of content items
- Transition metadata between items
- Estimated session arc (energy curve over time)

This is a relatively small service — LLM call with structured output. But it's the magic that makes the experience feel curated rather than random.

### Gap 3: Greenspace Component Library

Paul mentioned "greenspaces as components/portals/data services." This needs to be concrete: a library of reusable components that any Coalition member can plug into their app.

**Minimum viable greenspaces:**
- **Auth component** — Nostr keypair generation + management
- **Payment component** — Stripe Connect + x402 dual-rail widget
- **Governance reader** — Component that fetches and displays governance protocol
- **Content card** — Enriched content display with mood/energy badges
- **Session player** — Plays a composed session with transitions
- **Agent chat** — Interface for human ↔ agent communication

Ship these as a package. Every Coalition member gets them. Every new app built on them strengthens the standard.

### Gap 4: Convergent Syndication Tooling

The reverse syndication crawler (from the Tsunami Roadmap) needs to be a real tool:
- Scan platforms (YouTube, TikTok, SoundCloud) for content matching criteria
- Score content on quality, engagement ratio, alignment
- Auto-enrich metadata through the pipeline
- Flag top candidates for human outreach
- Track creator relationships (contacted → negotiating → signed → active)

This is the "Saunter AI" concept Paul described — agentic reverse syndication of systems. See [SAUNTER-AI.md](./SAUNTER-AI.md).

---

## X. The Schelling Point

Paul asked: "What's the Schelling point — the thing that just fits?"

The Schelling point for the first Web 4.0 app is the combination of three things that no Web 2.0 app can replicate:

1. **Governance protocol that agents can read** — not just an API, but a declaration of intent, values, and guarantees that an agent evaluates before recommending the service to its human.

2. **x402 payment rail** — agents can pay for content programmatically, at micropayment scale, without human intervention. This enables the "agent handles my morning routine" use case that no Stripe-only app can serve.

3. **Open enrichment data** — the monitoring station / open signals feed. This is the radical generosity move that makes the app magnetic to other agents and Coalition members. "Here's our data. Have it. Build something with it."

These three together are the minimum viable Web 4.0 differentiator. A PWA with good content is Web 2.0. A PWA with governance + x402 + open data is Web 4.0. That's the Schelling point.

---

## XI. First Week Checklist

Regardless of which product you choose, here's what ships in Week 1:

- [ ] Nostr keypair generation on user signup
- [ ] `/.well-known/governance.json` published
- [ ] `/.well-known/mcp/servers.json` published
- [ ] `/AGENTS.md` published
- [ ] Stripe Connect for producer payments
- [ ] x402 middleware on at least ONE API endpoint (content access)
- [ ] Enrichment pipeline running on first batch of content (even 100 items)
- [ ] `/handshake` endpoint accepting agent connections
- [ ] `/open/signals` endpoint sharing anonymized traffic data
- [ ] PWA (Option A) live and serving content to humans

That's the minimum viable Web 4.0 app. Everything else (full agentic rendering, Nostr relay publication, session composition engine, greenspace component library) builds on top of this foundation.

---

## Related Documents

- [Product Portfolio](./PRODUCT-PORTFOLIO.md) — Which product to build
- [Tsunami Roadmap](./TSUNAMI-ROADMAP.md) — The phased strategy
- [AEO Strategy](./AEO-STRATEGY.md) — How agents discover you
- [Agent Communication](./AGENT-COMMUNICATION.md) — How the handshake works
- [Coalition](./COALITION.md) — Who gets the greenspace components
- [Saunter AI](./SAUNTER-AI.md) — Agentic reverse syndication tooling
- [WEB4 Economics](./WEB4-ECONOMICS.md) — Payment infrastructure details

## Sources: Infrastructure Research

- [x402 Protocol](https://www.x402.org/) — HTTP-native payment standard
- [x402 on Solana](https://solana.com/x402/what-is-x402) — Chain integration details
- [Base L2 x402 Agents](https://docs.base.org/base-app/agents/x402-agents) — Agent payment documentation
- [MCP Architecture](https://modelcontextprotocol.io/docs/learn/architecture) — Model Context Protocol
- [Soniclinker MCP Discovery](https://www.soniclinker.com/blog/how-llms-discover-model-context-protocol-mcp) — `.well-known` discovery patterns
- [AGENTS.md](https://agents.md/) — Agent instruction specification
- [AAIF Announcement](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) — Agentic AI Foundation
- [Haystack Metadata Enrichment](https://haystack.deepset.ai/cookbook/metadata_enrichment) — Open-source enrichment pipeline
