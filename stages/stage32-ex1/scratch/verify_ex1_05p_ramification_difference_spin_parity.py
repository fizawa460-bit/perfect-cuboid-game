#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
ART = HERE / "ex1-05p-ramification-difference-spin-parity-preflight.json"
UP05H = STAGE / "ex1-05h-upstairs-conductor-discriminant-off-cusp-coupling.json"
UP05O = HERE / "ex1-05o-common-v4-branch-cycle-monodromy-lift-preflight.json"


def git_blob_sha1(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def load_canonical(path: Path):
    d = json.loads(path.read_text(encoding="utf-8"))
    claimed = d.pop("canonical_sha256_without_this_field")
    canon = json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    actual = hashlib.sha256(canon.encode()).hexdigest()
    assert actual == claimed, (path, actual, claimed)
    return d, claimed


d = json.loads(ART.read_text(encoding="utf-8"))
up05h, up05h_canon = load_canonical(UP05H)
up05o = json.loads(UP05O.read_text(encoding="utf-8"))

assert d["schema"] == "STAGE32EX1_EX1_05P_RAMIFICATION_DIFFERENCE_SPIN_PARITY_PREFLIGHT_V1"
assert d["authority"] == "SCRATCH_NONAUTHORITATIVE"
assert d["base_main_sha"] == "d5545b32e6b3088bca53318998d434f2745b03e9"
assert d["parent_scratch_head"] == "d963dfc979af4298503ab7a5336135c6859e2e3b"

locks = d["source_locks"]
assert locks["ex1_05h"]["canonical_sha256"] == up05h_canon == "e2f1c363b60f0af045843f887446be0cd67cb000d5cd42f05fa26c82d5860893"
assert git_blob_sha1(UP05O) == locks["parent_05o"]["blob_sha1"] == "db22f3fdf75be3371d2bf46a516067c0d2e0f4b8"
assert locks["external_spin_branched_cover"]["arxiv"] == "math/0312186"
assert locks["picard_divisibility"]["tag"] == "03RN"

# Re-establish the exact two-map Riemann-Hurwitz ladder from retained 05H.
L = up05h["upstairs_defect_ladder"]
Qvals = list(range(210, 267, 2))
rvals = list(range(29))
assert L["EX1_Q_values"] == Qvals
assert L["r_values"] == rvals
assert L["R105_values"] == [2*r for r in rvals]
assert L["R81_values"] == [48 + 2*r for r in rvals]

C = up05h["conductor_adjunction_coupling"]
assert C["ramification_difference_class"] == "R81-R105 ~ f1^*K_C2-f2^*K_C2"
assert C["ramification_difference_line_bundle_2_divisible"] is True

S = d["setup"]
assert S["degrees"] == [105, 81]
assert S["difference_identity"] == "R81-R105 ~ f105^*K_C2-f81^*K_C2"

I = d["compatible_square_root_identity"]
assert I["A_degree"] == 24 == 105 - 81
assert I["R105_even_degree"] is True
assert I["R81_even_degree"] is True
assert I["exact_equality"] == "Theta81 ~= Theta105"

for r, Q, R105, R81 in zip(rvals, Qvals, L["R105_values"], L["R81_values"]):
    gD = 106 + r
    deg_KD = 2*gD - 2
    assert deg_KD == Q == 210 + 2*r

    # deg K_C2=2. Both Riemann-Hurwitz expressions have the same degree.
    assert 2*105 + R105 == deg_KD
    assert 2*81 + R81 == deg_KD
    assert R81 - R105 == 48

    # eta on genus-2 C2 has degree 1. A=f105^*eta*(f81^*eta)^-1.
    deg_A = 105 - 81
    assert deg_A == I["A_degree"] == 24

    # Any square root M105 of O(R105) has degree r; compatible M81=M105*A.
    deg_M105 = R105 // 2
    deg_M81 = deg_M105 + deg_A
    assert deg_M105 == r
    assert deg_M81 == r + 24 == R81 // 2

    # The two induced theta characteristics have identical degree g(D)-1.
    deg_theta105 = 105 + deg_M105
    deg_theta81 = 81 + deg_M81
    assert deg_theta105 == deg_theta81 == 105 + r == gD - 1

N = d["noncanonical_root_firewall"]
assert N["roots_form_J2_torsor"] is True
assert N["parity_not_root_choice_invariant"] is True

H = d["spin_hurwitz_applicability"]
assert H["current_EX1_has_only_total_degrees"] is True
assert H["local_ramification_profiles_extracted"] is False
assert H["R105_coefficientwise_even_proved"] is False
assert H["R81_coefficientwise_even_proved"] is False
assert H["spin_hurwitz_parity_defined_canonically_from_current_data"] is False
assert H["total_even_degree_is_insufficient"] is True

R = d["statewise_replay"]
assert R["Q_values"] == Qvals
assert R["r_values"] == rvals
assert R["all_states_have_square_root_compatible_identity"] is True
assert R["Q_states_entering"] == 29
assert R["Q_states_excluded"] == 0
assert R["Q_states_leaving"] == 29

D = d["decision"]
assert D["route_status"] == "BLOCKED_NEW_PATTERN_ISOLATED"
assert D["spin_parity_obstruction_obtained"] is False
assert D["Q_states_excluded"] == 0
assert D["V6_carrier_excluded"] is False
assert d["next_route"]["route_id"] == "EX1_05Q_Q602_EFFECTIVE_CORRESPONDENCE_CLASS_MATERIALIZATION_PREFLIGHT"

FW = d["firewalls"]
for key in [
    "even_total_ramification_degree_promoted_to_even_ramification_divisor",
    "arbitrary_square_root_promoted_to_canonical_spin_structure",
    "theta_root_choice_parity_promoted_to_geometric_invariant",
    "spin_hurwitz_odd_ramification_hypothesis_assumed",
    "Q_state_exclusion_claimed",
    "Q602_exclusion_claimed",
    "O210_exclusion_claimed",
    "V6_population_wide_exclusion_claimed",
    "stage32_main_credit",
    "receiver_credit",
    "theorem_credit",
    "endpoint_credit",
    "perfect_cuboid_claim",
]:
    assert FW[key] is False, key

print("PASS_EX1_05P_SPIN_PARITY_BOUNDARY")
print("all_29_states", "compatible theta roots exist; no canonical spin parity from total ramification degrees")
print("next", d["next_route"]["route_id"])
