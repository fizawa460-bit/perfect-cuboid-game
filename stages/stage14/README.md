# Stage14 — exactly-two integral-face population

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1=COMPLETE
STAGE14_2=COMPLETE
STAGE14_3=COMPLETE
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
STAGE14_4AC=COMPLETE
STAGE14_4AD=COMPLETE
STAGE14_4AE=COMPLETE
STAGE14_4AF=COMPLETE
STAGE14_4AG=COMPLETE
STAGE14_4AH=COMPLETE
STAGE14_4AI=COMPLETE_MINIMAL_BISECTION_REDUCTION
STAGE14_4AJ=COMPLETE_SHIMADA_LATTICE_INTERFACE
STAGE14_4AK=COMPLETE_SPLIT_ROOT_COSET_VOID
STAGE14_4AL=COMPLETE_COLLECTIVE_ACTIVATION_MEASURE_AND_FINITE_FIRST_HIT_PROFILE
MAX_VERIFIED_B=2000000
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
PHYSICAL_LINE_BUNDLE=M=pi^*(-K_Y)
PHYSICAL_POLARIZATION_SQUARE=8
RAW_PAIR_AND_ACTIVE_VERTEX_POWER_EXPONENT_EQUAL=true
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
COLLECTIVE_FIRST_HIT_IDENTITY_LOCKED=true
SQRTB_EQUIVALENT_TO_INVERSE_SQRT_ACTIVATION_DENSITY=true
POSITIVE_RANK_DENSITY_PROVED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-4am uniform arithmetic lower-tail statement for mu(F)
```

Canonical source: `stages/stage14/main.md`. Detailed derivations are frozen in the stage archive.

## Locked population

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

The exact ledgers satisfy

\[
\boxed{E(B)=O_{\rm pair}^{raw}(B)=N_2(B)+3T(B)}.
\]

At `B=2,000,000`, two independent exact generation routes give

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,\qquad T=0.
\]

The finite zero triple census is not a perfect-cuboid nonexistence theorem.

## Kummer and physical height

For Pythagorean half-angle parameters `r,s`, the raw pair surface is

\[
\boxed{Z^2=(1+r^2)^2(1+s^2)^2-16r^2s^2}.
\]

Over `Q(i)` it is the level-4 modular elliptic K3; over `C` it is `Km(E_i x E_i)`. On the toric compactification

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\qquad L=-K_Y,
\]

the resolved double cover `pi:X->Y` has physical polarization

\[
\boxed{M=\pi^*L},\qquad \boxed{M^2=8},\qquad \boxed{H_M=d}.
\]

Thus the original cuboid cutoff is the exact Kummer `M`-height.

## Fixed-curve path is closed

Stage14-4ah through 4ai shows that a fixed physical rational curve capable of a `sqrt(B)` exponent must be an `M`-degree-four bisection. All connected degree-two image and arithmetic-genus-zero splitting/contact mechanisms are eliminated; the only remaining candidate was a split singular anticanonical member.

Stage14-4aj identifies the deck involution on

\[
E_t:y^2=x(x-1)(x+t^2)
\]

as `delta(P)=(0,0)-P`. For a hypothetical last split component, `x=2C-M` must satisfy

\[
\delta(x)=-x,\qquad x^2=-16,\qquad x\equiv M\pmod2.
\]

Stage14-4ak consumes Shimada's official level-4 computation data. The relevant deck anti-invariant NS lattice has rank `6`, positive-form determinant `256`, and `1020` norm-16 vectors, but the required parity coset is empty. PARI/Fincke--Pohst and an independent exact rational-LDL enumeration agree.

Therefore

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=true
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

The finite square-root signal, if asymptotic, must be collective rather than a finite collection of fixed accumulating curves.

## Stage14-4al — collective activation measure

For each primitive oriented Pythagorean first-face base

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

define `mu(F)` as the least physical Stage14 space-diagonal height among all partners of `F`, and infinity if none exists. Then

\[
\boxed{V(B)=\#\{F:\mu(F)\le B\}}.
\]

Let `A(B)` count all primitive oriented Pythagorean bases with `H<=B`. Euclid-parameter counting gives

\[
\boxed{A(B)=B/\pi+O(\sqrt B\log B)}.
\]

Hence any eventual square-root active-vertex law is exactly equivalent to inverse-square-root activation density:

\[
\boxed{V(B)\sim c\sqrt B
\iff V(B)/A(B)\sim \pi c/\sqrt B}.
\]

This is a reformulation, not an asymptotic theorem.

The exact late finite profile is

```text
B          A(B)      V(B)      sqrt(B)*V/A
200,000     63,638      155       1.0892565339
500,000    159,164      254       1.1284280517
1,000,000  318,278      347       1.0902418640
2,000,000  636,640      490       1.0884717353
```

Over `200k -> 2m`, the effective exponents are `1.0001774` for `A`, `0.4998644` for `V`, and `-0.5003130` for `V/A`. The scaled activation `sqrt(B)V/A` has mean `1.09910` and coefficient of variation about `1.54%` on the four late cutoffs. These are finite diagnostics only.

The signal is not concentrated in one exact-rank type: at `2m`, the active census contains `254` exact-rank-1 and `188` exact-rank-2 fibers. Stage14-s4a/b also records `483/490` distinct exact Kummer square-class triples and `393` coarse arithmetic signatures, largest coarse cluster `4`.

The first-small-point gate is quantitatively substantial. At `2m`, `mu(F)/H(F)` has median `21.03`, 75th percentile `98.23`, and maximum about `1.15e4`. Positive rank therefore cannot simply be identified with a physical hit near the base height.

## What remains

The main count is now organized as the moving joint gate

\[
V(B)=\sum_{\substack{F\text{ primitive oriented}\\H(F)\le B}}
1_{\{\operatorname{rank}E_F(\mathbf Q)>0\}}
1_{\{\mu(F)\le B\}}.
\]

Stage14-4am must obtain a uniform arithmetic lower-tail statement separating positive-rank frequency from the conditional frequency of a sufficiently small first physical point. It must not identify Selmer rank with Mordell--Weil rank or first hit with a shortest generator without proof.

The independent triple track still must control

\[
T(B)=o(\sqrt B)
\]

before a future raw-pair square-root law could transfer to exactly-two.

## Primary current artifacts

```text
stages/stage14/archive/stage14-4ak-shimada-split-root-void.md
stages/stage14/archive/stage14-4al-collective-first-hit.md
stages/stage14/data/14-4/shimada_stage14_4ak_result.json
stages/stage14/data/14-4/collective_first_hit_summary.json
stages/stage14/scripts/14-4/collective_first_hit_audit.py
.github/workflows/stage14-4al-collective-first-hit.yml
```
