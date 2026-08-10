# Stage14-s7-12 — unbalanced short-denominator receiver and the 10/11 whole-family bound

## Purpose

Merged Stage14-s7-10 / Stage14-4by prove

```text
V(B) << B^(13/14+o(1)).
```

Merged Stage14-s7-11 then shows that adding a third or fourth shared cell does not improve the two-cell square-sieve mechanism: the higher-cell detectors factor through the same two-variable quotient, and the direct higher-dimensional square-sieve exponents are worse.

The remaining active issue is therefore the **small-coordinate sector**.  Until now the branch

```text
min(Q,S) <= B^lambda
```

was charged by the raw Farey count `B^(2 lambda+o(1))`, even though every denominator has its own canonical square-part/squarefree-coefficient decomposition and the squarefree coefficient is precisely an adjacent two-cell product to which the proved s7-10 / 4by receiver applies.

Stage14-s7-12 keeps these two facts simultaneously.

The result is a new unconditional whole-family bound

```text
boxed:
V(B) << B^(10/11+o(1)).
```

No new external character-sum theorem is used in this stage.  The only analytic inputs are already merged:

- fixed reduced-coordinate `B^o(1)` physical multiplicity from the s7 fixed-coordinate genus-one receiver;
- adjacent two-cell coefficient saving `C^(-1/3)` from s7-10 / 4by.

The improvement is produced by an **unbalanced min-receiver**, not by multiplying the two estimates.

---

## 1. Merged inputs

### 1.1 Multiplicative first-point height

For a physical ordered pair write the reduced coordinates

```text
u=P/Q,
w=R/S,
0<w<u<1,
```

with `gcd(P,Q)=gcd(R,S)=1`.

Merged s7-03/s7-04 gives

```text
QS << B.                                             (1.1)
```

The implicit absolute constant is exponent-neutral.

### 1.2 Fixed-coordinate multiplicity

Merged s7-04 proves that a fixed reduced coordinate `u=P/Q` lies on a smooth genus-one direction fiber and supports only

```text
B^o(1)                                               (1.2)
```

bounded-height primitive directions.  Together with the already-merged fixed-direction physical partner multiplicity, this gives an exponent-neutral transfer from the number of admissible reduced coordinates to the physical whole-family count.

In particular, for a dyadic denominator block `Q~D`, the raw coordinate bound is

```text
#physical states with Q~D << D^2 B^o(1).             (1.3)
```

This is the same fixed-coordinate receiver already used in the earlier s7 small-denominator analysis.

### 1.3 Two-cell coefficient theorem

Write each reduced coordinate in canonical squarefree-times-square form

```text
P=a*x^2,
Q=b*y^2,
R=c*z^2,
S=d*w^2,
```

with `a,b,c,d` squarefree.  The product-square relation gives

```text
ab=cd=xi.
```

The exact shared-label four-cell factorisation is

```text
a=r*s,
b=t*j,
c=r*t,
d=s*j.                                             (1.4)
```

Hence the denominator squarefree coefficient `b=t*j` is an adjacent two-cell product.

Merged s7-10 / 4by proves that, on any restricted collection of physical packets in which a selected adjacent coefficient satisfies

```text
C >= B^rho,
```

the collection obeys

```text
#states << B^(1-rho/3+o(1)).                        (1.5)
```

This is the unconditional two-cell relative saving `C^(-1/3)`.

Important quantifier rule: in s7-12 we do **not** multiply (1.3) and (1.5).  They are two valid upper bounds on the same restricted set, so we take their minimum.

---

## 2. Canonically orient to the shorter denominator

From (1.1), one of `Q,S` is at most `B^(1/2+o(1))`.  Exchange the two reduced coordinates if necessary and choose the canonical orientation

```text
Q <= S.                                             (2.1)
```

Then

```text
Q <= B^(1/2+o(1)).                                  (2.2)
```

Dyadically write

```text
Q ~ D = B^q,
0 <= q <= 1/2+o(1).                                 (2.3)
```

The whole family is the union of `B^o(1)` such dyadic blocks.

For the canonical decomposition

```text
Q=b*y^2,
```

fix a square-part threshold

```text
Y=B^tau,
0<tau<1/4.                                          (2.4)
```

Every block is split into

```text
large square part: y>=Y,
thin square part:  y<Y.
```

---

## 3. Large denominator square part gives coordinate-support sparsity

Consider a dyadic block `D<=Q<2D` with canonical square root `y>=Y`.

For each denominator `Q`, there are at most `Q` possible numerators `0<P<Q`.  We may drop reducedness for an upper bound.

If `y^2|Q`, then writing `Q=b y^2` and also dropping squarefreeness of `b`,

