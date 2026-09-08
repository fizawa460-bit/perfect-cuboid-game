# Stage32 MAIN scratch — normalization multibranch support filter

Status: scratch exact finite diagnostic only. No MAIN authority, claim-DAG, Q602, O210, receiver, theorem, endpoint, or Perfect Cuboid credit.

## Input

The current AH certificate proves only that an integral geometric-genus-1 V6 carrier cannot have a globally bijective normalization map. Therefore, if such a carrier exists, normalization is noninjective somewhere. The current exact case split is:

1. noninjectivity over an ambient box-surface node; or
2. noninjectivity over the smooth ambient locus, for example a self-node of the curve.

AH also source-locks the A1 local model for each box-surface node and the V6 exceptional intersection multiplicities.

## Local branch-count lemma

Let `pi:X->S` be the minimal resolution of one A1 box-surface node, with exceptional curve `E`, and let `Ctilde` be the strict transform of an integral carrier not containing `E`. Let `nu:Cbar->Ctilde` be its normalization.

The pullback `nu^*(E)` is an effective divisor on `Cbar` of degree

`deg(nu^*(E)) = Ctilde.E`.

Every distinct normalization branch of the downstairs carrier over the contracted node yields a distinct point in the support of `nu^*(E)`, and each such point has positive integer order. Hence

`number of normalization branches over the node <= Ctilde.E`.

In particular, a surface-node multibranch point requires

`Ctilde.E >= 2`.

This is only a necessary condition. Intersection multiplicity is not identified with the exact branch count.

## V6 application

The retained V6 exceptional pairing vector has:

- 47 positive exceptional labels;
- one zero label: `6`;
- nine positive unit labels: `1,2,3,7,15,20,22,24,36`;
- 38 nonunit positive labels.

Therefore the surface-node multibranch branch can occur only among the 38 labels

`[4,5,8,9,10,11,12,13,14,16,17,18,19,21,23,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48]`.

So the exact MAIN case split refines to:

- `SURFACE_NODE_MULTIBRANCH`: one of those 38 nonunit exceptional labels;
- `SMOOTH_AMBIENT_LOCUS_CURVE_SINGULARITY`: still fully open.

The total branch-excess capacity satisfies the purely numerical upper bound

`sum_{m_i>0}(m_i-1) = 266 - 47 = 219`.

This is not an existence statement and does not constrain the smooth-locus singularity branch.

## Decision

This scratch leaf narrows the surface-node location candidate set from 47 to 38. It does not identify the actual nonbijectivity location and does not exclude a V6 genus-1 carrier.
