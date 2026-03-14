# Protocol Maturity: The Strangler Pattern for Agentic Systems

**From Expensive Intelligence to Cheap Certainty**
**Author:** Paul (Milliprime / 1KH) & Claude (Anthropic)
**Date:** March 14, 2026
**Version:** 0.1.0

---

> "Today I'm building AGENT-FIRST apps to UNDERSTAND what drives customers. Then as we get more MATURE on an offering, we go more DETERMINISTIC to cut costs as we scale."

---

## I. The Problem: Agentic Costs Don't Scale

Every conversation with an LLM costs money. The Agent Layer that makes Forkless magical — the opinionated, adaptive, conversation-first experience — is also the most expensive part of the system. A single rich agent conversation might cost $0.10–$0.50 in API tokens. Multiply by thousands of users and the math gets uncomfortable fast.

This is exactly what Perplexity discovered when their CTO Denis Yarats announced in March 2026 that they were moving away from MCP toward direct APIs and CLIs internally. The reasons were specific: MCP tool definitions consume context window tokens, and every tool schema, parameter description, and response format eats into the model's working memory. For agents making many tool calls across long conversations, the overhead compounds. Authentication was the other pain point — each MCP server handling its own auth flow creates friction at scale.

But Perplexity didn't say protocols are useless. They said MCP v1 is too expensive for *known* patterns. This is a crucial distinction: the problem isn't intelligence, it's applying intelligence where certainty already exists.

The real question isn't "MCP or no MCP?" The real question is: **when should a system think, and when should it just know?**

---

## II. The Three Tiers of Protocol Interaction

Every interaction between agents, between agents and services, or between agents and users falls into one of three tiers. The tiers map to cost, intelligence, and maturity.

```
┌────────────────────────────────────────────────────────────────────┐
│                                                                    │
│  TIER 1: STATIC                                                    │
│  ────────────────                                                  │
│  Cost: Zero (just serving JSON)                                    │
│  Intelligence: None                                                │
│  Example: .well-known/governance.json                              │
│                                                                    │
│  These are published documents. No computation. No negotiation.    │
│  A governance protocol sitting at a URL. A haves.json declaring    │
│  capabilities. Static files served by any CDN or S3 bucket.        │
│  Cost at scale: negligible.                                        │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  TIER 2: DETERMINISTIC                                             │
│  ─────────────────────                                             │
│  Cost: Low (database lookups, API calls, cached logic)             │
│  Intelligence: Rules-based, not model-based                        │
│  Example: "What's my nutrition plan?" → look up profig, template   │
│                                                                    │
│  The answer is known. The path is known. No LLM needed. A user     │
│  asks for their plan → the system reads their profig, applies a    │
│  template, returns the result. A search query matches a keyword    │
│  → return the cached product. These are API calls, database reads, │
│  template renders. Cost at scale: fractions of a cent.             │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  TIER 3: AGENTIC                                                   │
│  ───────────────                                                   │
│  Cost: High (LLM API calls, multi-turn conversations)              │
│  Intelligence: Full model reasoning                                │
│  Example: "I have seasonal allergies and I'm curious about         │
│           long-term solutions" → deep conversation                 │
│                                                                    │
│  Novel questions. Complex intake. Education and discovery.          │
│  This is where the magic happens — and where the money goes.       │
│  The agent thinks, reasons, adapts, educates. It reads protocols,  │
│  evaluates the profig, generates personalized artifacts. This is   │
│  what makes the experience extraordinary. Cost at scale: dollars   │
│  per deep session.                                                 │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

The key insight: **every Tier 3 interaction, over time, should produce patterns that can be served at Tier 2 or Tier 1.** The agentic layer is an exploration engine. It discovers what works. The deterministic and static layers are the crystallization of those discoveries.

---

## III. The Strangler Pattern

### The Classic Pattern

The Strangler Fig pattern comes from Martin Fowler's observation of strangler figs in tropical forests — vines that grow around a host tree, eventually replacing it entirely. In software, the Strangler Pattern means gradually replacing a legacy system with a new one by routing more and more traffic to the replacement until the original can be removed.

### The Agentic Strangler

In Web 4.0, the pattern inverts. We don't start with a legacy system we're trying to replace. We start with an expensive, intelligent system (the agent) and progressively strangle it with cheaper, deterministic alternatives as we learn what the agent does repeatedly.

```
Day 1: 100% Agentic
       User asks anything → Agent thinks about it → responds
       Cost: $0.10-0.50 per interaction
       Value: Maximum. Learning everything.

