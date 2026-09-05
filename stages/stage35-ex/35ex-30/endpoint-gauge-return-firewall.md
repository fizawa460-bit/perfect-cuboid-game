# Stage35-EX 35EX-30 — exact endpoint-gauge return and no-recredit firewall

Status: `PROVISIONAL_EXACT_ENDPOINT_GAUGE_RETURN_FIREWALL_NO_CREDIT`

This leaf starts after hostile-audit PASS of 35EX-29 at exact head
`21ce592d3f30fd10b421ed0d3be68a702c26c65a`, review node
`PRR_kwDOTr52Y88AAAABMS3Ipg`, exact-head CI `33946860829 / 101254427135`,
and merge main `38434ea3c4124efd1cc04a228e85b2fd207f2c14`. The mandatory post-35EX-29
fresh exhaustive-view / blind-rediscovery audit is
`stages/stage35-ex/35ex-29/post-reciprocal-common-factor-breadth-audit.json`.

The purpose is deliberately narrow: prove the strongest blind symmetric
reparameterization exactly, then identify whether it is genuinely new or only
returns to a historical endpoint-scale object. It does the latter. No E1,
Stage35, R29, or perfect-cuboid theorem credit is granted.

## 1. Audited compressed receiver

Retain

```text
A = alpha^2,
s = b^2,
c = (A^2+1)/(2*A),
1 < c < s < A,

R1: r^2   = (s-c)*(c*s-1),
R2: ell^2 = 2*(c*s-1)*(s^2-1).
```

Because `s>c`, define the positive square coordinate

```text
w = r/(s-c),
W = w^2.
```

Then R1 is equivalent to

```text
W = (c*s-1)/(s-c),                              (M1)
W*(s-c)=c*s-1.
```

The associated fractional-linear map

```text
F_c(x)=(c*x-1)/(x-c)
```

is an involution. Its fixed points are exactly `A` and `1/A`, since
`c=(A+A^{-1})/2`.

Moreover

```text
W-A = ((A^2-1)/(2*A))*(A-s)/(s-c) > 0,
```

so on positive square roots the inherited chamber sharpens to

```text
1 < b < alpha < w.
```

## 2. Eliminate the shared factor by the square ratio

Put

```text
t = ell/r.
```

R1 and R2 give exactly

```text
t^2 = 2*(s^2-1)/(s-c).                          (T1)
```

Using `(M1)`,

```text
s+W = (s^2-1)/(s-c),
```

hence

```text
t^2 = 2*(s+W).                                  (T2)
```

No new square condition has been introduced: `t` is the exact ratio of the
two existing Kummer square roots.

## 3. Symmetric three-square package

Define

```text
P = ((A+1)/(2*alpha))*t,
Q = ((A-1)/(2*alpha))*t.
```

Because `A=alpha^2`,

```text
((A+1)/(2*alpha))^2 = (c+1)/2,
((A-1)/(2*alpha))^2 = (c-1)/2.
```

Also `(M1)` is equivalent to

```text
s*W+1 = c*(s+W).                                 (M2)
```

Therefore

```text
P^2 = (c+1)*(s+W) = (s+1)*(W+1),               (S1)
Q^2 = (c-1)*(s+W) = (s-1)*(W-1),               (S2)
t^2 = 2*(s+W),                                  (S3)
P^2-Q^2 = t^2.                                  (S4)
```

The source square `A` remains visible rather than being silently discarded:

```text
P+Q = alpha*t,
P-Q = t/alpha,
A = (P+Q)/(P-Q).                                 (A1)
```

Conversely, on the positive nondegenerate open, suppose rational
`b,w,P,Q,t` satisfy `(S1)`--`(S4)` and choose the positive signs so that
`P>Q>0`. Define

```text
alpha = (P+Q)/t = t/(P-Q),
A = alpha^2,
s = b^2,
W = w^2.
```

Then

```text
(A^2+1)/(2*A)
 = (P^2+Q^2)/(P^2-Q^2)
 = (s*W+1)/(s+W)
 = c.
```

Thus `W*(s-c)=c*s-1`. Taking

```text
r   = (s-c)*w,
ell = t*r
```

reconstructs R1 and R2 exactly. With the inherited chamber
`1<b<alpha<w`, this is an exact iff coordinate description of the retained
R1/R2 receiver, not a necessary-only over-cover.

## 4. The symmetric package is a rational perfect-cuboid gauge

Set the three rational edge coordinates