```text
sum_{D<=Q<2D, y(Q)>=Y} Q
 <= sum_{y>=Y} sum_{D/y^2 <= b < 2D/y^2} b*y^2.
```

For fixed `y`, the inner weighted sum is

```text
<< D^2/y^2.
```

Therefore

```text
boxed:
#reduced coordinates in the large-square-part block
 << D^2/Y * B^o(1).                                 (3.1)
```

Using the fixed-coordinate multiplicity (1.2),

```text
boxed:
N_large(q,tau)
 << B^(2q-tau+o(1)).                                (3.2)
```

Since `q<=1/2`, the entire large-square-part sector satisfies

```text
boxed:
N_large(tau)
 << B^(1-tau+o(1)).                                 (3.3)
```

This is genuine support sparsity: no character cancellation is used here.

---

## 4. Thin denominator square part activates the two-cell coefficient theorem

Now suppose

```text
y<Y=B^tau.
```

In a dyadic block `Q~B^q`,

```text
b=Q/y^2 >= B^(q-2tau-o(1)).                         (4.1)
```

When `q>2tau`, the denominator coefficient `b=t*j` is therefore a large adjacent two-cell product.  Applying the merged theorem (1.5) with

```text
rho=q-2tau
```

gives

```text
N_thin(q,tau)
 << B^(1-(q-2tau)/3+o(1)).                          (4.2)
```

But the same set still satisfies the independent fixed-coordinate bound

```text
N_thin(q,tau)
 << B^(2q+o(1)).                                    (4.3)
```

Hence the correct unbalanced receiver is

```text
boxed:
N_thin(q,tau)
 << B^( min(2q, 1-(q-2tau)/3) + o(1) )
for q>=2tau.                                        (4.4)
```

For `q<=2tau`, we simply use

```text
N_thin(q,tau) << B^(2q+o(1)) <= B^(4tau+o(1)).      (4.5)
```

Again, (4.4) is a **minimum of two compatible bounds**, not a product of savings.  Thus it respects the quantifier warnings frozen in the toolbox and s7-11.

---

## 5. Exact worst dyadic thin block

Assume `0<tau<=1/4`.

For `q>=2tau`, define

```text
f1(q)=2q,
f2(q)=1-(q-2tau)/3.
```

The first is increasing and the second decreasing.  Their crossing point is exact:

```text
2q = 1-(q-2tau)/3
<=> 7q=3+2tau
<=> boxed: q0=(3+2tau)/7.                           (5.1)
```

For `tau<=1/4`,

```text
2tau <= q0 <= 1/2.                                  (5.2)
```

Therefore the maximum of the minimum in (4.4) occurs at `q0`, with value

```text
boxed:
E_thin(tau)
 = 2q0
 = (6+4tau)/7.                                      (5.3)
```

The very-small block (4.5) is harmless because

```text
4tau <= (6+4tau)/7
```

exactly when `tau<=1/4`.

Thus the full thin-square-part sector obeys

```text
boxed:
N_thin(tau)
 << B^((6+4tau)/7+o(1)).                            (5.4)
```

---

## 6. One-parameter minimax and the 10/11 bound

Sections 3 and 5 cover every physical state after the canonical short-denominator orientation.  Hence for every `0<tau<=1/4`,

```text
V(B)
 << B^( E(tau)+o(1)),

E(tau)=max(
  1-tau,
  (6+4tau)/7
).                                                   (6.1)
```

The first branch decreases with `tau`; the second increases.  Equality occurs when

```text
1-tau = (6+4tau)/7.
```

Thus

```text
7-7tau=6+4tau,
11tau=1,
boxed: tau=1/11.                                    (6.2)
```

At this value,

```text
1-tau=10/11,
(6+4tau)/7=10/11.                                  (6.3)
```

Therefore

```text
boxed:
V(B) << B^(10/11+o(1)).                             (6.4)
```

### 6.1 Exact barrier certificate for this receiver

If both branches in (6.1) are at most `E`, then

```text
tau >= 1-E.                                         (6.5)
```

Also

```text
7E >= 6+4tau
    >= 6+4(1-E)
    =10-4E.
```

Hence

```text
11E>=10,
boxed: E>=10/11.                                    (6.6)
```

Equality is attained at `tau=1/11`.  Thus `10/11` is the exact minimax barrier of the present **short-denominator support-sparsity OR two-cell-coefficient** receiver.

---

## 7. Critical dyadic geometry

At the optimum `tau=1/11`, the thin-sector crossing denominator is

```text
q0=(3+2/11)/7=5/11.                                 (7.1)
```

Thus the two active mechanisms are geometrically distinct:

1. large square-part support branch:
   ```text
   Q up to B^(1/2),
   y >= B^(1/11),
   exponent 10/11;
   ```
