# Stage32EX1 EX1-03 — smooth-ambient plane-curve singularity source note

Status: source note for the **unaudited EX1-03 candidate** only. It does not grant theorem, branch-exclusion, Stage32 MAIN, receiver, endpoint, or Perfect Cuboid credit.

## Local geometric model

Let `S` be the smooth minimal resolution and `E` its exceptional divisor. On

`U = S \ E`

the resolution map is an isomorphism to the regular locus of the singular canonical model. Hence, at any point `p in Gamma cap U`, the ambient surface is regular of dimension two. Because an integral curve on a smooth surface is locally Cartier, the completed local germ of `Gamma` is a reduced plane hypersurface curve singularity.

EX1-03 uses only this regular-surface local model. It does not transfer the canonical-model node fibre ledger into the intrinsic `delta` invariant.

## Delta and branch source locks

Primary reference:

- The Stacks Project, Section 33.39, tag `0C3Q`, “The delta invariant”:
  `https://stacks.math.columbia.edu/tag/0C3Q`.
  This supplies the normalization-length definition of the delta invariant for reduced one-dimensional Nagata local rings.

- The Stacks Project, Lemma 33.40.6, tag `0C43`:
  `https://stacks.math.columbia.edu/tag/0C43`.
  For a one-dimensional reduced Nagata local ring,
  `delta >= number of geometric branches - 1`.

Applied to a singular point `p` of the reduced curve `Gamma` in `U`, write `r_p` for the geometric branch count. Then

`r_p - 1 <= delta_p`.

Since a singular reduced curve point has positive normalization defect, `delta_p >= 1`. Thus, if

`delta_U = sum_{p in Sing(Gamma) cap U} delta_p`,

then

- `#(Sing(Gamma) cap U) <= delta_U`;
- `sum_p (r_p-1) <= delta_U`;
- with the Stage32EX1 global ledger, `0 <= delta_U <= 472`.

A multibranch smooth-locus singularity (`r_p >= 2`) therefore costs at least one unit of `delta_U`. The converse is false: a unibranch singularity can have positive delta.

## Canonical-hyperplane multiplicity lemma

This part is an elementary consequence of the source-locked cuboid-surface canonical model and the EX1-00 intersections.

The canonical model lies in `P^6`; on `U` the canonical morphism is an isomorphism to its image. The V6 target has

`K.Gamma = 186`,
`Gamma^2 = 758`.

Take any set `T` of at most six distinct points of `Gamma cap U`. Their images in `P^6` lie on some hyperplane `H`.

No canonical hyperplane section can contain `Gamma` as a component. Indeed, if

`H|_S = a Gamma + R`, `a >= 1`,

with `R` effective and without `Gamma` as a component, then on the smooth surface

`186 = K.Gamma = a Gamma^2 + R.Gamma >= 758`,

because intersections of distinct effective curves are nonnegative. Contradiction.

Therefore `H` intersects `Gamma` properly, with total intersection degree `186`. At each selected point,

`I_p(H,Gamma) >= mult_p(Gamma)`,

hence

`sum_{p in T} mult_p(Gamma) <= 186`.

This is only a multiplicity budget. EX1-03 does **not** convert it into a delta bound without a separately source-locked multiplicity-versus-delta theorem.

## Exact scope

The smooth-locus branch is not excluded. EX1-03 produces only a coarse numerical residual ledger:

- choose `delta_U in [0,472]`;
- choose at most `delta_U` singular points;
- choose positive local deltas summing to `delta_U`;
- choose branch counts `1 <= r_p <= delta_p+1`;
- impose the canonical six-point multiplicity budget above.

Local equations, Puiseux/semigroup data, branch tangency, and actual V6 realizability remain unresolved and are handed to EX1-04 global coupling.
