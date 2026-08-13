# Stage14-X1 — joint common-core/CRT physical-fiber lemma

## Status and source snapshot

`COMPLETE_JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_LEMMA`

This is an independent continuation of merged Stage14-X0. It writes only in
the dedicated `Stage14-X1` area and its dedicated CI workflow.

```text
main snapshot                         f36506bfe404637a6d989d5e56fa698018a661d9
merged X0                              3c53f66014d83f4eaec03eefcda69f96ff69aa95
merged mainline input                  14-4ch
merged s input                         14-s7-22
latest independent fixed-U input       14-t59
```

The relevant merge order matters. X0 recorded the physical-fiber lemma as
open. The stronger Stage14-4ch reconstruction theorem was merged immediately
after X0, so X1 may legally consume it and close the X0 obligation.

No canonical index, predecessor result, or exponent ledger is edited.

## 1. Verdict

X0 requested the following statement.

```text
JointCommonCoreCRTPhysicalFiberLemma:
for fixed legal (xi,k), eight cells, primewise orientations,
(C,u_res,v_res), and primitive z ratio, the number of physical
JointBalancedCollisionPackets is B^o(1), uniformly at the balanced endpoint.
```

The lemma is **proved**, and merged 4ch proves a stronger fixed-data theorem:

```text
fixed eight cells and fixed (C,u_res,v_res)
already give only B^o(1) physical lifts.                       (1.1)
```

Indeed the eight cells determine

```text
xi=R*S*T*J,
k=alpha*beta*gamma*delta.                                    (1.2)
```

Fixing primewise orientations and the primitive `z` ratio only takes a subset
of the 4ch physical lifts. They are not needed to obtain the fiber bound.

After the harmless `B^o(1)` decoration multiplicity from s7-21 orientations
and the unit ambiguity of the four 4cf Gaussian descents is included, the
same bound holds for decorated `JointBalancedCollisionPackets` rather than
only undecorated physical pairs.

Thus

```text
JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_LEMMA_PROVED=true
JOINT_PHYSICAL_FIBER_BO1_PROVED=true
```

## 2. Algebraic proof

Fix the balanced cells

```text
(R,S,T,J;alpha,beta,gamma,delta)
```

and a residual triple `(C,u,v)`. Put

```text
q_k=C*u,
q_xi=C*v.
```

All integers below are `B^O(1)` uniformly over the endpoint packet.

### 2.1 Recover the four root products from two factor-pair problems

Merged 4cg/4ch gives the exact positive factorizations

```text
xi*q_k=H_k^+*H_k^-,
k*q_xi=H_xi^+*H_xi^-,
H_k^+>H_k^->0,
H_xi^+>H_xi^->0.                                  (2.1)
```

There are at most

```text
tau(xi*C*u)*tau(k*C*v)=B^o(1)                      (2.2)
```

ordered choices for these factor pairs. For each valid choice, half-sums and
half-differences satisfy

```text
(H_k^+ + H_k^-)/2=delta^2*(s_1*s_2)^2,
(H_k^+ - H_k^-)/2=alpha^2*(r_1*r_2)^2,

(H_xi^+ + H_xi^-)/2=J^2*(y_1*y_2)^2,
(H_xi^+ - H_xi^-)/2=R^2*(x_1*x_2)^2.               (2.3)
```

After the divisibility and perfect-square tests, the four positive products

```text
r_1*r_2,
s_1*s_2,
x_1*x_2,
y_1*y_2                                                (2.4)
```

are uniquely determined.

### 2.2 Split the products and reconstruct the two states

For fixed products in (2.4), the number of ordered splits is at most

```text
tau(r_1*r_2)*tau(s_1*s_2)*tau(x_1*x_2)*tau(y_1*y_2)
=B^o(1).                                             (2.5)
```

There are only four choices for `(g_1,g_2) in {1,2}^2`. Then

