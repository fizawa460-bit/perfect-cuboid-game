#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "stages/stage32-ex3/scratch/ex3-04f-physical-c1-h-orbit-prym-linear-trace.json"
REL = ROOT / "stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-x-relative-h-marked-node-action.json"
LOC = ROOT / "stages/stage33/33-12/diagnose_e3_v91c1v_actual_prime_known140_locator.py"
V6 = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
TANG = ROOT / "stages/stage33/33-07/exceptional-p1-tangent-coordinates.json"
GATE = ROOT / "stages/stage32-ex3/scratch/ex3-04d-upstairs-h4-prym-rosati-fourier-gate.json"
QTRACE = ROOT / "stages/stage32/residual-32-01-production/post1518-o210-q602-residue73-trace-spectrum.json"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


art = json.loads(ART.read_text())
rel = json.loads(REL.read_text())
v6 = json.loads(V6.read_text())
tang = json.loads(TANG.read_text())
gate = json.loads(GATE.read_text())
qtrace = json.loads(QTRACE.read_text())

assert art["status"] == "SCRATCH_PROVISIONAL_CONDITIONAL_DIAGNOSTIC_NOT_RETAINED"
assert art["conditional_graph_firewall"]["condition_source_locked"] is False
assert art["conditional_graph_firewall"]["therefore_all_results_below_are_conditional"] is True
assert art["conditional_finite_reduction"]["unconditional_reduction_claimed"] is False
assert art["firewalls"]["O210_excluded"] is False
assert art["firewalls"]["Q602_excluded"] is False
assert art["firewalls"]["stage32_main_credit"] is False
assert art["firewalls"]["claim_dag_sync_triggered_by_this_scratch"] is False
assert art["firewalls"]["merge_authorized"] is False

# Exact source locks.
locks = art["source_locks"]
assert git_blob_sha(REL) == locks["relative_H_marked_action"]["blob_sha1"]
assert git_blob_sha(LOC) == locks["c1_exact_ordering"]["blob_sha1"]
assert git_blob_sha(V6) == locks["v6_witness"]["blob_sha1"]
assert git_blob_sha(TANG) == locks["physical_side_node_incidence"]["blob_sha1"]
assert git_blob_sha(GATE) == locks["upstairs_prym_norm_gate"]["blob_sha1"]
assert git_blob_sha(QTRACE) == locks["q602_trace_spectrum"]["blob_sha1"]
assert rel["canonical_sha256_without_this_field"] == locks["relative_H_marked_action"]["canonical_sha256"]
assert v6["canonical_sha256_without_this_field"] == locks["v6_witness"]["canonical_sha256"]
assert tang["canonical_sha256"] == locks["physical_side_node_incidence"]["canonical_sha256"]
assert qtrace["canonical_sha256_without_this_field"] == locks["q602_trace_spectrum"]["canonical_sha256"]

# Lock the exact first-24 C1 ordering transcription used by Stage33.
loc_text = LOC.read_text()
for marker in [
    'add_known("C1", 1',
    'add_known("C1", 2',
    'add_known("C1", 3',
    'add_known("C1", 4',
    'for e1 in eps:',
    'for e2 in eps:',
    'for e3 in eps:',
]:
    assert marker in loc_text

assert rel["modular_to_stoll"]["u=TTprime"] == "g7*g9"
assert rel["modular_to_stoll"]["v=RT"] == "g7*g8"
assert rel["modular_to_stoll"]["uv=RTprime"] == "g8*g9"

pair = v6["witness"]["all140_pairings"]
assert len(pair) == 140
mult = pair[92:140]
assert len(mult) == 48 and sum(mult) == 266

# Reconstruct side -> six exceptional nodes from the retained tangent certificate.
side_nodes: dict[int, set[int]] = defaultdict(set)
for ex in tang["exceptional_models"]:
    j = int(ex["exceptional_id"].split("_")[1])
    assert 1 <= j <= 48
    for rec in ex["physical_crossing_tangent_coordinates"]:
        side = int(rec["side_index_1based"])
        assert 1 <= side <= 24
        side_nodes[side].add(j)
assert sorted(side_nodes) == list(range(1, 25))
assert all(len(side_nodes[s]) == 6 for s in range(1, 25))

# Replay the 24 physical C1 candidate graph traces.
trace_by_side: dict[int, int] = {}
for side in range(1, 25):
    c_dot_k = pair[side - 1]
    node_mass = sum(mult[j - 1] for j in side_nodes[side])
    d_dot_kx = 2 * c_dot_k + node_mass
    graph_intersection = 4 * d_dot_kx
    trace_by_side[side] = 105 + 81 - graph_intersection
assert [trace_by_side[s] for s in range(1, 25)] == art["physical_c1_linear_traces"]["side_1_to_24"]

# First three C1 blocks have nested sign order e1,e2,e3 with eps=[+1,-1].
signs = []
for e1 in (1, -1):
    for e2 in (1, -1):
        for e3 in (1, -1):
            signs.append((e1, e2, e3))
assert len(signs) == 8

