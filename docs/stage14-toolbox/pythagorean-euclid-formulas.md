# Stage14-toolbox — Pythagorean / Euclid conversion formula atlas

This module is a reusable lookup sheet for the merged Stage14 main/s Pythagorean geometry. It does not prove new Stage14 mathematics. Every formula below is extracted from merged s6-01, s6-06, s6-07, and s6-08 work.

## 1. Primitive Euclid core

For coprime integers

```text
m>n>0,
gcd(m,n)=1,
m,n of opposite parity,
```

define

```text
E = 2mn,
O = m^2-n^2 = (m-n)(m+n),
H = m^2+n^2.
```

Then

```text
E^2+O^2=H^2.
```

A primitive oriented Stage14 face `(S,X,H)` is obtained by choosing one orientation:

```text
even-S orientation:  (S,X,H)=(E,O,H),
odd-S orientation:   (S,X,H)=(O,E,H).
```

Do not write `S=2mn` until the orientation has been fixed.

The five standard odd-support factors are

```text
m,
n,
m-n,
m+n,
m^2+n^2.
```

In the even-S orientation these are exactly the historical s5 columns attached to

```text
S=2mn,
X=(m-n)(m+n),
H=m^2+n^2.
```

## 2. Uniform half-angle normalization

For any primitive oriented face `(S,X,H)` define `kappa in {1,2}` and positive half-angle integers `t_-`, `t_+` by

```text
H-S = kappa*t_-^2,
H+S = kappa*t_+^2.
```

Then exactly

```text
S = kappa*(t_+^2-t_-^2)/2,
X = kappa*t_-*t_+,
H = kappa*(t_+^2+t_-^2)/2.
```

The Euclid-to-half-angle conversion is

```text
if S=2mn:
    kappa=1,
    t_-=m-n,
    t_+=m+n;

if S=m^2-n^2:
    kappa=2,
    t_-=n,
    t_+=m.
```

At odd primes `t_-` and `t_+` are coprime. The `kappa` value carries the finite 2-adic orientation convention.

## 3. Two-face physical gluing

Let

```text
F1=(S,X,H),
F2=(S2,X2,H2)
```

be primitive oriented Pythagorean faces forming an actual physical Stage14 edge, and set

```text
g=gcd(S,S2).
```

The primitive-face scale factors into the actual cuboid are

```text
r1=S2/g,
r2=S/g.
```

Hence the actual cuboid edges are

```text
shared = S*S2/g,
other1 = X*S2/g,
other2 = X2*S/g,
```

and the two face diagonals are

```text
diag1=H*S2/g,
diag2=H2*S/g.
```

If `d` is the integer space diagonal and

```text
G=g*d,
```

then

```text
G^2 = H^2*S2^2 + S^2*X2^2
    = S^2*H2^2 + X^2*S2^2.
```

Equivalently,

```text
(H*S2)^2+(S*X2)^2=G^2.
```

This is the third-Pythagorean-triple identity used throughout the current main/s physical transfer.

## 4. Primitive third-face transfer

Set

```text
c=gcd(H,X2).
```

Merged s6-07 proves

```text
gcd(H*S2,S*X2)=g*c,
c|d.
```

Therefore

```text
S3=H*S2/(g*c),
X3=S*X2/(g*c),
H3=G/(g*c)=d/c
```

defines a primitive oriented Pythagorean face

```text
F3=(S3,X3,H3),
H3<=d.
```

The transfer keeps the original physical edge injectively. Recovery uses

```text
S/H = X3*S2/(S3*X2),
c=gcd(H,X2),
d=c*H3,
X=sqrt(H^2-S^2).
```

The transferred pair necessarily satisfies

```text
(S3*X2)^2-(X3*S2)^2 = nonzero square.
```

This square condition is necessary for a physical image; by itself it is not declared sufficient for arbitrary primitive `(F2,F3)` pairs.

## 5. Half-angle form of the transferred square

For `F2,F3`, write

```text
a=t_-(F2),
b=t_+(F2),
c=t_-(F3),
d=t_+(F3).
```

Then

```text
S2=kappa2*(b^2-a^2)/2,
X2=kappa2*a*b,
S3=kappa3*(d^2-c^2)/2,
X3=kappa3*c*d.
```

Define

```text
A0=a*b*(d^2-c^2),
C0=c*d*(b^2-a^2).
```

The exact factorization is

```text
A0-C0=(a*d-b*c)*(b*d+a*c),
A0+C0=(a*d+b*c)*(b*d-a*c),
```

hence

```text
Delta0=A0^2-C0^2
      =(a*d-b*c)(a*d+b*c)(b*d-a*c)(b*d+a*c).
```

For every transferred physical image, `Delta0` is a nonzero integer square. This is the canonical four-bilinear half-angle form used after s6-08.

## 6. Fast conversion chain

```text
primitive Euclid pair (m,n)
  -> E=2mn, O=m^2-n^2, H=m^2+n^2
  -> choose orientation (S,X,H)
  -> (kappa,t_-,t_+)
  -> glue F1,F2 with g=gcd(S,S2)
  -> G=g*d and third integral Pythagorean triple
  -> c=gcd(H,X2)
  -> primitive F3=(S3,X3,H3)
  -> half-angle pairs of F2,F3
  -> four-bilinear cross-square factorization
```

## 7. Safety locks

- Orientation is data. Never silently replace `S` by the even leg.
- The two `kappa` values are not cosmetic; they encode the 2-adic orientation normalization.
- Primitive reduction by `g*c` is part of the third-face formula.
- The `(F2,F3)` square relation is a necessary physical-image condition, not a free converse theorem.
- `Delta0=square` is an exact reformulation on the transferred physical image; it does not make every formal half-angle quadruple physical.
- Historical letters `a,b,c,d` collide with other Stage14 modules. Outside the local formula display, prefer `t2-`, `t2+`, `t3-`, `t3+`.
