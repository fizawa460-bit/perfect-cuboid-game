# Stage35-EX 35EX-06A — exact four-factor gcd support

## Scope

Assume the conditional E1-counterexample normal form of 35EX-03 and the four-factor square identities of 35EX-05. This leaf determines exactly where a prime common to two factor-square terms can come from. It does not prove E1.

## Branch L

Write

```text
L1 = r*u+s*v,
L2 = r*v-s*u,
L3 = r*u-s*v,
L4 = r*v+s*u,
```

with

```text
gcd(r,s)=gcd(u,v)=1,
r-s odd,
u-v odd.
```

For odd-prime support define

```text
Gplus  = gcd(r^2+s^2, u^2+v^2),
Gminus = gcd(r^2-s^2, u^2-v^2),
C13    = gcd(r,v)*gcd(s,u),
C24    = gcd(r,u)*gcd(s,v).
```

The six pairwise gcds satisfy

```text
gcd(L1,L2) | Gplus,
gcd(L3,L4) | Gplus,
gcd(L1,L4) | Gminus,
gcd(L2,L3) | Gminus,
oddpart(gcd(L1,L3)) = oddpart(C13),
oddpart(gcd(L2,L4)) = oddpart(C24).
```

The first four divisibilities follow from the determinant combinations

```text
u*L1+v*L2 = r*(u^2+v^2),
v*L1-u*L2 = s*(u^2+v^2),
r*L1-s*L2 = u*(r^2+s^2),
s*L1+r*L2 = v*(r^2+s^2),

u*L1-v*L4 = r*(u^2-v^2),
v*L1-u*L4 = -s*(u^2-v^2),
r*L1-s*L4 = u*(r^2-s^2),
s*L1-r*L4 = -v*(r^2-s^2),
```

and the analogous sign-swapped identities for `(L3,L4)` and `(L2,L3)`.

For the same-coordinate pairs, if `X=ru` and `Y=sv`, then

```text
gcd(X+Y,X-Y) / gcd(X,Y) | 2.
```

Because `gcd(r,s)=gcd(u,v)=1`,

```text
gcd(ru,sv)=gcd(r,v)*gcd(s,u),
gcd(rv,su)=gcd(r,u)*gcd(s,v),
```

which proves the displayed odd-part equalities.

### Branch-L dynamic difference reservoir

The branch equations give

```text
r^2-s^2 = (W1/p)*(U2/c),
u^2-v^2 = (V1/q)*(U2/c).
```

Since `gcd(W1/p,V1/q)=1`,

```text
Gminus = U2/c.
```

Thus the pairwise gcd support is not confined to a fixed coefficient set: the live quantity `U2/c` is an exact odd-prime reservoir for the `(L1,L4)` and `(L2,L3)` pairs.

### Branch-L 2-adic part

Let

```text
k1=v2(V1), k2=v2(V2), k1<k2.
```

From the primitive E1 and Master even legs,

```text
v2(r*s)=k2-1,
v2(u*v)=k2-k1-1.
```

Hence the even parameter among `(r,s)` has strictly larger 2-adic valuation than the even parameter among `(u,v)`. Exactly one of the pairs

```text
(L1,L3), (L2,L4)
```

is even, and each member of that even pair has exact valuation

```text
v2 = k2-k1-1.
```

The other same-coordinate pair is odd, and every cross pair consists of one odd and one even factor. Therefore the total 2-adic valuation of

```text
L1*L2*L3*L4
```

is automatically

```text
2*(k2-k1-1),
```

so Branch L creates no additional 2-adic squareclass obstruction.

## Branch R

Set

```text
x=u-v,
y=u+v.
```

Because `u,v` are coprime and of opposite parity,

```text
x,y are odd, gcd(x,y)=1.
```

The four factors are

```text
R1 = r*x-s*y,
R2 = r*y+s*x,
R3 = r*x+s*y,
R4 = r*y-s*x.
```

This is the same bilinear pattern as Branch L, with `(u,v)` replaced by `(x,y)` and a permutation of factor labels. Define

```text
Hplus  = gcd(r^2+s^2, x^2+y^2),
Hminus = gcd(r^2-s^2, x^2-y^2),
D13    = gcd(r,y)*gcd(s,x),
D24    = gcd(r,x)*gcd(s,y).
```

Then

```text
gcd(R1,R2) | Hplus,
gcd(R3,R4) | Hplus,
gcd(R1,R4) | Hminus,
gcd(R2,R3) | Hminus,
gcd(R1,R3) = D13,
gcd(R2,R4) = D24,
```

where the last two equalities are exact because all quantities involved are odd.

Moreover

```text
x^2+y^2 = 2*(u^2+v^2),
x^2-y^2 = -4*u*v.
```

So the odd-prime reservoirs are equivalently

```text
oddpart(Hplus)  = oddpart(gcd(r^2+s^2, u^2+v^2)),
oddpart(Hminus) = oddpart(gcd(r^2-s^2, u*v)),
```

together with the live cross-gcd products `D13,D24`.

Every `Ri` is odd, since `(r,s)` have opposite parity while `x,y` are odd. Thus Branch R has no 2-adic factor-square support at all.

## Exact consequence

The four-factor square condition has now been separated into:

1. a completely controlled 2-adic part;
2. odd-prime sharing through live reservoirs `Gplus`, `U2/c`, `C13`, `C24` in Branch L;
3. odd-prime sharing through live reservoirs `Hplus`, `Hminus`, `D13`, `D24` in Branch R.

This is sufficient to test the Stage34 weapon contract in the next subleaf. No finite squareclass family is asserted here.

## Credit boundary

```text
PAIRWISE_GCD_SUPPORT_DERIVED=true
TWO_ADIC_SUPPORT_DERIVED=true
FINITE_SQUARECLASS_REDUCTION_PROVED=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
