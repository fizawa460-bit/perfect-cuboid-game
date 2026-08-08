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

## Frozen Stage13 upstream contract

Stage13-12ah freezes the downstream mathematical content at

```text
c843e039306b40bd3693f89d6199da78c2fb4657
```

with contract

```text
R03 + Stage13-12ag
```

and review record

```text
R03 Grok    = CLOSED
R03 Qwen    = CLOSED
R03 Claude  = NOT_RECORDED
R03 Copilot = PENDING_FINAL_REVIEW
```

Stage14 may use the frozen raw directional theorem, fixed-local-factor machinery, exact inert local state, quantitative harmonic closure, and pair/triple lower-order theorem.

Hence

\[
\boxed{N_2(B)=o(B(\log B)^3)}
\]

is an active upstream ceiling, not the true Stage14 order.

## 14-4 — True total growth order

Status: [>] Active.

### 14-4aa — independent two-face parametrization

Status: [x] Complete.

A raw pair object has one shared edge `e`, nonshared edges `x<y`, and four attached integer right triangles. The three directions are only the three chamber positions of `e`.

### 14-4ab — exact matching bijection

Status: [x] Complete.

For oriented primitive face data

\[
F_i=(S_i,X_i,H_i)
\]

with `S_i` designated as the shared leg, put

\[
g=(S_1,S_2),\qquad \alpha=S_1/g,\qquad \beta=S_2/g.
\]

The shared-edge scale equation has complete solution

\[
k_1=t\beta,\qquad k_2=t\alpha,
\]

and the global cuboid gcd is exactly `t`; primitive cuboids force `t=1`.

Therefore a fixed raw pair incidence is represented exactly once by

\[
\boxed{
\begin{aligned}
e&=\operatorname{lcm}(S_1,S_2),\\
x&=\beta X_1,\\
y&=\alpha X_2,\\
d^2&=\beta^2H_1^2+\alpha^2X_2^2,
\end{aligned}}
\]

with `x<y`, square `d`, and `d<=B`.

### 14-4ac — rational-slope height and arithmetic envelope

Status: [x] Complete.

Define the two primitive Pythagorean slopes

\[
t_1=X_1/S_1,\qquad t_2=X_2/S_2,
\]

and

\[
L=\operatorname{lcm}(S_1,S_2).
\]

Then the bijection becomes

\[
\boxed{(e,x,y)=L(1,t_1,t_2)}
\]

and

\[
\boxed{d=L\sqrt{1+t_1^2+t_2^2}}.
\]

The raw pair locus is the rational three-square system

\[
1+t_1^2=r_1^2,
\qquad
1+t_2^2=r_2^2,
\qquad
1+t_1^2+t_2^2=R^2,
\]

with `0<t1<t2`. Exactly-two excludes `t1^2+t2^2` being a rational square.

Direction chambers are

```text
a: 1<t1<t2
b: t1<1<t2
c: t1<t2<1
```

and with

\[
M=L\max(1,t_2)
\]

we have the universal height sandwich

\[
\boxed{M<d<\sqrt3 M}.
\]

The exact primitive-face multiplicity for a prescribed shared leg is

\[
\boxed{
a(S)=
\begin{cases}
0,&S\le1\text{ or }S\equiv2\pmod4,\\
2^{\omega(S)-1},&\text{otherwise}.
\end{cases}}
\]

The pre-space lcm denominator envelope has pole order `8`, hence standard Selberg--Delange scale

\[
B(\log B)^7.
\]

This is only an envelope before the space-square condition. R03 supplies the much sharper actual pair ceiling `o(B(log B)^3)`.

Finite growth diagnostic:

```text
B          N2/sqrt(B)
200k       0.2593838854
500k       0.2658721497
1m         0.2550000000
2m         0.2517300141
```

The late-range coefficient of variation is about `2.05%`. Therefore `sqrt(B)` is promoted only to a **high-priority candidate to test**, not to a theorem.

Artifacts:

```text
stages/stage14/archive/stage14-4ac-height-envelope.md
stages/stage14/scripts/14-4/height_envelope_audit.py
stages/stage14/data/14-4/height_envelope_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

Decision:

```text
STAGE14_4AC=COMPLETE
STAGE13_DOWNSTREAM_MATHEMATICAL_CONTENT=FROZEN
RATIONAL_SLOPE_HEIGHT_FACTORIZATION_LOCKED=true
RAW_PAIR_RATIONAL_SURFACE_LOCKED=true
UNIVERSAL_MAX_HEIGHT_SANDWICH_LOCKED=true
PRIMITIVE_FACE_MULTIPLICITY_FORMULA_LOCKED=true
PRE_SPACE_LCM_ENVELOPE_POLE_ORDER=8
R03_PAIR_CEILING_ACTIVE=true
TRUE_GROWTH_ORDER_IDENTIFIED=false
SQRT_B_ASYMPTOTIC_CLAIM=false
SQRT_B_FINITE_CANDIDATE_PRIORITY=HIGH
```

### 14-4ad — quantitative square-condition thinning / sqrt(B) test

Status: [>] Next.

Purpose:

- work inside the frozen Stage13 R03 one-face-plus-space-diagonal ambient family;
- isolate the added second-face rational-square condition `1+t2^2=square`;
- determine whether R03's fixed-prime zero-density squeeze can be upgraded quantitatively without an illegal growing-modulus step;
- in parallel, analyze the intrinsic rational three-square surface with lcm-denominator height;
- attempt a rigorous upper/lower envelope at or around `B^(1/2)`;
- reject `sqrt(B)` if the arithmetic structure contradicts it rather than fitting the finite table by force.

## 14-5 — Directionwise asymptotic structure

Status: pending Stage14-4.

## Scope boundary

No true growth exponent, leading constant, limiting directional ratio, eventual leader, Euler-side two-face equality, or perfect-cuboid nonexistence result is yet established for Stage14.

```text
NEXT=Stage14-4ad quantitative square-condition thinning and sqrt(B) test
```
