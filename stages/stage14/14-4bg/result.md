# Stage14-4bg — select the direct post-local global-small-point witness route

## Result

Stage14-4bf moved the main track away from further local-sieve micro-optimization.  The current merged main-track theorem is

```text
N_local(M) <<_epsilon M^(2-1/41+epsilon),
V(B)       <<_epsilon B^(81/82+epsilon),
```

with unweighted cumulative local retainer

```text
rho_loc(B) << B^(-1/82+epsilon),
E_loc(B)=0.
```

The purpose of 14-4bg is to choose the next post-local theorem target.  Two logically valid routes are available:

1. separate the post-local thinning into a global-solubility/Sha retainer and then a first-small-point/height retainer;
2. count, in one step, locally admissible descent classes that actually possess a rational point in the Stage14-s3 logarithmic height window.

The second route is selected as the primary main-track route.

```text
POST_LOCAL_ROUTE_SELECTED=DIRECT_GLOBAL_SMALL_POINT_WITNESS_COUNT
```

This selection does not assert a new positive post-local exponent.  It proves the exact one-sided reduction and an explicit bounded integral witness equation that the next analytic stage can count.

---

## 1. Why the separated Sha-plus-height route is not the first quantitative target

Stage14-4aq gave the exact sequence

\[
0\to E_F(\mathbf Q)/2E_F(\mathbf Q)
\to \operatorname{Sel}_2(E_F)
\to \Sha(E_F)[2]\to0
\]

and the exact global retainer identity

\[
R=\Sigma-T_{\Sha}.
\]

But the complete finite `H<=20,000` audit only gives

```text
R/Sigma about 0.73 .. 0.81,
```

with no evidence or theorem forcing a power-law decay of `R/Sigma`.  Thus there is currently no quantitative entry point for a positive `delta_glob`.

Stage14-4ar then defined the correct small-point retainer using

\[
\lambda(F)=\min\{\widehat h(P):P\in E_F(\mathbf Q)\text{ non-torsion}\},
\]

but the complete family count of the height-window event has not been measured, and no regulator/least-generator lower-tail theorem is available.

Consequently the separated route is logically clean but presently asks for two difficult family theorems before it can improve the main exponent:

```text
locally soluble -> globally soluble,
globally soluble -> logarithmically small rational point.
```

For a square-root main term, the merged 4bf local exponent would require

\[
\delta_{\rm glob}+\delta_{\rm ht}\ge
\frac12-\frac1{82}
=\frac{20}{41}.
\]

No positive part of this `20/41` is currently proved by 4aq or 4ar.

---

## 2. Direct post-local object

For a primitive oriented first-face base

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

write

\[
E_F:\quad W^2=Z(Z-S^2)(Z+X^2).
\]

Fix an admissible Stage14-s3 comparison constant `C`.  Define `J_C(B)` to be the number of pairs

```text
(F, xi)
```

such that

1. `H(F)<=B`;
2. `xi` is a nonzero Kummer/descent class in the actual supported Stage14 local system;
3. `xi` is globally soluble, i.e. contains a rational point `Q` on `E_F`;
4. some representative `Q` of `xi` satisfies

\[
\widehat h(Q)\le C(\log B+\log H(F)).
\]

Every globally soluble class is locally soluble, so

\[
J_C(B)\le N_{\rm loc}(B).
\]

The key lower inclusion is also exact.

```text
physical hit below B
=> non-torsion rational point P in the s3 height window
=> a nonzero mod-2 Kummer class with a representative no higher than P
=> one pair counted by J_C(B).
```

Hence

\[
\boxed{V(B)\le J_C(B)\le N_{\rm loc}(B).}
\]

No local-to-global converse and no independence assumption occur in this chain.

---

## 3. The mod-2 class can be chosen nonzero without increasing height

The physical point supplied by s3 is non-torsion.  If its class in

\[
E_F(\mathbf Q)/2E_F(\mathbf Q)
\]

is zero, write `P=2P_1`.  If `P_1` is still divisible by two, continue.

This process terminates because `E_F(Q)` is finitely generated; a non-torsion element cannot be infinitely 2-divisible.  Let `Q` be the final point.  Then

```text
Q notin 2 E_F(Q),
```

so its mod-2 Kummer class is nonzero, while canonical height gives

\[
\widehat h(Q)=4^{-k}\widehat h(P)\le\widehat h(P).
\]

Therefore the direct object `J_C` is genuinely covered by the nontrivial local 2-descent system already averaged in the s-track.

---

## 4. Canonical height gives a polynomial rational-coordinate box

For `H<=B`, the integral Weierstrass coefficients of

\[
W^2=Z(Z-S^2)(Z+X^2)
\]

have polynomial size in `B`.  The standard Weil-height/canonical-height comparison used already in s3 therefore implies that for every point counted by `J_C(B)`,

\[
h_Z(Q)\le K_C\log B
\]

for a fixed constant `K_C` depending only on the chosen s3 comparison constant and the fixed family model.

Write the rational coordinates primitively as

\[
Z=\frac{A}{D^2},\qquad
W=\frac{Y}{D^3},\qquad
\gcd(A,D)=1,
\]

with `D>0`.  The square/cube denominator shape follows directly from the monic integral Weierstrass equation.  The height bound gives

\[
\boxed{|A|\le B^{K_C},\qquad D^2\le B^{K_C}.}
\]

