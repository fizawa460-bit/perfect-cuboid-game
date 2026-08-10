# Stage14-t83 — fixed-U projective incidence to short determinant-quotient switch

## Status

`COMPLETE_FIXED_U_DIVISOR_PROJECTIVE_INCIDENCE_TO_SHORT_NONZERO_DETERMINANT_QUOTIENT`

Stage14-t83 consumes merged Stage14-t82 and merged Stage14-tH23.  The tH23 snapshot is treated as complete: its negative applicability verdict is not reopened or rewritten.  In accordance with `stages/stage14/H-PROTOCOL.md`, this stage performs the next internal reduction and does not ask tH23 to chase a new receiver.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

No new whole-family exponent is claimed here.

---

## 1. Entering hard packet

Fix the t82 packet

```text
(U,epsilon,k,h,kappa,beta),
U=R+iS,
m=N(U)=R^2+S^2,
gcd(R,S)=1.
```

Let

```text
d=d_diag.
```

Merged t82/tH23 give

```text
d | D_Ubeta | |R*S|,
# {d for fixed U}=B^o(1),
d <= m/2 < ell/4,
[pi]=sigma([V]) mod d,
```

where

```text
pi=x+i*y,
N(pi)=ell,
V=p+i*q,
N(V)=n=k*delta=(r^2+t^2)/2,
sigma in {+1,-1}
```

is the already-fixed identity/inversion orientation.  Every prime of `d` lies in the t77 ray-active unit modulus, hence

```text
gcd(d,ell*n)=1.
```

The physical masks retained below include

```text
ell>2n,
ell^2>4B,
h*ell*(r^2+t^2)<=4B,
ell*odd(h)*odd(r)*odd(t)<2B,
ell*delta<=Y_U,
```

as well as canonical `pi`, balanced primitive `V`, the four-cell coefficients, fixed beta, and the fixed reciprocal orientation.

---

## 2. The projective relation is one integer determinant divisibility

For the fixed orientation define

```text
Delta_sigma := y*p - sigma*x*q,
T_sigma     := x*p + sigma*y*q.
```

If `sigma=+1`, `Delta_sigma` is the signed determinant of `pi` and `V` up to sign.  If `sigma=-1`, it is the corresponding determinant against `conj(V)`.

Because all four projective coordinates are units modulo `d`, the t82 relation is exactly

```text
boxed:
d | Delta_sigma.                                      (2.1)
```

The companion identity is the elementary norm identity

```text
boxed:
Delta_sigma^2 + T_sigma^2 = ell*n.                  (2.2)
```

Thus the post-tH23 incomplete inverse-fraction incidence may be reparameterized without introducing a new frequency or modulus family.

```text
PURE_PROJECTIVE_INCIDENCE_EQUALS_INTEGER_DETERMINANT_DIVISIBILITY=true
PROJECTIVE_DETERMINANT_COMPANION_NORM_IDENTITY=true
```

---

## 3. The determinant cannot vanish on a physical state

Suppose `Delta_sigma=0`.  Since `pi=(x,y)` is primitive and `V=(p,q)` is primitive, the two integer vectors `pi` and `(p,sigma*q)` are rationally parallel only if they agree up to sign.  Consequently

```text
N(V)=N(pi)=ell.
```

But merged t65/t82 retain

```text
ell>2n,
n=N(V)>0.
```

This is impossible.  Hence

```text
boxed:
Delta_sigma != 0.                                   (3.1)
```

This removes the exact projective diagonal from the physical hard branch.  It is important not to replace it by a formal zero-frequency diagonal later.

```text
EXACT_INTEGER_PROJECTIVE_DIAGONAL_PHYSICAL=false
NONZERO_DETERMINANT_QUOTIENT_FORCED=true
```

---

## 4. Determinant-quotient switch

By (2.1) and (3.1), write uniquely

```text
Delta_sigma=d*j,
j in Z\{0}.
```

