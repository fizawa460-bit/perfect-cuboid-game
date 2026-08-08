# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain the primitive canonical exactly-two-face population inside the integer-space-diagonal cuboid family

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

```text
a-direction = ab+ac only
b-direction = ab+bc only
c-direction = ac+bc only
```

## 14-1 — Definition and counting interface

Status: [x] Complete.

## 14-2 — Complete finite enumeration

Status: [x] Complete. Two independent exact generation routes agree through `B=2,000,000`.

## 14-3 — Finite directional reconnaissance

Status: [x] Complete. No finite fit was promoted to an asymptotic theorem.

## Frozen Stage13 upstream contract

Stage13 freezes `R03 + Stage13-12ag`, including

\[
N_2(B)=o(B(\log B)^3).
\]

The fixed-prime overlap sieve gives zero density but no growing-modulus theorem and no explicit power saving in `B`.

## 14-4 — True total growth order

Status: [>] Active.

### 14-4aa — independent two-face parametrization

Status: [x] Complete. All directions are chambers of one shared-edge arithmetic object.

### 14-4ab — exact matching bijection

Status: [x] Complete. Primitive face-pair data give a fixed raw pair incidence with fiber multiplicity one.

### 14-4ac — rational-slope height envelope

Status: [x] Complete.

\[
(e,x,y)=L(1,t_1,t_2),
\qquad d=L\sqrt{1+t_1^2+t_2^2}.
\]

The pre-space denominator envelope is `B(log B)^7`; `sqrt(B)` was retained only as a finite candidate.

### 14-4ad — elliptic square thinning

Status: [x] Complete.

The space condition is birational, after fixing the first face, to

\[
E_{t_1}:Y^2=X(X-1)(X+t_1^2).
\]

The family is non-isotrivial. R03 supplies local obstructions but not the missing power exponent.

### 14-4ae — fiber/base height and generic rank

Status: [x] Complete.

For reduced second-face parameter `q=u/v`,

\[
v\asymp\sqrt{Bg/S_1}
\]

under the physical cutoff, uniformly up to absolute constants. The elliptic inverse is

\[
q=X/(sY),\qquad s=S_1/H_1.
\]

The full `t`-line elliptic surface has geometric singular fibers `I4,I4,I2,I2` and geometric generic Mordell--Weil rank `0`.

### 14-4af — Pythagorean-base specialization and triple geometry

Status: [x] Complete.

The actual Stage14 base is the Pythagorean degree-two cover

\[
t=\frac{2u}{1-u^2},
\qquad
H_1/S_1=\frac{1+u^2}{1-u^2}.
\]

The pulled-back elliptic surface has six `I4` fibers, Euler number `24`, and is K3. Its trivial lattice rank is already `20`; the K3 Picard upper bound and Shioda--Tate give

\[
\boxed{\operatorname{rank}E(\overline{\mathbf Q}(u))=0.}
\]

Thus no generic non-torsion section appears after restricting to Pythagorean first faces.

For every genuine Pythagorean base,

\[
\boxed{E_t(\mathbf Q)_{tors}\cong\mathbf Z/2\times\mathbf Z/4.}
\]

The order-4 points map to the degenerate boundary `q=+/-1`; rational 8-torsion is excluded by the impossibility of three rational squares in arithmetic progression with common difference `1`. Hence

\[
\boxed{\text{physical raw pair} \Longrightarrow \text{positive-rank specialization}.}
\]

The triple condition adds a second nonsingular quartic with disjoint branch set. Their fixed-base fiber product has

\[
\boxed{g=5},
\]

so each fixed first face has only finitely many rational triple points. No uniform moving-base bound and no `T=o(sqrt(B))` theorem is yet available.

Decision:

```text
STAGE14_4AF=COMPLETE
PYTHAGOREAN_BASE_CHANGE_K3=true
PYTHAGOREAN_BASE_FIBERS=I4_X6
PYTHAGOREAN_BASE_GENERIC_MW_RANK=0
TORSION_EXACT_Z2xZ4_ON_GENUINE_BASES=true
RATIONAL_4_TORSION_PHYSICAL=false
RATIONAL_8_TORSION_EXISTS=false
PHYSICAL_RAW_PAIR_IMPLIES_POSITIVE_RANK_SPECIALIZATION=true
TRIPLE_FIXED_BASE_GENUS=5
TRIPLE_FIXED_BASE_RATIONAL_POINTS_FINITE=true
UNIFORM_TRIPLE_POINT_BOUND_PROVED=false
T_O_SQRT_B_PROVED=false
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
```

Artifacts:

```text
stages/stage14/archive/stage14-4af-specialization-triple.md
stages/stage14/scripts/14-4/specialization_triple_audit.py
stages/stage14/data/14-4/specialization_triple_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

### 14-4ag — quantitative rank-jump / small-point count + uniform triple control

Status: [>] Next.

Purpose:

- count Pythagorean base specializations with positive rank under the Stage14 base height;
- strengthen that to the distribution of the first sufficiently small non-torsion point, not merely rank parity;
- make the `q`-height/canonical-height comparison sufficiently uniform over the Pythagorean base;
- incorporate `gcd(S1,S2)=g`, lcm coupling and the frozen R03 local restrictions;
- seek a uniform or averaged bound on rational points of the moving genus-5 triple fibers;
- determine whether the structural `sqrt(B)` fiber height survives the full base sum;
- transfer any raw-pair law to exactly-two only after the triple term is controlled at the same scale.

## 14-5 — Directionwise asymptotic structure

Status: pending Stage14-4.

## Scope boundary

No true growth exponent, leading constant, limiting directional ratio, eventual leader, Euler-side equality, perfect-cuboid existence/nonexistence theorem, or `T=o(sqrt(B))` theorem is currently established for Stage14.

```text
NEXT=Stage14-4ag quantitative rank-jump/small-point counting with uniform triple control
```
