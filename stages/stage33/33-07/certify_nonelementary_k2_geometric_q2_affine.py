#!/usr/bin/env python3
"""Exact pure-geometric Q[2] profile + affine compression on k=2 full-Q4 survivors."""
import hashlib,json,runpy
from collections import Counter
from pathlib import Path
H=Path(__file__).resolve().parent
Q4=H/'nonelementary-k2-geometric-full-q4-retained.json'; T=H/'picard-discriminant-compact.json'; OUT=H/'nonelementary-k2-geometric-q2-affine.json'
Q4LOCK='35e9812dc333b4e6b9ccc12965f79cafe6018883b3ae8378e1e6e6808694948c'; TLOCK='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0'
N=14; X=(1<<10)-1; Y=((1<<14)-1)^X; TARGET=(512,0,512,0)

def load(p,lock=None):
 d=json.loads(p.read_text()); s=d.get('canonical_sha256'); u=dict(d);u.pop('canonical_sha256',None);r=hashlib.sha256(json.dumps(u,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 if s!=r or (lock and s!=lock): raise SystemExit(f'hash regression: {p.name}')
 return d
q4=load(Q4,Q4LOCK); target=load(T,TLOCK)
if q4['arithmetic_generators_used']!=[] or not q4['full_Q4_condition_certified_for_k2']: raise SystemExit('Q4 firewall/cert regression')
runpy.run_path(str(H/'prepare_nonelementary_k2_geometric_q4_manifest.py'))
man=load(H/'nonelementary-k2-geometric-q4-manifest.json')
if man['arithmetic_generators_used']!=[] or man['source_geometric_support_sha256']!=q4['source_geometric_support_sha256']: raise SystemExit('manifest firewall/hash regression')

def canon(rows):
 p={}
 for z in rows:
  z=int(z)
  for k in sorted(p,reverse=True):
   if z>>k&1:z^=p[k]
  if not z:continue
  k=z.bit_length()-1
  for o in list(p):
   if p[o]>>k&1:p[o]^=z
  p[k]=z
 return tuple(p[k] for k in sorted(p,reverse=True))
def dot(a,b): return (int(a)&int(b)).bit_count()&1
def span(b):
 a=[0]
 for r in b:a += [x^int(r) for x in a]
 return tuple(a)
def null(rows,n=N):
 a=list(canon(rows)); rank=0;piv=[]
 for c in range(n):
  i=next((i for i in range(rank,len(a)) if a[i]>>c&1),None)
  if i is None:continue
  a[rank],a[i]=a[i],a[rank]
  for j in range(len(a)):
   if j!=rank and a[j]>>c&1:a[j]^=a[rank]
  piv.append(c);rank+=1
  if rank==len(a):break
 out=[]
 for f in [c for c in range(n) if c not in piv]:
  v=1<<f
  for r,c in zip(a[:rank],piv):
   if r>>f&1:v|=1<<c
  out.append(v)
 out=canon(out)
 if len(out)!=n-len(canon(rows)) or any(dot(x,y) for x in rows for y in out):raise SystemExit('nullspace regression')
 return out
def arref(rows):
 p={};allm=(1<<N)-1
 for m,r in rows:
  z=int(m)|((int(r)&1)<<N); c=z&allm
  while c:
   k=c.bit_length()-1
   if k in p:z^=p[k];c=z&allm
   else:
    for o in list(p):
     if p[o]>>k&1:p[o]^=z
    p[k]=z;break
  if not c and z>>N&1:return None
 return tuple(p[k] for k in sorted(p,reverse=True))
def sat(sol,rref):
 for z in rref:
  if dot(sol,z&((1<<N)-1)) != (z>>N&1):return False
 return True
def qhalf(lo,hi):
 lx=lo&X;ly=(lo&Y)>>10;hx=hi&X;hy=(hi&Y)>>10
 return (lx.bit_count()+4*hx.bit_count()+4*(lx&hx).bit_count()+2*ly.bit_count()+8*hy.bit_count()+8*(ly&hy).bit_count())%16
def corr(qb,i):
 z=0
 for b,v in enumerate(qb):
  if i>>b&1:z^=int(v)
 return z
def uprof(lo,hi,W):
 c=[0]*4; odd=bool(lo&X)
 for w in W:
  v=qhalf(lo,hi^w)
  if v%4:raise SystemExit('Q2 support regression')
  c[v//4]+=1;c[((v+8)%16)//4 if odd else v//4]+=1
 return tuple(c)
def twoq(w):
 w=canon(w); c=Counter()
 for v in span(null(w)):
  c[(4*(v&X).bit_count()+2*(v>>10).bit_count())%16]+=1
 m=1<<len(w);p={k:v*m for k,v in sorted(c.items())}
 if sum(p.values())!=16384:raise SystemExit('2Q cardinality')
 return p
# endpoint Q[2]
mods=list(map(int,target['discriminant_moduli'])); raw=target['discriminant_bilinear_numerator_over_8_reduced']; B=[[-int(x)%(16 if i==j else 8) for j,x in enumerate(row)] for i,row in enumerate(raw)]; ep=Counter()
for m in range(1<<14):
 v=[mods[i]//2 if m>>i&1 else 0 for i in range(14)];ep[sum(v[i]*B[i][j]*v[j] for i in range(14) for j in range(14))%16]+=1
if dict(sorted(ep.items()))!={0:8192,8:8192}:raise SystemExit('endpoint Q2 regression')
# retained bitset
bb=bytes.fromhex(q4['full_Q4_surviving_orbit_bitset_hex']); bits=int.from_bytes(bb,'little'); ids=tuple(i for i in range(1496) if bits>>i&1)
if len(bb)!=(1496+7)//8 or bits>>1496 or len(ids)!=867:raise SystemExit('Q4 bitset regression')
R=[]; gh=Counter();ot=Counter();tb=Counter();ta=Counter();rb=ra=wb=wa=0
for oi in ids:
 r=man['records'][oi]; p=tuple(map(int,r['P_basis_bits']));w=tuple(map(int,r['W_basis_bits']));qb=tuple(map(int,r['quotient_basis_bits']));base=tuple(map(int,r['base_affine_rref_augmented']));osz=int(r['orbit_size']);t=int(r['t']);eq=int(r['section_equation_rank']);n=int(r['representative_section_count'])
 if twoq(w)!={0:8192,8:8192}:raise SystemExit('2Q profile mismatch')
 W=span(w); cs=tuple(corr(qb,i) for i in range(128)); z0=uprof(0,0,W);A=tuple(uprof(p[0],c,W) for c in cs);C=tuple(uprof(p[1],c,W) for c in cs);carry=p[0]&p[1];D=tuple(uprof(p[0]^p[1],c^carry,W) for c in cs)
 passv=[];lh=Counter()
 for a in range(128):
  for b in range(128):
   sol=a|(b<<7)
   if not sat(sol,base):continue
   pr=tuple(z0[i]+A[a][i]+C[b][i]+D[a^b][i] for i in range(4));lh[pr]+=1;gh[pr]+=1
   if pr==TARGET:passv.append(sol)
 if sum(lh.values())!=n or len(passv)*4!=n:raise SystemExit('Q2 count/ratio regression')
 x0=passv[0]; dif=canon(x^x0 for x in passv[1:])
 if len(passv)!=(1<<len(dif)):raise SystemExit('Q2 non-affine')
 rr=arref((m,dot(m,x0)) for m in null(dif))
 if rr is None or len(rr)!=eq+2 or 14-len(rr)!=len(dif):raise SystemExit('Q2 affine rank regression')
 if {s for s in range(1<<14) if sat(s,rr)}!=set(passv):raise SystemExit('Q2 affine membership regression')
 rb+=n;ra+=len(passv);wb+=osz*n;wa+=osz*len(passv);tb[t]+=n;ta[t]+=len(passv);ot[(t,eq,len(dif))]+=1
 R.append({'orbit_index':oi,'orbit_size':osz,'t':t,'base_section_equation_rank':eq,'full_Q4_representative_sections':n,'Q2_profile_surviving_representative_sections':len(passv),'weighted_H_before_Q2_profile':osz*n,'weighted_H_after_Q2_profile':osz*len(passv),'Q2_survivor_affine_dimension':len(dif),'Q2_survivor_affine_rref_augmented':list(rr),'exact_2Q_profile_matches_endpoint':True,'Q2_profile_histogram_unit_counts':{','.join(map(str,k)):v for k,v in sorted(lh.items())}})
if (rb,ra,wb,wa)!=(8732672,2183168,517873664,129468416):raise SystemExit(f'global count regression {(rb,ra,wb,wa)}')
EXP={(256,256,256,256):5683200,(512,0,512,0):2183168,(256,128,256,384):491776,(256,384,256,128):374528}
if dict(gh)!=EXP:raise SystemExit('global Q2 histogram regression')
cert={'schema':'STAGE33_07_NONELEMENTARY_K2_GEOMETRIC_Q2_AFFINE_V1','source_Q4_retained_sha256':Q4LOCK,'source_full_Q4_aggregate_sha256':q4['source_full_Q4_aggregate_sha256'],'source_geometric_support_sha256':man['source_geometric_support_sha256'],'source_endpoint_picard_discriminant_sha256':TLOCK,'arithmetic_generators_used':[],'firewall':'PURE_GEOMETRIC_PREDECESSOR_AND_FINITE_Q_ONLY__NO_ARITHMETIC_CC_CT','endpoint_Q2_quadratic_value_profile_numerator_over_8':{'0':8192,'8':8192},'endpoint_2Q_quadratic_value_profile_numerator_over_8':{'0':8192,'8':8192},'all_867_full_Q4_survivor_orbits_match_exact_endpoint_2Q_profile':True,'full_Q4_surviving_orbit_count':867,'full_Q4_representative_sections_before_Q2_profile':rb,'full_Q4_weighted_H_before_Q2_profile':wb,'Q2_profile_surviving_orbit_families':867,'Q2_profile_surviving_representative_sections':ra,'Q2_profile_surviving_weighted_H':wa,'Q2_profile_survival_ratio':'1/4 in every one of 867 orbit families','all_Q2_survivor_sets_are_single_affine_subspaces':True,'extra_independent_affine_equations_per_orbit':2,'orbit_profile_by_t_baseeqrank_Q2affinedim':{f't={t},baseeqrank={e},q2dim={d}':v for (t,e,d),v in sorted(ot.items())},'representative_sections_by_t_before_Q2':{str(k):v for k,v in sorted(tb.items())},'representative_sections_by_t_after_Q2':{str(k):v for k,v in sorted(ta.items())},'global_Q2_profile_histogram_unit_counts':{','.join(map(str,k)):v for k,v in sorted(gh.items())},'records':R,'full_Q4_condition_inherited_certified':True,'exact_Q2_quadratic_profile_certified':True,'exact_2Q_quadratic_profile_certified':True,'Q2_survivor_affine_compression_certified':True,'full_finite_q_isometry_certified':False,'endpoint_finite_q_certified':False,'endpoint_full_action_certified':False,'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'next_exact_leaf':'L33-07-CLASSIFY-FULL-FINITE-Q-ISOMETRY-ON-867-K2-Q2-AFFINE-FAMILIES','unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest();OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'representative_sections_after_Q2':ra,'weighted_H_after_Q2':wa,'all_Q2_survivors_affine':True,'certificate_sha256':cert['canonical_sha256'],'next':cert['next_exact_leaf']},indent=2,sort_keys=True))
