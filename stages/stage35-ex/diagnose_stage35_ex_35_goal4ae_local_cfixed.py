#!/usr/bin/env python3
from __future__ import annotations

import ast
import json
import runpy
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PIC = ROOT / 'stages/stage33/33-07/certify_two_coordinate_swap_picard_rows.py'
PIC_DIR = str(PIC.parent)
if PIC_DIR not in sys.path:
    sys.path.insert(0, PIC_DIR)
ns = runpy.run_path(str(PIC))

RANK = 64
HP = 63
INDLIST = list(ns['INDLIST'])
known = [[int(x) for x in r] for r in ns['known']]
gram = [[int(x) for x in r] for r in ns['gram']]
hyperplane = [int(x) for x in ns['hyperplane']]
perms = [[int(x) for x in p] for p in ns['perms']]
q = [[int(x) for x in r] for r in ns['parsed']['q']]
qinv = ns['qinv']
basis_pairing_inv = ns['basis_pairing_inv']
row_times_fraction_matrix = ns['row_times_fraction_matrix']
integral_row = ns['integral_row']
row_times_matrix = ns['row_times_matrix']
mm = ns['mm']
transpose = ns['transpose']
pairing = ns['pairing']

I = [[int(i == j) for j in range(RANK)] for i in range(RANK)]

def add(a,b): return [x+y for x,y in zip(a,b)]
def sub(a,b): return [x-y for x,y in zip(a,b)]
def mat_eq(a,b): return a == b

def action_from_perm(p):
    return [known[p[j-1]-1] for j in INDLIST]

actions = [action_from_perm(p) for p in perms]
# Upstream automorphism indices 4..9 are the six a_i/b_i sign changes.
# Their product is projectively the sign change c -> -c.
c_action = I
for A in actions[3:9]:
    c_action = mm(c_action, A)
if mm(c_action, c_action) != I:
    raise SystemExit('c action is not involutive')
if row_times_matrix(hyperplane, c_action) != hyperplane:
    raise SystemExit('c action does not fix H')
if mm(mm(c_action, gram), transpose(c_action)) != gram:
    raise SystemExit('c action is not a Gram isometry')

# Exact Hperp basis in primitive INDLIST64 coordinates.  Stage32 stores
# q=-Gram(Hperp), so the pairing row of basis vector e_i is [0,-q_i].
hp_basis = []
for i in range(HP):
    prow = [0] + [-q[i][j] for j in range(HP)]
    e = integral_row(row_times_fraction_matrix(prow, basis_pairing_inv), f'Hperp basis {i}')
    if pairing(e, hyperplane, gram) != 0:
        raise SystemExit('Hperp basis lost orthogonality')
    hp_basis.append(e)
for i in range(HP):
    for j in range(HP):
        if pairing(hp_basis[i], hp_basis[j], gram) != -q[i][j]:
            raise SystemExit('Hperp Gram reconstruction mismatch')

# c action on Hperp coordinates: e_i*c = sum_j Ac[i,j] e_j.
Ac = []
for i,e in enumerate(hp_basis):
    ec = row_times_matrix(e, c_action)
    lin = [pairing(ec, hp_basis[j], gram) for j in range(HP)]
    coeff = []
    for j in range(HP):
        z = -sum(Fraction(lin[k]) * qinv[k][j] for k in range(HP))
        if z.denominator != 1:
            raise SystemExit(f'nonintegral c action on Hperp row {i}')
        coeff.append(int(z))
    Ac.append(coeff)
I63 = [[int(i == j) for j in range(HP)] for i in range(HP)]
if mm(Ac, Ac) != I63:
    raise SystemExit('Hperp c action not involutive')
if mm(mm(Ac, q), transpose(Ac)) != q:
    raise SystemExit('Hperp c action does not preserve q')

# Let x be Hperp coordinates.  For D=H+w, H.D=16 and D^2=-4 are
# exactly q(x)=20.  Restrict first to the saturated c-fixed integer kernel,
# then enumerate all norm <=20 vectors with PARI qfminim (Fincke-Pohst).
def gp_matrix(M):
    return '[' + ';'.join(','.join(str(int(x)) for x in row) for row in M) + ']'

gp = f'''q={gp_matrix(q)};
A={gp_matrix(Ac)};
K=matkerint((A-matid({HP}))~);
rk=matsize(K)[2]; print("FIXED_RANK="rk);
Q=K~*q*K;
R=qfminim(Q,20,,0);
print("ENUM_TOTAL_SIGNED="R[1]);
V=R[3]; print("ENUM_STORED_MOD_SIGN="matsize(V)[2]);
for(j=1,matsize(V)[2], if(qfeval(Q,V[,j])==20, print("X="Vec(K*V[,j]))));
'''
with tempfile.NamedTemporaryFile('w', suffix='.gp', delete=False) as f:
    f.write(gp)
    gp_path = f.name
try:
    cp = subprocess.run(['gp','-qf',gp_path], text=True, capture_output=True, timeout=240)
