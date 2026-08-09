# Stage14-4am — Selmer / Mordell–Weil rank / first-small-point factorization

## Purpose

Stage14-4al rewrote the moving-base problem as

\[
V(B)=\#\{F:\mu(F)\le B\},
\]

where `F=(S,X,H)` ranges over primitive oriented Pythagorean first-face bases and `mu(F)` is the first physical Stage14 space-diagonal height. Since the eligible-base count satisfies `A(B)=B/pi+O(sqrt(B) log B)`, an eventual `V(B)~c sqrt(B)` law is equivalent to inverse-square-root activation density.

Stage14-4am separates that activation into the exact nested arithmetic gates that were previously mixed together under the phrase “rank jump + first small point”.

## Exact three-gate identity

For cutoff `B`, define

```text
A(B)      = # primitive oriented Pythagorean bases F with H<=B
Sigma(B)  = # such bases with dim Sel_2(E_F)>2
R(B)      = # such bases with rank E_F(Q)>0
V(B)      = # such bases with mu(F)<=B
```

The integral elliptic model is

\[
E_F:\quad Y^2=Z(Z-S^2)(Z+X^2),
\]

with full rational 2-torsion. Every positive-rank fiber has nontrivial 2-Selmer beyond the two-dimensional rational 2-torsion baseline, while every physical active fiber has positive rank. Hence

\[
\boxed{V(B)\subset R(B)\subset \Sigma(B)\subset A(B)}
\]

and, whenever the denominators are nonzero,

\[
\boxed{
\frac{V}{A}=\frac{\Sigma}{A}\frac{R}{\Sigma}\frac{V}{R}.
}
\]

Writing the three factors schematically as `B^{-alpha_S}`, `B^{-alpha_R}`, and `B^{-beta_mu}`, the total activation thinning exponent is exactly

\[
\gamma=\alpha_S+\alpha_R+\beta_\mu.
\]

Thus if `A(B)=B^{1+o(1)}` and `V(B)=B^{1/2+o(1)}`, the three thinning exponents must sum to `1/2`. This is bookkeeping, not a square-root theorem.

## Complete finite base census, not a matched sample

The earlier s1 audit used 96 active and 96 height-matched inactive controls. Stage14-4am instead runs PARI/GP `ellrank(E,0)` on **every primitive oriented Pythagorean base with `H<=20,000`**.

For full rational 2-torsion, merged s1 records the exact relation

\[
\dim_{\mathbf F_2}\operatorname{Sel}_2(E_F)=r_2+2+s,
\]

where PARI returns unconditional Mordell–Weil rank bounds `[r1,r2]` and Cassels-pairing term `s`.

Therefore `Sigma(B)` is exact in this audit. The true `R(B)` is bracketed unconditionally:

- lower bound: every PARI-certified positive-rank fiber, plus any active fiber unresolved from below by effort-zero PARI;
- upper bound: every fiber whose PARI rank upper bound is positive.

In the actual census every active fiber through `20k` was already certified positive from below, so no geometric correction was needed in the reported lower bounds.

## Exact finite profile

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

So over this complete finite base family, nontrivial 2-Selmer is common and positive Mordell–Weil rank is also common, while a physical first hit below the same cutoff is rare.

This is much stronger finite evidence than the old matched-control observation. It does **not** prove that either `Sigma/A` or `R/A` has a positive limiting density.

## Finite thinning-exponent budget

At `B=20,000`, using logarithms to base `B`, the exact total activation exponent is

```text
gamma(total)                   = 0.4817176373
alpha_Selmer                   = 0.02034894195
alpha_MW | Selmer              in [0.02080686276, 0.03227209060]
beta_first-hit | MW            in [0.4290966047, 0.4405618326]
```

The true three exponents are correlated through the unknown exact value of `R(B)`, and their exact sum is `gamma`. The interval presentation must not be combined by independently choosing endpoints.

The finite conclusion is nevertheless robust: at this scale the overwhelming majority of the observed thinning budget occurs **after** positive rank, in the first-small-point / physical-hit gate.

Across the audited cuts, `Sigma/A` rises from about `0.746` to `0.817`, while the unconditional `R/A` interval stays near `0.58–0.67`. No finite power-law decay is visible in either preliminary gate. By contrast `V/R` remains at only a few percent and is about `1.3–1.4%` at `20k`.

No asymptotic conclusion is drawn from these finite percentages.

## Consequence for the s5a Euclid-parameter sieve

For primitive opposite-parity Euclid parameters

\[
S=m^2-n^2,\qquad X=2mn,\qquad H=m^2+n^2,
\]

the moving 2-descent support is carried by

```text
m, n, m-n, m+n, m^2+n^2
```

plus the fixed prime 2.

Stage14-s5a proposed a quadratic-character / Hilbert-symbol large sieve across these factors. Stage14-4am refines what such a theorem must accomplish:

1. a local-solubility character matrix naturally controls the `A -> Sigma` gate;
2. global representability / Sha information is needed to pass `Sigma -> R`;
3. even after positive rank, a height-sensitive theorem is needed for `R -> V` unless the family sieve is formulated from the outset with the physical small-point window.

Because the complete `H<=20k` census finds `Sigma/A` and `R/A` both large while `V/R` is tiny, a theorem that only proves scarcity of locally soluble 2-cover classes is not yet structurally aligned with the observed finite mechanism. The next analytic step should derive the explicit reciprocity matrix **and simultaneously identify how it can be coupled to the height window**, rather than stop at a Selmer-density estimate.

## Locked boundary

```text
STAGE14_4AM=COMPLETE_EXACT_SELMER_RANK_SMALLPOINT_FACTOR_AND_FINITE_FULL_BASE_CENSUS
ACTIVATION_DENSITY_THREE_GATE_FACTORIZATION_LOCKED=true
FULL_BASE_RANK_SELMER_CENSUS_MAX_H=20000
MATCHED_CASE_CONTROL_ONLY=false
FINITE_FIRST_SMALL_POINT_GATE_DOMINATES_THINNING_BUDGET=true
FINITE_SELMER_GATE_IS_RARE_EVENT=false
FINITE_POSITIVE_RANK_GATE_IS_RARE_EVENT=false
POSITIVE_RANK_DENSITY_PROVED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-4an derive Euclid-factor local character/reciprocity matrix and couple it to the height-sensitive R->V gate
```

## Artifacts

```text
stages/stage14/scripts/14-4/rank_smallpoint_factor_audit.py
stages/stage14/data/14-4/rank_smallpoint_factor_summary.json
.github/workflows/stage14-4am-rank-smallpoint.yml
```

The workflow regenerates the complete `H<=20k` PARI census and uploads the full generated audit JSON.
