# Stage14-s7-27 — full signed-quotient divisor collapse and reciprocal biquadratic reduction

## Status

`COMPLETE_FULL_SIGNED_QUOTIENT_DIVISOR_COLLAPSE_AND_RECIPROCAL_BIQUADRATIC_REDUCTION`

Stage14-s7-27 consumes merged `s7-26` and the simultaneously merged mainline `4cm`.  Both predecessors reduce the only remaining `7/8` saturation set to

```text
theta=5/16,
3/16 <= phi <= 1/4,
```

with no physical quadratic/`i` agreement branch.  The odd agreement support is split between the two linear factors on each reciprocal side.

The new point is that choosing only the *dominant* sign hides an exact product identity.  Retain both signs at once.  Then the four signed quotients have odd parts determined by the residual pair `(u_res,v_res)`.  Hence, after fixing the residual triple, the entire signed-quotient quadruple has only `B^o(1)` possibilities.  The apparent `B^(1/8+o(1))` raw quotient support in `4cm/s7-26` is therefore not an independent polynomial source on a fixed residual fiber.

After this collapse, all fixed-power freedom is carried by four mutually generated odd agreement moduli.  They satisfy two exact reciprocal quadratic equations.  Dividing out their scales gives one exact bidegree `(2,2)` ratio equation.  No uniform average estimate for this reciprocal biquadratic family is proved here, so the whole-family exponent remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Imported notation

Use the merged balanced packet

```text
xi cells: R,S,T,J,
k cells:  alpha,beta,gamma,delta.
```

Put

```text
X_sw=S*T,
X_ag=R*J,
K_sw=beta*gamma,
K_ag=alpha*delta,

r=r_1*r_2,
s=s_1*s_2,
X=x_1*x_2,
Y=y_1*y_2,

A=alpha*r,
D=delta*s,
P=R*X,
Q=J*Y.
```

Thus

```text
D>A>0,
Q>P>0,

H_k^- = D^2-A^2=(D-A)(D+A),
H_xi^-= Q^2-P^2=(Q-P)(Q+P).
```

Merged `s7-26/4cm` define the complete odd agreement allocations

```text
L_x^- = gcd(oddpart(X_ag),D-A),
L_x^+ = gcd(oddpart(X_ag),D+A),

L_k^- = gcd(oddpart(K_ag),Q-P),
L_k^+ = gcd(oddpart(K_ag),Q+P),
```

with

```text
L_x^- L_x^+ = oddpart(X_ag),
gcd(L_x^-,L_x^+)=1,

L_k^- L_k^+ = oddpart(K_ag),
gcd(L_k^-,L_k^+)=1.
```

No `i` branch remains.

---

## 2. Retain both signed quotients

Define four positive integral quotients

```text
c_x^- := (D-A)/L_x^-,
c_x^+ := (D+A)/L_x^+,

c_k^- := (Q-P)/L_k^-,
c_k^+ := (Q+P)/L_k^+.
```

These are exact because the corresponding allocation modulus divides its signed linear factor.

Their products are

```text
boxed:
c_x^- c_x^+
 = H_k^- / oddpart(X_ag),

boxed:
c_k^- c_k^+
 = H_xi^- / oddpart(K_ag).                    (2.1)
```

Merged `4cm` gives the complementary odd-part identities

```text
oddpart(H_k^-)
 = oddpart(X_ag)*oddpart(u_res),

oddpart(H_xi^-)
 = oddpart(K_ag)*oddpart(v_res).
```

Therefore

```text
boxed:
oddpart(c_x^- c_x^+) = oddpart(u_res),

boxed:
oddpart(c_k^- c_k^+) = oddpart(v_res).              (2.2)
```

This is stronger than the dominant-quotient range estimate: it controls both signs simultaneously.

---

## 3. Fixed residual data make the full quotient quadruple divisor-bounded

For a polynomially bounded endpoint packet, the 2-adic valuations of the two products in (2.1) are `O(log B)`.  Thus, for fixed `u_res`,

```text
c_x^- c_x^+
 = 2^j * oddpart(u_res)
```

