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

Two materially different exact cuboid-generation routes agree through `B=2,000,000`.

## 14-3 — Finite directional reconnaissance

Status: [x] Complete.

No finite fit was promoted to an asymptotic theorem.

## Stage13 upstream status for Stage14-4

Stage13 R03 is now fully available as an upstream proof map, together with Stage13-12ag.

```text
UPSTREAM_STAGE13_VERSION=R03_PLUS_12AG
R03_GROK_VERDICT=CLOSED
R03_QWEN_VERDICT=CLOSED
R03_FULL_ACCESS_AUTHORIZED=true
UPSTREAM_STAGE13_FINAL_REPOSITORY_FREEZE=false
```

Available imported statements/machinery include:

- raw directional asymptotics;
- fixed-local-factor transfer;
- exact inert-prime local states and multiplier;
- quantitative weighted-Wiener / harmonic closure;
- pair/triple lower-order theorem.

Therefore Stage14 may use

\[
O_{qr}(B)=o(B(\log B)^3),\qquad T(B)=o(B(\log B)^3),
\]

and hence

\[
\boxed{N_2(B)=o(B(\log B)^3)}.
\]

This is an inherited ceiling, not the true growth order.

## 14-4 — True total growth order

Status: [>] Active.

### 14-4aa — independent two-face parametrization

Status: [x] Complete.

A raw pair object has shared edge `e`, nonshared edges `x<y`, and four attached right triangles

```text
(e,x,u), (e,y,v), (u,y,d), (v,x,d)
```

with only three independent Pythagorean equations. The three Stage14 directions are the chamber positions

```text
a: e<x<y
b: x<e<y
c: x<y<e
```

on one common arithmetic object.

### 14-4ab — representation multiplicity and matching reduction

Status: [x] Complete.

Take two oriented primitive face data

\[
F_1=(S_1,X_1,H_1),\qquad F_2=(S_2,X_2,H_2),
\]

and put

\[
g=(S_1,S_2),\qquad \alpha=S_1/g,\qquad \beta=S_2/g.
\]

The shared-edge scale equation has the complete solution

\[
k_1=t\beta,\qquad k_2=t\alpha.
\]

The minimal gluing

\[
e_0=g\alpha\beta,\qquad x_0=\beta X_1,\qquad y_0=\alpha X_2
\]

satisfies

\[
\gcd(e_0,x_0,y_0)=1,
\]

so

\[
\boxed{\gcd(e,x,y)=t}.
\]

Thus primitive cuboids force `t=1`, while the physical face scales remain

\[
k_1=\beta,\qquad k_2=\alpha.
\]

The exact bijective raw-pair parameter space is

\[
\boxed{
\begin{aligned}
e&=\operatorname{lcm}(S_1,S_2),\\
x&=\beta X_1,\\
y&=\alpha X_2,\\
d^2&=\beta^2H_1^2+\alpha^2X_2^2,
\end{aligned}}
\]

subject to `x<y`, the exact square test for `d`, and `d<=B`.

The third Euclid triple is recovered uniquely and is not an independent parameter. Its scale is

\[
\boxed{k_3=\gcd(H_1,X_2)}.
\]

For a fixed raw pair incidence,

\[
\boxed{\text{parameter-fiber multiplicity}=1}.
\]

Independent face-pair enumeration reproduces the locked finite census at `B=1k,2k,5k,10k`.

Artifacts:

```text
stages/stage14/archive/stage14-4ab-matching-reduction.md
stages/stage14/scripts/14-4/bijection_audit.py
stages/stage14/data/14-4/bijection_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

Decision:

```text
STAGE14_4AB=COMPLETE
R03_FULL_ACCESS_AUTHORIZED=true
SHARED_EDGE_SCALE_SOLUTION_EXACT=true
GLOBAL_COMMON_SCALE_EQUALS_CUBOID_GCD=true
PRIMITIVE_COMMON_SCALE_T=1=true
MINIMAL_GLUING_AUTOMATICALLY_PRIMITIVE=true
FIXED_RAW_PAIR_PARAMETER_FIBER_MULTIPLICITY=1
THIRD_EUCLID_TRIPLE_INDEPENDENT=false
BIJECTIVE_TWO_FACE_PARAMETER_SPACE_LOCKED=true
TRUE_GROWTH_ORDER_IDENTIFIED=false
```

### 14-4ac — height inequality and arithmetic counting envelope

Status: [>] Next.

Purpose:

- rewrite `d<=B` explicitly in the two-face primitive parameters;
- isolate the roles of `g=gcd(S1,S2)`, `alpha`, `beta`, and cross-gcd `gcd(H1,X2)`;
- identify which variables create divisor/logarithmic multiplicity;
- use the full Stage13 R03 local/harmonic machinery where genuinely applicable;
- derive a rigorous counting envelope sharper than the inherited `o(B(log B)^3)` ceiling if possible;
- only then test candidate true growth orders.

## 14-5 — Directionwise asymptotic structure

Status: pending Stage14-4.

## Scope boundary

No true growth exponent, leading constant, limiting directional ratio, eventual leader, Euler-side two-face equality, or perfect-cuboid nonexistence result is yet established for Stage14.

```text
NEXT=Stage14-4ac height inequality and arithmetic counting envelope
```
