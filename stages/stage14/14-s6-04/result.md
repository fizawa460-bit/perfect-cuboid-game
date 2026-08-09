# Stage14-s6-04 — exact-witness resonance and denominator-square incidence

## Purpose

Stage14-s6-03 proves three exact centered quartic square projections and a fixed-packet auxiliary-prime square-sieve saving. It then proposes a possible next step: sum the auxiliary character over moving locally-admissible packets while retaining the exact global witness incidence.

Stage14-s6-04 audits that proposal before building a larger analytic machine.

The audit finds an exact obstruction:

> on the support of an actual two-quadrics witness, every centered quartic is already an integer square, so every good auxiliary quadratic character is identically `+1` away from its zero set.

Therefore an auxiliary-character correlation whose weight already imposes the full witness equations cannot exhibit cancellation. The moving-packet theorem suggested at the end of s6-03 is false in that form; its character is tautological on the support to be counted.

This stage replaces that invalid target with a new exact arithmetic restriction coming from the denominator itself. The eliminated `H`-edge equation gives a congruence modulo `D^2`, not merely modulo `D`. Because the primitive denominator is coprime to all packet square variables and squarefree kernels, the actual global square-variable pair lies on only `D^epsilon` projective congruence lines modulo `D^2`.

Thus the denominator is a genuine global incidence modulus:

```text
N_D(U1,U2)
 <<_epsilon
 D^epsilon (U1 U2 / D^2 + min(U1,U2) + 1).
```

Together with the s6-03 size forcing `D <= 2 max(|u1|,|u2|)`, this gives a kernel-independent relative `D^(-1+epsilon)` coordinate saving whenever `D` is large.

The stage is deliberately precise about scope. This still does not turn coordinate density into an unweighted packet-existence saving. Instead it isolates the correct next global statistic: the least denominator of a bounded-height rational representative in a locally-admissible packet.

No new external theorem is used.

---

## 1. Frozen witness packet

For a primitive oriented Pythagorean base

```text
S^2 + X^2 = H^2
```

and one s6-01 signed squarefree packet, write

```text
d0 u0^2 - d1 u1^2 = S^2 D^2,
d2 u2^2 - d0 u0^2 = X^2 D^2.
```

Adding gives

```text
d2 u2^2 - d1 u1^2 = H^2 D^2.          (H-edge)
```

The packet satisfies

```text
d0 d1 d2 = k^2 > 0
```

for an integer `k`, and s6-01 proves the primitive denominator coprimality

```text
gcd(D, d0 d1 d2 u0 u1 u2) = 1.
```

All variables in the present stage refer to this exact integral witness system.

---

## 2. Exact witness resonance of the centered quartics

Stage14-s6-03 defines

```text
Phi0(U,V)
 = d0 (d0 U^2 - S^2 V^2)(d0 U^2 + X^2 V^2),

Phi1(U,V)
 = d1 (d1 U^2 + S^2 V^2)(d1 U^2 + H^2 V^2),

Phi2(U,V)
 = d2 (d2 U^2 - X^2 V^2)(d2 U^2 - H^2 V^2).
```

For an exact witness the two quadrics give identically

```text
Phi0(u0,D) = (k u1 u2)^2,
Phi1(u1,D) = (k u0 u2)^2,
Phi2(u2,D) = (k u0 u1)^2.
```

This identity has an immediate character consequence.

Let `lambda` be a good odd auxiliary prime for `Phi_i`. If `lambda` does not divide the displayed square root, then

```text
chi_lambda(Phi_i(u_i,D)) = +1.
```

If it divides the square root, the value is `0`.

For squarefree auxiliary `q` composed of good primes,

```text
chi_q(Phi_i(u_i,D)) in {0,1}
```

on every exact witness, and it equals `1` whenever `q` is coprime to the corresponding square root.

Therefore

```text
EXACT_WITNESS_AUXILIARY_CHARACTER_RESONANCE=true.
```

There is no sign cancellation to extract after the full witness equations have already been imposed.

---

## 3. Why the s6-03 moving-weight correlation target cannot hold as stated

Suppose a nonnegative weight

```text
w(F,sigma;u,D)
```

is supported only on exact witnesses, as suggested in the schematic correlation target of s6-03.

For any good auxiliary squarefree `q` avoiding the corresponding square roots,

```text
sum w * chi_q(Phi_i)
 = sum w.
```

In particular, take a Dirac weight supported on one exact witness and choose any good auxiliary `q` coprime to its square root. Then

```text
|sum w * chi_q(Phi_i)| = sum w = 1.
```

No uniform estimate of the form

```text
|sum w * chi_q(Phi_i)|
 << q^(-kappa) sum w
```

with `kappa>0` can hold for this class of witness-supported weights.

The failure is not caused by an unhandled bad prime, a boundary term, or a weak large sieve. It is a logical resonance:

```text
exact witness condition
  => centered quartic is a square
  => quadratic character is already +1.
```

Hence

```text
MOVING_EXACT_WITNESS_CHARACTER_CANCELLATION_TARGET_VALID=false.
```

