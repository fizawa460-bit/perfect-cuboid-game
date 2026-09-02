# Stage32 post-1484 O=188 q'=4 symmetry-breaking provenance source scan

Scope: bounded source scan for the remaining B/C defect-to-retained-boundary pointwise bridge. This note does not close O=188 and does not promote any provisional replay.

## Pinned primary source checked

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, arXiv:1303.6495v1 / DOI 10.1307/mmj/1480734014.

Relevant locators:

- Section 2, Proposition 2.5 and the paragraph immediately before it.
- Section 3, proof of Theorem 3.1, local calculation at a node.
- Section 4, Lemma 4.1, already source-locked upstream for the free V4 action on X(8).

## Exact source boundary

Section 2 states that the 48 singular zero-dimensional cusps form one orbit under `Delta(1,2)`. The singular orbit is represented modularly by diagonal cusp types such as `(infinity,infinity)`, `(0,0)`, `(1,1)` before passage through the finite covering description.

Section 3 then performs the local curve calculation at a node by choosing, as a representative, the image of `(infinity,infinity)`. The local branch is encoded by the translation-lattice exponents `(a1,a2)` with

- `a1 == a2 == 0 mod 4`,
- `a1+a2 == 0 mod 8`,
- `a1,a2 > 0`.

This local calculation is exactly the source of the Stage32 contact-exponent adapter, but it does not attach a carrier-specific stable identifier selecting one of the 48 singular nodes. The theorem is applied at a representative node and its local exponent data are node-label-free.

## Consequence for the current leaf

The primary FSM local-cusp source does **not** supply the missing q'=4 symmetry-breaking provenance. In particular, re-reading the same Section 3 exponent calculation cannot select one retained boundary label from the currently unexcluded 6 quotient cusps / 12 retained labels certified by `post1484-o188-q4-current-constraint-nonuniqueness.json` (`b623b1ce...`).

A future uniqueness/transport proof must therefore import a genuinely carrier-specific datum not present in the current FSM local exponent package, for example a source-preserving point/formal-branch identifier or another source-locked invariant that breaks the relevant node/cusp symmetry.

## Firewalls

- This note does not prove that no external geometric uniqueness theorem exists.
- It does not say that all 48 nodes or all 12 retained labels are geometrically realized by B/C.
- It does not permit choosing a node from automorphism symmetry, counts, contact histograms, local saturation, or q'=2 labels.
- It does not close B, C, O=188, the receiver, route, theorem, endpoint, or perfect-cuboid problem.
- FULL178 remains inactive.

Next search boundary: do not repeat FSM Sections 2/3 local-exponent inspection. Search only for carrier-specific q'=4 provenance or a new symmetry-breaking invariant with an authorized comparison to the audited 48-node/retained-label frame.
