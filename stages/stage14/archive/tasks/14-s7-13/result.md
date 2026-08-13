# Stage14-s7-13 — full-coordinate canonical refinement and the 7/8 whole-family bound

## Purpose

Merged Stage14-s7-12 proves the current unconditional bound

```text
V(B) << B^(10/11+o(1)).
```

Its critical thin block occurs when the shorter reduced denominator has size

```text
Q ~ B^(5/11),
Q=b*y^2,
y < B^(1/11),
b >= B^(3/11-o(1)).
```

The s7-12 receiver dyadized the denominator square part `y` only after first counting all possible numerators `P<Q` trivially.  Stage14-s7-13 keeps the canonical squarefree-times-square decomposition on **both** entries of the same reduced coordinate

```text
u=P/Q,
P=a*x^2,
Q=b*y^2,
```

before applying either the fixed-coordinate support bound or the merged adjacent two-cell theorem.

This produces a stronger common-refinement receiver.  The two estimates are still not multiplied; they are two upper bounds on the same dyadic packet and are combined by a minimum.

The resulting unconditional whole-family bound is

```text
boxed:
V(B) << B^(7/8+o(1)).
```

No new external theorem is used.  The only analytic inputs are already merged:

- the fixed reduced-coordinate `B^o(1)` physical multiplicity;
- the adjacent two-cell coefficient saving `C^(-1/3)` from Stage14-s7-10 / Stage14-4by.

---

## 1. Merged inputs

### 1.1 Short-denominator orientation

For a physical ordered pair write

```text
u=P/Q,
w=R/S,
0<w<u<1,
```

in lowest terms.  Merged s7-03/s7-04 gives

```text
QS << B.
```

As in merged s7-12, exchange the two reduced coordinates if necessary and choose the canonical orientation

```text
Q <= S.
```

Then

```text
Q <= B^(1/2+o(1)).                                  (1.1)
```

Since `0<P<Q`, the numerator also satisfies

```text
P <= B^(1/2+o(1)).                                  (1.2)
```

### 1.2 Fixed-coordinate receiver

Merged s7-04 proves that a fixed reduced coordinate `P/Q` supports only

```text
B^o(1)
```

bounded-height primitive physical directions.  Hence any support bound for admissible reduced coordinates transfers to the whole physical family with only `B^o(1)` loss.

### 1.3 Adjacent two-cell theorem

Write the canonical decompositions

```text
P=a*x^2,
Q=b*y^2,
R=c*z^2,
S=d*w^2,
```

with `a,b,c,d` squarefree.  The product-square relation gives

```text
ab=cd=xi,
```

and the exact shared-label four-cell factorization is

```text
a=r*s,
b=t*j,
c=r*t,
d=s*j.                                             (1.3)
```

Thus **both** `a=r*s` and `b=t*j` are valid adjacent two-cell products.

Merged s7-10 / 4by proves that on any restricted physical packet collection in which a selected adjacent coefficient obeys

```text
C >= B^rho,
```

the collection satisfies

```text
#states << B^(1-rho/3+o(1)).                        (1.4)
```

We will select whichever of `a` and `b` is larger on each dyadic common-refinement block.

---

## 2. Full dyadic refinement of one reduced coordinate

Dyadically write

```text
P ~ B^p,
Q ~ B^q,
x ~ B^s,
y ~ B^t,                                          (2.1)
```

where exponent-neutral constants and endpoint blocks are absorbed in `B^o(1)`.

The physical inequalities imply

```text
0 <= p <= q <= 1/2.                                (2.2)
```

Because `x^2|P` and `y^2|Q`,

```text
0 <= s <= p/2,
0 <= t <= q/2.                                     (2.3)
```

Define the squarefree-coefficient exponents

```text
alpha = p-2s,
beta  = q-2t.                                      (2.4)
```

Thus on the block

```text
a ~ B^alpha,
b ~ B^beta.                                       (2.5)
```

Put

```text
m=max(alpha,beta).                                 (2.6)
```

A canonical tie-breaking rule selects `a` if `alpha>=beta` and `b` otherwise.

---

## 3. Coordinate-support bound on the common refinement

