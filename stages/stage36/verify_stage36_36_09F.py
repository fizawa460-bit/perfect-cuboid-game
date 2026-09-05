#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09F/paired-legendre-receiver-intersection-preflight.json'
PREV=ROOT/'stages/stage36/36-09E/character-elliptic-quotient-arithmetic-preflight.json'
PHYS=ROOT/'stages/stage36/36-03/physical-open-boundary.json'
SIGN=ROOT/'stages/stage29/29-02ha/exact-sign-cover-model.md'
CYCLE=ROOT/'docs/research-os/policies/cycle-exploration-safety-protocol.md'
W03=ROOT/'docs/arsenal/cards/formal/S34-W03.md'
W01=ROOT/'docs/arsenal/cards/formal/S34-W01.md'
W02=ROOT/'docs/arsenal/cards/formal/S34-W02.md'

CERT_BLOB='0615844de212eb3644f15cd3f5577b37ccc3855a'
EXPECTED_BASE='3b4b5969330ae89a41899598fbdf17e76be76f72'
LOCKS={PREV:'081b704fecaa3bd39e6a523ee7beaefe706683f4',PHYS:'fc1947b2de08f7d8a104bdc91902b20e88635349',SIGN:'fc2d5284a259750f45d2d756a952002671e3bccc',CYCLE:'4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37',W03:'1d5275321f42768a6414d4610ac912c63be43f96',W01:'01a8e90e34b4aa46edbfa825803d488e5230e9d0',W02:'13d41be776fcd2edcd258f11bd28c5a6596de45b'}

def req(ok:bool,msg:str)->None:
    if not ok: raise SystemExit(msg)