```text
e1 = w-b,
e2 = w+b,
e3 = Q.
```

The retained order gives `e1,e2,e3>0`. Directly from `(S1)`--`(S3)`,

```text
e1^2+e2^2 = t^2,

e1^2+e3^2 = (b*w-1)^2,

e2^2+e3^2 = (b*w+1)^2,

e1^2+e2^2+e3^2 = P^2.                           (PC)
```

So every retained 35EX-29 receiver point has an exact rational cuboid-square
image with all three face diagonals and the space diagonal rational.

Normalizing by the nonzero edge `e1` gives

```text
x   = e2/e1,
y   = e3/e1,
p   = t/e1,
q   = (b*w-1)/e1,
z   = (b*w+1)/e1,
wPC = P/e1,
```

and exactly

```text
p^2   = 1+x^2,
q^2   = 1+y^2,
z^2   = x^2+y^2,
wPC^2 = 1+x^2+y^2.                               (S-PC)
```

This is the same normalized rational cuboid square surface isolated and
hostile-audited in 35EX-21.

## 5. Historical comparison: this is a return, not a new closure

35EX-21 already proved that the normalized full receiver maps exactly to the
endpoint-scale surface `(S-PC)`, and explicitly froze the route because that
surface is two-dimensional and no rational-point classification or
primitive-source population reverse adapter was proved.

Therefore the blind `S1`--`S4` / `(PC)` discovery is useful as a cleaner exact
coordinate bridge from the later Kummer receiver, but it does **not** create a
new smaller arithmetic object. The direct endpoint-surface attack is classified
as historical-equivalent route species and receives no duplicate theorem
credit.

In particular, this leaf does not claim that an arbitrary rational point of
`S-PC` automatically reconstructs the designated primitive Euclid pairs,
canonical cross-gcd channels, parity orientation, or source labels required by
Stage35. The current direction is source receiver -> cuboid gauge; endpoint
population -> canonical source remains a separate adapter problem.

## 6. Arsenal comparison and next gate

Formal `S34-W03` remains a router only: if a future source-marked cuboid gauge
has an exact additional condition, one may close that exact intersection
without classifying the whole endpoint surface. It does not manufacture the
missing source marking.

`S34-W02` remains locked because no uniform full Mordell-Weil group is
certified. The old `S34-W01` factor-descent route remains frozen at moving
source-dependent support.

The post-35EX-29 blind breadth audit therefore selects

```text
E1-PRIMITIVE-SOURCE-MARKING-ON-COMPRESSED-CUBOID-GAUGE
```

as the next arithmetic leaf. Its job is not to solve the perfect-cuboid surface
directly. Its job is to transport the primitive Euclid / canonical gcd / parity
and source-label information through the exact compressed coordinates and test
whether that marking cuts out a strict arithmetic sublocus of `(S-PC)`.

## 7. Result and firewall

```text
MOBIUS_R1_SQUARE_PAIR_EXACT=true
RATIO_T_SQUARE_EXACT=true
SYMMETRIC_THREE_SQUARE_RECEIVER_IFF=true
R1_R2_TO_RATIONAL_CUBOID_GAUGE_FORWARD_EXACT=true
NORMALIZED_CUBOID_SURFACE_SPC_MATCH_35EX21=true
ENDPOINT_SURFACE_NEW_THEOREM_CREDIT=false
ARBITRARY_SPC_POINT_TO_CANONICAL_SOURCE_ADAPTER_PROVED=false
PRIMITIVE_SOURCE_POPULATION_REVERSE_ADAPTER_PROVED=false
RECEIVER_INTERSECTION_CLOSED=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Cycle classification:

```text
CYCLE_ROUTE_STATUS=BLOCKED_NEW_PATTERN_ISOLATED
CYCLE_NEW_PATTERN=EXACT_LATE_KUMMER_TO_ENDPOINT_CUBOID_GAUGE_RETURN_WITH_SOURCE_MARKING_IDENTIFIED_AS_THE_MISSING_INFORMATION
CYCLE_NEW_VIEW_SOURCE=BLIND
CYCLE_ACTIVE_RECEIVER=R1_R2_WITH_PRIMITIVE_SOURCE_PROVENANCE_NOT_YET_TRANSPORTED_TO_ENDPOINT_GAUGE
CYCLE_SPLIT_TRIGGERED=false
NEXT_IF_HOSTILE_PASS=35EX-31_PRIMITIVE_SOURCE_MARKING_ON_COMPRESSED_CUBOID_GAUGE
```
