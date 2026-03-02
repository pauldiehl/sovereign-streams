# Open Claw Task: Sovereign Streams Organization Setup

## Context

You are setting up a new GitHub organization called `sovereign-streams` (https://github.com/sovereign-streams). This org houses an Web 4.0 vision project and its first implementation, Good Vibes.

## Required Reading (IN THIS ORDER)

1. `/sovereign-streams/HANDOFF.md` — Org structure, repo relationships, setup steps
2. `/sovereign-streams/web4/MANIFESTO.md` — The Web 4.0 vision and SEP protocol overview
3. `/sovereign-streams/web4/README.md` — The org-level README
4. `/good-vibes/REQUIREMENTS.md` — The Good Vibes product spec (already substantially built)

## Task 1: Push `web4` repo

Create and push the `web4` repo to `sovereign-streams` org:

```bash
cd /path/to/sovereign-streams/web4
git init
git add .
git commit -m "Initial commit: Web 4.0 manifesto and SEP v0.1.0 specification"
gh repo create sovereign-streams/web4 --public --source=. --push --description "Web 4.0 manifesto and Stream Exchange Protocol (SEP) specification"
```

## Task 2: Push `good-vibes` repo

The good-vibes repo already exists locally with full git history. Migrate it:

1. Remove `INTERNET-4.0-MANIFESTO.md` from good-vibes (it now lives in web4)
2. Update `spec/2026-02-28/README.md` to note that canonical SEP schemas live in `sovereign-streams/web4`
3. Set remote and push:

```bash
cd /path/to/good-vibes
git rm INTERNET-4.0-MANIFESTO.md
git commit -m "Move manifesto to sovereign-streams/web4 org repo"
gh repo create sovereign-streams/good-vibes --public --source=. --push --description "Personal Algorithm Engine — cognitive environment designer (first SEP implementation)"
```

## Task 3: Build GitHub Pages site for `web4`

Create a clean, professional static site in `web4/docs/` (GitHub Pages). This is the public-facing landing page for the Sovereign Streams movement. Follow the same pattern as the AIP protocol site at `agent-intake-protocol.github.io`.

The site should have:
- Landing page with one-line pitch, layer diagram (1.0 → 2.0 → 3.0 → 4.0), and link to manifesto
- SEP protocol specification page with schema documentation
- Use cases overview (Good Vibes, Stanzas, Sovereign Kids, etc.)
- Clean, warm design (sunrise palette — not clinical blue). No frameworks. Vanilla HTML/CSS/JS.

## Important Notes

- The `good-vibes` codebase is already substantially built (enrichment pipeline, provider, consumer, shell, tests, docs). Don't rebuild what exists — explore it first and continue from where it left off.
- SEP (Stream Exchange Protocol) is the ORG-LEVEL protocol. Good Vibes is a PRODUCT-LEVEL implementation. Keep them cleanly separated.
- All code follows: vanilla Node.js 20, ES modules (.mjs), no frameworks, no build step.
