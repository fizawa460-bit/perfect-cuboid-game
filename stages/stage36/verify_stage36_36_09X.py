#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / 'stages' / 'stage36' / '36-09X' / 'kummer-class-coupled-hilbert-local-solvability-preflight.json'
W_CERT = ROOT / 'stages' / 'stage36' / '36-09W' / 'variable-prime-six-reservoir-reciprocity-preflight.json'
W_VERIFIER = ROOT / 'stages' / 'stage36' / 'verify_stage36_36_09W.py'
V_CERT = ROOT / 'stages' / 'stage36' / '36-09V' / 'gaussian-directional-prime-support-preflight.json'
U_CERT = ROOT / 'stages' / 'stage36' / '36-09U' / 'qi-antiinvariant-rankjump-descent-preflight.json'
DESCENT = ROOT / 'stages' / 'stage36' / '36-09N' / 'relative-2isogeny-specialization-source-lock.md'
HILBERT = ROOT / 'stages' / 'stage36' / '36-09W' / 'hilbert-reciprocity-source-lock.md'
QR = ROOT / 'stages' / 'stage36' / '36-09X' / 'quadratic-character-supplement-source-lock.md'
STATE = ROOT / 'stages' / 'stage36' / 'MAIN-STATE.json'

BASE='f8522bd1a38fa551186ad370f51d17c73c7927e2'
W_HEAD='84a60e2c74b90eb51c55cf871ad1305e0684e548'
CERT_BLOB='3eb6e42b563ee2b5042917467a62e7606f27a869'
W_CERT_BLOB='ddeed22ffdad51e6ba409396f82026680c46e8ab'
W_VERIFIER_BLOB='20ae2258443828004971a006842f467f29dc56ea'
V_CERT_BLOB='9fdec16f920104cc6c1961fb092185a0371258d5'
U_CERT_BLOB='a1f0c924d267ab4f45aaada6c9bcb3a5f544f284'
DESCENT_BLOB='a562d7053a6f04deff4473067777b7cfd538ea8a'
HILBERT_BLOB='52952e2afd1db636a236c6bd254acadc779fe09f'
QR_BLOB='89f3847397b5a2b8e4df2fb4762a3dfb5f362616'


def git(*args:str)->str:
    return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def C0(a:int,b:int)->int:
    return a**4-6*a*a*b*b+b**4

def D0(a:int,b:int)->int:
    return a*b*(a-b)*(a+b)

def S(a:int,b:int)->int:
    return a*a+b*b

def aminus(a:int,b:int)->int:
    return a*a-2*a*b-b*b

def aplus(a:int,b:int)->int:
    return a*a+2*a*b-b*b

