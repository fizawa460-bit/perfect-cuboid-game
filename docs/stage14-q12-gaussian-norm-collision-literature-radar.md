# Stage14-q12 — Gaussian norm-collision literature radar

## Trigger

```text
TRIGGER_STAGE=merged Stage14-4du + merged Stage14-t102 + merged Stage14-Work-bhX20
EXACT_OBSTRUCTION=Gaussian mover-candidate image size versus norm-ratio collision energy, with fixed-U generic-prime mover density/energy
CURRENT_BEST_BOUND=V(B) << B^(1/2+o(1))
WHY_EXISTING_Q_LEDGER_DOES_NOT_ALREADY_ANSWER_IT=q11 treats near-max Pythagorean selector correlation/Hecke structure; q10 treats centered inverse-fraction cancellation. Neither treats collision energy of Gaussian norm values across frozen cofactor states or prime-averaged mover actions.
SEARCH_FAMILIES=multiplicative pair correlation of quadratic norm forms; Gaussian sparse-modulus large sieve; linear correlations of sums of two squares; Gaussian multiplicative averages on primitive lattices
LAST_RADAR_BASELINE=Stage14-q11
PROMOTION_STANDARD=fixed-power saving for the full charged-once physical packet with primitive/gcd/range/orientation masks retained; no fixed-U to whole-family cross-promotion without an explicit finite-fiber bridge
```

Unmerged descendants, including Stage14-t103 and Stage14-s7-62 at the trigger snapshot, are advisory only and are not theorem sources.

## Current merged receiver

Merged 4du reduces the whole-family zero-mode square-root obstruction to the dichotomy

```text
candidate image size
versus
collision energy,
```

for mover candidates generated from frozen cofactor states. The repeated-candidate branch has the explicit plus-state collision equation

```text
x2 (r1^2+s1^2) = x1 (r2^2+s2^2).
```

Merged t102 independently proves on the fixed-U route that a square-root-saturating packet carries generic-prime mover density/energy of exponent zero in the `B^(-o(1))` sense, while the number of generic split primes is only `r=B^o(1)`. Work-bhX20 gives a common mover/stabilizer language but explicitly does not provide a common arithmetic adapter.

The q12 question is therefore not another generic Pythagorean-correlation search. It is whether existing norm-form pair-correlation, Gaussian large-sieve, or quadratic-form correlation results give a quantitative fixed-power deficit for either side of this image/energy dichotomy under the exact Stage14 masks.

## Family A — Parkkonen–Paulin 2026 multiplicative pair correlations of quadratic norm forms

Source: Jouni Parkkonen and Frédéric Paulin, *On the multiplicative pair correlations of sums of two squares*, arXiv:2602.13058 (2026).

Classification: `NEAR_STRUCTURE_HIGH_PRIORITY`.

This is the closest direct literature match to the new 4du geometry. It studies pair correlations of logarithms of integral values of quadratic norm forms, including `K=Q(i)`, hence ratios of sums of two squares / Gaussian norms. The paper proves asymptotic pair-correlation measures with quantitative error terms across scaling regimes.

The Stage14 collision equation can be rewritten as equality of two weighted Gaussian norm values,

```text
x2 N(z1) = x1 N(z2),
z_i=r_i+i s_i.
```

This is genuinely closer to q12 than the q11 multiplicative-function recurrence literature.

Direct import nevertheless fails at the current receiver because Parkkonen–Paulin averages a broad norm-value pair-correlation ensemble with geometric sector/proximity weights. Stage14 conditions on frozen cofactor states, primitive/gcd allocation, charged-once reconstruction, physical range masks, and state-dependent weights `x_i`; moreover the obstruction is exact collision energy / image concentration, not merely the existence of a limiting pair-correlation measure for logarithmic norm ratios.

```text
PP2026_QUADRATIC_NORM_RATIO_GEOMETRY_MATCH=true
PP2026_FULL_PHYSICAL_WEIGHT_MATCH=false
PP2026_EXACT_COLLISION_ENERGY_BOUND_IMPORTED=false
PP2026_FIXED_POWER_STAGE14_DELTA_PROVED=false
```

Falsifiable receiving test: rewrite one merged 4du collision cell as a Parkkonen–Paulin norm-pair statistic and check whether all Stage14 weights can be absorbed into their admissible sector/representation weights with constants uniform in the moving cofactor/conductor parameters. If not, keep this source structural only.

## Family B — Baier–Bansal Gaussian large sieve with sparse moduli

Source: Stephan Baier and Arpit Bansal, *Large sieve with sparse sets of moduli for Z[i]*, arXiv:1811.07300.

Classification: `NEAR_CONDITIONAL_ON_POLYNOMIAL_FAMILY`.

The theorem gives Gaussian large-sieve inequalities for sparse moduli, including Gaussian-prime moduli. This is a natural candidate if the mover problem can be reorganized into a genuinely long family of independent Gaussian moduli / residue actions.

At the current merged boundary, however, the fixed-U generic-prime family has only

```text
r=omega(delta_G)=B^o(1),
```

