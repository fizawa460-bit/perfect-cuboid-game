# Stage27-19-r5af — fixed-tau reconstruction saturation versus exact physical height

```text
TASK_ID=Stage27-19-r5af
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5ae
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARALLEL_LANE=true
```

The previous route showed that norm-support predicates alone are too weak. This route stress-tests the stronger strategy that also uses the two reconstruction equations, but only inside the coarse r402a parameter-height box. The test exposes an important distinction: that coarse box can contain a half-power fixed-tau family, while the exact physical cutoff `R<=B` cuts the same family much more strongly. Therefore the next upper attack should retain the exact physical-height identity instead of replacing it by `m^2+n^2<2B`, `r^2+s^2<2B` too early.

To avoid collision with the geometric space diagonal, write `delta=gcd(n,s)` for the r5aa common square scale.

## 1. A fixed reduced label tau=1/4

Fix

\[
s_0=1,\qquad n_0=2,\qquad a=b=1.
\]

Then

\[
p=s_0^2a=1,\qquad q=n_0^2b=4,
\qquad \tau=\frac14,
\qquad \kappa=\operatorname{sf}(p+q)=5.
\]

For positive coprime integers `u,v`, set

\[
\delta=2uv,
\]
\[
m=u^2-5v^2,\qquad r=u^2+5v^2,
\]
\[
n=2\delta=4uv,\qquad s=\delta=2uv.
\]

Assume in addition

\[
u\text{ odd},\qquad v\text{ even},\qquad 5\nmid u,
\qquad 6v<u<7v.
\]

Then `m>n>0` and `r>s>0`. The coprimalities are exact:

- `gcd(m,n)=1`, because `m` is odd, `gcd(m,u)=gcd(5v^2,u)=1`, and `gcd(m,v)=gcd(u^2,v)=1`;
- `gcd(r,s)=1` by the same argument.

Moreover

\[
r^2-m^2=5\delta^2.
\]

Hence

\[
M=m^2+n^2=m^2+4\delta^2,
\]
\[
K=r^2-s^2=r^2-\delta^2
\]

are exactly equal. Put

\[
h=M=K=u^4+6u^2v^2+25v^4.
\]

Thus the r5aa normalization is realized exactly:

\[
M=ha,\qquad K=hb,\qquad
p=1,\qquad q=4,\qquad g=\delta^2h.
\]

The three r5ac support predicates are also satisfied:

\[
p=1\in\mathcal S_2,
\qquad p+q=5=1^2+2^2\in\mathcal S_2,
\]

and

\[
g=\delta^2(m^2+n^2)=(\delta m)^2+(\delta n)^2\in\mathcal S_2.
\]

So this is not a norm-support artifact.

## 2. The coarse r402a height box contains a half-power family

On the wedge `6v<u<7v`,

\[
h=u^4+6u^2v^2+25v^4\asymp v^4.
\]

Therefore the r402a necessary bounds

\[
M<2B,\qquad r^2+s^2<2B
\]

hold for all such pairs with `v << B^(1/4)` after fixing a sufficiently small absolute wedge constant.

The number of coprime pairs `(u,v)` in a fixed positive-area wedge, subject to finitely many compatible congruence conditions, is `gg U^2` up to height `U`. Taking `U as B^(1/4)` gives

\[
\boxed{\gg B^{1/2}}
\]

primitive fixed-tau toric candidates inside the coarse r402a height box.

This is an ambient pre-space count, not a Stage19 survivor lower bound.

## 3. The family can simultaneously be forced to be exactly-two and non-space

The two toric faces through the shared edge are integral by construction. To force the third face to be nonintegral on a positive-density subfamily, additionally impose

\[
u\equiv1\pmod{11},\qquad v\equiv4\pmod{11}.
\]

For the raw toric coordinates

\[
E=4mnrs,\quad X=2rs(m^2-n^2),\quad Y=2mn(r^2-s^2),
\]

a direct expansion gives

\[
X^2+Y^2=16u^2v^2 F(u,v),
\]

where

\[
F(u,v)=5u^{12}-34u^{10}v^2+195u^8v^4+3620u^6v^6
+4875u^4v^8-21250u^2v^{10}+78125v^{12}.
\]

At `(u,v)=(1,4) mod 11`,

\[
F(u,v)\equiv8\pmod{11}.
\]

