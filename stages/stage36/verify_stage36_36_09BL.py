#!/usr/bin/env python3
from __future__ import annotations
import json, math, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BL/old-six-higher-qadic-hensel-reduction-preflight.json'
SRC=ROOT/'stages/stage36/36-09BL/odd-square-hensel-no-higher-digit-source-lock.md'
BK=ROOT/'stages/stage36/36-09BK/prime2-unit-gate-pullback-parameter-separation-preflight.json'
BKV=ROOT/'stages/stage36/verify_stage36_36_09BK.py'
BH=ROOT/'stages/stage36/36-09BH/bad-place-full-cover-valuation-preflight.json'
AD=ROOT/'stages/stage36/36-09AD/coupled-six-reservoir-factor-squareclass-parity-preflight.json'
AE=ROOT/'stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='e758e05953df2cf8cd4ab26ac1e9d72374e99760'
BK_HEAD='dce7d4f7c2dc33b0cf939551b4bc488137531831'
BK_CI='34105390997/101689110786'
CERT_BLOB='4d858793827216b2109b81c6a7fb9eaa83b7eaa7'
LOCKS={SRC:'8899e774a025b58d2fa464e7fbaadad2af1dd30e',BK:'0f264dfa584d41e2cf39578a1b61c80ecfc0aec1',BKV:'bbe2be663966fcaf1992ec101564eb54b1fbea53',BH:'76487371ed363868af18a9fa0f6f7e1367d28f27',AD:'9d0388845955efee71d1a761ae4ee943d8b565d5',AE:'ddae37dd35cd0e732cebadf9c17f3f3fa57930df'}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))

def lift_square_root(q:int,U:int,N:int)->int:
    assert q%2 and math.gcd(q,U)==1 and N>=1
    roots=[y for y in range(q) if (y*y-U)%q==0]
    assert roots
    y=roots[0]
    mod=q
    for _ in range(1,N):
        r=(y*y-U)//mod
        t=(-r*pow((2*y)%q,-1,q))%q
        y += t*mod
        mod *= q
        assert (y*y-U)%mod==0
    return y%mod

def main():
    assert blob(CERT)==CERT_BLOB,(blob(CERT),CERT_BLOB)
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BK_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bk=json.loads(BK.read_text()); bh=json.loads(BH.read_text()); ad=json.loads(AD.read_text()); ae=json.loads(AE.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1691,'36_09BK_exact_head':BK_HEAD,'36_09BK_exact_head_ci':BK_CI}
    assert bk['route_result']['next_leaf']=='36-09BL_OLD_SIX_HIGHER_QADIC_FULL_COVER_PREFLIGHT'
    assert bh['scope_firewalls']['old_six_higher_qadic_information_exhausted'] is False
    assert ad['S34_W01_progress']['complete_2adic_branch_list'] is False
    assert ae['interpretation']['fixed_finite_S_recovered'] is False

    crit=c['odd_Qq_square_criterion']
    assert crit['higher_digit_square_root_obstruction'] is False
    # Deterministically exercise the unit-derivative Hensel recursion over all
    # unit targets modulo q^3 for several odd primes. Higher digits are lifted,
    # not re-tested by a new residue predicate.
    for q in (3,5,7,11):
        qr={x*x%q for x in range(1,q)}
        for U in range(1,q**3):
            if U%q==0: continue
            is_residue=(U%q) in qr
            if is_residue:
                y=lift_square_root(q,U,4)
                assert (y*y-U)%(q**4)==0
            else:
                assert not any((y*y-U)%q==0 for y in range(q))

    assert c['old_six_reservoirs']==['P','M','a','b','a-b','a+b']
    rad=c['full_cover_radicands']
    assert 'M^2*u^2-P^2*v^2' in rad['Gminus'] and 'Qsum^2*r^2-4*T^2*s^2' in rad['Gminus']
    assert 'M^2*u^2+P^2*v^2' in rad['Gplus'] and 'Qsum^2*s^2-kappa^2*T^2*r^2' in rad['Gplus']
    ref=c['exact_refinement_of_BH_open_issue']
    assert ref['BH_old_six_higher_qadic_information_exhausted'] is False
    assert ref['independent_post_residue_hensel_digit_layer_exists'] is False
    assert ref['AD_AE_first_residue_rows_are_full_cover_complete'] is False
    assert ref['double_charge_AD_AE_forbidden'] is True
    rr=c['route_result']
    assert rr['route_status']=='PASS_SHARPENS_OLD_SIX_MISSING_LAYER_TO_DEGENERATE_VALUATION_AND_FIRST_RESIDUE'
    assert rr['generic_higher_digit_square_lifting_route_blocked'] is True
    assert rr['old_six_full_cover_cancellation_analysis_live'] is True
    assert rr['candidate_parameter_set_shrunk'] is False and rr['receiver_closed'] is False
    assert rr['next_leaf']=='36-09BM_OLD_SIX_FULL_COVER_DEGENERATE_CANCELLATION_RESIDUE_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V100_36_09BL_ODD_HENSEL_REDUCTION'
    bl=st['authority_frontier']['36-09BL']
    assert bl['certificate_blob_sha']==CERT_BLOB
    assert bl['POST_RESIDUE_HIGHER_DIGIT_OBSTRUCTION'] is False
    assert bl['OLD_SIX_CANCELLATION_ANALYSIS_LIVE'] is True
    assert bl['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and bl['RECEIVER_CLOSED'] is False
    assert st['current']['unit']=='36-09BL'
    assert st['current']['next_exact_leaf']=='36-09BM_OLD_SIX_FULL_COVER_DEGENERATE_CANCELLATION_RESIDUE_PREFLIGHT'
    assert st['current']['36_09BM_entry_allowed'] is True
    for key in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][key] is False
    print('36-09BL verified: for odd q, square lifting is fully controlled by exact valuation parity plus first normalized residue; no independent higher-digit Hensel obstruction remains. Old-six cancellation leading-data analysis selected next.')

if __name__=='__main__': main()
