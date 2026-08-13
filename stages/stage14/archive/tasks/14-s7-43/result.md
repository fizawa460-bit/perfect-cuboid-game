# Stage14-s7-43 — matched common-core square compression and zero-root-gcd square-root saturation

## Status

`COMPLETE_MATCHED_COMMON_CORE_SQUARE_COMPRESSION_AND_ZERO_ROOT_GCD_SQRT_SATURATION`

Stage14-s7-43 consumes latest merged `Stage14-s7-42`, merged `Stage14-4da`, merged `Stage14-X13`, and the common-core/root-line infrastructure of merged `s7-29`, `4cx`, and `4cz`.

The entering canonical theorem is already

```text
V(B) << B^(1/2+o(1)).
```

from merged X13.  Stage14-s7-43 does **not** claim a strict sub-square-root whole-family exponent.  Its new result is a stronger saturation contraction.

Merged 4da proves that every possible square-root-saturating packet must lie in the matched stratum

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
H=B^(s+o(1)),
0<=s<=phi-5/24,
J=B^(j+o(1)),
j=chi-2s,
K=B^o(1),
H^2/D0=B^o(1),
D0=B^(chi-j+o(1)).
```

Stage14-s7-43 changes the quantifier order for the **common-core choice only**.  On the matched stratum, `C/J` is a square `H^2` up to `B^o(1)` factors.  Thus instead of charging all `B^(chi+o(1))` possible common cores `C`, one may first choose `(J,H)` and reconstruct `C` with `B^o(1)` multiplicity.  This reduces the common-core support from `chi` to `j+s=chi-s`.

The X13 primitive-pair and single-column costs are unchanged, so the matched fixed-`s` complete count becomes

```text
E_match(s) <= 1/2-s.
```

Consequently every positive fixed-power cross-root gcd stratum is strictly sub-square-root.  Any remaining square-root saturation must satisfy

```text
s=0,
H=B^o(1),
j=chi,
C/J=B^o(1).
```

Together with merged s7-42/4da `K=B^o(1)`, all four cross-state odd root-gcd cells are subpolynomial and the full common core, joint core, and Cayley-good core coincide at fixed-power scale.

---

## 1. Imported X13 / s7-42 / 4da square-root data

Merged X13 gives

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Its possible equality band is

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
0<=s<=phi-5/24.                                   (1.1)
```

On this band the common-core plus primitive-pair base and the reduced single-column support are

```text
common core C:                    chi,
primitive xi-agreement pair:      2phi-chi=1/4,
reduced single column:             a_col=1/4-chi=1/2-2phi,
post-column reciprocal completion: B^o(1).        (1.2)
```

Hence

```text
chi+(2phi-chi)+a_col=1/2.                         (1.3)
```

Merged s7-42 proves that the same-side root gcd

```text
K=K_x*K_y
```

satisfies, for `K=B^(kappa+o(1))`,

```text
E_K<=1/2-kappa.
```

Merged 4da further introduces

```text
D=C/J,
D0=D/gcd(D,Omega_0),
Omega_0=B^o(1),
G=H^2/D0=B^(e+o(1)),                               (1.4)
```

and proves

```text
E_4da(kappa,e)<=1/2-kappa-e/2.                    (1.5)
```

Therefore any square-root-saturating sequence must already satisfy

```text
boxed:
kappa=0,
e=0.                                             (1.6)
```

Equivalently,

```text
K=B^o(1),
G=H^2/D0=B^o(1),
D0=H^2*B^o(1),
j=chi-2s.                                         (1.7)
```

Stage14-s7-43 works only on this remaining matched stratum.

---

## 2. Exact reconstruction of `C/J` from `H`

From merged 4da / 4cx,

```text
D0=D/gcd(D,Omega_0),
D=C/J,
Omega_0=B^o(1).                                    (2.1)
```

Set

```text
Omega_1:=gcd(D,Omega_0).
```

Then

```text
Omega_1=B^o(1),
D=D0*Omega_1.                                      (2.2)
```

On the matched stratum `e=0`,

```text
G=H^2/D0=B^o(1),
```

so exactly

```text
D0=H^2/G.                                          (2.3)
```

Therefore

```text
boxed:
C/J=D=H^2*Omega_1/G.                              (2.4)
```

Here `G|H^2`, and both `G` and `Omega_1` have only subpolynomial range on an equality sequence.  For fixed `H`, the number of possible pairs `(G,Omega_1)` is `B^o(1)`; divisibility/integrality only removes candidates.

Hence

```text
boxed:
fixed (J,H) => #C = B^o(1)                       (2.5)
```

on the matched square-root stratum.

This is not an assertion that `C=JH^2` literally at all small primes.  It is the exact `D0/G/Omega_1` reconstruction with only `B^o(1)` ambiguity.

---

## 3. Common-core support compresses by one copy of `H`

