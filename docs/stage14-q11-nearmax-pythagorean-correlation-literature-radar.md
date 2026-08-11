# Stage14-q11 — near-max Pythagorean correlation literature radar

## Trigger

```text
SOURCE_MAIN_SHA=31b309fe53c58434fbd102834cab2628b1654315
TRIGGER_STAGE=merged Stage14-4dl + merged Stage14-s7-55 + merged Stage14-t95 + merged Stage14-Work-beX17
LAST_RADAR_BASELINE=Stage14-q10
CURRENT_BEST_BOUND=V(B) << B^(1/2+o(1))
```

The q10 receiver was the post-sqrt dual-root-line compatibility energy.  That shape has materially changed.  X15/Work-X collapsed the global packet to a primitive Pythagorean three-projection correlation; 4dj--4dl and s7-51--s7-55 then removed fixed-power occupancy deficits, boundary variances, and non-maximal pair correlations.  The surviving global square-root mechanisms are now:

```text
GLOBAL_PRINCIPAL_BRANCH:
  full-conductor, near-maximal, interior-dense principal occupancy;

GLOBAL_PAIR_BRANCH:
  one representative primitive Pythagorean two-projection pair with
  |Delta_pair|=B^(-o(1))
  or
  |Err_pair|=B^(-o(1));

GLOBAL_CONNECTED_TRIPLE_BRANCH:
  all pairwise covariances fixed-power small but
  |kappa_3|=B^(-o(1)).
```

Merged s7-55 is especially important: the pair covariance is not merely the old centered inverse-fraction error.  It splits exactly into a principal pairwise joint-density defect plus the centered inverse-fraction error.  Therefore q10 still answers the analytic shape of `Err_pair`, while q11 must search for architecture addressing the **new principal joint-density / near-extremal correlation / connected-cumulant shape**.

The fixed-U advisory has also changed.  Merged t91--t95 reduce the primitive Gaussian representation fiber to an antipodal Boolean orientation quotient.  Odd Walsh spectrum is removed exactly; the survivor has near-maximal pair occupancy plus centered even quotient spectrum, with both low occupancy and fixed-power complement deficit already localized below sqrt.  Work-beX17 proves only a local occupancy-deficit adapter, not a common arithmetic receiver.

Required guards:

```text
Q10_INVERSE_FRACTION_BRANCH_NOT_RESEARCHED_AGAIN=true
GLOBAL_AND_FIXED_U_MEASURES_NOT_IDENTIFIED=true
FIXED_U_SAVING_NOT_CROSS_PROMOTED=true
PRINCIPAL_POSITIVE_DENSITY_NOT_REPLACED_BY_OSCILLATORY_ERROR=true
PAIRWISE_THREE_COORDINATE_REALIZATIONS_CHARGED_ONCE=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
```

## Search family A — 2026 Pythagorean multiplicative-function structure

Guilherme Azevedo and Joel Moreira, *Pythagorean triples in level sets of completely multiplicative functions*, arXiv:2607.04903.

Classification: `NEAR_STRUCTURE_HIGH_PRIORITY`.

This is the closest new literature to the **current geometric shape**, not to q10's old root-line shape.  The paper works directly on Pythagorean triples and proves joint Pythagorean recurrence for finite families of unimodular completely multiplicative functions.  Its proof combines two complementary mechanisms:

```text
APERIODIC / UNIFORM PART:
  higher-order Gowers uniformity gives vanishing averages;

PRETENTIOUS / STRUCTURED PART:
  concentration estimates preserve positive Pythagorean recurrence.
```

The exact Stage14 relevance is diagnostic rather than direct.  A successful transfer could potentially turn the current pair/triple correlation problem into a **structured-versus-uniform dichotomy** instead of bounding every physical selector by absolute values.

However the theorem is not an upper-bound theorem for arbitrary `0/1` physical selectors.  It assumes completely multiplicative functions (or the associated multiplicative systems), whereas `W_+, W_-, W_k` and the pair joint-density defect are not currently proved to be finite controlled combinations of such functions.  Moreover the pretentious branch supports recurrence rather than giving a saving; Stage14 would still have to show that its physical masks cannot occupy that structured class at full density, or quantify a density deficit inside it.

Falsifiable transfer test:

```text
Q11_PYTH_MULT_TRANSFER:
  on one full-conductor interior-dense Pythagorean cell,
  express each centered physical selector, or the representative pair joint-density defect,
  as a B^o(1)-term combination of bounded multiplicative / Hecke-multiplicative phases
  evaluated on the Euclid/Pythagorean factors;
  keep coefficient L2/L1 cost B^o(1);
  then separate aperiodic and pretentious pieces before absolute values.
```

