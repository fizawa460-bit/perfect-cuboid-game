#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AU/even-transposed-redei-stage36-equivalence-close-preflight.json"
AT = ROOT / "stages/stage36/36-09AT/odd-localrow-monsky-equivalence-even-transpose-gap-preflight.json"
ATV = ROOT / "stages/stage36/verify_stage36_36_09AT.py"
AE = ROOT / "stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json"
V = ROOT / "stages/stage36/36-09V/gaussian-directional-prime-support-preflight.json"
AO_SOURCE = ROOT / "stages/stage36/36-09AO/monsky-full2-kernel-source-lock.md"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "600eb3032d44d35cdc067a060f6e58f2ed18d16b"
AT_HEAD = "b798b4d5a5d8ac134f7831d8be7f25a4b060debc"
AT_CI = "34083474078/101623014316"
CERT_BLOB = "ae4572d4131464a8aca83d39e2faefbd4ffec18e"
AT_BLOB = "b4aaa9447f42ed60d51674bdaaee7ff16162437a"
ATV_BLOB = "62e3c992623284258c7b6e127f5ef2472757cda6"
AE_BLOB = "ddae37dd35cd0e732cebadf9c17f3f3fa57930df"
V_BLOB = "9fdec16f920104cc6c1961fb092185a0371258d5"
AO_SOURCE_BLOB = "9f22dfe19d42d7104d30d219aac1cfd72a67c72a"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def sx(bits) -> int:
    out=0
    for x in bits: out ^= x
    return out


def rrow(s, target: str, support: set[str]) -> int:
    if target in support:
        return sx(s[x] for x in "ABCD" if x not in support)
    return sx(s[x] for x in support)


def ae_rows(target: str, eta: int, e: int, f: int, s, minus1: int, two: int):
    minus_eta = minus1 if eta == 1 else 0
    eta_sign = minus1 if eta == -1 else 0
    if target == "A":
        return minus_eta ^ (e & two) ^ s["B"] ^ s["C"], (f & two) ^ s["B"] ^ s["D"]
    if target == "B":
        return eta_sign ^ (e & two) ^ s["A"] ^ s["C"], (f & two) ^ s["A"] ^ s["D"]
    if target == "C":
        return s["A"] ^ s["B"], ((1-f) & two) ^ s["A"] ^ s["D"]
    assert target == "D"
    return minus1 ^ s["A"] ^ s["B"], eta_sign ^ ((1-e) & two) ^ s["A"] ^ s["C"]


def even_y(eta: int, e: int, f: int):
    return {
        (1,0,1): {"B","D"},
        (1,1,0): {"A","C"},
        (-1,0,1): {"A","D"},
        (-1,1,0): {"B","C"},
    }[(eta,e,f)]


def first_reciprocity_rewrite(target: str, eta: int, e: int, f: int, s, minus1: int, two: int, global_s: int):
    x={"A","B"}
    y=even_y(eta,e,f)
    xi=int(target in x)
    yi=int(target in y)
    zi=xi^yi
    return rrow(s,target,x) ^ (two & xi) ^ (minus1 & zi) ^ (minus1 & global_s)


def second_local(target: str, eta: int, e: int, f: int, s, two: int):
    x={"A","B"}; y=even_y(eta,e,f)
    zi=int(target in x)^int(target in y)
    return rrow(s,target,y) ^ (two & zi)


def second_from_rows(target: str, eta: int, r1: int, r2: int):
    if eta == -1:
        return {"A":r1,"B":r2,"C":r2,"D":r1^r2}[target]
    return {"A":r2,"B":r1,"C":r1^r2,"D":r2}[target]


def final_pair(target: str, eta: int, r1: int, r2: int):
    m1 = (r1 ^ r2) if target in "AB" else r1
    return m1, second_from_rows(target,eta,r1,r2)


def det2_from_images(target: str, eta: int) -> int:
    a=final_pair(target,eta,1,0)
    b=final_pair(target,eta,0,1)
    return (a[0]&b[1]) ^ (a[1]&b[0])