def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def rank_f2(rows):
    a=[list(map(int,r)) for r in rows]; m=len(a); n=len(a[0]); rank=0
    for col in range(n):
        pivot=next((i for i in range(rank,m) if a[i][col]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        for i in range(m):
            if i!=rank and a[i][col]: a[i]=[x^y for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank,a

def main()->None:
    req(blob(CERT)==CERT_BLOB,'36-09F certificate blob drift')
    for p,sha in LOCKS.items(): req(blob(p)==sha,f'locked source drift: {p}')
    c=json.loads(CERT.read_text())
    req(c['schema']=='STAGE36_36_09F_PAIRED_LEGENDRE_RECEIVER_INTERSECTION_PREFLIGHT_V1','36-09F schema moved')
    req(c['base_main_sha']==EXPECTED_BASE,'36-09F base moved')
    req(c['entry_authority']=={'stage36_36_09E_promotion_pr':1595,'promotion_exact_head':'f75830b2fd54031c1af05e2377a9da365a4d7fdf','promotion_exact_head_ci_run':33957789368,'promotion_exact_head_ci_job':101284151736,'promotion_merged_main_sha':EXPECTED_BASE,'selected_route':'B6_FIBRATION_TO_CURVE_BASE'},'36-09F entry authority moved')
    prev=json.loads(PREV.read_text()); pair=prev['paired_receiver']; collapse=prev['four_family_collapse']
    req(pair['X_plus']=='s+t+1' and pair['X_minus']=='-s' and pair['linear_compatibility']=='X_plus+X_minus=t+1','36-09E paired X moved')
    req(collapse['E_t_PLUS']=='Y^2=X*(X-1)*(X-t)' and collapse['E_t_MINUS']=='Y^2=-X*(X-1)*(X-t)','E_t equations moved')
    req(collapse['E_t1_PLUS']=='Y^2=X*(X-1)*(X-(t+1))' and collapse['E_t1_MINUS']=='Y^2=-X*(X-1)*(X-(t+1))','E_t1 equations moved')
    expected_rhs={'E_t_PLUS':'B*C*D','E_t_MINUS':'A*B*C','E_t1_PLUS':'A*C*D','E_t1_MINUS':'A*B*D'}
    req({k:v['rhs'] for k,v in c['four_paired_legendre_equations'].items()}==expected_rhs,'four prescribed-X RHS moved')
    M=c['squareclass_linear_system']['matrix_F2']; req(M==[[0,1,1,1],[1,1,1,0],[1,0,1,1],[1,1,0,1]],'squareclass matrix moved')
    rank,rref=rank_f2(M); req(rank==4,'squareclass matrix not rank4'); req(rref==[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],f'unexpected rref {rref}')
    req(c['squareclass_linear_system']['kernel_dimension']==0 and c['squareclass_linear_system']['only_squareclass_solution']==['0','0','0','0'],'squareclass kernel moved')
    phys=json.loads(PHYS.read_text()); req(phys['seven_line_base']['coordinates']=='[x:y:z]=[a1^2:a2^2:a3^2]','physical base moved')
    expected_lines={'A1':'t','A2':'1','A3':'A=s','B3':'t+1','B2':'C=s+t','B1':'B=s+1','C':'D=s+t+1'}
    req(c['seven_line_reconstruction']['seven_line_values']==expected_lines,'seven-line dictionary moved')
    prevsq=prev['physical_squareclass_restriction']['chart_ratio_consequences']; req(prevsq['t=x/y']=='square' and prevsq['t+1=(x+y)/y']=='square','physical base squares moved')
    sign=SIGN.read_text()
    for text in ['the seven values `L_i(q)` have a common square class','q\\text{ lifts to }\\bar S(\\mathbf Q)','Clearing denominators converts a positive rational lift into an integral cuboid candidate']:
        req(text in sign,f'sign-cover phrase missing: {text}')
    req(c['seven_line_reconstruction']['paired_four_equations_force_all_moving_line_values_square'] is True and c['seven_line_reconstruction']['therefore_all_seven_line_values_square'] is True,'seven-line reconstruction moved')
    req(c['seven_line_reconstruction']['sign_cover_lift_criterion_applies'] is True and c['seven_line_reconstruction']['converse_checked'] is True,'sign-cover equivalence moved')
    req('RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION' in W03.read_text(),'S34-W03 moved')
    req('SUCCESSIVE_EXACT_FACTOR_SQUARECLASS_DESCENT' in W01.read_text(),'S34-W01 moved')
    req('GLOBAL_MORDELL_WEIL_CONGRUENCE_EXCLUSION' in W02.read_text(),'S34-W02 moved')
    route=c['route_decision']; req(route['B6_FIBRATION_TO_CURVE_BASE']=='BLOCKED_BY_EXACT_ENDPOINT_EQUIVALENCE_NO_PROPER_RECEIVER_GAIN','B6 block moved')
    req(route['cycle_route_status']=='BLOCKED_NEW_PATTERN_ISOLATED','cycle status moved'); req(route['S34_W03_INTERSECTION_EXCLUSION_EXECUTED'] is False,'S34-W03 falsely executed')
    req(route['S34_W01_TRIGGERED'] is False and route['S34_W02_TRIGGERED'] is False,'premature Arsenal trigger'); req(route['next_route_after_hostile_audit']=='36-09G_ENDPOINT_EQUIVALENCE_BREADTH_REFRESH','36-09G routing moved')
    cycle=CYCLE.read_text()
    for text in ['same essential receiver survives two consecutive cycle batches despite reformulation','EXHAUSTIVE_VIEW_AUDIT','BLIND_REDISCOVERY']:
        req(text in cycle,f'cycle phrase missing: {text}')
    cu=c['cycle_update']; req(cu['new_material_block'] is True and cu['fresh_breadth_audit_required_now'] is True,'fresh breadth trigger moved')
    req(cu['live_candidates_after_block']==0 and len(cu['untested_candidates_preserved'])==4,'post-block ledger moved'); req(cu['fresh_EXHAUSTIVE_VIEW_AUDIT_after_36_09F'] is False and cu['fresh_BLIND_REDISCOVERY_after_36_09F'] is False,'breadth falsely complete')
    pc=c['pass_condition']; req(pc['SQUARECLASS_MATRIX_RANK4'] is True and pc['FOUR_PRODUCTS_IFF_FOUR_MOVING_LINES_SQUARE'] is True,'36-09F algebra pass moved')
    req(pc['PHYSICAL_BASE_PLUS_PAIRED_RECEIVER_IFF_FULL_SEVEN_LINE_LIFT'] is True,'endpoint Kummer equivalence moved'); req(pc['B6_PROPER_RECEIVER_GAIN'] is False and pc['GLOBAL_RECEIVER_CLOSED'] is False,'route/closure firewall moved')
    req(all(v is False for v in c['claims'].values()),'36-09F higher credit leaked')
    print('PASS STAGE36_36_09F_PAIRED_LEGENDRE_RECEIVER_INTERSECTION_PREFLIGHT')
    print('four triple-product squareclasses have F2 rank 4 => A,B,C,D individually square')
    print('physical t,t+1 base + paired receiver iff full normalized seven-line Kummer lift')
    print('B6=BLOCKED_BY_ENDPOINT_EQUIVALENCE; fresh breadth refresh required; next=36-09G after hostile audit')

if __name__=='__main__': main()
