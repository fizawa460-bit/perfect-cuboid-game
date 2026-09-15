#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

WIDTH = 113
WAVES = ("CUT193", "CUT194", "CUT195", "CUT196", "CUT197", "CUT198")
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
GROUPS = [[101, 102, 103], [97, 98, 99], [93, 94, 95, 96]]
EXPECTED = {
    "n404_audit_blob": "db0e4b0302ab244664995c236b08359678c25b54",
    "n404_audit_canonical": "2bbe7cd04075a46bdcfa025b3358113bf8520d6dcfcdc044a7d5c2740a99d67c",
    "n391_result_blob": "3e72cea011e5a519173a710c20d88bc781c4cee8",
    "n391_result_canonical": "2b30f97aca0873568c324cf9a88ba6dc8ee0e3cceb29e1fc60e9e2c978b02da3",
    "indexer_blob": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
}

# Each clause is a conjunction of intrinsic modular equalities.  If any clause
# matches, required x49 parity is 0; otherwise the default parity is 1.
CLAUSES = [
    (("c", 5, 0),),
    (("a", 3, 0), ("block", 16, 5)),
    (("b", 2, 0), ("block", 7, 2)),
    (("b", 3, 0), ("block", 3, 2)),
    (("c", 2, 0), ("block", 14, 0)),
    (("c", 3, 1), ("block", 7, 6)),
    (("block", 7, 6), ("block", 12, 7)),
]
EXPECTED_CLAUSE_BLOCK_COUNTS = [14, 2, 3, 3, 10, 3, 2]
EXPECTED_MATCH_MULTIPLICITY = {0: 70, 1: 17, 2: 10}
EXPECTED_CLASSIFICATION_STREAM_SHA256 = "ea97105eca6f2154dca27661e00b3c3b5020001c96048b2d52e443524c56d8f1"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def checked(path: Path, expected_blob: str, expected_canonical: str) -> dict:
    req(path.is_file(), f"missing source: {path}")
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    req(claimed == expected_canonical, f"stored canonical drift: {path}")
    req(csha(body) == expected_canonical, f"canonical drift: {path}")
    return obj


def clause_matches(row: dict, clause: tuple[tuple[str, int, int], ...]) -> bool:
    return all(row[field] % modulus == residue for field, modulus, residue in clause)


