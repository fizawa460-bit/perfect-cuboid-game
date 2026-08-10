# Stage14-X2 — Pluecker rank-one collapse of the joint common-core/CRT packet

## Status and source snapshot

`COMPLETE_PLUECKER_RANK_ONE_COLLAPSE_AND_JOINT_PACKET_REDUCTION`

This stage is the independent continuation of merged Stage14-X1.  It writes
only in the dedicated `Stage14-X2` area and its dedicated CI workflow.

```text
main snapshot                         0c22182d1a0d9c3ef4eb7ecd5fce980e46c95d12
merged X1                              e7ead5bb902583b4b3c797e10e44007113dc8bd0
merged mainline input                  14-4ci
merged s input                         14-s7-23
latest independent fixed-U input       14-t60
```

No canonical index, predecessor result, or exponent ledger is edited.

### Publication-base alignment

Before X2 was published, current `main` advanced to
`9bc1481c2cc44499571beb628d9e08a3b2c16b11` and independently merged both
Stage14-4cj and Stage14-s7-24.  Those two stages prove the same rank-two
elimination / rank-one physical-root conclusion, with s7-24 additionally
recording the saturated `xi^2` quotient.  Therefore X2 does **not** claim
priority or a new rank-one theorem relative to its publication base.

Its retained cross-route contribution is the exact reduction of the merged X1
joint receiver to

```text
PrimitiveLineCommonCoreNormalizedHostMultiplicity,
```

together with the charged-once finite fiber diagnostics and the X3 decision.
The merged 4cj/s7-24 files are read-only corroborating inputs; no power saving
is promoted from their agreement.

## 1. Verdict

X1 left the joint receiver

```text
JointCommonCoreResidualDualResonancePacketEnergy
```

and proposed a split into `xi` short ranks at most two, rank-three
non-tangent, and rank-three tangent.  Merged s7-23 subsequently proved that
both rank-three branches are empty.

At the source snapshot, Stage14-X2 independently proved the stronger missing
statement

```text
RANK2_PHYSICAL_ENDPOINT_PACKETS_EXIST=false.
```

In fact, four exact Pluecker-minor divisibilities already rule out any two
independent endpoint-short vectors in one oriented `xi` CRT lattice.  Since
the positive physical root vector is present, the endpoint-short span has
exact rank one:

```text
boxed:
dim span_Q(Lambda_xi(Pi) cap [-CL,CL]^4)=1.        (1.1)
```

Thus the rank-three elimination of s7-23 remains valid but is subsumed, on the
current endpoint, by a direct rank-one theorem.

This closes the **internal short-vector rank/energy** of each fixed oriented
packet.  It does not count how many moving eight-cell packets occur over the
common-core residual support.  Therefore the joint packet-energy receiver is
not proved, no fixed `eta` is declared, and the whole-family exponent remains
`7/8`.

## 2. Exact cross-minor divisibilities

Fix one legal balanced endpoint orientation packet `Pi`.  Its `xi` lattice is

```text
Lambda_xi(Pi) subset Z^4
```

on coordinates

```text
X=(x_1,y_1,x_2,y_2)
```

with the merged s7-21 congruences

```text
y_1 == lambda_R*y_2 (mod R^2),
x_1 == lambda_J*x_2 (mod J^2),
x_2 == lambda_S*y_1 (mod S^2),
y_2 == lambda_T*x_1 (mod T^2).                    (2.1)
```

Take any two lattice vectors

```text
u=(u_1,u_2,u_3,u_4),
v=(v_1,v_2,v_3,v_4)
```

and write their Pluecker minors as

```text
p_ij=u_i*v_j-u_j*v_i.
```

Apply each fixed congruence in (2.1) to both `u` and `v`.  Taking the
determinant of the corresponding pair of coordinate columns cancels the
branch parameter exactly and gives

```text
boxed:
R^2 | p_24,
J^2 | p_13,
S^2 | p_23,
T^2 | p_14.                                       (2.2)
```

For example,

```text
p_24
 =u_2*v_4-u_4*v_2
 ==lambda_R*u_4*v_4-u_4*lambda_R*v_4
 ==0 (mod R^2).
```

The other three identities are identical.  No dual character, density
heuristic, or independence assertion is used.

## 3. Endpoint size forces all four cross minors to vanish

Merged s7-20/s7-21 gives

```text
|u_i|,|v_i| <= B^(1/16+o(1))                      (3.1)
```

for endpoint-short vectors.  Therefore

```text
|p_ij| <= B^(1/8+o(1)).                            (3.2)
```

Every balanced `xi` cell satisfies

```text
R,S,T,J >= B^(1/8-o(1)),                           (3.3)
```

so every cell-square modulus in (2.2) is at least

```text
B^(1/4-o(1)).                                      (3.4)
```

The exponent gap is

```text
1/4-1/8=1/8.                                       (3.5)
```

It is uniform under all retained `B^o(1)` dyadic widths.  Hence, for
sufficiently large `B`, divisibility (2.2) and bounds (3.2)-(3.4) imply

