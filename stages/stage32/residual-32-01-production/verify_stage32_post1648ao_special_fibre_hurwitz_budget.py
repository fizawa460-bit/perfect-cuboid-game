#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648ao-special-fibre-hurwitz-budget.json"
NOTE = HERE / "post1648ao-special-fibre-hurwitz-budget-source-note.md"
AM = HERE / "post1648am-beauville-fibration-picard-source-lock.json"
AN = HERE / "post1648an-a1-strict-transform-delta-feasibility.json"
V6 = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"


def canonical_sha(payload: dict) -> str:
    body = dict(payload)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    cert = json.loads(CERT.read_text())
    got = canonical_sha(cert)
    if got != cert["canonical_sha256_without_this_field"]:
        raise SystemExit(f"AO canonical mismatch: {got}")

    note_sha = hashlib.sha256(NOTE.read_bytes()).hexdigest()
    if note_sha != cert["source_locks"]["source_note_sha256"]:
        raise SystemExit(f"AO source note moved: {note_sha}")

    am = json.loads(AM.read_text())
    an = json.loads(AN.read_text())
    if am["canonical_sha256_without_this_field"] != cert["parent"]["am_canonical_sha256"]:
        raise SystemExit("AM canonical moved")
    if an["canonical_sha256_without_this_field"] != cert["parent"]["an_canonical_sha256"]:
        raise SystemExit("AN canonical moved")

    v6 = json.loads(V6.read_text())
    if v6["canonical_sha256_without_this_field"] != cert["source_locks"]["v6_witness_canonical_sha256"]:
        raise SystemExit("V6 canonical moved")
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    masses = pairings[92:]
    e = sum(masses)
    support = sum(x > 0 for x in masses)
    if (e, support) != (266, 47):
        raise SystemExit("V6 exceptional data moved")
    if masses != cert["v6_exact_inputs"]["exceptional_pairings"]:
        raise SystemExit("AO exceptional vector mismatch")

    # Exact genus of Z=X(4).  Γ(4) is torsion-free and -I is not in Γ(4).
    N = 4
    p_factor_num, p_factor_den = 3, 4  # 1-1/2^2
    sl_index = N**3 * p_factor_num // p_factor_den
    psl_index = sl_index // 2
    cusps = (N**2 * p_factor_num // p_factor_den) // 2
    genus_num = 12 + psl_index - 6 * cusps  # 12*g = 12+mu-6c when e2=e3=0
    if genus_num % 12:
        raise SystemExit("X(4) genus arithmetic nonintegral")
    genus_z = genus_num // 12
    fg = cert["factor_base_genus"]
    if (psl_index, cusps, genus_z) != (fg["psl_index"], fg["cusp_count"], fg["genus"]):
        raise SystemExit("factor-base genus data moved")
    if genus_z != 0:
        raise SystemExit("AO requires genus-zero factor base")

    am_classes = {
        int(x["C_dot_B"]): [int(j) for j in x["labels_1based"]]
        for x in am["retained_picard_replay"]["fibre_classes"]
    }
    if set(am_classes) != {81, 105}:
        raise SystemExit("AM fibre degrees moved")

    replay_bounds = []
    for row in cert["boundary_six_packs"]:
        n = int(row["projection_degree"])
        labels = [int(x) for x in row["labels_1based"]]
        if labels != am_classes[n]:
            raise SystemExit(f"AM label pack moved for n={n}")
        vals = [pairings[j - 1] for j in labels]
        q = sum(vals)
        if vals != row["C_dot_boundary_components"] or q != row["q_boundary_sum"]:
            raise SystemExit(f"boundary intersections moved for n={n}")
        lhs = 6 * n
        rhs = 2 * q + e
        if lhs != rhs or lhs != row["six_fibre_identity"]["lhs_6n"] or rhs != row["six_fibre_identity"]["rhs_2q_plus_e"]:
            raise SystemExit(f"six-fibre identity failed for n={n}")
        R = 2 * n
        Bmin = e + q - R
        if R != row["total_ramification_genus1_to_genus0"] or Bmin != row["minimum_node_preimages"]:
            raise SystemExit(f"Hurwitz replay moved for n={n}")
        replay_bounds.append(Bmin)

    Bmin = max(replay_bounds)
    excess = Bmin - support
    increments = sorted((m - 1 for m in masses if m > 1), reverse=True)
    cumulative = 0
    min_multi = 0
    for inc in increments:
        if cumulative >= excess:
            break
        cumulative += inc
        min_multi += 1
    if cumulative < excess:
        raise SystemExit("branch capacity cannot reach AO requirement")
    top23 = sum(increments[:23])
    top24 = sum(increments[:24])

    exp = cert["exact_results"]
    expected = {
        "minimum_total_normalization_preimages_over_met_surface_nodes": Bmin,
        "minimum_normalization_branch_excess_over_47_met_nodes": excess,
        "largest_23_multibranch_branch_increment_sum": top23,
        "largest_24_multibranch_branch_increment_sum": top24,
        "minimum_distinct_multibranch_surface_nodes": min_multi,
    }
    for key, value in expected.items():
        if exp[key] != value:
            raise SystemExit(f"{key} moved: cert={exp[key]} replay={value}")

    if not (top23 < excess <= top24 and min_multi == 24 and Bmin == 238):
        raise SystemExit("AO threshold regression")
    if Bmin <= am["exact_results"]["minimum_total_normalization_preimages_over_met_surface_nodes"]:
        raise SystemExit("AO failed to strengthen AM node-preimage bound")
    if min_multi <= am["exact_results"]["minimum_distinct_multibranch_surface_nodes"]:
        raise SystemExit("AO failed to strengthen AM multibranch bound")
    if any(cert["firewalls"].values()):
        raise SystemExit("AO firewall moved")
    if cert["decision"]["v6_carrier_excluded"]:
        raise SystemExit("AO must not exclude V6")

    print("PASS_STAGE32_POST1648AO_SPECIAL_FIBRE_HURWITZ_BUDGET")
    print(cert["canonical_sha256_without_this_field"])
    print(json.dumps({"Bmin": Bmin, "branch_excess": excess, "minimum_multibranch_nodes": min_multi}, sort_keys=True))


if __name__ == "__main__":
    main()
