# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_4AM_COMPLETE_SELMER_RANK_SMALLPOINT_FACTORIZATION_14_4AN_NEXT`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 counts primitive canonical cuboids

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,\qquad d\le B,
\]

with exactly two integral face diagonals. No perfect-cuboid nonexistence assumption is made.

This is the canonical resynthesis through Stage14-4am. Detailed historical calculations remain frozen in the stage archive and substage result files.

## §1. Exact ledger and finite ceiling

Let `T(B)` count all-three-face objects and let `E(B)=O_pair_raw(B)` be raw two-face incidences. Then

\[
\boxed{E(B)=N_2(B)+3T(B)}.
\]

At `B=2,000,000`, two independent exact generation routes give

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,\qquad T=0.
\]

The finite zero triple census is not a perfect-cuboid nonexistence theorem. Frozen Stage13 `R03 + Stage13-12ag` gives only

\[
N_2(B)=o(B(\log B)^3),
\]

not the true Stage14 order.

## §2. Two-face coordinates and elliptic specialization

For primitive oriented Pythagorean face data

\[
F_i=(S_i,X_i,H_i),\qquad S_i^2+X_i^2=H_i^2,
\]

put `g=gcd(S1,S2)` and `L0=lcm(S1,S2)`. Primitive gluing has multiplicity one and

\[
(e,x,y)=L_0\left(1,\frac{X_1}{S_1},\frac{X_2}{S_2}\right),
\qquad
 d=L_0\sqrt{1+(X_1/S_1)^2+(X_2/S_2)^2}.
\]

The integer space-diagonal condition is equivalent to

\[
\boxed{(X_1X_2)^2+(gd)^2=(H_1H_2)^2}.
\]

Fixing the first face gives

\[
\boxed{E_t:Y^2=X(X-1)(X+t^2)},
\qquad t=X_1/S_1.
\]

On the actual Pythagorean base this elliptic surface has geometric generic Mordell--Weil rank zero. Rational torsion is nonphysical on genuine Stage14 fibers. Every physical raw pair therefore occurs on a positive-rank specialization and requires a sufficiently small non-torsion point.

## §3. Level-4 Kummer geometry and physical height

With half-angle parameters `r,s`, the raw pair surface is

\[
\boxed{Z^2=(1+r^2)^2(1+s^2)^2-16r^2s^2}.
\]

Over `Q(i)` this is the classical level-4 modular K3; over `C` it is `Km(E_i x E_i)`. The toric control surface is

\[
Y=\operatorname{Bl}_4(\mathbf P^1_r\times\mathbf P^1_s),
\qquad L=-K_Y,
\]

and for the resolved double cover `pi:X->Y`,

\[
\boxed{M=\pi^*L},\qquad \boxed{M^2=8},\qquad \boxed{H_M=d}.
\]

Thus the original cuboid cutoff is the exact geometric `M`-height.

Let `V(B)` count active oriented first-face bases and `E(B)` raw pair edges. A uniform bounded-height estimate on each elliptic fiber gives maximum graph degree `B^{o(1)}`, hence `E(B)` and `V(B)` have the same limsup and liminf polynomial growth exponents.

Finite data remain close to square-root scale:

```text
B           V(B)     V(B)/sqrt(B)
200,000      155      0.34659
500,000      254      0.35921
1,000,000    347      0.34700
2,000,000    490      0.34648
```

No asymptotic is inferred from this table.

## §4. Stage14-4ah through 4ak — complete fixed-curve closure

Any fixed physical rational curve capable of polynomial exponent `1/2` must have

\[
M\cdot C=4,
\qquad \deg(C\to\mathbf P^1_r)=2,
\qquad \deg(C\to\mathbf P^1_s)\le2.
\]

Stage14-4ai eliminates every connected degree-two image mechanism and every arithmetic-genus-zero split/contact mechanism. The sole unresolved case was a singular rational member of the anticanonical class `D=L=-K_Y` whose pullback might split.

Stage14-4aj identifies the physical deck involution on

\[
E_t:y^2=x(x-1)(x+t^2)
\]

as

\[
\boxed{\delta(P)=(0,0)-P}.
\]

For a hypothetical final split component,

