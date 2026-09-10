#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
N260_STATE = HERE.parent / "N260/STATE.json"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"
sys.path.insert(0, str(RESIDUAL))

from aut_equivariant_pairing_adapter import EquivariantPrefixMembershipOracle
from hperp_integral_adapter import HperpIntegralPairingAdapter

EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING_CANONICAL = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
EXPECTED_STRATA = {
    ("g0-d174", 48): 3067,
    ("g0-d176", 48): 3105,
    ("g1-d190", 48): 3371,
    ("g1-d192", 48): 3409,
}
ALL48_EXCEPTIONAL_LABELS = list(range(93, 141))
X4_NORMAL_LABEL = 49


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import retained payload: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    payload = mod.load()
    if not isinstance(payload, dict):
        raise ValueError(f"retained payload is not dict: {path}")
    return payload


def count_residues_upto(limit_exclusive: int, modulus: int, residues: list[int]) -> int:
    if limit_exclusive <= 0:
        return 0
    q, r = divmod(limit_exclusive, modulus)
    return q * len(residues) + sum(1 for x in residues if x < r)


def main() -> None:
    n260 = json.loads(N260_STATE.read_text())
    if n260.get("node_id") != "N260":
        raise ValueError("N260 authority regression")
    if n260["proof"].get("full_exceptional_vector") != "[1]^48":
        raise ValueError("N260 [1]^48 authority missing")
    if n260["retained_result"].get("full_48_exceptional_vector_forced_all_ones") is not True:
        raise ValueError("N260 full exceptional rigidity missing")
    observed_strata = {
        (str(row["row_id"]), int(row["e"])): int(row["normal_x4_block"])
        for row in n260["retained_result"]["one_block_strata"]
    }
    if observed_strata != EXPECTED_STRATA:
        raise ValueError(f"N260 stratum/range regression: {observed_strata}")

    bundle = load_retained(RETAINED, "s32_n270_picard_bundle")
    marking = load_retained(MARKING, "s32_n270_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained Picard bundle canonical regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained Stage32 marking canonical regression")

    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    labels = ALL48_EXCEPTIONAL_LABELS + [X4_NORMAL_LABEL]
    oracle = EquivariantPrefixMembershipOracle(adapter, labels)
    cert = oracle.certificate()
    checks = cert.get("checks")
    if not isinstance(checks, list) or len(checks) != len(labels):
        raise ValueError("all140 HNF certificate depth regression")
    final = checks[-1]
    modulus = int(final["modulus"])
    if modulus <= 0:
        raise ValueError("invalid final HNF modulus")

    exceptional_only_feasible = oracle.feasible([1] * 48)
    if not exceptional_only_feasible:
        residue_values: list[int] = []
    else:
        residue_values = [
            x4 for x4 in range(modulus)
            if oracle.feasible([1] * 48 + [x4])
        ]

    rows = []
    total_terminals = 0
    total_hnf_rejected = 0
    total_hnf_survivors = 0
    for (row_id, e), block in sorted(EXPECTED_STRATA.items()):
        feasible = count_residues_upto(block, modulus, residue_values)
        rejected = block - feasible
        rows.append({
            "row_id": row_id,
            "e": e,
            "x4_range": [0, block - 1],
            "terminal_count": block,
            "hnf_feasible_x4_count": feasible,
            "hnf_rejected_x4_count": rejected,
            "all_x4_hnf_rejected": feasible == 0,
        })
        total_terminals += block
        total_hnf_rejected += rejected
        total_hnf_survivors += feasible

    body = {
        "schema": "STAGE32_32_01_178_N270_ALL48_EXCEPTIONAL_HNF_OBSTRUCTION_V1",
        "source_scope": "N260 four e=K=48 strata only",
        "pairing_assignment": {
            "fixed_exceptional_labels_1based": ALL48_EXCEPTIONAL_LABELS,
            "fixed_exceptional_values": [1] * 48,
            "symbolic_normal_label_1based": X4_NORMAL_LABEL,
            "remaining_91_normal_pairings_unassigned": True,
        },
        "oracle": {
            "mode": cert.get("mode"),
            "label_order_1based": labels,
            "depth": len(labels),
            "exceptional_only_depth48_feasible": exceptional_only_feasible,
            "final_modulus": modulus,
            "final_active_congruence_rows": int(final["active_congruence_rows"]),
            "final_quotient_index": str(final["quotient_index"]),
            "final_hnf_sha256": str(final["hnf_sha256"]),
            "feasible_x4_residues_mod_final_modulus": residue_values,
        },
        "strata": rows,
        "aggregate": {
            "terminal_count": total_terminals,
            "hnf_rejected_terminal_count": total_hnf_rejected,
            "hnf_survivor_terminal_count": total_hnf_survivors,
            "all_four_strata_hnf_empty": total_hnf_survivors == 0,
        },
        "semantics": {
            "exact_necessary_integral_picard_pairing_image_test": True,
            "hnf_rejection_is_safe_no_integral_picard64_completion": True,
            "hnf_feasible_is_not_picard_sat": True,
            "does_not_run_z3": True,
            "does_not_duplicate_ex5_adaptive_exceptional_partition": True,
            "n260_hostile_audit_still_required_before_consuming_four_stratum_rigidity_credit": True,
            "full178_complete": False,
            "heavy_compute": False,
            "theorem_credit": False,
        },
    }
    out = {**body, "canonical_sha256_without_this_field": csha(body)}
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