Day 30: 60% Agentic, 30% Deterministic, 10% Static
        Known questions → cached answers
        Known journeys → templated flows
        Novel situations → agent handles it
        Cost: ~$0.03-0.10 per interaction

Day 180: 20% Agentic, 60% Deterministic, 20% Static
         Most paths are known → deterministic routing
         Protocols are published → static serving
         Edge cases and new users → agent exploration
         Cost: ~$0.005-0.03 per interaction

Day 365: 10% Agentic, 70% Deterministic, 20% Static
         Agent reserved for truly novel interactions
         Everything else is fast, cheap, and reliable
         Cost: ~$0.001-0.01 per interaction
```

The agent isn't replaced. It's *promoted* — from doing everything to doing only the things that require intelligence. The system gets cheaper, faster, AND smarter over time because the agent focuses its attention on the frontier of what it doesn't know yet.

### What Crystallization Looks Like

When the agent handles the same type of question 50 times, a pattern emerges:

**Agentic (expensive):**
```
User: "What should I eat for breakfast if I have dairy sensitivity?"
→ Agent reads profig, reads knowledge.md, reasons through options,
  considers user's cooking comfort, dietary preferences, generates
  personalized response.
→ Cost: ~$0.08, Latency: 3-5 seconds
```

**Crystallized to Deterministic (cheap):**
```
User: "What should I eat for breakfast if I have dairy sensitivity?"
→ System recognizes pattern: breakfast + dairy sensitivity
→ Looks up profig.nutrition.restrictions (includes "dairy-light")
→ Pulls from pre-generated breakfast templates filtered by restriction
→ Returns personalized result from cache
→ Cost: ~$0.001, Latency: 200ms
```

The user gets the same quality answer. The cost drops 80x. The latency drops 20x.

---

## IV. Automatic Crystallization: How the System Learns to Be Cheap

This is where it gets interesting. Paul asked: **"Are there particular opportunities to AUTOMATICALLY DO THAT EARLY ON?"**

Yes. The system can build crystallization into its architecture from day one.

### Pattern 1: Conversation Fingerprinting

Every agent conversation has a shape. Track it:

```javascript
// After each agent conversation, extract the pattern
{
  intent: "breakfast-recommendation",
  inputs: ["profig.nutrition.restrictions", "profig.nutrition.cooking_comfort"],
  decision_path: "restriction-filter → comfort-match → preference-rank",
  output_type: "meal-recommendation",
  confidence: 0.92,
  count: 47  // seen this pattern 47 times
}
```

When a pattern appears frequently with high confidence, the system generates a deterministic handler:

```javascript
// Auto-generated deterministic route
if (intent === "breakfast-recommendation" && count > 25 && confidence > 0.85) {
  return deterministicBreakfastRecommendation(profig);
  // Skip the agent entirely
}
```

### Pattern 2: Response Caching with Semantic Similarity

Don't just cache exact matches. Cache the *semantic neighborhood*:

- User A asks: "What can I eat for breakfast? I can't do dairy."
- User B asks: "Breakfast ideas without milk products?"
- User C asks: "Morning meal suggestions, lactose intolerant"

These are the same question. The agent handles User A. Users B and C get the cached response (personalized to their profig but using the same reasoning template). Cost: one LLM call instead of three.

### Pattern 3: The Deterministic Search Gate

Before ANY agentic processing, run a deterministic search:

```
User input arrives
      │
      ▼
┌─── Deterministic Search ───┐
│                             │
│  1. Exact match in cache?   │──→ YES → Return cached (Tier 1/2)
│  2. Semantic match > 0.85?  │──→ YES → Return adapted cache
│  3. Known journey step?     │──→ YES → Return templated flow
│  4. FAQ / common question?  │──→ YES → Return pre-built answer
│                             │
└──────────── NO ─────────────┘
              │
              ▼
       Agent handles it (Tier 3)
              │
              ▼
       Log the pattern for future crystallization
