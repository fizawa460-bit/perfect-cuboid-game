#!/usr/bin/env python3
"""Scout only: profile exact small-state compression for surviving k=1,2 types.

This deliberately does NOT enumerate structural H.  It reuses the proved E7/Q8
parameterization and records how many P states and Q8 profile cells remain,
plus exact multiplicities.  The output is a planning certificate only: no
finite-q, action, actual-glue, or theorem credit.
"""
import hashlib,json,runpy
from collections import Counter,defaultdict
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
    if total!=base['summary_by_number_of_Z4_factors'][str(k)]['structural_H_after_t_le_2_and_Q8_exponent']:
        raise SystemExit(f'k{k} total mismatch')
    summary[str(k)]={
      'Q8_admissible_P_count':pcount,
      'exact_profile_cell_count':len(cells),
      'structural_H_total':total,
      'profile_cells':[{'dX':a,'dY':b,'t':t,'eqrank':r,'coisotropic_U_weighted_W_counts':list(u),'structural_H':n} for (a,b,t,r,u),n in sorted(cells.items())],
    }
cert={'schema':'STAGE33_07_NONELEMENTARY_K12_COMPRESSION_SCOUT_V1','source_Q8_sha256':LOCK,'summary':summary,'raw_H_enumerated':False,'planning_only':True,'full_Q4_condition_certified':False,'endpoint_finite_q_certified':False,'endpoint_full_action_certified':False,'actual_index512_glue_identified':False,'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'nonelementary-k12-compression-scout.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'summary':{k:{x:v for x,v in z.items() if x!='profile_cells'} for k,z in summary.items()},'sha256':cert['canonical_sha256']},indent=2,sort_keys=True))