# Stage14-s6-05 — compact 2-torsion normalization and physical-class reduction

## Purpose

Stage14-s6-04 isolates a genuine obstruction in the direct post-local route: after the full two-quadrics witness equations are imposed, the centered auxiliary characters are identically positive, while denominator-square incidence remains only a coordinate-density statement. It therefore introduces the least denominator of a bounded-height representative as a possible packet-level statistic.

Before building a new least-denominator distribution theory, Stage14-s6-05 returns to the **exact physical point** of Stage14-s3 and uses the real component structure of

```text
E_{S,X}: W^2 = Z(Z-S^2)(Z+X^2),
S^2+X^2=H^2.
```

The result is stronger than the maximal-halving normalization used in s6-01.

Every physical Stage14 point lies on the identity real component `Z>S^2`. Translating by the rational 2-torsion point

```text
T0=(0,0)
```

moves it explicitly to the compact component

```text
-X^2 < Z < 0.
```

Torsion translation preserves canonical height and non-torsion. A compact-component point cannot lie in `2E(R)`, hence cannot lie in `2E(Q)`. Therefore the translated point automatically represents a **nonzero** Kummer class. No repeated global halving is needed.

Consequences:

1. every physical hit has a bounded-height globally soluble nonzero 2-cover representative on the compact real component;
2. the sixteen sign/2-adic packets of s6-01 reduce, for the physical upper majorant, to exactly four `(--+)` packets;
3. the resulting two-quadrics system is positive definite in the `H`-edge and gives sharp relative coordinate bounds `|u_i| << B D`;
4. the torsion translation has an exact denominator involution, tying the compact witness denominator directly to the numerator of the original physical `Z` coordinate;
5. the least-denominator statistic of s6-04 remains valid, but maximal halving / arbitrary least-denominator selection is no longer necessary to obtain a nonzero physical majorant class.

This stage does **not** yet prove a positive post-local exponent. It removes the noncompact simultaneous-Pell chamber from the physical majorant and restores an exact invertible link to the physical point, so the next counting stage can retain physical reconstruction instead of counting arbitrary globally soluble cover points.

No new external theorem is used.

---

## 1. The physical s3 point is always on `Z>S^2`

Stage14-s3 writes the exact physical point using

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

For a positive physical Pythagorean face,

```text
0<q<1,
z>0.
```

Since `rho^2+s^2=1`,

```text
A0 = 1-2*rho^2 = 2*s^2-1.
```

Also

```text
X0=(Yq+1)/q^2 > 1.
```

Hence

```text
x
 = (2*s^2-1+X0)/(2*s^2)
 = 1 + (X0-1)/(2*s^2)
 > 1.
```

Therefore every physical point satisfies

```text
boxed: Z>S^2.
```

Thus the exact physical point lies on the identity/unbounded real component of `E_{S,X}(R)`.

```text
PHYSICAL_POINT_REAL_COMPONENT=Z_GT_S2.
```

---

## 2. Exact translation by the rational 2-torsion point `(0,0)`

Write the curve as

```text
W^2 = Z^3 + a2*Z^2 + a4*Z,
a2 = X^2-S^2,
a4 = -S^2*X^2.
```

Let

```text
P=(Z,W),
T0=(0,0).
```

For `Z!=0`, the chord slope is

```text
lambda = W/Z.
```

The addition law gives

```text
Z(P+T0)
 = lambda^2-a2-Z
 = -S^2*X^2/Z,
```

and

```text
W(P+T0)
 = -W + lambda*(Z-Z(P+T0))
 = S^2*X^2*W/Z^2.
```

Thus the torsion translation is the explicit involution

```text
boxed:
(Z,W)
 ->
(-S^2 X^2/Z, S^2 X^2 W/Z^2).
```

Applying it twice returns `(Z,W)`.

```text
T0_TRANSLATION_FORMULA_EXACT=true.
```

---

## 3. Physical points move to the compact real component

For the physical point, `Z>S^2>0`. Therefore

```text
Z' = -S^2 X^2/Z < 0,
```

and

```text
|Z'| = S^2 X^2/Z < X^2.
```

Hence

```text
boxed: -X^2 < Z' < 0.
```

For the cubic with three real roots

```text
-X^2 < 0 < S^2,
```

the real locus has two components:

```text
identity component: Z>=S^2 together with O,
compact component : -X^2<=Z<=0.
```

So translation by `T0` sends every physical Stage14 point from the identity component to the compact component.

```text
PHYSICAL_TORSION_TRANSLATE_COMPACT=true.
```

---

## 4. The compact translate is automatically nonzero modulo `2E(Q)`

