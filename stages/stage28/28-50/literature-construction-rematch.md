# Stage28-50 — current construction-literature rematch

```text
ROUTE=L3_LITERATURE_CONSTRUCTION_REMATCH
STATUS=SEARCHED_NO_STRONGER_MATCHED_LOWER_FOUND
SEARCH_DATE=2026-08-21
TARGET=M3_OR_N2_PHYSICAL_HEIGHT_POWER_LOWER
```

## 1. René Peschmann 2026 Mordell-Weil generator

Current source checked:

- René Peschmann, `Exponent-one blockers and a Mordell-Weil construction of Euler bricks`, arXiv:2605.00573 (2026).

The paper gives a rigorous correctness theorem for its Mordell-Weil algorithm: every output is a genuine Master-Hit / Euler brick.  It reports more than one million generated Master-Hits across hundreds of elliptic fibers and very large heights.

For Stage28 checkpoint50, however, the required theorem is a **uniform bounded-height lower count** under the repository's primitive/canonical Euclidean cutoff `R<=B`.  The paper does not provide a theorem of the form

```text
# distinct primitive Euler bricks with R<=B >> B^theta
```

with `theta>1/3`, nor a uniform height-versus-Mordell-Weil-coefficient/fiber-count estimate that can be converted to such a theorem.  The paper itself lists height/discriminant control as part of the further theoretical work needed around the fibration.

Therefore the large finite MW database is construction evidence but cannot supersede the generalized Saunderson lower theorem.

```text
PESCHMANN_MW_CORRECT_OUTPUT_THEOREM=true
PESCHMANN_MW_MATCHED_HEIGHT_POWER_LOWER_FOUND=false
PESCHMANN_FINITE_DATABASE_USED_AS_ASYMPTOTIC_PROOF=false
```

## 2. Peschmann master-tuple classification / perfect-cuboid fibers

Checked companion sources:

- arXiv:2604.09328, `Quartic reductions and elliptic obstructions for perfect Euler bricks`;
- arXiv:2604.28072, `A torsion-intersection proof of perfect-cuboid nonexistence on 1,072 explicit master-tuple fibers`.

These sources sharpen the structure of Euler bricks and the deferred perfect-cuboid condition.  The latter includes a structural classification that every primitive Euler brick arises from the standard master-tuple parametrization up to scaling.

That classification is useful for completeness of the parameter space but does not itself give a bounded-height density theorem for master-tuples.  The fiber nonexistence results concern the extra space-diagonal condition and therefore cannot be charged as a Stage28 `M3` construction lower.

```text
MASTER_TUPLE_STRUCTURAL_COMPLETENESS_RELEVANT=true
MASTER_TUPLE_HEIGHT_DENSITY_THEOREM_FOUND=false
PERFECT_CUBOID_FIBER_RESULTS_USED_FOR_M3_LOWER=false
```

## 3. Himane 2024 generator

Checked source:

- Djamel Himane, `Primitive Euler brick generator`, arXiv:2405.13061 (2024).

Himane gives several parametrization templates built from Pythagorean triples, but the non-Saunderson templates retain auxiliary square conditions on the input parameters.  No positive-density parameter count with a matched physical-height estimate is proved there that yields a lower exponent exceeding the generalized Saunderson `1/3` construction.

The classical Saunderson formula reproduced in that paper is exactly the theorem species already used in Stage26 and sharpened by Stage28-50's bounded-fiber inversion.

```text
HIMANE_ADDITIONAL_PARAMETRIZATIONS_REVIEWED=true
HIMANE_MATCHED_POWER_LOWER_GT_ONE_THIRD_FOUND=false
SAUNDERSON_DUPLICATE_REUSE=true
```

## 4. Classical-family / database evidence

Peschmann's 2026 database classifies records matching Saunderson, Lenhart-attributed, and Himane families.  Those counts are finite family tags under generator bounds, not asymptotic physical-height counts.  They do not prove a construction exponent above `1/3`.

No current primary source found in this bounded rematch supplies a stronger Stage20 lower theorem under the exact primitive/canonical `R<=B` measure.  This is a search result, not a novelty claim.

```text
STRONGER_PUBLISHED_MATCHED_M3_LOWER_FOUND=false
NOVELTY_BY_SEARCH_ABSENCE=false
UNBOUNDED_LITERATURE_SEARCH_REQUIRED=false
```

## 5. Stage19 lower-side rematch

The repository's Stage27 lower reentry already explored materially distinct routes beyond the Stage25 quarter-power families: low-height cross-cancellation, higher-density parameter families, Saunderson/Peschmann-compatible square lifts, and moving elliptic sections/multisections.  No `N2` lower exponent above `1/4` survived audit.

The 2026 Peschmann Euler-brick MW construction does not transfer to Stage19: imposing the integral space diagonal on an Euler brick is the deferred perfect-cuboid endpoint, while Stage19 is the exactly-two-face-plus-space stratum.

Thus no current external construction rematch changes

\[
N_2(B)\gg B^{1/4}.
\]

```text
N2_LOWER_GT_ONE_QUARTER_FOUND=false
M3_LOWER_GT_ONE_THIRD_FOUND=false
CURRENT_NEW_PROGRESS=M3_EPSILON_FREE_ONE_THIRD_VIA_INTERNAL_BOUNDED_FIBER
```
