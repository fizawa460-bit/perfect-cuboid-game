# Stage14-s5s — physical height-window insertion and unconditional one-sided descent bound

## Purpose

Stage14-s5r closed the complete **actual** local 2-descent character polynomial with a power-saving average on every regular dyadic Euclid box. Stage14-s3 had already proved that every physical Stage14 hit below the space-diagonal cutoff `B` produces a non-torsion rational point on the corresponding elliptic fiber with logarithmic canonical height.

This stage inserts that physical height condition into the now-closed local descent average and clarifies the remaining global-solubility / Tate--Shafarevich (`Sha`) issue.

The key logical point is one-sided:

```text
physical hit
=> global rational non-torsion point in the s3 height window
=> globally soluble 2-cover class
=> locally soluble 2-cover class.
```

Therefore `Sha` is **not an obstruction to an upper bound** for physical hits. It obstructs the converse direction and therefore any lower bound, density theorem, or asymptotic identification from local solubility alone.

No new external analytic theorem is used.

---

## 1. Euclid scale versus the physical cutoff

For a primitive oriented first face write

```text
S=m^2-n^2,
X=2mn,
H=m^2+n^2,
```

with `m>n>0`, `gcd(m,n)=1`, and opposite parity.

If this first face participates in a physical cuboid candidate with space diagonal `d<=B`, then its face diagonal satisfies

```text
H <= d <= B.
```

Hence

```text
m^2+n^2 <= B.
```

On a dyadic Euclid box with parameter scale `M`, this means

```text
M << B^(1/2).
```

Thus the physical cutoff `B` corresponds to Euclid parameter scale at most `sqrt(B)`.

---

## 2. The s3 physical height window

Stage14-s3 proved that a physical hit below `B` gives an exact non-torsion point `P` on

```text
E_{m,n}: W^2=Z(Z-S^2)(Z+X^2)
```

with

```text
hhat(P) = O(log B + log H).
```

Since `H<=B` on the physical range,

```text
hhat(P) = O(log B).
```

Let `Q_B^phys` denote the set of primitive opposite-parity Euclid bases carrying at least one physical Stage14 hit below `B`.

For every `(m,n) in Q_B^phys`, choose one first physical point and its associated full-2-descent/Kummer class. Then the chosen class is globally soluble and lies in the logarithmic height window.

In particular it is locally soluble at every place.

---

## 3. Locally soluble classes form an unconditional majorant

Let `L_B` be the set of pairs

```text
(base, local descent class)
```

with

1. primitive opposite-parity Euclid base `(m,n)` and `m^2+n^2<=B`;
2. descent support on the moving bad-prime set `2SXH`;
3. the exact odd local rows of s5c/s5d;
4. the exact eight-state `Q_2` condition of s5f;
5. local solubility at every place.

The s5f local system is exactly the indicator defining `L_B`, and s5r proves power-saving average for that actual finite character polynomial.

The physical map gives an injection after choosing one witnessing class per physical base:

```text
Q_B^phys -> L_B.
```

Therefore

```text
#Q_B^phys <= #L_B.
```

This inequality requires **no assumption on Sha**.

If a locally soluble 2-cover represents a nonzero Sha class, it contributes to `L_B` but not to `Q_B^phys`; this only makes the majorant larger.

---

## 4. What the s5r dyadic theorem gives

Write `N_loc(Omega_M)` for the total local-system weight / locally admissible descent-class count on one regular dyadic Euclid box of scale `M`.

Stage14-s5r closes the actual local system with conservative relative saving

```text
M^(-1/200+epsilon)
```

from the physical two-dimensional box scale `M^2`.

Hence

```text
N_loc(Omega_M)
 <<_epsilon M^(2-1/200+epsilon).
```

The finitely many local Fourier states, `Q_2` cases, signed E roots, and auxiliary state labels are already included in the s5r theorem. If one instead returns to the earlier base-indexed cover-class presentation, the s2 envelope

```text
4^(omega(2SXH)+1)=M^o(1)
```

is absorbed by `M^epsilon` and does not change the power exponent.

---

## 5. Summation to the physical B-scale

Decompose

```text
m^2+n^2<=B
```

into `O(log B)` regular dyadic Euclid boxes with top parameter scale

```text
M_max << B^(1/2).
```

The exponent `2-1/200` is positive, so the dyadic sum is dominated by the largest scale. Therefore

```text
#L_B
 <<_epsilon
 B^((2-1/200)/2 + epsilon)
 = B^(399/400 + epsilon).
```

Consequently

```text
#Q_B^phys
 <<_epsilon B^(399/400+epsilon).
```

Thus Stage14-s obtains its first unconditional family-level power saving over the trivial `B^(1+o(1))` Euclid-base count:

```text
ACTIVE_PHYSICAL_BASE_POWER_SAVING_UPPER_BOUND_PROVED=true.
```

The exponent `399/400` is deliberately conservative; it inherits the weakest graph-assembly saving from s5o/s5r and is not optimized.

---

## 6. The height window costs no extra exponent for an upper bound

The s3 height condition is essential to characterize physical points, but after s5r it does not require a separate distribution theorem to obtain the above upper bound.

Indeed

