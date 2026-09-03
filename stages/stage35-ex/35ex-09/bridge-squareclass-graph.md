# Stage35-EX 35EX-09 — complete bridge squareclass graph and descent test boundary

## Scope

Assume the conditional reductions through 35EX-08. This leaf feeds the new hypotenuse bridge squares back into the four factors of 35EX-05.

The goal is to determine whether the third primitive Pythagorean triple collapses the moving squareclass obstruction enough to authorize a finite `S34-W01` enumeration or an infinite descent.

It does neither yet, but it gives a complete three-reservoir squareclass graph.

Throughout, squareclass equalities are in `Q*/Q*^2` and all displayed four factors are positive on the relevant branch.

## 1. Branch L: all six pair products

Recall

```text
T = U2/c,
t = r*s/q = u*v/p,
e = gcd(c,H),
w = r^2+s^2,
H = u^2+v^2.
```

35EX-07 proves

```text
gcd(t,T)=1,
```

and 35EX-08 proves `e|H`, while the primitive Master hypotenuse `H` is coprime to both `t` and `T`. Hence

```text
gcd(t,T)=gcd(t,e)=gcd(T,e)=1.
```

The adjacent pair products from 35EX-07 are

```text
L1*L2 = t*T*(a-b)^2,
L3*L4 = t*T*(a+b)^2.                  (L-adj)
```

Now use the pure bilinear identities

```text
L1*L4 = u*v*(r^2+s^2) + r*s*(u^2+v^2),
L2*L3 = u*v*(r^2+s^2) - r*s*(u^2+v^2).
```

Because `uv=p*t`, `rs=q*t`, and 35EX-08 gives

```text
p*w-q*H=e*A^2,
p*w+q*H=e*B^2,
```

we get the new exact products

```text
L1*L4 = t*e*B^2,
L2*L3 = t*e*A^2.                      (L-diag)
```

Dividing the squareclass relations in `(L-adj)` and `(L-diag)` yields the remaining opposite pair:

```text
[L1*L3] = [T*e],
[L2*L4] = [T*e].                      (L-opp)
```

Thus all six Branch-L pair products are controlled by exactly three pairwise-coprime live reservoirs:

```text
12,34 : [t*T]
14,23 : [t*e]
13,24 : [T*e].
```

## 2. Branch R has the identical graph

Put

```text
j = (u^2-v^2)/p = 2*r*s/q,
T = U2/c,
e = gcd(c,H).
```

35EX-07 gives `gcd(j,T)=1`; since `j` divides `(u-v)(u+v)` and `H=u^2+v^2` is coprime to `u^2-v^2`, while `e|H`,

```text
gcd(j,T)=gcd(j,e)=gcd(T,e)=1.
```

35EX-07 gives

```text
R1*R2 = j*T*(a-b)^2,
R3*R4 = j*T*(a+b)^2.                  (R-adj)
```

The bilinear identities are

```text
R1*R4 = (u^2-v^2)*(r^2+s^2) - 2*r*s*(u^2+v^2),
R2*R3 = (u^2-v^2)*(r^2+s^2) + 2*r*s*(u^2+v^2).
```

Using `u^2-v^2=p*j`, `2rs=q*j` and the bridge double squares gives

```text
R1*R4 = j*e*A^2,
R2*R3 = j*e*B^2.                      (R-diag)
```

Therefore

```text
[R1*R3] = [T*e],
[R2*R4] = [T*e],                      (R-opp)
```

and the Branch-R graph is

```text
12,34 : [j*T]
14,23 : [j*e]
13,24 : [T*e].
```

So the two 2-adic branches have the same abstract odd squareclass graph after replacing `t` by `j`.

## 3. Common-hypotenuse reservoir collapses to e at squareclass level

35EX-06 allowed the full common-hypotenuse gcd

```text
Gplus = gcd(w,H)
```

in Branch L, and its equivalent `Hplus` channel in Branch R.

35EX-08 shows `e=gcd(c,H)` divides both `w` and `H`, so `e` is contained in that common-hypotenuse reservoir.

Let an odd prime `ell` divide the common-hypotenuse reservoir but not `e`. Such a prime can divide only one adjacent factor pair (`12` or `34`). But the bridge identities `(L-diag)` / `(R-diag)` have squareclass supported only on the coprime product of the cross reservoir (`t` or `j`) with `e`. Therefore `ell` has even valuation in each individual factor in the adjacent pair where it occurs.

