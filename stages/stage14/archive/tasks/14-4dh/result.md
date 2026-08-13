# Stage14-4dh — same-root synchronization and Ramanujan conductor spacing boundary

## Status

`COMPLETE_SAME_ROOT_PYTHAGOREAN_SYNCHRONIZATION_RAMANUJAN_CONDUCTOR_RECOMBINATION_AND_ABSOLUTE_SQRT_BOUNDARY`

Stage14-4dh consumes merged

```text
Stage14-4dg,
Stage14-s7-49,
Stage14-X15,
```

on latest main.

The entering whole-family theorem is

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

No new whole-family exponent is claimed here.  The purpose is to close two internal ambiguities left after 4dg/s7-49/X15:

1. whether the X15 third projection provides a second independent local root density;
2. whether the exact-conductor loss in s7-49 can enlarge or automatically improve the square-root ledger.

Both questions are settled exactly.

---

## 1. Imported primitive quarter-pair packet

Use the merged s7-49 rotated variables

```text
m=D+A,
n=D-A,
```

with

```text
m,n=B^(1/4+o(1)),
gcd(m,n)=B^o(1).
```

Let

```text
C:=C_*=B^(chi+o(1)),
1/6<=chi<=1/4,
P_-=m*n=epsilon_- u_* R J.
```

Merged 4df/s7-49 gives, after the permitted subpolynomial peel,

```text
gcd(C,m*n)=1.
```

Let

```text
R_-(C)={rho mod C: rho^2=-1 mod C}.
```

For every physical norm root line there is a unique root label

```text
rho == m*n^(-1) (mod C),
```

and

```text
m == rho*n (mod C).                                (1.1)
```

Merged X15 supplies the third Pythagorean projection

```text
X_-:=m*n=D^2-A^2,
X_0:=2D*A=(m^2-n^2)/2,                             (1.2)
```

with the eight atomic physical blocks pairwise separated at fixed-power scale.

---

## 2. The X15 third projection carries the same Gaussian root label

Reduce (1.2) modulo `C` on the root line (1.1).  Because `2`, `n`, and `rho` are units modulo the odd modulus `C`,

```text
X_-
 == rho*n^2                                          (mod C),

X_0
 == (rho^2-1)n^2/2
 == -n^2                                             (mod C).
```

Since

```text
rho^2=-1 (mod C)
=> rho^(-1)=-rho (mod C),
```

we obtain

```text
boxed:
X_0*X_-^(-1) == rho (mod C),                        (2.1)
```

or equivalently

```text
boxed:
X_0 == rho*X_- (mod C).                             (2.2)
```

Thus the norm root line and the Pythagorean-side root line have the **same root label**.

A useful exact congruence identity is

```text
(m-rho*n)^2
 - 2*(X_0-rho*X_-)
 = (rho^2+1)*n^2.                                  (2.3)
```

Because `C|(rho^2+1)`, every divisor `d|C` satisfies

```text
d | (m-rho*n)
=> d | (X_0-rho*X_-).                              (2.4)
```

The reverse implication is not asserted for arbitrary prime powers; no illegal square-modulus lifting is used.

Consequences:

```text
X15_THIRD_PROJECTION_SAME_GAUSSIAN_ROOT_LABEL=true
THIRD_PROJECTION_INDEPENDENT_LOCAL_ROOT_DENSITY=false
NORM_AND_PYTHAGOREAN_ROOT_DENSITIES_MULTIPLICABLE=false
NO_SECOND_LOCAL_1_OVER_C_FACTOR_FROM_X15=true.
```

This closes a possible but invalid route to a spurious extra factor `C^{-1}`.

---

## 3. Recombine s7-49 exact conductors into Ramanujan sums

Merged s7-49 writes each Gaussian root line as

```text
1_{C|m-rho*n}
 = (1/C) * sum_{h mod C} e_C(h(m-rho*n)).           (3.1)
```

and stratifies nonzero `h` by exact conductor

```text
q=C/gcd(h,C).
```