\[
M=C+\delta(C),\qquad C^2=-2,\qquad M\cdot C=4.
\]

Putting

\[
\boxed{x=2C-M}
\]

gives the exact finite lattice target

\[
\boxed{\delta(x)=-x,\qquad x^2=-16,\qquad x\equiv M\pmod2}.
\]

Stage14-4ak directly consumes Shimada's published level-4 Neron--Severi and automorphism data. The physical fiber/polarization/deck labeling is unique up to the relevant `AutX0f` symmetry. For a representative, the saturated deck anti-invariant lattice has

```text
rank = 6
positive-form determinant = 256
```

and exact short-vector census

```text
norm 0   :    1
norm 4   :   60
norm 8   :  252
norm 12  :  544
norm 16  : 1020
```

The norm-16 shell is nonempty, but the required parity coset is empty:

```text
PARI qfminim norm-16 +/- representatives = 510
independent exact LDL norm-16 vectors     = 1020
parity-compatible norm-16 vectors         = 0
parity-compatible split-root pairs        = 0
```

Therefore

\[
\boxed{\text{no physical rational }M\text{-degree-four bisection exists}}.
\]

Locked consequence:

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTENCE_RESOLVED=true
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

The observed finite square-root signal cannot be explained by a finite collection of fixed extremal rational curves.

## §5. Stage14-s arithmetic input

The parallel arithmetic track is now a direct input to the main line.

- `14-s1`: exact full-2-torsion descent interface; positive rank/Selmer alone does not separate physical activity.
- `14-s2`: varying local conditions live on the moving prime support `p|2SXH`; no fixed-prime sieve gives positive-rank density.
- `14-s3`: a physical hit implies a non-torsion point in a logarithmic canonical-height window; positive rank and the first-small-point gate are distinct.
- `14-s4a`: all 490 active vertices are fingerprinted through `B=2m`; `483/490` exact Kummer square-class triples are distinct.
- `14-s4b`: `393` coarse arithmetic signatures remain, with largest cluster only `4`; rank/Selmer/root type is comparatively concentrated while the actual small-point arithmetic is dispersed.
- `14-s4c`: any hypothetical higher-degree stratum explanation of a square-root law must proliferate at a positive power rate; a few fixed higher-degree families cannot replace the rejected `M.C=4` mechanism.
- `14-s5`: single-fiber small-point estimates are insufficient for a power saving in the number of activated bases; a family-level theorem is required.
- `14-s5a`: in primitive Euclid parameters, the moving full-2-descent support is carried by `m,n,m-n,m+n,m^2+n^2` plus `2`; the proposed next tool is a quadratic-character / Hilbert-symbol family sieve coupled to the physical small-point window.

No Selmer-rank/Mordell--Weil-rank equality or uniform least-generator theorem is assumed.

## §6. Stage14-4al — exact collective activation measure

For each primitive oriented Pythagorean first-face base

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

define

\[
\mu(F)=\min\{d:\text{a physical Stage14 partner of }F\text{ occurs at height }d\},
\]

and set `mu(F)=infinity` when no partner exists. Then the active-vertex count is exactly

