# Stage14-4ac — rational-slope height and arithmetic counting envelope

## Purpose

Stage14-4ab removed Euclid-representation multiplicity and gave a bijection between a fixed raw two-face incidence and two oriented primitive Pythagorean face data. Stage14-4ac converts that bijection into a shape/radial height formula, isolates the divisor multiplicity present before the space-diagonal square condition, and records the first growth candidate that the finite census genuinely suggests.

No true Stage14 asymptotic is proved in this substage.

## 0. Stage13 contract is now frozen for downstream use

Stage13-12ah freezes the downstream mathematical content at

```text
c843e039306b40bd3693f89d6199da78c2fb4657
```

with contract

```text
R03 + Stage13-12ag
```

and the repository records Grok `CLOSED` and Qwen `CLOSED` on R03. The planned paid-Copilot review remains `PENDING_FINAL_REVIEW`; this does not alter the frozen downstream mathematical content unless a new FATAL/MAJOR issue is found.

Stage14 may therefore use, explicitly and without the old provisional R02 quarantine,

\[
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\]

\[
O_{qr}(B)=o(B(\log B)^3),
\qquad
T(B)=o(B(\log B)^3),
\]

and hence

\[
\boxed{N_2(B)=o(B(\log B)^3)}.
\]

The fixed-local-factor lemma, exact inert local multiplier, weighted-Wiener estimates, harmonic closure and finite-order Selberg--Delange/Tauberian boundary are also available when their hypotheses match the new Stage14 coordinates.

The last displayed bound is only an inherited ceiling. It does not identify the true Stage14 order.

---

## 1. From primitive face data to rational Pythagorean slopes

Take the Stage14-4ab oriented primitive face data

\[
F_1=(S_1,X_1,H_1),
\qquad
F_2=(S_2,X_2,H_2),
\]

where `S_i` is the leg that becomes the shared cuboid edge. Define

\[
t_1:=\frac{X_1}{S_1},
\qquad
t_2:=\frac{X_2}{S_2}.
\]

Because each face datum is primitive,

\[
\gcd(S_i,X_i)=1
\]

and

\[
1+t_i^2=\left(\frac{H_i}{S_i}\right)^2.
\]

Thus `t_i` is a positive rational Pythagorean slope: a reduced positive rational for which `1+t_i^2` is a rational square.

Conversely, if

\[
t=\frac{X}{S}
\]

is reduced and `1+t^2` is a rational square, then

\[
S^2+X^2=H^2
\]

for an integer `H`, and `(S,X,H)` is a unique oriented primitive Pythagorean face datum. Therefore primitive oriented face data and positive rational Pythagorean slopes are equivalent coordinates.

Let

\[
\mathcal P
=\{t\in\mathbf Q_{>0}:1+t^2\in(\mathbf Q^\times)^2\}.
\]

---

## 2. The Stage14-4ab gluing becomes a minimal common denominator

Let

\[
L:=\operatorname{lcm}(S_1,S_2).
\]

Stage14-4ab gives

\[
e=L,
\qquad
x=\frac{L}{S_1}X_1,
\qquad
y=\frac{L}{S_2}X_2.
\]

Hence exactly

\[
\boxed{
(e,x,y)=L(1,t_1,t_2).
}
\]

The condition `x<y` is simply

\[
\boxed{t_1<t_2}.
\]

Since `L` is the least common denominator of `t_1,t_2`, the integral vector

\[
L(1,t_1,t_2)
\]

is primitive. Otherwise a common divisor of its three coordinates would allow a smaller common denominator, contradicting minimality. This is the rational-slope form of the Stage14-4ab identity `gcd(e,x,y)=1`.

The three shared-edge directions are now only the location of `1` among the two slopes:

```text
a-direction: 1 < t1 < t2
b-direction: t1 < 1 < t2
c-direction: t1 < t2 < 1
```

No separate Diophantine system exists for the three directions.

---

