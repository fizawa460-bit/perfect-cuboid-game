# Stage35-EX 35EX-07A — dynamic odd-prime reservoirs collapse to one moving squareclass

## Scope

Assume the conditional E1-counterexample normal form of 35EX-03, the additive factor identities of 35EX-05, and the pairwise gcd support of 35EX-06. This leaf asks whether the four-factor receiver actually acquires a fixed finite squareclass support as required by `S34-W01`.

It does not prove E1.

## Branch L

Put

```text
T = U2/c.
```

From

```text
p*r*s = q*u*v,
gcd(p,q)=1,
```

we have `q|rs`, `p|uv` and hence an integer

```text
t = r*s/q = u*v/p.
```

The branch even-leg equation gives equivalently

```text
2*p*q*t = (U1/c)*V2,
```

so

```text
t = (U1/c)*V2/(2*p*q).
```

Because `gcd(U1/c,U2/c)=1` and `gcd(U2,V2)=1`, while `T` is odd,

```text
gcd(t,T)=1.
```

### Exact collapse of the cross reservoirs

Since `gcd(r,s)=gcd(u,v)=1`, every prime power common to `rs` and `uv` lies in exactly one of the four cross intersections. Therefore

```text
gcd(r,v)*gcd(s,u)*gcd(r,u)*gcd(s,v)
  = gcd(r*s,u*v)
  = t.
```

With the 35EX-06 notation

```text
C13 = gcd(r,v)*gcd(s,u),
C24 = gcd(r,u)*gcd(s,v),
```

this gives the exact identity

```text
C13*C24 = t,
gcd(C13,C24)=1.
```

Thus the two same-coordinate odd-prime reservoirs are not independent: together they are exactly the single moving factor `t`.

The difference reservoir was already exact in 35EX-06:

```text
Gminus = gcd(r^2-s^2,u^2-v^2) = T.
```

Hence all squareclass-relevant odd-prime sharing outside the common-hypotenuse channel is supported on the two coprime live factors

```text
t and T.
```

### The common-hypotenuse channel is pair-product square-neutral

Let an odd prime `ell` actually divide one of the common-hypotenuse pair gcds, i.e. `ell` divides both `L1,L2` or both `L3,L4`. Such an `ell` lies in

```text
Gplus = gcd(r^2+s^2,u^2+v^2).
```

No odd prime dividing `Gplus` divides `r*s*u*v`; no odd prime can divide both a primitive sum and difference of squares. Therefore

```text
gcd(Gplus,t*T)=1.
```

The additive identities of 35EX-05 and `uv=p*t` now become exactly

```text
L1*L2 = t*T*(a-b)^2,
L3*L4 = t*T*(a+b)^2.
```

Consequently any common-hypotenuse prime occurring in `L1,L2` or in `L3,L4` contributes an even total valuation to that pair. It can affect the individual factor gcd, but it contributes no new squareclass to the pair product.

### Exact Branch-L moving squareclass

Define

```text
dL = t*T.
```

Then

```text
L1*L2 = dL*(a-b)^2,
L3*L4 = dL*(a+b)^2,
gcd(t,T)=1,
```

and therefore

```text
L1*L2*L3*L4 = [dL*(a-b)*(a+b)]^2.
```

Equivalently, in rational squareclasses,

```text
[L1*L2] = [L3*L4] = [dL].
```

The four-factor square condition of 35EX-05 therefore does not produce a fixed coefficient squareclass: it carries the live squareclass

```text
dL = (U1*U2*V2)/(2*c^2*p*q).
```

The factor `c^2` is squareclass-trivial, but the remaining support is still parameter-dependent.

## Branch R

Again put

```text
T = U2/c,
x = u-v,
y = u+v.
```

Here `x,y` are odd and coprime. Since 35EX-04 proves `p | (u^2-v^2)=x*y`, define

```text
j = (u^2-v^2)/p = x*y/p.
```

The cross-equation

```text
2*p*r*s = q*(u^2-v^2)
```

becomes

```text
2*r*s = q*j.
```

Hence

```text
r*s = (q/2)*j,
x*y = p*j.
```

Since `p` is odd and `gcd(p,q)=1`,

```text
gcd(q/2,p)=1,
gcd(r*s,x*y)=j.
```

Therefore the exact Branch-R cross reservoirs satisfy

```text
D13*D24 = j,
gcd(D13,D24)=1.
```

The Master odd-leg equation gives

```text
j = (U1/c)*V2/(p*q).
```

As in Branch L,

```text
gcd(j,T)=1.
```

For the difference reservoir, 35EX-06 gives

```text
oddpart(Hminus) = oddpart(gcd(r^2-s^2,u*v)).
```

Using

```text
r^2-s^2 = (W1/p)*T,
2*u*v   = (V1/q)*T,
```

and `gcd(W1/p,V1/q)=1`, with `W1/p` odd, gives exactly

```text
oddpart(Hminus) = T.
```

The common-hypotenuse reservoir again satisfies

```text
gcd(oddpart(Hplus),j*T)=1,
```

and is pair-product square-neutral.

Finally the 35EX-05 identities divide by `p` to give

```text
R1*R2 = j*T*(a-b)^2,
R3*R4 = j*T*(a+b)^2.
```

Define

```text
dR = j*T.
```

Then

```text
[R1*R2] = [R3*R4] = [dR],
R1*R2*R3*R4 = [dR*(a-b)*(a+b)]^2,
```

with

```text
dR = (U1*U2*V2)/(c^2*p*q).
```

Again the squareclass is live and parameter-dependent.

## Consequence for S34-W01

The 35EX-06 reservoirs collapse substantially:

```text
Branch L:  moving support = t * T,
Branch R:  moving support = j * T,
```

with the two factors coprime in each branch. This is stronger than merely saying that several uncontrolled gcds remain.

However it also identifies the precise failure of the Stage34 finite-squareclass adapter. The 35EX-05 four-factor square is already explained by two pair products carrying the same moving squareclass `dL` or `dR`. No theorem currently bounds the odd-prime support of these moving squareclasses by a fixed finite coefficient set over all Master-Hits.

Therefore the legal conclusion is

```text
DYNAMIC_RESERVOIRS_COLLAPSED=true
MOVING_SQUARECLASS_IDENTIFIED=true
FIXED_FINITE_SQUARECLASS_SUPPORT_PROVED=false
S34_W01_FINITE_ENUMERATION_AUTHORIZED=false
```

This does not prove that a later argument cannot control `dL` or `dR`; it proves only that the present factor-square layer itself does not supply that control.

## Route decision

The finite Stage34 descent route is frozen at its exact missing theorem:

> prove a uniform fixed-support theorem for `dL` and `dR`, or prove that their prime allocations cancel after a stronger transformation.

Absent such a theorem, continuing to enumerate Stage34-style squareclasses would be non-exhaustive.

The next legal research leaf is to leave finite squareclass enumeration and test the previously unspent Gaussian compatibility route on the two simultaneous primitive Pythagorean triples.

```text
35EX-08_GAUSSIAN_DOUBLE_SQUARE_COMPATIBILITY
```

## Credit boundary

```text
MOVING_SQUARECLASS_COLLAPSE_PROVED_CONDITIONALLY=true
FINITE_SQUARECLASS_REDUCTION_PROVED=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
