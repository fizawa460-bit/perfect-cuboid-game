# Stage14-4cj — xi rank-two elimination and rank-one physical rigidity

Stage14-4cj consumes merged `14-4ci` and `14-s7-23`.

The `xi` short CRT span is now shown to have physical rank exactly one.  Rank three was eliminated by s7-23.  Rank two is eliminated by applying the four cell-square CRT congruences to the Plucker minors of two endpoint-short vectors: the four mixed minors are divisible by `R^2,J^2,S^2,T^2`, while every such minor is only `B^(1/8+o(1))`; since every balanced cell square is at least `B^(1/4-o(1))`, all four mixed minors vanish.  The Plucker relation then forces one endpoint pair of columns to vanish, contradicting positivity of the physical root vector.

Thus every surviving physical packet has `xi` short span rank exactly one.  Reducedness makes the actual physical root vector primitive, so a fixed legal oriented xi-CRT packet contains at most one physical root vector.

This is a rigidity theorem, not yet a whole-family saving: the moving rank-one cell/orientation packet multiplicity over the common-core residual support remains to be counted.

Current whole-family exponent: `7/8`.

Next: `Stage14-4ck`.
