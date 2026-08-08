# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_4AC_COMPLETE_SQRT_B_CANDIDATE_14_4AD_NEXT`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals. Stage14-1 through Stage14-3 are complete. Stage14-4 is active at proof level. Stage13 is now frozen for downstream use at the R03 + 13-12ag contract, while the Stage14 two-face coordinates are independently derived.

## §1. Locked counting convention

For `B>=1`, count positive integers satisfying

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

Let

\[
I_{ab}=\mathbf1_{a^2+b^2=\square},\quad
I_{ac}=\mathbf1_{a^2+c^2=\square},\quad
I_{bc}=\mathbf1_{b^2+c^2=\square}.
\]

The raw pair populations are

\[
O_{ab,ac}=\sum I_{ab}I_{ac},\quad
O_{ab,bc}=\sum I_{ab}I_{bc},\quad
O_{ac,bc}=\sum I_{ac}I_{bc},
\]

and the triple population is

\[
T=\sum I_{ab}I_{ac}I_{bc}.
\]

The exactly-two directional populations are

\[
N_a^{(2)}=O_{ab,ac}-T,
\qquad
N_b^{(2)}=O_{ab,bc}-T,
\qquad
N_c^{(2)}=O_{ac,bc}-T,
\]

where

```text
a = ab+ac only = smallest shared edge
b = ab+bc only = middle shared edge
c = ac+bc only = largest shared edge
```

and

\[
N_2=N_a^{(2)}+N_b^{(2)}+N_c^{(2)}.
\]

No perfect-cuboid nonexistence assumption is made. Any `T>0` object remains an exact perfect-cuboid candidate and must be retained.

## §2. Frozen finite facts

Two materially different exact cuboid-generation routes agree at all 11 audited cutoffs through `B=2,000,000`. At the verified ceiling,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,
\qquad T=0.
\]

Stage14-3 established only finite directional geography. No limiting ratio or monotonicity theorem was inferred.

Canonical finite synthesis:

```text
stages/stage14/data/14-3/final_finite_reconnaissance.json
stages/stage14/archive/stage14-3c-final-finite-reconnaissance.md
```

## §3. Frozen Stage13 upstream contract

Stage13-12ah freezes the downstream mathematical content at

```text
c843e039306b40bd3693f89d6199da78c2fb4657
```

with contract

```text
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
STAGE13_DOWNSTREAM_MATHEMATICAL_CONTENT=FROZEN
```

and review record

```text
R03 Grok    = CLOSED
R03 Qwen    = CLOSED
R03 Claude  = NOT_RECORDED
R03 Copilot = PENDING_FINAL_REVIEW
```

The pending Copilot verdict is review bookkeeping unless it finds a new FATAL/MAJOR mathematical issue.

Stage14 may use the frozen raw directional theorem, fixed-local-factor transfer, exact inert-prime local states and multiplier, weighted-Wiener/harmonic closure, and pair/triple lower-order theorem.

In particular,

\[
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\]

\[
O_{qr}(B)=o(B(\log B)^3),
\qquad
T(B)=o(B(\log B)^3),
\]

so

\[
\boxed{
N_a^{(2)},N_b^{(2)},N_c^{(2)},N_2=o(B(\log B)^3).
}
\]

This is an inherited ceiling, not the true Stage14 order.

## §4. Stage14-4aa/4ab — exact two-face incidence coordinates

Let `e` be the edge shared by the two integral faces and let `x<y` be the nonshared edges. With face diagonals `u,v`, a raw pair incidence satisfies

\[
e^2+x^2=u^2,
\qquad
e^2+y^2=v^2,
\qquad
u^2+y^2=d^2,
\qquad
v^2+x^2=d^2.
\]

Only three Pythagorean equations are independent.

The three directions are only the chamber positions of `e`:

```text
a: e<x<y
b: x<e<y
c: x<y<e
```

Take two oriented primitive Pythagorean face data

\[
F_1=(S_1,X_1,H_1),
\qquad
F_2=(S_2,X_2,H_2),
\]

where `S_i` is the leg designated to become the shared edge. Put

\[
g=\gcd(S_1,S_2),
\qquad
\alpha=S_1/g,
\qquad
\beta=S_2/g.
\]

The complete shared-edge scale solution is

\[
k_1=t\beta,
\qquad
k_2=t\alpha.
\]

Stage14-4ab proves

\[
\gcd(g\alpha\beta,\beta X_1,\alpha X_2)=1,
\]

hence for the physical glued cuboid

\[
\boxed{\gcd(e,x,y)=t}.
\]

Global primitivity therefore forces exactly

\[
\boxed{t=1},
\]

while the actual face scales remain `k_1=beta`, `k_2=alpha` and need not be one.

