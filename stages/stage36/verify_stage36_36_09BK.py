#!/usr/bin/env python3
from __future__ import annotations
import json, math, subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BK/prime2-unit-gate-pullback-parameter-separation-preflight.json'
BJ=ROOT/'stages/stage36/36-09BJ/prime2-equal-valuation-unit-branch-preflight.json'
BJV=ROOT/'stages/stage36/verify_stage36_36_09BJ.py'
BI=ROOT/'stages/stage36/36-09BI/prime2-full-cover-congruence-preflight.json'
BB=ROOT/'stages/stage36/36-09BB/ay-receiver-scaled-self-intersection-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='e758e05953df2cf8cd4ab26ac1e9d72374e99760'
BJ_HEAD='89d22a0fa48c4c33d67cb9db1dc084ca4756171a'
BJ_CI='34104852297/101687413548'
CERT_BLOB='0f264dfa584d41e2cf39578a1b61c80ecfc0aec1'
LOCKS={BJ:'f9ef3dde7b756470f2fc882327a67d72db7902f1',BJV:'cbf8b85821ae165531319aac462ad7214d7e756e',BI:'ba6a705ce61b14e640b2c400d42dded60097b406',BB:'e4b63fd500d05ff5dc704e0c08409edee5895053'}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def v2i(n:int)->int:
    assert n
    n=abs(n); k=0
    while n%2==0: n//=2; k+=1
    return k

def q2_square(x:Fraction)->bool:
    if x==0: return True
    if x<0: return False
    vn=v2i(x.numerator); vd=v2i(x.denominator); val=vn-vd
    if val%2: return False
    un=(x.numerator>>vn)%8; ud=(x.denominator>>vd)%8
    return (un*pow(ud,-1,8))%8==1

def point_data(a,b,u,v,kappa):
    P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; Q=a*a+b*b; D0=a*b*(a-b)*(a+b)
    ay_minus=Fraction(u*u-v*v,kappa)
    ay_plus=Fraction(u*u+v*v,2)
    full_minus=Fraction(M*M*u*u-P*P*v*v,kappa)
    full_plus=Fraction(M*M*u*u+P*P*v*v,2)
    z2=Fraction(Q*Q*(u*u-v*v),4*D0*(u*u+v*v))
    return {'P':P,'M':M,'Q':Q,'D0':D0,'alpha':v2i(u*u-v*v),'ay_minus':ay_minus,'ay_plus':ay_plus,'full_minus':full_minus,'full_plus':full_plus,'z2':z2,'z2m1':z2-1}

