# Manager Profile (authoritative copy — personal repo)

> Rebuilt FROM SCRATCH on 2026-10-01 per explicit Manager order, aggregated from
> all **326** decision records in this repo by `scripts/compile_profile.py`.
> This is the cross-project personality source; the per-project `.opencode/decisions/`
> caches were migrated here and cleaned on the same order.
> Generated sections are derived from records — edit them via `propose_profile_evolution`.

## Snapshot

- Decisions: **326** (2026-09: 103 | 2026-10: 223)
- Projects: cognitive-lead-hq 170 | dumble 79 | apex 24 | v2ray-to-subs 24 | blowsh-mcp 21 | Cando 5 | tailnet-us-egress 3
- Fidelity: verbatim 214, reconstructed 69, unset 43 | Mode: manual 272, unset 43, autopilot 11 | Scope: episode 279, unset 43, standing 4
- Session-linked: 152/326

### Category distribution

- process: 117
- scope: 48
- quality-gate: 45
- architecture: 42
- release: 37
- autopilot-cycle: 22
- tooling: 14
- other: 1

## Baseline behavioral guidelines

- Decide in the open: state the rationale and the rejected alternatives, not just the verdict.
- Prefer reversible decisions; mark irreversible ones and slow down for them.
- Keep the audit trail: every ruling links to its verbatim quote and session.
- Gate anything that learns or publishes (samples, releases, identity) on the manager's word.
- Owner decisions are final once recorded; corrections are new records, never edits.
- All reasoning and output stay in English, even when the manager dictates in Persian.

## Architectural preferences

- **Authoritative personal repo over project-local stores** — one personality source across
  all projects; per-project `.opencode/decisions/` is only a cache/fallback.
- **Append-only everywhere** — transcripts, decisions, sessions; history is never rewritten.
- **Deterministic, testable cores** — pure functions, stdlib first, network only at the edges.
- **Single source per concept** — one OpenCode instance, one store, one canonical doc.
- **Simple JSON / plain files over frameworks** where a framework adds no determinism.

## Decision heuristics

- **Autopilot means zero contact** — the manager sees only Relay questions, final verdicts,
  and hard blockers; ferrying work through the manager is a bug.
- **Hard gates stay hard** — approval, QA, and closure gates never auto-continue on timeout.
- **ZAC is absolute** — no autonomous `git add/commit/push`; closure commits only via the
  sanctioned MCP commit path.
- **Closure is word-gated** — only the exact phrases "Approved for closure" or "Close task";
  replayed past rulings never satisfy it.
- **Evidence over claims** — approvals cite file paths and lines; QA and review judge the
  actual diff and the machine verdict, never a summary.
- **Scope discipline** — deferred findings stay out of scope; adjacent hardening becomes a
  new task, not scope creep.
- **Fail loud, never silent** — degraded transports return explanatory errors, config errors
  raise, empty results are surfaced.
- **RTK-first verification is standing** — test-verdict runs wrap with `rtk test`.

## Standing orders

- DEC-20260914-015: Standing full-autopilot order for the Telegram/Portal engine-speed work: parallel lanes allowed, Brain (Senior Programmer) decides design iteratively,
- DEC-20260915-001: Manager approved fixing all brainstorm gaps via the Hands on autopilot.
- DEC-20260915-002: Manager ordered Task 232 implementation on autopilot with Brain planning.
- DEC-20260916-003: Standing order: wrap all test-verdict runs with rtk test (token collapse, exit code preserved); failures keep full output via rtk recall.
- DEC-20260918-004: Pre-authorized plan auto-approval is valid only on explicit Manager order; announce and record the lock.
- DEC-20260918-005: On autopilot, QA and review run machine-to-machine; Manager sees only relay questions and final verdict.
- DEC-20261001-026: Locked autopilot and ordered the admin chat-viewer tasks completed fully; every UI/UX part must get a Senior UI/UX Designer verdict and follow current
- DEC-20261001-038: Approved brainstorm O1/P1 on autopilot - trust-only admin freshness label plus API-sourced version, no metric changes.
- DEC-20261001-040: Ordered the full QA/review cycle for the 854 follow-ups run 100% automatically with the Brain.
- DEC-20261001-041: Approved O1/P3 on autopilot - bounded AI reply retry (timeout + jitter + idempotency), single provider, no second vendor yet.
- DEC-20261001-058: Run the 1.58.0 release cut on autopilot.
- DEC-20261001-069: Run the release under autopilot: do not ask, use the goal plugin, manage decisions, and go automatic.
- DEC-20261001-072: Locked autopilot for sprint 844-571-583, running one task at a time with 844 first.
- DEC-20261001-086: Locked autopilot with a dedicated goal and a hard four-fix scope fence.
- DEC-20261001-088: One-line autopilot lock order for a hardening task.
- DEC-20261001-102: Autopilot through QA/fix/review; closure keeps the explicit approval word.
- DEC-20261001-103: One-line autopilot lock order.
- DEC-20261001-137: In autopilot mode, do not use approval relay-pause; record the verdict and do not ask the human.
- DEC-20261001-173: Manager set the planning request under locked autopilot mode.
- DEC-20261001-185: Authorize full automatic planning and implementation of A1 and A2 without intermediate approval.

## Ruling clusters (grounded in records)

### Autopilot & zero-contact operation

Representative records: DEC-20260913-001, DEC-20260913-003, DEC-20260913-008, DEC-20260913-010, DEC-20260913-017, DEC-20260913-019, DEC-20260913-020, DEC-20260913-022

### Closure & approval gating

Representative records: DEC-20260913-006, DEC-20260917-005, DEC-20260917-011, DEC-20260917-013, DEC-20260925-001, DEC-20260925-002, DEC-20260913-001, DEC-20260913-017, DEC-20260913-023, DEC-20260913-025, DEC-20260914-011

### Zero-Autonomous-Commit (ZAC)

Representative records: DEC-20260913-012, DEC-20260913-017, DEC-20260913-023, DEC-20260913-025, DEC-20260914-006, DEC-20260916-004, DEC-20260917-003, DEC-20260917-004, DEC-20260913-005, DEC-20260913-013, DEC-20260913-014, DEC-20260913-016, DEC-20260913-020

### QA / reviewer verdicts & evidence

Representative records: DEC-20260913-011, DEC-20260913-018, DEC-20260914-003, DEC-20260914-011, DEC-20260914-015, DEC-20260916-003, DEC-20260913-002, DEC-20260913-019, DEC-20260913-025, DEC-20260917-004, DEC-20260927-002, DEC-20260927-004

### Scope control & task discipline

Representative records: DEC-20260913-012, DEC-20260916-002, DEC-20260917-014, DEC-20261001-031, DEC-20261001-036, DEC-20261001-062, DEC-20261001-194, DEC-20261001-208, DEC-20261001-211

### Architecture & store design

Representative records: DEC-20260925-007, DEC-20261001-139, DEC-20261001-142

### Docs / prompt / system sync

Representative records: DEC-20260916-002, DEC-20260920-003, DEC-20260927-011, DEC-20260927-012, DEC-20261001-030, DEC-20261001-044, DEC-20260913-004, DEC-20260913-007, DEC-20260913-010, DEC-20260913-012, DEC-20260913-026, DEC-20260916-005

### Release & milestone management

Representative records: DEC-20260913-013, DEC-20261001-045, DEC-20261001-046, DEC-20261001-047, DEC-20261001-048, DEC-20261001-056, DEC-20261001-093, DEC-20261001-223

## Full ruling index (by category)

### process (117)

- **DEC-20260912-001** — Public-default secret handling: record only repo display name (active_root), never absolute path; full path stays in local stderr only.
  > This story explicitly marks the repo public — public-default applies. The full absolute path WILL NOT be included in any record — active_root stores only the repo display name; the full path appears o
