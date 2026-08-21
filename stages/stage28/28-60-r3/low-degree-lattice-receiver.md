# Stage28-60-r3 — low-degree lattice receiver after M5 closure

```text
ROUTE=R23_LOW_DEGREE_LATTICE_RECEIVER
STATUS=RESEARCH_REQUEST_READY_FINITE_COMPUTATION_GATE
M5_STATUS=CLOSED_BY_ANTI_INVARIANT_NORM_CONGRUENCE_CANDIDATE
```

The r3 exact Shimada probe closes the degree-five part of the former `M5M6` receiver. The only remaining bounded low-degree source question is degree six.

## Closed source strata

Audited Stage14 gives

```text
physical Stage19 M.C<4 = impossible
physical Stage19 M.C=4 = empty
```

The new r3 anti-invariant congruence gives, for every physical split curve,

\[
-x^2\equiv2(M\cdot C)\pmod4,
\]

where the exact physical anti-invariant lattice has all positive norms divisible by four. Since the positive physical branch is empty, an odd-degree physical curve cannot hide in the ramification locus and cannot be a connected degree-two pullback. Therefore

```text
physical Stage19 odd M-degree = empty candidate
physical Stage19 M.C=5 = empty candidate
```

Fresh audit is required before this is promoted as final theorem state.

## Remaining Stage19 exact finite receiver: M-degree six

Use the Stage14-4ak Shimada embedding of the physical Kummer surface with fixed

```text
GramS0
M
physical deck involution delta
physical fiber/corner labels
AutX0f-equivalence
Galmu/Q-descent data
Wout0 chamber data
```

and classify irreducible physical rational curves satisfying

\[
C^2\text{ arbitrary even as allowed by singular rational normalization},
\qquad M\cdot C=6.
\]

Both geometric mechanisms must be handled:

1. split pairs `C,delta(C)` over a base image `D`;
2. deck-invariant connected pullbacks whose normalization is rational.

For the split mechanism, `L.D=6`, adjunction parity and Hodge restrict the base numerical possibilities. In the smooth-component subcase the familiar candidate anti-invariant norms are `16,20,24`; unlike degree five, all are compatible with the mod-four lattice law. A complete computation must therefore retain the exact gluing/coset condition rather than using norm alone, then impose effectivity, chamber, boundary removal, automorphism quotient, Q-descent and the physical open.

The invariant mechanism must be checked separately; an even physical degree does not force splitting.

A valid finite computation should output

```text
SOURCE_M6_PHYSICAL_CLASSES=<complete classification up to physical equivalence>
SOURCE_M6_SPLIT_CLASSES=<complete classification>
SOURCE_M6_INVARIANT_CLASSES=<complete classification>
SOURCE_M6_Q_RATIONAL_CLASSES=<complete classification>
```

with exact completeness justification from the Shimada lattice/chamber data.

## Stage20 comparison receiver

The target already has a degree-six rational witness from the generalized Saunderson map. For an exact spectrum comparison, one may also classify whether the Stage20 third-face K3 has physical rational curves of degree `<6` under its matched physical quasi-polarization and count degree-six classes up to the same physical-equivalence semantics.

However the source-side M6 classification is the first bounded question needed after the new M5 closure.

## Why this remains intermediate

If source M6 curves exist, the two fixed-curve spectra meet at polynomial exponent `1/3`. If source M6 is empty, the target has a strictly lower known minimal fixed-curve degree than the source.

Neither outcome determines the whole-population bridge. Stage14-4al shows that Stage19 may be governed by a moving first-hit/rank-jump mechanism rather than a finite accumulating set. A global complement theorem is mandatory before fixed-curve spectra can be promoted to `J_28` or `M3/N2` asymptotics.

```text
FINITE_LATTICE_RECEIVER=PhysicalLowDegreeRootSpectrumM6
SOURCE_SURFACE=Stage19 space Kummer
TARGET_SURFACE=Stage20 third-face K3
HEIGHT=physical quasi-polarization under R<=B
SOURCE_M4_REGRESSION=EMPTY_AUDITED
SOURCE_M5=EMPTY_CANDIDATE_BY_R3_CONGRUENCE
TARGET_M6_WITNESS=SAUNDERSON
GLOBAL_COUNT_CONCLUSION_FROM_SPECTRUM_ALONE=FORBIDDEN
ENDPOINT_COUNT_FORBIDDEN=true
AUDIT_REQUIRED=true
```