Thus the post-local small-point problem is a polynomial-size integer incidence problem, not an abstract regulator-distribution problem.

---

## 5. Exact integral witness equation

Substituting

\[
Z=A/D^2,\qquad W=Y/D^3
\]

and clearing denominators gives

\[
\boxed{
Y^2=A(A-S^2D^2)(A+X^2D^2).
}
\]

Define

\[
G_0=A,
\quad
G_1=A-S^2D^2,
\quad
G_2=A+X^2D^2.
\]

Their exact differences are

\[
G_0-G_1=S^2D^2,
\]

\[
G_2-G_0=X^2D^2,
\]

\[
G_2-G_1=H^2D^2.
\]

Because `gcd(A,D)=1`, any odd prime dividing two distinct `G_i` cannot divide `D`.  Hence

```text
gcd(G0,G1) has odd support in S,
gcd(G0,G2) has odd support in X,
gcd(G1,G2) has odd support in H.
```

Therefore every odd prime outside `SXH` divides at most one `G_i`; since `G_0G_1G_2` is a square, its valuation there is even.  The signed squarefree kernels of the three factors are consequently supported on

\[
2SXH,
\]

exactly the moving bad-prime support of the Stage14 2-descent system.

So for a fixed descent state one may write, with signed squarefree `d_i` supported on `2SXH`,

\[
G_i=d_i u_i^2
\]

and obtain the explicit two-independent-equation witness system

\[
\boxed{d_0u_0^2-d_1u_1^2=S^2D^2,}
\]

\[
\boxed{d_2u_2^2-d_0u_0^2=X^2D^2,}
\]

with the third identity

\[
d_2u_2^2-d_1u_1^2=H^2D^2
\]

following from `S^2+X^2=H^2`.

This is the concrete post-local incidence object selected for the next main-track analytic attack.

---

## 6. Multiplicity and why this remains compatible with the local sieve

The local state already fixes the relevant signed squareclass data.  The earlier s2/s5 support envelope is subpolynomial:

```text
number of supported cover/squareclass states per base = B^o(1).
```

Hence returning from `J_C(B)` to the explicit kernel triples `(d_0,d_1,d_2)` costs only `B^epsilon` at the exponent level.

The direct route therefore preserves the local saving rather than replacing it with an unconstrained count of all rational points on all fibers.

It is essential to keep the local-state restriction: counting torsion or arbitrary low-height points on every fiber would introduce an ambient `~B` family and would not be a useful post-local majorant.

---

## 7. Quantitative target selected for 14-4h onward

With the currently merged 4bf theorem,

\[
N_{\rm loc}(B)\ll B^{81/82+\epsilon}.
\]

The first genuine post-local improvement target is therefore

\[
\boxed{
J_C(B)\ll B^{81/82-\delta_{\rm post}+\epsilon}
}
\]

for any fixed `delta_post>0`.

A square-root sufficient target is simply

\[
\boxed{J_C(B)\ll B^{1/2+\epsilon},}
\]

which corresponds to

\[
\delta_{\rm post}\ge\frac{20}{41}
\]

relative to the merged 4bf exponent.

The advantage of this formulation is that one does not need to prove either

```text
positive delta_glob for Sha thinning,
```

or

```text
positive delta_ht conditional on positive rank
```

separately.  Any saving obtained directly from the integral witness equations is immediately a saving for the physical count.

This does not prove that the direct route will reach `1/2`; it identifies the first explicit incidence theorem whose proof would quantitatively move the current bound.

---

## 8. Status of Stage14-s5u

At branch creation, Stage14-s5u PR #338 has dedicated CI success and proposes the stronger local theorem

```text
N_local(M) << M^(2-1/21+epsilon),
physical exponent 41/42,
S5_METHOD_CLOSED=true,
```

but it is not yet merged into `main`.  In accordance with the 4bf handoff contract, 14-4bg does not import an unmerged theorem.

If s5u merges before the next main-track stage, only the exponent ledger changes:

```text
local B exponent: 41/42,
post-local saving needed for sqrt: 10/21.
```

The selected direct witness object and all integral reductions above are unchanged.

---

## 9. Main-track decision

The route comparison is therefore:

```text
SEPARATED ROUTE
local -> rank/global -> small height
needs two new family retainers;
current positive global exponent = none;
complete height-window census = absent.

DIRECT ROUTE
local -> globally soluble low-height class
one conjunction count;
exact physical inclusion already known;
reduces to bounded integral witness equations;
any direct saving improves V(B).
```

Hence the main track selects the direct route.

The separated 4aq/4ar identities remain valid diagnostics and can be revisited if a strong Sha or regulator theorem appears, but they are not the blocking path for the next proof attempt.

---

## Boundary

```text
STAGE14_4BG=POST_LOCAL_DIRECT_GLOBAL_SMALL_POINT_WITNESS_ROUTE_SELECTED
FOUR_BF_LOCAL_EXPONENT_IMPORTED=true
CURRENT_MERGED_LOCAL_B_EXPONENT=81/82
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
DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
SEPARATED_GLOBAL_HEIGHT_ROUTE_REJECTED_AS_PRIMARY=true
S5U_PENDING_NOT_IMPORTED=true
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bh dyadically decompose the bounded witness system by D and the signed kernel triple, eliminate one square variable, and prove a first incidence saving or isolate the exact determinant/square-sieve obstruction; import merged s5u first if available
```
