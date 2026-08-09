# Stage14-4bc supplement — split-E density completion lemma

This note supplies the one-variable input used for a very-long reciprocal-active `E` vertex in the K5 bulk graph.

## Lemma

Let `chi` be a primitive real Dirichlet character of odd conductor `q`. Define

```text
b(n)
 = mu(n)^2
   * 1_{p|n => p=1 mod 4}
   * product_{p|n} (2p/(p+1)).
```

Then, uniformly for `x>=q`,

```text
sum_{n<=x} b(n) chi(n)
 <<_epsilon (xq)^(1/2) (xq)^epsilon.
```

Consequently, for split odd squarefree `n`,

```text
lambda_E(n)=product_{p|n} 2/(p+1)=b(n)/n,
```

and partial summation gives for every dyadic `N>=q`

```text
sum_{n~N} lambda_E(n) chi(n)
 <<_epsilon N^(-1/2) q^(1/2) (Nq)^epsilon.
```

The same bound survives finitely many fixed mod-4/mod-8 and coprimality restrictions at `B^epsilon` cost.

## Proof

Put `chi4` for the primitive character modulo `4`. The Dirichlet series

```text
F(s)=sum_n b(n)chi(n)n^(-s)
```

has Euler factors

```text
p=1 mod 4:
1 + (2p/(p+1))*chi(p)*p^(-s),

p=3 mod 4:
1.
```

Compare with

```text
L(s,chi)L(s,chi*chi4).
```

At a prime `p=1 mod 4`, its local expansion is

```text
1 + 2 chi(p)p^(-s) + O(p^(-2 Re(s))),
```

while

```text
2p/(p+1)=2+O(1/p).
```

At a prime `p=3 mod 4`, the linear terms of the two L-factors cancel and their product is

```text
1+O(p^(-2 Re(s))).
```

Therefore

```text
F(s)=L(s,chi)L(s,chi*chi4)G(s),
```

where the Euler product `G` is absolutely convergent in every half-plane

```text
Re(s)>1/2+epsilon.
```

Equivalently, at coefficient level,

```text
b(n)chi(n)
 = (chi * (chi*chi4) * g)(n)
```

with

```text
sum_n |g(n)|/n^(1/2+epsilon) < infinity.
```

Let

```text
C(T)=sum_{ab<=T} chi(a)(chi*chi4)(b).
```

For `T>=q`, Dirichlet hyperbola with the splitting point `sqrt(T)` and the Pólya--Vinogradov bound for both characters gives

```text
C(T) << sqrt(Tq) log(2q).
```

Indeed the two hyperbola sums each contain `O(sqrt(T))` incomplete character sums of size `O(sqrt(q)log(2q))`; the overlap term is `O(q log(2q)^2)` and is absorbed because `T>=q`.

Now

```text
sum_{n<=x} b(n)chi(n)
 = sum_{d<=x} g(d) C(x/d).
```

Split at `d=x/q`.

For `d<=x/q`, `x/d>=q`, so

```text
sum_{d<=x/q} |g(d)| |C(x/d)|
 << sqrt(xq) log(2q)
    * sum_d |g(d)|/sqrt(d)
 <<_epsilon sqrt(xq)(xq)^epsilon.
```

For `d>x/q`, use the trivial `|C(x/d)|<=x/d`. Absolute convergence of `G` at `1/2+epsilon` gives

```text
x * sum_{d>x/q} |g(d)|/d
 <<_epsilon
 x*(x/q)^(-1/2+epsilon)
 <<_epsilon
 sqrt(xq)(xq)^epsilon.
```

This proves the partial-sum lemma. The dyadic `lambda_E` estimate follows by Abel/partial summation because `lambda_E(n)=b(n)/n` on the split squarefree support.

## K5 consequence

In the no-long-long-edge case of Stage14-4bc, a reciprocal-active E vertex has at most four linear neighbors. If

```text
V>=M^(6 eta),
```

all neighbors are `<M^eta`, hence their product conductor satisfies

```text
q <= M^(4 eta).
```

The lemma gives the relative bulk saving

```text
V^(-1/2) q^(1/2)
 <= M^(-3 eta) M^(2 eta)
 = M^(-eta).
```

With `eta=1/100` this is `M^(-1/100+epsilon)`, stronger than the K5 long-long saving `M^(-1/200+epsilon)`.

If no E vertex reaches `M^(6eta)` and no linear vertex reaches the s5o very-long threshold `M^(4eta)`, the total active modulus product is at most

```text
M^(4*4eta+6eta)=M^(22eta).
```

The same bound holds for the number of dyadic modulus tuples up to `M^o(1)`. Exact local centering and the periodic box estimate then give

```text
M^(1+44eta+o(1)) + M^(66eta+o(1)).
```

For `eta=1/100` these are `M^1.44` and `M^0.66`, both far below `M^2`.

Thus all K5 rank-one bulk cases are covered, with conservative worst saving `1/200`.