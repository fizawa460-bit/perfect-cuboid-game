# Stage14 external theorem import contract

This contract governs every literature theorem used as a proof input in Stage14 main/s work. A theorem is not imported because its conclusion has the desired shape; it is imported only after the live Stage14 object is mapped to the theorem hypotheses and all exceptional strata are closed.

## Import states

```text
CANDIDATE
HYPOTHESIS_MAPPED
REJECTED
IMPORTED
```

- `CANDIDATE`: theorem located but hypotheses not yet mapped.
- `HYPOTHESIS_MAPPED`: every required hypothesis has a repository proof/check or explicit open gate.
- `REJECTED`: at least one required hypothesis fails for the proposed specialization.
- `IMPORTED`: all hypotheses for the exact specialization are proved, exceptions are treated, uniformity is correct, and the theorem output is connected to the intended receiver.

`REJECTED` is a useful terminal result. It must not be silently changed back to `CANDIDATE` by citing the same theorem under a different informal description.

## Mandatory theorem identity

```text
THEOREM_AUTHOR=
THEOREM_TITLE=
THEOREM_YEAR=
THEOREM_LOCATOR= theorem/corollary/section identifier
THEOREM_ROLE=
EXACT_CONCLUSION_USED=
```

A paper-level citation without locator and exact conclusion is insufficient for `IMPORTED`.

## Mandatory hypothesis map

```text
BASE_FIELD_AND_CHARACTERISTIC=
NUMBER_OF_MOVING_VARIABLES=
ADDITIVE_CHARACTER=
MULTIPLICATIVE_CHARACTERS=
CHARACTER_ORDERS=
DOMAIN_OR_TORUS=
DIVISOR_OR_NEWTON_SUPPORT=
SMOOTHNESS_OR_SNC_CONDITION=
NONDEGENERACY_CONDITION=
LOCAL_MONODROMY_CONDITION=
INFINITY_OR_COMPACTIFICATION_CONDITION=
FREQUENCY_OR_PARAMETER_CHAMBERS=
EXCEPTIONAL_PARAMETERS=
BAD_PRIMES=
UNIFORMITY_PARAMETERS=
COMPLEXITY_CONSTANT_DEPENDENCE=
OUTPUT_SCALE=
```

Each nontrivial entry must point to a merged repository derivation or to the external theorem statement. If an item is not required by the theorem, record `NOT_REQUIRED` rather than omitting it.

## Stage14 object map

Explicitly identify live variables with theorem variables:

```text
STAGE14_POLYNOMIAL_OR_SHEAF=
THEOREM_POLYNOMIAL_OR_SHEAF=
STAGE14_ADDITIVE_FREQUENCY=
THEOREM_ADDITIVE_PARAMETER=
STAGE14_GOOD_PRIME_CONDITION=
THEOREM_CHARACTERISTIC_EXCLUSIONS=
```

A theorem about a fixed object is not automatically uniform in a moving Stage14 packet.

## Exception split

Before applying a generic theorem, partition every excluded parameter/frequency/stratum and give it a receiver:

```text
GENERIC_CHAMBER -> external theorem
EXCEPTION_1     -> exact cancellation / lower-dimensional theorem / direct count
EXCEPTION_2     -> ...
BAD_PRIMES      -> finite or B^o(1) charge with proof
BOUNDARY        -> explicit boundary lemma
```

The generic theorem is not exhaustive until all exceptions are closed.

## Output transfer

An imported complete-sum theorem occupies only one receiver level:

```text
external complete-sum bound
 -> CRT / modulus composition
 -> Fourier completion
 -> square/large sieve
 -> packet or fiber count
 -> sector count
 -> exhaustive whole-family recombination
```

No arrow may be skipped because the exponents merely look compatible.

## Evidence versus theorem

Finite-field enumeration, numerical traces, symbolic discriminants, and small-prime checks are regressions and hypothesis diagnostics. They do not replace a uniform theorem.

## Live Stage14 case study

### Rejected shortcut: Katz 2007 nonsingular-polynomial route

For

```text
H(R,S)=(1-R^2 S^2)(S^2-R^2),
```

the top homogeneous piece contains repeated factors `R^2 S^2`. Merged s7-10 records

```text
DIRECT_KATZ_2007_DELIGNE_POLYNOMIAL_SHORTCUT_APPLICABLE=false.
```

### Imported route A: Katz--Laumon stationary phase

Merged s7-10 maps the finite divisor to four multiplicity-one SNC components, proves nontrivial quadratic Kummer monodromy, treats generic stationary points as isolated Morse points, controls infinity by nontrivial Artin--Schreier phase, and closes diagonal/axis exceptions separately. This yields the all-frequency `O(p)` mixed transform.

### Imported route B: Lei Fu Newton-polyhedron theorem

Merged 4by performs a four-Kummer Gauss lift to a six-variable Laurent polynomial, proves full-dimensional Newton support and face nondegeneracy for `h != +/-k`, and proves exact zero on the exceptional frequency lines. Lei Fu Corollary 0.3 gives the torus `O(p)` scale; axes are handled directly.

These are two valid imports of the same receiver. They are cross-checks, not multiplicative savings.

## Theorem consequence versus current global ledger

The imported all-frequency two-cell transform gives the reusable theorem

```text
N_2cell(R,S) << (RS)^(2/3) B^o(1)
```

and historically yielded

```text
V(B) << B^(13/14+o(1)).
```

Merged s7-13 later reuses this same two-cell theorem inside a finer full-coordinate common refinement and improves the terminal whole-family ledger to

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
CURRENT_REMAINING_GAP_TO_SQRT=3/8
FULL_COORDINATE_REFINEMENT_ARCHITECTURE_BARRIER=7/8
```

Thus an external theorem import can remain current as a receiver even after the global exponent it first produced becomes historical.