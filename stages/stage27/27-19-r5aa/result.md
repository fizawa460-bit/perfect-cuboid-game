# Stage27-19-r5aa — exact tau/core square-factor normalization

```text
TASK_ID=Stage27-19-r5aa
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r402c-f
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARALLEL_LANE=true
```

This route attacks the arithmetic representation theorem requested by `Stage27-19-r402f`. It does not try to improve the global exponent by another formal energy inequality. Instead it resolves the representation multiplicity at a **fixed reduced tau and fixed common core**.

Retain the Stage19 positive toric parameters

\[
A=s^2(m^2+n^2),\qquad D=n^2(r^2-s^2),
\]

with

\[
(m,n)=1,\qquad (r,s)=1,\qquad m>n>0,\qquad r>s>0,
\]

and write

\[
\tau=\frac pq,\qquad (p,q)=1,\qquad g=\gcd(A,D),
\]

so that the already-audited r402c receiver is

\[
A=pg,\qquad D=qg.
\]

## 1. Exact square-core factorization

Set

\[
d=\gcd(n,s),\qquad n=dn_0,\qquad s=ds_0,
\]

so `(n_0,s_0)=1`. Also set

\[
M=m^2+n^2,\qquad K=r^2-s^2.
\]

The primitive slope conditions imply

\[
(M,n)=1,\qquad (K,s)=1.
\]

In particular `M` and `K` are both coprime to `d`, while

\[
(s_0,K)=1,\qquad (n_0,M)=1.
\]

Therefore all cross-gcd contributions except `gcd(M,K)` disappear, and one gets exactly

\[
\boxed{g=\gcd(A,D)=d^2h},\qquad h:=\gcd(M,K).
\]

Now write

\[
M=ha,\qquad K=hb,\qquad (a,b)=1.
\]

Dividing `A=pg` and `D=qg` by `g=d^2h` gives the exact reduced-tau factorization

\[
\boxed{p=s_0^2a,\qquad q=n_0^2b}.
\]

The coprimality `(p,q)=1` is transparent from

\[
(s_0,n_0)=(s_0,b)=(n_0,a)=(a,b)=1.
\]

Thus every realized reduced tau/core pair carries canonical square divisors

\[
\boxed{s_0^2\mid p,\qquad n_0^2\mid q,\qquad d^2\mid g}.
\]

## 2. Deterministic reconstruction after the square-divisor choices

For fixed `(p,q,g)`, choose positive integers `s_0,n_0,d` satisfying

\[
s_0^2\mid p,\qquad n_0^2\mid q,\qquad d^2\mid g.
\]

Then define

\[
a=\frac{p}{s_0^2},\qquad b=\frac{q}{n_0^2},\qquad h=\frac{g}{d^2}.
\]

Any toric representation with these choices must satisfy

\[
\boxed{m^2=ah-d^2n_0^2},
\]

and

\[
\boxed{r^2=bh+d^2s_0^2}.
\]

Hence `m` and `r`, if they exist as positive integers, are uniquely determined. The primitive, parity, chamber, exactly-two-face and integral-space filters can only remove candidates; they cannot increase this multiplicity.

Let

\[
\rho_B(p,q,g)
\]

be the number of Stage19 physical objects with reduced tau `p/q` and common core `g`. Since Stage19's frozen toric chart is uniquely reconstructible from the physical shared-edge incidence, the preceding receiver gives

\[
\rho_B(p,q,g)
\le
\#\{s_0:s_0^2\mid p\}
\#\{n_0:n_0^2\mid q\}
\#\{d:d^2\mid g\}.
\]

Each square-divisor count is at most the ordinary divisor function. On the physical cutoff, r402a/r402c give

\[
p,q,g<2B^2.
\]

The standard uniform divisor bound therefore yields, for every fixed `epsilon>0`,

\[
\boxed{\rho_B(p,q,g)\ll_\varepsilon B^\varepsilon}
\]

