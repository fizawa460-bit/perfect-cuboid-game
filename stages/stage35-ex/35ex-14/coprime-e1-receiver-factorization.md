# Stage35-EX 35EX-14 — coprime E1 receiver factorization

## Scope

Continue from hostile-audited and merged 35EX-13. This leaf analyzes the exact arithmetic content of the Gaussian source sieve and re-expresses the E1 receiver without changing its quantifier.

No E1, receiver, Stage35 MAIN, Stage29-parent, or endpoint credit is claimed.

Use the standard primitive Euclid data

```text
U1=a^2-b^2, V1=2ab, W1=a^2+b^2,
U2=m^2-n^2, V2=2mn, W2=m^2+n^2,
p=gcd(W1,V2),
d=gcd(V1,W2).
```

As already proved in 35EX-13, `p,d` are positive odd and coprime.

## 1. Two canonical product factors

Put

```text
A = W1*W2,
B = V1*V2,
Pminus = A-B,
Pplus  = A+B.
```

Because each source Pythagorean triple is primitive, the only prime-power overlap between `A=W1*W2` and `B=V1*V2` comes from the two cross channels

```text
p = gcd(W1,V2),
d = gcd(V1,W2).
```

The two channels are coprime, so primewise

```text
gcd(A,B)=p*d.                                  (GAB)
```

Now `A` is odd and `B` is even. Hence `Pminus` and `Pplus` are odd and

```text
gcd(Pminus,Pplus)
 = gcd(A-B,A+B)
 = gcd(A-B,2*B)
 = gcd(A-B,B)
 = gcd(A,B)
 = p*d.                                        (GPM)
```

Therefore the exact normalized factors

```text
Lminus = (W1*W2-V1*V2)/(p*d),
Lplus  = (W1*W2+V1*V2)/(p*d)                  (L+-)
```

are positive odd coprime integers:

```text
gcd(Lminus,Lplus)=1.                          (COPRIME)
```

There are no zero, pole, sign, or infinity cases in this normalization.

## 2. Exact factorization of the E1 norm

Let

```text
N = (W1*U2)^2 + (U1*V2)^2.
```

Using

```text
U2^2 = W2^2-V2^2,
U1^2 = W1^2-V1^2,
```

we get

```text
N
 = W1^2*(W2^2-V2^2) + (W1^2-V1^2)*V2^2
 = W1^2*W2^2 - V1^2*V2^2
 = (W1*W2-V1*V2)*(W1*W2+V1*V2).
```

Hence exactly

```text
N = (p*d)^2 * Lminus * Lplus.                 (E1-FACT)
```

The canonical E1 normalization divides the raw norm by `g0^2=(c*p)^2`, which is itself a square. Thus the normalized E1 norm is a square if and only if the raw integer `N` is a square.

Since `Lminus,Lplus` are coprime positive integers, `(E1-FACT)` gives the exact equivalence

```text
E1 counterexample
<=> Lminus*Lplus is a square
<=> Lminus is a square AND Lplus is a square. (E1-IFF)
```

This is an exact receiver factorization, not a proof that the intersection is empty.

## 3. 35EX-13 Gaussian sieve is exactly the first factor

35EX-13 obtained the source-only rational-square condition

```text
S_plus = d*(W1*W2+V1*V2)/(p*N) in Q^x2.
```

Substitute `(E1-FACT)` before assuming E1:

```text
S_plus
 = d*Pplus/(p*Pminus*Pplus)
 = d/(p*Pminus)
 = 1/(p^2*Lminus).
```

Therefore, exactly and unconditionally on the primitive source population,

```text
S_plus in Q^x2
<=> Lminus is an integer square.               (GAUSS=Lminus)
```

So the Gaussian squareclass condition is not a separate mysterious receiver. It is the first coprime factor of the exact E1 norm factorization.

The residual receiver after the Gaussian sieve is exactly

```text
Lplus is a square.                             (RESIDUAL)
```

No information has been lost: under the source hypotheses, `Lminus=square` plus `(RESIDUAL)` is exactly E1 failure.

## 4. Primitive product-hypotenuse triple forced by the full receiver

Assume both exact receiver factors are squares:

```text
Lminus=x^2,
Lplus=y^2,
y>x>0.
```

