# Stage15-6dy — exact fixed-prime squareclass acceptance on the reconstructed physical measure

Base: merged Stage15-6dx after fresh audit PASS. Execute `RECONSTRUCTED_BASE_FIXED_PRIME_OVERLAP_SIEVE` without projecting away the completion variable in a way that changes the charged measure.

The exact survivor condition remains
\[
\operatorname{sf}(A_0)=\operatorname{sf}(B_0),
\]
with
\[
A_0=a^4M^2U^2+d^4N^2V^2,\qquad
B_0=b^4M^2V^2+c^4N^2U^2.
\]
Equivalently in the unique positive toric parameters,
\[
A=m^2r^2+n^2s^2,\qquad B=m^2s^2+n^2r^2,
\]
and the cell reduction changes `A,B` only by square factors, so prime-valuation parity is identical.

## 1. Local population and quantifier order

Do **not** existentially project `V` out of `(cells,M,N,U,V)`. Such a projection would ask only whether some local completion exists and can turn a genuine density condition on physical states into an almost-vacuous condition on bases.

Instead retain the unique completion label. Stage15-4 proves that one primitive physical shared-edge incidence has one positive toric parameter pair `((m,n),(r,s))`; Stage15-6ct gives one cross-gcd cell decomposition. Therefore
\[
\text{physical incidence}
\longleftrightarrow
((m,n),(r,s))
\longleftrightarrow
(a,b,c,d;M,N,U,V)
\]
is multiplicity one. Retaining `V` is the **same charged physical measure**, not the 6da candidate-completion multiplicity and not a second `B^{o(1)}` charge.

Quantifiers are:

1. fix one odd prime `p` outside the finite bad set of the integral toric model;
2. impose the exact `p`-adic squareclass acceptance on the physical toric state;
3. take `B -> infinity` in the same `R<=B` physical chamber;
4. only later tensor a fixed finite prime set.

## 2. Exact valuation-parity condition

For every odd prime,
\[
\operatorname{sf}(A)=\operatorname{sf}(B)
\quad\Longrightarrow\quad
\boxed{v_p(A)\equiv v_p(B)\pmod 2}.
\]
Conversely the conjunction of this parity equality over all primes is exactly the squareclass equality.

For a fixed prime define
\[
\mathcal E_p:=\{y\in Y(\mathbf Q_p):v_p(A(y))\equiv v_p(B(y))\pmod2\}.
\]
The projective scaling of either Euclid pair multiplies both relevant homogeneous forms by squares, so this parity condition is projectively well-defined.

In cell variables the same statement is
\[
v_p(A_0)\equiv v_p(B_0)\pmod2.
\]
If `p\nmid H=abcd`, all cell coefficients are units and the 6dv coefficient-removal convention is exact. If `p|H`, the state is **not discarded**: it lies in one of the boundary/ex\-ceptional residue tubes of the toric resolution and is included below. Thus `p\nmid H` is a convenient unit stratum, not a hidden population restriction.

## 3. Inert primes are automatically accepted

For `p\equiv3 (mod 4)`, every valuation of a Gaussian norm is even. Hence
\[
v_p(A)\equiv v_p(B)\equiv0\pmod2
\]
for every primitive toric state. Equivalently the reduced norms `A_0,B_0` have no odd `p`-valuation.

Therefore
\[
\boxed{\rho_p=1\qquad(p\equiv3\!\!\pmod4).}
\]
These primes give no overlap thinning. The bounded `p=2` convention remains isolated and is not a sieve source.

## 4. Split-prime divisor geometry on the smooth toric resolution

Now let `p\equiv1 (mod 4)` be good and choose `i\in\mathbf F_p` with `i^2=-1`. On `P^1 x P^1`,
\[
A=(mr+i ns)(mr-i ns),
\qquad
B=(ms+i nr)(ms-i nr).
\]
The four torus-fixed corners are exactly the base points blown up in Stage15-2a.

The two `A` components meet at two of those corners and the two `B` components meet at the other two. After the four blow-ups:

- the strict transforms `D_{A,+},D_{A,-}` are smooth and disjoint;
- the strict transforms `D_{B,+},D_{B,-}` are smooth and disjoint;
- the exceptional multiplicity of `A` or `B` at its two blown-up self-intersections is `2`, hence **even** and invisible to squareclass parity;
- every `D_{A,epsilon}` meets every `D_{B,delta}` transversely in two points, so there are exactly `8` `A/B` intersection points.

Each strict `(1,1)` transform has `p+1` rational points. Since
\[
\#Y(\mathbf F_p)=(p+1)^2+4p=p^2+6p+1,
\]
the residue classes split exactly as
\[
N_{00}=p^2+2p+5,
\]
with neither odd divisor present,
\[
N_{10}=N_{01}=2p-6,
\]
with exactly one of the `A` or `B` odd divisors present, and
\[
N_{11}=8
\]
transverse `A/B` intersections.

