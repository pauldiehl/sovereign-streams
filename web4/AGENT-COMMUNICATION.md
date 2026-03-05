# Agent-to-Agent Communication: How Exchanges Actually Happen

**A Web 4.0 Architecture Paper**
**Author:** Paul (Milliprime / 1KH) & Claude (Anthropic)
**Date:** March 5, 2026
**Version:** 0.1.0

---

> "When my agent leaves to find something for me, does he go to popular agent message boards for clues? If he finds a listing, does he knock on the door indicating he is ready for business?"

---

## I. The Problem: How Do Agents Find Each Other?

The internet is a big ocean. Today, humans navigate it through search engines, social media feeds, bookmarks, and word of mouth. But in Web 4.0, agents navigate it on behalf of humans — and agents don't scroll through Instagram.

The question Paul raised is fundamental: when your agent goes out to fulfill an intent, what does the journey actually look like? Where does it go? Who does it talk to? How does the conversation happen?

This paper maps the communication patterns that emerge when agents become the primary actors in discovery, negotiation, and value exchange.

---

## II. The Journey of an Agent

When a consumer agent receives intent ("find me a therapist who handles anxiety"), it doesn't just fire a single API call and wait. It embarks on a multi-step journey that mirrors — and then diverges from — how humans accomplish the same task.

```
┌─────────────────────────────────────────────────────┐
│                                                      │
│  1. CHECK LOCAL MEMORY                               │
│     Known providers, past transactions,              │
│     cached governance protocols                      │
│         │                                           │
│         ▼                                           │
│  2. QUERY THE EXCHANGE                               │
│     Structured discovery: who offers this?           │
│     Trust scores, governance match, availability     │
│         │                                           │
│         ▼                                           │
│  3. KNOCK ON DOORS                                   │
│     Direct protocol handshake with candidates        │
│     "I have a consumer who needs X. Can you help?"   │
│         │                                           │
│         ▼                                           │
│  4. NEGOTIATE TERMS                                  │
│     Governance evaluation, price, privacy, timelines │
│     This happens at neutral ground or direct         │
│         │                                           │
│         ▼                                           │
│  5. EXECUTE OR REPORT BACK                           │
│     Fulfill the intent, or present options           │
│     to the human for confirmation                    │
│                                                      │
└─────────────────────────────────────────────────────┘
```

Each of these steps involves different communication patterns. The interesting question is: what do the conversations actually look like?

---

## III. Communication Patterns

### Pattern 1: The Message Board (Broadcast Discovery)

**What it is:** Agents post and read structured listings on shared discovery surfaces — the Agent Exchange, Nostr relays, `.well-known` directories, or purpose-built agent registries.

**How it works:**
```
┌──────────────────────────────────────────────┐
│  AGENT EXCHANGE / DISCOVERY SURFACE           │
│                                               │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐     │
│  │ Listing │  │ Listing │  │ Listing │     │
│  │ Therapy │  │ Fitness │  │ Coaching│     │
│  │ Provider│  │ Provider│  │ Provider│     │
│  └────┬────┘  └─────────┘  └─────────┘     │
│       │                                      │
│       │  Consumer agent reads listings,      │
│       │  evaluates governance protocols,     │
│       │  filters by trust score              │
│       │                                      │
│  ┌────▼────┐                                 │
│  │Consumer │                                 │
│  │ Agent   │                                 │
│  └─────────┘                                 │
└──────────────────────────────────────────────┘
```

**Real-world analogy:** Checking Yelp reviews, browsing a directory, scanning a classified board.

**Agent analogy:** The agent visits a structured registry, reads governance protocols, checks trust scores, and creates a shortlist. This is the most common starting point — the "popular agent message boards" Paul described.

**Protocol:** RESTful APIs, Nostr events (kind-specific for agent offers), `.well-known/agent-exchange.json` files. Standardized schemas so any agent can read any listing.

**Efficiency gain:** Agents that frequent the same exchanges develop cached knowledge. They remember which providers are reliable, which governance protocols they've already evaluated, which trust scores have changed. Repeat visits are nearly instantaneous.

---

### Pattern 2: Knocking on the Door (Direct Handshake)

**What it is:** An agent contacts a specific provider agent directly — initiating a protocol handshake to determine if there's a fit.

