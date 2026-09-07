#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AT/odd-localrow-monsky-equivalence-even-transpose-gap-preflight.json"
AS = ROOT / "stages/stage36/36-09AS/all-parity-monsky-kernel-equation-compression-preflight.json"
ASV = ROOT / "stages/stage36/verify_stage36_36_09AS.py"
AE = ROOT / "stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json"
AO_SOURCE = ROOT / "stages/stage36/36-09AO/monsky-full2-kernel-source-lock.md"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "ab8fd6b3ff6660188d7d17c89960f02f5bf9eb90"
AS_HEAD = "2ac34f56fa6b63dcbf8ac67b5c46d34857acf9c8"
AS_CI = "34083152458/101622132699"
CERT_BLOB = "b4aaa9447f42ed60d51674bdaaee7ff16162437a"
AS_BLOB = "6b20e9a7d4bb1221feb06622db4d165fb2e3e1ee"
ASV_BLOB = "badc07dbfd0f4fdccf0f1e8f75198d48576c2e40"
AE_BLOB = "ddae37dd35cd0e732cebadf9c17f3f3fa57930df"
AO_SOURCE_BLOB = "9f22dfe19d42d7104d30d219aac1cfd72a67c72a"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def sx(bits) -> int:
    out = 0
    for x in bits: out ^= x
    return out


def rrow(s, target: str, support: set[str]) -> int:
    # R has row-sum diagonal. s[X] is [product of off-target primes in reservoir X / q].
    if target in support:
        return sx(s[x] for x in "ABCD" if x not in support)
    return sx(s[x] for x in support)


def ae_rows(target: str, eta: int, e: int, f: int, s, minus1: int, two: int):
    # additive form of the exact selected-prime rows in 36-09AE
    sign_minus_eta = minus1 if eta == 1 else 0  # [-eta/q]
    sign_eta = minus1 if eta == -1 else 0       # [eta/q]
    if target == "A":
        return sign_minus_eta ^ (e & two) ^ s["B"] ^ s["C"], (f & two) ^ s["B"] ^ s["D"]
    if target == "B":
        return sign_eta ^ (e & two) ^ s["A"] ^ s["C"], (f & two) ^ s["A"] ^ s["D"]
    if target == "C":
        return s["A"] ^ s["B"], ((1-f) & two) ^ s["A"] ^ s["D"]
    assert target == "D"
    return minus1 ^ s["A"] ^ s["B"], sign_eta ^ ((1-e) & two) ^ s["A"] ^ s["C"]


def odd_supports(eta: int, t: int):
    if eta == -1 and t == 0: return {"B","C"}, {"B","D"}
    if eta == -1 and t == 1: return {"A","D"}, {"B","D"}
    if eta == 1 and t == 0: return {"A","C"}, {"A","D"}
    assert eta == 1 and t == 1
    return {"B","D"}, {"A","D"}


def odd_monsky_local(target: str, eta: int, t: int, s, minus1: int, two: int):
    x,y = odd_supports(eta,t)
    xi = int(target in x)
    yi = int(target in y)
    delta_i = xi ^ yi
    m1 = rrow(s,target,x) ^ (two & delta_i)
    m2 = rrow(s,target,y) ^ (two & delta_i) ^ (minus1 & yi)
    return m1,m2


def even_y(eta: int, e: int, f: int):
    if (eta,e,f)==(1,0,1): return {"B","D"}
    if (eta,e,f)==(1,1,0): return {"A","C"}
    if (eta,e,f)==(-1,0,1): return {"A","D"}
    assert (eta,e,f)==(-1,1,0)
    return {"B","C"}


def even_second_local(target: str, eta: int, e: int, f: int, s, two: int):
    x={"A","B"}
    y=even_y(eta,e,f)
    z_i=int(target in x) ^ int(target in y)
    return rrow(s,target,y) ^ (two & z_i)


def transform(eta: int, target: str, r1: int, r2: int):
    if eta == -1:
        table={
            "A":(r1,r2),
            "B":(r2,r1),
            "C":(r2,r1^r2),
            "D":(r1^r2,r2),
        }
    else:
        table={
            "A":(r2,r1),
            "B":(r1,r2),
            "C":(r1^r2,r2),
            "D":(r2,r1^r2),
        }
    return table[target]