The residue `8` is a quadratic nonresidue modulo `11`, while `11` divides neither `u` nor `v`. Hence `X^2+Y^2` cannot be a square. The third face is nonintegral, so this congruence subfamily has exactly two integral faces.

To force failure of the Stage19 space condition as well, impose

\[
v\equiv0\pmod3,\qquad u\not\equiv0\pmod3.
\]

Here the normalized squareclass receiver is

\[
J=bm^2+p\delta^2=m^2+\delta^2,
\qquad p+q=5.
\]

Modulo `3`, one has `J=1`, hence

\[
5J\equiv2\pmod3,
\]

a quadratic nonresidue. Therefore `J(p+q)` is not a square. These congruences are compatible with the parity, modulo-5, and modulo-11 restrictions by CRT, and still leave a positive-density coprime lattice subfamily.

Thus the coarse r402a height box genuinely contains `gg B^(1/2)` primitive, exactly-two, fixed-`tau=1/4` toric candidates satisfying the r5ac norm supports and both reconstruction equations, while the space condition rejects the displayed congruence subfamily.

This proves that a counting argument based only on the r402a height box plus reconstruction/norm support cannot by itself produce a strict-subhalf theorem.

## 4. Exact primitive scaling on this family

Let `Gamma=gcd(E,X,Y)` be the primitive toric scaling factor. On the present family,

\[
\boxed{\Gamma=2\delta}.
\]

Indeed, after dividing `(E,X,Y)` by `2delta`, the three coordinates are

\[
4mr\delta,
\qquad r(m^2-4\delta^2),
\qquad 2mh.
\]

No odd prime can divide all three: a prime dividing `r`, `m`, or `delta` is excluded from one of the other coordinates by the primitive coprimalities and by

\[
h=r^2-\delta^2=m^2+4\delta^2.
\]

The middle coordinate is odd, so no further factor `2` survives either.

Using the exact Stage19 identity

\[
\Gamma^2R^2=4UV,
\]

or expanding directly, one obtains the exact factorization

\[
\boxed{
R^2=
5(u^2-4uv+5v^2)
(u^2-2uv+5v^2)^2
(u^2+2uv+5v^2)^2
(u^2+4uv+5v^2).
}
\]

On `6v<u<7v`, every displayed quadratic factor is comparable to `v^2`, so

\[
\boxed{R\asymp v^6}.
\]

Consequently the exact physical cutoff `R<=B` restricts this same two-parameter wedge to

\[
v\ll B^{1/6},
\]

and hence to only

\[
\boxed{O(B^{1/3})}
\]

members of this stress-test family before the space filter.

The half-power saturation was therefore an artifact of replacing the exact physical cutoff by the one-way r402a parameter box. This does not prove a global `B^(1/3)` upper bound; it proves that exact physical height contains arithmetic/geometric slack invisible to the earlier coarse box.

## 5. Route conclusion

The next upper attack should not import a generic Pell count on the coarse box and then sum `d` up to `sqrt(B)`. On at least this canonical fixed-tau family, that would count a `B^(1/2)` ambient box which the exact physical cutoff already compresses to `B^(1/3)`.

The correct next receiver is therefore the exact normalized formula for `Gamma^2 R^2` in the r5aa/r5ab variables, retaining `Gamma` until the final height estimate.

```text
FIXED_TAU_STRESS_LABEL=1/4
R402A_HEIGHT_BOX_FIXED_TAU_HALFPOWER_SATURATION_PROVED=true
R402A_HEIGHT_BOX_SATURATION_SIZE=gg_B^(1/2)
EXACT_TWO_CONGRUENCE_SUBFAMILY_PROVED=true
SPACE_FAILURE_CONGRUENCE_SUBFAMILY_PROVED=true
EXACT_PRIMITIVE_SCALE_ON_STRESS_FAMILY_PROVED=true
EXACT_PRIMITIVE_SCALE_ON_STRESS_FAMILY=Gamma=2*delta
EXACT_R_FACTOR_STRESS_FAMILY_PROVED=true
EXACT_PHYSICAL_HEIGHT_STRESS_GROWTH=R_asymp_v^6
EXACT_PHYSICAL_CUTOFF_STRESS_COUNT=O(B^(1/3))
GLOBAL_B_ONE_THIRD_UPPER_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5ag
NEXT_TARGET=EXACT_NORMALIZED_PHYSICAL_HEIGHT_IDENTITY_WITH_PRIMITIVE_SCALE_RETAINED
```
