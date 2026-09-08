# Stage32 MAIN scratch — FSM node-fiber injectivity exclusion

Status: scratch proof-extension candidate only. No MAIN authority, claim-DAG, Q602, O210, receiver, theorem, endpoint, or Perfect Cuboid credit.

## Published input

Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), Theorem 3.1 and proof; author preprint printed pp. 10--11.

The published theorem assumes that the normalization map `Cbar -> C` is globally bijective. Inspection of the proof shows the explicit use of this hypothesis at the pole-count step: after pulling the meromorphic tensor to `Cbar`, the authors say that bijectivity implies `Cbar` can meet each of the 48 exceptional curves at most once, hence the pole set has at most 48 points.

The rest of the relevant bookkeeping is local on `Cbar`:

- the tensor is holomorphic outside the exceptional curves;
- at a node branch the translation pair satisfies `a1,a2>0`, both divisible by 4, with `a1+a2` divisible by 8;
- a branch pole has order at most `(16-(a1+a2))k`, hence at most `8k`;
- the pulled-back tensor has divisor degree `16(2g-2)k`;
- the chosen modular form contributes at least `2kd` zeros and is chosen nonzero at the nodes.

A singularity of the curve over the smooth ambient locus does not create a pole because the ambient tensor is holomorphic there. Ramification of the normalization map at such a point can only add vanishing to the pullback, which strengthens the zero lower bound rather than weakening the pole estimate.

Therefore the same pole/zero argument applies under the weaker hypothesis:

`the normalization has at most one preimage over each box-surface node`.

This is a derived proof inspection, not a theorem stated verbatim by Freitag--Salvati Manni.

## V6 arithmetic

For the fixed V6 target:

- `g=1`, `d=186`;
- the strict transform meets 47 exceptional curves positively;
- zeros are at least `2kd=372k`.

Under node-fiber injectivity there is at most one normalization branch over each of those 47 nodes. If any one of these branches is nonminimal, then its lattice sum satisfies `a1+a2>=16`, so it contributes no positive pole. The other 46 branches contribute at most `8k` each. Thus total poles are at most

`46*8k = 368k < 372k`,

contradicting the genus-one identity

`0 = #zeros - #poles`.

Hence all 47 unique node branches must be the unique pole-producing lattice type below sum 16, namely `(a1,a2)=(4,4)`.

The retained A1 resolution calculation gives exceptional intersection multiplicity exactly 1 for a `(4,4)` branch. Under node-fiber injectivity this forces total V6 exceptional mass `47`, but the exact retained V6 exceptional mass is `266`. Contradiction.

## Consequence

There is no integral geometric-genus-1 V6 carrier whose normalization is injective over every box-surface-node fiber.

Thus, if a V6 genus-1 carrier exists, it must have at least one box-surface node with two or more normalization preimages. Smooth-locus noninjectivity may coexist, but it cannot be the only failure of bijectivity.

Combining this with the elementary branch-count filter `#branches <= V6.E_i`, the required multibranch node must have `V6.E_i>=2`. Therefore only 38 of the 48 exceptional labels remain possible:

`[4,5,8,9,10,11,12,13,14,16,17,18,19,21,23,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48]`.

This does not identify the exact node and does not exclude the carrier itself.
