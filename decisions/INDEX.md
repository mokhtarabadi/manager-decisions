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
| DEC-20260925-001 | release | Approved closure of Task 841 Phase 1 offline-cache kill-switch | `decisions/2026/09/DEC-20260925-001.json` |
| DEC-20260925-002 | release | Approved closure of Task 839 typing indicator as static text | `decisions/2026/09/DEC-20260925-002.json` |
| DEC-20260925-003 | release | Approved closure of Task 838 billing hardening A1-A6 | `decisions/2026/09/DEC-20260925-003.json` |
| DEC-20260925-004 | release | Approved closure of Task 579 timezone hardening | `decisions/2026/09/DEC-20260925-004.json` |
| DEC-20260925-005 | release | Approved closure of Task 471 AI research queries | `decisions/2026/09/DEC-20260925-005.json` |
| DEC-20260925-006 | release | Approved closure of Task 842 UI audit | `decisions/2026/09/DEC-20260925-006.json` |
| DEC-20260925-007 | release | Approved closure of Task 840 time ticker | `decisions/2026/09/DEC-20260925-007.json` |
| DEC-20260925-008 | release | Approved closure of Task 837 analytics fix | `decisions/2026/09/DEC-20260925-008.json` |
| DEC-20260927-001 | quality-gate | S2 upgrade-path QA skipped: fresh install means no upgrade path exists; revisit when an older build  | `decisions/2026/09/DEC-20260927-001.json` |
| DEC-20260927-002 | architecture | Keep placeholder fallback_webhook_secret on staging; production carries the real secret. Staging/pro | `decisions/2026/09/DEC-20260927-002.json` |
| DEC-20260927-003 | tooling | Staging Zarinpal set to sandbox mock (code supports merchant_id=sandbox); parse service recreated to | `decisions/2026/09/DEC-20260927-003.json` |
| DEC-20260927-004 | process | Search-tab VIP bug: diagnose root cause vs working activity hub, explain, then file a backlog task ( | `decisions/2026/09/DEC-20260927-004.json` |
| DEC-20260927-005 | quality-gate | S9 verified jointly: agent finds/tests/sets a working public proxy and confirms adapter pickup from  | `decisions/2026/09/DEC-20260927-005.json` |
| DEC-20260927-006 | architecture | Balancer selection policy: always prefer fastest known nodes, exclude stale nodes, keep load fair ac | `decisions/2026/09/DEC-20260927-006.json` |
| DEC-20260927-007 | tooling | Manual rotate helper must be a global zero-argument command (rr) that auto-detects and rotates the c | `decisions/2026/09/DEC-20260927-007.json` |
| DEC-20260927-008 | process | New balancer-adjacent features (e.g. 429 pre-flight check) must be env-configurable and toggleable,  | `decisions/2026/09/DEC-20260927-008.json` |
| DEC-20260927-009 | process | Small timer-interval tweaks do not need Kanban task tracking; change and reload directly. | `decisions/2026/09/DEC-20260927-009.json` |
| DEC-20260927-010 | scope | Rejected chaining Psiphon with WARP (usque MASQUE client) to gain UDP support; chose the simpler TCP | `decisions/2026/09/DEC-20260927-010.json` |
| DEC-20260927-011 | architecture | Exit node routes only TCP peer traffic through the Psiphon US tunnel; QUIC (UDP/443) is dropped to f | `decisions/2026/09/DEC-20260927-011.json` |
| DEC-20260927-012 | quality-gate | Accepted peer-side test evidence (browser IP US, STUN-discovered server IP accepted as by-design, DN | `decisions/2026/09/DEC-20260927-012.json` |
| DEC-20261001-001 | architecture | Pin the OpenRay vless feed as the live subscription source via a systemd drop-in override, leaving t | `decisions/2026/10/DEC-20261001-001.json` |
| DEC-20261001-002 | process | Ad-hoc operational changes against systemd units need no upfront Kanban tracking; the task file is c | `decisions/2026/10/DEC-20261001-002.json` |
| DEC-20261001-003 | tooling | Force double-quoted YAML scalars for REALITY public-key/short-id so Go-YAML cannot misread hex value | `decisions/2026/10/DEC-20261001-003.json` |
| DEC-20261001-004 | architecture | Switch the Load Balance group to consistent-hashing with active 60s health checks so traffic spreads | `decisions/2026/10/DEC-20261001-004.json` |
| DEC-20261001-005 | process | For quick one-shot fixes, implement first without Kanban tracking, then create the task file and clo | `decisions/2026/10/DEC-20261001-005.json` |
| DEC-20261001-006 | architecture | Configure mihomo to health-check every proxy in Auto, Load Balance, and Fallback with a strict https | `decisions/2026/10/DEC-20261001-006.json` |
| DEC-20261001-007 | quality-gate | Accept the lightweight HTTP-204 status check instead of a body-download test, to avoid overloading t | `decisions/2026/10/DEC-20261001-007.json` |
| DEC-20261001-008 | architecture | Keep the PROXY group in select mode and ignore mihomo auto-balance; an external Python script using  | `decisions/2026/10/DEC-20261001-008.json` |
| DEC-20261001-009 | scope | When a feature is implementable but not wanted yet, capture it as a task file and defer implementati | `decisions/2026/10/DEC-20261001-009.json` |
| DEC-20261001-010 | architecture | Provide a manual rotate helper (API or command) to force rotation to the next alive node when a prox | `decisions/2026/10/DEC-20261001-010.json` |
| DEC-20261001-011 | other | The `PROXY` entry seen in the balancer is the select group's own name, not a node or bug; answer wit | `decisions/2026/10/DEC-20261001-011.json` |
| DEC-20261001-012 | scope | Park the POST-based 429 pre-flight in backlog and do not implement it until the manager provides the | `decisions/2026/10/DEC-20261001-012.json` |
| DEC-20261001-013 | architecture | A POST-triggered 429 cannot be reproduced inside mihomo (GET-only checks); implement the pre-flight  | `decisions/2026/10/DEC-20261001-013.json` |
| DEC-20261001-014 | architecture | Lengthen the rotation interval (proposed 30-60 min) so clean, unflagged IPs survive longer. | `decisions/2026/10/DEC-20261001-014.json` |
| DEC-20261001-015 | architecture | Add a unique-host/unique-IP dedup argument (off by default): the parser never registers duplicate ho | `decisions/2026/10/DEC-20261001-015.json` |
| DEC-20261001-016 | process | Tasked work runs the full autopilot stages including Brain-driven QA and Brain reviewer. | `decisions/2026/10/DEC-20261001-016.json` |
| DEC-20261001-017 | scope | Fold small related checks (e.g. rotation wrap-around) into the current task instead of opening a new | `decisions/2026/10/DEC-20261001-017.json` |
| DEC-20261001-018 | scope | Wire the existing --unique-host flag into the live refresh path and tune the freshness/coverage bala | `decisions/2026/10/DEC-20261001-018.json` |
| DEC-20261001-019 | architecture | Dedup roughly halves the live pool (about 7230 to 3770) and the retest batch is raised to 500, cutti | `decisions/2026/10/DEC-20261001-019.json` |
| DEC-20261001-020 | architecture | On every balancer selection change, close connections still chained to the previous node, in both th | `decisions/2026/10/DEC-20261001-020.json` |
| DEC-20261001-021 | process | Approved a read-only code audit (no code changes) to verify the pasted admin-panel analytics claims  | `decisions/2026/10/DEC-20261001-021.json` |
| DEC-20261001-022 | architecture | Approved brainstorm path O1 (P1 freshness label, P2 force-update gate with kill switch, P3 bounded A | `decisions/2026/10/DEC-20261001-022.json` |
| DEC-20261001-023 | release | Ordered closure of task 854 once all child tasks (857-863) were closed. | `decisions/2026/10/DEC-20261001-023.json` |
| DEC-20261001-024 | process | Mandated a strictly read-only production export: no writes, deletes, restarts or config changes; dow | `decisions/2026/10/DEC-20261001-024.json` |
| DEC-20261001-025 | release | Ordered the delivered chat export moved to completed; export artifacts (in /tmp) are never committed | `decisions/2026/10/DEC-20261001-025.json` |
| DEC-20261001-026 | autopilot-cycle | Locked autopilot and ordered the admin chat-viewer tasks completed fully; every UI/UX part must get  | `decisions/2026/10/DEC-20261001-026.json` |
| DEC-20261001-027 | architecture | Admin chat viewer must be access-controlled and audit-logged; deleted-flag messages are clearly badg | `decisions/2026/10/DEC-20261001-027.json` |
| DEC-20261001-028 | architecture | Approved path O1 - extend the existing moderation module with a new master-key cloud function and an | `decisions/2026/10/DEC-20261001-028.json` |
| DEC-20261001-029 | architecture | B1 - the direct flavor IS the Google Play flavor; Play Install Referrer goes into the DIRECT variant | `decisions/2026/10/DEC-20261001-029.json` |
| DEC-20261001-030 | tooling | B2 - crawl the Bazaar, Myket and Play referrer docs and store them in docs/bazaar, docs/myket and do | `decisions/2026/10/DEC-20261001-030.json` |
| DEC-20261001-031 | scope | B3 - full implementation scope: per-variant SDK dependency, per-flavor ReferrerReader, AttributionMa | `decisions/2026/10/DEC-20261001-031.json` |
| DEC-20261001-032 | architecture | Per-variant packaging accepted over bundling all referrer SDKs in every APK. | `decisions/2026/10/DEC-20261001-032.json` |
| DEC-20261001-033 | process | Run referrer implementation in autopilot with the Brain, then inject the Manager's words into the ta | `decisions/2026/10/DEC-20261001-033.json` |
| DEC-20261001-034 | process | Dashboard-watch order: keep the analytics/dashboard/admin-panel data showing install sources correct | `decisions/2026/10/DEC-20261001-034.json` |
| DEC-20261001-035 | quality-gate | Rejected the 5-second auto-advance countdown on the purchase sheet; explicit tap only; keep the pre- | `decisions/2026/10/DEC-20261001-035.json` |
| DEC-20261001-036 | scope | Approved building A1-A5 on both purchase sheets - UI only, billing untouched. | `decisions/2026/10/DEC-20261001-036.json` |
| DEC-20261001-037 | quality-gate | No dark patterns that stores would reject; the Designer seat must explicitly rule on the auto-advanc | `decisions/2026/10/DEC-20261001-037.json` |
| DEC-20261001-038 | autopilot-cycle | Approved brainstorm O1/P1 on autopilot - trust-only admin freshness label plus API-sourced version,  | `decisions/2026/10/DEC-20261001-038.json` |
| DEC-20261001-039 | architecture | Approved O1/P2 on autopilot - server-driven force-update gate with remote flag, kill switch, store f | `decisions/2026/10/DEC-20261001-039.json` |
| DEC-20261001-040 | autopilot-cycle | Ordered the full QA/review cycle for the 854 follow-ups run 100% automatically with the Brain. | `decisions/2026/10/DEC-20261001-040.json` |
| DEC-20261001-041 | autopilot-cycle | Approved O1/P3 on autopilot - bounded AI reply retry (timeout + jitter + idempotency), single provid | `decisions/2026/10/DEC-20261001-041.json` |
| DEC-20261001-042 | process | Re-verify the auto-created Parse Created-at field name, audit all usages, document the rule, and wri | `decisions/2026/10/DEC-20261001-042.json` |
| DEC-20261001-043 | scope | If invite links are truly useful, wire them into the referrer work; ensure utm_source is actually ca | `decisions/2026/10/DEC-20261001-043.json` |
| DEC-20261001-044 | scope | Read the ACRA library docs and source, implement the hashed crash reporter ID fully (hash-only, neve | `decisions/2026/10/DEC-20261001-044.json` |
| DEC-20261001-045 | process | Create one final consolidation task; apply all needed postfix fixes including concurrency; cover eve | `decisions/2026/10/DEC-20261001-045.json` |
| DEC-20261001-046 | process | Plan approval of the C1-C4 release-gate plan. | `decisions/2026/10/DEC-20261001-046.json` |
| DEC-20261001-047 | release | Make a new release per memory/skills/workflows, then run the full sweep on autopilot. | `decisions/2026/10/DEC-20261001-047.json` |
| DEC-20261001-048 | release | QA BDD waiver for release 1.56.0 - admin-dashboard/style/device scenarios deferred to a staging pass | `decisions/2026/10/DEC-20261001-048.json` |
| DEC-20261001-049 | architecture | Chose O3 for account deletion: soft-hide (deleted_at + 30-day pending_purge_at, images blanked, feed | `decisions/2026/10/DEC-20261001-049.json` |
| DEC-20261001-050 | architecture | Rejected the masquerade option for account deletion - deception, store risk, and moderation-data cor | `decisions/2026/10/DEC-20261001-050.json` |
| DEC-20261001-051 | process | Self-extract the unfixed production crashes via the admin-panel cloud functions (master key from .en | `decisions/2026/10/DEC-20261001-051.json` |
| DEC-20261001-052 | scope | Add status sort/filter to the admin crashes page; it can be its own separate task. | `decisions/2026/10/DEC-20261001-052.json` |
| DEC-20261001-053 | scope | Sort/filter crashes by status in the admin panel (accepted as its own task); autopilot locked. | `decisions/2026/10/DEC-20261001-053.json` |
| DEC-20261001-054 | process | Collect all remaining non-fixed crash logs from the admin panel, fix them in autopilot with a goal r | `decisions/2026/10/DEC-20261001-054.json` |
| DEC-20261001-055 | quality-gate | Mark guard-covered crash groups fixed post-ship; leave the Inflate (1.53) and OOM (1.36) singletons  | `decisions/2026/10/DEC-20261001-055.json` |
| DEC-20261001-056 | release | Make a new release based on the stored workflows after loading memory and skills. | `decisions/2026/10/DEC-20261001-056.json` |
| DEC-20261001-057 | release | QA BDD waiver for release 1.58.0 - standing BDD debt carried to a staging pass. | `decisions/2026/10/DEC-20261001-057.json` |
| DEC-20261001-058 | autopilot-cycle | Run the 1.58.0 release cut on autopilot. | `decisions/2026/10/DEC-20261001-058.json` |
| DEC-20261001-059 | scope | Wherever the app shows time, make it automatic - online status flips instantly and relative times ti | `decisions/2026/10/DEC-20261001-059.json` |
| DEC-20261001-060 | architecture | Implement the approved 2026-09-22 time-display design (single shared TimeTicker singleton, 60s, life | `decisions/2026/10/DEC-20261001-060.json` |
| DEC-20261001-061 | release | Plan approval for the time-display task. | `decisions/2026/10/DEC-20261001-061.json` |
| DEC-20261001-062 | architecture | Investigate enabling caching on the SDK forks; approved 3-layer scope - labeled-pin SDK cache (feeds | `decisions/2026/10/DEC-20261001-062.json` |
| DEC-20261001-063 | release | Phase-1 approval for the caching task - guardrails + kill-switch first, zero new cached reads. | `decisions/2026/10/DEC-20261001-063.json` |
| DEC-20261001-064 | process | Build a full context report (layouts + strings + styles/themes + colors), hand it to the UI/UX Desig | `decisions/2026/10/DEC-20261001-064.json` |
| DEC-20261001-065 | process | Plan approval for the UI/UX audit task. | `decisions/2026/10/DEC-20261001-065.json` |
| DEC-20261001-066 | scope | Expanded the UI/UX audit scope to align all bottom snackbars with the chat snackbar theming. | `decisions/2026/10/DEC-20261001-066.json` |
| DEC-20261001-067 | release | Load memory, skills and workflows to make a release; tracking = create a task file; version = 1.56.0 | `decisions/2026/10/DEC-20261001-067.json` |
| DEC-20261001-068 | process | Reopen order: move the release task to qa, inject the working-tree changes into it, then run it as Q | `decisions/2026/10/DEC-20261001-068.json` |
| DEC-20261001-069 | autopilot-cycle | Run the release under autopilot: do not ask, use the goal plugin, manage decisions, and go automatic | `decisions/2026/10/DEC-20261001-069.json` |
| DEC-20261001-070 | process | ZAC override - raw git add/commit/tag/push steps in the version-bump workflow memory are superseded  | `decisions/2026/10/DEC-20261001-070.json` |
| DEC-20261001-071 | architecture | Scope ruling: non-VIP Search shows a full lock screen; a VIP opens Search based on the fresh server  | `decisions/2026/10/DEC-20261001-071.json` |
| DEC-20261001-072 | autopilot-cycle | Locked autopilot for sprint 844-571-583, running one task at a time with 844 first. | `decisions/2026/10/DEC-20261001-072.json` |
| DEC-20261001-073 | scope | No special default Search filters - the default state must display all users with no implicit gender | `decisions/2026/10/DEC-20261001-073.json` |
| DEC-20261001-074 | process | Check the latest crash in the database and fix it even if small. | `decisions/2026/10/DEC-20261001-074.json` |
| DEC-20261001-075 | process | Always work and reply in English; translate Persian input internally. | `decisions/2026/10/DEC-20261001-075.json` |
| DEC-20261001-076 | scope | Manager authorized the full v2.0 improvement set (search, extraction, caching, SSRF, real errors, do | `decisions/2026/10/DEC-20261001-076.json` |
| DEC-20261001-077 | architecture | Expose blowsh only over MCP stdio transport, with no network ports. | `decisions/2026/10/DEC-20261001-077.json` |
| DEC-20261001-078 | tooling | Verify features only through Docker; never run the server on the host. | `decisions/2026/10/DEC-20261001-078.json` |
| DEC-20261001-079 | architecture | Minimal tool surface: fold PDF into fetch_web, keep enrich opt-in, add page arg. | `decisions/2026/10/DEC-20261001-079.json` |
| DEC-20261001-080 | quality-gate | Errors throw FetchError (isError:true); every new HTTP path passes the SSRF guard. | `decisions/2026/10/DEC-20261001-080.json` |
| DEC-20261001-081 | process | Backlog brainstorm output is non-functional guidance that governs but does not override the task. | `decisions/2026/10/DEC-20261001-081.json` |
| DEC-20261001-082 | release | Authorized the full registry + CI/CD pipeline, including the explicit push. | `decisions/2026/10/DEC-20261001-082.json` |
| DEC-20261001-083 | process | ZAC holds: stage only via the MCP tool; push only on explicit manager instruction. | `decisions/2026/10/DEC-20261001-083.json` |
| DEC-20261001-084 | quality-gate | Fast-path closure without the normal QA/review flow when the manager orders it. | `decisions/2026/10/DEC-20261001-084.json` |
| DEC-20261001-085 | release | Commit + tag + push as a single release sequence. | `decisions/2026/10/DEC-20261001-085.json` |
| DEC-20261001-086 | autopilot-cycle | Locked autopilot with a dedicated goal and a hard four-fix scope fence. | `decisions/2026/10/DEC-20261001-086.json` |
| DEC-20261001-087 | architecture | Chose persistent profile + warm reuse + larger viewport + guard detection. | `decisions/2026/10/DEC-20261001-087.json` |
| DEC-20261001-088 | autopilot-cycle | One-line autopilot lock order for a hardening task. | `decisions/2026/10/DEC-20261001-088.json` |
| DEC-20261001-089 | scope | A3 wide-screen goal transferred to a follow-up task; A3 stays unchecked in task 08. | `decisions/2026/10/DEC-20261001-089.json` |
| DEC-20261001-090 | quality-gate | Voice closure approval phrasing accepted as the closure gate. | `decisions/2026/10/DEC-20261001-090.json` |
| DEC-20261001-091 | scope | Authorized adding HTTP transport to blowsh (an own project). | `decisions/2026/10/DEC-20261001-091.json` |
| DEC-20261001-092 | release | Release 2.4.0 agreed; the task file carries the working-tree diff. | `decisions/2026/10/DEC-20261001-092.json` |
| DEC-20261001-093 | release | Full release run; push and pipeline stay Manager-owned. | `decisions/2026/10/DEC-20261001-093.json` |
| DEC-20261001-094 | process | Bundle tasks fully automatically and archive them; never purge. | `decisions/2026/10/DEC-20261001-094.json` |
| DEC-20261001-095 | scope | Reversed an earlier comment-only order; project_path work added to task 279 now. | `decisions/2026/10/DEC-20261001-095.json` |
| DEC-20261001-096 | process | Approved a plan without an explicit option pick; the honest default was chosen. | `decisions/2026/10/DEC-20261001-096.json` |
| DEC-20261001-097 | quality-gate | Fix pre-existing test failures before releasing. | `decisions/2026/10/DEC-20261001-097.json` |
| DEC-20261001-098 | process | Full system-workflow upgrade to new versions, plus the global install. | `decisions/2026/10/DEC-20261001-098.json` |
| DEC-20261001-099 | scope | Rate-limit rescue plugin fires only on free-tier 429s. | `decisions/2026/10/DEC-20261001-099.json` |
| DEC-20261001-100 | architecture | Chose one mode-parameterized prompt over two separate prompt files. | `decisions/2026/10/DEC-20261001-100.json` |
| DEC-20261001-101 | process | Approved the Designer plan (A1-A5) and routed it to implementation. | `decisions/2026/10/DEC-20261001-101.json` |
| DEC-20261001-102 | autopilot-cycle | Autopilot through QA/fix/review; closure keeps the explicit approval word. | `decisions/2026/10/DEC-20261001-102.json` |
| DEC-20261001-103 | autopilot-cycle | One-line autopilot lock order. | `decisions/2026/10/DEC-20261001-103.json` |
| DEC-20261001-104 | process | Ordered a single debug harness; legacy debug controllers deleted after proving no prod refs. | `decisions/2026/10/DEC-20261001-104.json` |
| DEC-20261001-105 | process | Adopt the classifier project-wide with no breaking changes. | `decisions/2026/10/DEC-20261001-105.json` |
| DEC-20261001-106 | process | Read-only audit of analytics claims; no code changes. | `decisions/2026/10/DEC-20261001-106.json` |
| DEC-20261001-107 | release | Releases follow the stored approved workflow; no invention, reversible until the release commit. | `decisions/2026/10/DEC-20261001-107.json` |
| DEC-20261001-108 | quality-gate | Standing order: reviewer technical APPROVED + PO_REVIEW_PENDING counts as Manager acceptance for clo | `decisions/2026/10/DEC-20261001-108.json` |
| DEC-20261001-109 | release | Closure approval bundled with release authorization. | `decisions/2026/10/DEC-20261001-109.json` |
| DEC-20261001-110 | architecture | One shared OpenCode instance + one MCP-server instance per server + one OpenChamber instance across  | `decisions/2026/10/DEC-20261001-110.json` |
| DEC-20261001-111 | architecture | Switch OpenCode to serve mode only, pin OpenChamber to the existing server, remove DCP plugin locall | `decisions/2026/10/DEC-20261001-111.json` |
| DEC-20261001-112 | scope | Add a full project and system-prompt audit against the latest OpenCode 2 docs to task 283 while reaf | `decisions/2026/10/DEC-20261001-112.json` |
| DEC-20261001-113 | process | Manager approved implementation of the task 283 plan. | `decisions/2026/10/DEC-20261001-113.json` |
| DEC-20261001-114 | scope | Change retry delay from 30s to 2s per Manager order; keep the plugin archived and unreferenced by an | `decisions/2026/10/DEC-20261001-114.json` |
| DEC-20261001-115 | scope | Update task goal, scope, acceptance criteria, and execution log to reflect delivered architecture: s | `decisions/2026/10/DEC-20261001-115.json` |
| DEC-20261001-116 | quality-gate | QA must judge the actual staged diff and explicitly state any truncation rather than rejecting solel | `decisions/2026/10/DEC-20261001-116.json` |
| DEC-20261001-117 | process | Require an architect implementation plan with no code changes. | `decisions/2026/10/DEC-20261001-117.json` |
| DEC-20261001-118 | process | Use only the Architect seat for this planning round; skip Designer and Programmer. | `decisions/2026/10/DEC-20261001-118.json` |
| DEC-20261001-119 | scope | Limit staged changes to repo docs, config, memory, skills, and tests; do not change server code. | `decisions/2026/10/DEC-20261001-119.json` |
| DEC-20261001-120 | process | Implementation must be driven solely by the XML with cited file paths and lines. | `decisions/2026/10/DEC-20261001-120.json` |
| DEC-20261001-121 | tooling | Limit re-emitted XML to 3500 tokens and omit prose outside the XML. | `decisions/2026/10/DEC-20261001-121.json` |
| DEC-20261001-122 | process | Manager approved final closure of task 282 after QA passed twice and Code Reviewer approved. | `decisions/2026/10/DEC-20261001-122.json` |
| DEC-20261001-123 | process | Reserved winner selection for the Manager and prohibited implementation during the seven-seat brains | `decisions/2026/10/DEC-20261001-123.json` |
| DEC-20261001-124 | architecture | Selected O1: one mode-parameterized prompt instead of two generated prompt variants (manual and auto | `decisions/2026/10/DEC-20261001-124.json` |
| DEC-20261001-125 | release | Approved final closure of task 281 after QA_PASSED and Code Reviewer APPROVED, authorizing the move  | `decisions/2026/10/DEC-20261001-125.json` |
| DEC-20261001-126 | scope | Assign Software Architect to produce an ordered implementation plan for task 280 covering two work i | `decisions/2026/10/DEC-20261001-126.json` |
| DEC-20261001-127 | process | Direct Software Architect to emit final ordered plan for both items, citing fed context, and explici | `decisions/2026/10/DEC-20261001-127.json` |
| DEC-20261001-128 | quality-gate | Assign QA Engineer to perform adversarial review of the factual diff for task 280, judging defects,  | `decisions/2026/10/DEC-20261001-128.json` |
| DEC-20261001-129 | quality-gate | Assign Code Reviewer to perform final technical review of task 280 after QA_PASSED, auditing the dif | `decisions/2026/10/DEC-20261001-129.json` |
| DEC-20261001-130 | release | Direct Senior Programmer to emit final closure XML for task 280, moving the task file from qa to com | `decisions/2026/10/DEC-20261001-130.json` |
| DEC-20261001-131 | architecture | Require every caller to pass its absolute project path per tool call with a clear field description. | `decisions/2026/10/DEC-20261001-131.json` |
| DEC-20261001-132 | architecture | Approve the Architect plan using OPTIONAL project_root with fallback, superseding the required-path  | `decisions/2026/10/DEC-20261001-132.json` |
| DEC-20261001-133 | quality-gate | Accept F2; leave both rollback boxes unchecked because full revert never ran; avoid overclaiming. | `decisions/2026/10/DEC-20261001-133.json` |
| DEC-20261001-134 | architecture | Dispute F4; treat the unit bodies as ground truth; no reboot-to-stdio risk exists. | `decisions/2026/10/DEC-20261001-134.json` |
| DEC-20261001-135 | scope | Agree F1/F5/F6/F7 remain open with the recorded reasons. | `decisions/2026/10/DEC-20261001-135.json` |
| DEC-20261001-136 | release | Accept window residuals M1-M4, M5 blowsh, M6 traceability, list-tool notice, and locking as O3 items | `decisions/2026/10/DEC-20261001-136.json` |
| DEC-20261001-137 | autopilot-cycle | In autopilot mode, do not use approval relay-pause; record the verdict and do not ask the human. | `decisions/2026/10/DEC-20261001-137.json` |
| DEC-20261001-138 | process | Zero-Autonomous-Commit holds; XML must never contain git add, git commit, or git push. | `decisions/2026/10/DEC-20261001-138.json` |
| DEC-20261001-139 | scope | Manager defined Task 278 scope: update repo docs and LLM.txt for new-user setup; update memory workf | `decisions/2026/10/DEC-20261001-139.json` |
| DEC-20261001-140 | process | Manager instructed that if repository data is needed before planning, the architect should return a  | `decisions/2026/10/DEC-20261001-140.json` |
| DEC-20261001-141 | quality-gate | Manager required a phased implementation plan containing file lists, per-phase verification, and rol | `decisions/2026/10/DEC-20261001-141.json` |
| DEC-20261001-142 | process | Manager ruled no second discovery round and ordered the final implementation plan covering four phas | `decisions/2026/10/DEC-20261001-142.json` |
| DEC-20261001-143 | scope | Manager requires that the existing opencode-server and OpenChamber service remain healthy during the | `decisions/2026/10/DEC-20261001-143.json` |
| DEC-20261001-144 | process | Manager permits returning a discovery task instead of an implementation plan when repository data is | `decisions/2026/10/DEC-20261001-144.json` |
| DEC-20261001-145 | scope | Manager defines the required sections of the implementation plan: per-server transport choice, local | `decisions/2026/10/DEC-20261001-145.json` |
| DEC-20261001-146 | quality-gate | Manager requires the final plan to be grounded in the discovery report and to cite file paths with l | `decisions/2026/10/DEC-20261001-146.json` |
| DEC-20261001-147 | quality-gate | Manager rules that a plan without citations to the fed context is considered ungrounded and unaccept | `decisions/2026/10/DEC-20261001-147.json` |
| DEC-20261001-148 | process | Manager provides the full discovery text and forbids the architect from asking for it again; the arc | `decisions/2026/10/DEC-20261001-148.json` |
| DEC-20261001-149 | scope | Manager requires the final implementation plan to include transport and port per server, supervision | `decisions/2026/10/DEC-20261001-149.json` |
| DEC-20261001-150 | quality-gate | Mandate the question tool for all approval gates (plan, review, closure) in cognitive-executor and s | `decisions/2026/10/DEC-20261001-150.json` |
| DEC-20261001-151 | process | Make brainstorming trigger evaluation automatic on every planning turn, including autopilot/XML path | `decisions/2026/10/DEC-20261001-151.json` |
| DEC-20261001-152 | release | Manager accepted PO review and approved task closure. | `decisions/2026/10/DEC-20261001-152.json` |
| DEC-20261001-153 | quality-gate | Ordered Code Reviewer to audit task 272 strictly against goal, acceptance criteria, and verification | `decisions/2026/10/DEC-20261001-153.json` |
| DEC-20261001-154 | process | Ordered re-audit because prior rejection was based on stale round-1 diff; reviewer must judge curren | `decisions/2026/10/DEC-20261001-154.json` |
| DEC-20261001-155 | release | Ruled that Code Reviewer approval is technical approval only and task must enter PO_REVIEW_PENDING p | `decisions/2026/10/DEC-20261001-155.json` |
| DEC-20261001-156 | quality-gate | Requested final review after Round 5 applied three documentation patches; verdict must be APPROVED w | `decisions/2026/10/DEC-20261001-156.json` |
| DEC-20261001-157 | quality-gate | Requested final confirmation after one-word AC hotfix; expected APPROVED with PO_REVIEW_PENDING or d | `decisions/2026/10/DEC-20261001-157.json` |
| DEC-20261001-158 | release | Manager accepted/approved task 272 for closure. | `decisions/2026/10/DEC-20261001-158.json` |
| DEC-20261001-159 | release | Ordered Senior Programmer to emit final closure XML because technical approval and manager acceptanc | `decisions/2026/10/DEC-20261001-159.json` |
| DEC-20261001-160 | tooling | Constrained closure XML to no shell and no git mv; use MCP commit path only because Hands lacks shel | `decisions/2026/10/DEC-20261001-160.json` |
| DEC-20261001-161 | process | Specified current task file path for closure XML operations. | `decisions/2026/10/DEC-20261001-161.json` |
| DEC-20261001-162 | quality-gate | Manager approved final closure and authorized resuming the goal. | `decisions/2026/10/DEC-20261001-162.json` |
| DEC-20261001-163 | process | Manager mandated that only exact phrases count as approval for closure. | `decisions/2026/10/DEC-20261001-163.json` |
| DEC-20261001-164 | scope | Manager scoped QA to skip formatting checks. | `decisions/2026/10/DEC-20261001-164.json` |
| DEC-20261001-165 | process | Manager forbade implementation during the planning turn. | `decisions/2026/10/DEC-20261001-165.json` |
| DEC-20261001-166 | process | Manager required logging the Brainstorm verdict and seat routing at execution start. | `decisions/2026/10/DEC-20261001-166.json` |
| DEC-20261001-167 | process | Manager reaffirmed role separation: Brain plans, Hands implement, Brain performs QA/review, autopilo | `decisions/2026/10/DEC-20261001-167.json` |
| DEC-20261001-168 | process | Manager selected Software Architect + Senior Programmer for planning and skipped UI/UX, QA, and Code | `decisions/2026/10/DEC-20261001-168.json` |
| DEC-20261001-169 | quality-gate | Manager instructed QA to hunt specific regression classes introduced by the new contract. | `decisions/2026/10/DEC-20261001-169.json` |
| DEC-20261001-170 | process | Manager mandated a machine-readable QA verdict format. | `decisions/2026/10/DEC-20261001-170.json` |
| DEC-20261001-171 | process | Manager instructed Code Reviewer to use PO_REVIEW_PENDING and include strict approval-phrase notice. | `decisions/2026/10/DEC-20261001-171.json` |
| DEC-20261001-172 | process | Manager specified exact closure steps and restricted commit path to custom_context_commit_and_clean_ | `decisions/2026/10/DEC-20261001-172.json` |
| DEC-20261001-173 | autopilot-cycle | Manager set the planning request under locked autopilot mode. | `decisions/2026/10/DEC-20261001-173.json` |
| DEC-20261001-174 | architecture | Settle the stacks/ folder: keep it only if a live consumer exists and report where; otherwise delete | `decisions/2026/10/DEC-20261001-174.json` |
| DEC-20261001-175 | process | Consolidate all related work into one task file. | `decisions/2026/10/DEC-20261001-175.json` |
| DEC-20261001-176 | process | Review all language/framework skills; for each, launch a research agent to gather internet data abou | `decisions/2026/10/DEC-20261001-176.json` |
| DEC-20261001-177 | quality-gate | Edit every stack skill so new projects enforce the strictest lint and available tooling for that sta | `decisions/2026/10/DEC-20261001-177.json` |
| DEC-20261001-178 | scope | Ensure complete coverage of all templates; nothing skipped. | `decisions/2026/10/DEC-20261001-178.json` |
| DEC-20261001-179 | scope | Accept long runtime and complete this task. | `decisions/2026/10/DEC-20261001-179.json` |
| DEC-20261001-180 | quality-gate | Primary objective: best code quality, best performance, least AI hallucination cost; design a system | `decisions/2026/10/DEC-20261001-180.json` |
| DEC-20261001-181 | process | Require a full seven-seat brainstorming report for task 269 before planning proceeds. | `decisions/2026/10/DEC-20261001-181.json` |
| DEC-20261001-182 | quality-gate | Gate implementation on Manager review and approval of the Blueprint before any file edits. | `decisions/2026/10/DEC-20261001-182.json` |
| DEC-20261001-183 | scope | Use an evidence-based gap-analysis approach: research external top-tool practices, weigh them agains | `decisions/2026/10/DEC-20261001-183.json` |
| DEC-20261001-184 | process | Reserve conflict C1 for explicit Manager choice; do not auto-switch language or auto-resolve it duri | `decisions/2026/10/DEC-20261001-184.json` |
| DEC-20261001-185 | autopilot-cycle | Authorize full automatic planning and implementation of A1 and A2 without intermediate approval. | `decisions/2026/10/DEC-20261001-185.json` |
| DEC-20261001-186 | autopilot-cycle | Confirm autopilot locked mode: plan through Brain then implement without separate plan-approval paus | `decisions/2026/10/DEC-20261001-186.json` |
| DEC-20261001-187 | quality-gate | Require auditable brainstorm trigger line and hard rule for cross-disciplinary + hard-to-reverse tas | `decisions/2026/10/DEC-20261001-187.json` |
| DEC-20261001-188 | scope | Repair fragment 11 to name seven seats, make step 2 conditional consistent with fragment 12, and fix | `decisions/2026/10/DEC-20261001-188.json` |
| DEC-20261001-189 | scope | Forbid new brainstorm skill, always-on brainstorming, and edits to historical files. | `decisions/2026/10/DEC-20261001-189.json` |
| DEC-20261001-190 | release | Require system-prompt regeneration, version bump, lint sync, and CHANGELOG Unreleased entry. | `decisions/2026/10/DEC-20261001-190.json` |
| DEC-20261001-191 | quality-gate | Direct QA to adversarially test five specific consistency and safety checks and produce machine verd | `decisions/2026/10/DEC-20261001-191.json` |
| DEC-20261001-192 | quality-gate | Direct Code Reviewer to audit standards compliance, rebuild/version bump, test pin legitimacy, scope | `decisions/2026/10/DEC-20261001-192.json` |
| DEC-20261001-193 | autopilot-cycle | Under the full-automatic standing order, a reviewer technical APPROVED with PO_REVIEW_PENDING is tre | `decisions/2026/10/DEC-20261001-193.json` |
| DEC-20261001-194 | scope | Deferred audit findings R3-R7 are out of scope for Task 265; do not expand scope. | `decisions/2026/10/DEC-20261001-194.json` |
| DEC-20261001-195 | quality-gate | QA must adversarially test the HTTPS guard and timeout changes, explicitly checking for guard bypass | `decisions/2026/10/DEC-20261001-195.json` |
| DEC-20261001-196 | process | Code Reviewer may grant technical approval, but final closure requires the Manager's explicit words. | `decisions/2026/10/DEC-20261001-196.json` |
| DEC-20261001-197 | release | Manager approves closure of Task 265. | `decisions/2026/10/DEC-20261001-197.json` |
| DEC-20261001-198 | process | Execute the closure sequence exactly once: move task file to tasks/completed/, set Status: closed, u | `decisions/2026/10/DEC-20261001-198.json` |
| DEC-20261001-199 | quality-gate | Assigned QA engineer to perform adversarial testing on task 264 with specific probe angles and a ver | `decisions/2026/10/DEC-20261001-199.json` |
| DEC-20261001-200 | quality-gate | Assigned Code Reviewer to perform the final review of task 264 with specified angles and verdict opt | `decisions/2026/10/DEC-20261001-200.json` |
| DEC-20261001-201 | release | Manager authorized closure of task 264 via the message 'Approved for clousre' (typo for 'Approved fo | `decisions/2026/10/DEC-20261001-201.json` |
| DEC-20261001-202 | autopilot-cycle | Adopt autopilot baseline mode for new tasks: plan first, then fix automatically, then extract the Ma | `decisions/2026/10/DEC-20261001-202.json` |
| DEC-20261001-203 | process | For task 263, request Software Architect and Senior Programmer seats; skip UI/UX Designer, Sprint St | `decisions/2026/10/DEC-20261001-203.json` |
| DEC-20261001-204 | scope | Keep the transcript-cap and config-validation work inside existing task 263; do not create a new tas | `decisions/2026/10/DEC-20261001-204.json` |
| DEC-20261001-205 | tooling | Adopt DECISION_TRANSCRIPT_MAX_CHARS with default 131072 characters, blank-means-unset, and ValueErro | `decisions/2026/10/DEC-20261001-205.json` |
| DEC-20261001-206 | quality-gate | Truncate oversized joined transcript text and append an explicit marker stating the dropped characte | `decisions/2026/10/DEC-20261001-206.json` |
| DEC-20261001-207 | architecture | Apply the transcript cap before prompt construction; send the capped text; allow the cache key to ke | `decisions/2026/10/DEC-20261001-207.json` |
| DEC-20261001-208 | quality-gate | Include _get_decision_temperature() in scope and make it raise ValueError on malformed or out-of-ran | `decisions/2026/10/DEC-20261001-208.json` |
| DEC-20261001-209 | process | Skip missing DESIGN.md, docs/architecture.md, and docs/data_model.md; treat the provided default as  | `decisions/2026/10/DEC-20261001-209.json` |
| DEC-20261001-210 | quality-gate | Set seven acceptance criteria for task 263 covering bounded transcript, truncation note, loud config | `decisions/2026/10/DEC-20261001-210.json` |
| DEC-20261001-211 | scope | Exclude attachment caps, numbered parts/resume, append-only transcript storage, diff-extractor work, | `decisions/2026/10/DEC-20261001-211.json` |
| DEC-20261001-212 | process | Proceed to the final implementation plan; do not ask further questions; choose and state consistent  | `decisions/2026/10/DEC-20261001-212.json` |
| DEC-20261001-213 | quality-gate | Run an adversarial QA pass on task 263 before review. | `decisions/2026/10/DEC-20261001-213.json` |
| DEC-20261001-214 | quality-gate | Run the Code Reviewer gate after QA to audit the change set against goal and acceptance criteria. | `decisions/2026/10/DEC-20261001-214.json` |
| DEC-20261001-215 | quality-gate | Re-review task 263 after the round-1 documentation fix. | `decisions/2026/10/DEC-20261001-215.json` |
| DEC-20261001-216 | process | In autopilot, the Hands must consult all Brain personas (QA, Planner, Designer, Strategist, Programm | `decisions/2026/10/DEC-20261001-216.json` |
| DEC-20261001-217 | process | Manager approved merging the first reviewed profile promotion into the personal repo (clean migrate) | `decisions/2026/10/DEC-20261001-217.json` |
| DEC-20261001-218 | process | Task closure runs one by one per the Kanban protocol (verify, git mv to completed, commit_and_clean_ | `decisions/2026/10/DEC-20261001-218.json` |
| DEC-20261001-219 | process | GitHub issues linked to closed tasks are closed with a closing comment carrying the feature commit h | `decisions/2026/10/DEC-20261001-219.json` |
| DEC-20261001-220 | tooling | Open a new task for the Brain empty-output root cause: MCP-side retry hint plus stronger MCP-server  | `decisions/2026/10/DEC-20261001-220.json` |
| DEC-20261001-221 | release | No new task and no new release for the .env version skew, only a quick env update. | `decisions/2026/10/DEC-20261001-221.json` |
| DEC-20261001-222 | process | Approved updating .env CANDO_BACKEND_VERSION to 1.52.0 as a quick fix with no task file. | `decisions/2026/10/DEC-20261001-222.json` |
| DEC-20261001-223 | process | Approved creating milestone-33 summary and archiving completed tasks 812-815. | `decisions/2026/10/DEC-20261001-223.json` |
