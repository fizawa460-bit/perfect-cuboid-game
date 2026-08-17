# Stage27-19-r5ag — exact normalized physical-height receiver with primitive scale retained

```text
TASK_ID=Stage27-19-r5ag
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5af
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARALLEL_LANE=true
```

r5af showed that the one-way r402a parameter box can lose a genuine power of physical height on a fixed-tau family. This route restores the exact `R` receiver in the normalized r5aa/r5ab variables without discarding the primitive scaling factor.

Write `Gamma=gcd(E,X,Y)` for the primitive toric scale, and write `delta=gcd(n,s)` for the r5aa common square scale. Retain

\[
p=s_0^2a,\qquad q=n_0^2b,\qquad g=\delta^2h,
\]

and from r5ab

\[
U=hJ,
\qquad
V=\delta^2h(p+q),
\qquad
J=abh+\delta^2(p-q)=bm^2+p\delta^2.
\]

## 1. Exact physical-height identity

The frozen Stage19 toric interface gives

\[
\Gamma^2R^2=4UV.
\]

Substituting the normalized factors gives exactly

\[
\boxed{
\Gamma^2R^2
=4\delta^2h^2J(p+q).
}
\]

For a Stage19 survivor, let

\[
\kappa=\operatorname{sf}(p+q),
\qquad p+q=\kappa c^2,
\qquad J=\kappa w^2.
\]

Then

\[
\sqrt{J(p+q)}=\kappa wc,
\]

so the exact positive identity is

\[
\boxed{
\Gamma R=2\delta h\kappa wc.
}
\]

This is the physical-height form of the normalized squareclass receiver. No comparable-height substitution has been made.

## 2. Exact survivor inequalities from the primitive-scale upper bounds

The r402a primitive-scale facts remain

\[
\Gamma\le4mn=4m\delta n_0,
\qquad
\Gamma\le4rs=4r\delta s_0.
\]

On `R<=B`, the exact identity therefore implies

\[
\boxed{
h\kappa wc\le2Bm n_0,
}
\]

and

\[
\boxed{
h\kappa wc\le2Br s_0.
}
\]

Equivalently,

\[
\boxed{
h\sqrt{J(p+q)}
\le 2B\min(mn_0,rs_0).
}
\]

These inequalities are strictly stronger data than the separate r402a box constraints, because they retain the squareclass height and the primitive scale in the same physical inequality.

## 3. Two immediate core-height corollaries

Since

\[
J=bm^2+p\delta^2,
\]

one has both

\[
\sqrt{J(p+q)}\ge m\sqrt{b(p+q)}
\]

and

\[
\sqrt{J(p+q)}\ge \delta\sqrt{p(p+q)}.
\]

Using the first lower bound in the `Gamma<=4mn` inequality gives

\[
h\sqrt{b(p+q)}\le2Bn_0.
\]

Because `q=n_0^2b`, this can be written as

\[
\boxed{
bh\le2B\sqrt{\frac{q}{p+q}}.}
\]

Thus the normalized difference core `K=bh=r^2-s^2` carries an exact tau-asymmetric sharpening of the crude `K<2B` bound.

For the common core `g=delta^2 h`, multiply the same inequality by `delta^2` and use `n^2=delta^2 n_0^2<B`:

\[
\boxed{
g\sqrt{q(p+q)}<2B^2.}
\]

Using instead the second lower bound together with `Gamma<=4rs`, then multiplying by `delta` and using `rs<B`, gives

\[
\boxed{
g\sqrt{p(p+q)}<2B^2.}
\]

Combining the two yields

\[
\boxed{
g\sqrt{H(\tau)(p+q)}<2B^2,}
\]

where `H(tau)=max(p,q)`. Since

\[
H<p+q\le2H,
\]

this sharpens the r402c core-height receiver only by a bounded factor:

\[
g<\frac{2B^2}{\sqrt{H(p+q)}}
\le \frac{2B^2}{H}.
\]

Accordingly, this route does **not** falsely promote the exact identity into a new exponent theorem. Its value is that it identifies the physical quantity that must remain inside any future incidence count.

## 4. Why the exact identity changes the next counting problem

r5ad counted possible cores after first replacing the exact physical cutoff by

\[
m,r,n,s\ll B^{1/2}.
\]

r5af exhibited a fixed-tau family for which this box allows `gg B^(1/2)` candidates while exact physical height permits only `O(B^(1/3))` members of that family. Therefore a future Pell/determinant/square-sieve count that works only in the r402a box can lose the very power saving Stage27 is trying to detect.

The next arithmetic object is the weighted incidence set

\[
\boxed{
\Gamma R=2\delta h\sqrt{J(p+q)},
\qquad
J=bm^2+p\delta^2,
}
\]

with the exact divisibility definition of `Gamma=gcd(E,X,Y)` retained. A strict-subhalf theorem now requires a uniform count on this **exact physical-height incidence receiver**, not merely on the ambient conic under coordinate boxes.

```text
EXACT_NORMALIZED_PHYSICAL_HEIGHT_IDENTITY_PROVED=true
EXACT_NORMALIZED_PHYSICAL_HEIGHT_IDENTITY=Gamma^2*R^2=4*delta^2*h^2*J*(p+q)
EXACT_SURVIVOR_HEIGHT_IDENTITY=Gamma*R=2*delta*h*kappa*w*c
PRIMITIVE_SCALE_RETAINED=true
TAU_ASYMMETRIC_K_HEIGHT_SHARPENING_PROVED=true
TAU_ASYMMETRIC_K_HEIGHT_BOUND=b*h<=2*B*sqrt(q/(p+q))
REFINED_COMMON_CORE_HEIGHT_PROVED=true
REFINED_COMMON_CORE_HEIGHT=g*sqrt(H(tau)*(p+q))<2*B^2
REFINED_COMMON_CORE_HEIGHT_POWER_IMPROVEMENT=false
R402C_EXPONENT_IMPROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
BATCH_STOP_REASON=NEXT_STEP_REQUIRES_UNIFORM_COUNT_ON_EXACT_PHYSICAL_HEIGHT_INCIDENCE_WITH_GAMMA
NEXT_DERIVED_ROUTE=27-19-r5ah
NEXT_TARGET=UNIFORM_EXACT_HEIGHT_INCIDENCE_COUNT_OR_BARRIER_WITH_GAMMA_RETAINED
CODY_USEFUL_FOR_NEXT_ROUTE=true
```
