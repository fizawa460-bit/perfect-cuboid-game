# Stage32 post1648BI — complex-conjugation fixed-set mass partition

Scratch-only bounded diagnostic. This note grants no MAIN authority, theorem, receiver, route, endpoint, Q602, O210, or perfect-cuboid credit.

## Input locked by the scratch leaf

- V6 witness: `stages/stage32/32-21/post1473-v6-witness-body-recovered.json`, canonical `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`.
- BH exact source-lift diagnostic result: `stages/stage32/residual-32-01-production/post1648bh-exact-source-lifts-node-adapter-scratch-result.json`.
- Retained Picard action of actual complex conjugation is loaded runner-side from the existing Stage33 retained Picard data. The permanent giant-payload denylist is not whole-fetched into assistant/chat context.

BH does **not** produce a unique source-node bijection. It produces 256 distinct 48-node bijections which intertwine all tested automorphisms and actual complex conjugation. BI therefore does not promote any node-by-node source labeling.

## Adapter-independent fixed-set lemma

Let `sigma` be complex conjugation on the 48 source nodes, `tau` complex conjugation on the 48 retained exceptional curves, and let `f` be any bijection satisfying

`f sigma = tau f`.

Then

`f(Fix(sigma)) = Fix(tau)`.

Indeed, `sigma(s)=s` implies `tau(f(s))=f(s)`. Conversely, if `tau(e)=e` and `e=f(s)`, then `f(sigma(s))=tau(f(s))=f(s)`; injectivity of `f` gives `sigma(s)=s`.

Therefore the **aggregate** V6 exceptional mass on source conjugation-fixed nodes is independent of which BH bijection is chosen, even though the node-by-node adapter remains nonunique.

## Exact BI replay result

The retained exceptional complex-conjugation permutation has:

- 24 fixed exceptional curves;
- 12 moving conjugate pairs.

For the exact V6 exceptional multiplicity vector of total mass 266:

- mass on the 24 conjugation-fixed nodes = 126;
- mass on the 24 moving nodes = 140.

All 12 moving conjugate pairs have unequal V6 multiplicities.

Independently, applying the retained Picard64 complex-conjugation matrix to the exact V6 Picard64 coordinate row gives a different class. The same non-invariance is reproduced in the spanning known140 pairing vector. Hence the fixed V6 Picard class is **not** invariant under this `Gal(Q(i)/Q)` complex-conjugation action.

## Scope consequence

The `126/140` Q-fixed versus Q(i)-moving aggregate partition is exact and adapter-independent, but it cannot be upgraded to a contradiction by demanding equal multiplicities on conjugate pairs for the fixed V6 class. Such equality would require a separate proof that the relevant carrier/class is invariant under the conjugation action; BI proves the opposite for the current fixed V6 class itself.

Thus the route

`fixed V6 class -> assume Q-defined / cc-invariant carrier -> force conjugate-pair equality -> contradiction`

is invalid and must remain closed unless a separate Galois-class/orbit argument changes the object under study.

This does not exclude a V6 genus-1 carrier and does not localize the normalization nonbijectivity left open by AH.
