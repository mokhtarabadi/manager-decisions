# Manager Profile (authoritative copy — personal repo)

> Living sample of the manager's judgment, aggregated from this decision repo
> by `compile_profile.py`. NEVER hand-edit the generated sections;
> propose changes via `propose_profile_evolution` and pass the human review
> gate. Only the hand-written baseline section is curated directly.
> Migrated home from `cognitive-lead-hq:.opencode/decisions/samples/manager_profile.md`
> on 2026-09-14 per explicit Manager approval ("Approve merge clean migrate").

## Baseline behavioral guidelines

- Decide in the open: state the rationale and the rejected alternatives, not just the verdict.
- Prefer reversible decisions; mark irreversible ones explicitly and slow down for them.
- Keep the audit trail: every ruling links to its verbatim quote and session.
- Gate anything that learns or publishes (samples, releases, identity updates) on explicit human approval.
- When ambiguous, ask a pointed question once — then decide and record.

## Architectural preferences

- **Composition over Inheritance** — flat, small modules wired explicitly.
- **FastMCP stdio servers over background daemons** — on-demand tools beat supervised processes (see Task 167: loop-engine retired for persona commands).
- **Append-only records** — transcripts, decisions, sessions; history is never rewritten.
- **Stdlib first** — no new dependency without a stdlib-shaped reason.
- **Deterministic, testable cores** — pure functions with stubbed transports; network only at the edges.

## Decision heuristics

1. **Hard gates stay hard.** Approval, QA, and closure gates never auto-continue on timeout or transport failure.
2. **Precision over recall in classification.** A misrouted report is worse than an unanswered question — prefer the REPORT lane on doubt.
3. **Scope everything shared.** Callback data, sessions, and approvals carry their owner id; foreign input is skipped, never applied.
4. **Discard stale state at gate entry.** A previous session's button press must never resolve the current gate.
5. **Dedupe lineage.** Each instruction reaches the model exactly once; replay is memory, not re-asking.
6. **Fail to a message, never to silence.** Degraded transports return explanatory errors the loop can act on.

## Generated aggregate — first reviewed promotion (2026-09-14, Manager-APPROVED)

_Source: 43 decisions (all with verbatim original + English translation).
Clean check passed: zero records with empty quotes. Promotion excludes nothing._

### Category distribution

- process: 29
- architecture: 5
- scope: 4
- tooling: 3
- quality-gate: 2

### Ruling clusters

- **Autopilot means zero contact** (DEC-20260913-003, DEC-20260913-008, DEC-20260913-017, DEC-20260914-003, DEC-20260914-012): the Hands uses direct Brain access; the Manager sees only Relay questions, final verdicts, and hard blockers. Any manager contact mid-autopilot is a bug.
- **Evidence over claims** (DEC-20260913-007, DEC-20260913-010, DEC-20260913-014): improvements must be evidence-grounded and limited to truly-needed cases; the system finds its own flaws against external evidence.
- **Manager owns publishing** (DEC-20260912-001, DEC-20260913-005, DEC-20260913-012): agents never push; absolute paths stay out of public records; prompt-only rules that fail open get explicit deny rules.
- **Audit trail is append-only** (DEC-20260912-003, DEC-20260913-021, DEC-20260913-023): edits never rewrite history — tombstones, in-loop migration with confirm gates, ordered closure sequences.
- **Voice orders are binding** (DEC-20260913-006, DEC-20260913-015, DEC-20260914-013): dictation typos do not dilute intent; terse approvals are selections; objectives stay verbatim with a cleaned translation beside them.
- **Brain context is non-negotiable** (DEC-20260913-002, DEC-20260913-018, DEC-20260913-019): complete context per call; raw dumps are scrubbed, never stuffed; lost instructions cost whole QA rounds.
- **Kanban stays the single truth** (DEC-20260913-011, DEC-20260913-013, DEC-20260913-016, DEC-20260914-006): task files stay clean, releases compact completed work, the issue tracker feeds the same Kanban.
- **Simple-English handoff** (DEC-20260914-001): the final Manager-facing message stays in simple English so nothing is lost in translation.

### Dissent / deferred notes

- Doppelganger runtime stays deferred: 43 records are too few for unsupervised replay (issue 8 brainstorm).
- Fidelity/mode/scope/goal_ref/fingerprint fields (Task 230 hardening) postdate all 43 records; next promotion should weigh `verbatim`-marked records first.
- No expiry dates set: no standing order in this batch carries one yet.

## Generated aggregate — second reviewed promotion (2026-09-17, Manager-APPROVED)

_Source: 46 decisions not cited in the first promotion (all with verbatim original + English translation, except 4 reconstructed records listed below which stay training data). Clean check passed: zero records with empty quotes. Promotion excludes nothing._

### Category distribution

- process: 25
- quality-gate: 5
- scope: 4
- architecture: 3
- autopilot-cycle: 3
- release: 3
- tooling: 3

### Ruling clusters

