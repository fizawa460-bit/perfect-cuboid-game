#!/usr/bin/env python3
"""Retain and verify function-level Galois scalars for the 14 Stage33-11 generators.

The audited Stage33-11 certificate compares prime divisors, so it deliberately
forgets multiplicative constants of the boundary residue functions.  Those
constants belong to the constant-character side of the Stage33-12 problem.
This verifier restores exactly that finite interface without claiming a global
Gersten/Brauer representative or a Hochschild--Serre value.

Use ``--refresh-source SIDE.json EXCEPTIONAL.json`` only to rebuild the compact
source lock from the two immutable SHA-locked #1430 artifacts.  The ordinary
argumentless invocation is network-free and verifies the committed lock.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
SOURCE = HERE / "boundary-function-generator-source-lock.json"
OUT = HERE / "boundary-function-scalar-descent-certificate.json"
E_SOURCE = STAGE33 / "33-11e" / "stage33-11e-source-lock.json"
F_CERT = STAGE33 / "33-11f" / "stage33-11f-26-column-exact-closure-certificate.json"

GENERATOR_IDS = [
    "A2_02", "A2_03", "A2_24", "A2_25", "A2_26", "A2_04", "A2_01",
    "A2_07", "A2_05", "A2_10", "A2_08", "A2_09", "A2_16", "A2_15",
]
ARTIFACTS = {
    "side": {
        "id": 9640210685,
        "zip_sha256": "057c63d1f823d7a9bd1f23676f36f32606dfc8cf85a865ebdeeb67dd4953795e",
        "json_file_sha256": "3e4498364f89b7f8934aef913d2721d25a209db296c49ed809069c3fda1d93a7",
        "canonical_sha256": "2f137842fffbabe7fa9f91879f379e0662803204d6753c342fc31f6dfe12fa6d",
    },
    "exceptional": {
        "id": 9640318609,
        "zip_sha256": "3cb9271b729b37b975b9fbd5117d1e74335be816296a5461a3a13ddf589a52dd",
        "json_file_sha256": "54342171a2986588f108169291db86fbfecfcec15f45a3d6c86d2159204cefb5",
        "canonical_sha256": "a9d5ceb66625dfa561db61a3afc95388bf5a8371fb81905988991514a765d397",
    },
}
E_SOURCE_SHA = "a1bce01bb7041d9cc48bfb7ce6e6f6095afc36ef8bc08fcb1588a885ed61e2e2"
F_CERT_SHA = "c7ba9a5a4a9475830e62276292abcdb89deb729a6aecab2c0b6f48a71a65f6e4"


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_canonical(path: Path, expected: str | None = None) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    if claimed != csha(body) or (expected is not None and claimed != expected):
        raise SystemExit(f"canonical lock mismatch: {path}")
    return obj


def q(z: list[int] | tuple[int, int, int, int]) -> tuple[Fraction, Fraction]:
    return Fraction(z[0], z[1]), Fraction(z[2], z[3])


ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))


def qmul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def qinv(x):
    den = x[0] * x[0] + x[1] * x[1]
    if den == 0:
        raise SystemExit("zero Gaussian rational pivot")
    return x[0] / den, -x[1] / den


def qpow(x, n: int):
    if n < 0:
        return qpow(qinv(x), -n)
    out = ONE
    base = x
    while n:
        if n & 1:
            out = qmul(out, base)
        base = qmul(base, base)
        n >>= 1
    return out


def qcc(x):
    return x[0], -x[1]


def qenc(x) -> list[int]:
    return [x[0].numerator, x[0].denominator, x[1].numerator, x[1].denominator]


def normalize_signature(raw: list[list[int]]):
    values = [q(z) for z in raw]
    pivot = next((x for x in values if x != ZERO), None)
    if pivot is None:
        raise SystemExit("zero linear form")
    inv = qinv(pivot)
    normalized = [qenc(qmul(x, inv)) for x in values]
    return normalized, pivot


def compact_package(package: dict, kind: str) -> dict:
    if kind == "SIDE":
        numerator_key = "ambient_linear_factor_coefficients_L_basis"
        denominator = package["D_coefficients_L_basis"]
    else:
        numerator_key = "ambient_tangent_linear_factor_coefficients_L_basis"
        denominator = package["ambient_projection_R0_R1_coefficients_L_basis"][1]
    return {
        "component_id": package["component_id"],
        "kind": kind,
        "numerator_factors": [
            {
                "coefficients_Qi": factor[numerator_key],
                "exponent": int(factor["exponent"]),
            }
            for factor in package["numerator_factors"]
        ],
        "denominator": {
            "coefficients_Qi": denominator,
            "exponent": int(package["denominator"]["exponent"]),
        },
    }


def refresh_source(side_path: Path, exceptional_path: Path) -> None:
    if file_sha(side_path) != ARTIFACTS["side"]["json_file_sha256"]:
        raise SystemExit("side artifact JSON SHA mismatch")
    if file_sha(exceptional_path) != ARTIFACTS["exceptional"]["json_file_sha256"]:
        raise SystemExit("exceptional artifact JSON SHA mismatch")
    side = load_canonical(side_path, ARTIFACTS["side"]["canonical_sha256"])
    exc = load_canonical(exceptional_path, ARTIFACTS["exceptional"]["canonical_sha256"])
    side_by = {r["source_basis_name"]: r for r in side["source_ambient_side_lifts"]}
    exc_by = {r["source_basis_name"]: r for r in exc["source_ambient_exceptional_lifts"]}
    if set(side_by) != {f"A2_{i:02d}" for i in range(1, 27)} or set(exc_by) != set(side_by):
        raise SystemExit("artifact source basis regression")
    records = []
    for source_id in GENERATOR_IDS:
        srow, erow = side_by[source_id], exc_by[source_id]
        if srow["raw_order"] != erow["raw_order"]:
            raise SystemExit(f"raw order mismatch: {source_id}")
        packages = [
            compact_package(p, "SIDE") for p in srow["side_ambient_function_lifts"]
        ] + [
            compact_package(p, "EXCEPTIONAL")
            for p in erow["exceptional_ambient_tangent_function_lifts"]
        ]
        records.append({
            "source_direction": source_id,
            "raw_order": int(srow["raw_order"]),
            "component_packages": sorted(packages, key=lambda p: p["component_id"]),
        })
    lock = {
        "schema": "STAGE33_12_BOUNDARY_FUNCTION_GENERATOR_SOURCE_LOCK_V1",
        "source_artifacts": ARTIFACTS,
        "stage33_11_working_generators": GENERATOR_IDS,
        "generator_records": records,
    }
    lock["canonical_sha256"] = csha(lock)
    SOURCE.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def package_data(package: dict):
    vector: dict[str, int] = {}
    scalar = ONE
    for factor in package["numerator_factors"]:
        normalized, pivot = normalize_signature(factor["coefficients_Qi"])
        carrier = csha(normalized)
        exponent = int(factor["exponent"])
        vector[carrier] = vector.get(carrier, 0) + exponent
        scalar = qmul(scalar, qpow(pivot, exponent))
    denominator = package["denominator"]
    normalized, pivot = normalize_signature(denominator["coefficients_Qi"])
    carrier = csha(normalized)
    exponent = int(denominator["exponent"])
    vector[carrier] = vector.get(carrier, 0) - exponent
    if vector[carrier] == 0:
        del vector[carrier]
    scalar = qmul(scalar, qpow(pivot, -exponent))
    return dict(sorted(vector.items())), scalar


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh-source", nargs=2, metavar=("SIDE_JSON", "EXCEPTIONAL_JSON"))
    args = parser.parse_args()
    if args.refresh_source:
        refresh_source(Path(args.refresh_source[0]), Path(args.refresh_source[1]))

    lock = load_canonical(SOURCE)
    e_source = load_canonical(E_SOURCE, E_SOURCE_SHA)
    f_cert = load_canonical(F_CERT, F_CERT_SHA)
    if lock["stage33_11_working_generators"] != GENERATOR_IDS:
        raise SystemExit("working generator order regression")
    e_records = {r["source_direction"]: r for r in e_source["generator_records"]}
    if set(e_records) != set(GENERATOR_IDS):
        raise SystemExit("Stage33-11e generator set regression")
    if len(f_cert["columns"]) != 26 or any(
        column["unresolved"]
        or (
            column["source_transport"]["kind"] == "CERTIFIED_F2_ORBIT_SPAN"
            and not column["source_transport"]["witness"]["xor_equals_target_exactly"]
        )
        or column["source_transport"]["kind"]
        not in ("CERTIFIED_F2_ORBIT_SPAN", "DIRECT_EXACT_GENERATOR")
        for column in f_cert["columns"]
    ):
        raise SystemExit("Stage33-11f 26-direction orbit-span regression")
    inventory = {
        carrier: signature for carrier, signature in e_source["carrier_inventory"].items()
    }
    by_signature = {
        tuple(tuple(z) for z in signature): carrier for carrier, signature in inventory.items()
    }
    if len(inventory) != 30 or len(by_signature) != 30:
        raise SystemExit("carrier inventory regression")
    carrier_actions = {"cc": {}, "ct": {}}
    for carrier, signature in inventory.items():
        cc_raw = [[z[0], z[1], -z[2], z[3]] for z in signature]
        cc_signature, _ = normalize_signature(cc_raw)
        cc_target = by_signature.get(tuple(tuple(z) for z in cc_signature))
        if cc_target is None:
            raise SystemExit("carrier inventory not cc-stable")
        carrier_actions["cc"][carrier] = cc_target
        carrier_actions["ct"][carrier] = carrier

    output_records = []
    ratio_values = set()
    package_count = 0
    candidate_count = 0
    for row in lock["generator_records"]:
        source_id = row["source_direction"]
        e_record = e_records[source_id]
        packages = {p["component_id"]: p for p in row["component_packages"]}
        if set(packages) != set(e_record["component_signed_carrier_vectors"]):
            raise SystemExit(f"component coverage mismatch: {source_id}")
        pdata = {}
        for component, package in packages.items():
            vector, scalar = package_data(package)
            expected = {
                k: int(v) for k, v in e_record["component_signed_carrier_vectors"][component].items()
            }
            if vector != expected:
                raise SystemExit(f"carrier-vector reconstruction mismatch: {source_id}/{component}")
            pdata[component] = (vector, scalar)
        action_rows = []
        for action in ("cc", "ct"):
            for component in sorted(packages):
                vector, scalar = pdata[component]
                acted_vector = {}
                carrier_action = carrier_actions[action]
                for carrier, exponent in vector.items():
                    target = carrier_action[carrier]
                    acted_vector[target] = acted_vector.get(target, 0) + exponent
                candidates = []
                for target_component in e_record["component_galois_target_candidates"][action][component]:
                    target_vector, target_scalar = pdata[target_component]
                    if acted_vector != target_vector:
                        continue
                    acted_scalar = qcc(scalar) if action == "cc" else scalar
                    ratio = qmul(acted_scalar, qinv(target_scalar))
                    encoded = qenc(ratio)
                    ratio_values.add(tuple(encoded))
                    candidates.append({
                        "target_component": target_component,
                        "function_scalar_ratio": encoded,
                    })
                if not candidates:
                    raise SystemExit(f"no function-level target: {source_id}/{component}/{action}")
                action_rows.append({
                    "action": action,
                    "source_component": component,
                    "candidate_targets": candidates,
                })
                candidate_count += len(candidates)
        output_records.append({
            "source_direction": source_id,
            "raw_order": int(row["raw_order"]),
            "component_count": len(packages),
            "action_scalar_record_count": len(action_rows),
            "candidate_target_count": sum(len(x["candidate_targets"]) for x in action_rows),
            "all_candidate_scalar_ratios_one": all(
                candidate["function_scalar_ratio"] == [1, 1, 0, 1]
                for action_row in action_rows
                for candidate in action_row["candidate_targets"]
            ),
            "action_scalar_records_sha256": csha(action_rows),
        })
        package_count += len(packages)

    cert = {
        "schema": "STAGE33_12_BOUNDARY_FUNCTION_SCALAR_DESCENT_V1",
        "source_locks": {
            "boundary_function_generator_source_lock_sha256": lock["canonical_sha256"],
            "stage33_11e_source_lock_sha256": e_source["canonical_sha256"],
            "stage33_11f_certificate_sha256": f_cert["canonical_sha256"],
            "side_artifact_id": ARTIFACTS["side"]["id"],
            "side_artifact_zip_sha256": ARTIFACTS["side"]["zip_sha256"],
            "exceptional_artifact_id": ARTIFACTS["exceptional"]["id"],
            "exceptional_artifact_zip_sha256": ARTIFACTS["exceptional"]["zip_sha256"],
        },
        "working_generator_count": len(GENERATOR_IDS),
        "working_generator_ids": GENERATOR_IDS,
        "boundary_function_package_count": package_count,
        "cc_ct_action_candidate_count": candidate_count,
        "distinct_scalar_ratios_Qi": [list(x) for x in sorted(ratio_values)],
        "generator_records": output_records,
        "exact_conclusion": {
            "all_14_generator_boundary_function_packages_recovered_with_occurrence_scalars": True,
            "all_package_divisor_vectors_match_audited_stage33_11e": True,
            "cc_ct_function_level_scalar_ratios_finitely_materialized": True,
            "all_cc_ct_function_level_scalar_ratios_equal_one": ratio_values == {(1, 1, 0, 1)},
            "boundary_function_constant_correction_zero_on_all_14_generators": ratio_values == {(1, 1, 0, 1)},
            "stage33_11f_orbit_span_transports_zero_scalar_correction_to_all_26_directions": ratio_values == {(1, 1, 0, 1)},
            "prime_level_zero_forgets_constant_function_scalars": True,
            "finite_and_constant_two_primary_obstruction_blocks_coupled_by_boundary_function_scalars": False,
            "other_global_gersten_or_hs_coupling_ruled_out": False,
        },
        "promotion_firewall": {
            "global_gersten_brauer_representatives_materialized": 0,
            "hoch_schild_serre_d2_values_computed": 0,
            "global_q_residue_lifts_promoted": 0,
            "boundary_function_hilbert90_data_alone_closes_stage33_12": False,
        },
        "next_exact_leaf": "USE_THE_FINITE_QI_SCALAR_TABLE_IN_A_GLOBAL_GERSTEN_2COCHAIN_OR_PROVE_IT_LANDS_IN_THE_CONSTANT_COKERNEL_ADAPTER",
    }
    cert["canonical_sha256"] = csha(cert)
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "working_generators": len(GENERATOR_IDS),
        "boundary_function_packages": package_count,
        "distinct_scalar_ratios": len(ratio_values),
        "hs_d2_values_computed": 0,
        "certificate_sha256": cert["canonical_sha256"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
