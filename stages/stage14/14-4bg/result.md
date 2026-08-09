# Stage14-4bg — direct post-local global-small-point witness route

## Result

Merged Stage14-s5u closes the s5 local-2-descent / reciprocity-sieve method with

```text
N_local(M) <<_epsilon M^(2-1/21+epsilon),
N_local(B) <<_epsilon B^(41/42+epsilon),
V(B)       <<_epsilon B^(41/42+epsilon).
```

Thus the current unweighted local retainer has B-scale saving `1/42`, and the remaining saving needed to reach `B^(1/2+epsilon)` is

\[
\frac{41}{42}-\frac12=\boxed{\frac{10}{21}}.
\]

This stage compares the two post-local interfaces already isolated by 4aq/4ar and selects the next main-track counting object.

```text
POST_LOCAL_ROUTE_SELECTED=DIRECT_GLOBAL_SMALL_POINT_WITNESS_COUNT
```

No positive post-local exponent is proved here. The new result is an exact one-sided reduction to a bounded integral witness incidence.

---

## 1. Separated versus direct route

The separated route is

```text
local class
 -> globally soluble / positive-rank class
 -> rational point in the s3 logarithmic height window.
```

Stage14-4aq makes the first arrow exact through

\[
R=\Sigma-T_{\Sha},
\]

but its finite `H<=20,000` data only place `R/Sigma` around `0.73..0.81`; no positive power-law global saving is proved.

Stage14-4ar formulates the correct least-nontorsion-height retainer, but the complete height-window family census and a uniform least-generator/regulator lower-tail theorem are both absent.

So the separated route presently requires two new family distribution theorems, with

\[
\delta_{glob}+\delta_{ht}\ge 10/21
\]

needed for the square-root scale after s5u.

The direct route instead counts the conjunction “globally soluble and logarithmically small” in one object. It avoids any need to prove a Sha density theorem separately.

---

## 2. Direct class count

For a primitive oriented Pythagorean first-face base

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

use

\[
E_F:\quad W^2=Z(Z-S^2)(Z+X^2).
\]

Fix an admissible Stage14-s3 height constant `C`. Let `J_C(B)` count pairs `(F,xi)` such that

1. `H(F)<=B`;
2. `xi` is a nonzero supported Kummer/2-descent class;
3. `xi` is globally soluble;
4. some representative `Q` satisfies

\[
\widehat h(Q)\le C(\log B+\log H(F)).
\]

Global solubility implies local solubility, so

\[
J_C(B)\le N_{loc}(B).
\]

Every physical hit below `B` supplies a non-torsion point in the s3 height window. Therefore, after choosing one witnessing nonzero class per active base,

\[
\boxed{V(B)\le J_C(B)\le N_{loc}(B).}
\]

---

## 3. Nonzero mod-2 representative without height increase

If a physical non-torsion point `P` lies in `2E_F(Q)`, halve it and continue while possible. Since `E_F(Q)` is finitely generated, a non-torsion point is not infinitely 2-divisible. The final point `Q` satisfies

```text
Q notin 2E_F(Q),
```

and hence defines a nonzero mod-2 Kummer class.

Canonical height obeys

\[
\widehat h(2R)=4\widehat h(R),
\]

so repeated halving never increases the height. Thus the physical injection stays inside the nontrivial local system counted by s5u.

---

## 4. Polynomial rational-coordinate box

For `H<=B`, the coefficients of the integral Weierstrass model have polynomial height in `B`. The s3 Weil-height/canonical-height comparison therefore gives

\[
h_Z(Q)\le K_C\log B
\]

for a fixed constant `K_C`.

Write primitive rational coordinates

\[
Z=A/D^2,\qquad W=Y/D^3,\qquad D>0,\quad \gcd(A,D)=1.
\]

Then

\[
\boxed{|A|\le B^{K_C},\qquad D^2\le B^{K_C}.}
\]

So the direct post-local count is a polynomial-size integer incidence problem.

---

## 5. Exact integral witness equation

Clearing denominators yields

\[
\boxed{Y^2=A(A-S^2D^2)(A+X^2D^2).}
\]

Set

\[
G_0=A,\quad G_1=A-S^2D^2,\quad G_2=A+X^2D^2.
\]

Then

\[
G_0-G_1=S^2D^2,
\]

\[
G_2-G_0=X^2D^2,
\]

