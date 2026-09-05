# Stage32 post1570 three-involution Q602 batch — terminal symmetry-parity note

## Fixed target

This leaf keeps the audited Stage32 target fixed at `g1-d186`, `O=210`, `qprime=4`, `Q=602`. The surviving mod-2 residue orbit is exactly `73,97,235`. No controller edit or downstream credit is authorized here.

## Route A — exact principal-involution table

Using the retained principal matrices in `post1532-q602-single-b3-commutator.json`, let

- `A0 = b4`,
- `A1 = b3*b4*b3^-1`,
- `A2 = b3^2*b4*b3^-2`.

The exact F2 calculation gives one commuting involution for each surviving residue:

- `73` commutes with `A0` only;
- `97` commutes with `A2` only;
- `235` commutes with `A1` only.

This is a positive finite identification, not an exclusion. Any residue-specific contradiction must therefore force the corresponding commutator to be nonzero **modulo 2**. Integral noncommutation by itself is insufficient.

## Route B — #1570 blow-down detector modulo 2

The #1570 characteristic-zero orbit-sum argument is recomputed from the retained 140-class marking and the full Stoll group of order 1536. The exceptional block is quotiented modulo 2 before testing the H-orbit-sum class.

The result is terminal for this detector:

- retained Stoll group order: `1536`;
- mod-2 blow-down orbit-sum stabilizer count: `1536`;
- stabilizer elements outside H: `1532`;
- hence the mod-2 stabilizer is the full Stoll group, not H.

Thus the numerical noninvariance that powered #1570 in characteristic zero disappears completely after the mod-2 exceptional quotient. It cannot certify `[T,Ai] != 0 (mod 2)` for any of the three residue-specific involutions.

## Route C — degree-2 push-pull does not restore mod-2 injectivity

The common-cover route supplies degree-2 pullback/pushforward relations. Formally, `push_* pull^* = 2 id` on the relevant divisor-class layer. After reduction mod 2 this composite is zero. Therefore degree 2 alone gives no injectivity statement for the mod-2 pullback. This leaf does **not** claim that a kernel is nonzero; it records the narrower exact obstruction that the standard push-pull identity cannot transfer #1570 noninvariance injectively in characteristic 2.

So the failed mod-2 detector cannot be rescued merely by moving to the retained degree-2 common cover.

## Route D — Arsenal routing

Research OS lookup was performed after the exact missing weapon was identified.

`S30-W01` is the formal finite-equivariant-action identification router. Its contract requires a source/common-model semantic anchor before adapter credit. `S32-PW05` is provisional finite-group equivariant reconstruction and explicitly requires the action/invariance hypotheses already to be proved; it must not be used for semantic/geometric identification from reconstructed algebra.

Accordingly, these cards validate the finite reconstruction workflow but do not supply a new geometric invariant whose mod-2 noninvariance would replace the collapsed orbit-sum detector.

## Decision / lane closure

The symmetry-parity route has now been tested at the exact point required to eliminate `73,97,235`: the commutator modulo 2. The retained #1570 blow-down detector collapses under that reduction, degree-2 push-pull does not provide a mod-2 injectivity bridge, and the applicable Arsenal cards do not create the missing semantic invariant.

Therefore this leaf freezes further retries of the same ambient-symmetry / orbit-sum / parity detector. Reentry requires genuinely new input, for example a direct mod-2 divisor/correspondence identity, an independently proved primitive/odd commutator invariant, or another non-automorphism geometric invariant that survives the exceptional quotient.

No arithmetic exclusion is promoted: `Q602_excluded=false`, `O210_excluded=false`, and `O212+` remains unauthorized.