The auxiliary square sieve remains valid and useful only when applied to an ambient coordinate family **before** the square condition is imposed. It cannot be re-applied as a cancellation theorem on the exact witness set itself.

This corrects, rather than contradicts, s6-03: the fixed-packet square-sieve theorem is unchanged; only the proposed mechanism for transferring that density estimate to an unweighted packet-existence count is rejected.

---

## 4. A canonical selector alone does not repair the resonance

One might choose one canonical witness from every soluble packet, for example by minimizing

```text
(D, |u0|+|u1|+|u2|, |u0|, |u1|, |u2|)
```

lexicographically, and then put weight one only on those selected points.

This removes coordinate multiplicity, but it does not create character cancellation. Every selected point is still an exact witness, so the same identity gives

```text
chi_q(Phi_i)=1
```

for all good `q` avoiding its square root.

Therefore

```text
CANONICAL_SELECTOR_ALONE_CREATES_AUXILIARY_CANCELLATION=false.
```

A successful packet-existence theorem must use arithmetic structure of the selector itself — for example least-denominator distribution, first-point geometry, or a direct incidence count in which the ambient volume is controlled — rather than an auxiliary character which is tautologically positive on the selected support.

---

## 5. The denominator produces an exact modulus `D^2`

Return to the eliminated `H`-edge equation

```text
d2 u2^2 - d1 u1^2 = H^2 D^2.
```

Reducing modulo `D^2` gives

```text
d2 u2^2 == d1 u1^2  (mod D^2).        (*)
```

By primitive denominator coprimality,

```text
gcd(D, d1 d2 u1 u2)=1.
```

Thus `d1,d2,u1,u2` are units modulo `D^2`. Put

```text
r = u2 * u1^(-1)  (mod D^2).
```

Then `(*)` is equivalent to

```text
r^2 == d1 * d2^(-1)  (mod D^2).
```

For every square root `r`, the actual square variables lie on the projective congruence line

```text
u2 == r u1  (mod D^2).
```

This yields a global-point incidence modulus which is present even when the odd edge kernel is trivial.

```text
DENOMINATOR_SQUARE_MODULUS_EXACT=true.
```

---

## 6. Number of denominator congruence lines

Write

```text
D = 2^e * D_odd.
```

For an odd prime power `p^(2a)`, a unit has either zero or exactly two square roots whenever it is a square. Hence the odd part contributes at most

```text
2^omega(D_odd)
```

roots.

For the 2-primary unit group modulo `2^(2e)`, a unit square has at most four square roots. Therefore the total number of roots of

```text
r^2 == d1 d2^(-1) (mod D^2)
```

is at most

```text
4 * 2^omega(D_odd).
```

Using the standard divisor bound,

```text
2^omega(D) <<_epsilon D^epsilon,
```

so the exact witness pair `(u1,u2)` is covered by only

```text
D^epsilon
```

congruence lines modulo `D^2`.

The same construction is available from the `S`- and `X`-edge equations for `(u0,u1)` and `(u0,u2)` respectively.

```text
DENOMINATOR_LINE_MULTIPLICITY_SUBPOLYNOMIAL=true.
```

---

## 7. Dyadic rectangle count with denominator modulus

Let

```text
|u1| ~ U1,
|u2| ~ U2,
```

with `U1,U2>=1`.

For one line

```text
u2 == r u1 (mod D^2),
```

sum over the shorter variable. For each value of the shorter variable, the longer variable lies in one residue class modulo `D^2`. Hence one line contributes

```text
O(U1 U2 / D^2 + min(U1,U2) + 1).
```

Summing the `D^epsilon` possible roots gives

```text
boxed:
N_D(U1,U2)
 <<_epsilon
 D^epsilon
 ( U1 U2 / D^2 + min(U1,U2) + 1 ).
```

Thus

```text
DENOMINATOR_SQUARE_LINE_RECTANGLE_BOUND_PROVED=true.
```

This estimate is elementary and exact at the incidence level; it uses no character cancellation.

---

## 8. Large denominator gives a kernel-independent coordinate saving

Stage14-s6-03 proves

```text
D <= 2 max(|u1|,|u2|).
```

On a dyadic witness box this implies

```text
Umax >= D/2.
```

Therefore

```text
min(U1,U2)
 <= 2 U1 U2 / D,
```

and, since `Umin>=1`,

```text
1 <= 2 U1 U2 / D.
```

Also

```text
U1 U2 / D^2 <= U1 U2 / D.
```

Consequently the denominator-line bound simplifies to

```text
boxed:
N_D(U1,U2)
 <<_epsilon
 D^(-1+epsilon) U1 U2.
```

For

```text
D >= B^eta
```

this is a genuine coordinate-level saving

```text
B^(-eta+epsilon).
```

It is stronger than the `B^(-eta/3)` fixed-packet auxiliary-square-sieve saving available from s6-03 in the same large-denominator regime, and it is completely independent of the kernel size.

We record

