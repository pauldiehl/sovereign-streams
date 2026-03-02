# Sovereign Streams — Organization Setup & Handoff

**Date:** February 28, 2026
**Purpose:** Instructions for setting up the `sovereign-streams` GitHub organization and migrating existing repos.

---

## 1. Create the GitHub Organization

Go to https://github.com/organizations/plan and create:

- **Org name:** `sovereign-streams`
- **Plan:** Free (upgrade later if needed)
- **Contact email:** apollo.d.paradise@gmail.com

## 2. Organization Repos

### Repo 1: `web4` (NEW — Public)

**Description:** Web 4.0 manifesto and Stream Exchange Protocol (SEP) specification

**Source:** `/sovereign-streams/web4/` in this project folder

**Contains:**
```
web4/
├── README.md                              # Org landing + SEP overview
├── MANIFESTO.md                           # The Web 4.0 vision document
├── LICENSE                                # MIT
├── spec/
│   ├── SEP-EVOLUTION.md                   # Protocol evolution notes
│   ├── SEP-v0.2.0-DRAFT.md              # Draft next version
│   └── 2026-02-28/                       # Current spec version
│       ├── README.md
│       ├── enrichment-envelope.schema.json
│       ├── consumer-intent.schema.json
│       ├── provider-response.schema.json
│       ├── provider-manifest.schema.json
│       └── telemetry.schema.json
└── docs/                                  # GitHub Pages site (future)
    └── assets/
```

**Setup commands:**
```bash
cd /path/to/sovereign-streams/web4
git init
git add .
git commit -m "Initial commit: Web 4.0 manifesto and SEP v0.1.0 specification"
gh repo create sovereign-streams/web4 --public --source=. --push --description "Web 4.0 manifesto and Stream Exchange Protocol (SEP) specification"
```

### Repo 2: `good-vibes` (EXISTING — needs migration)

**Description:** Personal Algorithm Engine — cognitive environment designer (first SEP implementation)

**Source:** `/good-vibes/` in the projects folder (already has git history)

**Current state:** Fully built with enrichment pipeline, provider, consumer, shell, tests, docs. Has local git history but no remote.

**Migration steps:**

1. Remove files that now live in `web4`:
```bash
cd /path/to/good-vibes

# Remove the manifesto (it lives in web4 now)
git rm INTERNET-4.0-MANIFESTO.md

# Note: Keep spec/ in good-vibes for now — it can reference the org spec
# but the working code depends on having schemas locally.
# Add a note in spec/README.md pointing to the canonical source.
```

2. Update `spec/2026-02-28/README.md` to add:
```markdown
> **Canonical source:** These schemas are maintained in
> [sovereign-streams/web4](https://github.com/sovereign-streams/web4/tree/main/spec).
> This copy is kept for local development convenience.
```

3. Push to org:
```bash
gh repo create sovereign-streams/good-vibes --public --source=. --push --description "Personal Algorithm Engine — cognitive environment designer (SEP implementation)"
```

## 3. What Each Repo Is For

| Repo | Purpose | Audience |
|------|---------|----------|
| `web4` | Vision + protocol spec | Everyone: developers, investors, press, community |
| `good-vibes` | Working product implementation | Developers building/using Good Vibes |
| Future: `stanzas` | Text/publishing implementation | Developers building Stanzas |
| Future: `sep-sdk` | SDK/library for SEP protocol | Developers building any SEP provider/consumer |

## 4. Relationship Between Repos

```
sovereign-streams (org)
│
├── web4           # THE VISION + THE SPEC
│   ├── MANIFESTO.md        # Why Web 4.0 matters
│   └── spec/               # SEP protocol schemas (canonical)
│
├── good-vibes              # FIRST IMPLEMENTATION
│   ├── REQUIREMENTS.md     # Product-specific requirements
│   ├── spec/               # Local copy of SEP schemas (for dev convenience)
│   ├── enrichment/         # LLM tagging pipeline
│   ├── provider/           # Good Vibes SEP provider server
│   ├── consumer/           # PAE engine
│   ├── shell/              # User interface (PWA)
│   └── docs/               # Product documentation + GitHub Pages
│
└── (future repos)
```

## 5. Key Architectural Decisions

- **SEP is org-level.** The protocol spec lives in `web4`, not in any product repo. Products keep local copies for dev convenience but the canonical source is the org repo.
- **Good Vibes is product-level.** Its REQUIREMENTS.md is specific to the Good Vibes product. The manifesto lives at the org level.
- **Each future product gets its own repo.** Stanzas, YOMO, Sovereign Kids — each will be a separate repo under `sovereign-streams`, implementing SEP for their content type.
- **An SDK repo may emerge.** Once SEP stabilizes, a `sep-sdk` repo (npm package) could provide reusable client/server libraries — similar to the `agent-intake-protocol-npm` package in AIP.

## 6. GitHub Pages Strategy

- `web4` repo → GitHub Pages at `sovereign-streams.github.io/web4` (manifesto site, protocol docs)
- `good-vibes` repo → GitHub Pages at `sovereign-streams.github.io/good-vibes` (product site, guardrails, taxonomy)
- Custom domain TBD (purchase when ready)

## 7. Immediate Next Steps

1. **Paul:** Create `sovereign-streams` org on GitHub
2. **Paul or Open Claw:** Push `web4` repo to org
3. **Paul or Open Claw:** Push `good-vibes` repo to org (after removing manifesto)
4. **Open Claw:** Build GitHub Pages site for `web4` (the vision/protocol landing page)
5. **Open Claw:** Continue Good Vibes development per REQUIREMENTS.md

## 8. Open Claw Context

When handing to Open Claw for continued development, provide:

- This HANDOFF.md for org setup context
- `web4/MANIFESTO.md` for vision context
- `good-vibes/REQUIREMENTS.md` for product build instructions
- Point Open Claw to the existing codebase in `good-vibes/` — it's already substantially built

Open Claw should read REQUIREMENTS.md first, then explore the existing code, then pick up where the previous build left off. The enrichment pipeline, provider, consumer, and shell all have working code and tests.

---

*This document is the single source of truth for org setup and repo migration.*