for only `O(log B)=B^o(1)` possible `j`.  Each product has at most divisor-many ordered positive factorizations.  Hence

```text
# {(c_x^-,c_x^+) : fixed u_res} <= B^o(1).
```

Likewise

```text
# {(c_k^-,c_k^+) : fixed v_res} <= B^o(1).
```

Consequently

```text
boxed:
fixed (C,u_res,v_res)
=> full signed quotient quadruple
   (c_x^-,c_x^+,c_k^-,c_k^+)
   has B^o(1) possibilities.                         (3.1)
```

The common gcds are also harmless.  If an odd prime divides both `c_x^-` and `c_x^+`, it divides both `D-A` and `D+A`, hence divides `gcd(A,D)`, whose odd support is contained in `r*s` because `gcd(alpha,delta)=1`.  Similarly the odd common gcd of `c_k^-` and `c_k^+` is supported on `X*Y` because `gcd(R,J)=1`.

No density estimate is used.

---

## 4. The four dominant sign classes are bookkeeping, not separate receivers

`s7-26/4cm` selected one dominant sign on each side and obtained four sign pairs

```text
(-,-),(-,+),(+,-),(+,+).
```

When both signs are retained, every packet carries the single full system

```text
D-A=L_x^- c_x^-,
D+A=L_x^+ c_x^+,

Q-P=L_k^- c_k^-,
Q+P=L_k^+ c_k^+.
```

The previous four classes are recovered only by comparing `L_x^-` with `L_x^+` and `L_k^-` with `L_k^+`.  No case split is mathematically necessary for the exact reconstruction below.

Thus

```text
DOMINANT_SIGN_SPLIT_REQUIRED_FOR_EXACT_RECEIVER=false.
```

This does not eliminate any physical packet; all four dominance patterns observed in `s7-26` remain allowed.

---

## 5. Exact reciprocal four-modulus quadratic system

Let the finite 2-primary parts of the agreement products be

```text
epsilon_x := X_ag/oddpart(X_ag),
epsilon_k := K_ag/oddpart(K_ag).
```

Then

```text
X_ag=epsilon_x*L_x^-*L_x^+,
K_ag=epsilon_k*L_k^-*L_k^+.
```

Use

```text
(D+A)^2-(D-A)^2=4AD=4*r*s*alpha*delta,
```

and the four signed equations.  This gives the exact first reciprocal equation

```text
boxed:
(L_x^+ c_x^+)^2-(L_x^- c_x^-)^2
 = 4*r*s*epsilon_k*L_k^-*L_k^+.          (5.1)
```

Similarly

```text
(Q+P)^2-(Q-P)^2=4PQ=4*X*Y*R*J
```

gives

```text
boxed:
(L_k^+ c_k^+)^2-(L_k^- c_k^-)^2
 = 4*X*Y*epsilon_x*L_x^-*L_x^+.          (5.2)
```

Thus, after the residual triple fixes the quotient quadruple up to `B^o(1)`, the remaining agreement freedom is a pair of *mutually generated modulus equations*.  Neither modulus pair is an independent ambient parameter.

```text
RECIPROCAL_FOUR_MODULUS_QUADRATIC_SYSTEM_PROVED=true.
```

---

## 6. Exact bidegree `(2,2)` ratio equation

Set the positive rational modulus ratios

```text
x := L_x^+/L_x^-,
y := L_k^+/L_k^-.
```

Divide (5.1) by `(L_x^-)^2` and (5.2) by `(L_k^-)^2`, then multiply.  The scale variables cancel exactly, giving

```text
boxed:
((c_x^+)^2*x^2-(c_x^-)^2)
((c_k^+)^2*y^2-(c_k^-)^2)
 = 16*r*s*X*Y*epsilon_x*epsilon_k*x*y.    (6.1)
```

After projective homogenization this is a bidegree `(2,2)` equation in the two modulus ratios.  It may be smooth or degenerate for special coefficient packets; no generic smoothness assertion is made in this stage.

Equation (6.1) is not a relaxed quartic-energy replacement.  It is an exact consequence of the physical common-core packet, with all four signed quotient factors and reciprocal modulus products retained.

---