Instead of bounding the primitive frequencies separately, first sum all frequencies of the same exact conductor.

For

```text
x_rho:=m-rho*n,
```

and every divisor `q|C`, the primitive-frequency sum is the Ramanujan sum

```text
c_q(x_rho)
 := sum_{1<=a<=q,(a,q)=1} e_q(a*x_rho).             (3.2)
```

The standard divisor identity, verified directly in the dedicated audit, is

```text
boxed:
sum_{q|C} c_q(x)=C*1_{C|x}.                       (3.3)
```

Hence the exact root-line indicator becomes

```text
boxed:
1_{C|m-rho*n}
 = (1/C) * sum_{q|C} c_q(m-rho*n).                 (3.4)
```

Summing over `rho in R_-(C)` gives the exact norm-divisibility decomposition

```text
boxed:
1_{C|m^2+n^2}
 = (1/C)
   * sum_{rho in R_-(C)}
     sum_{q|C} c_q(m-rho*n).                       (3.5)
```

The root lines are disjoint because `n` is a unit modulo `C`.

The `q=1` term is exactly

```text
r_-(C)/C,
```

so (3.5) recovers the s7-49 principal/nonprincipal split without introducing any new frequency support.

```text
EXACT_CONDUCTOR_RAMANUJAN_RECOMBINATION_PROVED=true
Q_EQUALS_ONE_TERM_IS_LOCAL_PRINCIPAL_DENSITY=true
NONZERO_CONDUCTORS_ARE_SIGNED_RAMANUJAN_CORRECTIONS=true.
```

---

## 4. Ramanujan amplitude is controlled by the discrepancy gcd

For a nonzero conductor divisor `q|C`, define

```text
d:=gcd(q,m-rho*n).                                 (4.1)
```

Ramanujan sums satisfy the elementary bound

```text
boxed:
|c_q(m-rho*n)| <= d.                               (4.2)
```

Once `C` is fixed, both `q` and `d` are divisor choices:

```text
q|C,
d|q.
```

Therefore their multiplicities are

```text
tau(C)^2=B^o(1),                                   (4.3)
```

and no polynomial exponent is charged for the conductor/gcd stratification after the parent modulus is fixed.

The condition in a fixed `d` stratum is the primitive root-line congruence

```text
m == rho*n (mod d).                                (4.4)
```

The reduction of `rho` modulo `d` still satisfies `rho^2=-1 mod d` and is a unit.

---

## 5. Primitive root-line spacing cancels the Ramanujan amplitude exactly

The quarter-pair box has

```text
m,n=B^(1/4+o(1)),
mn=B^(1/2+o(1)).
```

The same primitive determinant/root-line spacing mechanism already used in the merged root-line stages gives, uniformly in every `d|C`,

```text
boxed:
# {(m,n): d|m-rho*n, physical box/masks}
 <= B^o(1)*(1+B^(1/2)/d).                          (5.1)
```

The inherited physical masks only decrease this count, while the divisor-many completion weights contribute `B^o(1)`.

Multiply (5.1) by the absolute Ramanujan amplitude (4.2).  For fixed `(C,q,d,rho)`,

```text
sum_{d-stratum} |c_q(m-rho*n)|
 <= B^o(1) * d*(1+B^(1/2)/d)
 = B^o(1) * (B^(1/2)+d).                           (5.2)
```

The Fourier/Ramanujan coefficient is `1/C`.  Thus the fixed-`C` contribution is

```text
<= B^o(1) * (B^(1/2)/C + d/C).                    (5.3)
```

Now sum the dyadic common-core family

```text
C=B^(chi+o(1)).
```

There are at most

```text
B^(chi+o(1))
```

possible `C` values.  Since `d<=q<=C`, (5.3) gives

```text
boxed:
B^chi * B^(1/2)/B^chi = B^(1/2),                  (5.4)
```

for the main spacing term, while the endpoint term is at most

```text
B^chi * (d/C)
 <= B^(chi+o(1))
 <= B^(1/4+o(1)).                                  (5.5)
```

