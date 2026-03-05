# Web 4.0 in a Box: Simulation Design

**Finding Critical Mass Before Going Live**
**Author:** Paul (Milliprime / 1KH) & Claude (Anthropic)
**Date:** March 5, 2026
**Version:** 0.1.0

---

> "Build actual ecosystem: 100 real agent organic runs (with simulated humans) on a contained exchange → evaluate how runoffs and what it takes to go critical mass."

---

## I. Why Simulate

Web 4.0 is an ecosystem play. Agents discovering each other, negotiating governance protocols, building trust, exchanging value — none of this works in isolation. You can't test a single agent and declare the architecture viable. You need to test the ecosystem: the interactions between dozens of agents, the emergent behaviors that arise from those interactions, and the critical mass threshold where the ecosystem becomes self-sustaining.

Paul's concept is precise: build Web 4.0 in a contained box. Run real agents (not mocks, not simulations — actual LLM-powered agents) with simulated humans providing intent. Observe what happens. Find the answers to the questions that can't be answered by architecture papers alone:

- **What is the minimum viable ecosystem?** How few agents does it take for the system to be useful?
- **Where is the critical mass threshold?** At what point does growth become self-sustaining?
- **What breaks first?** Where are the failure modes nobody anticipated?
- **Do emergent behaviors appear?** Do agents form clubs, develop dialects, create unexpected patterns?
- **What does the trust curve look like?** How quickly do trust scores become meaningful?
- **What does the economics look like at scale?** Do the numbers work?

---

## II. Simulation Architecture

### The Box

