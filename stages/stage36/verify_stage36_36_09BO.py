#!/usr/bin/env python3
from __future__ import annotations
import json, math, subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BO/q-reservoir-full-qq-cancellation-preflight.json'
BN=ROOT/'stages/stage36/36-09BN/old-six-tie-normalized-unit-residue-preflight.json'
BNV=ROOT/'stages/stage36/verify_stage36_36_09BN.py'
BH=ROOT/'stages/stage36/36-09BH/bad-place-full-cover-valuation-preflight.json'
BC=ROOT/'stages/stage36/36-09BC/boundary-neighborhood-open-local-no-loop-preflight.json'
BK=ROOT/'stages/stage36/36-09BK/prime2-unit-gate-pullback-parameter-separation-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='e758e05953df2cf8cd4ab26ac1e9d72374e99760'
BN_HEAD='7d9d6e3b1011715c5884a2da0a642892d8cf3984'
BN_CI='34108363855/101698552520'
CERT_BLOB='d239c709d0bffe460897c93cd1fdb24fa7f1e190'
LOCKS={BN:'c64ad051bb1466aa05dfb0cf638b9e7759766ed9',BNV:'1013bad8244708d84aa99908c1fcbeb2c7af6353',BH:'76487371ed363868af18a9fa0f6f7e1367d28f27',BC:'317638c4d1a76f683c7af9bdb4e8285af35f4d05',BK:'0f264dfa584d41e2cf39578a1b61c80ecfc0aec1'}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def vq_int(n:int,q:int)->int:
    assert n
    n=abs(n); k=0
    while n%q==0: n//=q; k+=1
    return k
def vq(x:Fraction,q:int)->int:
    return vq_int(x.numerator,q)-vq_int(x.denominator,q)