The root labels, `q`, and `d` cost only `B^o(1)`.

Therefore the entire nonzero-conductor Ramanujan correction obeys the uniform absolute bound

```text
boxed:
NONZERO_RAMANUJAN_ABSOLUTE_CONTRIBUTION
 << B^(1/2+o(1)).                                  (5.6)
```

uniformly for

```text
1/6<=chi<=1/4.
```

This is a deterministic conductor-loss closure at the current square-root scale.

```text
CONDUCTOR_LOSS_HARMLESS_AT_SQRT_SCALE=true
NONZERO_RAMANUJAN_ABSOLUTE_SQRT_BOUND_PROVED=true.
```

---

## 6. Why the same calculation cannot yield a strict power saving

The key feature of (5.2) is exact fixed-power cancellation:

```text
Ramanujan amplitude : d,
root-line spacing   : 1/d.
```

Their product is constant at the leading scale.

Thus a large discrepancy gcd does not automatically save: its larger Ramanujan amplitude exactly compensates for the thinner congruence class.  Small `d` has small amplitude but correspondingly larger support.

Consequently the absolute conductor/gcd peel gives

```text
E_nonzero,absolute <= 1/2,
```

but no uniform

```text
E_nonzero,absolute <= 1/2-delta
```

with fixed `delta>0`.

The merged s7-49 principal term already has

```text
E_principal=1/2.
```

Hence both sides of the exact Ramanujan decomposition are individually capable of the current square-root scale after absolute values are taken.

```text
RAMANUJAN_AMPLITUDE_SPACING_FIXED_POWER_CANCELLATION=true
ABSOLUTE_CONDUCTOR_PEEL_STRICT_SAVING=false
PRINCIPAL_TERM_STRICT_SAVING=false.
```

This is the main theorem boundary of 4dh.

---

## 7. The X15 third projection does not provide another spacing factor

On every `d`-stratum in Section 5,

```text
d | m-rho*n.
```

By (2.4), the same stratum already implies

```text
d | X_0-rho*X_-.                                  (7.1)
```

But this is the image of the **same** root-line condition under the Pythagorean projection, with the same root `rho` and the same modulus `d`.

Therefore one may not multiply the two apparent densities

```text
1/d from m==rho*n,
1/d from X_0==rho*X_-.
```

They are not independent congruences.

```text
RAMANUJAN_D_STRATUM_AND_X15_ROOTLINE_SAME_EVENT=true
SECOND_1_OVER_D_SPACING_FACTOR_ALLOWED=false
X15_THIRD_PROJECTION_DOES_NOT_BREAK_AMPLITUDE_SPACING_CANCELLATION=true.
```

This is the conductor-level form of the charged-once rule proved in Section 2.

---

## 8. Correct remaining mainline obstruction

After 4dh the following issues are no longer open at the current `1/2` scale:

```text
raw frequency-conductor proliferation,
small effective conductor causing an exponent blow-up,
third-projection root density as an independent saving,
absolute Ramanujan gcd strata as a source of automatic power saving.
```

The exact local root-line identity is now best viewed as

```text
principal q=1 density
+
signed q>1 Ramanujan conductor correction.         (8.1)
```

A strict sub-square-root theorem must therefore use information not present in the absolute conductor ledger.  At least one of the following is necessary:

1. a genuine fixed-power deficit in the **physical principal density** after conditioning on the full eight-block masks; or
2. a signed correlation estimate which retains the Ramanujan divisor/conductor sum long enough to exploit cancellation with the physical factorization weights; or
3. a later exact structure which changes the receiver before either of the above is attempted.

Taking absolute values conductor-by-conductor cannot prove the desired strict saving.

The refined mainline receiver is

```text
boxed:
PrimitiveQuarterPairSameRootRamanujanConductorWeightedPhysicalPrincipalDensityDeficitAndSignedCorrelation.
```

Mandatory retained structure:

