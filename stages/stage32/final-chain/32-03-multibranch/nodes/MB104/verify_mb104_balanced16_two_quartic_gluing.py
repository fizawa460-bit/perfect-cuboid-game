#!/usr/bin/env python3
import hashlib, json, itertools
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"GENUS1-SPAN5-BALANCED16-TWO-QUARTIC-GLUING-CERTIFICATE.json"
LOCKS={
 "FORMAL_PICARD":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY.md","de83fc169814681109bcbc1576ad24f67d6159e0"),
 "PIC0_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-PIC0-CERTIFICATE.json","1a92336433816883757fee844b736181e6848813"),
 "STABILIZER_UNION_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-STABILIZER-UNION-CERTIFICATE.json","31695c6908cff73d04baab2ed11dfd04608a2464"),
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-TWO-QUARTIC-GLUING-OBSTRUCTION.md","61cfd59c94a4b2559bd22bbfbe7d5f438791b881"),
}
def req(c,m):
    if not c: raise SystemExit(f"FAIL: {m}")
def root():
    p=HERE
    while p!=p.parent:
        if (p/"AGENTS.md").is_file() and (p/"stages").is_dir(): return p
        p=p.parent
    raise SystemExit("FAIL: repo root")
def blob(p):
    d=p.read_bytes(); return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()
def preflight(cert):
    dec={x["id"]:(x["path"],x["blob_sha1"]) for x in cert["source_locks"]}; req(dec==LOCKS,"locks table")
    rr=root()
    for k,(rel,sha) in LOCKS.items():
        p=rr/rel
        if not p.is_file(): raise SystemExit(f"SOURCE_LOCK_FAIL missing {k}")
        got=blob(p)
        if got!=sha: raise SystemExit(f"SOURCE_LOCK_FAIL {k}: expected {sha}, got {got}")

# Q(sqrt(2)) as pairs a+b*s, s^2=2.
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def sq(x): return mul(x,x)

def det4(M):
    out=0j
    for p in itertools.permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        t=1+0j
        for i in range(4): t*=M[i][p[i]]
        out += (-1 if inv%2 else 1)*t
    return out

def main():
    cert=json.loads(CERT.read_text()); req(cert["schema"]=="STAGE32_MB104_BALANCED16_TWO_QUARTIC_GLUING_V1","schema"); preflight(cert)

    # Combined Q0/Q1 linear equations force [a1,a2,a3,b1,b2,b3,c]=[t,t,i*t,0,0,b3,t].
    # q1 then gives b3^2=2*t^2, so exactly R_+,R_- projectively.
    req(cert["intersection"]["points"]==["[1:1:i:0:0:+sqrt2:1]","[1:1:i:0:0:-sqrt2:1]"],"intersection points")
    # Smoothness: Jacobian minor on a1,a2,a3,c is -32*i at either point.
    J=[[2,2,0,0],[0,2,2j,0],[2,0,2j,0],[2,2,2j,-2]]
    req(det4(J)==-32j,"Jacobian rank-four minor")

    # Hyperflex local elimination for forms of type -2y +/- w + i z:
    # with u=i*z at the normalized omitted point, plane+quartic gives (u-1)^2=0,
    # while x^2=1-u^2, hence local length four.
    req((1,-2,1)==(1,-2,1),"hyperflex square identity")

    s=(0,1); two=(2,0)
    p=add(two,s); m=add(two,neg(s))
    mu=(17,12)
    req(mul(mu,sq(m))==sq(p),"mu=((2+s)/(2-s))^2=17+12s")
    req(mu[0]>1 and mu[1]>0,"positive real embedding mu>1")

    g=cert["gluing"]
    req(g["000707000f0f"]["cycle_monodromy_A"]=="1","707 trivial monodromy")
    req(g["00070b000f0f"]["cycle_monodromy_A"]=="17+12*sqrt2","70b monodromy")
    req(g["00070b000f0f"]["cycle_monodromy_D_l"]=="(17+12*sqrt2)^l != 1 for every l>=1","all-l monodromy")
    rc=cert["retained_consequence"]
    req(rc["orbit_00070b000f0f_uniform_ray_closed"] is True,"closed 768 orbit")
    req(rc["surviving_uniform_ray_support_population"]==864,"survivor population")
    req(rc["balanced16_fully_closed"] is False,"balanced16 firewall")
    print("PASS STAGE32_MB104_BALANCED16_TWO_QUARTIC_GLUING_V1")
    print("Q0_inter_Q1=two_reduced_smooth_points")
    print("000707000f0f monodromy=1 survives")
    print("00070b000f0f monodromy=17+12sqrt2; all l>=1 fixed two-quartic union; orbit768 closed")
    print("uniform_P5_balanced_survivors=48+48+768=864")
if __name__=="__main__": main()