Let `A=B^p` and `X=B^s`.  The number of integers `P~A` whose canonical square-part root lies in `x~X` is bounded by

```text
sum_{x~X} O(A/x^2)
 << A/X.                                           (3.1)
```

Indeed, for each `x`, writing `P=a*x^2` leaves at most `O(A/x^2)` choices for `a`; dropping squarefreeness only enlarges the count.

Similarly, for `Q~B^q` and `y~B^t`,

```text
#Q << B^(q-t+o(1)).                                (3.2)
```

Therefore the number of reduced-coordinate candidates in the full block is

```text
#(P,Q)
 << B^(p-s+q-t+o(1)).                              (3.3)
```

Reducedness and `P<Q` may be dropped for this upper bound.

Using the fixed-coordinate `B^o(1)` physical multiplicity,

```text
boxed:
N_support(p,q,s,t)
 << B^(p+q-s-t+o(1)).                              (3.4)
```

In terms of `alpha,beta`,

```text
p+q-s-t
 = (p+q+alpha+beta)/2.                             (3.5)
```

Since `p+q<=1` and `alpha+beta<=2m`,

```text
boxed:
p+q-s-t <= 1/2+m.                                 (3.6)
```

This is the first upper envelope.

---

## 4. Two-cell bound on the same common refinement

By definition of `m`, the selected coefficient satisfies

```text
C=max(a,b) >= B^(m-o(1)).                           (4.1)
```

Both possible selections are legitimate adjacent products by (1.3).  Therefore merged s7-10 / 4by gives

```text
boxed:
N_2cell(p,q,s,t)
 << B^(1-m/3+o(1)).                                (4.2)
```

Equations (3.4) and (4.2) are two upper bounds on the **same restricted block**.  The valid combination is

```text
boxed:
N_block
 << B^( min(p+q-s-t, 1-m/3) + o(1)).               (4.3)
```

We do not multiply the fixed-coordinate and two-cell savings.

Using (3.6),

```text
N_block
 << B^( min(1/2+m, 1-m/3) + o(1)).                 (4.4)
```

---

## 5. Exact one-variable optimization

Define

```text
F(m)=min(1/2+m, 1-m/3),
0<=m<=1/2.                                         (5.1)
```

The first branch increases and the second decreases.  They meet when

```text
1/2+m = 1-m/3
<=> 4m/3=1/2
<=> boxed: m=3/8.                                  (5.2)
```

At this point

```text
1/2+3/8 = 7/8,
1-(3/8)/3 = 7/8.                                   (5.3)
```

Hence for every full-coordinate dyadic block,

```text
boxed:
N_block << B^(7/8+o(1)).                            (5.4)
```

There are only `B^o(1)` dyadic choices for `(p,q,s,t)`, so summing them preserves the exponent.

Therefore

```text
boxed:
V(B) << B^(7/8+o(1)).                              (5.5)
```

---

## 6. Exact architecture barrier and equality geometry

The bound (4.4) itself has worst value exactly `7/8`; this is not merely a convenient choice of cutoffs.

Equality in all relaxations requires

```text
p+q=1,
alpha+beta=2m,
m=3/8.                                             (6.1)
```

Since

```text
p<=q<=1/2,
```

the first equality forces

```text
boxed:
p=q=1/2.                                           (6.2)
```

The second equality with `m=max(alpha,beta)` forces

```text
boxed:
alpha=beta=3/8.                                    (6.3)
```

Thus

```text
s=(p-alpha)/2=1/16,
t=(q-beta)/2=1/16.                                 (6.4)
```

The critical geometry for this receiver is therefore

```text
boxed:
P,Q ~ B^(1/2),
a,b ~ B^(3/8),
x,y ~ B^(1/16).                                    (6.5)
```

At that block the support and two-cell estimates are both exactly `B^(7/8+o(1))` at exponent scale.

Consequently

```text
FULL_COORDINATE_REFINEMENT_ARCHITECTURE_BARRIER=7/8.
```

This is an architecture barrier only: it does not assert that the true physical count attains `B^(7/8)`.

---

## 7. Why the argument is compatible with s7-11

