# Stage35-EX 35EX-04 — coprime product-rectangle reduction

35EX-03 leaves two branches. This leaf extracts all divisibility forced by the cross-equation before attempting any deeper descent.

## Elementary product-rectangle lemma

Suppose positive integers satisfy

```text
R*S = U*V,
gcd(R,S)=gcd(U,V)=1.
```

Then there are pairwise coprime positive integers `alpha,beta,gamma,delta` such that

```text
R = alpha*beta,
S = gamma*delta,
U = alpha*gamma,
V = beta*delta.
```

One construction is

```text
alpha = gcd(R,U),
beta  = gcd(R,V),
gamma = gcd(S,U),
delta = gcd(S,V).
```

Every prime-power on either side belongs to exactly one row and one column because the two factors within each side are coprime. Hence the four cells are pairwise coprime and reconstruct the four original factors exactly.

This lemma is bookkeeping, but it prevents later arguments from silently assuming unsupported independence between factors.

## Branch L: k1 < k2

35EX-03 gives

```text
p*r*s = q*u*v,
gcd(p,q)=1,
gcd(r,s)=gcd(u,v)=1.
```

Therefore `q|r*s` and `p|u*v`. Because the pairs are coprime, split uniquely by prime-power support:

```text
q = q_r*q_s,   q_r|r, q_s|s, gcd(q_r,q_s)=1,
p = p_u*p_v,   p_u|u, p_v|v, gcd(p_u,p_v)=1.
```

Write

```text
r=q_r*R,
s=q_s*S,
u=p_u*U,
v=p_v*V.
```

The cross-equation cancels to

```text
R*S = U*V,
```

with `gcd(R,S)=gcd(U,V)=1`. Hence the product-rectangle lemma gives pairwise coprime `alpha,beta,gamma,delta` with

```text
R=alpha*beta,
S=gamma*delta,
U=alpha*gamma,
V=beta*delta.
```

Thus every Branch-L counterexample admits a complete prime-support allocation into

```text
(q_r,q_s,p_u,p_v; alpha,beta,gamma,delta)
```

before the two difference-of-squares equations are imposed.

## Branch R: k1 > k2

35EX-03 gives

```text
2*p*r*s = q*(u^2-v^2).
```

Write

```text
q=2^k*q0,  q0 odd.
```

Here `k=v2(V2)=k2`. From the E1-even equation

```text
(U1/c)*(V2/p)=2*r*s
```

and oddness of `U1/c` and `p`, we get

```text
v2(r*s)=k-1.
```

Since `r,s` are coprime and of opposite parity, all of this 2-power lies in exactly one of them. Remove it and set

```text
R = r/2^v2(r),
S = s/2^v2(s).
```

Then `R,S` are odd and coprime, and division of the Branch-R cross-equation by `2^k` yields

```text
p*R*S = q0*(u-v)*(u+v).
```

Because `u,v` are coprime and of opposite parity,

```text
gcd(u-v,u+v)=1,
```

and both factors are odd. Since `gcd(p,q0)=1`, we have

```text
q0 | R*S,
p  | (u-v)*(u+v).
```

Split `q0` between `R,S` and `p` between `u-v,u+v` by prime-power support, cancel them, and again obtain an equality

```text
R0*S0 = X0*Y0
```

between two coprime pairs. The same product-rectangle lemma therefore supplies four pairwise-coprime cell factors.

## Consequence and next attack

The cross-equations contain no hidden entanglement after their forced `p,q` support is removed: both branches reduce to a four-cell coprime rectangle. Therefore **the cross-equation alone cannot close E1**; the next proof attempt must use at least one of the remaining additive equations

```text
r^2-s^2 = (W1/p)*(U2/c)
```

and the branch-specific Master equation, together with the Euclid identities

```text
W1-V1=(a-b)^2,
W1+V1=(a+b)^2.
```

This identifies the next exact leaf:

```text
35EX-05_GAUSSIAN_OR_DESCENT_COMPATIBILITY
```

Try to combine the product-rectangle allocation with the additive difference-of-squares identities. If no size-decreasing map or local contradiction follows, freeze the obstruction instead of treating the factor allocation as a theorem-strength saving.

## Credit boundary

This is an exact conditional reduction, not an E1 proof. No receiver or endpoint credit is granted.