```text
m,n=B^(1/4+o(1)),
C=B^(chi+o(1)), 1/6<=chi<=1/4,
gcd(C,mn)=1,
rho^2=-1 mod C,

X_-=mn,
X_0=(m^2-n^2)/2,
X_0==rho*X_- on every physical C-root line,

1_{C|m^2+n^2}
 =(1/C) sum_rho sum_{q|C} c_q(m-rho*n),

all eight atomic block, balanced-cell, reciprocal,
orientation, squarefree and reconstruction masks retained.
```

---

## 9. Relation to the active s route

Merged s7-49 remains active and points to

```text
Stage14-s7-50.
```

4dh does not make a route-reactivation judgment.  It supplies a mainline interpretation of the conductor peel:

```text
conductor loss can be bounded internally at exponent 1/2,
but absolute conductor bounds cannot supply a strict saving.
```

If s7-50 produces a stronger signed or conductor-sensitive theorem, the next mainline stage should consume it rather than duplicate it.

---

## 10. H / fixed-U boundary

No new mainline H is needed at 4dh.

Reason: the remaining receiver has just been sharpened by an internal exact Ramanujan-conductor calculation, and the active s route has not yet exhausted its `s7-50` conductor step.  A new theorem audit now would freeze an unnecessarily broad object.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
ADDITIONAL_MAINLINE_H_NEEDED=false
SH48_REOPENED=false.
```

Merged fixed-`U` results remain separate:

```text
T88_CROSS_PROMOTED_TO_MAINLINE=false
FIXED_U_TO_WHOLE_FAMILY_CROSS_PROMOTION_PROVED=false.
```

---

## 11. Whole-family theorem and next stage

The canonical theorem remains

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Next mainline:

```text
NEXT=Stage14-4di.
```

Stage14-4di should condition the same-root Ramanujan packet on one of the large physical atomic blocks and test whether the principal `q=1` density actually loses fixed-power mass under the full eight-block selectors, while preserving the signed `q>1` correction rather than taking absolute values too early.

---

## Stage boundary

```text
STAGE14_4DH=COMPLETE_SAME_ROOT_PYTHAGOREAN_SYNCHRONIZATION_RAMANUJAN_CONDUCTOR_RECOMBINATION_AND_ABSOLUTE_SQRT_BOUNDARY
MERGED_4DG_IMPORTED=true
MERGED_S7_49_IMPORTED=true
MERGED_X15_IMPORTED=true
X15_THIRD_PROJECTION_SAME_GAUSSIAN_ROOT_LABEL=true
THIRD_PROJECTION_INDEPENDENT_LOCAL_ROOT_DENSITY=false
NORM_AND_PYTHAGOREAN_ROOT_DENSITIES_MULTIPLICABLE=false
EXACT_CONDUCTOR_RAMANUJAN_RECOMBINATION_PROVED=true
Q_EQUALS_ONE_TERM_IS_LOCAL_PRINCIPAL_DENSITY=true
NONZERO_CONDUCTORS_ARE_SIGNED_RAMANUJAN_CORRECTIONS=true
RAMANUJAN_AMPLITUDE_BOUND_BY_DISCREPANCY_GCD=true
PRIMITIVE_D_ROOTLINE_SPACING_PROVED=true
CONDUCTOR_LOSS_HARMLESS_AT_SQRT_SCALE=true
NONZERO_RAMANUJAN_ABSOLUTE_SQRT_BOUND_PROVED=true
RAMANUJAN_AMPLITUDE_SPACING_FIXED_POWER_CANCELLATION=true
ABSOLUTE_CONDUCTOR_PEEL_STRICT_SAVING=false
RAMANUJAN_D_STRATUM_AND_X15_ROOTLINE_SAME_EVENT=true
SECOND_1_OVER_D_SPACING_FACTOR_ALLOWED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
REMAINING_RECEIVER=PrimitiveQuarterPairSameRootRamanujanConductorWeightedPhysicalPrincipalDensityDeficitAndSignedCorrelation
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
SH48_REOPENED=false
T88_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4di
```