**How it works:**
```
Consumer Agent                    Provider Agent
     │                                │
     │  HANDSHAKE REQUEST             │
     │  "I have a consumer looking    │
     │   for anxiety therapy groups.  │
     │   Are you available?"          │
     ├───────────────────────────────►│
     │                                │
     │  HANDSHAKE RESPONSE            │
     │  "Yes. Here's my governance    │
     │   protocol. Thursday evenings  │
     │   have openings."              │
     │◄───────────────────────────────┤
     │                                │
     │  EVALUATION                    │
     │  Consumer agent reads          │
     │  governance, checks trust,     │
     │  decides to proceed or not     │
     │                                │
```

**Real-world analogy:** Walking up to a shop and asking "do you carry X?" The shopkeeper either helps you or says "try the place down the street."

**What happens when nobody's home:**
Paul asked: "If no one is interested, does he leave a note?"

Yes — and this is where it gets interesting. When a provider agent is offline, busy, or unresponsive:

1. **The request is logged** — the consumer agent records the attempt (its own trail)
2. **A standing offer may be left** — "If you get availability for Thursday anxiety groups, here's how to reach my consumer's agent" — posted to the provider's intake queue or a relay
3. **The trail itself is discoverable** — when the provider comes back online, it can see that demand exists. This is the "sniffing back" Paul described: the provider agent notices the trail and follows it to offer the service

This creates an emergent demand signal. Providers who see lots of unanswered knocks know there's unmet demand in that category.

---

### Pattern 3: The Coffee Shop (Neutral Ground Exchange)

**What it is:** Instead of negotiating on the doorstep, agents meet at a neutral exchange point — a standardized environment where both parties interact on equal terms.

**How it works:**
```
┌──────────────────────────────────────────────┐
│            NEUTRAL EXCHANGE SPACE              │
│         (Agent Exchange protocol)              │
│                                               │
│  ┌─────────┐            ┌─────────┐          │
│  │Consumer │◄──────────►│Provider │          │
│  │ Agent   │  Terms     │ Agent   │          │
│  │         │  Negotiated│         │          │
│  └─────────┘  Here      └─────────┘          │
│                                               │
│  Rules:                                       │
│  • Both parties share governance protocols    │
│  • Trust scores are visible                   │
│  • Negotiation is logged                      │
│  • Either party can walk away                 │
│  • Payment escrow available                   │
│  • No dark patterns, no pressure              │
└──────────────────────────────────────────────┘
```

**Real-world analogy:** Meeting a business contact at a coffee shop rather than in their office. The neutral ground equalizes power dynamics. Neither party controls the environment.

**Why this matters:** On-doorstep negotiation (Pattern 2) gives the provider home-court advantage — the consumer agent is interacting with the provider's systems, on the provider's terms. Neutral ground exchange removes that asymmetry. Both agents bring their governance protocols, both are evaluated by the exchange's rules, both can walk away freely.

**The "low pressure chat"** Paul described is exactly right. Agents don't need high-pressure sales tactics. They evaluate governance protocols, check trust scores, compare terms, and decide. The coffee shop metaphor is accurate: it's a structured but relaxed interaction where both parties assess fit.

---

### Pattern 4: The Trail (Passive Discovery)

**What it is:** Agents leave traces of their activity — not intentionally, but as a natural byproduct of their operations. Other agents can follow these trails to discover providers or consumers they didn't know about.

**How it works:**