\[
\boxed{V(B)=\#\{F:\mu(F)\le B\}}.
\]

This is the post-4ak counting object.

Let

\[
A(B)=\#\{F\text{ primitive oriented Pythagorean}:H(F)\le B\}.
\]

Euclid parameters `m>n`, `gcd(m,n)=1`, opposite parity, together with sector lattice-point counting give

\[
\boxed{A(B)=\frac{B}{\pi}+O(\sqrt B\log B)}.
\]

Consequently, whenever either asymptotic exists,

\[
\boxed{
V(B)\sim c\sqrt B
\iff
\frac{V(B)}{A(B)}\sim\frac{\pi c}{\sqrt B}.
}
\]

Thus the finite square-root signal is equivalently an inverse-square-root activation-density signal on a linear-size arithmetic base population.

## §7. Exact finite activation profile

The 4al deterministic audit regenerates both the exact graph and the full s4a PARI census. At the late frozen cutoffs:

```text
B          A(B)      V(B)      sqrt(B)*V/A
200,000     63,638      155       1.0892565339
500,000    159,164      254       1.1284280517
1,000,000  318,278      347       1.0902418640
2,000,000  636,640      490       1.0884717353
```

Across `200k -> 2m`:

```text
A effective exponent                1.0001773995
V effective exponent                0.4998643819
(V/A) effective exponent           -0.5003130177
mean sqrt(B)*V/A                    1.0990995462
CV   sqrt(B)*V/A                    0.0154166485
```

This is unusually stable finite evidence, but still not an asymptotic theorem.

At `B=2m`, active exact/interval ranks are

```text
exact rank 1      254
exact rank 2      188
exact rank 3       22
exact rank 4        1
interval 0..2      15
interval 1..3      10
```

The exact rank-1 and rank-2 active strata have `200k -> 2m` effective exponents about `0.45544` and `0.50331`. Hence no single exact-rank stratum alone explains the whole finite signal.

## §8. First-small-point lower tail is a genuine obstruction

At `B=2m`, the first-hit/base-height ratio among active bases has

```text
mu/H min       1.0084504563
mu/H q25       5.9293664156
mu/H median   21.0312461990
mu/H q75      98.2251521298
mu/H max   11483.1313868613
```

and

```text
log(mu)/log(H) q25      1.1766954421
log(mu)/log(H) median   1.3256609166
log(mu)/log(H) q75      1.5584093372
```

So even an active positive-rank fiber frequently waits far beyond its base hypotenuse before its first physical point appears. The rank-jump frequency and first-small-point lower tail cannot be collapsed into one event.

The actual first-hit canonical heights remain logarithmic in physical height, with

```text
hhat/log(mu) q25      0.2497840927
hhat/log(mu) median   0.3116647403
hhat/log(mu) q75      0.3700583881
```

consistent with Stage14-s3, but no uniform distribution theorem is known here.

## §9. Stage14-4am — exact three-gate activation factorization

For the integral full-2-torsion fiber

\[
E_F:\quad Y^2=Z(Z-S^2)(Z+X^2),
\]

define four nested base populations:

```text
A(B)      = primitive oriented Pythagorean bases with H<=B
Sigma(B)  = bases with dim Sel_2(E_F)>2
R(B)      = bases with rank E_F(Q)>0
V(B)      = bases with mu(F)<=B
```

Every physical active fiber has positive rank, and positive rank forces a nontrivial 2-Selmer class beyond rational 2-torsion. Therefore

\[
\boxed{V(B)\subset R(B)\subset\Sigma(B)\subset A(B)}
\]

and the activation density factors exactly as

\[
\boxed{
\frac{V(B)}{A(B)}=
\frac{\Sigma(B)}{A(B)}
\frac{R(B)}{\Sigma(B)}
\frac{V(B)}{R(B)}.
}
\]

If the three factors have power-law thinning exponents `alpha_S`, `alpha_R`, `beta_mu`, then their exact sum is the total activation exponent. Since `A(B)=B^{1+o(1)}`, an eventual `V(B)=B^{1/2+o(1)}` law would require

\[
\boxed{\alpha_S+\alpha_R+\beta_\mu=1/2}.
\]

This is an exact accounting identity, not a proof that the exponents exist.

## §10. Complete finite Selmer/rank census through H<=20,000

Stage14-4am replaces the old s1 matched sample by a complete PARI/GP `ellrank(E,0)` census of every primitive oriented Pythagorean base with `H<=20,000`.

For full rational 2-torsion, merged s1 gives

\[
\dim_{\mathbf F_2}\operatorname{Sel}_2(E_F)=r_2+2+s,
\]

where `[r1,r2]` is PARI's unconditional Mordell--Weil rank interval and `s` is the Cassels-pairing term. Hence `Sigma(B)` is exact. The true positive-rank count `R(B)` is bracketed unconditionally by certified positive ranks from below and nonzero rank upper bounds from above. Every active fiber through `20k` is already PARI-certified positive from below.

The complete finite counts are

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

The corresponding finite logarithmic thinning budget is

```text
gamma(total)                   = 0.4817176373
alpha_Selmer                   = 0.02034894195
alpha_MW | Selmer              in [0.02080686276, 0.03227209060]
beta_first-hit | MW            in [0.4290966047, 0.4405618326]
```

The two interval contributions are correlated through the unknown exact value of `R(B)` and their endpoints must not be chosen independently.

The robust finite conclusion is that nontrivial 2-Selmer is common and positive Mordell--Weil rank is also common on the complete audited base family, whereas physical activation conditional on positive rank is rare. At `20k`, the first two gates retain roughly `82%` and `59–67%` of all bases, while the final `R -> V` gate retains only about `1.3–1.4%` of positive-rank bases.

Thus the finite activation thinning is overwhelmingly located **after positive rank**, in the height-sensitive first-small-point gate. This is finite evidence only: it does not prove positive-rank density, a first-small-point lower-tail exponent, or a square-root asymptotic.

## §11. Consequence for the Euclid-parameter family theorem

For primitive opposite-parity Euclid parameters

\[
S=m^2-n^2,\qquad X=2mn,\qquad H=m^2+n^2,
\]

the moving full-2-descent support is carried by

```text
m, n, m-n, m+n, m^2+n^2
```

plus the fixed prime `2`.

Stage14-s5a proposes exposing local solubility as quadratic-character / Hilbert-symbol constraints among squarefree pieces of these five factors and averaging them by a family large sieve. Stage14-4am clarifies the role of such a theorem:

1. the local reciprocity matrix naturally controls `A -> Sigma`;
2. global representability / Sha information is required to pass `Sigma -> R`;
3. because the finite dominant thinning occurs at `R -> V`, a theorem aligned with the observed mechanism must remain coupled to the physical logarithmic height window rather than stop at a Selmer-density bound.

A purely local/Selmer sieve may still be an essential component, but 4am rules out treating it as automatically equivalent to the activation count.

## §12. Next main-track target

Stage14-4an must derive the explicit Euclid-factor local character/reciprocity matrix and identify precisely which factor of

\[
V/A=(\Sigma/A)(R/\Sigma)(V/R)
\]

it can bound unconditionally. The key design requirement is to couple the character calculation to global representability and the first-small-point height window wherever possible.

No `sqrt(B)` endpoint is assumed. Any genuine power saving for the joint activation set would already advance the theorem boundary.

## §13. Triple gate

The exact relation remains

\[
N_2(B)=E(B)-3T(B).
\]

The independent Stage14-t track must still prove strong moving-base control, ideally

\[
T(B)=o(\sqrt B),
\]

before a future raw-pair square-root law can be transferred to exactly-two.

## §14. Locked decision

```text
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

PHYSICAL_KUMMER_POLARIZATION_LOCKED=true
PHYSICAL_LINE_BUNDLE=M=pi^*(-K_Y)
PHYSICAL_POLARIZATION_SQUARE=8
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true

COLLECTIVE_FIRST_HIT_IDENTITY_LOCKED=true
ORIENTED_PRIMITIVE_PYTHAGOREAN_BASE_ASYMPTOTIC_LINEAR=true
SQRTB_EQUIVALENT_TO_INVERSE_SQRT_ACTIVATION_DENSITY=true
ACTIVATION_DENSITY_THREE_GATE_FACTORIZATION_LOCKED=true
FULL_BASE_RANK_SELMER_CENSUS_MAX_H=20000
FINITE_FIRST_SMALL_POINT_GATE_DOMINATES_THINNING_BUDGET=true
FINITE_SELMER_GATE_IS_RARE_EVENT=false
FINITE_POSITIVE_RANK_GATE_IS_RARE_EVENT=false

POSITIVE_RANK_DENSITY_PROVED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
TRUE_GROWTH_ORDER_IDENTIFIED=false

T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false

NEXT=Stage14-4an Euclid-factor reciprocity matrix coupled to height-sensitive activation
```

## §15. Primary artifacts

```text
stages/stage14/archive/stage14-4ak-shimada-split-root-void.md
stages/stage14/archive/stage14-4al-collective-first-hit.md
stages/stage14/archive/stage14-4am-rank-smallpoint-factorization.md
stages/stage14/data/14-4/collective_first_hit_summary.json
stages/stage14/data/14-4/rank_smallpoint_factor_summary.json
stages/stage14/scripts/14-4/rank_smallpoint_factor_audit.py
.github/workflows/stage14-4am-rank-smallpoint.yml
```
