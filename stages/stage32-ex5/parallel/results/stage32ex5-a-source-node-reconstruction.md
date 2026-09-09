# Stage32EX5-a — BTVA source-side 48-node reconstruction

Scope: source-side reconstruction only for `BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE`. This note does not identify any Stoll/runtime exceptional index with a projective node and grants no Stage32/receiver credit.

## Exact source lock

BTVA use the coordinate order `[x1,x2,x3,y1,y2,y3,z]` on the perfect-cuboid surface `X_pc ⊂ P^6`. The paper gives the equivalent complete-intersection presentation

- `y1^2 = x2^2 + x3^2`,
- `y2^2 = x3^2 + x1^2`,
- `y3^2 = x1^2 + x2^2`,
- `z^2  = x1^2 + x2^2 + x3^2`.

Theorem 1.2 states that `X_pc` has the 48 nodal singularities used in the low-genus restrictions. The arXiv v3 ancillary computation `perfectcuboid.out` base-extends to `Q(i)`, constructs the same surface, sets `sing := Support(SingularSubscheme(X));` and asserts `#sing eq 48`.

Pinned locators:
- arXiv `1912.08908v3`, paper p.4 / Theorem 1.2;
- `https://arxiv.org/src/1912.08908v3/anc/perfectcuboid.out`, singular-locus computation and symmetry computation.

## Exact reconstruction

Write `i^2=-1`. After projective normalization by the first nonzero member of `(x1,x2,x3)`, the 48 nodes split into six explicit 8-point families:

1. `AXIS_X1`: `[1,0,0,0,a,b,c]`;
2. `AXIS_X2`: `[0,1,0,a,0,b,c]`;
3. `AXIS_X3`: `[0,0,1,a,b,0,c]`;
4. `Y1_Z_ZERO`: `[0,1,s*i,0,a*i,b,0]`;
5. `Y2_Z_ZERO`: `[1,0,s*i,a*i,0,b,0]`;
6. `Y3_Z_ZERO`: `[1,s*i,0,a*i,b,0,0]`;

where every displayed parameter is independently in `{+1,-1}`.

The first three families arise over the three coordinate-axis points of the `(x1:x2:x3)` projection. The last three arise at the tangencies `y_j=z=0`, equivalently `q_j=q_4=0`, with the remaining two square roots giving the independent signs.

The retained verifier checks, exactly over `Q(i)`, that:
- all 48 rows satisfy the four defining quadrics;
- the 4×7 Jacobian has rank exactly 3 at every row;
- projective normalization is already canonical;
- all 48 canonical projective tuples are distinct;
- the six family counts are exactly `8+8+8+8+8+8`.

Because the pinned BTVA computation independently asserts that the singular support has exactly 48 points over `Q(i)`, these 48 distinct singular points exhaust that support.

## Label / scale / symmetry convention

BTVA do **not** publish a canonical node numbering `0..47`. Their ancillary computation stores the singular support in `sing` and subsequently uses set/orbit operations. Therefore no Magma set iteration order is source authority for a node label.

Lane A introduces deterministic labels only from the six formulas above. These labels are a repository-side adapter, not BTVA terminology.

Projective equivalence identifies multiplication of all seven coordinates by one common nonzero scalar. Independent coordinate sign changes are not projective equivalence; they generally give distinct nodes. BTVA's ancillary computation separately builds a linear automorphism group from simultaneous permutations of `(x1,x2,x3)` and `(y1,y2,y3)` plus coordinate sign changes, then restricts to a determinant-one subgroup used for orbit calculations. Lane A does not quotient the 48 target nodes by that group.

## Remaining BC2-01B gap

Source-side target recovery is complete, but the load-bearing runtime bridge is still absent: there is no established identification from Stoll exceptional index `k=0..47` (Picard slots `92+k`) to one of the canonical tuples retained here. In particular, source `sing` order must not be assumed to equal Stoll `pts` order, and neither order should be treated as canonical without an exact adapter.

Thus lane-A status is `PASS` only for `SOURCE_SIDE_48_NODE_TARGET_RECONSTRUCTION`; overall `BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE` remains unresolved pending the A/B/C/D synthesis.
