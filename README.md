# Research skills

Claude Code skills for product and competitor research for ad creative, one project per client.

## What is in here

| Path | What it is |
|---|---|
| `skills/research/` | The `/research` skill: website brief, voice-of-customer collection, competitor ads (TrendTrack or Meta Ad Library), consolidation, DRIVE strategy, angle and avatar exploration with competitor validation. Includes reference files and two scripts (`count_quotes.py`, `ad_matrix.py`). Also: the client's own ad account and offer audit (Phase 0B), TikTok and trend scan, science and claim guardrails, the DRIVE Strategy Document (Phase 4) and the Angle Exploration Document with competitor takeover cards ("This angle is currently running from [competitor]" → "Here's how we dominate it"), plus `verify_quotes.py`, `depth_check.py` and `mechanism_check.py`. |
| `skills/client-research-workflow/` | The house workflow around it: one project per client, local-market sources only, reuse existing research, prioritise angles competitors have not used, optional weekly trend scan. |
| `CLAUDE.md` | Default instructions that make the skills the standard way to research in any folder. |

## Use it in a Claude project

Add this repository to the project (Project settings > Repositories). Every thread in the project then has both skills.

## Use it in Claude Code on your computer

1. Copy `skills/research/` and `skills/client-research-workflow/` into `~/.claude/skills/` (Windows: `C:\Users\<you>\.claude\skills\`).
2. Paste the contents of `CLAUDE.md` at the end of `~/.claude/CLAUDE.md`.
3. Open any project folder and type `/research`.

For competitor ads connect the TrendTrack MCP; for browser-only sources connect Claude in Chrome.
To use your own frameworks, edit `skills/research/references/definitions.md` (keep the headings).
