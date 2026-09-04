# Stage35-EX 35EX-15 — joint-local receiver test and free split-prime support

## Scope

Continue from hostile-audited and merged 35EX-14. Keep the exact receiver

```text
B35 := primitive Master-Hit source conditions + Lminus=square,
K35 := Lplus=square,
```

where

```text
Lminus=(W1*W2-V1*V2)/(p*d),
Lplus =(W1*W2+V1*V2)/(p*d),
p=gcd(W1,V2),
d=gcd(V1,W2).
```

35EX-14 proved that `B35 intersect K35` is exactly E1 failure and that this is the exact branch/receiver shape required by formal Arsenal weapon `S34-W03`. The purpose here is to test whether the available local arithmetic actually empties that intersection.

It does not. What closes exactly is the boundary of the current local route: after `Lminus=square`, the residual obstruction carried by `Lplus` is a moving squareclass supported only on split primes, while the 2-adic and real places are automatically soluble. This is precisely the prime class for which 35EX-11 retained free split-prime choices.

No E1 theorem or receiver-close credit is claimed.

## 1. Both normalized factors have split-only squareclass support

The two raw factors have exact bilinear norm presentations

```text
Pminus=W1*W2-V1*V2
      =(a*m-b*n)^2+(a*n-b*m)^2,

Pplus =W1*W2+V1*V2
      =(a*m+b*n)^2+(a*n+b*m)^2.
```

Every odd prime dividing `p` divides the primitive Pythagorean hypotenuse `W1`; every odd prime dividing `d` divides the primitive Pythagorean hypotenuse `W2`. Hence every odd prime dividing `p*d` is `1 mod 4`.

For an odd prime `ell=3 mod4`, the standard sum-of-two-squares valuation lemma gives

```text
v_ell(Pminus) even,
v_ell(Pplus)  even.
```

Since `p*d` has no `3 mod4` prime divisor,

```text
v_ell(Lminus) even,
v_ell(Lplus)  even                         (SPLIT-SUPPORT)
```

for every `ell=3 mod4`.

Therefore the squarefree kernels satisfy

```text
sf(Lminus), sf(Lplus)
```

supported only on primes `1 mod4`.

This statement is unconditional on the primitive source population; it does not use the Master square or either receiver square.

## 2. The residual receiver has no 2-adic obstruction on B35

For a primitive Euclid triple, the even leg `V=2ab` is divisible by `4`. Thus

```text
v2(V1)>=2,
v2(V2)>=2.
```

Because `p*d` is odd,

```text
Lplus-Lminus = 2*V1*V2/(p*d)
```

is divisible by `32`.

On `B35`, write

```text
Lminus=x^2.
```

`Lminus` is odd, so

```text
Lminus == 1 mod 8.
```

The divisibility above gives

```text
Lplus == Lminus == 1 mod 8.
```

Every odd `2`-adic unit congruent to `1 mod8` is a square in `Q_2`. Therefore

```text
B35 => Lplus is a square in Q_2.              (2-ADIC-REDUNDANCY)
```

Also `Lplus>0`, so the real place is automatically soluble.

Hence neither the real place nor the `2`-adic place can close `B35 intersect K35`.

## 3. Exact residual nonsquare witness class

Suppose a point lies on `B35` but fails `K35`. Then `Lplus` is a positive odd nonsquare integer. Therefore some prime has odd valuation in `Lplus`.

By `(SPLIT-SUPPORT)`, no prime `3 mod4` can have odd valuation, and `2` does not divide `Lplus`. Consequently every failure of the residual receiver admits an odd valuation witness

```text
ell == 1 mod4,
v_ell(Lplus) odd.                            (FREE-SPLIT-WITNESS)
```

Thus the residual squareclass obstruction is entirely carried by split primes.

This is the exact opposite of the strongest part of the 35EX-11 local routing theorem: there inert primes were uniquely oriented, while locally-good split primes retained independent binary freedom. The new receiver does not create an inert-prime witness class.

## 4. The support is genuinely source-dependent

The genuine Master-Hit

```text
(a,b,m,n)=(8,5,11,2)
```

has

```text
(U1,V1,W1)=(39,80,89),
(U2,V2,W2)=(117,44,125),
p=1,
d=5,
Master hypotenuse=9516.
```

For this point

```text
Lminus=1521=39^2,
Lplus =2929=29*101.
```

So it lies on the exact branch `B35` and fails only the residual receiver `K35`.

The odd source support of

```text
U1*U2*V1*V2*p*d
```

is

```text
{3,5,11,13},
```

whereas the squarefree residual support is

```text
sf(Lplus)=29*101.
```

Hence the residual split-prime obstruction can occur on primes not present in the source support used by the earlier reservoir-routing layer.

This one branch witness is not used to infer a universal theorem about all residual supports. It proves only the exact point needed for route discipline: no existing source-support inclusion theorem is available, and the residual witness support is demonstrably capable of moving outside the old source support.

The tuple is not an E1 counterexample because `Lplus` is not a square.

## 5. S34-W03 joint-local adapter boundary

The formal `S34-W03` branch/receiver adapter remains exact:

```text
B35 = primitive Master-Hit + Lminus=square,
K35 = Lplus=square.
```

However, the current local machinery does not provide the card's required exhaustive joint obstruction:

- the real place is automatically soluble;
- the `2`-adic place is automatically soluble on `B35`;
- inert-prime odd valuation witnesses are excluded structurally by the sum-of-two-squares norm presentations;
- any residual valuation witness is a moving `1 mod4` split prime;
- 35EX-11 proved precisely that locally-good split-prime choices are not globally coupled at the current primewise routing layer;
- no fixed finite support, fixed modulus, or new global product relation for `sf(Lplus)` has been proved.

Therefore the exact legal status is

```text
S34_W03_EXACT_BRANCH_RECEIVER_ADAPTER_MATCHED=true
S34_W03_RECEIVER_INTERSECTION_CLOSED=false
CURRENT_S34_W03_JOINT_LOCAL_ROUTE=FROZEN_FREE_SPLIT_SUPPORT
```

This does **not** prove that no local/global argument can ever close E1. It freezes only the current receiver-restricted local route based on the existing source/reservoir routing data.

## 6. Route decision

The fresh 35EX-14 breadth audit preserved two untested candidates:

```text
E1-PRODUCT-HYPOTENUSE-NONNAIVE-DESCENT,
E1-COPRIME-PAIR-GLOBAL-RECIPROCITY.
```

The local route has now exposed a sharper missing object: a global relation coupling the moving split-prime squareclass of `Lplus`. No matching formal Arsenal reciprocity/Hilbert/Jacobi weapon is registered in the current Arsenal index.

Accordingly the next active leaf is

```text
35EX-16_COPRIME_PAIR_GLOBAL_RECIPROCITY_OR_INDEPENDENT_SPLIT_ORIENTATIONS
```

It must test whether `gcd(Lminus,Lplus)=1`, the source cross-gcd units `p,d,c,q`, and the product-hypotenuse structure force a global Jacobi/Hilbert relation on the split-prime allocations. If the split orientations remain independent, freeze that route and return to the product-hypotenuse nonnaive descent candidate.

## Credit boundary

```text
RESIDUAL_SQUARECLASS_SPLIT_ONLY=true
B35_IMPLIES_LPLUS_Q2_SQUARE=true
CURRENT_S34_W03_JOINT_LOCAL_ROUTE_FROZEN_FREE_SPLIT_SUPPORT=true
S34_W03_RECEIVER_INTERSECTION_CLOSED=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
