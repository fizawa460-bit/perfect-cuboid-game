# Stage32EX6 scratch — six-rank3 Beauville square root and FSM1116 support wall

Status: `SCRATCH_EXACT_BOUNDED_SIX_RANK3_BEAUVILLE_SQUARE_ROOT_FSM1116_SUPPORT_WALL_NO_ENDPOINT_CREDIT`.

Scratch only. This does not update `MAIN-STATE`, exclude O266, authorize O264 descent, or create Stage32 MAIN / hostile-audit credit.

## Source locks

Repo/EX6:

- PR #1715 retained head inspected in this batch: `5e8e0cd64a1cb74574f8dff9b43d33ecfbf937e7`.
- `stages/stage32/residual-32-01-production/post1473-specific-class-multibranch-beauville-odd-branch-wall.md`.
- `stages/stage32-ex6/post1697-fsm16-f-residual-divisor-wall.md`.
- preceding scratch rank3 leaves, in particular `scratch-rank3-fibration-ruling-fourjet-adapter-wall.md` and the six-rank3 simultaneous RH scratch chain.

External geometry:

- M. Stoll, D. Testa, *The surface parametrizing cuboids* / updated cuboid-surface manuscript, Section 5 rank-three fibrations.
- Their geometric Picard group result states that `Pic(S)` is free abelian of rank 64, hence has no torsion.
- The six rank-three fibrations have disjoint eight-node base sets covering the 48 nodes, and for each rank-three fibration class `F_j`

  `2 F_j = H - E_{B_j}`

  on the minimal resolution `S`, where `H=K_S` is the pullback of the hyperplane class and `E_{B_j}` is the sum of the eight exceptional curves over its singular-plane base set.

Freitag--Salvati Manni / retained Beauville source gives a double cover

`Xtilde -> S`

branched exactly along the total exceptional divisor

`E_tot = sum_{48} E_i`.

## 1. Exact surface-level square root from the six rank-three fibrations

Sum the six rank-three class relations.  Because the six base sets partition the 48 nodes,

`2 * sum_{j=1}^6 F_j = 6H - E_tot`.

Hence exactly in `Pic(S)`

`E_tot = 2 * (3H - sum_j F_j)`.

Define

`L_r3 := 3H - sum_j F_j`.

Then

`2 L_r3 = E_tot`.

The Beauville double cover branched on `E_tot` is defined by some line bundle `L_B` with

`2 L_B = E_tot`.

Since Stoll--Testa prove that `Pic(S)` is torsion-free, the difference

`L_B - L_r3`

is 2-torsion only if it is zero. Therefore the branch square root is uniquely identified:

`L_B = 3H - sum_j F_j`.

This is stronger than a degree coincidence and removes the possible surface-level 2-torsion ambiguity.

## 2. Restriction to the hypothetical O266 genus-one carrier

Let `N` be the normalization of the same hypothetical integral genus-one V6 carrier.

Write

- `H_N := H|_N`, with `deg H_N = d = 186`;
- `L_j := F_j|_N`, where `n_j := deg L_j` is the degree of the corresponding rank-three map `N -> P1`;
- `D_O` for the O266 odd-contact/node divisor on `N`.

At O266 every exceptional contact is unit and odd, so

`deg D_O = 266`.

Restricting the six surface relations gives

`2 L_j = H_N - D_j`

for the eight-node block contact divisor `D_j`, and summing gives

`2 * sum_j L_j = 6H_N - D_O`.

Therefore

`A := L_B|_N = 3H_N - sum_j L_j`

satisfies

`2A = D_O`.

Degrees are forced:

`sum_j n_j = (6*186-266)/2 = 425`,

and hence

`deg A = 3*186 - 425 = 133`.

This exactly identifies the degree-133 branch half-line-bundle of the Beauville double cover `Y -> N`.

Since `g(N)=1`, the double-cover canonical formula gives

`K_Y = pi^* A`,

and `deg K_Y=266`, reproducing `g(Y)=134`.

## 3. Six rank-three ramification divisors and the number 1116

