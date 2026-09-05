#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from itertools import product
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09D/q-defined-pencil-fibration-preflight.json'
INVENTORY=ROOT/'stages/stage36/36-02/representative-inventory.json'
PHYSICAL=ROOT/'stages/stage36/36-03/physical-open-boundary.json'
ADAPTER=ROOT/'stages/stage29/29-02hb/campedelli-quotient-adapter.md'
PREV=ROOT/'stages/stage36/36-09C/single-place-direct-receiver-obstruction-preflight.json'
ARSENAL_MW=ROOT/'docs/arsenal/cards/formal/S34-W02.md'
CERT_BLOB='7fb67b8bf5a37d16ef527aea6109eb0782d61201'
EXPECTED_BASE='591e513ad5d7f3f8824f14c6ce529125b0a4f193'

LOCKS={
 INVENTORY:'88130b9380a677a191f91c24df87618e65be0a2f',
 PHYSICAL:'fc1947b2de08f7d8a104bdc91902b20e88635349',
 ADAPTER:'5f959d60106243bb31df06a3961ab04182d78fc7',
 PREV:'67fd5cd61ef35582dce32811aac4bebdb9356138',
 ARSENAL_MW:'13d41be776fcd2edcd258f11bd28c5a6596de45b',
}
MOVING=['A3','B2','B1','C']
POINT={'A3':'0','B2':'-t','B1':'-1','C':'-(t+1)'}
SET_TYPE={
 frozenset(['B2','B1','C','INF']):'J_MINUS',
 frozenset(['A3','B2','B1','INF']):'J_MINUS',
 frozenset(['A3','B2','C','INF']):'J_PLUS',
 frozenset(['A3','B1','C','INF']):'J_PLUS',
}


def req(ok:bool,msg:str)->None:
 if not ok: raise SystemExit(msg)
def blob(p:Path)->str:
 b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def bits(s:str)->tuple[int,...]: return tuple(int(x) for x in s)
def xor(vs):
 out=[0,0,0]
 for v in vs: out=[a^b for a,b in zip(out,v)]
 return tuple(out)
def dot(a,b): return sum(x*y for x,y in zip(a,b))%2
def rank_f2(rows):
 a=[list(r) for r in rows if any(r)]; rank=0; col=0
 while col<3 and rank<len(a):
  pivot=next((i for i in range(rank,len(a)) if a[i][col]),None)
  if pivot is None: col+=1; continue
  a[rank],a[pivot]=a[pivot],a[rank]
  for i in range(len(a)):
   if i!=rank and a[i][col]: a[i]=[x^y for x,y in zip(a[i],a[rank])]
  rank+=1; col+=1
 return rank

# low-to-high integer polynomial helpers
def trim(a):
 a=list(a)
 while len(a)>1 and a[-1]==0: a.pop()
 return a
def padd(a,b):
 n=max(len(a),len(b)); return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)])
def pneg(a): return [-x for x in a]
def psub(a,b): return padd(a,pneg(b))
def pmul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b): out[i+j]+=x*y
 return trim(out)
def ppow(a,n):
 out=[1]
 for _ in range(n): out=pmul(out,a)
 return out
def pscale(a,c): return trim([c*x for x in a])

def j_from_lambda(n,d):
 A=padd(psub(pmul(d,d),pmul(n,d)),pmul(n,n))
 num=pscale(ppow(A,3),256)
 den=pmul(pmul(pmul(d,d),pmul(n,n)),ppow(psub(d,n),2))
 return trim(num),trim(den)

def expected_j(kind):
 if kind=='J_MINUS':
  q=[1,-1,1]; den=pmul([0,0,1],[1,-2,1])
 else:
  q=[1,1,1]; den=pmul([0,0,1],[1,2,1])
 return pscale(ppow(q,3),256),trim(den)