Thus the primitive raw pair incidence is obtained bijectively from the two face data by

\[
\boxed{
\begin{aligned}
e&=\operatorname{lcm}(S_1,S_2)=g\alpha\beta,\\
x&=\beta X_1,\\
y&=\alpha X_2,\\
u&=\beta H_1,\\
v&=\alpha H_2,\\
d^2&=\beta^2H_1^2+\alpha^2X_2^2.
\end{aligned}}
\]

The convention `x<y` removes the face swap, and the parameter-fiber multiplicity of a fixed raw pair incidence is exactly `1`.

The third Euclid triple introduced in Stage14-4aa is not independent; if the space-square condition holds, its scale is recovered uniquely as

\[
\boxed{k_3=\gcd(H_1,X_2)}.
\]

Independent face-pair enumeration reproduces the locked counts through `B=10000`.

## §5. Stage14-4ac — rational-slope factorization

### §5.1 Primitive Pythagorean slopes

Define

\[
t_1:=\frac{X_1}{S_1},
\qquad
t_2:=\frac{X_2}{S_2}.
\]

Each `t_i` is reduced and satisfies

\[
1+t_i^2=\left(\frac{H_i}{S_i}\right)^2.
\]

Conversely every positive reduced rational `t` for which `1+t^2` is a rational square determines a unique oriented primitive Pythagorean face datum.

Let

\[
\mathcal P
=\{t\in\mathbf Q_{>0}:1+t^2\in(\mathbf Q^\times)^2\}.
\]

### §5.2 Minimal common denominator

Put

\[
L:=\operatorname{lcm}(S_1,S_2).
\]

Then the Stage14-4ab gluing becomes exactly

\[
\boxed{(e,x,y)=L(1,t_1,t_2)}.
\]

The condition `x<y` is simply

\[
\boxed{t_1<t_2}.
\]

Because `L` is the least common denominator of `t_1,t_2`, the integral vector `L(1,t_1,t_2)` is primitive.

The direction label becomes

```text
a: 1<t1<t2
b: t1<1<t2
c: t1<t2<1
```

on one common arithmetic set.

### §5.3 Exact space height

Define

\[
R(t_1,t_2):=\sqrt{1+t_1^2+t_2^2}.
\]

Then

\[
\boxed{d=L R(t_1,t_2)}.
\]

Since `L^2R^2=e^2+x^2+y^2` is an integer, `R` is rational if and only if `d` is integral.

Therefore a raw Stage14 pair incidence is equivalent to

\[
(t_1,t_2)\in\mathcal P^2,
\qquad
0<t_1<t_2,
\qquad
R(t_1,t_2)\in\mathbf Q,
\]

with height

\[
\boxed{L(t_1,t_2)R(t_1,t_2)\le B}.
\]

The raw-pair rational locus may be written as

\[
\boxed{
\begin{aligned}
r_1^2-t_1^2&=1,\\
r_2^2-t_2^2&=1,\\
R^2-t_1^2-t_2^2&=1.
\end{aligned}}
\]

Exactly-two additionally excludes

\[
\boxed{t_1^2+t_2^2\in(\mathbf Q^\times)^2},
\]

which is precisely the triple-face condition.

### §5.4 Exact relation to Stage13

Choose `(e,x,u)` as the distinguished Stage13 face. In slope variables, the Stage13 one-face-plus-space-diagonal ambient family is

\[
r_1^2=1+t_1^2,
\qquad
R^2=r_1^2+t_2^2.
\]

Stage14 adds the second-face condition

\[
\boxed{r_2^2=1+t_2^2}.
\]

Thus the R03 fixed-prime overlap sieve is a local analysis of this concrete extra rational-square condition. Stage14 does not model it as an independent random event.

## §6. Universal height envelope

Because `0<t_1<t_2`, the largest cuboid edge is

\[
M:=L\max(1,t_2)=\max(e,y).
\]

Since all three positive edges are at most `M`,

\[
\boxed{M<d<\sqrt3\,M}.
\]

Hence

\[
\boxed{
M\le B/\sqrt3
\Longrightarrow d\le B
\Longrightarrow M<B.
}
\]

By direction,

```text
a: M=L t2=y
b: M=L t2=y
c: M=L=e
```

so the curved Euclidean height is comparable to a simple max-height independently of the arithmetic square condition.

## §7. Exact primitive-face multiplicity

Let `a(S)` be the number of oriented primitive Pythagorean face data whose distinguished shared leg equals `S`.

Stage14-4ac proves

\[
\boxed{
a(S)=
\begin{cases}
0,&S\le1,\\
0,&S\equiv2\pmod4,\\
2^{\omega(S)-1},&\text{otherwise}.
\end{cases}}
\]

