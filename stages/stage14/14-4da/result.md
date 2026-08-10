# Stage14-4da — reverse reciprocal divisor reconstruction and mainline square-root closure

## Status

`COMPLETE_REVERSE_RECIPROCAL_DIVISOR_RECONSTRUCTION_AND_MAINLINE_SQRT_CLOSURE`

Stage14-4da is based only on merged main inputs. It consumes merged `Stage14-4cz`, merged `Stage14-s7-41`, and the exact reciprocal / column reconstruction infrastructure of merged `s7-27`, `s7-28`, `4cv`, `4cx`, `4cy`, and `s7-37`.

The entering canonical theorem is

```text
V(B) << B^(23/44+o(1)).
```

Stage14-4da proves the exact square-root upper bound

```text
boxed:
V(B) << B^(1/2+o(1)).
```

The new ingredient is deterministic. No external sieve, determinant theorem, genus-one theorem, large sieve, H theorem, or tH theorem is used.

The key lemma is:

```text
fixed legal outer decoration + fixed (U,V,M)
=> # {(a,b,c,d,p,q)} <= B^o(1)
=> # {N=abcd} <= B^o(1).
```

Thus the old Cayley-row lift is not an independent support once the endpoint-linear column has reconstructed `M`.

---

## 1. Imported balanced packet

Use the merged endpoint strip

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8,

C=B^(chi+o(1)),
chi=2theta+2phi-3/4.
```

The available complete bounds include

```text
E_s <= max(2theta,1-2theta),
E_k <= 3theta-1/4.
```

Merged s7-37 gives for the proportional branch

```text
boxed:
E_prop <= 7/16 < 1/2.                              (1.1)
```

Merged 4cx proves that every fixed-power nonproportional packet with

```text
chi>1/4
```

is empty. Therefore every nonproportional packet that still needs counting satisfies

```text
boxed:
chi<=1/4.                                          (1.2)
```

Merged 4cy/s7-40/4cz/s7-41 refine the old 23/44 endpoint, but 4da will use a uniform low-core reconstruction and does not require old 23/44 saturation to remain primitive.

---

## 2. Reciprocal notation and legal quantifier order

Use the signed quotient notation

```text
U=L_x^+,
V=L_x^-,
gcd(U,V)=1,

p=L_k^+,
q=L_k^-,

a=c_x^+,
b=c_x^-,
c=c_k^+,
d=c_k^-.
```

The exact reciprocal equations are

```text
(aU)^2-(bV)^2 = 4rs epsilon_k p q,                 (2.1)
(cp)^2-(dq)^2 = 4XY epsilon_x U V.                 (2.2)
```

On physical packets

```text
aU=D+A,
bV=D-A,
D>A>0,