\[
G_2-G_1=H^2D^2.
\]

Because `gcd(A,D)=1`, any odd prime dividing two `G_i` cannot divide `D`. Hence

```text
odd gcd support(G0,G1) subset S,
odd gcd support(G0,G2) subset X,
odd gcd support(G1,G2) subset H.
```

Every odd prime outside `SXH` divides at most one factor. Since `G0 G1 G2=Y^2`, its valuation there is even. Therefore the signed squarefree kernels of the three factors are supported on

\[
\boxed{2SXH.}
\]

This is exactly the bad-prime support already controlled by the closed Stage14 local 2-descent system.

---

## 6. Fixed-state two-quadrics incidence

For a fixed descent state write

\[
G_i=d_i u_i^2
\]

with signed squarefree `d_i` supported on `2SXH`. Then

\[
\boxed{d_0u_0^2-d_1u_1^2=S^2D^2,}
\]

\[
\boxed{d_2u_2^2-d_0u_0^2=X^2D^2.}
\]

The third difference equals `H^2D^2` automatically from `S^2+X^2=H^2`.

Thus `J_C(B)` reduces, up to the existing `B^o(1)` state multiplicity, to an averaged bounded incidence count for an explicit intersection-of-two-quadrics system.

---

## 7. Quantitative contract

Merged s5u gives

\[
J_C(B)\le N_{loc}(B)\ll B^{41/42+\epsilon}.
\]

Any first post-local improvement has the form

\[
\boxed{J_C(B)\ll B^{41/42-\delta_{post}+\epsilon}}
\]

for some fixed `delta_post>0`.

A square-root sufficient target is

\[
\boxed{J_C(B)\ll B^{1/2+\epsilon},}
\]

requiring

\[
\boxed{\delta_{post}\ge10/21.}
\]

On `B~M^2`, the current local count is `M^(41/21+epsilon)` and the square-root target is `M^(1+epsilon)`, so the eventual post-local saving required is `M^(-20/21)`.

No such saving is claimed in this stage.

---

## Decision

The separated 4aq/4ar identities remain valid secondary interfaces, but the direct witness count is now the primary main-track target because it

- preserves the closed local-state restrictions;
- counts global solubility and small height jointly;
- has an exact physical inclusion;
- becomes an explicit bounded integer system;
- converts any incidence saving immediately into a physical upper-bound improvement.

```text
STAGE14_4BG=POST_LOCAL_DIRECT_GLOBAL_SMALL_POINT_WITNESS_ROUTE_SELECTED
S5U_LOCAL_METHOD_CLOSURE_IMPORTED=true
CURRENT_LOCAL_M_SCALE_SAVING_EXPONENT=1/21
CURRENT_LOCAL_B_SCALE_SAVING_EXPONENT=1/42
CURRENT_LOCAL_CLASS_B_EXPONENT=41/42
CURRENT_SQRT_REMAINING_POST_LOCAL_DELTA=10/21
DIRECT_POST_LOCAL_CLASS_COUNT_DEFINED=true
PHYSICAL_BASE_INJECTS_TO_DIRECT_POST_LOCAL_CLASS=true
DIRECT_POST_LOCAL_CLASS_IS_LOCALLY_SOLUBLE=true
NONZERO_KUMMER_REPRESENTATIVE_WITH_NO_HEIGHT_INCREASE_PROVED=true
LOW_CANONICAL_HEIGHT_TO_POLYNOMIAL_RATIONAL_COORDINATE_BOX=true
INTEGRAL_WITNESS_EQUATION_EXACT=true
WITNESS_EQUATION=Y^2=A(A-S^2D^2)(A+X^2D^2)
WITNESS_FACTOR_PAIRWISE_ODD_GCD_SUPPORT_IN_S_X_H=true
WITNESS_SQUAREFREE_KERNEL_SUPPORTED_ON_2SXH=true
FIXED_STATE_TWO_QUADRIC_DIFFERENCE_SYSTEM_EXACT=true
SEPARATED_GLOBAL_HEIGHT_ROUTE_REJECTED_AS_PRIMARY=true
DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
S5_METHOD_CLOSED=true
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bh dyadically decompose the bounded witness system by D and the signed kernel triple, eliminate one square variable, and prove a first incidence saving or isolate the exact determinant/square-sieve obstruction
```
