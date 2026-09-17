# Stage32 MB104 — U8 canonical-orbifold cotangent wall — 2026-09-17

Status: **NEW VIEW AUDITED / CMS AND RR BIGNESS CRITERIA FAIL / DIRECT ORBIFOLD CURVE COMPLEXITY REDUCES TO R8 / NO CREDIT**

## Motivation

The smooth resolution `S` has

```text
K_S^2=16,
c2(S)=80,
s2(S)=-64.
```

The singular box/canonical surface has 48 canonical `A1` points. A naive orbifold calculation is much more favorable: each `A1` changes the orbifold Euler number by `2-1/2=3/2`, hence

```text
c2_orb(X)=80-48*(3/2)=8,
s2_orb(X)=16-8=8>0.
```

This suggested using the canonical orbifold directly rather than the smooth-resolution log-BMY route.

## 1. Smooth-model cotangent bigness is not certified

Asega--De Oliveira--Weiss, *Surface quotient singularities and bigness of the cotangent bundle: Part I* (European J. Math. 11 (2025), article 22), give the Canonical Model Singularities (CMS) criterion

```text
sum_(y in Sing X_can) h^1_Omega(y) + s2(S)/3! > 0
```

as a sufficient criterion for bigness of the cotangent bundle of the smooth birational class.

For an `A_n` singularity their closed formula gives, at `n=1`,

```text
h^1_Omega(A1)=4/27.
```

Thus the 48 nodes contribute

```text
48*(4/27)=64/9,
```

whereas

```text
s2(S)/6=-64/6=-32/3.
```

Therefore the CMS left-hand side is

```text
64/9-32/3=-32/9 < 0.
```

So 48 `A1` points do not meet the 2025 CMS sufficient criterion. With only `A1` contributions one would need strictly more than 72 such singularities, i.e. at least 73.

The older Roulleau--Rousseau criterion is also unavailable. It requires

```text
s2(S)+s2_orb(X)>0,
```

but here

```text
-64+8=-56<0.
```

Hence the positive orbifold Segre number of the singular model does **not** by itself imply that the minimal resolution has big cotangent bundle.

## 2. Direct orbifold use sees linearly growing source complexity

There is a second possibility: use orbifold symmetric differentials directly on the singular surface instead of extending them to `S`.

For a minimal `A1` branch, the retained local model is

```text
(x,y,z)=(t,lambda*t,lambda^2*t),
xz=y^2.
```

Upstairs on the local quotient chart `C^2 -> C^2/{+-1}` this is lifted by

```text
t=u^2,
p=u,
q=lambda*u.
```

Thus a normalization branch through the `A1` point acquires an order-two stacky point in the natural twisted normalization mapping representably to the canonical stack.

For the balanced MB104 packet,

```text
coarse normalization genus g=1,
R=R8=112l
```

normalization branches occur over the supported box nodes. Hence the orbifold canonical degree of the twisted normalization is

```text
deg K_orb(source)
 = 2g-2 + R*(1-1/2)
 = 56l.
```

But the canonical degree of the carrier is

```text
K_X.C=112l.
```

Therefore the exact balanced packet lies on the identity

```text
K_X.C = 2 * deg K_orb(source).
```

The source orbifold complexity itself grows linearly with `l`. Consequently a general orbifold algebraic-hyperbolicity/canonical-degree estimate of the form

```text
K_X.C <= A * deg K_orb(source) + B
```

cannot yield a finite `l` window unless it supplies the special strict coefficient `A<2` (or some additional negative term tied to the exact support passport). Ordinary orbifold positivity by itself only bounds canonical degree relative to a complexity that is already proportional to `R8`.

## 3. Relation to the archived R8 problem

On the exact balanced survivor

```text
d = K_X.C = R8 = 112l,
deg K_orb(source)=R8/2.
```

Thus direct quotient-orbifold boundedness is not an independent all-`l` closure mechanism: after writing the source stack complexity explicitly, it becomes another inequality whose load-bearing variable is `R8`.

The archived MB104 route already identified that the missing global input is precisely a branch-sensitive restriction strong enough to beat the linear `R8` slope. The orbifold reformulation does not remove that missing input.

## Verdict

```text
U8_CMS_BIG_COTANGENT = BLOCKED_BY_EXACT_NUMERICS
U8_ROULLEAU_ROUSSEAU = BLOCKED_BY_EXACT_NUMERICS
U8_DIRECT_ORBIFOLD_CURVE_BOUND = EQUIVALENT/DOMINATED_BY_R8_BRANCH_COMPLEXITY
```

The useful new information is the exact critical identity

```text
K_X.C = 2 * deg K_orb(source),
```

which explains why the attractive positive orbifold Segre number of the singular model does not automatically collapse the balanced multibranch ray.

A re-entry would require a cuboid-specific orbifold inequality with effective coefficient strictly below `2`, or another exact term that penalizes the balanced support/landing passport beyond the stacky-point count.

No finite degree window, receiver/effectivity/theorem/endpoint credit, merge authorization, or Perfect-Cuboid claim is produced.