def main():
    assert blob(CERT)==CERT_BLOB,(blob(CERT),CERT_BLOB)
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BJ_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bj=json.loads(BJ.read_text()); bi=json.loads(BI.read_text()); bb=json.loads(BB.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1691,'36_09BJ_exact_head':BJ_HEAD,'36_09BJ_exact_head_ci':BJ_CI}
    assert bj['route_result']['next_leaf']=='36-09BK_PRIME2_UNIT_GATE_PULLBACK_TO_PARAMETER_RESIDUES_PREFLIGHT'
    assert bi['route_result']['prime2_full_cover_first_valuation_layer_classified'] is True
    assert bb['receiver_restricted_intersection']['S34_W03_exact_joint_system_materialized'] is True

    # Global polynomial identities underlying the pullback.
    for a in range(-9,10):
        for b in range(-9,10):
            if not a or not b or math.gcd(abs(a),abs(b))!=1 or a==b or a==-b: continue
            P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; Q=a*a+b*b; D0=a*b*(a-b)*(a+b)
            assert Q*Q-4*D0==M*M
            assert Q*Q+4*D0==P*P
            for u,v in ((1,3),(3,5)):
                lhs=Q*Q*(u*u-v*v)-4*D0*(u*u+v*v)
                rhs=M*M*u*u-P*P*v*v
                assert lhs==rhs

    w=c['fixed_parameter_witness']
    assert w=={'a':1,'b':2,'p':'1/2','D0':-6,'P':1,'M':-7,'Qsum':5,'delta':1,'sigma':0,'kappa':-3,'BI_equality_alpha':4,'retained_parameter_open':True}
    a,b,kappa=1,2,-3
    fail=point_data(a,b,1,57,kappa)
    pas=point_data(a,b,3,107,kappa)
    assert fail['D0']==pas['D0']==-6 and fail['P']==pas['P']==1 and fail['M']==pas['M']==-7 and fail['Q']==pas['Q']==5
    assert fail['alpha']==pas['alpha']==4

    # Both are retained-open AY Q2 branches for the same parameter.
    lam=Fraction(1,-7)
    for u,v,d in ((1,57,fail),(3,107,pas)):
        t=Fraction(v,u)
        assert t not in (0,1,-1) and lam*t not in (1,-1)
        assert q2_square(d['ay_minus']) and q2_square(d['ay_plus'])
        assert q2_square(d['full_plus'])
        # exact BJ pullback identity after dividing by the AY square factors
        assert d['z2m1']==Fraction(d['full_minus'], 1) / Fraction(4*d['D0']*(u*u+v*v), kappa)

    assert fail['ay_minus']==Fraction(3248,3) and fail['ay_plus']==1625
    assert fail['full_plus']==1649 and fail['full_minus']==Fraction(3200,3)
    assert fail['z2']==Fraction(203,195) and fail['z2m1']==Fraction(8,195)
    assert q2_square(fail['full_minus']) is False and q2_square(fail['z2m1']) is False
    assert v2i(fail['full_minus'].numerator)-v2i(fail['full_minus'].denominator)==7
    assert v2i(fail['z2m1'].numerator)-v2i(fail['z2m1'].denominator)==3

    assert pas['ay_minus']==Fraction(11440,3) and pas['ay_plus']==5729
    assert pas['full_plus']==5945 and pas['full_minus']==Fraction(11008,3)
    assert pas['z2']==Fraction(17875,17187) and pas['z2m1']==Fraction(688,17187)
    assert q2_square(pas['full_minus']) is True and q2_square(pas['z2m1']) is True
    assert v2i(pas['full_minus'].numerator)-v2i(pas['full_minus'].denominator)==8
    assert v2i(pas['z2m1'].numerator)-v2i(pas['z2m1'].denominator)==4

    ec=c['exact_conclusion']; rr=c['route_result']
    assert ec['same_parameter_has_BJ_pass_and_fail_AY_Q2_branches'] is True
    assert ec['prime2_gate_is_parameter_only_predicate'] is False
    assert ec['prime2_gate_may_still_help_with_global_receiver_point_control'] is True
    assert ec['candidate_parameter_set_shrunk'] is False and ec['receiver_closed'] is False
    assert rr['route_status']=='BLOCKED_AS_STANDALONE_PARAMETER_FILTER_SAME_PARAMETER_SEPARATION_WITNESS'
    assert rr['prime2_parameter_only_filter_route_blocked'] is True
    assert rr['prime2_receiver_point_gate_retained'] is True
    assert rr['next_leaf']=='36-09BL_OLD_SIX_HIGHER_QADIC_FULL_COVER_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V99_36_09BK_Q2_SAME_PARAMETER_SEPARATION'
    bk=st['authority_frontier']['36-09BK']
    assert bk['certificate_blob_sha']==CERT_BLOB
    assert bk['SAME_PARAMETER_BJ_PASS_FAIL_SEPARATION'] is True
    assert bk['PRIME2_PARAMETER_ONLY_FILTER'] is False
    assert bk['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and bk['RECEIVER_CLOSED'] is False
    assert st['current']['unit']=='36-09BK'
    assert st['current']['next_exact_leaf']=='36-09BL_OLD_SIX_HIGHER_QADIC_FULL_COVER_PREFLIGHT'
    assert st['current']['36_09BL_entry_allowed'] is True
    for key in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][key] is False
    print('36-09BK verified: fixed p=1/2 has retained-open h=0 AY Q2 branches that both pass and fail BJ. Prime 2 is not a standalone parameter-only filter; receiver-point gate retained. BL selected next.')

if __name__=='__main__': main()
