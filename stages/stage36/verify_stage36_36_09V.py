#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09V" / "gaussian-directional-prime-support-preflight.json"
U_CERT = ROOT / "stages" / "stage36" / "36-09U" / "qi-antiinvariant-rankjump-descent-preflight.json"
U_VERIFIER = ROOT / "stages" / "stage36" / "verify_stage36_36_09U.py"
CYCLE = ROOT / "docs" / "research-os" / "policies" / "cycle-exploration-safety-protocol.md"

BASE = "f8522bd1a38fa551186ad370f51d17c73c7927e2"
U_HEAD = "dfbd0ddff789b9e1a6f3b8033e553fd3d7bd56b4"
U_CERT_BLOB = "a1f0c924d267ab4f45aaada6c9bcb3a5f544f284"
U_VERIFIER_BLOB = "21b3b1461195cfae1a1294832f8e77f09a09983b"
CERT_BLOB = "9fdec16f920104cc6c1961fb092185a0371258d5"
CYCLE_BLOB = "4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


# Sparse Z[a,b] polynomials keyed by (deg_a, deg_b).
def padd(x: dict[tuple[int, int], int], y: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    z = dict(x)
    for k, v in y.items():
        z[k] = z.get(k, 0) + v
        if z[k] == 0:
            del z[k]
    return z


def pscale(x: dict[tuple[int, int], int], c: int) -> dict[tuple[int, int], int]:
    return {k: c * v for k, v in x.items() if c * v}


def pmul(x: dict[tuple[int, int], int], y: dict[tuple[int, int], int]) -> dict[tuple[int, int], int]:
    z: dict[tuple[int, int], int] = {}
    for (i, j), u in x.items():
        for (k, l), v in y.items():
            key = (i + k, j + l)
            z[key] = z.get(key, 0) + u * v
    return {k: v for k, v in z.items() if v}


def ppow(x: dict[tuple[int, int], int], n: int) -> dict[tuple[int, int], int]:
    z = {(0, 0): 1}
    for _ in range(n):
        z = pmul(z, x)
    return z


def gmul(z1, z2):
    a, b = z1
    c, d = z2
    return padd(pmul(a, c), pscale(pmul(b, d), -1)), padd(pmul(a, d), pmul(b, c))


# Univariate integer resultant via Sylvester matrix + Bareiss determinant.
def trim(p: list[int]) -> list[int]:
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def det_bareiss(M: list[list[int]]) -> int:
    A = [row[:] for row in M]
    n = len(A)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            swap = next((r for r in range(k + 1, n) if A[r][k] != 0), None)
            if swap is None:
                return 0
            A[k], A[swap] = A[swap], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) // prev
        prev = pivot
    return sign * A[-1][-1]


def resultant(f: list[int], g: list[int]) -> int:
    f = trim(f[:])
    g = trim(g[:])
    m, n = len(f) - 1, len(g) - 1
    F = list(reversed(f))
    G = list(reversed(g))
    N = m + n
    M = [[0] * N for _ in range(N)]
    for row in range(n):
        for j, c in enumerate(F):
            M[row][row + j] = c
    for row in range(m):
        for j, c in enumerate(G):
            M[n + row][row + j] = c
    return det_bareiss(M)