cp=Q+P,
dq=Q-P,
Q>P>0.                                             (2.3)
```

Hence all four quantities in (2.3) are positive integers.

The legal count order inherited from merged 4cv/4cx is

```text
once-charged common-core data
-> primitive common-core pair (U,V)
-> legal endpoint-linear column sign allocation
-> endpoint-linear cofactors
-> z1,z2
-> M
-> remaining reciprocal completion.
```

Endpoint-small values such as `r_i,s_i`, finite 2-primary choices, `g_i in {1,2}`, and sign/orientation decorations have total multiplicity `B^o(1)` and are included in the phrase **fixed legal outer decoration** below.

---

## 3. The column fixes M and XY

The endpoint variables satisfy

```text
z_i = 2x_i y_i/g_i,
g_i in {1,2},
X=x1*x2,
Y=y1*y2.
```

Therefore

```text
z1*z2 = 4XY/(g1*g2).                               (3.1)
```

The Cayley numerator is

```text
M=4rsXY epsilon_x epsilon_k.                       (3.2)
```

Combining (3.1) and (3.2),

```text
boxed:
M=rs epsilon_x epsilon_k g1 g2 z1 z2.              (3.3)
```

Merged endpoint-linear column reconstruction has

```text
L_- = z1 r2 s2-z2 r1 s1,
L_+ = z1 r2 s2+z2 r1 s1,
```

and reconstructs `(z1,z2)` from the column data with only divisor-many endpoint-small ambiguity. Thus, after fixing the legal outer decoration, the column fixes `M`.

Equivalently, (3.2) fixes

```text
boxed:
XY=M/(4rs epsilon_x epsilon_k)                     (3.4)
```

whenever a physical completion exists.

This is the only fact needed before reversing the reciprocal equations.

---

## 4. Reverse the second reciprocal equation

Fix a legal outer decoration and `(U,V,M)`. By (3.4), `XY` is fixed. Hence the positive integer

```text
W_2:=4XY epsilon_x U V                             (4.1)
```

is fixed.

Equation (2.2) is

```text
(cp)^2-(dq)^2=W_2.
```

Using physical positivity,

```text
(cp-dq)(cp+dq)=W_2,                                (4.2)
```

with

```text
cp-dq=2P>0,
cp+dq=2Q>0.                                        (4.3)
```

A polynomially bounded fixed integer has `B^o(1)` positive divisor pairs. Therefore (4.2) gives `B^o(1)` possibilities for

```text
F_2^-:=cp-dq,
F_2^+:=cp+dq.
```

For each legal parity pair,

```text
cp=(F_2^++F_2^-)/2,
dq=(F_2^+-F_2^-)/2.                                (4.4)
```

Each fixed positive product in (4.4) has only divisor-many ordered factorizations. Hence

```text
boxed:
fixed legal outer decoration + (U,V,M)
=> # {(c,d,p,q)} <= B^o(1).                        (4.5)
```

All coprimality, squarefree-cell, dyadic, sign, orientation, and physical masks are filters on these divisor pairs and cannot enlarge the count.

No common-core modulus is used in this step.

---

## 5. Reverse the first reciprocal equation

For each divisor-many tuple `(c,d,p,q)` from Section 4, the product `pq` is fixed. Set

```text
W_1:=4rs epsilon_k p q.                            (5.1)
```

Equation (2.1) becomes

```text
(aU)^2-(bV)^2=W_1.
```

Physical positivity gives

```text
(aU-bV)(aU+bV)=W_1,                                (5.2)
```

with

```text
aU-bV=2A>0,
aU+bV=2D>0.                                        (5.3)
```

Again the fixed integer `W_1` has only divisor-many positive factor pairs. For each legal parity pair

```text
F_1^-:=aU-bV,
F_1^+:=aU+bV,
```

we recover

```text
aU=(F_1^++F_1^-)/2,
bV=(F_1^+-F_1^-)/2.                                (5.4)
```

Because `U,V` are fixed, divisibility by `U,V` determines `a,b` whenever the candidate is physical. Consequently

```text
boxed:
fixed legal outer decoration + (U,V,M,c,d,p,q)
=> # {(a,b)} <= B^o(1).                            (5.5)
```

Combining (4.5) and (5.5),

```text
boxed:
fixed legal outer decoration + (U,V,M)
=> # {(a,b,c,d,p,q)} <= B^o(1).                    (5.6)
```

and therefore

```text
boxed:
fixed legal outer decoration + (U,V,M)
=> # {N=a b c d} <= B^o(1).                        (5.7)
```

This is the **reverse reciprocal divisor reconstruction lemma**.

---

## 6. Relation to merged s7-41 and its H gate

Merged s7-41 proves that, after its common base is fixed, the first residual state and the twin row/column short state map to one another with `B^o(1)` fibers. It also correctly records

```text
REVERSE_ROOT_LINE_REUSE_WITHOUT_QUANTIFIER_BRIDGE_ALLOWED=false.
```

That prohibition remains valid.

Stage14-4da does not fix `(U,V)` and then reapply the same common-core root line to `(a,b)`. Instead:

1. the common core is charged once to choose the primitive `(U,V)` packet;
2. the endpoint-linear column reconstructs the integer `M`;
3. with `(U,V,M)` fixed, Sections 4--5 use only exact integer equalities and divisor factorization.

Thus the missing quantifier bridge is supplied without any reverse use of the common-core spacing modulus.

```text
boxed:
S7_41_REVERSE_ROOT_LINE_NOGO_RESPECTED=true,

boxed:
S7_41_MAINLINE_H_GATE_SUPERSEDED_BY_REVERSE_RECIPROCAL_BRIDGE=true.   (6.1)
```

The s7-41 H target remains a meaningful independent s-route analytic receiver, but it is no longer necessary for the mainline square-root upper bound.

---

## 7. The Cayley row is now a filter

Merged row/column reconstruction imposes, after the column has reconstructed `M`,

```text
N == M  (mod C_-),
N == -M (mod C_+),
C_- C_+=C_Cayley.                                  (7.1)
```

Previously a short `N` lift was counted after this step.

But Section 5 proves that, for the already-fixed `(U,V,M)`, only `B^o(1)` values of `N` are compatible with the original reciprocal equations. Therefore the congruences (7.1) only retain or reject divisor-many candidates.

Hence

```text
boxed:
ROW_CRT_LIFT_INDEPENDENT_SUPPORT=false,             (7.2)