Hence common-hypotenuse primes outside `e` are individually squareclass-neutral. The only squareclass-relevant common-hypotenuse support is the live divisor `e`.

## 4. Complete factorwise squareclass allocation

Let `sf(n)` denote the positive squarefree kernel of `n`.

For Branch L, split the three pairwise-coprime squarefree kernels uniquely by the factor pair on which their odd valuation occurs:

```text
sf(t) = t13*t24,
sf(T) = T14*T23,
sf(e) = e12*e34,
```

where

```text
t13 : primes occurring on L1,L3,
t24 : primes occurring on L2,L4,
T14 : primes occurring on L1,L4,
T23 : primes occurring on L2,L3,
e12 : primes occurring on L1,L2,
e34 : primes occurring on L3,L4.
```

All six labels are pairwise coprime. Then the four individual squareclasses are exactly

```text
[L1] = [t13*T14*e12],
[L2] = [t24*T23*e12],
[L3] = [t13*T23*e34],
[L4] = [t24*T14*e34].                 (L-vertices)
```

Indeed every listed reservoir prime occurs on exactly the two incident vertices, and every odd prime outside `t*T*e` is squareclass-neutral by the pairwise gcd support together with the six pair-product relations.

Branch R is identical after `t -> j`:

```text
sf(j) = j13*j24,
sf(T) = T14*T23,
sf(e) = e12*e34,

[R1] = [j13*T14*e12],
[R2] = [j24*T23*e12],
[R3] = [j13*T23*e34],
[R4] = [j24*T14*e34].                 (R-vertices)
```

This is a complete factorwise odd-prime squareclass theorem for the current four-factor layer.

## 5. What this gains — and what it does not

35EX-07 had one moving pair-product squareclass `dL=tT` or `dR=jT`. 35EX-08 adds the bridge reservoir `e` and forces all six pair products into the three-edge pattern

```text
cross * difference,
cross * bridge,
difference * bridge.
```

Thus the previously broad common-hypotenuse reservoir is no longer uncontrolled at squareclass level.

However `t`/`j`, `T`, and `e` remain live parameter-dependent integers. Their prime-power allocations between the two possible edges are not uniformly supported on any fixed finite coefficient set. The complete vertex theorem above is therefore a parametric squareclass graph, not a finite exhaustive list of constant squareclasses.

So

```text
S34_W01_FACTORWISE_SUPPORT_COMPLETE=true
S34_W01_FIXED_FINITE_ENUMERATION=false
```

## 6. Descent test

The third parameter pair `(alpha,beta)` from 35EX-08 satisfies

```text
(alpha-beta)*(alpha+beta) = U1*U2/(c*e).
```

The two factors on the left are coprime odd integers, so this gives another exact prime-power allocation of the right-hand side. But no map has been derived that sends

```text
(a,b,m,n; r,s,u,v)
```

to a new tuple of the same Master-Hit + E1-counterexample type with a strictly smaller positive height.

In particular, the bridge parameterization alone does not reconstruct new canonical `c,p,q`, the two original Euclid triples, and both required square conditions. Therefore treating `(alpha,beta)` as an infinite-descent successor would be unsupported.

The exact status is

```text
THIRD_TRIPLE_GIVES_NEW_FACTOR_ALLOCATION=true
SIZE_DECREASING_ADMISSIBLE_COUNTEREXAMPLE_MAP_PROVED=false
INFINITE_DESCENT_PROVED=false
```

## Next exact leaf

```text
35EX-10_BRIDGE_DESCENT_MAP_OR_SPLIT_PRIME_OBSTRUCTION
```

Either construct and verify a genuine smaller admissible counterexample from the bridge data, or use the now-complete three-reservoir graph to seek a prime-valuation incompatibility. If neither occurs, freeze the bridge route before changing theorem species.

## Credit boundary

```text
COMPLETE_THREE_RESERVOIR_SQUARECLASS_GRAPH_PROVED_CONDITIONALLY=true
FINITE_FIXED_SQUARECLASS_FAMILY_PROVED=false
INFINITE_DESCENT_PROVED=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
