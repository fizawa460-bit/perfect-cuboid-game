# Stage27-18 — Stage18 re-excavation roadmap

```text
TASK_ID=Stage27-18-roadmap
OWNER_STAGE=Stage27
ROLE=STAGE18_TO_STAGE19_TRANSFER_REEXCAVATION
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
STAGE18_ABSOLUTE_ASYMPTOTIC=M2(B)~C_M2*B*(log B)^5
STAGE18_REPROOF_REQUIRED=false
PRIMARY_GOAL=decompose the settled Stage18 mass into Stage19-relevant coordinates and quantify survival after imposing the integral space-diagonal condition
ADVANCE_TO_CHECKPOINT50=false
```

## 1. Scope lock

Stage18 itself is already closed at the asymptotic resolution

`M2(B) ~ C_M2 B (log B)^5`, `C_M2>0`,

for primitive canonical exactly-two-face cuboids under the common physical cutoff `R<=B`, with no space-diagonal integrality requirement.

Stage27-18 therefore must not reopen Stage18's absolute upper/lower theorem.  Its purpose is to reuse that settled population law as a source measure for the Stage18 -> Stage19 transition.

The live question is:

> Where does the `B(log B)^5` Stage18 mass live in the arithmetic/toric coordinates used by Stage19, and how much of that mass survives the additional condition that the space diagonal is integral?

## 2. Main route

### 27-18a — BASELINE_REAUDIT

- lock the literal Stage18 population, cutoff, primitivity, canonical ordering, and physical-object multiplicity;
- verify direct compatibility with the Stage19 source population before the space-diagonal predicate is imposed;
- forbid measure/height/multiplicity substitutions.

### 27-18b — PARAMETRIC_NORMAL_FORM_EXTRACTION

Start from the shared-edge normal form

`s^2+x^2=p^2`, `s^2+y^2=q^2`, `x^2+y^2 not square`,

and translate the Stage18 population into the same toric / slope / core coordinates used by Stage19 (`m,n,r,s`, and where legal `tau,g,kappa,R`-type coordinates).

Target: an exact many-to-one/finitely-many-to-one interface with all primitive/canonical/exactly-two masks retained and no polynomial multiplicity loss.

### 27-18c — ARSENAL_REMATCH

Rematch StructureRadar / Arsenal against the Stage18 source measure, specifically looking for tools that may be ineffective after the space-diagonal constraint but strong before it.

Candidate weapon species:
- divisor distribution / hyperbolic counting;
- coupled Pythagorean-pair incidence;
- squareclass and Gaussian factorization structure;
- determinant/incidence estimates;
- quadratic/large-sieve inputs;
- support-energy or moment estimates.

No weapon is credited merely because it reproves the already-settled Stage18 asymptotic.

### 27-18d — MASS_LOCALIZATION

Decompose the settled Stage18 mass into Stage19-relevant dyadic coordinates.  Candidate localizations include reduced-direction height, realized core, common squarefree kernel, fixed/shared-edge fibers, occupied diagonal/support variables, and critical slope bands.

Target species:

`M18,T(B)` asymptotics or matched upper/lower estimates on the same physical measure.

The purpose is to identify whether the full `B(log B)^5` mass is concentrated in precisely the bands that later form the Stage19 half-power wall.

### 27-18e — SPACE_DIAGONAL_SURVIVAL_RECEIVER

On the exact Stage18 source measure, impose

`s^2+x^2+y^2 = R^2`

and formulate the Stage18 -> Stage19 survival operator without independence assumptions.

Target: a zero-loss or quantified-loss weighted transfer connecting localized Stage18 mass to Stage19 occupied support / object count.

A theorem of the form

`M19,T(B) <= B^{-delta+o(1)} M18,T(B)`

on all relevant bands would be sufficient for a new upper saving; a matched lower survival theorem on a positive-dimensional subfamily would strengthen the lower route.

### 27-18f — LOWER_TRANSFER

Search inside high-mass Stage18 families for space-diagonal-surviving subfamilies.

Relevant interfaces include the Stage27-19 r8/r9 lower construction program, especially thick moving families and Saunderson-type two-parameter sources.  The required output is an actual physical Stage19 family with controlled height and finite-to-subpower multiplicity, not merely many Stage18 objects.

### 27-18g — UPPER_TRANSFER

Search for same-measure suppression showing that the space-diagonal condition kills a fixed power of the localized Stage18 mass.

Admissible outputs include:
- fixed-power support deficit;
- weighted second-moment/energy deficit;
- determinant/incidence suppression;
- new nonduplicate sieve condition;
- a legal Gaussian/character adapter preserving the physical measure.

Do not recharge Stage15 squareclass, already-paid core/divisor entropy, or an unweighted theorem on a larger host.

### 27-18h — CHECKPOINT50_RECOMPUTE

Feed all proved localization/survival information back into the Stage27 comparison controller and recompute the 18 -> 19 thinning statement.

Checkpoint50 may advance only if the re-excavation produces genuinely new fixed-power information or a stronger certified lower survival exponent.  Repackaging `M2(B)~C B(log B)^5` alone is not progress.

## 3. Priority order

```text
PRIMARY_CHAIN=27-18b -> 27-18d -> 27-18e
SECONDARY_UPPER=27-18g
SECONDARY_LOWER=27-18f
ARSENAL_REMATCH=27-18c
FINAL_RECOMPUTE=27-18h
```

The main conceptual shift is that Stage18 is treated as a completed source theorem, not a stage needing better absolute bounds.

## 4. Anti-loop policy

Forbidden:
- trying to improve the Stage18 absolute exponent `1` when the asymptotic is already matched;
- reproving `B(log B)^5` under an equivalent parameterization;
- charging Stage15 squareclass/common-core conditions a second time;
- using finite census data as an asymptotic theorem;
- importing a different-measure or larger-host saving without an explicit adapter;
- creating renamed subroutes after a receiver has been reduced to a theorem gate with no new input.

## 5. Success criteria

Stage27-18 is useful if it yields at least one of:

1. a Stage18 mass-localization theorem on Stage19-relevant bands;
2. a same-measure fixed-power survival deficit for adding the space diagonal;
3. a stronger Stage19 lower family arising from a high-mass Stage18 source;
4. a new legal StructureRadar/Arsenal receiver that was invisible when attacking Stage19 directly;
5. a revised Stage27 checkpoint comparison with strictly stronger certified information.

```text
CURRENT_STAGE18_EXPONENT=1
CURRENT_STAGE18_LOG_POWER=5
STAGE18_ABSOLUTE_LAW_REOPENED=false
SPACE_DIAGONAL_SURVIVAL_FIXED_POWER_PROVED=false
NEW_STAGE19_UPPER_EXPONENT_PROVED=false
NEW_STAGE19_LOWER_EXPONENT_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_EXPECTED_COMMAND=Stage27-18-audit
```
