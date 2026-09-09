#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path
import sympy as sp
import materialize_e3_v91c1x_r5b3b3b_classify_20_novel_carriers_and_unify_27 as b3

H=Path(__file__).resolve().parent
P={
 'b3':(H/'e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json','52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e'),
 'c2c':(H/'e3-v91c1x-r5b3b3c2c-orbit-representative-strict-prime-decomposition-and-transport.json','01fc321272106a1ce7c382783c4dcb128c164d21ee4deedf4060137ef9ed971a'),
 'b2':(H/'e3-v91c1x-r5b3b3c4b2b2-remaining24-strict-prime-squareclass-partition.json','c35b8737bd310935c844b170975617e69f2745b60a932349b3c297dd6909fb27'),
 'a':(H/'e3-v91c1x-r5b3b3c4b2b2a-f4-pair-multiquadratic-residue-norm-witness.json','0defae3bd0bd809bcee4ab22fadf159b168a43c987c903b734d14f7b01478769')}
OUT=H/'e3-v91c1x-r5b3b3c4b2b2b-f14-four-residual-prime-residue-norm-witness.json'
F14='da9c1c762b7deb1ac7c630325bcfa1ee9b1a44916f5bd9df410bf16c9effd5b4'; FN='7f6274634f622b0e675111085ed050e65e4207f3f327d2c9b7a615f5f5dbf064'
AUTH='V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT'; S=['LIN_008','LIN_015','LIN_020','LIN_025']
OD={'LIN_008':['LIN_013','LIN_014'],'LIN_015':['LIN_014','LIN_019'],'LIN_020':['LIN_013','LIN_024'],'LIN_025':['LIN_019','LIN_024']}
I=sp.I; a1,a2,a3=b3.BASE; BASE=b3.BASE