2. thin square-part crossing branch:
   ```text
   Q ~ B^(5/11),
   y < B^(1/11),
   b >= B^(3/11-o(1)),
   ```
   where
   ```text
   fixed-coordinate exponent = 2q0 = 10/11,
   two-cell coefficient exponent
   =1-(q0-2/11)/3
   =10/11.
   ```

At the top dyad `q=1/2`, the thin coefficient theorem is already stronger:

```text
1-(1/2-2/11)/3 = 59/66 < 10/11.                    (7.2)
```

So the true thin obstruction migrates from the square-root denominator scale down to `Q~B^(5/11)`.

---

## 8. Improvement ledger

The previous merged whole-family theorem is

```text
13/14.
```

The new gain is

```text
13/14 - 10/11 = 3/154.                              (8.1)
```

For comparison,

```text
15/16 - 10/11 = 5/176,
18/19 - 10/11 = 8/209.                              (8.2)
```

Relative to the post-local `41/42` baseline, the cumulative proved saving is

```text
41/42 - 10/11 = 31/462.                             (8.3)
```

The remaining exponent gap to square root is

```text
10/11 - 1/2 = 9/22.                                 (8.4)
```

The square-root upper bound is not proved.

---

## 9. Why this does not contradict the s7-11 multicell barrier

s7-11 closes **higher-cell enlargement of the same square detector**.  Stage14-s7-12 does something different:

- it reduces the physical universe first by choosing the shorter denominator;
- on one branch it uses arithmetic sparsity of integers with a large square divisor;
- on the complementary branch it uses the already-proved two-cell theorem;
- the two bounds are combined by `min`, never by multiplying correlated square-sieve savings.

Thus no new independent Kummer detector is being claimed.

The gain comes from retaining the canonical square-part decomposition inside the previously raw small-coordinate count.

---

## 10. Next receiver

The new barrier has two active pieces at `10/11`:

```text
A. large-square-part support at the short denominator;
B. the q=5/11 crossing where fixed-coordinate support and the two-cell coefficient theorem are equally strong.
```

Threshold retuning alone cannot improve them because Section 6 gives an exact lower-bound certificate.

The natural next s7 task is therefore not another cell enlargement.  It should correlate the two bounds **inside the crossing dyad** rather than merely taking their minimum.

A valid improvement would need one of:

1. an active-coordinate sparsity theorem showing that only a power-saving fraction of reduced coordinates `P/Q` with `Q~B^(5/11)` actually occur in the physical two-point family;
2. a common-refinement incidence theorem combining the fixed-coordinate genus-one fiber with the `b=t*j` two-cell dispersion without the forbidden naive multiplication;
3. a sharper distribution theorem for the canonical square-part root near the `y~B^(1/11)` transition.

Accordingly:

```text
NEXT=Stage14-s7-13
```

should attack the `q=5/11`, `b>=B^(3/11)` crossing block by a common-refinement first-point/two-cell incidence theorem.

---

## 11. Stage boundary

```text
STAGE14_S7_12=COMPLETE_UNBALANCED_SHORT_DENOMINATOR_RECEIVER_AND_10_11_BOUND
MERGED_S7_11_IMPORTED=true
MERGED_S7_10_TWO_CELL_THEOREM_IMPORTED=true
MERGED_FIXED_COORDINATE_GENUS_ONE_RECEIVER_IMPORTED=true
SHORTER_DENOMINATOR_CANONICAL_ORIENTATION=true
SHORT_DENOMINATOR_MAX_EXPONENT=1/2
DENOMINATOR_CANONICAL_DECOMPOSITION=Q=b*y^2
LARGE_SQUAREPART_COORDINATE_SUPPORT_SAVING=Y^(-1)
THIN_SQUAREPART_FORCES_ADJACENT_COEFFICIENT=b>=Q/Y^2
UNBALANCED_THIN_RECEIVER_IS_MIN_OF_TWO_VALID_BOUNDS=true
FIXED_COORDINATE_AND_TWO_CELL_SAVINGS_MULTIPLIED=false
THIN_DYAD_CROSSING_Q_EXPONENT=(3+2*tau)/7
OPTIMAL_DENOMINATOR_SQUAREPART_THRESHOLD_EXPONENT=1/11
CRITICAL_THIN_DENOMINATOR_EXPONENT=5/11
CRITICAL_DENOMINATOR_COEFFICIENT_EXPONENT=3/11
SHORT_DENOMINATOR_ARCHITECTURE_BARRIER=10/11
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=10/11
IMPROVEMENT_OVER_13_14=3/154
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=31/462
CURRENT_GAP_TO_SQRT=9/22
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-13
```