## 3. Exact space-diagonal height factorization

Define

\[
r_1:=\frac{H_1}{S_1}=\sqrt{1+t_1^2},
\qquad
r_2:=\frac{H_2}{S_2}=\sqrt{1+t_2^2}.
\]

Then

\[
u=Lr_1,
\qquad
v=Lr_2.
\]

The integer-space-diagonal condition becomes

\[
d^2=e^2+x^2+y^2
=L^2(1+t_1^2+t_2^2).
\]

Put

\[
R(t_1,t_2):=\sqrt{1+t_1^2+t_2^2}.
\]

Therefore

\[
\boxed{d=L R(t_1,t_2).}
\]

Because `L^2R^2` is an integer, `R` is rational if and only if `d` is integral: if `R` is rational then `LR` is a rational square root of an integer and hence is an integer.

Thus a raw Stage14 pair incidence is equivalent to

\[
(t_1,t_2)\in\mathcal P^2,
\qquad
0<t_1<t_2,
\]

with

\[
\boxed{R(t_1,t_2)\in\mathbf Q}
\]

and height

\[
\boxed{L(t_1,t_2)R(t_1,t_2)\le B},
\]

where `L` is the lcm of the reduced denominators of the two slopes.

This gives an exact rational-point counting problem rather than a heuristic parameter count.

---

## 4. A three-square rational surface

Introduce rational variables

\[
r_1,r_2,R>0.
\]

The raw-pair slope set is the positive rational locus of

\[
\boxed{
\begin{aligned}
r_1^2-t_1^2&=1,\\
r_2^2-t_2^2&=1,\\
R^2-t_1^2-t_2^2&=1.
\end{aligned}}
\]

with `0<t_1<t_2` and the lcm-denominator height `LR`.

This formulation shows exactly how Stage13 sits inside Stage14. If `(e,x,u)` is the distinguished Stage13 face, then Stage13's one-face ambient conditions are

\[
r_1^2=1+t_1^2
\]

and

\[
R^2=r_1^2+t_2^2.
\]

Stage14 adds the second-face condition

\[
\boxed{r_2^2=1+t_2^2.}
\]

So the Stage13 fixed-prime overlap squeeze is acting on a concrete additional rational-square condition on the same two shape variables; it is not an abstract independent probability model.

For exactly-two rather than raw-pair incidence, exclude the third-face square:

\[
\boxed{t_1^2+t_2^2\notin(\mathbf Q^\times)^2.}
\]

If that square is rational, the object is in the triple population `T` and must remain in the raw ledger.

---

## 5. Universal max-height sandwich

Because `0<t_1<t_2`, the largest cuboid edge is

\[
M:=L\max(1,t_2)=\max(e,y).
\]

Since

\[
d^2=e^2+x^2+y^2
\]

and all three edges are positive and at most `M`,

\[
\boxed{M<d<\sqrt3\,M.}
\]

Consequently

\[
\boxed{
M\le \frac{B}{\sqrt3}
\Longrightarrow d\le B
\Longrightarrow M<B.
}
\]

Thus the Euclidean height is trapped, up to a universal constant, by the max-height

\[
L\max(1,t_2).
\]

By chamber:

```text
a: 1<t1<t2   -> M=L t2=y
b: t1<1<t2   -> M=L t2=y
c: t1<t2<1   -> M=L=e
```

This separation will matter later for directional constants, but Stage14-4ac makes no directional asymptotic claim.

The main use in Stage14-4 is that a power/log growth order, once proved for one of these comparable height functions with uniform control, cannot be an artifact of the curved Euclidean boundary alone.

---

## 6. Exact multiplicity of primitive faces with prescribed shared leg

Let

\[
a(S)
\]

denote the number of oriented primitive Pythagorean face data `(S,X,H)` with `S` as distinguished leg.

Then

