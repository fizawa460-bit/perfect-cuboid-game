#!/usr/bin/env python3
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "stages/stage35-ex/35ex-22/obvious-surface-brauer-symbol-blocker.md"
CERT = ROOT / "stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json"
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"

doc = DOC.read_text()
cert = json.loads(CERT.read_text())
state = json.loads(STATE.read_text())

# Exact audited parent and pending-audit lifecycle.
assert cert["schema"] == "STAGE35_EX_22_OBVIOUS_SURFACE_BRAUER_SYMBOL_BLOCKER_V1"
assert cert["parent"] == {
    "pr": 1531,
    "hostile_reaudit_review": 5110646292,
    "audited_head_sha": "35431061f571da5b425f30da7974c160685bf1a4",
    "merged_main_sha": "85e12c7b810eaafc13e663a0047111b7f3333e8b",
}
assert state["schema"] == "STAGE35_EX_PESCH_E1_STATE_V21_POST_35EX22_OBVIOUS_BRAUER_SYMBOL_BLOCKER"
assert state["base_main_sha"] == "85e12c7b810eaafc13e663a0047111b7f3333e8b"
parent = state["parent_authority"]
assert parent["unit"] == "35EX-21B"
assert parent["status"] == "AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT"
assert parent["hostile_audit_verdict"] == "PASS"
assert parent["hostile_audit_review"] == 5110646292
assert parent["audited_head_sha"] == "35431061f571da5b425f30da7974c160685bf1a4"
assert parent["merged_main_sha"] == "85e12c7b810eaafc13e663a0047111b7f3333e8b"
assert parent["audited_theorem_credit"] is False

for key in ("35EX-21", "35EX-21B"):
    u = state["completed_units"][key]
    assert u["hostile_audit_verdict"] == "PASS"
    assert u["hostile_audit_review"] == 5110646292
    assert u["audited_head_sha"] == "35431061f571da5b425f30da7974c160685bf1a4"
    assert u["merged_main_sha"] == "85e12c7b810eaafc13e663a0047111b7f3333e8b"
    assert u["audited_theorem_credit"] is False

unit = state["completed_units"]["35EX-22"]
assert unit["status"] == "PROVISIONAL_EXACT_OBVIOUS_BRAUER_SYMBOL_LAYER_BLOCKER_NO_CREDIT"
assert unit["artifact"] == "stages/stage35-ex/35ex-22/obvious-surface-brauer-symbol-blocker.md"
assert unit["certificate"] == "stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json"
assert unit["verifier"] == "stages/stage35-ex/verify_stage35_ex_22.py"
assert unit["obvious_radicand_symbols_trivial"] is True
assert unit["obvious_linear_boundary_squareclass_generators"] == 7
assert unit["obvious_quaternion_presentation_generators"] == 28
assert unit["generic_infinity_residue_presentation_rank"] == 6
assert unit["common_zero_evaluation_adele_for_obvious_symbol_span"] is True
assert unit["obvious_symbol_layer_Brauer_Manin_obstruction"] is False
assert unit["Brauer_group_computed"] is False
assert unit["Brauer_group_trivial"] is False
assert unit["nonobvious_Brauer_classes_ruled_out"] is False
assert unit["audited_theorem_credit"] is False

current = state["current"]
assert current["unit"] == "35EX-22_SURFACE_BRAUER_CLASS_OR_OBVIOUS_SYMBOL_BLOCKER"
assert current["status"] == "PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT"
assert current["candidate"] == "E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER"
assert current["next_if_audited_pass"] == "35EX-23_GENUS5_MULTIQUADRATIC_CHARACTER_QUOTIENT_DESCENT_OR_UNIFORMITY_BLOCKER"
next_ledger = state["candidate_ledger_after_35ex22_provisional"]
assert next_ledger["current_candidate"] == "E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER"
assert next_ledger["next_if_hostile_audit_passes"] == "E1-GENUS5-MULTIQUADRATIC-FIBER-CHARACTER-DESCENT"
assert next_ledger["fresh_breadth_audit_required_for_that_selection"] is False

# Four displayed radicands are already squares in Q(S_PC).
for marker in (
    "1+x^2       = p^2",
    "1+y^2       = q^2",
    "x^2+y^2     = z^2",
    "1+x^2+y^2   = w^2",
):
    assert marker in doc
assert cert["surface"]["four_radicand_squareclasses_trivial"] is True