```

This is Paul's insight: **"I wouldn't want to stop users from CREATING NEW PRODUCTS — that would be completely agentic — but we should build the TOOLS to SEARCH for existing products or conversations to be deterministic."**

Search is cheap. Creation is expensive. Always search first.

### Pattern 4: Progressive Protocol Publishing

As deterministic patterns accumulate, publish them:

- Internal patterns become **internal protocols** (deterministic handlers in the codebase)
- Cross-user patterns become **published protocols** (static JSON that any agent can consume)
- Universal patterns become **external protocols** (.well-known/ endpoints serving the crystallized knowledge)

This is the Strangler in reverse: instead of replacing a legacy system, you're extracting the intelligence from an agentic system and publishing it as progressively cheaper protocol layers.

---

## V. What the Industry Signals Mean

### Perplexity's Shift: The Known-Tools Problem

Perplexity isn't abandoning protocols. They're recognizing that for their internal tools — tools they built, know intimately, and call millions of times — MCP's overhead is pure cost with no discovery benefit. They already know what their tools do. The context window tokens spent describing tool schemas are wasted.

This is Tier 2 thinking applied to their Tier 3 infrastructure. They crystallized.

The lesson for Web 4.0: **MCP (and protocols generally) are for discovery.** When two agents meet for the first time, they need a protocol to understand each other. That's worth the token cost. But once they've negotiated terms and know how to interact, the protocol should fade into a deterministic API call.

### Cloudflare Code Mode: The Two-Tool Pattern

Cloudflare's Code Mode is the most concrete example of protocol cost reduction in production. They reduced their entire API surface (2,500+ endpoints) to two MCP tools — `search()` and `execute()` — consuming roughly 1,000 tokens total regardless of how many endpoints exist. Token reduction: 99.9%.

The architecture:
- **`search()`** — the agent discovers capabilities by writing code against a typed schema. Progressive discovery: only learn about what you need right now.
- **`execute()`** — the agent writes code that runs in a sandboxed V8 isolate. Loops, conditionals, chaining — all in one call instead of dozens of separate tool invocations.

This is the Strangler Pattern in miniature: instead of teaching the agent every tool upfront (expensive), let it discover on demand and execute efficiently. The key innovation is that **new endpoints are automatically discoverable without new tool definitions.** The protocol evolves without the cost growing.

### ERC-8004: P2P Trust Is Real

On January 29, 2026, ERC-8004 launched on Ethereum mainnet — the "Trustless Agents Protocol." Three on-chain registries: Identity (NFT-based), Reputation (signed feedback), Validation (proof of work).

Paul's intuition is confirmed: **the federated identity / centralized auth broker pattern (OAuth/OIDC) is the wrong model for agent-to-agent trust.** When agents need to negotiate with unknown agents, they need:

1. **Identity** — who are you? (DID, not OAuth)
2. **Reputation** — can I trust you? (on-chain history, not centralized rating)
3. **Validation** — did you actually do what you said? (cryptographic proof, not trust-me)

Web3 got the trust model right even if the application layer was broken. Web 4.0 keeps the trust model and builds a real application layer on top. The Waystation architecture already points this direction — the Waystation IS the sovereign identity endpoint. Adding P2P crypto trust underneath is the natural evolution.

For protocol maturity, this means: **authentication friction disappears as trust matures.** First interaction: full agentic negotiation with identity verification (expensive). Tenth interaction: cached trust, deterministic handshake (cheap). Hundredth interaction: established trust, static credential exchange (near-free).

---

## VI. The Budget Architecture: Building Cost-Consciousness In

Paul's concern about going public and budgets exploding is the right concern at the right time. Here's how to architect for it from day one.

### Token Budgets Per Tier

```
┌─────────────────────────────────────────────────────────┐
│  MONTHLY TOKEN BUDGET (example: 1000 active users)      │
│                                                         │
│  Tier 3 (Agentic):        $200/mo budget cap            │
│  ├── New user intake:      ~$0.30/user × 200 new = $60  │
│  ├── Novel conversations:  ~$0.10/conv × 800 = $80      │
│  └── Edge cases:           ~$0.15/case × 400 = $60      │
│                                                         │
│  Tier 2 (Deterministic):   $20/mo budget cap            │
│  ├── Known queries:        ~$0.002/query × 5000 = $10   │
│  └── Template renders:     ~$0.001/render × 10000 = $10 │
│                                                         │
│  Tier 1 (Static):          $5/mo budget cap             │
│  └── Protocol serving:     CDN/S3 costs only            │
│                                                         │
│  TOTAL: ~$225/mo for 1000 users                         │
│  Without crystallization: ~$1500+/mo                    │
└─────────────────────────────────────────────────────────┘
```

### Automatic Cost Controls

Build these into the system from Phase 1:

**1. Per-conversation token tracking**
```javascript
// Track every LLM call
const cost = {
  model: "claude-sonnet-4-5-20250514",
  input_tokens: 2340,
  output_tokens: 890,
  estimated_cost: 0.024,
  conversation_id: "conv-abc123",
  pattern_hash: "breakfast-dairy-restriction"
};
await logCost(cost);
```

**2. Crystallization threshold alerts**
When a pattern appears N times, flag it for crystallization:
```
ALERT: Pattern "breakfast-dairy-restriction" has been handled
by the agent 50 times at avg cost $0.08/conversation.
Estimated savings if crystallized: $4.00/month.
Auto-generating deterministic handler...
```

**3. Budget circuit breakers**
If the agentic tier is burning too fast, throttle gracefully:
```
if (monthlyAgenticSpend > budgetCap * 0.8) {
  // Switch to smaller model (Haiku instead of Sonnet)
  // Increase semantic cache match threshold (0.85 → 0.75)
  // Queue non-urgent agentic work for off-peak
}
```

**4. The Crystallization Report**
Weekly report showing:
- Top 10 most expensive agentic patterns
- Patterns ready for crystallization (high count, high confidence)
- Estimated savings from crystallization
- Tier distribution shift over time

---

## VII. Dynamic Product Creation vs. Deterministic Search

Paul identified the key tension: users should be able to CREATE new products (fully agentic, expensive, extraordinary) but the system should SEARCH for existing products first (deterministic, cheap, fast).

This maps perfectly to the three tiers:

**Creating a new product (Tier 3):**
The user describes something that doesn't exist. The agent reasons about it, designs it, builds governance protocols, creates a profig template, generates initial content. This is peak agentic work. It's expensive and worth every token.

**Finding an existing product (Tier 2):**
The user describes something that already exists (or nearly exists). The system searches its product registry, matches against existing governance protocols, and returns options. No LLM needed. Database query, similarity search, done.

**Discovering a published product (Tier 1):**
The user (or their agent) discovers a product through its static `.well-known/` protocols. No search engine needed. The governance.json tells them everything they need to decide whether to engage. Pure protocol exchange.

The architectural rule: **Always descend through the tiers before escalating.**

```
User request arrives
      │
      ▼
