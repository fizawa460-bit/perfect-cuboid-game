# Stage14-4bg — exact integral model for the selected post-local witness count

## Result

Merged Stage14-s6-00 has already selected the direct post-local global-small-point incidence as the primary Stage14-s6 architecture. Stage14-4bg therefore does **not** repeat that route-selection claim. Its job is to instantiate the selected route on the main `14-4` line as an exact bounded integer incidence problem.

Merged Stage14-s5u supplies

```text
N_local(B) <<_epsilon B^(41/42+epsilon),
```

and s6-00 locks the remaining square-root saving budget

```text
41/42 - 1/2 = 10/21.
```

Stage14-4bg defines the direct class count `J_C(B)`, proves

\[
\boxed{V(B)\le J_C(B)\le N_{\rm loc}(B)},
\]

and derives the exact primitive integral witness equation

\[
\boxed{Y^2=A(A-S^2D^2)(A+X^2D^2)}.
\]

For a fixed supported descent state this becomes the two-quadrics system

\[
\boxed{d_0u_0^2-d_1u_1^2=S^2D^2,}
\]

\[
\boxed{d_2u_2^2-d_0u_0^2=X^2D^2.}
\]

This is the concrete object handed to Stage14-4bh / the parallel s6 incidence analysis.

No positive post-local saving is claimed in 4bg.

---

## 1. Imported post-local architecture

Stage14-s6-00 freezes

```text
DIRECT_POST_LOCAL_GLOBAL_SMALL_POINT_INCIDENCE_PRIMARY=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21.
```

Thus the local sieve is no longer the main bottleneck. The next task is to count the locally supported classes that actually possess a bounded-height rational point.

Stage14-4bg adopts this architecture exactly. The separated Sha/global-solubility and least-height retainers from 4aq/4ar remain valid secondary interfaces, but they are not reopened here.

---

## 2. Direct class count `J_C(B)`

For a primitive oriented Pythagorean first-face base

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

use the integral elliptic model

\[
E_F:\quad W^2=Z(Z-S^2)(Z+X^2).
\]

Fix any admissible Stage14-s3 comparison constant `C`. Let `J_C(B)` count pairs `(F,xi)` such that

1. `H(F)<=B`;
2. `xi` is a nonzero supported mod-2 Kummer/descent class from the actual Stage14 local system;
3. `xi` is globally soluble;
4. some rational representative `Q` of `xi` satisfies

\[
\widehat h(Q)\le C(\log B+\log H(F)).
\]

Every such class is locally soluble, hence

\[
J_C(B)\le N_{\rm loc}(B).
\]

Conversely Stage14-s3 proves that every physical hit below `B` gives a non-torsion rational point in the same logarithmic canonical-height window. Section 3 shows that this point can be replaced by a nonzero mod-2 representative without increasing height. Choosing one witnessing class per physical base therefore gives

\[
\boxed{V(B)\le J_C(B)\le N_{\rm loc}(B).}
\]

The current unconditional bound is consequently

\[
J_C(B)\ll_\epsilon B^{41/42+\epsilon}.
\]

---

## 3. Nonzero Kummer representative with no height loss

Let `P` be a physical non-torsion point. If `P` is divisible by two in `E_F(Q)`, write

```text
P=2P_1
```

and continue while possible. Since `E_F(Q)` is finitely generated, a non-torsion point cannot be infinitely 2-divisible. The process terminates at `Q` satisfying

```text
Q notin 2E_F(Q).
```

Thus `Q` determines a nonzero class in `E_F(Q)/2E_F(Q)`. Since

\[
\widehat h(2R)=4\widehat h(R),
\]

repeated halving gives

\[
\widehat h(Q)\le\widehat h(P).
\]

Hence the physical injection genuinely lands in the nonzero supported local system already bounded by s5u.

---

## 4. Low canonical height gives a polynomial coordinate box

For `H<=B`, the coefficients of

\[
W^2=Z(Z-S^2)(Z+X^2)
\]

have polynomial height in `B`. The same Weil-height versus canonical-height comparison used in Stage14-s3 therefore gives

\[
h_Z(Q)\le K_C\log B
\]

for a fixed constant `K_C`.

Write the rational point primitively as

\[
Z=A/D^2,\qquad W=Y/D^3,
\qquad D>0,\quad \gcd(A,D)=1.
\]

Then

\[
\boxed{|A|\le B^{K_C},\qquad D^2\le B^{K_C}.}
\]

Thus the post-local problem lives in a polynomial-size integer box; it is no longer merely an abstract least-regulator statement.

---

## 5. Exact denominator-cleared witness equation