boxed:
POST_COLUMN_ROW_RECONSTRUCTION_MULTIPLICITY=Bo1.    (7.3)
```

This is not a double saving. It is a correction of the legal quantifier order: the row lift was an upper-bound convenience, not a genuinely independent physical degree of freedom after `M` is known.

Merged s7-28 then reconstructs the remaining labelled physical cell data with divisor-many multiplicity; no new fixed-power residual support reappears.

---

## 8. New low-core nonproportional complete count

On the nonproportional low-core region `chi<=1/4`, use the legal order

```text
C
-> primitive common-core pair (U,V)
-> reduced endpoint-linear column
-> M
-> reverse reciprocal divisor reconstruction
-> row filter
-> divisor-many physical completion.
```

The fixed-power costs are

```text
common core C:                       chi,
primitive (U,V) after C:             2phi-chi,
reduced column support:              1/4-chi,
reverse reciprocal completion:       0,
row CRT filter:                       0.
```

Therefore

```text
boxed:
E_RRF <= 2phi+1/4-chi.                              (8.1)
```

Using

```text
chi=2theta+2phi-3/4,
```

we obtain the exact simplification

```text
boxed:
E_RRF <= 1-2theta.                                 (8.2)
```

For fixed-power `chi>1/4`, merged 4cx already makes the nonproportional region empty.

---

## 9. Whole-family square-root closure

We cover the entire physical family with complete bounds.

### 9.1 Proportional branch

Merged s7-37 gives

```text
E_prop<=7/16<1/2.                                  (9.1)
```

### 9.2 Nonproportional branch, theta<=1/4

Use the merged k-host bound:

```text
E<=E_k<=3theta-1/4<=1/2.                           (9.2)
```

### 9.3 Nonproportional branch, theta>=1/4

If `chi>1/4`, the fixed-power packet is empty by merged 4cx. Otherwise (8.2) gives

```text
E<=E_RRF<=1-2theta<=1/2.                           (9.3)
```

The three cases are exhaustive. Hence

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2,         (9.4)

boxed:
V(B) << B^(1/2+o(1)).                              (9.5)
```

The improvement over the entering merged theorem is exactly

```text
23/44-1/2=1/44.                                    (9.6)
```

Therefore

```text
boxed:
IMPROVEMENT_OVER_MERGED_23_44=1/44,

boxed:
SQRT_B_UPPER_BOUND_PROVED=true.                    (9.7)
```

No uniform bound `B^(1/2-delta)` for fixed `delta>0` is claimed.

---

## 10. Square-root saturation geometry

The new envelope is strict away from `theta=1/4`:

- if `theta<1/4`, `E_k<1/2`;
- if `theta>1/4` and the packet is nonempty, `E_RRF<1/2`.

Therefore any sequence saturating the `1/2` upper envelope must satisfy

```text
boxed:
theta=1/4.                                         (10.1)
```

At `theta=1/4`,

```text
chi=2phi-1/4,
E_k=1/2,
E_s=1/2,
E_RRF=1/2.                                         (10.2)
```

The balanced strip gives

```text
1/8<=phi<=1/4.                                     (10.3)
```

Retain the merged fourth-power cross-root complete count

```text
E_H<=3phi-1/8-3s,
H=B^(s+o(1)).                                      (10.4)
```

For this alternative count not to save below `1/2`, one must have

```text
3phi-1/8-3s>=1/2,
```

or equivalently

```text
boxed:
phi-s>=5/24.                                       (10.5)
```

Thus every possible square-root equality packet lies in

```text
boxed:
theta=1/4,
5/24<=phi<=1/4,
0<=s<=phi-5/24,
chi=2phi-1/4 in [1/6,1/4].                         (10.6)
```

The fixed-power decomposition of the new complete count is

```text
common-core + primitive-pair base = 2phi,
column support                    = 1/4-chi = 1/2-2phi,
post-column reciprocal completion = 0.
```

At `phi=5/24` these are

```text
5/12 + 1/12 = 1/2.
```

At `phi=1/4` they are

```text
1/2 + 0 = 1/2.
```

Hence the old twin-short / first-residual `23/44` receiver is closed. The obstruction to a strict sub-square-root bound is now a theta-quarter band with only a **single** column support after the common-core/primitive-pair base.

Define the new receiver

```text
SquareRootThetaQuarterPrimitiveCommonCoreSingleColumnReverseReciprocalIncidence.
```