By `(COPRIME)`, `x,y` are coprime odd integers. Subtracting and adding gives

```text
y^2-x^2 = 2*V1*V2/(p*d),
y^2+x^2 = 2*W1*W2/(p*d).
```

Put

```text
R=(y+x)/2,
S=(y-x)/2.
```

Then `R,S` are positive, coprime, and of opposite parity, and

```text
2*R*S       = V1*V2/(p*d),
R^2+S^2     = W1*W2/(p*d),
R^2-S^2     = x*y = sqrt(N)/(p*d).             (PRODUCT-TRIPLE)
```

Thus a hypothetical E1 counterexample forces a primitive Pythagorean triple whose hypotenuse is the exact cross-gcd-normalized product of the two original hypotenuses.

This is a receiver coordinate, not a same-type descent map. No smaller admissible Master-Hit has been constructed from `(R,S)`.

## 5. Exact S34-W03 adapter check

The formal Arsenal card `S34-W03 RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION` applies as a routing pattern only after an exact branch `B`, exact receiver condition `K`, exhaustive joint test, and explicit degenerate-case treatment are supplied.

35EX-14 now supplies the exact branch/receiver split:

```text
B35 := primitive Master-Hit source conditions + Lminus=square,
K35 := Lplus=square.
```

By `(E1-IFF)`, every E1 counterexample lies in

```text
B35 intersect K35,
```

and conversely every point of that intersection is an E1 counterexample once the Master-Hit condition is retained. The field is `Q`; the quantifier is all primitive Master-Hits; the normalization is canonical through `p,d`; and `Lminus,Lplus` are positive odd integers, so there is no zero-factor/pole/infinity exceptional locus.

Therefore

```text
S34_W03_EXACT_BRANCH_RECEIVER_ADAPTER_MATCHED=true.
```

However the card also requires an exact local/global test proving the joint intersection empty or receiver-degenerate. 35EX-14 does not supply that theorem. Hence

```text
S34_W03_RECEIVER_INTERSECTION_CLOSED=false.
```

No claim about the full `B35(Q)` point set is made or needed.

## 6. Bounded regression evidence only

On the same deterministic primitive + Master-square panel used by 35EX-13,

```text
2<=a<=50,
2<=m<=100,
gcd(a,b)=gcd(m,n)=1,
a-b and m-n odd,
Master square = square,
```

there are exactly 131 Master-Hits. The exact first factor test gives

```text
Lminus=square survivors = 3:
(8,5,11,2),
(11,2,8,5),
(17,16,52,47).
```

For these three,

```text
Lplus = 2929, 2929, 313921,
```

respectively, and none is a square. Thus the bounded panel has no E1 counterexample, exactly as before.

This finite panel is regression/evidence only. It is not an exhaustive proof over all Master-Hits.

## 7. Route decision

The materially new receiver is now

```text
MASTER-HIT + Lminus=square + Lplus=square,
gcd(Lminus,Lplus)=1.
```

The Gaussian route has delivered a strictly cleaner exact gate and is therefore replaced by this factorized receiver.

The next exact task is not another bounded enumeration. It is the already-preserved receiver-restricted joint-local route, now with a complete exact adapter:

```text
35EX-15_COPRIME_RECEIVER_JOINT_LOCAL_OR_FREE_SUPPORT
```

It must either:

1. prove an exhaustive local/global obstruction for `B35 + K35`, with all source/gcd residue cases handled exactly; or
2. show that the surviving prime/residue support remains genuinely free, freeze this `S34-W03` local attempt, and return to the fresh candidate ledger.

Because `(E1-FACT)` materially changes the active receiver, a fresh `EXHAUSTIVE_VIEW_AUDIT + BLIND_REDISCOVERY` is recorded separately at 35EX-14B before that next route is promoted.

## Credit boundary

```text
COPRIME_E1_RECEIVER_FACTORIZATION_PROVED_CONDITIONALLY=true
GAUSSIAN_SIEVE_IDENTIFIED_WITH_LMINUS_SQUARE=true
S34_W03_EXACT_BRANCH_RECEIVER_ADAPTER_MATCHED=true
S34_W03_RECEIVER_INTERSECTION_CLOSED=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
