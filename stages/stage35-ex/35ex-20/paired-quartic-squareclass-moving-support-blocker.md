# Stage35-EX 35EX-20 — paired-quartic squareclass descent and moving-support blocker

## Scope

Continue only from hostile-audited and merged 35EX-19/19B. Work conditionally under a hypothetical full E1 counterexample and retain both primitive source circles.

The active leaf is the exact paired source-filter system

```text
Y^2=(u^2+1-sigma)(u^2+1+sigma),
Z^2=(u^2-1-sigma)(u^2-1+sigma),
k^2+sigma^2=1,
```

with

```text
r=U1/W1,
s1=V1/W1,
k=1-2*r^2,
sigma=2*r*s1.
```

The question is whether formal Arsenal weapon `S34-W01` is now unlocked as one finite exhaustive squareclass family for the whole Stage35-EX receiver.

The answer at the present identity level is **no**. The paired factorization admits an exact finite squareclass over-cover after fixing the first primitive source triple, but its odd support is the moving squarefree support of `U1*V1`. No source-independent finite branch family is derived.

No claim is made that every future squareclass/global argument is impossible.

## 1. The source parameter `1±sigma` is already a square

For the primitive first Pythagorean triple

```text
U=U1,
V=V1,
W=W1,
U^2+V^2=W^2,
```

we have `U,W` odd, `4|V`, and `gcd(U,V)=gcd(U,W)=gcd(V,W)=1`.

Put

```text
e=U-V,
f=U+V.
```

Then `e,f,W` are odd and

```text
gcd(e,f)=gcd(e,W)=gcd(f,W)=1.
```

Moreover

```text
1-sigma=(U-V)^2/W^2=e^2/W^2,
1+sigma=(U+V)^2/W^2=f^2/W^2.                 (SOURCE-SQ)
```

Thus the paired quartics are exactly

```text
Y^2=(u^2+e^2/W^2)(u^2+f^2/W^2),
Z^2=(u^2-f^2/W^2)(u^2-e^2/W^2).              (PAIR-SQ)
```

This is stronger than treating `sigma` as an arbitrary rational parameter, but it still retains the moving primitive source data `U,V,W`.

## 2. Primitive projective clearing

Set

```text
x=W*u=P/Q,
gcd(P,Q)=1,
Q>0.
```

Define four integers

```text
A=P^2+Q^2*e^2,
B=P^2+Q^2*f^2,
C=P^2-Q^2*f^2,
D=P^2-Q^2*e^2.                                (ABCD)
```

Multiplying `(PAIR-SQ)` by the square denominator `Q^4*W^4` gives

```text
(Q^2*W^2*Y)^2=A*B,
(Q^2*W^2*Z)^2=C*D.                            (INT-PROD)
```

Since an integer which is a rational square is an integer square,

```text
A*B is an integer square,
C*D is an integer square.                     (SQUARE-PRODUCTS)
```

For an actual source point, `Z=s2*(k-u^2)` with `s2>0` and `k-u^2!=0` by the audited 35EX-19 source adapter. Hence

```text
C!=0,
D!=0.                                         (NO-ZERO)
```

Since `C*D` is a positive square, `C,D` have the same sign. Because `f>|e|`, exactly one of the two sign regions occurs:

```text
|P/Q|>f       => C>0,D>0,
|P/Q|<|e|     => C<0,D<0.                     (SIGN)
```

The intermediate region is excluded by `C*D<0`; the equality boundaries are excluded by `(NO-ZERO)`.

## 3. Exact pairwise gcd/resultant support

The factor differences are

```text
B-A = Q^2*(f^2-e^2) = 4*Q^2*U*V,
D-C = Q^2*(f^2-e^2) = 4*Q^2*U*V,
A-C = Q^2*(e^2+f^2) = 2*Q^2*W^2,
B-D = Q^2*(e^2+f^2) = 2*Q^2*W^2,
A-D = 2*Q^2*e^2,
B-C = 2*Q^2*f^2.
```