```
┌─────────────────────────────────────────────────────────┐
│                  WEB 4.0 IN A BOX                        │
│                                                          │
│  ┌────────────────────────────────┐                     │
│  │  SIMULATED HUMANS (PERSONAS)   │                     │
│  │  50 consumer personas          │                     │
│  │  30 provider personas          │                     │
│  │  20 hybrid personas            │                     │
│  │  (consumer + micro-provider)   │                     │
│  └──────────────┬─────────────────┘                     │
│                 │                                        │
│                 ▼                                        │
│  ┌────────────────────────────────┐                     │
│  │  AGENTS (REAL LLM-POWERED)     │                     │
│  │  100 agents total              │                     │
│  │  Each bound to a persona       │                     │
│  │  Running actual governance     │                     │
│  │  protocol evaluation           │                     │
│  └──────────────┬─────────────────┘                     │
│                 │                                        │
│                 ▼                                        │
│  ┌────────────────────────────────┐                     │
│  │  CONTAINED EXCHANGE            │                     │
│  │  Agent Exchange protocol       │                     │
│  │  On-chain trust (testnet)      │                     │
│  │  x402 / simulated payments     │                     │
│  │  Governance protocol registry  │                     │
│  └──────────────┬─────────────────┘                     │
│                 │                                        │
│                 ▼                                        │
│  ┌────────────────────────────────┐                     │
│  │  MEASUREMENT LAYER             │                     │
│  │  Watch signals / buoys         │                     │
│  │  Transaction logs              │                     │
│  │  Communication pattern tracker │                     │
│  │  Trust curve monitor           │                     │
│  │  Economic health dashboard     │                     │
│  └────────────────────────────────┘                     │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### What's Real vs. Simulated

| Component | Real or Simulated | Why |
|-----------|------------------|-----|
| **Agents** | REAL — actual LLM-powered agents | The whole point is testing real agent behavior, not scripted responses |
| **Governance protocols** | REAL — actual JSON governance docs | Must test real protocol parsing and evaluation |
| **Exchange** | REAL — running exchange protocol | Must test actual discovery, listing, and matching |
| **Trust scores** | REAL — on testnet blockchain | Must test actual trust accumulation and verification |
| **Payments** | SIMULATED — testnet tokens or mock x402 | Real money isn't needed to test economic patterns |
| **Humans** | SIMULATED — LLM-generated personas | We need consistent, repeatable human behavior patterns |
| **Network** | CONTAINED — local or single-server | Isolate from real internet to control variables |
| **Time** | COMPRESSED — 1 sim-day = minutes | Accelerate to observe long-term patterns in hours |

---

## III. Persona Design

### Why Personas Matter

The simulation's validity depends on the realism of its simulated humans. If every persona behaves identically, the simulation tells us nothing about real-world diversity. The personas must capture the spectrum of human behavior that agents will encounter.

### The 100 Personas

**50 Consumer Personas** — People who primarily consume services:

| Category | Count | Behavioral Profile |
|----------|-------|--------------------|
| Early adopters | 10 | Tech-savvy, willing to try new things, low friction tolerance, high expectations |
| Mainstream users | 20 | Moderate tech comfort, need things to "just work," judge by outcomes not process |
| Cautious users | 10 | Privacy-conscious, slow to trust, need visible evidence that the system works |
| Low-tech users | 5 | Minimal tech literacy, rely entirely on agent defaults, don't customize |
| Power users | 5 | Optimize everything, tweak agent settings, push boundaries of what's possible |

**30 Provider Personas** — People/businesses offering services:

| Category | Count | Behavioral Profile |
|----------|-------|--------------------|
| Quality-focused | 10 | Detailed governance protocols, higher prices, strong guarantees |
| Volume-focused | 8 | Simpler governance, lower prices, faster transactions |
| New entrants | 7 | Zero trust score, trying to build reputation, willing to offer deals |
| Niche specialists | 5 | Deep expertise in narrow domain, excellent governance for that domain |

**20 Hybrid Personas** — Both consumers and micro-providers:

| Category | Count | Behavioral Profile |
|----------|-------|--------------------|
| Creator-consumers | 8 | Create content (music, writing, video) AND consume services |
| Freelancers | 7 | Offer professional services AND use the exchange for their own needs |
| Community builders | 5 | Run groups/events AND participate in others' offerings |

### Persona Specification Format

Each persona is defined as a structured document that the simulated human agent consumes:

```json
{
  "persona_id": "consumer-early-003",
  "name": "Maya Chen",
  "type": "consumer",
  "category": "early_adopter",

  "behavior_profile": {
    "trust_threshold": 0.4,
    "price_sensitivity": "low",
    "quality_sensitivity": "high",
    "patience": "low",
    "exploration_tendency": "high",
    "privacy_concern": "moderate",
    "agent_customization": "extensive"
  },

  "intent_patterns": {
    "frequency": "5-8 intents per sim-day",
    "categories": ["wellness", "music", "food_delivery", "professional_services"],
    "complexity_distribution": {
      "fire_and_forget": 0.4,
      "confirm_and_execute": 0.35,
      "browse_and_engage": 0.2,
      "ambient": 0.05
    }
  },

  "economic_profile": {
    "daily_budget": 50,
    "willing_to_try_new_providers": true,
    "repeat_purchase_loyalty": 0.6,
    "referral_tendency": "high"
  }
}
```

### Intent Generation

The simulated humans don't have free will. They generate intents based on their persona profiles, with randomization to create natural variance:

```
Persona Profile → Intent Generator → Agent receives intent
                                      │
                  ┌───────────────────┘
                  │
                  ▼
         "Find me a yoga class this evening"
         "Reorder the coffee from last time"
         "I want to listen to something chill"
         "Book a plumber for Saturday"
         "Show me what's new on the marketplace"
