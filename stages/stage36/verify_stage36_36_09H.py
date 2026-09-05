#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09H/common-jminus-factor-squareclass-descent-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
G=ROOT/'stages/stage36/36-09G/endpoint-equivalence-breadth-refresh.json'
E=ROOT/'stages/stage36/36-09E/character-elliptic-quotient-arithmetic-preflight.json'
W01=ROOT/'docs/arsenal/cards/formal/S34-W01.md'
CYCLE=ROOT/'docs/research-os/policies/cycle-exploration-safety-protocol.md'
CERT_BLOB='08e7e87f866aebbc92b7d5cd776ce8b5fe60744d'
BASE='29ce620a693f7cbdec48bce9b720cc02dfe5fa74'
LOCKS={
 G:'bae34622d8ab7f94fafab4a290e770a3830e47fc',
 E:'081b704fecaa3bd39e6a523ee7beaefe706683f4',
 W01:'01a8e90e34b4aa46edbfa825803d488e5230e9d0',
 CYCLE:'4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37',
}

def req(ok:bool,msg:str)->None:
    if not ok: raise SystemExit(msg)
def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

# Tiny exact multivariate polynomial ring for independent expansion checks.
# monomial=(e_r,e_q) or generic tuples; coefficients are integers.
def padd(a,b):
    c=dict(a)
    for m,v in b.items(): c[m]=c.get(m,0)+v
    return {m:v for m,v in c.items() if v}
def pneg(a): return {m:-v for m,v in a.items()}
def psub(a,b): return padd(a,pneg(b))
def pmul(a,b):
    c={}
    for ma,va in a.items():
        for mb,vb in b.items():
            m=tuple(x+y for x,y in zip(ma,mb)); c[m]=c.get(m,0)+va*vb
    return {m:v for m,v in c.items() if v}
def ppow(a,n):
    one={(0,)*len(next(iter(a))):1}; out=one
    for _ in range(n): out=pmul(out,a)
    return out
def pscale(a,k): return {m:k*v for m,v in a.items() if k*v}