# In each C1 family, record which e-variable multiplies b1,b2,b3.
# Derived directly from the exact Stage33 transcription:
# group1: e1*b3, e2*b2, e3*c with b1+e3*c -> b1:e3,b2:e2,b3:e1
# group2: e1*b1, e2*b3, b2+e3*c -> b1:e1,b2:e3,b3:e2
# group3: e1*b2, e2*b1, b3+e3*c -> b1:e2,b2:e1,b3:e3
b_to_e = {
    1: {"b1": 2, "b2": 1, "b3": 0},
    2: {"b1": 0, "b2": 2, "b3": 1},
    3: {"b1": 1, "b2": 0, "b3": 2},
}

def act(sig: tuple[int, int, int], group: int, which: str) -> tuple[int, int, int]:
    out = list(sig)
    flips = {
        "1": (),
        "u": ("b1", "b3"),
        "v": ("b1", "b2"),
        "uv": ("b2", "b3"),
    }[which]
    for b in flips:
        out[b_to_e[group][b]] *= -1
    return tuple(out)

sign_to_local = {sig: i + 1 for i, sig in enumerate(signs)}
chars = {
    "trivial": [1, 1, 1, 1],
    "chi_u": [1, -1, 1, -1],
    "chi_v": [1, 1, -1, -1],
    "chi_uv": [1, -1, -1, 1],
}
q602_traces = set(qtrace["exact_spectrum"]["trace_values"])
assert qtrace["rational_trace"]["gauge_invariant_by_conjugation"] is True
assert q602_traces == set(range(-68, 69, 8))
forced = gate["elliptic_prym_consequence"]["forced_degrees_by_retained_character"]
degrees = {k: v["degree"] for k, v in forced.items()}
assert degrees == {"chi_u": 9, "chi_v": 137, "chi_uv": 9}


def gaussian_from_norm_and_rational_trace(norm: int, tr: int) -> list[str]:
    assert tr % 2 == 0
    a = tr // 2
    b2 = norm - a * a
    if b2 < 0:
        return []
    b = math.isqrt(b2)
    if b * b != b2:
        return []
    if b == 0:
        return [str(a)]
    def fmt(im: int) -> str:
        sign = "+" if im > 0 else "-"
        return f"{a}{sign}{abs(im)}i"
    return [fmt(b), fmt(-b)]

replayed = []
scalar_triples: list[list[str]] = []
for group in (1, 2, 3):
    offset = 8 * (group - 1)
    unseen = set(signs)
    while unseen:
        origin = min(unseen, key=lambda s: sign_to_local[s])
        orbit_signs = [act(origin, group, h) for h in ("1", "u", "v", "uv")]
        assert len(set(orbit_signs)) == 4
        for s in orbit_signs:
            unseen.discard(s)
        ids = [offset + sign_to_local[s] for s in orbit_signs]
        A = [trace_by_side[i] for i in ids]
        sums = {name: sum(c * a for c, a in zip(row, A)) for name, row in chars.items()}
        assert all(x % 4 == 0 for x in sums.values())
        blocks = {name: x // 4 for name, x in sums.items()}
        qok = blocks["trivial"] in q602_traces
        rec = {
            "side_ids": ids,
            "A": A,
            "block_linear_traces": blocks,
            "q602_trace_compatible": qok,
        }
        if qok:
            scalars = {
                ch: gaussian_from_norm_and_rational_trace(degrees[ch], blocks[ch])
                for ch in ("chi_u", "chi_v", "chi_uv")
            }
            # Norm compatibility is required simultaneously.
            if all(scalars[ch] for ch in scalars):
                rec["conditional_gaussian_scalars"] = scalars
                local = [
                    [u, v, uv]
                    for u in scalars["chi_u"]
                    for v in scalars["chi_v"]
                    for uv in scalars["chi_uv"]
                ]
                rec["conditional_scalar_triple_count"] = len(local)
                scalar_triples.extend(local)
            else:
                rec["q602_trace_compatible"] = False
        replayed.append(rec)

# Deterministic order: by first side id.
replayed.sort(key=lambda r: r["side_ids"][0])
assert replayed == art["H_orbits_order_1_u_v_uv"]
assert sum(1 for r in replayed if r["q602_trace_compatible"]) == 2
assert scalar_triples == art["conditional_finite_reduction"]["conditional_scalar_triples_after_H_orbit_and_linear_trace"]
assert len(scalar_triples) == 4
assert art["conditional_finite_reduction"]["maximal_order_scalar_superset_before_linear_trace"] == 128
assert art["diagnostic_verdict"]["graph_quotient_identification_closed"] is False

print(json.dumps({
    "success": True,
    "physical_H_orbit_count": len(replayed),
    "q602_compatible_physical_H_orbit_count": 2,
    "conditional_scalar_triple_count": len(scalar_triples),
    "conditional_scalar_triples": scalar_triples,
    "graph_quotient_identification_closed": False,
    "O210_excluded": False,
    "Q602_excluded": False,
}, indent=2, sort_keys=True))