def add_symbol(a: int, p: int) -> int:
    a%=p
    assert a
    t=pow(a,(p-1)//2,p)
    if t==1: return 0
    assert t==p-1
    return 1


def redei(primes):
    k=len(primes); R=[[0]*k for _ in range(k)]
    for i,p in enumerate(primes):
        row=0
        for j,q in enumerate(primes):
            if i==j: continue
            R[i][j]=add_symbol(q,p); row^=R[i][j]
        R[i][i]=row
    return R


def main() -> None:
    assert blob(CERT)==CERT_BLOB
    assert blob(AT)==AT_BLOB
    assert blob(ATV)==ATV_BLOB
    assert blob(AE)==AE_BLOB
    assert blob(V)==V_BLOB
    assert blob(AO_SOURCE)==AO_SOURCE_BLOB
    subprocess.check_call(["git","merge-base","--is-ancestor",BASE,"HEAD"], cwd=ROOT)
    subprocess.check_call(["git","merge-base","--is-ancestor",AT_HEAD,"HEAD"], cwd=ROOT)
    assert git("rev-parse",f"{AT_HEAD}:stages/stage36/36-09AT/odd-localrow-monsky-equivalence-even-transpose-gap-preflight.json")==AT_BLOB

    c=json.loads(CERT.read_text())
    assert c["schema"]=="STAGE36_36_09AU_EVEN_TRANSPOSED_REDEI_STAGE36_EQUIVALENCE_CLOSE_PREFLIGHT_V1"
    assert c["base_main_sha"]==BASE
    assert c["freshness_sync"]["sync_merge_commit"]=="ba633a560ed0fdc9f27d0e8450ddd62de40058e0"
    assert c["freshness_sync"]["stage36_source_drift"] is False
    assert c["batch_parent"]["36_09AT_exact_head"]==AT_HEAD
    assert c["batch_parent"]["36_09AT_exact_head_ci"]==AT_CI

    for primes in ([3,5,7,11],[13,17,19,23],[31,37,41,43],[73,89,97,113]):
        R=redei(primes); k=len(primes)
        eps=[add_symbol(-1,p) for p in primes]
        for i in range(k):
            for j in range(k):
                rhs=R[i][j] ^ (eps[i]&eps[j]) ^ (eps[i] if i==j else 0)
                assert R[j][i]==rhs

    for vals in itertools.product((0,1), repeat=7):
        local=dict(zip("ABCD",vals[:4]))
        minus1,two,global_s=vals[4:]
        for eta in (-1,1):
            for e,f in ((0,1),(1,0)):
                for target in "ABCD":
                    r1,r2=ae_rows(target,eta,e,f,local,minus1,two)
                    first=first_reciprocity_rewrite(target,eta,e,f,local,minus1,two,global_s)
                    base=(r1^r2) if target in "AB" else r1
                    assert first == (base ^ (minus1 & (global_s ^ e)))
                    second=second_local(target,eta,e,f,local,two)
                    assert second == second_from_rows(target,eta,r1,r2)

    for a7,b7 in itertools.product((0,1), repeat=2):
        A8=7 if a7 else 1
        B8=7 if b7 else 1
        global_s=a7^b7
        same=(A8==B8)
        assert same == (global_s==0)
        e=0 if same else 1
        f=1-e
        assert (e,f) in ((0,1),(1,0))
        assert global_s==e

    for eta in (-1,1):
        for target in "ABCD":
            assert det2_from_images(target,eta)==1
            for r1,r2 in itertools.product((0,1), repeat=2):
                m=final_pair(target,eta,r1,r2)
                assert (m==(0,0)) == ((r1,r2)==(0,0))

    ae=json.loads(AE.read_text())
    alpha=ae["alpha_two_residue_input"]
    assert "every odd q dividing C0=M*P has (2/q)=+1" in alpha["audited_36_09V_fact"]
    uv=ae["UV_two_adic_compatibility"]
    assert uv["combined_rule"]=="for A=B, (e,f)=(1,0) is impossible; for A!=B, (e,f)=(0,1) is impossible"

    allp=c["all_parity_conclusion"]
    assert allp["odd_equivalence_from_AT"] is True
    assert allp["even_equivalence_from_AU"] is True
    assert allp["AE_selected_prime_rows_iff_stage36_Monsky_kernel_all_parities"] is True
    assert allp["Monsky_gate_adds_new_receiver_filter_after_AE"] is False
    assert allp["Tunnell_gate_remains_new_and_independent"] is True
    assert allp["candidate_parameter_set_shrunk_by_AU"] is False
    assert allp["receiver_closed"] is False

    st=json.loads(STATE.read_text())
    assert st["schema"]=="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V83_36_09AU_AUDIT_CHECKPOINT"
    assert st["status"]=="ACTIVE_BATCH_HOSTILE_AUDIT_CHECKPOINT"
    au=st["authority_frontier"]["36-09AU"]
    assert au["ALL_PARITY_AE_MONSKY_EXACT_EQUIVALENCE"] is True
    assert au["MONSKY_NEW_FILTER_AFTER_AE"] is False
    assert au["TUNNELL_ONLY_NEW_GLOBAL_GATE_IN_AP_AU"] is True
    assert au["CANDIDATE_PARAMETER_SET_SHRUNK"] is False
    assert au["RECEIVER_CLOSED"] is False
    assert st["current"]["unit"]=="36-09AU-AUDIT-CHECKPOINT"
    assert st["current"]["next_owner"]=="HOSTILE_AUDIT"
    assert st["current"]["hostile_audit_checkpoint_reached"] is True
    assert st["current"]["36_09AV_entry_allowed"] is False
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False

    print("36-09AU verified: quadratic reciprocity rewrites the even transposed-Redei block; Stage36 alpha (2/q)=+1 on A/B plus the audited UV mod8 rule force s=e, after which every even Monsky local pair is an invertible F2 change of basis of the AE selected-prime row pair. Combined with AT, AE local rows iff Stage36 Monsky kernel for all parities. Monsky adds no post-AE receiver filter; Tunnell remains the only new global gate. Batch hostile-audit checkpoint reached; no parameter shrink or receiver closure.")

if __name__=="__main__":
    main()