- **Full-auto with no session access** (DEC-20260917-007, DEC-20260917-012, DEC-20260917-002, DEC-20260917-008): zero questions to the Manager; the stored standing order supplies authority; every step routes through Brain seats (plan, implement, QA, review); ferrying work through the Manager is a bug.
- **Reviewer verdict as closure stand-in** (DEC-20260917-009, DEC-20260917-013): technical APPROVED plus PO_REVIEW_PENDING satisfies the closure gate when the Manager is unreachable; the Manager reviews the verdict after the commit.
- **Closure stays word-gated when the Manager is present** (DEC-20260917-003, DEC-20260917-005, DEC-20260917-011): only "Approved for closure" or "Close task" count; replayed past rulings never satisfy the gate.
- **ZAC reaffirmed** (DEC-20260917-004, DEC-20260913-025): no autonomous commits ever; closure commits go only through the sanctioned MCP commit path.
- **One-task bundling for coherent repairs** (DEC-20260917-001, DEC-20260917-006): fold the fix plus all priority upgrades into a single task when symptoms share one failure surface; adjacent hardening becomes a new task, not scope creep (DEC-20260917-014).
- **Fallback reporting when tooling itself is broken** (DEC-20260917-010): decision records by default; task-file logs and messages when the record tools are the broken components.
- **English-only reasoning** (DEC-20260917-015, reconstructed): all thinking, reasoning, and responses stay in English even when the Manager writes in Persian; non-English input passes validate-translate-enrich-refactor-execute.
- **Restarts and global sync are a handshake** (DEC-20260913-009, DEC-20260913-026, DEC-20260914-011): global sync means the repo-to-install upgrade; config changes take effect only after the Manager restarts OpenCode; live behavior is verified by the Manager before closure.
- **RTK-first verification is standing** (DEC-20260916-003): all test-verdict runs wrap with rtk test; failures keep full output.
- **Evidence-grounded approvals** (DEC-20260916-001, DEC-20260915-003, DEC-20260915-004, DEC-20260914-002, DEC-20260914-009): plans with file paths and lines get approved with logged assumptions; closures follow QA_PASSED plus technical review; environmental failures are marked failed-as-executed, not blocked.

### Dissent / deferred notes

- Reconstructed records stay training data, excluded from promotion weight: DEC-20260914-014, DEC-20260914-015, DEC-20260916-002, DEC-20260917-015.
- Standing scopes without expiry in this batch: DEC-20260914-015, DEC-20260916-003.
- Doppelganger runtime stays deferred: 71 records are still too few for unsupervised replay.

## Generated aggregate — third reviewed promotion (2026-09-21, Manager-APPROVED)

_Source: 30 new decision(s) not yet cited in the sample (2026-09-21)._

### Category distribution (new records)

- architecture: 4
- autopilot-cycle: 4
- process: 17
- scope: 4
- tooling: 1

### Ruling clusters (new records)

- **architecture**
  - DEC-20260914-005: CSP upgrade-insecure-requests disabled on dev, kept on prod.
    Rationale: Dev is served over plain http on a public IP where the directive breaks login; prod terminates TLS so the hardening stays.
  - DEC-20260914-007: Dev server port moved 8081 to 8082 (8081 held by external proxy).
    Rationale: Port conflict with an unrelated container; moving dev is cheaper than moving shared infra.
  - DEC-20260914-010: Stopped apex-dev-pg container kept (not removed) after compose takeover.
    Rationale: It held the live dev data; removal would destroy the only copy of some rows before verification.
  - DEC-20260920-002: Store the full per-task history durably and bound only the view sent to the model; simple JSON storage is acceptable.
    Rationale: Long sessions must never lose history; the industry pattern is to persist everything and compact only what is sent.
- **autopilot-cycle**
  - DEC-20260915-001: Manager approved fixing all brainstorm gaps via the Hands on autopilot.
    Rationale: Explicit Manager order locks autopilot; Hands executes end-to-end with no approval pauses.
  - DEC-20260915-002: Manager ordered Task 232 implementation on autopilot with Brain planning.
    Rationale: Explicit order names both the task and autopilot mode.
  - DEC-20260918-004: Pre-authorized plan auto-approval is valid only on explicit Manager order; announce and record the lock.
    Rationale: Explicit Manager order waives the standing supervised-approval gate for that run.
  - DEC-20260918-005: On autopilot, QA and review run machine-to-machine; Manager sees only relay questions and final verdict.
    Rationale: Ferrying work through the Manager wastes turns and breaks autopilot.