def main() -> None:
    repo = Path(__file__).resolve().parents[5]
    node_root = repo / "stages/stage32/32-01-178/nodes"
    residual = repo / "stages/stage32/residual-32-01-production"

    audit404 = checked(node_root / "N404/AUDIT-PASS.json", EXPECTED["n404_audit_blob"], EXPECTED["n404_audit_canonical"])
    n391 = checked(node_root / "N391/RESULT.json", EXPECTED["n391_result_blob"], EXPECTED["n391_result_canonical"])
    req(audit404["status"] == "HOSTILE_AUDIT_PASS_RETAINED", "N404 audit receipt status drift")
    req(audit404["hostile_audit"]["verdict"] == "PASS", "N404 hostile-audit verdict drift")
    req(audit404["accepted_scope"]["decision_tree_leaf_count"] == 13, "N404 leaf-count drift")
    req(audit404["route_control"]["n405_permitted_after_receipt"] is True, "N405 not permitted by N404 receipt")

    idx_path = residual / "compressed_terminal_indexer.py"
    fam_path = residual / "compressed_terminal_family.py"
    req(blob(idx_path) == EXPECTED["indexer_blob"], "indexer blob drift")
    req(blob(fam_path) == EXPECTED["family_blob"], "family blob drift")
    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer

    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget + 1 == WIDTH, "terminal width drift")
    blocks: list[int] = []
    for wave in WAVES:
        blocks.extend(map(int, n391["waves"][wave]["residual_blocks"]))
    req(len(blocks) == 97 and len(set(blocks)) == 97, "N391 residual block union drift")

    entries: list[dict] = []
    parity_counts = Counter()
    survivor_total = 0
    for block in blocks:
        base = list(map(int, idx.unrank(block * WIDTH)))
        req(base[4] == 0, f"base x49 drift at block {block}")
        by = dict(zip(ASSIGNMENT_ORDER, base))
        sums = [sum(by[label] for label in group) for group in GROUPS]
        required = (by[93] + by[96]) & 1
        req(required == ((1 - by[98]) & 1), f"N399 parity relation drift at block {block}")
        survivors = sum(1 for x49 in range(WIDTH) if (x49 & 1) == required)
        parity_counts[required] += 1
        survivor_total += survivors
        entries.append({
            "block": block,
            "a": sums[0],
            "b": sums[1],
            "c": sums[2],
            "b_minus_c": sums[1] - sums[2],
            "required_x49_parity": required,
        })

    req(dict(sorted(parity_counts.items())) == {0: 27, 1: 70}, "required parity distribution drift")
    req(survivor_total == 5459, "N399 survivor reconstruction drift")

    clause_counts: list[int] = []
    for clause in CLAUSES:
        matched = [row for row in entries if clause_matches(row, clause)]
        req(matched, f"empty retained clause: {clause}")
        req({row["required_x49_parity"] for row in matched} == {0}, f"non-pure clause: {clause}")
        clause_counts.append(len(matched))
    req(clause_counts == EXPECTED_CLAUSE_BLOCK_COUNTS, f"clause coverage regression: {clause_counts}")

    stream: list[str] = []
    conflicts = 0
    multiplicity = Counter()
    zero_union: set[int] = set()
    for row in entries:
        hits = [i for i, clause in enumerate(CLAUSES) if clause_matches(row, clause)]
        predicted = 0 if hits else 1
        multiplicity[len(hits)] += 1
        if hits:
            zero_union.add(row["block"])
        conflicts += int(predicted != row["required_x49_parity"])
        stream.append(f'{row["block"]}:{predicted}:{",".join(map(str, hits))}')

    expected_zero_blocks = {row["block"] for row in entries if row["required_x49_parity"] == 0}
    req(zero_union == expected_zero_blocks and len(zero_union) == 27, "zero-parity cover is not exact")
    req(conflicts == 0, f"bounded DNF parity conflicts: {conflicts}")
    req(dict(sorted(multiplicity.items())) == EXPECTED_MATCH_MULTIPLICITY, f"match multiplicity regression: {dict(multiplicity)}")
    stream_sha = hashlib.sha256("\n".join(stream).encode()).hexdigest()
    req(stream_sha == EXPECTED_CLASSIFICATION_STREAM_SHA256, "classification stream drift")

    payload = {
        "semantics": "EXACT_BOUNDED_INTRINSIC_MODULAR_DNF_CLASSIFIER_ON_RETAINED_97_BLOCK_POPULATION_ONLY",
        "source_block_count": 97,
        "source_terminal_count": 10961,
        "survivor_terminal_count": survivor_total,
        "required_parity_block_distribution": {"even": parity_counts[0], "odd": parity_counts[1]},
        "n404_decision_tree_leaf_count": 13,
        "dnf_zero_parity_clause_count": len(CLAUSES),
        "default_parity": 1,
        "classifier_branch_count_including_default": len(CLAUSES) + 1,
        "clause_block_counts": clause_counts,
        "match_multiplicity_distribution": {str(k): v for k, v in sorted(multiplicity.items())},
        "zero_parity_block_count": len(zero_union),
        "classification_conflicts": conflicts,
        "classification_stream_sha256": stream_sha,
        "strictly_fewer_rule_branches_than_n404_tree_leaves": len(CLAUSES) + 1 < 13,
        "optimality_or_minimality_claimed": False,
        "transport_beyond_retained_97_blocks": False,
        "terminal_reenumeration_of_n399_rank_stream": False,
        "n400_main_handoff_reopened": False,
        "additional_pruning_terminals": 0,
        "main_authority_subtraction_performed": False,
        "numerical_leaf_compression_credit": False,
        "full178_complete": False,
        "heavy_compute_authorized": False,
        "merge_authorized": False,
    }
    print("PASS_N405_BOUNDED_MODULAR_DNF_COMPRESSION_PROBE")
    print(f"blocks=97 clauses={len(CLAUSES)} branches={len(CLAUSES)+1} conflicts={conflicts}")
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
