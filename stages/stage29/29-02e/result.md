# Stage29-02e — endpoint L-function, coordinate-K3 modular traces, and cross quotient

```text
TASK=Stage29-02e
STATUS=SUBMISSION_PENDING_FRESH_AUDIT
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## Executive result

This suffix completes the previously unfinished Stage29-02e package and sharpens it with a reproducible exact finite-field calculation.

The endpoint L-function is already explicitly known from Horie--Yamauchi. The missing project adapter was to identify which modular summand belongs to which natural K3 quotient used by Stage19/20.

The exact regression at 14 odd primes gives the unique clean assignment

```text
K_b orbit -> h16,
K_c       -> h32,
K_a orbit -> h8.
```

This matches both multiplicity patterns

```text
coordinate K3s:  3 K_b + 1 K_c + 3 K_a
endpoint forms:  3 h16 + 1 h32 + 3 h8.
```

The assignment is submitted as `PASS_CANDIDATE`, not self-certified as a global l-adic theorem.

## A. Endpoint source lock

Horie--Yamauchi arXiv:2512.22520v3 prove

```text
H2_nonT(Sbar)
 = 3 V_h16 + V_h32 + 3 V_h8
```

with explicit Tate/Dirichlet algebraic summands. Consequently, for good odd `p`,

```text
T_Sbar(p)
 = 3 a_p(h16) + a_p(h32) + 3 a_p(h8)
   + p*(10+2 chi_-1(p)+chi_-2(p)+3 chi_2(p)),

#Sbar(F_p)=1+p^2+T_Sbar(p).
```

This is an exact endpoint finite-field oracle, not a rational-point theorem over Q.

## B. Exact quotient models

Three representative coordinate quotients are counted directly:

```text
K_c  = forget long diagonal c      = Euler-brick / Stage20 orbit,
K_b1 = forget a face diagonal b1   = Stage19 space-completion orbit,
K_a1 = forget a side coordinate a1 = third coordinate-sign orbit.
```

The models are exact eliminations of the four endpoint quadrics. No family parametrization or heuristic sampling is used.

## C. Reproducible exact computation

`k3_trace_check.py` uses only exact arithmetic modulo `p` and no external package. It:

1. enumerates projective points of each three-quadric singular model;
2. detects rational singularities by exact Jacobian rank mod `p`;
3. adds `p` for each rational A1 exceptional curve to obtain the smooth K3 point count;
4. computes `T=#K(F_p)-1-p^2`;
5. compares against the candidate newform plus algebraic-character trace.

The checked primes are

```text
3,5,7,11,13,17,19,23,29,31,37,41,43,47.
```

All assertions pass exactly.

The resulting formulas are

```text
K_b:
 T_Kb(p)=a_p(h16)+p*(15+5 chi_-1(p)).

K_c:
 T_Kc(p)=a_p(h32)+p*(16+chi_-1(p)+3 chi_2(p)).

K_a:
 T_Ka(p)=a_p(h8)
         +p*(13+4 chi_-1(p)+2 chi_2(p)+chi_-2(p)).
```

## D. Stage19 / Stage20 arithmetic labels

Using the already-merged Stage29-02b geometric adapter:

```text
Stage19 space K3 = K_b orbit,
Stage20 Euler K3 = K_c.
```

Therefore the candidate modular labels are

```text
Stage19 -> h16,
Stage20 -> h32.
```

This converts the earlier geometric comparison into an explicit Frobenius/modular comparison.

## E. Cross quotient

The exact V4 finite-field identity is

```text
#X_joint=#X_face+#X_sp+#X_cross-2#Y.
```

Since rational `Y` contributes no non-Tate part, the candidate global semisimple non-Tate subtraction is

```text
H2_nonT(X_cross)
 = (3 h16 + h32 + 3 h8) - h16 - h32
 = 2 h16 + 3 h8.
```

Its dimension is `10`, exactly matching the independent Stage29-02b prediction `pg_cross=5`, for which `2 pg=10`.

This is a strong consistency check and reduces `R29-L2` to the audit status of the K3/newform identification plus a separate algebraic/boundary/bad-prime ledger.

## F. What remains open

The following are deliberately not promoted:

```text
GLOBAL_LADIC_KB_EQUALS_H16_PROVED=false
GLOBAL_LADIC_KC_EQUALS_H32_SELF_CERTIFIED=false
GLOBAL_LADIC_KA_EQUALS_H8_PROVED=false
FULL_CROSS_LFUNCTION_WITH_BAD_PRIMES=false
CROSS_ALGEBRAIC_TATE_LEDGER_COMPLETE=false
RATIONAL_POINT_SET_COMPUTED=false
PHYSICAL_HEIGHT_COUNT_OBTAINED=false
```

Fresh audit should decide whether the quotient geometry, CM structure and exact traces already discharge `R29-L3`, or whether a short formal representation-identification lemma remains.

## G. Receivers after submission

```text
R29-L3
 = CoordinateSignK3QuotientFrobeniusModuleIdentification
 = PASS_CANDIDATE_BY_EXACT_TRACE_REGRESSION

R29-L2-NT
 = V4CrossQuotientNonTateModularDecomposition
 = PASS_CANDIDATE_CONDITIONAL_ON_R29-L3

R29-L2-ALG
 = CompatibleResolutionBoundaryAndAlgebraicTateCharacterLedger
 = OPEN_BOUNDED

R29-L2-BAD
 = CrossQuotientBadPrimeLocalFactorLedger
 = OPEN_BOUNDED
```

No new Stage16--28 reentry is justified by this suffix. The arithmetic data are Stage29-native and are intended for later 29-09 joint-local arithmetic / endpoint routing.

## Files

- `source-lock.md`
- `frobenius-trace-oracle.md`
- `k3-modular-identification.md`
- `v4-cohomology-rematch.md`
- `k3_trace_check.py`
- `trace-check-output.md`
- `route-contract.json`
- `controller-delta.json`

```text
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM_AFTER_PASS=29-02f
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
