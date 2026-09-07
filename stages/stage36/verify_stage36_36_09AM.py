#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AM/uniform-rankzero-tunnell-sha2-sieve-preflight.json"
SOURCE = ROOT / "stages/stage36/36-09AM/tunnell-rankzero-torsion-sector-source-lock.md"
AE = ROOT / "stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json"
AJ = ROOT / "stages/stage36/36-09AJ/congruent-number-full2-covering-class-preflight.json"
AL = ROOT / "stages/stage36/36-09AL/b7-selmer-class-nontrivial-sha2-preflight.json"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "58e81a647b63bcea17ab396409c2813b667f45e2"
AUDITED_HEAD = "56f815b9bc25ca91a2ba6e0c0291664bfeac733d"
AUDIT_REVIEW = 5127436589
AUDIT_CI = "34074355295/101597480228"
CERT_BLOB = "6d9e9392df8fc70a90a356932724e0a589b6b446"
SOURCE_BLOB = "0c64262ac11979fa1f5e25039cfc0f4f0426ca62"
AE_BLOB = "ddae37dd35cd0e732cebadf9c17f3f3fa57930df"
AJ_BLOB = "27950f53a89e28d02d04f2c19628504561c206e7"
AL_BLOB = "10962f8d2471a8236d66a602c0f4952ce497e56c"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def xor(*xs: frozenset[str]) -> frozenset[str]:
    out: set[str] = set()
    for x in xs:
        out.symmetric_difference_update(x)
    return frozenset(out)


def atom(name: str, present: bool) -> frozenset[str]:
    return frozenset({name}) if present else frozenset()


