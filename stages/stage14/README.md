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
STAGE14_4AM=COMPLETE_EXACT_SELMER_RANK_SMALLPOINT_FACTOR_AND_FINITE_FULL_BASE_CENSUS
MAX_VERIFIED_B=2000000
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
PHYSICAL_LINE_BUNDLE=M=pi^*(-K_Y)
PHYSICAL_POLARIZATION_SQUARE=8
RAW_PAIR_AND_ACTIVE_VERTEX_POWER_EXPONENT_EQUAL=true
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
COLLECTIVE_FIRST_HIT_IDENTITY_LOCKED=true
SQRTB_EQUIVALENT_TO_INVERSE_SQRT_ACTIVATION_DENSITY=true
ACTIVATION_DENSITY_THREE_GATE_FACTORIZATION_LOCKED=true
FULL_BASE_RANK_SELMER_CENSUS_MAX_H=20000
FINITE_FIRST_SMALL_POINT_GATE_DOMINATES_THINNING_BUDGET=true
POSITIVE_RANK_DENSITY_PROVED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-4an Euclid-factor reciprocity matrix coupled to height-sensitive activation
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

The late finite profile is

```text
B          A(B)      V(B)      sqrt(B)*V/A
200,000     63,638      155       1.0892565339
500,000    159,164      254       1.1284280517
1,000,000  318,278      347       1.0902418640
2,000,000  636,640      490       1.0884717353
```

Over `200k -> 2m`, the effective exponents are `1.0001774` for `A`, `0.4998644` for `V`, and `-0.5003130` for `V/A`. The scaled activation `sqrt(B)V/A` has coefficient of variation about `1.54%`. These are finite diagnostics only.

## Stage14-4am — where the activation thinning occurs

For the integral full-2-torsion fiber

\[
E_F:\quad Y^2=Z(Z-S^2)(Z+X^2),
\]

define

```text
A(B)      = all primitive oriented bases with H<=B
Sigma(B)  = bases with dim Sel_2(E_F)>2
R(B)      = bases with rank E_F(Q)>0
V(B)      = bases with mu(F)<=B
```

Then exactly

\[
\boxed{V(B)\subset R(B)\subset\Sigma(B)\subset A(B)}
\]

and

\[
\boxed{
\frac{V}{A}=\frac{\Sigma}{A}\frac{R}{\Sigma}\frac{V}{R}.
}
\]

Thus a hypothetical square-root activation law has an exact thinning budget: because `A(B)=B^{1+o(1)}`, the Selmer, MW-rank-given-Selmer, and first-hit-given-rank exponents must sum to `1/2` if `V(B)=B^{1/2+o(1)}`.

Stage14-4am runs PARI/GP `ellrank(E,0)` on **every** primitive oriented Pythagorean base through `H<=20,000`, replacing the old s1 matched-control sample by a complete finite base census.

```text
B        A       Sigma      R interval       V
2,000      638      476       371..385         7
5,000     1584     1234       916..989        25
10,000    3186     2553      1875..2057       39
20,000    6372     5209      3784..4239       54
```

At `B=20,000`:

```text
Sigma/A          = 0.8174827369742624
R/A              in [0.5938480853735091, 0.6652542372881356]
V/R              in [0.012738853503184714, 0.01427061310782241]
V/A              = 0.00847457627118644
```

The corresponding finite exponent budget is

```text
gamma(total)                   = 0.4817176373
alpha_Selmer                   = 0.02034894195
alpha_MW | Selmer              in [0.02080686276, 0.03227209060]
beta_first-hit | MW            in [0.4290966047, 0.4405618326]
```

The interval endpoints are correlated through the unknown exact `R(B)` and must not be combined independently. No asymptotic conclusion is drawn from them.

The finite structural result is nevertheless clear: nontrivial 2-Selmer occurs on about `82%` of the audited bases, and positive Mordell--Weil rank on between about `59%` and `67%`, while physical activation among positive-rank fibers is only about `1.3–1.4%` at `20k`. On this complete finite family, most observed thinning therefore occurs **after positive rank**, at the height-sensitive first-small-point gate.

This refines the s5a program. In Euclid parameters

```text
S=m^2-n^2
X=2mn
H=m^2+n^2
```

the moving 2-descent support lies on

```text
m, n, m-n, m+n, m^2+n^2
```

plus `2`. A local character/reciprocity matrix naturally controls `A -> Sigma`; global representability is needed for `Sigma -> R`; and a proof aligned with the finite mechanism must still control the physical height window for `R -> V` rather than stop at Selmer density.

## What remains

Stage14-4an will derive the explicit quadratic-character / Hilbert-symbol reciprocity matrix on the five Euclid factors and determine how much of the three-gate factorization it can rigorously control. Because 4am places the finite dominant thinning at `R -> V`, the next family theorem must be coupled to the small-point height window.

The independent triple track still must control

\[
T(B)=o(\sqrt B)
\]

before a future raw-pair square-root law could transfer to exactly-two.

## Primary current artifacts

```text
stages/stage14/archive/stage14-4ak-shimada-split-root-void.md
stages/stage14/archive/stage14-4al-collective-first-hit.md
stages/stage14/archive/stage14-4am-rank-smallpoint-factorization.md
stages/stage14/data/14-4/collective_first_hit_summary.json
stages/stage14/data/14-4/rank_smallpoint_factor_summary.json
stages/stage14/scripts/14-4/rank_smallpoint_factor_audit.py
.github/workflows/stage14-4am-rank-smallpoint.yml
```
