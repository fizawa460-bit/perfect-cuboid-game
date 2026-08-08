# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain the primitive canonical exactly-two-face population inside the integer-space-diagonal cuboid family.

```text
a-direction = ab+ac only
b-direction = ab+bc only
c-direction = ac+bc only
```

Locked ambient population:

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

## 14-1 — Definition and counting interface

Status: [x] Complete.

## 14-2 — Complete finite enumeration

Status: [x] Complete.

Two materially different exact generation routes agree through `B=2,000,000`.

## 14-3 — Finite directional-ratio reconnaissance

Status: [x] Complete.

The coarse `a/c=7/4` pattern failed dense-grid inspection. The last verified `a/b` crossing occurs at `d=1,148,545`, after which `a>b` persists only through the finite ceiling `B=2,000,000`.

No finite fit was promoted to an asymptotic theorem.

## 14-4 — True total growth order

Status: [>] Active.

Current provisional upstream assumption:

```text
UPSTREAM_STAGE13_VERSION=R02
UPSTREAM_STAGE13_STATUS=ASSUMED_PROVISIONALLY
UPSTREAM_STAGE13_FINAL_EXTERNAL_FREEZE=false
STAGE13_R03_USED=false
```

The imported statement is only the Stage13 R02 directional raw asymptotic candidate

\[
A_q(B)\sim \frac{\kappa I_q}{3\pi^3}B(\log B)^3.
\]

The R02 pair-overlap and triple-overlap little-o claims are not imported in 14-4aa.

### 14-4aa — independent two-face parametrization and proof-input audit

Status: [x] Complete.

Use generic coordinates with shared edge `e` and nonshared edges `x<y`:

\[
e^2+x^2=u^2,\qquad
 e^2+y^2=v^2,\qquad
 u^2+y^2=d^2.
\]

Then automatically

\[
v^2+x^2=d^2.
\]

The three directions are the chamber positions of `e`:

```text
a: e<x<y
b: x<e<y
c: x<y<e
```

So all three directions share one arithmetic object.

Each raw pair object carries four right triangles

```text
(e,x,u), (e,y,v), (u,y,d), (v,x,d)
```

with only three independent equations.

Using primitive Euclid bases and arbitrary positive scales, the two face triples satisfy the shared-edge fiber-product equation

\[
k_1L_{\sigma_1}(m,n)=k_2L_{\sigma_2}(r,s),
\]

with four role charts `DD,DP,PD,PP`. A third Euclid triple imposes the space diagonal by matching

\[
k_1H(m,n)=k_3L_{\sigma_3}(p,q),
\qquad
k_2L_{\bar\sigma_2}(r,s)=k_3L_{\bar\sigma_3}(p,q).
\]

Global cuboid primitivity is applied **after** gluing:

\[
\gcd(e,x,y)=1.
\]

The scales must not be forced to one.

Artifacts:

```text
stages/stage14/archive/stage14-4aa-parametrization-input-audit.md
stages/stage14/data/14-4/proof_input_audit.json
```

Decision:

```text
STAGE14_4AA=COMPLETE
ONE_GENERIC_ARITHMETIC_OBJECT_FOR_ALL_THREE_DIRECTIONS=true
EUCLID_SHARED_EDGE_FIBER_PRODUCT_LOCKED=true
THIRD_PYTHAGOREAN_GLUING_LOCKED=true
TRUE_GROWTH_ORDER_IDENTIFIED=false
UNIQUE_PARAMETERIZATION=false
BOUNDED_PARAMETER_MULTIPLICITY=false
```

### 14-4ab — representation multiplicity and explicit matching-variable reduction

Status: [>] Next.

Purpose:

- determine the exact/controlled multiplicity of the three-triple Euclid representation;
- isolate duplicate symmetries from genuine arithmetic multiplicity;
- solve the shared-edge scale equation in gcd/lcm variables;
- rewrite the remaining two matching equations as an explicit divisibility/counting problem;
- preserve the three chamber inequalities separately from the arithmetic core;
- do not guess the growth exponent yet.

## 14-5 — Directionwise asymptotic structure

Status: pending Stage14-4.

## Scope boundary

No true growth exponent, leading constant, limiting directional ratio, eventual leader, Euler-side equality, or perfect-cuboid nonexistence result is currently established for Stage14.

```text
NEXT=Stage14-4ab representation multiplicity and explicit matching-variable reduction
```