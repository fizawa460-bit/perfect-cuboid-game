#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import runpy
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PIC = ROOT / "stages/stage33/33-07/certify_two_coordinate_swap_picard_rows.py"
PIC_DIR = str(PIC.parent)
if PIC_DIR not in sys.path:
    sys.path.insert(0, PIC_DIR)
ns = runpy.run_path(str(PIC))

UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
INDLIST = list(ns["INDLIST"])
known = [[int(x) for x in r] for r in ns["known"]]
gram = [[int(x) for x in r] for r in ns["gram"]]
hyperplane = [int(x) for x in ns["hyperplane"]]
perms = [[int(x) for x in p] for p in ns["perms"]]
pairing = ns["pairing"]
row_times_matrix = ns["row_times_matrix"]
mm = ns["mm"]
transpose = ns["transpose"]

if len(INDLIST) != 64 or len(known) != 140 or len(known[0]) != 64:
    raise SystemExit("retained Picard shape regression")

# Exact arithmetic in Q(zeta_8)=Q[t]/(t^4+1).
class Z8:
    __slots__ = ("c",)
    def __init__(self, c=(0,0,0,0)):
        z = list(c) + [0] * (4-len(c))
        self.c = tuple(Fraction(x) for x in z[:4])
    def __add__(self, other):
        other = q8(other)
        return Z8(tuple(a+b for a,b in zip(self.c, other.c)))
    __radd__ = __add__
    def __neg__(self): return Z8(tuple(-a for a in self.c))
    def __sub__(self, other): return self + (-q8(other))
    def __rsub__(self, other): return q8(other) - self
    def __mul__(self, other):
        other = q8(other)
        z = [Fraction(0) for _ in range(7)]
        for i,a in enumerate(self.c):
            for j,b in enumerate(other.c):
                z[i+j] += a*b
        for k in range(6,3,-1):
            z[k-4] -= z[k]  # t^4=-1
        return Z8(tuple(z[:4]))
    __rmul__ = __mul__
    def __eq__(self, other): return self.c == q8(other).c
    def __hash__(self): return hash(self.c)
    def __bool__(self): return any(self.c)
    def inv(self): return z8_inv(self.c)
    def __truediv__(self, other): return self * q8(other).inv()
    def __repr__(self): return f"Z8{self.c}"

def q8(x):
    if isinstance(x,Z8): return x
    return Z8((x,0,0,0))

ONE=q8(1); ZERO=q8(0); T=Z8((0,1,0,0)); II=T*T; SS=T-T*T*T
if II*II != -ONE or SS*SS != q8(2):
    raise SystemExit("Q(zeta8) relation regression")

@lru_cache(maxsize=None)
def z8_inv(c):
    a=Z8(c)
    if not a: raise ZeroDivisionError
    # Multiplication matrix: column j is a*t^j. Solve M*b=1 over Q.
    basis=[Z8((1,0,0,0)),Z8((0,1,0,0)),Z8((0,0,1,0)),Z8((0,0,0,1))]
    M=[[Fraction(0) for _ in range(5)] for _ in range(4)]
    for j,b in enumerate(basis):
        col=(a*b).c
        for i in range(4): M[i][j]=col[i]
    M[0][4]=Fraction(1)
    row=0
    for col in range(4):
        p=next((r for r in range(row,4) if M[r][col]),None)
        if p is None: raise ZeroDivisionError
        M[row],M[p]=M[p],M[row]
        d=M[row][col]
        M[row]=[x/d for x in M[row]]
        for r in range(4):
            if r==row: continue
            f=M[r][col]
            if f: M[r]=[x-f*y for x,y in zip(M[r],M[row])]
        row+=1
    return Z8(tuple(M[i][4] for i in range(4)))

COORD={"a1":0,"a2":1,"a3":2,"b1":3,"b2":4,"b3":5,"c":6}
def lin(**kw):
    v=[ZERO for _ in range(7)]
    for k,x in kw.items(): v[COORD[k]]=q8(x)
    return tuple(v)
def ladd(*forms):
    return tuple(sum((f[i] for f in forms),ZERO) for i in range(7))
def lscale(k,form): return tuple(q8(k)*x for x in form)
def leval(form,p): return sum((a*b for a,b in zip(form,p)),ZERO)
BASE={name:lin(**{name:1}) for name in COORD}

