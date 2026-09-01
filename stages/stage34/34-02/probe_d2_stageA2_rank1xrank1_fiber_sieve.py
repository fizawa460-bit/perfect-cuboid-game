#!/usr/bin/env python3
from __future__ import annotations
import collections,json,pathlib,runpy
from fractions import Fraction
from math import gcd,lcm
ROOT=pathlib.Path(__file__).resolve().parent
ns=runpy.run_path(str(ROOT/"run_d2_stageA2_rank1_mw_congruence_sieve.py"))
sel=ns["sel"]; gens1=ns["gens"]
add=json.loads((ROOT/"d2-stageA2-additional-rank1-selection.json").read_text())
mw2=json.loads((ROOT/"d2-stageA2-additional-rank1-mw-default.json").read_text())
gens2={int(x["model_id"]):ns["parse_gen"](x["mwrank_o_line"]) for x in mw2["models"]}
brmap={x["branch_id"]:x for x in sel["branches"]}
CAP=120000;MAX_PRIMES=8;BOUND=211

def bd_pair(br,mid,pair,G):
 ent=next(x for x in br["pair_ranks"] if x["pair"]==pair and int(x["model_id"])==mid);s=int(ent["squareclass"]);q=br["q"];f1,f2=pair.split('*');roots1=ns["roots_form"](q,f1);r=next(x for x in roots1 if x is not None)
 A,B,C,D,pp,qq=ns["direct_cubic"](q,pair,s,r);a4=Fraction(int(ent["a4"]));a6=Fraction(int(ent["a6"]));assert a4==81*pp and a6==729*qq
 roots=roots1+ns["roots_form"](q,f2);assert len(roots)==4 and len(set(roots))==4;tors=[None]
 for rr in roots:
  if rr==r:continue
  x=3*B if rr is None else 9*A/(rr-r)+3*B;assert x**3+a4*x+a6==0;tors.append((x,Fraction(0)))
 assert len(tors)==4;assert G[1]**2==G[0]**3+a4*G[0]+a6
 return {"mid":mid,"pair":pair,"s":s,"q":q,"r":r,"A":A,"B":B,"a4":a4,"a6":a6,"tors":tors,"G":G}
def tkey(T,S,p):return ("inf",) if S%p==0 else (T*pow(S,-1,p)%p,)
def local_tables(br,bd,p):
 if not ns["good_prime_for_branch"](br,bd,p):return None
 a4=int(bd["a4"])%p;a6=int(bd["a6"])%p;G=ns["reduce_point"](bd["G"],p);m=ns["point_order"](G,p,a4,a6);tors=[ns["reduce_point"](T,p) for T in bd["tors"]]
 out=[]
 for Ti in tors:
  tab=collections.defaultdict(list);nG=None
  for n in range(m):
   R=ns["point_add"](nG,Ti,p,a4);T,S=ns["tproj_from_E"](R,bd,p)
   if ns["branch_pass_mod"](br,T,S,p):tab[tkey(T,S,p)].append(n)
   nG=ns["point_add"](nG,G,p,a4)
  out.append(tab)
 return m,out
def local_pairs(br,b1,b2,p):
 x=local_tables(br,b1,p);y=local_tables(br,b2,p)
 if x is None or y is None:return None
 m1,t1=x;m2,t2=y;arr=[]
 for i in range(4):
  for j in range(4):
   pairs=set()
   for k in set(t1[i])&set(t2[j]):
    for a in t1[i][k]:
     for b in t2[j][k]:pairs.add((a,b))
   arr.append(pairs)
 return m1,m2,arr
def combine(states,M,N,allowed,m1,m2):
 out=set()
 for a,b in states:
  for u,v in allowed:
   x=ns["crt_pair"](a,M,u,m1);y=ns["crt_pair"](b,N,v,m2)
   if x is not None and y is not None:
    out.add((x[0],y[0]))
    if len(out)>CAP:return None,None,None
 return out,lcm(M,m1),lcm(N,m2)
def sieve(br,b1,b2):
 cand=[]
 for p in ns["primes"](BOUND):
  z=local_pairs(br,b1,b2,p)
  if z is None:continue
  m1,m2,arr=z
  if sum(len(s) for s in arr)<16*m1*m2:cand.append((p,m1,m2,arr))
 states=[{(0,0)} for _ in range(16)];Ms=[1]*16;Ns=[1]*16;used=[];remaining=cand[:]
 for _ in range(MAX_PRIMES):
  best=None
  for p,m1,m2,arr in remaining:
   ss=[];mm=[];nn=[];bad=False
   for k in range(16):
    a,b,c=combine(states[k],Ms[k],Ns[k],arr[k],m1,m2)
    if a is None:bad=True;break
    ss.append(a);mm.append(b);nn.append(c)
   if bad:continue
   score=(sum(len(x) for x in ss),max(len(x) for x in ss),p)
   if best is None or score<best[0]:best=(score,p,m1,m2,arr,ss,mm,nn)
  if best is None:break
  _,p,m1,m2,arr,states,Ms,Ns=best;used.append({"p":p,"ord1":m1,"ord2":m2,"state_counts":[len(x) for x in states]});remaining=[z for z in remaining if z[0]!=p]
  if all(not x for x in states):break
 return all(not x for x in states),used,[len(x) for x in states]
closed=[];details=[]
for rec in add["branches"]:
 br=brmap[rec["branch_id"]];b1=ns["branch_data"](br,gens1);mid2=int(rec["selected_model_id"]);best=None
 for pair2 in rec["pair_occurrences"]:
  b2=bd_pair(br,mid2,pair2,gens2[mid2]);ok,used,counts=sieve(br,b1,b2);row={"q":br["q"],"branch_id":br["branch_id"],"model1":b1["mid"],"pair1":b1["pair"],"model2":mid2,"pair2":pair2,"closed":ok,"used":[[u["p"],u["ord1"],u["ord2"]] for u in used],"final_nonempty_torsion_pairs":sum(c>0 for c in counts),"max_final_states":max(counts) if counts else 0};details.append(row)
  if ok:best=row;break
 if best:closed.append(best)
cc=collections.Counter(x["q"] for x in closed)
print("RANK1XRANK1_FIBER_PROBE="+json.dumps({"status":"DIAGNOSTIC_NO_CREDIT","input_branches":28,"closed_count":len(closed),"closed_by_q":dict(sorted(cc.items())),"remaining_from_52":52-len(closed),"closed":closed},sort_keys=True))
