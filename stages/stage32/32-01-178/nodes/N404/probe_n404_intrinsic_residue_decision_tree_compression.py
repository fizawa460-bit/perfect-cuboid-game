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
    "n403_audit_blob": "4630412fe09382de5368661cf9649f81ff60c9e1",
    "n403_audit_canonical": "dddb1125cab8b566c6d7771d03161d601c080e9c87d2a539b6ae5505e050f197",
    "n391_result_blob": "3e72cea011e5a519173a710c20d88bc781c4cee8",
    "n391_result_canonical": "2b30f97aca0873568c324cf9a88ba6dc8ee0e3cceb29e1fc60e9e2c978b02da3",
    "indexer_blob": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
}

# Frozen exact binary decision tree. Internal node:
# (field, modulus, residue, yes_branch, no_branch); leaf is required x49 parity 0/1.
TREE = (
    "b", 4, 1, 1,
    ("block", 14, 5, 1,
     ("block", 18, 3, 1,
      ("a", 3, 2,
       ("block", 9, 0, 1, 0),
       ("block", 12, 0, 0,
        ("block", 11, 7, 0,
         ("block", 13, 7, 0,
          ("block", 16, 10, 0,
           ("block", 19, 2,
            ("b", 2, 0, 1, 0),
            ("block", 16, 15, 0, 1))))))))))


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


def classify(node: object, row: dict, path: str = "") -> tuple[int, str]:
    if isinstance(node, int):
        return node, path
    field, modulus, residue, yes_branch, no_branch = node
    if row[field] % modulus == residue:
        return classify(yes_branch, row, path + "L")
    return classify(no_branch, row, path + "R")


def main() -> None:
    repo = Path(__file__).resolve().parents[5]
    node_root = repo / "stages/stage32/32-01-178/nodes"
    residual = repo / "stages/stage32/residual-32-01-production"

    audit403 = checked(node_root / "N403/AUDIT-PASS.json", EXPECTED["n403_audit_blob"], EXPECTED["n403_audit_canonical"])
    n391 = checked(node_root / "N391/RESULT.json", EXPECTED["n391_result_blob"], EXPECTED["n391_result_canonical"])
    req(audit403["status"] == "HOSTILE_AUDIT_PASS_RETAINED", "N403 audit receipt status drift")
    req(audit403["hostile_audit"]["verdict"] == "PASS", "N403 hostile-audit verdict drift")
    req(audit403["accepted_scope"]["best_class_count"] == 56, "N403 class-count drift")

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
        entries.append({"block": block, "a": sums[0], "b": sums[1], "b_minus_c": sums[1] - sums[2], "required_x49_parity": required})

    req(dict(sorted(parity_counts.items())) == {0: 27, 1: 70}, "required parity distribution drift")
    req(survivor_total == 5459, "N399 survivor reconstruction drift")

    leaves = Counter()
    stream = []
    conflicts = 0
    for row in entries:
        predicted, path = classify(TREE, row)
        if predicted != row["required_x49_parity"]:
            conflicts += 1
        leaves[(path, predicted)] += 1
        stream.append(f'{row["block"]}:{predicted}:{path}')
    stream_sha = hashlib.sha256("\n".join(stream).encode()).hexdigest()
    leaf_counts = [count for (_key, count) in sorted(leaves.items(), key=lambda item: item[0][0])]
    max_depth = max(len(path) for path, _parity in leaves)

    req(conflicts == 0, f"decision-tree parity conflicts: {conflicts}")
    req(len(leaves) == 13, f"leaf-count regression: {len(leaves)}")
    req(max_depth == 10, f"max-depth regression: {max_depth}")
    req(sorted(leaf_counts) == sorted([44, 5, 4, 1, 11, 5, 3, 3, 2, 1, 2, 1, 15]), "leaf-population regression")
    req(stream_sha == "d79f09a4d30e2193166a4ef5f93b5c12a1d453a6fad20ec3cb5c14e718516245", "classification stream drift")

    payload = {
        "semantics": "EXACT_BOUNDED_N403_INTRINSIC_RESIDUE_DECISION_TREE_COMPRESSION_ON_RETAINED_97_BLOCK_POPULATION_ONLY",
        "source_block_count": 97,
        "source_terminal_count": 10961,
        "survivor_terminal_count": survivor_total,
        "required_parity_block_distribution": {"even": parity_counts[0], "odd": parity_counts[1]},
        "n403_cartesian_quotient_class_count": 56,
        "decision_tree_leaf_count": len(leaves),
        "decision_tree_max_depth": max_depth,
        "decision_tree_conflicting_leaf_count": conflicts,
        "leaf_population_counts": [44, 5, 4, 1, 11, 5, 3, 3, 2, 1, 2, 1, 15],
        "classification_stream_sha256": stream_sha,
        "strictly_fewer_partition_cells_than_n403": len(leaves) < 56,
        "optimality_or_minimality_claimed": False,
        "transport_beyond_retained_97_blocks": False,
        "terminal_reenumeration_of_n399_rank_stream": False,
        "n400_main_handoff_reopened": False,
        "additional_pruning_terminals": 0,
        "main_authority_subtraction_performed": False,
        "main_pruning_credit": False,
        "numerical_leaf_compression_credit": False,
        "full178_complete": False,
        "heavy_compute_authorized": False,
        "merge_authorized": False,
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    req(payload["canonical_sha256_without_this_field"] == "c6d4bcd43efc95b312b0bdf22a5d2c6743096440ee3bce98addcebb06d6de466", "payload canonical regression")

    print("PASS_N404_N403_INTRINSIC_RESIDUE_DECISION_TREE_COMPRESSION_PROBE")
    print(f"blocks=97 leaves={len(leaves)} max_depth={max_depth} conflicts={conflicts}")
    print("N404_PROBE_JSON=" + json.dumps(payload, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
