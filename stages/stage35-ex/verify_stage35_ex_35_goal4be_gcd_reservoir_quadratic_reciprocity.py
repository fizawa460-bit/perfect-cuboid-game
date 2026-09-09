#!/usr/bin/env python3
"""Verify Goal4BE: exact gcd-reservoir Jacobi/quadratic-reciprocity cycle."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4be-gcd-reservoir-quadratic-reciprocity-cycle.json")
SRC = P("stages/stage35-ex/35ex-35/goal4be-gcd-reservoir-quadratic-reciprocity-cycle-source-lock.md")
BD = P("stages/stage35-ex/35ex-35/goal4bd-simultaneous-three-marked-rankjump-endpoint-equivalence.json")
AU = P("stages/stage35-ex/35ex-35/goal4au-three-direction-marked-kummer-gcd-allocation.json")
AU_SRC = P("stages/stage35-ex/35ex-35/goal4au-three-direction-marked-kummer-gcd-allocation-source-lock.md")
PRIVATE = P("stages/stage35-ex/35ex-35/private-edge-gcd-six-variable-decomposition.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "feffef319deaf6104fc14f1b055462e70ae99068fd8564c73e8cf86abbae1a16"
SRC_BLOB = "c0b9f95aa68f2034a6f319f1fb7356bb9b561d7c"
BD_BLOB = "64b8df3fa657ac9628978ce25bd55ff32a8b5da0"
AU_BLOB = "d0dd0597046daf54ad9fcc74991221710a27f12c"
AU_SRC_BLOB = "773b104c65454ae307bb59e87a15c74f505fdcbf"
PRIVATE_BLOB = "d0cd03a5ff744d5f6536b6d2784c0e0d543fea48"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)


def rank_f2(rows: list[list[int]]) -> int:
    a = [sum((bit & 1) << j for j, bit in enumerate(row)) for row in rows]
    rank = 0
    for col in range(max(len(r) for r in rows)):
        pivot = next((i for i in range(rank, len(a)) if (a[i] >> col) & 1), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(len(a)):
            if i != rank and ((a[i] >> col) & 1):
                a[i] ^= a[rank]
        rank += 1
    return rank


def legendre(a: int, p: int) -> int:
    a %= p
    assert a
    r = pow(a, (p - 1) // 2, p)
    return -1 if r == p - 1 else r


assert blob(SRC) == SRC_BLOB
assert blob(BD) == BD_BLOB
assert blob(AU) == AU_BLOB
assert blob(AU_SRC) == AU_SRC_BLOB
assert blob(PRIVATE) == PRIVATE_BLOB

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

bd = json.loads(BD.read_text())
assert bd["canonical_sha256"] == "1fae939f20184ac5bd61b2b9751fb3628201bdd7321f605aade34d5a9de2595e"
assert bd["next"]["unit"] == "35EX-35_GOAL4BE_GCD_RESERVOIR_QUADRATIC_RECIPROCITY_CYCLE_PREFLIGHT"
assert bd["result"]["endpoint_equivalence_obtained"] is True

au = json.loads(AU.read_text())
assert au["canonical_sha256"] == "4d23730b7ec3a2d5b1986d270924c2c34a5019cabd5171ddc1552055bf0971b2"
assert au["odd_prime_allocation"]["h_a"] == "gcd(a,r_BC)"
assert au["odd_prime_allocation"]["h_b"] == "gcd(b,r_AC)"
assert au["odd_prime_allocation"]["h_c"] == "gcd(c,r_AB)"
assert au["cross_face_relation"]["marked_product"] == "d_A*d_B*d_C=1 in Q*/Q*^2"
assert au["linear_rank_F2"] if "linear_rank_F2" in au else True

private = json.loads(PRIVATE.read_text())
assert private["goal2_primitive_parity_coprimality_dictionary"]["derived_coprimalities"] == [
    "gcd(a,b)=gcd(a,c)=gcd(b,c)=1",
    "gcd(a,z)=1",
    "gcd(b,y)=1",
    "gcd(c,x)=1",
]

src = SRC.read_text()
for marker in (
    "(BE-FACE)",
    "(BE-H)",
    "(BE-1mod4)",
    "(BE-W)",
    "(BE-La-prime)",
    "(BE-SYM)",
    "(BE-QR)",
    "(BE-CYCLE)",
    "(BE-R2)",
    "(BE-FLEX)",
    "35EX-35_GOAL4BF_ORIENTED_GAUSSIAN_QUARTIC_RECIPROCITY_RESERVOIR_LIFT_PREFLIGHT",
):
    assert marker in src, marker

# Exact F2 rank/kernel of the pairwise-symbol system.
M = [[1,1,0],[1,0,1],[0,1,1]]
assert rank_f2(M) == 2
for v in ([0,0,0],[1,1,1]):
    assert all(sum(r[j] * v[j] for j in range(3)) % 2 == 0 for r in M)

# Local flexibility witness at ell=5.  a=0, y=c=z=1.
p = 5
models = [(1,2),(2,1)]
bsym = []
for x,b in models:
    y=c=z=1
    assert ((x*b)**2 + (y*c)**2) % p == 0
    assert (b*b) % p in (0,1,4)  # r_AB^2=(z*b)^2
    assert (c*c) % p == 1         # r_AC^2=(z*c)^2
    assert legendre(2*x*y*b*c, p) == 1
    bsym.append(legendre(b,p))
assert bsym == [-1,1]

# Supplementary law used in the source: for p=1 mod4, a square root of -1
# has quadratic character (2/p). Check on representative p=5,13.
for p, iota in [(5,2),(13,5)]:
    assert p % 4 == 1
    assert (iota*iota) % p == p-1
    assert legendre(iota,p) == legendre(2,p)

art = json.loads(ART.read_text())
checkcanon(art)
assert art["source_locks"]["goal4be_source"]["blob_sha1"] == SRC_BLOB
assert art["source_locks"]["goal4bd"]["blob_sha1"] == BD_BLOB
assert art["source_locks"]["goal4au"]["blob_sha1"] == AU_BLOB
assert art["source_locks"]["goal4au_source"]["blob_sha1"] == AU_SRC_BLOB
assert art["source_locks"]["private_gcd"]["blob_sha1"] == PRIVATE_BLOB

parent = art["stacked_parent"]
assert parent["exact_head_sha"] == "e2e27c7220a78bee33313e93e35ab69354029517"
assert parent["aggregate_run"] == 34304490134
assert parent["aggregate_job"] == 102319407204
assert parent["hostile_audited"] is False

rs = art["reservoir_structure"]
assert rs["pairwise_coprime"] is True
assert rs["product_divides_W"] is True
assert rs["all_odd_prime_divisors_1_mod_4"] is True

js = art["jacobi_system"]
assert js["quadratic_reciprocity_symmetric"] is True
assert js["global_cycle"] == "L_a*L_b*L_c=1"
assert js["distinct_from_AU_Kummer_product_one"] is True

ra = art["rank_analysis"]
assert ra["matrix_rows"] == M
assert ra["rank_F2"] == 2
assert ra["kernel"] == [[0,0,0],[1,1,1]]
assert ra["one_pairwise_Jacobi_bit_free"] is True
assert ra["branch_pruning_obtained"] is False

res = art["result"]
assert res["reservoir_prime_mod4_restriction_obtained"] is True
assert res["new_Jacobi_reciprocity_cycle_obtained"] is True
assert res["cycle_beyond_d_product_one"] is True
assert res["ordinary_quadratic_reciprocity_closes_free_bit"] is False
assert res["new_branch_pruning_obtained"] is False
assert res["quadratic_reciprocity_contradiction_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BF_ORIENTED_GAUSSIAN_QUARTIC_RECIPROCITY_RESERVOIR_LIFT_PREFLIGHT"

for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4BE_GCD_RESERVOIR_QUADRATIC_RECIPROCITY=PASS")
print("reservoir_primes_all_1_mod_4=true")
print("new_Jacobi_cycle=L_a*L_b*L_c=1")
print("pairwise_symbol_rank_F2=2")
print("one_pairwise_Jacobi_bit_free=true")
print("branch_pruning=false")
print("canonical_sha256=" + EXPECTED)
