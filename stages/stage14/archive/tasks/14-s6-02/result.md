# Stage14-s6-02 — genus-one packet geometry and canonical large-prime incidence

## Purpose

Stage14-s6-01 converts the direct post-local global-small-point event into the exact fixed-packet system

```text
d0 u0^2 - d1 u1^2 = S^2 D^2,
d2 u2^2 - d0 u0^2 = X^2 D^2,
```

with

```text
d0=tau0*a*b,
d1=tau1*a*c,
d2=tau2*b*c,
```

where `a|rad(S)`, `b|rad(X)`, `c|rad(H)`, `S^2+X^2=H^2`, and the finite sign/2-adic packet `(tau0,tau1,tau2)` belongs to the sixteen s6-01 patterns.

Stage14-s6-02 does four things.

1. It proves that every fixed nonzero packet is a smooth genus-one complete intersection of two quadrics in `P^3`.
2. It proves that the coordinate/torsion boundary `u0*u1*u2*D=0` is zero-dimensional; no positive-dimensional accumulating component is hidden in the integral relaxation.
3. It eliminates one square variable exactly and exhibits the curve as a double cover of a smooth conic branched at four geometric points.
4. It turns a canonical large odd edge-kernel prime into a genuine congruence-line restriction on the **global square variables**. On a dyadic rectangle this gives a `1/ell` incidence gain, hence `B^{-eta}` in the large-prime/long-variable sector.

This is the first s6 stage where an actual post-local **sectoral** saving appears. It is not yet a full bound

```text
J_C(B) << B^(41/42-delta+epsilon)
```

because the tiny/smooth edge-kernel complement and the short incident-variable complement remain open.

No new external theorem is used.

---

## 1. Fixed packet curve

Fix a primitive oriented Pythagorean base

```text
S>0, X>0, H>0,
S^2+X^2=H^2,
```

and one nonzero signed squarefree packet `(d0,d1,d2)` from s6-01.

In projective coordinates

```text
[u0:u1:u2:D] in P^3
```

define

```text
Q1 = d0*u0^2 - d1*u1^2 - S^2*D^2,
Q2 = d2*u2^2 - d0*u0^2 - X^2*D^2.
```

The fixed witness curve is

```text
C_sigma = {Q1=Q2=0} subset P^3.
```

All coefficients `d0,d1,d2,S,X,H` are nonzero.

---

## 2. Pencil determinant

For pencil parameters `[lambda:mu]`,

```text
lambda*Q1 + mu*Q2
```

is diagonal with coefficients

```text
u0^2 : d0*(lambda-mu),
u1^2 : -d1*lambda,
u2^2 : d2*mu,
D^2  : -(lambda*S^2 + mu*X^2).
```

Therefore, up to an irrelevant nonzero sign,

```text
Det(lambda,mu)
 = d0*d1*d2
   * lambda
   * mu
   * (lambda-mu)
   * (lambda*S^2 + mu*X^2).
```

The four singular members occur at

```text
[0:1],
[1:0],
[1:1],
[-X^2:S^2].
```

They are pairwise distinct because `S,X,H` are positive and

```text
S^2+X^2=H^2 != 0.
```

In particular, `[-X^2:S^2]` cannot equal `[1:1]` because that would force `S^2+X^2=0`.

```text
FIXED_PACKET_PENCIL_DETERMINANT_EXACT=true.
```

---

## 3. Direct smoothness proof

The gradients are

```text
grad Q1 = (2 d0 u0, -2 d1 u1, 0, -2 S^2 D),
grad Q2 = (-2 d0 u0, 0, 2 d2 u2, -2 X^2 D).
```

Suppose a projective point of `C_sigma` were singular. Then the two gradients would be linearly dependent:

```text
grad Q2 = t * grad Q1
```

for some scalar `t`.

From the `u2` coordinate we get

```text
u2=0.
```

If `t=0`, the `u0` and `D` coordinates force `u0=D=0`, and then `Q1=0` forces `u1=0`, impossible in projective space.

