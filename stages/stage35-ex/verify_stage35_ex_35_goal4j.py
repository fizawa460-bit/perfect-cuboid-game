#!/usr/bin/env python3
from __future__ import annotations
import json
from itertools import product
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT/'stages/stage35-ex/35ex-35/goal4j-linked-congruent-number-selmer-coupling-preflight.json'
STATE = ROOT/'stages/stage35-ex/MAIN-STATE.json'
a = json.loads(ART.read_text())
s = json.loads(STATE.read_text())

assert a['schema'] == 'STAGE35_EX_35_GOAL4J_LINKED_CONGRUENT_NUMBER_SELMER_COUPLING_PREFLIGHT_V1'
assert a['status'].startswith('PROVISIONAL_EXACT_')
assert a['base_main_sha'] == s['base_main_sha']
assert a['last_audited_authority']['pr'] == 1633
assert a['stacked_parent']['hostile_audited'] is False

# Exact face -> congruent-number curve map.
U,V,D = sp.symbols('U V D')
N = U*V/2
X = U*(U+D)/2
Y = U**2*(U+D)/2
face_rel = D**2-U**2-V**2
curve_err = sp.factor(Y**2 - X**3 + N**2*X)
assert sp.factor(curve_err - U**3*(U+D)*(U**2+V**2-D**2)/8) == 0
assert sp.rem(sp.Poly(sp.together(curve_err*8), D), sp.Poly(face_rel, D)) == 0
assert sp.factor(X-N - U*(U+D-V)/2) == 0
assert sp.factor(X+N - U*(U+D+V)/2) == 0
assert sp.rem(sp.Poly(sp.together((X*(X-N)*(X+N)-Y**2)*8), D), sp.Poly(face_rel, D)) == 0

# Exact three-face area product and squareclass [2].
A,B,C = sp.symbols('A B C')
Nab,Nac,Nbc = A*B/2, A*C/2, B*C/2
assert sp.factor(Nab*Nac*Nbc - (A*B*C)**2/8) == 0
assert sp.factor(Nab*Nac*Nbc/2 - (A*B*C/4)**2) == 0

# F2 edge-parity -> twist-parity map.
M = ((1,1,0),(1,0,1),(0,1,1))
def mv(e):
    return tuple(sum(r[i]*e[i] for i in range(3)) % 2 for r in M)
allv = list(product((0,1), repeat=3))
image = {mv(e) for e in allv}
kernel = {e for e in allv if mv(e)==(0,0,0)}
assert image == {(0,0,0),(1,1,0),(1,0,1),(0,1,1)}
assert kernel == {(0,0,0),(1,1,1)}
primitive = [e for e in allv if e != (1,1,1)]
pre = {t:[e for e in primitive if mv(e)==t] for t in image}
assert set(pre[(1,1,0)]) == {(1,0,0),(0,1,1)}
assert set(pre[(1,0,1)]) == {(0,1,0),(1,0,1)}
assert set(pre[(0,1,1)]) == {(0,0,1),(1,1,0)}
assert pre[(0,0,0)] == [(0,0,0)]
# Exact rank 2 over F2: all three rows sum to zero, while first two are independent.
assert tuple((M[0][i]+M[1][i]+M[2][i])%2 for i in range(3)) == (0,0,0)
assert M[0] != M[1] and M[0] != (0,0,0) and M[1] != (0,0,0)
# Over F2 two distinct nonzero vectors are dependent only if equal, hence rank >=2; row relation gives rank <=2.

# At 2 division by 2 adds affine 111; total twist parity is odd.
for e in allv:
    t2 = tuple((x+1)%2 for x in mv(e))
    assert sum(t2) % 2 == 1

# Arbitrary odd-q local model: residues are literal nonzero squares 3^2,4^2,5^2.
# For q != 3,5 they are units, so the standard odd-p Hensel square criterion applies.
assert [3**2,4**2,5**2] == [9,16,25]
assert mv((1,0,0)) == (1,1,0)
assert mv((0,1,0)) == (1,0,1)
assert mv((0,0,1)) == (0,1,1)

# Semantic firewalls.
assert a['selmer_coupling_verdict']['individual_selmer_membership_new_condition'] is False
assert a['selmer_coupling_verdict']['cross_twist_selmer_pruning_obtained'] is False
assert a['selmer_coupling_verdict']['finite_global_squareclass_family_obtained'] is False
assert a['scope_boundary']['linked_congruent_number_twist_architecture_obtained'] is True
assert a['scope_boundary']['canonical_face_kummer_classes_obtained'] is True
assert a['scope_boundary']['new_branch_pruning_obtained'] is False
assert a['scope_boundary']['E1_proved'] is False
assert a['scope_boundary']['perfect_cuboid_nonexistence_claim'] is False

assert s['schema'] == 'STAGE35_EX_PESCH_E1_STATE_V47_GOAL4J_LINKED_CONGRUENT_NUMBER_SELMER_PREFLIGHT_PENDING_LATER_AUDIT'
assert s['current']['unit'] == '35EX-35_GOAL4J_LINKED_CONGRUENT_NUMBER_SELMER_COUPLING_PREFLIGHT'
assert s['claims']['goal4j_executed'] is True
assert s['claims']['cross_twist_selmer_pruning_obtained'] is False
assert s['claims']['E1_proved'] is False and s['claims']['stage35_closed'] is False
print('PASS STAGE35_EX_35_GOAL4J_LINKED_CONGRUENT_NUMBER_SELMER_COUPLING_PREFLIGHT_V1')
