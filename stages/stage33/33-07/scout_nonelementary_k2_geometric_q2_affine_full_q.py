#!/usr/bin/env python3
"""Deterministic exact full finite-q scout on pure-geometric k=2 Q2-affine families.

This is a scout only. It samples three quantile-spaced orbit families for each
t=0,1,2 stratum and two deterministic sections from each sampled affine
family. For every sampled H it reconstructs H <= A0, computes H^perp/H by
exact integral Smith algebra, and asks exact mixed-modulus Z3 finite quadratic
module isometry to the locked endpoint. No arithmetic cc/ct action is loaded.
"""
import hashlib, json, math, os, runpy, time
from collections import Counter, defaultdict
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp
from z3 import BitVec, BitVecVal, Extract, Or, Solver, ULT, Xor, sat, unsat

HERE = Path(__file__).resolve().parent
Q2 = HERE / 'nonelementary-k2-geometric-q2-affine.json'
Q2_LOCK = 'f9dd684e2813acdbec07fc59575d9d487828c97f6fa8f111983fec5a6fe6b9b0'
TARGET_LOCK = '4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0'
MODS0 = [8]*10 + [16]*4
QDIAG = [2]*10 + [1]*4
TARGET_MODS = [2]*4 + [4]*6 + [8]*4
NVAR = 14
SAMPLE_FAMILIES_PER_T = int(os.environ.get('SAMPLE_FAMILIES_PER_T','3'))
Z3_TIMEOUT_MS = int(os.environ.get('Z3_TIMEOUT_MS','60000'))
OUT = HERE / 'nonelementary-k2-geometric-q2-affine-full-q-scout.json'