Write

```text
H=B^(s+o(1)),
J=B^(j+o(1)).
```

The number of possible integers in the dyadic `J` range is at most

```text
B^(j+o(1)),
```

and the number of possible `H` is at most

```text
B^(s+o(1)).
```

By (2.5), after `(J,H)` are fixed the common core `C` has only `B^o(1)` possibilities.  Thus the old direct common-core charge

```text
B^(chi+o(1))
```

may be replaced on the matched stratum by

```text
boxed:
#(J,H,C) <= B^(j+s+o(1)).                         (3.1)
```

Merged 4da gives

```text
j=chi-2s,
```

so

```text
boxed:
j+s=chi-s.                                       (3.2)
```

Therefore the matched square structure saves exactly one copy of the cross-root exponent `s` in the common-core enumeration.

No modulus is multiplied as an independent spacing gain.  The full reconstructed `C` is still the single modulus used by the primitive common-core root-line count.

```text
COMMON_CORE_AND_JH_DOUBLE_CHARGED=false.           (3.3)
```

---

## 4. Primitive root-line cost is unchanged

Merged s7-29 proves, after the quotient/small decoration is conditioned, that the primitive xi-agreement pair `(U,V)` lies on `B^o(1)` Gaussian root lines modulo the full common core `C`, with

```text
#(U,V)<=B^(2phi-chi+o(1)).                         (4.1)
```

On `theta=1/4`,

```text
boxed:
2phi-chi=1/4.                                      (4.2)
```

The new enumeration order is

```text
J,H
-> B^o(1) choices of C
-> primitive (U,V) on the same full-C root line.
```

Thus (4.1) is used once and unchanged.  The matched-square compression is a reduction in the **choice of C**, not a second root-line spacing argument.

```text
COMMON_CORE_ROOT_LINE_REUSED_IN_REVERSE=false.    (4.3)
```

---

## 5. Single-column cost and X13 reverse completion are unchanged

Merged X13 and 4da give, after the lost-core/cross-root factors are removed,

```text
R_col <= B^(a_col+o(1)),
a_col=1/2-2phi.                                    (5.1)
```

On the matched stratum `K=B^o(1)` and `G=B^o(1)`, no remaining fixed-power forced divisor is being charged inside `R_col`.  We therefore retain the safe ambient support

```text
boxed:
E_col<=a_col.                                      (5.2)
```

After the column reconstructs `(z1,z2)` and `M`, merged X13 gives

```text
fixed (U,V,M)
=> #(a,b,c,d,p,q,N)=B^o(1).                        (5.3)
```

Hence no row CRT lift or first-residual support is added independently.

---

## 6. Matched fixed-`s` complete count

Combine Sections 3--5 in the legal order

```text
J,H
-> C
-> primitive (U,V)
-> reduced single column
-> M
-> X13 reverse reciprocal completion.
```

The fixed-power costs are

```text
J,H,C support:                 j+s = chi-s,
primitive (U,V):               2phi-chi,
reduced single column:         1/2-2phi,
post-column completion:        0.
```

Therefore

```text
E_match(s)
 <=(chi-s)+(2phi-chi)+(1/2-2phi)
 =1/2-s.                                             (6.1)
```

Thus

```text
boxed:
E_match(s)<=1/2-s.                                  (6.2)
```

Every matched fixed-power stratum with

```text
s>0
```

is strictly sub-square-root.

Together with 4da (1.5), all square-root-band strata satisfy a strict saving whenever at least one of

```text
kappa,
e,
s
```

is positive at fixed-power scale.

---

## 7. Square-root saturation forces all cross-state root gcds to be subpolynomial

For equality at `1/2`, Sections 1 and 6 force

```text
boxed:
kappa=e=s=0.                                        (7.1)
```

Hence

```text
boxed:
K=B^o(1),
H=B^o(1).                                           (7.2)
```

Recall

```text
K=K_x*K_y,
H=H_S*H_T,
```

with the four odd cross-state gcd cells pairwise coprime and positive.  Therefore each cell is separately subpolynomial:

```text
boxed:
K_x=K_y=H_S=H_T=B^o(1).                            (7.3)
```

Together with the statewise exact reducedness

```text
gcd(x1,y1)=gcd(x2,y2)=1,
```

the four-root tuple is globally odd-primitive up to `B^o(1)` pairwise gcds.

```text
SQRT_SATURATION_GLOBALLY_ODD_PRIMITIVE=true.        (7.4)
```

---

## 8. Lost core and Cayley annulus disappear at fixed-power scale

Since `s=0`, merged 4da gives

```text
j=chi,
D0=B^o(1).                                          (8.1)
```

Equation (2.4) then gives

```text
C/J=B^o(1).                                         (8.2)
```

Merged 4cx proves the Cayley-only annulus is endpoint-small:

```text
C_Cayley/J=B^o(1).                                  (8.3)
```