The short ellipse gives

```text
h*ell*(r^2+t^2)<=4B.
```

Since `n=(r^2+t^2)/2`, this is

```text
h*ell*n<=2B.                                        (4.1)
```

Combining (2.2) with (4.1),

```text
|Delta_sigma|<=sqrt(ell*n)<=sqrt(2B/h).
```

Therefore

```text
boxed:
0<|j|<=sqrt(2B/h)/d,                                (4.2)
```

or equivalently

```text
boxed:
d*|j|<=sqrt(2B/h).                                 (4.3)
```

In particular

```text
d>sqrt(2B/h) => no physical state,                  (4.4)
```

and every surviving state has

```text
min(d,|j|) <= (2B/h)^(1/4).                         (4.5)
```

Thus the fixed-divisor single-frequency problem has an exact divisor-switch variable: either the divisor modulus or its nonzero determinant quotient is quarter-scale or shorter.

```text
DETERMINANT_QUOTIENT_SWITCH_PROVED=true
DETERMINANT_QUOTIENT_PRODUCT_BUDGET=sqrt(2B/h)
ONE_OF_DIVISOR_OR_QUOTIENT_IS_QUARTER_SCALE=true
```

No cancellation theorem is used here.

---

## 5. Fixed determinant quotient has at most two cover vectors

Fix `pi`, `sigma`, `d`, and a nonzero integer `j`.  The equation

```text
y*p-sigma*x*q=d*j                                  (5.1)
```

is an affine integer line.  Since `gcd(x,y)=1`, any two integer solutions differ by an integer multiple of

```text
(x,sigma*y),
```

whose Euclidean length is exactly

```text
sqrt(x^2+y^2)=sqrt(ell).
```

Every physical cover vector satisfies

```text
N(V)=n<ell/2,
```

so it lies in the open disk of radius `sqrt(ell/2)`.  The intersection of any line with that disk has length strictly less than

```text
2*sqrt(ell/2)=sqrt(2*ell)<2*sqrt(ell).
```

Three lattice points on (5.1) would span at least `2*sqrt(ell)`, impossible.  Therefore

```text
boxed:
# {primitive physical V for fixed (pi,sigma,d,j)} <= 2.   (5.2)
```

The positivity/balanced/primitive masks can only reduce this count.

Combining with (4.2), for fixed `(pi,sigma,d)` one obtains the deterministic cover bound

```text
#V
 <= 4*floor(sqrt(2B/h)/d),                         (5.3)
```

with the convention that the count is zero when the floor is zero.  This is a counting statement for the projective-incidence fiber; it is not promoted here to a whole-packet power saving because the remaining sums over canonical `pi`, the physical hyperbolas, and fixed-packet/global quantifiers still have to be charged exactly once.

```text
FIXED_DETERMINANT_QUOTIENT_COVER_MULTIPLICITY_AT_MOST=2
FIXED_PI_DIVISOR_COVER_COUNT_BY_QUOTIENT_SWITCH_PROVED=true
FIXED_U_PACKET_POWER_SAVING_PROVED=false
```

---

## 6. Companion coordinate is automatically a unit modulo d

Because

```text
gcd(d,ell*n)=1,
d|Delta_sigma,
Delta_sigma^2+T_sigma^2=ell*n,
```

one has

```text
boxed:
gcd(T_sigma,d)=1.                                  (6.1)
```

Hence the switched norm equation

```text
boxed:
T_sigma^2+d^2*j^2=ell*k*delta                       (6.2)
```

is primitive at every prime of `d`.  No ray-active prime can disappear into both coordinates of the switched binary norm form.

This is the exact arithmetic object handed to the next internal stage.

```text
SWITCHED_COMPANION_COORDINATE_UNIT_MOD_D=true
SWITCHED_BINARY_NORM_FORM_PRIMITIVE_ON_D=true
```

---

## 7. What this does and does not close