```text
omega_i=g_i*r_i*s_i,
z_i=2*x_i*y_i/g_i,

P_1=(R*S)*x_1^2,    Q_1=(T*J)*y_1^2,
P_2=(R*T)*x_2^2,    Q_2=(S*J)*y_2^2.               (2.6)
```

are fixed whenever integral. Reducedness, signs, interval conditions,
primitive coprimalities, same-`(xi,k)` identities, and reconstruction masks are
only rejection tests. They cannot enlarge the candidate list.

Consequently, for every fixed cell/residual datum `D`,

```text
# physical lifts(D)
 <= 4*tau(xi*C*u)*tau(k*C*v)
      *max tau(r_1*r_2)tau(s_1*s_2)
           tau(x_1*x_2)tau(y_1*y_2)
 = B^o(1).                                           (2.7)
```

This is uniform because the number of divisor factors is fixed and every
argument is polynomially bounded in `B`.

### 2.3 Joint decorations do not reopen the fiber

For each physical lift:

- the primitive `z` ratio is the deterministic reduction of `(z_1,z_2)`;
- s7-21 has only `B^o(1)` legal primewise orientation branches in total;
- each 4cf Gaussian square divisor is unique up to a Gaussian unit;
- canonical and physical masks remain deterministic tests.

Multiplying (2.7) by these `B^o(1)`/constant decoration counts still gives
`B^o(1)`. This proves the X0 lemma for the complete
`JointBalancedCollisionPacket`, not merely for its undecorated state pair.

## 3. Exact transfer now available

Let

```text
G=(eight cells; C,u_res,v_res)
```

be the common-core shell datum, and let

```text
D=(primewise CRT orientation; primitive z ratio; xi-short-rank data)
```

be the dual-CRT refinement. Every physical endpoint pair determines both.
X0 proved the exact common refinement `(G,D)`. X1 now proves that the physical
fiber over fixed `G` — and therefore over fixed `(G,D)` — is `B^o(1)`.

The legal conclusion is

```text
common-core count may retain all CRT restrictions at B^o(1) charge;
CRT short-vector count may retain the common-core labels with no
independent-savings multiplication;
every physical pair is charged only B^o(1) times in the joint packet.       (3.1)
```

This closes the **adapter/fiber obligation** between the two s-side
descriptions. It does not prove either remaining average estimate. In
particular, X1 does not turn the number of possible eight-cell or orientation
packets into `B^o(1)`.

## 4. What remains after the lemma

Merged 4ch leaves

```text
CommonCoreResidualEightCellMultiplicity
```

over the residual support

```text
C<=B^(3/8+o(1)),
u_res*v_res<=B^(1/4+o(1)),
# residual triples<=B^(5/8+o(1)).                  (4.1)
```

Merged s7-22 refines the same cell packets to

```text
ProductRatioStratifiedXiDualResonanceEnergy,
```

with a separate rank-at-most-two branch and a rank-three branch carrying
primitive normal `c`, near-full saturation `d_H`, cellwise dual components,
and the tangent/non-tangent split.

The minimal joint receiver after X1 is therefore

```text
JointCommonCoreResidualDualResonancePacketEnergy.  (4.2)
```

For one residual triple, let `Omega(C,u_res,v_res)` be the legal balanced
eight-cell/orientation packets equipped with their s7-22 product-ratio and
rank/resonance data. X1 supplies the charge-preserving inequality

```text
physical endpoint collision mass
 <= B^o(1) * sum_{C,u_res,v_res} #Omega(C,u_res,v_res).  (4.3)
```

The next analytic target is

```text
sum #Omega(C,u_res,v_res)
 <= B^(7/8-eta+o(1))                               (4.4)
```

for some fixed `eta>0`. Equivalently, an average packet multiplicity below
`B^(1/4-eta+o(1))` over the `B^(5/8+o(1))` residual support suffices.

Neither (4.4) nor any fixed positive `eta` is proved in X1.

