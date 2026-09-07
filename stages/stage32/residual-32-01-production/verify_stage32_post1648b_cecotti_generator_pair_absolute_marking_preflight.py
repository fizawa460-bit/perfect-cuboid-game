#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1648b-cecotti-generator-pair-absolute-marking-preflight.json"
EXPECTED_CERT = "b0737602656ff5de3c98ba98cc862ec7b29599255c8da621099c2a63a69e503b"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def canonical_without_field(obj: dict, field: str) -> str:
    body = dict(obj)
    body.pop(field, None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_locked_json(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), lock["path"]
    assert git_blob_sha(path) == lock["blob_sha1"], lock["path"]
    obj = json.loads(path.read_text(encoding="utf-8"))
    expected = lock["canonical_sha256"]
    if "canonical_sha256_without_this_field" in obj:
        field = "canonical_sha256_without_this_field"
    elif "canonical_sha256" in obj:
        field = "canonical_sha256"
    else:
        raise AssertionError(f"no canonical field: {lock['path']}")
    assert obj[field] == expected, lock["path"]
    assert canonical_without_field(obj, field) == expected, lock["path"]
    return obj


# Exact Gaussian-rational arithmetic for the six Bolza branch points.
G = tuple[Fraction, Fraction]
INF = None


def g(a=0, b=0):
    return (Fraction(a), Fraction(b))


def add(x: G, y: G) -> G:
    return (x[0] + y[0], x[1] + y[1])


def mul(x: G, y: G) -> G:
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def inv(x: G) -> G:
    n = x[0] * x[0] + x[1] * x[1]
    assert n != 0
    return (x[0] / n, -x[1] / n)


def div(x: G, y: G) -> G:
    return mul(x, inv(y))


def mobius(x, a: G, b: G, c: G, d: G):
    if x is INF:
        if c == g(0):
            return INF
        return div(a, c)
    num = add(mul(a, x), b)
    den = add(mul(c, x), d)
    if den == g(0):
        return INF
    return div(num, den)


cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
assert cert["canonical_sha256_without_this_field"] == EXPECTED_CERT
assert canonical_without_field(cert, "canonical_sha256_without_this_field") == EXPECTED_CERT

locks = cert["source_locks"]
post1648 = load_locked_json(locks["post1648_localization"])
abstract_w = load_locked_json(locks["abstract_w_weierstrass"])
gauge = load_locked_json(locks["marked_w_gauge_orbit"])
rosati = load_locked_json(locks["principal_rosati"])

assert post1648["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert abstract_w["weierstrass_model"]["cusp_pairs"] == {
    "Z1": [1, 6], "Z2": [3, 5], "Z3": [2, 4]
}
assert abstract_w["weierstrass_model"]["id_to_x"] == {
    "1": "+1", "6": "-1", "3": "+i", "5": "-i", "2": "0", "4": "infinity"
}
assert abstract_w["torsor_plane"]["retained_F2_4_coordinates_identified"] is False
assert rosati["quadratic_order"] == {
    "symbol": "r", "relation": "r^2=-2", "ring": "Z[r]=Z[sqrt(-2)]", "conjugation": "bar(r)=-r"
}

points = {
    "+1": g(1), "-1": g(-1), "+i": g(0, 1), "-i": g(0, -1),
    "0": g(0), "infinity": INF,
}
reverse = {v: k for k, v in points.items()}
I = g(0, 1)
ONE = g(1)

# phi2(x)=-(x+i)/(1+i*x) = (-x-i)/(i*x+1)
phi2_coeff = (g(-1), g(0, -1), I, ONE)
# phi6(x)=i*(x-1)/(x+1) = (i*x-i)/(x+1)
phi6_coeff = (I, g(0, -1), ONE, ONE)

phi2_point = {name: reverse[mobius(x, *phi2_coeff)] for name, x in points.items()}
phi6_point = {name: reverse[mobius(x, *phi6_coeff)] for name, x in points.items()}
assert phi2_point == {
    "0": "-i", "infinity": "+i", "+1": "-1", "-1": "+1",
    "+i": "infinity", "-i": "0",
}
assert phi6_point == {
    "0": "-i", "infinity": "+i", "+1": "0", "-1": "infinity",
    "+i": "-1", "-i": "+1",
}

pairs = {
    "Z1": frozenset({"+1", "-1"}),
    "Z2": frozenset({"+i", "-i"}),
    "Z3": frozenset({"0", "infinity"}),
}


def induced_pair_action(point_action: dict[str, str]) -> dict[str, str]:
    out = {}
    for name, pair in pairs.items():
        image = frozenset(point_action[x] for x in pair)
        out[name] = next(k for k, v in pairs.items() if v == image)
    return out


phi2_pair = induced_pair_action(phi2_point)
phi6_pair = induced_pair_action(phi6_point)
assert phi2_pair == {"Z1": "Z1", "Z2": "Z3", "Z3": "Z2"}
assert phi6_pair == {"Z1": "Z3", "Z2": "Z1", "Z3": "Z2"}
assert cert["curve_pair_action"]["phi2_pair_permutation"] == phi2_pair
assert cert["curve_pair_action"]["phi6_pair_permutation"] == phi6_pair

assert gauge["audited_input"]["residues_decimal"] == [73, 97, 235]
assert gauge["mod2_W_action"]["line_labels"] == {
    "L1": [1, 0], "L2": [0, 1], "L3": [1, 1]
}
assert gauge["mod2_W_action"]["b3_line_permutation"] == "L1->L3->L2->L1"
assert gauge["mod2_W_action"]["b4_line_permutation"] == "L1 fixed; L2<->L3"

target_b4 = {"L1": "L1", "L2": "L3", "L3": "L2"}
target_b3 = {"L1": "L3", "L2": "L1", "L3": "L2"}
source = ["Z1", "Z2", "Z3"]
target = ["L1", "L2", "L3"]
all_maps = [dict(zip(source, p)) for p in itertools.permutations(target)]
assert len(all_maps) == 6
compatible = []
for m in all_maps:
    if all(m[phi2_pair[x]] == target_b4[m[x]] for x in source) and all(
        m[phi6_pair[x]] == target_b3[m[x]] for x in source
    ):
        compatible.append(m)
assert compatible == [{"Z1": "L1", "Z2": "L2", "Z3": "L3"}]

pre = cert["finite_equivariant_preflight"]
assert pre["equivariant_bijection_count"] == 1
assert pre["unique_pair_to_line"] == compatible[0]
assert pre["unique_delta_to_line"] == {
    "delta_pm1": "L1", "delta_pmi": "L2", "delta_0inf": "L3"
}
assert pre["conditional_delta0inf_residue_decimal"] == 235
assert pre["conditional_only_not_current_credit"] is True

obs = cert["actual_obstruction"]
assert obs["curve_to_lattice_generator_pair_source_bound"] is False
assert obs["conjugating_g_mod2_on_J2_materialized"] is False
assert obs["explicit_marked_ppav_isomorphism_source_bound"] is False
assert obs["all_six_unmarked_bijections_still_admissible_for_current_credit"] is True

external = cert["external_source_locks"]
assert any(
    "does not explicitly identify phi2 with S=b4 or phi6 with T=-b3" in fact
    for fact in external["cecotti"]["exact_supported_facts"]
)
assert "H48=g*G48*g^{-1}" in external["koziarz_rito_roulleau"]["exact_supported_facts"]

assert cert["fixed_target"]["surviving_residues_decimal"] == [73, 97, 235]
assert cert["decision"]["survivors_current_credit"] == [73, 97, 235]
assert cert["decision"]["conditional_survivor_if_generator_pair_bound"] == 235
assert cert["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert cert["decision"]["Q602_excluded"] is False
assert cert["decision"]["O210_excluded"] is False
assert cert["firewalls"]["conditional_residue235_promoted_to_current_survivor"] is False
assert cert["firewalls"]["matching_orders_or_group_presentation_promoted_to_semantic_adapter"] is False
assert cert["firewalls"]["koziarz_conjugacy_existence_promoted_to_marked_conjugacy"] is False

print("POST1648B_CECOTTI_GENERATOR_PAIR_ABSOLUTE_MARKING_PREFLIGHT_COMPLETE")
print(f"certificate_canonical={EXPECTED_CERT}")
print("conditional_equivariant_marking=Z1->L1,Z2->L2,Z3->L3")
print("conditional_delta0inf=L3 residue=235 NOT_CURRENT_CREDIT")
print("current_survivors=73,97,235 Q602_excluded=false O210_excluded=false")
print("missing=marked_ppav_conjugacy_g_mod2_or_equivalent_generator_pair_source_lock")
