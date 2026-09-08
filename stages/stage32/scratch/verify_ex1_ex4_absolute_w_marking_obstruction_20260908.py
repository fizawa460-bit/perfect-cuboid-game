#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter, deque
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT = ROOT / "stages/stage32/scratch/ex1-ex4-absolute-w-marking-obstruction-20260908.json"
EXPECTED_CANONICAL = "e113ef9e55eb5205266b54718c2b62f0b113d657538aedd68ac4f1438edaf2b0"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_locked_json(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), path
    if "blob_sha1" in lock:
        assert blob_sha1(path) == lock["blob_sha1"], path
    doc = json.loads(path.read_text(encoding="utf-8"))
    if "canonical_sha256" in lock:
        assert canonical_sha256(doc) == lock["canonical_sha256"], path
        assert doc.get("canonical_sha256_without_this_field") == lock["canonical_sha256"], path
    return doc


@dataclass(frozen=True)
class R:
    a: int
    b: int

    def __add__(self, other: "R") -> "R":
        return R(self.a + other.a, self.b + other.b)

    def __neg__(self) -> "R":
        return R(-self.a, -self.b)

    def __sub__(self, other: "R") -> "R":
        return self + (-other)

    def __mul__(self, other: "R") -> "R":
        # r^2 = -2
        return R(self.a * other.a - 2 * self.b * other.b,
                 self.a * other.b + self.b * other.a)


ZERO = R(0, 0)
ONE = R(1, 0)
MINUS_ONE = R(-1, 0)
RR = R(0, 1)


def mat(rows):
    return tuple(tuple(x if isinstance(x, R) else R(int(x), 0) for x in row) for row in rows)


def mm(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(2)), ZERO)
                       for j in range(2)) for i in range(2))


def mneg(a):
    return tuple(tuple(-x for x in row) for row in a)


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def inv(a):
    d = det(a)
    assert d in (ONE, MINUS_ONE), d
    dinv = d
    return (
        (dinv * a[1][1], dinv * (-a[0][1])),
        (dinv * (-a[1][0]), dinv * a[0][0]),
    )


def wmat_mod2(a):
    # On W=ker(r mod 2), an entry a+b*r acts on r*e_j by a*r*e_i mod 2.
    return tuple(tuple(a[i][j].a & 1 for j in range(2)) for i in range(2))


def mv2(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(2)) & 1 for i in range(2))