Consequently every square-root-saturating sequence satisfies

```text
boxed:
J=C_Cayley=C * B^o(1)^{-1}                         (8.4)
```

at fixed-power scale.  In exponent notation,

```text
boxed:
j=c_C=chi.                                         (8.5)
```

Thus neither a fixed-power lost core nor a fixed-power Cayley-only annulus survives.

---

## 9. Current saturation band and new receiver

The current whole-family theorem remains

```text
boxed:
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.           (9.1)
```

The possible equality band has now contracted to

```text
boxed:
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
H=K=B^o(1),
J=C_Cayley=C*B^o(1)^{-1},
column support<=B^(1/2-2phi+o(1)),
post-column reciprocal completion=B^o(1).           (9.2)
```

The residual single-column coordinate is still power-equivalent to the first residual by merged s7-42 and is not charged twice.

Define the new minimal receiver

```text
boxed:
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreDualPrimitiveRootLineIncidence.
```

There are now two visible primitive root-line objects sharing essentially the full same common core:

1. the primitive xi-agreement pair `(U,V)`, product scale `B^(2phi)`, on the Gaussian root line modulo `C`;
2. the globally odd-primitive endpoint-linear pair `(z1,z2)` after endpoint-small normalization, whose single-column support has exponent `1/4-chi` and whose modulus is `J=C*B^o(1)`.

The remaining question is whether these two primitive lifts can saturate independently once the exact reciprocal equations and common orientation data are imposed.

---

## 10. Why no new H/tH is requested

No auxiliary H theorem is needed at s7-43.

The receiver has become **more exact and more primitive**:

```text
H=K=B^o(1),
C/J=B^o(1),
C_Cayley/J=B^o(1).
```

The next unused structure is the shared full-core modulus and the relation between two primitive root-line lifts.  Before invoking an incidence/dispersion theorem, one should first test the exact determinant/resultant obtained from the two line equations and the reciprocal reconstruction.

Therefore

```text
S7_43_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
TH23_CROSS_PROMOTED_TO_S7_43=false.
```

If the dual primitive root-line determinant remains genuinely two-dimensional after exact elimination, formulate a new s-specific H only for that final receiver.

---

## 11. Next

`Stage14-s7-44` should work only on

```text
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreDualPrimitiveRootLineIncidence
```

and derive the exact relation between the primitive common-core slope `(U:V)` and the normalized endpoint-linear slope `(z1:z2)` modulo the now-full common core `C`.

The first target is to determine whether the two determinants share a forced nonzero multiple of `C^2` (or an equivalent resultant constraint) without double-using the same modulus.  Any fixed saving on the remaining `theta=1/4` band would give a strict sub-square-root whole-family theorem.

---

## Stage boundary

```text
STAGE14_S7_43=COMPLETE_MATCHED_COMMON_CORE_SQUARE_COMPRESSION_AND_ZERO_ROOT_GCD_SQRT_SATURATION
MERGED_S7_42_IMPORTED=true
MERGED_4DA_IMPORTED=true
MERGED_X13_IMPORTED=true
MERGED_S7_29_ROOT_LINE_IMPORTED=true
MERGED_4CX_IMPORTED=true
MERGED_4CZ_IMPORTED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
FOURDA_SATURATION_KAPPA_ZERO_IMPORTED=true
FOURDA_SATURATION_EXCESS_E_ZERO_IMPORTED=true
MATCHED_STRATUM_C_OVER_J_RECONSTRUCTED_FROM_H=Bo1
FIXED_J_H_TO_COMMON_CORE_MULTIPLICITY=Bo1
MATCHED_COMMON_CORE_SUPPORT_EXPONENT=chi-s
MATCHED_FIXED_S_BLOCK_EXPONENT=1/2-s
SQRT_SATURATION_CROSS_ROOT_EXPONENT=0
SQRT_SATURATION_SAMESIDE_ROOT_GCD_EXPONENT=0
SQRT_SATURATION_GLOBALLY_ODD_PRIMITIVE=true
SQRT_SATURATION_JOINT_CORE_EXPONENT=chi
SQRT_SATURATION_CAYLEY_CORE_EXPONENT=chi
SQRT_SATURATION_COMMON_CORE_EXPONENT=chi
SQRT_SATURATION_LOST_CORE_EXPONENT=0
SQRT_SATURATION_CAYLEY_ANNULUS_EXPONENT=0
COMMON_CORE_AND_JH_DOUBLE_CHARGED=false
COMMON_CORE_ROOT_LINE_REUSED_IN_REVERSE=false
S7_43_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
TH23_CROSS_PROMOTED_TO_S7_43=false
REMAINING_RECEIVER=SquareRootThetaQuarterGloballyOddPrimitiveFullCoreDualPrimitiveRootLineIncidence
NEXT=Stage14-s7-44
```
