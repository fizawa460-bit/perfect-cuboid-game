# Stage35-EX 35EX-31 — primitive-source marking is a 2-adic endpoint gauge

Status: `PROVISIONAL_EXACT_PRIMITIVE_SOURCE_REVERSE_ADAPTER_ENDPOINT_EQUIVALENCE_NO_CLOSURE`

This leaf starts after hostile-audit PASS of 35EX-30 at exact head
`00d6199c0df611b0606b15b8a46897629363cb10`, review node
`PRR_kwDOTr52Y88AAAABMS_hqA`, exact-head CI `33950151293 / 101263267837`, and
merge main `3d63864b0a10a53549f64a9e0dc3acf6f59ef9c0`.

The post-35EX-29 breadth audit had already selected

```text
E1-PRIMITIVE-SOURCE-MARKING-ON-COMPRESSED-CUBOID-GAUGE
```

and the hostile audit of 35EX-30 explicitly confirmed that no additional breadth
audit is required before this leaf.

The result is a blocker rather than an E1 proof: the missing primitive-source
marking can be transported exactly, but after endpoint scaling and edge
permutation it is only a 2-adic gauge choice. It does not cut the unlabeled
rational-perfect-cuboid population to a smaller arithmetic family.

No E1, R29, Stage35, or perfect-cuboid existence/nonexistence credit is granted.

## 1. Source-normalized endpoint coordinates

Retain the primitive Stage35 source triples

```text
(U1,V1,W1), (U2,V2,W2),
Ui^2+Vi^2=Wi^2,
Ui,Wi odd, Vi even,
gcd(Ui,Vi)=gcd(Ui,Wi)=gcd(Vi,Wi)=1.
```

As in 35EX-19/21, put

```text
x = V1/U1,
y = V2/U2,

d1 = W1/U1,
d2 = W2/U2,
d3 = MasterHyp/(U1*U2),
d4 = E1Hyp/(U1*U2).
```

For a hypothetical full E1 counterexample these are positive rationals and

```text
d1^2 = 1+x^2,
d2^2 = 1+y^2,
d3^2 = x^2+y^2,
d4^2 = 1+x^2+y^2.                              (SPC-src)
```

Thus `(1,x,y)` is the source-labeled normalized cuboid of 35EX-21.

The source parity immediately gives

```text
v2(x)>0,
v2(y)>0.                                           (MARK-src)
```

Moreover `d3^2=x^2+y^2` forces `v2(x)!=v2(y)`: if both valuations were the
same, after removing the common power of two the two square terms would be odd
units and their sum would have odd 2-adic valuation, impossible for a rational
square. This recovers the 35EX-02 Master 2-adic dichotomy directly in endpoint
coordinates.

## 2. Exact source formulas inside the late Kummer chart

The 35EX-26/27 source-locked coordinates simplify on `(SPC-src)` to

```text
alpha = (d4+y)/d1,
b     = (d2+d3)/(x+1).                            (S1)
```

Indeed 35EX-26 has `b=(q+z)/(x+1)` in the 35EX-21 notation, while the
35EX-27 formula for `alpha` reduces using the source quotient identities to the
displayed expression.

Because

```text
(d4+y)*(d4-y)=d1^2,
```

we have

```text
alpha^{-1}=(d4-y)/d1.
```

Hence, with `A=alpha^2`,

```text
c=(A^2+1)/(2*A)
 =(alpha^2+alpha^{-2})/2
 =(d2^2+d3^2)/d1^2.                              (S2)
```

Let `s=b^2` and let the positive 35EX-30 coordinate be `omega`, so

```text
omega^2=(c*s-1)/(s-c).
```

Using `(S1)`--`(S2)` and

```text
(d2+d3)*(d3-d2)=x^2-1,
```

the Möbius equation is exactly

```text
omega^2=((d2+d3)/(x-1))^2.                       (S3)
```

Thus the positive square root is branchwise

```text
x>1:       omega=(d2+d3)/(x-1),
0<x<1:     omega=(d2+d3)/(1-x).                  (S4)
```