Hence `t!=0`. The `u1` coordinate then gives

```text
u1=0.
```

The two quadric equations become

```text
d0*u0^2 = S^2*D^2,
-d0*u0^2 = X^2*D^2.
```

Adding gives

```text
H^2*D^2=0.
```

Thus `D=0`, then `u0=0`, again impossible.

So `C_sigma` is smooth.

A smooth complete intersection of two quadrics in `P^3` has degree four and, by adjunction,

```text
K_C = (K_P3 + 2H + 2H)|_C = 0.
```

Therefore

```text
2g-2=0,
g=1.
```

Thus every fixed nonzero packet is a smooth genus-one curve.

```text
FIXED_PACKET_SMOOTH_GENUS_ONE_PROVED=true.
```

This identifies the exact geometric object which the post-local count is averaging.

---

## 4. Coordinate/torsion boundary is finite

The integral witness construction excludes zero factors `Gi`, because `Gi=0` gives `W=0`, hence a rational 2-torsion point. In packet coordinates this is reflected by coordinate hyperplanes such as `ui=0`; `D=0` is the projective infinity boundary of the denominator-cleared model.

Since `C_sigma` is a smooth irreducible degree-four curve and is not contained in any coordinate hyperplane, every hyperplane section

```text
u0=0,
u1=0,
u2=0,
D=0
```

is zero-dimensional of total intersection degree four.

The claim can also be seen directly. For example, `u0=0` gives

```text
-d1*u1^2 = S^2*D^2,
d2*u2^2   = X^2*D^2.
```

Over the algebraic closure `D` cannot vanish, and after scaling `D=1` there are only the four sign choices for `u1,u2`.

Likewise `D=0` gives

```text
d0*u0^2=d1*u1^2=d2*u2^2,
```

again only finitely many projective points.

Hence

```text
POSITIVE_DIMENSIONAL_TORSION_BOUNDARY_COMPONENT=false.
```

There is no hidden rational line/conic coming from the coordinate boundary which could dominate the post-local incidence count.

---

## 5. Eliminate one square variable

Adding the two defining equations eliminates `u0`:

```text
d2*u2^2 - d1*u1^2 = H^2*D^2.
```

Thus the projection

```text
pi0 : C_sigma -> K_sigma,
[u0:u1:u2:D] |-> [u1:u2:D]
```

lands on the conic

```text
K_sigma:
  d2*u2^2 - d1*u1^2 = H^2*D^2.
```

This conic is smooth because its diagonal coefficients are all nonzero.

The forgotten coordinate is recovered from

```text
d0*u0^2 = d1*u1^2 + S^2*D^2.
```

Therefore `C_sigma` is an exact degree-two square lift of the conic.

The branch points are given by `u0=0`. On the conic they satisfy

```text
d1*u1^2 = -S^2*D^2,
d2*u2^2 =  X^2*D^2.
```

As above `D!=0`, so after `D=1` there are exactly four distinct geometric choices

```text
u1 = +/- S/sqrt(-d1),
u2 = +/- X/sqrt(d2).
```

Hence the conic double cover is branched at four geometric points, another direct genus-one certificate.

```text
ONE_SQUARE_VARIABLE_ELIMINATION_EXACT=true
CONIC_PLUS_SQUARE_LIFT_EXACT=true.
```

---

## 6. Recall the three odd edge kernels

From s6-01 the odd kernel packet factors as

```text
d0_odd = a*b,
d1_odd = a*c,
d2_odd = b*c,
```

with pairwise coprime odd squarefree

```text
a | rad_odd(S),
b | rad_odd(X),
c | rad_odd(H).
```

Thus every odd kernel prime belongs to exactly one edge:

```text
ell|a  -> edge (u0,u1), base difference S,
ell|b  -> edge (u0,u2), base difference X,
ell|c  -> edge (u1,u2), base difference H.
```

Let

```text
ell = P^+(abc)
```

