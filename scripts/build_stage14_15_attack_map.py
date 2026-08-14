#!/usr/bin/env python3
"""Build an AI-readable Stage14/15 bound-attack ledger from every result.md."""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import subprocess
from pathlib import Path


TARGET_PATTERNS = {
    "UPPER": r"upper bound|upper-bound|上界|\\ll|\bO\s*\(",
    "LOWER": r"lower bound|lower-bound|下界|construction|constructive|\\gg",
    "ASYMPTOTIC": r"asymptotic|asymptotic formula|\\sim|\\asymp|Theta|真の指数|leading constant",
    "UNBOUNDEDNESS": r"unbounded|infinite family|infinitely many|無限族|positive-power",
    "ZERO_DENSITY": r"zero[- ]density|density zero|ratio.*(?:to|\\to)\s*0|survival",
    "CAUSAL": r"causal|mechanism|obstruction|restriction|double charge|interaction",
    "COMPUTATION": r"census|enumerat|computation|finite data|benchmark|SHA-256|regression",
}

METHOD_PATTERNS = {
    "PARAMETRIC_CONSTRUCTION": r"parametri|explicit family|construction|Saunderson|Pythagorean parametr",
    "INCIDENCE_GRAPH": r"incidence graph|face graph|vertex degree|raw-pair|edge ledger",
    "ELLIPTIC_GENUS_ONE": r"elliptic|genus[- ]one|Mordell|Selmer|rank",
    "K3_SURFACE_COVER": r"K3|degree[- ]two cover|double cover|surface",
    "GAUSSIAN_SQUARECLASS": r"Gaussian|squareclass|squarefree kernel|sf\(|norm parity",
    "LOCAL_CONGRUENCE_VALUATION": r"local dens|congruence|mod(?:ulo)?\s|valuation|v_p|quadratic residue|squareclass",
    "SIEVE_CHARACTER_SUM": r"sieve|character sum|large sieve|Selberg|Wiener|Hecke|Dirichlet",
    "DIVISOR_RECONSTRUCTION": r"divisor|difference of squares|factor pair|reconstruct|support",
    "LATTICE_GEOMETRY": r"lattice|geometry of numbers|volume|coarea|chamber|Peyre|Tamagawa",
    "FINITE_CENSUS_REGRESSION": r"census|enumerat|finite|benchmark|regression|SHA-256|exact count",
    "LITERATURE_ADAPTER": r"literature|external theorem|published|citation|adapter",
    "NEGATIVE_ROUTE_CERTIFICATE": r"cannot|does not prove|insufficient|no .*proved|blocked|open_gate|negative result",
}

SIGNATURE_PATTERNS = {
    "PYTHAGOREAN_FACE": r"Pythagorean|Euclid parametr|m\^2\s*[-+]\s*n\^2|2mn",
    "INTEGRAL_SPACE_DIAGONAL": r"space diagonal|R\s*(?:in|\\in).*Z|d\^2\s*=\s*a\^2",
    "EXACTLY_TWO_FACES": r"exactly[- ]two|two[- ]face|N_2|M_2|A_2|B_2",
    "THREE_FACES_EULER": r"Euler cuboid|Euler brick|three[- ]face|M_3",
    "PAIRED_NORMS": r"paired.*norm|A\s*=.*N\(|B\s*=.*N\(|AB.*square",
    "MOVING_MODULUS": r"moving modulus|growing modulus|fixed[- ]U|residue class",
    "COMMON_CORE": r"common core|lost core|common gcd|shared factor|square divisor",
    "DIRECTIONAL_CHAMBER": r"directional|chamber|ordered sector|N_a|N_b|N_c",
    "OVERLAP_INTERSECTION": r"overlap|intersection|shared edge|survivor ratio",
}

