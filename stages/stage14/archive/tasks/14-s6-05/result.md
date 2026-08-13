# Stage14-s6-05 — compact 2-torsion normalization and physical-class reduction

## Purpose

Merged Stage14-4bj reunifies the main track and freezes the least denominator `D_min` of an abstract bounded-height global representative as the remaining packet-level gate. Stage14-s6-05 sharpens that setup before attempting a new distribution theorem.

The key point is that a physical Stage14 hit already supplies a very special rational point on

```text
E_{S,X}: W^2=Z(Z-S^2)(Z+X^2),
S^2+X^2=H^2.
```

The exact s3 physical map places that point on the identity real component `Z>S^2`. Translating by the rational 2-torsion point

```text
T0=(0,0)
```

sends it explicitly to the compact component `-X^2<Z<0` while preserving canonical height and non-torsion. A compact-component point cannot lie in `2E(R)`, hence cannot lie in `2E(Q)`. Therefore the translated point already gives a nonzero Kummer class.

Consequently the maximal-halving step used in s6-01 is unnecessary for the physical upper majorant. More importantly, the selected physical class is forced into the compact `(--+)` cover chamber, where the two-quadrics become positive definite and the square variables satisfy `|u_i|<=BD`.

The translation is an explicit involution, so physical reconstruction is retained. Its reduced denominator is tied exactly to the numerator of the original physical point. This refines the 4bj `D_min` gate: `D_min` remains valid for arbitrary packets, but the physical upper bound can use the stronger torsion-normalized physical denominator `D_T`.

No positive post-local exponent is claimed in this stage.

---

## 1. Exact s3 physical point lies on `Z>S^2`

Stage14-s3 writes

```text
q   = X2/(H2+S2),
rho = X/H,
s   = S/H,
z   = gcd(S,S2)*d/(H*H2),
Yq  = z*(1+q^2),
X0  = (Yq+1)/q^2,
A0  = 1-2*rho^2,
x   = (A0+X0)/(2*s^2),
Z   = S^2*x.
```

For a positive physical partner,

```text
0<q<1,
z>0.
```

Since `rho^2+s^2=1`,

```text
A0=2*s^2-1.
```

Also `X0>1`. Hence

```text
x
 = (2*s^2-1+X0)/(2*s^2)
 = 1+(X0-1)/(2*s^2)
 >1.
```

Therefore

```text
boxed: Z>S^2.
```

The physical point is always on the identity/unbounded real component.

```text
PHYSICAL_POINT_REAL_COMPONENT=Z_GT_S2.
```

---

## 2. Exact translation by `(0,0)`

Write

```text
W^2=Z^3+(X^2-S^2)Z^2-S^2X^2 Z.
```

For `P=(Z,W)` and `T0=(0,0)`, the chord slope is `W/Z`. The addition law gives

```text
boxed:
Z(P+T0)=-S^2X^2/Z,
W(P+T0)=S^2X^2 W/Z^2.
```

Applying the map twice returns `P`.

```text
T0_TRANSLATION_FORMULA_EXACT=true.
```

If `Z>S^2`, then

```text
-X^2 < -S^2X^2/Z <0.
```

Thus every physical point is sent to the compact real component.

```text
PHYSICAL_TORSION_TRANSLATE_COMPACT=true.
```

---

## 3. The compact translate is automatically nonzero modulo 2

For this cubic the real locus has two components:

```text
identity component: Z>=S^2 together with O,
compact component : -X^2<=Z<=0.
```

The component group is `Z/2Z`; doubling kills it. Hence

```text
2E(R) subset E(R)^0.
```

Let `Q=P+T0`. Since `Q` lies on the compact/nonidentity component,

```text
Q notin 2E(R),
```

so certainly

```text
Q notin 2E(Q).
```

Therefore the Kummer class of `Q` is nonzero without any global halving.

```text
COMPACT_TRANSLATE_NONZERO_MOD_2=true
MAXIMAL_HALVING_REQUIRED_FOR_PHYSICAL_MAJORANT=false.
```

Merged Stage14 proves `P` is non-torsion; torsion translation preserves non-torsion. The Neron--Tate height is invariant under torsion translation, so

```text
hhat(Q)=hhat(P)=O(log B).
```

