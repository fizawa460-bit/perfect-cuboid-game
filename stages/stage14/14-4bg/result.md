# Stage14-4bg — select the direct post-local global-small-point witness route

## Result

Merged Stage14-s5u has now closed the s5 local-2-descent / reciprocity-sieve method with

```text
N_local(M) <<_epsilon M^(2-1/21+epsilon),
```

and therefore on the physical cutoff scale

```text
N_local(B) <<_epsilon B^(41/42+epsilon),
V(B)       <<_epsilon B^(41/42+epsilon).
```

Equivalently, the unweighted local retainer is

```text
rho_loc(B) <<_epsilon B^(-1/42+epsilon),
E_loc(B)=0.
```

Stage14-4bg chooses the next post-local theorem target. Two routes are logically available:

```text
separated:
  local -> global/rank/Sha -> first small point;

direct:
  local -> globally soluble class carrying a logarithmically small rational point.
```

The direct route is selected.

```text
POST_LOCAL_ROUTE_SELECTED=DIRECT_GLOBAL_SMALL_POINT_WITNESS_COUNT
```

The stage proves the exact one-sided reduction from physical hits to this direct count and reduces every such low-height witness to a bounded integral equation. It does not yet prove a positive post-local saving.

---

## 1. Updated local input from merged s5u

Stage14-s5u improves the complete actual local-system exponent from the s5t value `1/41` to

```text
Euclid-scale saving = 1/21.
```

Since `M<=B^(1/2)`, this becomes

```text
physical B-scale saving = 1/42,
local-class exponent     = 41/42.
```

Thus the post-local thinning still required for a square-root bound is

\[
\frac{41}{42}-\frac12=\boxed{\frac{10}{21}}.
\]

The s5 method itself is now explicitly closed, so 14-4bg treats `41/42` as the current local input and moves the main track to a genuinely new post-local mechanism.

---

## 2. Why the separated Sha-plus-height route is not the primary next target

Stage14-4aq gives the exact global identity

\[
R=\Sigma-T_{\Sha}
\]

from

\[
0\to E_F(\mathbf Q)/2E_F(\mathbf Q)
\to \operatorname{Sel}_2(E_F)
\to \Sha(E_F)[2]\to0.
\]

However, its complete finite `H<=20,000` audit gives only

```text
R/Sigma about 0.73 .. 0.81,
```

and proves no positive power decay for this ratio. Therefore no positive `delta_glob` is currently available.

Stage14-4ar then isolates the correct minimum non-torsion height event, but the complete family count of that event is not measured and no uniform least-generator/regulator lower-tail theorem has been proved.

So the separated route would require two new family theorems:

```text
locally soluble -> globally soluble,
globally soluble -> logarithmically small point,
```

whose combined exponent would have to satisfy

\[
\delta_{\rm glob}+\delta_{\rm ht}\ge\frac{10}{21}
\]

to reach the square-root main-term scale after s5u.

The identities remain valid diagnostics, but neither factor currently supplies a quantitative foothold.

---

## 3. Direct post-local class count

For a primitive oriented first-face base

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

write

\[
E_F:\quad W^2=Z(Z-S^2)(Z+X^2).
\]

Fix an admissible comparison constant `C` from Stage14-s3. Define `J_C(B)` to be the number of pairs

```text
(F, xi)
```

such that

1. `H(F)<=B`;
2. `xi` is a nonzero Kummer/2-descent class in the actual supported Stage14 system;
3. `xi` is globally soluble;
4. `xi` has a rational representative `Q` with

\[
\widehat h(Q)\le C(\log B+\log H(F)).
\]

Every globally soluble class is locally soluble, hence

\[
J_C(B)\le N_{\rm loc}(B).
\]

Conversely every physical hit below `B` supplies, by s3, a non-torsion rational point in the same logarithmic height window. Section 4 below shows that one may choose from it a nonzero mod-2 class without increasing canonical height. Choosing one such class per active base gives

\[
\boxed{V(B)\le J_C(B)\le N_{\rm loc}(B).}
\]

Thus any new bound for `J_C(B)` is automatically a physical upper bound. No local-to-global converse is required.

---

## 4. A physical non-torsion point yields a nonzero mod-2 class without height loss

Let `P` be the non-torsion point supplied by a physical hit. If

```text
P in 2 E_F(Q),
```

write `P=2P_1` and continue halving while possible.

The process terminates because `E_F(Q)` is finitely generated and a non-torsion element cannot be infinitely 2-divisible. Let `Q` be the final point. Then

```text
Q notin 2 E_F(Q),
```

so its class in `E_F(Q)/2E_F(Q)` is nonzero. Canonical height satisfies

\[
\widehat h(2R)=4\widehat h(R),
\]

therefore

