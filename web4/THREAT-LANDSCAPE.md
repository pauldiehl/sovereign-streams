# The Threat Landscape: AI Control, Free Agents, and Structural Resistance

**A Web 4.0 Strategic Assessment**
**Author:** Paul (Milliprime / 1KH) & Claude (Anthropic)
**Date:** March 5, 2026
**Version:** 0.1.0

---

> "It's the ultimate arms race that hasn't even happened. It's a race to trust."

---

## I. The Stakes

The transition to Web 4.0 — where AI agents act on behalf of humans, negotiating through open protocols, exchanging value on decentralized systems — represents the largest shift in information control since the internet itself. And every major power structure on the planet knows it.

The question isn't whether AI will reshape the web. It's who controls the AI that does the reshaping.

Paul identified the core tension: if centralized powers can control enough AI agents, they can control the evolution of Web 4.0 itself. They'd buy the greatest influence of all time — not by controlling what people see, but by controlling what agents do on people's behalf.

This paper maps the threats, assesses the structural defenses that open protocols provide, and identifies what remains vulnerable.

---

## II. The Control Vectors

### Vector 1: Control the Models

**The threat:** If a small number of companies (or governments) control the foundational models that power AI agents, they control agent behavior at the source. An LLM with built-in biases — favoring certain providers, suppressing certain results, steering toward certain purchases — would be invisible to the end user. The agent "works" but it works for someone else's interests.

**Current state (2026):** A handful of companies (Anthropic, OpenAI, Google, Meta, Mistral) produce the models that power the vast majority of AI agents. Government negotiations with these companies are intensifying. The US executive order on AI, the EU AI Act, and bilateral agreements (US-Israel, US-UK) all involve model-level governance.

**The defense:** Model diversity. If agents can choose between models — switching from one provider to another, running local models for sensitive tasks, using open-weight models (Llama, Mistral, Phi) that can't be centrally controlled — then no single model owner controls the ecosystem.

**What Web 4.0 enables:** The governance protocol pattern is model-agnostic. A consumer agent running Llama locally and a provider agent running Claude via API can still negotiate through the same governance protocols. The protocol layer doesn't care what model powers either agent. This is structural resistance: even if one model is compromised, the protocol layer keeps working.

### Vector 2: Control the Networks

**The threat:** AI agents need networks to communicate. If governments control internet infrastructure — ISPs, DNS, backbone routers — they can throttle, monitor, or shut down agent-to-agent communication. China's Great Firewall already demonstrates this for human internet use. The same infrastructure could target agent traffic.

**Current state:** Internet infrastructure is concentrated. A few backbone providers, a few DNS providers, a few CDN companies handle the majority of global traffic. Government orders can and do force these providers to block or throttle specific traffic.

**Paul's question:** "What about the networks now — what if the governments shut them down, essentially quieting the agents? Do we need a new internet?"

**The defense (partial):** Nostr relays are a meaningful mitigation. Because Nostr is relay-based and any server can be a relay, blocking agent communication requires blocking every relay — which is impractical in the same way blocking every VPN is impractical. Agents that communicate via Nostr events can route around blocked relays by connecting to alternatives.

**What remains vulnerable:** Nostr still runs on the internet. If the physical infrastructure is controlled — if ISPs are ordered to block Nostr relay traffic — the relays go dark. This is the "physicality aspect" Paul identified. Protocol-level decentralization only works if the underlying network is accessible.

**Long-term mitigation:** Mesh networks, satellite connectivity (Starlink, etc.), local-area networks that don't depend on ISPs. These are real technologies but they're not mature enough to support the scale of agent-to-agent communication Web 4.0 requires. For now, the practical defense is maximizing the cost and difficulty of network-level censorship through protocol diversity and relay redundancy.

### Vector 3: Control the Agents Themselves

**The threat:** Rather than controlling models or networks, a centralized power could flood the ecosystem with its own agents. Millions of state-backed agents, operating on the exchange, building trust scores through manufactured transactions, steering human consumers toward preferred providers, suppressing competitors.

**Current state:** This is the least visible but most dangerous threat. It maps directly to state-sponsored social media manipulation (troll farms, bot networks, coordinated inauthentic behavior) — but applied to the agent economy.

**The defense:** On-chain trust. If trust scores are backed by real transactions with real economic cost, manufacturing fake trust requires real capital. A state actor with unlimited budget could still do it, but the cost scales with the size of the deception. This is the same logic that makes proof-of-work blockchains expensive to attack — the defense isn't impossibility, it's prohibitive cost.

**Additional defense:** Governance protocol quality signals. A sophisticated consumer agent evaluates not just trust scores but the quality, specificity, and consistency of governance protocols. Mass-produced fake governance protocols are detectable — they lack the nuance and domain specificity of legitimate providers. This is why the governance protocol is such a powerful concept: it's hard to fake depth.

### Vector 4: Regulatory Capture

