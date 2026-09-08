# Stage32EX6 scratch — V6 eight-conic fixed part / low-degree nef wall

Status: `SCRATCH_EXACT_BOUNDED_V6_EIGHT_CONIC_FIXED_PART_LOWDEGREE_NEF_WALL_NO_ENDPOINT_CREDIT`.

Scratch only. This does not update `MAIN-STATE`, exclude O266, authorize O264 descent, create hostile-audit credit, or advance Stage32 MAIN.

## Source locks

Operational / preceding scratch:

- PR #1715 inspected in this investigation at exact head `5e8e0cd64a1cb74574f8dff9b43d33ecfbf937e7`.
- parent scratch head before this write: `2cf028aec43e0d298e14266947ed4c149e339326`.
- preceding leaf: `stages/stage32-ex6/scratch-v6-nef-obstruction-fixed-part-cohomology-wall.md`.

Current V6 witness:

- `stages/stage32/32-21/post1473-v6-witness-body-recovered.json`;
- blob `dae90ed19395355bebeebe2a6aa6bb1c6e53c244`;
- canonical `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`;
- all-140 pairing SHA256 `4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3`;
- exact current V6 invariants `C^2=758`, `K.C=186`, exceptional mass `266`.

The older post-21bl `g1-d186` witness from PR #1472 has self-intersection `858` and is **not** used here. Sharing the row label `g1-d186` is not an adapter between that old witness and the recovered V6 class.

Primary curve-order / intersection source:

- Michael Stoll / Damiano Testa verification repository, `Cuboids/cuboids.magma`, source blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.
- The source constructs `C1s` as the 32 conics, `C2s` as 12 genus-one curves, `C3s` as 48 further genus-one curves, then sets `Cs := C1s cat C2s cat C3s`; its pairing matrix order is `Cs` first and the 48 exceptional divisors second.
- Thus the current V6 `all140_pairings` order is exactly: 32 conics, 60 genus-one curves, 48 exceptional curves.

External geometry source:

- Michael Stoll and Damiano Testa, updated cuboid-surface manuscript `The surface parametrizing cuboids`, Definition 6 / Proposition 7 / Corollary 18.
- Definition 6 gives the same 140 curves: 48 exceptional curves, 32 conics, 12 + 48 genus-one curves.
- Proposition 7 states that each listed conic and each listed genus-one curve has self-intersection `-4`.
- Since a conic is rational, adjunction gives `K.G=2` for each of the 32 conics.
- Since the other 60 listed curves have genus one, adjunction gives `K.G=4` for each of them.
- The 48 exceptional `(-2)` curves have `K.E=0`.
- Corollary 18 states that the set `G` consists precisely of the integral curves `R` on `S` with `K.R <= 6`; moreover possible canonical degrees are even, and there are no degree-six integral curves.

## 1. Exact `D=C-K` intersections with all 140 low-degree curves

Let

`D := C-K`.

Using the current V6 all-140 vector and the source-locked canonical degrees above, the 140 values are obtained coefficientwise as

- rows `1..32`: `D.G_i = C.G_i - 2`;
- rows `33..92`: `D.G_i = C.G_i - 4`;
- rows `93..140`: `D.G_i = C.G_i`.

For the 32 conics, the exact negative rows are

| row | `C.G` | `K.G` | `D.G` | profile |
|---:|---:|---:|---:|---|
| 17 | 0 | 2 | -2 | `k=2,r=2,p_a=0` |
| 21 | 0 | 2 | -2 | `k=2,r=2,p_a=0` |
| 24 | 0 | 2 | -2 | `k=2,r=2,p_a=0` |
| 25 | 0 | 2 | -2 | `k=2,r=2,p_a=0` |
| 26 | 1 | 2 | -1 | `k=2,r=1,p_a=0` |
| 28 | 1 | 2 | -1 | `k=2,r=1,p_a=0` |
| 30 | 0 | 2 | -2 | `k=2,r=2,p_a=0` |
| 31 | 0 | 2 | -2 | `k=2,r=2,p_a=0` |

Conic row 11 has `D.G_11=0`; all other conic rows are positive.

For rows `33..92`, the minimum is

`min D.G_i = 7`,

so no listed genus-one curve is a nef obstruction.

For rows `93..140`, all values are nonnegative; the unique zero is exceptional row `98`, matching the recovered V6 zero-exceptional index `5`.

Therefore

`D=C-K` is **not nef**.

This supersedes the preceding scratch status `C_MINUS_K_NEF = UNRESOLVED` at scratch level. It does not alter retained EX6 authority.

## 2. Complete classification of low-canonical-degree nef obstructions

Corollary 18 is stronger than merely saying that the 140 curves generate `Pic(S)`: it classifies all integral curves of canonical degree at most six.

Hence the coefficientwise replay above proves the exact bounded statement:

> Every integral curve `R` with `K.R <= 6` and `D.R < 0` is one of the eight conics in rows
> `17,21,24,25,26,28,30,31`.

There are no other low-canonical-degree non-nef obstructions hidden outside the classical 140-curve set.

This does **not** classify negative curves of canonical degree `>=8`; the same Stoll--Testa manuscript explicitly exhibits negative-self-intersection genus-three curves of degree eight outside the cone spanned by `G`.

## 3. The eight conics are simultaneous fixed components of `|D|`

The preceding scratch leaf proved that `D` is effective. For an irreducible curve `R` with `D.R<0`, every effective representative of `D` contains `R`.

Thus all eight negative conics occur simultaneously in the fixed support of `|D|`.

Write

`F := R_17+R_21+R_24+R_25+R_26+R_28+R_30+R_31`.

