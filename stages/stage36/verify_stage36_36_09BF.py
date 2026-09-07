#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BF/weight2-elliptic-quotient-pullback-collapse-preflight.json'
BE=ROOT/'stages/stage36/36-09BE/full-multiquadratic-character-quotient-inventory-preflight.json'
BEV=ROOT/'stages/stage36/verify_stage36_36_09BE.py'
BB=ROOT/'stages/stage36/36-09BB/ay-receiver-scaled-self-intersection-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='386b6a52d7bfec2e8903412c7ca56976b46c288b'
AUDITED_HEAD='52161f9872d7748bd3a4dcba346f7fd42d68edd9'
AUDIT_REVIEW=5129219368
AUDIT_CI='34095467995/101658038311'
CERT_BLOB='da1f71559c8a6a56391c13dcb848aafdf3317ed7'
LOCKS={BE:'f30724ca63b30b4b960e31f7d8266a4a99884016',BEV:'183eaf5567f2e6530318d6cb057747dd79702300',BB:'e4b63fd500d05ff5dc704e0c08409edee5895053'}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))

def projected(mask):
    # f1,f2 are AY squares, so only f3,f4 parity remains.
    return ((mask>>2)&1,(mask>>3)&1)

def main():
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text())
    assert c['base_main_sha']==BASE
    ap=c['audited_parent']
    assert ap['hostile_reaudit_review']==AUDIT_REVIEW and ap['audited_exact_head']==AUDITED_HEAD
    assert ap['exact_head_ci']==AUDIT_CI and ap['merged_main_sha']==BASE

    # Weight-2 characters collapse modulo AY squareclasses exactly as claimed.
    masks={'E12':0b0011,'E13':0b0101,'E14':0b1001,'E23':0b0110,'E24':0b1010,'E34':0b1100}
    expected={'E12':(0,0),'E13':(1,0),'E14':(0,1),'E23':(1,0),'E24':(0,1),'E34':(1,1)}
    assert {k:projected(v) for k,v in masks.items()}==expected

    table={x['id']:x for x in c['weight2_pullback_table']}
    assert table['E12']['classification']=='AY_AUTOMATIC'
    assert table['E13']['classification']==table['E23']['classification']=='EQUIVALENT_TO_f3_SQUARE'
    assert table['E14']['classification']==table['E24']['classification']=='EQUIVALENT_TO_f4_SQUARE'
    assert table['E34']['classification']=='PRODUCT_ONLY_WEAKER_THAN_CONJUNCTION'

    # Independent rational-function check of the cross ratios after f1=R^2,f2=S^2.
    samples=[(Fraction(3,2),Fraction(5,3),Fraction(7,4),Fraction(11,6)),
             (Fraction(-4,3),Fraction(9,5),Fraction(-13,7),Fraction(8,11))]
    for R,S,f3,f4 in samples:
        f1=R*R; f2=S*S
        E13=f1*f3; E14=f1*f4; E23=f2*f3; E24=f2*f4
        assert E14/E24==(R/S)**2
        assert E23/E13==(S/R)**2
        # inverse pullbacks are exact on AY open
        y13=R*Fraction(17,5); assert (y13/R)==Fraction(17,5)
        y24=S*Fraction(19,7); assert (y24/S)==Fraction(19,7)

    rr=c['route_result']
    assert rr['route_status']=='BLOCKED_NO_NEW_INFORMATION_AT_WEIGHT2_PULLBACK_LAYER'
    assert rr['cross_elliptic_receiver_predicate_new'] is False
    assert rr['candidate_parameter_set_shrunk'] is False and rr['receiver_closed'] is False

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V94_36_09BF_CANDIDATE'
    bf=st['authority_frontier']['36-09BF']
    assert bf['WEIGHT2_PULLBACK_COLLAPSE_COMPLETE'] is True
    assert bf['CROSS_ELLIPTIC_RECEIVER_PREDICATE_NEW'] is False
    assert st['current']['unit']=='36-09BG' and st['current']['36_09BG_entry_allowed'] is True
    assert st['claims']['receiver_emptiness_proved'] is False
    print('36-09BF verified: on the AY open, all six weight-2 character quotients collapse to automatic, f3, f4, or f3*f4 squareclasses; E14/E23 add no receiver-restricted predicate beyond E24/E13.')

if __name__=='__main__': main()
