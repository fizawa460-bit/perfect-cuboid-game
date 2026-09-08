# Stage32EX6 scratch — degree-133 canonical / Wronski / surface-section wall

Status: `SCRATCH_EXACT_BOUNDED_DEGREE133_CANONICAL_WRONSKI_SURFACE_SECTION_WALL_NO_ENDPOINT_CREDIT`.

Scratch only. This does not update `MAIN-STATE`, exclude O266, authorize O264 descent, create hostile-audit credit, or advance Stage32 MAIN.

## Source locks

Repo / preceding scratch:

- PR #1715 retained operational head inspected in this investigation: `5e8e0cd64a1cb74574f8dff9b43d33ecfbf937e7`.
- `stages/stage32/residual-32-01-production/post1473-specific-class-multibranch-beauville-odd-branch-wall.md`.
- `stages/stage32-ex6/scratch-six-rank3-beauville-square-root-fsm1116-support-wall.md`.
- `stages/stage32-ex6/scratch-beauville-branch-pullback-plucker-saturation-wall.md`.

External geometry:

- M. Stoll, D. Testa, *The surface parametrizing cuboids*, updated 2025 manuscript.  Their Picard result gives `Pic(S)` free abelian of rank 64.  The canonical morphism is the contraction of the 48 exceptional `(-2)` curves followed by the box embedding.

Verifier:

`stages/stage32-ex6/scratch_verify_degree133_canonical_wronski_surface_wall.py`.

## 1. The surface branch-half class has no global section

The preceding six-rank3 leaf identifies the Beauville branch-half class on the minimal resolution `S` as

`L_B = 3H - sum_{j=1}^6 F_j`

with

`2L_B = E_tot := sum_{i=1}^{48} E_i`.

Here `H=K_S` is the canonical/hyperplane pullback and the exceptional curves are pairwise disjoint `(-2)` curves.

Since `H.E_i=0`,

`H.L_B = 0`.

Assume an effective divisor `D` represents `L_B`.  The canonical morphism contracts exactly the exceptional curves, so every irreducible component of an effective divisor with `H.D=0` is exceptional.  Thus

`D = sum_i a_i E_i`, `a_i >= 0` integers.

But

`L_B.E_i = (E_tot.E_i)/2 = -1`,

whereas

`D.E_i = -2a_i`

is even.  Contradiction. Therefore

`H0(S,L_B)=0`.

So the degree-133 line bundle

`A=L_B|_N`

on the hypothetical genus-one normalization can have `h0(N,A)=133` without those sections being restrictions of ambient surface sections.  In particular the explicit surface square root does **not** by itself select a distinguished section or pencil in `H0(N,A)`.

## 2. Full canonical series on the Beauville double cover

Let

`pi:Y->N`

be the O266 Beauville double cover.  The preceding leaf gives

`deg A=133`, `A^2=O_N(D_O)`, `K_N=O_N`, `K_Y=pi^*A`, and `g(Y)=134`.

For the double cover,

`pi_*O_Y = O_N + A^{-1}`,

so by projection formula

`pi_*K_Y = A + O_N`.

Hence

`H0(Y,K_Y) = H0(N,A) + H0(N,O_N)`.

The first summand is invariant.  The second is the one-dimensional anti-invariant canonical summand; its tautological section vanishes exactly at the ramification divisor of `pi`, i.e. at the 266 O266 branch points.

### Generic branch-point canonical weight

At a branch point choose parameters `t=s^2`.  At a non-inflection point of the complete `g^132_133=|A|` on `N`, its vanishing sequence is

`0,1,...,132`.

The invariant canonical sections therefore have orders

`0,2,4,...,264`,

while the anti-invariant section has order `1`.

The full canonical vanishing sequence is

`0,1,2,4,6,...,264`.

Its Weierstrass weight is exactly

`8646`.

### If the branch point is also an A-inflection point

For a degree-133 line bundle on an elliptic curve, the complete series has a weight-one inflection at `P` precisely when

`A ~= O_N(133P)`.

The base vanishing sequence is then

`0,1,...,131,133`.

After pullback and adding the anti-invariant order-one section, the canonical weight at the branch point is

`8648`,

exactly two more than the generic branch baseline.

There are `133^2=17689` such A-inflection points on the elliptic curve, counted in the standard multiplication-by-133 fibre.

## 3. Full canonical Weierstrass budget is not an exclusion

For genus `g=134`, the total canonical Weierstrass weight is

`g^3-g = 2,405,970`.

The universal contribution of the 266 branch points at the generic branch weight is

`266*8646 = 2,299,836`.

The remaining budget is