The same involution recovers `P=Q+T0`, so physical reconstruction is not discarded.

```text
TORSION_TRANSLATION_PRESERVES_HEIGHT_WINDOW=true
TORSION_TRANSLATION_PRESERVES_PHYSICAL_RECONSTRUCTION=true.
```

---

## 4. Physical packet signs are forced

Write the compact point in reduced coordinates

```text
Z_Q=A/D^2,
gcd(A,D)=1.
```

Its three cleared factors are

```text
G0=A,
G1=A-S^2D^2,
G2=A+X^2D^2.
```

Because `-X^2<Z_Q<0`,

```text
G0<0,
G1<0,
G2>0.
```

Thus the signed squarefree kernels satisfy

```text
d0<0,
d1<0,
d2>0.
```

In the s6-01 edge factorization

```text
d0=tau0*a*b,
d1=tau1*a*c,
d2=tau2*b*c,
```

with positive odd squarefree `a,b,c`, the signs are fixed to `(--+)`.

The admissible 2-adic parity condition allows exactly

```text
(-1,-1, 1),
(-2,-2, 1),
(-2,-1, 2),
(-1,-2, 2).
```

Hence the physical upper majorant needs only four of the sixteen abstract tau packets.

```text
PHYSICAL_COMPACT_TAU_PACKET_COUNT=4.
```

---

## 5. Compact cover is positive definite

Put

```text
e0=|d0|,
e1=|d1|,
e2=d2.
```

The two-quadrics and their sum become

```text
e1*u1^2-e0*u0^2 = S^2D^2,
e2*u2^2+e0*u0^2 = X^2D^2,
e2*u2^2+e1*u1^2 = H^2D^2.
```

The last two are positive definite. Therefore

```text
sqrt(e0)*|u0| <= X D,
sqrt(e2)*|u2| <= X D,
sqrt(e1)*|u1| <= H D.
```

Since `X,H<=B`,

```text
boxed: |u0|,|u1|,|u2| <= B D.
```

Thus the noncompact `+++` simultaneous-Pell chamber is not required for the physical upper majorant.

```text
PHYSICAL_COMPACT_COVER_POSITIVE_DEFINITE=true
PHYSICAL_COMPACT_COORDINATE_BOUND_U_LE_BD=true
NONCOMPACT_PELL_CHAMBER_REQUIRED_FOR_PHYSICAL_MAJORANT=false.
```

For comparison, in the abstract `+++` chamber one may fix `D` and let a real parameter `t=u1` grow, with

```text
u0^2=(d1*t^2+S^2D^2)/d0,
u2^2=(d1*t^2+H^2D^2)/d2.
```

So denominator size alone gives no archimedean coordinate bound there. The torsion normalization removes this escape before counting.

---

## 6. Exact denominator involution

Write the original physical point as

```text
Z_P=A_P/D_P^2,
gcd(A_P,D_P)=1,
A_P>0.
```

Then

```text
Z_Q=-S^2X^2D_P^2/A_P.
```

Let

```text
g=gcd(A_P,S^2X^2).
```

Since `gcd(A_P,D_P)=1`, the reduced denominator of `Z_Q` is exactly `A_P/g`. On the monic integral Weierstrass model, the reduced `Z` denominator is a square. Hence

```text
boxed:
D_T^2=D_Q^2=A_P/gcd(A_P,S^2X^2).
```

The reduced numerator is

```text
A_Q=-S^2X^2D_P^2/g.
```

The same formula in reverse follows because translation by `T0` is an involution.

```text
TORSION_TRANSLATE_DENOMINATOR_INVOLUTION_EXACT=true.
```

This gives a direct arithmetic receiver in the original physical variables: the compact-cover denominator is the square root of the part of the physical `Z` numerator not absorbed by `S^2X^2`.

---

## 7. Refinement of the merged 4bj least-denominator gate

Merged 4bj correctly defines, for an arbitrary locally admissible packet, the least denominator

```text
D_min(F,sigma;B)
```

among bounded-height global representatives and freezes its distribution as the main-track gate.

Stage14-s6-05 does not invalidate that statistic. It proves that for a **physical hit** there is a stronger canonical representative:

```text
Q=P_phys+(0,0).
```

This point is already

