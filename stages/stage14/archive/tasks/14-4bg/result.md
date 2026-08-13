# Stage14-4bg — exact integral model for the selected post-local witness count

## Result

Merged Stage14-s6-00 already selects direct post-local global-small-point incidence as the primary route. Stage14-4bg does not duplicate that decision; it instantiates it on the `14-4` line as an exact bounded integer incidence problem.

Merged s5u gives

```text
N_local(B) <<_epsilon B^(41/42+epsilon),
```

and s6-00 fixes the square-root budget

```text
41/42 - 1/2 = 10/21.
```

For an admissible s3 height constant `C`, define `J_C(B)` as the number of pairs `(F,xi)` where `F=(S,X,H)` is a primitive oriented Pythagorean first-face base with `H<=B`, `xi` is a nonzero supported mod-2 Kummer/descent class, `xi` is globally soluble, and some rational representative `Q` satisfies

\[
\widehat h(Q)\le C(\log B+\log H).
\]

Then

\[
\boxed{V(B)\le J_C(B)\le N_{\rm loc}(B)}.
\]

The lower inclusion follows from s3. If the physical non-torsion point is divisible by 2, repeatedly halve it. Mordell--Weil finite generation makes the process terminate at a nonzero mod-2 class, while `\widehat h(2R)=4\widehat h(R)` means height never increases.

For

\[
E_F:\quad W^2=Z(Z-S^2)(Z+X^2),
\]

canonical-height comparison gives a fixed `K_C` such that a point counted by `J_C(B)` has primitive rational coordinates

\[
Z=A/D^2,\qquad W=Y/D^3,\qquad \gcd(A,D)=1,
\]

with

\[
|A|\le B^{K_C},\qquad D^2\le B^{K_C}.
\]

Clearing denominators gives the exact witness equation

\[
\boxed{Y^2=A(A-S^2D^2)(A+X^2D^2)}.
\]

Set

\[
G_0=A,\qquad G_1=A-S^2D^2,\qquad G_2=A+X^2D^2.
\]

Then

\[
G_0-G_1=S^2D^2,\qquad
G_2-G_0=X^2D^2,\qquad
G_2-G_1=H^2D^2.
\]

Since `gcd(A,D)=1`, any odd prime dividing two `G_i` cannot divide `D`; hence

```text
odd support gcd(G0,G1) subset odd support(S),
odd support gcd(G0,G2) subset odd support(X),
odd support gcd(G1,G2) subset odd support(H).
```

Every odd prime outside `SXH` therefore divides at most one factor. Since `G0*G1*G2=Y^2`, its valuation there is even. Thus the signed squarefree kernels are supported on

\[
\boxed{2SXH},
\]

exactly the moving bad-prime support of the closed Stage14 local system.

For a fixed supported descent state write

\[
G_i=d_i u_i^2
\]

with signed squarefree `d_i` supported on `2SXH`. The witness equations become

\[
\boxed{d_0u_0^2-d_1u_1^2=S^2D^2,}
\]

\[
\boxed{d_2u_2^2-d_0u_0^2=X^2D^2.}
\]

The third difference is `H^2D^2` automatically. Thus the selected post-local problem is now an averaged bounded incidence count for an explicit intersection of two quadrics, with the local squareclass state frozen. Supported-state multiplicity remains `B^o(1)`.

The quantitative contract is

\[
J_C(B)\ll B^{41/42+\epsilon}
\]

currently, and any

\[
J_C(B)\ll B^{41/42-\delta_{post}+\epsilon},\qquad \delta_{post}>0,
\]

is genuine post-local progress. The square-root upper-bound scale requires

\[
\boxed{\delta_{post}\ge10/21}.
\]

No positive post-local saving is proved in 4bg; the exact incidence object is now frozen for 4bh / s6-01.

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