```text
small physical global classes
subset
all globally soluble classes
subset
all locally soluble classes.
```

Dropping the height restriction only enlarges the counting set.

Therefore

```text
SMALL_POINT_WINDOW_INSERTED_IN_UPPER_BOUND=true,
SMALL_POINT_WINDOW_COSTS_NO_POWER_LOSS_FOR_UPPER_BOUND=true.
```

What remains unproved is a theorem describing how many locally soluble classes actually contain a rational point in the s3 logarithmic window. That information would be needed for a sharp asymptotic or a lower bound, not for the one-sided upper bound above.

---

## 7. Exact status of the Sha / global point gap

The logical relations are

```text
globally soluble cover => locally soluble cover,
```

but not conversely in general.

So the current Stage14-s theorem gives

```text
physical hits <= global small-point classes <= local classes.
```

The final inequality is now quantitatively power-saving.

Accordingly:

```text
GLOBAL_SOLUBILITY_NEEDED_FOR_UPPER_BOUND=false,
SHA_GAP_BLOCKS_CURRENT_UPPER_BOUND=false,
SHA_GAP_BLOCKS_LOCAL_TO_GLOBAL_CONVERSE=true.
```

We do **not** set `GLOBAL_SOLUBILITY_AVERAGED=true`: no distribution theorem for the globally soluble fraction of locally soluble covers has been proved.

---

## 8. Why this is still far from the sqrt(B) target

The desired Stage14 scale suggested by the finite data is

```text
B^(1/2+o(1)).
```

The present theorem is only

```text
B^(399/400+epsilon).
```

So the local-descent route has achieved a genuine power saving but has not approached the observed square-root exponent.

The remaining exponent gap is not caused by an unresolved local character sum: s5r closed those. It is the weakness of the **uniform saving exponent** supplied by the graph/transition analysis when converted from the two-dimensional Euclid parameter scale to the physical `B` scale.

This distinction matters for roadmap design:

- the local analytic architecture is closed;
- the s3 height window is inserted for upper bounds;
- Sha is not a blocker for upper bounds;
- the remaining question is whether the s5 machinery can be quantitatively strengthened enough to move the exponent substantially toward `1/2`, or whether that belongs to the next method/stage.

---

## 9. Stage boundary and roadmap

There is no reason at this point to split `s5s` into `s5s1`, `s5s2`, ... . This stage has one coherent task and closes it.

A sensible remaining s5 sequence is short:

```text
s5t: optimize / stress-test the assembled exponent and identify the exact bottleneck responsible for 1/200;
s5u: formulate the strongest theorem genuinely delivered by the s-track and decide whether further s-analysis can improve the exponent;
s5v (if needed): adversarial closure audit / theorem packaging;
then move to s6.
```

The letters `w,x,y,z` should not be consumed merely because they exist. If s5 is mathematically closed at `t`, `u`, or `v`, Stage14 should move directly to s6.

If a genuinely new independent obstruction appears, a local branch label such as `s5t1` is preferable to artificially extending the main chain. At the present boundary no such split is required.

---

## Deterministic audit

The accompanying audit checks the exact logical/exponent interfaces:

- `H=m^2+n^2<=d<=B` implies Euclid scale `M<=sqrt(B)`;
- the s3 window simplifies from `O(log B+log H)` to `O(log B)` on the physical range;
- the set-inclusion chain from physical hit to locally soluble cover;
- conversion of `M^(2-1/200+epsilon)` to `B^(399/400+epsilon)`;
- absorption of logarithmic dyadic count and the s2 subpolynomial class envelope into `B^epsilon`;
- the gap between the proved exponent `399/400` and the target `1/2`.

Finite computation is not used to prove the upper bound.

---

## Boundary

```text
STAGE14_S5S=COMPLETE_PHYSICAL_HEIGHT_WINDOW_INSERTION_AND_ONE_SIDED_LOCAL_DESCENT_UPPER_BOUND
S5R_ACTUAL_LOCAL_SYSTEM_USED_AS_POSITIVE_MAJORANT=true
PHYSICAL_HIT_IMPLIES_LOCALLY_SOLUBLE_DESCENT_CLASS=true
SHA_GAP_BLOCKS_CURRENT_UPPER_BOUND=false
SHA_GAP_BLOCKS_LOCAL_TO_GLOBAL_CONVERSE=true
SMALL_POINT_WINDOW_INSERTED_IN_UPPER_BOUND=true
SMALL_POINT_WINDOW_COSTS_NO_POWER_LOSS_FOR_UPPER_BOUND=true
EUCLID_SCALE_TO_B_CONVERSION_PROVED=true
LOCALLY_SOLUBLE_CLASS_BOUND_B_EXPONENT=399/400
ACTIVE_PHYSICAL_BASE_POWER_SAVING_UPPER_BOUND_PROVED=true
ACTIVE_PHYSICAL_BASE_UPPER_BOUND=B^(399/400+epsilon)
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_DISTRIBUTION_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
S5S_SUBSTAGE_SPLIT_REQUIRED=false
NEXT=Stage14-s5t optimize and adversarially stress-test the assembled exponent, identify whether the 1/200 bottleneck is structural or only bookkeeping, and decide the shortest closure path to Stage14-s6
```