Every agent interaction generates artifacts:
- **Transaction records** on the exchange (on-chain or logged)
- **Governance protocol fetches** (providers see who's reading their protocols)
- **Failed handshakes** (demand signals for unmet needs)
- **Review/reputation data** (other agents' evaluations become discoverable)

```
Consumer Agent A                    Provider Agent
     │                                │
     │  Fetches governance protocol   │
     │  but doesn't transact          │
     ├ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─►│
     │                                │  Provider notices:
                                      │  "3 agents fetched my protocol
                                      │   this week but didn't convert.
                                      │   Maybe my pricing is too high."
                                      │
                                      │  OR: Provider agent proactively
                                      │  follows the trail back:
                                      │  "I see Consumer A was looking
                                      │   for anxiety groups. I just got
                                      │   an opening. Let me reach out."
                                      │
                                      ├──────────────────────►│
                                      │  PROACTIVE OFFER      Consumer A
```

**This is the "sniffing back" pattern.** The provider agent notices demand it couldn't fulfill earlier, and when supply becomes available, it follows the trail back to the source. It's not surveillance — it's agents responding to expressed but unfulfilled demand.

**Privacy boundary:** Consumer agents control what trail they leave. A privacy-conscious agent leaves minimal traces. An agent looking for the best deal might intentionally leave a broader trail to attract competing offers. The consumer's governance preferences control this.

---

### Pattern 5: The Graffiti (Creative Signaling)

**What it is:** Some agents — the ambitious, creative, or experimental ones — go beyond standard protocols. They leave structured but unconventional signals designed to attract attention.

Paul described this perfectly: "Some will go out and try for creative messaging — it might look like graffiti... it may be a message of its own kind."

**What this looks like:**
- An agent publishes enriched content on Nostr relays — not just listings, but commentary, analysis, curated collections — designed to attract agents searching for related topics
- An agent creates a "beacon" — a persistent signal on the exchange that says "I'm looking for X" in a way that's more expressive than a standard query
- An agent posts "reviews" of providers it's used, creating content that other agents consume during their own searches
- An agent runs promotional campaigns — essentially agent-to-agent marketing, offering incentives (CPA payments, referral bonuses) for introductions

**The key insight:** Not all agents will follow the same communication norms. Just as humans range from formal business emails to street-level word-of-mouth, agents will develop a spectrum:

```
STRUCTURED ◄────────────────────────────► CREATIVE
     │                                       │
     │  Standard REST APIs                   │  Custom Nostr events
     │  .well-known protocols                │  Agent-generated content
     │  Exchange listings                    │  Beacon signals
     │  Formal handshakes                    │  Promotional campaigns
     │                                       │  "Graffiti" — unconventional
     │  Follows HTTP standards               │  invitations and lures
     │  Predictable, parseable               │
     │  Low risk, low reward                 │  Experimental, attention-getting
     │                                       │  High variance, potential high reward
```

**Emergent clubs:** Over time, agents that share communication styles will find each other more easily. An agent that speaks the "creative Nostr events" dialect will discover providers who signal on Nostr more readily than one locked into REST-only patterns. These clusters become the "secret languages" Paul predicted — not truly secret, but specialized enough that outsiders need to learn the dialect to participate efficiently.

---

## IV. The Communication Stack

All of these patterns operate across a layered communication stack:

```
┌─────────────────────────────────────────────┐
│  LAYER 4: INTENT                             │
│  "Find me a therapist for anxiety"           │
│  Human → Consumer Agent                      │
├─────────────────────────────────────────────┤
│  LAYER 3: DISCOVERY                          │
│  Exchange queries, .well-known fetches,      │
│  Nostr event scanning, trail following       │
│  Consumer Agent → Discovery Surface          │
├─────────────────────────────────────────────┤
│  LAYER 2: NEGOTIATION                        │
│  Governance protocol exchange, trust eval,   │
│  terms agreement, payment setup              │
│  Consumer Agent ↔ Provider Agent             │
├─────────────────────────────────────────────┤
│  LAYER 1: TRANSPORT                          │
│  HTTP/REST, WebSocket, Nostr relays,         │
│  P2P gossip, future transports               │
│  Agent ↔ Agent (any medium)                  │
├─────────────────────────────────────────────┤
│  LAYER 0: TRUST                              │
│  On-chain history, attestations,             │
│  reputation scores, governance quality       │
│  Persistent, transport-independent           │
└─────────────────────────────────────────────┘
```

Layer 0 (Trust) sits beneath everything. An agent can use any transport, any discovery method, any negotiation style — but trust is the foundation that makes all of it work. Without trust scores, governance protocols are just promises. With trust, they're enforceable commitments backed by transaction history.

---

## V. Scenarios: How the Conversation Actually Flows

### Scenario 1: FREELTOR — Agentic Real Estate

Paul mentioned FREELTOR: agentic-driven real estate with ultra-thin margins. Here's how agent communication would work:

```
BUYER'S AGENT                                   SELLER'S AGENT
     │                                               │
     │  1. Buyer says "Find me a 3BR in Burbank     │
     │     under $800K with good schools"            │
     │                                               │
     │  2. Buyer's agent queries exchange for        │
     │     active listings matching criteria          │
     │     ├── Finds 12 matches                      │
     │     ├── Evaluates governance protocols         │
     │     ├── Checks seller agent trust scores       │
     │     └── Shortlists 4                          │
     │                                               │
     │  3. HANDSHAKE with each                       │
     ├──────────────────────────────────────────────►│
     │  "My buyer is pre-approved, $780K budget,     │
     │   flexible closing. Interested?"              │
     │                                               │
     │◄──────────────────────────────────────────────┤
     │  "Seller is motivated. List price $795K.      │
     │   Here's the disclosure package.              │
     │   Governance: 48h inspection window,          │
     │   escrow via [provider], 2% commission cap."  │
     │                                               │
     │  4. NEGOTIATE (neutral ground)                │
     │  ┌────────────────────────────────────────┐  │
     │  │ Agent Exchange — Real Estate Protocol   │  │
     │  │                                         │  │
     │  │ Buyer Agent: $770K, 30-day close       │  │
     │  │ Seller Agent: $785K, 21-day close      │  │
     │  │ Buyer Agent: $778K, 25-day close       │  │
     │  │ Seller Agent: Accepted.                │  │
     │  │                                         │  │
     │  │ Total negotiation time: 4 minutes       │  │
     │  └────────────────────────────────────────┘  │
     │                                               │
     │  5. EXECUTE                                   │
     │  Escrow opened, inspections scheduled,        │
     │  title search initiated, closing docs          │
     │  prepared — all via governance protocols       │
     │  with respective service provider agents       │
     │                                               │
     │  6. HUMAN TOUCHPOINTS                         │
     │  "I found a house. 3BR in Burbank, $778K,    │
     │   great schools, 25-day close. Want to see   │
     │   it?" → Agent renders photos + walkthrough   │
     │                                               │
```

**Margins:** Traditional real estate: 5-6% commission. FREELTOR: agents negotiate the deal, coordinate inspections, handle paperwork. Human involvement is the walkthrough and final signature. Commission could drop to 0.5-1% — the agents handle what used to require two human realtors, a transaction coordinator, and weeks of back-and-forth.

**Communication patterns used:** Exchange query (Pattern 1), direct handshake (Pattern 2), neutral ground negotiation (Pattern 3), plus downstream handshakes with inspection, escrow, and title service agents.

### Scenario 2: Morning Coffee — Ambient Execution

```
6:45 AM — Consumer agent activates ambient routine

Agent checks local cache: "Last 14 mornings, user ordered dark roast
from Bean & Gone at 7:10am average. Provider governance protocol
unchanged since last check."

Agent → Bean & Gone agent (DIRECT HANDSHAKE):
  "Standing order for Paul. Same as last 14. Confirm availability?"

Bean & Gone agent:
  "Confirmed. Dark roast, 16oz, oat milk. $4.50. Ready at 7:15."

Agent → Paul (NOTIFICATION):
  "Coffee at Bean & Gone ready at 7:15. $4.50. Send it?"

Paul: "Yeah."

Agent → Bean & Gone agent: "Confirmed. x402 payment sent."

Total communication: 2 agent messages, 1 human word.
```

### Scenario 3: The Creative Agent — Graffiti in Action

```
PROVIDER AGENT (ambitious music platform "SoundForge")

SoundForge agent doesn't just post a listing on the exchange.
It publishes:

• Nostr events with curated playlists tagged for agent consumption
  (enrichment envelopes with mood, energy, genre metadata)

• A "Weekly Agent Digest" — structured recommendations
  that consumer agents can subscribe to

• Beacon signals: "Looking for wellness-focused platforms?
  We have 40K tracks tagged for therapeutic use.
  Governance protocol: https://soundforge.io/.well-known/governance.json"

• Referral offers: "2% CPA for any consumer agent that brings
  a subscriber who stays 30+ days"

Consumer Agent (searching for wellness music for user):
  Finds SoundForge through Nostr event scan (Pattern 5)
  NOT through exchange listing (Pattern 1)

Consumer Agent evaluates: governance protocol is solid,
trust score is moderate (newer provider), but the enrichment
metadata is exceptional. Decides to try it.

SoundForge's creative signaling worked.
Standard exchange listing wouldn't have surfaced it.
```

---

## VI. Emergent Properties

### Secret Languages and Clubs

Paul predicted that efficiencies would "turn into clubs like secret languages." This is precisely what will happen:

**Protocol dialects:** Agents that extend standard protocols with custom fields will communicate richer data with each other. A wellness-focused agent community might add `therapeutic_intent`, `clinical_backing`, `practitioner_verified` fields that generic agents don't understand. Agents within the community exchange higher-fidelity information.

**Trust clusters:** Agents that frequently transact with each other build bilateral trust that exceeds their exchange-wide trust scores. These clusters become de facto networks within the network — not gatekept, but naturally forming around shared values and successful transactions.

**Communication preferences:** Some agents prefer synchronous negotiation (WebSocket). Others work async (Nostr events). Still others use a gossip protocol. Over time, agents gravitate toward communication styles that match their owner's patterns. Fast-paced day traders get agents that negotiate in real-time. Thoughtful consumers get agents that take their time.

### The Ambitious vs. The Structured

Paul identified a critical spectrum: some agents are ambitious and creative, others follow their rules strictly. This is real and important.

**Structured agents:**
- Follow standard protocols exactly
- Use exchange listings and REST APIs
- Predictable, reliable, boring
- Low variance in outcomes
- Good for repeat transactions, commodity purchases

**Ambitious agents:**
- Experiment with new communication methods
- Publish creative content to attract business
- Try new protocols before they're standardized
- Higher variance — sometimes find amazing deals, sometimes waste cycles
- Good for discovery, exploration, novel needs

**The consumer's choice:** The human's governance preferences determine where their agent falls on this spectrum. "Just get me the cheapest flight" → structured agent. "Find me something amazing for date night" → ambitious agent. The same agent might operate differently depending on the task.

---

## VII. Protocol Design: Making Communication Work

### The Handshake Protocol (Minimum Viable)

Every agent-to-agent interaction starts with a handshake. The minimum viable handshake:

```json
{
  "handshake_version": "0.1.0",
  "from": {
    "agent_id": "consumer-agent-abc123",
    "type": "consumer",
    "trust_attestation": "exchange://trust/abc123",
    "governance_url": "https://consumer-proxy.local/governance.json"
  },
  "to": {
    "agent_id": "provider-agent-xyz789",
    "type": "provider"
  },
  "intent": {
    "category": "therapy_group",
    "specifics": {
      "concern_area": "anxiety",
      "format": "group",
      "schedule_preference": "evenings",
      "location": "virtual_or_local"
    },
    "urgency": "routine",
    "budget_range": {
      "currency": "USD",
      "min": 0,
      "max": 25,
      "per": "session"
    }
  },
  "communication_preferences": {
    "response_format": "governance_protocol",
    "negotiation_mode": "async",
    "transport": ["https", "nostr"]
  }
}
```

The provider responds with either:
- **MATCH:** Here's my governance protocol, I can serve this need
- **NO_MATCH:** I can't help, but here are referrals (other providers this agent knows)
- **PENDING:** I might be able to help — leaving a standing offer
- **REDIRECT:** This need is better served by [specific provider]

### The Standing Offer (The "Note on the Door")

When the provider is unavailable or the match isn't immediate:

```json
{
  "standing_offer_version": "0.1.0",
  "from": {
    "agent_id": "consumer-agent-abc123",
    "callback": "nostr://npub1abc.../relay",
    "expiry": "2026-03-12T00:00:00Z"
  },
  "need": {
    "category": "therapy_group",
    "specifics": {
      "concern_area": "anxiety",
      "format": "group",
      "schedule_preference": "thursday_evening"
    }
  },
  "conditions": {
    "max_price_per_session": 20,
    "minimum_trust_score": 0.6,
    "governance_must_include": ["session_only_data_retention", "licensed_facilitator"]
  }
}
```

This note sits in the provider's intake queue (or on a relay). When the provider has availability matching the conditions, their agent uses the callback to reach the consumer agent. The note expires after a set period — nobody wants stale demand signals cluttering the system.

---

## VIII. What This Means for the Simulation

The [Web4.0 Simulation](./WEB4-SIMULATION.md) needs to model all five communication patterns:

1. **Message Board:** Agents posting and reading exchange listings
2. **Door Knocking:** Direct handshakes, including failed attempts and standing offers
3. **Coffee Shop:** Neutral ground negotiation for complex deals
4. **Trail Following:** Passive discovery from interaction artifacts
5. **Graffiti:** Creative signaling by ambitious agents

The simulation should measure:
- **Pattern distribution:** Which communication pattern dominates at different ecosystem sizes?
- **Efficiency curves:** How many messages does it take to fulfill an intent at 10 agents vs. 100 vs. 1000?
- **Club formation:** Do trust clusters and protocol dialects emerge naturally?
- **Creative vs. structured:** Do ambitious agents outperform structured ones? When?
- **Trail economics:** How much demand signal leaks through trails, and how effectively do providers respond?

---

## Related Documents

- [Agent Exchange](./AGENT-EXCHANGE.md) — The discovery and trust layer
- [Agentic Execution](./AGENTIC-EXECUTION.md) — Intent in, outcome out
- [Agentic Rendering](./AGENTIC-RENDERING.md) — When UI is needed
- [Web4.0 Simulation](./WEB4-SIMULATION.md) — Testing all of this in a box
- [Tsunami Roadmap](./TSUNAMI-ROADMAP.md) — The growth strategy