def only_two_power(n: int) -> bool:
    n = abs(n)
    if n == 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(U_CERT) == U_CERT_BLOB
    assert blob(U_VERIFIER) == U_VERIFIER_BLOB
    assert blob(CYCLE) == CYCLE_BLOB
    assert git("merge-base", "--is-ancestor", BASE, "HEAD") == ""
    assert git("rev-parse", f"{U_HEAD}:stages/stage36/36-09U/qi-antiinvariant-rankjump-descent-preflight.json") == U_CERT_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09V_GAUSSIAN_DIRECTIONAL_PRIME_SUPPORT_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert c["batch_parent"]["pr"] == 1664
    assert c["batch_parent"]["36_09U_exact_head"] == U_HEAD
    assert c["batch_parent"]["36_09U_certificate_blob_sha"] == U_CERT_BLOB
    assert c["batch_parent"]["36_09U_verifier_blob_sha"] == U_VERIFIER_BLOB

    a = {(1, 0): 1}
    b = {(0, 1): 1}
    a2, b2 = ppow(a, 2), ppow(b, 2)
    ab = pmul(a, b)
    aminus = padd(padd(a2, pscale(ab, -2)), pscale(b2, -1))
    aplus = padd(padd(a2, pscale(ab, 2)), pscale(b2, -1))
    C0 = padd(padd(ppow(a, 4), pscale(pmul(a2, b2), -6)), ppow(b, 4))
    D0 = pmul(pmul(a, b), pmul(padd(a, pscale(b, -1)), padd(a, b)))
    norm = padd(a2, b2)

    assert pmul(aminus, aplus) == C0
    z2 = gmul((a, b), (a, b))
    z4 = gmul(z2, z2)
    assert z4[0] == C0
    assert z4[1] == pscale(D0, 4)
    assert padd(ppow(C0, 2), pscale(ppow(D0, 2), 16)) == ppow(norm, 4)

    # Pairwise odd disjointness on the affine chart b != 0. Coefficients low-to-high.
    affine = {
        "a": [0, 1],
        "a-b": [-1, 1],
        "a+b": [1, 1],
        "Aminus": [-1, -2, 1],
        "Aplus": [-1, 2, 1],
    }
    results = {}
    keys = list(affine)
    for i, k1 in enumerate(keys):
        for k2 in keys[i + 1:]:
            R = resultant(affine[k1], affine[k2])
            results[(k1, k2)] = R
            assert only_two_power(R)
    assert results[("Aminus", "Aplus")] == -16
    # The projective b=0 direction is disjoint from all other reservoirs at odd primes
    # because every other homogeneous factor has leading coefficient 1 in a.

    part = c["odd_prime_reservoir_partition"]
    assert part["pairwise_odd_disjoint"] is True
    assert part["Aminus_Aplus_resultant"] == -16
    assert len(part["reservoirs"]) == 6

    gauss = c["gaussian_direction_adapter"]
    assert gauss["beta_equivalence"] == "q divides D0 iff u_q^4=1"
    assert gauss["alpha_equivalence"] == "q divides C0 iff u_q^4=-1"
    assert gauss["beta_exact_directions"] == {
        "q|b": "u_q=1",
        "q|a": "u_q=-1",
        "q|(a-b)": "u_q=i",
        "q|(a+b)": "u_q=-i",
    }
    assert gauss["alpha_extra_residue_identity"] == "2=((a^2+b^2)/(2*a*b))^2 mod q"

    # Exact finite-S obstruction: for every odd prime ell, (a,b)=(ell,1).
    # D0=ell*(ell-1)*(ell+1), while C0=ell^4-6ell^2+1 == 1 (mod ell).
    fs = c["finite_S_obstruction"]
    assert fs["uniform_fixed_finite_rational_prime_support_recovered"] is False
    assert fs["witness_family"] == "for every odd prime ell choose (a,b)=(ell,1), hence p=ell is retained"
    # Direction is B0 because a == 0 modulo ell, hence u=(i)/(-i)=-1.
    assert "u_ell=-1" in fs["witness_calculation"][2]

    dc = c["descent_consequence"]
    assert dc["directional_label_count"] == 6
    assert dc["prime_identity_still_variable_inside_direction"] is True
    assert dc["direction_vector_determines_Q_squareclass"] is False
    assert dc["candidate_set_shrunk"] is False
    assert dc["Qi_rankjump_locus_empty"] is False

    route = c["cycle_route_result"]
    assert route["CYCLE_ROUTE_STATUS"] == "BLOCKED_NEW_PATTERN_ISOLATED"
    assert route["C2_GAUSSIAN_NORM_COMPRESSION"].startswith("BLOCKED_AS_FIXED_FINITE_S_COMPRESSION")
    assert route["B11_DIRECT_MULTIPLACE_ADELIC_RECIPROCITY"] == "LIVE_SELECTED_VARIABLE_PRIME_SIX_RESERVOIR_ATTACK"
    assert route["split_triggered"] is False
    assert c["next_leaf"] == "36-09W_VARIABLE_PRIME_SIX_RESERVOIR_RECIPROCITY_PREFLIGHT"

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V56_36_09V_BATCHED"
    assert st["status"] == "ACTIVE_BATCHING_SUBSTANTIVE_PR"
    assert st["base_main_sha"] == BASE
    v = st["authority_frontier"]["36-09V"]
    assert v["certificate_blob_sha"] == CERT_BLOB
    assert v["verifier_blob_sha"] == blob(Path(__file__))
    assert v["SIX_RESERVOIR_DIRECTIONAL_PARTITION"] is True
    assert v["FIXED_FINITE_S_RECOVERED"] is False
    assert v["BETA_SINGLE_DIRECTION_CARRIES_ARBITRARY_ODD_PRIMES"] is True
    assert v["C2_FIXED_FINITE_S_COMPRESSION_BLOCKED"] is True
    assert v["B11_SELECTED_NEXT"] is True
    assert v["CANDIDATE_SET_SHRUNK"] is False
    assert v["QI_RANKJUMP_LOCUS_EMPTY"] is False
    assert st["current"]["unit"] == "36-09W"
    assert st["current"]["next_exact_leaf"] == "36-09W_VARIABLE_PRIME_SIX_RESERVOIR_RECIPROCITY_PREFLIGHT"
    assert st["current"]["36_09W_entry_allowed"] is True
    assert st["current"]["hostile_audit_checkpoint_reached"] is False
    assert st["promotion_gates"]["36_09V_hostile_audit_passed"] is False
    assert st["promotion_gates"]["multiplace_reciprocity_obstruction_proved"] is False
    assert st["promotion_gates"]["receiver_emptiness_proved"] is False
    assert st["claims"]["candidate_set_shrunk"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09V six-reservoir Gaussian directional partition verified; fixed finite-S compression blocked; B11 variable-prime reciprocity selected; audit deferred")


if __name__ == "__main__":
    main()
