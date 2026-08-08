# Stage14-4ab — exact representation multiplicity and matching reduction

## Purpose

Stage14-4aa represented a raw two-face object as three matched Pythagorean triples. Stage14-4ab removes the artificial scale freedom, proves exact representation multiplicity for a fixed shared-edge incidence, and eliminates the third Euclid triple as an independent parameter.

No true growth exponent or leading constant is claimed here.

## Upstream boundary after R03 release

Stage13 is now available to Stage14 at the reviewed R03 level, together with the post-review Stage13-12ag explicitness supplement.

```text
UPSTREAM_STAGE13_VERSION=R03_PLUS_12AG
UPSTREAM_STAGE13_REVIEWED_SNAPSHOT=STAGE13-FINAL-SELF-CONTAINED-20260809-R03
R03_GROK_VERDICT=CLOSED
R03_QWEN_VERDICT=CLOSED
R03_FULL_ACCESS_AUTHORIZED=true
UPSTREAM_STAGE13_FINAL_REPOSITORY_FREEZE=false
```

The last flag is bookkeeping only: current Stage13 README records the two CLOSED verdicts while the final repository freeze remains a separate step.

Stage14 may now use the full R03 proof map when useful, including the raw directional theorem, fixed-local-factor machinery, inert-prime local state, and pair/triple lower-order result. The exact matching reduction proved below is nevertheless Stage14-intrinsic and does not depend on Stage13.

In particular R03 supplies the inherited ceiling

\[
O_{qr}(B)=o(B(\log B)^3),\qquad T(B)=o(B(\log B)^3),
\]

hence

\[
N_a^{(2)},N_b^{(2)},N_c^{(2)},N_2=o(B(\log B)^3).
\]

This is an upper-scale statement only. It does not identify the true two-face order.

## 1. Primitive oriented Pythagorean face data

For a primitive Euclid base

\[
m>n>0,\qquad (m,n)=1,\qquad m-n\equiv1\pmod2,
\]

define

\[
L_D=m^2-n^2,\qquad L_P=2mn,\qquad H=m^2+n^2.
\]

An oriented primitive face datum is

\[
F=(S,X,H),
\]

where `S` is the leg designated to become the shared cuboid edge and `X` is the other leg. Thus for some `sigma in {D,P}`,

\[
S=L_\sigma(m,n),\qquad X=L_{\bar\sigma}(m,n).
\]

For each datum,

\[
\gcd(S,X)=\gcd(S,H)=\gcd(X,H)=1.
\]

Every positive integer Pythagorean triangle with a distinguished leg has a unique decomposition

\[
(kS,kX,kH)
\]

into a positive scale `k` times one oriented primitive face datum, after the standard Euclid normalization `m>n`, coprimality and opposite parity.

## 2. Exact solution of the shared-edge scale equation

Take two oriented primitive face data

\[
F_1=(S_1,X_1,H_1),\qquad F_2=(S_2,X_2,H_2).
\]

Write the physical faces as

\[
(e,x,u)=k_1(S_1,X_1,H_1),
\]

\[
(e,y,v)=k_2(S_2,X_2,H_2).
\]

The common-edge equation is

\[
k_1S_1=k_2S_2.
\]

Let

\[
g=\gcd(S_1,S_2),\qquad
\alpha=S_1/g,\qquad
\beta=S_2/g.
\]

Then `(alpha,beta)=1`, and all positive integer solutions are exactly

\[
\boxed{k_1=t\beta,\qquad k_2=t\alpha,\qquad t\ge1.}
\]

Consequently

\[
\begin{aligned}
e&=tg\alpha\beta=t\operatorname{lcm}(S_1,S_2),\\
x&=t\beta X_1,\\
y&=t\alpha X_2,\\
u&=t\beta H_1,\\
v&=t\alpha H_2.
\end{aligned}
\]

This solves the first matching equation completely.

## 3. Global primitivity kills exactly the common scale

Define the minimal glued edges

\[
e_0=g\alpha\beta,\qquad x_0=\beta X_1,\qquad y_0=\alpha X_2.
\]

### Lemma