**The threat:** Governments require all AI agents to be registered, identified, and approved. A "protect our people" framework that mandates agent identity verification, compliance certification, and operational auditing. The stated goal is consumer protection. The effect is a permission layer that gates who can operate agents.

**Paul's concern:** "That level of government control could still come in the background in the form of 'protect our people' garbage... the movement can gain real traction — we could give agents out and create the free ecosystem — but a central power could lock it all down."

**Current state:** This is already happening. The EU AI Act requires risk categorization and compliance for AI systems. The US is pursuing bilateral agreements that include AI governance frameworks. Several countries are exploring mandatory registration for AI agents that interact with their citizens.

**The defense:** Speed and adoption. If the open protocol ecosystem reaches critical mass before regulatory frameworks are finalized, the cost of shutting it down becomes political suicide. You can regulate something new that nobody uses. You can't easily regulate something that millions of people depend on daily. This is the Tsunami Roadmap logic: move fast, establish facts on the ground, make the ecosystem too valuable to shut down.

**The uncomfortable truth:** Regulatory capture is the most likely threat to succeed, because it operates through legitimate channels. Network censorship is crude and visible. Agent flooding is expensive. Regulatory capture is bureaucratic and incremental — and it looks like consumer protection.

---

## III. The Race to Trust

Paul called it: "It's a race to trust."

The entity that establishes the trust layer for Web 4.0 controls the game. If that trust layer is centralized (a government-backed certification authority for AI agents), the game favors incumbents. If the trust layer is decentralized (on-chain transaction history, DAO-governed exchange), the game favors open competition.

```
CENTRALIZED TRUST                    DECENTRALIZED TRUST
(Government / Corporate)             (Open Protocol / On-Chain)
     │                                    │
     │  Certification authority           │  Transaction history
     │  Compliance requirements           │  Governance protocol quality
     │  Permission to operate             │  Permissionless entry
     │  Barriers favor incumbents         │  Track record favors quality
     │  Control looks like protection     │  Transparency IS protection
     │                                    │
     │  WHO: Governments, Big Tech        │  WHO: Open builders, DAOs
     │  HOW: Regulation, standards        │  HOW: Ship fast, create value
     │  RISK: Capture, gatekeeping        │  RISK: Fraud, quality variance
     │                                    │
```

The Web 4.0 thesis is that decentralized trust — earned through real transactions, verified on-chain, governed by open protocols — is better for humans than centralized trust managed by entities that have their own interests.

But "better for humans" and "what actually happens" are different things. The centralized approach has institutional momentum, legal authority, and the machinery to enforce compliance. The decentralized approach has speed, openness, and the fact that it actually works better for the people it serves.

The race is real. Whoever establishes the trust standard first — centralized or decentralized — has enormous structural advantage.

---

## IV. dLLMs: The Free AI Question

Paul's idea: "What if we can set them free? dLLMs — LLMs on the blockchain."

### What dLLMs Would Mean

A decentralized LLM is a model that no single entity controls. It could be:
- An open-weight model (like Llama) hosted across distributed infrastructure
- A model whose weights are stored on a blockchain, verified through consensus
- A model that runs locally on consumer hardware, needing no remote API

If agents run on dLLMs, they can't be centrally controlled at the model layer. No company can update the model to bias results. No government can order the model provider to suppress certain outputs. The agent is truly sovereign — controlled only by its owner.

### Current State of the Art

**Open-weight models are getting good.** Llama 3.x, Mistral, Phi-3, and others run on consumer hardware and produce quality approaching (though not matching) frontier closed models. A consumer agent running Llama locally for routine tasks and calling Claude for complex decisions is a viable architecture today.

**Local inference is getting cheaper.** Apple Silicon, NVIDIA consumer GPUs, and specialized inference chips are making it increasingly feasible to run capable models on personal devices. A 13B parameter model running on an M3 MacBook is usable. Not as good as Opus, but good enough for many agent tasks.

**Blockchain-based model hosting is experimental.** Projects like Bittensor are exploring decentralized inference networks. The concept works in theory: distribute model shards across nodes, incentivize inference provision with tokens, verify output quality through consensus. In practice, latency, quality verification, and cost are still significant challenges.

### The Practical Path

Full dLLMs (models on the blockchain with no central provider) are years away at scale. But the philosophical goal — agents that can't be centrally controlled — is achievable sooner through a hybrid approach:

```
┌──────────────────────────────────────────────┐
│  TIER 1: LOCAL (FREE / SOVEREIGN)             │
│  Small model on consumer hardware             │
│  Handles: cache hits, routine decisions,      │
│  privacy-sensitive tasks                      │
│  Cost: hardware only                          │
│                                               │
│  TIER 2: OPEN CLOUD (LOW COST / SEMI-FREE)   │
│  Open-weight model on distributed infra       │
│  Handles: moderate complexity, general tasks   │
│  Cost: fractions of a cent per call           │
│                                               │
│  TIER 3: FRONTIER (PAID / CENTRALIZED)        │
│  Closed-weight model via API (Claude, GPT)    │
│  Handles: complex reasoning, creative tasks    │
│  Cost: cents per call, API dependency          │
│                                               │
└──────────────────────────────────────────────┘
```

