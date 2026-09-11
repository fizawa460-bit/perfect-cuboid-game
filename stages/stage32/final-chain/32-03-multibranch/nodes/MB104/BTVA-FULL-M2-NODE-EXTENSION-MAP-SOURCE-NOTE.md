# Stage32 MB104 — full `m=2` node-extension map on the 48 cuboid nodes

Status: **RETAINED EXACT FINITE-DIMENSIONAL ADAPTER / NONFINAL / NO POPULATION-WIDE FINITE WINDOW**.

## Sources

Primary mathematical source:

- Bruin--Thomas--Várilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*, Algebra & Number Theory 16 (2022), DOI `10.2140/ant.2022.16.1377`, arXiv `1912.08908v3`.
- Table 1 gives the seven displayed `m=2` generators `omega_1,...,omega_7`; the degree-zero part is completed by `x_2 omega_7, x_3 omega_7, y_1 omega_7, y_2 omega_7, y_3 omega_7, z omega_7`, giving `h^0(X_pc, \hat S^2 Omega^1)=13`.
- The local `A_1` calculation writes the completed resolution near an exceptional curve using `(x_1,x_2,x_3)=(t,tu,tu^2) mod t^2`; for `m=2`, the regular-extension quotient has dimension `chi^0(A_1,2)=3`.
- The vanishing-on-hyperplane corollary explains the already-retained seven-dimensional package `H^0(P^6,O(1))*eta`.

Ancillary source lock used for the exact Table-1 representatives:

- mirror commit `c5a8240aed71ed30c63528a2e8f1411f9cc2e04f`;
- `papers/1912.08908/anc/perfectcuboid_script.m`, blob `7b84650178bd077a9829b51f669c78118b6ce4b9`;
- the Magma script constructs `hatS2DX`, verifies grading `[0,0,0,0,0,0,-1]`, and prints the 13 affine representatives used in Table 1.

Node coordinates and the exact node permutation model are inherited from MB103, ultimately source-locked to Stoll--Testa verification commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, `Cuboids/cuboids.magma`, blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.

## Basis convention

The verifier uses the ordered 13-dimensional basis

`(omega1,...,omega6, x1*eta, x2*eta, x3*eta, y1*eta, y2*eta, y3*eta, z*eta)`,

where `x1*eta=omega7` on the chart `x1=1`.

Only row spaces of local pole maps matter, so harmless nonzero rescaling of a displayed generator or of a local `A_1` basis does not change the retained conclusions.

## Exact local models in the chart `x1=1`

The 24 nodes with `x1 != 0` split into three eight-element types.

### V: line-pair vertex

`x2=x3=y1=0`, with `y2,y3,z in {+1,-1}`.

Use the quotient cover

`x2=(s^2-t^2)/2`, `x3=s*t`, `y1=(s^2+t^2)/2`.

Substituting the Table-1 tensors and retaining the leading exceptional pole gives a three-component linear pole map.  In the basis above its first seven columns are

- `omega1 -> 0`,
- `omega2 -> (0,-2,0)`,
- `omega3 -> (z,0,-z)`,
- `omega4 -> 0`,
- `omega5 -> (1,0,-1)`,
- `omega6 -> (0,2z,0)`,
- `omega7 -> (y2*y3,0,y2*y3)`.

The last six columns are obtained by multiplying the `omega7` column by the node values of `x2,x3,y1,y2,y3,z`.

### T3: tangency with `y3=z=0`

`x2=a in {+i,-i}`, `x3=0`, `y1=b in {+i,-i}`, `y2=e in {+1,-1}`.

Locally put `u=x3`, `v=y3`, `w=z`; then `w^2=u^2+v^2`, `x2^2=v^2-1`, `y1^2=w^2-1`, `y2^2=1+u^2`, and `dx2=(v/x2)dv`.  The exact leading pole columns are

- `omega1 -> (-a,0,a)`,
- `omega2 -> (1,0,-1)`,
- `omega3 -> (a,0,a)`,
- `omega4 -> (-1,0,-1)`,
- `omega5,omega6 -> 0`,
- `omega7 -> (0,2*b*e,0)`.

Again the coordinate multiples are obtained from the node values.

### T2: tangency with `y2=z=0`

`x3=a in {+i,-i}`, `x2=0`, `y1=b in {+i,-i}`, `y3=e in {+1,-1}`.

The exact leading pole columns are

- `omega1 -> (-a,0,a)`,
- `omega2,omega3 -> 0`,
- `omega4 -> (1,0,1)`,
- `omega5 -> (-1,0,1)`,
- `omega6 -> (a,0,a)`,
- `omega7 -> (0,2*b*e,0)`.

Each of the 24 chart maps has rank exactly 3, matching the `A_1,m=2` local defect.

## Extending to all 48 nodes

Direct substitution of the Table-1 formulas under the coordinate transpositions gives exact actions on the first six generators:

- `(12)`: `omega1<->omega2`, `omega3<->omega4`, `omega5->omega5`, `omega6->-omega6`;
- `(13)`: `omega1->-omega5`, `omega5->-omega1`, `omega2->omega2`, `omega3->-omega3`, `omega4->-omega6`, `omega6->-omega4`.

On the seven-dimensional `coordinate*eta` package these transpositions act by the corresponding coordinate permutations.  The two matrices are involutions and their product has order 3.

A node with `x1=0` is moved into the `x1 != 0` chart by `(12)` or `(13)`.  On the eight nodes where both choices are available, the two propagated local pole maps have identical row spaces.  This supplies an exact `3 x 13` extension map for every one of the 48 nodes without assigning a privileged Magma ordering.

## Retained finite computations

The resulting 48-node map has the following exact coordinate-hyperplane checks.

| node support | node count | projective coordinate rank | extension-condition rank | simultaneous `m=2` kernel dimension |
| --- | ---: | ---: | ---: | ---: |
| `x1=0` | 24 | 6 | 12 | 1 |
| `x2=0` | 24 | 6 | 12 | 1 |
| `x3=0` | 24 | 6 | 12 | 1 |
| `z=0`  | 24 | 6 | 12 | 1 |
| `y1=0` | 16 | 6 | 10 | 3 |
| `y2=0` | 16 | 6 | 10 | 3 |
| `y3=0` | 16 | 6 | 10 | 3 |

For each of these seven supports, adjoining **any one** of the remaining nodes raises the projective coordinate rank to 7 and the extension-condition rank to 13.  Thus the simultaneous `m=2` extension space becomes zero for those specific hyperplane-plus-one configurations.

Across all 48 nodes the extension-condition rank is 13.

## What this does and does not prove

This is stronger than the preceding `H^0(O(1))*eta` adapter: the complete 13-dimensional reflexive `m=2` space is now represented by exact local extension maps at all 48 nodes.

It does **not** yet prove that *every* node set spanning `P^6` has extension rank 13.  Random/exploratory checks show that pattern, but the retained certificate deliberately does not promote it.  The next finite task is to classify the node-spanned hyperplane orbits (or, equivalently, rank-6 node configurations) under the exact node automorphism action and certify the rank jump for every orbit.

The adapter also does not itself bound degree, ordinary self-singularities, exceptional mass, or the number of multibranch nodes.

## Firewalls

- No unibranch `176/192` cap is imported.
- A local extension-map rank is not a degree bound.
- Coordinate-hyperplane tests are not promoted to all hyperplanes.
- Exploratory full-span samples are not promoted to a theorem.
- No finite Picard enumeration release.
- No `R29-LG2-MB` discharge, receiver/effectivity/theorem/endpoint credit, or Perfect-Cuboid conclusion.
- Merge remains unauthorized.