finally:
    Path(gp_path).unlink(missing_ok=True)
if cp.returncode != 0:
    print(cp.stdout); print(cp.stderr)
    raise SystemExit('PARI qfminim failed')
fixed_rank = None; enum_total = None; stored = None; half = []
for line in cp.stdout.splitlines():
    line=line.strip()
    if line.startswith('FIXED_RANK='): fixed_rank=int(line.split('=',1)[1])
    elif line.startswith('ENUM_TOTAL_SIGNED='): enum_total=int(line.split('=',1)[1])
    elif line.startswith('ENUM_STORED_MOD_SIGN='): stored=int(line.split('=',1)[1])
    elif line.startswith('X='):
        x=[int(v) for v in ast.literal_eval(line.split('=',1)[1])]
        if len(x)!=HP: raise SystemExit('PARI vector width regression')
        half.append(x)
if fixed_rank != 19:
    raise SystemExit(f'expected c-fixed Hperp rank 19, got {fixed_rank}')
if enum_total is None or stored is None:
    raise SystemExit('missing PARI enumeration metadata')

xs = []
seenx=set()
for x in half:
    for z in (x,[-a for a in x]):
        t=tuple(z)
        if t not in seenx:
            seenx.add(t); xs.append(z)

def qnorm(x):
    return sum(x[i]*q[i][j]*x[j] for i in range(HP) for j in range(HP))

def divisor_from_x(x):
    lin=[-sum(x[i]*q[i][j] for i in range(HP)) for j in range(HP)]
    return integral_row(row_times_fraction_matrix([16]+lin,basis_pairing_inv),'candidate divisor')

candidates=[]
for x in xs:
    if qnorm(x)!=20: raise SystemExit('PARI exact norm regression')
    d=divisor_from_x(x)
    if pairing(d,hyperplane,gram)!=16 or pairing(d,d,gram)!=-4:
        raise SystemExit('candidate Picard invariant regression')
    if row_times_matrix(d,c_action)!=d:
        raise SystemExit('candidate is not c-fixed')
    candidates.append(d)
raw_set={tuple(d) for d in candidates}
if len(raw_set)!=len(candidates): raise SystemExit('candidate duplicate regression')

# Build source-bound K-style numerical-effectivity receivers C+c(C).
# The first 92 are source curves; the last 48 are exceptional classes.
def csum(v): return add(v,row_times_matrix(v,c_action))
def uniq(rows):
    out=[]; seen=set()
    for r in rows:
        t=tuple(r)
        if any(t) and t not in seen:
            seen.add(t); out.append(r)
    return out
curve_receivers=uniq([csum(v) for v in known[:92]])
all_receivers=uniq([csum(v) for v in known])
exceptional_receivers=uniq([csum(v) for v in known[92:]])

def nonnegative(d, receivers):
    return all(pairing(d,r,gram)>=0 for r in receivers)
def exceptional_le2(d):
    return all(pairing(d,r,gram)<=2 for r in exceptional_receivers)

sets={
    'raw': raw_set,
    'curve_nonnegative': {tuple(d) for d in candidates if nonnegative(d,curve_receivers)},
    'all_nonnegative': {tuple(d) for d in candidates if nonnegative(d,all_receivers)},
    'curve_nonnegative_exceptional_le2': {tuple(d) for d in candidates if nonnegative(d,curve_receivers) and exceptional_le2(d)},
    'all_nonnegative_exceptional_le2': {tuple(d) for d in candidates if nonnegative(d,all_receivers) and exceptional_le2(d)},
}

# Orbit sizes under all nine source-locked Aut(S) generators, restricted to
# each candidate set.  c is central so these preserve the c-fixed locus.
def orbit_sizes(S):
    unseen=set(S); sizes=[]
    while unseen:
        seed=next(iter(unseen)); orb={seed}; queue=[list(seed)]
        while queue:
            v=queue.pop()
            for A in actions:
                w=tuple(row_times_matrix(v,A))
                if w not in S:
                    return ['NOT_STABLE']
                if w not in orb:
                    orb.add(w); queue.append(list(w))
        unseen-=orb; sizes.append(len(orb))
    return sorted(sizes)

summary={
    'schema':'STAGE35_EX_GOAL4AE_LOCAL_CFIXED_DIAGNOSTIC_V1',
    'fixed_hperp_rank':fixed_rank,
    'pari_enum_total_signed_norm_le20':enum_total,
    'pari_stored_mod_sign_norm_le20':stored,
    'norm20_signed_candidate_count':len(candidates),
    'receiver_counts':{
        'curve_csum_unique':len(curve_receivers),
        'all_csum_unique':len(all_receivers),
        'exceptional_csum_unique':len(exceptional_receivers),
    },
    'candidate_counts':{k:len(v) for k,v in sets.items()},
    'orbit_sizes':{k:orbit_sizes(v) for k,v in sets.items()},
    'remote_cas_used':False,
    'theorem_credit':False,
    'endpoint_credit':False,
}
print(json.dumps(summary,indent=2,sort_keys=True))