def even_second_transform(eta: int, target: str, r1: int, r2: int):
    if eta == -1:
        return {"A":r1,"B":r2,"C":r2,"D":r1^r2}[target]
    return {"A":r2,"B":r1,"C":r1^r2,"D":r2}[target]


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(AS) == AS_BLOB
    assert blob(ASV) == ASV_BLOB
    assert blob(AE) == AE_BLOB
    assert blob(AO_SOURCE) == AO_SOURCE_BLOB
    subprocess.check_call(["git","merge-base","--is-ancestor",BASE,"HEAD"], cwd=ROOT)
    subprocess.check_call(["git","merge-base","--is-ancestor",AS_HEAD,"HEAD"], cwd=ROOT)
    assert git("rev-parse",f"{AS_HEAD}:stages/stage36/36-09AS/all-parity-monsky-kernel-equation-compression-preflight.json") == AS_BLOB

    c=json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AT_ODD_LOCALROW_MONSKY_EQUIVALENCE_EVEN_TRANSPOSE_GAP_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert c["batch_parent"]["36_09AS_exact_head"] == AS_HEAD
    assert c["batch_parent"]["36_09AS_exact_head_ci"] == AS_CI

    # Formal local identity: exhaust all six independent local bits
    # sA,sB,sC,sD,[-1/q],[2/q]. No reciprocity assumption is needed on odd N.
    for vals in itertools.product((0,1), repeat=6):
        s=dict(zip("ABCD", vals[:4]))
        minus1,two=vals[4],vals[5]
        for eta in (-1,1):
            for t in (0,1):
                for target in "ABCD":
                    r1,r2=ae_rows(target,eta,t,t,s,minus1,two)
                    m=odd_monsky_local(target,eta,t,s,minus1,two)
                    assert m == transform(eta,target,r1,r2)
                    # Every listed transform is invertible: zero iff zero.
                    assert (m==(0,0)) == ((r1,r2)==(0,0))

        # Even second block: exact pointwise identification, independent of e/f choice.
        for eta in (-1,1):
            for e,f in ((0,1),(1,0)):
                for target in "ABCD":
                    r1,r2=ae_rows(target,eta,e,f,s,minus1,two)
                    m2=even_second_local(target,eta,e,f,s,two)
                    assert m2 == even_second_transform(eta,target,r1,r2)

    odd=c["odd_exact_local_change_of_basis"]
    assert odd["independent_of_t_e_equals_f"] is True
    assert odd["each_2x2_map_invertible_over_F2"] is True
    assert c["odd_route_classification"]["Monsky_gate_adds_new_filter_after_AE_selected_prime_rows"] is False
    assert c["odd_route_classification"]["Monsky_gate_is_exact_repackaging_of_AE_selected_prime_rows"] is True
    even=c["even_partial_local_identification"]
    assert even["independent_of_ef_choice"] is True
    assert even["pointwise_AE_localrow_basis_change_for_first_block_obtained"] is False
    assert "R^T*x" in even["first_Monsky_block_contains"]
    interp=c["interpretation"]
    assert interp["odd_Monsky_gate_redundancy_exact"] is True
    assert interp["even_second_block_redundancy_exact"] is True
    assert interp["even_first_block_reciprocity_bridge_needed"] is True
    assert interp["candidate_parameter_set_shrunk"] is False
    assert interp["receiver_closed"] is False

    st=json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V82_36_09AT_CANDIDATE"
    at=st["authority_frontier"]["36-09AT"]
    assert at["ODD_AE_MONSKY_EXACT_EQUIVALENCE"] is True
    assert at["ODD_MONSKY_GATE_NEW_AFTER_AE"] is False
    assert at["EVEN_SECOND_BLOCK_AE_EQUIVALENCE"] is True
    assert at["EVEN_FIRST_TRANSPOSED_REDEI_BRIDGE"] is False
    assert at["RECEIVER_CLOSED"] is False
    assert st["current"]["unit"] == "36-09AU"
    assert st["current"]["36_09AU_entry_allowed"] is True
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False

    print("36-09AT verified: on odd N the AE selected-prime row pair and Monsky residual pair are related at every q by an explicit invertible F2 change of basis, independent of t; on even N the second block is likewise a local AE combination, while the transposed-Redei first block remains the exact reciprocity gap; no parameter shrink or receiver closure; AU unlocked")

if __name__ == "__main__":
    main()
