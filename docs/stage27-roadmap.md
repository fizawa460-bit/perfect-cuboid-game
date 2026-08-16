# Stage27 roadmap — true `N2` exponent attack

```text
STAGE=Stage27
PROGRAM=TRUE_N2_EXPONENT_ATTACK
TRANSITION=Stage18 -> Stage19
SOURCE=M2: primitive canonical exactly-two-face cuboids, no space requirement
TARGET=N2: same physical objects with R integral
CUTOFF=R<=B
LITERAL_SUBSET_TRANSITION=true
STARTS_AFTER=Stage26 closeout audit PASS and PR #1020 merge
OPERATOR_SELECTION=Stage27-main-batch
```

## Purpose

Stage27 attacks the unresolved quantitative growth law of

\[
N_2(B),
\]

the primitive canonical exactly-two-face population with integral space diagonal under the exact Euclidean cutoff `R<=B`.

The current audited surface is

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}},
\]

with directional lower bounds

\[
\boxed{N_{2,j}(B)\gg_j B^{1/4}},\qquad j=a,b,c.
\]

The true exponent is not identified. Stage27 must try to shrink this interval; it must not infer a true exponent from finite data or from unrelated Stage26 Euler-cuboid counts.

## Checkpoint order

| Checkpoint | Role | Required output |
|---|---|---|
| `10` | contract + reuse preflight | freeze current `N2` theorem surface, exact population/cutoff/multiplicity, and legal attack routes |
| `20` | matched finite diagnostic | reuse the exact Stage19/Stage14 census to measure effective exponents/directional balance; diagnostic only |
| `30` | corridor normalization | express precisely what an improved lower or upper theorem would imply for `N2/M2`, directional survival, and Stage23/24 receivers |
| `40` | upper attack | seek a strict sub-square-root whole-family upper using same-measure squareclass/thin-cover/moving-family tools; fixed-prime zero-density alone is insufficient |
| `50` | lower attack | generalize or replace R501/R502/Meskhishvili constructions; target exponent strictly above `1/4` with primitivity, height, injectivity/fiber control and exact-two exception control |
| `60` | deep gap attack | combine all compatible lower/upper discoveries, open derived routes when genuinely new, and attack the remaining exponent gap as far as repo-native methods permit |
| `70` | bounded synthesis | freeze the strongest audited `N2` corridor, propagate receivers, promote reusable weapons if warranted, and close Stage27 |

## Mandatory incoming interfaces

1. `stages/stage19/post-stage25-50-supersession.md`
   - `N2(B)>>B^(1/4)`;
   - `N2(B)<<_epsilon B^(1/2+epsilon)`;
   - all three directional `N2,j(B)>>_j B^(1/4)`;
   - true exponent open.
2. `stages/stage24/post-stage25-r01/result.md`
   - literal Stage18->Stage19 survival ratio;
   - global/directional quarter-power survival lower;
   - zero density remains proved.
3. `stages/stage25/25-reentry-20/result.md` and audited r008a backflow
   - R501/R502 cone mechanisms;
   - current one-quarter lower is not proved optimal;
   - moving-family/growing-modulus uniformity remains open.
4. `stages/stage26/26-70/self-contained-bundle.md` and `docs/stage26-arsenal-promotion.md`
   - method reuse is allowed only after population compatibility checks;
   - the generalized Saunderson `M3` lower is **not** an `N2` lower theorem.

## Lower-side attack contract

The current quarter-power constructions have parameter mass of quadratic size with physical height of order `T^8`, giving the `B^(1/4)` scale after bounded-fiber/exact-two control.

A genuine exponent upgrade must produce at least one of:

```text
MORE_PARAMETER_MASS_AT_COMPARABLE_HEIGHT=true
LOWER_HEIGHT_DEGREE_WITH_COMPARABLE_PARAMETER_MASS=true
NEW_HIGHER_DIMENSIONAL_PRIMITIVE_FAMILY=true
NEW_FIBER_CONTROL_UNLOCKING_EXISTING_REDUNDANT_PARAMETERS=true
```

Every lower theorem must prove:

- primitive physical output;
- strict canonicalization or a bounded multiplicity adapter;
- exact `R<=B` height control;
- integral space diagonal;
- exactly two, not three, integral face diagonals except for a controlled exceptional set;
- distinct-object count after fibers/symmetries.

Stage26's `w^3` divisor-fiber argument is a methodological template only; it cannot be transferred without a new invariant for the Stage19 population.

## Upper-side attack contract

The current whole-family upper is

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

A genuine upper improvement requires a same-measure theorem that yields a polynomial saving beyond the existing half-power boundary. Candidate mechanisms include:

- moving-family or growing-modulus uniformity for the squareclass parity sieve;
- a stronger rational-point count on the space-square cover;
- a new height-monotone descent/torsor restriction;
- an external theorem with an exact population/height adapter.

Forbidden shortcuts:

```text
FIXED_PRIME_ZERO_DENSITY_AS_POWER_SAVING=false
MULTIPLY_INDEPENDENT_SAVINGS_WITHOUT_JOINT_THEOREM=false
K3_OR_THIN_COVER_MANIN_SUBTRACTION=false
FINITE_EFFECTIVE_EXPONENT_AS_THEOREM=false
```

## Stage27 success classes

```text
CLASS_A=true exponent/asymptotic identified
CLASS_B=global exponent interval strictly narrowed
CLASS_C=one side strictly improved, other side unchanged
CLASS_D=no exponent improvement, but a new audited obstruction/negative certificate or reusable theorem interface is proved
```

A Stage27 closeout may legitimately be `CLASS_D`; it must not manufacture progress.

## Stage28 boundary

Stage19's frozen bundle assigns cross-transition synthesis to Stage28. Stage27 therefore focuses on the `N2` growth law itself and its immediate Stage18/23/24 receivers. It does not pre-empt a future Stage28 global synthesis.

## Commands

```text
Stage27-main-batch
Stage27-audit
```

One `main-batch` executes only the current authorized checkpoint and already-authorized derived work. Fresh theorem-changing output must receive a fresh hostile audit before merge or propagation.