# Seven conjugate-factor squareclass reductions.
x, y, p, q, z, w = sp.symbols("x y p q z w")
rels = [
    ((p+x)*(p-x)-1, p**2, 1+x**2),
    ((q+y)*(q-y)-1, q**2, 1+y**2),
    ((w+z)*(w-z)-1, w**2-z**2, 1),
    ((z+x)*(z-x)-y**2, z**2, x**2+y**2),
    ((z+y)*(z-y)-x**2, z**2, x**2+y**2),
    ((w+p)*(w-p)-y**2, w**2-p**2, y**2),
    ((w+q)*(w-q)-x**2, w**2-q**2, x**2),
]
subs = {p**2:1+x**2, q**2:1+y**2, z**2:x**2+y**2, w**2:1+x**2+y**2}
for expr, _, _ in rels:
    assert sp.expand(expr.subs(subs)) == 0

gens = ["p+x", "q+y", "w+z", "z+x", "z+y", "w+p", "w+q"]
assert cert["linear_squareclass_generators"] == gens
pres = cert["obvious_quaternion_presentation"]
assert (pres["minus_one_symbols"], pres["pair_symbols"], pres["total_nonconstant_generator_symbols"]) == (7,21,28)
assert pres["independence_claimed"] is False

# Generic infinity residues over Q(T).
T = sp.symbols("T")
X, Y, Z = 1-T**2, 2*T, 1+T**2
basis = ["-1", "2", "T", "T-1", "T+1", "T^2+1"]

def sc(expr):
    expr = sp.factor(sp.cancel(expr))
    num, den = sp.fraction(expr)
    cn, fn = sp.factor_list(num)
    cd, fd = sp.factor_list(den)
    out = set()
    c = sp.Rational(cn, cd)
    if c < 0:
        out.add("-1"); c = -c
    for prime, e in sp.factorint(int(c.p)).items():
        if e % 2: out.symmetric_difference_update({str(prime)})
    for prime, e in sp.factorint(int(c.q)).items():
        if e % 2: out.symmetric_difference_update({str(prime)})
    for fac, e in fn + fd:
        if e % 2:
            monic = sp.Poly(fac, T).monic().as_expr()
            choices = {
                sp.srepr(T): "T",
                sp.srepr(T-1): "T-1",
                sp.srepr(T+1): "T+1",
                sp.srepr(T**2+1): "T^2+1",
            }
            key = choices.get(sp.srepr(sp.expand(monic)))
            assert key is not None, monic
            out.symmetric_difference_update({key})
    assert out <= set(basis), out
    return out

columns = [("-1",i) for i in range(7)] + [(i,j) for i,j in combinations(range(7),2)]
rows = []
for eps, delta, eta in product((1,-1), repeat=3):
    U = [
        2*X if eps == 1 else -1/(2*X),
        2*Y if delta == 1 else -1/(2*Y),
        2*Z if eta == 1 else -1/(2*Z),
        Z+X,
        Z+Y,
        eta*Z+eps*X,
        eta*Z+delta*Y,
    ]
    residues = [sc(-1) if a == "-1" else sc(-U[a]*U[b]) for a,b in columns]
    for basis_element in basis:
        rows.append([int(basis_element in s) for s in residues])

assert len(rows) == 48 and all(len(row) == 28 for row in rows)

def rank_f2(a):
    a = [row[:] for row in a]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((r for r in range(rank,len(a)) if a[r][col]), None)
        if pivot is None: continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for r in range(len(a)):
            if r != rank and a[r][col]:
                a[r] = [u ^ v for u,v in zip(a[r], a[rank])]
        rank += 1
    return rank

assert rank_f2(rows) == 6
boundary = cert["infinity_boundary"]
assert boundary["generic_components"] == 8
assert boundary["presentation_residue_matrix_rows"] == 48
assert boundary["presentation_residue_matrix_columns"] == 28
assert boundary["presentation_residue_rank_F2"] == 6
assert boundary["actual_Brauer_dimension_inferred"] is False

# Exact P0 and Hilbert symbols.
F = Fraction
x0, y0, p0, q0, z0, w0 = F(272,225), F(0), F(353,225), F(1), F(272,225), F(353,225)
assert p0*p0 == 1+x0*x0
assert q0*q0 == 1+y0*y0
assert z0*z0 == x0*x0+y0*y0
assert w0*w0 == 1+x0*x0+y0*y0
assert all(v != 0 for v in (p0,q0,z0,w0))
fvals = [p0+x0, q0+y0, w0+z0, z0+x0, z0+y0, w0+p0, w0+q0]
assert [str(v) for v in fvals] == cert["common_zero_specialization"]["generator_values"]