def assignments(order, convention):
    vals=(1,-1)
    for tup in itertools.product(vals, repeat=len(order)):
        if convention=="left_slow": use=tup
        elif convention=="left_fast": use=tuple(reversed(tup))
        else: raise ValueError(convention)
        yield dict(zip(order,use))

def known_curve_forms(convention):
    out=[]
    a1,a2,a3,b1,b2,b3,c=(BASE[x] for x in ("a1","a2","a3","b1","b2","b3","c"))
    def push(order, maker):
        for e in assignments(order,convention): out.append(tuple(maker(e)))
    # Pinned Stoll C1s.
    push(("e1","e2","e3"),lambda e:(a1,ladd(a2,lscale(e["e1"],b3)),ladd(a3,lscale(e["e2"],b2)),ladd(b1,lscale(e["e3"],c))))
    push(("e1","e2","e3"),lambda e:(a2,ladd(a3,lscale(e["e1"],b1)),ladd(a1,lscale(e["e2"],b3)),ladd(b2,lscale(e["e3"],c))))
    push(("e1","e2","e3"),lambda e:(a3,ladd(a1,lscale(e["e1"],b2)),ladd(a2,lscale(e["e2"],b1)),ladd(b3,lscale(e["e3"],c))))
    push(("e3","e2","e1"),lambda e:(c,ladd(lscale(II,a1),lscale(e["e1"],b1)),ladd(lscale(II,a2),lscale(e["e2"],b2)),ladd(lscale(II,a3),lscale(e["e3"],b3))))
    # Pinned Stoll C2s.
    push(("e1","e2"),lambda e:(b1,ladd(lscale(II,a2),lscale(e["e1"],a3)),ladd(a1,lscale(e["e2"],c))))
    push(("e1","e2"),lambda e:(b2,ladd(lscale(II,a3),lscale(e["e1"],a1)),ladd(a2,lscale(e["e2"],c))))
    push(("e1","e2"),lambda e:(b3,ladd(lscale(II,a1),lscale(e["e1"],a2)),ladd(a3,lscale(e["e2"],c))))
    # Pinned Stoll C3s.
    push(("e1","e2","e3"),lambda e:(ladd(a1,lscale(e["e1"],a2)),ladd(lscale(SS,a1),lscale(e["e2"],b3)),ladd(b1,lscale(e["e3"],b2))))
    push(("e1","e2","e3"),lambda e:(ladd(a2,lscale(e["e1"],a3)),ladd(lscale(SS,a2),lscale(e["e2"],b1)),ladd(b2,lscale(e["e3"],b3))))
    push(("e1","e2","e3"),lambda e:(ladd(a3,lscale(e["e1"],a1)),ladd(lscale(SS,a3),lscale(e["e2"],b2)),ladd(b3,lscale(e["e3"],b1))))
    push(("e3","e2","e1"),lambda e:(ladd(lscale(II,a1),lscale(e["e1"],c)),ladd(lscale(II,b2),lscale(e["e2"],b3)),ladd(lscale(II*SS,a1),lscale(e["e3"],b1))))
    push(("e3","e2","e1"),lambda e:(ladd(lscale(II,a2),lscale(e["e1"],c)),ladd(lscale(II,b3),lscale(e["e2"],b1)),ladd(lscale(II*SS,a2),lscale(e["e3"],b2))))
    push(("e3","e2","e1"),lambda e:(ladd(lscale(II,a3),lscale(e["e1"],c)),ladd(lscale(II,b1),lscale(e["e2"],b2)),ladd(lscale(II*SS,a3),lscale(e["e3"],b3))))
    if len(out)!=92: raise SystemExit(f"known source curve count {len(out)} != 92")
    return out

def surface_eqs(p):
    a1,a2,a3,b1,b2,b3,c=p
    return (a1*a1+a2*a2-b3*b3,a2*a2+a3*a3-b1*b1,a1*a1+a3*a3-b2*b2,a1*a1+a2*a2+a3*a3-c*c)

def surface_jac(p):
    a1,a2,a3,b1,b2,b3,c=p
    return [
        [2*a1,2*a2,ZERO,ZERO,ZERO,-2*b3,ZERO],
        [ZERO,2*a2,2*a3,-2*b1,ZERO,ZERO,ZERO],
        [2*a1,ZERO,2*a3,ZERO,-2*b2,ZERO,ZERO],
        [2*a1,2*a2,2*a3,ZERO,ZERO,ZERO,-2*c],
    ]