```text
boxed:
p_13=p_14=p_23=p_24=0.                             (3.6)
```

## 4. Pluecker classification excludes rank two

Assume `u,v` are independent.  Their six minors obey the Grassmann-Pluecker
relation

```text
p_12*p_34-p_13*p_24+p_14*p_23=0.                  (4.1)
```

By (3.6),

```text
p_12*p_34=0.                                       (4.2)
```

Since `u,v` are independent, not all minors vanish.

- If `p_12 != 0`, the first two coordinate columns are independent.  Their
  determinants with each of columns three and four are zero by (3.6), so
  columns three and four themselves are zero.  The plane spanned by `u,v` is
  contained in `{x_2=y_2=0}`.
- If `p_34 != 0`, the symmetric argument puts the plane in
  `{x_1=y_1=0}`.
- If both `p_12` and `p_34` vanish, all six minors vanish, contradicting
  independence.

Every physical packet contains

```text
X_phys=(x_1,y_1,x_2,y_2),
x_1,y_1,x_2,y_2>0,                                 (4.3)
```

inside its endpoint-short span.  It belongs to neither coordinate plane.
Thus two independent endpoint-short vectors cannot exist:

```text
boxed:
dim S(Pi)<=1.                                      (4.4)
```

Because `X_phys` is nonzero and lies in `S(Pi)`, equality holds.  This proves
(1.1) and eliminates rank two as well as rank three.

## 5. The surviving line is the primitive physical root line

For each reduced physical state,

```text
gcd(P_i,Q_i)=1,
P_i=a_i*x_i^2,
Q_i=b_i*y_i^2.
```

Hence

```text
gcd(x_i,y_i)=1,
```

so the four-coordinate vector `X_phys` is primitive in `Z^4`.  Consequently

```text
Z^4 cap Q*X_phys=Z*X_phys.                          (5.1)
```

Combining (1.1) and (5.1), every integer endpoint-short vector in the fixed
orientation packet is an integer multiple of the physical root vector.
Since the retained endpoint dyadic cell has

```text
max(x_1,y_1,x_2,y_2)=B^(1/16+o(1)),
```

only `B^o(1)` such multiples remain in the endpoint box.  Therefore

```text
boxed:
#(Lambda_xi(Pi) cap endpoint box)=B^o(1)           (5.2)
```

for every physical oriented packet `Pi`.

The `k` side was already a primitive fully saturated line by merged 4ci.  X2
shows that the `xi` side also has no rank-two or rank-three short-direction
choice.  Primewise orientation and short-vector multiplicity are no longer
live fixed-power losses in the joint packet.

## 6. Exact reduction of the X1 receiver

Let

```text
Omega(C,u_res,v_res)
```

be the X1 charged-once joint packets.  Decompose it by `xi` short rank:

```text
Omega=Omega_rank1 disjoint union Omega_rank2 disjoint union Omega_rank3.
```

Merged s7-23 and X2 give

```text
Omega_rank3=empty,
Omega_rank2=empty.                                  (6.1)
```

For the surviving rank-one packet, (5.2) gives only `B^o(1)` compatible
short vectors.  Together with the X1 fixed-cell/residual physical-fiber lemma,
the physical endpoint collision mass is therefore bounded by

```text
B^o(1)
* # {
    (C,u_res,v_res),
    balanced eight cells,
    primitive positive physical root line,
    4ci normalized host data
  }.                                                (6.2)
```

Every item in (6.2) belongs to the same physical packet.  No independent
common-core and CRT saving is multiplied.

Define the remaining receiver

```text
PrimitiveLineCommonCoreNormalizedHostMultiplicity. (6.3)
```

It retains

```text
- q_k=C*u_res and q_xi=C*v_res;
- all eight balanced cells;
- t^2 | C*u_res and h^2 | C*v_res;
- the four normalized host equations of 4ci;
- the primitive positive root line Z*X_phys;
- the fully saturated primitive k line;
- all canonical, primitive, interval, and reconstruction masks.
```

The old three-way dual-resonance receiver has therefore been reduced exactly
to this rank-one common-core cell/line multiplicity.

## 7. Quantitative target after the collapse

Globally, merged 4ch gives residual support

```text
# {(C,u_res,v_res)} <= B^(5/8+o(1)).                (7.1)
```

Merged 4ci refines the support in a fixed `(theta,phi)` block to exponent

```text
2*(theta+phi)-1/2.                                 (7.2)
```

X2 removes every additional fixed-power short-rank and orientation fiber, but
does not bound how many primitive-line/eight-cell packets lie above this
support.  A sufficient global theorem remains

```text
average primitive-line/eight-cell multiplicity
per residual triple
 << B^(1/4-eta+o(1))                               (7.3)
```

for some fixed `eta>0`.  Equivalently,

```text
PrimitiveLineCommonCoreNormalizedHostMultiplicity
 << B^(7/8-eta+o(1)).                              (7.4)
```

Neither (7.3) nor (7.4) is proved here.

