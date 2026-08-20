# Stage27-60b — Stage18 -> Stage19 mechanism and double-charge ledger

```text
TASK_ID=Stage27-60b
CHECKPOINT=60
PARENT=Stage27-60a
ROUTE_KIND=CAUSAL_MECHANISM_AND_DOUBLE_CHARGE_LEDGER
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## 1. The genuinely new condition

The only new defining condition in the Stage18 -> Stage19 transition is that the
space diagonal be integral:

\[
w^2=a^2+b^2+c^2.
\]

On the Stage18 shared-edge double-Pythagorean host this is the new space-square
predicate.  In the paired-Gaussian/squareclass coordinates it may be rewritten as
a squareclass equality; geometrically it is a degree-two space-square cover.
These are equivalent faces of one added condition, not independent constraints to
be multiplied together.

```text
NEW_ARITHMETIC_MECHANISM=space-square condition on the two-face host
SQUARECLASS_REFORMULATION_IS_NEW_SECOND_CONDITION=false
THIN_COVER_REFORMULATION_IS_NEW_SECOND_CONDITION=false
```

## 2. Certified rarity mechanisms

The audited Stage24/Stage27 stack supplies three logically distinct levels.

- **Geometric rarity:** the space-square lift is a genuine geometrically integral
  degree-two cover, giving qualitative thinness/zero-density information.
- **Local arithmetic rarity:** split-prime valuation parity / squareclass sieves
  give an independent qualitative zero-density route.
- **Quantitative whole-family ceiling:** the current global theorem gives
  `N2(B) <<_epsilon B^(1/2+epsilon)`.

The first two do not, by themselves, explain the numerical half-power exponent.
They must not be multiplied with the global upper theorem as additional power
savings.

```text
GEOMETRIC_ZERO_DENSITY_MECHANISM=PROVED
LOCAL_SQUARECLASS_ZERO_DENSITY_MECHANISM=PROVED
HALF_POWER_RATE_DERIVED_FROM_THINNESS_ALONE=false
HALF_POWER_RATE_DERIVED_FROM_FIXED_PRIME_SIEVE_ALONE=false
ZERO_DENSITY_MECHANISMS_MULTIPLIED=false
```

## 3. What the Stage27 upper reentry actually learned

The r5--r7/r402 campaigns tested several candidate explanations for the half-power
wall.

- Fixed-`R` physical fibers are only `R^o(1)`, but summing over occupied `R` gives
  no new global power saving by itself.
- Exact `kappa` integer/Gaussian factor packets compress local multiplicity, but
  no surviving negative power of the dyadic boundary parameter was proved.
- The old squareclass collision is already the Stage15 condition in another form;
  charging it again would be double counting.
- Fixed-core multiplicity was reduced to divisor size, removing one former
  obstruction, but the realized-core/support energy needed for a global saving
  remains unproved.
- StructureRadar candidates `SR-STR-166/169/161` did not yield a new independent
  determinant/correlation theorem under the repo's current adapters.

Thus the campaign did **not** identify a second independent condition responsible
for `1/2`.  It instead localized the missing information to a whole-family support
or correlation theorem on the same physical measure.

```text
FIXED_R_FIBER_CAUSES_HALF_POWER=false
KAPPA_PACKET_CAUSES_NEW_POWER_SAVING=false
SQUARECLASS_CAN_BE_RECHARGED=false
FIXED_CORE_MULTIPLICITY_OBSTRUCTION_REMOVED=true
GLOBAL_SUPPORT_ENERGY_THEOREM_PROVED=false
HALF_POWER_CAUSAL_MECHANISM_IDENTIFIED=false
```

## 4. What the Stage27 lower reentry learned

The quarter-power lower bound is supplied by explicit Stage19-compatible
construction families.  r8--r10 tested whether it could be improved by:

- lower physical height / stronger polynomial cross-cancellation;
- a thicker moving family with source-count exponent `rho` satisfying
  `rho/h>1/4`;
- Saunderson-type thick families after imposing the space-square condition;
- Peschmann/Master-Hit moving square-lift sections or multisections.

The Saunderson space-square locus collapses to a genus-3 hyperelliptic condition,
so the hoped-for thick two-parameter family is not obtained.  The Peschmann route
currently supplies no moving section/multisection on which the square-lift is
identically satisfied.  No denser Stage19 family was proved.

Therefore the lower mechanism is constructive and genuine, but there is no proof
that exponent `1/4` is intrinsic.

```text
QUARTER_POWER_CONSTRUCTION_PROVED=true
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
QUARTER_POWER_INTRINSIC_PROVED=false
THICK_SAUNDERSON_SPACE_LIFT_PROVED=false
MOVING_TAU_SQUARE_SECTION_PROVED=false
```

## 5. Double-charge verdict

The causal decomposition has one added condition with several representations and
several proof tools.  The following are explicitly forbidden as separate charges:

- squareclass equality on top of the same space-square condition;
- thin-cover rarity on top of the same condition as an independent probability;
- fixed-prime sieve loss multiplied by the global half-power theorem;
- fixed-`R` subpower fiber sparsity multiplied independently after summing over
  `R`;
- Stage15 squareclass collision charged a second time under a new variable name.

```text
DOUBLE_CHARGE_CHECK=PASS
ONE_ADDED_CONDITION_MULTIPLE_REPRESENTATIONS=true
INDEPENDENT_POWER_SAVINGS_PROVED=false
NEXT_DERIVED_ROUTE=27-60c
```