## 5. Finite audit

The dedicated audit enumerates reduced states through `Q<=600`, selects every
same-`(xi,k)` dual-cross physical pair, reruns the s7-21 CRT checks and the 4ch
factor-pair reconstruction, and measures the exact fibers.

```text
dual-cross physical pairs                         52
distinct residual triples                         50
residual-triple max physical fiber                  2
fixed (eight cells,residual triple) max fiber       1
fixed joint data max fiber                          1
maximum finite divisor-bound proxy             491520
```

The two residual collisions of size two are:

```text
(C,u,v)=(5,104,17)
(41,54;1,246)  and  (29,70;45,406)

(C,u,v)=(5,17,104)
(13,95;245,247)  and  (41,99;361,451)
```

The first is the merged 4ch guard; the second is its companion with the
residual roles interchanged. Each collision uses two different eight-cell
packets. Thus the finite run confirms both sides of the quantifier boundary:

- dropping the cells is not injective;
- retaining the cells makes the tested physical fiber injective.

Finite injectivity is diagnostic only. The asymptotic `B^o(1)` theorem is
(2.1)--(2.7), not an inference from this scan.

## 6. Independent fixed-U route

Latest merged t59 narrows the fixed-`U` receiver to

```text
SharedUEnergyBalancedOrthogonalRectangleSecondMoment.
```

Its same-modulus signed bilinear cancellation is not a specialization of the
positive s-side fiber theorem above. X1 neither proves nor alters it. `tH16`
remains needed for that updated receiver; no new X-side or toolbox H line is
created.

## Route decision

```text
MAIN_S_ROUTE_BLOCKED_BY_X1=false
S_ROUTE_BLOCKED_BY_X1=false
T_TH_ROUTE_BLOCKED_BY_X1=false
TOOLBOX_ROUTE_BLOCKED_BY_X1=false
X1_AUXILIARY_H_NEEDED=false
```

All ordinary routes may continue. The joint cell/resonance intersection is
reserved for a possible `Stage14-X2`; it should not be duplicated as an
independent lemma by the ordinary routes.

## Locked boundary

```text
STAGE14_X1=COMPLETE_JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_LEMMA
MAIN_SNAPSHOT=f36506bfe404637a6d989d5e56fa698018a661d9
MERGED_X0_IMPORTED=true
MERGED_4CH_IMPORTED=true
MERGED_S7_22_IMPORTED=true
JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_LEMMA_PROVED=true
JOINT_PHYSICAL_FIBER_BO1_PROVED=true
STRONGER_FIXED_EIGHT_CELLS_RESIDUAL_TRIPLE_FIBER_BO1_PROVED=true
PRIMITIVE_Z_RATIO_NEEDED_FOR_FIBER_BOUND=false
PRIMEWISE_ORIENTATION_NEEDED_FOR_FIBER_BOUND=false
CCGRI_BDCSVE_JOINT_CHARGE_ADAPTER_PROVED=true
COMMON_CORE_RESIDUAL_EIGHT_CELL_MULTIPLICITY_PROVED=false
PRODUCT_RATIO_STRATIFIED_XI_DUAL_RESONANCE_ENERGY_PROVED=false
JOINT_COMMON_CORE_RESIDUAL_DUAL_RESONANCE_PACKET_ENERGY_PROVED=false
SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAIN_S_ROUTE_BLOCKED_BY_X1=false
S_ROUTE_BLOCKED_BY_X1=false
T_TH_ROUTE_BLOCKED_BY_X1=false
TOOLBOX_ROUTE_BLOCKED_BY_X1=false
X1_AUXILIARY_H_NEEDED=false
NEXT_RECOMMENDED=Stage14-X2 attack JointCommonCoreResidualDualResonancePacketEnergy by splitting rank<=2, rank3-nontangent, and rank3-tangent packets over the B^(5/8+o(1)) residual support
```
