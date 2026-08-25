#!/usr/bin/env python3
"""Exact target-Q[4] rank obstruction after the E7 structural reduction.

Let K=H^perp and Q=K/H.  The endpoint group
  Q ~= (Z/2)^4 +(Z/4)^6 +(Z/8)^4
has log2 |Q[4]| = 24.

For an exponent<=4 sign-stable H, use the normalized notation from
certify_nonelementary_sign_q2_structural_reduction.py.  Let t be the F2-rank
of the Kb/X projection P_X (equivalently the first three E7 coordinates).
Then:

  log2 |H intersect 4A0| = 9-t,
  log2 |{x in A0 : 4x in H}| = 28 + (9-t) = 37-t.

Pairing this fourth-root set with H gives a homomorphism theta whose kernel is
K intersect {4x in H}.  The target Q[4] order forces

  log2 |im theta| = (37-t) - (9+24) = 4-t.

But A0[4] is contained in the fourth-root set, and its pairing image on H has
exact order 2^t: it detects precisely the Kb/X projection P_X.  Therefore
2^t <= 2^(4-t), hence t<=2.

This rejects every structural candidate with t=3.  In particular all surviving
P for H type (Z/4)^4 + Z/2 have t=3, so that entire non-elementary type is
impossible before any full finite-q/action search.
"""
import hashlib,json,runpy
from pathlib import Path

HERE=Path(__file__).resolve().parent
# Execute the preceding exact structural census and reuse its deterministic
# certificate plus profile counts.  This also revalidates all E7 counts here.
ns=runpy.run_path(str(HERE/'certify_nonelementary_sign_q2_structural_reduction.py'))
base=json.loads((HERE/'nonelementary-sign-target-q2-structural-reduction.json').read_text())
if base['schema']!='STAGE33_07_NONELEMENTARY_SIGN_TARGET_Q2_STRUCTURAL_REDUCTION_V1':
    raise SystemExit('E7 structural source regression')

# Exact contributions by (d,t,eqrank) are recomputed from the source functions
# rather than inferred from rounded/profile metadata.
subspaces=ns['subspaces'];span=ns['span'];rank=ns['rank'];eqrc=ns['eq_rank_and_consistency'];qbinom2=ns['qbinom2']
summary={}
for k in range(1,5):
    wdim=9-k
    before=after=0
    p_before=p_after=0
    for B in subspaces[k]:
        supp=0
        for x in span(B):supp|=x
        d=supp.bit_count()
        if d>wdim:continue
        t=rank([x&0b111 for x in B])
        eqrank,ok=eqrc(B)
        if not ok:continue
        dimU=14-t
        nW=qbinom2(dimU-d,wdim-d)
        nF=1 << (k*(5+k)-eqrank)
        n=nW*nF
        before+=n;p_before+=1
        if t<=2:
            after+=n;p_after+=1
    summary[str(k)]={
      'structural_H_before_Q4_rank_obstruction':before,
      'structural_H_after_t_le_2':after,
      'rejected_structural_H':before-after,
      'consistent_P_before':p_before,
      'consistent_P_after_t_le_2':p_after,
    }

expected={
 '1':(91996493167936,91996493167936),
 '2':(8985668747264,8985668747264),
 '3':(490213474304,462724005888),
 '4':(6442450944,0),
}
for k,(a,b) in expected.items():
    z=summary[k]
    if (z['structural_H_before_Q4_rank_obstruction'],z['structural_H_after_t_le_2'])!=(a,b):
        raise SystemExit(f'Q4 obstruction census regression k={k}: {z}')
if summary['4']['consistent_P_after_t_le_2']!=0:
    raise SystemExit('Z4^4+Z2 type unexpectedly survived t<=2')

surviving_types=[
 '(Z/4)^3 direct_sum (Z/2)^3',
 '(Z/4)^2 direct_sum (Z/2)^5',
 'Z/4 direct_sum (Z/2)^7',
]
cert={
 'schema':'STAGE33_07_NONELEMENTARY_TARGET_Q4_RANK_OBSTRUCTION_V1',
 'source_structural_sha256':base['canonical_sha256'],
 'target_Q4_log2':24,
 'target_Q2_log2':14,
 'theorem':'log2 fourth-root set = 37-t; target Q[4] forces image log2=4-t; A0[4] pairing image has log2=t; hence t<=2',
 'Kb_X_rank_t_upper_bound':2,
 'summary_by_number_of_Z4_factors':summary,
 'non_elementary_abstract_types_before':4,
 'non_elementary_abstract_types_after':3,
 'rejected_type':'(Z/4)^4 direct_sum Z/2',
 'surviving_types':surviving_types,
 'full_target_Q4_condition_certified':False,
 'endpoint_finite_q_certified':False,
 'endpoint_full_action_certified':False,
 'actual_index512_glue_identified':False,
 'next_exact_leaf':'L33-07-IMPOSE-EXACT-Q4-IMAGE-ORDER-AND-Q8-EXPONENT-ON-THREE-NONELEMENTARY-E7-TYPES',
 'new_residual_kernel':'R33-BR2A-INDEX512-ELEMENTARY-3-INTEGRAL-ORBITS-PLUS-NONELEMENTARY-3-E7-TYPES',
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'nonelementary-target-q4-rank-obstruction.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'types_before':4,'types_after':3,'rejected_type':cert['rejected_type'],'structural_H_after':{k:v['structural_H_after_t_le_2'] for k,v in summary.items()},'certificate_sha256':cert['canonical_sha256'],'next':cert['next_exact_leaf']},indent=2,sort_keys=True))
