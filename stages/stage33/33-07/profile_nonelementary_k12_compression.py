#!/usr/bin/env python3
"""Exact planning compression for the surviving non-elementary k=1,2 types.

This does NOT enumerate raw structural H.  It reuses the proved E7/Q8
parameterization and groups every admissible P state into exact profile cells
(dX,dY,t,eqrank, coisotropic-U weighted W counts).  The complete Q8 totals are
reconstructed exactly, so the output is a lossless planning compression of the
already-certified predecessor census, not a heuristic sample.

No full-Q[4], finite-q, action, actual-glue, or theorem credit is granted.
"""
import hashlib,json,runpy
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
ns=runpy.run_path(str(HERE/'certify_nonelementary_target_q8_exponent_reduction.py'))
base=json.loads((HERE/'nonelementary-target-q8-exponent-reduction.json').read_text())
LOCK='4a5c84ad765f93442f08991ffdcea0bab6f1ae5a3ab6561157201bba262f75ee'
if base.get('canonical_sha256')!=LOCK: raise SystemExit('Q8 source lock moved')
subspaces=ns['subspaces']; span=ns['span']; rank=ns['rank']; eqrc=ns['eqrc']; qbinom2=ns['qbinom2']; coisotropic=ns['coisotropic']; contains=ns['contains']
summary={}
for k in (1,2):
    wdim=9-k; cells=Counter(); pcount=0; total=0
    for B in subspaces[k]:
        supp=0
        for x in span(B): supp|=x
        d=supp.bit_count()
        if d>wdim: continue
        t=rank([x&0b111 for x in B])
        eqrank,ok=eqrc(B)
        if not ok or t>2: continue
        dX=(supp&0b111).bit_count(); y_support=[1<<j for j in range(4) if (supp>>(3+j))&1]
        nF=1 << (k*(5+k)-eqrank); nW8=0; byu=Counter()
        for U in coisotropic:
            u=len(U)
            if any(not contains(U,e) for e in y_support): continue
            r=wdim-u
            if not (dX<=r<=10-t): continue
            n=qbinom2(10-t-dX,r-dX) * (1<<((r-dX)*(4-u)))
            nW8+=n; byu[u]+=n
        if not nW8: continue
        pcount+=1; total+=nW8*nF
        key=(dX,len(y_support),t,eqrank,tuple(sorted(byu.items())))
        cells[key]+=nW8*nF
    predecessor=base['summary_by_number_of_Z4_factors'][str(k)]['structural_H_after_t_le_2_and_Q8_exponent']
    if total!=predecessor: raise SystemExit(f'k{k} total mismatch')
    summary[str(k)]={
      'Q8_admissible_P_count':pcount,
      'exact_profile_cell_count':len(cells),
      'structural_H_total':total,
      'predecessor_total_reconstructed_exactly': total==predecessor,
      'profile_cells':[{'dX':a,'dY':b,'t':t,'eqrank':r,'coisotropic_U_weighted_W_counts':[list(x) for x in u],'structural_H':n} for (a,b,t,r,u),n in sorted(cells.items())],
    }
expected={'1':(63,9,1375727569216),'2':(647,19,437454110720)}
for k,want in expected.items():
    z=summary[k]; got=(z['Q8_admissible_P_count'],z['exact_profile_cell_count'],z['structural_H_total'])
    if got!=want: raise SystemExit(f'k{k} profile compression regression: {got}')
cert={
 'schema':'STAGE33_07_NONELEMENTARY_K12_COMPRESSION_SCOUT_V2',
 'source_Q8_sha256':LOCK,
 'summary':summary,
 'raw_H_enumerated':False,
 'all_Q8_admissible_P_states_accounted_for':True,
 'predecessor_totals_reconstructed_exactly':True,
 'profile_partition_lossless_for_recorded_invariants':True,
 'next_exact_leaf':'L33-07-DERIVE-CELLWISE-THETA-Q4-AND-Q-FILTRATION-OBSTRUCTIONS-FOR-K1-K2',
 'planning_only':True,
 'full_Q4_condition_certified':False,
 'endpoint_finite_q_certified':False,
 'endpoint_full_action_certified':False,
 'actual_index512_glue_identified':False,
 'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'nonelementary-k12-compression-scout.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'summary':{k:{x:v for x,v in z.items() if x!='profile_cells'} for k,z in summary.items()},'sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