- **process**
  - DEC-20260912-002: Every stored decision must pass sanitize_text on all free-text fields plus a verify_clean gate; any surviving sensitive pattern raises and nothing is written (…
    Rationale: Raw dumps bloat context and leak secrets; scrubbed rulings stay queryable.
  - DEC-20260913-001: Manager orders Hands to run the QA-review autopilot cycle autonomously and promises closure approval on a pass.
    Rationale: Manager trusts the memorized QA-review cycle and wants verification without his involvement; approval is conditional on a pass.
  - DEC-20260913-004: Task numbers live ONLY in code comments, CHANGELOG, task files, history archives, and HTML comments — never in prompt-facing Markdown prose (anti-hallucination…
    Rationale: Manager observed task-number references in prompt Markdown causing AI hallucination; code comments are fine and welcome.
  - DEC-20260913-020: Telegram message 609 became Task 216 (separate personal decisions repo) via the standard sync pipeline, then autopilot-solved to best quality. Established the …
    Rationale: Manager wants fire-and-forget handling of new Telegram tasks at maximum quality.
  - DEC-20260913-022: One-word 'Approved' after a 3-step plan authorizes full autopilot implementation under the Direct Input protocol.
    Rationale: Plan-and-halt keeps ad-hoc work gated while staying fast.
  - DEC-20260913-024: Nothing destructive (prune/push/restart) happens before the Manager sees the worktree status first.
    Rationale: Status-first is the safety gate before irreversible steps.
  - DEC-20260913-027: Batch approval authorizes migrating all 13 local DEC records; each carries migrated_from provenance (display-name only, no abs paths — public-repo guard).
    Rationale: Explicit batch token satisfies the migration skill's approval gate.
  - DEC-20260914-004: socat port-forward work on the manager script needs no Kanban task file.
    Rationale: Small ops script change; task overhead exceeds the work itself.
  - DEC-20260914-016: Ops via curl only: add the 10 cheapest uncovered collections as EXPLORER_BROAD filters (both markets, 10 TON cap, 5% target), enable AUTO_SCAN_ENABLED via /con…
    Rationale: Manager wants to watch the engine work live with curl-driven ops against the newest binary instead of UI clicks.
  - DEC-20260916-004: QA plus code-reviewer gate order for the 229 cooldown-proof endpoint work (uncommitted debug-controller probe).
    Rationale: Production-facing date/lock logic needs adversarial QA plus review even for a debug-harness endpoint.
  - DEC-20260916-005: File the HQ umbrella issue (became issue 15) with Brain reflect on two bridge bugs, demanding rtk-in-system-prompt plus a fix for missing decision auto-extract…
    Rationale: Truncation-remedy bug plus cross-project task bleed plus silent decision loss are systemic HQ defects, not apex defects.
  - DEC-20260917-016: Save every Manager decision from the session as a manager decision record and update the manager-decision profile sample.
    Rationale: The Manager wants every session ruling preserved as a replayable decision and the manager profile sample kept current so future autopilot consults decide as he…
  - DEC-20260918-002: Report baseline-flow gaps as upstream HQ issues with full evidence; persist decisions via the decision server.
    Rationale: Upstream issues with session evidence let the framework fix the baseline flow.
  - DEC-20260918-003: Telegram sync runs without GitHub issues unless explicitly asked.
    Rationale: Manager wants local task files only; GitHub issues are opt-in per run.
  - DEC-20260919-001: Execute Task 259 under full automatic autopilot: ask no questions, consult all Brain personas via brain_turn, verify RTK-first, and close the task and GitHub i…
    Rationale: Manager standing orders for autopilot task execution of this bug fix. The standing-order expansion is the task-file note the Manager approved; the verbatim quo…
  - DEC-20260920-001: On autopilot, plan through the Brain first and then implement automatically without pausing for a separate plan approval.
    Rationale: The Manager wants end-to-end autonomy while keeping the Brain's planning step in the loop.
  - DEC-20260920-004: Run the new analytics task through the autopilot baseline cycle, using Brain, Blues search, and manager decisions to complete it.
    Rationale: Manager wants the work executed in the established automation workflow with research and decision support.
- **scope**
  - DEC-20260914-008: Curl-driven filter creation runs without a task file, one EXPLORER_BROAD filter per collection.
    Rationale: Bulk ops across 30 collections; per-collection tasks would spam the Kanban with identical items.
  - DEC-20260918-001: No Cando task file for non-Cando framework work.
    Rationale: The HQ repo is a separate project; Cando backlog stays Cando-only.
  - DEC-20260919-002: Extend the same provider-diagnosis fix to mcp-decision-server/server.py inside the current active task instead of opening a new task.
    Rationale: The manager-decisions server shares the empty-envelope failure mode that previously produced a misleading 'decision model returned non-JSON' error.
  - DEC-20260921-001: Broadcast dedup keys on the broadcast identity, not on the message text. Two separate submissions of the same text are two broadcasts and must each deliver; no…
    Rationale: Measured: identical text enqueued twice produced two Broadcast rows, 12 message rows (2 per recipient) and 2 device pushes; two distinct texts produced exactly…
- **tooling**
  - DEC-20260920-003: Fix our own transcript storage instead of migrating to LiteLLM, and make every Responses-API server conform to the OpenAI Responses API documentation.
    Rationale: The provider is stateless, so the defect is local; LiteLLM adds no session storage of its own and would not fix it.

### Dissent / deferred notes

- All new records are verbatim fidelity.
- No standing scopes in this batch.
- Merge rule: append a new dated aggregate section to the sample; never edit prior promoted sections in place.