def legendre(x:int,q:int)->int:
    r=pow(x%q,(q-1)//2,q)
    return 1 if r==1 else (-1 if r==q-1 else 0)

def main()->None:
    assert blob(CERT)==CERT_BLOB
    assert blob(W_CERT)==W_CERT_BLOB
    assert blob(W_VERIFIER)==W_VERIFIER_BLOB
    assert blob(V_CERT)==V_CERT_BLOB
    assert blob(U_CERT)==U_CERT_BLOB
    assert blob(DESCENT)==DESCENT_BLOB
    assert blob(HILBERT)==HILBERT_BLOB
    assert blob(QR)==QR_BLOB
    assert git('merge-base','--is-ancestor',BASE,'HEAD')==''
    assert git('rev-parse',f'{W_HEAD}:stages/stage36/36-09W/variable-prime-six-reservoir-reciprocity-preflight.json')==W_CERT_BLOB
    assert git('rev-parse',f'{W_HEAD}:stages/stage36/verify_stage36_36_09W.py')==W_VERIFIER_BLOB

    c=json.loads(CERT.read_text())
    assert c['schema']=='STAGE36_36_09X_KUMMER_CLASS_COUPLED_HILBERT_LOCAL_SOLVABILITY_PREFLIGHT_V1'
    assert c['base_main_sha']==BASE
    assert c['batch_parent']['36_09W_exact_head']==W_HEAD

    # Homogenization identities.
    for a in range(-8,9):
        for b in range(-8,9):
            assert C0(a,b)==aminus(a,b)*aplus(a,b)
            assert C0(a,b)**2+16*D0(a,b)**2==S(a,b)**4

    # Selected-alpha valuation trichotomy. m=v_q(C0)>=1 and t=v_q(z).
    # For t<0 the d*z^4 term is the unique minimum and has odd valuation.
    # For t>=0 the first term lies above the middle; middle (even) and last
    # (odd) never tie. If last wins it is impossible; if middle wins the
    # residue condition is exactly (-2/q)=+1.
    for m in range(1,9):
        for t in range(-8,9):
            va=1+4*t; vm=2*t; vc=2*m-1
            if t<0:
                assert va<vm and va<vc and va%2!=0
            else:
                assert vm<va
                assert vm!=vc
                if vc<vm:
                    assert vc%2!=0
                else:
                    assert vm<vc and vm%2==0

    primes=[3,5,7,11,13,17,19,23,29,31,41,47,73,79,89,97]
    # Supplementary-character intersection: (2/q)=(-2/q)=1 iff q=1 mod 8.
    for q in primes:
        lhs=(legendre(2,q)==1 and legendre(-2,q)==1)
        assert lhs==(q%8==1)

    # Exact residue-level replay on primitive projective pairs.
    for q in primes:
        for a in range(q):
            for b in range(q):
                if a==0 and b==0 or math.gcd(math.gcd(a,b),q)!=1:
                    continue
                ss=S(a,b)%q
                if C0(a,b)%q==0:
                    assert ss!=0
                    # V's Gaussian identity forces 2 to be a square at alpha primes.
                    assert legendre(2,q)==1
                    # z=1 alpha reduction is w^2=-2*S^2.
                    alpha_simple_root_exists=(legendre((-2*ss*ss)%q,q)==1)
                    assert alpha_simple_root_exists==(q%8==1)
                if D0(a,b)%q==0 and C0(a,b)%q!=0:
                    assert ss!=0
                    # z=1 beta reduction is w^2=4*S^2, always a nonzero square.
                    assert legendre((4*ss*ss)%q,q)==1

    # Explicit alpha blocked/allowed local witnesses.
    assert aminus(4,1)==7 and 7%8==7 and legendre(-2,7)==-1
    assert aplus(5,1)==34 and 17%8==1 and legendre(-2,17)==1

    A=c['selected_alpha_prime_lemma']
    assert A['necessary_condition']=='(-2/q)=+1'
    assert A['exact_selected_prime_equivalence']=='alpha cover has a Q_q-point iff (-2/q)=+1'
    G=c['alpha_gaussian_combination']
    assert G['equivalent_congruence']=='q=1 mod 8'
    assert G['alpha_selected_support_pruned'] is True
    assert G['alpha_growth_excluded'] is False
    B=c['selected_beta_prime_lemma']
    assert B['selected_beta_selfplace_character_restriction'] is False
    assert B['beta_growth_excluded'] is False
    R=c['receiver_sensitive_reciprocity_status']
    assert R['Kummer_class_has_entered_local_analysis'] is True
    assert R['global_Hilbert_contradiction_from_selected_primes_alone'] is False
    assert R['multiplace_reciprocity_obstruction_proved'] is False
    assert R['candidate_parameter_set_shrunk'] is False
    assert R['Kummer_candidate_support_pruned'] is True
    assert c['next_leaf']=='36-09Y_KUMMER_COMPLEMENT_PRIME_AND_2ADIC_HILBERT_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V58_36_09X_BATCHED'
    assert st['base_main_sha']==BASE
    x=st['authority_frontier']['36-09X']
    assert x['certificate_blob_sha']==CERT_BLOB
    assert x['ALPHA_SELECTED_Q_MOD8_FILTER']=='q=1 mod 8'
    assert x['ALPHA_KUMMER_SUPPORT_PRUNED'] is True
    assert x['BETA_SELECTED_SELFPLACE_AUTOMATIC'] is True
    assert x['GLOBAL_HILBERT_OBSTRUCTION_PROVED'] is False
    assert x['CANDIDATE_PARAMETER_SET_SHRUNK'] is False
    assert st['current']['unit']=='36-09Y'
    assert st['current']['36_09Y_entry_allowed'] is True
    assert st['promotion_gates']['36_09X_hostile_audit_passed'] is False
    assert st['promotion_gates']['Kummer_class_coupled_Hilbert_obstruction_proved'] is False
    assert st['claims']['receiver_emptiness_proved'] is False
    assert st['claims']['perfect_cuboid_nonexistence_claim'] is False
    print('36-09X selected-prime Kummer local solvability verified: alpha q=1 mod8 filter, beta self-place neutral; 36-09Y unlocked')

if __name__=='__main__':
    main()
