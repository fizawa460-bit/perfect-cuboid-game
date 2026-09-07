# Stage35-EX Goal4AB source lock — class-B Q(i)-cyclic low-degree Riemann–Roch feeder blocker

Scope: continue only the Goal4AA class-B principalization target on the Stage35 open receiver `U={h!=0}`. Goal4AB strengthens the retained linear-section analysis by reconstructing the exact exceptional multiplicities for all 43 degree-16 source linear sections and then tests the natural retained Stoll C4/C5 low-degree nonlinear elimination identities. It does **not** construct `F_B`, prove `V_B` non-principal, or exhaust higher-degree Riemann–Roch sections.

## Exact parent and source locks

- immutable V64 parent state: `stages/stage35-ex/snapshots/MAIN-STATE-V64-691e934b0f7b.json`, blob `8122328a4f6592de1756a560f86f5999ec4310a7`, parent live head `691e934b0f7b2048cc4c862d3aeea6873c784b52`, snapshot commit `a026198809ee1be482fc22c50aa6a6e717a3f12a`;
- Goal4AA artifact: `stages/stage35-ex/35ex-35/goal4aa-second-class-qi-cyclic-linear-hyperplane-blocker.json`, blob `e0c3e31839b8f396e18fbafce7b021f66b8671a2`;
- Goal4AA source lock: `stages/stage35-ex/35ex-35/goal4aa-second-class-qi-cyclic-linear-hyperplane-blocker-source-lock.md`, blob `b341cfc2fc8201a4554c3b3c670e1be88c03d0f8`;
- Goal4AA verifier: `stages/stage35-ex/verify_stage35_ex_35_goal4aa.py`, blob `5fd27d49a4bf9ec5fea9572e9f5ba40464938387`;
- Goal4Z artifact: `stages/stage35-ex/35ex-35/goal4z-one-explicit-biquaternion-second-qi-principalization.json`, blob `21507047b6189d87f4c38c71cb3aeb55687de55d`;
- Goal4Y exact runner-side core: `stages/stage35-ex/stage35_ex_35_goal4y_core.py`, blob `b4f5ed6ef52b3b6d81aa6cc6617d67f30d9bf0d2`;
- provisional Arsenal semantic router `S33-PW07`: `docs/arsenal/cards/provisional/S33-PW07.md`, blob `7f1337858bc6f9006e101d810dd72e67aef534fd`; used only for the literal-representative firewall, not theorem credit;
- pinned upstream configuration: `MichaelStollBayreuth/Verification`, commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, path `Cuboids/cuboids.magma`, git blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.

The coordinate adapter remains

`(a1,a2,a3,b1,b2,b3,c)=(h,x,y,z,q,p,w)`.

Exploratory exact probe provenance only: run `34026524527`, job `101468360020`, exact head `c61bb9417fb80c16be32b5a0248c50fc6df8e614`, SUCCESS. Permanent credit is carried by the committed Goal4AB verifier, not by this temporary run.

## Exact completion of all 43 retained degree-16 linear sections

Goal4AA reconstructed 79 scalar-equivalence classes of C1/C2/C3 source linear forms and found 43 whose retained strict components have total degree 16. It certified 31 complete hyperplane sections using the conservative rule “add each incident exceptional curve with multiplicity one”.

Goal4AB removes that conservatism. The 48 retained exceptional classes are linearly independent in `Pic(Sbar)` (exact rank 48). For each of the 43 degree-16 strict divisors `C_L`, solve

`sum_j m_j E_j = H - [C_L]`

in the 48 exceptional classes, where `H` is the source-explicit hyperplane class from `a1=0`. Every one of the 43 systems has a unique integral nonnegative solution. Across all 43×48 exceptional coefficients the exact multiplicity histogram is

`0:1680, 1:336, 2:48`.

Thus all 43 source linear forms are exact complete hyperplane sections on the smooth minimal resolution, with their exceptional multiplicities fully reconstructed.

The 140×43 exact divisor matrix has rank 31. Its quotient/difference lattice has rational rank 30. The fixed Goal4AA target `V_B` is in neither the rational span of the 43 complete section divisors nor the rational span of their differences. Therefore completing the previously conservative 12 sections does not produce the required principal divisor.

## Retained C4/C5 low-degree nonlinear elimination identities

The pinned Stoll source also retains degree-8 genus-3 curves C4 and C5, each cut by a source linear equation together with a source quadratic equation. Goal4AB checks the natural degree-balanced eliminations directly in the homogeneous coordinate ring of the projective cuboid surface.

For the four C4 source families, the product of the four conjugate linear sections equals `-4` times the product of the two conjugate quadratic sections on `S`. Concretely the four pairs of quadratic factors are

- `a2*a3 ± i*a1*b1`, with linear family `b1 + e2*b2 + e3*b3`;
- `a1*a3 ± b2*c`, with linear family `b1 + e2*i*b2 + e3*b3`;
- `a1*a2 ± b3*c`, with linear family `b1 + e2*b2 + e3*i*b3`;
- `a2*a3 ± b1*c`, with linear family `b1 + e2*i*b2 + e3*i*b3`.

For C5, for each `(e2,e3) in {±1}^2`, pairing the two source quadratic factors gives the exact identity

`prod_{e4=±1}(a1+e2*a2+e3*a3+e4*i*c) * prod_{e4=±1}(a1-e2*a2-e3*a3+e4*i*c)`

`= 4 * prod_{e1=±1}((e2*a2+e3*a3)*b1+e1*i*b2*b3)`

on `S`.

All eight identities are reduced exactly modulo the four defining quadrics of `S`; no numerical sampling is used. These natural aggregate C4/C5 low-degree nonlinear eliminations therefore collapse to products of the already-completed linear hyperplane sections and add no new divisor direction for the fixed target.

## Semantic firewall

Goal4AB certifies only the bounded negative result

`ALL_43_RETAINED_DEGREE16_LINEAR_SECTIONS_PLUS_NATURAL_C4_C5_LOW_DEGREE_ELIMINATIONS_DO_NOT_SYNTHESIZE_F_B`.

It does **not** certify any of the following:

- `F_B` is nonexistent in `Q(i)(S)^*` or `Q(i)(U)^*`;
- `V_B` is non-principal;
- individual C5 quadratic sections have no useful residual degree-16 component;
- arbitrary nonlinear or higher-degree graded-coordinate-ring/Riemann–Roch synthesis is exhausted;
- both Goal4Y explicit symbols are materialized;
- the full algebraic Brauer group, local evaluations, verticality, or a Brauer–Manin obstruction;
- E1, R29-PESCH-E1, R29-FIB2, Stage35 closure, or a perfect-cuboid theorem.

The next legal leaf is the smallest genuinely new low-degree nonlinear object left by this calculation: inspect the individual retained C5 quadratic sections and their residual degree-16 divisors rather than repeat aggregate products that are already exact identities.