Mandatory fixed-power data:

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
nonproportional,
0<=s<=phi-5/24,
column support<=B^(1/2-2phi+o(1)),
post-column reciprocal multiplicity=B^o(1),
row CRT lift independent support=false.
```

---

## 11. Parallel-route compatibility

A parallel working branch `Stage14-X13` contains a compatible reverse-reciprocal square-root derivation. It is not used as a hard predecessor, imported theorem, or CI dependency of Stage14-4da.

Stage14-4da was written against merged main equations and predecessor theorem locks only.

The fixed-U t/tH route remains a different coefficient space. In particular merged t79 / open t80 / tH22 are not cross-promoted into the 4da proof.

```text
OPEN_X13_USED_AS_HARD_PREDECESSOR=false,
X13_REVERSE_RECIPROCAL_RESULT_COMPATIBLE=true,
T79_CROSS_PROMOTED_TO_MAINLINE=false,
T80_CROSS_PROMOTED_TO_MAINLINE=false,
TH22_CROSS_PROMOTED_TO_MAINLINE=false.
```

---

## 12. H / tH decision

The mainline does not need a new H theorem for square-root closure.

Merged s7-41 requested the s-specific auxiliary theorem

```text
TwentyThreeFortyFourthsZeroCrossRootEqualCoreFirstResidualTwinShortIncidencePowerSaving.
```

That request was valid for the s-route receiver it had reached. Stage14-4da now bypasses the missing incidence saving by proving that the post-column row variable has only divisor-many multiplicity through the exact reciprocal equations.

Therefore

```text
boxed:
MAINLINE_H_NEEDED=false,
MAINLINE_BLOCKED_BY_H=false,
S7_41_MAINLINE_H_GATE_SUPERSEDED=true,
GENERIC_GENUS_ONE_H_REOPENED=false.                (12.1)
```

If future work seeks a **strict** sub-square-root exponent, the relevant target must be formulated on the new theta-quarter single-column band, not on the eliminated twin-short `23/44` receiver.

---

## 13. Validation contract

The dedicated Stage14-4da audit must verify:

1. exact difference-of-squares divisor reconstruction;
2. reverse second-equation factorization and product splitting;
3. reverse first-equation factorization;
4. exact identity `E_RRF=1-2theta`;
5. exhaustive rational-grid whole-strip square-root coverage;
6. square-root saturation band arithmetic;
7. merged 4cz regression;
8. merged s7-41 regression;
9. merged 4cx high-core emptiness lock;
10. merged s7-37 proportional `7/16` lock;
11. no open X13 or t-route file is required by CI.

---

## Stage boundary

```text
STAGE14_4DA=COMPLETE_REVERSE_RECIPROCAL_DIVISOR_RECONSTRUCTION_AND_MAINLINE_SQRT_CLOSURE
MERGED_4CZ_IMPORTED=true
MERGED_S7_41_IMPORTED=true
S7_41_REVERSE_ROOT_LINE_NOGO_RESPECTED=true
REVERSE_RECIPROCAL_QUANTIFIER_BRIDGE_PROVED=true
FIXED_UV_M_REVERSE_SECOND_RECIPROCAL_MULTIPLICITY=Bo1
FIXED_UV_M_REVERSE_FIRST_RECIPROCAL_MULTIPLICITY=Bo1
FIXED_UV_M_FULL_SIGNED_QUOTIENT_MULTIPLICITY=Bo1
FIXED_UV_M_N_MULTIPLICITY=Bo1
ROW_CRT_LIFT_INDEPENDENT_SUPPORT=false
POST_COLUMN_ROW_RECONSTRUCTION_MULTIPLICITY=Bo1
LOW_CORE_REVERSE_RECIPROCAL_COMPLETE_COUNT=2phi+1/4-chi
LOW_CORE_REVERSE_RECIPROCAL_COMPLETE_COUNT_SIMPLIFIED=1-2theta
NONPROPORTIONAL_HIGH_CORE_FIXED_POWER_REGION_EMPTY=true
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
IMPROVEMENT_OVER_MERGED_23_44=1/44
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUB_SQRT_POWER_SAVING_PROVED=false
SQRT_SATURATION_THETA=1/4
SQRT_SATURATION_PHI_RANGE=[5/24,1/4]
SQRT_SATURATION_CHI_RANGE=[1/6,1/4]
SQRT_SATURATION_CROSS_ROOT_CONDITION=phi-s>=5/24
REMAINING_RECEIVER=SquareRootThetaQuarterPrimitiveCommonCoreSingleColumnReverseReciprocalIncidence
S7_41_MAINLINE_H_GATE_SUPERSEDED=true
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
OPEN_X13_USED_AS_HARD_PREDECESSOR=false
X13_REVERSE_RECIPROCAL_RESULT_COMPATIBLE=true
T79_CROSS_PROMOTED_TO_MAINLINE=false
T80_CROSS_PROMOTED_TO_MAINLINE=false
TH22_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4db
```
