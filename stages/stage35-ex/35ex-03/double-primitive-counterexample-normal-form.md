# Stage35-EX 35EX-03 — double primitive Pythagorean counterexample normal form

This leaf assumes the exact lemmas of 35EX-02 and asks only:

> What must an E1 counterexample look like after all forced gcds are removed?

No counterexample is assumed to exist outside this conditional derivation.

## 1. Canonical factors from 35EX-02

Use

```text
c = gcd(U1,U2),
p = gcd(W1,V2),
q = gcd(V1,V2),
```

so that

```text
g0 = c*p,
h  = c*q,
gcd(c,p)=gcd(c,q)=gcd(p,q)=1,
c,p odd.
```

The reduced E1 legs are

```text
xi  = (W1/p)*(U2/c),
eta = (U1/c)*(V2/p).
```

The reduced Master legs are

```text
A = (V1/q)*(U2/c),
B = (U1/c)*(V2/q).
```

## 2. E1-counterexample triple

Assume, for contradiction, that the Master-Hit violates E1:

```text
xi^2 + eta^2 = w^2.
```

Because `gcd(xi,eta)=1`, `xi` is odd and `eta` is even, the primitive Pythagorean-triple theorem gives coprime integers

```text
r > s > 0,
gcd(r,s)=1,
r-s odd,
```

such that

```text
(E1-odd)   (W1/p)*(U2/c) = r^2-s^2,
(E1-even)  (U1/c)*(V2/p) = 2*r*s,
(E1-hyp)   w = r^2+s^2.
```

Thus E1 failure is not merely another square condition: after canonical gcd removal it is a primitive triple with fixed odd/even orientation.

## 3. Master-Hit triple has exactly two 2-adic branches

Let

```text
k1=v2(V1),
k2=v2(V2).
```

35EX-02 proves `k1!=k2`.

### Branch L: k1 < k2

Here `A` is odd and `B` is even. Therefore there are coprime

```text
u > v > 0,
gcd(u,v)=1,
u-v odd,
```

with

```text
(M-L-odd)   (V1/q)*(U2/c) = u^2-v^2,
(M-L-even)  (U1/c)*(V2/q) = 2*u*v.
```

Comparing the common raw factor `U1*V2` in the E1-even and Master-even equations gives

```text
eta/B = q/p,
```

hence the exact cross-equation

```text
(L-cross)  p*r*s = q*u*v.
```

Because `gcd(p,q)=1`, this immediately implies

```text
q | r*s,
p | u*v.
```

Since each of `(r,s)` and `(u,v)` is coprime, every prime-power component of `q` is forced wholly into one of `r,s`, and every prime-power component of `p` wholly into one of `u,v`.

### Branch R: k1 > k2

Here `A` is even and `B` is odd. Thus there are coprime `u>v>0` of opposite parity with

```text
(M-R-even)  (V1/q)*(U2/c) = 2*u*v,
(M-R-odd)   (U1/c)*(V2/q) = u^2-v^2.
```

Again `eta/B=q/p`, now giving

```text
(R-cross)  2*p*r*s = q*(u^2-v^2).
```

The odd part of `q` therefore divides `r*s`; more precisely, after writing

```text
q = 2^k2 * q_odd,
```

we have

```text
q_odd | r*s.
```

All odd prime-power components of `q_odd` are again assigned wholly to `r` or to `s`.

## 4. Exact ratio identity shared by both branches

The E1 and Master leg ratios satisfy identically

```text
(eta/xi) / (B/A) = V1/W1.
```

Since

```text
V1/W1 = 2ab/(a^2+b^2),
```

this couples the two primitive triples back to the original first Euclid pair rather than leaving two independent Pythagorean parametrizations.

Explicitly:

Branch L:

```text
[2rs/(r^2-s^2)] * [(u^2-v^2)/(2uv)] = V1/W1.
```

Branch R:

```text
[2rs/(r^2-s^2)] * [(2uv)/(u^2-v^2)] = V1/W1.
```

## 5. What has been reduced

Any E1 counterexample must now lie in exactly one of two explicit systems:

```text
L: k1<k2, E1 primitive triple + Master primitive triple + p*r*s=q*u*v,
R: k1>k2, E1 primitive triple + Master primitive triple + 2*p*r*s=q*(u^2-v^2),
```

with `c,p,q` pairwise coprime and the original Euclid-pair coprimality/parity constraints still active.

This is the next attack surface. 35EX-04 should determine whether the prime-power allocation forced by `p,q` yields a genuine descent/local contradiction or is merely a repackaging of the original square equations.

## Credit boundary

This is a conditional normal-form reduction only. It proves neither E1 nor perfect-cuboid nonexistence and does not close `R29-PESCH-E1`.
