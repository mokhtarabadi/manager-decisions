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
