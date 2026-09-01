#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, math, pathlib, re, subprocess
from fractions import Fraction

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-full-support-projective.json"
LOCK=ROOT/"d2-stageA2-rankzero-AB-complete-pullback-lock.json"
OUT=ROOT/"d2-stageA2-rankzero-AB-complete-pullback.json"
RAW=ROOT/"d2-stageA2-rankzero-AB-complete-pullback-stdout.txt"
TIMEOUT=120
TARGETS={
 "20/21":{"a":20,"b":21,"s":-105,"count":12,"a4":-3366636380100,"a6":-2377617087993840000,"roots":[Fraction(2,5),Fraction(3,7),Fraction(-5,2),Fraction(-7,3)]},
 "80/39":{"a":80,"b":39,"s":-195,"count":4,"a4":-932895725264100,"a6":-10508610941884186560000,"roots":[Fraction(3,13),Fraction(5,8),Fraction(-8,5),Fraction(-13,3)]}
}

def factor(n:int):
    n=abs(n); out=[]; p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p=3 if p==2 else p+2
    if n>1:out.append(n)
    return out

def sf(n:int)->int:
    sign=-1 if n<0 else 1; n=abs(n); out=1
    for p in factor(n):
        parity=0
        while n%p==0:n//=p; parity^=1
        if parity:out*=p
    return sign*out