Stage14-tH23 correctly found that no off-the-shelf fixed-modulus Kloosterman theorem applies directly to the t82 incomplete physical slope sum.  Stage14-t83 removes that particular presentation from the next step: the surviving hard incidence is now represented by

```text
d | R*S,
0<|j|,
d*|j|<=sqrt(2B/h),
T^2+d^2*j^2=ell*k*delta,
gcd(T,d)=1,
ell>2k*delta,
```

plus the unchanged canonical-prime, balanced-cover, four-cell, short-ellipse, sharp-hyperbola, and `ell*delta` masks.

The exact `j` switch does **not** by itself prove a fixed `B`-power saving.  In particular the branch `d=B^o(1)` may still have a determinant quotient of square-root length, while a fixed-power `d` still requires a correct summation over canonical `pi` and the physical norm variable.

The refined receiver is

```text
SharedUBalancedFixedUSelectorDivisorShortDeterminantQuotientCanonicalPrimeCoverBinaryNormEnergy.
```

Its irreducible equation is

```text
T^2+d^2*j^2=ell*k*delta,
0<d*|j|<=sqrt(2B/h),
gcd(T,d)=1.
```

Stage14-t84 should exploit this binary norm equation together with the canonical-largest-prime and `ell*delta` constraints before any further broad theorem audit.

---

## 8. H/tH decision under the frozen-snapshot protocol

Merged tH23 is complete and is consumed as its own scoped snapshot certificate.

```text
TH23_CONSUMED=true
TH23_TARGET_REOPENED=false
TH23_REFINEMENT_REQUESTED=false
```

The t83 receiver is materially different from the tH23 fixed-modulus inverse-fraction target, but it is not yet in a standard external theorem form.  Therefore a new auxiliary audit would be premature.

```text
TH24_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH24=false
```

If t84 converts (6.2) to a genuine standard binary-form / prime-dispersion theorem adapter, it may open `tH24` against the t84 snapshot.  Under `H-PROTOCOL.md`, that future target must then remain immutable while the t-route continues.

---

## 9. Global ledger

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T83_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t84
```

---

## Locked boundary

```text
STAGE14_T83=COMPLETE_FIXED_U_DIVISOR_PROJECTIVE_INCIDENCE_TO_SHORT_NONZERO_DETERMINANT_QUOTIENT
MERGED_T82_IMPORTED=true
MERGED_TH23_IMPORTED=true
TH23_TARGET_REOPENED=false
PURE_PROJECTIVE_INCIDENCE_EQUALS_INTEGER_DETERMINANT_DIVISIBILITY=true
PROJECTIVE_DETERMINANT_COMPANION_NORM_IDENTITY=true
EXACT_INTEGER_PROJECTIVE_DIAGONAL_PHYSICAL=false
NONZERO_DETERMINANT_QUOTIENT_FORCED=true
DETERMINANT_QUOTIENT_SWITCH_PROVED=true
DETERMINANT_QUOTIENT_PRODUCT_BUDGET=sqrt(2B/h)
ONE_OF_DIVISOR_OR_QUOTIENT_IS_QUARTER_SCALE=true
FIXED_DETERMINANT_QUOTIENT_COVER_MULTIPLICITY_AT_MOST=2
FIXED_PI_DIVISOR_COVER_COUNT_BY_QUOTIENT_SWITCH_PROVED=true
SWITCHED_COMPANION_COORDINATE_UNIT_MOD_D=true
SWITCHED_BINARY_NORM_FORM_PRIMITIVE_ON_D=true
FIXED_U_PACKET_POWER_SAVING_PROVED=false
TH23_CONSUMED=true
TH24_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH24=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T83_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
PREFERRED_RECEIVER=SharedUBalancedFixedUSelectorDivisorShortDeterminantQuotientCanonicalPrimeCoverBinaryNormEnergy
NEXT=Stage14-t84
```