The case `x=1` is impossible for a nonzero rational Pythagorean source, since
`d1^2=2` would be required.

## 3. 35EX-30 gauge remembers the source up to the first-edge swap

35EX-30 defines

```text
e1=omega-b,
e2=omega+b,
e3=Q30,
```

and normalizes by `e1`. Write its normalized endpoint coordinates as

```text
X=e2/e1,
Y=e3/e1,
D1=t/e1,
D2=(b*omega-1)/e1,
D3=(b*omega+1)/e1,
D4=P30/e1.
```

There are exactly two source branches.

### Branch A: `x>1`

Using `(S1)` and `(S4)` gives

```text
X=x,
Y=y,
D1=d1,
D2=d2,
D3=d3,
D4=d4.                                             (GA)
```

So the 35EX-30 normalized gauge is literally the original source-labeled
35EX-21 chart.

### Branch B: `0<x<1`

The positive choice in `(S4)` instead gives

```text
X=1/x,
Y=y/x,
D1=d1/x,
D2=d3/x,
D3=d2/x,
D4=d4/x.                                           (GB)
```

This is exactly the same cuboid after swapping the first two source edges and
rescaling by `x`. The two face diagonals `d2,d3` are correspondingly exchanged.

Therefore the late Kummer compression did not destroy the source data. It
forgot only the branch bit of the first-edge reciprocal involution.

## 4. The branch bit is recovered 2-adically

Let

```text
a=v2(X),
beta2=v2(Y).
```

A canonical Stage35 source has `(MARK-src)`. Therefore the source-marked locus
inside the fixed 35EX-30 gauge is exactly

```text
MARK-A: a>0 and beta2>0,
```

with source reconstruction

```text
x=X, y=Y,
```

or

```text
MARK-B: a<0 and beta2>a,
```

with source reconstruction

```text
x=1/X, y=Y/X.                                      (MARK-gauge)
```

Equivalently, among the three normalized edge valuations

```text
v2(1)=0, v2(X), v2(Y),
```

the unique minimum is not the `Y` edge. If the minimum is `0`, use Branch A;
if the minimum is `v2(X)`, use Branch B.

For any rational cuboid all three edge valuations are pairwise distinct. If two
edges had the same 2-adic valuation, their squared sum would have odd valuation
and could not be the square of a rational face diagonal. Thus the minimum edge
is always unique.

This gives an exact, intrinsic reconstruction of the source reciprocal branch.

## 5. Primitive Euclid reverse adapter from the marked endpoint

Now start with a positive rational point of `(SPC-src)` satisfying

```text
v2(x)>0,
v2(y)>0.                                           (M)
```

Write the two edge ratios in lowest terms:

```text
x=V1/U1,
y=V2/U2,
```

with positive coprime numerator/denominator pairs. Condition `(M)` gives

```text
U1,U2 odd,
V1,V2 even.
```

Because `d1` is rational and

```text
(U1*d1)^2=U1^2+V1^2
```

is an integer, `W1=U1*d1` is an integer: a rational number whose square is an
integer is itself an integer. Likewise `W2=U2*d2` is an integer. Hence

```text
(Ui,Vi,Wi)
```

are primitive Pythagorean triples with odd/even Stage35 orientation. The
standard primitive-triple theorem therefore reconstructs unique positive
coprime opposite-parity Euclid parameter pairs `(a,b)` and `(m,n)` under the
usual `a>b`, `m>n` convention.

The remaining endpoint squares reconstruct the two Stage35 square conditions:

```text
M0=U1*U2*d3,
E0=U1*U2*d4.
```

Their squares are the integers

```text
M0^2=(V1*U2)^2+(U1*V2)^2,
E0^2=(W1*U2)^2+(U1*V2)^2.
```

Since `M0,E0` are rational and have integral squares, they are integers.
Therefore the reconstructed tuple is a genuine Master-Hit and an E1
counterexample.

This proves the previously missing reverse population adapter on the exact
source-marked endpoint locus.

## 6. Canonical gcd channels are primitive normalization factors

Define the Stage35 canonical cross-gcd data