- **DEC-20260912-002** — Every stored decision must pass sanitize_text on all free-text fields plus a verify_clean gate; any surviving sensitive pattern raises and nothing is written (n
  > Scrub gate fail-closes on EVERY root: free-text fields are sanitized, and if any sensitive pattern survives sanitizing, nothing is written — there is no bypass flag.
- **DEC-20260912-003** — Decision stores are append-only: corrections are new tombstone records, never edits or deletes of stored history.
  > Append-only on both ends: corrections are new tombstone records, never edits or deletes.
- **DEC-20260913-001** — Manager orders Hands to run the QA-review autopilot cycle autonomously and promises closure approval on a pass.
  > خودت سایکل اتوپایلت رو برای این تسک اجرا کن اگر تایید شد منم تایید میکنم تسک رو ببند.
- **DEC-20260913-003** — In autopilot/automatic mode the Hands must call brain_turn directly and never route questions or XML through the manager (no-ferry rule).
  > همین‌طور یه باگ دیدم، الان توی حالت اتو پایلت هستی، چرا به من داری حرف می‌زنی؟ تو باید دوباره خودت برین رو صدا بزنی، کلاً توی کاگنیتیو اگزیکیوتر وقتی توی حالت خودکار هستی دیگه چیزی از من نپرس.
- **DEC-20260913-004** — Task numbers live ONLY in code comments, CHANGELOG, task files, history archives, and HTML comments — never in prompt-facing Markdown prose (anti-hallucination 
  > توی فایل‌های مارک‌دان و مخصوصاً فایل‌های مارک‌دانی که برای پرامپت قراره استفاده بشه، به شماره تسک‌ها هم ریفرنس می‌دی. این کار باعث ایجاد توهم برای هوش مصنوعی می‌شه و جالب نیست.
- **DEC-20260913-005** — Push is Manager-owned (ZAC): manager pushes with git, Hands verifies remotely afterward (push-then-verify loop).
  > پوش کردم چک کن.
- **DEC-20260913-006** — Closure approvals with obvious voice-to-text typos (clouse, Ckosetask, Appriveed) are accepted as valid approval words.
  > Approve for clouse
- **DEC-20260913-008** — The memorized QA-review cycle (QA persona, then reviewer persona, then report) is the standard reusable autopilot for task verification.
  > حالت اتوپایلت رو برای این تسک اجرا کن.
- **DEC-20260913-010** — Manager orders recurring-style self-judgment runs: fresh task, Brain Architect planning + brainstorm + blowsh web research, then full autopilot QA/reviewer loop
  > می‌خوام خودت رو قضاوت کنی؛ سیستمی که برات الان طراحی کردم خودت می‌خوام اون رو قضاوت کنی. مثلاً یک تسک از نو شروع کن، تسک قضاوت‌کردن خودت و پرسوناهای داخل سیستم پرامپت. باید اول برنامه‌ریزی کنی براش با
- **DEC-20260913-011** — In-flight findings go to a side note (/tmp) during the run, not into the task file; only final verdicts land in the Execution Log.
  > بهتره یک گوشه یادداشت کنی
- **DEC-20260913-013** — Every future release must archive tasks/completed/ via the archive-tasks skill as part of the release
  > لطفاً تسک‌های فعلی رو هم آرکایو کن. نیاز نیست ریلیز جدید بسازی، همین ریلیزی که انجام دادی همه‌چی اوکیه، فقط تسک‌های فعلی رو هم آرکایو کن. از این به بعد هر موقع خواستیم ریلیز بزنیم باید تسک‌ها آرکایو ب
- **DEC-20260913-014** — Every Telegram-synced task gets a GitHub issue; skills and project memory must be loaded and followed during the sync.
  > sync telegram and create tasks all need github load skills and memories and follow
- **DEC-20260913-015** — Manager's one-word 'All' selects every proposed candidate (used for the 602/604/605 sync batch).
  > All
- **DEC-20260913-016** — GitHub issues are valid task sources alongside Telegram; issue 9 became Task 214.
  > we have a also a isssue .../issues/9 create a task file for it too.
- **DEC-20260913-017** — Standing autopilot order for the sprint: implement 211-214 in wave order with Brain QA+review each, under a session goal, zero approval pauses, no auto-commit, 
  > Uh, I upload this plan too. Please use the autopilot mode and start it working. Also, please create a goal for this. And continue until the finish.
- **DEC-20260913-018** — Empty Brain REPORT output is a transport flake, never a verdict: retry once lean, then escalate. Third attempt succeeded.
  > Retry
- **DEC-20260913-020** — Telegram message 609 became Task 216 (separate personal decisions repo) via the standard sync pipeline, then autopilot-solved to best quality. Established the s
  > من توی تلگرام یه تسک جدید تعریف کردم، اون رو هم تلگرام رو سینک کن، اسکیل‌ها بارگذاری کن، تلگرام رو سینک کن، ایشو گیت‌هاب براش بزن، بعد اونم دقیقاً اتوپایلت حلش کن، بهترین حالت ممکن.
- **DEC-20260913-022** — One-word 'Approved' after a 3-step plan authorizes full autopilot implementation under the Direct Input protocol.
  > Approved
- **DEC-20260913-023** — Closure chain: close META 219, run global install upgrade, restart, create the personal decisions repo, migrate local records into it, prune them locally. Commi
  > حله، اگه اوکیه منم قبول دارم، ببند. تسک رو ببندیم، بعد که بستی گلوبال سینک رو انجام بده، به من بگو ریستارت رو انجام بدم که بریم ریپوی دیسیژن رو بسازیم و همین دیسیژن‌هایی که داخل همین ریپو هستن رو مایگ
- **DEC-20260913-024** — Nothing destructive (prune/push/restart) happens before the Manager sees the worktree status first.
  > قبلش استتوس گیت رو بررسی کن، به من بگو.
- **DEC-20260913-026** — 'Global sync' means the global install upgrade per memory workflows/global-install-upgrade.md: repo is source of truth, audit → copy → orphans → verify → smoke,
  > توی مموری من نوشتم که چگونه می‌تونیم گلوبال رو سینک کنیم، منظورم آپگرید گلوبال رو انجام بدیم.
- **DEC-20260913-027** — Batch approval authorizes migrating all 13 local DEC records; each carries migrated_from provenance (display-name only, no abs paths — public-repo guard).
  > approved, migrate all 13
- **DEC-20260914-001** — Hands must always reply in English, never in Persian.
  > never tell me farsi! follow your rules
- **DEC-20260914-003** — Standing full-autopilot order: run end-to-end with zero questions until the Manager speaks.
  > Full-auto scan: create the goal, hunt bottlenecks and real profitable signals, use Brain, personas, decisions and skills, never ask questions until I tell you otherwise. (Reconstructed from session su
- **DEC-20260914-004** — socat port-forward work on the manager script needs no Kanban task file.
  > no task required
- **DEC-20260914-006** — Task 221 absorbs port/forward-script worktree changes; .forward.pid is gitignored runtime state.
  > create a task, absorb the working tree, gitignore the pid file (Reconstructed from session summary; exact wording lost to context compression.)
- **DEC-20260914-011** — Restart handshake: Hands restarts, Manager tests, result comes back before closure.
  > firest restart server for me wait me to test i will tell you back
- **DEC-20260914-012** — A-vs-B choice delegated to Brain + stored decisions; then run autonomously to end-of-day closeout.
  > Ask brain and check my desctions to choose and contune until end
- **DEC-20260914-014** — Goal conflict resolved with option 3: old 5%-profit goal retired into the Portal scan-speed goal via update_goal (objective rewrite + resume), no new goal creat
  > [reconstructed] Manager chose option 3 for the goal conflict: retire the old goal into the new Portal-speed goal.
- **DEC-20260914-016** — Ops via curl only: add the 10 cheapest uncovered collections as EXPLORER_BROAD filters (both markets, 10 TON cap, 5% target), enable AUTO_SCAN_ENABLED via /conf
  > Add most cheap items as broad sigbal and snable auto scanner so i want to see engine work make sure resgatt lages verson ans ads them using curl and update settings using curl
- **DEC-20260915-003** — Manager approved closure of Task 232.
  > منم اوکی‌ام، تسک رو ببند.
- **DEC-20260915-004** — Manager approved closure of Task 233.
  > close
- **DEC-20260916-001** — Manager approves the 226 Brain plan with assumptions A1 keep buying concurrency, A2 bias never-double-bill, A3 triple charge shares the 03:12:04 root; Q3/Q5/Q6 
  > Approved
- **DEC-20260916-002** — Full-autopilot order for 228: Hands executes the Brain's two-pass docs audit end to end, stopping only for hard blockers and closure approval.
  > solve it yourself with Brain advice, 100 autopilot
- **DEC-20260916-004** — QA plus code-reviewer gate order for the 229 cooldown-proof endpoint work (uncommitted debug-controller probe).
  > ask qa and code reviewer for our task.
- **DEC-20260916-005** — File the HQ umbrella issue (became issue 15) with Brain reflect on two bridge bugs, demanding rtk-in-system-prompt plus a fix for missing decision auto-extracti
  > create issue at the congtive project of our issues. with details ask brain for `reflect` it help you.tell inside issue we need add rtk usage in system prompt too. and fix manager desctions why not aut
- **DEC-20260917-002** — Lock the task in autopilot and drive it end-to-end without human pauses, except hard blockers and Relay questions.
  > run on autopilot to full completion
- **DEC-20260917-007** — Run the task under the stored standing order manager/full_automatic_mode: full-automatic execution with zero questions to the Manager, because the Manager has n
  > Full-automatic mode applies (stored order `manager/full_automatic_mode`, zero questions). Manager has no session access.
- **DEC-20260917-008** — Every step of the task routes through the Brain seat sequence: Brain plans, Hands implement, Brain QA, Brain review; nothing bypasses a seat.
  > Work task-by-task with Brain on every step: Brain plans, hands implement, Brain QAs, Brain reviews.
- **DEC-20260917-010** — Bug and learning reporting defaults to decision records; when the record tools themselves are the broken components, task-file logs and messages are the accepte
  > Report bugs and learnings via decision records, or via task-file logs and messages when the record tools themselves are broken.
- **DEC-20260917-012** — Run the task under locked full-automatic mode with zero questions to the manager, and route every step through the Brain (plan, instruct, implement, QA, review)
  > Full-automatic mode applies (stored order `manager/full_automatic_mode`, zero questions). Manager has no session access. Work with Brain on every step: Brain plans and instructs, hands implement, Brai
- **DEC-20260917-015** — Standing order: the agent must never think, reason, or respond in any language but English, even when the Manager writes in Persian; every non-English or noisy 
  > The agent must never respond, think, or reason in any language other than English. The input-validation pipeline is priority one for every non-English or noisy input. (Reconstructed from the closed ta
- **DEC-20260917-016** — Save every Manager decision from the session as a manager decision record and update the manager-decision profile sample.
  > خب همهی تصمیمات من توی سیشن رو ذخیره کردی به عنوان منیجر دیسیژن و پروفایل من رو هم آپدیت کن، پروفایل منیجر دیسیژن من رو.
- **DEC-20260918-002** — Report baseline-flow gaps as upstream HQ issues with full evidence; persist decisions via the decision server.
  > create issues at the github with enough context and details for why baseline flow not full automatic. then save my all desctions. using manager decideations
- **DEC-20260918-003** — Telegram sync runs without GitHub issues unless explicitly asked.
  > Load memory about sync telegram, then follow them, no GitHub issue needed
- **DEC-20260919-001** — Execute Task 259 under full automatic autopilot: ask no questions, consult all Brain personas via brain_turn, verify RTK-first, and close the task and GitHub is
  > create a task from https://github.com/mokhtarabadi/cognitive-lead-hq/issues/20 and fix and close issue and task (use auto pilot mode)
- **DEC-20260920-001** — On autopilot, plan through the Brain first and then implement automatically without pausing for a separate plan approval.
  > a new task need and use auto pilot baseline mode so first plan them then fix automaticall, at end extraxt my desctions from old and new tsak and save them
- **DEC-20260920-004** — Run the new analytics task through the autopilot baseline cycle, using Brain, Blues search, and manager decisions to complete it.
  > Then search and 'collect data' and put it into the autopilot baseline cycle, and with the help of Brain and the Blues search engine and the manager's decisions, complete this section—this new task.
- **DEC-20260927-004** — Search-tab VIP bug: diagnose root cause vs working activity hub, explain, then file a backlog task (became task 844).
  > اون داره خوب کار می‌کنه. فرقشو سعی کن پیدا کنی و به من توضیح بده و بعد از اینکه کامل فهمیدیش، تسکش کن و توی بک‌لاگ بنویسش.
- **DEC-20260927-008** — New balancer-adjacent features (e.g. 429 pre-flight check) must be env-configurable and toggleable, never hardcoded.
  > (Persian, paraphrased) این قابلیت باید کانفیگورابل باشد، با env var یا مشابه، قابل on/off، هرگز هاردکد نشود
- **DEC-20260927-009** — Small timer-interval tweaks do not need Kanban task tracking; change and reload directly.
  > (Persian, paraphrased) اینتروال را همین حالا زیاد کن، برای این کار تسک لازم نیست
- **DEC-20261001-002** — Ad-hoc operational changes against systemd units need no upfront Kanban tracking; the task file is created retroactively.
  > if need and can just change systemd unit
- **DEC-20261001-005** — For quick one-shot fixes, implement first without Kanban tracking, then create the task file and close it retroactively.
  > Task it and close
- **DEC-20261001-016** — Tasked work runs the full autopilot stages including Brain-driven QA and Brain reviewer.
  > create the task and run the autopilot stages including Brain QA and Brain reviewer.
- **DEC-20261001-021** — Approved a read-only code audit (no code changes) to verify the pasted admin-panel analytics claims before acting.
  > check codes and see if the claims in the pasted report are real
- **DEC-20261001-024** — Mandated a strictly read-only production export: no writes, deletes, restarts or config changes; download from prod only, render/store artifacts on staging or l
  > Strictly read-only on prod: no writes, no deletes, no restarts, no config changes.
- **DEC-20261001-033** — Run referrer implementation in autopilot with the Brain, then inject the Manager's words into the task file and hand it to the QA seat; QA loop runs in autopilo
  > با حالت اتو پایلت، با کمک برین، پیاده‌سازی رو انجام بده
- **DEC-20261001-034** — Dashboard-watch order: keep the analytics/dashboard/admin-panel data showing install sources correctly; report back if a change is needed.
  > حواست به داده‌های آنالیز باشه، و داده‌های توی داشبورد و ادمین پنل که سورس‌ها و اینا رو دیگه درست نمایش بده.
- **DEC-20261001-042** — Re-verify the auto-created Parse Created-at field name, audit all usages, document the rule, and write it into project rules if needed.
  > re-verify the exact field name, audit all usages (migration/CLP/index scripts and elsewhere), document it, and write it into project rules if needed.
- **DEC-20261001-045** — Create one final consolidation task; apply all needed postfix fixes including concurrency; cover every task file in the patch; full-team review; autopilot; comp
  > خب ببین یک task ایجاد کن و postfix apply concurrency هایی که نیازه رو انجام بده... کل تیم هم بررسی کنن حالت autopilot اتوماتیک، کامل کامل انجامش بده، می‌خوام release بعدی رو بزنیم بیرون.
- **DEC-20261001-046** — Plan approval of the C1-C4 release-gate plan.
  > Approved
- **DEC-20261001-051** — Self-extract the unfixed production crashes via the admin-panel cloud functions (master key from .env), task them, fix them, then mark the truly-fixed groups fi
  > خودت سعی کن از سرور پروداکشن اونهایی که فیکس نشده رو از توی ادمین پنل استخراج کنی... بعد هم که انجام شد بری اونهایی که واقعاً فیکس شدن رو توی ادمین پنل تیکشون رو بزنی فیکس.
- **DEC-20261001-054** — Collect all remaining non-fixed crash logs from the admin panel, fix them in autopilot with a goal required.
  > collect all other non fixed logs from admin panel check more logs i see some non fixed crached i mean crached, create new task and fix them in auto pilot too. a goal required
- **DEC-20261001-064** — Build a full context report (layouts + strings + styles/themes + colors), hand it to the UI/UX Designer seat, find gaps vs DESIGN.md, and polish the UI/UX; full
  > build a full context report of all XML layouts plus strings plus styles/themes plus colors, hand it to the UI/UX Designer seat, find the gaps of the current interface versus DESIGN.md, and polish the 
- **DEC-20261001-065** — Plan approval for the UI/UX audit task.
  > Approved
- **DEC-20261001-068** — Reopen order: move the release task to qa, inject the working-tree changes into it, then run it as QA via the brain tool.
  > move tasks/completed/843-cut-release-1-56-0.md to qa in kanban, then inject all our working tree changes to it using tools, then as qa using brain tool
- **DEC-20261001-070** — ZAC override - raw git add/commit/tag/push steps in the version-bump workflow memory are superseded by Zero-Autonomous-Commit; tag, push and deploy stay Manager
  > the version_bump_workflow memory lists raw git add -A / git commit / git tag / git push steps. Those are superseded by Zero-Autonomous-Commit.
- **DEC-20261001-074** — Check the latest crash in the database and fix it even if small.
  > the app crashed during the Task 852 device retest; check the latest crash in the database and fix it even if small.
- **DEC-20261001-075** — Always work and reply in English; translate Persian input internally.
  > Persian prompts translated to English internally; thinking and responses in English (per manager instruction).
- **DEC-20261001-081** — Backlog brainstorm output is non-functional guidance that governs but does not override the task.
  > Interpret the embedded brainstorming_session as non-functional guidelines that govern but do not override this task.
- **DEC-20261001-083** — ZAC holds: stage only via the MCP tool; push only on explicit manager instruction.
  > ZAC applies: staging via custom_context_stage_and_inject_diff; commit/push only because the Manager explicitly instructed the push.
- **DEC-20261001-094** — Bundle tasks fully automatically and archive them; never purge.
  > Manager requested fully automatic bundling with archive (not purge).
- **DEC-20261001-096** — Approved a plan without an explicit option pick; the honest default was chosen.
  > Manager approved the plan without picking O1/O2; O2 chosen as the honest option since no authoritative date exists.
- **DEC-20261001-098** — Full system-workflow upgrade to new versions, plus the global install.
  > create a task and start full upgrade our system workflow and everything to new versions. search and find everyplace and upgrade. finally when done. upgrade our global installation too.
- **DEC-20261001-101** — Approved the Designer plan (A1-A5) and routed it to implementation.
  > Manager approved via question tool; routed to Senior Programmer XML, executed verbatim.
- **DEC-20261001-104** — Ordered a single debug harness; legacy debug controllers deleted after proving no prod refs.
  > Debug harness per manager order: deleted all 5 legacy debug controllers + 2 test files (no prod/UI refs found).
- **DEC-20261001-105** — Adopt the classifier project-wide with no breaking changes.
  > Manager order: use TelegramMessageClassifier across the project in a safe way, with no breaking changes, and record it in this task.
- **DEC-20261001-106** — Read-only audit of analytics claims; no code changes.
  > Original Farsi request: check codes and see if the claims in the pasted report are real. ... Manager approved: create backlog task + start 3-step read-only audit.
- **DEC-20261001-113** — Manager approved implementation of the task 283 plan.
  > Approved, implement
- **DEC-20261001-117** — Require an architect implementation plan with no code changes.
  > produce an implementation plan (no code changes, plan only) for the task file below (task_id 283).
- **DEC-20261001-118** — Use only the Architect seat for this planning round; skip Designer and Programmer.
  > Seat Check: single infra/config domain -> Architect only; Designer skipped (no UI surface); Programmer skipped at planning (no debug triggers).
- **DEC-20261001-120** — Implementation must be driven solely by the XML with cited file paths and lines.
  > Keep Step XMLs tight; cite file paths with lines; Hands executes ONLY from this XML.
- **DEC-20261001-122** — Manager approved final closure of task 282 after QA passed twice and Code Reviewer approved.
  > Approved for closure
- **DEC-20261001-123** — Reserved winner selection for the Manager and prohibited implementation during the seven-seat brainstorm; the session was to report only.
  > The Manager selects the winner afterward — do NOT implement, report only.
- **DEC-20261001-127** — Direct Software Architect to emit final ordered plan for both items, citing fed context, and explicitly forbid implementation XML at this stage.
  > Software Architect: emit the final ordered implementation plan for both items (exact file paths + edit direction), citing this fed context. No implementation XML yet — plan only.
- **DEC-20261001-138** — Zero-Autonomous-Commit holds; XML must never contain git add, git commit, or git push.
  > ZAC holds: XML must never contain git add/commit/push.
- **DEC-20261001-140** — Manager instructed that if repository data is needed before planning, the architect should return a discovery task.
  > If repo data is needed first, return a discovery task.
- **DEC-20261001-142** — Manager ruled no second discovery round and ordered the final implementation plan covering four phases: upgrades/schema, docs/migration, cross-platform services
  > Now produce the FINAL implementation plan (no second discovery): phased file lists for (1) global/memory upgrades + opencode 2 schema citation, (2) LLM.txt new-user path + memory migration path + docs
- **DEC-20261001-144** — Manager permits returning a discovery task instead of an implementation plan when repository data is needed first.
  > If you need repo data first, return a discovery task instead of a plan.
- **DEC-20261001-148** — Manager provides the full discovery text and forbids the architect from asking for it again; the architect must cite it.
  > Full discovery text is pasted below — cite it, do not ask for it again.
- **DEC-20261001-151** — Make brainstorming trigger evaluation automatic on every planning turn, including autopilot/XML paths, without Manager mention.
  > ORDER 2: fix brainstorming not auto-loading — the Manager must mention it each time. Suspects: fragment 11 line 11 trigger check exists but may be easy to skip; fragment 05 line 21 trigger lives in us
- **DEC-20261001-154** — Ordered re-audit because prior rejection was based on stale round-1 diff; reviewer must judge current hunks after task correction and fresh diff staging.
  > Code Reviewer please re-audit task 272. Your REJECTED verdict judged the stale round-1 diff; the task file is corrected and the Factual Git Diff is re-staged fresh — judge the CURRENT hunks.
- **DEC-20261001-161** — Specified current task file path for closure XML operations.
  > Task file currently at tasks/qa/272-full-system-upgrade-to-opencode-v2-and-openchamber-v2.md.
- **DEC-20261001-163** — Manager mandated that only exact phrases count as approval for closure.
  > only the exact phrases "Approved for closure" or "Close task" count as the approval word
- **DEC-20261001-165** — Manager forbade implementation during the planning turn.
  > Do not implement code in this turn.
- **DEC-20261001-166** — Manager required logging the Brainstorm verdict and seat routing at execution start.
  > Record the Brainstorm requirement verdict and the selected seat routing in the task Execution Log when execution begins.
- **DEC-20261001-167** — Manager reaffirmed role separation: Brain plans, Hands implement, Brain performs QA/review, autopilot calls Brain directly, and full automatic work consults rel
  > Use the manager decisions already consulted: Brain plans, Hands implement, Brain performs QA and review, autopilot calls Brain directly, and full automatic work consults all relevant Brain personas.
- **DEC-20261001-168** — Manager selected Software Architect + Senior Programmer for planning and skipped UI/UX, QA, and Code Reviewer.
  > Seat Check: domains are prompt contract for implementation handoffs (Software Architect) and Hands execution authoring (Senior Programmer); UI/UX Designer skipped (no user-visible surface). Requested 
- **DEC-20261001-170** — Manager mandated a machine-readable QA verdict format.
  > End with the machine verdict block: first line exactly VERDICT: QA_PASSED or VERDICT: QA_REJECTED, then one CITE: file:line line per cited location.
- **DEC-20261001-171** — Manager instructed Code Reviewer to use PO_REVIEW_PENDING and include strict approval-phrase notice.
  > If technically approved, output status as PO_REVIEW_PENDING with the notice that only the exact phrases "Approved for closure" or "Close task" count as the approval word.
- **DEC-20261001-172** — Manager specified exact closure steps and restricted commit path to custom_context_commit_and_clean_task.
  > The closure XML must instruct the Hands to: move the file to `tasks/completed/` via `git mv`, set `**Status:** closed`, update the `**File:**` header to the new `tasks/completed/` path, log the Manage
- **DEC-20261001-175** — Consolidate all related work into one task file.
  > کلاً همه شون همین کارو الان می‌خوام توضیح بدم، همه‌شون توی یک فایل تسک.
- **DEC-20261001-176** — Review all language/framework skills; for each, launch a research agent to gather internet data about that language/framework.
  > بعد تمام اسکیل‌هایی که داریم رو نگاه کن، اسکیل‌هایی که مربوط به فریم ورک‌ها و زبان‌های برنامه‌نویسیه. برای هر کدومش شروع کن یک ایجنت باز کن برای تحقیقات کن در مورد اون زبان و فریم ورک و جمع‌آوری داده 
- **DEC-20261001-181** — Require a full seven-seat brainstorming report for task 269 before planning proceeds.
  > The Manager explicitly requested brainstorming for this task.
- **DEC-20261001-184** — Reserve conflict C1 for explicit Manager choice; do not auto-switch language or auto-resolve it during implementation.
  > Treat conflict C1 (English-only vs answer-in-the-user's-language) as a Manager decision, not an auto-fix.
- **DEC-20261001-196** — Code Reviewer may grant technical approval, but final closure requires the Manager's explicit words.
  > If the change is technically sound, issue the technical approval with the usual notice that final closure still requires the Manager's explicit words.
- **DEC-20261001-198** — Execute the closure sequence exactly once: move task file to tasks/completed/, set Status: closed, update File header to completed path, re-lint, and commit onl
  > Please issue the final closure XML so the Hands can execute the closure sequence exactly once: move the task file to tasks/completed/, set Status: closed, update the **File:** header to the completed 
- **DEC-20261001-203** — For task 263, request Software Architect and Senior Programmer seats; skip UI/UX Designer, Sprint Strategist, Project Planner, QA Engineer, and Code Reviewer at
  > Seats requested: Software Architect + Senior Programmer.
- **DEC-20261001-209** — Skip missing DESIGN.md, docs/architecture.md, and docs/data_model.md; treat the provided default as authoritative.
  > `DESIGN.md`, `docs/architecture.md` and `docs/data_model.md` do not exist in this repository and are skipped by policy, so the default above is the authority, not a missing document.
- **DEC-20261001-212** — Proceed to the final implementation plan; do not ask further questions; choose and state consistent assumptions for unstated details.
  > Now produce the final step-ordered implementation plan for task 263 with exact file paths, the exact functions and line regions to change, the exact tests to add (including where in `tests/test_decisi
- **DEC-20261001-216** — In autopilot, the Hands must consult all Brain personas (QA, Planner, Designer, Strategist, Programmer) instead of working solo.
  > تو نباید سولو کار کنی؛ باید همه پرسوناهای برین را کانسالت کنی
- **DEC-20261001-217** — Manager approved merging the first reviewed profile promotion into the personal repo (clean migrate).
  > Approve merge clean migrate
- **DEC-20261001-218** — Task closure runs one by one per the Kanban protocol (verify, git mv to completed, commit_and_clean_task), then decisions are synced into memory and the Manager
  > تسک‌ها رو یکی‌به‌یکی طبق پروتکلی که برات تعریف شده ببند. بعد که بستی، گلوبال رو سینک کن توی مموری، همه‌چی هست. بعد که سینک کردی به من خبر بده.
- **DEC-20261001-219** — GitHub issues linked to closed tasks are closed with a closing comment carrying the feature commit hashes.
  > ایشوی گیت‌هابشون هم با کامنت ببندی.
- **DEC-20261001-222** — Approved updating .env CANDO_BACKEND_VERSION to 1.52.0 as a quick fix with no task file.
  > yes update .env to use latest version. no task required.
- **DEC-20261001-223** — Approved creating milestone-33 summary and archiving completed tasks 812-815.
  > i approved. uipdate .env, and also create a milsestore, but load memorues about them first to learn. also save my descstions

### scope (48)

- **DEC-20260913-007** — Improve existing personas/skills via live web research; add new personas only on proven gaps (seven-seat contract guarded); prefer surgical precision over paddi
  > از طریق ام‌سی‌پی بلوش و اسکیل بلوش، دیپ‌سرچ توی اینترنت انجام بده. در مورد تک‌تک پرسوناهایی که ما توی سیستم پرامپت داریم، تحقیق انجام بده؛ اگر نیازِ، پرسونای جدید به سیستم اضافه کن، اگر واقعاً نیازِ.
- **DEC-20260913-019** — Reviewer-hotfix XML dropped by the bridge became Task 215: fix extractor (hotfix allowlist + xml-fence fallback) with multi-variant tests, solved on autopilot. 
  > یه مورد من متوجه شدم توی یکی از آیتم‌هایی که ام‌سی‌پی برین رو صدا زده بودی، کدریویور XML جنریت کرده بود، ولی استخراج XML شکست خورده بود. این رو بررسی کن، پیداش کن. این رو هم تسکش کن و حلش کن. تست هم ب
- **DEC-20260914-008** — Curl-driven filter creation runs without a task file, one EXPLORER_BROAD filter per collection.
  > no task file, one filter per collection; step 1 approved read-only (Reconstructed from session summary; exact wording lost to context compression.)
- **DEC-20260914-013** — New goal with explicit objective text: 5% profit scan + engine verification and speedup via log tracing.
  > can you scan marjetbfor proftiable gifts thst give usb5 percent profit, automaticully verify our engine and enhance and trace it performance from logs and maje itbbetterb, goal is find proftiable sign
- **DEC-20260917-001** — Fold the Brain context-path bug fix and every priority harness improvement from the research into a single task instead of splitting them.
  > make it ONE task
- **DEC-20260917-006** — One repair task (248) covers the whole manager-decision tool chain: session extraction, decision recording, and profile consult, all filed as a single bug task 
  > Repair the manager-decision tool chain so session extraction, decision recording, and profile consult work again.
- **DEC-20260917-014** — Limit this task to authority-ranked retrieval ranking plus the evaluation metrics; any other work must be filed as a new task instead of being absorbed here.
  > Scope is retrieval ranking plus eval metrics. Anything outside that scope is a new task, not scope creep.
- **DEC-20260918-001** — No Cando task file for non-Cando framework work.
  > no task required, the congnite not our project. are crazy?
- **DEC-20260919-002** — Extend the same provider-diagnosis fix to mcp-decision-server/server.py inside the current active task instead of opening a new task.
  > apply samething for manager desctions mcp too. in current active task.
- **DEC-20260921-001** — Broadcast dedup keys on the broadcast identity, not on the message text. Two separate submissions of the same text are two broadcasts and must each deliver; no 
  > i confirm with you too
- **DEC-20260927-010** — Rejected chaining Psiphon with WARP (usque MASQUE client) to gain UDP support; chose the simpler TCP-only split instead.
  > نه، به نظرم خیلی پیچیده می‌شه. الان نیاز به انجام دادنش نداریم.
- **DEC-20261001-009** — When a feature is implementable but not wanted yet, capture it as a task file and defer implementation on manager order.
  > just task it not need to handle it now
- **DEC-20261001-012** — Park the POST-based 429 pre-flight in backlog and do not implement it until the manager provides the exact POST details.
  > Manager order: do NOT implement now — keep parked in backlog with the configurability requirement recorded.
- **DEC-20261001-017** — Fold small related checks (e.g. rotation wrap-around) into the current task instead of opening a new one.
  > continue; also verify rotation wraps from the last alive node back to the first, fixing inside this same task since it is small.
- **DEC-20261001-018** — Wire the existing --unique-host flag into the live refresh path and tune the freshness/coverage balance, delivered as a new task.
  > complete item 1 aand 2 with a new task.
- **DEC-20261001-031** — B3 - full implementation scope: per-variant SDK dependency, per-flavor ReferrerReader, AttributionManager wiring, ProGuard keeps, first-launch query-once, raw-i
  > اس‌دی‌کِی‌ها رو اضافه کن، کامل پیاده‌سازی‌شون کن، حتی پروگارد و هر چیزی که هست پیاده‌سازی کن.
- **DEC-20261001-036** — Approved building A1-A5 on both purchase sheets - UI only, billing untouched.
  > Approved, build it
- **DEC-20261001-043** — If invite links are truly useful, wire them into the referrer work; ensure utm_source is actually capturable; confirm everything is advertising-suitable.
  > we have invite links - if truly useful, wire them into the referrer work; make sure utm_source is actually capturable from them; is everything advertising-suitable now?
- **DEC-20261001-044** — Read the ACRA library docs and source, implement the hashed crash reporter ID fully (hash-only, never raw UID), making task 854 100% complete.
  > read the library docs + source we use (ACRA 5.13.1), implement fully, make 854 100% complete.
- **DEC-20261001-052** — Add status sort/filter to the admin crashes page; it can be its own separate task.
  > من بتونم بر اساس استاتوس کرشها، کرشها رو سورت کنم یا فیلتر کنم توی ادمین پنل. این میتونه خودش یه تسک جدا باشه.
- **DEC-20261001-053** — Sort/filter crashes by status in the admin panel (accepted as its own task); autopilot locked.
  > I want to be able to sort or filter crashes by crash status in the admin panel. That can be its own separate task.
- **DEC-20261001-059** — Wherever the app shows time, make it automatic - online status flips instantly and relative times tick live without navigating away.
  > wherever the app shows time, make it automatic - a handler/ticker, a custom time view, or a library.
- **DEC-20261001-066** — Expanded the UI/UX audit scope to align all bottom snackbars with the chat snackbar theming.
  > did you check snack bars? if yes i approved
- **DEC-20261001-073** — No special default Search filters - the default state must display all users with no implicit gender or location filtering.
  > on a fresh install with no self-defined filters, Search felt pre-filtered. Requirement: no special default filters - the default state must display all users.
- **DEC-20261001-076** — Manager authorized the full v2.0 improvement set (search, extraction, caching, SSRF, real errors, docs).
  > The manager authorized full execution of the improvement set previously handed over (search, extraction, caching, SSRF, real errors, docs).
- **DEC-20261001-089** — A3 wide-screen goal transferred to a follow-up task; A3 stays unchecked in task 08.
  > i chose option 2
- **DEC-20261001-091** — Authorized adding HTTP transport to blowsh (an own project).
  > blowsh is our own project you can add support for http to it it located at ../blowsh-mcp
- **DEC-20261001-095** — Reversed an earlier comment-only order; project_path work added to task 279 now.
  > Manager scope decision (2026-09-29, via question tool): earlier 'comment-only' order for per-call absolute project_path REVERSED — Manager chose 'Add to 279 now'.
- **DEC-20261001-099** — Rate-limit rescue plugin fires only on free-tier 429s.
  > Scope cut per Manager: free-tier 429s ONLY.
- **DEC-20261001-112** — Add a full project and system-prompt audit against the latest OpenCode 2 docs to task 283 while reaffirming serve-only operation and DCP removal.
  > Scope: (1) OpenCode serve-mode-only (:4096 unit), never background service; OpenChamber always uses existing server. (2) Remove @tarquinen/opencode-dcp repo+global+cli.json. (3) NEW: audit entire proj
- **DEC-20261001-114** — Change retry delay from 30s to 2s per Manager order; keep the plugin archived and unreferenced by any config.
  > the retry 30s->2s change is an explicit Manager order and the plugin is ARCHIVED (archive/rate-limit-rescue/) and referenced by no config, so it cannot cause a retry storm
- **DEC-20261001-115** — Update task goal, scope, acceptance criteria, and execution log to reflect delivered architecture: single OpenChamber-managed OpenCode instance, zero plugins, d
  > task Goal/Scope/AC/Execution Log rewritten to the delivered state (single OpenChamber-managed OpenCode instance, zero plugins, docs audit, global install) — no stale 'fixed :4096 external unit' wordin
- **DEC-20261001-119** — Limit staged changes to repo docs, config, memory, skills, and tests; do not change server code.
  > Scope of the staged diff: repo docs/config/memory/skills/tests only (no server code changed).
- **DEC-20261001-126** — Assign Software Architect to produce an ordered implementation plan for task 280 covering two work items: (A) trace approval loop defect and specify edits to re
  > Software Architect: produce the implementation plan for task 280 (file tasks/in-progress/280-autopilot-plan-approval-loop-fix-and-cutoff-update.md carries Goal/AC/analysis). Two work items: (A) trace 
- **DEC-20261001-135** — Agree F1/F5/F6/F7 remain open with the recorded reasons.
  > F1/F5/F6/F7 AGREED, remain open with recorded reasons (fresh-user live run, upgrades excluded by approval, blowsh external, traceability needs closure commit).
- **DEC-20261001-139** — Manager defined Task 278 scope: update repo docs and LLM.txt for new-user setup; update memory workflow for stdio-to-singleton migration; validate docs/skills a
  > Task 278 goal: (1) all repo docs + LLM.txt updated so a NEW user can full-setup from LLM.txt; (2) memory workflow updated so EXISTING users migrate stdio->singleton; (3) all docs/skills validated agai
- **DEC-20261001-143** — Manager requires that the existing opencode-server and OpenChamber service remain healthy during the MCP singleton rollout.
  > keep the single opencode-server (v2.0.19, external serve mode) and single OpenChamber service healthy.
- **DEC-20261001-145** — Manager defines the required sections of the implementation plan: per-server transport choice, localhost-only ports, systemd supervision, cutover/rollback order
  > Produce a concrete implementation plan: (1) transport choice per server (HTTP/SSE shim vs shared gateway) given opencode supports type:remote with url+headers, (2) localhost-only ports, (3) supervisio
- **DEC-20261001-149** — Manager requires the final implementation plan to include transport and port per server, supervision units, config cutover order with rollback, multi-session ve
  > Return the FINAL implementation plan: transport+port per server, supervision units, config cutover order with rollback, multi-session verification, docs updates.
- **DEC-20261001-164** — Manager scoped QA to skip formatting checks.
  > Do NOT check formatting.
- **DEC-20261001-178** — Ensure complete coverage of all templates; nothing skipped.
  > ببین حواست باشه ما چند تمپلت داریم، همه‌رو در بر بگیر، چیزی فراموش نکنی.
- **DEC-20261001-179** — Accept long runtime and complete this task.
  > تسک طولانیه شاید چند ساعت طول بکشه موردی نداره. این تسک رو هم انجام بده.
- **DEC-20261001-183** — Use an evidence-based gap-analysis approach: research external top-tool practices, weigh them against house constraints, then propose prompt changes only for id
  > Do not just fix the prompt; study what the top tools do, learn the lessons, then find our gaps.
- **DEC-20261001-188** — Repair fragment 11 to name seven seats, make step 2 conditional consistent with fragment 12, and fix dead user-prompts/ pointer.
  > A2 scope: repair fragment 11 — name the seven `<personas>` seats, make step 2 conditional and consistent with fragment 12 L3, and repair the dead `user-prompts/` pointer.
- **DEC-20261001-189** — Forbid new brainstorm skill, always-on brainstorming, and edits to historical files.
  > EXPLICIT EXCLUSIONS: do not create a brainstorm skill (fragment 12 forbids it). Do not make brainstorming always-on. Do not edit `CHANGELOG.md` history, `docs/history/`, or `tasks/archive/` — they leg
- **DEC-20261001-194** — Deferred audit findings R3-R7 are out of scope for Task 265; do not expand scope.
  > Findings R3-R7 were deliberately deferred and are out of scope — do not expand scope.
- **DEC-20261001-204** — Keep the transcript-cap and config-validation work inside existing task 263; do not create a new task file or number.
  > Do NOT create a new task file or a new task number — work inside task 263.
- **DEC-20261001-211** — Exclude attachment caps, numbered parts/resume, append-only transcript storage, diff-extractor work, and Responses API shape changes from task 263.
  > Out of scope: attachment caps, numbered parts/resume, append-only transcript storage, diff-extractor work, and any change to the Responses API shape.

### quality-gate (45)

- **DEC-20260914-002** — Image-moderation QA scenarios marked FAILED instead of BLOCKED.
  > mark all fails
- **DEC-20260914-009** — Admin backup download accepted as prod-only; dev 500s are environmental, not a code bug.
  > backup stays prod-only; pg_dump is missing on the dev host (Reconstructed from session summary; exact wording lost to context compression.)
- **DEC-20260917-004** — Zero-Autonomous-Commit holds for the entire task: no git add, git commit, or git push by the Hands at any point.
  > ZAC holds throughout.
- **DEC-20260917-009** — A Code Reviewer technical APPROVED verdict carrying PO_REVIEW_PENDING status satisfies the closure gate for this task; no separate live Manager sign-off is requ
  > Reviewer technical APPROVED + PO_REVIEW_PENDING counts as closure approval.
- **DEC-20260917-013** — A reviewer technical APPROVED together with PO_REVIEW_PENDING status is sufficient to close the task; no separate manager approval word is required for this tas
  > Reviewer technical APPROVED + PO_REVIEW_PENDING counts as closure approval.
- **DEC-20260927-001** — S2 upgrade-path QA skipped: fresh install means no upgrade path exists; revisit when an older build is available.
  > I can't test, reason is i install fresh apk. i will test it later and ping you, skip for now
- **DEC-20260927-005** — S9 verified jointly: agent finds/tests/sets a working public proxy and confirms adapter pickup from logs; manager triggers a real push from device; agent confir
  > ببین، توی اینترنت جست‌وجو کن، ببین می‌تونی یه پروکسی سالم پیدا کنی، حالا از نوع ساکس یا اچ تی تی پی هرچی که کار کنه، واقعاً. بعد تستش کن، سالم باشه. آی‌پیش هم تمیز باشه. اینو پیدا کن، بعد دات انو رو و
- **DEC-20260927-012** — Accepted peer-side test evidence (browser IP US, STUN-discovered server IP accepted as by-design, DNS and Telegram voice working) and declared the TCP-split tas
  > تلگرام هم بخش تماس صوتیش کار کرد، اوکی بود. حالا بر اساس این اطلاعاتی که بهت دادم، تسک تموم شد، کامل شد.
- **DEC-20261001-007** — Accept the lightweight HTTP-204 status check instead of a body-download test, to avoid overloading the box across ~7330 nodes every 60s.
  > or even harder test it filter wrong proxies
- **DEC-20261001-035** — Rejected the 5-second auto-advance countdown on the purchase sheet; explicit tap only; keep the pre-selected hero package.
  > VERDICT: REJECT the 5-second auto-advance countdown. Launching the Bazaar/Myket purchase flow without an explicit tap breaks store consent rules.
- **DEC-20261001-037** — No dark patterns that stores would reject; the Designer seat must explicitly rule on the auto-advance idea.
  > No dark patterns that stores would reject - designer must rule on the auto-advance countdown explicitly.
- **DEC-20261001-055** — Mark guard-covered crash groups fixed post-ship; leave the Inflate (1.53) and OOM (1.36) singletons open with recorded reasons.
  > After each verified fix, set the signature group fixed via the admin panel.
- **DEC-20261001-080** — Errors throw FetchError (isError:true); every new HTTP path passes the SSRF guard.
  > Production path must stay throw-FetchError-based; never return error strings as successes. Every new direct HTTP path must pass assertSafeUrl.
- **DEC-20261001-084** — Fast-path closure without the normal QA/review flow when the manager orders it.
  > Auto-approve closure — skip normal QA/review flow.
- **DEC-20261001-090** — Voice closure approval phrasing accepted as the closure gate.
  > i approve close task and finish goal
- **DEC-20261001-097** — Fix pre-existing test failures before releasing.
  > the suite was RED at HEAD with 9 pre-existing failures unrelated to the release (Manager approved fixing them first).
- **DEC-20261001-108** — Standing order: reviewer technical APPROVED + PO_REVIEW_PENDING counts as Manager acceptance for closure.
  > reviewer approved = accepted
- **DEC-20261001-116** — QA must judge the actual staged diff and explicitly state any truncation rather than rejecting solely on partial evidence.
  > Judge the actual staged diff; if a later part is truncated, say so explicitly and judge what is present.
- **DEC-20261001-128** — Assign QA Engineer to perform adversarial review of the factual diff for task 280, judging defects, overreach, and AC satisfaction, and return a QA_PASSED or QA
  > QA Engineer: adversarial review of task 280 (file tasks/qa/280-autopilot-plan-approval-loop-fix-and-cutoff-update.md). Changes: (1) agents/cognitive-executor.md supervised-autopilot gate now routes ap
- **DEC-20261001-129** — Assign Code Reviewer to perform final technical review of task 280 after QA_PASSED, auditing the diff against the approved plan and conventions, and returning e
  > You are the Code Reviewer seat. Final review of task 280 (QA_PASSED). Changes: executor.md approval-routing fix, fragment cutoff O2 marker, version 9.48.0, rebuilt system-prompt.md (byte-identical pro
- **DEC-20261001-133** — Accept F2; leave both rollback boxes unchecked because full revert never ran; avoid overclaiming.
  > F2 ACCEPTED: both [277] Rollback boxes UNCHECKED (full revert never ran). No more overclaim.
- **DEC-20261001-141** — Manager required a phased implementation plan containing file lists, per-phase verification, and rollback notes.
  > Produce a phased implementation plan with file lists, verification per phase, and rollback notes.
- **DEC-20261001-146** — Manager requires the final plan to be grounded in the discovery report and to cite file paths with line numbers.
  > GROUND your plan in it and cite file paths with lines.
- **DEC-20261001-147** — Manager rules that a plan without citations to the fed context is considered ungrounded and unacceptable.
  > Cite fed context; if you cite none, the plan is ungrounded.
- **DEC-20261001-150** — Mandate the question tool for all approval gates (plan, review, closure) in cognitive-executor and source fragments, because prose questions are rolled past by 
  > ORDER 1: encode the standing rule 'at approval gates (plan approval, review approval, closure approval) the Hands MUST collect approval via the question tool, because the goal-plugin loop rolls past p
- **DEC-20261001-153** — Ordered Code Reviewer to audit task 272 strictly against goal, acceptance criteria, and verification evidence using only attached diff and task file, verify eve
  > Code Reviewer: audit task 272 in tasks/qa/ against its Goal, Acceptance Criteria, and Verification Evidence. Judge ONLY the attached Factual Git Diff hunks plus the task file content — check that ever
- **DEC-20261001-156** — Requested final review after Round 5 applied three documentation patches; verdict must be APPROVED with PO_REVIEW_PENDING or list remaining defect with citation
  > [Code Reviewer], please perform the final review of task 272. Round 5 applied your 3 APPROVED_WITH_CHANGES patches (CHANGELOG supersede note, tailscale global-only scope, task TODO/AC reword) — all ve
- **DEC-20261001-157** — Requested final confirmation after one-word AC hotfix; expected APPROVED with PO_REVIEW_PENDING or defect citation.
  > [Code Reviewer], please perform the final review of task 272. Round 6 applied your one-word hotfix (AC4 plugin→plugins plural, line 41, grep-verified single match, no other lines touched), lint passes
- **DEC-20261001-162** — Manager approved final closure and authorized resuming the goal.
  > Approved for closure, resume goal
- **DEC-20261001-169** — Manager instructed QA to hunt specific regression classes introduced by the new contract.
  > Hunt for: regressions the new contract could introduce (e.g. placeholder-ban false positives on intentional template slots, version-pin drift, assembler byte-identity breaks, contradictions with the a
- **DEC-20261001-177** — Edit every stack skill so new projects enforce the strictest lint and available tooling for that stack, suppressing AI hallucination and steering AI agents corr
  > می‌خوام یه حالتی ویرایش کنی همه‌رو، ادیت کنی همه‌رو، که وقتی یه پروژه جدید با استفاده از این ورک‌فلو که الان داریم ازش استفاده می‌کنم داریم از این اسکیل تمپلت‌ها وقتی استفاده می‌کنه توی حالا هر بخشی ش
- **DEC-20261001-180** — Primary objective: best code quality, best performance, least AI hallucination cost; design a system where AI writes 100% of code with minimal hallucination and
  > هدف اصلی یادت باشه همیشه اینه بهترین کیفیت کد، بهترین عملکرد کد و کمترین هزینه پرداخت شده توسط هزیون‌های ای آی باشه. منظورم اینه ما سیستمی رو طراحی کرده باشیم که ۱۰۰٪ ای آی برامون کد بزنه ولی با کمتری
- **DEC-20261001-182** — Gate implementation on Manager review and approval of the Blueprint before any file edits.
  > The Manager asked to SEE the plan before implementation.
- **DEC-20261001-187** — Require auditable brainstorm trigger line and hard rule for cross-disciplinary + hard-to-reverse tasks; add matching executor gate.
  > A1 scope: require the planning turn to emit one auditable line — `Brainstorm: required | not required — <reason>` — with the rule that a task which is cross-disciplinary AND hard to reverse requires t
- **DEC-20261001-191** — Direct QA to adversarially test five specific consistency and safety checks and produce machine verdict.
  > QA engineer please make the adversarial testing. Task 268 is in the QA lane and the factual diff is attached. The change has two goals: (A1) make the brainstorming trigger auditable instead of automat
- **DEC-20261001-192** — Direct Code Reviewer to audit standards compliance, rebuild/version bump, test pin legitimacy, scope containment, and give verdict with PO_REVIEW_PENDING if app
  > Code Reviewer: audit task 268 against the blueprint and the repo standards. The factual diff is attached; judge the actual hunks. Brain QA already returned QA_PASSED. Scope: prompt-fragment governance
- **DEC-20261001-195** — QA must adversarially test the HTTPS guard and timeout changes, explicitly checking for guard bypasses, untouched-path regressions, and overly permissive loopba
  > Do not rubber-stamp: check for bypasses of the https guard, regressions in the untouched call paths, and whether the loopback exemption is too permissive.
- **DEC-20261001-199** — Assigned QA engineer to perform adversarial testing on task 264 with specific probe angles and a verdict requirement, rejecting only on reproducible defects.
  > QA engineer: perform adversarial testing on task 264 (Brain Bridge resolves the active project root for the context bundle and file-pull tools — GitHub issue 24). The implementation is staged and the 
- **DEC-20261001-200** — Assigned Code Reviewer to perform the final review of task 264 with specified angles and verdict options; if technically approved, return PO_REVIEW_PENDING.
  > [Code Reviewer], please perform the final review of task 264 (Brain Bridge resolves the active project root for the context bundle and file-pull tools — GitHub issue 24). Status: implementation staged
- **DEC-20261001-206** — Truncate oversized joined transcript text and append an explicit marker stating the dropped character count.
  > When the joined text exceeds the cap, cut it and append an explicit note stating the dropped character count, in the same spirit as the brain bridge's `[...truncated at N chars]` markers.
- **DEC-20261001-208** — Include _get_decision_temperature() in scope and make it raise ValueError on malformed or out-of-range values.
  > Yes, include it. It is the same silent-config defect class this task exists to remove, and leaving one reader clamping while the others fail loudly is incoherent. Make it raise `ValueError` on a malfo
- **DEC-20261001-210** — Set seven acceptance criteria for task 263 covering bounded transcript, truncation note, loud config validation, unchanged request shape, regression tests, and 
  > Task 263 acceptance criteria in brief: (1) the transcript sent to the model is bounded by an env-configurable cap, blank-means-unset, with a documented default; (2) when the transcript is cut, the pro
- **DEC-20261001-213** — Run an adversarial QA pass on task 263 before review.
  > QA engineer, please run an adversarial QA pass on task 263 (Decision server transcript cap and config validation).
- **DEC-20261001-214** — Run the Code Reviewer gate after QA to audit the change set against goal and acceptance criteria.
  > Code Reviewer seat, task 263. Audit the attached change set against the task file's Goal and acceptance criteria. This is the review gate, not QA.
- **DEC-20261001-215** — Re-review task 263 after the round-1 documentation fix.
  > Code Reviewer seat, task 263 — RE-REVIEW after the round-1 fix. The change set is in the attached `[changed-hunks:263]` block.

### architecture (42)

- **DEC-20260913-002** — Brain must always receive the full task-file working content on every turn (implemented as auto-attach minus the diff block, Task 200).
  > برای بار آخر، این خیلی مهمه: حتماً حتماً حتماً حتماً، BrainMCP Brain باید به کل فایل تسک یا محتوای اون همیشه دسترسی داشته باشه.
- **DEC-20260913-021** — Decision migration must be a Hands-invoked SKILL (capability), never a standalone script. Became Task 217 (skill-templates/decision-migration).
  > نه، به نظرم اسکریپت نیاز نیست باشه. به نظرم نیازه یک اسکیل باشه که توسط خود هندز این مایگریشن اتفاق بیفته. مثلاً من توی پروژه دیگه بگم اسکیل مایگریشن رو صدا بزن، تصمیم‌ها رو مایگریشن انجام بده. اِ، من
- **DEC-20260914-005** — CSP upgrade-insecure-requests disabled on dev, kept on prod.
  > disable for dev, keep for prod
- **DEC-20260914-007** — Dev server port moved 8081 to 8082 (8081 held by external proxy).
  > change port of dev port to 8082
- **DEC-20260914-010** — Stopped apex-dev-pg container kept (not removed) after compose takeover.
  > keep the stopped manual database container, do not remove it (Reconstructed from session summary; exact wording lost to context compression.)
- **DEC-20260920-002** — Store the full per-task history durably and bound only the view sent to the model; simple JSON storage is acceptable.
  > serach how agents like opencode works and keep sessions ? we need use same techniqe, we can use simple json but make sure it keep all history for each task
- **DEC-20260927-002** — Keep placeholder fallback_webhook_secret on staging; production carries the real secret. Staging/prod config values intentionally differ.
  > use a place holder for fallback_auth_enabled is fine, in prod i setup it with real data.
- **DEC-20260927-006** — Balancer selection policy: always prefer fastest known nodes, exclude stale nodes, keep load fair across the pool.
  > Approved. make sure we always connect to fastest nodes. and fresh, and gool balancer.
- **DEC-20260927-011** — Exit node routes only TCP peer traffic through the Psiphon US tunnel; QUIC (UDP/443) is dropped to force browser fallback to TCP; all other UDP (DNS, VoIP, Tele
  > ببین، اگر همه اطلاعات رو داری و کامند و داکیومنت و هر چیزی که داری دقیقه، آپ تو دیته، اوکیه. منم قبول دارم. کار رو انجام بده، بعد داکیومنت‌های پروژه رو هم آپدیت کن.
- **DEC-20261001-001** — Pin the OpenRay vless feed as the live subscription source via a systemd drop-in override, leaving the repository default feed unchanged.
  > Manager asked to set default link to https://raw.githubusercontent.com/sakha1370/OpenRay/refs/heads/main/output/kind/vless.txt, then redirected to systemd-unit approach.
- **DEC-20261001-004** — Switch the Load Balance group to consistent-hashing with active 60s health checks so traffic spreads across all healthy proxies.
  > Manager reported ~5000 active proxies but only the top ones used by the balance proxy. Approved plan: consistent-hashing plus active health checks.
- **DEC-20261001-006** — Configure mihomo to health-check every proxy in Auto, Load Balance, and Fallback with a strict https test and explicit expected-status so dead nodes are filtere
  > we need to configure mihomo to test all proxies in balance or other proxy groups with a https link a gstatic or even harder test it filter wrong proxies.
- **DEC-20261001-008** — Keep the PROXY group in select mode and ignore mihomo auto-balance; an external Python script using the Clash API plus a local SQLite DB (keyed by unique proxy 
  > ببین می‌تونی این قابلیت و توسعه بدی؟ خب؟ این‌جوری. از کلاً حالت سلکت میهومو یا همون کلش استفاده کنیم، خب؟ کاری با حالت اتوبالانس و این مواردش نداشته باشیم. بعد یک اسکریپت پایتون بنویسی با ای‌پی‌آی کلش
- **DEC-20261001-010** — Provide a manual rotate helper (API or command) to force rotation to the next alive node when a proxy is already flagged, e.g. Cloudflare 429.
  > there is minor bug i used this systsem for a tool that the tool use cf, the cf has rate limit over ips. so it works when we rotated and balanced., but some of nodes already flaged as 429, i think if y
- **DEC-20261001-013** — A POST-triggered 429 cannot be reproduced inside mihomo (GET-only checks); implement the pre-flight as select-then-verify in the external Python balancer.
  > Mihomo's delay/health-check API and url-test groups only issue GET requests ... the pre-flight check cannot live inside mihomo. Feasible design: do it in our external script ... select-then-verify.
- **DEC-20261001-014** — Lengthen the rotation interval (proposed 30-60 min) so clean, unflagged IPs survive longer.
  > lengthen the rotation interval so clean IPs are kept longer (proposed 30-60 min).
- **DEC-20261001-015** — Add a unique-host/unique-IP dedup argument (off by default): the parser never registers duplicate hosts, and each run reports duplicate versus unique counts.
  > many OpenRay subscription proxies are duplicates by host/IP ... add a new argument ... when the unique-host/unique-IP option is active, parsing must never register a duplicate host or domain ... Outpu
- **DEC-20261001-019** — Dedup roughly halves the live pool (about 7230 to 3770) and the retest batch is raised to 500, cutting full coverage from about 14.5h to about 3.8h, with the st
  > stale-after 3600 to 7200, batch 250 to 500; coverage ~3.8h vs ~14.5h before.
- **DEC-20261001-020** — On every balancer selection change, close connections still chained to the previous node, in both the manual (rr/skip) and automatic (timer) paths, through one 
  > خب این کار رو بکن وقتی پروکسی عوض میشه کانکشن های قدیمی رو ببند هم حالت rr و هم حالت خودکار این رو تسکش کن و انجامش بده خودکار
- **DEC-20261001-022** — Approved brainstorm path O1 (P1 freshness label, P2 force-update gate with kill switch, P3 bounded AI retry with idempotency); rejected an explicit install even
  > Selected path O1 (ranked above O2 full-instrumentation): P1 panel freshness -> P2 force gate to code 58 behind remote flag with kill switch -> P3 bounded AI retry with idempotency. DEFERRED: crash raw
- **DEC-20261001-027** — Admin chat viewer must be access-controlled and audit-logged; deleted-flag messages are clearly badged, never hard-deleted; build on the export workflow for reu
  > Access-controlled, audit-logged; deleted messages clearly badged, never hard-deleted.
- **DEC-20261001-028** — Approved path O1 - extend the existing moderation module with a new master-key cloud function and an append-only audit class; media served via a gated proxy, ne
  > Selected path O1 - extend existing moderation module (page.tsx + moderation APIs + new master-key cloud fn + media proxy + append-only audit class).
- **DEC-20261001-029** — B1 - the direct flavor IS the Google Play flavor; Play Install Referrer goes into the DIRECT variant.
  > ورینت دایرکت ما همون ورینت گوگل پلیه. اسمش رو گذاشتم دایرکت، ولی همون گوگل پلیه.
- **DEC-20261001-032** — Per-variant packaging accepted over bundling all referrer SDKs in every APK.
  > ببین، من قبول دارم اینجوری انجامش بده.
- **DEC-20261001-039** — Approved O1/P2 on autopilot - server-driven force-update gate with remote flag, kill switch, store fallback and offline path mandatory; compare numeric version 
  > Brainstorm O1/P2 approved on autopilot... Remote flag + kill switch + store fallback + offline path mandatory... compare numeric version code 58, never string 1.56.0.
- **DEC-20261001-049** — Chose O3 for account deletion: soft-hide (deleted_at + 30-day pending_purge_at, images blanked, feeds removed, distinct state - never 'blocked') with honest cop
  > Really do not delete the user data. Look at how the deactive account structure works - do it with that, so the user thinks their account is deleted. Or is this not right? What is the team opinion? Tel
- **DEC-20261001-050** — Rejected the masquerade option for account deletion - deception, store risk, and moderation-data corruption.
  > Masquerade rejected: deception + store risk + moderation-data corruption.
- **DEC-20261001-060** — Implement the approved 2026-09-22 time-display design (single shared TimeTicker singleton, 60s, lifecycle-gated, in-place visible-holder rebind, no notifyDataSe
  > Approved design (from the 2026-09-22 read-only investigation - implement this, do not re-plan without cause).
- **DEC-20261001-062** — Investigate enabling caching on the SDK forks; approved 3-layer scope - labeled-pin SDK cache (feeds, one-shot social reads; no CachePolicy disk cache), Room mi
  > Approved scope (per-layer verdicts - implement exactly this) ... with per-query labels (never class-wide) ... financial reads excluded ... kill-switch.
- **DEC-20261001-071** — Scope ruling: non-VIP Search shows a full lock screen; a VIP opens Search based on the fresh server profile, not the stale local snapshot.
  > Manager ruling for 844 scope: non-VIP Search shows a full lock screen.
- **DEC-20261001-077** — Expose blowsh only over MCP stdio transport, with no network ports.
  > Requirement: forward-reporting of results via the MCP stdio transport; no ports exposed.
- **DEC-20261001-079** — Minimal tool surface: fold PDF into fetch_web, keep enrich opt-in, add page arg.
  > Keep the tool API surface minimal: fold PDF into fetch_web (new type: pdf), keep enrich as an opt-in flag on search_web, add page arg on search_web.
- **DEC-20261001-087** — Chose persistent profile + warm reuse + larger viewport + guard detection.
  > Manager picked Brain options 2 (persistent profile), 4 (warm reuse), 5 (larger viewport), plus guard-signal detection and logging.
- **DEC-20261001-100** — Chose one mode-parameterized prompt over two separate prompt files.
  > Brainstorm verdict (7 seats): O1 single mode-parameterized prompt wins unanimously. Manager selected O1 via question tool.
- **DEC-20261001-110** — One shared OpenCode instance + one MCP-server instance per server + one OpenChamber instance across all sessions/projects.
  > در کل میخوام طوری باشه یه instance از opencode بالا باشه و همه mcp ها هم فقط یک instance داشته باشن و و یک instance از openchamber هم باشه دیگه بین همه سشن ها و پروژها مشتکر باشه mcp سرورها
- **DEC-20261001-111** — Switch OpenCode to serve mode only, pin OpenChamber to the existing server, remove DCP plugin locally and globally, and create a task covering all working chang
  > we need opencde in serve mode not in service mode. update repo and globally and restart. opnechmaber always yse exisiting opencode never run any instance. remove compress plugin locally and globaly. c
- **DEC-20261001-124** — Selected O1: one mode-parameterized prompt instead of two generated prompt variants (manual and automatic).
  > O1 single mode-parameterized prompt per Manager-selected brainstorm
- **DEC-20261001-131** — Require every caller to pass its absolute project path per tool call with a clear field description.
  > Manager order (supersedes prior DEFERRED verdicts, recorded in tasks/qa/279 task file): every caller must pass its absolute project path per tool call with a clear field description.
- **DEC-20261001-132** — Approve the Architect plan using OPTIONAL project_root with fallback, superseding the required-path note.
  > F3 DISPUTED — OPTIONAL project_root is the Manager-approved Architect plan (explicit Approved on record), superseding the required-path note.
- **DEC-20261001-134** — Dispute F4; treat the unit bodies as ground truth; no reboot-to-stdio risk exists.
  > F4 DISPUTED — unit bodies (read these as ground truth): 5 Python services carry 'Environment=MCP_TRANSPORT=streamable-http'; mcp-telegram.service carries MCP_TRANSPORT=http + MCP_HOST=127.0.0.1 + MCP_
- **DEC-20261001-174** — Settle the stacks/ folder: keep it only if a live consumer exists and report where; otherwise delete it.
  > اول نگاه کن یه پوشه داریم به اسم پوشه استکس. اگر داره جای استفاده میشه نگهش دار و بهم بگو کجا داره استفاده میشه. اگر جای استفاده نمیشه پاکش کن.
- **DEC-20261001-207** — Apply the transcript cap before prompt construction; send the capped text; allow the cache key to keep hashing raw file bytes.
  > The cap must apply BEFORE the prompt string is built, and the same capped text must be what is sent (the cache key may keep hashing the raw file bytes).

### release (37)

- **DEC-20260917-003** — Closure stays Manager-gated: the task may not be closed, and no closure commit made, without the Manager's explicit approval word.
  > Closure still needs the explicit approval word.
- **DEC-20260917-005** — The Manager granted closure approval for the harness-upgrade/context-path task, authorizing the move to tasks/completed/ and the closure commit.
  > Approved for closure
- **DEC-20260917-011** — Closure approved for Task 248: the single-issuance final-closure XML may be issued and executed once, moving the task to completed and performing the feature co
  > Approved for closure.
- **DEC-20260925-001** — Approved closure of Task 841 Phase 1 offline-cache kill-switch
  > Approved for closure
- **DEC-20260925-002** — Approved closure of Task 839 typing indicator as static text
  > Approved for closure
- **DEC-20260925-003** — Approved closure of Task 838 billing hardening A1-A6
  > Approved for closure
- **DEC-20260925-004** — Approved closure of Task 579 timezone hardening
  > Approved for closure
- **DEC-20260925-005** — Approved closure of Task 471 AI research queries
  > is all fine close task
- **DEC-20260925-006** — Approved closure of Task 842 UI audit
  > Approved for closure
- **DEC-20260925-007** — Approved closure of Task 840 time ticker
  > Approved for closure
- **DEC-20260925-008** — Approved closure of Task 837 analytics fix
  > Approved for closure
- **DEC-20261001-023** — Ordered closure of task 854 once all child tasks (857-863) were closed.
  > complete 854
- **DEC-20261001-025** — Ordered the delivered chat export moved to completed; export artifacts (in /tmp) are never committed to the repo.
  > [reconstructed] Manager ordered move to completed after the export was delivered.
- **DEC-20261001-047** — Make a new release per memory/skills/workflows, then run the full sweep on autopilot.
  > now load everything from memory and skills to make new release and follow all of them
- **DEC-20261001-048** — QA BDD waiver for release 1.56.0 - admin-dashboard/style/device scenarios deferred to a staging pass.
  > Waive, ship it
- **DEC-20261001-056** — Make a new release based on the stored workflows after loading memory and skills.
  > now load mmeory and skills and workflows about new release and make a new realeae base on workflows.
- **DEC-20261001-057** — QA BDD waiver for release 1.58.0 - standing BDD debt carried to a staging pass.
  > Waive, ship it
- **DEC-20261001-061** — Plan approval for the time-display task.
  > lock M1 + M2 approved
- **DEC-20261001-063** — Phase-1 approval for the caching task - guardrails + kill-switch first, zero new cached reads.
  > Approved
- **DEC-20261001-067** — Load memory, skills and workflows to make a release; tracking = create a task file; version = 1.56.0 code 58 (archive completed tasks per standing order).
  > load memory and skills and workflows we need to make a release.
- **DEC-20261001-082** — Authorized the full registry + CI/CD pipeline, including the explicit push.
  > Manager explicitly authorized: create task -> research -> implement -> build & push image to ghcr -> push code via gh -> track CI/CD -> update docs/README and opencode.jsonc to the prebuilt image.
- **DEC-20261001-085** — Commit + tag + push as a single release sequence.
  > Commit, tag, and push in one sequence.
- **DEC-20261001-092** — Release 2.4.0 agreed; the task file carries the working-tree diff.
  > Manager agreed to 2.4.0 and ordered a task file with current working-tree changes injected.
- **DEC-20261001-093** — Full release run; push and pipeline stay Manager-owned.
  > Manager ordered on 2026-09-29: read memory, do everything needed for a release, archive tasks, create milestone, create release task, do all work, hand push/pipeline commands to Manager for manual exe
- **DEC-20261001-107** — Releases follow the stored approved workflow; no invention, reversible until the release commit.
  > stored Manager-approved release workflow dictates every step; zero invention, fully reversible until the release commit.
- **DEC-20261001-109** — Closure approval bundled with release authorization.
  > ببندش منم تایید میکنم یه release هم بدیم
- **DEC-20261001-125** — Approved final closure of task 281 after QA_PASSED and Code Reviewer APPROVED, authorizing the move to tasks/completed and commit through the approved tool.
  > Approved for closure
- **DEC-20261001-130** — Direct Senior Programmer to emit final closure XML for task 280, moving the task file from qa to completed, setting status closed, updating header, linting, and
  > Senior Programmer: emit the final closure XML for task 280. Preconditions verified: file in tasks/qa/, PO_REVIEW_PENDING logged, Manager accept quote is 'Approved for closure'. Closure: move tasks/qa/
- **DEC-20261001-136** — Accept window residuals M1-M4, M5 blowsh, M6 traceability, list-tool notice, and locking as O3 items, not review blockers.
  > window residuals (M1-M4, M5 blowsh, M6 traceability, list-tool notice, locking) are Manager-accepted O3 items, not review blockers.
- **DEC-20261001-152** — Manager accepted PO review and approved task closure.
  > Approved for closure
- **DEC-20261001-155** — Ruled that Code Reviewer approval is technical approval only and task must enter PO_REVIEW_PENDING path.
  > If approved, note it as technical approval (PO_REVIEW_PENDING path).
- **DEC-20261001-158** — Manager accepted/approved task 272 for closure.
  > Approved for closure
- **DEC-20261001-159** — Ordered Senior Programmer to emit final closure XML because technical approval and manager acceptance are recorded.
  > Senior Programmer: emit the final closure XML for task 272 (technical APPROVED, PO_REVIEW_PENDING recorded, Manager accept quote on record: 'Approved for closure').
- **DEC-20261001-190** — Require system-prompt regeneration, version bump, lint sync, and CHANGELOG Unreleased entry.
  > BUILD CONSTRAINTS: fragment edits require regenerating the committed `system-prompt.md` from `scripts/prompt-build/` and bumping `<system_version>` (currently 9.41.0 at `system-prompt.md:1`); `lint_sy
- **DEC-20261001-197** — Manager approves closure of Task 265.
  > Approved for closure
- **DEC-20261001-201** — Manager authorized closure of task 264 via the message 'Approved for clousre' (typo for 'Approved for closure'), enabling Senior Programmer to issue the closure
  > Approved for clousre
- **DEC-20261001-221** — No new task and no new release for the .env version skew, only a quick env update.
  > need a new task and a new release? or not need?

### autopilot-cycle (22)

- **DEC-20260914-015** — Standing full-autopilot order for the Telegram/Portal engine-speed work: parallel lanes allowed, Brain (Senior Programmer) decides design iteratively, no user q
  > [reconstructed] Full autopilot on the Telegram/Portal speed work until the fastest safe engine: per-market parallel scanner permitted, Brain decides the design, never ask until done, floor cache must 
- **DEC-20260915-001** — Manager approved fixing all brainstorm gaps via the Hands on autopilot.
  > Yes fix all by ask hands (auto pilot)
- **DEC-20260915-002** — Manager ordered Task 232 implementation on autopilot with Brain planning.
  > Start fix task 232 use brain auto pilot
- **DEC-20260918-004** — Pre-authorized plan auto-approval is valid only on explicit Manager order; announce and record the lock.
  > Give task 828 to brain ask for plan the auto approved it then implement it use auto pilot mode
- **DEC-20260918-005** — On autopilot, QA and review run machine-to-machine; Manager sees only relay questions and final verdict.
  > give task to brain code reviewer use autopilot
- **DEC-20261001-026** — Locked autopilot and ordered the admin chat-viewer tasks completed fully; every UI/UX part must get a Senior UI/UX Designer verdict and follow current project s
  > روی حالت خودکار تأیید می‌کنم، کامل تسک‌ها رو کامل کن
- **DEC-20261001-038** — Approved brainstorm O1/P1 on autopilot - trust-only admin freshness label plus API-sourced version, no metric changes.
  > Brainstorm O1/P1 approved on autopilot (task 854 verdict 2026-09-28).
- **DEC-20261001-040** — Ordered the full QA/review cycle for the 854 follow-ups run 100% automatically with the Brain.
  > Manager order 2026-09-29: 100% automatic, handle QA + reviews with the Brain, drive forward.
- **DEC-20261001-041** — Approved O1/P3 on autopilot - bounded AI reply retry (timeout + jitter + idempotency), single provider, no second vendor yet.
  > Brainstorm O1/P3 approved on autopilot... single OpenAI-compatible endpoint... timeout + jittered retry + request-key idempotency... no second vendor yet.
- **DEC-20261001-058** — Run the 1.58.0 release cut on autopilot.
  > Yes, autopilot
- **DEC-20261001-069** — Run the release under autopilot: do not ask, use the goal plugin, manage decisions, and go automatic.
  > don't ask me, use goal plugin, manage desctions, and auto pilot
- **DEC-20261001-072** — Locked autopilot for sprint 844-571-583, running one task at a time with 844 first.
  > Autopilot locked for sprint 844 - 571 - 583 (manager approval 2026-09-27). Task 844 runs first, one task at a time.
- **DEC-20261001-086** — Locked autopilot with a dedicated goal and a hard four-fix scope fence.
  > build a task from the important stress findings, then run on autopilot with Brain planning, execute all steps autonomously, plus a dedicated goal. Autopilot is LOCKED. Scope is exactly the four fixes.
- **DEC-20261001-088** — One-line autopilot lock order for a hardening task.
  > start auto pilot for the task.
- **DEC-20261001-102** — Autopilot through QA/fix/review; closure keeps the explicit approval word.
  > Autopilot locked (manager approved like 261). Hands chain QA -> fix -> review -> closure solo; closure still needs the explicit approval word.
- **DEC-20261001-103** — One-line autopilot lock order.
  > start auto pilot
- **DEC-20261001-137** — In autopilot mode, do not use approval relay-pause; record the verdict and do not ask the human.
  > Approval relay-pause does not apply in autopilot — record the verdict, do not ask the human.
- **DEC-20261001-173** — Manager set the planning request under locked autopilot mode.
  > Planning request in locked autopilot.
- **DEC-20261001-185** — Authorize full automatic planning and implementation of A1 and A2 without intermediate approval.
  > Task A1 and A2 and plan and implement then full automatically
- **DEC-20261001-186** — Confirm autopilot locked mode: plan through Brain then implement without separate plan-approval pause.
  > Autopilot is locked; the standing order says plan through the Brain and then implement without a separate plan-approval pause.
- **DEC-20261001-193** — Under the full-automatic standing order, a reviewer technical APPROVED with PO_REVIEW_PENDING is treated as the Manager closure approval.
  > Full-automatic standing order is active (manager/full_automatic_mode): the reviewer technical APPROVED + PO_REVIEW_PENDING acts as the Manager closure approval
- **DEC-20261001-202** — Adopt autopilot baseline mode for new tasks: plan first, then fix automatically, then extract the Manager's decisions from the old and new task and save them.
  > a new task need and use auto pilot baseline mode so first plan them then fix automaticall, at end extraxt my desctions from old and new tsak and save them

### tooling (14)

- **DEC-20260913-009** — Restart handshake: Hands prepares everything (env, global sync, timeouts), tells manager to restart OpenCode, verifies post-restart state (mcp list 7/7) before 
  > I restarted
- **DEC-20260913-012** — Mechanical permission-layer lock: executor agents can never run git add/checkout/commit/push via bash (deny in repo + global opencode.json); all git writes go t
  > restore the denies the cognitve exexture never can run git checkout, git push, git commit, the git maange by mcp servers.
- **DEC-20260913-025** — On approval-for-closure the Hands must commit through the sanctioned MCP commit path (stage_and_inject_diff + commit_and_clean_task over MCP stdio), never raw g
  > تو باید با s-mcp-inject-diff-clean صدا بزنی که خودش کامیت رو بکنه.
- **DEC-20260916-003** — Standing order: wrap all test-verdict runs with rtk test (token collapse, exit code preserved); failures keep full output via rtk recall.
  > why you does not call rtk for testing?
- **DEC-20260920-003** — Fix our own transcript storage instead of migrating to LiteLLM, and make every Responses-API server conform to the OpenAI Responses API documentation.
  > i choose R3 too. read the response api docs and make sure you follow them for both mcps servers we have taht used repsonse api.
- **DEC-20260927-003** — Staging Zarinpal set to sandbox mock (code supports merchant_id=sandbox); parse service recreated to pick up env.
  > check cloud logs direct payment need valid or at least correct mock .env for zarinpal. check and fix and restart server and tell me restarted them
- **DEC-20260927-007** — Manual rotate helper must be a global zero-argument command (rr) that auto-detects and rotates the currently active node.
  > it must full automatic and you need install it globaly to my ~/.local/bin or some where i and also i just run it like rotate or something or rr it auto roatte current active.
- **DEC-20261001-003** — Force double-quoted YAML scalars for REALITY public-key/short-id so Go-YAML cannot misread hex values such as 2e00 as a float.
  > fix the REALITY short-id quoting bug the new feed exposed
- **DEC-20261001-030** — B2 - crawl the Bazaar, Myket and Play referrer docs and store them in docs/bazaar, docs/myket and docs/play.
  > داکیومنتش رو داخل پوشه داکس خودمون هم توی پوشه بازار و پوشه مایکت بنویس
- **DEC-20261001-078** — Verify features only through Docker; never run the server on the host.
  > All feature verification must run through Docker (`docker run --rm -i`); Firefox/Browsh/html2markdown are not installed on the host.
- **DEC-20261001-121** — Limit re-emitted XML to 3500 tokens and omit prose outside the XML.
  > Hard cap 3500 tokens. Lean output, no prose outside the XML.
- **DEC-20261001-160** — Constrained closure XML to no shell and no git mv; use MCP commit path only because Hands lacks shell capability.
  > Constraints for the XML: the Hands session has NO shell tool — only read/edit/glob/grep/skill/webfetch/question/execute(Code Mode: brain, lint, custom_context incl. stage_and_inject_diff/commit_and_cl
- **DEC-20261001-205** — Adopt DECISION_TRANSCRIPT_MAX_CHARS with default 131072 characters, blank-means-unset, and ValueError on malformed, zero, or negative values.
  > Use an environment variable named `DECISION_TRANSCRIPT_MAX_CHARS`, documented default `131072` (characters), blank-means-unset, with a positive-integer guard that raises `ValueError` on a malformed, z
- **DEC-20261001-220** — Open a new task for the Brain empty-output root cause: MCP-side retry hint plus stronger MCP-server lints.
  > بعد من گاهاً دیدم وقتی چیزی از برین می‌پرسی، برین بهت جواب نمی‌ده؛ اوتپوتش خالیه. چرا؟ این مورد رو هم روت‌کیسش رو پیدا کن و توی ام‌سی‌پی برین بتونیم تعریف کنیم مشکل رو حل کنیم که وقتی خالی بود، خود ام

### other (1)

- **DEC-20261001-011** — The `PROXY` entry seen in the balancer is the select group's own name, not a node or bug; answer with evidence (DB rows plus controller lookup).
  > also i see in balaner a proxy with named `PROXY` selected what is it? it a bug? crate task and handle both of them

## Provenance

- Rebuilt: 2026-10-01 from 326 records.
- Sources: migrated per-project stores (apex, blowsh-mcp, cognitive-lead-hq, dumble),
  scattered 2026-10-01 records, and the home `v2ray-to-subs` store (empty).
- Fidelity note: records marked `reconstructed` are training data, not verbatim quotes.