The component group is

```text
E(R)/E(R)^0 ~= Z/2Z.
```

Doubling kills this component group. Consequently

```text
2E(R) subset E(R)^0.
```

A point on the compact/nonidentity component therefore cannot be twice a real point.

Let

```text
Q=P+T0.
```

Since `Q` lies on the compact component,

```text
Q notin 2E(R),
```

and a fortiori

```text
Q notin 2E(Q).
```

Thus its Kummer class in

```text
E(Q)/2E(Q)
```

is automatically nonzero.

This is exactly the property for which s6-01 used maximal repeated halving. For physical upper bounds that halving is unnecessary.

```text
COMPACT_TRANSLATE_NONZERO_MOD_2=true
MAXIMAL_HALVING_REQUIRED_FOR_PHYSICAL_MAJORANT=false.
```

---

## 5. Height and non-torsion are preserved

Merged Stage14 proves every physical point `P` is non-torsion. Translation by the torsion point `T0` preserves non-torsion.

For the Neron--Tate height, torsion has zero canonical height and zero height pairing with every point, so

```text
hhat(P+T0)=hhat(P).
```

Stage14-s3 therefore gives

```text
hhat(Q)=O(log B+log H)=O(log B)
```

on the physical range `H<=B`.

Hence every physical hit produces directly

```text
non-torsion
+ nonzero mod-2 Kummer class
+ global rational representative
+ logarithmic canonical-height window
+ compact real component.
```

No physical reconstruction information is lost: `P=Q+T0` is recovered by the same involution.

```text
TORSION_TRANSLATION_PRESERVES_HEIGHT_WINDOW=true
TORSION_TRANSLATION_PRESERVES_PHYSICAL_RECONSTRUCTION=true.
```

---

## 6. The physical cover sign pattern is forced to `(--+)`

Write the compact translated point in primitive rational coordinates

```text
Z'=A/D^2,
gcd(A,D)=1.
```

The three cleared factors are

```text
G0=A,
G1=A-S^2 D^2,
G2=A+X^2 D^2.
```

Because

```text
-X^2 < Z' < 0,
```

we have exactly

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

In the s6-01 factorization

```text
d0=tau0*a*b,
d1=tau1*a*c,
d2=tau2*b*c,
```

with positive odd squarefree `a,b,c`, the signs are therefore fixed:

```text
tau0<0,
tau1<0,
tau2>0.
```

The admissible 2-adic parity condition says an even number of the three `|tau_i|` equal `2`. Hence the only physical sign/2-adic packets are

```text
(-1,-1, 1),
(-2,-2, 1),
(-2,-1, 2),
(-1,-2, 2).
```

So the physical upper majorant uses exactly four tau packets, not all sixteen abstract real/complex packet states.

```text
PHYSICAL_COMPACT_TAU_PACKET_COUNT=4.
```

---

## 7. Positive-definite compact two-quadrics

Put

```text
e0=|d0|,
e1=|d1|,
e2=d2,
```

so all `e_i>0`.

The s6-01 equations become

```text
e1*u1^2 - e0*u0^2 = S^2*D^2,          (S)
e2*u2^2 + e0*u0^2 = X^2*D^2,          (X)
e2*u2^2 + e1*u1^2 = H^2*D^2.          (H)
```

The `X`- and `H`-edge equations are positive definite.

They immediately imply

```text
sqrt(e0)*|u0| <= X*D,
sqrt(e2)*|u2| <= X*D,
sqrt(e1)*|u1| <= H*D.
```

Since `X,H<=B` on the physical range,

```text
boxed:
|u0|,|u1|,|u2| <= B*D.
```

More precisely the squarefree coefficients improve these bounds by their square roots.

Thus the noncompact `+++` simultaneous-Pell geometry which exists for arbitrary globally soluble packet representatives is **not needed** for the physical upper majorant.

```text
PHYSICAL_COMPACT_COVER_POSITIVE_DEFINITE=true
PHYSICAL_COMPACT_COORDINATE_BOUND_U_LE_BD=true
NONCOMPACT_PELL_CHAMBER_REQUIRED_FOR_PHYSICAL_MAJORANT=false.
```

---

## 8. Why the abstract `+++` chamber was genuinely dangerous

For comparison, if all `d_i>0`, fixing `D` and allowing real `u1=t` gives

```text
u0^2=(d1*t^2+S^2*D^2)/d0,
u2^2=(d1*t^2+H^2*D^2)/d2.
```

As a real curve this runs to infinity with `t`; there is no archimedean inequality of the form

```text
|u_i| << B^C D
```