`106,134 = 6*17,689`.

Thus the full canonical series also has ample exact room for the expected base-inflection and nonbranch contributions.  The anti-invariant canonical section does not turn the previous invariant-subseries Pluecker saturation into a contradiction.

More importantly, the abstract condition

`D_O in |2A|`

does not force `supp(D_O)` to meet the finite set

`{P : A ~= O(133P)}`.

Over the complex elliptic curve, a reduced divisor of degree 266 in the fixed class `2A` can be chosen with support avoiding any prescribed finite set: choose 265 generic distinct points away from it and use the Abel-sum condition for the last point; generically the last point also avoids the finite set and the preceding points.  Therefore no A-inflection incidence follows from the double-cover line-bundle class alone.

## 4. A degree-133 pencil whose Wronskian equals D_O is a real extra condition

Let `V subset H0(N,A)` be a base-point-free pencil.  Because `K_N` is trivial, its Wronskian is a section of

`A^2`

and its ramification divisor has degree 266.

Thus it is numerically possible that

`R_V = D_O`.

But this is not automatic from `D_O in |2A|`.

The Wronski map has source

`Gr(2,H0(A)) = Gr(2,133)`

of dimension

`2*(133-2)=262`,

whereas the projective target

`P H0(A^2)`

has dimension

`h0(A^2)-1 = 266-1 = 265`.

Therefore the Wronski image has codimension at least three in the full projective space of branch sections.

Consequently, a theorem that the actual O266 branch section lies in the Wronski image of a distinguished degree-133 pencil would be a genuinely new member-level restriction.  It is not supplied by the branch square-root identity, Riemann--Roch, or the complete canonical series.

## 5. Decision

Canonical scratch decisions:

- `BEAUVILLE_SURFACE_BRANCH_HALF_CLASS = 3H_MINUS_SUM_SIX_RANK3_FIBERS`;
- `SURFACE_BRANCH_HALF_INTERSECTION_WITH_EACH_EXCEPTIONAL = -1`;
- `SURFACE_BRANCH_HALF_HAS_GLOBAL_SECTION = false`;
- `SURFACE_GEOMETRY_AUTOMATICALLY_SELECTS_A_SECTION_OR_PENCIL_IN_H0_A = false`;
- `FULL_CANONICAL_DECOMPOSITION = H0_A_INVARIANT_PLUS_ONE_ANTIINVARIANT`;
- `ANTIINVARIANT_CANONICAL_SECTION_ZERO_DIVISOR = O266_RAMIFICATION_DIVISOR`;
- `GENERIC_O266_BRANCH_CANONICAL_WEIGHT = 8646`;
- `A_INFLECTED_O266_BRANCH_CANONICAL_WEIGHT = 8648`;
- `A_INFLECTION_POINT_COUNT = 17689`;
- `FULL_CANONICAL_TOTAL_WEIERSTRASS_WEIGHT = 2405970`;
- `BRANCH_CLASS_FORCES_A_INFLECTION_INCIDENCE = false`;
- `DEGREE133_PENCIL_WRONSKI_SOURCE_DIMENSION = 262`;
- `BRANCH_SECTION_PROJECTIVE_TARGET_DIMENSION = 265`;
- `WRONSKI_IMAGE_CODIMENSION_AT_LEAST = 3`;
- `BRANCH_SECTION_AUTOMATICALLY_IN_WRONSKI_IMAGE = false`;
- `DISTINGUISHED_DEGREE133_PENCIL_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Re-entry

The degree-133 route now needs an input stronger than the line-bundle identity.  Useful possibilities are:

1. a source-locked construction of a particular pencil `V subset H0(N,A)` from the V6/six-rank3/theta geometry;
2. a theorem forcing the actual branch section into the Wronski image of such a pencil;
3. a member-level Abel relation forcing some O266 branch points into the finite A-inflection set;
4. or a direct equation for the V6 carrier that constrains the degree-133 branch section.

Absent one of these, complete canonical/Pluecker/abstract Wronski data are structural equivalences rather than endpoint exclusions.

## Firewalls

- `H0(S,L_B)=0` does not imply `H0(N,A)=0`; restriction to the hypothetical curve can gain sections.
- The full canonical decomposition is conditional on the same hypothetical O266 carrier/double cover.
- The finite A-inflection set is not claimed rational or source-marked; only its geometric cardinality/condition is used.
- A dimension count for the Wronski image is not proof that a specific branch section lies outside it.
- No FSM residual divisor is identified with the rank3/Beauville divisors.
- No Stage32 MAIN, hostile-audit, merge, endpoint, lower-O, or Perfect Cuboid credit follows.