def hs(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(k):
 p,e=P[k]; o=json.loads(p.read_text()); b=dict(o); c=b.pop('canonical_sha256',None)
 if c!=e or hs(b)!=e: raise SystemExit(f'lock moved: {p.name}')
 return o
def z(): return sp.Poly(0,*BASE,extension=I)
def add(x,y):
 o=dict(x)
 for m,p in y.items():
  q=o.get(m,z())+p
  if q.is_zero:o.pop(m,None)
  else:o[m]=q
 return o
def flip(e,bit):
 f=1<<bit; return {m:(-p if m&f else p) for m,p in e.items()}
def nd(enc):
 v=[b3.decode_qi(q) for q in enc]; e={}; q=v[0]*a1+v[1]*a2+v[2]*a3
 if q!=0:e[0]=sp.Poly(q,*BASE,extension=I)
 for j,c in enumerate(v[3:]):
  if c!=0:e[1<<j]=sp.Poly(c,*BASE,extension=I)
 ds=[{0:sp.Poly(1,*BASE,extension=I)}]+[{1<<j:sp.Poly(1,*BASE,extension=I)} for j in range(4)]
 for bit in range(4):
  ef=flip(e,bit); ne=b3.elem_mul(e,ef); nds=[]
  for d in ds: nds.append(add(b3.elem_mul(d,ef),b3.elem_mul(e,flip(d,bit))))
  e,ds=ne,nds
 if set(e)!={0} or any(set(d)-{0} for d in ds): raise SystemExit('derivative norm retained radicals')
 return e[0],[d.get(0,z()) for d in ds]
def rn(enc,ds):
 v=[b3.decode_qi(q) for q in enc]; d0,d1,d2,d3,d4=ds
 q=(v[0]*a1+v[1]*a2+v[2]*a3)*d0+v[3]*d1+v[4]*d2+v[5]*d3+v[6]*d4
 return sp.Poly(sp.expand(q.as_expr() if isinstance(q,sp.Poly) else q),*BASE,extension=I)
def pc(p,x):
 p=sp.Poly(p,x,extension=I).monic(); return hs({'degree':int(p.degree()),'coefficients_high_to_low_Qi':[b3.enc_qi(sp.sympify(c)) for c in p.all_coeffs()]})
def sf(p,x):
 p=sp.Poly(p,x,extension=I); _c,L=sp.sqf_list(p); q=sp.Poly(1,x,extension=I)
 for f,e in L:
  if int(e)%2:q*=sp.Poly(f,x,extension=I).monic()
 return q
def normmod(f,g,y,x):
 R=sp.resultant(f,g,y); m=int(sp.Poly(g,y).degree()); lc=sp.Poly(f,y).LC(); u=sp.cancel(R/lc**m); n,d=sp.fraction(u)
 return sf(sp.Poly(n,x,extension=I),x),sf(sp.Poly(d,x,extension=I),x),int(sp.Poly(R,x,extension=I).degree())
def combine(rows,x):
 n=sp.Poly(1,x,extension=I); d=sp.Poly(1,x,extension=I)
 for a,b,_ in rows:n*=a;d*=b
 n,d=sf(n,x),sf(d,x); g=sp.gcd(n,d)
 if not g.is_one:n=n.exquo(g);d=d.exquo(g)
 n,d=sf(n,x),sf(d,x); out=[]
 for side,p in [('NUMERATOR',n),('DENOMINATOR',d)]:
  if p.degree()>0:out.append({'side':side,'degree':int(p.degree()),'squarefree_support_sha256':pc(p,x)})
 return out

def build():
 B,C,Q,A=load('b3'),load('c2c'),load('b2'),load('a')
 if A['exact_consequence']['F4_pair_remaining_squareclass_debt_count']!=0 or A['next_exact_leaf']!='V91C1X_R5B3B3C4B2B2B_F14_FOUR_RESIDUAL_PRIME_RESIDUE_NORM_WITNESS': raise SystemExit('F4 gate moved')
 inv={r['carrier_id']:r for r in B['finite_linear_carrier_inventory']['carrier_rows']}; reps={r['carrier_id']:r for r in C['representative_strict_prime_decompositions']['rows']}
 bucket=next(r for r in Q['remaining24_partition']['rows_by_bucket'] if r['bucket']=='F14_RESIDUAL_REPEATED_FACTOR_STRICT_PRIMES')
 if bucket['carrier_ids']!=S or bucket['target_count']!=4: raise SystemExit('F14 bucket moved')
 tr={r['carrier_id']:r for r in bucket['rows']}
 N,_=nd(inv['LIN_008']['normalized_coefficients_Qi'])
 if hs(b3.normalize_norm(N))!=FN: raise SystemExit('special norm moved')
 F=N.exquo(sp.Poly(a1**2,*BASE,extension=I))
 if F.total_degree()!=14 or hs(b3.normalize_norm(F))!=F14: raise SystemExit('F14 reconstruction moved')
 x,y=a2,a3; f=sp.expand(F.as_expr().subs(a1,1)); ff=sp.Poly(f,y,domain=sp.QQ_I.frac_field(x))
 if ff.degree()<=0 or sp.Poly(F.as_expr().subs(a1,0),a2,a3,extension=I).is_zero: raise SystemExit('bad F14 chart')
 rows=[]; ns=0
 for cid in S:
  t=tr[cid]; odd=t['combined_tame_residue_odd_linear_carrier_ids']
  if odd!=OD[cid]: raise SystemExit(f'odd pair moved {cid}')
  rp=reps[cid]['special_reducible_norm_prime_decomposition_certificate']['residual_prime']
  if rp['base_factor']!='F14' or not rp['unique_minimal_prime_above_factor'] or int(rp['residue_degree'])!=1 or int(rp['local_multiplicity'])!=1: raise SystemExit(f'C2C moved {cid}')
  Nt,ds=nd(inv[cid]['normalized_coefficients_Qi'])
  if hs(b3.normalize_norm(Nt))!=FN: raise SystemExit(f'target norm moved {cid}')
  d0=sp.Poly(ds[0].as_expr().subs(a1,1),y,domain=sp.QQ_I.frac_field(x)).rem(ff)
  if d0.is_zero: raise SystemExit(f'd0 zero {cid}')
  if not sp.Poly(rn(inv[cid]['normalized_coefficients_Qi'],ds).as_expr().subs(a1,1),y,domain=sp.QQ_I.frac_field(x)).rem(ff).is_zero: raise SystemExit(f'adapter target failure {cid}')
  nr=[]; degs=[]
  for oid in odd:
   g=sp.expand(rn(inv[oid]['normalized_coefficients_Qi'],ds).as_expr().subs(a1,1))
   if sp.Poly(g,y,domain=sp.QQ_I.frac_field(x)).rem(ff).is_zero: raise SystemExit(f'odd carrier zero {cid}/{oid}')
   a,b,deg=normmod(f,g,y,x); nr.append((a,b,deg)); degs.append({'carrier_id':oid,'resultant_x_degree':deg,'numerator_y_degree':int(sp.Poly(g,y).degree())})
  sup=combine(nr,x); ok=bool(sup); ns+=int(ok)
  rows.append({'carrier_id':cid,'strict_prime_ids':t['c4a_strict_prime_ids'],'odd_residue_carrier_ids':odd,'residual_prime_residue_degree_over_F14':1,'derivative_adapter':{'scalar_derivative_nonzero_mod_F14':True,'target_linear_form_recovers_zero_mod_F14':True,'common_denominator_is_squared_in_two_carrier_product':True},'per_carrier_resultant_degrees':degs,'combined_norm_odd_squarefree_support':sup,'residue_nonsquare_certified':ok,'classification':'NONSQUARE_BY_ODD_SQUAREFREE_SUPPORT_IN_F14_TO_QI_X_NORM' if ok else 'INCONCLUSIVE_NORM_SQUARECLASS'})
 cert={'schema':'stage33.e3.v91c1x_r5b3b3c4b2b2b.f14_four_residual_prime_residue_norm_witness.v1','stage':'33-12','candidate':'V91C1X_R5B3B3C4B2B2B_F14_FOUR_RESIDUAL_PRIME_RESIDUE_NORM_WITNESS','role':'EXACT_NONCREDIT_F14_RESIDUE_NONSQUARE_WITNESS_BY_RESIDUE_DEGREE_ONE_DERIVATIVE_ADAPTER_AND_RESULTANT_NORM','entry':{'authority':AUTH,'stage33_progress':'6/11','successor_pr':1722},'source_locks':{k:v[1] for k,v in P.items()},'f14_geometry':{'shared_base_factor_sha256':F14,'total_degree':14,'a1_chart_y_degree':int(ff.degree()),'derived_as_special_sign_norm_divided_by_a1_squared':True,'residue_degree_one_locked_by_C2C':True},'residue_norm_reduction':{'target_count':4,'nonsquare_by_norm_count':ns,'remaining_squareclass_debt_count':4-ns,'rows':rows},'exact_consequence':{'F14_four_residue_nonsquare_certified_count':ns,'F14_four_remaining_squareclass_debt_count':4-ns,'F4_pair_and_F14_four_repeated_factor_debts_all_resolved_as_nonsquare':ns==4,'current_literal_eight_symbol_candidate_was_already_known_ramified_from_C4B2B1':True,'offboundary_codimension_one_residue_cancellation_verified':False,'unramifiedness_verified':False},'next_exact_leaf':'V91C1X_R5B3B3C4B2B2C_UNIQUE_C1_FACTOR_LOW_COST_RESIDUE_NORM_SWEEP' if ns==4 else 'V91C1X_R5B3B3C4B2B2B1_F14_STRONGER_SQUARECLASS_TEST','credit_firewall':{'authority_promotion':False,'hostile_audit_credit':False,'marked_brauer_image_credit':False,'offboundary_cancellation_credit':False,'unramifiedness_credit':False,'stage33_close_credit':False,'stage33_release_credit':False,'theorem_credit':False,'endpoint_credit':False,'merge_allowed':False}}
 cert['canonical_sha256']=hs(cert); return cert

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();c=build();t=json.dumps(c,indent=2,sort_keys=True)+'\n'
 if a.write:
  OUT.write_text(t);r=c['residue_norm_reduction'];print(json.dumps({'success':True,'marker':c['candidate'],'nonsquare_by_norm_count':r['nonsquare_by_norm_count'],'remaining_squareclass_debt_count':r['remaining_squareclass_debt_count'],'certificate_sha256':c['canonical_sha256'],'next_exact_leaf':c['next_exact_leaf']},sort_keys=True));return
 if not OUT.exists() or json.loads(OUT.read_text())!=c: raise SystemExit('materialized C4B2B2B differs from exact rebuild')
 print(c['canonical_sha256'])
if __name__=='__main__':main()
