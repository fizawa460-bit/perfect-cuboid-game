# Stage35-EX 35EX-27 — rational source-lift firewall and Kummer normal form

Status: `PROVISIONAL_EXACT_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_NO_CREDIT`

This unit starts only after the mandatory post-35EX-26 fresh breadth audit. It does not revoke 35EX-26: the fixed-field descent there is exact over `K/K0`. The new point is arithmetic. A rational Master-Hit is a rational source point, so a rational point on the quotient over-cover must still lift rationally through `x^2-u*x+1=0`.

No E1, Stage35, or perfect-cuboid closure is claimed.

## 1. Input from 35EX-26

On the positive nondegenerate chamber, retain

```text
K0 = Q(u,h),
h^2 = u*(u+2),
```

and the descended receiver

```text
R = (u+2)*r^2,                                      (Q1)
R+u = (u+2)*s^2,                                    (Q2)
B^2 = R^2+u*R+1,                                    (Q3)
b^2 = (2*R+u+2*B)/(u+2).                            (Q4)
```

The original source extension is

```text
x^2-u*x+1=0.
```

35EX-26 reconstructs over that quadratic extension. For arithmetic over `Q`, rational lifting is an extra exact condition.

## 2. Rational source-lift criterion

For a rational source define

```text
k = x - 1/x.
```

Then

```text
k^2 = u^2-4.                                        (L)
```

Conversely, suppose `u,h,k in Q` satisfy

```text
h^2=u*(u+2),
k^2=u^2-4.
```

Put

```text
x=(u+k)/2.
```

Then

```text
1/x=(u-k)/2
```

because `(u+k)(u-k)=4`, and define

```text
p=h*x/(x+1).
```

A direct calculation gives `p^2=1+x^2`. Thus, on the retained positive chamber,

```text
rational source quotient point
<=> h^2=u(u+2) and k^2=u^2-4.
```

This is the required rationality firewall. Dropping `(L)` enlarges the rational population and is not authorized for an `S34-W03` receiver-exclusion argument.

## 3. First hyperbola coordinate: alpha

From `Q1,Q2`,

```text
s^2-r^2 = u/(u+2) = (u/h)^2.
```

Define

```text
alpha = h*(s+r)/u.
```

Then automatically

```text
alpha^{-1}=h*(s-r)/u,
```

because the product is one. Therefore

```text
r = (u/(2h))*(alpha-alpha^{-1}),
s = (u/(2h))*(alpha+alpha^{-1}).
```

On the positive nondegenerate receiver, `r>0`, so `alpha!=1`; positivity also excludes `alpha=-1`.

Set

```text
C=(u+2)*r*s.
```

Then

```text
C = (u/4)*(alpha^2-alpha^{-2}).                      (A)
```

## 4. Second hyperbola coordinate: beta

Using `Q1,Q2`,

```text
R*(R+u)=(u+2)^2*r^2*s^2=C^2.
```

Hence `Q3` is exactly

```text
B^2-C^2=1.
```

Define

```text
beta=B+C.
```

Then

```text
beta^{-1}=B-C,
B=(beta+beta^{-1})/2,
C=(beta-beta^{-1})/2.                                (B)
```

Comparing `(A)` and `(B)` yields

```text
2*(beta-beta^{-1}) = u*(alpha^2-alpha^{-2}),
```

or, with `A=alpha^2`,

```text
u = 2*A*(beta^2-1)/(beta*(A^2-1)).                   (K1)
```

This use of hyperbola coordinates is not a reopening of the old standalone hyperbola route: the selected object is the exact rational-source lift together with the descended receiver.

## 5. Q4 becomes one Möbius square

From `Q1,Q2`,

```text
2R+u=(u+2)*(r^2+s^2).
```

Substituting the alpha/beta expressions into `Q4` and simplifying gives the exact identity

```text
b^2 = (A*beta+1)/(A+beta),    A=alpha^2.             (K2)
```