def vp(a,l):
    a=F(a); n,d,e=a.numerator,a.denominator,0
    while n and n%l==0: n//=l; e+=1
    while d%l==0: d//=l; e-=1
    return e

def unit_mod(a,l,mod):
    a=F(a); e=vp(a,l)
    u=F(a.numerator//(l**e),a.denominator) if e>=0 else F(a.numerator,a.denominator//(l**(-e)))
    return (u.numerator*pow(u.denominator,-1,mod))%mod

def leg(a,l):
    t=pow(a%l,(l-1)//2,l)
    assert t in (1,l-1)
    return 1 if t==1 else -1

def hs_odd(a,b,l):
    A,B=vp(a,l),vp(b,l); ua,ub=unit_mod(a,l,l),unit_mod(b,l,l)
    s=-1 if (A*B*((l-1)//2))%2 else 1
    if B%2: s*=leg(ua,l)
    if A%2: s*=leg(ub,l)
    return s

def hs2(a,b):
    A,B=vp(a,2),vp(b,2); u,v=unit_mod(a,2,8),unit_mod(b,2,8)
    e=(((u-1)//2)*((v-1)//2)+A*((v*v-1)//8)+B*((u*u-1)//8))%2
    return -1 if e else 1

def primes_for(a,b):
    ans={2}
    for value in (F(a),F(b)):
        ans.update(sp.factorint(abs(value.numerator)).keys())
        ans.update(sp.factorint(abs(value.denominator)).keys())
    return sorted(ans)

def splits_everywhere(a,b):
    if F(a)<0 and F(b)<0: return False
    for l in primes_for(a,b):
        if (hs2(a,b) if l==2 else hs_odd(a,b,l)) != 1: return False
    return True

for value in fvals:
    assert splits_everywhere(F(-1),value)
for i,j in combinations(range(7),2):
    assert splits_everywhere(fvals[i],fvals[j])
assert cert["common_zero_specialization"]["all_28_quaternion_generators_split_over_every_Q_v"] is True
assert cert["adelic_deformation"]["common_zero_evaluation_adele_exists"] is True

# No overclaim / exact route boundary.
for marker in (
    "OBVIOUS_RADICAND_SYMBOLS_TRIVIAL=true",
    "OBVIOUS_LINEAR_BOUNDARY_SQUARECLASS_GENERATORS=7",
    "OBVIOUS_QUATERNION_PRESENTATION_GENERATORS=28",
    "GENERIC_INFINITY_RESIDUE_PRESENTATION_RANK=6",
    "COMMON_ZERO_EVALUATION_ADELE_FOR_OBVIOUS_SYMBOL_SPAN=true",
    "OBVIOUS_SYMBOL_LAYER_BRAUER_MANIN_OBSTRUCTION=false",
    "CURRENT_OBVIOUS_SURFACE_BRAUER_SYMBOL_LAYER=FROZEN_COMMON_ZERO_EVALUATION_ADELE_NO_OBSTRUCTION",
    "BRAUER_GROUP_COMPUTED=false",
    "BRAUER_GROUP_TRIVIAL=false",
    "NONOBVIOUS_BRAUER_CLASSES_RULED_OUT=false",
    "BRAUER_OBSTRUCTION_PROVED=false",
    "E1_PROVED=false",
    "STAGE35_CLOSED=false",
):
    assert marker in doc

for key in (
    "new_theorem_credit",
    "primitive_source_population_reverse_adapter_proved",
    "global_surface_rational_points_classified",
    "brauer_obstruction_proved",
    "R29_PESCH_E1_closed",
    "R29_FIB2_closed",
    "J12_PARAMETRIC_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert state["claims"][key] is False
assert state["arsenal"]["S33_PW07"] == "PROVISIONAL_ROUTING_ONLY_REQUIRES_EXISTING_BRAUER_REPRESENTATIVE_COMMON_COCYCLE_AND_TORSOR_NOT_A_CLASS_CONSTRUCTOR"

print("PASS STAGE35_EX_22_OBVIOUS_SURFACE_BRAUER_SYMBOL_BLOCKER")
