# Stage35-EX 35EX-26 — exact base-involution receiver descent

Status: `PROVISIONAL_EXACT_BASE_INVOLUTION_RECEIVER_DESCENT_NO_CREDIT`

This unit starts only after the post-35EX-25 fresh breadth audit.  It does not claim E1, Stage35, or perfect-cuboid closure.

## 1. Audited input

Work on the positive nondegenerate Stage35-EX chamber over

```text
K = Q(x,p),    p^2 = 1+x^2,    a=x^2,
```

with the 35EX-25 exact receiver

```text
Eplus_a : Y^2=(X+1)(X+a)(X+1+a),
X, X+1, X+a, X+1+a all squares in K.
```

Equivalently there are `y,q,z,w` with

```text
X=y^2,
q^2=X+1,
z^2=X+a,
w^2=X+1+a,
Y=q*z*w.
```

The source involution is

```text
sigma(x)=1/x,
sigma(p)=p/x,
sigma(a)=1/a.
```

It has order two because `p^2=1+x^2` is preserved.

## 2. Exact semilinear self-equivalence of Eplus

Define

```text
X' = X/a = X/x^2,
Y' = Y/x^3.
```

Then

```text
(Y')^2
 = Y^2/x^6
 = (X'+1)(X'+1/a)(X'+1+1/a).
```

Thus the fiber at `a` is carried exactly to the fiber at `1/a`.

The four square conditions are preserved and permuted:

```text
X'             = X/a,
X'+1           = (X+a)/a,
X'+1/a         = (X+1)/a,
X'+1+1/a       = (X+1+a)/a.
```

Because `a=x^2` is already a square, the four-square locus is invariant.

On square roots one may take

```text
sigma_receiver:
(y,q,z,w) -> (y/x, z/x, q/x, w/x).
```

Applying this twice gives the identity.  In particular this is a symmetry of the *full receiver lift*, not merely of the j-invariant.

## 3. Fixed field of the source involution

Set

```text
u = x + 1/x,
h = p*(x+1)/x.
```

Both are sigma-invariant, and

```text
h^2 = u*(u+2).
```

Conversely

```text
x^2-u*x+1=0,
p=h*x/(x+1).
```

Hence, on the retained positive chamber (`x>0`, so `x+1!=0`),

```text
K0 := K^sigma = Q(u,h),
h^2=u(u+2),
K=K0(x),  x^2-u*x+1=0.
```

The quotient base is therefore again a rational conic.  The involution identifies reciprocal source fibers but does not make the base zero-dimensional.

## 4. Descended elliptic model

Define sigma-invariant coordinates

```text
R = X/x,
V = Y/(x*(x+1)).
```

Using `(x+1)^2=x(u+2)`, one obtains

```text
D_u : (u+2)*V^2 = (R+u)*(R^2+u*R+1).
```

This equation has coefficients in `Q(u)` and hence in `K0`.

The descended family is still nonisotrivial.  Since the original

```text
j(Eplus_a)=256*(a^2-a+1)^3/(a^2*(a-1)^2)
```

and `a+1/a=u^2-2`, the quotient-family invariant is

```text
j(D_u)=256*(u^2-3)^3/(u^2-4),
```

which is nonconstant in `u`.

Therefore the base involution does **not** reduce the receiver to one fixed elliptic curve or one fixed Mordell-Weil computation.

## 5. Exact descended full-square receiver

The full receiver can be descended, not only the elliptic equation.  Define

```text
r = y/(x+1),
s = w/(x+1),
B = q*z/x,
b = (q+z)/(x+1).
```

All four quantities are sigma-invariant.  They satisfy

```text
R = (u+2)*r^2,                                      (Q1)
R+u = (u+2)*s^2,                                    (Q2)
B^2 = R^2+u*R+1,                                    (Q3)
b^2 = (2*R+u+2*B)/(u+2),                            (Q4)
V = B*s.                                             (Q5)
```

Together with

```text
h^2=u(u+2),
D_u : (u+2)V^2=(R+u)(R^2+uR+1),
```

these equations define the descended receiver on the retained chamber.

### Forward verification

`Q1` and `Q2` use `(x+1)^2=x(u+2)`:

```text
R=X/x=y^2/x=(u+2)r^2,
R+u=(X+1+x^2)/x=(u+2)s^2.
```

For `Q3`,

```text
(qz/x)^2=((X+1)(X+x^2))/x^2=R^2+uR+1.
```

For `Q4`,

```text
(q+z)^2
 = q^2+z^2+2qz
 = x*(2R+u+2B),
```

and division by `(x+1)^2=x(u+2)` gives the result.

Finally `V=Y/(x(x+1))=(qz/x)*(w/(x+1))=B*s`.

## 6. Converse reconstruction

Assume a `K0`-point satisfies the quotient-base equation and `Q1`--`Q4`.  Extend to `K` by choosing the retained root `x` of

```text
x^2-u*x+1=0
```

and recover

```text
p=h*x/(x+1),
X=R*x,
y=r*(x+1),
w=s*(x+1).
```

Then `y^2=X` and `w^2=X+1+x^2` follow from `Q1,Q2`.

Set

```text
q+z = b*(x+1),
q*z = B*x.
```

The discriminant of this quadratic pair is

```text
Delta = b^2*(x+1)^2 - 4*B*x
      = x*(2R+u-2B).
```

From `Q3,Q4`,

```text
(2R+u+2B)(2R+u-2B)=u^2-4,
```

so

```text
2R+u-2B = (u-2)/b^2.
```

Because

```text
x*(u-2)=(x-1)^2,
```

we get

```text
Delta=((x-1)/b)^2.
```

To preserve the original names `q^2=X+1` and `z^2=X+x^2`, take

```text
q = ( b*(x+1) - (x-1)/b )/2,
z = ( b*(x+1) + (x-1)/b )/2.
```

Then `q+z` and `q*z` are the prescribed values and

```text
q^2-z^2=1-x^2,
q^2+z^2=2X+1+x^2,
```

so exactly

```text
q^2=X+1,
z^2=X+x^2.
```

On the positive Stage35-EX chamber the denominators `x`, `x+1`, `u+2`, and `b` are nonzero.  The fixed locus `x=1` is included: then the discriminant is zero and the reconstruction has `q=z`; no division by `x-1` is used.

Thus the original four-square receiver and the quotient receiver are exact mutually reconstructible descriptions on the retained chamber.

## 7. What this does and does not buy

The descent is genuine:

```text
BASE_INVOLUTION_FULL_RECEIVER_EQUIVARIANT=true
FIXED_FIELD_QUOTIENT_CONIC_EXACT=true
DESCENDED_ELLIPTIC_MODEL_EXACT=true
DESCENDED_FULL_SQUARE_RECEIVER_IFF=true
RECIPROCAL_SOURCE_FIBERS_IDENTIFIED=true
```

But it is not a closure theorem:

```text
QUOTIENT_BASE_DIMENSION=1
DESCENDED_J_NONCONSTANT=true
FIXED_ELLIPTIC_CURVE_REDUCTION=false
UNIFORM_MW_CLOSURE=false
DESCENDED_RECEIVER_EMPTY=false
E1_PROVED=false
STAGE35_CLOSED=false
```

The legal next arithmetic question, after hostile audit and the required successor protocol, is whether the *descended receiver intersection* can be excluded directly (for example by `S34-W03`-style joint local/global tests).  Symmetry alone supplies no emptiness statement.