Merged s7-11 forbids multiplying correlated pairwise two-cell square-sieve savings and shows that direct three-/four-cell enlargement is weaker than the two-cell theorem.

Stage14-s7-13 does neither.

The improvement comes from three operations which are all already valid separately:

1. exact canonical decomposition of the numerator and denominator of one reduced coordinate;
2. elementary support counting inside the resulting common dyadic refinement;
3. one application of the proved two-cell theorem to the larger of `a` and `b`.

The support estimate and the analytic estimate are combined by `min`, not multiplication.

No new Kummer detector, independence assumption, or probabilistic density is introduced.

---

## 8. Improvement ledger

The previous merged whole-family exponent is

```text
10/11.
```

The new gain is

```text
10/11 - 7/8 = 3/88.                                (8.1)
```

Relative to the earlier `13/14` theorem,

```text
13/14 - 7/8 = 3/56.                                (8.2)
```

Relative to the post-local `41/42` baseline, the cumulative proved saving is

```text
41/42 - 7/8 = 17/168.                              (8.3)
```

The remaining exponent gap to square root is

```text
7/8 - 1/2 = 3/8.                                   (8.4)
```

The square-root upper bound is not proved.

---

## 9. Next receiver

The new critical block has much more rigid geometry than the s7-12 crossing:

```text
P,Q ~ B^(1/2),
a,b ~ B^(3/8),
x,y ~ B^(1/16).                                    (9.1)
```

In particular,

```text
xi=ab ~ B^(3/4)                                    (9.2)
```

at the exponent-critical configuration, while `a` and `b` are coprime squarefree coefficients of the same reduced coordinate and the partner pair `(c,d)` carries the same shared label `xi`.

The next improvement cannot come from simply applying the `a`- and `b`-two-cell estimates separately, because s7-11 already forbids multiplying them without a transverse theorem.

The natural next target is instead a **large-shared-label common-refinement incidence theorem** which retains

```text
ab=cd=xi
```

and the near-square-root first coordinate simultaneously.  It should determine whether the critical `xi~B^(3/4)` support itself is sparse or whether a new genuinely transverse detector is required.

Accordingly:

```text
NEXT=Stage14-s7-14
```

---

## 10. Stage boundary

```text
STAGE14_S7_13=COMPLETE_FULL_COORDINATE_CANONICAL_REFINEMENT_AND_7_8_BOUND
MERGED_S7_12_IMPORTED=true
MERGED_S7_10_TWO_CELL_THEOREM_IMPORTED=true
MERGED_FIXED_COORDINATE_GENUS_ONE_RECEIVER_IMPORTED=true
FULL_COORDINATE_DYADIC_REFINEMENT=true
NUMERATOR_CANONICAL_DECOMPOSITION=P=a*x^2
DENOMINATOR_CANONICAL_DECOMPOSITION=Q=b*y^2
DYADIC_COORDINATE_SUPPORT_EXPONENT=p+q-s-t
SELECTED_ADJACENT_COEFFICIENT_EXPONENT=m=max(p-2s,q-2t)
FULL_COORDINATE_SUPPORT_UPPER_ENVELOPE=1/2+m
TWO_CELL_SELECTED_COEFFICIENT_UPPER_ENVELOPE=1-m/3
COMMON_REFINEMENT_RECEIVER_IS_MIN_OF_TWO_VALID_BOUNDS=true
FIXED_COORDINATE_AND_TWO_CELL_SAVINGS_MULTIPLIED=false
CRITICAL_SELECTED_COEFFICIENT_EXPONENT=3/8
CRITICAL_NUMERATOR_EXPONENT=1/2
CRITICAL_DENOMINATOR_EXPONENT=1/2
CRITICAL_NUMERATOR_SQUAREPART_ROOT_EXPONENT=1/16
CRITICAL_DENOMINATOR_SQUAREPART_ROOT_EXPONENT=1/16
CRITICAL_SHARED_LABEL_EXPONENT=3/4
FULL_COORDINATE_REFINEMENT_ARCHITECTURE_BARRIER=7/8
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
IMPROVEMENT_OVER_10_11=3/88
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=17/168
CURRENT_GAP_TO_SQRT=3/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-14
```