Every one of `A,B,C,D` is coprime to `Q`, because reduction modulo any prime divisor of `Q` gives `P^2` and `gcd(P,Q)=1`. Therefore

```text
gcd(A,B)       | 4*U*V,
gcd(|C|,|D|)   | 4*U*V,
gcd(A,|C|)     | 2*W^2,
gcd(B,|D|)     | 2*W^2,                       (GCD-SUPPORT)
```

and the same-coefficient opposite-sign pairs satisfy the sharper exact odd-part identities

```text
oddpart(gcd(A,|D|)) = gcd(P,e)^2,
oddpart(gcd(B,|C|)) = gcd(P,f)^2.              (SQUARE-CROSS-GCD)
```

Thus those two cross gcds contribute no odd squareclass support at all. The remaining cross support is source-supported by `W`, while the two load-bearing within-product gcds are source-supported by `U*V`.

## 4. Exact squareclass over-cover for a fixed first source

Because `A,B>0` and `A*B` is a square, there is a unique positive squarefree integer `dY` such that

```text
A=dY*aY^2,
B=dY*bY^2.                                    (Y-BRANCH)
```

Likewise let

```text
epsilon=sign(C)=sign(D) in {+1,-1}.
```

Because `(epsilon*C)*(epsilon*D)>0` is a square, there is a unique positive squarefree integer `dZ` such that

```text
epsilon*C=dZ*aZ^2,
epsilon*D=dZ*bZ^2.                             (Z-BRANCH)
```

The gcd support above proves

```text
oddpart(dY) | rad_odd(U*V),
oddpart(dZ) | rad_odd(U*V).                    (UV-SUPPORT)
```

Moreover the odd supports are disjoint:

```text
gcd(oddpart(dY),oddpart(dZ))=1.               (DISJOINT)
```

Indeed an odd prime in both would divide all four of `A,B,C,D`; `(GCD-SUPPORT)` would then force it to divide both `U*V` and `W`, impossible for a primitive Pythagorean triple.

There is also an exact local orientation on the `Y` branch. If an odd prime `ell|dY`, then `ell|U*V`; reducing `A` modulo `ell` gives a nonzero square times `-1`. Hence

```text
ell == 1 (mod 4) for every odd ell|dY.         (Y-SPLIT-ONLY)
```

More explicitly:

```text
ell|U and ell|dY => (P/(Q*V))^2 == -1 mod ell,
ell|V and ell|dY => (P/(Q*U))^2 == -1 mod ell.
```

For `dZ` the corresponding congruence has `+1`:

```text
ell|U and ell|dZ => P == ±Q*V mod ell,
ell|V and ell|dZ => P == ±Q*U mod ell.         (Z-ORIENTATION)
```

No contradiction follows: odd primes of `U*V` can still remain absent from both branch kernels, and the present identities do not force a source-independent allocation of the moving split/inert support.

## 5. Complete 2-adic bookkeeping for this factor layer

Because `e,f` are odd, parity is controlled only by the reduced projective pair `(P,Q)`.

### Case A: `P,Q` have opposite parity

Then all four of `A,B,C,D` are odd. Therefore

```text
2∤dY,
2∤dZ.                                         (2A)
```

### Case B: `P,Q` are both odd

Odd squares are `1 mod 8`, so

```text
A==B==2 mod 8,
v2(A)=v2(B)=1,
8|C,
8|D.                                          (2B-RAW)
```

Thus

```text
2|dY.                                         (2B-Y)
```

Since `C*D` is a square,

```text
v2(C) == v2(D) mod 2.                         (2B-Z-PARITY)
```

Consequently `dZ` contains `2` exactly when this common valuation parity is odd. The valuation itself is not uniformly fixed: for odd `P,Q,e,f`, the factors `P±Qe` and `P±Qf` allow arbitrarily deeper 2-adic cancellation subject to the square-product condition.