OUTCOME_PATTERNS = [
    ("OPEN_GATE", r"OPEN_GATE|open gate"),
    ("BLOCKED", r"\bBLOCKED\b|NEW_INPUT_REQUIRED=true"),
    ("NEGATIVE", r"negative result|route.*(?:cannot|fails)|does not deliver|impossible under|no-go"),
    ("PROVED", r"\bPROVED\b|theorem proved|we prove|AUDIT_VERDICT=PASS|STATUS: \*\*PASS"),
    ("COMPUTED", r"\bCOMPUTED\b|exact finite census|census.*complete|benchmark.*complete"),
    ("PARTIAL", r"partial|conditional|candidate|pending|heuristic"),
]


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True, errors="replace")


def matches(pattern: str, text: str) -> bool:
    return re.search(pattern, text, re.I | re.S) is not None


def extract_lines(text: str, pattern: str, limit: int = 8) -> list[str]:
    out = []
    for raw in text.splitlines():
        line = " ".join(raw.strip().split())
        if line and re.search(pattern, line, re.I):
            out.append(line[:500])
            if len(out) >= limit:
                break
    return out


def marker_values(text: str) -> dict[str, str]:
    keys = re.findall(r"(?m)^\s*([A-Z][A-Z0-9_]{2,})\s*=\s*(.+?)\s*$", text)
    return {k: v[:500] for k, v in keys[-80:]}


def classify_outcome(text: str, markers: dict[str, str]) -> str:
    status_blob = " ".join(f"{k}={v}" for k, v in markers.items()) + "\n" + text[:12000]
    for label, pattern in OUTCOME_PATTERNS:
        if matches(pattern, status_blob):
            return label
    return "UNCLASSIFIED"


def series_id(path: str) -> str:
    task = path.split("/")[-2]
    m = re.match(r"(.+?)(?:\d+[a-z]*)?$", task, re.I)
    return (m.group(1).rstrip("-_") if m else task) or task


