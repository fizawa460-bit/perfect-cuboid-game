# Stage35-EX Goal4AA source lock — class-B Q(i)-cyclic principal divisor, retained linear-hyperplane blocker

Scope: continue only the Goal4Z class-B principalization target on the Stage35 open receiver `U={h!=0}`. Goal4AA makes the boundary correction integral and small, reconstructs the complete linear hyperplane sections visible in the pinned Stoll C1/C2/C3 configuration, and tests whether their divisor lattice can materialize the required principal divisor. It does **not** prove that the required rational function `F_B` does not exist.

## Exact parent and source locks

- immutable V63 parent state: `stages/stage35-ex/snapshots/MAIN-STATE-V63-a0dd8eca3211.json`, blob `570f778bad86de1c908dd660d84ede8f6531d4ce`;
- Goal4Z artifact: `stages/stage35-ex/35ex-35/goal4z-one-explicit-biquaternion-second-qi-principalization.json`, blob `21507047b6189d87f4c38c71cb3aeb55687de55d`;
- Goal4Y exact UPic two-class artifact: `stages/stage35-ex/35ex-35/goal4y-open-receiver-upic-two-class-lift.json`, blob `9351c92747365838cda92d98854ad136df1847d5`;
- Goal4Y runner-side exact core: `stages/stage35-ex/stage35_ex_35_goal4y_core.py`, blob `b4f5ed6ef52b3b6d81aa6cc6617d67f30d9bf0d2`;
- Stage33 Galois permutation certificate: `stages/stage33/33-07/galois-known-class-permutations.json`, canonical SHA256 `e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30`;
- pinned upstream configuration: `MichaelStollBayreuth/Verification`, commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, path `Cuboids/cuboids.magma`, git blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.

The exact coordinate adapter remains

`(a1,a2,a3,b1,b2,b3,c)=(h,x,y,z,q,p,w)`.

## Exact class-B principal-divisor target

Goal4Z supplies a Picard lift `D_B` of the class-B `cc` cocycle and proves the remaining cyclic direction is `Q(i)/Q`. Goal4AA recomputes the Goal4Y two-step lift against its immutable V61 parent and solves the integral boundary correction equation

`E_B * B = D_B + cc(D_B)`

in the retained 32-component boundary lattice.

The raw Smith-derived solution has maximum absolute coefficient `683`. The boundary kernel has exact rank three. Adding the exact kernel combination

`4*K1 + 218*K2 - 12*K3`

preserves the Picard image and preserves every coefficient modulo two. The resulting exact boundary divisor has maximum absolute coefficient `36` and coefficients on the known boundary components

`1:3, 2:-21, 3:-1, 4:-1, 5:-1, 6:-1, 7:-21, 8:3, 93:-26, 94:-1, 95:2, 96:-21, 97:2, 98:-21, 99:-26, 100:-1, 101:-9, 102:14, 103:15, 104:-10, 105:-11, 106:-36, 107:-35, 108:-12, 117:20, 118:4, 119:4, 120:20, 121:4, 122:20, 123:20, 124:4`.

Call this simplified divisor `E_B`. The formal divisor

`V_B = D_B + cc(D_B) - E_B`

has exact zero class in the retained rank-64 Picard lattice. Its support on the 140 retained divisors has size `69`.

This certifies a concrete principal-divisor **class target**. Picard-class zero is not by itself a literal rational function certificate; a semantic principal-function adapter is still required.

## Bounded retained linear-hyperplane library

Using only the C1/C2/C3 defining equations in the pinned Stoll configuration, Goal4AA reconstructs scalar-equivalence classes of retained linear forms over `Q(i,sqrt(2))`.

- retained distinct linear forms appearing in C1/C2/C3: `79`;
- raw forms whose retained curve components have total degree `16`: `43`;
- source-explicit anchor: `a1=0`, whose strict components are C1 indices `1..8`;
- accept a raw degree-16 form as a complete hyperplane section only when its exact total-transform Picard class equals the anchor hyperplane class;
- Picard-certified complete linear hyperplane sections: `31`.

The total transform includes every retained exceptional divisor intersecting one of the strict components. This makes the comparison on the smooth minimal resolution, not merely on the singular projective model.

Exact rational linear algebra on the 140 divisor coordinates gives

`V_B notin Span_Q{ divisors of the 31 certified complete linear hyperplane sections }`.

Therefore no product/quotient of these 31 retained linear forms can have divisor `V_B`.

## Semantic firewall

Goal4AA certifies only the following bounded negative result:

`RETAINED_C1_C2_C3_CERTIFIED_LINEAR_HYPERPLANE_PRODUCT_ROUTE_BLOCKED`.

It does **not** certify any of the following:

- `F_B` is nonexistent in `Q(i)(S)^*` or `Q(i)(U)^*`;
- `V_B` is non-principal;
- no nonlinear section, higher-degree rational function, Riemann--Roch construction, or other principalization can realize `V_B`;
- the second Goal4Y explicit cyclic/quaternion symbol is materialized;
- the full algebraic Brauer group, local evaluations, verticality, or a Brauer--Manin obstruction;
- E1, R29-PESCH-E1, R29-FIB2, Stage35 closure, or a perfect-cuboid theorem.

The Stage33 `boundary-function` packages are residue-field functions and are not silently promoted to global principal functions on `S`.

The next legal leaf is a broader literal principal-function synthesis, beginning with an exact Riemann--Roch / nonlinear-section feasibility adapter for the fixed 69-support divisor target, rather than repeating the blocked retained linear-hyperplane product search.
