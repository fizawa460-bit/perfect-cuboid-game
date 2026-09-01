#!/usr/bin/env python3
from __future__ import annotations
import collections,json,math,pathlib,runpy
from fractions import Fraction
ROOT=pathlib.Path(__file__).resolve().parent
base=runpy.run_path(str(ROOT/"probe_d2_stageA2_rank1xrank1_fiber_sieve.py"))
details=base["details"];brmap=base["brmap"];gens1=base["gens1"];gens2=base["gens2"];ns=base["ns"];bd_pair=base["bd_pair"]

def qadd(P,Q,a4):
 if P is None:return Q
 if Q is None:return P
 x1,y1=P;x2,y2=Q
 if x1==x2 and y1==-y2:return None
 if P==Q:
  if y1==0:return None
  lam=(3*x1*x1+a4)/(2*y1)
 else:lam=(y2-y1)/(x2-x1)
 x3=lam*lam-x1-x2;y3=lam*(x1-x3)-y1
 return x3,y3
def qneg(P):return None if P is None else (P[0],-P[1])
def qmul(n,P,a4):
 if n<0:return qmul(-n,qneg(P),a4)
 R=None;Q=P
 while n:
  if n&1:R=qadd(R,Q,a4)
  Q=qadd(Q,Q,a4);n//=2
 return R
def epoint(n,T,bd):return qadd(qmul(n,bd["G"],bd["a4"]),bd["tors"][T],bd["a4"])
def texact(P,bd):
 if P is None:return ("finite",bd["r"])
 x=P[0];den=x-3*bd["B"]
 if den==0:return ("infinity",None)
 return ("finite",bd["r"]+9*bd["A"]/den)
def forms(q,t):
 a,b=map(int,q.split('/'))
 if t[0]=="infinity":U,V=Fraction(1),Fraction(0)
 else:
  z=t[1];U=z*z-1;V=2*z
 return [U,V,a*U+b*V,b*U+a*V]
def ratsq(x):
 if x<0:return False
 return math.isqrt(x.numerator)**2==x.numerator and math.isqrt(x.denominator)**2==x.denominator
def tstr(t):return "infinity" if t[0]=="infinity" else str(t[1])

def classify(br,t):
 F=forms(br["q"],t);zeros=[n for n,v in zip(["U","V","A","B"],F) if v==0]
 parent=all(ratsq(v/Fraction(int(d))) for v,d in zip(F,br["delta"]))
 return F,zeros,parent
rows=[];eq=0;parentok=0;deg=0;nondeg=0
for d in details:
 br=brmap[d["branch_id"]];b1=ns["branch_data"](br,gens1);b2=bd_pair(br,int(d["model2"]),d["pair2"],gens2[int(d["model2"])])
 assert len(d["surviving_classes"])==1;c=d["surviving_classes"][0]
 checks=[]
 for z in c["residue_pairs"]:
  n=int(z["n_symmetric"]);m=int(z["m_symmetric"]);t1=texact(epoint(n,int(c["torsion1_index"]),b1),b1);t2=texact(epoint(m,int(c["torsion2_index"]),b2),b2);same=t1==t2
  chk={"n":n,"m":m,"t1":tstr(t1),"t2":tstr(t2),"same_t":same}
  if same:
   eq+=1;F,zeros,pok=classify(br,t1);chk.update({"parent_squareconditions_exact":pok,"zero_factors":zeros,"receiver_exception_type":"torsion_or_origin" if zeros else "none"})
   if pok:
    parentok+=1
    if zeros:deg+=1
    else:nondeg+=1
  checks.append(chk)
 rows.append({"q":br["q"],"branch_id":br["branch_id"],"model1":d["model1"],"pair1":d["pair1"],"model2":d["model2"],"pair2":d["pair2"],"torsion_pair":[c["torsion1_index"],c["torsion2_index"]],"moduli":[c["n_modulus"],c["m_modulus"]],"exact_representative_checks":checks})
summary={"status":"DIAGNOSTIC_NO_CREDIT","tested_maps":len(rows),"tested_small_representatives":sum(len(x["exact_representative_checks"]) for x in rows),"exact_same_t_representatives":eq,"exact_parent_squarecondition_representatives":parentok,"exact_degenerate_parent_representatives":deg,"exact_nondegenerate_parent_representatives":nondeg,"same_t_by_q":dict(sorted(collections.Counter(x["q"] for x in rows for z in x["exact_representative_checks"] if z["same_t"]).items())),"rows":rows,"firewalls":{"finite_residue_class_is_exact_representative":False,"small_symmetric_representative_exhausts_congruence_class":False,"degenerate_representative_closes_padic_disk":False,"R29_EXT_CHANG_C_closed":False}}
print("RANK1XRANK1_EXACT_REPRESENTATIVE_PROBE="+json.dumps(summary,sort_keys=True))