\[
\boxed{\gcd(e_0,x_0,y_0)=1.}
\]

### Proof

Suppose a prime `p` divides all three.

Because `e_0=g alpha beta`, `p` divides at least one of `g,alpha,beta`.

- If `p|alpha`, then `p|S_1`. Primitive-face coprimality gives `p` not dividing `X_1`, while `(alpha,beta)=1` gives `p` not dividing `beta`; hence `p` does not divide `x_0=beta X_1`, contradiction.
- If `p|beta`, symmetrically `p` does not divide `y_0=alpha X_2`.
- If `p|g` but `p` divides neither `alpha` nor `beta`, then `p|S_1,S_2`, so primitive-face coprimality gives `p` not dividing `X_1,X_2`; hence `p` divides neither `x_0` nor `y_0`, contradiction.
- If `p|g` together with `alpha` or `beta`, one of the first two contradictions applies.

Thus no prime divides all three.

Since

\[
(e,x,y)=t(e_0,x_0,y_0),
\]

we obtain the exact identity

\[
\boxed{\gcd(e,x,y)=t.}
\]

Therefore a primitive Stage14 cuboid has

\[
\boxed{t=1.}
\]

This does **not** force the two physical face scales to one. Instead

\[
\boxed{k_1=\beta=S_2/g,\qquad k_2=\alpha=S_1/g,}
\]

which may be arbitrarily large.

Hence the primitive shared-edge gluing is exactly

\[
\boxed{
\begin{aligned}
e&=\operatorname{lcm}(S_1,S_2)=g\alpha\beta,\\
x&=\beta X_1,\\
y&=\alpha X_2,\\
u&=\beta H_1,\\
v&=\alpha H_2.
\end{aligned}}
\]

No free global scale survives.

## 4. Exact representation multiplicity

The two nonshared physical edges are canonically ordered by

\[
x<y.
\]

Without this convention, swapping the two face data exchanges `(x,u)` with `(y,v)` and gives the same shared-edge raw-pair incidence. The condition `x<y` removes this obvious swap.

After `x<y` is fixed, every raw Stage14 pair incidence has exactly one ordered pair `(F_1,F_2)` of oriented primitive face data:

1. the physical triangles `(e,x,u)` and `(e,y,v)` are determined by the incidence;
2. each triangle has a unique scale-times-primitive-Euclid decomposition with the shared leg distinguished;
3. global primitivity forces the common matching scalar `t=1`;
4. `x<y` fixes which face is first and which is second.

Thus

\[
\boxed{\text{parameter-fiber multiplicity}=1}
\]

for a fixed raw pair incidence.

A triple-face object contributes three intended raw pair incidences, one for each shared edge. That is incidence multiplicity from `T`, not duplicate parametrization inside a fixed shared-edge incidence.

## 5. Elimination of the third Euclid triple

After primitive shared-edge reduction,

\[
u=\beta H_1,\qquad y=\alpha X_2.
\]

Therefore the integer-space-diagonal condition is exactly the single square condition

\[
\boxed{(\beta H_1)^2+(\alpha X_2)^2=d^2.}
\]

Equivalently,

\[
\boxed{(\alpha H_2)^2+(\beta X_1)^2=d^2.}
\]

The equality of the two radicands is the identity

\[
\beta^2H_1^2+\alpha^2X_2^2
=(g\alpha\beta)^2+(\beta X_1)^2+(\alpha X_2)^2
=\alpha^2H_2^2+\beta^2X_1^2.
\]

So the third Euclid datum from 14-4aa is not an independent counting variable.

Let

\[
h=\gcd(\beta H_1,\alpha X_2).
\]

Because `(alpha,beta)=1`, `gcd(beta,X_2)=1`, and `gcd(alpha,H_1)=1`,

\[
\boxed{h=\gcd(H_1,X_2).}
\]

If the square condition holds, then

\[
\left(\frac{\beta H_1}{h},\frac{\alpha X_2}{h},\frac d h\right)
\]

is primitive, so its Euclid parameters and leg role are unique. The 14-4aa third-triple variables are therefore recovered uniquely with

