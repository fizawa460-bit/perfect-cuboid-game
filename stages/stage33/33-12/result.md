# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_BLOCKED_BY_REOPENED_STAGE33_05_CORRECTED_J2_Q_DESCENT_RESIDUAL_4_OF_5`

Stage33-12 remains open. Stage33-13 is not released. Class-3 promotion is **not** authorized.

## Batch 4 / 4 hostile-audit verdict

The committed four-batch class-2 audit budget is exhausted, but the Batch3 `NO_GO_AFTER_BATCH3` verdict does **not** survive hostile audit. The reason is upstream: the Stage33-05 Q-defined function formerly called the named geometric `J2` representative is geometrically trivial in the exact Creutz--Viray function quotient.

The hostile regression proves the old Q-defined `ell_Q` is diagonal scalar times component squares in

```text
Lbar^*/(Kbar^* Lbar^{*2}),  Kbar=Qbar(t),
```

hence `[ell_Q]=0`. Certificate: `j2-cv-lclass-zero-regression.json`.

This revokes the old named-representative/Q-descent witness but does not revoke the abstract geometric basis element `J2`.

## Repair R1--R4

The upstream Stage33-05 repair reconstructed the class without reusing the revoked witness:

```text
R1 abstract J2 nonzero                         PASS
R2 corrected full-L pair (f2,1) nonzero       PASS
R3 explicit CV E[2] cocycle xi(rho)=Tr        PASS
R4 correct attempt-2 torsor / lattice marking PASS
```

The correct attempt-2 torsor is

```text
d*v^2=n^4-2*a*d*n^2+d^2*q^2,
a=(t^2+1)^2,
d=f2.
```

Its free involution `(n,v)->(-n,-v)` has quotient

```text
X=n^2/d,
Y=-n*v/d,
E'_Tr: Y^2=X*(X^2-2*a*X+q^2).
```

The degree-one base change

```text
u=-(1+sqrt(2))*(t+sqrt(2)-1)/(t-1-sqrt(2))
```

and the Legendre root permutation identify the `E'_Tr` elliptic K3 with `Kc` over `Q(i,sqrt(2))`. The hostile theorem adapter now additionally fixes the previously implicit integral step: Creutz--Viray Lemma 4.6 + Proposition 5.1 identify the corrected CV class with the torsor/Sha image, and Căldăraru Theorem 1.2 with the elliptic-K3 Ogg--Shafarevich dictionary gives

```text
T(X_J2) ~= ker(J2:T(Kc)->Q/Z)
```

as an **integral** Hodge isometry with inherited pairing. The separate degree-two quotient pullback gives

```text
T(Kc)(2)=<8> direct_sum <16>, det=128.
```

The nonzero order-two kernel has the same determinant, hence pullback index one. Therefore

```text
T(X_J2)=<8> direct_sum <16>,
minimum norm=8,
marked J2=[1,0].
```

Certificates:

```text
../33-05/j2-r4-translation-quotient-lattice.json
../33-05/j2-r4-hostile-torsor-brauer-kernel-verification.json
```

Attempt 1 remains revoked as the named torsor; `E'_Tr` is only the quotient target of the correct attempt-2 torsor.

## R5 hostile replay and credit reconciliation

R5 independently replayed R1--R4 and **PASSed the geometric repair**. Certificate/verifier:

```text
../33-05/j2-r5-hostile-replay.json
../33-05/certify_j2_r5_hostile_replay.py
```

However, R5 also found that the historical Stage33-05 audit credit

```text
j2_q_descent_certified=true
```

cannot be inherited. That historical claim used the old Q-defined `ell_Q`/CSA whose geometric class is now exactly known to be zero. The corrected nonzero geometric representative `(f2,1)` has not yet been supplied with a replacement Q-defined arithmetic Brauer representative or equivalent descent datum.

Therefore the Stage33-05 closure contract condition

```text
ALL_SURVIVING_K3_CLASSES_HAVE_EXPLICIT_ARITHMETIC_REPRESENTATIVES=true
```

is still unsatisfied for corrected `J2`.

## Current exact blocker

```text
POST_R5_CORRECTED_J2_Q_DEFINED_DESCENT_OR_EXPLICIT_ARITHMETIC_REPRESENTATIVE
```

Required before Stage33-05 reclosure:

```text
1. source-lock the full Galois action on corrected J2;
2. construct an explicit Q-defined Azumaya/CSA or equivalent descent cocycle;
3. prove its geometric restriction is corrected nonzero (f2,1), not revoked ell_Q;
4. verify the required arithmetic unramifiedness/residue conditions;
5. hostile replay the Stage33-05 explicit-arithmetic-representative closure criterion.
```

## Firewalls

```text
R4 minimum norm 8 / marked J2=[1,0] = RETAINED GEOMETRIC CREDIT
corrected J2 Q-defined descent = NOT RESTORED
Stage33-05 reclosed = false
Stage33-12 exact closure = false
Stage33-13 released = false
Stage33 progress = 5/11
class3 promoted = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```

Do not reuse the attempt-1 quartic as the named torsor. Do not reuse the old geometrically-trivial `ell_Q` as the corrected J2 arithmetic representative.