```text
c0 = gcd(U1,U2),
p0 = gcd(W1,V2),
q0 = gcd(V1,V2).
```

Then the already-audited 35EX-02 identities give

```text
g0=c0*p0,
h =c0*q0,
```

with `c0,p0,q0` pairwise coprime and `c0,p0` odd.

In endpoint coordinates these gcds have a direct geometric meaning. The
Master diagonal section `(x,y,d3)` has primitive integer representative

```text
((V1*U2)/h, (U1*V2)/h, M0/h),
```

with common rational scale `U1*U2/h`. The E1 diagonal section `(d1,y,d4)` has
primitive integer representative

```text
((W1*U2)/g0, (U1*V2)/g0, E0/g0),
```

with common scale `U1*U2/g0`.

Thus the canonical `h` and `g0` channels are not extra hidden endpoint
conditions: they are exactly the primitive-normalization factors of two
endpoint Pythagorean sections. The source marking restores them deterministically.

## 7. Why the marking does not reduce the endpoint population

Take any hypothetical positive rational perfect cuboid, with three positive
rational edge lengths. Rational face diagonals force the three edge `v2`
valuations to be pairwise distinct, as above. Hence there is a unique edge of
minimum 2-adic valuation.

Scale by that edge and place it first. The other two normalized edge ratios then
have strictly positive 2-adic valuation. Therefore the normalized point
satisfies `(M)` and Section 5 reconstructs a canonical Stage35 Master-Hit/E1
counterexample.

Conversely, 35EX-21 already sends every Stage35 E1 counterexample to a positive
rational perfect cuboid, and Sections 2--6 make the source marking/reverse map
exact.

Consequently, after quotienting by positive scaling and edge permutation, the
primitive-source marking does **not** define a smaller endpoint population. It
is the canonical choice of the unique minimum-`v2` edge as base. The ordering
of the remaining two edges corresponds to swapping the two source triples.

Equivalently, at the population level,

```text
Stage35 E1 counterexamples / source-pair swap
<=>
positive rational perfect cuboids / positive scaling and edge permutation.
                                                               (POP-EQ)
```

This is an exact equivalence of hypothetical populations, not an existence or
nonexistence result.

It also explains why the 35EX-30 endpoint return did not unlock a smaller
arithmetic receiver: restoring all primitive source labels takes us back to a
canonical gauge slice of the endpoint itself.

## 8. Arsenal and credit firewall

Formal Arsenal `S30-WF03` governs the credit boundary: completing the reverse
adapter grants only adapter/population-equivalence credit after hostile audit;
it does not by itself close the receiver, E1, Stage35, or the endpoint.

Formal `S34-W03` remains available only if a future genuinely additional
receiver condition is found. This leaf shows that primitive source marking by
itself is not such an unlabeled endpoint restriction.

No formal Arsenal card supplies this primitive-source 2-adic gauge theorem; it
is proved here from the Stage35 source locks.

The result is materially new structural information, so after hostile PASS a
fresh exhaustive-view / blind-rediscovery audit is required before selecting a
successor arithmetic route.

## 9. Result

```text
SOURCE_TO_35EX30_BRANCHWISE_LABEL_MAP_EXACT=true
SOURCE_RECIPROCAL_BRANCH_RECOVERED_BY_V2=true
PROVISIONAL_PRIMITIVE_SOURCE_REVERSE_ADAPTER=true
CANONICAL_GCD_CHANNELS_RECONSTRUCTED_FROM_ENDPOINT=true
MASTER_2ADIC_DICHOTOMY_RECOVERED_FROM_ENDPOINT=true
UNIQUE_MINIMUM_V2_EDGE_FOR_RATIONAL_CUBOID=true
SOURCE_MARKING_REDUCES_UNLABELED_ENDPOINT_POPULATION=false
PROVISIONAL_E1_COUNTEREXAMPLE_RATIONAL_PC_POPULATION_EQUIVALENCE=true
AUDITED_ADAPTER_CREDIT=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
FRESH_BREADTH_AUDIT_REQUIRED_AFTER_HOSTILE_PASS=true
```