when `abc>1`. Because `a,b,c` are pairwise coprime, `ell` has a unique edge label.

This is the canonical large edge-kernel prime used below.

---

## 7. Divide once by the edge prime

### 7.1 S-edge: ell divides a

Write `a=ell*a'`. The first equation is

```text
ell*a'*(tau0*b*u0^2 - tau1*c*u1^2)
 = S^2*D^2.
```

Because `ell|S`, the right side is divisible by `ell^2`. Divide once by `ell` and reduce modulo `ell`:

```text
tau0*b*u0^2 = tau1*c*u1^2  (mod ell).
```

All displayed coefficients are units modulo the odd prime `ell`.

If the coefficient ratio is a quadratic residue, the solutions are contained in at most two lines

```text
u0 = +rho*u1 (mod ell),
u0 = -rho*u1 (mod ell).
```

If the ratio is a nonresidue, the only residue solution has `u0=u1=0 mod ell`, which is even sparser.

Hence in all cases the residue set is contained in at most two one-dimensional congruence lines.

### 7.2 X-edge: ell divides b

The second equation gives after one division by `ell`

```text
tau2*c*u2^2 = tau0*a*u0^2  (mod ell),
```

so `(u0,u2)` lies on at most two congruence lines modulo `ell`.

### 7.3 H-edge: ell divides c

Use the eliminated relation

```text
d2*u2^2-d1*u1^2=H^2*D^2.
```

After one division by `ell`:

```text
tau2*b*u2^2 = tau1*a*u1^2 (mod ell),
```

so `(u1,u2)` lies on at most two congruence lines.

Therefore

```text
CANONICAL_EDGE_LARGE_PRIME_TWO_LINE_INCIDENCE=true.
```

This is crucially a restriction on the actual global square variables. It is not merely another local Legendre-symbol acceptance condition.

---

## 8. Rectangle count on a congruence line

Let the incident square variables range in dyadic boxes

```text
|ui| ~ Ui,
|uj| ~ Uj,
Ui,Uj >= 1.
```

For one congruence line

```text
ui = rho*uj (mod ell),
```

sum over the shorter variable. For each value of the shorter variable, the longer variable lies in one residue class modulo `ell`, hence has

```text
O(Umax/ell + 1)
```

choices.

Thus one line contributes

```text
O(Ui*Uj/ell + min(Ui,Uj) + 1),
```

and the union of at most two lines satisfies the same bound up to an absolute constant:

```text
N_ij(Ui,Uj;ell)
 << Ui*Uj/ell + min(Ui,Uj) + 1.
```

This is an exact geometry-of-numbers-free incidence bound; no character cancellation is needed.

```text
EDGE_LINE_RECTANGLE_BOUND_PROVED=true.
```

---

## 9. Sectoral power saving

Fix `eta>0` and consider a dyadic packet sector satisfying

```text
ell >= B^eta
```

for the canonical odd edge-kernel prime and

```text
max(Ui,Uj) >= B^eta
```

for its incident square-variable pair.

Relative to the trivial pair count `O(Ui*Uj)`,

```text
Ui*Uj/ell <= B^(-eta) Ui*Uj.
```

Also

```text
min(Ui,Uj)
 <= Ui*Uj/max(Ui,Uj)
 <= B^(-eta) Ui*Uj.
```

Therefore

```text
N_ij(Ui,Uj;ell)
 << B^(-eta) Ui*Uj + 1.
```

Away from the finitely small unit boxes, the square-variable layer obtains a genuine `B^{-eta}` incidence gain.

We record this carefully as

```text
LARGE_EDGE_KERNEL_LONG_VARIABLE_SECTOR_SAVING=B^(-eta).
```

It is a **sectoral witness-incidence saving**, not yet the global `delta_post` required to improve `B^(41/42)` for the entire family.

The difference matters: to turn this into a full post-local theorem, the complementary packets must also be shown sparse.

---

## 10. Exact complement left after the gain

Every packet not covered by Section 9 lies in at least one of the following complements.

