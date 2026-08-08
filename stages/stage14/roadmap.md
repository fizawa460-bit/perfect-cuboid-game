# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain the primitive canonical exactly-two-face population inside the integer-space-diagonal cuboid family.

Locked ambient population:

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

```text
a-direction = ab+ac only
b-direction = ab+bc only
c-direction = ac+bc only
```

## 14-1 — Definition and counting interface

Status: [x] Complete.

## 14-2 — Complete finite enumeration

Status: [x] Complete.

Two independent exact generation routes agree through `B=2,000,000`.

## 14-3 — Finite directional reconnaissance

Status: [x] Complete.

No finite fit was promoted to an asymptotic theorem.

## Frozen Stage13 upstream contract

Stage13 downstream mathematics is frozen at

```text
c843e039306b40bd3693f89d6199da78c2fb4657
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
```

Stage14 may use the raw directional theorem, fixed-local-factor machinery, exact inert local state, harmonic closure, and pair/triple lower-order theorem. In particular,

\[
\boxed{N_2(B)=o(B(\log B)^3)}.
\]

The inert-prime local multiplier is

\[
\lambda_p=\frac{p+5}{2(p+1)}.
\]

The R03 overlap squeeze uses fixed finite prime sets. It proves zero density but supplies no growing-modulus theorem and no explicit power saving in `B`.

## 14-4 — True total growth order

Status: [>] Active.

### 14-4aa — independent two-face parametrization

Status: [x] Complete.

All three directions are chamber positions of one shared-edge arithmetic object.

### 14-4ab — exact matching bijection

Status: [x] Complete.

For primitive oriented Pythagorean face data `F_i=(S_i,X_i,H_i)`, shared-edge matching is solved exactly. Cuboid primitivity kills exactly the common scale, and the parameter-fiber multiplicity of a fixed raw pair incidence is `1`.

### 14-4ac — rational-slope height envelope

Status: [x] Complete.

With

\[
t_i=X_i/S_i,
\qquad
L=\operatorname{lcm}(S_1,S_2),
\]

we have

\[
(e,x,y)=L(1,t_1,t_2),
\qquad
 d=L\sqrt{1+t_1^2+t_2^2}.
\]

The pre-space denominator envelope has `B(log B)^7` scale. The frozen finite table makes `sqrt(B)` a high-priority candidate, not a theorem.

### 14-4ad — quantitative square thinning / elliptic reduction

Status: [x] Complete.

The R03 fixed-prime squeeze cannot be turned into a `sqrt(B)` bound by silently choosing a prime set depending on `B`. Therefore the exponent must come from additional global arithmetic.

Stage14-4ad identifies that arithmetic exactly. If

\[
g=\gcd(S_1,S_2),
\]

then the integer-space-diagonal condition is equivalent to the product-Pythagorean closure

\[
\boxed{
(X_1X_2)^2+(gd)^2=(H_1H_2)^2.
}
\]

Normalize

\[
\rho_i=X_i/H_i.
\]

Then the extra global square condition is

\[
\boxed{1-(\rho_1\rho_2)^2\in(\mathbf Q^\times)^2.}
\]

Fix `rho=rho1` and parameterize the second unit-circle point by

\[
\rho_2=\frac{2q}{1+q^2}.
\]

The fixed fiber is the Jacobi quartic

\[
W^2=q^4+2Aq^2+1,
\qquad A=1-2\rho^2.
\]

Because

\[
A^2-1=-4\rho^2(1-\rho^2)\ne0,
\]

it is nonsingular genus one. After an explicit birational transformation and scaling by the first-face data, the fiber is

\[
\boxed{
E_{t_1}:Y^2=X(X-1)(X+t_1^2),
\qquad t_1=X_1/S_1.
}
\]

Its `j`-invariant

\[
 j(t_1)=256\frac{(1+t_1^2+t_1^4)^3}
 {t_1^4(1+t_1^2)^2}
\]

is nonconstant. Thus the Stage14 square-thinning locus is a **non-isotrivial elliptic fibration**.

Deterministic validation checks all 25 raw-pair incidences at `B=10000`; every product identity, quartic, cubic and elliptic model passes, with exactly-two `(9,11,5)` and `T=0`.

Finite exponent diagnostics remain compatible with `1/2`, but no power law is proved.

Decision:

```text
STAGE14_4AD=COMPLETE
PRODUCT_PYTHAGOREAN_CLOSURE_IDENTITY=true
SECOND_FACE_FIXED_FIBER_GENUS=1
JACOBI_QUARTIC_MODEL_LOCKED=true
ELLIPTIC_FIBER_MODEL=Y^2=X(X-1)(X+t1^2)
ELLIPTIC_FIBRATION_NON_ISOTRIVIAL=true
R03_FIXED_PRIME_SIEVE_GIVES_ZERO_DENSITY=true
R03_FIXED_PRIME_SIEVE_GIVES_POWER_SAVING=false
SQRT_B_FINITE_CANDIDATE_SURVIVES=true
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
```

Artifacts:

```text
stages/stage14/archive/stage14-4ad-elliptic-thinning.md
stages/stage14/scripts/14-4/elliptic_fiber_audit.py
stages/stage14/data/14-4/elliptic_fiber_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

### 14-4ae — elliptic-fibration height/rank analysis

Status: [>] Next.

Purpose:

- express the original cutoff `d<=B` as a height condition on the base `t1` and points on `E_t1`;
- compare the induced height with standard naive/canonical heights on the fibers;
- stratify the base by the first primitive face denominator and lcm coupling;
- determine what uniform or averaged rank/rational-point estimates are actually sufficient to sum the fibers;
- retain the R03 inert-prime conditions as auxiliary local restrictions, without treating them as independent probabilities;
- prove or reject a `B^(1/2)`-type scale only after the elliptic height sum is controlled.

## 14-5 — Directionwise asymptotic structure

Status: pending Stage14-4.

## Scope boundary

No true growth exponent, leading constant, limiting directional ratio, eventual leader, Euler-side equality, or perfect-cuboid nonexistence theorem is currently established for Stage14.

```text
NEXT=Stage14-4ae elliptic-fibration height/rank analysis
```