Thus the descended four-square receiver has a two-hyperbola Kummer presentation with one remaining Möbius square condition.

On the retained positive chamber all displayed denominators are nonzero: `u,h,b,beta,A^2-1,A+beta` are nonzero.

## 6. Rational source lift becomes a second Kummer square

Factor `u^2-4` using `(K1)`:

```text
u^2-4
 = 4*(beta-A)*(A*beta+1)*(A+beta)*(A*beta-1)
   / (beta^2*(A^2-1)^2).
```

Using `(K2)`, this becomes

```text
u^2-4
 = [ 2*b*(A+beta)/(beta*(A^2-1)) ]^2
   * (beta-A)*(A*beta-1).
```

Therefore the rational-lift condition `(L)` is equivalent to

```text
kappa^2=(beta-A)*(A*beta-1),                         (K3)
```

where

```text
kappa = k*beta*(A^2-1)/(2*b*(A+beta)).
```

This is the new exact receiver gate. A quotient `K0(Q)` point satisfying only `Q1--Q4` is not enough for rational-source credit; the `K3` square must also hold.

## 7. Fixed-alpha genus-one quartic

For fixed `A=alpha^2`, write

```text
t=b^2.
```

Solving `(K2)` for beta gives

```text
beta=(1-A*t)/(t-A).
```

Substitute into `(K3)` and set

```text
W=kappa*(t-A).
```

Then

```text
W^2 = (A^2+1-2*A*b^2)*(2*A-(A^2+1)*b^2).            (G_A)
```

This is a quartic in `b`. Its binary-quartic invariants may be written with

```text
C0=A^2+1,
D0=2*A,
```

as the palindromic quartic

```text
W^2=C0*D0*b^4-(C0^2+D0^2)*b^2+C0*D0.
```

The invariant combination

```text
4*I^3-J^2
 = 1728*A^2*(A-1)^8*(A+1)^8*(A^2+1)^2
```

is nonzero on the retained open `A!=0,±1`, so the generic fixed-`A` fiber is genus one. The absolute invariant ratio `J^2/I^3` is nonconstant in `A`, so this is again a moving genus-one family, not one fixed elliptic curve.

Accordingly `S31-W01` is only a fixed-fiber birational router here; it gives no uniform Mordell-Weil or global closure.

## 8. Arsenal routing and firewalls

`S34-W03` now has a sharper exact target:

```text
(K1) + (K2) + (K3) + quotient-base/source conditions.
```

Any local/global exclusion must test this joint rational-source receiver, not the larger fixed-field quotient receiver with `(K3)` omitted.

`S34-W02` remains locked because no full Mordell-Weil group is certified uniformly over the moving parameter.

The old 35EX-19 lesson remains active: a genus-one fiber with a moving parameter is not a fixed-curve closure theorem. No exact equivalence with the 35EX-19 quartic is claimed here.

## 9. Result

```text
RATIONAL_SOURCE_LIFT_DISCRIMINANT_REQUIRED=true
RATIONAL_SOURCE_LIFT_IFF_H_AND_K_SQUARES=true
DESCENDED_KUMMER_NORMAL_FORM_EXACT=true
Q4_MOBIUS_SQUARE_EXACT=true
SOURCE_LIFT_SECOND_KUMMER_SQUARE_EXACT=true
FIXED_ALPHA_GENUS_ONE_QUARTIC_EXACT=true
FIXED_ALPHA_GENERIC_SMOOTH=true
FIXED_ALPHA_FAMILY_NONISOTRIVIAL=true
S34_W03_ROUTER_SHARPENED=true
S31_W01_FIXED_FIBER_ROUTER_ONLY=true
RECEIVER_INTERSECTION_CLOSED=false
E1_PROVED=false
STAGE35_CLOSED=false
```

Because this introduces a materially new rational-source Kummer receiver, a fresh breadth audit is required after hostile PASS before selecting another successor.
