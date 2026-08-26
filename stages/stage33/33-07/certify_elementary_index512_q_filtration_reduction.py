#!/usr/bin/env python3
"""Exact quadratic-filtration reduction of the 8192 full-V4 elementary H.

This is a necessary finite-quadratic-form filter, not a full isometry test.
For every H surviving the complete cc/ct/joint fixed-subgroup conditions, the
q-value distributions on Q[2], 2Q, and 4Q are computed directly from H and
H^perp.  The endpoint distributions are independently recomputed from the
locked endpoint B8 matrix.
"""
import hashlib,itertools,json
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
TGT=json.loads((HERE/'picard-discriminant-compact.json').read_text())
if TGT['canonical_sha256']!='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0':raise SystemExit('endpoint q-form lock moved')
if not TGT['transcendental_discriminant_form_is_negative_of_picard_form']:raise SystemExit('transcendental sign convention regression')

import certify_elementary_index512_full_joint_v4_fixed_type_reduction_v2 as JV4
Q2=JV4.Q2
if JV4.target!=(9,13,14):raise SystemExit('joint target regression')

mods=[int(x) for x in TGT['discriminant_moduli']]
if mods!=[2]*4+[4]*6+[8]*4:raise SystemExit('endpoint Smith regression')
# Transcendental B8 is negative of the retained Picard B8.
B8=[[-int(x) for x in row] for row in TGT['discriminant_bilinear_numerator_over_8_reduced']]

def qnum(x,B):
    return sum(x[i]*B[i][j]*x[j] for i in range(14) for j in range(14))%16

