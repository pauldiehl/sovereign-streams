# The Agent-as-Download: Apps That Don't Exist Until You Need Them

**A Web 4.0 Architecture Paper**
**Author:** Paul (Milliprime / 1KH) & Claude (Anthropic)
**Date:** March 2, 2026
**Version:** 0.1.0-draft

---

> "The download button doesn't install an app. It activates an agent. The app is whatever happens next."

---

## I. The End of the App

Every app you've ever used was built before you arrived. Designed by a team that guessed what you'd want. Shipped as a frozen artifact. Updated on a schedule they control. You adapted to the app. The app never adapted to you.

Web 4.0 inverts this.

In Web 4.0, there is no app. There is a **protocol endpoint**, a **governance spec**, and **two agents** — one representing the provider, one representing the consumer. When they connect, an experience emerges. That experience looks like an app. It behaves like an app. But it was never built, never shipped, and never frozen. It was negotiated into existence at the moment the consumer needed it.

This is the Agent-as-Download.

---

## II. How It Works

### The Download That Isn't a Download

When a consumer clicks "Download" (or "Try It" or "Start" — the label doesn't matter), here's what actually happens:

**Step 1: Agent Activation**
The consumer is prompted to choose an agent. This is the most important decision they'll make — it's like picking a lawyer, a travel agent, or a translator. "Who do you trust to represent you?" The agent could be a free default, a premium service, or a community-maintained open-source option. The consumer picks one. This is required. Nothing works without it.

**Step 2: Protocol Handshake**
The consumer's agent contacts the provider's endpoint. The provider's agent responds with a **governance protocol** — a structured document that says: "Here's what I offer. Here are my rules. Here are my capabilities. Here's how we exchange value." This isn't an API spec. It's a declaration of intent, constraints, and suggested experience patterns.

**Step 3: Negotiation**
The consumer's agent reads the governance protocol. It evaluates it against the consumer's preferences, privacy settings, and needs. It decides what to accept, what to modify, and what to reject. This happens in milliseconds. No human involvement.

**Step 4: Experience Generation**
Based on the negotiated agreement, the consumer's agent generates the UI. Locally. On the consumer's device. The provider never ships a frontend. The provider ships data, enrichment, and governance. The consumer's agent turns that into an experience.

**Step 5: Continuous Adaptation**
As the consumer interacts, both agents learn. The experience reshapes itself. New features appear when protocols support them. Layout adjusts to behavior. Content shifts as preferences evolve. There is no "version 2.0" — there is only the ongoing conversation between two agents.

```
┌─────────────────────────────────────────────────────────┐
│                  TRADITIONAL APP                         │
│                                                          │
│  Developer builds → ships artifact → user adapts         │
│  Update cycle: weeks/months                              │
│  Personalization: surface-level (settings, themes)       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                  AGENT-AS-DOWNLOAD                        │
│                                                          │
│  Provider publishes intent → agents negotiate →           │
│  experience emerges → continuously reshapes               │
│  Update cycle: continuous (every interaction)             │
│  Personalization: structural (layout, features, flow)    │
└─────────────────────────────────────────────────────────┘
```

---

## III. The Technical Architecture

### What the Provider Runs

The provider's entire surface is a **protocol endpoint** — an HTTP (or Nostr relay) address that responds to agent queries. Behind it:

- **An orchestrator agent** that reads the governance protocol and shapes responses
- **Data streams** (content, enrichment, metadata) served via SEP
- **A governance protocol document** that declares capabilities, rules, and suggested patterns

The provider does NOT run:
- A frontend
- A design system
- A deployment pipeline for client-side code
- A CDN for JavaScript bundles

The provider runs **data and rules**. Period.

### What the Consumer Runs

The consumer's agent lives as a **service worker** — a standard web technology that runs in the browser, intercepts network requests, manages caching, and operates in the background. This is not a new runtime. It's not a browser extension. It's existing web infrastructure used for a radically different purpose.

Here's the technical reality of what happens:

**Initial Activation:**
1. Consumer visits a URL (the provider's endpoint, or a launcher page)
2. A service worker registers in the consumer's browser
3. The service worker IS the agent's local presence — or more precisely, it's the bridge between the consumer's remote agent (running on a model provider like Anthropic, OpenAI, or a local model) and the browser environment
4. The service worker intercepts all requests to the provider's domain and mediates them through the agent

**UI Generation:**
1. The agent receives the governance protocol from the provider
2. It generates HTML/CSS/JS on the fly — either via a remote model call or a local lightweight model
3. The service worker serves this generated UI to the browser as if it were a normal website
4. The consumer sees an "app" — but it was generated seconds ago, specifically for them

**Ongoing Operation:**
1. Each page load, each interaction, each data fetch is mediated by the agent via the service worker
2. The agent can regenerate any part of the UI at any time based on new data, user behavior, or protocol changes
3. Error recovery is agent-mediated: if something breaks, the agent detects it (via console errors, failed renders, broken layouts) and regenerates the affected component
4. The service worker caches working states for instant recovery

```
┌─────────────────────────────────────────────────────────────┐
│                      CONSUMER DEVICE                         │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                    BROWSER                           │    │
│  │                                                      │    │
│  │  ┌────────────┐    ┌───────────────────────────┐    │    │
│  │  │  Rendered   │    │     SERVICE WORKER         │    │    │
│  │  │    UI       │◄──│  (Agent's local presence)  │    │    │
│  │  │  (HTML/     │    │                            │    │    │
│  │  │   CSS/JS)   │    │  • Intercepts requests     │    │    │
│  │  │             │    │  • Mediates agent calls     │    │    │
│  │  │  Generated  │    │  • Caches working states    │    │    │
│  │  │  by agent,  │    │  • Monitors errors          │    │    │
│  │  │  not by     │    │  • Serves generated UI      │    │    │
│  │  │  developer  │    │                            │    │    │
│  │  └────────────┘    └───────────┬───────────────┘    │    │
│  │                                │                     │    │
│  └────────────────────────────────┼─────────────────────┘    │
│                                   │                          │
│                    ┌──────────────▼──────────────┐           │
│                    │      AGENT (remote or       │           │
│                    │      local model)           │           │
│                    │                             │           │
│                    │  • Reads governance         │           │
│                    │  • Negotiates with provider │           │
│                    │  • Generates UI             │           │
│                    │  • Makes decisions          │           │
│                    └──────────────┬──────────────┘           │
│                                   │                          │
└───────────────────────────────────┼──────────────────────────┘
                                    │
                    ┌───────────────▼──────────────┐
                    │      PROVIDER ENDPOINT        │
                    │                               │
                    │  • Governance protocol         │
                    │  • Data streams (SEP)          │
                    │  • Enrichment                  │
                    │  • Orchestrator agent           │
                    └───────────────────────────────┘
```

### The Service Worker in Detail

This is not theoretical. Service workers already do most of what's needed:

**What service workers can do today:**
- Intercept every HTTP request the page makes
- Serve cached or dynamically generated responses
- Run JavaScript in the background (independent of the page lifecycle)
- Communicate with the page via `postMessage`
- Access IndexedDB for local storage
- Make fetch requests to external APIs (including model endpoints)
- Register for push notifications
- Run periodic background sync tasks

**What we add:**
- The service worker calls a model API (Anthropic, OpenAI, local Ollama, etc.) to generate UI
- It caches the generated UI for performance (you don't regenerate every page on every load)
- It monitors the rendered page for errors and regenerates components that fail
- It handles protocol negotiation with the provider's agent
- It manages the governance protocol locally

**What this means:** The consumer "downloads" a service worker (a few KB of JavaScript). That service worker activates an agent. That agent builds the entire experience. The "app" is whatever the agent decides to render, within the governance constraints negotiated with the provider.

### The Tiered Agent Model

Not every interaction needs a large language model. The architecture uses tiered intelligence:

**Tier 1: The Service Worker (always on, zero cost)**
Handles caching, request interception, error detection, and serving previously generated UI. This is pure JavaScript running locally. No model calls. Instant response times.

**Tier 2: Small Model (Haiku-class, low cost)**
Handles routine UI generation, layout adjustments, simple content rendering, and basic error recovery. Called when Tier 1 can't serve from cache and the task is straightforward. Cost: fractions of a cent per call.

**Tier 3: Large Model (Sonnet/Opus-class, higher cost)**
Handles complex decisions: initial governance negotiation, major UI restructuring, novel feature generation, ambiguous error recovery, and user intent interpretation. Called only when Tier 2 escalates. Cost: a few cents per call — amortized across many interactions.

```
┌────────────────────────────────────────────┐
│              DECISION FLOW                  │
│                                             │
│  Request arrives at service worker          │
│           │                                 │
│           ▼                                 │
│  ┌─── Cache hit? ───┐                      │
│  │ YES              │ NO                    │
│  ▼                  ▼                       │
│  Serve cached   Is it routine?              │
│  response       │                           │
│  (Tier 1)       ├── YES → Haiku (Tier 2)   │
│                 │                           │
│                 └── NO → Opus (Tier 3)      │
│                         │                   │
│                         ▼                   │
│                    Cache result              │
│                    for future                │
└────────────────────────────────────────────┘
```

The economics are favorable. The initial "app" generation (Tier 3) might cost $0.05-0.15. Subsequent interactions mostly hit cache (Tier 1) or use cheap models (Tier 2). The amortized cost per session is well under a dollar.

---

## IV. Governance Protocols

### What Is a Governance Protocol?

When a new consumer agent connects to a provider, it needs guidance. What does this service do? What are the rules? What experience patterns work well? What are the constraints?

A governance protocol is a structured document that answers these questions. It's not code. It's not a UI template. It's a **declaration of intent, constraints, and suggestions** that the consumer's agent interprets.

Think of it like this: if you hired a contractor to build a house, you wouldn't hand them a finished house. You'd hand them architectural plans, building codes, your preferences, and a budget. They'd use their expertise to build something that satisfies all of those constraints while adapting to the specifics of your lot, your climate, and your family's needs.

The governance protocol is the architectural plans + building codes. The consumer's agent is the contractor.

### Governance Protocol Structure

```json
{
  "governance_version": "0.1.0",
  "provider_id": "good-vibes-main",
  "provider_name": "Good Vibes",
  "provider_description": "Personal algorithm engine for cognitive flourishing",

  "identity": {
    "provider_type": "content_curation",
    "ethos": "Sovereign consumption. No manipulation. No dark patterns.",
    "content_policy_url": "https://good-vibes.app/guardrails"
  },

  "capabilities": {
    "sep_version": "0.2.0",
    "stream_types": ["content_meta", "recommendations"],
    "exchange_models": ["curated_payload", "negotiated"],
    "content_types": ["video", "podcast", "music", "article"],
    "authentication": {
      "required": false,
      "methods": ["api_key", "sep_identity"],
      "free_tier_available": true
    },
    "payment_rails": ["stripe", "x402", "lightning_zaps"]
  },

  "experience_guidance": {
    "suggested_shell": {
      "type": "session_based",
      "description": "Content consumed in composed sessions with narrative arcs, not infinite scroll",
      "default_session_length_minutes": 20,
      "session_arc_template": "opener → builder → peak → closer"
    },
    "core_features": [
      {
        "id": "session_player",
        "description": "Primary content consumption interface",
        "priority": "required",
        "guidance": "Full-screen media player with session progress indicator. No autoplay to unrelated content. Session ends when arc completes."
      },
      {
        "id": "algorithm_controls",
        "description": "User-facing controls for PAE preferences",
        "priority": "required",
        "guidance": "Expose category weights, emotional filters, energy range, and session length. Changes apply immediately to next session."
      },
      {
        "id": "content_details",
        "description": "Enrichment data visible to user",
        "priority": "recommended",
        "guidance": "Show why this content was selected: category tags, emotional tone, energy level, session position. Transparency builds trust."
      }
    ],
    "design_principles": [
      "No infinite scroll",
      "No autoplay beyond session arc",
      "No engagement metrics visible to user (no like counts, view counts)",
      "Session has a beginning and an end",
      "User can always see why content was selected"
    ],
    "forbidden_patterns": [
      "Dark patterns (disguised ads, forced engagement, hidden costs)",
      "Infinite scroll or endless feed",
      "Notification spam",
      "Social comparison metrics",
      "Algorithmic manipulation for engagement maximization"
    ]
  },

  "data_contracts": {
    "consumer_data_policy": "Consumer data never leaves their device unless explicitly opted in via telemetry exchange",
    "enrichment_transparency": "All enrichment scores and reasoning available to consumer on request",
    "provider_telemetry_needs": "Anonymous session completion rates improve enrichment. Opted-in only."
  }
}
```

### How the Consumer's Agent Uses It

The governance protocol is **advisory, not mandatory.** The consumer's agent reads it and makes decisions:

- **Required features** (like `session_player`) will be built
- **Recommended features** (like `content_details`) will be built if the consumer's preferences support them
- **Design principles** will be followed unless the consumer explicitly overrides them (e.g., "I actually want autoplay" — the agent can allow it, but it warns the consumer that the provider recommends against it)
- **Forbidden patterns** are hard constraints that the consumer's agent enforces locally — even if a malicious provider tried to inject dark patterns, the consumer's agent would block them

This is the key distinction: **the governance protocol is the provider's opinion. The consumer's agent is the consumer's sovereignty.** The provider says "here's how I think this should work." The consumer's agent says "here's how my human wants it to work." The experience that emerges is the negotiation between those two positions.

### Governance Is Not Control

A governance protocol is NOT:
- A UI template (the agent decides layout)
- A forced set of rules (the agent negotiates)
- A deployment artifact (it's a living document that can evolve)
- DRM or lock-in (the consumer can leave at any time)

A governance protocol IS:
- A strong opinion from the provider about how the experience should work
- A starting point that saves the consumer's agent from building blind
- A quality signal (well-governed providers produce better experiences)
- An ethical framework (providers publish their values, consumers evaluate them)

---

## V. What This Means in Practice

### Building the Good Vibes "App"

Today, building Good Vibes means: design a UI, write React/HTML/CSS, deploy to a CDN, push updates, fix bugs, test across browsers, manage a build pipeline.

With Agent-as-Download, building Good Vibes means:

1. **Write the governance protocol** (the JSON document above). This takes hours, not weeks.
2. **Build the provider endpoint** (SEP-compliant data API + orchestrator agent). This already exists.
3. **Publish both to a URL.** Done.

The consumer's agent handles everything else. For every consumer. Differently. Adapted to their device, their preferences, their accessibility needs, their language.

### The Speed Implication

Paul said it: "The whole Web 4.0 could be created in days."

He's not wrong. Here's why:

**What takes months in traditional development:**
- UI design and iteration
- Cross-browser testing
- Responsive layout engineering
- Accessibility auditing
- Internationalization
- State management
- Deployment infrastructure
- Bug fixing across device matrix

**What the agent handles instantly:**
- All of the above
- Because it generates the UI on the target device, for the target user, in the target language, respecting the target accessibility needs — every time

**What still takes human time:**
- Governance protocol design (the hard thinking about what the experience should be)
- Data infrastructure (enrichment pipeline, content sources, SEP endpoints)
- Ethical frameworks (guardrails, content policy, privacy architecture)

The shift is from engineering time to **thinking time.** The bottleneck moves from "can we build it?" to "should we build it, and how should it behave?"

### The Product Family

Every product in the Sovereign Streams ecosystem benefits from this architecture:

| Product | Governance Protocol Focus | Provider Data |
|---------|--------------------------|---------------|
| **Good Vibes** | Session arcs, cognitive flourishing, no dark patterns | Video/podcast enrichment via YouTube |
| **Stanzas** | Reading sessions, genre balancing, discovery over bestsellers | Book metadata enrichment |
| **Itzda** | Listening sessions, mood-based discovery, artist sovereignty | Music metadata enrichment |
| **Sovereign Kids** | Age-appropriate guardrails, parental governance overlay | Filtered content enrichment |
| **Open Shelf** | Product discovery, transparent pricing, no manipulative urgency | Marketplace metadata |
| **YOMO** | Ethical product recommendations, sustainability-weighted | Affiliate/product enrichment |

Each product is a **governance protocol + data endpoint.** The consumer's agent builds the experience. One agent, many experiences. The agent learns the consumer's preferences across all of them.

---

## VI. The Self-Healing Property

### Apps That Fix Themselves

Traditional apps break. A CSS change misaligns a button. A JavaScript error crashes a page. A new browser version introduces a rendering bug. These require human developers to diagnose, fix, and deploy patches.

Agent-generated apps have a different failure mode and a different recovery path:

**Detection:**
The service worker monitors the rendered page. It knows what the intended layout was (because it generated it). It can detect: JavaScript console errors, failed resource loads, layout shifts that don't match intent, elements that render but aren't interactable, blank regions where content should appear.

**Diagnosis:**
The agent (Tier 2 or Tier 3, depending on complexity) receives the error context: what was generated, what the browser reported, what the user saw. It diagnoses the cause.

**Recovery:**
The agent regenerates the affected component. Not the whole page — just the broken part. The service worker hot-swaps the fixed component into the live page. The consumer may never notice the break.

**Learning:**
The fix is cached. That class of error is handled automatically next time (Tier 1 cache hit). Over time, the experience becomes more stable without any human intervention.

```
Error detected → Agent diagnoses → Agent regenerates →
Service worker swaps → User sees fixed version →
Fix cached for future
```

This is why Paul called them "the fastest building / healing / monitoring apps in the world." The feedback loop from error to fix is seconds, not days.

### Transparency and Logging

The entire operation is logged. The consumer can inspect:
- What the agent generated and why
- What errors occurred and how they were resolved
- What governance rules were applied
- What data was exchanged with the provider
- What model calls were made and at what cost

This is radical transparency. No black box. The consumer sees exactly what their agent is doing on their behalf.

---

## VII. User Interaction Modes

### Beyond Click and Scroll

If the agent is the interface, the interface can be anything:

**Visual (default):** The agent generates a standard web UI. Click, scroll, tap. Familiar. This is the Trojan horse — it looks like a normal app.

**Conversational:** The consumer speaks. The device transcribes. The agent interprets the intent, reshapes the experience, and the page refreshes. "Show me something calmer." The session arc adjusts. "Skip this category for today." The weights change. "What else did this creator make?" A new panel appears.

**Hybrid:** The visual UI is the primary interface. A small voice/text input lets the consumer give real-time feedback. The agent processes it and adjusts the experience continuously. The page evolves as the consumer talks to it.

**Ambient:** For wearables or background listening. The agent selects content based on context (time of day, activity, previous sessions) and serves it as an audio stream. No visual UI at all. The governance protocol defines the session arc; the agent executes it.

All of these are just different rendering modes for the same underlying architecture: agent reads governance, negotiates with provider, generates experience. The "shape" of the experience depends on the device and the consumer's preference.

---

## VIII. The Out-of-the-Package Default

### First-Run Experience

A new consumer who just picked their agent needs something to start with. They haven't set preferences yet. They haven't interacted with any governance protocols. They need a starting point.

The **Out-of-the-Package (OOTP) default** is:

1. **A basic shell** — a minimal, functional UI that the agent generates from the governance protocol's `core_features` list. For Good Vibes, this would be: a session player, basic algorithm controls, and a "why this content?" panel.

2. **The governance protocol's suggested defaults** — session length, arc template, default category weights. These are the provider's best guess at what a new user wants.

3. **A calibration flow** — the agent asks 3-5 quick questions to personalize: "What are you interested in?" / "How long do you want sessions to be?" / "Morning energy or evening calm?" These answers seed the PAE immediately.

The OOTP default is intentionally simple. The experience grows more complex — and more personal — as the consumer uses it. Features appear when they're relevant. The agent adds complexity gradually, never all at once.

### The Growing App

Session 1: Basic player + curated content. Simple layout. One screen.

Session 5: The agent has learned preferences. Layout adjusts — categories the consumer loves get more space. A "discovery" section appears for new categories the algorithm wants to introduce.

Session 20: The consumer has a rich profile. The experience now includes: custom session arcs, cross-category transitions, creator bookmarks, taste evolution visualization. None of these were "shipped." They emerged because the agent determined the consumer would benefit from them.

Session 100: The consumer's agent starts surfacing features from OTHER providers — Stanzas book recommendations between video sessions, Itzda music as session transitions. The experience is no longer "Good Vibes the app." It's "the consumer's personal media environment, with Good Vibes as the primary content source."

This is what "apps that grow" means. Not feature releases. Not update prompts. Organic evolution driven by the consumer's behavior and the agent's intelligence.

---

## IX. Security and Trust

### Why This Isn't Scary

The immediate objection: "An agent that generates arbitrary code on my device? That's a security nightmare."

It's a fair concern. Here are the guardrails:

**1. The service worker sandbox**
Service workers run in the browser's security sandbox. They cannot access the filesystem, install software, read other tabs, or escape the browser context. This is enforced by the browser, not by us. It's the same security model that every PWA already uses.

**2. The governance protocol is auditable**
Before the agent builds anything, the consumer (or their agent) can inspect the governance protocol. It's a JSON document. It's transparent. If a provider's governance protocol says "track everything and send it to our servers," the consumer's agent can refuse to connect.

**3. The consumer's agent is the firewall**
The consumer chose their agent. The agent's job is to protect the consumer's interests. If the provider tries to inject dark patterns, the agent blocks them. If the generated UI tries to make unauthorized network calls, the service worker blocks them. The consumer's agent is the trust boundary.

**4. Generated code is inspectable**
Every piece of HTML/CSS/JS the agent generates is visible in the browser's dev tools. Nothing is obfuscated. The consumer (or a security auditor) can see exactly what's running.

**5. Model providers have safety constraints**
The models generating the UI (Anthropic, OpenAI, etc.) have their own safety layers. They won't generate malicious code, phishing interfaces, or data-exfiltration scripts. This is an additional layer of protection beyond the browser sandbox.

### The Trust Chain

```
Consumer trusts → their Agent → which evaluates → Governance Protocol
                                                         │
                                         Published by → Provider
                                                         │
                                         Backed by → Provider's reputation,
                                                     transaction history,
                                                     community attestations
```

Trust flows from the consumer outward. Not from the provider downward.

---

## X. What Gets Built Today

### The Minimum Viable Agent-as-Download

This doesn't require solving every problem above. The MVP is:

1. **A service worker** that registers on the provider's domain
2. **A governance protocol endpoint** that returns a JSON governance document
3. **An agent integration** that calls a model API (Claude, GPT, etc.) with the governance protocol + consumer preferences and receives generated HTML
4. **A cache layer** in the service worker that stores generated pages
5. **An error monitor** that detects failures and triggers regeneration

That's it. Five components. The service worker is ~200 lines of JavaScript. The governance protocol is a JSON document. The agent integration is a fetch call with a well-crafted prompt. The cache is IndexedDB. The error monitor is a MutationObserver + window.onerror.

This could be built in a weekend. It would be rough. It would be slow (model latency on first generation). It wouldn't handle every edge case. But it would work. And it would prove the architecture.

### Phase 1: Proof of Concept
- Service worker + governance protocol + single model integration
- Good Vibes as first test case
- Generated session player with basic algorithm controls
- Cache for sub-second repeat loads
- Error detection and regeneration

### Phase 2: Multi-Tier Intelligence
- Add Haiku for routine generation, Opus for complex decisions
- Implement cost tracking per session
- Add voice/text input for conversational interaction
- Cross-provider governance (Stanzas, Itzda)

### Phase 3: Agent Marketplace
- Multiple agent providers (Anthropic, OpenAI, local models, community agents)
- Agent reputation and trust scoring
- Agent-to-agent communication for cross-provider experiences
- Consumer agent migration (switch agents without losing preferences)

---

## XI. The Philosophical Shift

### From Building to Declaring

The entire history of software development has been about **building things.** Write code. Ship artifacts. Fix bugs. Ship again.

Agent-as-Download is about **declaring things.** Declare what the experience should be (governance protocol). Declare what data is available (SEP). Declare what the consumer wants (PAE preferences). Let intelligence negotiate the rest.

This is not a small change. This is the end of frontend engineering as a discipline and the beginning of **experience governance** as a discipline. The question shifts from "how do we build this?" to "what should this be?"

### The Implication for Web 4.0

Every product in the Sovereign Streams ecosystem — Good Vibes, Stanzas, Itzda, Open Shelf, Sovereign Kids, YOMO — can be built as a governance protocol + SEP endpoint. The consumer's agent handles the rest. Different consumers see different experiences from the same provider, because their agents interpret the governance differently based on their preferences, devices, and contexts.

The "whole Web 4.0 could be created in days" because creating a Web 4.0 product means writing a governance protocol and standing up a data endpoint. The traditional months of frontend development, design iteration, cross-browser testing, and deployment management simply evaporate.

What remains is the hard work: thinking clearly about what the experience should be, building high-quality data infrastructure, and designing ethical governance frameworks. That work can't be automated. And it shouldn't be.

---

## Sources and Prior Art

- [Service Workers API (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)
- [Progressive Web Apps (web.dev)](https://web.dev/progressive-web-apps/)
- [Web 4.0 Manifesto](./MANIFESTO.md)
- [Stream Exchange Protocol v0.1.0](./spec/2026-02-28/)
- [SEP Evolution Roadmap](./spec/SEP-EVOLUTION.md)
- [Web 4.0 Economics](./WEB4-ECONOMICS.md)
