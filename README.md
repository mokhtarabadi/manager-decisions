# manager-decisions

A personal decision store. It records the rulings, trade-offs and constraints
of one person, and exposes them so an agent can decide the way that person
would instead of paging him.

Today the owner is the manager of the Cognitive Lead AI system. His own agents
read this repo through the `manager_decisions` MCP server. The longer-term
purpose is wider: when a colleague needs a decision that belongs to him, their
agent can read this repo and act with his judgment instead of waiting.

## What problem this solves

Most instructions from a person are lost the moment the chat ends. A decision
that took ten minutes to reach is re-litigated a week later. This repo makes
each ruling a durable, quotable record, and then summarizes the pattern behind
those rulings into a profile.

Two artifacts come out of that:

- **Records** — one per ruling, with the manager's own words kept verbatim.
- **A profile** — a short document describing how he decides, built only from
  rulings he has approved.

## Layout

```
decisions/
  INDEX.md                        index of every record, regenerated on each write
  2026/09/
    DEC-20260921-001.json         the machine record
    DEC-20260921-001.md           the same record, formatted for humans
samples/
  manager_profile.md              the profile: curated baseline + approved promotions
scripts/
  compile_profile.py              read-only compiler for the next profile promotion
```

## Anatomy of a record

Every record carries these required fields:

| Field                 | Meaning                                                                        |
| --------------------- | ------------------------------------------------------------------------------ |
| `decision_id`         | `DEC-YYYYMMDD-NNN`, assigned by the server                                     |
| `timestamp`           | ISO-8601 UTC timestamp                                                         |
| `project_name`        | the project the ruling belongs to                                              |
| `verbatim_quote`      | the manager's own words: `{original, english_translation}`                     |
| `extracted_decision`  | `{summary, category, rationale, alternatives[], tradeoffs}`                    |
| `redaction_verified`  | set to `true` by the server only after the scrub gate passes                   |

Optional fields, with safe defaults:

| Field         | Values                                | Default     |
| ------------- | ------------------------------------- | ----------- |
| `fidelity`    | `verbatim`, `reconstructed`           | `verbatim`  |
| `mode`        | `manual`, `autopilot`                 | `manual`    |
| `scope`       | `standing`, `episode`                 | `episode`   |
| `goal_ref`    | free string                           | empty       |
| `fingerprint` | 64-char sha256 over the deciding text | computed    |

`category` is a closed set of eight values: `architecture`, `process`,
`scope`, `quality-gate`, `tooling`, `release`, `other`, `autopilot-cycle`.

Two fields are stamped by the server and are never written by hand:
`active_root` (the store's display name, never an absolute path) and
`store_mode` (`personal` or `project-fallback`).

## How a record comes to exist

The only writer is the `manager_decisions` MCP server, which lives in the
`cognitive-lead-hq` repository under `mcp-decision-server/`.

1. **Capture.** A ruling is extracted from a session transcript, or the manager
   states it directly.
2. **Confirm.** Nothing is recorded until the manager approves the candidate.
   Auto-recording is forbidden by policy, not just by convention.
3. **Scrub.** Every free-text field is sanitized. The gate fails closed: if any
   sensitive pattern survives, the write is refused.
4. **Validate.** Required fields, id shape, timestamp, non-empty quote, known
   category, enum values and fingerprint are all checked before anything lands.
5. **Write.** The `.json` record and its `.md` companion are written, then
   `INDEX.md` is regenerated.

## Privacy

- Records are scrubbed of provider API keys (`sk-`, `ghp_`, `AIzaSy`), Bearer
  tokens, private IPv4 ranges and generic credential assignments.
- A verification pass runs after sanitizing. Any surviving match blocks the
  write; there is no bypass flag.
- Absolute filesystem paths are never stored in a record. Only the store's
  display name is kept.
- Quoted material is limited to what the manager actually said, which is the
  point of the `verbatim_quote` field.

## Reading the profile

`samples/manager_profile.md` has three kinds of section:

- **Baseline** — hand-curated guidelines, architecture preferences and decision
  heuristics. This is the only section edited directly.
- **Promotions** — dated aggregates, each compiled from records not yet cited
  and each merged only after explicit manager approval.

Never hand-edit a generated section. Propose a change, get approval, then
append a new dated section. Prior sections are never rewritten.

## Consuming this repo from another agent

1. **Read `samples/manager_profile.md` first.** It is the compact form of the
   manager's standing judgment and costs little context.
2. **Then search the records** for the topic at hand. Records carry the real
   evidence; the profile carries the pattern.
3. **Prefer `fidelity: verbatim` records.** Reconstructed records are training
   data and are excluded from the profile's promotion weight.
4. **Cite the record id** when you rely on a ruling, for example
   `DEC-20260913-004`. An uncited claim about his judgment is a guess.
5. **Respect the scope.** A ruling made for one project may not transfer to
   another. If the record's `project_name` differs from yours, treat it as
   guidance, not as an order.
6. **Ask when the record is silent.** A missing ruling is not permission.

## Boundaries

This repo records what one person decided in his own context. Applying those
decisions to someone else's work is a judgment call, and the caller owns it.
The profile is evidence about a person, not an authority over a project.

If a decision here would be irreversible, expensive, or affect another person,
ask the manager directly. Do not infer consent from a nearby record.

## Conventions

- Commits are `docs: record manager decisions`.
- History is append-only. Records are never rewritten; corrections arrive as
  new records.
- Generated sections are only ever appended, never edited in place.
- The compiler `scripts/compile_profile.py` is read-only by design. It drafts;
  a human approves; a separate step merges.

## Related

- `cognitive-lead-hq` — the framework repository. It holds the
  `mcp-decision-server/` MCP server that writes and reads this store, the
  `manager-decision` skill, and `docs/manager-decisions.md`, which documents
  each of the six tools in schema detail.
