#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from collections import defaultdict
from pathlib import Path
import sympy as sp
import materialize_e3_v91c1x_r5b3b3b_classify_20_novel_carriers_and_unify_27 as b3b3b
HERE=Path(__file__).resolve().parent
B3B2=HERE/'e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json'
B3B3B=HERE/'e3-v91c1x-r5b3b3b-classify-20-novel-carriers-and-unify-27.json'
OUT=HERE/'e3-v91c1x-r5b3b3c1-qq-unique-norm-factorization-scratch.json'
B3B2_SHA='52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e'
B3B3B_SHA='7f52f0988cb82983afc0759272e2420e73944b4258940aeffc8a9923816c4a7d'

def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args()
 b2=b3b3b.load(B3B2,B3B2_SHA); b3=b3b3b.load(B3B3B,B3B3B_SHA)
 rows={r['carrier_id']:r for r in b2['finite_linear_carrier_inventory']['carrier_rows']}
 off=list(b3['unified_27_classification']['off_boundary_carrier_ids'])
 groups=defaultdict(list); polys={}
 for cid in off:
  poly=b3b3b.full_sign_norm_poly(rows[cid]['normalized_coefficients_Qi'])
  norm=b3b3b.normalize_norm(poly); h=csha(norm); groups[h].append(cid); polys[h]=poly
 print(f'offboundary={len(off)} unique_norms={len(groups)}',flush=True)
 out=[]
 for j,h in enumerate(sorted(groups),1):
  poly=polys[h]
  if not all(c.is_Rational is True for c in poly.coeffs()): raise SystemExit(f'nonrational norm {h}')
  q=sp.Poly(poly.as_expr(),*b3b3b.BASE,domain=sp.QQ)
  print(f'[{j:02d}/{len(groups):02d}] carriers={groups[h]} terms={len(q.terms())}',flush=True)
  coeff,factors=sp.factor_list(q.as_expr(),*b3b3b.BASE,domain=sp.QQ)
  pats=sorted([int(sp.Poly(f,*b3b3b.BASE,domain=sp.QQ).total_degree()) for f,m in factors for _ in range(int(m))])
  print(f'  QQ pattern={pats}',flush=True)
  out.append({'normalized_full_sign_norm_sha256':h,'carrier_ids':groups[h],'factor_degree_multiset_QQ':pats,'distinct_factor_count_QQ':len(factors),'squarefree_QQ':all(int(m)==1 for _,m in factors)})
 cert={'schema':'stage33.e3.v91c1x_r5b3b3c1.qq_unique_norm_factorization_scratch.v1','role':'SCRATCH_NONCREDIT_QQ_FACTORIZATION_OF_UNIQUE_OFFBOUNDARY_FULL_SIGN_NORMS','source_locks':{'r5b3b2_sha256':B3B2_SHA,'r5b3b3b_sha256':B3B3B_SHA},'result':{'offboundary_carrier_count':len(off),'unique_norm_count':len(groups),'rows':out},'firewall':{'authority_promotion':False,'qi_irreducible_factorization_credit':False,'resolved_surface_prime_credit':False,'combined_tame_residue_credit':False,'merge_allowed':False}}
 body=dict(cert);cert['canonical_sha256']=csha(body);txt=json.dumps(cert,indent=2,sort_keys=True)+'\n'
 if a.write: OUT.write_text(txt)
 else: print(txt)
if __name__=='__main__': main()