def sector_predicate(Ap: bool, Bp: bool, Cp: bool, Dp: bool, eta: int, e: int, f: int) -> tuple[bool, str | None]:
    if eta == 1 and e == 0 and f == 0 and not Ap and not Cp and not Dp:
        return True, "S0_ETA_PLUS_O"
    if eta == 1 and not Ap and not Bp and not Dp and f == 1:
        return True, "SPLUS_ETA_PLUS_TPLUS"
    if eta == -1 and e == 0 and f == 0 and not Bp and not Cp and not Dp:
        return True, "SZERO_ETA_MINUS_TZERO"
    if eta == -1 and not Ap and not Bp and not Dp and f == 1:
        return True, "SMINUS_ETA_MINUS_TMINUS"
    return False, None


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(AE) == AE_BLOB
    assert blob(AJ) == AJ_BLOB
    assert blob(AL) == AL_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    # The old audited exact head remains an ancestor of this continuation branch,
    # while BASE is the squash-merged main authority produced from that audit.
    subprocess.check_call(["git", "merge-base", "--is-ancestor", AUDITED_HEAD, "HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09AL/b7-selmer-class-nontrivial-sha2-preflight.json") == AL_BLOB
    assert git("rev-parse", f"{AUDITED_HEAD}:stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json") == AE_BLOB
    assert git("rev-parse", f"{BASE}:stages/stage36/36-09AL/b7-selmer-class-nontrivial-sha2-preflight.json") == AL_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AM_UNIFORM_RANKZERO_TUNNELL_SHA2_SIEVE_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    ap = c["audited_parent"]
    assert ap["pr"] == 1677
    assert ap["hostile_audit_review"] == AUDIT_REVIEW
    assert ap["audited_exact_head"] == AUDITED_HEAD
    assert ap["exact_head_ci"] == AUDIT_CI
    assert ap["merged_to_main"] is True
    assert ap["merged_main_sha"] == BASE

    ae = json.loads(AE.read_text())
    props = ae["squareclass_variables"]["properties"]
    assert "A,B,C,D are positive odd squarefree" in props
    assert "pairwise gcd(A,B)=gcd(A,C)=...=1" in props

    two = frozenset({"2"})
    neg = frozenset({"-1"})
    torsion_hits: list[tuple[bool,bool,bool,bool,int,int,int,int]] = []
    sector_hits: list[tuple[bool,bool,bool,bool,int,int,int,str]] = []
    for Ap, Bp, Cp, Dp in itertools.product((False, True), repeat=4):
        A, B, C, D = (atom("A",Ap), atom("B",Bp), atom("C",Cp), atom("D",Dp))
        for eta in (1, -1):
            for e, f in itertools.product((0,1), repeat=2):
                g = (e + f) & 1
                n = xor(A,B,C,D, two if g else frozenset())
                d1 = xor(C,D, two if g else frozenset(), neg if eta < 0 else frozenset())
                if eta > 0:
                    d2 = xor(A,D, two if f else frozenset())
                else:
                    d2 = xor(A,C, two if e else frozenset(), neg)
                pair = (d1,d2)
                torsion = [
                    (frozenset(), frozenset()),
                    (neg, xor(neg,n)),
                    (n, two),
                    (xor(neg,n), xor(neg,two,n)),
                ]
                in_image = pair in torsion
                pred, sid = sector_predicate(Ap,Bp,Cp,Dp,eta,e,f)
                assert in_image == pred, (Ap,Bp,Cp,Dp,eta,e,f,pair,torsion,sid)
                if in_image:
                    torsion_hits.append((Ap,Bp,Cp,Dp,eta,e,f,torsion.index(pair)))
                    assert sid is not None
                    sector_hits.append((Ap,Bp,Cp,Dp,eta,e,f,sid))

    assert len(torsion_hits) == 12
    assert {x[-1] for x in sector_hits} == {
        "S0_ETA_PLUS_O",
        "SPLUS_ETA_PLUS_TPLUS",
        "SZERO_ETA_MINUS_TZERO",
        "SMINUS_ETA_MINUS_TMINUS",
    }

    sectors = {x["id"]: x for x in c["exact_torsion_shaped_sector_union"]}
    assert set(sectors) == {x[-1] for x in sector_hits}
    assert sectors["S0_ETA_PLUS_O"]["conditions"] == ["eta=+1","e=0","f=0","A=1","C=1","D=1"]
    assert sectors["SPLUS_ETA_PLUS_TPLUS"]["conditions"] == ["eta=+1","A=1","B=1","D=1","f=1"]
    assert sectors["SZERO_ETA_MINUS_TZERO"]["conditions"] == ["eta=-1","e=0","f=0","B=1","C=1","D=1"]
    assert sectors["SMINUS_ETA_MINUS_TMINUS"]["conditions"] == ["eta=-1","A=1","B=1","D=1","f=1"]

    rank0 = c["rankzero_MW_mod2_Kummer_image"]
    assert rank0["exhaustive_when_rank_zero"] is True
    assert rank0["pair_classes"] == [["1","1"],["-1","-n"],["n","2"],["-n","-2*n"]]

    sieve = c["conditional_uniform_sieve"]
    assert "the full Stage36 covering is everywhere locally soluble, hence its class lies in Sel^2(E_n/Q)" in sieve["hypotheses"]
    assert "the parity-appropriate Tunnell necessary equality fails" in sieve["hypotheses"]
    assert sieve["Tunnell_equality_branch"] == "unresolved unconditionally; BSD converse is not used"

    out = c["route_result"]
    assert out["uniform_rankzero_Tunnell_fail_classifier_obtained"] is True
    assert out["finite_exception_sector_count"] == 4
    assert out["all_variable_n_classified"] is False
    assert out["candidate_parameter_set_shrunk"] is False
    assert out["receiver_closed"] is False
    assert out["next_leaf"] == "36-09AN_TORSION_SHAPED_SECTOR_RETAINED_OPEN_PREFLIGHT"

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V75_36_09AM_CANDIDATE"
    assert st["base_main_sha"] == BASE
    a = st["audited_batch_promotion"]
    assert a["candidate_pr"] == 1677 and a["hostile_audit_review"] == AUDIT_REVIEW and a["merged_main_sha"] == BASE
    assert st["promotion_gates"]["36_09AJ_hostile_audit_passed"] is True
    assert st["promotion_gates"]["36_09AK_hostile_audit_passed"] is True
    assert st["promotion_gates"]["36_09AL_hostile_audit_passed"] is True
    assert st["promotion_gates"]["36_09AL_promoted_to_main"] is True
    am = st["authority_frontier"]["36-09AM"]
    assert am["UNIFORM_RANKZERO_TUNNELL_FAIL_CLASSIFIER"] is True
    assert am["TORSION_SHAPED_EXCEPTION_SECTOR_COUNT"] == 4
    assert am["TUNNELL_EQUALITY_SIDE_CLASSIFIED"] is False
    assert st["current"]["unit"] == "36-09AN"
    assert st["current"]["36_09AN_entry_allowed"] is True
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AM verified: merged audited PR1677 supplies AJ-AL authority; parity-complete Tunnell failure gives rank zero; exhaustive F2 squareclass comparison leaves exactly four torsion-shaped sectors; every ELS Tunnell-fail branch outside them is nontrivial Sha[2] and has no projective covering Q-point; Tunnell-equality and retained-open torsion sectors remain unresolved; AN unlocked")


if __name__ == "__main__":
    main()