```text
LARGE_DENOMINATOR_COORDINATE_SAVING=B^(-eta+epsilon).
```

The s6-03 auxiliary sieve remains useful as a separate ambient tool, but it is no longer the sharpest elementary mechanism for the large-`D` pair layer.

---

## 9. The existence-vs-density gap survives the stronger denominator modulus

The stronger `D^2` incidence still counts coordinate pairs **inside a fixed packet**. It does not by itself show that fewer locally-admissible packets possess at least one such pair.

Indeed, the statement

```text
packet has a global witness
```

requires only one coordinate pair to lie on one of the allowed congruence lines. A sparse union of lines can still contain one point for every packet.

Therefore neither

```text
fixed-packet auxiliary square density
```

nor

```text
fixed-packet D^2 congruence-line density
```

may simply be multiplied into

```text
N_local(B) << B^(41/42+epsilon).
```

Thus the s6-03 quantifier boundary remains:

```text
EXISTENCE_VS_COORDINATE_DENSITY_QUANTIFIER_GAP=true.
```

and

```text
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false.
```

---

## 10. Least denominator is the correct next packet-level statistic

For a locally-admissible packet `(F,sigma)` and fixed Stage14-s3 height-window constant `C`, define

```text
D_min(F,sigma;B)
```

to be the least positive denominator `D` among non-torsion rational representatives satisfying the s6-00/s6-03 logarithmic height window. Set `D_min=infinity` when no such representative exists.

Because a bounded rational-height set is finite, the minimum is well-defined whenever the packet contributes to `J_C(B)`.

Then exactly

```text
J_C(B)
 = #{(F,sigma) locally admissible : D_min(F,sigma;B) < infinity},
```

up to the already-frozen subpolynomial state multiplicity conventions.

For any threshold `T`, split

```text
J_C(B)
 = J_smallD(B;T) + J_largeD(B;T),
```

where

```text
J_smallD = #{D_min <= T},
J_largeD = #{T < D_min < infinity}.
```

This is now a packet-level split, not a coordinate-volume split.

The next theorem must control this **least-denominator distribution** or an equivalent first-point statistic. A statement only about the density of arbitrary coordinates in a packet box is insufficient.

```text
LEAST_DENOMINATOR_PACKET_STATISTIC_DEFINED=true.
```

---

## 11. What can and cannot be imported from parallel tracks

Merged Stage14-4bi-L strengthens the edge-prime incidence to the entire composite edge kernel and obtains an `incidence-saved OR small-D` dichotomy. That result is fully compatible with the present denominator analysis.

Merged Stage14-t32 proves complete split-torus angular correlation on a different Gaussian norm skeleton, but explicitly leaves its divisor-coupled norm-index family sum open. Its lesson is the same one seen here: complete local/angular correlation does not automatically imply a moving-family projection theorem.

Neither parallel result supplies a theorem for the least denominator of the s6 global-small-point packet. Therefore s6-04 does not import a nonexistent global exponent from those branches.

---

## 12. Quantitative position after s6-04

The unconditional physical upper bound remains

```text
V(B) <<_epsilon B^(41/42+epsilon).
```

The remaining saving needed for a square-root upper bound remains

```text
10/21.
```

What has changed is the structure of the open problem.

Before s6-04 the proposed route was

```text
moving exact-witness auxiliary-character correlation
+ small-D exception.
```

After the resonance audit, the valid route is

```text
least-denominator / first-point packet distribution
+ exact D^2 incidence geometry
+ composite-kernel incidence when useful.
```

The first item is genuinely global and cannot be manufactured from a character which is already `+1` on every exact witness.

---

## Boundary

```text
STAGE14_S6_04=COMPLETE_EXACT_WITNESS_RESONANCE_AUDIT_AND_DENOMINATOR_SQUARE_INCIDENCE
S6_03_FIXED_PACKET_AUXILIARY_SIEVE_RETAINED=true
EXACT_WITNESS_AUXILIARY_CHARACTER_RESONANCE=true
MOVING_EXACT_WITNESS_CHARACTER_CANCELLATION_TARGET_VALID=false
CANONICAL_SELECTOR_ALONE_CREATES_AUXILIARY_CANCELLATION=false
DENOMINATOR_SQUARE_MODULUS_EXACT=true
DENOMINATOR_LINE_MULTIPLICITY_SUBPOLYNOMIAL=true
DENOMINATOR_SQUARE_LINE_RECTANGLE_BOUND_PROVED=true
D_LARGE_FORCES_LONG_U1_OR_U2=true
LARGE_DENOMINATOR_COORDINATE_SAVING=B^(-eta+epsilon)
EXISTENCE_VS_COORDINATE_DENSITY_QUANTIFIER_GAP=true
LEAST_DENOMINATOR_PACKET_STATISTIC_DEFINED=true
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21
NEXT=Stage14-s6-05 attack the least-denominator distribution: count locally-admissible packets with D_min<=B^theta directly, and determine whether the complementary large-D_min family admits a genuine packet-level incidence saving rather than a coordinate-density saving
```
