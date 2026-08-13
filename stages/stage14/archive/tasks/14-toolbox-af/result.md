# Stage14-toolbox-af — integral global-small-point witness formulas

## Purpose

Package the exact integerization from merged Stage14-s6-01 as reusable main/s formulas, without reopening the proof and without prematurely mixing in the next kernel-packet layer.

## Canonical cards

```text
TB-FORMULA-rational-witness-denominator
TB-FORMULA-integral-witness-equation
TB-LEMMA-witness-pairwise-gcd-support
TB-BOUND-witness-polynomial-box
TB-RECIPE-physical-to-integral-witness
TB-WARNING-witness-quantifier-and-denominator-boundary
```

## Frozen chain

```text
physical active base
 -> non-torsion global small point
 -> maximally 2-halved nonzero descent class
 -> Z=A/D^2, W=Y/D^3
 -> Y^2=A(A-S^2D^2)(A+X^2D^2)
 -> G0,G1,G2
 -> pairwise overlap support on S/X/H
 -> polynomial witness box
```

Exact identities:

```text
G0=A
G1=A-S^2D^2
G2=A+X^2D^2
G0-G1=S^2D^2
G2-G0=X^2D^2
G2-G1=H^2D^2
G0G1G2=Y^2

gcd(G0,G1)|S^2
gcd(G0,G2)|X^2
gcd(G1,G2)|H^2
```

The count-level implication remains only

```text
V(B)<=J_C(B)<=N_local(B).
```

No converse is introduced.

## Deliberate boundary with toolbox-ag

This stage does not canonicalize the complete signed squarefree factorization

```text
d0=tau0*a*b
d1=tau1*a*c
d2=tau2*b*c.
```

That structure, its 16 sign/2-adic packets, radical support, and five-column refinement are reserved for `Stage14-toolbox-ag` so the integerization and kernel-incidence layers remain separately reusable.

## Boundary

```text
STAGE14_TOOLBOX_AF=COMPLETE_INTEGRAL_GLOBAL_SMALL_POINT_WITNESS_FORMULAS
CANONICAL_NEW_CARD_COUNT=6
RATIONAL_WITNESS_SQUARE_CUBE_DENOMINATOR_FROZEN=true
INTEGRAL_WITNESS_EQUATION_FROZEN=true
PAIRWISE_GCD_EDGE_SUPPORT_FROZEN=true
WITNESS_POLYNOMIAL_BOX_FROZEN=true
PHYSICAL_TO_WITNESS_UPPER_MAJORANT_RECIPE_FROZEN=true
INTEGRAL_WITNESS_IMPLIES_PHYSICAL_RECONSTRUCTION=false
POLYNOMIAL_BOX_PROMOTED_TO_COUNT_SAVING=false
GENERIC_D_IDENTIFIED_WITH_COMPACT_D_T=false
SIGNED_KERNEL_EDGE_PACKET_CANONICALIZED_IN_AF=false
OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-ag odd kernel edge packet and full-radical incidence
```