def h(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def square_fraction(q:Fraction)->bool:
    if q<0:return False
    return math.isqrt(q.numerator)**2==q.numerator and math.isqrt(q.denominator)**2==q.denominator

def forms(a:int,b:int,t:Fraction):
    U=t*t-1; V=2*t; A=a*U+b*V; B=b*U+a*V
    return U,V,A,B

def invariants(coeff):
    a,b,c,d,e=coeff
    I=12*a*e-3*b*d+c*c
    J=72*a*c*e+9*b*c*d-27*a*d*d-27*b*b*e-2*c*c*c
    return I,J

def quartic_coeff(a:int,b:int,s:int):
    # A=a*t^2+2*b*t-a; B=b*t^2+2*a*t-b.
    q1=[a,2*b,-a]; q2=[b,2*a,-b]; out=[0]*5
    for i,x in enumerate(q1):
        for j,y in enumerate(q2):out[i+j]+=s*x*y
    return out

def pari_rank_torsion(a4:int,a6:int):
    program=(f"E=ellinit([0,0,0,{a4},{a6}]);R=ellrank(E,0);T=elltors(E);"
             "print(\"STAGE34_RANK=\",R[1],\",\",R[2]);"
             "print(\"STAGE34_TORS=\",T[1]);quit;\n")
    proc=subprocess.run(["gp","-q","-f"],input=program,text=True,capture_output=True,timeout=TIMEOUT)
    txt=proc.stdout+("\nSTDERR:\n"+proc.stderr if proc.stderr else "")
    mr=re.search(r"STAGE34_RANK=(-?\d+),(-?\d+)",txt); mt=re.search(r"STAGE34_TORS=(\d+)",txt)
    if proc.returncode!=0 or not mr or not mt:raise RuntimeError(f"PARI parse/process failure a4={a4} a6={a6}: {txt}")
    lo,hi=map(int,mr.groups()); tors=int(mt.group(1))
    return lo,hi,tors,txt

lock=json.loads(LOCK.read_text()); data=json.loads(SRC.read_text())
assert lock["status"]=="SOURCE_LOCKED_PREEXECUTION"
assert data["status"]=="PASS_EXACT_FULL_SUPPORT_PROJECTIVE_REDUCTION"
assert data["remaining_d1"]==92 and data["remaining_d2"]==0
raw=[]; quotient_cert=[]
for q,tgt in TARGETS.items():
    a,b,s=tgt["a"],tgt["b"],tgt["s"]
    coeff=quartic_coeff(a,b,s); I,J=invariants(coeff); a4=-27*I; a6=-27*J
    assert (a4,a6)==(tgt["a4"],tgt["a6"])
    roots=[]
    h0=math.isqrt(a*a+b*b); assert h0*h0==a*a+b*b
    roots.extend([Fraction(-b+h0,a),Fraction(-b-h0,a)])
    roots.extend([Fraction(-a+h0,b),Fraction(-a-h0,b)])
    assert set(roots)==set(tgt["roots"]) and len(set(roots))==4
    for t in roots:
        U,V,A,B=forms(a,b,t); assert A==0 or B==0
    leading=coeff[0]
    assert leading<0 and math.isqrt(-leading)**2==-leading
    lo,hi,tors,txt=pari_rank_torsion(a4,a6); raw.append(f"===== {q} a4={a4} a6={a6} =====\n{txt}")
    assert (lo,hi)==(0,0) and tors==4
    quotient_cert.append({
      "q":q,"a":a,"b":b,"pair":"A*B","squareclass":s,
      "quartic_coefficients_t4_to_t0":coeff,
      "finite_rational_points":[{"t":str(t),"Y":0} for t in tgt["roots"]],
      "rational_points_at_infinity":0,
      "rank_interval":[lo,hi],"jacobian_torsion_order":tors,
      "complete_Q_point_count":4,
      "pointset_complete_reason":"four explicit rational branch points + rational basepoint identifies the smooth genus-one quartic with its rank-zero Jacobian of torsion order four; negative-square leading coefficient gives no rational points at infinity"
    })

branches=[]
for rec in data["cases"]:
    if int(rec["d"])!=1 or rec["q"] not in TARGETS:continue
    q=rec["q"]; tgt=TARGETS[q]; a,b=tgt["a"],tgt["b"]
    for delta0 in rec["survivor_squareclasses"]:
        delta=tuple(map(int,delta0))
        if sf(delta[2]*delta[3])!=tgt["s"]:continue
        branch_id=h([q,delta])[:20]; lifts=[]
        for t in tgt["roots"]:
            vals=forms(a,b,t)
            if all(square_fraction(Fraction(v,dd)) for v,dd in zip(vals,delta)):
                U,V,A,B=vals; assert V!=0
                x=Fraction(a,b)*U/V
                if A==0:
                    assert x==Fraction(-1,1); kind="A_ZERO_X_MINUS_ONE"
                else:
                    assert B==0 and x==-Fraction(a*a,b*b); kind="B_ZERO_X_MINUS_Q_SQUARED"
                lifts.append({"t":str(t),"quotient_Y":0,"receiver_x":str(x),"classification":kind,"receiver_point":"RATIONAL_2_TORSION_ZERO_FREE_PART"})
        branches.append({"q":q,"branch_id":branch_id,"delta":list(delta),"complete_quotient_points_tested":4,"full_branch_lifts":lifts,"closure":"NO_FULL_Q_LIFT" if not lifts else "ONLY_PURE_RECEIVER_2_TORSION_LIFTS"})

assert len(branches)==16
assert sum(1 for b in branches if not b["full_branch_lifts"])==8
assert sum(1 for b in branches if b["full_branch_lifts"])==8
assert all(len(b["full_branch_lifts"])<=1 for b in branches)
byq={q:sum(1 for b in branches if b["q"]==q) for q in TARGETS}
assert byq=={"20/21":12,"80/39":4}
RAW.write_text("\n".join(raw))
payload={
 "schema":"STAGE34_02_D2_STAGEA2_RANKZERO_AB_COMPLETE_PULLBACK_V1",
 "status":"PASS_COMPLETE_QPOINTSETS_AND_EXACT_PARENT_PULLBACK",
 "source":"d2-stageA2-full-support-projective.json",
 "source_lock":"d2-stageA2-rankzero-AB-complete-pullback-lock.json",
 "software":{"package":"pari-gp","routines":["ellrank","elltors"],"effort":0},
 "input_d1_factor_branches":92,
 "rank_zero_AB_parent_branches":16,
 "quotient_certificates":quotient_cert,
 "branches":branches,
 "branches_with_no_full_Q_lift":8,
 "branches_with_only_pure_receiver_2_torsion_lifts":8,
 "non_torsion_receiver_survivors_from_rank_zero_AB_branches":0,
 "remaining_d1_factor_branches":76,
 "credit":"These 16 branches are closed only for the audited non-torsion R29-EXT-CHANG-C population. The other 76 d1 branches remain open.",
 "firewalls":{"sixteen_branch_closure_is_all_factor_branch_closure":False,"direct_cover_rational_points_complete":False,"all_multiples_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"closed_rankzero_AB_branches":16,"no_lift":8,"torsion_only":8,"remaining_d1":76},sort_keys=True))
