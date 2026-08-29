#!/usr/bin/env python3
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-four-even-contact-pairing-orbits.json"

def poly_eval(coeffs, x):
    return sum(c * (x ** i) for i, c in enumerate(coeffs))

def xor_bits(a, b):
    return "".join(str(int(x) ^ int(y)) for x, y in zip(a, b))

def invariant(bits):
    v = [int(c) for c in bits]
    return [v[0] ^ v[1], v[2] ^ v[3]]

with CERT.open() as f:
    c = json.load(f)

assert c["schema"] == "STAGE33_12_J2_FOUR_EVEN_CONTACT_PAIRING_ORBITS_V1"
assert c["status"] == "PASS_EXACT_LOCAL_RESOLUTION_AND_COMPLETE_PAIRING_ORBIT_CENSUS"
assert c["class2_budget_batch"] == 1
assert c["class2_budget_total"] == 4

# Exact polynomial identities in coefficient order constant..highest.
# r=(t^2-1)^2=t^4-2t^2+1, q=t^4-6t^2+1.
r = [1, 0, -2, 0, 1]
q = [1, 0, -6, 0, 1]
r_minus_q = [a-b for a, b in zip(r, q)]
assert r_minus_q == [0, 0, 4, 0, 0]
assert poly_eval(q, 1) == -4
assert poly_eval(q, -1) == -4
assert poly_eval(q, 0) == 1
# At infinity, after t=1/u and division by t^4, qbar=1-6u^2+u^4.
qbar = [1, 0, -6, 0, 1]
rbar = [1, 0, -2, 0, 1]
assert poly_eval(qbar, 0) == 1
assert [a-b for a, b in zip(rbar, qbar)] == [0, 0, 4, 0, 0]

local = c["local_resolutions"]
assert len(local) == 4
assert all(row["unit_at_contact"] == 4 for row in local)
assert all(row["strict_transforms_transverse"] for row in local)
assert all(row["both_normalized_covers_unramified"] for row in local)
assert all(row["pairing_count"] == 2 for row in local)
assert c["local_pairing_lemma"]["binary_pairing_proved_at_all_four_contacts"] is True
assert c["local_pairing_lemma"]["independent_raw_choices"] == 4
assert c["local_pairing_lemma"]["raw_pairing_count"] == 16

raw = ["".join(map(str, p)) for p in itertools.product((0,1), repeat=4)]
assert sorted(c["raw_pairings"]) == raw

flips = c["sheet_relabeling_action"]["component_deck_flips"]
assert flips == {"delta_C0":"1100", "delta_Cr":"1111", "delta_Cq":"0011"}
assert xor_bits(xor_bits(flips["delta_C0"], flips["delta_Cr"]), flips["delta_Cq"]) == "0000"
H = sorted({"0000", flips["delta_C0"], flips["delta_Cr"], flips["delta_Cq"]})
assert H == sorted(c["sheet_relabeling_action"]["effective_action_subspace"])
assert len(H) == 4
assert c["sheet_relabeling_action"]["effective_group_order"] == 4
assert c["sheet_relabeling_action"]["effective_group_rank_over_F2"] == 2

# Construct every orbit from every predecessor; no canonical pruning assumption.
seen = set()
constructed = []
for p in raw:
    if p in seen:
        continue
    orb = sorted({xor_bits(p, h) for h in H})
    constructed.append(orb)
    seen.update(orb)
assert len(constructed) == 4
assert seen == set(raw)
assert all(len(o) == 4 for o in constructed)

cert_orbits = [sorted(o["members"]) for o in c["orbits"]]
assert sorted(cert_orbits) == sorted(constructed)
all_members = [m for o in cert_orbits for m in o]
assert len(all_members) == len(set(all_members)) == 16

for row in c["orbits"]:
    rep = row["representative"]
    assert rep in row["members"]
    inv = invariant(rep)
    assert inv == row["invariant"]
    assert all(invariant(m) == inv for m in row["members"])

assert c["orbit_invariants"]["complete"] is True
coverage = c["coverage"]
assert coverage["orbit_count"] == 4
assert coverage["orbit_size_each"] == 4
assert coverage["union_size"] == coverage["raw_space_size"] == 16
assert coverage["pairwise_disjoint"] is True
assert coverage["complete_coverage"] is True
assert coverage["canonical_pruning_used"] is False
assert coverage["predecessor_reconstruction_available"] is True

fw = c["firewalls"]
for key in [
    "named_cv_j2_pairing_orbit_selected",
    "pairing_orbit_bits_equal_marked_brauer_bits",
    "j2_marked_coordinate_selected",
    "j2_twisted_transcendental_kernel_identified",
    "j2_explicit_torsor_surface_materialized",
    "stage33_12_closed_exact",
    "stage33_13_released",
    "heavy_actions_authorized",
    "theorem_credit",
    "receiver_credit",
    "endpoint_credit",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
]:
    assert fw[key] is False

print("PASS: exact four-even-contact local resolution and 16-to-4 pairing orbit census")
