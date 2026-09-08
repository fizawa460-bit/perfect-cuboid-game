# Stage32EX6 scratch — V6 `C-K` eight-conic disjoint peel wall

Status: `SCRATCH_EXACT_BOUNDED_V6_C_MINUS_K_EIGHT_CONIC_DISJOINT_PEEL_WALL_NO_ENDPOINT_CREDIT`.

Scratch only. This does not update `MAIN-STATE`, exclude O266, authorize O264 descent, create hostile-audit credit, or advance Stage32 MAIN.

## Source locks

Operational / preceding scratch:

- PR #1715 inspected in this investigation at exact head `5e8e0cd64a1cb74574f8dff9b43d33ecfbf937e7`.
- parent scratch head before this write: `48cb6f309f315c674a7f266c1b0ad30a841a6434`.
- preceding leaf: `stages/stage32-ex6/scratch-v6-eight-conic-fixed-part-lowdegree-nef-wall.md`.
- preceding replay: `stages/stage32-ex6/scratch_verify_v6_eight_conic_fixed_part_lowdegree_nef_wall.py`.

Current V6 witness:

- `stages/stage32/32-21/post1473-v6-witness-body-recovered.json`;
- blob `dae90ed19395355bebeebe2a6aa6bb1c6e53c244`;
- canonical `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`;
- all-140 pairing SHA256 `4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3`;
- exact current V6 invariants `C^2=758`, `K.C=186`, exceptional mass `266`.

Primary curve/intersection source:

- Michael Stoll / Damiano Testa verification repository `MichaelStollBayreuth/Verification` at commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`;
- `Cuboids/cuboids.magma`, source blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`;
- the source defines the 32 conics `C1s`, the singular-point sets `Cpts`, and the resolved intersection routine

  `intersection(C,j) = Degree(C meet Cs[j]) - singular multiplicity corrections`

  for distinct curves, exactly implementing the reduction caused by blowing up the 48 singular points.

The pairwise calculation below replays those explicit conic equations and this exact intersection convention. It is a bounded computation on the eight already-identified conics, not a new Mori-cone claim.

## 1. The eight forced conics are pairwise disjoint on the resolution

Let

`D := C-K`

and let the eight fixed conics from the preceding leaf be

`R_17,R_21,R_24,R_25,R_26,R_28,R_30,R_31`.

The preceding leaf has

- each `R_i^2=-4`;
- `D.R_i=-2` for rows `17,21,24,25,30,31`;
- `D.R_i=-1` for rows `26,28`;
- all eight occur simultaneously in the fixed support of `|D|`.

Replaying the Stoll--Testa conic equations for all `C(8,2)=28` pairs gives

`R_i.R_j = 0` for every distinct pair.

On the singular box model, the pairs either do not meet or meet only at one/two of the 48 singular points. The source `intersection()` routine subtracts precisely those singular contributions, so their strict transforms on the minimal resolution are disjoint.

Therefore the formerly unknown quantity

`I := sum_{i<j} R_i.R_j`

is exactly

`I=0`.

Define

`F := R_17+R_21+R_24+R_25+R_26+R_28+R_30+R_31`.

Then exactly

- `F^2 = 8*(-4) = -32`;
- `K.F = 16`;
- `D.F = -14`.

## 2. Exact first peel `D1=D-F`

Set

`D1 := D-F = C-K-F`.

Because all eight curves are fixed components of `|D|`, multiplication by their defining section gives an isomorphism

`H0(S,O(D1)) ~= H0(S,O(D))`.

The numerical invariants are

`D1^2 = D^2 - 2D.F + F^2`
`      = 402 - 2*(-14) - 32`
`      = 398`,

and

`K.D1 = K.D-K.F = 170-16 =154`.

Surface Riemann--Roch gives

`chi(O(D1)) = 8 + (398-154)/2 = 130`.

Also

`K.(K-D1)=16-154=-138<0`.

Since `K` is nef, `K-D1` is not effective, hence

`h2(O(D1))=0`.

The preceding leaf has `chi(O(D))=124`, `h2(O(D))=0`. Therefore

`h0(D)=124+h1(D)`

and

`h0(D1)=130+h1(D1)`.

Using `h0(D1)=h0(D)` yields the exact equality

`h1(D)-h1(D1)=6`.

So the preceding lower bound sharpens structurally from an unknown `6+I` to the exact cohomology shift

`h1(C-K) = h1(C-K-F)+6`.

In particular

`h1(C-K)>=6`

and

`h0(C-K)>=130`.

## 3. `D1` remains big

For every integer `n>=1`,

`K.(K-nD1)=16-154n<0`,

so `h2(nD1)=0` by nefness of `K`.

Riemann--Roch gives

`chi(O(nD1)) = 8 + (398 n^2 -154 n)/2`
`             = 8 +199 n^2 -77 n`.

Thus `h0(nD1)` has quadratic growth, so `D1` is big.

The fixed-conic peel removes the known low-degree negative part without destroying bigness.

## 4. Exact scan against the 92 known nonexceptional curves

Using the Stoll--Testa source order and intersection convention, the exact intersection vector `F.G_i` for rows `1..92` is

`[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-4,0,0,0,-4,0,0,-4,-4,-4,0,-4,0,-4,-4,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,3,2,3,2,2,3,2,3,2,3,2,3,3,2,3,2,2,1,1,2,2,1,1,2,0,3,3,0,0,3,3,0,0,0,0,0,0,0,0,0]`.