\[
\boxed{
a(S)=
\begin{cases}
0,&S\le1,\\
0,&S\equiv2\pmod4,\\
2^{\omega(S)-1},&\text{otherwise},
\end{cases}}
\]

where `omega(S)` is the number of distinct prime factors.

### 6.1 Odd shared leg

For odd `S`, the shared leg is the difference leg

\[
S=m^2-n^2=(m-n)(m+n).
\]

In a primitive Euclid triple, `m-n` and `m+n` are positive odd coprime factors. Every prime-power divisor of `S` must therefore be assigned wholly to one of the two factors. Up to swapping the factors there are

\[
2^{\omega(S)-1}
\]

assignments.

### 6.2 Even shared leg

A primitive even leg is divisible by `4`; no primitive leg is `2 mod 4`. Write

\[
S=2mn
\]

with `(m,n)=1` and opposite parity. Again each odd prime power belongs wholly to one of the coprime Euclid parameters, while the entire 2-power belongs to the even one. The resulting count is again

\[
2^{\omega(S)-1}.
\]

The deterministic audit verifies this formula for every `1<=S<=1000` with zero mismatches.

This is the first exact explanation of the divisor/logarithmic multiplicity visible in the Stage14 face-pair coordinates.

---

## 7. What happens before the space-diagonal square condition

To measure how large the raw face-pair denominator space is, temporarily ignore:

- `t_1<t_2`;
- the shape factor `R`;
- the condition `R in Q`.

Consider only

\[
E(B)
:=\sum_{\operatorname{lcm}(S_1,S_2)\le B}
a(S_1)a(S_2).
\]

This is **not** the Stage14 population. It is a pre-space-diagonal arithmetic envelope.

Use the multiplicative majorant

\[
c(n):=2^{\omega(n)}.
\]

For one prime `p`, `c(p^0)=1` and `c(p^j)=2` for every `j>=1`. Put `x=p^{-s}`. If `max(i,j)=k>=1`, the total local weight is

\[
(1+2k)^2-(1+2(k-1))^2=8k.
\]

Hence the exact local lcm-pair series is

\[
\boxed{
F_p(s)
=1+\sum_{k\ge1}8k x^k
=1+\frac{8x}{(1-x)^2}.
}
\]

In particular

\[
F_p(s)=1+8p^{-s}+O(p^{-2\Re s}).
\]

Thus

\[
\prod_pF_p(s)=\zeta(s)^8G(s),
\]

with `G` holomorphic in a half-plane past `1` at the standard finite-order Selberg--Delange level. The admissibility restriction `S not congruent 2 mod 4` changes only the 2-adic local factor, and `a(S)=c(S)/2` on every admissible `S>1`; the exceptional `S=1` boundary is lower-dimensional.

Therefore the pre-space lcm envelope has scale

\[
\boxed{E(B)\asymp B(\log B)^7}
\]

and in fact admits a positive-constant `B(log B)^7` asymptotic under the same standard finite-order Selberg--Delange theorem boundary. Stage14-4ac does not need or evaluate that constant.

This result is intentionally an envelope, not a prediction for the actual integer-space-diagonal population.

---

## 8. Why the Stage13 map matters so much

The naive two-face denominator envelope is at `B(log B)^7` scale before the space-diagonal square condition. An analysis that began from those two face denominators alone would therefore have to discover a very severe arithmetic thinning mechanism from scratch.

Stage13 R03 has already analyzed the one-face-plus-space-diagonal ambient family and the second-face local obstruction. Its frozen contract gives directly

\[
\boxed{N_2(B)=o(B(\log B)^3).}
\]

So Stage13 replaces a very weak `B(log B)^7` face-pair envelope by a meaningful zero-density statement inside the correct `B(log B)^3` integer-space-diagonal ambient scale.

This is precisely why opening the Stage13 map materially changes Stage14-4.

But R03 still does **not** give the true Stage14 rate. Its pair-overlap squeeze works by:

```text
fix k inert primes
B -> infinity
then k -> infinity
```

