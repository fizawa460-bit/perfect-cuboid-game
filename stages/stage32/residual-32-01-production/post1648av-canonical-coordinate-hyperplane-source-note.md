# Stage32 post1648AV — canonical coordinate-hyperplane recovery source note

Scratch-only source note. No Stage32 MAIN / receiver / route / theorem / endpoint credit is granted by this file.

## Primary source

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675–691, DOI `10.1307/mmj/1480734014`.

Author preprint:
`https://www.mathi.uni-heidelberg.de/~freitag/preprints/box.pdf`

Exact locators used here:

- §2, Proposition 2.6 (printed pp. 8–9): the 32 smooth rational curves are exactly the zero set of a modular form equal to `4 i W1 W2 W3 C`; the proof states that each of `W1=0`, `W2=0`, `W3=0`, `C=0` consists of 8 rational curves.
- §2 immediately before Proposition 2.6 (printed p. 8): the box variety has 48 nodes and the minimal resolution has 48 exceptional lines.
- §3 immediately before Theorem 3.1 (printed p. 10): the canonical map of the minimal resolution is the composition with the original box embedding `B -> P^6`; therefore projective degree equals intersection with the canonical divisor.

## Elementary 48-node coordinate-incidence replay

The four defining quadrics in the source introduction are diagonal in the seven projective coordinates. Writing squared coordinates in the order
`(Z1^2,Z2^2,Z3^2,W1^2,W2^2,W3^2,C^2)`, their linear coefficient matrix is

`[0,0,-1,1,1,0,0]`
`[0,-1,0,1,0,1,0]`
`[-1,0,0,0,1,1,0]`
`[0,0,0,1,1,1,-1]`.

For a projective point with a fixed nonzero-coordinate support, Jacobian rank drops below four exactly when the corresponding restricted coefficient matrix has rank below four. Exact rational support enumeration gives precisely six one-dimensional squared-coordinate solutions with four nonzero coordinates. In terms of which of `{W1,W2,W3,C}` vanish, the six types are all six unordered pairs:
`{W1,C}`, `{W2,W3}`, `{W1,W3}`, `{W2,C}`, `{W1,W2}`, `{W3,C}`.
Each type has four nonzero projective coordinates and therefore `2^(4-1)=8` sign lifts, giving `6*8=48` singular points, exactly the source node count.

Consequently every box node lies on exactly two of `W1=0,W2=0,W3=0,C=0`, and every one of those four coordinate hyperplanes contains exactly `3*8=24` box nodes. This incidence statement is thus replayed directly from the source-locked defining equations rather than imported as an unsupported semantic assumption.

## Exact retained-Picard recovery used in AV

The AV diagnostic imports the two permanent-denylist retained Picard payloads runner-side only and emits no retained payload. It reconstructs the full known140 intersection matrix through the existing `HperpIntegralPairingAdapter`.

Among the first 32 normal rational curves it searches for 8-curve subsets satisfying the source geometry of one coordinate hyperplane:

1. the eight rational components are pairwise disjoint on the resolved surface;
2. exactly 24 exceptional curves are incident to those components;
3. every selected exceptional curve is incident to exactly two selected rational components, and every other exceptional curve to zero.

This yields 28 single-hyperplane candidates.

For the unordered four coordinate hyperplanes `{W1=0,W2=0,W3=0,C=0}`, AV then imposes the simultaneous source condition that:

- all 32 rational curves occur exactly once across the four zero divisors;
- all 48 box nodes occur exactly twice across the four coordinate hyperplanes.

This leaves 25 exact covers. The retained V6 intersection vector gives, across all admissible covers, per-hyperplane exceptional mass between 110 and 168, strictly below `K.C=186`. Every exact cover has total exceptional mass `532=2*266` and total rational contribution `212`, and each individual candidate satisfies `exceptional mass + rational contribution = 186`.

## Scope

This is a bounded canonical-coordinate-hyperplane recovery and capacity diagnostic. It does not identify a unique ordered labeling `(W1,W2,W3,C)`, does not match the retained 48 exceptional labels to explicit box-coordinate nodes, and does not prove that AO's total normalization-preimage lower bound is concentrated in one coordinate hyperplane.

Therefore AV does not exclude a V6 genus-one carrier. Its next useful interface is an explicit/equivariant matching between the 48 box-coordinate nodes and the 48 retained exceptional labels, after which one can study general hyperplanes containing many relevant nodes rather than only the four coordinate hyperplanes.