uniformly in all realized `(p,q,g)`. Equivalently,

\[
\boxed{\max_{(p,q,g)}\rho_B(p,q,g)=B^{o(1)}}.
\]

This is a genuine moving-label uniform theorem: tau may vary with `B`, provided the common core `g` is retained as part of the label. It is strictly stronger than the r402b pointwise fixed-tau theorem in this refined label space, but it does **not** imply a uniform fixed-tau subpower theorem because one tau fiber may contain many distinct `g` values.

## 3. Joint-core support reduction

For a dyadic tau-height band

\[
T\le H(\tau)<2T,
\]

define the realized joint support

\[
\mathcal K_T(B)
=
\{(p,q,g):\ p/q\text{ is reduced, }T\le H(p/q)<2T,\ \rho_B(p,q,g)>0\},
\]

and

\[
K_T(B)=\#\mathcal K_T(B).
\]

Then the uniform refined-label multiplicity theorem gives immediately

\[
\boxed{N_T(B)\le B^{o(1)}K_T(B)}.
\]

Consequently a sufficient strict-subhalf restart theorem is now simply: there exists one fixed `delta>0` such that uniformly over every dyadic `T<=2B^2`,

\[
\boxed{K_T(B)\ll B^{1/2-\delta+o(1)}}.
\]

The `O(log B)` dyadic bands are absorbed into `B^{o(1)}`, giving

\[
N_2(B)\ll B^{1/2-\delta+o(1)}.
\]

The r402c height/core tradeoff remains available on this joint support:

\[
\boxed{g\ll B^2/T}.
\]

Thus the representation-multiplicity part of the r402f restart request is discharged. The unresolved arithmetic problem is reduced to **joint support**: count which `(p,q,g)` are actually realizable, or equivalently control how many distinct common cores `g` can occur above a moving reduced tau.

## 4. Collision interpretation

Write `j(t,g)` for the refined-label multiplicity. The same-core part of the ordered same-tau collision energy is

\[
C_{\mathrm{same\ core}}
=
\sum_{t,g}j(t,g)(j(t,g)-1).
\]

Since `max j(t,g)=B^{o(1)}`,

\[
\boxed{C_{\mathrm{same\ core}}\le B^{o(1)}N_2(B)}.
\]

Therefore any genuinely large same-tau collision mass must come from pairs with **different common cores** `g_1\ne g_2`, up to a subpower same-core contribution. This isolates the remaining collision obstruction without claiming it has been bounded.

No strict sub-square-root theorem follows from this route alone. In particular, neither `K_T(B)<<B^(1/2-delta)` nor a fixed-power bound for the number of realized `g` values above each tau is proved here.

```text
TAU_CORE_GCD_SQUARE_FACTORIZATION_PROVED=true
TAU_CORE_GCD_FACTORIZATION=g=d^2*h
TAU_REDUCED_NUMERATOR_FACTORIZATION=p=s0^2*a
TAU_REDUCED_DENOMINATOR_FACTORIZATION=q=n0^2*b
FIXED_TAU_G_CORE_MULTIPLICITY_UNIFORM_SUBPOWER_PROVED=true
FIXED_TAU_G_CORE_MULTIPLICITY_BOUND=B^o(1)
JOINT_TAU_G_SUPPORT_DEFINED=true
JOINT_TAU_G_SUPPORT_REDUCTION_PROVED=true
JOINT_TAU_G_SUPPORT_REDUCTION=N_T<=B^o(1)*K_T
SAME_CORE_COLLISION_SUBPOWER_OVERHEAD_PROVED=true
DISTINCT_G_COLLISION_ISOLATED=true
JOINT_SUPPORT_STRICT_SUBHALF_PROVED=false
TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_ARITHMETIC_TARGET=UNIFORM_DYADIC_JOINT_SUPPORT_OR_DISTINCT_G_PER_TAU_BOUND
NEXT_DERIVED_ROUTE=27-19-r5ab
```
