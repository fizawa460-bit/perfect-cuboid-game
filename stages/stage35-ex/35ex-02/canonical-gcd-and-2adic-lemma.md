# Stage35-EX 35EX-02 — canonical gcd split and Master 2-adic dichotomy

## Setup

For an admissible master tuple use

```text
U1=a^2-b^2,  V1=2ab,  W1=a^2+b^2,
U2=m^2-n^2,  V2=2mn,  W2=m^2+n^2,
```

with `gcd(a,b)=gcd(m,n)=1` and each pair of opposite parity. Hence each Euclid triple is primitive:

```text
gcd(Ui,Vi)=gcd(Ui,Wi)=gcd(Vi,Wi)=1,
Ui,Wi odd, Vi even.
```

Define three cross-gcd components

```text
c = gcd(U1,U2),
p = gcd(W1,V2),
q = gcd(V1,V2).
```

Also define

```text
g0 = gcd(W1*U2, U1*V2),
h  = gcd(V1*U2, U1*V2).
```

`g0` is the canonical E1 gcd. `h` is the gcd of the two legs in the Master square condition.

## Lemma 35EX-02A — exact gcd factorization

We have

```text
g0 = c*p,
h  = c*q.
```

Moreover `c,p,q` are pairwise coprime, and `c,p` are odd.

### Proof

Fix a prime `ell`.

For `g0=gcd(W1*U2,U1*V2)`, primitivity gives

```text
gcd(W1,U1)=1,
gcd(U2,V2)=1.
```

Therefore a prime common to `W1*U2` and `U1*V2` can only cross from `W1` to `V2`, or from `U2` to `U1`. Primewise the two possibilities contribute

```text
min(v_ell(W1),v_ell(V2)) + min(v_ell(U2),v_ell(U1)),
```

which is exactly `v_ell(p)+v_ell(c)`. Hence `g0=cp`.

The same argument for

```text
h=gcd(V1*U2,U1*V2)
```

uses `gcd(V1,U1)=1` and `gcd(U2,V2)=1`, leaving only the cross pairs `(V1,V2)` and `(U2,U1)`. Thus `h=cq`.

For pairwise coprimality:

- a prime dividing both `c` and `p` would divide both `U1` and `W1`;
- a prime dividing both `c` and `q` would divide both `U2` and `V2`;
- a prime dividing both `p` and `q` would divide both `W1` and `V1`.

Each is impossible by primitivity. Finally `c` divides odd `U1,U2` and `p` divides odd `W1`, so `c,p` are odd. QED.

## Lemma 35EX-02B — Master-Hit 2-adic dichotomy

Assume the tuple is a Master-Hit, so

```text
M=(V1*U2)^2+(U1*V2)^2 = square.
```

Let

```text
A = (V1*U2)/h = (V1/q)*(U2/c),
B = (U1*V2)/h = (U1/c)*(V2/q).
```

Then `gcd(A,B)=1` and `A^2+B^2` is a square. If

```text
k1=v2(V1),  k2=v2(V2),
```

then necessarily

```text
k1 != k2.
```

More precisely:

```text
k1 < k2  => A odd,  B even,
k1 > k2  => A even, B odd.
```

### Proof

Because `h` is exactly the gcd of the two raw Master legs, `gcd(A,B)=1`; dividing the square `M` by `h^2` gives a primitive Pythagorean triple.

The factor `c` is odd and

```text
v2(q)=min(k1,k2).
```

Hence

```text
v2(A)=k1-min(k1,k2),
v2(B)=k2-min(k1,k2).
```

If `k1=k2`, both `A` and `B` are odd, so

```text
A^2+B^2 = 1+1 = 2 (mod 4),
```

which cannot be a square. Therefore `k1!=k2`, and the displayed parity branches follow immediately. QED.

## E1 normalization unlocked by the lemma

Because `g0=cp` is odd, the canonical E1 pair is now exactly

```text
xi  = (W1/p)*(U2/c)   [odd],
eta = (U1/c)*(V2/p)   [even],
gcd(xi,eta)=1.
```

Thus any hypothetical E1 counterexample is automatically a **primitive** Pythagorean triple with fixed odd/even orientation. This is the input for 35EX-03.

## Credit boundary

These are elementary exact deductions from the master-tuple hypotheses. They are provisional Stage35-EX lemmas pending hostile audit. They do not prove E1 and grant no receiver or endpoint credit.