### Complement A — tiny/smooth odd edge kernel

```text
P^+(abc) < B^eta
```

or `abc=1`.

This is a moving friability condition on the selected divisors of the five s5 columns. It is not controlled merely by the closed local-character theorem.

### Complement B — short incident square variables

For the canonical edge of `ell`,

```text
max(Ui,Uj) < B^eta.
```

The two-line congruence then need not produce a power gain relative to the tiny rectangle. This sector should instead exploit the remaining conic/square-lift equation and the anisotropic height relations.

### Complement C — coarse polynomial height ledger

s6-01 only used a generic fixed exponent `K_C` to prove that all witness variables are polynomially bounded. For a global assembly, this is too coarse to optimize the trade between

```text
large kernel,
short square variables,
denominator D,
base height H.
```

The next stage must sharpen those relative size relations rather than merely enlarge the polynomial box.

Thus

```text
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false.
```

---

## 11. Determinant-method status

The geometry is now suitable for determinant-method or genus-one point-count inputs:

- fixed packet is smooth;
- degree is four;
- genus is one;
- no positive-dimensional coordinate boundary remains;
- the coefficients and witness height are polynomially bounded.

However, a black-box point bound applied separately to each fixed packet does not by itself reduce the number of moving locally-soluble base/state packets, currently bounded on the physical scale by `B^(41/42+epsilon)`.

The new large-prime congruence-line mechanism is therefore more relevant to the immediate post-local goal because it couples the moving kernel state to the actual global witness coordinates.

```text
DETERMINANT_METHOD_GEOMETRY_READY=true
PER_FIXED_CURVE_BLACK_BOX_ALONE_SUFFICIENT_FOR_POST_LOCAL_POWER_SAVING=false.
```

---

## 12. Quantitative position after s6-02

The s5u/s6-00 starting point remains

```text
V(B) <= J_C(B) <= B^(41/42+epsilon).
```

The square-root upper-bound target still needs

```text
10/21
```

of additional physical-scale exponent saving.

s6-02 proves something narrower but genuinely new in the s6 architecture:

> whenever a post-local packet carries a sufficiently large odd edge-kernel prime and at least one incident global square variable is comparably long, that packet sector pays an explicit `B^{-eta}` incidence factor.

There is no arithmetic resonance in that sector. The remaining problem is now a **complement problem**: show that tiny/smooth kernels and short incident square-variable packets cannot collectively recover the full `B^(41/42)` mass.

That is the task of s6-03.

---

## Boundary

```text
STAGE14_S6_02=COMPLETE_GENUS_ONE_PACKET_GEOMETRY_AND_LARGE_PRIME_INCIDENCE_SECTOR
FIXED_PACKET_PENCIL_DETERMINANT_EXACT=true
FIXED_PACKET_SMOOTH_GENUS_ONE_PROVED=true
POSITIVE_DIMENSIONAL_TORSION_BOUNDARY_COMPONENT=false
ONE_SQUARE_VARIABLE_ELIMINATION_EXACT=true
CONIC_PLUS_SQUARE_LIFT_EXACT=true
CANONICAL_EDGE_LARGE_PRIME_TWO_LINE_INCIDENCE=true
EDGE_LINE_RECTANGLE_BOUND_PROVED=true
LARGE_EDGE_KERNEL_LONG_VARIABLE_SECTOR_POWER_SAVING_PROVED=true
LARGE_EDGE_KERNEL_LONG_VARIABLE_SECTOR_SAVING=B^(-eta)
DETERMINANT_METHOD_GEOMETRY_READY=true
PER_FIXED_CURVE_BLACK_BOX_ALONE_SUFFICIENT_FOR_POST_LOCAL_POWER_SAVING=false
SMALL_KERNEL_COMPLEMENT_OPEN=true
SHORT_INCIDENT_VARIABLE_COMPLEMENT_OPEN=true
ANISOTROPIC_HEIGHT_LEDGER_NEEDED=true
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s6-03
```