If that decomposition does not exist with the full physical masks retained, this literature is `BACKGROUND`, not a theorem import.

## Search family B — higher-order Fourier decomposition of multiplicative functions

Nikos Frantzikinakis and Bernard Host, *Higher order Fourier analysis of multiplicative functions and applications*, arXiv:1403.0945 (published 2017).

Classification: `NEAR_ARCHITECTURE`.

The paper gives a structure theorem decomposing bounded multiplicative functions into an approximately periodic/structured component and a component with arbitrarily small Gowers uniformity norm, and derives polynomial-correlation consequences.  Azevedo--Moreira 2026 explicitly uses this higher-order uniformity input in its Pythagorean setting.

This gives q11 a concrete receiving-stage question: can the Stage14 cellwise selector algebra be reduced to a bounded-complexity multiplicative coefficient system before the three-way expectation is formed?  If yes, the connected third cumulant becomes a plausible generalized-von-Neumann/Gowers-uniformity target and the principal structured term becomes a finite pretentious/local-density computation.

Direct import currently fails because:

```text
PHYSICAL_SELECTORS_PROVED_MULTIPLICATIVE=false
UNIFORM_BOUNDED_COMPLEXITY_DECOMPOSITION_PROVED=false
CONNECTED_THIRD_CUMULANT_CONTROLLED_BY_GOWERS_NORM=false
PRETENTIOUS_PRINCIPAL_DENSITY_DEFICIT_PROVED=false
```

The architecture is therefore `NEAR`, not `DIRECT`.

## Search family C — pretentious recurrence is a warning, not a saving theorem

Nikos Frantzikinakis and Andreas Mountakis, *Recurrence for pretentious systems along generalized Pythagorean triples*, arXiv:2508.09778.

Classification: `BACKGROUND_STRUCTURAL_WARNING`.

This work establishes multiple recurrence along generalized Pythagorean triples for pretentious multiplicative actions.  For Stage14 this matters because it prevents a false inference:

```text
LARGE_PYTHAGOREAN_CORRELATION => PRETENTIOUS_STRUCTURE
```

would **not** by itself imply a power saving.  Pretentious structure can sustain positive multiple recurrence on Pythagorean configurations.  A Stage14 use of the multiplicative-function route must therefore continue one step further and prove one of:

```text
PHYSICAL_PRETENTIOUS_CLASS_EMPTY_AT_SQRT=true
or
PHYSICAL_PRETENTIOUS_DENSITY_HAS_FIXED_POWER_DEFICIT=true
or
PRETENTIOUS_MAIN_TERMS_HAVE_SIGNED_ANTICORRELATION=true.
```

This source is useful mainly as a guard against overclaiming the structure/uniformity split.

## Search family D — Boolean low-degree stability for the fixed-U orientation quotient

Representative sources:

- Piotr Nayar, *FKN Theorem on the biased cube*, arXiv:1311.3179;
- Nathan Keller and Ohad Klein, *A structure theorem for almost low-degree functions on the slice*, arXiv:1901.08839, building on the Kindler--Safra low-degree structure theorem.

Classification: `BLOCKED_FIXED_U_LOW_DEGREE_PRECONDITION`.

These theorems say, in different Boolean settings, that a Boolean function whose Fourier mass is concentrated at low degree is close to a bounded-coordinate structured object (dictator/junta-type structure).  That would be highly useful for the t91--t95 orientation quotient **if** the surviving centered even Walsh spectrum were first shown to have a fixed-degree tail bound.

But merged t92 explicitly did not prove bounded Walsh degree or a power-decaying high-degree tail.  Antipodal quotienting removes odd degrees, but even degrees of arbitrary size remain legal.  Parseval and the t95 occupancy-variance dichotomy alone do not imply the low-degree hypothesis.

Therefore:

```text
FKN_KINDLER_SAFRA_DIRECT_IMPORT=false
T_LOW_DEGREE_TAIL_REQUIRED=true
T_LOW_DEGREE_TAIL_CURRENTLY_PROVED=false
```

Smallest t-route falsification test: before opening any theorem audit, measure whether the exact physical selector admits a uniform bounded-degree or bounded-influence reduction after conditioning on the fixed exceptional prime support.  Without that internal lemma, q11 should not route FKN/Kindler--Safra into t.

## Search family E — inverse Gowers theory on Boolean / bounded-exponent groups

Asgar Jamneshan, Or Shalom and Terence Tao, *Polynomial towers and inverse Gowers theory for bounded-exponent groups*, arXiv:2601.00961.

Classification: `BLOCKED_NO_GOWERS_NORM_TRIGGER`.

