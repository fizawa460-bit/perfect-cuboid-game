# Stage32EX5-a — BTVA source-side 48-node reconstruction

Scope: source-side reconstruction only for `BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE`. This note does not identify any Stoll/runtime exceptional index with a projective node and grants no Stage32/receiver credit.

## Exact source lock

BTVA use the coordinate order `[x1,x2,x3,y1,y2,y3,z]` on the perfect-cuboid surface `X_pc ⊂ P^6`. The paper gives the complete-intersection presentation

- `y1^2 = x2^2 + x3^2`,
- `y2^2 = x3^2 + x1^2`,
- `y3^2 = x1^2 + x2^2`,
- `z^2  = x1^2 + x2^2 + x3^2`.

The paper states immediately before Theorem 1.2 that `X_pc` has 48 singularities of type `A1`; Theorem 1.2 is the low-genus restriction that uses these singularities. The arXiv v3 ancillary computation `perfectcuboid.out` base-extends to `Q(i)`, constructs the same surface, sets `sing := Support(SingularSubscheme(X));` and asserts `#sing eq 48`.

Pinned locators:
- arXiv `1912.08908v3`, paper p.4, perfect-cuboid display and Theorem 1.2;
- `https://arxiv.org/src/1912.08908v3/anc/perfectcuboid.out`, singular-locus and symmetry computation.

## Exact reconstruction

Write `i^2=-1`. After projective normalization by the first nonzero member of `(x1,x2,x3)`, the 48 nodes split into six explicit 8-point families:

1. `AXIS_X1`: `[1,0,0,0,a,b,c]`;
2. `AXIS_X2`: `[0,1,0,a,0,b,c]`;
3. `AXIS_X3`: `[0,0,1,a,b,0,c]`;
4. `Y1_Z_ZERO`: `[0,1,s*i,0,a*i,b,0]`;
5. `Y2_Z_ZERO`: `[1,0,s*i,a*i,0,b,0]`;
6. `Y3_Z_ZERO`: `[1,s*i,0,a*i,b,0,0]`;

where every displayed parameter is independently in `{+1,-1}`.

The first three families arise over the three coordinate-axis points of the `(x1:x2:x3)` projection. The last three arise when one face diagonal and the body diagonal vanish, with the remaining square roots giving the independent signs.

The retained verifier checks, exactly over `Q(i)`, that:
- all 48 rows satisfy the four defining quadrics;
- the 4×7 Jacobian has rank exactly 3 at every row;
- projective normalization is already canonical;
- all 48 canonical projective tuples are distinct;
- the six family counts are exactly `8+8+8+8+8+8`.

Because the pinned BTVA computation independently asserts that the singular support has exactly 48 points over `Q(i)`, these 48 distinct singular points exhaust that support.

## Exact BTVA -> Stoll projective-model adapter

The pinned Stoll runtime source `MichaelStollBayreuth/Verification`, commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, `Cuboids/cuboids.magma` defines

`Pr6<a1,a2,a3,b1,b2,b3,c>`

with equations

- `a1^2+a2^2-b3^2`,
- `a2^2+a3^2-b1^2`,
- `a1^2+a3^2-b2^2`,
- `a1^2+a2^2+a3^2-c^2`.

Thus the coordinate rename

`(x1,x2,x3,y1,y2,y3,z) -> (a1,a2,a3,b1,b2,b3,c)`

identifies the BTVA complete-intersection model with the Stoll runtime projective model exactly, equation by equation. Stoll then sets `pts := Points(SingularSubscheme(S)); assert #pts eq 48`.

This closes a possible model/convention ambiguity: the Lane-A 48-node table transports directly into Stoll's projective coordinate system by renaming coordinates. It does **not** close the runtime-order ambiguity. The exact adapter is retained separately in `stage32ex5-a-source-to-stoll-model-adapter.json`.

## Label / scale / symmetry convention

The pinned BTVA ancillary computation does not define a canonical node numbering `0..47`; it stores the singular support in `sing` and then forms set/span/orbit objects. Therefore no Magma singular-set iteration order is source authority for a node label.

Lane A introduces deterministic labels only from the six formulas above. These labels are a repository-side adapter, not BTVA terminology.

Projective equivalence identifies multiplication of all seven coordinates by one common nonzero scalar. Independent coordinate sign changes are not projective equivalence; they generally give distinct nodes. BTVA's ancillary computation separately builds a linear automorphism group from simultaneous permutations of `(x1,x2,x3)` and `(y1,y2,y3)` plus coordinate sign changes, then restricts to a determinant-one subgroup used for orbit calculations. Lane A does not quotient the 48 target nodes by that group.

## Remaining BC2-01B gap

Source-side target recovery and the BTVA-to-Stoll **projective-model** adapter are complete, but the load-bearing runtime bridge is still absent: there is no established identification from Stoll exceptional index `k=0..47` (Picard slots `92+k`) to one of the canonical tuples retained here. In particular, BTVA `sing` order must not be assumed to equal Stoll `pts` order, and neither order should be treated as canonical without an exact adapter.

Thus Lane-A reaches its handoff checkpoint with `PASS` for `SOURCE_SIDE_48_NODE_TARGET_RECONSTRUCTION` plus `SOURCE_TO_STOLL_PROJECTIVE_MODEL_ADAPTER`. Overall `BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE` remains unresolved pending the A/B/C/D synthesis.