def main()->None:
 req(blob(CERT)==CERT_BLOB,'36-09D certificate blob drift')
 for p,sha in LOCKS.items(): req(blob(p)==sha,f'locked source drift: {p}')
 c=json.loads(CERT.read_text())
 req(c.get('schema')=='STAGE36_36_09D_Q_DEFINED_PENCIL_FIBRATION_PREFLIGHT_V1','36-09D schema moved')
 req(c.get('base_main_sha')==EXPECTED_BASE,'36-09D base moved')
 entry=c.get('entry_authority',{})
 req(entry=={'stage36_36_09C_promotion_pr':1589,'promotion_exact_head':'6e0c40eeb7a533b47aba0d224c34e85822db373c','promotion_exact_head_ci_run':33955369695,'promotion_exact_head_ci_job':101277643284,'promotion_merged_main_sha':EXPECTED_BASE,'selected_route':'B6_FIBRATION_TO_CURVE_BASE'},'36-09D entry authority moved')

 p=json.loads(PHYSICAL.read_text())
 req(p['global_quotient_chain']['Q_defined'] is True and p['global_quotient_chain']['H_torsor_degree']==8,'exact quotient chain moved')
 req(p['seven_line_base']['coordinates']=='[x:y:z]=[a1^2:a2^2:a3^2]','base-square coordinates moved')
 req(p['physical_open']['side_coordinates_nonzero']==['a1','a2','a3'],'physical side open moved')
 req(p['seven_line_base']['line_coefficients']=={'A1':[1,0,0],'A2':[0,1,0],'A3':[0,0,1],'B3':[1,1,0],'B2':[1,0,1],'B1':[0,1,1],'C':[1,1,1]},'seven-line arrangement moved')
 adapter=ADAPTER.read_text()
 for text in ['Cbar_H := Sbar/H.','deg(beta_H)=8','both `Cbar_H=Sbar/H` and the resolved quotient `C_H=S/H` are Q-defined']:
  req(text in adapter,f'quotient adapter source phrase missing: {text}')
 prev=json.loads(PREV.read_text())
 req(prev['post_block_cycle_audit']['selected_next_candidate']=='B6_FIBRATION_TO_CURVE_BASE','36-09C selected route moved')
 req(prev['post_block_cycle_audit']['next_route_after_hostile_audit']=='36-09D_Q_DEFINED_PENCIL_FIBRATION_PREFLIGHT','36-09D predecessor route moved')
 mw=ARSENAL_MW.read_text()
 for text in ['GLOBAL_MORDELL_WEIL_CONGRUENCE_EXCLUSION','a proved full MW basis/generator and complete torsion subgroup','exact quotient-to-parent receiver functions']:
  req(text in mw,f'S34-W02 hypothesis phrase missing: {text}')

 pencil=c['q_defined_pencil']
 req(pencil['map']=='t=x/y on the exact quotient-to-P2 base' and pencil['q_defined'] is True,'Q-defined pencil moved')
 req(pencil['physical_parameter']=='t=(a1/a2)^2' and pencil['physical_parameter_is_positive_rational_square'] is True,'physical base-square condition moved')
 req(pencil['generic_affine_chart']=='y=1, x=t, z=s','generic affine chart moved')
 req(pencil['special_parameters_requiring_separate_treatment']==['0','1','-1','infinity'],'special base set moved')
 req(pencil['physical_special_parameters_not_automatically_eliminated']==['1'],'physical t=1 firewall moved')
 common=c['generic_fiber_common_geometry']
 req(common['moving_branch_lines_in_s']==MOVING and common['finite_branch_points']==POINT,'generic moving branch data moved')
 req(common['degree']==8 and common['branch_point_count_including_infinity']==5,'generic degree/branch count moved')
 req(common['riemann_hurwitz']=='2g-2=8*(-2)+5*8*(1-1/2)=4' and common['generic_fiber_genus']==3,'Riemann-Hurwitz result moved')

 inv=json.loads(INVENTORY.read_text())
 reps=inv['representatives']
 expected_cert=c['representative_fibers']
 all_j_multisets=[]
 for name in ['Q6_GEOM8','Q2_GEOM8','Q2_GEOM2']:
  labels=reps[name]['label_map']
  finite={L:bits(labels[L]) for L in MOVING}
  req(rank_f2(finite.values())==3,f'{name}: finite inertia rank is not 3')
  infinity=xor(finite.values())
  declared=expected_cert[name]
  req(declared['finite_inertia']=={L:''.join(map(str,finite[L])) for L in MOVING},f'{name}: finite inertia declaration moved')
  req(declared['infinity_inertia']==''.join(map(str,infinity)),f'{name}: infinity inertia moved')
  inertias={**finite,'INF':infinity}
  genus1=[]; genus0=0
  for ch in product([0,1],repeat=3):
   if ch==(0,0,0): continue
   br=[L for L,v in inertias.items() if dot(ch,v)]
   req(len(br) in (2,4),f'{name}: unexpected character branch count {ch}: {br}')
   g=(len(br)-2)//2
   if g==0: genus0+=1
   elif g==1:
    kind=SET_TYPE.get(frozenset(br))
    req(kind is not None,f'{name}: unknown genus1 branch set {br}')
    genus1.append({'character':''.join(map(str,ch)),'branch_lines':br,'j_type':kind})
   else: req(False,f'{name}: unexpected character genus {g}')
  req(genus0==4 and len(genus1)==3,f'{name}: character genus inventory moved')
  req(genus1==declared['genus1_characters'],f'{name}: exact genus1 character table moved')
  all_j_multisets.append(sorted(x['j_type'] for x in genus1))
 req(all(x==['J_MINUS','J_MINUS','J_PLUS'] for x in all_j_multisets),'j multiset differs across representatives')

 lambdas={
  'J_MINUS_1':([-1],[-1,1],'J_MINUS'),
  'J_MINUS_2':([1],[0,1],'J_MINUS'),
  'J_PLUS_1':([1,1],[0,1],'J_PLUS'),
  'J_PLUS_2':([1,1],[1],'J_PLUS'),
 }
 for key,(n,d,kind) in lambdas.items():
  got=j_from_lambda(n,d); exp=expected_j(kind)
  req(got==exp,f'exact j polynomial identity failed for {key}: {got} != {exp}')
 qi=c['character_quotient_inventory']
 req(qi['nontrivial_characters_each']==7 and qi['genus1_character_quotients_each']==3 and qi['genus0_character_quotients_each']==4,'character counts moved')
 req(qi['j_functions']=={'J_MINUS':'256*(t^2-t+1)^3/(t^2*(t-1)^2)','J_PLUS':'256*(t^2+t+1)^3/(t^2*(t+1)^2)'},'recorded j formulas moved')
 req(qi['j_multiset_each_representative']==['J_MINUS','J_MINUS','J_PLUS'],'recorded j multiset moved')
 req(qi['both_j_functions_nonconstant'] is True and qi['fixed_elliptic_curve_reduction_obtained'] is False,'moving-family firewall moved')

 route=c['route_decision']
 req(route['B6_FIBRATION_TO_CURVE_BASE']=='LIVE_GENUS3_WITH_THREE_MOVING_ELLIPTIC_CHARACTER_QUOTIENTS','B6 route status moved')
 req(route['S34_W02_TRIGGERED'] is False,'S34-W02 falsely triggered')
 req(route['next_route_after_hostile_audit']=='36-09E_CHARACTER_ELLIPTIC_QUOTIENT_ARITHMETIC_PREFLIGHT','36-09E routing moved')
 req(c['cycle_update']['new_material_block'] is False and c['cycle_update']['B6_remains_sole_live'] is True,'cycle continuation moved')
 req(all(v is False for v in c['claims'].values()),'36-09D higher credit leaked')
 print('PASS STAGE36_36_09D_Q_DEFINED_PENCIL_FIBRATION_PREFLIGHT')
 print('generic_fiber=connected degree8 genus3; branch_count=5; character_quotients=3 genus1 + 4 genus0')
 print('j_multiset_each=[J_MINUS,J_MINUS,J_PLUS]; both moving; t=1 special retained')
 print('B6=LIVE; S34-W02 not triggered; next=36-09E pending hostile audit')

if __name__=='__main__': main()
