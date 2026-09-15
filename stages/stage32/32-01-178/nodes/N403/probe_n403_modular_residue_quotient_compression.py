#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

WIDTH = 113
WAVES = ("CUT193", "CUT194", "CUT195", "CUT196", "CUT197", "CUT198")
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
FIXED_LABELS = [label for label in ASSIGNMENT_ORDER if label != 49]
GROUPS = [[101, 102, 103], [97, 98, 99], [93, 94, 95, 96]]
A_MODULI = range(2, 6)
B_MODULI = range(2, 6)
BC_MODULI = range(2, 9)
BLOCK_MODULI = range(2, 65)
EXPECTED = {
    "n402_audit_blob": "0c60cda38370333b4b1fb4393132809644d52edf",
    "n402_audit_canonical": "fd37543ebe9e0f68205cfa92bba3d5816e823d4e0a60a1827bd83c411bcfd63e",
    "n402_result_blob": "bb2ebe0db7c36f98441db1b1c199756400418b00",
    "n402_result_canonical": "74acccda2597f493167be9ca222d59eb926c6aa7dc59b8b67520b957d3b385a2",
    "n391_result_blob": "3e72cea011e5a519173a710c20d88bc781c4cee8",
    "n391_result_canonical": "2b30f97aca0873568c324cf9a88ba6dc8ee0e3cceb29e1fc60e9e2c978b02da3",
    "indexer_blob": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
}


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


def classify(entries: list[dict], ma: int, mb: int, md: int, mblock: int) -> dict:
    groups: dict[tuple[int, ...], set[int]] = defaultdict(set)
    for row in entries:
        key = (
            row["a"] % ma,
            row["b"] % mb,
            row["b_minus_c"] % md,
            row["block"] % mblock,
        )
        groups[key].add(row["required_x49_parity"])
    conflicts = sum(1 for values in groups.values() if len(values) > 1)
    return {
        "a_modulus": ma,
        "b_modulus": mb,
        "b_minus_c_modulus": md,
        "block_modulus": mblock,
        "class_count": len(groups),
        "conflicting_class_count": conflicts,
        "determines_required_parity": conflicts == 0,
    }


def main() -> None:
    repo = Path(__file__).resolve().parents[5]
    node_root = repo / "stages/stage32/32-01-178/nodes"
    residual = repo / "stages/stage32/residual-32-01-production"

    audit402 = checked(node_root / "N402/AUDIT-PASS.json", EXPECTED["n402_audit_blob"], EXPECTED["n402_audit_canonical"])
    result402 = checked(node_root / "N402/RESULT.json", EXPECTED["n402_result_blob"], EXPECTED["n402_result_canonical"])
    n391 = checked(node_root / "N391/RESULT.json", EXPECTED["n391_result_blob"], EXPECTED["n391_result_canonical"])
    req(audit402["status"] == "HOSTILE_AUDIT_PASS_RETAINED", "N402 audit receipt status drift")
    req(audit402["hostile_audit"]["verdict"] == "PASS", "N402 audit verdict drift")
    req(result402["bounded_result"]["best_intrinsic_congruence_model"]["class_count"] == 64, "N402 class count drift")
    req(result402["bounded_result"]["best_intrinsic_congruence_model"]["modulus"] == 42, "N402 block modulus drift")

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
            "mass": sum(by[label] for label in FIXED_LABELS),
            "a": sums[0],
            "b": sums[1],
            "c": sums[2],
            "b_minus_c": sums[1] - sums[2],
            "required_x49_parity": required,
        })

    req(dict(sorted(parity_counts.items())) == {0: 27, 1: 70}, "required parity distribution drift")
    req(survivor_total == 5459, "N399 survivor reconstruction drift")
    req((min(x["a"] for x in entries), max(x["a"] for x in entries)) == (0, 3), "a range drift")
    req((min(x["b"] for x in entries), max(x["b"] for x in entries)) == (1, 4), "b range drift")
    req((min(x["b_minus_c"] for x in entries), max(x["b_minus_c"] for x in entries)) == (-3, 4), "b-c range drift")

    models = []
    for ma in A_MODULI:
        for mb in B_MODULI:
            for md in BC_MODULI:
                for mblock in BLOCK_MODULI:
                    models.append(classify(entries, ma, mb, md, mblock))
    deterministic = [x for x in models if x["determines_required_parity"]]
    deterministic.sort(key=lambda x: (x["class_count"], x["block_modulus"], x["a_modulus"], x["b_modulus"], x["b_minus_c_modulus"]))
    req(deterministic, "no deterministic modular quotient model")
    best = deterministic[0]
    best_count = best["class_count"]
    best_ties = [x for x in deterministic if x["class_count"] == best_count]
    min_block = min(x["block_modulus"] for x in deterministic)
    min_block_models = [x for x in deterministic if x["block_modulus"] == min_block]
    min_block_models.sort(key=lambda x: (x["class_count"], x["a_modulus"], x["b_modulus"], x["b_minus_c_modulus"]))

    payload = {
        "semantics": "EXACT_BOUNDED_N402_MODULAR_RESIDUE_QUOTIENT_COMPRESSION_ON_RETAINED_97_BLOCK_POPULATION_ONLY",
        "source_block_count": 97,
        "source_terminal_count": 10961,
        "survivor_terminal_count": survivor_total,
        "required_parity_block_distribution": {"even": parity_counts[0], "odd": parity_counts[1]},
        "n402_class_count": 64,
        "search_ranges": {
            "a_modulus": [2, 5],
            "b_modulus": [2, 5],
            "b_minus_c_modulus": [2, 8],
            "block_modulus": [2, 64],
        },
        "tested_model_count": len(models),
        "deterministic_model_count": len(deterministic),
        "best_model": best,
        "best_model_tie_count": len(best_ties),
        "minimum_deterministic_block_modulus": min_block,
        "best_model_at_minimum_block_modulus": min_block_models[0],
        "strictly_improves_n402_class_count": best_count < 64,
        "transport_beyond_retained_97_blocks": False,
        "terminal_reenumeration_of_n399_rank_stream": False,
        "n400_main_handoff_reopened": False,
        "additional_pruning_terminals": 0,
        "main_authority_subtraction_performed": False,
        "main_pruning_credit": False,
        "full178_complete": False,
        "heavy_compute_authorized": False,
        "merge_authorized": False,
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)

    req(len(models) == 7056, f"model count regression: {len(models)}")
    req(len(deterministic) == 1873, f"deterministic count regression: {len(deterministic)}")
    req(best == {"a_modulus": 3, "b_modulus": 2, "b_minus_c_modulus": 2, "block_modulus": 42, "class_count": 56, "conflicting_class_count": 0, "determines_required_parity": True}, f"best model regression: {best}")
    req(len(best_ties) == 1, f"best tie count regression: {len(best_ties)}")
    req(min_block == 15, f"minimum deterministic block modulus regression: {min_block}")
    req(min_block_models[0]["class_count"] == 84, f"minimum-block best class count regression: {min_block_models[0]}")

    print("PASS_N403_N402_MODULAR_RESIDUE_QUOTIENT_COMPRESSION_PROBE")
    print(f"models={len(models)} deterministic={len(deterministic)}")
    print("best=" + json.dumps(best, sort_keys=True, separators=(",", ":")))
    print("N403_PROBE_JSON=" + json.dumps(payload, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
