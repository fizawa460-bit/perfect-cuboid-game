# Stage14-t63 — consume tH17 and isolate the exact transverse vertical Kummer defect

## Purpose

Merged Stage14-t62 compressed one t59 orthogonal-rectangle family to matched block averages and proposed the stronger sufficient theorem `MatchedRectangleProjectedKummerDualLargeSieve`.

Merged Stage14-tH17 independently proved the signed vertical TT* identity

\[
\sum_{p,q}|T_{pq}|^2=\|V\|_{S_4}^4
=\sum_{s,t}\left|\sum_r K_r(s)K_r(t)\right|^2,
\]

and showed that generic duality, one-prime Bessel, t59 geometry alone, Ping Xi, and FKMS do not supply the missing vertical arithmetic estimate.

Stage14-t63 consumes tH17 and removes two theorem contracts that are stronger than the original fixed-`U` problem:

1. full vertical Schatten-4, which contains diagonal, same-`pi`, and same-`V` correlations already separated at tH15;
2. the arbitrary matched-block dual large sieve from t62, which is sufficient but not minimal for the unit-weight physical receiver.

The correct object is the exact **transverse Schatten defect**, and it is identical to the transverse Frobenius energy already isolated in merged tH15.

No new global Stage14 power saving is claimed.

---

## 1. Fixed-U packet and vertical Gram

Fix one legal tH15 packet: primitive `U`, finite `epsilon`, divisor-fan `k,h`, and branch/orientation. Retain moving canonical prime `pi`, primitive `V`, `delta`, the chamber, sharp hyperbola, reconstruction masks and canonical selector.

Let the full physical state set be `S_U`. The t59 rectangle families are an exact disjoint construction of this selector; after constructing the set there is no reason to Cauchy-sum those families before forming the vertical Gram.

For the common good split auxiliary-prime family `Pcal`, define

\[
V_U(r,s)=K_r(s)=\chi_r(\widetilde F_s),
\qquad
G_U(s,t)=\sum_{r\in\mathcal P}K_r(s)K_r(t).
\tag{63.1}
\]

Merged tH17 gives

\[
\|V_U\|_{S_4}^4
=\sum_{s,t\in S_U}|G_U(s,t)|^2.
\tag{63.2}
\]

No polar absolute value occurs.

---

## 2. Exact row/column/transverse vertical inclusion-exclusion

For fixed `pi` let `S_{U,pi}` be its incident states, and for fixed `V` let `S_{U,V}` be its incident states. For any state subset `A`, put

\[
\mathcal Q(A)=\sum_{s,t\in A}|G_U(s,t)|^2.
\tag{63.3}
\]

Define

\[
\boxed{
\mathcal D_U^{\rm tr}
=\mathcal Q(S_U)
-\sum_\pi\mathcal Q(S_{U,\pi})
-\sum_V\mathcal Q(S_{U,V})
+\sum_{s\in S_U}|G_U(s,s)|^2.
}
\tag{63.4}
\]

For one ordered pair `(s,t)`, its coefficient is

```text
1 - 1_{pi_s=pi_t} - 1_{V_s=V_t} + 1_{s=t}.
```

Since a physical state is one bipartite edge, this coefficient is exactly zero on the diagonal, zero on same-`pi` distinct pairs, zero on same-`V` distinct pairs, and one precisely when both endpoints move. Hence

\[
\boxed{
\mathcal D_U^{\rm tr}
=\sum_{\substack{s,t\in S_U\\
\pi_s\ne\pi_t\\V_s\ne V_t}}
|G_U(s,t)|^2
\ge0.
}
\tag{63.5}
\]

Expanding `G_U` and interchanging sums gives exactly merged tH15 equation H15.18:

\[
\boxed{\mathcal D_U^{\rm tr}=\mathfrak F_U^{\rm tr}.}
\tag{63.6}
\]

Thus the tH17 vertical TT* road and the tH15 Frobenius road meet at the same object once the already-solved row/column slices are removed.

```text
VERTICAL_TRANSVERSE_DEFECT_IDENTITY_PROVED=true
T63_TRANSVERSE_DEFECT_EQUALS_TH15_FROBENIUS=true
```

