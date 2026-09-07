#!/usr/bin/env python3
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ART = HERE / "ex1-05f-h4-local-cusp-projection-ramification-adapter.json"
UP05B = HERE / "ex1-05b-inertia-parity-stabilizer.json"
UP05C = HERE / "ex1-05c-inertia-class-capacity.json"
UP05E = HERE / "ex1-05e-h4-modular-factor-projection-reduction.json"
FSM = ROOT / "stage32/residual-32-01-production/post1648ah-fsm-unibranch-source-note.md"
BIDEG = ROOT / "stage32/residual-32-01-production/post1484-v6-modular-factor-bidegree-source-note.md"
ODD = ROOT / "stage32/residual-32-01-production/post1473-specific-class-multibranch-beauville-odd-branch-wall.md"


def git_blob_sha1(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def load_canonical(path: Path):
    d = json.loads(path.read_text())
    expected = d.pop("canonical_sha256_without_this_field")
    canon = json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    assert hashlib.sha256(canon.encode()).hexdigest() == expected
    return d, expected


d, expected = load_canonical(ART)
u05b = json.loads(UP05B.read_text())
u05c = json.loads(UP05C.read_text())
u05e = json.loads(UP05E.read_text())
assert d["source_locks"]["ex1_05b"]["canonical_sha256"] == u05b["canonical_sha256_without_this_field"]
assert d["source_locks"]["ex1_05c"]["canonical_sha256"] == u05c["canonical_sha256_without_this_field"]
assert d["source_locks"]["ex1_05e"]["canonical_sha256"] == u05e["canonical_sha256_without_this_field"]
assert git_blob_sha1(FSM) == d["source_locks"]["fsm_local_orders"]["blob_sha1"]
assert git_blob_sha1(BIDEG) == d["source_locks"]["resolved_modular_fiber"]["blob_sha1"]
assert git_blob_sha1(ODD) == d["source_locks"]["beauville_odd_contact"]["blob_sha1"]

# Local base-change formula: normalization of v^2=t^k has gcd(k,2)
# branches, each of local degree k/g to the v-line.
def rho(k):
    g = math.gcd(k, 2)
    return g * (k // g - 1)

for k in range(1, 50):
    assert rho(k) == k - math.gcd(k, 2)
    if k % 2:
        assert rho(k) == k - 1
    else:
        assert rho(k) == k - 2

# Boundary labels 33..44 are the four C2 groups concatenated in source order.
groups = u05c["divisor_mass_adapter"]["C2_pairings"]
boundary = groups["b1_zero"] + groups["b2_zero"] + groups["b3_zero"]
V = d["fixed_v6_six_cusp_degree_replay"]
assert boundary == V["boundary_labels_33_to_44_pairings"]
first_labels = V["first_factor_labels"]
second_labels = V["second_factor_labels"]
first = [boundary[i-33] for i in first_labels]
second = [boundary[i-33] for i in second_labels]
assert first == V["first_factor_boundary_pairings"]
assert second == V["second_factor_boundary_pairings"]
assert sum(first) == V["first_factor_boundary_sum"] == 182
assert sum(second) == V["second_factor_boundary_sum"] == 110
P = u05b["target"]["exceptional_pairings"]
assert len(P) == 48 and sum(P) == V["exceptional_mass"] == 266
assert 2*sum(first) + sum(P) == 6*105 == 630
assert 2*sum(second) + sum(P) == 6*81 == 486

# Every even Q from the parity minimum 26 through 266 can be represented
# nodewise by parts 1 and 2 only.  This gives zero special-cusp projection
# ramification using the minimal a1=a2=4m valuation choice.
parity_min = sum(m % 2 for m in P)
assert parity_min == 26
capacity_steps = sum(m // 2 for m in P)
assert capacity_steps == (266 - 26)//2 == 120


def q_vector(Q):
    q = [m % 2 for m in P]
    need = (Q - sum(q)) // 2
    assert Q >= sum(q) and (Q - sum(q)) % 2 == 0
    for i, m in enumerate(P):
        take = min(need, m // 2)
        q[i] += 2*take
        need -= take
        if need == 0:
            break
    assert need == 0
    return q

Qvals = list(range(210, 267, 2))
assert len(Qvals) == 29
for r, Q in enumerate(Qvals):
    q = q_vector(Q)
    assert sum(q) == Q
    total_mass = 0
    odd_parts = 0
    cusp_r1 = 0
    cusp_r2 = 0
    for M, qi in zip(P, q):
        assert 0 <= qi <= M and qi % 2 == M % 2
        parts = [1]*qi + [2]*((M-qi)//2)
        assert sum(parts) == M
        total_mass += sum(parts)
        odd_parts += sum(x % 2 for x in parts)
        # minimal a1=a2=4m gives k1=k2=m and ell1=ell2=0
        cusp_r1 += sum(rho(x) for x in parts)
        cusp_r2 += sum(rho(x) for x in parts)
    assert total_mass == 266
    assert odd_parts == Q
    assert cusp_r1 == cusp_r2 == 0
    # Realize each unit of C.L as a distinct transverse smooth boundary hit:
    # k=2, so rho=0.
    assert rho(2) == 0
    R105 = Q - 210
    R81 = Q - 162
    assert R105 == 2*r
    assert R81 == 48 + 2*r
    assert R105 >= cusp_r1 and R81 >= cusp_r2

D = d["decision"]
assert D["Q_states_entering_05F"] == 29
assert D["Q_states_excluded_by_local_cusp_adapter"] == 0
assert D["Q_states_leaving_05F"] == 29
assert not D["local_cusp_route_excludes_target"]
assert D["next_route"] == "EX1-05G_H4_COMMON_COVER_CORRESPONDENCE_COUPLING"
assert d["cycle_exit"]["CYCLE_ROUTE_STATUS"] == "BLOCKED_NEW_PATTERN_ISOLATED"
assert not d["exit"]["all_residual_configurations_disposed"]
assert not d["exit"]["full_target_closure"]
assert not d["firewalls"]["coarse_local_valuation_witness_promoted_to_global_curve"]
assert not d["firewalls"]["off_cusp_ramification_numerical_assignment_promoted_to_map_existence"]
print("EX1-05F replay PASS: exact local cusp ramification adapter removes 0/29 Q states; common-cover/off-cusp coupling is the next receiver")