and 4dt/4du show that a frozen cofactor state has only divisor-many mover candidates. Therefore the present receiver does not expose a polynomial-length sparse-modulus family from which a fixed power of `B` can be saved. Applying a large sieve after counting the same `B^o(1)` candidate support would merely repackage an already charged subpolynomial factor.

```text
GAUSSIAN_LARGE_SIEVE_STRUCTURALLY_RELEVANT=true
POLYNOMIAL_LENGTH_MODULUS_FAMILY_PROVED=false
CURRENT_DIRECT_FIXED_POWER_SAVING=false
```

Reopen only if a later stage produces a common arithmetic boundary/action with a genuinely power-sized family of moduli or independent samples before absolute values.

## Family C — Browning–Munshi correlations among sums of two squares

Source: T. D. Browning and R. Munshi, *Pairs of diagonal quadratic forms and linear correlations among sums of two squares*, arXiv:1302.2434.

Classification: `BACKGROUND_NEAR_DIFFERENT_CORRELATION_SHAPE`.

This work uses the circle method for pairs of diagonal quadratic forms and derives linear-correlation information for sums of two squares. It confirms that strong analytic machinery exists for simultaneous two-square representation conditions, but its correlation variable is additive/linear rather than the weighted multiplicative norm-ratio collision

```text
x2 N(z1)=x1 N(z2).
```

The Stage14 frozen cofactor weights and charged-once masks are not an instance of the published setup. No direct exponent transfer is justified.

## Family D — Gaussian multiplicative averages / primitive lattice averages

Sources:

- Sebastián Donoso, Anh N. Le, Joel Moreira, Wenbo Sun, *Pointwise convergence of additive ergodic averages associated with multiplicative actions of the Gaussian integers* (Trans. AMS 377 (2024));
- Biao Wang, *On averages of completely multiplicative functions over co-prime integer pairs* (2025/2026 publication cycle; arXiv:2406.09243).

Classification: `BACKGROUND_STRUCTURE_NOT_COLLISION_SAVING`.

These results give convergence statements for multiplicative functions over Gaussian integers and primitive/coprime lattice points. They are useful background for retaining primitive structure in Gaussian averages, but they do not give a fixed-power collision-energy estimate uniform in the moving Stage14 physical coefficients. They therefore do not supersede the q11/AM blocked-adapter conclusion.

## Advisory consequence of unmerged t103

Unmerged t103 reports a further pigeonhole to one common elementary boundary skeleton across primes, while its action parameter still varies with the prime and the prime family remains `B^o(1)`. This would make the Baier–Bansal route more concrete if merged, but it still does not supply the polynomial-length family needed for an immediate fixed-power large-sieve gain. Because t103 is unmerged at the q12 theorem snapshot, this paragraph is advisory only.

## Verdict

No surveyed theorem directly proves strict sub-square-root saving for the current 4du/t102 physical receiver.

The new q12 information is nevertheless material:

1. Parkkonen–Paulin 2026 is an exact thematic match to the **multiplicative pair correlation of Gaussian norm values** and is the first external shelf to test on the 4du collision branch;
2. Gaussian sparse-modulus large sieve is not yet quantitatively activated because the available mover-prime/candidate families are only `B^o(1)`;
3. linear correlations of sums of two squares and qualitative Gaussian multiplicative averages do not match the weighted exact collision receiver strongly enough for cross-promotion.

```text
STAGE14_Q12=COMPLETE_GAUSSIAN_NORM_COLLISION_LITERATURE_RADAR
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_FROM_LITERATURE_PROVED=false
PARKKONEN_PAULIN_2026=NEAR_STRUCTURE_HIGH_PRIORITY
BAIER_BANSAL_GAUSSIAN_LARGE_SIEVE=NEAR_CONDITIONAL_ON_POLYNOMIAL_FAMILY
BROWNING_MUNSHI_LINEAR_CORRELATION=BACKGROUND_DIFFERENT_SHAPE
GAUSSIAN_MULTIPLICATIVE_AVERAGES=BACKGROUND_STRUCTURE
Q10_INVERSE_FRACTION_BRANCH_RETAINED=true
Q11_HECKE_PHYSICAL_ADAPTER_BOUNDARY_RETAINED=true
FIXED_U_TO_GLOBAL_CROSS_PROMOTION_PROVED=false
```

## Falsifiable handoff

Preferred next internal test:

```text
Q12_NORM_PAIR_TRANSFER_TEST:
  choose one merged 4du repeated-candidate cell;
  write x2*N(z1)=x1*N(z2) with the exact primitive/gcd/range/orientation masks;
  compare the resulting weighted pair statistic term-by-term with Parkkonen--Paulin 2026;
  prove or disprove a uniform embedding with B^o(1) coefficient loss;
  if the embedding succeeds, extract the strongest quantitative error term uniform in the moving x_i/conductor packet;
  if it fails, isolate the first non-absorbable physical weight/mask as the next named receiver.
```

The q-route should park after q12 until this norm-pair transfer test, a polynomial-length common mover family, or another materially different stable obstruction appears.