def csha(d):
    u=dict(d); s=u.pop('canonical_sha256',None)
    h=hashlib.sha256(json.dumps(u,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return s,h
q2=json.loads(Q2.read_text()); s,h=csha(q2)
if s!=h or s!=Q2_LOCK: raise SystemExit('Q2 affine artifact hash regression')
for key in ('full_finite_q_isometry_certified','endpoint_finite_q_certified','endpoint_full_action_certified','actual_index512_glue_identified','arithmetic_HS_closed'):
    if q2.get(key): raise SystemExit(f'Q2 predecessor crossed firewall: {key}')
if q2.get('arithmetic_generators_used') != []: raise SystemExit('Q2 predecessor used arithmetic generators')
if len(q2['records']) != 867 or q2['Q2_profile_surviving_weighted_H'] != 129468416:
    raise SystemExit('Q2 affine universe regression')

runpy.run_path(str(HERE/'prepare_nonelementary_k2_geometric_q4_manifest.py'))
man=json.loads((HERE/'nonelementary-k2-geometric-q4-manifest.json').read_text())
if man.get('arithmetic_generators_used') != [] or man.get('orbit_count') != 1496:
    raise SystemExit('manifest firewall/universe regression')
manifest={int(r['orbit_index']):r for r in man['records']}

target=json.loads((HERE/'picard-discriminant-compact.json').read_text())
if target.get('canonical_sha256') != TARGET_LOCK: raise SystemExit('target lock moved')
TARGET_B8=[[-int(x)%(16 if i==j else 8) for j,x in enumerate(row)] for i,row in enumerate(target['discriminant_bilinear_numerator_over_8_reduced'])]

def canon(rows):
    p={}
    for raw in rows:
        x=int(raw)
        for k in sorted(p,reverse=True):
            if x>>k&1: x^=p[k]
        if not x: continue
        k=x.bit_length()-1
        for o in list(p):
            if p[o]>>k&1: p[o]^=x
        p[k]=x
    return tuple(p[k] for k in sorted(p,reverse=True))
def complement(base,whole):
    cur=list(canon(base)); out=[]
    for v in canon(whole):
        a=canon(cur+[v])
        if len(a)>len(canon(cur)): cur.append(v); out.append(v)
    return tuple(out)
def free_variables(rref):
    piv=set()
    for z in rref:
        c=int(z)&((1<<NVAR)-1)
        if not c: raise SystemExit('zero affine row')
        piv.add(c.bit_length()-1)
    return tuple(i for i in range(NVAR) if i not in piv)
def solution_from_free(rref,free,mask):
    sol=0
    for j,v in enumerate(free):
        if int(mask)>>j&1: sol|=1<<v
    for z in reversed(rref):
        c=int(z)&((1<<NVAR)-1); p=c.bit_length()-1
        rhs=((int(z)>>NVAR)&1)^((c&sol).bit_count()&1)
        if rhs: sol|=1<<p
    return sol
def order4_corrections(p_basis, quotient_basis, solution):
    q=len(quotient_basis); out=[]
    for g in range(len(p_basis)):
        c=0
        for b,v in enumerate(quotient_basis):
            if int(solution)>>(q*g+b)&1: c^=int(v)
        out.append(c)
    return tuple(out)
def actual_row(low,high):
    row=[]
    for j in range(14):
        normalized=((int(low)>>j)&1)+2*((int(high)>>j)&1)
        scale=2 if j<10 else 4
        row.append((scale*normalized)%MODS0[j])
    return tuple(row)
def actual_order2_row(bits):
    return tuple((4 if j<10 else 8) if int(bits)>>j&1 else 0 for j in range(14))
def reconstruct_rows(rec,solution):
    p=tuple(map(int,rec['P_basis_bits'])); w=tuple(map(int,rec['W_basis_bits'])); qb=tuple(map(int,rec['quotient_basis_bits']))
    corrections=order4_corrections(p,qb,solution)
    rows=[actual_row(a,b) for a,b in zip(p,corrections)]
    rows.extend(actual_order2_row(x) for x in complement(p,w))
    if len(rows)!=7: raise SystemExit('k2 H generator count regression')
    return rows
def q32(a): return sum(c*int(x)*int(x) for c,x in zip(QDIAG,a))%32
def b16(a,b): return sum(c*int(x)*int(y) for c,x,y in zip(QDIAG,a,b))%16
def verify_isotropic(rows):
    for i,r in enumerate(rows):
        if q32(r): raise SystemExit('nonisotropic H generator')
        for j in range(i):
            if b16(r,rows[j]): raise SystemExit('nonorthogonal H generators')

def quotient_data(rows):
    count=len(rows)
    congr=[[int(h[j])*(16//MODS0[j]) for j in range(14)] for h in rows]
    aug=sp.Matrix([congr[i]+[-16*int(i==j) for j in range(count)] for i in range(count)])
    diag,left,right=smith_normal_decomp(aug,domain=ZZ)
    if left*aug*right != diag: raise SystemExit('orthogonal Smith transform regression')
    rank=sum(diag[i,i]!=0 for i in range(min(diag.shape)))
    basis=sp.Matrix([[int(right[i,j]) for i in range(14)] for j in range(rank,right.cols)])
    if basis.shape!=(14,14) or abs(int(basis.det()))!=512: raise SystemExit('Hperp basis/index regression')
    inv=basis.inv(); rel=[]
    for j,m in enumerate(MODS0):
        z=[0]*14;z[j]=m;rel.append(z)
    rel.extend(rows); coords=[]
    for r in rel:
        v=sp.Matrix([r])*inv
        if any(x.q!=1 for x in v): raise SystemExit('nonintegral relation in Hperp basis')
        coords.append([int(x) for x in v])
    R=sp.Matrix(coords); qdiag,qleft,qright=smith_normal_decomp(R,domain=ZZ)
    if qleft*R*qright != qdiag: raise SystemExit('quotient Smith transform regression')
    factors=[abs(int(qdiag[i,i])) for i in range(14)]
    if factors!=TARGET_MODS: raise SystemExit(f'quotient factors moved: {factors}')
    pair16=sp.zeros(14)
    for a in range(14):
        for b in range(14):
            pair16[a,b]=sum((16//MODS0[j])*int(basis[a,j])*int(basis[b,j]) for j in range(14))
    ri=qright.inv(); tr=ri*pair16*ri.T
    if any(int(tr[i,j])%2 for i in range(14) for j in range(14)): raise SystemExit('pair denominator regression')
    return [[int(tr[i,j]//2)%(16 if i==j else 8) for j in range(14)] for i in range(14)]

def qnum(row,B): return sum(row[a]*B[a][b]*row[b] for a in range(14) for b in range(14))%16
def bnum(x,y,B): return sum(x[a]*B[a][b]*y[b] for a in range(14) for b in range(14))%8
def gf2_rank(rows):
    p={}
    for row in rows:
        x=sum((int(v)&1)<<j for j,v in enumerate(row))
        while x:
            k=x.bit_length()-1
            if k in p:x^=p[k]
            else:p[k]=x;break
    return len(p)
def solve_isometry(Bc):
    P=[[BitVec(f'p_{i}_{j}',4) for j in range(14)] for i in range(14)]
    solver=Solver();solver.set(timeout=Z3_TIMEOUT_MS);solver.set(random_seed=0)
    for i,mi in enumerate(TARGET_MODS):
        for j,mj in enumerate(TARGET_MODS):
            solver.add(ULT(P[i][j],BitVecVal(mj,4)))
            step=mj//math.gcd(mi,mj)
            if step>1: solver.add((P[i][j]&BitVecVal(step-1,4))==BitVecVal(0,4))
    def q4(row):
        z=BitVecVal(0,4)
        for a in range(14):
            for b in range(14): z=z+row[a]*BitVecVal(TARGET_B8[a][b]%16,4)*row[b]
        return z
    def b3(x,y):
        z=BitVecVal(0,3)
        for a in range(14):
            xa=Extract(2,0,x[a])
            for b in range(14): z=z+xa*BitVecVal(TARGET_B8[a][b]%8,3)*Extract(2,0,y[b])
        return z
    for i in range(14):
        solver.add(q4(P[i])==BitVecVal(Bc[i][i]%16,4))
        for j in range(i): solver.add(b3(P[i],P[j])==BitVecVal(Bc[i][j]%8,3))
    def bit0(x): return Extract(0,0,x)==BitVecVal(1,1)
    def xorall(vals):
        z=vals[0]
        for v in vals[1:]:z=Xor(z,v)
        return z
    for lo,hi in ((0,4),(4,10),(10,14)):
        for mask in range(1,1<<(hi-lo)):
            selected=[lo+r for r in range(hi-lo) if mask>>r&1]
            solver.add(Or(*[xorall([bit0(P[r][c]) for r in selected]) for c in range(lo,hi)]))
    t=time.perf_counter(); result=solver.check(); elapsed=time.perf_counter()-t
    if result==unsat:return 'UNSAT',None,elapsed
    if result!=sat:return 'UNKNOWN',None,elapsed
    model=solver.model(); W=[[model.eval(P[i][j],model_completion=True).as_long() for j in range(14)] for i in range(14)]
    for i,mi in enumerate(TARGET_MODS):
        for j,mj in enumerate(TARGET_MODS):
            if not 0<=W[i][j]<mj or (mi*W[i][j])%mj: raise SystemExit('SAT hom verification failed')
        if qnum(W[i],TARGET_B8)!=Bc[i][i]%16: raise SystemExit('SAT q verification failed')
        for j in range(i):
            if bnum(W[i],W[j],TARGET_B8)!=Bc[i][j]%8: raise SystemExit('SAT b verification failed')
    ranks=[]
    for lo,hi in ((0,4),(4,10),(10,14)):
        ranks.append(gf2_rank([[W[i][j]&1 for j in range(lo,hi)] for i in range(lo,hi)]))
    if ranks!=[4,6,4]: raise SystemExit('SAT automorphism rank regression')
    wh=hashlib.sha256(json.dumps(W,separators=(',',':')).encode()).hexdigest()
    return 'SAT',wh,elapsed

def quantiles(vals,n):
    if n>=len(vals): return vals
    if n==1:return [vals[len(vals)//2]]
    return [vals[(i*(len(vals)-1))//(n-1)] for i in range(n)]
by_t=defaultdict(list)
for r in q2['records']: by_t[int(r['t'])].append(r)
chosen=[]
for t in (0,1,2):
    vals=sorted(by_t[t],key=lambda r:int(r['orbit_index']))
    chosen.extend(quantiles(vals,SAMPLE_FAMILIES_PER_T))

results=[]; statuses=Counter(); family_agreement=Counter()
for qr in chosen:
    oi=int(qr['orbit_index']); mr=manifest[oi]; rref=tuple(map(int,qr['Q2_survivor_affine_rref_augmented']))
    free=free_variables(rref)
    if len(free)!=int(qr['Q2_survivor_affine_dimension']): raise SystemExit('Q2 affine dimension regression')
    solutions=[solution_from_free(rref,free,0), solution_from_free(rref,free,1)]
    local=[]
    for ordinal,solution in enumerate(solutions):
        rows=reconstruct_rows(mr,solution); verify_isotropic(rows); B=quotient_data(rows)
        raw_hash=hashlib.sha256(json.dumps(B,separators=(',',':')).encode()).hexdigest()
        status,witness,elapsed=solve_isometry(B); statuses[status]+=1; local.append(status)
        results.append({'orbit_index':oi,'t':int(qr['t']),'section_ordinal':ordinal,'solution_bits':solution,'raw_smith_B8_sha256':raw_hash,'solver_status':status,'sat_witness_sha256':witness,'solver_seconds':round(elapsed,6)})
    family_agreement['same_status' if len(set(local))==1 else 'different_status']+=1

cert={
 'schema':'STAGE33_07_NONELEMENTARY_K2_GEOMETRIC_Q2_AFFINE_FULL_Q_SCOUT_V1',
 'source_Q2_affine_certificate_sha256':Q2_LOCK,
 'source_endpoint_picard_discriminant_sha256':TARGET_LOCK,
 'arithmetic_generators_used':[],
 'firewall':'PURE_GEOMETRIC_Q2_AFFINE_FAMILIES_ONLY__NO_ARITHMETIC_CC_CT',
 'sample_rule':f'{SAMPLE_FAMILIES_PER_T} quantile-spaced orbit families in each t=0,1,2 stratum; affine basepoint plus first free-direction translate',
 'sampled_family_count':len(chosen),
 'sampled_section_count':len(results),
 'z3_timeout_ms_per_section':Z3_TIMEOUT_MS,
 'status_counts':dict(sorted(statuses.items())),
 'within_sampled_family_status_agreement':dict(sorted(family_agreement.items())),
 'records':results,
 'sampled_full_q_isometry_exact_where_status_is_SAT_or_UNSAT':True,
 'full_q_exhaustive_certified':False,
 'full_finite_q_isometry_certified':False,
 'endpoint_finite_q_certified':False,
 'endpoint_full_action_certified':False,
 'actual_index512_glue_identified':False,
 'arithmetic_HS_closed':False,
 'next_exact_leaf':'L33-07-USE-K2-Q2-AFFINE-FULL-Q-SCOUT-TO-DESIGN-EXACT-FAMILY-WIDE-FINITE-Q-CLASSIFICATION',
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest(); OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'families':len(chosen),'sections':len(results),'statuses':dict(statuses),'family_agreement':dict(family_agreement),'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
