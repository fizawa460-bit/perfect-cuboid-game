# Stage29-02e — audited endpoint L-function / coordinate-K3 modular rematch

```text
TASK=Stage29-02e
STATUS=AUDITED_PASS_PENDING_MERGE
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## Executive result

Horie--Yamauchi give the endpoint non-Tate representation

```text
T(endpoint) = 3*h16 + h32 + 3*h8.
```

Testa--Stoll give the seven coordinate-sign K3 quotient orbits

```text
3*K_b + 1*K_c + 3*K_a.
```

Fresh audit proves globally, without using finite-prime coincidence as the proof, that the seven coordinate K3 transcendental pieces are the seven canonical coordinate eigenspaces and exhaust the rank-14 endpoint transcendental representation. Hence

```text
K_b -> h16,
K_c -> h32,
K_a -> h8.
```

Using the already-audited Stage29-02b geometric bridge,

```text
Stage19 space-completion K3 -> h16,
Stage20 Euler/third-face K3 -> h32.
```

The V4 cross quotient therefore has global semisimple non-Tate package

```text
T(X_cross) = 2*h16 + 3*h8.
```

The complete algebraic Tate/resolution/bad-prime L-function is not claimed.

## A. Endpoint source lock

Horie--Yamauchi arXiv `2512.22520v3`, Theorem 4.4 / Corollary 4.6, give after scalar extension to `Qbar_l`

```text
H2(Sbar)
 = 3*V_h16 + V_h32 + 3*V_h8 + L_ell(-1),
```

where `h16` has CM by `Q(i)`, `h32` has CM by `Q(sqrt(-2))`, and

```text
V_h8 ~= chi_2 tensor V_h32.
```

The source lock was repaired only to state the scalar-extension field precisely and to describe `34/26/1/3` as the fields of definition of a chosen Picard generating set.

## B. Global coordinate-eigenspace proof

Testa--Stoll prove

```text
omega_Sbar ~= O_Sbar(1),
pg=7,
h11=64,
rho=64.
```

For the sign change of one canonical coordinate, the defining quadrics are invariant while the ambient determinant is `-1`. In the residue realization of `H0(K)`, the invariant line is exactly the line spanned by the changed coordinate.

Thus the seven coordinate K3 quotients pull back the seven distinct canonical `H20` coordinate lines. Since

```text
rank T(S)=78-64=14
```

and there is no transcendental `(1,1)` part, every coordinate K3 has rank-two transcendental part and the seven pieces form a direct sum equal to `T(S)`.

The orbit multiplicities `3+1+3` then compare globally with Horie--Yamauchi's irreducible modular multiplicities `3+1+3`. The unique orbit forces

```text
K_c -> h32.
```

Since `K_a ~= K_c` over `Q(i)`, and `h8 ~= chi_-1 tensor h32` using the `chi_-2` CM self-twist of `h32`,

```text
K_a -> h8,
```

leaving

```text
K_b -> h16.
```

Full details are in `global-k3-eigenspace-adapter.md`.

## C. Exact finite-field regression

The committed dependency-free checker counts the literal quotient models at

```text
p=3,5,7,11,13,17,19,23,29,31,37,41,43,47.
```

Fresh audit additionally checked the local quadratic tangent form at every rational Jacobian-rank-defect point. Every such point is an A1 node, so replacing it by the exceptional conic changes the point count by exactly `p`.

The exact checked formulas remain

```text
K_b:
 T_Kb(p)=a_p(h16)+p*(15+5 chi_-1(p)).

K_c:
 T_Kc(p)=a_p(h32)+p*(16+chi_-1(p)+3 chi_2(p)).

K_a:
 T_Ka(p)=a_p(h8)
         +p*(13+4 chi_-1(p)+2 chi_2(p)+chi_-2(p)).
```

These 14-prime identities are retained as an exact regression oracle. They are no longer load-bearing for the global non-Tate identification, and the displayed algebraic character formulas are not promoted beyond the checked primes for `K_a`/`K_b` without a global Picard-character ledger.

## D. V4 cross quotient

The audited V4 identity has three nontrivial character quotients

```text
X_sp,
X_face,
X_cross
```

over rational `Y`. Since `Y` has no transcendental H2,

```text
T(endpoint)=T(X_sp)+T(X_face)+T(X_cross).
```

Substituting the audited labels gives

```text
T(X_cross)
 = (3*h16+h32+3*h8)-h16-h32
 = 2*h16+3*h8.
```

Its dimension is `10`, matching the independent `pg_cross=5` computation.

## E. Receiver state

```text
R29-L3
 = CoordinateSignK3QuotientFrobeniusModuleIdentification
 = DISCHARGED_GLOBAL_EIGENSPACE_ORBIT_ARGUMENT

R29-L2-NT
 = V4CrossQuotientNonTateModularDecomposition
 = DISCHARGED_GLOBAL_V4_SUBTRACTION

R29-L2-ALG
 = CompatibleResolutionBoundaryAndAlgebraicTateCharacterLedger
 = OPEN_BOUNDED

R29-L2-BAD
 = CrossQuotientBadPrimeLocalFactorLedger
 = OPEN_BOUNDED
```

No rational-point theorem, physical-height count, or perfect-cuboid existence/nonexistence conclusion follows from this L-function decomposition.

## Audit artifacts

- `audit.md`
- `global-k3-eigenspace-adapter.md`
- `source-lock.md`
- `frobenius-trace-oracle.md`
- `k3-modular-identification.md`
- `v4-cohomology-rematch.md`
- `k3_trace_check.py`
- `trace-check-output.md`
- `route-contract.json`
- `controller-delta.json`

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_02E_AUDIT=PASS
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-02f
NEXT_EXPECTED_COMMAND=Stage29-main-batch
FULL_CROSS_LFUNCTION_COMPLETE=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