def rank_f2(rows):
    a=[list(map(int,r)) for r in rows]; rank=0; m=len(a); n=len(a[0])
    for col in range(n):
        piv=next((i for i in range(rank,m) if a[i][col]),None)
        if piv is None: continue
        a[rank],a[piv]=a[piv],a[rank]
        for i in range(m):
            if i!=rank and a[i][col]: a[i]=[x^y for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank

def primes_upto(n):
    out=[]
    for x in range(2,n+1):
        if all(x%d for d in range(2,int(math.isqrt(x))+1)): out.append(x)
    return out

def vp(n,p):
    n=abs(n); e=0
    while n and n%p==0: e+=1; n//=p
    return e

def local_witness(p):
    # Find a root h mod p, then choose a non-Hensel lift mod p^2 so alpha != 0 mod p.
    root=next(h for h in range(1,p) if (h*h+1)%p==0)
    h=None; alpha=None
    for k in range(p):
        cand=root+k*p
        a=(cand*cand+1)//p
        if a%p!=0:
            h=cand; alpha=a; break
    req(h is not None,'non-Hensel lift not found')
    inv2=pow(2,-1,p)
    bad={0,(alpha*inv2)%p,(-alpha*inv2)%p}
    m=next(x for x in range(1,p) if x not in bad)
    P,Q,R,S=h,1,1+p*m,1
    N1=Q*Q*S*S+P*P*R*R
    N2=Q*Q*R*R+P*P*S*S
    N3=Q*Q*(R-S)**2+P*P*(R+S)**2
    N4=Q*Q*(R+S)**2+P*P*(R-S)**2
    return h,alpha,m,(P,Q,R,S),(N1,N2,N3,N4)

def main()->None:
    req(blob(CERT)==CERT_BLOB,'36-09H certificate blob drift')
    for p,sha in LOCKS.items(): req(blob(p)==sha,f'locked source drift: {p}')
    c=json.loads(CERT.read_text())
    req(c['schema']=='STAGE36_36_09H_COMMON_JMINUS_FACTOR_SQUARECLASS_DESCENT_PREFLIGHT_V1','36-09H schema moved')
    req(c['base_main_sha']==BASE,'36-09H base moved')
    ent=c['entry_authority']
    req(ent['stage36_36_09G_promotion_pr']==1606 and ent['promotion_exact_head']=='bb793831be80d5c5b98d1878dc8ff5212a239037','36-09H entry identity moved')
    req(ent['promotion_exact_head_ci_run']==33960848351 and ent['promotion_exact_head_ci_job']==101292353340,'36-09H promotion CI moved')
    req(ent['promotion_merged_main_sha']=='4ed21de07a935ed848400515a44f53aba49234c7','36-09H promotion merge moved')

    g=json.loads(G.read_text())
    req(g['common_jminus_exact_reduction']['reduced_receiver']==['D=s+t+1 is a rational square','B*C=(s+1)*(s+t) is a rational square'],'36-09G common receiver source moved')
    req(g['common_jminus_exact_reduction']['strict_rational_properness_witness_obtained'] is False,'36-09G strictness firewall moved')
    e=json.loads(E.read_text())
    bp=e['physical_base_parameterization']
    req(bp['t']=='(r^2-1)^2/(4*r^2)' and bp['t_plus_1']=='(r^2+1)^2/(4*r^2)','physical r-parameter source moved')

    # Independent exact expansion in Z[r,q].
    one={(0,0):1}; R={(1,0):1}; Q={(0,1):1}
    r2=ppow(R,2); q2=ppow(Q,2)
    r2p1=padd(r2,one); r2m1=psub(r2,one); omq2=psub(one,q2)
    # a = q(r^2+1)/(r(1-q^2)); B numerator over r^2(1-q^2)^2.
    Bnum=padd(pmul(q2,ppow(r2p1,2)),pmul(r2,ppow(omq2,2)))
    F1=padd(q2,r2)
    F2=padd(pmul(q2,r2),one)
    req(Bnum==pmul(F1,F2),'B four-factor first half identity failed')
    # C numerator over 4r^2(1-q^2)^2.
    Cnum=padd(pscale(pmul(q2,ppow(r2p1,2)),4),pmul(ppow(r2m1,2),ppow(omq2,2)))
    rp1=padd(R,one); rm1=psub(R,one)
    F3=padd(pmul(q2,ppow(rm1,2)),ppow(rp1,2))
    F4=padd(pmul(q2,ppow(rp1,2)),ppow(rm1,2))
    req(Cnum==pmul(F3,F4),'C four-factor second half identity failed')
    ff=c['exact_four_factor_reduction']['factors']
    req(list(ff)==['F1','F2','F3','F4'],'factor dictionary moved')

    # Independent homogeneous integer formulas and identities.
    def Ns(P,Qv,Rv,S):
        return (
            Qv*Qv*S*S+P*P*Rv*Rv,
            Qv*Qv*Rv*Rv+P*P*S*S,
            Qv*Qv*(Rv-S)**2+P*P*(Rv+S)**2,
            Qv*Qv*(Rv+S)**2+P*P*(Rv-S)**2,
        )
    for P,Qv,Rv,S in [(2,1,6,1),(3,2,5,2),(7,3,8,5),(5,2,-7,3)]:
        N1,N2,N3,N4=Ns(P,Qv,Rv,S)
        req(N1-N2==(P*P-Qv*Qv)*(Rv*Rv-S*S),'N1-N2 identity failed')
        req(N3-N4==4*Rv*S*(P*P-Qv*Qv),'N3-N4 identity failed')
        req(N3+N4==2*(N1+N2),'N3+N4 identity failed')

    # Formal p-adic expansion using a polynomial ring Z[p,alpha,m].
    z={(0,0,0):1}; pp={(1,0,0):1}; aa={(0,1,0):1}; mm={(0,0,1):1}
    Rexpr=padd(z,pmul(pp,mm)); R2=ppow(Rexpr,2)
    h2=padd({(0,0,0):-1},pmul(pp,aa))
    N1expr=padd(z,pmul(R2,h2))
    N2expr=padd(R2,h2)
    expected1=padd(pmul(pp,psub(aa,pscale(mm,2))),padd(pmul(ppow(pp,2),psub(pscale(pmul(mm,aa),2),ppow(mm,2))),pmul(ppow(pp,3),pmul(ppow(mm,2),aa))))
    expected2=padd(pmul(pp,padd(aa,pscale(mm,2))),pmul(ppow(pp,2),ppow(mm,2)))
    req(N1expr==expected1,'generic N1 p-adic expansion failed')
    req(N2expr==expected2,'generic N2 p-adic expansion failed')

    # Replay the construction for many p == 1 mod 4; exact theorem is the algebra above plus elementary existence of sqrt(-1).
    tested=[]
    for p in primes_upto(500):
        if p%4!=1: continue
        h,alpha,m,coords,vals=local_witness(p)
        P,Qv,Rv,S=coords; N1,N2,N3,N4=vals
        req(math.gcd(P,Qv)==1 and math.gcd(Rv,S)==1,'local witness not primitive')
        req(Qv and Rv and P and S and Rv not in (S,-S) and Qv not in (P,-P),'local witness hits physical boundary')
        req([vp(x,p) for x in vals]==[1,1,0,0],f'p={p}: valuation vector failed')
        req((N1*N2*N3*N4)% (p*p)==0,'local product parity compatibility failed')
        tested.append(p)
    req(len(tested)>=20,'too few p==1 mod4 replay primes')

    w=W01.read_text()
    for text in ['pairwise gcd/resultant or equivalent valuation-support control','complete sign and 2-adic bookkeeping','finite exhaustive branch family']:
        req(text in w,f'S34-W01 contract phrase missing: {text}')
    pre=c['S34_W01_preflight']
    req(pre['exact_rational_reconstruction_formulas'] is True and pre['primitive_denominator_cleared_coordinates'] is True and pre['exact_bounded_low_degree_factorization'] is True,'S34-W01 positive preflight facts moved')
    req(pre['pairwise_fixed_finite_shared_prime_support'] is False,'shared-prime blocker lost')
    req(pre['complete_sign_and_2_adic_bookkeeping'] is False and pre['finite_exhaustive_squareclass_branch_family_proved'] is False,'S34-W01 credit leaked')
    req(pre['status']=='NOT_TRIGGERED_FIRST_LAYER_UNBOUNDED_SHARED_ODD_PRIME_SUPPORT','S34-W01 status moved')

    route=c['route_decision']
    req(route['B10_INTERMEDIATE_SIGN_QUOTIENT_OR_CHARACTER']=='LIVE_RECEIVER_S34_W01_FIRST_LAYER_BLOCKED','B10 route moved')
    req(route['new_material_block'] is True and route['fresh_breadth_refresh_required_after_hostile_audit'] is True,'post-block breadth trigger moved')
    req(route['next_route_after_hostile_audit']=='36-09I_COMMON_JMINUS_POST_W01_BREADTH_REFRESH','36-09I routing moved')
    req(c['unbounded_shared_odd_prime_support']['scope_firewall'].startswith('this is a local valuation-support construction'),'local/global firewall moved')
    req(all(v is False for v in c['claims'].values()),'36-09H higher credit leaked')

    s=json.loads(STATE.read_text())
    req(s['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V28_36_09H_PENDING_HOSTILE_AUDIT','V28 schema moved')
    req(s['status']=='ACTIVE_PENDING_HOSTILE_AUDIT' and s['base_main_sha']==BASE,'V28 authority/base moved')
    a=s['authority_frontier']['36-09H']
    req(a['certificate_blob_sha']==CERT_BLOB and a['S34_W01_TRIGGERED'] is False,'V28 36-09H evidence moved')
    req(a['UNBOUNDED_SHARED_ODD_PRIME_SUPPORT_PROVED'] is True,'V28 p-support result lost')
    req(a['NEXT_ROUTE_AFTER_AUDIT']=='36-09I_COMMON_JMINUS_POST_W01_BREADTH_REFRESH','V28 next route moved')
    req(s['current']['36_09I_entry_allowed'] is False,'36-09I prematurely unlocked')
    req(s['promotion_gates']['S34_W01_finite_squareclass_branch_family_proved'] is False,'V28 finite branch credit leaked')
    req(all(v is False for v in s['claims'].values()),'V28 higher credit leaked')

    print('PASS STAGE36_36_09H_COMMON_JMINUS_FACTOR_SQUARECLASS_DESCENT_PREFLIGHT')
    print('two conics -> exact four factors F1..F4 -> primitive N1..N4')
    print(f'unbounded odd shared-prime pattern replayed for {len(tested)} primes p=1 mod4 below 500; generic p-adic expansions exact')
    print('S34-W01 NOT TRIGGERED at this layer; B10 receiver remains live; 36-09I breadth refresh locked pending hostile audit')

if __name__=='__main__': main()