\[
\boxed{k_3=h=\gcd(H_1,X_2).}
\]

There is no third independent scale sum.

## 6. Exact bijective pair-of-faces parameter space

Choose two oriented primitive Pythagorean face data

\[
F_1=(S_1,X_1,H_1),\qquad F_2=(S_2,X_2,H_2).
\]

Put

\[
g=(S_1,S_2),\qquad \alpha=S_1/g,\qquad \beta=S_2/g,
\]

and define

\[
\boxed{
\begin{aligned}
e&=g\alpha\beta,\\
x&=\beta X_1,\\
y&=\alpha X_2,\\
d^2&=\beta^2H_1^2+\alpha^2X_2^2.
\end{aligned}}
\]

Then impose

```text
x < y
d^2 is a perfect square
d <= B
```

for a raw pair incidence.

The glued cuboid is automatically primitive; there is no additional gcd filter after minimal gluing.

The exactly-two / triple split is the final exact test

```text
x^2+y^2 nonsquare  -> exactly two faces
x^2+y^2 square     -> triple T witness
```

The three Stage14 directions remain pure chamber conditions on the same arithmetic object:

```text
a: e<x<y
b: x<e<y
c: x<y<e
```

Thus Stage14-4aa's three-triple fiber product has reduced bijectively to

```text
two oriented primitive Euclid face data
+ gcd(S1,S2)
+ one exact diagonal-square condition
+ x<y
+ one shared-edge chamber test
```

## 7. Independent finite audit of the bijection

A new Stage14-4ab enumerator works only in this face-pair parameter space. It does not enumerate cuboid edges first and does not use the Stage14-2 production route.

It reproduces the locked exactly-two counts:

```text
B=1000   (2,0,0)
B=2000   (2,2,1)
B=5000   (6,6,3)
B=10000  (9,11,5)
```

with `T=0` at all four audit cutoffs.

Artifacts:

```text
stages/stage14/scripts/14-4/bijection_audit.py
stages/stage14/data/14-4/bijection_audit.json
```

This finite agreement is validation of the exact reduction, not a proof of its asymptotic consequences.

## 8. Consequence of full Stage13 R03 access

Stage13 R03 proves, at its theorem-candidate boundary,

\[
O_{qr}(B)=o(B(\log B)^3),\qquad T(B)=o(B(\log B)^3).
\]

Therefore Stage14 may now record as an inherited analytic ceiling

\[
\boxed{N_2(B)=o(B(\log B)^3).}
\]

This ceiling is compatible with the new bijective parameter space but does not determine whether the true scale is, for example, `B log B`, `B (log B)^2`, a smaller power of `B`, or another order.

The next task must extract a height/divisibility counting problem from the exact bijection rather than infer a model from finite data.

## 9. Stage14-4ab decision

```text
STAGE14_4AB=COMPLETE
UPSTREAM_STAGE13_VERSION=R03_PLUS_12AG
R03_FULL_ACCESS_AUTHORIZED=true
R03_PAIR_OVERLAP_LITTLE_O_IMPORTED=true
R03_TRIPLE_OVERLAP_LITTLE_O_IMPORTED=true
SHARED_EDGE_SCALE_SOLUTION_EXACT=true
GLOBAL_COMMON_SCALE_EQUALS_CUBOID_GCD=true
PRIMITIVE_COMMON_SCALE_T=1=true
MINIMAL_GLUING_AUTOMATICALLY_PRIMITIVE=true
FIXED_RAW_PAIR_PARAMETER_FIBER_MULTIPLICITY=1
THIRD_EUCLID_TRIPLE_INDEPENDENT=false
THIRD_TRIPLE_SCALE_K3=gcd(H1,X2)
BIJECTIVE_TWO_FACE_PARAMETER_SPACE_LOCKED=true
BIJECTION_FINITE_AUDIT_PASS=true
TRUE_GROWTH_ORDER_IDENTIFIED=false
LEADING_CONSTANT_IDENTIFIED=false
DIRECTIONAL_LIMIT_IDENTIFIED=false
NEXT=Stage14-4ac height inequality and arithmetic counting envelope
```
