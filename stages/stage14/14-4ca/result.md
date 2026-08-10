# Stage14-4ca — dyadic short-denominator min receiver and the 9/10 whole-family bound

## Purpose

Merged Stage14-s7-12 proves the current unconditional whole-family bound

```text
V(B) << B^(10/11+o(1)).
```

Its short-denominator argument introduces a global square-part threshold.  Large square parts are charged by support sparsity, while thin square parts are charged by the adjacent two-cell coefficient theorem.

Stage14-4ca removes that artificial global threshold.  Instead, keep the short denominator and its canonical square part simultaneously dyadic:

```text
Q ~ B^q,
y ~ B^t,
Q=b*y^2.
```

On every such block there are already two compatible upper bounds on the same restricted physical set:

```text
support sparsity:        B^(2q-t+o(1)),
two-cell coefficient:   B^(1-(q-2t)/3+o(1)).
```

They are **not multiplied**.  Their minimum is optimized block by block.

The exact two-variable dyadic optimization gives

```text
boxed:
V(B) << B^(9/10+o(1)).
```

No new external character-sum theorem is used.  The only nontrivial analytic input is the already-merged adjacent two-cell theorem from Stage14-s7-10 / Stage14-4by.

---

## 1. Merged inputs

### 1.1 Canonical short denominator

For a physical ordered pair, write reduced coordinates

```text
u=P/Q,
w=R/S,
0<w<u<1.
```

Merged s7-03/s7-04 gives

```text
QS << B.
```

Exchange the two reduced coordinates if necessary and canonically orient

```text
Q<=S.
```

Hence

```text
Q <= B^(1/2+o(1)).                                  (1.1)
```

Write dyadically

```text
Q ~ D=B^q,
0<=q<=1/2+o(1).                                    (1.2)
```

### 1.2 Canonical squarefree-times-square decomposition

Write uniquely

```text
Q=b*y^2,
```

with `b` squarefree and `y>=1`.  Refine dyadically again:

```text
y ~ T=B^t,
0<=t<=q/2+o(1).                                    (1.3)
```

Then

```text
b ~ B^(q-2t).                                      (1.4)
```

### 1.3 Adjacent two-cell coefficient theorem

Under the shared product-square label, the exact four-cell factorisation is

```text
a=r*s,
b=t1*j,
c=r*t1,
d=s*j.
```

Thus the denominator squarefree coefficient `b=t1*j` is an adjacent two-cell product.

Merged s7-10 / 4by proves that a restricted physical family in which the selected adjacent coefficient has scale

```text
b >= B^(rho-o(1))
```

obeys

```text
#states << B^(1-rho/3+o(1)).                       (1.5)
```

This is the proved two-cell relative saving `b^(-1/3)` at the whole-family level.

### 1.4 Fixed-coordinate transfer

Merged s7-04 proves `B^o(1)` bounded-height physical multiplicity for each fixed reduced coordinate.  Therefore any upper bound for the number of reduced coordinates in a restricted denominator block transfers to the physical whole-family count with only `B^o(1)` loss.

---

## 2. Exact support bound on one `(q,t)` block

Fix

```text
Q~D,
y~T,
Q=b*y^2.
```

For a fixed square root `y`, the number of possible coefficients `b` with `Q~D` is

```text
O(D/y^2).
```

For each resulting denominator `Q`, there are at most `Q=O(D)` possible numerators `0<P<Q`.  Dropping reducedness only enlarges the set.

Thus the number of reduced-coordinate candidates at fixed `y` is

```text
O(D^2/y^2).
```

There are `O(T)` integers in the dyadic range `y~T`, so

```text
boxed:
N_support(D,T)
 << D^2/T * B^o(1).                                (2.1)
```

In exponent notation,

```text
boxed:
E_support(q,t)=2q-t.                               (2.2)
```

By the fixed-coordinate genus-one transfer, (2.1) is also a valid physical-family upper bound for this restricted block.

This is the dyadic version of the large-squarepart support estimate in s7-12; no global threshold has been imposed.

---

## 3. Exact adjacent-coefficient bound on the same block

From `Q=b*y^2`,

```text
b ~ B^(q-2t).                                      (3.1)
```

When `q-2t>0`, apply the merged two-cell theorem (1.5) with

```text
rho=q-2t.
```

This gives the second upper bound

```text
boxed:
N_cell(q,t)
 << B^(1-(q-2t)/3+o(1)).                           (3.2)
```

At the endpoint `q=2t`, this simply becomes the trivial exponent `1`, so the formula remains harmless across the full closed dyadic domain.

Define

```text
boxed:
E_cell(q,t)=1-(q-2t)/3.                            (3.3)
```

---

## 4. The valid receiver is a minimum, not a product

Equations (2.1) and (3.2) are two upper bounds on the **same restricted physical block**.  Therefore

```text
boxed:
N(q,t)
 << B^( min(E_support(q,t),E_cell(q,t)) + o(1) ).  (4.1)
```

Explicitly,

```text
boxed:
E(q,t)
 = min(
     2q-t,
     1-(q-2t)/3
   ),                                               (4.2)
```

with

```text
0<=q<=1/2,
0<=t<=q/2.                                         (4.3)
```

No independent savings are multiplied.  This is exactly the quantifier-safe `min` architecture already used in merged s7-12, now retained on every square-part dyad instead of only on one side of a threshold.

---

## 5. Exact two-variable optimization

For fixed `q`, put

```text
f1(t)=2q-t,
f2(t)=1-(q-2t)/3.
```

Then `f1` is decreasing and `f2` is increasing.

