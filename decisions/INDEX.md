# Manager Decisions Index

> Auto-generated on every `record_manager_decision` call. Do not edit directly.

| ID | Category | Summary | Path |
|---|---|---|---|
| DEC-20260913-001 | process | Manager orders Hands to run the QA-review autopilot cycle autonomously and promises closure approval | `decisions/2026/09/DEC-20260913-001.json` |
| DEC-20260913-002 | architecture | Brain must always receive the full task-file working content on every turn (implemented as auto-atta | `decisions/2026/09/DEC-20260913-002.json` |
| DEC-20260913-003 | process | In autopilot/automatic mode the Hands must call brain_turn directly and never route questions or XML | `decisions/2026/09/DEC-20260913-003.json` |
| DEC-20260913-004 | process | Task numbers live ONLY in code comments, CHANGELOG, task files, history archives, and HTML comments  | `decisions/2026/09/DEC-20260913-004.json` |
| DEC-20260913-005 | process | Push is Manager-owned (ZAC): manager pushes with git, Hands verifies remotely afterward (push-then-v | `decisions/2026/09/DEC-20260913-005.json` |
| DEC-20260913-006 | process | Closure approvals with obvious voice-to-text typos (clouse, Ckosetask, Appriveed) are accepted as va | `decisions/2026/09/DEC-20260913-006.json` |
| DEC-20260913-007 | scope | Improve existing personas/skills via live web research; add new personas only on proven gaps (seven- | `decisions/2026/09/DEC-20260913-007.json` |
| DEC-20260913-008 | process | The memorized QA-review cycle (QA persona, then reviewer persona, then report) is the standard reusa | `decisions/2026/09/DEC-20260913-008.json` |
| DEC-20260913-009 | tooling | Restart handshake: Hands prepares everything (env, global sync, timeouts), tells manager to restart  | `decisions/2026/09/DEC-20260913-009.json` |
| DEC-20260913-010 | process | Manager orders recurring-style self-judgment runs: fresh task, Brain Architect planning + brainstorm | `decisions/2026/09/DEC-20260913-010.json` |
| DEC-20260913-011 | process | In-flight findings go to a side note (/tmp) during the run, not into the task file; only final verdi | `decisions/2026/09/DEC-20260913-011.json` |
| DEC-20260913-012 | tooling | Mechanical permission-layer lock: executor agents can never run git add/checkout/commit/push via bas | `decisions/2026/09/DEC-20260913-012.json` |
| DEC-20260913-013 | process | Every future release must archive tasks/completed/ via the archive-tasks skill as part of the releas | `decisions/2026/09/DEC-20260913-013.json` |
| DEC-20260913-014 | process | Every Telegram-synced task gets a GitHub issue; skills and project memory must be loaded and followe | `decisions/2026/09/DEC-20260913-014.json` |
| DEC-20260913-015 | process | Manager's one-word 'All' selects every proposed candidate (used for the 602/604/605 sync batch). | `decisions/2026/09/DEC-20260913-015.json` |
| DEC-20260913-016 | process | GitHub issues are valid task sources alongside Telegram; issue 9 became Task 214. | `decisions/2026/09/DEC-20260913-016.json` |
| DEC-20260913-017 | process | Standing autopilot order for the sprint: implement 211-214 in wave order with Brain QA+review each,  | `decisions/2026/09/DEC-20260913-017.json` |
| DEC-20260913-018 | process | Empty Brain REPORT output is a transport flake, never a verdict: retry once lean, then escalate. Thi | `decisions/2026/09/DEC-20260913-018.json` |
| DEC-20260913-019 | scope | Reviewer-hotfix XML dropped by the bridge became Task 215: fix extractor (hotfix allowlist + xml-fen | `decisions/2026/09/DEC-20260913-019.json` |
| DEC-20260913-020 | process | Telegram message 609 became Task 216 (separate personal decisions repo) via the standard sync pipeli | `decisions/2026/09/DEC-20260913-020.json` |
| DEC-20260913-021 | architecture | Decision migration must be a Hands-invoked SKILL (capability), never a standalone script. Became Tas | `decisions/2026/09/DEC-20260913-021.json` |
| DEC-20260913-022 | process | One-word 'Approved' after a 3-step plan authorizes full autopilot implementation under the Direct In | `decisions/2026/09/DEC-20260913-022.json` |
| DEC-20260913-023 | process | Closure chain: close META 219, run global install upgrade, restart, create the personal decisions re | `decisions/2026/09/DEC-20260913-023.json` |
| DEC-20260913-024 | process | Nothing destructive (prune/push/restart) happens before the Manager sees the worktree status first. | `decisions/2026/09/DEC-20260913-024.json` |
| DEC-20260913-025 | tooling | On approval-for-closure the Hands must commit through the sanctioned MCP commit path (stage_and_inje | `decisions/2026/09/DEC-20260913-025.json` |
| DEC-20260913-026 | process | 'Global sync' means the global install upgrade per memory workflows/global-install-upgrade.md: repo  | `decisions/2026/09/DEC-20260913-026.json` |
| DEC-20260913-027 | process | Batch approval authorizes migrating all 13 local DEC records; each carries migrated_from provenance  | `decisions/2026/09/DEC-20260913-027.json` |