## 7. What the `B^o(1)` quotient collapse does and does not buy

The mainline `4cm` correctly records the raw range estimate

```text
(t_xi,t_k) support <= B^(1/8+o(1))
```

for a chosen dominant sign pair.  Stage14-s7-27 shows that, after conditioning on `(u_res,v_res)`, the *full* four-quotient data have only `B^o(1)` possibilities.  Therefore the raw `1/8` quotient support is not an independent factor in a charged-once residual fiber.

However this does **not** imply

```text
fixed (C,u_res,v_res)
=> B^o(1) switch products X_sw.
```

Many switch products could in principle map to the same quotient quadruple through different reciprocal modulus solutions of (5.1)-(5.2).  The remaining fixed-power question is precisely the number of legal modulus-ratio/scale solutions carrying the original squarefree cell, interval, root, orientation and reconstruction masks.

Thus

```text
FIXED_RESIDUAL_XI_SWITCH_FIBER_BO1_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false.
```

---

## 8. New minimal receiver

The top-edge receiver can now be stated without a dominant-sign split:

```text
TopThetaReciprocalBiquadraticModulusRatioIncidence.
```

For fixed residual data and one of the divisor-many quotient quadruples, count positive coprime allocation moduli

```text
(L_x^-,L_x^+,L_k^-,L_k^+)
```

satisfying (5.1)-(5.2), equivalently the ratio constraint (6.1) together with one scale equation, and all original physical masks.

A fixed-power average saving for this receiver would break the remaining `7/8` edge.

---

## 9. H / tH decision

No existing `tH17` theorem is cross-promoted: its signed fixed-U Kummer/rectangle coefficient space is different from the present positive common-core reciprocal modulus system.

A generic binary-quartic or Gaussian large-sieve request is also premature.  Before opening an auxiliary H line, `s7-28` should separate the singular/degenerate cases of (6.1), primitive-reduce the two modulus ratios, and test whether the remaining scale equation gives an elementary divisor/determinant bound.

```text
TH17_CROSS_PROMOTED_TO_S7_27=false
S7_27_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.
```

If a smooth nondegenerate bidegree `(2,2)` family with a genuine average rational-point obligation survives that exact reduction, then an s-specific H audit becomes justified at `s7-28`.

---

## Stage boundary

```text
STAGE14_S7_27=COMPLETE_FULL_SIGNED_QUOTIENT_DIVISOR_COLLAPSE_AND_RECIPROCAL_BIQUADRATIC_REDUCTION
MERGED_S7_26_IMPORTED=true
MERGED_4CM_COMPATIBILITY_CHECKED=true
FULL_XI_SIGNED_QUOTIENT_PAIR_DEFINED=true
FULL_K_SIGNED_QUOTIENT_PAIR_DEFINED=true
XI_SIGNED_QUOTIENT_PRODUCT_EXACT=H_k^-/oddpart(R*J)
K_SIGNED_QUOTIENT_PRODUCT_EXACT=H_xi^-/oddpart(alpha*delta)
XI_SIGNED_QUOTIENT_PRODUCT_ODDPART=oddpart(u_res)
K_SIGNED_QUOTIENT_PRODUCT_ODDPART=oddpart(v_res)
FIXED_RESIDUAL_FULL_SIGNED_QUOTIENT_QUADRUPLE_MULTIPLICITY=Bo1
DOMINANT_SIGN_SPLIT_REQUIRED_FOR_EXACT_RECEIVER=false
RECIPROCAL_FOUR_MODULUS_QUADRATIC_SYSTEM_PROVED=true
RECIPROCAL_RATIO_BIDEGREE_2_2_CURVE_PROVED=true
TOP_THETA_RECIPROCAL_BIQUADRATIC_MODULUS_RATIO_INCIDENCE_REQUIRED=true
TOP_THETA_RECIPROCAL_BIQUADRATIC_MODULUS_RATIO_INCIDENCE_PROVED=false
FIXED_RESIDUAL_XI_SWITCH_FIBER_BO1_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH17_CROSS_PROMOTED_TO_S7_27=false
S7_27_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
NEXT=Stage14-s7-28
```