Their crossing is

```text
2q-t = 1-(q-2t)/3
<=> 6q-3t = 3-q+2t
<=> 7q-5t=3.
```

Hence

```text
boxed:
t0(q)=(7q-3)/5.                                    (5.1)
```

### 5.1 Low denominator scale: `q<=3/7`

If `q<=3/7`, then `t0<=0`.  At `t=0`,

```text
f1(0)=2q <= f2(0)=1-q/3.
```

Since `f1` decreases and `f2` increases,

```text
E(q,t)<=2q<=6/7<9/10.                              (5.2)
```

So no low-denominator dyad is critical.

### 5.2 Critical range: `3/7<=q<=1/2`

Now `t0>=0`.  Also

```text
t0<=q/2
<=> 2(7q-3)<=5q
<=> 9q<=6,
```

which is automatic for `q<=1/2`.

Therefore the maximum of the minimum occurs at the crossing.  Substituting (5.1),

```text
E_crit(q)
 = 2q-(7q-3)/5
 = (3q+3)/5
 = 3(q+1)/5.                                      (5.3)
```

This is increasing in `q`.  Because the canonical short denominator satisfies `q<=1/2`,

```text
boxed:
E_crit(q)<=3(1+1/2)/5=9/10.                       (5.4)
```

Equality occurs exactly at

```text
boxed:
q=1/2,
t=1/10.                                           (5.5)
```

At this point

```text
q-2t = 1/2-1/5 = 3/10,                             (5.6)
```

so the critical denominator geometry is

```text
Q ~ B^(1/2),
y ~ B^(1/10),
b ~ B^(3/10).                                     (5.7)
```

Both valid bounds are exactly

```text
support: 2q-t = 1-1/10 = 9/10,
cell:    1-(q-2t)/3 = 1-(3/10)/3 = 9/10.          (5.8)
```

---

## 6. New unconditional whole-family bound

The canonical short-denominator orientation covers the entire physical family, and the dyadic `(q,t)` partition costs only `B^o(1)` blocks.

Sections 4-5 therefore give

```text
boxed:
V(B) << B^(9/10+o(1)).                              (6.1)
```

This strictly improves merged s7-12:

```text
10/11 - 9/10 = 1/110.                              (6.2)
```

Relative to the previous 4by / s7-10 `13/14` bound,

```text
13/14 - 9/10 = 1/35.                               (6.3)
```

Relative to the post-local baseline `41/42`, the cumulative proved post-local saving is

```text
41/42 - 9/10 = 8/105.                              (6.4)
```

The remaining exponent gap to square root is

```text
9/10 - 1/2 = 2/5.                                  (6.5)
```

No square-root upper bound is claimed.

---

## 7. What remains after 9/10

The critical block is now completely explicit:

```text
Q = shorter denominator ~ B^(1/2),
y = canonical square part ~ B^(1/10),
b = adjacent squarefree coefficient ~ B^(3/10).
```

The current proof uses only

```text
min(
  support sparsity Q^2/y,
  whole-family adjacent-two-cell bound B*b^(-1/3)
).
```

Therefore a strict improvement below `9/10` requires at least one genuinely new coupling:

1. a two-cell estimate relative to the **restricted support volume** `Q^2/y`, rather than only relative to the whole `B`-scale packet universe;
2. a joint short-denominator theorem coupling the support variable `y` and adjacent coefficient `b` instead of taking the minimum of separate bounds;
3. a family-level active-coordinate sparsity theorem on the critical `Q~B^(1/2)` strip.

Merely changing a global square-part threshold cannot improve (6.1); Stage14-4ca has removed that threshold completely.

---

## 8. Stage boundary

Proved in Stage14-4ca:

- the s7-12 large/thin global threshold can be replaced by a full dyadic `(q,t)` receiver;
- on each block, support sparsity gives exponent `2q-t`;
- the merged adjacent two-cell theorem gives exponent `1-(q-2t)/3` on the same block;
- taking the minimum is quantifier-safe and no savings are multiplied;
- the exact worst dyad is `q=1/2`, `t=1/10`;
- the critical denominator coefficient exponent is `3/10`;
- the unconditional whole-family exponent improves from `10/11` to `9/10`.

Not proved:

- any support-relative multiplication of the two-cell saving;
- any joint `(y,b)` cancellation theorem beyond the minimum receiver;
- `V(B)<<B^(1/2+o(1))`.

```text
STAGE14_4CA=DYADIC_SHORT_DENOMINATOR_SUPPORT_TWO_CELL_MIN_RECEIVER_AND_9_10_BOUND
MERGED_S7_12_10_11_IMPORTED=true
GLOBAL_SQUAREPART_THRESHOLD_REMOVED=true
SHORT_DENOMINATOR_DYADIC_EXPONENT=q
SHORT_DENOMINATOR_SQUAREPART_DYADIC_EXPONENT=t
DYADIC_SUPPORT_EXPONENT=2q-t
DYADIC_TWO_CELL_EXPONENT=1-(q-2t)/3
DYADIC_RECEIVER_COMBINATION=min
DYADIC_RECEIVER_SAVINGS_MULTIPLIED=false
CRITICAL_SHORT_DENOMINATOR_EXPONENT=1/2
CRITICAL_SQUAREPART_EXPONENT=1/10
CRITICAL_DENOMINATOR_COEFFICIENT_EXPONENT=3/10
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=9/10
IMPROVEMENT_OVER_10_11=1/110
IMPROVEMENT_OVER_13_14=1/35
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=8/105
CURRENT_GAP_TO_SQRT=2/5
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cb
```
