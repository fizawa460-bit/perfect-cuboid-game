#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AK/b7-everywhere-local-full2-covering-preflight.json"
SOURCE = ROOT / "stages/stage36/36-09AK/local-solvability-source-lock.md"
AJ = ROOT / "stages/stage36/36-09AJ/congruent-number-full2-covering-class-preflight.json"
AH = ROOT / "stages/stage36/36-09AH/common-uv-two-quadric-genusone-preflight.json"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "4e6708cb807cc37bea6509245447a5817965256f"
AJ_HEAD = "3a808af3404c7d57add3c4dca120b9d1696aa46e"
AJ_CI = "34073432508"
CERT_BLOB = "05bf95344372b362be47d11df7f930e72fa8ee18"
SOURCE_BLOB = "415962e74eab88748e99ad2265535b4eecdb7da2"
AJ_BLOB = "27950f53a89e28d02d04f2c19628504561c206e7"
AJ_VERIFIER_BLOB = "af5be150ae9b7a07542875fcfc99f9270564b69d"
AH_BLOB = "732431bef8dfafe25cbdeb005c4237d72a40ae4b"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def rank_mod_p(rows: list[list[int]], p: int) -> int:
    a = [[x % p for x in row] for row in rows]
    nr, nc, rank = len(a), len(a[0]), 0
    for col in range(nc):
        pivot = next((i for i in range(rank, nr) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(x * inv) % p for x in a[rank]]
        for i in range(nr):
            if i != rank and a[i][col] % p:
                f = a[i][col] % p
                a[i] = [(a[i][j] - f * a[rank][j]) % p for j in range(nc)]
        rank += 1
        if rank == nr:
            break
    return rank


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(AJ) == AJ_BLOB
    assert blob(AH) == AH_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    subprocess.check_call(["git", "merge-base", "--is-ancestor", AJ_HEAD, "HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{AJ_HEAD}:stages/stage36/36-09AJ/congruent-number-full2-covering-class-preflight.json") == AJ_BLOB
    assert git("rev-parse", f"{AJ_HEAD}:stages/stage36/verify_stage36_36_09AJ.py") == AJ_VERIFIER_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AK_B7_EVERYWHERE_LOCAL_FULL2_COVERING_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    bp = c["batch_parent"]
    assert bp["pr"] == 1677 and bp["36_09AJ_exact_head"] == AJ_HEAD and bp["36_09AJ_exact_head_ci"] == AJ_CI

    b = c["branch"]
    A,B,C,D,eta,e,f = (b[k] for k in ("A","B","C","D","eta","e","f"))
    assert (A,B,C,D,eta,e,f) == (73,7,11,13,-1,1,1)
    cc = eta*(2**e)*C
    dd = (2**f)*D
    assert (cc,dd) == (b["c"],b["d"]) == (-22,26)
    assert A*B*cc*dd == b["raw_T"] == -292292
    assert b["normalized_n"] == 73073
    assert b["AJ_full2_class_representatives"] == [-143,1898,-1606]

    def F(pt: tuple[int,int,int,int]) -> tuple[int,int]:
        u,v,r,s = pt
        return (A*u*u-B*v*v-cc*r*r, A*u*u+B*v*v-dd*s*s)

    bad = c["odd_bad_places"]
    assert bad["primes"] == [7,11,13,73]
    for p in bad["primes"]:
        pt = tuple(bad["explicit_nonsingular_Fp_points"][str(p)])
        f1,f2 = F(pt)
        assert f1 % p == f2 % p == 0
        u,v,r,s = pt
        J = [
            [2*A*u, -2*B*v, -2*cc*r, 0],
            [2*A*u,  2*B*v, 0, -2*dd*s],
        ]
        assert rank_mod_p(J,p) == 2
    assert bad["jacobian_rank_at_each_point"] == 2

    # Exact Q_2 witness: u=1,s=2 forces two odd units, both 1 mod 8.
    v2 = Fraction(31,7)
    r2 = Fraction(-21,11)
    assert A + B*v2 == dd*4
    assert A - B*v2 == cc*r2
    inv7 = pow(7,-1,8); inv11 = pow(11,-1,8)
    assert (31*inv7) % 8 == 1
    assert ((-21)%8*inv11) % 8 == 1
    q2 = c["two_adic_place"]
    assert q2["forced_squares"] == {"v^2":"31/7","r^2":"-21/11"}
    assert q2["unit_residues_mod8"] == {"31/7":1,"-21/11":1}

    # Exact real witness via positive square values.
    rr = Fraction(39,22); ss = Fraction(185,26)
    assert A - B*16 == cc*rr
    assert A + B*16 == dd*ss
    assert rr > 0 and ss > 0
    assert c["real_place"]["forced_positive_squares"] == {"r^2":"39/22","s^2":"185/26"}

    # Good-prime uniformity uses audited AH: p not dividing 2ABCD leaves four
    # distinct pencil roots 0, infinity, +/-1 in odd characteristic.
    assert 2*A*B*C*D == 2*73*7*11*13
    good = c["all_other_odd_places"]
    assert "lambda*mu*(mu^2-lambda^2)" in good["AH_input"]
    assert good["conclusion"] == "Q_p point exists at every good odd prime"

    gl = c["global_local_conclusion"]
    assert gl["covering_everywhere_locally_soluble"] is True
    assert gl["AJ_H1_class_lies_in_2Selmer_of_E73073"] is True
    assert gl["local_obstruction_uniform_closure_possible"] is False
    bd = c["MW_Sha_boundary"]
    assert bd["class_in_Kummer_image_proved"] is False
    assert bd["class_nontrivial_in_Sha2_proved"] is False
    assert bd["rational_point_on_covering_proved"] is False

    out = c["route_result"]
    assert out["route_status"] == "BLOCKED_NEW_PATTERN_ISOLATED"
    assert out["blocked_route"] == "UNIFORM_FULL2_LOCAL_OBSTRUCTION_CLOSURE"
    assert out["new_live_route"] == "B7_SELMER_CLASS_MW_VS_SHA"
    assert out["receiver_closed"] is False

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V73_36_09AK_CANDIDATE"
    assert st["base_main_sha"] == BASE
    ak = st["authority_frontier"]["36-09AK"]
    assert ak["EXPLICIT_B7_COVERING_ELS"] is True
    assert ak["B7_CLASS_IN_2SELMER_E73073"] is True
    assert ak["KUMMER_IMAGE_PROVED"] is False
    assert ak["SHA2_NONTRIVIAL_PROVED"] is False
    assert st["current"]["unit"] == "36-09AL"
    assert st["current"]["36_09AL_entry_allowed"] is True
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AK verified: B=7 branch has Q_v points at 2, infinity, all bad odd primes, and every good odd prime; AJ class survives in Sel^2(E_73073); local-obstruction uniform closure blocked; MW-vs-Sha remains")


if __name__ == "__main__":
    main()
