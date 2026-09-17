"""Compile a manager-profile evolution draft from new decision records.

Read-only tool for the `propose_profile_evolution` MCP path. It scans
``decisions/YYYY/MM/DEC-*.json`` under the repo, subtracts every record
already cited in ``samples/manager_profile.md``, and prints a staged
draft payload to stdout. It NEVER writes to the sample or the store:
the manager review gate owns every merge.

Exit contract (consumed by `mcp-decision-server/server.py`):
  exit 0 + draft on stdout            -> DRAFT_READY
  exit 0 + "No decisions found..."    -> EMPTY
  exit != 0 (stderr carries reason)   -> ERROR
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

ID_PATTERN = re.compile(r"DEC-\d{8}-\d{3}")


def _load_records(decisions_dir: Path) -> list[dict]:
    records = []
    if not decisions_dir.is_dir():
        return records
    for path in sorted(decisions_dir.rglob("DEC-*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if isinstance(data, dict) and data.get("decision_id"):
            records.append(data)
    records.sort(key=lambda r: str(r.get("decision_id", "")))
    return records


def _cited_ids(profile_path: Path) -> set[str]:
    if not profile_path.is_file():
        return set()
    try:
        text = profile_path.read_text(encoding="utf-8")
    except OSError:
        return set()
    return set(ID_PATTERN.findall(text))


def _one_line(text: object, limit: int = 160) -> str:
    flat = " ".join(str(text or "").split())
    return flat if len(flat) <= limit else flat[: limit - 1] + "…"


def _build_draft(records: list[dict]) -> str:
    today = datetime.date.today().isoformat()
    lines = [
        "## Proposed profile promotion (UNREVIEWED DRAFT — needs manager approval)",
        "",
        f"_Source: {len(records)} new decision(s) not yet cited in the sample ({today})._",
        "",
        "### Category distribution (new records)",
        "",
    ]
    counts: dict[str, int] = {}
    for rec in records:
        cat = str(rec.get("extracted_decision", {}).get("category", "uncategorized"))
        counts[cat] = counts.get(cat, 0) + 1
    for cat in sorted(counts):
        lines.append(f"- {cat}: {counts[cat]}")
    lines += ["", "### Ruling clusters (new records)", ""]
    by_cat: dict[str, list[dict]] = {}
    for rec in records:
        cat = str(rec.get("extracted_decision", {}).get("category", "uncategorized"))
        by_cat.setdefault(cat, []).append(rec)
    for cat in sorted(by_cat):
        lines.append(f"- **{cat}**")
        for rec in by_cat[cat]:
            rid = rec.get("decision_id", "?")
            ext = rec.get("extracted_decision", {})
            lines.append(f"  - {rid}: {_one_line(ext.get('summary'))}")
            lines.append(f"    Rationale: {_one_line(ext.get('rationale'))}")
    non_verbatim = [
        str(r.get("decision_id", "?"))
        for r in records
        if r.get("fidelity", "verbatim") != "verbatim"
    ]
    standing = [
        str(r.get("decision_id", "?"))
        for r in records
        if r.get("scope") == "standing"
    ]
    lines += ["", "### Dissent / deferred notes", ""]
    if non_verbatim:
        lines.append(
            "- Non-verbatim records stay training data, excluded from "
            f"promotion weight: {', '.join(non_verbatim)}."
        )
    else:
        lines.append("- All new records are verbatim fidelity.")
    if standing:
        lines.append(
            "- Standing scopes without expiry in this batch: "
            f"{', '.join(standing)}."
        )
    else:
        lines.append("- No standing scopes in this batch.")
    lines += [
        "- Merge rule: append a new dated aggregate section to the sample; "
        "never edit prior promoted sections in place.",
        "",
        "Reply APPROVED to merge, or REJECTED with rationale to drop.",
    ]
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="Decision repo root")
    args = parser.parse_args(argv)
    repo = Path(args.repo)
    records = _load_records(repo / "decisions")
    if not records:
        print("No decisions found in the store.")
        return 0
    cited = _cited_ids(repo / "samples" / "manager_profile.md")
    new_records = [r for r in records if str(r.get("decision_id")) not in cited]
    if not new_records:
        print("No decisions found since the last profile promotion.")
        return 0
    sys.stdout.write(_build_draft(new_records))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
