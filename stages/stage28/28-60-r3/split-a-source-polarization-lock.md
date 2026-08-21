# Stage28-60-r3 split A — Stage19 source polarization lock

```text
SPLIT_ID=Stage28-60-r3A
ROLE=SOURCE_ONLY_REUSE_LOCK
STATUS=COMPLETE
NEW_THEOREM=false
```

This split isolates the Stage19 side so the target-family degree calculation cannot silently change the physical height or divisor normalization.

## Audited source contract

Stage14-4ah / PR #164 fixes the common toric base

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),\qquad
L=-K_Y=2H_1+2H_2-\sum E_j,\qquad L^2=4.
\]

For the Stage19 space-square double cover

\[
\pi_{sp}:X_{sp}\to Y
\]

the physical quasi-polarization is

\[
\boxed{M_{sp}=\pi_{sp}^*L=\Phi_{sp}^*\mathcal O_{\mathbf P^2}(1)},
\qquad
\boxed{M_{sp}^2=8}.
\]

On a primitive physical point with edge coordinates `[e:x:y]`, its associated height is exactly

\[
H_{M_{sp}}=\sqrt{e^2+x^2+y^2}=d.
\]

Hence `M_sp`-degree is the correct fixed-curve degree for the actual Stage19 physical cutoff, not an auxiliary projective degree.

## Low-degree source spectrum already available to r3

The audited Stage14-4ak chain / PR #199 proves the complete physical `M_sp.C=4` rational-bisection stratum empty:

```text
STAGE19_PHYSICAL_M4_FIXED_CURVE=ABSENT_AUDITED
```

The current r3 exact anti-invariant-lattice computation supplies the separate candidate obstruction that every physical odd `M_sp`-degree is impossible. Subject to fresh mathematical audit this removes degree five as well:

```text
STAGE19_PHYSICAL_ODD_FIXED_CURVE_DEGREES=ABSENT_CANDIDATE
STAGE19_PHYSICAL_M5_FIXED_CURVE=ABSENT_CANDIDATE
STAGE19_FIXED_CURVE_DEGREE_FLOOR_CANDIDATE=6
```

No Stage20 statement is used in this split.

## Lock

```text
SOURCE_PHYSICAL_POLARIZATION_LOCKED=true
SOURCE_PHYSICAL_LINE_BUNDLE=M_sp=pi_sp^*(-K_Y)
SOURCE_PHYSICAL_HEIGHT_EXACT=true
SOURCE_M_SQUARED=8
SOURCE_M4_VOID_REUSED_AUDITED=true
SOURCE_ODD_DEGREE_VOID_REUSED_R3_CANDIDATE=true
TARGET_DEGREE_CLAIM_MADE=false
```