This 2026 inverse theorem is potentially attractive for the t orientation cube because `{+-1}^r` is a bounded-exponent group.  Large `U^{k+1}` norm forces correlation with a bounded-degree polynomial structure.  But the current fixed-U packet supplies Parseval energy, antipodal parity, and occupancy information; it does **not** supply a lower bound for a Gowers norm of the centered physical coefficient.  Likewise the global connected third cumulant is not automatically a `U^3` norm.

Thus no legal inverse-theorem invocation exists yet:

```text
T_CENTERED_COEFFICIENT_LARGE_UK_PROVED=false
GLOBAL_KAPPA3_LARGE_U3_PROVED=false
INVERSE_GOWERS_DIRECT_IMPORT=false
```

This family should be reopened only if an internal Cauchy--Schwarz cube argument converts a square-root-saturating correlation into a quantitative Gowers-norm lower bound without losing the physical masks.

## q10 carry-forward — centered inverse-fraction branch

The q11 trigger does **not** supersede all of q10.  Merged s7-55 isolates

```text
Gamma_pair = Delta_pair + Err_pair.
```

The `Err_pair` term is precisely where the q10 Dong--Robles--Zeindler / Bettin--Chandee inverse-fraction technology remains the first external analytic test once the coefficient/range hypotheses are fully matched.  q11 adds no better direct theorem for that already-known branch.

```text
Q10_DONG_ROBLES_ZEINDLER_HANDOFF_REMAINS_ACTIVE=true
Q10_REUSS_HANDOFF_REMAINS_CONDITIONAL_ON_NEW_ELIMINANT=false
Q11_DOES_NOT_DOUBLE_COUNT_Q10=true
```

## Verdict

No surveyed source directly proves a fixed-power strict sub-square-root saving for the current charged-once physical packet.

The most useful new q11 information is structural:

1. the 2026 Azevedo--Moreira Pythagorean multiplicative-function theorem gives a genuinely current **Pythagorean structured/uniform architecture**;
2. Frantzikinakis--Host supplies the higher-order Fourier decomposition behind the uniform side;
3. pretentious Pythagorean recurrence shows that detecting structure alone is not a saving;
4. Boolean low-degree and inverse-Gowers tools are premature for t until a low-degree/Gowers-norm bridge is proved;
5. q10 remains the correct shelf for the already-isolated centered inverse-fraction error.

```text
STAGE14_Q11=COMPLETE_NEARMAX_PYTHAGOREAN_CORRELATION_LITERATURE_RADAR
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_FROM_LITERATURE_PROVED=false
AZEVEDO_MOREIRA_2026_PYTHAGOREAN_MULTIPLICATIVE=NEAR_STRUCTURE_HIGH_PRIORITY
FRANTZIKINAKIS_HOST_HIGHER_ORDER_FOURIER=NEAR_ARCHITECTURE
PRETENTIOUS_PYTHAGOREAN_RECURRENCE=BACKGROUND_STRUCTURAL_WARNING
FKN_KINDLER_SAFRA_FIXED_U=BLOCKED_NO_LOW_DEGREE_TAIL
BOUNDED_EXPONENT_GOWERS_INVERSE=BLOCKED_NO_GOWERS_NORM_TRIGGER
Q10_INVERSE_FRACTION_BRANCH_RETAINED=true
FIXED_U_TO_GLOBAL_CROSS_PROMOTION_PROVED=false
```

## Falsifiable handoff

Preferred global internal test:

```text
Q11_GLOBAL_TRANSFER_TEST:
  choose one merged s7-55 representative pair and one connected-third-cumulant cell;
  factor every physical selector through the Pythagorean/Euclid coordinates;
  test whether the centered coefficients are a B^o(1)-complexity combination of
  multiplicative/Hecke-multiplicative phases;
  if yes:
      split aperiodic versus pretentious pieces before absolute values;
      test Gowers-uniform decay on the aperiodic piece;
      compute/defeat the pretentious principal density separately;
  if no:
      retain the current joint-density/cumulant receiver as genuinely nonmultiplicative.
```

Preferred fixed-U internal test:

```text
Q11_T_TRANSFER_TEST:
  on the antipodal quotient after t95,
  prove or refute a uniform fixed-degree Fourier-tail / bounded-influence lemma;
  only if proved, reopen Boolean stability or bounded-exponent inverse theory.
```

Recommended receivers:

```text
HANDOFF_S=Stage14-s7-56+
HANDOFF_MAIN=Stage14-4dm+
HANDOFF_T=Stage14-t96+
NEXT_Q_STAGE=NONE_UNTIL_THE_MULTIPLICATIVE_PHASE_TEST_OR_A_NEW_STABLE_OBSTRUCTION
```
