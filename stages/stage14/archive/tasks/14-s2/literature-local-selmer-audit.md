# Stage14-s2 literature audit — local 2-Selmer support and family boundary

## Scope

This audit asks which external Selmer-distribution theorems can actually be imported for

\[
E_t:y^2=x(x-1)(x+t^2),\qquad t=\frac{2r}{1-r^2},
\]

when `r` ranges over primitive Pythagorean bases.

The standard is deliberately strict: similarity of torsion structure is not enough. A theorem is imported only when the parameter family and ordering hypotheses match the Stage14 setting.

## PARI/GP 2-descent implementation

PARI/GP `ellrank` is the computational implementation used by s1. Its current documentation states that the routine performs 2-descent together with the 2-part of the Cassels pairing and returns unconditional rank bounds. This is computational infrastructure only; s2 does not treat PARI output as an average theorem.

Classification: `REUSABLE_METHOD`.

## Bruin--Stoll: two-cover descent

Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic curves* (2008), give a general explicit two-cover framework, including genus-one applications. This is consistent with the s1/s2 use of square classes supported at bad places and local solubility tests.

Classification: `REUSABLE_METHOD`.

## Alexander Smith: full-2-torsion quadratic twists

Alexander Smith, *2^infinity-Selmer groups, 2^infinity-class groups, and Goldfeld's conjecture* studies quadratic twists of a **fixed** elliptic curve with full rational 2-torsion, under an additional hypothesis excluding a rational cyclic subgroup of order four.

Stage14 does not meet either family hypothesis:

1. its `j`-invariant varies with the Pythagorean base, so it is not a quadratic-twist family of one fixed curve;
2. genuine Stage14 fibers have rational torsion `Z/2 x Z/4`.

Classification: `ADJACENT_RESULT`, **not imported**.

## Pan--Tian: distributions in quadratic-twist families

Jinzhao Pan and Ye Tian study distributions of 2-Selmer ranks in quadratic twists of elliptic curves over `Q` with full rational 2-torsion. This broadens the twist-family picture and is directly relevant context for the effect of rational 2-torsion.

It still concerns quadratic twists of fixed elliptic curves. The non-isotrivial Stage14 Pythagorean-base family is not of that form.

Classification: `ADJACENT_RESULT`, **not imported**.

## Morgan--Paterson: twists after quadratic extension

Adam Morgan and Ross Paterson study 2-Selmer groups of quadratic twists of a fixed full-2-torsion elliptic curve after quadratic extension. Their paper also explicitly illustrates that thin subfamilies can behave differently from the ambient statistical family.

That warning is directly relevant to Stage14, whose Pythagorean parameterization is a structured thin/base-changed family.

Classification: `ADJACENT_RESULT`; statistical conclusions are **not imported**.

## Current boundary

No primary source identified in this audit gives an average 2-Selmer distribution theorem for the exact Stage14 family ordered by primitive Pythagorean base height, much less by the later physical first-hit height `mu(F)`.

This is not a novelty claim. It is only the theorem-import boundary used by s2.

```text
DIRECT_STAGE14_PYTHAGOREAN_BASE_AVERAGE_2_SELMER=NO_MATCHING_THEOREM_IMPORTED
NOVELTY_BY_SEARCH_ABSENCE=false
QUADRATIC_TWIST_DISTRIBUTION_THEOREMS_IMPORTED=false
PARITY_CONJECTURE_IMPORTED=false
BSD_IMPORTED=false
```

## Consequence for s2

The rigorous s2 contribution is therefore repository-local:

- exact projective densities for when an odd prime enters the moving bad set `p|SXH`;
- the good-prime/unramified boundary;
- the `4^(omega(2SXH)+1)` ambient cover-class envelope;
- identification of the fixed-prime product-sieve obstruction.

A genuine average-Selmer theorem for this Pythagorean base change remains future work rather than an assumed black box.