Substitute the primitive rational coordinates into the elliptic equation and clear `D^6`:

\[
\boxed{
Y^2=A(A-S^2D^2)(A+X^2D^2).
}
\]

Put

\[
G_0=A,
\qquad G_1=A-S^2D^2,
\qquad G_2=A+X^2D^2.
\]

Then exactly

\[
G_0-G_1=S^2D^2,
\]

\[
G_2-G_0=X^2D^2,
\]

\[
G_2-G_1=H^2D^2.
\]

The third equality uses `S^2+X^2=H^2`.

---

## 6. Pairwise gcd support and squarefree kernels

Because `gcd(A,D)=1`, any odd prime dividing two distinct factors `G_i` cannot divide `D`.

If an odd prime `p` divides `G_0` and `G_1`, then it divides their difference `S^2D^2`; as `p` cannot divide `D`, one has `p|S`. Likewise

```text
p | gcd(G0,G2) => p | X,
p | gcd(G1,G2) => p | H.
```

Therefore

```text
odd support gcd(G0,G1) subset odd support(S),
odd support gcd(G0,G2) subset odd support(X),
odd support gcd(G1,G2) subset odd support(H).
```

Every odd prime outside `SXH` divides at most one of the three factors. Since

\[
G_0G_1G_2=Y^2,
\]

its valuation in that unique factor must be even. Consequently all signed squarefree kernels are supported on

\[
\boxed{2SXH}.
\]

This is exactly the moving bad-prime support already owned by the closed Stage14 2-descent system.

---

## 7. Fixed-state two-quadrics system

For a fixed supported descent state, write

\[
G_i=d_i u_i^2,
\]

where each `d_i` is signed squarefree and supported on `2SXH` with the compatibility constraints inherited from that state.

The three factor differences give

\[
d_0u_0^2-d_1u_1^2=S^2D^2,
\]

\[
d_2u_2^2-d_0u_0^2=X^2D^2,
\]

\[
d_2u_2^2-d_1u_1^2=H^2D^2.
\]

Only the first two are independent. Hence the selected global-small-point problem is an averaged bounded incidence count for an explicit intersection of two quadrics, with the local squareclass data already frozen.

The supported state multiplicity is `B^o(1)`, so dyadic/state decomposition costs only `B^epsilon` at exponent scale.

---

## 8. Quantitative contract

The current imported local theorem gives

\[
J_C(B)\ll B^{41/42+\epsilon}.
\]

Any estimate

\[
\boxed{
J_C(B)\ll B^{41/42-\delta_{post}+\epsilon}
}
\]

with fixed `delta_post>0` is genuine progress beyond s5.

The square-root upper-bound scale requires

\[
\boxed{\delta_{post}\ge10/21.}
\]

Equivalently on `B~M^2`, the current exponent is `M^(41/21+epsilon)` and the square-root target is `M^(1+epsilon)`, requiring eventual post-local saving `M^(-20/21)`.

4bg proves no such saving. It freezes the exact incidence object to which the next counting method must be applied.

---

## Boundary

```text
STAGE14_4BG=S6_PRIMARY_ROUTE_IMPORTED_AND_EXACT_INTEGRAL_WITNESS_MODEL_FROZEN
S6_00_PRIMARY_ROUTE_IMPORTED=true
S5U_LOCAL_METHOD_CLOSURE_IMPORTED=true
CURRENT_LOCAL_CLASS_B_EXPONENT=41/42
CURRENT_SQRT_REMAINING_POST_LOCAL_DELTA=10/21
DIRECT_POST_LOCAL_CLASS_COUNT_DEFINED=true
PHYSICAL_BASE_INJECTS_TO_DIRECT_POST_LOCAL_CLASS=true
NONZERO_KUMMER_REPRESENTATIVE_WITH_NO_HEIGHT_INCREASE_PROVED=true
LOW_CANONICAL_HEIGHT_TO_POLYNOMIAL_RATIONAL_COORDINATE_BOX=true
INTEGRAL_WITNESS_EQUATION_EXACT=true
WITNESS_EQUATION=Y^2=A(A-S^2D^2)(A+X^2D^2)
WITNESS_FACTOR_PAIRWISE_ODD_GCD_SUPPORT_IN_S_X_H=true
WITNESS_SQUAREFREE_KERNEL_SUPPORTED_ON_2SXH=true
FIXED_STATE_TWO_QUADRIC_DIFFERENCE_SYSTEM_EXACT=true
DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
S5_METHOD_CLOSED=true
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bh dyadically decompose D and the signed kernel triple, eliminate one square variable, and prove a first direct incidence saving or isolate the exact determinant/square-sieve obstruction
```
