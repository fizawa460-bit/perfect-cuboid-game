# Stage27-19-r5ad — uniform moving-tau core ceiling

```text
TASK_ID=Stage27-19-r5ad
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5aa-r5ac
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARALLEL_LANE=true
PREDECESSOR_FRESH_AUDIT=PASS
```

This route uses only the exact r5aa normalization and the r402a physical height bounds. It gives a genuinely uniform bound for the number of distinct common cores above a moving reduced tau. It does not use Mordell–Weil rank uniformity and it does not prove a subpower tau fiber.

Retain

\[
p=s_0^2a,\qquad q=n_0^2b,\qquad g=d^2h,
\]
\[
m^2=ah-d^2n_0^2,\qquad r^2=bh+d^2s_0^2,
\]
with
\[
(dn_0,a)=(ds_0,b)=1.
\]
Let
\[
H=H(\tau)=\max(p,q).
\]
For a fixed reduced tau `p/q`, write `D_B(p,q)` for the number of distinct integers `g` realized by Stage19 objects with `R<=B` and reduced tau `p/q`.

## 1. Fix one square-divisor decomposition

Fix one admissible choice
\[
s_0^2\mid p,\qquad n_0^2\mid q,
\]
and set
\[
a=p/s_0^2,\qquad b=q/n_0^2,
\qquad A=\max(a,b),\qquad S=\max(s_0,n_0).
\]
The r402a bounds `n^2<B` and `s^2<B` give
\[
d<\frac{B^{1/2}}{S}.
\]
Also `m,r<\sqrt{2B}`.

For each fixed `d`, the first reconstruction equation implies
\[
m^2\equiv-(dn_0)^2\pmod a.
\]
Because `(dn0,a)=1`, after normalization this is `z^2=-1 mod a`. The number of roots modulo `a` is at most `2^{omega(a)+O(1)}=a^{o(1)}` uniformly. Hence the number of possible `m<sqrt(2B)` is
\[
\ll_\varepsilon B^\varepsilon\left(\frac{B^{1/2}}a+1\right).
\]
Each such `m` determines
\[
h=\frac{m^2+d^2n_0^2}{a}
\]
and therefore `g=d^2h` uniquely.

Likewise the second reconstruction equation gives
\[
r^2\equiv d^2s_0^2\pmod b.
\]
Because `(ds0,b)=1`, this normalizes to `z^2=1 mod b`, whose root count is at most `4*2^{omega(b)}=b^{o(1)}`. Thus for fixed `d`, the number of possible `g` is also
\[
\ll_\varepsilon B^\varepsilon\left(\frac{B^{1/2}}b+1\right).
\]
Use the equation corresponding to `A=max(a,b)`. Summing over `d<B^{1/2}/S` gives, for this fixed decomposition,
\[
\boxed{
D_B(p,q;s_0,n_0)
\ll_\varepsilon
B^\varepsilon\left(\frac{B}{AS}+\frac{B^{1/2}}S\right).
}
\]

## 2. Eliminate the decomposition scale

Since
\[
p=s_0^2a\le S^2A,\qquad q=n_0^2b\le S^2A,
\]
we have
\[
H\le S^2A.
\]
As `A>=1`,
\[
AS\ge S\sqrt A=\sqrt{AS^2}\ge\sqrt H.
\]
Therefore
\[
\frac{B}{AS}\le\frac{B}{\sqrt H},
\qquad
\frac{B^{1/2}}S\le B^{1/2}.
\]
The number of square-divisor decompositions `(s0,n0)` is at most
\[
\#\{s_0:s_0^2|p\}\#\{n_0:n_0^2|q\}=B^{o(1)}
\]
uniformly because `p,q<2B^2`. Summing the fixed-decomposition bound yields the uniform moving-label theorem
\[
\boxed{
D_B(p,q)
\ll_\varepsilon
B^\varepsilon\left(\frac{B}{\sqrt{H(p/q)}}+B^{1/2}\right).
}
\]
Equivalently, on a dyadic band `T<=H(tau)<2T`,
\[
\boxed{
D_B(\tau)
\ll_\varepsilon
B^\varepsilon\left(\frac{B}{\sqrt T}+B^{1/2}\right).
}
\]

## 3. Consequence for the physical tau fiber

r5aa proved that each fixed `(tau,g)` carries only `B^{o(1)}` physical representations. Hence the Stage19 tau-fiber multiplicity satisfies uniformly in moving tau
\[
\boxed{
w_B(\tau)
\ll_\varepsilon
B^\varepsilon\left(\frac{B}{\sqrt{H(\tau)}}+B^{1/2}\right).
}
\]
This is a uniform theorem, unlike the pointwise fixed-tau Mordell–Weil estimate from r402b. But it is only a square-root ceiling in the worst branch, not a uniform subpower theorem.

The refined fixed-decomposition form
\[
D_B(p,q;s_0,n_0)
\ll B^{o(1)}\left(\frac{B}{AS}+\frac{B^{1/2}}S\right)
\]
is retained for future stratification: large square scale `S` or large normalized coefficient `A` does improve the individual fiber.

## 4. Boundary

This result does not by itself beat the global Stage19 half-power upper bound. The term `B^(1/2)` is a genuine remaining uniform branch, and multiplying this ceiling by a tau-support bound would only lose information relative to the already frozen whole-family theorem.

```text
UNIFORM_MOVING_TAU_DISTINCT_CORE_BOUND_PROVED=true
UNIFORM_MOVING_TAU_DISTINCT_CORE_BOUND=D_B(tau)<<B^epsilon*(B/sqrt(H(tau))+sqrt(B))
REFINED_DECOMPOSITION_CORE_BOUND_PROVED=true
REFINED_DECOMPOSITION_CORE_BOUND=D_B(tau;s0,n0)<<B^epsilon*(B/(A*S)+sqrt(B)/S)
UNIFORM_MOVING_TAU_FIBER_POWER_BOUND_PROVED=true
UNIFORM_MOVING_TAU_FIBER_BOUND=w_B(tau)<<B^epsilon*(B/sqrt(H(tau))+sqrt(B))
TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5ae
NEXT_TARGET=TEST_WHETHER_R5AC_NORM_SUPPORT_PLUS_CORE_HEIGHT_CAN_BY_ITSELF_GIVE_POWER_SAVING
```
