# Stage14-4bc supplement — split-E density completion lemma

This note supplies the one-variable input used in `14-4bc/result.md` when the reciprocal-active split-`E` vertex is very long but all of its linear neighbors are short.

It applies only to the **rank-one E-density bulk**.  The signed-root E discrepancy tensor is treated separately in the main 4bc result and is not estimated by this lemma.

## 1. Weighted split-squarefree coefficient

Let `chi_4` be the primitive real character modulo `4`. For odd squarefree `n` supported only on primes `p=1 mod 4`, the s5i E-density is

```text
lambda_E(n)=product_{p|n} 2/(p+1).
```

Define

```text
b(n)
 = mu(n)^2
   * 1_{p|n => p=1 mod 4}
   * product_{p|n} (2p/(p+1)).
```

Then on that support

```text
lambda_E(n)=b(n)/n.
```

## 2. Dirichlet-series factorization

Let `chi` be a primitive real Dirichlet character of odd conductor `q`. Put

```text
F(s)=sum_{n>=1} b(n)chi(n)n^(-s).
```

For `p=1 mod 4`, the local factor is

```text
1 + (2p/(p+1))*chi(p)*p^(-s).
```

For `p=3 mod 4`, it is `1`. At primes dividing the conductor, `chi(p)=0`, so the corresponding local factor is also `1`.

Compare this with

```text
L(s,chi)L(s,chi*chi_4).
```

For `p=1 mod 4`, away from the conductors,

```text
(1-chi(p)p^(-s))^(-2)
 = 1 + 2chi(p)p^(-s) + O(p^(-2 Re(s))),
```

while

```text
2p/(p+1)=2+O(1/p).
```

Hence the quotient local factor differs from `1` by

```text
O(p^(-1-Re(s)) + p^(-2 Re(s))).
```

For `p=3 mod 4`, the linear terms of the two L-factors cancel:

```text
(1-chi(p)p^(-s))^(-1)
(1+chi(p)p^(-s))^(-1)
 = 1 + O(p^(-2 Re(s))).
```

The prime `2` contributes only one fixed local factor. Therefore

```text
F(s)=L(s,chi)L(s,chi*chi_4)G(s),
```

where `G(s)` is absolutely convergent in every half-plane

```text
Re(s)>1/2+epsilon.
```

Write

```text
G(s)=sum_{d>=1} g(d)d^(-s).
```

Then for every `epsilon>0`,

```text
sum_d |g(d)|/d^(1/2+epsilon) < infinity.
```

At coefficient level,

```text
b(n)chi(n)
 = (chi * (chi*chi_4) * g)(n).
```

## 3. Hyperbola bound for the two-character convolution

Define

```text
C(T)=sum_{ab<=T} chi(a)(chi*chi_4)(b).
```

Both characters have conductor `O(q)`. Pólya--Vinogradov gives

```text
max_X |sum_{n<=X} chi(n)|
 + max_X |sum_{n<=X} (chi*chi_4)(n)|
 << sqrt(q) log(2q).
```

Use Dirichlet hyperbola with splitting point `sqrt(T)`. Each of the two hyperbola sums has `O(sqrt(T))` bounded incomplete character sums, while the overlap is `O(q log(2q)^2)`. Hence, for `T>=q`,

```text
C(T) << sqrt(Tq) log(2q)^2.
```

The extra logarithm is harmless in every Stage14 `B^epsilon` budget.

## 4. Partial-sum bound for b(n)chi(n)

By convolution,

```text
sum_{n<=x} b(n)chi(n)
 = sum_{d<=x} g(d) C(x/d).
```

Assume `x>=q` and split at

```text
d0=x/q.
```

For `d<=d0`, we have `x/d>=q`, so the hyperbola estimate gives

```text
sum_{d<=d0} |g(d)| |C(x/d)|
 << sqrt(xq) log(2q)^2
    * sum_{d<=d0} |g(d)|/sqrt(d).
```

Absolute convergence of `G` at `1/2+epsilon` yields

```text
sum_{d<=d0}|g(d)|/sqrt(d)
 <<_epsilon d0^epsilon.
```

Thus this part is

```text
<<_epsilon sqrt(xq)(xq)^epsilon.
```

For `d>d0`, use the trivial bound `|C(x/d)|<=x/d`. Again by convergence at `1/2+epsilon`,

```text
sum_{d>d0}|g(d)|/d
 <<_epsilon d0^(-1/2+epsilon),
```

and therefore the tail is

```text
<<_epsilon
x*(x/q)^(-1/2+epsilon)
<<_epsilon sqrt(xq)(xq)^epsilon.
```

We have proved:

```text
boxed:
sum_{n<=x} b(n)chi(n)
 <<_epsilon (xq)^(1/2) (xq)^epsilon,
qquad x>=q.
```

The same estimate survives finitely many fixed coprimality or mod-4/mod-8 restrictions at `B^epsilon` cost.

## 5. Dyadic lambda_E consequence

Since `lambda_E(n)=b(n)/n` on the split squarefree support, Abel/partial summation gives, for every dyadic `N>=q`,

```text
boxed:
sum_{n~N} lambda_E(n)chi(n)
 <<_epsilon
 N^(-1/2) q^(1/2) (Nq)^epsilon.
```

This is the one-variable E-density completion used in the K5 bulk graph escape.

## 6. Stage14-4bc exponent consequence

Take the graph threshold

```text
eta=1/100.
```

Suppose there is no long-long reciprocal edge and the E vertex has size

```text
V>=M^(6eta).
```

The E vertex has at most four linear neighbors; each neighbor is `<M^eta`. Their product conductor therefore satisfies

```text
q<=M^(4eta).
```

The dyadic lemma gives the relative saving

```text
V^(-1/2)q^(1/2)
 <= M^(-3eta)M^(2eta)
 = M^(-eta)
 = M^(-1/100).
```

This is stronger than the long-long K5 graph saving `M^(-1/200)`.

If no linear active variable reaches `M^(4eta)` and the E variable is below `M^(6eta)`, the product of all five active moduli is at most

```text
M^(4*4eta+6eta)=M^(22eta).
```

The crude number of modulus tuples has the same exponent. Exact local centering plus the fixed-conductor periodic box estimate, with s5p auxiliary-energy multiplicity absorbed into `M^o(1)`, gives

```text
M^(1+44eta+o(1)) + M^(66eta+o(1))
 = M^(1.44+o(1)) + M^(0.66+o(1)),
```

well below the physical `M^2` scale.

Hence the rank-one K5 bulk sector is closed in every size configuration, with conservative worst saving `1/200`.