and proves zero density without choosing `k=k(B)`. It therefore supplies `little-o`, not a quantitative power or logarithmic saving. A true Stage14 order requires additional global information.

---

## 9. Finite growth clue: sqrt(B)

Stage14-3 deliberately did not fit an asymptotic law. Stage14-4 is now the growth-order stage, so it is appropriate to record candidate diagnostics while keeping them separate from theorems.

For the frozen exactly-two total,

```text
B          N2       N2/sqrt(B)
200,000    116      0.2593838854
500,000    188      0.2658721497
1,000,000  255      0.2550000000
2,000,000  356      0.2517300141
```

On these four late cutoffs the mean is

```text
0.2579965123
```

with population coefficient of variation about

```text
0.02053
```

or two percent.

The local pure-power effective exponents remain noisy:

```text
100k -> 200k   0.38225
200k -> 500k   0.52696
500k -> 1m     0.43976
1m   -> 2m     0.48138
```

Therefore Stage14-4ac records only:

\[
\boxed{\sqrt B\text{ is a high-priority finite candidate to test next}.}
\]

It does **not** record

\[
N_2(B)\sim C\sqrt B
\]

or any `sqrt(B)` upper/lower bound as a theorem.

The stability is strong enough to determine the next experiment/proof target, not strong enough to determine the answer.

---

## 10. Independent deterministic audit

New audit:

```text
stages/stage14/scripts/14-4/height_envelope_audit.py
stages/stage14/data/14-4/height_envelope_audit.json
```

It checks:

1. the exact formula for `a(S)` for every `S<=1000`;
2. the slope identities using integer cross-products only;
3. the max-height sandwich on every accepted face-pair incidence in the independent `B=10000` face-pair census;
4. reproduction of `(9,11,5)` with `T=0` at `B=10000`;
5. the exact lcm-majorant local coefficient `8k` and local factor `1+8x/(1-x)^2`;
6. the frozen `N2/sqrt(B)` diagnostic.

No floating-point square decision enters the census audit.

---

## 11. Stage14-4ac decision

Locked conclusions:

```text
STAGE14_4AC=COMPLETE
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
STAGE13_DOWNSTREAM_MATHEMATICAL_CONTENT=FROZEN
RATIONAL_SLOPE_HEIGHT_FACTORIZATION_LOCKED=true
RAW_PAIR_RATIONAL_SURFACE_LOCKED=true
UNIVERSAL_MAX_HEIGHT_SANDWICH_LOCKED=true
PRIMITIVE_FACE_MULTIPLICITY_FORMULA_LOCKED=true
PRE_SPACE_LCM_ENVELOPE_POLE_ORDER=8
PRE_SPACE_LCM_ENVELOPE_SCALE=B(log B)^7
R03_PAIR_CEILING_ACTIVE=o(B(log B)^3)
TRUE_GROWTH_ORDER_IDENTIFIED=false
SQRT_B_ASYMPTOTIC_CLAIM=false
SQRT_B_FINITE_CANDIDATE_PRIORITY=HIGH
```

## 12. Next — Stage14-4ad

The remaining hard question is now sharply isolated.

In R03 ambient coordinates, Stage14 adds the global square condition

\[
1+t_2^2\in(\mathbf Q^\times)^2.
\]

R03 proves this condition has zero density at the `B(log B)^3` scale, but not its quantitative thinning rate.

Stage14-4ad should therefore compare two routes:

1. **quantitative R03-side sieve:** determine whether the fixed-prime local machinery can be upgraded, without an illegal growing-modulus step, to a rate strong enough to test `sqrt(B)`;
2. **intrinsic rational-surface route:** analyze rational points on the three-square surface with lcm-denominator height and test whether a `B^(1/2)` law is geometrically/arithmeticly plausible.

No choice between those routes is assumed in advance.

```text
NEXT=Stage14-4ad quantitative square-condition thinning and sqrt(B) test
```