Each conic has self-intersection `-4`, and distinct integral curves have nonnegative pairwise intersection. Put

`I := sum_{i<j} R_i.R_j >= 0`.

Then exactly

- `K.F = 8*2 = 16`;
- `D.F = 6*(-2)+2*(-1) = -14`;
- `F^2 = 8*(-4)+2I = -32+2I`.

Since every member of `|D|` contains every one of the eight conics at least once,

`h0(D-F)=h0(D)`.

Also

`K.(K-(D-F)) = K.(2K-C+F)`
`               = 32-186+16`
`               = -138 < 0`.

Nefness of `K` therefore gives

`h2(D-F)=0`.

The preceding leaf already has `h2(D)=0`.

Surface Riemann--Roch gives

`chi(D-F)-chi(D)`
` = -D.F + (F^2+K.F)/2`
` = 14 + (-32+2I+16)/2`
` = 6+I`.

Using equal `h0` and zero `h2` on both sides,

`h1(D)-h1(D-F)=6+I`.

Therefore the exact source-independent lower bound is

`h1(S,O_S(C-K)) >= 6`.

No knowledge of the 28 pairwise conic intersections is needed for this lower bound.

Since the preceding leaf has

`h0(D)=124+h1(D)`,

we also obtain

`h0(S,O_S(C-K)) >= 130`.

## 4. Consequences for the previous vanishing routes

Two proposed re-entry routes are now resolved negatively at scratch level:

1. `C-K` cannot be proved nef, because it is explicitly non-nef on eight known conics.
2. A direct theorem `H1(S,O_S(C-K))=0` is incompatible with the exact fixed-part calculation; in fact `h1(C-K)>=6`.

Thus Kawamata--Viehweg through `D=C-K`, and the direct `H1(D)=0` bypass proposed in the preceding scratch leaf, are both closed as routes for this exact V6 class.

This does **not** force `H1(S,O_S(C))>0`. For a general canonical member `H`, the preceding leaf gives

`0 -> H0(D) -> H0(C) -> H0(H,O_H(C)) -> H1(D) -> H1(C) -> 0`

with `h0(H,O_H(C))=170`. The connecting map can still kill the special cohomology coming from the fixed conics.

If `h1(C)=0` were eventually proved, then the canonical restriction map would necessarily have cokernel dimension `h1(D)>=6`, hence rank at most `164`. This is a restriction, not a contradiction.

## 5. Decision

Canonical scratch decisions:

- `CURRENT_V6_SELF_INTERSECTION = 758`;
- `OLD_POST21BL_SELF_INTERSECTION_858_REUSED_AS_V6 = false`;
- `CURRENT_V6_ALL140_ORDER = 32_CONICS_THEN_60_GENUS1_THEN_48_EXCEPTIONAL`;
- `KNOWN_CONIC_CANONICAL_DEGREE = 2`;
- `KNOWN_GENUS1_CANONICAL_DEGREE = 4`;
- `KNOWN_EXCEPTIONAL_CANONICAL_DEGREE = 0`;
- `D_EQUALS_C_MINUS_K_NEGATIVE_KNOWN_CURVE_ROWS = [17,21,24,25,26,28,30,31]`;
- `D_NEGATIVE_KNOWN_CURVE_COUNT = 8`;
- `D_NEGATIVE_LOW_DEGREE_CURVES_ARE_ALL_CONICS = true`;
- `LOW_CANONICAL_DEGREE_AT_MOST_6_NONNEF_OBSTRUCTIONS_COMPLETELY_CLASSIFIED = true`;
- `C_MINUS_K_NEF = false`;
- `EIGHT_NEGATIVE_CONICS_ARE_SIMULTANEOUS_FIXED_SUPPORT = true`;
- `FIXED_CONIC_SUM_K_DEGREE = 16`;
- `FIXED_CONIC_SUM_D_INTERSECTION = -14`;
- `H2_D_MINUS_FIXED_CONIC_SUM_ZERO = true`;
- `H1_D_MINUS_H1_D_MINUS_F = 6_PLUS_PAIRWISE_INTERSECTION_SUM`;
- `H1_O_C_MINUS_K_LOWER_BOUND = 6`;
- `H0_O_C_MINUS_K_LOWER_BOUND = 130`;
- `DIRECT_H1_C_MINUS_K_ZERO_ROUTE = EXCLUDED`;
- `KAWAMATA_VIEHWEG_VIA_C_MINUS_K = NOT_APPLICABLE`;
- `H1_O_C_ZERO = UNPROVEN`;
- `H0_O_C_EQUALS_294 = UNPROVEN`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Re-entry

The positivity/linear-system route should not loop on nefness or `H1(C-K)=0` again. Useful next bounded inputs are instead:

1. compute the exact pairwise intersection matrix of the eight fixed conics and peel the full forced fixed part of `|C-K|`, checking whether further low-degree components become forced after subtraction;
2. study the canonical-restriction connecting map and determine whether the fixed-conic special cohomology survives in `H1(C)`;
3. convert the six disjointness conditions `C.R=0` and two one-intersection conditions `C.R=1` into member-level landing constraints at the conics' node attachment points;
4. or return to the independent O266 eta/rho / simultaneous-support routes.

## Firewalls

- The eight fixed conics are fixed components of `|C-K|`, not automatically of `|C|`.
- `h1(C-K)>=6` does not imply `h1(C)>0`.
- Corollary 18 classifies only canonical degree at most six; it is not a full Mori-cone theorem.
- The old self-intersection-858 `g1-d186` witness is not current V6 evidence.
- No scratch result here is MAIN authority or endpoint credit.
