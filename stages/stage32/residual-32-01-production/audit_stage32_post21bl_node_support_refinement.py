#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

EXPECTED_ADAPTER = "ef3f21e4166d4bfcacce3503213b0a72afee5f5002ab7145de01fc9c54d47038"
EXPECTED_CERT = "d1b446dd8fa32db16a3ec4f2eb8a4db06b2cc65b80a0ef7580cec1437b4ff5ad"
EXPECTED_UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"


def csha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path, expected: str):
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    got = csha(raw)
    if claimed != expected or got != expected:
        raise SystemExit(f"canonical regression: {path}: claimed={claimed} got={got}")
    raw["canonical_sha256_without_this_field"] = claimed
    return raw


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--adapter", type=Path, required=True)
    ap.add_argument("--certificate", type=Path, required=True)
    ap.add_argument("--proof", type=Path, required=True)
    ap.add_argument("--upstream-lock", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    adapter = load_canonical(args.adapter, EXPECTED_ADAPTER)
    cert = load_canonical(args.certificate, EXPECTED_CERT)
    proof = args.proof.read_text()
    upstream = args.upstream_lock.read_text()

    if EXPECTED_UPSTREAM_BLOB not in upstream:
        raise SystemExit("upstream blob lock regression")
    for required in ("48 nodes", "exceptional divisors"):
        if required not in upstream:
            raise SystemExit(f"upstream semantic lock missing: {required}")
    for required in ("d <= 16g - 16 + 4n", "positive support = 44", "d <= 4*44 = 176 < 186"):
        if required not in proof:
            raise SystemExit(f"proof text regression: {required}")

    target = adapter["target"]
    if (int(target["genus"]), int(target["degree"])) != (1, 186):
        raise SystemExit("representative target regression")
    if int(adapter["quadratic"]["picard_self_square"]) != 858:
        raise SystemExit("representative self-square regression")

    pairings = [int(v) for v in adapter["all140"]["pairings"]]
    if len(pairings) != 140:
        raise SystemExit("all140 pairing count regression")
    if min(pairings) < 0:
        raise SystemExit("pairing nonnegativity regression")

    # Immutable upstream row order is 92 known nonexceptional curves followed by
    # 48 exceptional divisors. Stage32's adapter uses that exact gensinPicL order.
    exceptional = pairings[92:]
    if len(exceptional) != 48:
        raise SystemExit("exceptional row count regression")
    if sum(exceptional) != int(target["e"]) or sum(exceptional) != 266:
        raise SystemExit("exceptional mass regression")

    support = sum(v > 0 for v in exceptional)
    zeros = [i + 1 for i, v in enumerate(exceptional) if v == 0]
    if support != 44 or zeros != [2, 6, 7, 8]:
        raise SystemExit(f"exceptional support regression: support={support} zeros={zeros}")

    g, d = 1, 186
    # Refined Freitag-Salvati Manni proof:
    # 16(2g-2)k >= 2kd - 8kn  => d <= 16g-16+4n.
    max_degree = 16 * g - 16 + 4 * support
    required_support = ceil_div(d - (16 * g - 16), 4)
    contradiction = d > max_degree
    if (max_degree, required_support, contradiction) != (176, 47, True):
        raise SystemExit("node-support arithmetic regression")

    if cert["target"]["exceptional_pairings"] != exceptional:
        raise SystemExit("certificate exceptional vector regression")
    if cert["target"]["positive_exceptional_support_count"] != support:
        raise SystemExit("certificate support regression")
    if cert["exclusion"]["max_degree_from_available_support"] != max_degree:
        raise SystemExit("certificate max-degree regression")
    if cert["exclusion"]["required_node_support"] != required_support:
        raise SystemExit("certificate required-support regression")

    result = {
        "schema": "STAGE32_POST21BL_NODE_SUPPORT_REFINEMENT_FRESH_AUDIT_V1",
        "status": "PASS_STAGE32_POST21BL_FRESH_NODE_SUPPORT_REFINEMENT_AUDIT",
        "source_locks": {
            "adapter_canonical_sha256": EXPECTED_ADAPTER,
            "refinement_certificate_canonical_sha256": EXPECTED_CERT,
            "upstream_cuboids_magma_blob": EXPECTED_UPSTREAM_BLOB,
        },
        "independent_replay": {
            "all140_count": len(pairings),
            "exceptional_rows_1based": [93, 140],
            "exceptional_count": len(exceptional),
            "exceptional_mass": sum(exceptional),
            "positive_exceptional_support": support,
            "zero_exceptional_support": len(zeros),
            "zero_exceptional_indices_1based": zeros,
            "refined_bound": "d <= 16g-16+4n",
            "g": g,
            "d": d,
            "required_node_support": required_support,
            "available_node_support_upper": support,
            "max_degree_at_available_support": max_degree,
            "degree_excess": d - max_degree,
            "contradiction": contradiction,
        },
        "verdict": {
            "bijective_normalization_genus1_curve_in_representative_class": False,
            "representative_only": True,
            "multibranch_at_node_closed": False,
            "full178_closed": False,
            "r29_lg2_eff_full_receiver_closed": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": result["status"],
        "support": support,
        "required_support": required_support,
        "max_degree": max_degree,
        "actual_degree": d,
        "degree_excess": d-max_degree,
        "canonical": result["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