## 5. Exact valuation-parity probabilities inside one residue tube

At a smooth `A`-only divisor tube, after removing unit and even exceptional factors,
\[
A=u x,\qquad B\in\mathbf Z_p^\times,
\]
with `x\in p\mathbf Z_p`. Conditional on reduction to the divisor,
\[
\Pr(v_p(x)=n)=(1-p^{-1})p^{-(n-1)},\qquad n\ge1.
\]
Thus
\[
\Pr(v_p(A)\text{ even}\mid A\equiv0\bmod p)=\frac1{p+1}.
\]
The same holds on a `B`-only tube.

At one of the eight transverse intersections,
\[
A=u x,\qquad B=v y,
\]
with independent `x,y\in p\mathbf Z_p`. Hence
\[
\Pr(v_p(A)\equiv v_p(B)\bmod2)=
\frac{p^2+1}{(p+1)^2}.
\]

For the standard good finite-place anticanonical model used in Stage15-2b, smooth residue tubes have equal local measure. Therefore the **actual charged local acceptance density** is
\[
\boxed{
\rho_p=
\frac{
N_{00}+\frac{N_{10}+N_{01}}{p+1}
+N_{11}\frac{p^2+1}{(p+1)^2}
}{p^2+6p+1}
}
\]
and simplifies to
\[
\boxed{
\rho_p=
\frac{p^4+4p^3+22p^2+4p+1}
{(p+1)^2(p^2+6p+1)}
}
\qquad(p\equiv1\!\!\pmod4).
\]
Equivalently
\[
\boxed{
1-\rho_p=
\frac{4p(p-1)^2}{(p+1)^2(p^2+6p+1)}
=\frac4p+O(p^{-2}).
}
\]
So every good split prime rejects a positive local fraction, but that fraction decays like `4/p`; it is **not** bounded below by a fixed positive constant as `p` grows.

## 6. k=1 versus k>1 local branches

Let the common parity be `epsilon_p`.

- `epsilon_p=0` means `p\nmid k`. This includes the entire `k=1` branch and the `k>1` branch with `p\nmid k`.
- `epsilon_p=1` means `p|k`, hence necessarily belongs to the `k>1` branch.

The exact split-prime local densities are
\[
\boxed{
\rho_{p,0}=
\frac{p^4+4p^3+14p^2+4p+1}
{(p+1)^2(p^2+6p+1)}
}
\]
for even-even parity and
\[
\boxed{
\rho_{p,1}=
\frac{8p^2}{(p+1)^2(p^2+6p+1)}
}
\]
for odd-odd parity, with `rho_p=rho_{p,0}+rho_{p,1}`.

Thus the local sieve preserves the branch distinction exactly; it never identifies `k=1` with a `k>1` state.

## 7. Physical masks and measure firewall

- `R<=B` remains the exact anticanonical height from Stage15-2b.
- positivity and the three canonical direction chambers are archimedean restrictions and do not alter the finite local factor;
- primitive projective normalization and unique shared-edge multiplicity are already part of the toric physical measure;
- the exactly-two mask is retained by subtracting the third-face thin set only after the fixed-local count;
- cell labels and `V` are reconstruction coordinates, not additional weights;
- `kg^2|Delta` is a survivor consequence retained after local acceptance, not recharged as an independent sieve factor;
- no Stage14 exponent or Stage15-5 thinning theorem is used.

```text
STAGE15_6_SUBSTAGE=6dy
STAGE15_6DY_LOCAL_MEASURE=UNIQUE_LABELED_PHYSICAL_TORIC_STATE
STAGE15_6DY_EXISTENTIAL_BASE_PROJECTION_USED=false
STAGE15_6DY_COMPLETION_LABEL_RETAINED_SAME_MEASURE=true
STAGE15_6DY_LOCAL_ACCEPTANCE=vp(A)==vp(B)_MOD_2
STAGE15_6DY_INERT_PRIME_ACCEPTANCE=1
STAGE15_6DY_SPLIT_DIVISOR_GEOMETRY_EXACT=true
STAGE15_6DY_SPLIT_LOCAL_DENSITY_EXACT=true
STAGE15_6DY_SPLIT_REJECTION_ASYMPTOTIC=4/p+O(1/p^2)
STAGE15_6DY_K1_KGT1_LOCAL_BRANCH_SPLIT_EXACT=true
STAGE15_6DY_PHYSICAL_MEASURE_PRESERVED=true
STAGE15_6DY_EXIT=FIXED_ADELIC_REFINED_COUNT_READY
```