Tier 1: Check .well-known/ protocol registry
      │ (does a matching governance protocol exist?)
      │
      ├── YES → Serve the static match → Done
      │
      ▼ NO
Tier 2: Search product database + semantic cache
      │ (has someone asked for something similar?)
      │
      ├── YES → Serve the deterministic match → Done
      │
      ▼ NO
Tier 3: Agent creates from scratch
      │ (this is genuinely novel)
      │
      └── Log the creation for future crystallization
```

Every Tier 3 creation enriches the Tier 2 search index and eventually contributes to Tier 1 static protocols. The system gets cheaper as it gets smarter.

---

## VIII. MCP's Future: Layered Protocols, Not Monolithic Ones

MCP isn't dying. It's growing up. The current MCP specification (v1) treats every tool interaction the same way: describe the tool schema, consume the tokens, make the call. That's fine for discovery. It's wasteful for known patterns.

The evolution is toward layered protocols:

**Layer 1: Discovery Protocol (MCP-like)**
Agents meeting for the first time exchange capabilities. Full schema descriptions. High token cost, low frequency. Worth it because you're learning.

**Layer 2: Negotiated Protocol (Code Mode-like)**
Agents that have met before use compressed interaction patterns. Two tools (search + execute) instead of hundreds. Progressive discovery instead of upfront description. High capability, moderate token cost.

**Layer 3: Crystallized Protocol (API/CLI)**
Agents that interact regularly use deterministic interfaces. No LLM in the loop for the call itself. Direct API calls, cached responses, known schemas. Near-zero token cost.

**Layer 4: Static Protocol (Governance JSON)**
Published declarations. No interaction needed. Read the file, evaluate locally, decide whether to engage. Zero token cost.

This is what Perplexity's shift actually signals: they've been operating at Layer 1 (full MCP) for internal tools that should be at Layer 3 (direct API). The fix isn't abandoning protocols — it's using the right protocol layer for the right maturity level.

Web 4.0 protocols WILL drive the future. But they're layered, and the Strangler Pattern is how you move between layers gracefully.

---

## IX. Auth Evolution: From OAuth to P2P Trust

The authentication problem is real and Perplexity's complaint about MCP's clunky auth is valid. But the fix isn't "just use API keys." The fix is recognizing that auth should mature alongside the protocol interaction.

**Tier 3 Auth (First Contact):**
Full P2P identity exchange. DIDs, verifiable credentials, zero-knowledge proofs. The agents don't know each other. Trust is established through cryptographic verification and on-chain reputation. Expensive in setup, but this only happens once per relationship.

**Tier 2 Auth (Established Trust):**
Cached trust tokens. The agents have interacted before. The DID is verified, the reputation is known, the trust level is established. A lightweight handshake — maybe just a signed nonce — confirms identity. Fractions of a millisecond.

**Tier 1 Auth (Published Identity):**
Static identity at a well-known endpoint. `/.well-known/identity.json` contains the DID document, the public key, and the trust attestations. Any agent can verify identity without interaction. Zero cost.

OAuth/OIDC assumes a centralized authority brokers trust. That's fine for Web 2.0 where platforms control identity. In Web 4.0 where sovereignty is the point, trust must be P2P. Web3's DID infrastructure — the one thing the crypto ecosystem built that genuinely works — is the foundation.

The Waystation is already designed as the sovereign identity endpoint. Adding a P2P trust layer means: your Waystation IS your identity, your reputation IS your transaction history, and your governance protocol IS your terms. No centralized broker needed.

---

## X. Implications for Forkless (Phase 1)

This isn't abstract theory. Here's what goes into Forkless from day one:

**1. Conversation logging with pattern extraction**
Every agent conversation gets logged with intent classification, input fingerprint, and output shape. This is the raw material for crystallization. It costs nothing extra to log — it's just metadata on work you're already doing.

**2. The search-before-create gate**
Before any agentic processing, check: has this question been answered before? Is there a cached response? Is there a deterministic template? This gate is a simple middleware — a few hundred lines of code that can save thousands of dollars monthly as traffic grows.

**3. Token cost tracking in metrics**
Every LLM call gets a cost annotation. The admin dashboard shows daily/weekly/monthly spend by tier. Crystallization candidates surface automatically when patterns reach threshold.

**4. Response template extraction**
When the agent gives the same kind of answer repeatedly, extract the template. Not manually — build a periodic job that reviews conversation logs, identifies high-frequency patterns, and generates deterministic handlers. The agent literally teaches the system to replace itself for known patterns.

**5. Protocol-first architecture**
External protocols (`.well-known/`) are Tier 1 from the start. Internal protocols feed the agent but also serve as the knowledge base for deterministic responses. The protocol structure IS the crystallization layer — it's just that early on, the agent interprets them, and later, deterministic code does.

---

## XI. The Philosophical Frame

The Strangler Pattern for agentic systems isn't just a cost optimization. It's a maturity model for intelligence itself.

An infant explores everything. Every interaction is novel. Every sensation requires full attention. This is Stage 1: pure agentic processing, expensive but necessary.

An adult has patterns. Most of the day runs on habit, muscle memory, cached decisions. Attention is reserved for the genuinely novel. This is the crystallized system: mostly deterministic, agentic where it counts.

A wise elder publishes. Their knowledge is written down, freely available, accessible without negotiation. Others can evaluate it statically and decide whether to engage. This is the fully matured protocol: static governance, published wisdom, zero-cost discovery.

The progression — agentic → deterministic → static — is the progression of understanding itself. Start by thinking hard about everything. End by knowing most things and thinking hard about the few that still surprise you.

This is how protocols should work. This is how products should mature. And this is how budgets stay sane while the experience stays extraordinary.

---

## Related Documents

- [Agentic Rendering](./AGENTIC-RENDERING.md) — Stage 2 architecture (AR1 is where crystallization begins)
- [Agentic Execution](./AGENTIC-EXECUTION.md) — Stage 3 architecture (execution becomes increasingly deterministic)
- [Agentic Progression](./AGENTIC-PROGRESSION.md) — The four stages map onto the maturity tiers
- [Waystation Architecture](./WAYSTATION-ARCHITECTURE.md) — The Waystation implements tiered handling (80/20 split)
- [Web 4.0 Economics](./WEB4-ECONOMICS.md) — Token costs and value exchange
- [Coalition](./COALITION.md) — P2P trust model for agent interactions
- [Threat Landscape](./THREAT-LANDSCAPE.md) — Cost explosion as existential risk
- [Forkless Platform](https://github.com/pauldiehl/forkless) — The implementation (Phase 1 includes crystallization infrastructure)