---

## 3. Full vertical Schatten-4 is stronger than necessary

The full norm `Q(S_U)` includes exact diagonal, every same-`pi` vertical correlation, and every same-`V` vertical correlation, principal and nonprincipal. The fixed-`U` principal problem no longer needs those sectors: merged tH15 already routed same-`pi` principal energy to t36 and same-`V` principal energy to t38.

Therefore requiring full ORVKS4 imposes extra nonprincipal row/column fourth-moment work that is irrelevant to the remaining principal collision theorem.

```text
FULL_VERTICAL_SCHATTEN4_REQUIRED=false
ORTHOGONAL_RECTANGLE_VERTICAL_KUMMER_SCHATTEN4_IS_STRONGER_THAN_MINIMAL=true
```

---

## 4. Principal transverse amplification inside the defect

Let

\[
b_s=\#\{r\in\mathcal P:r\mid\widetilde F_s\},
\qquad b=\max_s b_s.
\]

If two transverse states have the same rational squareclass, then on every common good auxiliary prime

\[
K_r(s)K_r(t)=1.
\]

Thus

\[
|G_U(s,t)|\ge P-2b,
\]

and if `I_U^tr` is the ordered transverse equal-squareclass count,

\[
\boxed{I_U^{\rm tr}(P-2b)^2\le\mathcal D_U^{\rm tr}.}
\tag{63.7}
\]

This is tH15 H15.19 in vertical-Gram language.

Consequently the sufficient target is

\[
\boxed{\mathcal D_U^{\rm tr}\ll P^2R_U B^{o(1)}.}
\tag{63.8}
\]

Together with tH15/t36/t38,

\[
E_U=R_U+I_U^{(\pi)}+I_U^{(V)}+I_U^{\rm tr}
\ll R_U B^{o(1)}.
\tag{63.9}
\]

No `E4` coefficient energy appears.

---

## 5. Exact no-go: vertical Bessel already contains squareclass fiber control

Let one squareclass `kappa` occur `h_kappa` times in a common-good-prime set. The corresponding vertical columns are identical. On the normalized all-ones vector on that class, the Gram Rayleigh quotient is at least

\[
(P-2b)h_\kappa.
\]

Hence

\[
\boxed{\|V_U\|_{op}^2\ge(P-2b)\max_\kappa h_\kappa.}
\tag{63.10}
\]

Therefore a generic Bessel estimate `||V_U||op^2 << P B^o(1)` already forces `max h_kappa <= B^o(1)`.

Likewise the full vertical fourth moment contains the positive principal contribution

\[
\boxed{
\|V_U\|_{S_4}^4
\ge(P-2b)^2\sum_\kappa h_\kappa^2.
}
\tag{63.11}
\]

So generic Bessel or full S4 are not free functional-analysis inputs; both already encode strong squareclass decorrelation.

```text
VERTICAL_BESSEL_ALREADY_REQUIRES_MAX_SQUARECLASS_FIBER_CONTROL=true
FULL_VERTICAL_S4_ALREADY_CONTAINS_SQUARECLASS_ENERGY=true
GENERIC_DUALITY_IS_NOT_NEW_ARITHMETIC_INPUT=true
```

---

## 6. Status of the t62 matched projection

Merged t62's block-average Bessel projection remains exact and zero-loss. Its proposed `MatchedRectangleProjectedKummerDualLargeSieve` also remains a valid sufficient theorem.

However it allows arbitrary auxiliary coefficients and simultaneously controls every matched rectangle coordinate. The physical Stage14 application needs only the unit-weight fixed-`U` selector and, after tH15 subtraction, only transverse pair-space energy.

Therefore the projected dual large sieve is no longer the minimal target.

```text
MATCHED_RECTANGLE_PROJECTED_KUMMER_DUAL_LARGE_SIEVE_STILL_SUFFICIENT=true
MATCHED_RECTANGLE_PROJECTED_KUMMER_DUAL_LARGE_SIEVE_REQUIRED=false
T62_MATCHED_BLOCK_PROJECTION_RETAINED=true
```