```

The intent generator draws from:
- The persona's category preferences (wellness, music, food, etc.)
- The persona's complexity distribution (fire-and-forget vs. browse-and-engage)
- Time-of-day patterns (morning routine intents, workday intents, evening intents)
- Previous transaction history (reorders, follow-ups, complaints)
- Random events (appliance breaks, friend recommends something, seasonal needs)

---

## IV. What to Measure: Watch Signals and Buoys

### The Four Buoy Types

Paul asked about measurement buoys — persistent monitors that track the health and behavior of the ecosystem in real time.

#### Buoy Type 1: Protocol Reliance

**What it measures:** How much are agents relying on structured governance protocols vs. falling back to unstructured methods?

**Signals:**
- **Protocol fetch rate:** How many governance protocols are fetched per sim-hour?
- **Protocol-to-transaction ratio:** What percentage of protocol fetches lead to transactions?
- **Protocol evaluation depth:** Are agents reading the full governance protocol or just skimming headers?
- **Fallback rate:** How often does an agent fail to find a protocol endpoint and resort to unstructured search?
- **Protocol quality correlation:** Do higher-quality governance protocols correlate with higher conversion rates?

**Critical threshold:** When >70% of successful transactions begin with a governance protocol fetch (rather than an unstructured query), the protocol layer is working.

**What it tells us:** Whether the governance protocol pattern is actually useful in practice, or whether agents prefer to negotiate ad-hoc.

#### Buoy Type 2: Model Size Impact

**What it measures:** How does agent intelligence level affect ecosystem behavior?

**Signals:**
- **Resolution rate by model tier:** What percentage of intents are fulfilled by Tier 1 (local/small), Tier 2 (open-weight), and Tier 3 (frontier) models?
- **Negotiation quality by model:** Do agents powered by larger models negotiate better deals? How much better?
- **Governance evaluation accuracy:** Do smaller models miss red flags in governance protocols that larger models catch?
- **Cost-per-resolution by model:** What's the all-in cost (inference + transaction fees) of fulfilling an intent at each tier?
- **Satisfaction correlation:** Do personas served by larger-model agents report higher satisfaction?

**Critical threshold:** When Tier 1 + Tier 2 models handle >80% of intents with <15% quality degradation vs. Tier 3, the system doesn't depend on frontier models. This is the dLLM viability indicator.

**What it tells us:** Whether open/small models can power a viable agent economy, or whether the system requires expensive frontier models.

#### Buoy Type 3: Governance Health

**What it measures:** The quality, honesty, and evolution of governance protocols across the ecosystem.

**Signals:**
- **Governance protocol diversity:** How many unique governance patterns exist? Are providers copying each other or innovating?
- **Governance inflation:** Are providers adding promises they can't keep to attract agents? (The governance equivalent of keyword stuffing)
- **Dispute rate:** What percentage of transactions result in a governance violation claim?
- **Governance update frequency:** How often do providers update their protocols? (Healthy sign if done thoughtfully, red flag if churning)
- **Consumer agent trust in governance:** Over time, do consumer agents increase or decrease the weight they place on governance protocol quality vs. trust score?

**Critical threshold:** When governance dispute rate drops below 5% AND governance diversity remains high (>20 unique patterns), the governance system is healthy — providers are competing on quality rather than gaming the system.

#### Buoy Type 4: Context and Emergence

**What it measures:** Unexpected behaviors, pattern formation, and systemic properties that weren't designed.

**Signals:**
- **Club formation:** Do agents cluster into groups that communicate preferentially with each other?
- **Protocol dialect emergence:** Do subsets of agents develop extended protocol vocabularies?
- **Communication pattern shifts:** Over time, does the distribution of communication patterns (message board vs. door knocking vs. coffee shop vs. trail vs. graffiti) change?
- **Trust network topology:** Does the trust graph become centralized (few highly-trusted hubs) or distributed (many moderately-trusted nodes)?
- **Economic concentration:** Does wealth concentrate in a few providers or distribute across many?
- **Oscillation and instability:** Do any metrics show cyclical behavior (boom/bust in specific categories)?
- **Cascade failures:** If a major provider goes offline, does the ecosystem recover or spiral?

**Critical threshold:** Emergence buoys don't have thresholds — they have alerts. Any novel pattern triggers a review. The point is to discover things we didn't know to look for.

---

## V. Simulation Phases

### Phase 1: Seed (Sim-Days 1-7)

**Goal:** Establish the basic ecosystem. Does it function at all?

**Setup:**
- 20 agents active (10 consumers, 7 providers, 3 hybrids)
- 5 provider governance protocols published
- Exchange running with basic listings
- No trust history (all starting from zero)

**What to observe:**
- Do consumer agents successfully discover providers?
- Do governance protocol negotiations complete successfully?
- Does the first trust score accumulate?
- What's the average time from intent to resolution?
- Where does the process break?

**Expected outcome:** Clunky but functional. High failure rate (agents can't find what they need). Long resolution times. But some transactions complete, and the basic loop works.

### Phase 2: Growth (Sim-Days 8-30)

**Goal:** Scale to full ecosystem. Does it improve with more participants?

**Setup:**
- Scale from 20 to 100 agents over the phase
- Add 5 new providers per sim-week
- Introduce agent-to-agent referrals
- Enable standing offers (notes on the door)
- Turn on trust history accumulation

**What to observe:**
- Does resolution rate improve as more providers join?
- Do consumer agents start preferring providers with established trust?
- Do standing offers result in successful later matches?
- At what agent count does discovery become noticeably easier?
- Do communication pattern distributions shift?

**Expected outcome:** Improvement curve. Early in the phase, more agents means more noise. Mid-phase, network effects kick in — more providers means more choices, trust scores become meaningful, and agents start making better decisions. Late in the phase, the ecosystem should feel qualitatively different from Phase 1.

### Phase 3: Stress (Sim-Days 31-45)

**Goal:** Test resilience. What breaks under pressure?

**Scenarios:**
- **Provider dropout:** Remove 20% of providers. How quickly do consumer agents adapt?
- **Demand spike:** Triple consumer intent frequency for 48 hours. Does the exchange handle it?
- **Bad actor injection:** Introduce 5 agents with fraudulent governance protocols. Are they detected? How quickly?
- **Model downgrade:** Force all agents to Tier 1 (smallest model). What degrades?
- **Network partition:** Split the exchange in half for 24 hours. What happens when it reconnects?
- **Trust attack:** Create 3 agents that collude to inflate each other's trust scores. Is the pattern detectable?

**What to observe:**
- Recovery time after each stress event
- Which stress events the ecosystem handles gracefully vs. which cause cascading failures
- Whether agents develop adaptive strategies in response to stress
- How the trust system performs under adversarial conditions

### Phase 4: Emergence (Sim-Days 46-90)

**Goal:** Run long enough for emergent properties to appear.

**Setup:**
- Full 100-agent ecosystem, stabilized from Phase 3
- No intervention — let it run
- Time compression: 1 sim-day = 10 minutes real-time
- 90 sim-days = ~15 hours real-time

**What to observe:**
- Everything in Buoy Type 4 (Context and Emergence)
- Long-term trust curve shapes
- Economic health metrics over extended operation
- Whether the ecosystem reaches a steady state or keeps evolving
- Novel agent behaviors that weren't programmed

---

## VI. Minimum Viable Ecosystem Size

### The Question

Paul asked: what's the minimum ecosystem size for a viable agent economy?

### The Framework

Viability requires three things:
1. **Discovery success rate >60%** — consumer agents can find a relevant provider most of the time
2. **Trust differentiation** — trust scores are meaningfully different between providers (not all near zero or all near max)
3. **Repeat transactions >30%** — agents are returning to providers they've used before (indicating satisfaction)

### The Estimate

**10 agents:** Not viable. Too few providers. Consumer agents find nothing useful. No trust accumulates.

**25 agents:** Marginally functional. If category coverage is well-distributed (at least 1 provider per major category), basic transactions complete. But no competition, no choice, no trust differentiation. It's a directed graph, not a market.

**50 agents:** The minimum for meaningful dynamics. With ~15 providers covering 5-8 categories, consumers have choices. Trust scores start to differentiate. Referrals become possible. Communication patterns beyond message-board queries emerge.

**100 agents:** The target for the simulation. With 30 providers across diverse categories, the ecosystem should exhibit most of the dynamics of a real market: competition, specialization, trust-based selection, standing offers, creative signaling. If 100 agents can't sustain a viable economy, the architecture has a problem.

**500+ agents:** Where emergent properties become visible. Club formation, protocol dialects, economic concentration patterns, trust network topology. The simulation should be designed to scale to 500 if Phase 4 results warrant it.

### The Real Critical Mass Question

The simulation answers the technical minimum — how many agents make the protocol work. But the real-world critical mass question is different: how many HUMANS need to adopt before the ecosystem is self-sustaining?

This depends on:
- **Agent-to-human ratio:** Initially 1:1. At scale, each human might have multiple specialized agents, or one agent that handles everything. The ratio determines how many humans you need for N agents.
- **Provider acquisition cost:** How much does it cost (in CPA or direct recruitment) to get one provider on the exchange?
- **Consumer activation cost:** How much does it cost to get one consumer to trust their agent enough to transact?
- **Churn rates:** How many consumers leave in the first 30 days? How many providers stop updating their governance protocols?

The simulation can model all of these by varying persona parameters and running sensitivity analysis.

---

## VII. Agent-to-Agent Communication Experiments

The [Agent Communication paper](./AGENT-COMMUNICATION.md) describes five communication patterns. The simulation tests which ones actually matter.

### Experiment 1: Communication Pattern Dominance

**Hypothesis:** In small ecosystems (<50 agents), message board (Pattern 1) dominates. As the ecosystem grows, trail following (Pattern 4) and direct handshakes (Pattern 2) become increasingly important.

**Setup:** Track every agent-to-agent interaction. Classify by pattern type. Graph distribution over time.

**What we learn:** Whether the communication architecture needs to optimize for broadcast discovery (small network) or peer-to-peer communication (large network) — or both.

### Experiment 2: The Standing Offer Economy

**Hypothesis:** Standing offers ("notes on the door") create a secondary discovery mechanism that becomes significant once >30% of providers have unmet demand sitting in their queues.

**Setup:** Track all standing offers: created, matched, expired, converted. Graph the standing offer economy over time.

**What we learn:** Whether the async demand signal is useful or just noise. If standing offers have a high conversion rate, the architecture should optimize for them. If they mostly expire unmatched, the system needs better real-time matching.

### Experiment 3: Creative Signaling ROI

**Hypothesis:** Ambitious agents (Pattern 5, "graffiti") have higher variance but better average outcomes than structured agents when seeking new providers.

**Setup:** Assign 20% of consumer agents an "ambitious" flag. These agents publish beacons, read creative signals, and try non-standard discovery methods. Compare their resolution rates, costs, and satisfaction to the structured majority.

**What we learn:** Whether creative signaling is worth building into the protocol stack or whether it should be left as an emergent behavior.

### Experiment 4: Club Formation

**Hypothesis:** After >50 sim-days, clusters of agents that preferentially transact with each other will be detectable through network analysis.

**Setup:** Build a transaction graph (nodes = agents, edges = transactions). Run community detection algorithms (Louvain, modularity optimization) at regular intervals.

**What we learn:** Whether "clubs" and "secret languages" emerge naturally, and what drives their formation (category specialization? trust clustering? communication style? geography?).

---

## VIII. What the Simulation Doesn't Test

### Human Resistance

The simulation can model cautious and low-tech personas, but it can't model genuine human resistance — the emotional, cultural, and psychological barriers to trusting an AI agent with real decisions. This requires real human testing (alpha/beta with actual users).

### Corporate Resistance

Existing platforms (Google, Amazon, Apple) will resist Web 4.0 because it disintermediates them. The simulation can't model the competitive response — lawsuits, platform blocking, regulatory lobbying, copycat products. This is strategy, not simulation.

### Regulatory Friction

Government intervention can't be modeled in a contained simulation. The threat landscape paper ([THREAT-LANDSCAPE.md](./THREAT-LANDSCAPE.md)) covers this.

### Network Effects Beyond the Box

The simulation is contained. It can't model the viral adoption dynamics that come from human word-of-mouth, media coverage, or cultural shifts. It tests whether the architecture works — not whether humans will adopt it.

---

## IX. Technical Implementation

### Stack

```
┌──────────────────────────────────────────────┐
│  SIMULATION RUNNER                            │
│  Python + async (orchestrates all agents)     │
│                                               │
│  ┌────────────────────────────────────────┐  │
│  │  AGENT RUNTIME                         │  │
│  │  Each agent = async process            │  │
│  │  LLM calls via API (Claude / Llama)   │  │
│  │  Governance protocol parser            │  │
│  │  Trust score evaluator                 │  │
│  │  Communication pattern handler         │  │
│  └────────────────────────────────────────┘  │
│                                               │
│  ┌────────────────────────────────────────┐  │
│  │  EXCHANGE SERVICE                      │  │
│  │  REST API (FastAPI)                    │  │
│  │  Listing registry                      │  │
│  │  Trust score database                  │  │
│  │  Transaction log                       │  │
│  │  Standing offer queue                  │  │
│  └────────────────────────────────────────┘  │
│                                               │
│  ┌────────────────────────────────────────┐  │
│  │  MEASUREMENT LAYER                     │  │
│  │  Time-series database (InfluxDB/Prom) │  │
│  │  Buoy signal collectors                │  │
│  │  Dashboard (Grafana / custom)          │  │
│  │  Alert engine for emergence detection  │  │
│  └────────────────────────────────────────┘  │
│                                               │
│  ┌────────────────────────────────────────┐  │
│  │  PERSONA ENGINE                        │  │
│  │  Intent generator (LLM-powered)        │  │
│  │  Behavior model per persona            │  │
│  │  Satisfaction evaluator                │  │
│  │  Time-of-day / lifecycle patterns      │  │
│  └────────────────────────────────────────┘  │
│                                               │
└──────────────────────────────────────────────┘
```

### Cost Estimate

Running 100 LLM-powered agents with compressed time (90 sim-days in ~15 hours):

**If using API calls (Claude Haiku for routine, Sonnet for complex):**
- ~100 agents × ~50 LLM calls per sim-day × 90 sim-days = ~450,000 LLM calls
- At Haiku pricing (~$0.25/M input, $1.25/M output tokens): estimated $50-150 for the full simulation run
- At Sonnet for 20% of calls: add ~$100-300
- **Total estimate: $150-450 per full simulation run**

**If using local models (Llama 3 on GPU):**
- Hardware cost only (requires GPU server)
- Significantly slower but reusable
- Good for iterative testing; use API for final runs

### Time to Build

```
Week 1-2:   Agent runtime + persona engine + intent generator
Week 2-3:   Exchange service + governance protocol registry
Week 3-4:   Communication pattern handlers (all 5 patterns)
Week 4-5:   Measurement layer + buoy signal collectors
Week 5-6:   Dashboard + alert engine
Week 6-8:   Phase 1-2 runs, debug, iterate
Week 8-10:  Phase 3 (stress testing)
Week 10-12: Phase 4 (emergence observation)
```

**Total: ~12 weeks to meaningful results.** But Phase 1 (basic ecosystem functioning) produces results within 6 weeks.

---

## X. What We Learn — And What We Build

The simulation answers Paul's core question: "What is the critical ecosystem for a viable economy?"

**From the simulation, we learn:**
- Minimum agent count for functional discovery
- Trust curve shape (how long until trust scores are meaningful)
- Economic viability (do the numbers work at different scales)
- Communication pattern distribution (what to optimize in the protocol)
- Failure modes (what breaks first, what's resilient)
- Emergence patterns (clubs, dialects, concentration)
- Model tier viability (can open-weight models power the economy)
- Governance protocol effectiveness (do they actually improve outcomes)

**What we build after the simulation:**
- The real Agent Exchange, informed by what worked in the box
- Governance protocol templates, refined by simulation feedback
- Communication protocol optimizations based on pattern analysis
- Trust system parameters calibrated by the trust curve data
- Provider onboarding playbook based on simulation provider behavior
- Agent personality framework (structured vs. ambitious) based on which performed better

The simulation isn't a demo. It's a laboratory. We build the real thing from what we learn in the box.

---

## Related Documents

- [Agent Communication](./AGENT-COMMUNICATION.md) — The five communication patterns being tested
- [Agent Exchange](./AGENT-EXCHANGE.md) — The exchange architecture being simulated
- [Agentic Execution](./AGENTIC-EXECUTION.md) — The execution patterns being modeled
- [AEO Strategy](./AEO-STRATEGY.md) — Agent discovery optimization
- [Threat Landscape](./THREAT-LANDSCAPE.md) — Threat scenarios for stress testing
- [Tsunami Roadmap](./TSUNAMI-ROADMAP.md) — How simulation results feed the live strategy
