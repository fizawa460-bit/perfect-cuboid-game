#!/usr/bin/env python3
from __future__ import annotations

import json
import runpy
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "stages/stage35-ex/diagnose_stage35_ex_35_goal4ag_degree25_residual.py"
PERMS = ROOT / "stages/stage33/33-07/galois-known-class-permutations.json"

# Goal4AG already reconstructs the exact 69-support target, its positive/negative
# parts P,N, the canonical/hyperplane class H, the retained 140 irreducible
# curves, and the primitive Picard Gram matrix.
base = runpy.run_path(str(BASE))
H = base["H"]
Pc = base["Pc"]
Nc = base["Nc"]
P = [int(x) for x in base["P"]]
N = [int(x) for x in base["N"]]
known = [[int(x) for x in r] for r in base["known"]]
gram = sp.Matrix(base["gram"])
assert Pc == Nc
assert len(P) == len(N) == len(known) == 140
assert all(len(r) == 64 for r in known)

perms = json.loads(PERMS.read_text())
assert perms["canonical_sha256"] == "e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30"
cc = [int(x) for x in perms["cc_permutation_1based"]]
ct = [int(x) for x in perms["ct_permutation_1based"]]

def permute_formal(v, p):
    out = [0] * len(v)
    for i, c in enumerate(v, 1):
        out[p[i - 1] - 1] = c
    return out

# Positive and negative effective target parts are literal Galois-stable divisor
# packets, not merely invariant Picard classes.  Hence 31K-P and 31K-N are
# line bundles defined over Q.
assert permute_formal(P, cc) == P
assert permute_formal(P, ct) == P
assert permute_formal(N, cc) == N
assert permute_formal(N, ct) == N

Hvec = [int(x) for x in list(H)]
Pvec = [int(x) for x in list(Pc)]
G = [[int(gram[i, j]) for j in range(64)] for i in range(64)]

def transform(v):
    return [sum(v[i] * G[i][j] for i in range(64)) for j in range(64)]

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def qvec(a, b):
    return dot(transform(a), b)

tknown = [transform(r) for r in known]
pairmat = [[dot(tknown[j], known[k]) for k in range(140)] for j in range(140)]
Hpair = [qvec(Hvec, r) for r in known]
Ppair = [qvec(Pvec, r) for r in known]

# Stoll--Testa, The surface parametrizing cuboids, revised 2025-02-24,
# pp. 3--4: O_S(K_S) = b^* O_{Sbar}(1), K_S^2=16,
# chi(O_S)=8, and K_S is big and nef.  Thus the retained H is K_S.
K2 = 16
CHI_O = 8
assert qvec(Hvec, Hvec) == K2
assert qvec(Hvec, Pvec) == 396
assert all(pairmat[j][j] == -4 for j in range(92))
assert all(pairmat[j][j] == -2 for j in range(92, 140))

# Re-run only the first surviving Goal4AG degree.  Every subtraction is justified
# by a negative intersection with a retained irreducible curve, hence is a forced
# fixed component for any effective representative of the current class.
d = 31
D0 = [d * Hvec[u] - Pvec[u] for u in range(64)]
D = list(D0)
ints = [d * Hpair[k] - Ppair[k] for k in range(140)]
counts = [0] * 140
strip_sequence = []
while True:
    neg = [j for j, x in enumerate(ints) if x < 0]
    if not neg:
        break
    j = min(neg, key=lambda t: (ints[t], t))
    strip_sequence.append({"known_index_1based": j + 1, "intersection_before": int(ints[j])})
    D = [D[u] - known[j][u] for u in range(64)]
    ints = [ints[k] - pairmat[j][k] for k in range(140)]
    counts[j] += 1
    if len(strip_sequence) > 20000:
        raise SystemExit("Goal4AH fixed-component strip step cap")

initial_k_degree = qvec(Hvec, D0)
final_k_degree = qvec(Hvec, D)
final_square = qvec(D, D)
assert initial_k_degree == 100
assert len(strip_sequence) == 325
assert sum(counts[:92]) == 2
assert sum(counts[92:]) == 323
assert sum(x != 0 for x in counts) == 44
assert final_k_degree == 96
assert final_square == 212
assert min(ints) >= 0
assert all(step["intersection_before"] < 0 for step in strip_sequence)

# Surface Riemann--Roch:
# chi(O(D)) = chi(O_S) + (D.(D-K))/2 = 8 + (212-96)/2 = 66.
# Serre duality gives h^2(D)=h^0(K-D).  Since K is nef and
# K.(K-D)=16-96=-80<0, K-D cannot be effective; hence h^2(D)=0.
# Therefore h^0(D)=66+h^1(D) >= 66, so the stripped residual is effective.
rr_numerator = final_square - final_k_degree
assert rr_numerator % 2 == 0
chi_D = CHI_O + rr_numerator // 2
k_minus_d_k_degree = K2 - final_k_degree
assert chi_D == 66
assert k_minus_d_k_degree == -80
assert k_minus_d_k_degree < 0
h2_zero_by_nef_K = True
h0_lower_bound = chi_D
assert h0_lower_bound > 0

# The stripped curves are forced fixed components, so adding them back proves
# the original class 31K-P effective.  The same Picard class is 31K-N because
# Pc=Nc exactly.  P and N are Q-defined above; H^0 commutes with field extension,
# so geometric non-emptiness gives nonzero Q-rational sections of both residual
# line bundles.  This is existence/effectivity credit only, not a materialized
# common residual or an explicit rational function F_B.
out = {
    "schema": "STAGE35_EX_GOAL4AH_DEGREE31_RIEMANN_ROCH_EFFECTIVITY_V1",
    "degree": 31,
    "formal_positive_cc_stable": True,
    "formal_positive_ct_stable": True,
    "formal_negative_cc_stable": True,
    "formal_negative_ct_stable": True,
    "positive_negative_picard_classes_equal": True,
    "canonical_class_equals_hyperplane": True,
    "canonical_square": K2,
    "chi_O_S": CHI_O,
    "canonical_nef": True,
    "initial_residual_K_degree": initial_k_degree,
    "strip_steps": len(strip_sequence),
    "forced_support_count": sum(x != 0 for x in counts),
    "forced_strict_multiplicity_sum": sum(counts[:92]),
    "forced_exceptional_multiplicity_sum": sum(counts[92:]),
    "all_strip_steps_negative": True,
    "final_retained_curve_min_intersection": min(ints),
    "final_residual_K_degree": final_k_degree,
    "final_residual_square": final_square,
    "rr_chi_final_residual": chi_D,
    "K_minus_final_residual_K_degree": k_minus_d_k_degree,
    "h2_final_residual_zero_by_nef_K": h2_zero_by_nef_K,
    "h0_final_residual_lower_bound": h0_lower_bound,
    "degree31_geometric_effectivity_proved": True,
    "degree31_Q_rational_residual_sections_exist": True,
    "explicit_common_residual_divisor_materialized": False,
    "explicit_F_B_materialized": False,
    "principal_function_formula_materialized": False,
    "full_Br_a_U_computed": False,
    "local_evaluations_computed": False,
    "brauer_manin_obstruction_obtained": False,
    "E1_proved": False,
    "stage35_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
print("GOAL4AH_RR_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
