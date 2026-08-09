# Stage14-4ak — Shimada lattice enumeration closes the M-degree-4 fixed-curve mechanism

## Purpose

Stage14-4ai reduced every fixed rational curve capable of a physical `sqrt(B)` contribution to one remaining case: a split singular anticanonical member `D in |L|` whose lift is

\[
\pi^{-1}(D)=C+\delta(C),\qquad M\cdot C=4.
\]

Stage14-4aj identified the exact interface with Shimada's published level-4 modular K3 computation package. Stage14-4ak executes that interface against the official `GramS0`, distinguished curves, fiber data, torsion translations, inversion, and automorphism matrices.

The result is decisive for the fixed-curve question:

\[
\boxed{\text{there is no integral Neron--Severi root class satisfying the Stage14 split condition}.}
\]

Hence there is no physical `Q`-rational `M`-degree-four bisection. The complete fixed-curve `sqrt(B)` mechanism is rejected. This does **not** prove a different global growth order; the finite `sqrt(B)` signal must now come from a collective rank-jump/small-point mechanism if it persists asymptotically.

## 1. Published lattice data actually consumed

The workflow downloads Shimada's official level-4 computation archive and parses literal Maple assignments only. The active objects are

```text
GramS0
L40vs
SixFs
fsigma
AutX0h0
AutX0f
MWtorsigmaz
Tsigma
iotasigmaz
```

with the published row-vector/right-action convention.

The `AutX0h0` orbit of `fsigma` has size five. Applying the intrinsic Stage14 fiber/corner fingerprint gives four initial candidates for the second symmetric fiber class `f_s`. Requiring the geometric coordinate swap `r <-> s` to exchange the two fibrations and the corresponding boundary systems leaves two labelings.

Those two labelings are not distinct physical geometries: `AutX0f` contains 64 matrices mapping one complete labeling to the other, including `f_s`, `M`, the corner set, and the deck involution. Thus one representative suffices for the lattice enumeration.

A representative is

```text
f_s = [0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
M   = [1,-1,1,-1,0,0,0,2,0,2,2,2,0,2,2,0,0,0,0,0]
deck 2-torsion label = [0,2]
```

The alternative surviving labeling is `AutX0f`-equivalent.

## 2. Exact split-root reduction

For a hypothetical split component `C`, Stage14-4aj gives

\[
M=C+\delta(C),\qquad C^2=-2,\qquad M\cdot C=4.
\]

Put

\[
\boxed{x=2C-M}.
\]

Because `delta(M)=M` and `delta(C)=M-C`, one gets

\[
\boxed{\delta(x)=-x}.
\]

Moreover

\[
x^2=(2C-M)^2=4(-2)-4(4)+8=-16,
\]

and integrality of `C=(M+x)/2` is exactly

\[
\boxed{x\equiv M\pmod 2}.
\]

Therefore the entire remaining Stage14-4ai problem is equivalent to finding a vector in the saturated anti-invariant lattice satisfying

```text
delta(x) = -x
x^2 = -16
x = M mod 2.
```

No effectivity or Galois filter is needed if this integral lattice coset is already empty.

## 3. Anti-invariant lattice

Let `K` be a saturated integer basis of

\[
\ker(\delta+1)\cap NS(X).
\]

The computation gives

```text
rank K = 6
det(-K^T GramS0 K) = 256.
```

For the positive definite form

\[
Q=-K^T\operatorname{GramS0}K,
\]

the exact vector counts through norm 16 are

```text
norm 0   :    1
norm 4   :   60
norm 8   :  252
norm 12  :  544
norm 16  : 1020
```

Thus the lattice certainly has many norm-16 vectors; the decisive condition is the Stage14 parity coset, not norm alone.

## 4. Complete parity-coset enumeration

Two independent exact enumeration routes were run.

### PARI/GP route

`matkerint` constructs the saturated anti-invariant integer kernel. `qfminim` performs the finite positive-definite enumeration through norm 16.

It returns

```text
nonzero vectors with norm <=16 = 1876
norm-16 +/- representatives    = 510
parity-compatible split pairs  = 0
```

### Independent exact LDL route

A separate Python implementation performs rational LDL decomposition and recursive exact enumeration without using `qfminim` for the vector search. It returns

```text
norm-16 vectors                = 1020
parity-compatible norm-16      = 0
parity-compatible split pairs  = 0
```

The two routes agree exactly after accounting for the `+/-` convention.

The independent verifier was useful: an earlier diagnostic mistakenly extracted the PARI norm and temporarily reported no norm-16 vectors. The independent LDL census exposed that implementation error immediately. The corrected calculation has 1020 norm-16 vectors but **zero vectors in the required Stage14 parity coset**. Only this corrected cross-checked result is promoted.

## 5. Consequence for Stage14-4ai

Every hypothetical split singular-anticanonical `M`-degree-four component would produce an integral anti-invariant vector `x=2C-M` of norm `-16` in the required parity coset. None exists.

Therefore

\[
\boxed{\text{no split singular anticanonical }M\text{-degree-four bisection exists}.}
\]

Combined with Stage14-4ai, which already eliminated the connected degree-two image mechanism and every genus-zero splitting mechanism, this closes **all** fixed rational curves with the extremal degree pattern

\[
M\cdot C=4,\qquad \deg(C\to\mathbf P^1_r)=2.
\]

Hence

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=true
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

This is stronger than a `Q`-descent obstruction: the necessary integral geometric NS class is absent already before `Galmu`, effectivity, or physical-open filtering.

## 6. What this does not prove

The finite active-vertex data remain numerically close to a `sqrt(B)` scale, but Stage14-4ak shows that this signal cannot be explained by a finite collection of fixed `M`-degree-four accumulating rational curves.

It does not prove

```text
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
```

The main track must return to the genuinely moving specialization problem: frequency of positive-rank fibers together with the first-small-point height gate isolated by Stage14-s.

## 7. Reproducibility

Primary scripts:

```text
stages/stage14/scripts/14-4/shimada_stage14_identify.py
stages/stage14/scripts/14-4/shimada_stage14_refine.py
stages/stage14/scripts/14-4/shimada_stage14_equiv.py
stages/stage14/scripts/14-4/shimada_stage14_roots.py
stages/stage14/scripts/14-4/shimada_stage14_verify.py
```

Frozen compact result:

```text
stages/stage14/data/14-4/shimada_stage14_4ak_result.json
```

CI:

```text
.github/workflows/stage14-4ak-shimada-probe.yml
```

## 8. Locked decision

```text
STAGE14_4AJ=COMPLETE_SHIMADA_LATTICE_INTERFACE
STAGE14_4AK=COMPLETE_SPLIT_ROOT_COSET_VOID
SHIMADA_PHYSICAL_LABELINGS_UP_TO_AUTX0F=1
ANTI_INVARIANT_LATTICE_RANK=6
ANTI_INVARIANT_POSITIVE_FORM_DETERMINANT=256
NORM16_VECTOR_COUNT=1020
PARITY_COMPATIBLE_NORM16_VECTOR_COUNT=0
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=true
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-4al collective rank-jump / first-small-point mechanism
```
