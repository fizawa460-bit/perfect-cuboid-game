#!/usr/bin/env python3
import itertools, json, subprocess
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT/'stages/stage35-ex/35ex-35/goal4q-compactification-picard-galois-brauer-candidate-preflight.json'
STATE = ROOT/'stages/stage35-ex/MAIN-STATE.json'
a = json.loads(ART.read_text())

assert a['schema'] == 'STAGE35_EX_35_GOAL4Q_COMPACTIFICATION_PICARD_GALOIS_BRAUER_CANDIDATE_PREFLIGHT_V1'
assert a['singular_locus']['geometric_node_count'] == 48
assert a['singular_locus']['rational_nodes'] == 24
assert a['singular_locus']['Q_i_conjugate_pairs'] == 12
assert a['divisor_configuration']['certified_geometric_picard_rank_lower_bound'] == 53
assert a['brauer_candidate_boundary']['H1_Q_Pic_computed'] is False
assert a['credit_boundary']['E1_proved'] is False

def blob(path):
    return subprocess.check_output(['git','hash-object',str(ROOT/path)], text=True).strip()
assert blob('stages/stage35-ex/35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md') == a['source_locks']['global_surface']['blob_sha']
assert blob('stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json') == a['source_locks']['obvious_brauer_layer']['blob_sha']
assert blob('stages/stage35-ex/35ex-35/goal4p-stage35-specific-vertical-brauer-from-scratch-preflight.json') == a['source_locks']['goal4p']['blob_sha']

h,x,y,p,q,z,w = sp.symbols('h x y p q z w')
vs = [h,x,y,p,q,z,w]
F = [p*p-h*h-x*x, q*q-h*h-y*y, z*z-x*x-y*y, w*w-h*h-x*x-y*y]
J = sp.Matrix([[sp.diff(f,v) for v in vs] for f in F])
mins = [sp.factor(J[:,cols].det()/16) for cols in itertools.combinations(range(7),4)]
I = sp.I
pts=[]
for P,Q,W in itertools.product([1,-1], repeat=3): pts.append((1,0,0,P,Q,0,W))
for P,Y,Z in itertools.product([1,-1],[I,-I],[I,-I]): pts.append((1,0,Y,P,0,Z,0))
for Q,X,Z in itertools.product([1,-1],[I,-I],[I,-I]): pts.append((1,X,0,0,Q,Z,0))
for Q,Z,W in itertools.product([1,-1], repeat=3): pts.append((0,0,1,0,Q,Z,W))
for P,Z,W in itertools.product([1,-1], repeat=3): pts.append((0,1,0,P,0,Z,W))
for Y,P,Qsgn in itertools.product([I,-I],[1,-1],[1,-1]): pts.append((0,1,Y,P,Qsgn*I,0,0))
assert len(pts)==48 and len(set(pts))==48
for pt in pts:
    sub=dict(zip(vs,pt))
    assert all(sp.simplify(f.subs(sub))==0 for f in F)
    assert J.subs(sub).rank()==3
    assert all(sp.simplify(m.subs(sub))==0 for m in mins)

aff_vars=[x,y,p,q,z,w]
aff_polys=[sp.expand(f.subs(h,1)) for f in F] + [sp.expand(m.subs(h,1)) for m in mins if m!=0]
assert len(sp.solve(aff_polys, aff_vars, dict=True))==24

def solve_inf(chart):
    if chart=='x': variables=[y,p,q,z,w]; sub={h:0,x:1}
    else: variables=[x,p,q,z,w]; sub={h:0,y:1}
    polys=[sp.expand(f.subs(sub)) for f in F]+[sp.expand(m.subs(sub)) for m in mins if m!=0]
    return sp.solve(polys, variables, dict=True)
assert len(solve_inf('x'))==16 and len(solve_inf('y'))==16
assert a['singular_locus']['infinity_h_zero']['count']==24
assert sp.expand(F[2]) == z*z-x*x-y*y
assert sp.expand(F[3]-F[1]) == w*w-q*q-x*x
assert sp.expand(F[3]-F[0]) == w*w-p*p-y*y
assert sp.expand(F[0]) == p*p-h*h-x*x
assert sp.expand(F[1]) == q*q-h*h-y*y
assert sp.expand(F[3]-F[2]) == w*w-z*z-h*h

verts=list(itertools.product([0,1], repeat=3)); vi={v:i for i,v in enumerate(verts)}
edges=[]
for v in verts:
    for c in range(3):
        if v[c]==0:
            u=list(v); u[c]=1; u=tuple(u)
            edges.extend([(vi[v],vi[u],c,0),(vi[v],vi[u],c,1)])
assert len(verts)==8 and len(edges)==24
M=sp.zeros(32)
for i in range(8): M[i,i]=-4
for j,(u,v,_,_) in enumerate(edges):
    k=8+j; M[k,k]=-2; M[u,k]=M[k,u]=1; M[v,k]=M[k,v]=1
assert M.rank()==29
Mall=sp.diag(M, *([-2]*24))
assert Mall.shape==(56,56) and Mall.rank()==53
assert a['galois_inventory']['rational_exceptional_curves']==24
assert a['galois_inventory']['nonrational_exceptional_conjugate_pairs']==12
assert a['infinity_boundary']['dual_multigraph']=='3-cube with every edge doubled'
s=json.loads(STATE.read_text())
assert s['schema'].startswith('STAGE35_EX_PESCH_E1_STATE_V54_')
assert s['current']['unit']=='35EX-35_GOAL4Q_COMPACTIFICATION_PICARD_GALOIS_BRAUER_CANDIDATE_PREFLIGHT'
assert s['claims']['geometric_picard_rank_lower_bound_53_obtained'] is True
assert s['claims']['algebraic_brauer_group_computed'] is False
print('PASS Stage35-EX Goal4Q: 48 A1 nodes, doubled-cube boundary, visible Picard rank >=53')