def endpoint_values(kind):
    if kind=='Q2':return [[0,m//2] for m in mods]
    if kind=='2Q':return [list(range(0,m,2)) for m in mods]
    if kind=='4Q':return [list(range(0,m,4)) for m in mods]
    raise ValueError(kind)

def endpoint_dist(kind):
    c=Counter()
    for x in itertools.product(*endpoint_values(kind)):c[qnum(x,B8)]+=1
    return c

target_q2=endpoint_dist('Q2');target_2q=endpoint_dist('2Q');target_4q=endpoint_dist('4Q')
if target_q2!=Counter({0:8192,8:8192}):raise SystemExit(f'endpoint Q2 distribution regression {target_q2}')
if target_2q!=Counter({0:8192,8:8192}):raise SystemExit(f'endpoint 2Q distribution regression {target_2q}')
if target_4q!=Counter({0:16}):raise SystemExit(f'endpoint 4Q distribution regression {target_4q}')

Xmask=(1<<10)-1

def q2_dist(H):
    # Q[2] -> H via doubling has fibers A0[2]/H of size 2^(14-9)=32.
    c=Counter()
    for h in Q2.span(Q2.canon(H)):
        wx=(h&Xmask).bit_count();wy=((h>>10)&15).bit_count()
        c[(4*wx+8*wy)%16]+=32
    if sum(c.values())!=2**14:raise SystemExit('Q2 distribution mass regression')
    return c

def twoq_dist(H):
    # A class in 2Q is controlled by the parity p of a quarter-lift.  p runs
    # through H^perp (32 vectors).  For py=1111 all 512 internal lifts have
    # the same q; otherwise they split 256/256 between base and base+8.
    Hp=Q2.nullspace_basis(Q2.canon(H),14)
    if len(Hp)!=5:raise SystemExit('Hperp dimension regression')
    c=Counter()
    for p in Q2.span(Hp):
        wx=(p&Xmask).bit_count();py=(p>>10)&15;wy=py.bit_count()
        base=(4*wx+2*wy)%16
        if py==15:c[base]+=512
        else:c[base]+=256;c[(base+8)%16]+=256
    if sum(c.values())!=2**14:raise SystemExit('2Q distribution mass regression')
    return c

def fourq_dist(H):
    # pY lies in (H cap Y)^perp=span(t); the structural branch has even-weight
    # t, so q(4x)=8*wt(pY)=0 mod16.  Enumerate the 16 classes explicitly.
    c=Counter()
    Hp=Q2.nullspace_basis(Q2.canon(H),14)
    seen=set()
    for p in Q2.span(Hp):seen.add((p>>10)&15)
    # 4Q has 16 classes; their q-value is forced to zero in this branch.
    if any(v.bit_count()%2 for v in seen):raise SystemExit('odd Y parity reached 4Q')
    c[0]=16
    return c

def key(c):return tuple(sorted((int(k),int(v)) for k,v in c.items()))

def iter_joint_survivors():
    for H,b,t,dm in JV4.iter_full_cc_H():
        sigs=[JV4.joint_signature(H,Bt,B4) for _,Bt,B4,_ in JV4.global_types]
        if all(s==JV4.target for s in sigs):yield H,b,t,dm

before=0;twoq_census=Counter();q2_after_2q_census=Counter();fourq_census=Counter();after_2q=0;after_q2=0
for H,b,t,dm in iter_joint_survivors():
    before+=1
    d2=twoq_dist(H);twoq_census[key(d2)]+=1
    d4=fourq_dist(H);fourq_census[key(d4)]+=1
    if d2!=target_2q:continue
    after_2q+=1
    d1=q2_dist(H);q2_after_2q_census[key(d1)]+=1
    if d1!=target_q2:continue
    after_q2+=1
if before!=8192:raise SystemExit(f'full joint input census regression {before}')
expected_2q=Counter({
 ((0,4096),(4,4096),(8,4096),(12,4096)):6528,
 ((0,8192),(8,8192)):640,
 ((0,4096),(4,2048),(8,4096),(12,6144)):448,
 ((0,4096),(4,6144),(8,4096),(12,2048)):192,
 ((0,6144),(8,10240)):192,
 ((0,10240),(8,6144)):192,
})
if twoq_census!=expected_2q:raise SystemExit(f'2Q q-distribution census regression {twoq_census}')
if after_2q!=640:raise SystemExit('2Q target survivor regression')
expected_q2=Counter({((0,8192),(8,8192)):256,((0,4096),(4,4096),(8,4096),(12,4096)):384})
if q2_after_2q_census!=expected_q2:raise SystemExit(f'Q2 q-distribution census regression {q2_after_2q_census}')
if after_q2!=256:raise SystemExit('Q2 target survivor regression')
if fourq_census!=Counter({((0,16),):8192}):raise SystemExit(f'4Q automatic match regression {fourq_census}')

fmt=lambda C:{';'.join(f'{a}:{b}' for a,b in k):v for k,v in sorted(C.items())}
cert={
 'schema':'STAGE33_07_ELEMENTARY_INDEX512_Q_FILTRATION_REDUCTION_V1',
 'source_locks':{'endpoint_picard_discriminant_sha256':TGT['canonical_sha256'],'joint_v4_reduction_schema':'STAGE33_07_ELEMENTARY_INDEX512_FULL_JOINT_V4_FIXED_TYPE_REDUCTION_V2'},
 'target_q_value_distributions':{'Q2':{str(k):v for k,v in sorted(target_q2.items())},'2Q':{str(k):v for k,v in sorted(target_2q.items())},'4Q':{str(k):v for k,v in sorted(target_4q.items())}},
 'direct_formula_exact':{'Q2_qnum':'4*wt_X(h)+8*wt_Y(h) mod16, fiber 32 per h in H','2Q_qnum':'base=4*wt_X(p)+2*wt_Y(p); py=1111 gives 512 at base, otherwise 256 at base and base+8','4Q_qnum':'8*wt(pY)=0 mod16 because pY lies in even-weight span(t)'},
 'before_q_filtration':before,
 'twoQ_distribution_census':fmt(twoq_census),
 'after_twoQ_target_distribution':after_2q,
 'Q2_distribution_census_after_twoQ':fmt(q2_after_2q_census),
 'after_Q2_target_distribution':after_q2,
 'fourQ_distribution_census':fmt(fourq_census),
 'fourQ_target_distribution_automatic_for_all_8192':True,
 'elementary_candidates_after_q_filtration_total':after_q2,
 'full_finite_quadratic_form_isometry_certified_for_survivors':False,
 'all_elementary_order512_glue_rejected':False,'actual_index512_glue_identified':False,'simultaneous_endpoint_cc_ct_action_conjugacy_certified':False,
 'next_exact_leaf':'L33-07-DECIDE-FULL-FINITE-Q-ISOMETRY-AND-SIMULTANEOUS-ENDPOINT-V4-CONJUGACY-FOR-256-ELEMENTARY-H',
 'new_residual_kernel':'R33-BR2A-INDEX512-ELEMENTARY-GLUE-256-FULL-Q-V4-CONJUGACY-CENSUS-PLUS-NONELEMENTARY-GLUE',
 'unit_status':'RUNNING_REPAIR','unit_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-q-filtration-reduction.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before':before,'after_2Q':after_2q,'after_Q2':after_q2,'fourQ_automatic':True,'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
