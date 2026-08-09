# Stage14-4bc supplement — split-E density completion lemma

This note supplies the one-variable input used in `14-4bc/result.md` when the reciprocal-active split-`E` vertex is very long but all of its linear neighbors are short.

It applies only to the **rank-one E-density bulk**. The signed-root E discrepancy tensor is treated separately in the main 4bc result and is not estimated by this lemma.

## 1. Weighted split-squarefree coefficient

Let `chi_4` be the primitive real character modulo `4`. For odd squarefree `n` supported only on primes `p=1 mod 4`, the s5i E-density is

```text
lambda_E(n)=product_{p|n} 2/(p+1).
```

Define

```text
b(n)=mu(n)^2
    * 1_{p|n => p=1 mod 4}
    * product_{p|n} (2p/(p+1)).
```

Then `lambda_E(n)=b(n)/n` on this support.

## 2. Dirichlet-series factorization

Let `chi` be a primitive real Dirichlet character of odd conductor `q`. Put

```text
F(s)=sum_{n>=1} b(n)chi(n)n^(-s).
```

For `p=1 mod 4`, the local factor is

```text
1+(2p/(p+1))*chi(p)*p^(-s),
```

and for `p=3 mod 4` it is `1`. Comparing with

```text
L(s,chi)L(s,chi*chi_4)
```

shows that

```text
F(s)=L(s,chi)L(s,chi*chi_4)G(s),
```

where `G` is absolutely convergent in every half-plane `Re(s)>1/2+epsilon`. Indeed, at `p=1 mod 4` the quotient differs from `1` by `O(p^(-1-Re(s))+p^(-2Re(s)))`, while at `p=3 mod 4` the linear terms of the two L-factors cancel and the quotient differs from `1` by `O(p^(-2Re(s)))`.

Write

```text
G(s)=sum_{d>=1}g(d)d^(-s).
```

Then for every `epsilon>0`,

```text
sum_d |g(d)|/d^(1/2+epsilon)<infinity,
```

and coefficientwise

```text
b(n)chi(n)=(chi*(chi*chi_4)*g)(n).
```

## 3. Hyperbola bound

Define

```text
C(T)=sum_{ab<=T}chi(a)(chi*chi_4)(b).
```

Both characters have conductor `O(q)`. Pólya--Vinogradov and Dirichlet hyperbola give, for `T>=q`,

```text
C(T)<<sqrt(Tq)log(2q)^2.
```

The two hyperbola sums contain `O(sqrt(T))` incomplete character sums of size `O(sqrt(q)log(2q))`; the overlap is `O(q log(2q)^2)` and is absorbed when `T>=q`.

## 4. Partial sum for b(n)chi(n)

By convolution,

```text
sum_{n<=x}b(n)chi(n)=sum_{d<=x}g(d)C(x/d).
```

Assume `x>=q` and split at `d0=x/q`. For `d<=d0`, use the hyperbola estimate and absolute convergence of `G` at `1/2+epsilon`; for `d>d0`, use `|C(x/d)|<=x/d`. This yields

```text
boxed:
sum_{n<=x}b(n)chi(n)
 <<_epsilon (xq)^(1/2)(xq)^epsilon,
qquad x>=q.
```

Finitely many fixed coprimality or mod-4/mod-8 restrictions cost only `B^epsilon`.

## 5. Dyadic lambda_E consequence

Because `lambda_E(n)=b(n)/n`, Abel summation gives for `N>=q`

```text
boxed:
sum_{n~N}lambda_E(n)chi(n)
 <<_epsilon N^(-1/2)q^(1/2)(Nq)^epsilon.
```

## 6. K5 exponent consequence

Take `eta=1/100`. If there is no long-long reciprocal edge and the E vertex satisfies

```text
V>=M^(6eta),
```

then all at most four linear neighbors are `<M^eta`, so their product conductor is `q<=M^(4eta)`. The dyadic lemma gives relative saving

```text
V^(-1/2)q^(1/2)
 <= M^(-3eta)M^(2eta)
 =M^(-eta)=M^(-1/100),
```

stronger than the K5 long-long saving `M^(-1/200)`.

If no linear active variable reaches `M^(4eta)` and the E variable is below `M^(6eta)`, the product of all five active moduli is at most `M^(22eta)`. Exact local centering and the fixed-conductor periodic box estimate, with the s5p auxiliary-energy multiplicity absorbed into `M^o(1)`, give

```text
M^(1+44eta+o(1))+M^(66eta+o(1))
=M^(1.44+o(1))+M^(0.66+o(1)),
```

well below `M^2`. Hence the rank-one K5 bulk sector is closed in every size configuration, with conservative worst saving `1/200`.