This is complete for the present four-factor squareclass layer: the only 2-adic branch data are the parity class of `(P,Q)` and, in the odd/odd case, the one bit `v2(C) mod 2`.

## 6. What S34-W01 does and does not give here

For one fixed primitive first source `(U,V,W)`, Sections 2–5 give a finite exact over-cover:

```text
- choose epsilon in {+1,-1};
- choose the projective parity branch;
- choose disjoint odd squarefree kernels dY,dZ supported on rad_odd(U*V);
- require every odd prime of dY to be 1 mod 4;
- impose the one residual 2-adic bit when P,Q are both odd;
- solve the four equations (Y-BRANCH),(Z-BRANCH).
```

Thus

```text
FIXED_FIRST_SOURCE_SQUARECLASS_OVERCOVER_PROVED=true.
```

But this is **not** the source-independent finite exhaustive branch family required to unlock the Stage35-EX global use of `S34-W01`.

The unresolved labels range over squarefree divisors of the moving source product `U*V`. This is not a cosmetic coefficient drift. The support reservoir itself has unbounded prime complexity on the primitive first-source population: for example `b=1` and even `a` coprime to `1` gives a primitive Euclid source with `V=2a`, and `a` may contain arbitrarily many distinct odd prime factors.

Therefore the current theorem only gives

```text
(dY,dZ) in disjoint squarefree divisor pairs of rad_odd(U*V),
```

not one fixed finite list of squareclasses independent of the source.

Precisely:

```text
S34_W01_FIXED_SOURCE_ROUTING_MATCH=true,
S34_W01_GLOBAL_FINITE_EXHAUSTIVE_FAMILY_UNLOCKED=false,
UNIFORM_FIXED_SQUARECLASS_SUPPORT_PROVED=false.
```

This does not prove that no stronger transformation can eliminate the moving support. It proves that the present paired-factor gcd/resultant descent stops at a dynamic source-supported branch family.

## 7. Route decision

The selected 35EX-20 route is therefore frozen at the same exact kind of load-bearing boundary that S34-W01 itself requires us to expose rather than hide:

```text
CURRENT_PAIRED_QUARTIC_SQUARECLASS_ROUTE
 = FROZEN_DYNAMIC_UV_SUPPORT_NO_GLOBAL_FINITE_FAMILY.
```

The fresh 35EX-19B breadth audit already preserved the mathematically distinct untested candidate

```text
E1-GLOBAL-BIQUADRATIC-SURFACE-GEOMETRY.
```

Under the Cycle Exploration Safety Protocol, a blocked route with no new live object should not be mistaken for a receiver proof. The next legal candidate is therefore the preserved global-surface view; no new breadth audit is required merely to recover a candidate that the immediately preceding audit explicitly retained as `UNTESTED`.

## 8. Credit boundary

```text
PAIR_SOURCE_SQUARE_IDENTITY_PROVED=true
PRIMITIVE_INTEGER_FOUR_FACTOR_MODEL_PROVED=true
PAIRWISE_GCD_RESULTANT_SUPPORT_PROVED=true
FIXED_FIRST_SOURCE_SQUARECLASS_OVERCOVER_PROVED=true
Y_BRANCH_ODD_SUPPORT_SPLIT_ONLY=true
PAIR_2ADIC_BRANCH_BOOKKEEPING_PROVED=true
UNIFORM_FIXED_SQUARECLASS_SUPPORT_PROVED=false
S34_W01_GLOBAL_FINITE_EXHAUSTIVE_FAMILY_UNLOCKED=false
CURRENT_PAIRED_QUARTIC_SQUARECLASS_ROUTE=FROZEN_DYNAMIC_UV_SUPPORT_NO_GLOBAL_FINITE_FAMILY
ALL_PAIRED_QUARTIC_DESCENTS_RULED_OUT_IN_PRINCIPLE=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