The t59/t62 roadworks remain useful for exact selector construction, avoiding ambient Cartesian enlargement and avoiding rectangle-count loss.

---

## 7. Frozen exact audit

The deterministic audit rebuilds the 560 reciprocal states and 419 invisible states, groups the latter into the eight fixed `(U,epsilon,k)` packets, and chooses split auxiliary primes that divide none of the frozen `F` values.

For every packet it verifies:

1. `full S4 - sum row S4 - sum column S4 + singleton diagonal` equals the direct ordered transverse pair sum;
2. total squareclass energy decomposes exactly as `R + same-row-principal + same-column-principal + transverse-principal`;
3. every equal-squareclass pair has Gram value exactly `P` on the common-good finite set;
4. full S4 is at least `P^2 * total squareclass energy`;
5. transverse defect is at least `P^2 * transverse principal energy`;
6. a coherent class of size `h` gives Rayleigh quotient `P*h`.

These are finite identity checks; the asymptotic proof is (63.4)--(63.11).

---

## 8. Current minimal theorem

The live object is

```text
SharedUTransverseVerticalKummerDispersion
```

which is exactly merged tH15

```text
SharedUPhysicalBipartiteDispersion (SUBD).
```

Prove uniformly

\[
\boxed{
\sum_{\substack{s,t\\\pi_s\ne\pi_t\\V_s\ne V_t}}
\left|\sum_{r\in\mathcal P}K_r(s)K_r(t)\right|^2
\ll P^2R_U B^{o(1)}.
}
\tag{63.12}
\]

The remaining difficulty is arithmetic/geometric decorrelation of the transverse `(pi,V)` projective trace, not another functional-analytic wrapper.

---

## 9. tH decision

`tH17` is consumed at t63. No `tH18` is needed yet: this stage introduces no new external theorem family, only exact TT*/inclusion-exclusion reconciliation and removal of stronger-than-needed contracts.

Stage14-t64 should return to the explicit tH15 projective formulas `P_U^inv`, `P_U^vis,+`, `P_U^vis,-` and attack transverse equal-squareclass/vertical dispersion directly. If that exposes a genuinely new K3/incidence/Chebotarev theorem whose applicability is uncertain, that is the trigger for tH18.

```text
TH17_CONSUMED=true
TH18_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
```

---

## Locked boundary

```text
STAGE14_T63=COMPLETE_TH17_CONSUMPTION_AND_TRANSVERSE_VERTICAL_DEFECT_REDUCTION
MERGED_T62_IMPORTED=true
MERGED_TH17_IMPORTED=true
VERTICAL_TTSTAR_IDENTITY_IMPORTED=true
VERTICAL_TRANSVERSE_DEFECT_IDENTITY_PROVED=true
T63_TRANSVERSE_DEFECT_EQUALS_TH15_FROBENIUS=true
FULL_VERTICAL_SCHATTEN4_REQUIRED=false
ORTHOGONAL_RECTANGLE_VERTICAL_KUMMER_SCHATTEN4_IS_STRONGER_THAN_MINIMAL=true
TRANSVERSE_PRINCIPAL_AMPLIFICATION_PROVED=true
VERTICAL_BESSEL_ALREADY_REQUIRES_MAX_SQUARECLASS_FIBER_CONTROL=true
FULL_VERTICAL_S4_ALREADY_CONTAINS_SQUARECLASS_ENERGY=true
GENERIC_DUALITY_IS_NOT_NEW_ARITHMETIC_INPUT=true
MATCHED_RECTANGLE_PROJECTED_KUMMER_DUAL_LARGE_SIEVE_STILL_SUFFICIENT=true
MATCHED_RECTANGLE_PROJECTED_KUMMER_DUAL_LARGE_SIEVE_REQUIRED=false
T62_MATCHED_BLOCK_PROJECTION_RETAINED=true
SHARED_U_TRANSVERSE_VERTICAL_KUMMER_DISPERSION_PROVED=false
SHARED_U_PHYSICAL_BIPARTITE_DISPERSION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
TH17_CONSUMED=true
TH18_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH=false
NEXT=Stage14-t64 return to the tH15 explicit projective transverse trace and attack equal-squareclass/vertical dispersion directly
```
