# MB104 Z46 — log Bogomolov–Miyaoka correction preflight wall — 2026-09-19

Status: **PRE-AUDIT SOURCE-CLASS MISMATCH / CONTRACTION-LOCAL-EULER ROUTE FROZEN / NO CREDIT**

## Target

Z45 applies Sabatino's open-surface orbibundle inequality to the exact complete null boundary and leaves the size-48 surviving supports with asymptotic positive margin

```
4/3.
```

Z46 asks one deliberately narrow question:

> Is there a source-valid local correction for the actual non-log-canonical index-three Q-Gorenstein contraction singularities whose signed contribution is known to exceed this margin?

If not, contraction-local-Euler methods are to be frozen rather than extended by analogy.

## Exact retained surface class

Z41/Z41B give the contraction

```
phi:S -> Y
```

with

```
O_S(P)=phi^* O_Y(3K_Y),
3K_Y ample Cartier,
K_Y^2=112/3,
e(Y_reg)=16.
```

For every nonrational contracted point in the surviving supports, the canonical index is exactly three.

The retained graph/discrepancy computation does **not** classify these singularities as quotient, klt, log terminal, log canonical, or as a named analytic type. Z42 and Z43 already firewall precisely those transfers.

## Literature/source gate

The relevant standard local-orbifold framework found in the source search is Adrian Langer,
*Logarithmic orbifold Euler numbers of surfaces with applications*.

Its advertised BMY-type inequality is proved in the **log canonical** case for normal surface pairs with Q-divisors. That hypothesis is load-bearing: the current Z41 contraction points are retained as non-lc.

Pietro Sabatino,
*An explicit bound for the log-canonical degree of curves on open surfaces*,
works instead on a smooth projective surface with a simple-normal-crossing boundary and constructs the orbibundle used already in Z45. It does not supply a new singular-point correction for arbitrary non-lc index-three Q-Gorenstein surface singularities.

The search found no source-complete theorem assigning to an arbitrary non-lc index-three Q-Gorenstein surface singularity, from only the retained resolution graph/index data, a local Euler/Chern correction of known sign and magnitude usable in the Z45 inequality.

## Why quotient/klt/lc formulas cannot be imported

The exact active obstruction is not a missing arithmetic evaluation. It is a category mismatch.

A correction formula valid for:

- quotient singularities;
- klt/log-terminal singularities;
- log-canonical pairs;
- or a named analytic local model

cannot be substituted merely because the retained singularity has index three or because an index-one canonical cover exists.

Z43 already proves that the degree-three canonical cover exists but its analytic type is not determined by the retained data. Z44 likewise shows that the local canonical algebra multiplication is not source-locked.

Therefore neither the sign nor the numerical value of a quotient/lc local Euler correction is presently licensed.

## Margin check

For the size-48 supports, Z45 gives

```
min F_48(l)=4(l+57)/(3(l+1)) > 4/3.
```

To create a contradiction by strengthening that same inequality, a valid additional term must have a favorable asymptotic effect exceeding `4/3`.

No source-valid non-lc index-three correction with such a certified sign/magnitude was found.

This is stronger than saying "the correction has not been computed": the available standard correction theorems located in this preflight do not apply to the retained singularity class.

## Disposition

```
SOURCE_VALID_NONLC_INDEX3_LOCAL_BMY_CORRECTION = NOT_FOUND
LANGER_LC_ORBIFOLD_EULER_IMPORT = FORBIDDEN_CLASS_MISMATCH
QUOTIENT_KLT_FORMULA_IMPORT = FORBIDDEN_CLASS_MISMATCH
CANONICAL_COVER_ANALYTIC_TYPE_KNOWN = false
SIGNED_CORRECTION_GT_4_OVER_3 = not_established
CONTRACTION_LOCAL_EULER_ROUTE = FROZEN
```

Per the active-leaf contract, rotate away from contraction-local-Euler methods.

## Next leaf

```
MB104-Z47-POST-CONTRACTION-GLOBAL-RESCORE
```

The next pass should use Z40B/Z41B only as global geometry already earned:

- complete null locus;
- exact descent `P=phi^*(3K_Y)`;
- three surviving balanced support orbits;
- no further local-Euler/orbifold correction assumptions.

Rescore genuinely global mechanisms that can distinguish existence of an irreducible genus-one member of `|lP|` from mere numerical/effectivity data. Do not reopen Z42–Z46 without new analytic local input.

## Firewalls

```
finite_degree_window=false
surviving_orbits_excluded=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
