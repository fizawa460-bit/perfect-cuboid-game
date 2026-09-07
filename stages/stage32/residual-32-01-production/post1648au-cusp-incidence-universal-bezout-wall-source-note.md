# Stage32 post1648AU — exact cusp-incidence graph and universal cusp-weight Bezout wall

Scratch-only bounded-negative routing leaf. This leaf starts from AT's exact intermediate quotient/blowup model and AQ's runner-replayed 12 target-cusp rows. It proves that the target-cusp multiplicities, by themselves, cannot force the bidegree `(81,105)` image curve to contain any auxiliary divisor component by a Bezout multiplicity argument. No MAIN authority or theorem/receiver/route/endpoint credit is changed.

## Parent

- AT canonical SHA256: `bc11998f941f4791ac0a394c85725368659262a55ec8206288aefa5ee2241b86`.
- AT finalized scratch head: `31096feeab9a82e0aeac3d902e109283e41c4c30`.

The 12 target-cusp rows are replayed runner-side from AQ; the permanent retained Picard payloads are not emitted into this note.

## Exact incidence graph

Write the six degree-81 special fibres as the A-side and the six degree-105 special fibres as the B-side. The 12 target cusps, weighted by the image multiplicity `m`, are:

- block 1: `(33,34;35)`, `(33,35;24)`, `(36,34;18)`, `(36,35;19)`;
- block 2: `(37,38;28)`, `(37,39;21)`, `(40,38;25)`, `(40,39;34)`;
- block 3: `(41,42;20)`, `(41,43;5)`, `(44,42;5)`, `(44,43;32)`.

Thus the bipartite incidence graph is exactly three disjoint copies of `K_{2,2}`. Every one of the 12 special-fibre vertices has degree two. The three block weight sums are `96,108,62`, totaling `266`.

The exact special-fibre cusp-weight sums are:

- A/degree-81 side: `59,37,49,59,25,37`, each at most 81;
- B/degree-105 side: `53,43,53,55,25,37`, each at most 105.

So no single special fibre is forced as a component of the image curve.

## Universal multiplicity-capacity bound

Let `D` be AP/AT's hypothetical image curve in `P1 x P1`, with factor degrees

`D.F81 = 81`, `D.F105 = 105`.

Let `L` be any curve of class

`L = a*F81 + b*F105`,

with `a,b>0`, and first assume `L` contains no special fibre component. At target cusp `e`, let

`k_e = mult_e(L)`.

Because a degree-81 special fibre is smooth and not a component of `L`, intersecting `L` with that fibre gives

`sum_{e on A_i} k_e <= b`.

Likewise, for every degree-105 special fibre,

`sum_{e on B_j} k_e <= a`.

At a cusp where `D` has multiplicity `m_e`, the local intersection satisfies

`I_e(D,L) >= m_e*k_e`.

Therefore the total cusp-forced intersection is bounded using the A rows by

`sum_e m_e*k_e <= b * sum_i max_{e on A_i}(m_e)`.

The six A-row maxima are

`35,19,28,34,20,32`,

with sum `168`. Hence

`sum_e m_e*k_e <= 168*b`.

Using the B columns, the six maxima are

`35,24,28,34,20,32`,

with sum `173`, hence also

`sum_e m_e*k_e <= 173*a`.

Thus universally

`sum_e m_e*k_e <= min(168*b,173*a)`.

But

`D.L = 81*a + 105*b`.

For a cusp-multiplicity Bezout obstruction one would need both

`168*b > 81*a+105*b`,
`173*a > 81*a+105*b`.

These imply respectively

`b/a > 81/63 = 9/7`,
`b/a < 92/105`.

Since `9/7 > 92/105`, they cannot hold simultaneously. Therefore

`sum_e m_e*k_e <= D.L`

for every positive bidegree `(a,b)`.

This argument already allows arbitrary higher multiplicity `k_e`; it is not restricted to simple passages through the cusps and does not require the actual cusp coordinates.

If `L` contains special-fibre components, remove them one at a time. Each such component individually has cusp-weight sum no larger than its exact intersection with `D`, as recorded above. Additivity then reduces to the no-special-fibre case. Hence adding special-fibre components cannot create a Bezout contradiction either.

As a small independent check, the maximum-weight `(1,1)` matching in the 12-edge graph has weight `168`, strictly below

`D.(F81+F105)=186`.

## Decision

The exact 12-cusp incidence and multiplicity data cannot, by themselves, force any auxiliary bidegree component by Bezout. This route is therefore a bounded wall, not a V6 exclusion.

The next missing input must be genuinely stronger than cusp multiplicity:

- member-level tangent or higher-jet relations;
- an independent global singularity inequality;
- or another structure not reducible to weighted Bezout at these 12 points.

Firewalls:

- `V6_carrier_excluded=false`;
- `Q602_excluded=false`;
- `O210_excluded=false`;
- `O212_plus_advance_allowed=false`;
- scratch only; shared `MAIN-STATE.json` and Stage32 authority unchanged.
