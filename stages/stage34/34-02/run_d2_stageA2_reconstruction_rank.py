#!/usr/bin/env python3
from __future__ import annotations
import json, math, pathlib, re, subprocess

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-factor-branch-support.json"
OUT=ROOT/"d2-stageA2-reconstruction-rank.json"
RAW=ROOT/"d2-stageA2-reconstruction-rank-stdout.txt"
FULL="The rank and full Mordell-Weil basis have been determined unconditionally."

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
        m=n; parity=0
        while m%p==0:
            parity^=1; m//=p
        if parity:out*=p
    return sign*out

def isprime(n:int)->bool:
    if n<2:return False
    if n%2==0:return n==2
    p=3
    while p*p<=n:
        if n%p==0:return False
        p+=2
    return True

def count_E_mod_p(n:int,p:int)->int:
    assert (2*n)%p
    total=1
    nn=(n*n)%p
    for x in range(p):
        rhs=(x*x*x-nn*x)%p
        if rhs==0: total+=1
        else: total += 2 if pow(rhs,(p-1)//2,p)==1 else 0
    return total

def torsion_upper(n:int):
    g=0; used=[]
    for p in range(3,80):
        if not isprime(p) or (2*n)%p==0:continue
        c=count_E_mod_p(n,p); used.append([p,c]); g=math.gcd(g,c)
        if g==4:break
    assert g==4
    return g,used

def parse_rank(stdout:str)->tuple[int,str]:
    lines=[ln.strip().replace(" ","") for ln in stdout.splitlines() if ln.strip().startswith("[[")]
    for ln in reversed(lines):
        m=re.match(r"^\[\[(\d+)\],",ln)
        if m:return int(m.group(1)),ln
    raise RuntimeError("could not parse mwrank -o rank line")

data=json.loads(SRC.read_text())
d1_species=set(); d2_e1=0
for c in data["cases"]:
    for x in c["survivor_squareclasses"]:
        e=abs(sf(int(x[0])*int(x[1])))
        if int(c["d"])==1:
            d1_species.add(abs(sf(2*e)))
        elif e==1:
            d2_e1+=1
species=sorted(d1_species|{1})
assert species==[1,2,5,6,10,21,22,26,30,39,66,78,110,195,210,330,390,546]
assert d2_e1==62

records=[]; raw=[]
for n in species:
    curve=f"[0,0,0,{-n*n},0]\n"
    proc=subprocess.run(["mwrank","-q","-v","1","-o"],input=curve,text=True,capture_output=True,timeout=120)
    txt=proc.stdout+("\nSTDERR:\n"+proc.stderr if proc.stderr else "")
    raw.append(f"===== n={n} =====\n{txt}")
    if proc.returncode!=0: raise SystemExit(f"mwrank failed n={n} rc={proc.returncode}")
    low=txt.lower()
    if any(s in low for s in ["unable to saturate","saturation failed","not saturated","conditional rank"]):
        raise SystemExit(f"mwrank warning n={n}")
    if FULL not in txt: raise SystemExit(f"missing unconditional full-basis marker n={n}")
    rank,oline=parse_rank(txt)
    tors,reds=torsion_upper(n)
    records.append({"n":n,"curve":f"y^2=x^3-{n*n}*x","rank":rank,"mwrank_o_line":oline,"unconditional_full_basis":True,"torsion_order":tors,"torsion_reduction_upper_bound":reds})
    print(f"PASS n={n}: rank={rank} torsion={tors}")
rank_map={r["n"]:r["rank"] for r in records}
rank0={n for n,r in rank_map.items() if r==0}

case_out=[]; eliminated=0
for c in data["cases"]:
    kept=[]; killed=[]
    for x in c["survivor_squareclasses"]:
        e=abs(sf(int(x[0])*int(x[1])))
        if int(c["d"])==1:
            n=abs(sf(2*e)); kill=n in rank0
        else:
            n=e; kill=(e==1 and 1 in rank0)
        (killed if kill else kept).append(x)
    eliminated+=len(killed)
    case_out.append({"q":c["q"],"d":c["d"],"input_survivors":len(c["survivor_squareclasses"]),"rank0_reconstruction_eliminated":len(killed),"survivors":len(kept),"survivor_squareclasses":kept})
    print(f"FILTER {c['q']} d={c['d']}: {len(c['survivor_squareclasses'])} -> {len(kept)}")

payload={
 "schema":"STAGE34_02_D2_STAGEA2_RECONSTRUCTION_TWIST_RANK_V1",
 "status":"PASS_UNCONDITIONAL_MWRANK_RECONSTRUCTION_TWIST_CERTIFICATE",
 "source_support":"d2-stageA2-factor-branch-support.json",
 "source_reconstruction":"d2-stageA2-reconstruction-diagonal-lock.json",
 "software":{"package":"eclib-tools","routine":"mwrank","command":"mwrank -q -v 1 -o","required_success_marker":FULL},
 "species":records,
 "rank_zero_species":sorted(rank0),
 "closure_semantics":"For d1, a rank-zero reconstruction Jacobian with torsion order 4 makes the four explicit axis points complete, hence only U=0 or V=0 and receiver torsion/origin. For d2 only the e=1 species is discharged here: W^2=2(R^4+S^4) has four explicit points R/S=+/-1; rank0 and torsion order 4 makes them complete, giving U/V=+/-1 and the audited d2 pole torsion values.",
 "input_survivors":sum(c["input_survivors"] for c in case_out),
 "rank0_reconstruction_eliminated":eliminated,
 "survivors":sum(c["survivors"] for c in case_out),
 "cases":case_out,
 "firewalls":{"positive_rank_species_is_Q_point":False,"d2_e7_torsors_closed":False,"remaining_reconstruction_conditions_complete":False,"receiver_closed":False,"R29_EXT_CHANG_C_closed":False}
}
assert payload["input_survivors"]==1214
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
RAW.write_text("\n".join(raw))
print(json.dumps({"status":payload["status"],"rank0_species":sorted(rank0),"eliminated":eliminated,"survivors":payload["survivors"]},sort_keys=True))