For odd `S`, this is the coprime factor split of

\[
S=(m-n)(m+n).
\]

For even `S`, primitive Pythagorean parity requires `4|S`, and the odd prime powers are distributed between the coprime Euclid parameters while the full 2-power remains on the even parameter.

The deterministic audit verifies the formula for every `S<=1000` with zero mismatches.

## §8. Pre-space lcm denominator envelope

Temporarily ignore slope ordering, the shape factor and the space-square condition, and define

\[
E(B)
=\sum_{\operatorname{lcm}(S_1,S_2)\le B}a(S_1)a(S_2).
\]

This is **not** the Stage14 population. It measures only how large the two-face denominator space is before the integer-space-diagonal condition.

For the multiplicative majorant

\[
c(n)=2^{\omega(n)},
\]

one prime contributes, with `x=p^{-s}`,

\[
\boxed{
F_p(s)
=1+\sum_{k\ge1}8k x^k
=1+\frac{8x}{(1-x)^2}.
}
\]

Indeed the total weight with local exponents at most `k` is `(1+2k)^2`, so the weight with exact maximum `k` is `8k`.

Thus

\[
F_p(s)=1+8p^{-s}+O(p^{-2\Re s})
\]

and the global lcm-pair Dirichlet series has pole order `8` at `s=1`. The admissibility restriction `S not congruent 2 mod 4` changes only the 2-adic factor, while `a(S)=c(S)/2` on admissible `S>1`.

At the standard finite-order Selberg--Delange theorem boundary this gives

\[
\boxed{E(B)\asymp B(\log B)^7},
\]

indeed with a positive leading constant that is not needed here.

This enormous pre-space envelope is why the frozen Stage13 map is valuable. R03 immediately places the genuine integer-space-diagonal pair population at

\[
\boxed{o(B(\log B)^3)},
\]

whereas starting from the two face denominators alone leaves a `B(log B)^7` forest to thin.

R03 does not, however, identify the true thinning rate: its fixed-prime argument takes fixed `k`, then `B->infinity`, then `k->infinity`, and therefore proves zero density rather than an explicit power/log saving.

## §9. First growth candidate: sqrt(B)

Stage14-3 deliberately did not fit a growth law. Stage14-4 is the growth-order stage, so finite candidate diagnostics are now admissible provided they are not promoted to theorems.

The frozen totals give

```text
B          N2       N2/sqrt(B)
200,000    116      0.2593838854
500,000    188      0.2658721497
1,000,000  255      0.2550000000
2,000,000  356      0.2517300141
```

Across these four late cutoffs,

```text
mean N2/sqrt(B) = 0.2579965123
coefficient of variation = 0.0205281
```

The local pure-power effective exponents remain noisy, ranging from about `0.38` to `0.53` on the late coarse intervals.

Therefore the only locked conclusion is

\[
\boxed{\sqrt B\text{ is a high-priority finite candidate for Stage14-4ad}.}
\]

Stage14-4ac does **not** claim

\[
N_2(B)\sim C\sqrt B
\]

or any rigorous `sqrt(B)` upper or lower bound.

## §10. Stage14-4ac audit artifacts

```text
stages/stage14/archive/stage14-4ac-height-envelope.md
stages/stage14/scripts/14-4/height_envelope_audit.py
stages/stage14/data/14-4/height_envelope_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

The audit checks:

- the exact shared-leg multiplicity formula through `S=1000`;
- the slope/height identities using integer cross-products;
- the max-height sandwich on every accepted `B=10000` independent face-pair incidence;
- reproduction of `(9,11,5)` and `T=0` at `B=10000`;
- the exact lcm-majorant local coefficient `8k`;
- the frozen `N_2/sqrt(B)` diagnostic.

## §11. Locked Stage14-4ac decision

```text
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
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
LEADING_CONSTANT_IDENTIFIED=false
SQRT_B_ASYMPTOTIC_CLAIM=false
SQRT_B_FINITE_CANDIDATE_PRIORITY=HIGH
```

## §12. Next — Stage14-4ad

The hard problem is now isolated to the quantitative thinning produced by the added second-face rational-square condition inside the frozen R03 one-face ambient family.

Stage14-4ad will test two routes in parallel:

```text
R03-side:
  can the fixed-prime local machinery yield a quantitative rate without an
  illegal growing-modulus step?

Stage14-native:
  can rational points on the three-square surface with lcm-denominator height
  be counted sharply enough to prove or reject a sqrt(B) scale?
```

No route or answer is assumed in advance.

```text
NEXT=Stage14-4ad quantitative square-condition thinning and sqrt(B) test
```
