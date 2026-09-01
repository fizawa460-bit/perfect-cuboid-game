#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

import diagnose_stage32_post1473_x8_satake_boundary_marking as marking
import diagnose_stage32_post1473_x8_v4_cusp_quotient as quotient_replay

MARKING_EXPECTED = "69a2a6d3cdf7b0d5c6162424a8102ec41cd09ac7e303469d30577d454363e31d"
INCIDENCE_EXPECTED = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"
CZERO_EXPECTED = "96e9d9b78201e99d98b31b8ece51c3e6227a2637c35356f012d0049d589a0f42"
QUOTIENT_EXPECTED = "2869208e7509d7b79378264ea1982299b0f1745b1a54c5856cfbba0754567ce5"

PER_BLOCK = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
BLOCK_START = {"Z1": 33, "Z2": 37, "Z3": 41}
RATIO_BY_BLOCK_BRANCH = {
    "Z1": {1: "+1", -1: "-1"},
    "Z2": {1: "+i", -1: "-i"},
    "Z3": {1: "0", -1: "infinity"},
}
# Exact cusp-ratio source facts for r=t10(2z)/t00(2z):
# r(infinity)=0 from q-expansion; S gives r(0)=+1;
# z->z+1 multiplies r by i and z->z+2 by -1.
# Hence representatives 0,2,1,3,infinity,1/2 give +1,-1,+i,-i,0,infinity.
RATIO_REPRESENTATIVE = {
    "+1": (0, 1),
    "-1": (2, 1),
    "+i": (1, 1),
    "-i": (3, 1),
    "0": (1, 0),
    "infinity": (1, 2),
}


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    data = json.loads(path.read_text())
    claimed = data.get("canonical_sha256_without_this_field")
    body = dict(data)
    body.pop("canonical_sha256_without_this_field", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise ValueError(f"canonical source moved for {path}: claimed={claimed} actual={actual}")
    return data


def build_abstract_cusp_orbits():
    cusps = quotient_replay.all_x8_cusps()
    pu = quotient_replay.permutation(quotient_replay.V4_MATRICES["u"], cusps)
    pv = quotient_replay.permutation(quotient_replay.V4_MATRICES["v"], cusps)
    puv = quotient_replay.permutation(quotient_replay.V4_MATRICES["uv"], cusps)
    pt = quotient_replay.permutation(quotient_replay.T4, cusps)
    v4 = quotient_replay.closure([pu, pv], len(cusps))
    full = quotient_replay.closure([pu, pv, pt], len(cusps))
    seen = set()
    orbits = []
    for i in range(len(cusps)):
        if i in seen:
            continue
        o = quotient_replay.orbit(v4, i)
        orbits.append(o)
        seen.update(o)
    if len(orbits) != 6:
        raise ValueError("abstract V4 cusp orbit count moved")
    orbit_id = {cusps[i]: j + 1 for j, o in enumerate(orbits) for i in o}

    ratio_to_orbit = {}
    for ratio, rep in RATIO_REPRESENTATIVE.items():
        rep = quotient_replay.cusp_canon(rep)
        ratio_to_orbit[ratio] = orbit_id[rep]
    if len(set(ratio_to_orbit.values())) != 6:
        raise ValueError(f"theta-ratio values failed to separate six quotient cusps: {ratio_to_orbit}")

    ident = tuple(range(len(cusps)))
    vlabels = {ident: "1", pu: "u", pv: "v", puv: "uv"}
    outside = [g for g in full if g not in v4]
    outside_labels = {}
    for x in outside:
        names = ["T4*" + name for vv, name in vlabels.items() if quotient_replay.compose(pt, vv) == x]
        if len(names) != 1:
            raise ValueError("outside coset naming regression")
        outside_labels[x] = names[0]

    inertia_by_orbit = {}
    for j, o in enumerate(orbits, start=1):
        stabilizers = []
        for x in outside:
            if any(x[i] == i for i in o):
                stabilizers.append(outside_labels[x])
        if len(stabilizers) != 1:
            raise ValueError(f"quotient cusp inertia regression at orbit {j}: {stabilizers}")
        inertia_by_orbit[j] = stabilizers[0]

    expected_inertia_pairs = {
        "Z1": ({1, 6}, "T4*u"),
        "Z2": ({3, 5}, "T4*uv"),
        "Z3": ({2, 4}, "T4*1"),
    }
    for block, (ids, inertia) in expected_inertia_pairs.items():
        if {ratio_to_orbit[r] for r in RATIO_BY_BLOCK_BRANCH[block].values()} != ids:
            raise ValueError(f"{block} quotient cusp pair moved")
        if {inertia_by_orbit[i] for i in ids} != {inertia}:
            raise ValueError(f"{block} inertia pairing moved")
    return cusps, orbits, ratio_to_orbit, inertia_by_orbit


def build_label_mapping(ratio_to_orbit: dict[str, int]):
    result = {}
    for block in ("Z1", "Z2", "Z3"):
        start = BLOCK_START[block]
        for factor in ("z", "w"):
            for branch in (1, -1):
                signs = marking.matching_signs(block, factor, branch)
                offset = PER_BLOCK.index(signs)
                label = start + offset
                ratio = RATIO_BY_BLOCK_BRANCH[block][branch]
                if label in result:
                    raise ValueError(f"duplicate retained boundary label {label}")
                result[label] = {
                    "factor": "first/z" if factor == "z" else "second/w",
                    "block": block,
                    "theta_ratio": ratio,
                    "weierstrass_cusp_id": ratio_to_orbit[ratio],
                    "magma_signs": list(signs),
                }
    if sorted(result) != list(range(33, 45)):
        raise ValueError("retained C2 label coverage regression")
    expected = {
        34: 6, 35: 1, 38: 3, 39: 5, 42: 4, 43: 2,
        33: 6, 36: 1, 37: 5, 40: 3, 41: 4, 44: 2,
    }
    if {k: v["weierstrass_cusp_id"] for k, v in result.items()} != expected:
        raise ValueError("retained boundary-label to Weierstrass-cusp adapter moved")
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--incidence", type=Path, required=True)
    ap.add_argument("--czero", type=Path, required=True)
    ap.add_argument("--quotient", type=Path, required=True)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    load_canonical(args.marking, MARKING_EXPECTED)
    incidence = load_canonical(args.incidence, INCIDENCE_EXPECTED)
    czero = load_canonical(args.czero, CZERO_EXPECTED)
    quotient_cert = load_canonical(args.quotient, QUOTIENT_EXPECTED)
    if quotient_cert["quotient_geometry"]["genus_C0"] != 2 or not quotient_cert["quotient_geometry"]["six_quotient_cusps_are_Weierstrass_points"]:
        raise ValueError("quotient geometry source moved")

    _, orbits, ratio_to_orbit, inertia_by_orbit = build_abstract_cusp_orbits()
    labels = build_label_mapping(ratio_to_orbit)

    zero_pairs = set(czero["structure"]["c_zero_pairs"])
    nonzero_pairs = set(czero["structure"]["c_nonzero_pairs"])
    all_pair_counts = incidence["boundary_pair_counts"]
    if set(all_pair_counts) != zero_pairs | nonzero_pairs or zero_pairs & nonzero_pairs:
        raise ValueError("c-zero/nonzero pair partition ceased to cover exact incidence pairs")

    node_pair_rows = []
    cusp_pair_counts = Counter()
    for key, count in sorted(all_pair_counts.items()):
        a, b = (int(x) for x in key.split(":"))
        ai = labels[a]["weierstrass_cusp_id"]
        bi = labels[b]["weierstrass_cusp_id"]
        if labels[a]["block"] != labels[b]["block"]:
            raise ValueError(f"node pair crossed X(2) cusp blocks: {key}")
        row = {
            "boundary_pair": key,
            "node_count": count,
            "block": labels[a]["block"],
            "first_weierstrass_cusp_id": ai,
            "second_weierstrass_cusp_id": bi,
            "c_zero": key in zero_pairs,
        }
        node_pair_rows.append(row)
        cusp_pair_counts[(ai, bi)] += int(count)

    if len(node_pair_rows) != 12 or any(r["node_count"] != 4 for r in node_pair_rows):
        raise ValueError("marked node pair structure regression")

    blocks = {
        "Z1": {"weierstrass_cusp_ids": [1, 6], "inertia": "T4*u"},
        "Z2": {"weierstrass_cusp_ids": [3, 5], "inertia": "T4*uv"},
        "Z3": {"weierstrass_cusp_ids": [2, 4], "inertia": "T4*1"},
    }
    for block, info in blocks.items():
        ids = set(info["weierstrass_cusp_ids"])
        if {inertia_by_orbit[i] for i in ids} != {info["inertia"]}:
            raise ValueError(f"{block} inertia certificate regression")

    result = {
        "schema": "STAGE32_POST1473_BOUNDARY_LABEL_WEIERSTRASS_ADAPTER_REPLAY_V1",
        "stage": 32,
        "status": "PASS",
        "source_locks": {
            "satake_marking_canonical_sha256": MARKING_EXPECTED,
            "exceptional_incidence_canonical_sha256": INCIDENCE_EXPECTED,
            "c_zero_partition_canonical_sha256": CZERO_EXPECTED,
            "v4_cusp_quotient_canonical_sha256": QUOTIENT_EXPECTED,
        },
        "theta_ratio_source": {
            "ratio": "theta10(2z)/theta00(2z)",
            "values": ratio_to_orbit,
            "derivation": "q-expansion at infinity plus exact theta transformations S, z->z+1, z->z+2; Gamma[4]/Gamma[8] leaves the ratio invariant projectively",
        },
        "boundary_label_to_weierstrass": {str(k): v for k, v in sorted(labels.items())},
        "three_cusp_pairs_by_X2_block": blocks,
        "node_pair_rows": node_pair_rows,
        "cusp_pair_counts": {f"{a}:{b}": n for (a, b), n in sorted(cusp_pair_counts.items())},
        "firewall": "exact label/cusp adapter only; it restricts B/C branch values to one of twelve ordered cusp pairs inside three inertia pairs but does not prove or exclude a global carrier",
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    text = json.dumps(result, sort_keys=True, separators=(",", ":"))
    print(text)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