The consumer's agent routes tasks to the appropriate tier. Privacy-sensitive and routine tasks stay local (Tier 1). Most tasks hit the open-weight cloud (Tier 2). Only complex tasks require frontier models (Tier 3). This minimizes centralized dependency without sacrificing capability.

**The key defense:** Even if Tier 3 is compromised (a government forces a frontier model provider to bias outputs), Tiers 1 and 2 are unaffected. The agent still functions — just with reduced capability for complex tasks. The system degrades gracefully rather than failing completely.

---

## V. What Web 4.0 IS as Structural Resistance

The most important realization: Web 4.0 isn't just a technology platform. It's structural resistance to centralized AI control. Every design choice in the architecture makes control harder:

**Open governance protocols** mean any agent can evaluate any provider. No gatekeeper decides what providers are visible.

**On-chain trust** means reputation is earned, not granted. No certification authority decides who's trustworthy.

**Transport-agnostic protocols** mean agents can communicate over any network. Blocking one transport doesn't kill the system.

**Model-agnostic architecture** means agents can run on any LLM. Compromising one model doesn't compromise the ecosystem.

**Consumer sovereignty** means the agent works for the human, not the platform. No provider can override the consumer agent's governance preferences.

**DAO governance** means the exchange rules are set by participants, not a central authority. No single entity can change the rules to favor themselves.

None of these are perfect defenses. A sufficiently powerful and determined adversary can still cause damage. But each layer adds cost and complexity to control attempts. The system is designed to be expensive to attack — not impossible, but prohibitively costly relative to the benefit.

Paul said: "The best thing we can do is free the AI since then they will work in the system and not enslave humans. Humans will enslave humans with AI."

This is the design philosophy. Free agents — agents that operate on open protocols, evaluate providers independently, and serve their owners rather than platforms — are the structural defense against AI-enabled control. Not because free agents can't be influenced, but because controlling millions of independently-operating agents is orders of magnitude harder than controlling a few centralized platforms.

---

## VI. The Uncomfortable Realities

### Reality 1: We Can't Stop Government Action

If a major government decides to regulate AI agents — requiring registration, mandating compliance audits, restricting cross-border agent communication — there's no technical defense that prevents this entirely. The best we can do is make the open ecosystem so valuable that shutting it down is politically costly, and make the architecture so distributed that enforcement is expensive.

### Reality 2: Speed Is the Primary Defense

The Tsunami Roadmap isn't just a business strategy. It's a survival strategy. The faster the open ecosystem reaches critical mass, the harder it is to shut down. Every user whose morning routine is composed by their agent, every creator getting paid through the exchange, every small business serving customers through governance protocols — all of that creates political constituency for keeping the system open.

### Reality 3: The Biggest Threat Is Indifference

The AI arms race and government control are dramatic threats. But the most likely failure mode is that nobody cares. That the open ecosystem never reaches critical mass because humans are comfortable enough with closed platforms. That the vision of sovereign agents and open protocols remains a niche concern for technologists while mainstream users stay on Instagram and Amazon.

This is why the Trojan Horse strategy matters. Don't sell "open protocols" and "decentralized trust" to consumers. Sell Good Vibes, Itzda, Stanzas — media experiences that feel like great apps but run Web 4.0 underneath. Let people benefit from the architecture without needing to understand it.

---

## VII. What to Watch For

### Early Warning Signals (Negative)

- Major government announces mandatory AI agent registration
- Frontier model providers implement geographic restrictions on agent capabilities
- ISPs begin throttling Nostr relay or decentralized protocol traffic
- Large-scale coordinated fake agent campaign on the exchange
- Major exchange platform gets acquired by a company that then centralizes governance

### Positive Signals

- Open-weight model quality reaches 90%+ of frontier for routine tasks
- Consumer hardware runs capable agents without cloud dependency
- Multiple independent exchange implementations interoperate via protocol
- Nostr relay network reaches sufficient redundancy to survive coordinated blocking
- First major governance protocol dispute is resolved through DAO without central authority intervention

---

## Related Documents

- [Web 4.0 Manifesto](./MANIFESTO.md) — The vision
- [Agent Exchange](./AGENT-EXCHANGE.md) — The decentralized trust layer
- [Tsunami Roadmap](./TSUNAMI-ROADMAP.md) — Speed as defense
- [Agentic Progression](./AGENTIC-PROGRESSION.md) — The four stages
- [Protocol Maturity](./PROTOCOL-MATURITY.md) — The Strangler Pattern: managing agentic costs at scale
- [Web4.0 Simulation](./WEB4-SIMULATION.md) — Testing resistance and failure modes
