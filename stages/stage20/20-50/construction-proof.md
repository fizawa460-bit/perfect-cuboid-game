# Stage20-50a — explicit primitive Euler-brick construction

## Goal
Produce a quantitative lower bound for the audited Stage20 population

```text
0<a<b<c,
gcd(a,b,c)=1,
R=sqrt(a^2+b^2+c^2)<=B,
all three face diagonals integral,
space diagonal integrality not required.
```

The starting identity is the classical Saunderson/Sounderson Euler-brick construction, also recorded as Corollary 3 in Djamel Himane, *Primitive Euler brick generator* (arXiv:2405.13061). The Stage20 adaptation below is proved directly and does not rely on a bounded-height claim from that paper.

## 1. One-parameter primitive Pythagorean input
For every even integer `m>=10`, put

```text
u=m^2-1,
v=2m,
w=m^2+1.
```

Then `u^2+v^2=w^2`, `gcd(u,v,w)=1`, `u,w` are odd and `v` is even.

Define

```text
A = u |4v^2-w^2|,
B = v |4u^2-w^2|,
C = 4uvw.
```

For `m>=10` the signs are fixed and

```text
A=(m^2-1)(m^4-14m^2+1)
 =m^6-15m^4+15m^2-1,
B=2m(3m^4-10m^2+3),
C=8m(m^4-1).
```

All are positive.

## 2. Three face diagonals are integral
Using `u^2+v^2=w^2`,

```text
A^2+B^2
 =u^2(4v^2-w^2)^2+v^2(4u^2-w^2)^2
 =w^6,
```

so the first face diagonal is `w^3`.

Also

```text
A^2+C^2
 =u^2[(4v^2-w^2)^2+16v^2w^2]
 =u^2(4v^2+w^2)^2,
```

and similarly

```text
B^2+C^2
 =v^2(4u^2+w^2)^2.
```

Thus `(A,B,C)` is an Euler brick for every even `m>=10`.

## 3. Primitivity
Suppose a prime `p` divides `A,B,C`.

`p=2` is impossible because `u,w` are odd, `v` is even, and `4v^2-w^2` is odd, hence `A` is odd.

Let `p` be odd. Since `p|C=4uvw`, it divides one of the pairwise coprime integers `u,v,w`.

- If `p|u`, then `B=v(4u^2-w^2) == -v w^2 (mod p)`, nonzero.
- If `p|v`, then `A=u(4v^2-w^2) == -u w^2 (mod p)`, nonzero.
- If `p|w`, then `A == 4u v^2 (mod p)`, nonzero.

Contradiction in every case. Hence

```text
gcd(A,B,C)=1.
```

No post-hoc primitive reduction is needed.

## 4. Canonical ordering and injectivity
For `m>=10`,

```text
C-B = 2m^5+20m^3-14m > 0,
```

so `B<C`.

Furthermore

```text
A-C
 =m^4(m^2-8m-15)+15m^2+8m-1 >0,
```

and

```text
A-B
 =m^4(m^2-6m-15)+20m^3+15m^2-6m-1 >0.
```

Thus the canonical order is exactly

```text
0<B<C<A.
```

The largest edge

```text
A(m)=m^6-15m^4+15m^2-1
```

is strictly increasing for `m>=10`, because

```text
A'(m)=6m(m^4-10m^2+5)>0.
```

Therefore distinct allowed `m` give distinct canonical primitive Stage20 objects.

## 5. Common R-cutoff
Crude uniform bounds for `m>=10` are enough:

```text
u<m^2,
v=2m,
w<2m^2,
A<20m^6,
B<16m^6,
C<16m^6.
```

Hence

```text
R=sqrt(A^2+B^2+C^2)
 < sqrt(20^2+16^2+16^2) m^6
 = sqrt(912)m^6
 <31m^6.
```

So every even `m>=10` with

```text
m <= (B/31)^(1/6)
```

produces a distinct Stage20 object counted by `M_3(B)`.

Consequently, for all sufficiently large `B`,

```text
M_3(B) >= floor((B/31)^(1/6)/2)-4,
```

and therefore

```text
M_3(B) >> B^(1/6).
```

## 6. Boundary
This construction proves infinitude and a positive-power lower bound only. It does not match the Stage14-e8 upper envelope `M_3(B)=B^(1+o(1))`, identify the true exponent, prove an asymptotic, or impose an integral space diagonal.