def legendre_unit(x:Fraction,q:int)->int:
    vn=vq_int(x.numerator,q); vd=vq_int(x.denominator,q)
    a=(x.numerator//(q**vn))%q; b=(x.denominator//(q**vd))%q
    u=a*pow(b,-1,q)%q
    return 1 if pow(u,(q-1)//2,q)==1 else -1
def q_square(x:Fraction,q:int)->bool:
    if x==0: return True
    return vq(x,q)%2==0 and legendre_unit(x,q)==1

def point_data(u:int,v:int):
    D0=-6; P=1; M=-7; Q=5; kappa=-3
    aym=Fraction(u*u-v*v,kappa); ayp=Fraction(u*u+v*v,2)
    gm=Fraction(M*M*u*u-P*P*v*v,kappa)
    gp=Fraction(M*M*u*u+P*P*v*v,2)
    T2=Fraction(2*D0,kappa)
    zm1=Fraction(Q*Q)*aym/(4*T2*ayp)-1
    zp1=Fraction(Q*Q)*ayp/(kappa*kappa*T2*aym)-1
    return aym,ayp,gm,gp,zm1,zp1

def main():
    assert blob(CERT)==CERT_BLOB,(blob(CERT),CERT_BLOB)
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BN_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bn=json.loads(BN.read_text()); bh=json.loads(BH.read_text()); bc=json.loads(BC.read_text()); bk=json.loads(BK.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1691,'36_09BN_exact_head':BN_HEAD,'36_09BN_exact_head_ci':BN_CI}
    assert bn['route_result']['next_leaf']=='36-09BO_Q_RESERVOIR_FULL_QQ_CANCELLATION_PREFLIGHT'
    assert bh['branch_discriminant_support']['new_odd_reservoir_from_full_cover']=='Q=a^2+b^2'
    assert bh['scope_firewalls']['Q_reservoir_full_Qq_solubility_classified'] is False
    assert bc['good_prime_local_analysis']['generic_good_prime_boundary_neighborhood_obstruction'] is False
    assert bk['exact_conclusion']['prime2_gate_is_parameter_only_predicate'] is False

    s=c['Q_reservoir_setup']
    assert s['minus_one_square'] is True
    assert s['units']==['D0','P','M','kappa','T']
    # For an odd q|a^2+b^2 with primitive a,b, q cannot divide an old beta reservoir and -1 is a residue.
    for a,b in [(1,2),(2,3),(3,4),(4,7),(5,8)]:
        if math.gcd(a,b)!=1: continue
        Q=a*a+b*b
        for q in range(3,50,2):
            if Q%q: continue
            if any(d%q==0 for d in (a,b,a-b,a+b)):
                raise AssertionError((a,b,q))
            assert pow(q-1,(q-1)//2,q)==1  # (-1/q)=+1 on these actual odd prime divisors

    n=c['nontie_classification']; ties=c['tie_branches']
    assert n['all_Q_reservoir_nontie_branches_automatic'] is True
    assert n['parameter_filter_from_nontie'] is False
    assert ties['Gplus_tie']=='R=h,S=0' and ties['Gminus_tie']=='S=h,R=0'
    assert ties['all_Q_reservoir_tie_species_covered'] is True
    # Exhaust the valuation taxonomy abstractly: R,S are not both positive.
    for h in range(1,5):
        for R,S in [(0,0)]+[(r,0) for r in range(1,7)]+[(0,s0) for s0 in range(1,7)]:
            gm=(2*h+2*R,2*S)
            gp=(2*h+2*S,2*R)
            tie_m=gm[0]==gm[1]
            tie_p=gp[0]==gp[1]
            assert tie_m == (R==0 and S==h)
            assert tie_p == (S==0 and R==h)

    # Exact p=1/2, q=5 tie separation witnesses.
    lam=Fraction(-1,7); q=5
    for u,v,should_pass,R,S in [(26,1,True,1,0),(1,18,False,0,1)]:
        t=Fraction(v,u)
        assert t not in (0,1,-1) and lam*t not in (1,-1)
        aym,ayp,gm,gp,zm1,zp1=point_data(u,v)
        assert q_square(aym,q) and q_square(ayp,q)
        assert (vq(aym,q)//2,vq(ayp,q)//2)==(R,S)
        actual=q_square(gm,q) and q_square(gp,q)
        assert actual is should_pass
        if should_pass:
            assert (aym,ayp,gm,gp,zp1)==(Fraction(-225),Fraction(677,2),Fraction(-11041),Fraction(33125,2),Fraction(-1325,648))
            assert vq(zp1,5)==2 and legendre_unit(zp1,5)==1
        else:
            assert (aym,ayp,gm,gp,zm1)==(Fraction(323,3),Fraction(325,2),Fraction(275,3),Fraction(373,2),Fraction(11,312))
            assert vq(zm1,5)==0 and legendre_unit(zm1,5)==-1

    comb=c['combined_bad_place_local_status']; rr=c['route_result']
    assert comb['bad_place_parameter_only_local_route_status']=='BLOCKED'
    assert comb['local_receiver_point_gates_retained'] is True
    assert comb['all_bad_place_local_square_layers_classified'] is True
    assert rr['route_status']=='BLOCKED_AS_STANDALONE_PARAMETER_FILTER_ALL_BAD_PLACE_LOCAL_LAYERS_CLASSIFIED'
    assert rr['natural_hostile_audit_checkpoint'] is True
    assert rr['candidate_parameter_set_shrunk'] is False and rr['receiver_closed'] is False
    assert rr['next_leaf_after_audit']=='36-09BP_FULL_COVER_GLOBAL_DESCENT_ROUTER_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V103_36_09BO_BAD_PLACE_LOCAL_AUDIT_CHECKPOINT'
    bo=st['authority_frontier']['36-09BO']
    assert bo['certificate_blob_sha']==CERT_BLOB
    assert bo['Q_RESERVOIR_LOCAL_LAYER_COMPLETE'] is True
    assert bo['ALL_BAD_PLACE_LOCAL_SQUARE_LAYERS_CLASSIFIED'] is True
    assert bo['BAD_PLACE_PARAMETER_ONLY_LOCAL_ROUTE_BLOCKED'] is True
    assert bo['LOCAL_RECEIVER_POINT_GATES_RETAINED'] is True
    assert bo['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and bo['RECEIVER_CLOSED'] is False
    assert st['current']['unit']=='36-09BO-AUDIT-CHECKPOINT'
    assert st['current']['hostile_audit_checkpoint_reached'] is True
    assert st['current']['36_09BP_entry_allowed'] is False
    for key in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][key] is False
    print('36-09BO verified: Q-reservoir non-tie branches are automatic; the two tie species use BN z^2-1 criteria and fixed p=1/2,q=5 has pass/fail branches. All bad-place local square layers are classified; standalone parameter-local route blocked. Hostile audit checkpoint reached.')

if __name__=='__main__': main()
