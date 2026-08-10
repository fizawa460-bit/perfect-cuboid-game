# Selector-sensitive two-modulus second-moment gap

```yaml
ID: TB-LEDGER-selector-sensitive-two-modulus-gap
TYPE: LEDGER
STATUS: CURRENT
TITLE: t50 isolates the live selector-sensitive two-auxiliary Gaussian second-moment theorem and triggers tH14
SCOPE: BOTH
SOURCE_STAGE: Stage14-t50
SOURCE_PR: 439
SOURCE_MERGE_SHA: 72dd462552e64c312c13746f4533c5ef7512d52a
SOURCE_FILES:
  - stages/stage14/14-t50/result.md
  - stages/stage14/14-t49/result.md
```

## INPUT

The good two-auxiliary Frobenius kernel after the external bad-prime aggregate has been removed.

## OUTPUT

Merged t50 isolates the required theorem

```text
sum_{p!=q} |sum_R S_R(p,q)|^2
 << P^2*(sum_R ||w_R||_2^2)*B^o(1)
```

while preserving signed common refinement, the shared `U/V` modulus group, divisor-coupled hyperbola, physical/canonical selector, and two distinct split primes.

Frozen status:

```text
EXTERNAL_BAD_AUXILIARY_AGGREGATE_BOUND_PROVED=true
SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_REQUIRED=true
SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_PROVED=false
GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED=false
TH14_NEEDED=true
```

## VARIABLE DICTIONARY

- `R`: common disjoint refinement block.
- `S_R(p,q)`: selector-sensitive weighted two-prime character sum.
- `p,q`: distinct split auxiliary primes.

## USED BY

- t51/tH14 support work.
- Main/s bridge planning from the direct `(xi,k)` collision obstruction.

## DO NOT USE FOR

- This theorem is not yet proved.
- Even if proved on the t/tH operator, main/s exponent promotion still requires an exact bridge to the live main/s receiver.

## PROVENANCE NOTES

Merged t50 closes the bad-prime side and identifies this as the remaining good-kernel theorem.