def enumerate_g12():
    identity = mat([[1, 0], [0, 1]])
    b3 = mat([[-1, -1], [1, 0]])
    b4 = ((ONE, ONE + RR), (ZERO, MINUS_ONE))
    generators = [b3, b4, inv(b3), inv(b4)]
    group = {identity}
    q = deque([identity])
    while q:
        x = q.popleft()
        for g in generators:
            y = mm(x, g)
            if y not in group:
                group.add(y)
                q.append(y)
    return identity, b3, b4, group


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert cert["schema"] == "STAGE32_MAIN_SCRATCH_EX1_EX4_ABSOLUTE_W_MARKING_OBSTRUCTION_V1"
    assert cert["status"] == "SCRATCH_EXACT_BOUNDED_TESTED_SOURCE_PACKAGE_OBSTRUCTION_UNAUDITED"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL
    assert cert["decision"]["authority_changed"] is False
    assert cert["decision"]["claim_dag_changed"] is False
    assert cert["decision"]["EX4_terminal_outcome_claimed"] is False

    locks = cert["source_locks"]
    uniform = load_locked_json(locks["uniform_ex1_28_to_3"])
    localization = load_locked_json(locks["absolute_marking_localization"])
    cecotti_b = load_locked_json(locks["cecotti_generator_preflight"])
    cecotti_j = load_locked_json(locks["cecotti_trace_orientation"])
    hperp = load_locked_json(locks["hperp_chi_u"])
    gauge = load_locked_json(locks["gauge_orbit"])
    fsm = load_locked_json(locks["fsm_stoll_action"])
    principal = load_locked_json(locks["principal_rosati"])
    ex4_state = load_locked_json(locks["ex4_bootstrap_state"])

    assert uniform["scope"]["EX1_state_count"] == 29
    assert uniform["scope"]["Q_Rosati"] == 602
    assert uniform["direct_filter"]["surviving_residues_decimal"] == [73, 97, 235]
    assert uniform["coarse_joint_effect"]["new_cells_29_times_3"] == 87

    source = localization["source_bound_chain"]
    assert source["normal_label_9_character"] == "chi_u"
    assert source["chi_u_canonical_pair"] == "Z3"
    assert source["Z3_pair_values"] == ["0", "infinity"]
    assert source["abstract_class"] == "delta_0inf"
    assert localization["decision"]["absolute_delta0inf_retained_W_line_identified"] is False

    assert hperp["abstract_character_to_w_binding"]["chi_u_canonical_pair"] == "Z3"
    assert hperp["abstract_character_to_w_binding"]["retained_F2_4_coordinate_line_identified"] is False

    target = localization["retained_W_side"]
    assert target["lines"] == {"L1": [1, 0], "L2": [0, 1], "L3": [1, 1]}
    assert target["residue_to_line"] == {"73": "L1", "97": "L2", "235": "L3"}
    assert gauge["residue_conjugation"]["single_orbit"] is True
    assert gauge["mod2_W_action"]["transitive_on_nonzero_W_lines"] is True

    # Recompute G12 and the trace-compatible plus-r ordered-generator orbit.
    identity, b3, b4, group = enumerate_g12()
    assert len(group) == 48
    S = b4
    T = mneg(b3)
    Tinv = inv(T)

    pair_to_conjugators = {}
    for g in group:
        gi = inv(g)
        pair = (mm(mm(g, S), gi), mm(mm(g, Tinv), gi))
        pair_to_conjugators.setdefault(pair, []).append(g)

    assert len(pair_to_conjugators) == 24
    assert {len(v) for v in pair_to_conjugators.values()} == {2}

    lines = {"L1": (1, 0), "L2": (0, 1), "L3": (1, 1)}
    line_name = {v: k for k, v in lines.items()}
    reference_line = lines["L2"]
    counts = Counter()
    for conjugators in pair_to_conjugators.values():
        images = {line_name[mv2(wmat_mod2(g), reference_line)] for g in conjugators}
        # The two conjugators differ by central +/-I, which is identical mod 2 on W.
        assert len(images) == 1
        counts[next(iter(images))] += 1
    assert counts == Counter({"L1": 8, "L2": 8, "L3": 8})

    replay = cert["exact_group_replay"]
    assert replay["G12_order"] == 48
    assert replay["distinct_inner_conjugates_of_reference_pair"] == 24
    assert replay["conjugator_multiplicity_per_pair"] == 2
    assert replay["delta0inf_line_counts_over_24_pairs"] == {"L1": 8, "L2": 8, "L3": 8}
    assert cecotti_j["ordered_generator_pair_enumeration"]["trace_plus_r_orbit"]["size"] == 24
    assert cecotti_j["W_line_consequence"]["all_plus_r_inner_conjugates"]["delta0inf_image_counts"] == {"L1": 8, "L2": 8, "L3": 8}
    assert cecotti_j["decision"]["absolute_delta0inf_retained_W_line_identified"] is False

    # The named literal plus-r representative itself is only conditional.
    assert cecotti_j["W_line_consequence"]["literal_plus_r_unique_pair_to_line"]["Z3"] == "L2"
    assert cecotti_j["W_line_consequence"]["literal_plus_r_conditional_only_not_current_credit"] is True
    assert cecotti_b["actual_obstruction"]["conjugating_g_mod2_on_J2_materialized"] is False
    assert cecotti_b["actual_obstruction"]["explicit_marked_ppav_isomorphism_source_bound"] is False

    # Recompute the weaker conditional FSM-S anchor.  Matching only the
    # transposition Z1<->Z3, Z2 fixed to principal b4 leaves two bijections.
    src = ["Z1", "Z2", "Z3"]
    tgt = ["L1", "L2", "L3"]
    source_S = {"Z1": "Z3", "Z3": "Z1", "Z2": "Z2"}
    target_b4 = {"L1": "L1", "L2": "L3", "L3": "L2"}
    bijections = []
    for p in itertools.permutations(tgt):
        f = dict(zip(src, p))
        if all(f[source_S[x]] == target_b4[f[x]] for x in src):
            bijections.append(f)
    assert len(bijections) == 2
    assert sorted(f["Z3"] for f in bijections) == ["L2", "L3"]
    assert localization["finite_marking_obstruction"]["conditional_if_fsm_S_equals_principal_b4"]["equivariant_bijection_count"] == 2
    assert localization["finite_marking_obstruction"]["conditional_if_fsm_S_equals_principal_b4"]["delta_0inf_possible_lines"] == ["L2", "L3"]

    assert fsm["fsm_section2_actions"]["S"]["stoll_word"] == "g2*g5"
    assert principal["quadratic_order"]["relation"] == "r^2=-2"

    # EX4 contract says a bounded negative terminal would require an exhaustive
    # frozen package and residual ambiguity calculation.  This scratch result
    # deliberately does not claim EX4 terminal closure because the EX4 source
    # inventory itself has not been completed here.
    terminal = ex4_state["completion_contract"]
    assert "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE" in terminal["allowed_terminal_outcomes"]
    assert cert["tested_package_definition"]["package_is_repository_wide_exhaustive"] is False
    assert cert["decision"]["EX4_terminal_outcome_claimed"] is False

    obstruction = cert["bounded_obstruction"]
    assert obstruction["tested_package_selects_absolute_delta0inf_line"] is False
    assert obstruction["tested_package_selects_absolute_Q602_residue"] is False
    assert obstruction["uniform_EX1_residue_count_per_Q_state"] == 3
    assert obstruction["uniform_EX1_coarse_cells_remaining"] == 87
    assert obstruction["EX1_Q_states_excluded"] == 0

    print("PASS scratch EX1-EX4 absolute-W marking obstruction replay")
    print("G12=48 plus_r_pairs=24 delta0inf_counts=L1:8,L2:8,L3:8")
    print("FSM_S_only_equivariant_bijections=2 delta0inf=L2_or_L3")
    print("uniform_EX1_cells=87 absolute_residue=UNSELECTED authority=SCRATCH_UNAUDITED")


if __name__ == "__main__":
    main()