Canonical SHA256 of this compact vector under sorted/minified JSON convention:

`ea960468c133814c1fb342efa8be682fd6c56880785abdf087fa2f5ca671b38c`.

Subtracting it from the exact `D=C-K` pairings gives

`D1.G_i = [11,8,4,5,6,9,7,10,6,4,0,5,8,10,15,8,2,12,7,3,2,11,3,2,2,3,2,3,2,2,2,6,7,22,27,18,12,22,21,7,24,36,30,18,30,42,44,28,36,36,38,34,9,50,35,24,33,26,19,40,16,41,44,13,27,30,39,18,20,27,35,28,34,29,21,26,14,28,37,23,26,28,25,23,12,15,47,44,38,29,21,30]`.

Canonical SHA256:

`0ee12ba4030500fa0e61d67c3e46a83541508d48d6609926df0afb67bfa17ace`.

Hence among all 92 known nonexceptional curves:

- there are no negative `D1` intersections;
- the unique zero is conic row `11`;
- every other known nonexceptional curve has positive intersection with `D1`.

A zero intersection does not force row 11 into the fixed support. The low-degree forced-component iteration therefore stops after the eight-conic peel unless new information is supplied.

## 5. Exceptional incidence and the remaining label adapter

Each of the eight fixed conics contains exactly six singular points of the box model. Their incidence with the 48 singular points has total mass

`8*6=48`.

The exact unlabeled multiplicity distribution is

- multiplicity 3 at 2 singular points;
- multiplicity 2 at 10 singular points;
- multiplicity 1 at 22 singular points;
- multiplicity 0 at 14 singular points.

Thus the support has size `34` and the multiset is

`{3^2,2^10,1^22,0^14}`.

For the current V6 witness the exceptional intersection vector (rows `93..140`) has total mass `266`, with one zero exceptional row (`98`). After subtracting `F`, the total exceptional mass of `D1` is therefore

`266-48=218`.

However, this batch does not source-lock the permutation identifying the 48 Stoll--Testa singular-point coordinates with the Stage32 recovered-witness exceptional row ordering. Without that adapter, the actual coefficientwise exceptional values `D1.E_j` are not authorized.

This is not merely cosmetic: the two unlabeled multisets admit a nonnegative matching. Sorting the current V6 exceptional masses and the `F` incidence multiset gives coefficientwise domination, so the unlabeled data alone do not force a further negative exceptional intersection.

Therefore no additional exceptional fixed component is obtained from the current source locks.

## 6. Decision

Canonical scratch decisions:

- `EIGHT_FORCED_CONICS_PAIRWISE_DISJOINT_ON_RESOLUTION = true`;
- `EIGHT_CONIC_PAIRWISE_INTERSECTION_SUM_I = 0`;
- `FIXED_CONIC_SUM_F_SQUARED = -32`;
- `FIXED_CONIC_SUM_K_DOT_F = 16`;
- `FIXED_CONIC_SUM_D_DOT_F = -14`;
- `D1_EQUALS_C_MINUS_K_MINUS_F_SQUARED = 398`;
- `D1_K_INTERSECTION = 154`;
- `CHI_O_D1 = 130`;
- `H2_O_D1 = 0`;
- `H0_D1_EQUALS_H0_D = true`;
- `H1_D_MINUS_H1_D1 = 6`;
- `H1_C_MINUS_K_LOWER_BOUND = 6`;
- `H0_C_MINUS_K_LOWER_BOUND = 130`;
- `D1_BIG = true`;
- `D1_NEGATIVE_KNOWN_NONEXCEPTIONAL_ROWS = []`;
- `D1_ZERO_KNOWN_NONEXCEPTIONAL_ROWS = [11]`;
- `F_EXCEPTIONAL_INCIDENCE_TOTAL = 48`;
- `F_EXCEPTIONAL_INCIDENCE_SUPPORT_SIZE = 34`;
- `F_EXCEPTIONAL_INCIDENCE_MULTISET = {3^2,2^10,1^22,0^14}`;
- `D1_EXCEPTIONAL_TOTAL_INTERSECTION = 218`;
- `STOLL_TESTA_SINGULAR_POINT_TO_STAGE32_EXCEPTIONAL_ROW_ADAPTER = UNRESOLVED`;
- `UNLABELED_EXCEPTIONAL_DATA_FORCE_FURTHER_NEGATIVE_INTERSECTION = false`;
- `FURTHER_FIXED_COMPONENT_AFTER_FIRST_PEEL_OBTAINED = false`;
- `H1_O_C_ZERO = UNPROVEN`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Re-entry

Useful next bounded inputs are:

1. source-lock the exact singular-point / exceptional-row permutation and test the 48 exceptional intersections of `D1` coefficientwise;
2. study whether the exact six-dimensional special-cohomology contribution survives the canonical restriction sequence from `D=C-K` to `C`;
3. turn the six `C.R=0` conics and two `C.R=1` conics into member-level landing/attachment restrictions on the hypothetical O266 carrier;
4. or return to the independent eta/rho / simultaneous-critical-support route.

## Firewalls

- Disjointness of the eight fixed conics is a statement on their strict transforms on the minimal resolution.
- Row 11 having `D1.R_11=0` does not make it a fixed component.
- The unlabeled exceptional incidence multiset is not an exceptional-row adapter.
- `h1(C-K)>=6` still does not imply `h1(C)>0`.
- No scratch result here is MAIN authority or endpoint credit.
