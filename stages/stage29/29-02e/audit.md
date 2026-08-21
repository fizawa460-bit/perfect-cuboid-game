# Stage29-02e — fresh audit

```text
AUDITED_PR=1298
AUDITED_SUBMISSION_HEAD=dc8fdded6c58f99f1841d17a4a50145515b08822
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
```

## Verdict

The endpoint L-function source lock is correct, the three coordinate-sign K3 models are the literal quotient models, and the finite-field trace table is internally consistent. The audit strengthens the submission in one decisive way: the global K3/newform assignment does not need to be inferred from fourteen Frobenius samples.

The canonical coordinate-sign eigenspaces give a global decomposition of the endpoint transcendental representation into the seven coordinate K3 transcendental pieces. Combining this with Testa--Stoll's `3 K_b + 1 K_c + 3 K_a` Q-isomorphism orbits and Horie--Yamauchi's `3 h16 + h32 + 3 h8` decomposition proves

```text
K_b -> h16,
K_c -> h32,
K_a -> h8
```

globally at the semisimple l-adic non-Tate level. Consequently

```text
Stage19 -> h16,
Stage20 -> h32,
T(X_cross) = 2*h16 + 3*h8.
```

The detailed proof is `global-k3-eigenspace-adapter.md`.

## Source audit

Horie--Yamauchi arXiv `2512.22520v3` was checked against the current v3 source. Theorem 1.1 / Corollary 4.6 give

```text
L(H2(Sbar)) = L(h16)^3 L(h32) L(h8)^3 L(s-1,L_ell),
```

and Theorem 4.4 gives, after scalar extension to `Qbar_l`,

```text
H2(Sbar)_nonT = V_h16^3 + V_h32 + (chi_2 tensor V_h32)^3,
chi_2 tensor V_h32 ~= V_h8.
```

Testa--Stoll Section 6 was checked for the seven coordinate-sign K3 quotients, the Q-isomorphism of the three `K_a` and three `K_b` quotients, the isomorphism `K_a ~= K_c` over `Q(i)`, and the Euler-brick interpretation of `K_c`.

Two wording repairs are required in the source lock:

1. Theorem 4.4's displayed decomposition is over `Qbar_l` after scalar extension, not literally an unqualified `Q_l` direct sum.
2. The `34/26/1/3` statement is the field-of-definition distribution of a chosen generating set of irreducible divisors, not a partition statement about every Picard class.

These repairs do not alter any mathematical conclusion.

## Finite-field A1-resolution audit

The submission trace script detects rational singular points by Jacobian rank and then uses the A1 resolution correction

```text
#K_smooth(F_p) = #K_singular(F_p) + p * (# rational A1 nodes).
```

Fresh audit independently checked the missing local condition at every rational singular point for every tested prime. For each rank-two Jacobian point, the unique quadratic relation among the three defining equations was restricted to the three-dimensional projective tangent quotient; its quadratic form has full rank `3` in every case.

```text
primes=3,5,7,11,13,17,19,23,29,31,37,41,43,47

K_c rational nodes=12 at every tested prime; all A1
K_b rational nodes=8 or 16 according to the prime; all A1
K_a rational nodes=4 or 12 according to the prime; all A1
```

Thus the `+p` correction is exact for every rational singularity used in the committed trace table. A smooth conic over a finite field has `p+1` points, so replacing one rational A1 point by its exceptional conic changes the count by exactly `p`.

```text
FINITE_FIELD_TRACE_REGRESSION=PASS_EXACT
RATIONAL_NODE_A1_TYPE_AUDIT=PASS
FINITE_PRIME_MATCH_USED_AS_GLOBAL_PROOF=false
```

## Global coordinate-K3 audit

Testa--Stoll give

```text
omega_Sbar = O_Sbar(1),
pg=7,
h11=64,
rho=64.
```

For the sign change of one canonical coordinate, the four quadrics are invariant and the ambient determinant is `-1`. In the residue model for canonical sections, the invariant canonical line is therefore exactly the line spanned by that changed coordinate. The seven K3 quotient pullbacks give seven distinct `H20` lines.

Since `rank T(S)=78-64=14` and `T(S)_C=H20+H02`, each coordinate K3 transcendental lattice injects with rank exactly `2`, the seven pieces are disjoint, and their direct sum exhausts `T(S)`. This makes the orbit multiplicity comparison load-bearing and discharges `R29-L3` globally.

```text
R29-L3=DISCHARGED
K_B_TO_H16=PASS_GLOBAL
K_C_TO_H32=PASS_GLOBAL
K_A_TO_H8=PASS_GLOBAL
STAGE19_TO_H16=PASS_GLOBAL
STAGE20_TO_H32=PASS_GLOBAL
```

## V4 cross quotient

The audited Stage29-02b V4 quotient diamond gives the three nontrivial character pieces `X_sp`, `X_face`, and `X_cross` over rational `Y`. Therefore the non-Tate cross piece is globally

```text
2*h16 + 3*h8.
```

This closes the non-Tate portion of `R29-L2` but not the complete L-function.

```text
R29-L2-NT=DISCHARGED
R29-L2-ALG=OPEN_BOUNDED
R29-L2-BAD=OPEN_BOUNDED
FULL_CROSS_LFUNCTION_COMPLETE=false
```

## Routing

No Stage16--28 backflow is required. The new arithmetic identification is Stage29-native and should feed later joint-local arithmetic and endpoint routing.

PR #1297 / Stage29-02d is already merged and the canonical controller is synchronized during this audit.

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_02E_AUDIT=PASS
BOUNDED_REPAIR=GLOBAL_EIGENSPACE_PROOF_PLUS_SOURCE_SCOPE_AND_A1_LOCAL_CHECK
SOURCE_LOCK_AUDIT=PASS_AFTER_SCOPE_REPAIR
FINITE_FIELD_TRACE_AUDIT=PASS
R29_L3=DISCHARGED
R29_L2_NONTATE=DISCHARGED
R29_L2_ALG=OPEN_BOUNDED
R29_L2_BAD=OPEN_BOUNDED
FULL_CROSS_LFUNCTION_COMPLETE=false
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-02f
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