def field_rank(M):
    A=[[q8(x) for x in row] for row in M]
    if not A: return 0
    nr=len(A); nc=len(A[0]); r=0
    for c in range(nc):
        p=next((i for i in range(r,nr) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        d=A[r][c]
        A[r]=[x/d for x in A[r]]
        for i in range(nr):
            if i==r: continue
            f=A[i][c]
            if f: A[i]=[x-f*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==nr: break
    return r

def node_key(p): return tuple(x.c for x in p)
def make_nodes():
    pts=[]
    signs=list(itertools.product((1,-1),repeat=3))
    for u,v,w in signs:
        pts.append((ONE,ZERO,ZERO,ZERO,q8(u),q8(v),q8(w)))
        pts.append((ZERO,ONE,ZERO,q8(u),ZERO,q8(v),q8(w)))
        pts.append((ZERO,ZERO,ONE,q8(u),q8(v),ZERO,q8(w)))
    for eps,dlt,eta in signs:
        pts.append((ONE,q8(eps)*II,ZERO,q8(dlt)*II,q8(eta),ZERO,ZERO))
        pts.append((ZERO,ONE,q8(eps)*II,ZERO,q8(dlt)*II,q8(eta),ZERO))
        pts.append((ONE,ZERO,q8(eps)*II,q8(dlt)*II,ZERO,q8(eta),ZERO))
    uniq={node_key(p):p for p in pts}
    if len(uniq)!=48: raise SystemExit(f"explicit node count {len(uniq)} != 48")
    for p in uniq.values():
        if any(surface_eqs(p)): raise SystemExit("explicit node is not on S")
        if field_rank(surface_jac(p))>=4: raise SystemExit("explicit node is not singular")
    return list(uniq.values())

nodes=make_nodes()
retained_sigs=[]
for k in range(48):
    E=known[92+k]
    sig=tuple(int(pairing(known[j],E,gram)) for j in range(92))
    if any(x not in (0,1) for x in sig):
        raise SystemExit(f"retained exceptional incidence nonbinary at {k}")
    retained_sigs.append(sig)
if len(set(retained_sigs))!=48:
    raise SystemExit("retained exceptional incidence signatures are not unique")
retained_by_sig={s:k for k,s in enumerate(retained_sigs)}

matches=[]
for conv in ("left_slow","left_fast"):
    curves=known_curve_forms(conv)
    sigs=[]
    for p in nodes:
        sigs.append(tuple(int(all(leval(f,p)==ZERO for f in C)) for C in curves))
    if len(set(sigs))==48 and set(sigs)==set(retained_sigs):
        mapping={node_key(p):retained_by_sig[s] for p,s in zip(nodes,sigs)}
        matches.append((conv,curves,mapping))
if len(matches)!=1:
    raise SystemExit(f"source tuple-order incidence alignment ambiguous/failed: {[x[0] for x in matches]}")
convention,source_curves,node_to_exc=matches[0]

# Strong quotient-source sanity check: final 24 exceptional rows must be exactly c=0 nodes.
for p in nodes:
    k=node_to_exc[node_key(p)]
    if (k>=24) != (p[6]==ZERO):
        raise SystemExit("final24 contracted exceptional packet != c=0 node packet")

# Picard action of sigma_c: product of pinned source sign changes 4..9.
def action_from_perm(p): return [known[p[j-1]-1] for j in INDLIST]
actions=[action_from_perm(p) for p in perms]
I64=[[int(i==j) for j in range(64)] for i in range(64)]
c_action=I64
for A in actions[3:9]: c_action=mm(c_action,A)
if mm(c_action,c_action)!=I64: raise SystemExit("sigma_c action regression")
known_index={tuple(v):i for i,v in enumerate(known)}
for p in nodes:
    k=node_to_exc[node_key(p)]
    p2=list(p); p2[6]=-p2[6]; p2=tuple(p2)
    k2=node_to_exc[node_key(p2)]
    moved=row_times_matrix(known[92+k],c_action)
    if known_index.get(tuple(moved)) != 92+k2:
        raise SystemExit("node c-flip != retained sigma_c exceptional action")

# C5 node incidence and smoothness: source C5 equations are L=0,Q=0.
def c5_values(t,p):
    e1,e2,e3,e4=t
    a1,a2,a3,b1,b2,b3,c=p
    L=a1+e2*a2+e3*a3+e4*II*c
    Q=(e2*a2+e3*a3)*b1+e1*II*b2*b3
    return L,Q

def c5_jac(t,p):
    e1,e2,e3,e4=t
    a1,a2,a3,b1,b2,b3,c=p
    gradL=[ONE,q8(e2),q8(e3),ZERO,ZERO,ZERO,q8(e4)*II]
    gradQ=[ZERO,q8(e2)*b1,q8(e3)*b1,e2*a2+e3*a3,q8(e1)*II*b3,q8(e1)*II*b2,ZERO]
    return surface_jac(p)+[gradL,gradQ]

labels=list(itertools.product((1,-1),repeat=4))
c5_nodes={}
for t in labels:
    inc=[]
    for p in nodes:
        L,Q=c5_values(t,p)
        if L==ZERO and Q==ZERO:
            if field_rank(c5_jac(t,p))!=5:
                raise SystemExit(f"C5 not smooth multiplicity-one at node {t} / {node_to_exc[node_key(p)]}")
            inc.append(node_to_exc[node_key(p)])
    c5_nodes[t]=tuple(sorted(inc))

# Check sigma_c maps e4 signs exactly on retained exceptional incidences.
for e1,e2,e3 in itertools.product((1,-1),repeat=3):
    a=set(c5_nodes[(e1,e2,e3,1)])
    b=set(c5_nodes[(e1,e2,e3,-1)])
    moved=set()
    for k in a:
        E2=row_times_matrix(known[92+k],c_action)
        moved.add(known_index[tuple(E2)]-92)
    if moved!=b: raise SystemExit(f"C5 node sigma_c sign transport regression {(e1,e2,e3)}")

# Build the common linear system characterizing a total pullback pair y:
# y*sigma_c=y, y.E=0 for contracted c=0 exceptionals, prescribed pairings
# with the other 24 exceptionals, and H.y=16.
def pairing_column(e):
    return [sum(gram[i][j]*e[j] for j in range(64)) for i in range(64)]
fixed=transpose([[c_action[i][j]-I64[i][j] for j in range(64)] for i in range(64)])
contracted=[known[116+k] for k in range(24)]
uncontracted=[known[92+k] for k in range(24)]
A=[list(map(int,r)) for r in fixed]
A += [pairing_column(E) for E in contracted]
A += [pairing_column(E) for E in uncontracted]
A += [pairing_column(hyperplane)]
if len(A)!=113 or any(len(r)!=64 for r in A): raise SystemExit("pair extraction linear system shape regression")

triples=list(itertools.product((1,-1),repeat=3))
rhs_cols=[]
for tr in triples:
    plus=set(c5_nodes[tr+(1,)])
    minus=set(c5_nodes[tr+(-1,)])
    p_un=[int(k in plus)+int(k in minus) for k in range(24)]
    rhs_cols.append([0]*64+[0]*24+p_un+[16])

# Exact rational Gauss-Jordan on A with all eight RHS columns at once.
M=[[Fraction(x) for x in A[r]]+[Fraction(rhs_cols[j][r]) for j in range(8)] for r in range(len(A))]
row=0; piv=[]
for col in range(64):
    p=next((r for r in range(row,len(M)) if M[r][col]),None)
    if p is None: continue
    M[row],M[p]=M[p],M[row]
    d=M[row][col]
    M[row]=[x/d for x in M[row]]
    for r in range(len(M)):
        if r==row: continue
        f=M[r][col]
        if f: M[r]=[x-f*y for x,y in zip(M[r],M[row])]
    piv.append(col); row+=1
if len(piv)!=64:
    raise SystemExit(f"exceptional+sigma_c+degree conditions do not determine pair class uniquely; rank={len(piv)}")
for r in range(row,len(M)):
    if any(M[r][64+j] for j in range(8)):
        raise SystemExit("pair extraction linear system inconsistent")
solutions=[]
for j in range(8):
    x=[Fraction(0) for _ in range(64)]
    for r,col in enumerate(piv): x[col]=M[r][64+j]
    if any(v.denominator!=1 for v in x):
        raise SystemExit(f"nonintegral total pair solution {triples[j]}")
    solutions.append([int(v) for v in x])

def addi(a,b): return [x+y for x,y in zip(a,b)]
def subi(a,b): return [x-y for x,y in zip(a,b)]
def scalei(k,a): return [k*x for x in a]
def psq(v): return int(pairing(v,v,gram))

pair_rows=[]; total_by_triple={}
for tr,total in zip(triples,solutions):
    plus=set(c5_nodes[tr+(1,)])
    correction=[0]*64
    corr_coeff=[]
    for local_k,E in enumerate(contracted,24):
        m=int(local_k in plus)  # smooth C5 => multiplicity one at each incident node
        corr_coeff.append(m)
        if m: correction=addi(correction,E)
    strict=subi(total,correction)
    if row_times_matrix(total,c_action)!=total or row_times_matrix(strict,c_action)!=strict:
        raise SystemExit(f"pair sigma_c invariance regression {tr}")
    if any(pairing(total,E,gram)!=0 for E in contracted):
        raise SystemExit(f"total pair not orthogonal to contracted packet {tr}")
    if pairing(total,hyperplane,gram)!=16 or pairing(strict,hyperplane,gram)!=16:
        raise SystemExit(f"pair degree regression {tr}")
    # Recheck all exceptional pairings against geometry.
    plus_nodes=set(c5_nodes[tr+(1,)])
    minus_nodes=set(c5_nodes[tr+(-1,)])
    for k,E in enumerate(known[92:140]):
        strict_expected=int(k in plus_nodes)+int(k in minus_nodes)
        if pairing(strict,E,gram)!=strict_expected:
            raise SystemExit(f"strict pair exceptional incidence regression {tr}, E{k}")
    total_by_triple[tr]=total
    pair_rows.append({
        "sign_triple":list(tr),
        "c5_plus_exceptional_indices_0based":sorted(plus_nodes),
        "c5_minus_exceptional_indices_0based":sorted(minus_nodes),
        "contracted_correction_coefficients_24":corr_coeff,
        "strict_pair_INDLIST64":strict,
        "total_pullback_pair_INDLIST64":total,
        "strict_pair_square":psq(strict),
        "total_pullback_pair_square":psq(total),
    })

anti_checks={}
for tr in triples:
    anti=tuple(-x for x in tr)
    anti_checks[str(tr)]=addi(total_by_triple[tr],total_by_triple[anti])==scalei(2,hyperplane)

residual=[]
for e2,e3 in itertools.product((1,-1),repeat=2):
    chosen=(1,e2,e3); anti=(-1,-e2,-e3)
    residual.append({
        "chosen_section_representative":list(chosen),
        "residual_antipodal_pair":list(anti),
        "strict_pair_INDLIST64":next(r["strict_pair_INDLIST64"] for r in pair_rows if tuple(r["sign_triple"])==anti),
        "total_pullback_pair_INDLIST64":total_by_triple[anti],
    })

summary={
    "schema":"STAGE35_EX_GOAL4AF_C5_LOCAL_NODE_LATTICE_DIAGNOSTIC_V1",
    "upstream_git_blob_sha1":UPSTREAM_BLOB,
    "source_tuple_order_convention":convention,
    "explicit_singular_node_count":48,
    "retained_exceptional_signature_count":48,
    "contracted_packet_equals_c_zero_nodes":True,
    "c5_individual_count":16,
    "c5_node_count_histogram":{str(n):sum(1 for x in c5_nodes.values() if len(x)==n) for n in sorted(set(map(len,c5_nodes.values())))},
    "c5_all_incident_nodes_smooth_multiplicity_one":True,
    "pair_characterization_matrix_rank":len(piv),
    "pair_count":8,
    "pair_rows":pair_rows,
    "antipodal_total_pair_sum_equals_2H":all(anti_checks.values()),
    "antipodal_checks":anti_checks,
    "goal4ac_residual_pair_count":4,
    "goal4ac_residual_pairs":residual,
    "remote_cas_used":False,
    "target_span_computed":False,
    "theorem_credit":False,
    "endpoint_credit":False,
}
print("GOAL4AF_LOCAL_NODE_LATTICE_JSON="+json.dumps(summary,sort_keys=True,separators=(",",":")))