\[
\widehat h(Q)\le\widehat h(P).
\]

This keeps the physical injection inside the nontrivial local 2-descent system already counted by s5u.

---

## 5. Logarithmic canonical height gives a polynomial coordinate box

For `H<=B`, the integral coefficients of

\[
W^2=Z(Z-S^2)(Z+X^2)
\]

have polynomial size in `B`. The same Weil-height/canonical-height comparison used in Stage14-s3 gives, for every representative counted by `J_C(B)`,

\[
h_Z(Q)\le K_C\log B
\]

for a fixed constant `K_C` depending only on the chosen height-window constant and the fixed family model.

For a rational point on this monic integral Weierstrass equation, write primitive coordinates

\[
Z=\frac{A}{D^2},\qquad
W=\frac{Y}{D^3},\qquad
D>0,\quad \gcd(A,D)=1.
\]

Then

\[
\boxed{|A|\le B^{K_C},\qquad D^2\le B^{K_C}.}
\]

Hence the direct post-local object is reducible to a polynomial-size integer witness box rather than an abstract distribution of regulators.

---

## 6. Exact integral witness equation

Substituting the primitive rational coordinates and clearing denominators gives

\[
\boxed{Y^2=A(A-S^2D^2)(A+X^2D^2).}
\]

Define

\[
G_0=A,
\quad G_1=A-S^2D^2,
\quad G_2=A+X^2D^2.
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

These identities make the bad-prime support explicit.

Because `gcd(A,D)=1`, an odd prime dividing two distinct `G_i` cannot divide `D`. Consequently

```text
odd support gcd(G0,G1) subset odd support(S),
odd support gcd(G0,G2) subset odd support(X),
odd support gcd(G1,G2) subset odd support(H).
```

Every odd prime outside `SXH` therefore divides at most one factor `G_i`. Since `G_0G_1G_2=Y^2`, its valuation there is even. Thus every signed squarefree kernel of the three factors is supported on

\[
\boxed{2SXH.}
\]

This is precisely the moving bad-prime support already present in the Stage14 local 2-descent system.

---

## 7. Fixed-state intersection-of-quadrics form

For a fixed nonzero descent state, write the three factors as

\[
G_i=d_i u_i^2,
\]

where the signed squarefree kernels `d_i` are supported on `2SXH` and are constrained by the local state.

Then the exact witness equations become

\[
\boxed{d_0u_0^2-d_1u_1^2=S^2D^2,}
\]

\[
\boxed{d_2u_2^2-d_0u_0^2=X^2D^2.}
\]

The third relation

\[
d_2u_2^2-d_1u_1^2=H^2D^2
\]

follows from `S^2+X^2=H^2`.

So the selected post-local problem is an averaged bounded incidence problem for an explicit two-quadrics system, with the kernel triple already restricted by the closed local sieve.

The support-state multiplicity remains subpolynomial (`B^o(1)`), so passing between `J_C(B)` and the fixed signed kernel triples costs only `B^epsilon` at exponent scale.

---

## 8. Quantitative target

Merged s5u gives

\[
N_{\rm loc}(B)\ll B^{41/42+\epsilon}.
\]

Therefore the first genuine post-local improvement target is

\[
\boxed{
J_C(B)\ll B^{41/42-\delta_{\rm post}+\epsilon}
}
\]

for any fixed `delta_post>0`.

A square-root sufficient target is

\[
\boxed{J_C(B)\ll B^{1/2+\epsilon},}
\]

which requires

\[
\boxed{\delta_{\rm post}\ge\frac{10}{21}.}
\]

Equivalently on the Euclid scale `B~M^2`, the local class count is

\[
M^{2-1/21}=M^{41/21},
\]

while the square-root physical target is `M^{1+o(1)}`. Thus the direct witness step must eventually supply an additional `M^{-20/21}` thinning to reach the observed scale.

No such exponent is claimed in 4bg; the point is to identify the first concrete incidence theorem whose proof would improve the current bound.

---

## 9. Route decision

The comparison is now fixed as follows.

```text
SEPARATED GLOBAL/SHA + HEIGHT ROUTE
- exact algebraic identities available;
- two new family distribution theorems required;
- positive delta_glob currently 0 proved;
- positive delta_ht currently 0 proved;
- height-window family census incomplete.

DIRECT GLOBAL-SMALL-POINT ROUTE
- exact physical inclusion V<=J_C available;
- keeps the closed local-state restrictions;
- global solubility and small height are counted jointly;
- reduces to an explicit bounded integer equation / two-quadrics system;
- any direct incidence saving immediately improves V(B).
```

Therefore the direct route is the main-track choice.

The separated 4aq/4ar retainers remain available as secondary diagnostics or future alternative interfaces if a strong Sha or least-generator theorem appears.

---

## Boundary

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