coming merely from the two difference equations with a small fixed exponent `C` independent of the chosen height theorem.

The compact torsion normalization eliminates this real escape **before** any counting theorem is applied.

This does not assert that the integral points of one fixed `+++` genus-one curve are infinite; it only records that denominator minimality alone had no elementary archimedean control in that chamber.

---

## 9. Exact denominator involution under torsion translation

Write the original physical point as

```text
Z_P=A_P/D_P^2,
gcd(A_P,D_P)=1,
A_P>0.
```

Then

```text
Z_Q
 = -S^2 X^2 D_P^2/A_P.
```

Let

```text
g = gcd(A_P,S^2 X^2).
```

Because `gcd(A_P,D_P)=1`, reduction of this fraction removes exactly `g`, so the reduced denominator of `Z_Q` is

```text
A_P/g.
```

On the monic integral Weierstrass model, s6-01 proves that a reduced rational `Z` coordinate has square denominator. Therefore

```text
boxed:
D_Q^2 = A_P / gcd(A_P,S^2 X^2).
```

The reduced numerator is

```text
A_Q = -S^2 X^2 D_P^2/g.
```

Since translation by `T0` is an involution, the reverse relation has the same form.

Thus the compact-cover denominator is not an arbitrary new variable: it is an exact arithmetic transform of the numerator of the physical point.

```text
TORSION_TRANSLATE_DENOMINATOR_INVOLUTION_EXACT=true.
```

This is the key new receiver for Stage14-s6-06.

---

## 10. Status of the s6-04 least-denominator statistic

The least-denominator statistic

```text
D_min(F,sigma;B)
```

introduced in s6-04 remains mathematically valid for an arbitrary globally soluble packet.

However, for the **physical upper majorant**, it is no longer necessary to:

1. repeatedly halve the physical point until a nonzero class is found;
2. forget the physical reconstruction;
3. choose an arbitrary least-denominator representative of that abstract class.

Instead one may choose the exact torsion-normalized point

```text
Q=P_phys+(0,0),
```

which is already compact, non-torsion, nonzero modulo `2`, and in the same logarithmic height window.

Define its denominator by

```text
D_T(P_phys)=D_Q.
```

Then for the Kummer packet of `Q`,

```text
D_min <= D_T,
```

but the physically meaningful selector `D_T` retains the exact inverse map back to the physical point.

Accordingly,

```text
LEAST_DENOMINATOR_STATISTIC_RETAINED=true
LEAST_DENOMINATOR_PRIMARY_PHYSICAL_SELECTOR=false
TORSION_NORMALIZED_PHYSICAL_DENOMINATOR_PRIMARY=true.
```

---

## 11. What this fixes and what remains open

Stage14-s6-05 fixes three structural losses from the earlier direct route.

### Fixed A — repeated halving

The physical point can be sent directly to a nonzero Kummer class by rational 2-torsion translation.

### Fixed B — noncompact cover geometry

The selected physical class always lies in the compact `(--+)` chamber, where the cover equations are positive definite and `|u_i|<=BD`.

### Fixed C — loss of physical reconstruction

Torsion translation is an explicit involution, so the translated witness still remembers the original physical point exactly.

What remains open is quantitative:

- the denominator `D_T` is only polynomially bounded by the existing height comparison;
- denominator-square / full-radical congruence sparsity is still a coordinate statement unless the physical reconstruction variables are counted jointly;
- exact-witness auxiliary characters still resonate and cannot be used after the square condition is imposed;
- no full packet/base saving `delta_post>0` follows from compactness alone.

Thus

```text
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false.
```

---

## 12. Next quantitative target

Stage14-s6-06 should now work with the **physical torsion-normalized witness**, not an arbitrary globally soluble class.

Insert

```text
Z_Q=-S^2 X^2/Z_P
```

into the exact Stage14-s3 physical formulas for `Z_P`. The goal is to express

```text
D_T^2=A_P/gcd(A_P,S^2X^2)
```

in the primitive second-face / space-diagonal variables and recover any additional divisibility, norm, or scale constraint that was lost by the s6-01 upper-majorant relaxation.

This is also the natural place to compare with the merged `t32`/open `t33` physical norm skeleton, but no result from that separate route is imported unless the variables are identified exactly.

If the physical numerator/denominator involution yields a thin global incidence, it can finally attack the existence count rather than coordinate density inside an arbitrary packet.

---

## Boundary

```text
STAGE14_S6_05=COMPLETE_COMPACT_TORSION_NORMALIZATION_AND_PHYSICAL_CLASS_REDUCTION
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
