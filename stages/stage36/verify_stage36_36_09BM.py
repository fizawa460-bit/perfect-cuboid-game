#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BM/old-six-full-cover-degenerate-cancellation-residue-preflight.json'
BL=ROOT/'stages/stage36/36-09BL/old-six-higher-qadic-hensel-reduction-preflight.json'
BLV=ROOT/'stages/stage36/verify_stage36_36_09BL.py'
AD=ROOT/'stages/stage36/36-09AD/coupled-six-reservoir-factor-squareclass-parity-preflight.json'
V=ROOT/'stages/stage36/36-09V/gaussian-directional-prime-support-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='e758e05953df2cf8cd4ab26ac1e9d72374e99760'
BL_HEAD='6e44915f4d9ca6435b3a70eea4e48c5d5a74a0fd'
BL_CI='34106280151/101691927672'
CERT_BLOB='4fae43a7ebc9022acb4283a40f6eb95cb88d2aa5'
LOCKS={BL:'4d858793827216b2109b81c6a7fb9eaa83b7eaa7',BLV:'386ff67804c5a5764fb681d84ce96b6b58e5c28b',AD:'9d0388845955efee71d1a761ae4ee943d8b565d5',V:'9fdec16f920104cc6c1961fb092185a0371258d5'}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))

def diff_rule(first:int,second:int)->str:
    if first<second: return 'AUTOMATIC'
    if first>second: return 'REQUIRES_MINUS_ONE_RESIDUE'
    return 'TIE_BRANCH'

def main():
    assert blob(CERT)==CERT_BLOB,(blob(CERT),CERT_BLOB)
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BL_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bl=json.loads(BL.read_text()); ad=json.loads(AD.read_text()); v=json.loads(V.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1691,'36_09BL_exact_head':BL_HEAD,'36_09BL_exact_head_ci':BL_CI}
    assert bl['route_result']['next_leaf']=='36-09BM_OLD_SIX_FULL_COVER_DEGENERATE_CANCELLATION_RESIDUE_PREFLIGHT'
    assert bl['odd_Qq_square_criterion']['higher_digit_square_root_obstruction'] is False
    assert ad['odd_reservoir_disjointness']['alpha']==['P','M']
    assert ad['odd_reservoir_disjointness']['beta']==['a','b','a-b','a+b']
    assert v['gaussian_direction_adapter']['alpha_extra_residue']=='if odd q divides C0 then 2 is a quadratic residue mod q'

    u=c['universal_nontie_rule']
    assert u['Gminus_term_valuations']==['2R','2L+2S']
    assert u['Gplus_term_valuations']==['2S','2K+2L+2R']
    assert u['post_leading_data_hensel_obstruction'] is False

    # Alpha reservoirs: K=L=0, and R,S cannot both be positive.
    a=c['alpha_reservoirs_P_or_M']
    for R in range(5):
        for S in range(5):
            if R>0 and S>0: continue
            gm=diff_rule(2*R,2*S)
            gp=diff_rule(2*S,2*R)
            if R<S:
                assert gm=='AUTOMATIC' and gp=='REQUIRES_MINUS_ONE_RESIDUE'
            elif S<R:
                assert gm=='REQUIRES_MINUS_ONE_RESIDUE' and gp=='AUTOMATIC'
            else:
                assert R==S==0 and gm==gp=='TIE_BRANCH'
    assert a['R_less_than_S']=={'Gminus':'AUTOMATIC','Gplus':'REQUIRES_MINUS_ONE_RESIDUE'}
    assert a['S_less_than_R']=={'Gminus':'REQUIRES_MINUS_ONE_RESIDUE','Gplus':'AUTOMATIC'}
    assert a['R_equal_S']=={'forced':'R=S=0','status':'DOUBLE_TIE_BRANCH'}
    # (2/q)=+1 gives q mod8 in {1,7}; (-1/q)=+1 gives {1,5}; intersection is {1}.
    two_res={r for r in (1,3,5,7) if r in (1,7)}
    minus_one_res={r for r in (1,3,5,7) if r in (1,5)}
    assert two_res & minus_one_res == {1}
    assert a['parameter_only_exclusion'] is False

    b=c['beta_reservoirs_a_b_a_minus_b_a_plus_b']
    # Odd m: K=1, L=(m-1)/2, S=0; Gplus is automatically square-leading.
    for m in (1,3,5,7):
        K=1; L=(m-K)//2; S=0
        for R in range(7):
            gm=diff_rule(2*R,2*L+2*S)
            gp=diff_rule(2*S,2*K+2*L+2*R)
            assert gp=='AUTOMATIC'
            if R<L: assert gm=='AUTOMATIC'
            elif R>L: assert gm=='REQUIRES_MINUS_ONE_RESIDUE'
            else: assert gm=='TIE_BRANCH'
    # Even m: K=0, L=m/2>=1; exactly one of R,S may be positive.
    for m in (2,4,6,8):
        K=0; L=m//2
        for R,S in [(0,0)]+[(r,0) for r in range(1,7)]+[(0,s) for s in range(1,7)]:
            gm=diff_rule(2*R,2*L+2*S)
            gp=diff_rule(2*S,2*K+2*L+2*R)
            if R==S==0:
                assert gm==gp=='AUTOMATIC'
            elif R>0:
                assert gp=='AUTOMATIC'
                if R<L: assert gm=='AUTOMATIC'
                elif R>L: assert gm=='REQUIRES_MINUS_ONE_RESIDUE'
                else: assert gm=='TIE_BRANCH'
            else:
                assert gm=='AUTOMATIC'
                if S<L: assert gp=='AUTOMATIC'
                elif S>L: assert gp=='REQUIRES_MINUS_ONE_RESIDUE'
                else: assert gp=='TIE_BRANCH'

    ex=c['exact_progress']; rr=c['route_result']
    assert ex['old_six_nontie_branches_classified'] is True
    assert ex['new_full_cover_conditional_minus_one_gate'] is True
    assert ex['alpha_non_tie_q_mod8_gate'] is True
    assert ex['tie_branches_isolated'] is True
    assert ex['all_old_six_tie_residues_classified'] is False
    assert ex['candidate_parameter_set_shrunk'] is False and ex['receiver_closed'] is False
    assert rr['route_status']=='PASS_NEW_FULL_COVER_NONTIE_RESIDUE_GATE_TIE_BRANCHES_ISOLATED'
    assert rr['next_leaf']=='36-09BN_OLD_SIX_TIE_BRANCH_NORMALIZED_UNIT_RESIDUE_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V101_36_09BM_NONTIE_RESIDUE_TAXONOMY'
    bm=st['authority_frontier']['36-09BM']
    assert bm['certificate_blob_sha']==CERT_BLOB
    assert bm['OLD_SIX_NONTIE_BRANCHES_CLASSIFIED'] is True
    assert bm['ALPHA_NONTIE_Q_MOD8_GATE'] is True
    assert bm['TIE_BRANCHES_ISOLATED'] is True
    assert bm['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and bm['RECEIVER_CLOSED'] is False
    assert st['current']['unit']=='36-09BM'
    assert st['current']['next_exact_leaf']=='36-09BN_OLD_SIX_TIE_BRANCH_NORMALIZED_UNIT_RESIDUE_PREFLIGHT'
    assert st['current']['36_09BN_entry_allowed'] is True
    for key in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][key] is False
    print('36-09BM verified: all old-six unequal-valuation full-cover branches are classified. Negative-square dominance gives (-1/q)=+1; on alpha reservoirs this combines with (2/q)=+1 to force q=1 mod8. Tie branches remain; no parameter shrink.')

if __name__=='__main__': main()
