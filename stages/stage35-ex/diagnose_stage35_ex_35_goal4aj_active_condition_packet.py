#!/usr/bin/env python3
"""Goal4AJ diagnostic: compact active divisor-condition packet after Q-hyperplane peel.

Freeze the exact numerator degree-31 and denominator residual degree-19 retained140
multiplicity vectors from the passing Q-defined hyperplane-factor peel.  Split them
into strict-curve (1..92) and A1-exceptional (93..140) conditions, and compress the
strict conditions into exact V4 Galois orbits.  This is the bounded input packet for
the later quotient-ring section intersection; it does not solve any section.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PERMS = ROOT / "stages/stage33/33-07/galois-known-class-permutations.json"

DIVISOR_PACKET_SHA256 = "c3c03a7be1d09ac61c29afb855febc0424c2f8818ba428efcc920861dc75a009"
DIVISOR_PACKET_RUN = 34086027177
DIVISOR_PACKET_JOB = 101630197014
QPEEL_CANONICAL_SHA256 = "c74c8f976ea4c26ebd9a614c2c6314f5bcb9dcccc46861461634657c8fd460ba"
QPEEL_RUN = 34092066114
QPEEL_JOB = 101647794285
STRICT_PREFLIGHT_CANONICAL_SHA256 = "43aa7374e83c5f245997e0b7cbdb67b27d1bc045d7606b9544b6cbc7b2e31f69"
GALOIS_PERMS_SHA256 = "e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30"

# Exact post-peel vectors copied from GOAL4AJ_Q_HYPERPLANE_FACTOR_PEEL_JSON.
NUM = {2:21,3:1,4:1,5:1,6:1,7:21,9:3,10:10,12:10,13:18,14:4,15:12,16:1,17:3,18:12,19:12,22:12,23:10,24:1,27:1,30:1,38:13,40:13,58:9,60:9,65:1,67:1,93:26,94:3,95:2,96:21,97:2,98:21,99:26,100:3,101:22,102:2,103:3,104:23,105:15,106:37,107:36,108:14,109:20,110:17,111:13,112:22,113:27,114:12,115:12,116:21,117:1,118:11,119:11,120:1,121:11,122:1,123:1,124:11,125:18,126:13,127:13,128:18,129:13,130:12,131:12,132:13,133:6,134:8,135:8,136:6,137:6,138:6,139:6,140:6}
DEN = {1:3,8:3,9:3,11:2,16:1,17:3,21:2,24:1,25:7,26:9,28:1,29:1,31:9,32:7,33:2,35:2,37:13,39:13,58:9,60:9,65:1,67:1,94:2,95:4,97:4,100:2,101:13,102:16,103:18,104:13,105:4,106:1,107:1,108:2,109:13,110:4,111:4,112:11,113:12,114:1,115:1,116:10,117:9,118:3,119:3,120:9,121:3,122:9,123:9,124:3,125:10,126:13,127:13,128:10,129:12,130:11,131:11,132:12,133:4,134:6,135:6,136:4,137:5,138:5,139:5,140:5}

p = json.loads(PERMS.read_text(encoding="utf-8"))
assert p["canonical_sha256"] == GALOIS_PERMS_SHA256
cc = [int(x) for x in p["cc_permutation_1based"]]
ct = [int(x) for x in p["ct_permutation_1based"]]
assert len(cc) == len(ct) == 140


def dense(d: dict[int, int]) -> list[int]:
    return [int(d.get(i, 0)) for i in range(1, 141)]


def permute(v: list[int], perm: list[int]) -> list[int]:
    out = [0] * 140
    for j, m in enumerate(v):
        out[perm[j] - 1] += m
    return out


def family(i: int) -> str:
    if 1 <= i <= 32:
        return "C1"
    if 33 <= i <= 44:
        return "C2"
    if 45 <= i <= 92:
        return "C3"
    if 93 <= i <= 140:
        return "A1_EXCEPTIONAL"
    raise ValueError(i)


def orbit_packet(d: dict[int, int]) -> list[dict]:
    active = {i for i in d if i <= 92 and d[i] > 0}
    unseen = set(active)
    rows = []
    while unseen:
        seed = min(unseen)
        orb = {seed}
        todo = [seed]
        while todo:
            j = todo.pop()
            for perm in (cc, ct):
                k = perm[j - 1]
                if k > 92:
                    raise SystemExit("strict/exc Galois partition regression")
                if k not in orb:
                    orb.add(k)
                    todo.append(k)
        if not orb <= active:
            raise SystemExit(f"active strict support not Galois closed at seed {seed}")
        mults = {d[i] for i in orb}
        if len(mults) != 1:
            raise SystemExit(f"orbit multiplicity mismatch at seed {seed}: {mults}")
        fams = {family(i) for i in orb}
        if len(fams) != 1:
            raise SystemExit(f"strict family orbit mismatch at seed {seed}: {fams}")
        rows.append({
            "indices_1based": sorted(orb),
            "orbit_size": len(orb),
            "multiplicity": next(iter(mults)),
            "family": next(iter(fams)),
        })
        unseen -= orb
    return rows


def packet(name: str, degree: int, d: dict[int, int]) -> dict:
    v = dense(d)
    if permute(v, cc) != v or permute(v, ct) != v:
        raise SystemExit(f"{name} retained140 vector not V4 invariant")
    strict = {str(i): d[i] for i in sorted(d) if i <= 92}
    exc = {str(i): d[i] for i in sorted(d) if i >= 93}
    orbits = orbit_packet(d)
    fam_counts = Counter(r["family"] for r in orbits)
    fam_max = {}
    for fam in ("C1", "C2", "C3"):
        vals = [d[i] for i in d if i <= 92 and family(i) == fam]
        fam_max[fam] = max(vals) if vals else 0
    return {
        "homogeneous_degree_after_q_peel": degree,
        "retained_support_count": len(d),
        "strict_support_count": len(strict),
        "exceptional_support_count": len(exc),
        "strict_total_multiplicity": sum(strict.values()),
        "exceptional_total_multiplicity": sum(exc.values()),
        "strict_max_multiplicity": max(strict.values()) if strict else 0,
        "exceptional_max_multiplicity": max(exc.values()) if exc else 0,
        "strict_family_max_multiplicity": fam_max,
        "strict_orbit_count": len(orbits),
        "strict_orbit_family_counts": dict(sorted(fam_counts.items())),
        "strict_orbits": orbits,
        "strict_multiplicities_1based": strict,
        "exceptional_multiplicities_1based": exc,
        "v4_invariant_exact": True,
    }

num = packet("numerator", 31, NUM)
den = packet("denominator_residual", 19, DEN)
assert num["retained_support_count"] == 75
assert den["retained_support_count"] == 66
assert num["strict_max_multiplicity"] == 21
assert den["strict_max_multiplicity"] == 13

out = {
    "schema": "STAGE35_EX_GOAL4AJ_ACTIVE_DIVISOR_CONDITION_PACKET_DIAGNOSTIC_V1",
    "source_locks": {
        "degree31_divisor_packet_sha256": DIVISOR_PACKET_SHA256,
        "degree31_divisor_packet_run": DIVISOR_PACKET_RUN,
        "degree31_divisor_packet_job": DIVISOR_PACKET_JOB,
        "q_hyperplane_factor_peel_canonical_sha256": QPEEL_CANONICAL_SHA256,
        "q_hyperplane_factor_peel_run": QPEEL_RUN,
        "q_hyperplane_factor_peel_job": QPEEL_JOB,
        "strict_symbolic_power_preflight_canonical_sha256": STRICT_PREFLIGHT_CANONICAL_SHA256,
        "galois_known_class_permutations_sha256": GALOIS_PERMS_SHA256,
    },
    "numerator": num,
    "denominator_residual": den,
    "full_active_condition_packet_compacted": True,
    "all_strict_conditions_grouped_into_v4_orbits": True,
    "all_exceptional_conditions_retained_individually": True,
    "global_section_intersection_solved": False,
    "literal_numerator_coefficients_materialized": False,
    "literal_denominator_coefficients_materialized": False,
    "literal_F_B_materialized": False,
    "local_evaluations_computed": False,
    "brauer_manin_obstruction_obtained": False,
    "E1_proved": False,
    "stage35_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = hashlib.sha256(json.dumps(out, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
print("GOAL4AJ_ACTIVE_CONDITION_PACKET_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
print("GOAL4AJ_ACTIVE_CONDITION_PACKET=PASS")