def build(repo: Path, ref: str) -> tuple[list[dict], dict, str]:
    worktree_mode = ref == "WORKTREE"
    if worktree_mode:
        paths = [str(p.relative_to(repo)) for root in (repo / "stages/stage14", repo / "stages/stage15") for p in root.rglob("*") if p.is_file()]
    else:
        paths = git(repo, "ls-tree", "-r", "--name-only", ref, "stages/stage14", "stages/stage15").splitlines()
    results = sorted(p for p in paths if p.endswith("/result.md"))
    pathset = set(paths)
    entries = []
    for index, path in enumerate(results, 1):
        text = (repo / path).read_text(encoding="utf-8", errors="replace") if worktree_mode else git(repo, "show", f"{ref}:{path}")
        markers = marker_values(text)
        title = next((x.lstrip("# ").strip() for x in text.splitlines() if x.startswith("#")), path)
        targets = [k for k, p in TARGET_PATTERNS.items() if matches(p, text)]
        methods = [k for k, p in METHOD_PATTERNS.items() if matches(p, text)]
        signatures = [k for k, p in SIGNATURE_PATTERNS.items() if matches(p, text)]
        outcome = classify_outcome(text, markers)
        audit_path = path.rsplit("/", 1)[0] + "/audit.md"
        status_path = path.rsplit("/", 1)[0] + "/status.txt"
        evidence = extract_lines(text, r"\\(?:ll|gg|sim|asymp|to)|Theta|upper bound|lower bound|OPEN_GATE|does not prove|not proved|finite census", 10)
        missing = extract_lines(text, r"missing|remain(?:s|ing)?|unproved|not proved|does not prove|requires? (?:a |an )?new|open_gate|next=|blocked", 8)
        failure = extract_lines(text, r"fails?|failure|cannot|insufficient|obstruction|not enough|no-go|does not deliver", 6)
        superseded = extract_lines(text, r"supersed|replac|stronger than|prior .* remains valid", 4)
        confidence = "HIGH" if markers and (targets or methods) else "MEDIUM" if targets or methods else "LOW"
        review_required = confidence == "LOW" or outcome in {"UNCLASSIFIED", "PARTIAL", "BLOCKED"} or not targets
        entries.append({
            "attack_id": f"S1415-ATTACK-{index:04d}",
            "source_stage": "Stage14" if "/stage14/" in path else "Stage15",
            "series": series_id(path),
            "task": path.split("/")[-2],
            "source_path": path,
            "source_blob_sha256": hashlib.sha256(text.encode()).hexdigest(),
            "title": title,
            "pr_references": sorted(set(re.findall(r"(?:PR\s*#|pull/)(\d+)", text, re.I))),
            "status_markers": markers,
            "target": targets or ["UNCLASSIFIED"],
            "method_family": methods or ["UNCLASSIFIED"],
            "structural_signature": signatures or ["UNCLASSIFIED"],
            "result": outcome,
            "bound_or_claim_evidence": evidence,
            "population_evidence": extract_lines(text, r"population|primitive|canonical|exactly[- ](?:one|two)|three face|Euler cuboid", 6),
            "cutoff_evidence": extract_lines(text, r"cutoff|d\s*<=\s*B|R\s*<=\s*B|height", 5),
            "multiplicity_evidence": extract_lines(text, r"multiplicity|dedup|canonical key|counted once|orientation|permutation", 5),
            "missing_input": missing,
            "failure_reason_evidence": failure,
            "supersession_evidence": superseded,
            "audit_path": audit_path if audit_path in pathset else None,
            "status_path": status_path if status_path in pathset else None,
            "reusable_for": extract_lines(text, r"reuse|future use|handoff|receiver|Stage2[1-8]|NEXT=", 6),
            "extraction_confidence": confidence,
            "review_required": review_required,
            "theorem_claim_from_extraction": False,
        })

    def count_list(field: str) -> dict[str, int]:
        c = collections.Counter(v for e in entries for v in e[field])
        return dict(sorted(c.items(), key=lambda kv: (-kv[1], kv[0])))

    coverage = {
        "schema_version": 1,
        "source_ref": ref,
        "scope": ["stages/stage14/**/result.md", "stages/stage15/**/result.md"],
        "total_result_files": len(entries),
        "by_stage": dict(collections.Counter(e["source_stage"] for e in entries)),
        "by_result": dict(collections.Counter(e["result"] for e in entries)),
        "by_series": dict(collections.Counter(e["series"] for e in entries).most_common()),
        "by_target": count_list("target"),
        "by_method_family": count_list("method_family"),
        "by_structural_signature": count_list("structural_signature"),
        "confidence": dict(collections.Counter(e["extraction_confidence"] for e in entries)),
        "review_required_count": sum(e["review_required"] for e in entries),
        "audited_neighbor_count": sum(bool(e["audit_path"]) for e in entries),
        "coverage_semantics": {
            "PROVED": "source text contains a proof/pass marker; inspect source before reuse",
            "NEGATIVE": "source records a failed or insufficient route",
            "UNCLASSIFIED": "automatic classifier found no reliable class; this is a discovery queue, not absence",
            "review_required": "human/AI targeted reading required before a strongest/no-known/open-gate claim",
        },
        "prohibitions": [
            "machine classification is not a theorem audit",
            "absence from a method cluster does not prove the viewpoint was never considered",
            "NO_MATCH and no-new-viewpoint claims require targeted review of LOW/UNCLASSIFIED/PARTIAL/BLOCKED entries",
        ],
    }

    top_methods = list(coverage["by_method_family"].items())[:12]
    top_signatures = list(coverage["by_structural_signature"].items())[:12]
    md = [
        "# Stage14/15 bound-attack map",
        "",
        "`STATUS=AI_READABLE_DISCOVERY_INDEX`",
        "",
        f"This map inventories all **{len(entries)}** `result.md` files under Stage14 and Stage15. It is a discovery interface, not a replacement for the sources or audits.",
        "",
        "## Purpose",
        "",
        "Use this map before claiming a strongest bound, missing lower bound, new mechanism, or OPEN_GATE. Search the JSONL by population, target, method family, structural signature, failure reason, and missing input; then read every candidate source selected for reuse or rejection.",
        "",
        "## Generated artifacts",
        "",
        "- `docs/stage14-15-bound-attack-ledger/manifest.json` — shard manifest for the complete ledger.",
        "- `docs/stage14-15-bound-attack-ledger/part-*.jsonl` — one record for every result file, split for GitHub/API readability.",
        "- `docs/stage14-15-bound-coverage.json` — aggregate coverage and review queue counts.",
        "- `scripts/build_stage14_15_attack_map.py` — deterministic regenerator.",
        "",
        "## Coverage summary",
        "",
        f"- Stage14 records: {coverage['by_stage'].get('Stage14', 0)}",
        f"- Stage15 records: {coverage['by_stage'].get('Stage15', 0)}",
        f"- Records requiring targeted review: {coverage['review_required_count']}",
        f"- Records with a neighboring `audit.md`: {coverage['audited_neighbor_count']}",
        "",
        "### Method families",
        "",
        "| Family | Records |",
        "|---|---:|",
    ]
    md += [f"| `{k}` | {v} |" for k, v in top_methods]
    md += ["", "### Structural signatures", "", "| Signature | Records |", "|---|---:|"]
    md += [f"| `{k}` | {v} |" for k, v in top_signatures]
    md += [
        "",
        "## Required consumer procedure",
        "",
        "1. Filter the ledger for the target population and bound direction.",
        "2. Search both direct terminology and structural signatures.",
        "3. Inspect accepted candidates and every plausible rejected candidate in the source.",
        "4. Check population, cutoff, multiplicity, measure, quantifier order, and audit status.",
        "5. Review LOW/UNCLASSIFIED/PARTIAL/BLOCKED entries before asserting no compatible route exists.",
        "6. Record accepted/rejected attack IDs in the Stage21–28 discovery ledger.",
        "",
        "## Interpretation boundary",
        "",
        "The ledger answers *what repository artifacts appear to have attacked which structures, and where they stopped*. It cannot prove that no genuinely new viewpoint exists. `UNCLASSIFIED` and `review_required=true` are explicit invitations for targeted AI reading.",
        "",
        "## Reproduction",
        "",
        "```bash",
        "python3 scripts/build_stage14_15_attack_map.py --repo . --ref HEAD --out docs",
        "```",
    ]
    return entries, coverage, "\n".join(md) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--ref", default="HEAD")
    ap.add_argument("--out", type=Path, default=Path("docs"))
    args = ap.parse_args()
    entries, coverage, md = build(args.repo.resolve(), args.ref)
    args.out.mkdir(parents=True, exist_ok=True)
    ledger_dir = args.out / "stage14-15-bound-attack-ledger"
    ledger_dir.mkdir(parents=True, exist_ok=True)
    max_bytes = 700_000
    shards, current, current_bytes = [], [], 0
    for entry in entries:
        line = json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n"
        size = len(line.encode("utf-8"))
        if current and current_bytes + size > max_bytes:
            shards.append(current)
            current, current_bytes = [], 0
        current.append(line)
        current_bytes += size
    if current:
        shards.append(current)
    manifest_parts = []
    for i, lines in enumerate(shards, 1):
        name = f"part-{i:04d}.jsonl"
        payload = "".join(lines)
        (ledger_dir / name).write_text(payload, encoding="utf-8")
        manifest_parts.append({"path": f"docs/stage14-15-bound-attack-ledger/{name}", "records": len(lines), "sha256": hashlib.sha256(payload.encode()).hexdigest()})
    (ledger_dir / "manifest.json").write_text(json.dumps({"schema_version": 1, "total_records": len(entries), "parts": manifest_parts}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out / "stage14-15-bound-coverage.json").write_text(
        json.dumps(coverage, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (args.out / "stage14-15-bound-attack-map.md").write_text(md, encoding="utf-8")


if __name__ == "__main__":
    main()