## 8. Finite diagnostics

The dedicated audit enumerates all same-`(xi,k)`, dual-cross physical pairs
through `Q<=600`, reconstructs the X1/4ci data, builds an independent exact
vector in each corresponding `xi` lattice, and verifies every divisibility in
(2.2).  It also exhausts all ordered pairs of vectors in `[-2,2]^4` satisfying
the four-zero-cross-minor condition and checks the coordinate-plane
classification.

```text
dual-cross physical pairs                              52
distinct residual triples                              50
residual-triple maximum physical fiber                  2
fixed residual triple + primitive root line max fiber   1
fixed cells + residual + primitive line max fiber       1
nonzero cross minors checked with exact divisibility   176
coordinate-plane matrix pairs exhaustively checked     992
```

The frozen X1 witness remains:

```text
(C,u,v)=(5,104,17)
(41,54;1,246) and (29,70;45,406).
```

The two packets have different cells and different primitive root lines.
Thus residual-only injectivity remains false in the finite sample even after
the rank-one coordinate is recorded as the correct surviving variable.

Finite injectivity after adjoining the line is diagnostic only.  It is not a
proof of (7.3).  The asymptotic rank-one theorem is Sections 2-5.

## 9. Independent fixed-U route

Merged t60 reduces the fixed-`U` receiver to the matched pair

```text
CanonicalPrimePolarKummerFourthMoment,
PrimitiveCoverPolarKummerFourthMoment.
```

Those signed same-auxiliary-pair fourth moments are not consequences of the
positive Pluecker argument above.  X2 neither proves nor alters them.  No new
X-side H line or tH line is needed for the rank-one theorem.

## 10. X3 decision

`Stage14-X3` is justified.  The remaining object still simultaneously uses
the mainline common-core normalized equations and the s-side primitive CRT
line, so it is a genuine cross-route problem rather than a single-route
duplicate.

The next attack should fix `(C,u_res,v_res)` and its divisor-many scales
`(t,h)`, retain the primitive root line, and test whether the four 4ci
normalized host equations recover the moving eight cells with a fixed-power
average saving.  It must also search for parametric high-multiplicity
counterexamples before declaring any fiber theorem.

All ordinary routes may continue.  No route is blocked by X2.

## Locked boundary

```text
STAGE14_X2=COMPLETE_PLUECKER_RANK_ONE_COLLAPSE_AND_JOINT_PACKET_REDUCTION
MAIN_SNAPSHOT=0c22182d1a0d9c3ef4eb7ecd5fce980e46c95d12
PUBLICATION_BASE_MAIN=9bc1481c2cc44499571beb628d9e08a3b2c16b11
MERGED_X1_IMPORTED=true
MERGED_4CI_IMPORTED=true
MERGED_S7_23_IMPORTED=true
MERGED_4CJ_CORROBORATES_X2=true
MERGED_S7_24_CORROBORATES_X2=true
X2_RANK_ONE_NOVEL_ON_PUBLICATION_BASE=false
XI_CRT_CROSS_MINOR_DIVISIBILITY_EXACT=true
R_SQUARE_DIVIDES_P24=true
J_SQUARE_DIVIDES_P13=true
S_SQUARE_DIVIDES_P23=true
T_SQUARE_DIVIDES_P14=true
XI_SHORT_PLUECKER_MINOR_MAX_EXPONENT=1/8
XI_CELL_SQUARE_MIN_EXPONENT=1/4
XI_MINOR_MODULUS_GAP_EXPONENT=1/8
XI_SHORT_CROSS_MINORS_ZERO=true
RANK2_PHYSICAL_ENDPOINT_PACKETS_EXIST=false
RANK3_PHYSICAL_ENDPOINT_PACKETS_EXIST=false
XI_ROOT_SHORT_VECTOR_RANK_EXACT=1
PHYSICAL_XI_ROOT_LINE_PRIMITIVE=true
FIXED_ORIENTED_XI_PACKET_SHORT_VECTOR_MASS_BO1=true
JOINT_PACKET_RANK2_ENERGY=0
JOINT_PACKET_RANK3_ENERGY=0
PRIMITIVE_LINE_COMMON_CORE_NORMALIZED_HOST_MULTIPLICITY_REQUIRED=true
PRIMITIVE_LINE_COMMON_CORE_NORMALIZED_HOST_MULTIPLICITY_PROVED=false
JOINT_COMMON_CORE_RESIDUAL_DUAL_RESONANCE_PACKET_ENERGY_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAIN_S_ROUTE_BLOCKED_BY_X2=false
S_ROUTE_BLOCKED_BY_X2=false
T_TH_ROUTE_BLOCKED_BY_X2=false
TOOLBOX_ROUTE_BLOCKED_BY_X2=false
X2_AUXILIARY_H_NEEDED=false
X3_RECOMMENDED=true
NEXT_RECOMMENDED=Stage14-X3 attack PrimitiveLineCommonCoreNormalizedHostMultiplicity by fixed-residual primitive-line cell elimination and parametric counterexample search
```