```text
compact,
non-torsion,
nonzero mod 2,
in the same height window,
physically reconstructible by the inverse torsion translation.
```

Define

```text
D_T(P_phys)=denominator(Q).
```

For the packet containing `Q`,

```text
D_min <= D_T.
```

But `D_T` keeps the exact physical numerator identity from Section 6, while a generic least-denominator representative need not.

Therefore the 4bj statement

```text
UNIQUE_POST_LOCAL_QUANTITATIVE_GATE=RADICAL_RICH_LEAST_DENOMINATOR_PACKET_DISTRIBUTION
```

is sharpened on the physical subfamily to

```text
RADICAL_RICH_TORSION_NORMALIZED_PHYSICAL_DENOMINATOR_AND_RECONSTRUCTION.
```

This is a refinement, not a contradiction: `D_min` remains the abstract packet statistic; `D_T` is the stronger physical selector.

```text
LEAST_DENOMINATOR_STATISTIC_RETAINED=true
LEAST_DENOMINATOR_PRIMARY_PHYSICAL_SELECTOR=false
TORSION_NORMALIZED_PHYSICAL_DENOMINATOR_PRIMARY=true.
```

---

## 8. Quantitative status

The structural gains are now:

1. no repeated halving for the physical majorant;
2. no noncompact real cover chamber for the selected physical class;
3. exactly four physical tau packets;
4. positive-definite coordinate control `|u_i|<=BD`;
5. exact physical reconstruction retained;
6. exact denominator/numerator involution.

What is **not** yet proved:

- a power-saving count for the torsion-normalized physical denominators;
- a moving-family count combining the compact witness with the second-face reconstruction;
- a packet/base-level transfer of the existing coordinate congruence savings.

Therefore

```text
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false.
```

The unconditional physical exponent remains

```text
41/42,
```

and the remaining saving required for the square-root scale remains

```text
10/21.
```

---

## 9. Next stage

Stage14-s6-06 should substitute the exact s3 physical formula for `Z_P` into

```text
D_T^2=A_P/gcd(A_P,S^2X^2)
```

and express the torsion-normalized denominator directly in the primitive second-face / space-diagonal variables.

The target is a genuine thin physical incidence involving

```text
first face (S,X,H),
second face (S2,X2,H2),
space diagonal d,
physical numerator A_P,
compact denominator D_T.
```

Because the torsion translation is invertible, any such restriction acts on the physical existence problem itself rather than on arbitrary coordinate density in a relaxed locally soluble packet.

The merged t33 Gaussian/Mellin route may be compared only after an exact variable identification; no spectral saving is imported here.

---

## Boundary

```text
STAGE14_S6_05=COMPLETE_COMPACT_TORSION_NORMALIZATION_AND_PHYSICAL_CLASS_REDUCTION
MERGED_4BJ_LEAST_DENOMINATOR_GATE_IMPORTED=true
PHYSICAL_POINT_REAL_COMPONENT=Z_GT_S2
T0_TRANSLATION_FORMULA_EXACT=true
PHYSICAL_TORSION_TRANSLATE_COMPACT=true
COMPACT_TRANSLATE_NONZERO_MOD_2=true
MAXIMAL_HALVING_REQUIRED_FOR_PHYSICAL_MAJORANT=false
TORSION_TRANSLATION_PRESERVES_HEIGHT_WINDOW=true
TORSION_TRANSLATION_PRESERVES_PHYSICAL_RECONSTRUCTION=true
PHYSICAL_COMPACT_TAU_PACKET_COUNT=4
PHYSICAL_COMPACT_COVER_POSITIVE_DEFINITE=true
PHYSICAL_COMPACT_COORDINATE_BOUND_U_LE_BD=true
NONCOMPACT_PELL_CHAMBER_REQUIRED_FOR_PHYSICAL_MAJORANT=false
TORSION_TRANSLATE_DENOMINATOR_INVOLUTION_EXACT=true
LEAST_DENOMINATOR_STATISTIC_RETAINED=true
LEAST_DENOMINATOR_PRIMARY_PHYSICAL_SELECTOR=false
TORSION_NORMALIZED_PHYSICAL_DENOMINATOR_PRIMARY=true
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21
NEXT=Stage14-s6-06
```
