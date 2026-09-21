# Manager Decisions Index

> Auto-generated on every `record_manager_decision` call. Do not edit directly.

| ID | Category | Summary | Path |
|---|---|---|---|
| DEC-20260912-001 | process | Public-default secret handling: record only repo display name (active_root), never absolute path; fu | `decisions/2026/09/DEC-20260912-001.json` |
| DEC-20260912-002 | process | Every stored decision must pass sanitize_text on all free-text fields plus a verify_clean gate; any  | `decisions/2026/09/DEC-20260912-002.json` |
| DEC-20260912-003 | process | Decision stores are append-only: corrections are new tombstone records, never edits or deletes of st | `decisions/2026/09/DEC-20260912-003.json` |
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
| DEC-20260914-001 | process | Hands must always reply in English, never in Persian. | `decisions/2026/09/DEC-20260914-001.json` |
| DEC-20260914-002 | quality-gate | Image-moderation QA scenarios marked FAILED instead of BLOCKED. | `decisions/2026/09/DEC-20260914-002.json` |
| DEC-20260914-003 | process | Standing full-autopilot order: run end-to-end with zero questions until the Manager speaks. | `decisions/2026/09/DEC-20260914-003.json` |
| DEC-20260914-004 | process | socat port-forward work on the manager script needs no Kanban task file. | `decisions/2026/09/DEC-20260914-004.json` |
| DEC-20260914-005 | architecture | CSP upgrade-insecure-requests disabled on dev, kept on prod. | `decisions/2026/09/DEC-20260914-005.json` |
| DEC-20260914-006 | process | Task 221 absorbs port/forward-script worktree changes; .forward.pid is gitignored runtime state. | `decisions/2026/09/DEC-20260914-006.json` |
| DEC-20260914-007 | architecture | Dev server port moved 8081 to 8082 (8081 held by external proxy). | `decisions/2026/09/DEC-20260914-007.json` |
| DEC-20260914-008 | scope | Curl-driven filter creation runs without a task file, one EXPLORER_BROAD filter per collection. | `decisions/2026/09/DEC-20260914-008.json` |
| DEC-20260914-009 | quality-gate | Admin backup download accepted as prod-only; dev 500s are environmental, not a code bug. | `decisions/2026/09/DEC-20260914-009.json` |
| DEC-20260914-010 | architecture | Stopped apex-dev-pg container kept (not removed) after compose takeover. | `decisions/2026/09/DEC-20260914-010.json` |
| DEC-20260914-011 | process | Restart handshake: Hands restarts, Manager tests, result comes back before closure. | `decisions/2026/09/DEC-20260914-011.json` |
| DEC-20260914-012 | process | A-vs-B choice delegated to Brain + stored decisions; then run autonomously to end-of-day closeout. | `decisions/2026/09/DEC-20260914-012.json` |
| DEC-20260914-013 | scope | New goal with explicit objective text: 5% profit scan + engine verification and speedup via log trac | `decisions/2026/09/DEC-20260914-013.json` |
| DEC-20260914-014 | process | Goal conflict resolved with option 3: old 5%-profit goal retired into the Portal scan-speed goal via | `decisions/2026/09/DEC-20260914-014.json` |
| DEC-20260914-015 | autopilot-cycle | Standing full-autopilot order for the Telegram/Portal engine-speed work: parallel lanes allowed, Bra | `decisions/2026/09/DEC-20260914-015.json` |
| DEC-20260914-016 | process | Ops via curl only: add the 10 cheapest uncovered collections as EXPLORER_BROAD filters (both markets | `decisions/2026/09/DEC-20260914-016.json` |
| DEC-20260915-001 | autopilot-cycle | Manager approved fixing all brainstorm gaps via the Hands on autopilot. | `decisions/2026/09/DEC-20260915-001.json` |
| DEC-20260915-002 | autopilot-cycle | Manager ordered Task 232 implementation on autopilot with Brain planning. | `decisions/2026/09/DEC-20260915-002.json` |
| DEC-20260915-003 | process | Manager approved closure of Task 232. | `decisions/2026/09/DEC-20260915-003.json` |
| DEC-20260915-004 | process | Manager approved closure of Task 233. | `decisions/2026/09/DEC-20260915-004.json` |
| DEC-20260916-001 | process | Manager approves the 226 Brain plan with assumptions A1 keep buying concurrency, A2 bias never-doubl | `decisions/2026/09/DEC-20260916-001.json` |
| DEC-20260916-002 | process | Full-autopilot order for 228: Hands executes the Brain's two-pass docs audit end to end, stopping on | `decisions/2026/09/DEC-20260916-002.json` |
| DEC-20260916-003 | tooling | Standing order: wrap all test-verdict runs with rtk test (token collapse, exit code preserved); fail | `decisions/2026/09/DEC-20260916-003.json` |
| DEC-20260916-004 | process | QA plus code-reviewer gate order for the 229 cooldown-proof endpoint work (uncommitted debug-control | `decisions/2026/09/DEC-20260916-004.json` |
| DEC-20260916-005 | process | File the HQ umbrella issue (became issue 15) with Brain reflect on two bridge bugs, demanding rtk-in | `decisions/2026/09/DEC-20260916-005.json` |
| DEC-20260917-001 | scope | Fold the Brain context-path bug fix and every priority harness improvement from the research into a  | `decisions/2026/09/DEC-20260917-001.json` |
| DEC-20260917-002 | process | Lock the task in autopilot and drive it end-to-end without human pauses, except hard blockers and Re | `decisions/2026/09/DEC-20260917-002.json` |
| DEC-20260917-003 | release | Closure stays Manager-gated: the task may not be closed, and no closure commit made, without the Man | `decisions/2026/09/DEC-20260917-003.json` |
| DEC-20260917-004 | quality-gate | Zero-Autonomous-Commit holds for the entire task: no git add, git commit, or git push by the Hands a | `decisions/2026/09/DEC-20260917-004.json` |
| DEC-20260917-005 | release | The Manager granted closure approval for the harness-upgrade/context-path task, authorizing the move | `decisions/2026/09/DEC-20260917-005.json` |
| DEC-20260917-006 | scope | One repair task (248) covers the whole manager-decision tool chain: session extraction, decision rec | `decisions/2026/09/DEC-20260917-006.json` |
| DEC-20260917-007 | process | Run the task under the stored standing order manager/full_automatic_mode: full-automatic execution w | `decisions/2026/09/DEC-20260917-007.json` |
| DEC-20260917-008 | process | Every step of the task routes through the Brain seat sequence: Brain plans, Hands implement, Brain Q | `decisions/2026/09/DEC-20260917-008.json` |
| DEC-20260917-009 | quality-gate | A Code Reviewer technical APPROVED verdict carrying PO_REVIEW_PENDING status satisfies the closure g | `decisions/2026/09/DEC-20260917-009.json` |
| DEC-20260917-010 | process | Bug and learning reporting defaults to decision records; when the record tools themselves are the br | `decisions/2026/09/DEC-20260917-010.json` |
| DEC-20260917-011 | release | Closure approved for Task 248: the single-issuance final-closure XML may be issued and executed once | `decisions/2026/09/DEC-20260917-011.json` |
| DEC-20260917-012 | process | Run the task under locked full-automatic mode with zero questions to the manager, and route every st | `decisions/2026/09/DEC-20260917-012.json` |
| DEC-20260917-013 | quality-gate | A reviewer technical APPROVED together with PO_REVIEW_PENDING status is sufficient to close the task | `decisions/2026/09/DEC-20260917-013.json` |
| DEC-20260917-014 | scope | Limit this task to authority-ranked retrieval ranking plus the evaluation metrics; any other work mu | `decisions/2026/09/DEC-20260917-014.json` |
| DEC-20260917-015 | process | Standing order: the agent must never think, reason, or respond in any language but English, even whe | `decisions/2026/09/DEC-20260917-015.json` |
| DEC-20260917-016 | process | Save every Manager decision from the session as a manager decision record and update the manager-dec | `decisions/2026/09/DEC-20260917-016.json` |
| DEC-20260918-001 | scope | No Cando task file for non-Cando framework work. | `decisions/2026/09/DEC-20260918-001.json` |
| DEC-20260918-002 | process | Report baseline-flow gaps as upstream HQ issues with full evidence; persist decisions via the decisi | `decisions/2026/09/DEC-20260918-002.json` |
| DEC-20260918-003 | process | Telegram sync runs without GitHub issues unless explicitly asked. | `decisions/2026/09/DEC-20260918-003.json` |
| DEC-20260918-004 | autopilot-cycle | Pre-authorized plan auto-approval is valid only on explicit Manager order; announce and record the l | `decisions/2026/09/DEC-20260918-004.json` |
| DEC-20260918-005 | autopilot-cycle | On autopilot, QA and review run machine-to-machine; Manager sees only relay questions and final verd | `decisions/2026/09/DEC-20260918-005.json` |
| DEC-20260919-001 | process | Execute Task 259 under full automatic autopilot: ask no questions, consult all Brain personas via br | `decisions/2026/09/DEC-20260919-001.json` |
| DEC-20260919-002 | scope | Extend the same provider-diagnosis fix to mcp-decision-server/server.py inside the current active ta | `decisions/2026/09/DEC-20260919-002.json` |
| DEC-20260920-001 | process | On autopilot, plan through the Brain first and then implement automatically without pausing for a se | `decisions/2026/09/DEC-20260920-001.json` |
| DEC-20260920-002 | architecture | Store the full per-task history durably and bound only the view sent to the model; simple JSON stora | `decisions/2026/09/DEC-20260920-002.json` |
| DEC-20260920-003 | tooling | Fix our own transcript storage instead of migrating to LiteLLM, and make every Responses-API server  | `decisions/2026/09/DEC-20260920-003.json` |
| DEC-20260920-004 | process | Run the new analytics task through the autopilot baseline cycle, using Brain, Blues search, and mana | `decisions/2026/09/DEC-20260920-004.json` |
| DEC-20260921-001 | scope | Broadcast dedup keys on the broadcast identity, not on the message text. Two separate submissions of | `decisions/2026/09/DEC-20260921-001.json` |