For each rank-three map `f_j:N->P1` of degree `n_j`, genus-one Riemann--Hurwitz gives an effective ramification divisor `R_j` with

`R_j ~ 2 L_j`,

`deg R_j = 2 n_j`.

Summing and using the branch-square-root identity,

`sum_j R_j ~ 2 sum_j L_j ~ 6H_N - D_O`.

Equivalently,

`D_O + sum_j R_j ~ 6H_N`.

The degree is therefore exactly

`266 + 2*425 = 1116 = 6*186`.

Thus the repeated EX6 integer `1116` admits a new global rank-three/Beauville interpretation: it is the degree of the effective divisor

`D_O + sum_j R_j`

in the class `6H_N`.

## 4. Critical firewall: this does not realize the FSM16 residual nonnode divisor

The retained FSM16 f-divisor leaf gives, after removing the exact canonical `f` contribution `372k`, a required **signed nonnode** compensation

`(1116+8E)k`,

where `E=eta81+rho81+eta105+rho105`.

The rank-three identity above does **not** provide that object:

1. `D_O` is supported at the O266 node contacts, whereas the FSM16 residual after the node pole debt is specifically a nonnode signed compensation;
2. `sum_j R_j` is the ramification divisor of six different rank-three maps, not the divisor of the FSM tensor with `f` removed;
3. the identity is linear equivalence of divisors/line bundles and does not identify pointwise tensor orders;
4. the rank-three degree is `1116`, not the required `(1116+8E)k`, and no independent source identifies the extra `8E` or the tensor power `k` with this ramification construction.

Therefore the numerical match at `1116` is structural but cannot be recharged as FSM16 residual effectivity or as a new eta/rho cap.

## 5. What is genuinely new

The useful retained scratch object is the exact branch-root formula

`L_B = 3H - sum_{j=1}^6 F_j`

and its genus-one restriction

`A = 3H_N - sum_j L_j`, `deg A=133`, `2A=D_O`.

This gives an explicit global algebraization of the Beauville branch half-line-bundle using the six rank-three fibrations.

Possible future uses must exploit more than positivity/degree, for example:

- a distinguished pencil/subspace in `H0(N,A)` whose Wronskian is forced by the geometry;
- a source-locked Abel/Picard constraint on the actual node divisor `D_O` relative to the six `L_j`;
- a modular/theta identification of the branch section in `A^2`;
- or a member-level relation coupling the six rank-three ramification divisors beyond their summed class.

On a genus-one curve, positive degree/effectivity alone gives no contradiction.

## Decision

- `SIX_RANK3_BASE_BLOCKS_PARTITION_48_EXCEPTIONALS = true`;
- `TOTAL_EXCEPTIONAL_CLASS = 6H_MINUS_2_SUM_FJ = true`;
- `TOTAL_EXCEPTIONAL_CLASS_IS_TWO_DIVISIBLE = true`;
- `PICARD_TORSION_FREE_REMOVES_BRANCH_ROOT_AMBIGUITY = true`;
- `BEAUVILLE_BRANCH_ROOT_CLASS = 3H_MINUS_SUM_FJ`;
- `O266_BRANCH_HALF_LINE_BUNDLE_DEGREE = 133`;
- `SUM_SIX_RANK3_DEGREES = 425`;
- `DO_PLUS_SUM_RJ_LINEAR_EQUIVALENT_6H = true`;
- `DO_PLUS_SUM_RJ_DEGREE = 1116`;
- `FSM1116_NUMERICAL_MATCH_IS_STRUCTURAL = true`;
- `RANK3_1116_DIVISOR_IDENTIFIED_WITH_FSM_RESIDUAL_NONNODE_DIVISOR = false`;
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- Torsion-free Picard removes only the surface square-root ambiguity; it does not create a distinguished genus-one pencil.
- Linear equivalence is not pointwise equality of divisors.
- The node divisor is not reclassified as nonnode compensation.
- The FSM16 signed residual is not promoted to an effective rank-three divisor.
- No Stage32 MAIN, hostile-audit, merge, endpoint, lower-O, or Perfect Cuboid credit follows.
