# Stage14-4cb — shared-label compression of the 7/8 critical block

## Purpose

Merged Stage14-s7-13 improves the physical whole-family count to

```text
V(B) << B^(7/8+o(1)).
```

Its equality block is

```text
P,Q ~ B^(1/2),
a,b ~ B^(3/8),
x,y ~ B^(1/16),
```

for the canonical decomposition

```text
P=a*x^2,
Q=b*y^2,
```

with squarefree coprime `a,b`.  The product-square relation with the partner coordinate is

```text
ab=cd=xi.
```

Stage14-4cb compresses the full-coordinate critical geometry further to the single shared squarefree label `xi`, proves that the existing support receiver and selected adjacent-two-cell receiver meet exactly at `xi~B^(3/4)`, and freezes the precise theorem contract needed to move below `7/8`.

No new whole-family exponent is claimed here.

---

## 1. Merged inputs

We use only merged results.

1. Stage14-s7-13:
   - canonical short-coordinate orientation `P<Q`, `Q<=B^(1/2+o(1))`;
   - full canonical decomposition `P=a*x^2`, `Q=b*y^2`;
   - fixed-coordinate physical multiplicity `B^o(1)`;
   - current whole-family exponent `7/8`.
2. Stage14-s7-10 / Stage14-4by:
   - exact shared-label four-cell factorisation
     `a=r*s`, `b=t*j`, `c=r*t`, `d=s*j`;
   - either `a` or `b` may be selected as a valid adjacent two-cell coefficient;
   - if a selected coefficient `C>=B^rho`, then
     `#states << B^(1-rho/3+o(1))`.
3. Stage14-s7-11 / Stage14-4bz:
   - pairwise two-cell savings are not multiplied without a transverse theorem;
   - naive higher-cell square-sieve enlargement does not improve the current two-cell receiver.

The open Stage14-t49 draft is not used as theorem input.

---

## 2. Shared-label dyadic parameter

For one reduced coordinate write

```text
P=a*x^2,
Q=b*y^2,
gcd(P,Q)=1,
```

where `a,b` are squarefree and coprime.  Put

```text
xi = a*b.
```

The partner coordinate has the same label,

```text
R=c*z^2,
S=d*w^2,
cd=xi.
```

Dyadically write

```text
xi ~ B^gamma,
0 <= gamma <= 1+o(1).                              (2.1)
```

The upper range follows from

```text
xi=a*b <= P*Q <= B^(1+o(1)).                       (2.2)
```

Because `xi` is squarefree, a fixed label has only

```text
2^omega(xi)=B^o(1)                                 (2.3)
```

ordered coprime factorizations `xi=a*b`.

---

## 3. Label-support upper bound

Fix `xi~B^gamma` and one factorization

```text
a~B^alpha,
b~B^beta,
alpha+beta=gamma.                                  (3.1)
```

Since

```text
P=a*x^2 <= B^(1/2+o(1)),
Q=b*y^2 <= B^(1/2+o(1)),
```

we have

```text
x <= B^((1/2-alpha)/2+o(1)),
y <= B^((1/2-beta)/2+o(1)).                        (3.2)
```

Hence for a fixed label and factorization the number of possible square-part pairs `(x,y)` is at most

```text
B^((1-gamma)/2+o(1)).                              (3.3)
```

There are at most `B^(gamma+o(1))` squarefree labels in a dyadic shell of size `B^gamma`.  Summing (3.3) over labels and the `B^o(1)` factorizations gives

```text
boxed:
N_label-support(gamma)
 << B^(1/2+gamma/2+o(1)).                           (3.4)
```

The fixed-coordinate genus-one receiver transfers this support bound to the physical whole-family count with only `B^o(1)` loss.

This is exactly the s7-13 support geometry rewritten in the natural shared-label variable.

---

## 4. Selected adjacent two-cell upper bound in terms of xi

For the same block,

```text
alpha+beta=gamma.
```

Therefore

```text
max(alpha,beta) >= gamma/2.                        (4.1)
```

Both `a` and `b` are valid adjacent two-cell products in the exact four-cell factorisation.  Select the larger one canonically.  The merged two-cell theorem then gives

```text
boxed:
N_2cell(gamma)
 << B^(1-gamma/6+o(1)).                             (4.2)
```

Indeed a coefficient of exponent at least `gamma/2` supplies relative saving at least

```text
B^(-(gamma/2)/3)=B^(-gamma/6).                     (4.3)
```

No saving from `a` and `b` is multiplied.

---

## 5. Exact shared-label minimax

On every `xi~B^gamma` common-refinement block we therefore have two valid upper bounds on the same set:

```text
E_support(gamma)=1/2+gamma/2,
E_2cell(gamma)=1-gamma/6.                           (5.1)
```

Thus

```text
boxed:
E(gamma)=min(1/2+gamma/2, 1-gamma/6).              (5.2)
```

The support branch is increasing and the two-cell branch decreasing.  They meet when

```text
1/2+gamma/2 = 1-gamma/6
<=> 3+3gamma = 6-gamma
<=> 4gamma=3.
```

Hence

```text
boxed:
gamma=3/4.                                         (5.3)
```

At this point

```text
1/2+3/8 = 7/8,
1-(3/4)/6 = 7/8.                                   (5.4)
```

Therefore the existing support-plus-selected-two-cell architecture has the exact shared-label barrier

```text
boxed:
E >= 7/8.                                          (5.5)
```

This independently reproduces the merged s7-13 exponent, but with the obstruction compressed to one variable `xi`.

---

## 6. Equality geometry

Equality in (5.5) requires

```text
xi ~ B^(3/4).                                      (6.1)
```

To saturate the selected-coefficient relaxation `max(alpha,beta)>=gamma/2`, one must also have

```text
alpha=beta=3/8.                                    (6.2)
```

To saturate the support bound, both coordinate entries must reach the short-coordinate ceiling,

```text
P,Q ~ B^(1/2),                                     (6.3)
```

which forces

```text
x,y ~ B^(1/16).                                    (6.4)
```

Thus the shared-label critical block is exactly the s7-13 equality block:

```text
boxed:
xi ~ B^(3/4),
a,b ~ B^(3/8),
P,Q ~ B^(1/2),
x,y ~ B^(1/16).                                    (6.5)
```

This is now the unique exponent-critical geometry for the present main-line receiver.

---

## 7. Why further dyadic refinement alone cannot improve 7/8

The derivation above already keeps the exact common label `xi` before applying either bound.  Further splitting of

```text
alpha,beta,x,y
```

cannot improve the worst exponent while only the following two ingredients are used:

1. ambient/shared-label support count;
2. one selected adjacent two-cell saving `C^(-1/3)`.

At the balanced equality configuration

```text
alpha=beta=3/8
```

both selected coefficients have exactly the same strength, and s7-11 forbids multiplying their correlated pairwise savings without a new transverse theorem.

Similarly, direct three-/four-cell square-sieve enlargement is already known to be weaker.

Hence

```text
SHARED_LABEL_SUPPORT_PLUS_ONE_TWO_CELL_ARCHITECTURE_BARRIER=7/8.
```

---

## 8. Quantitative next-theorem contracts

The compression makes the next useful theorem requirements explicit.

### 8.1 Realized-label sparsity contract

Suppose one proves, uniformly in the critical label range, that the number of **physically realizable** squarefree labels obeys

```text
# {xi~B^gamma : xi occurs physically}
 << B^((1-delta)*gamma+o(1))                       (8.1)
```

for some fixed `delta>0`.

Then the support exponent improves to

```text
E_support,delta(gamma)
 = 1/2 + gamma/2 - delta*gamma.                    (8.2)
```

Combining with the existing two-cell theorem gives, while the crossing remains inside `0<=gamma<=1`,

```text
gamma_delta = 3/(4-6delta),                        (8.3)
E_delta = 1 - 1/(8-12delta).                       (8.4)
```

Every `delta>0` therefore gives a strict whole-family improvement over `7/8`.

For example,

```text
delta=1/12
=> gamma_delta=6/7
=> E_delta=6/7.                                    (8.5)
```

No such realized-label sparsity theorem is claimed in Stage14-4cb.

### 8.2 Stronger transverse coefficient contract

Alternatively, suppose the selected coefficient theorem were improved from

```text
C^(-1/3)
```

to

```text
C^(-1/3-eta)                                       (8.6)
```

for some fixed `eta>0`, by a genuinely transverse squareclass/mean-square theorem rather than by multiplying the existing `a` and `b` estimates.

Then the shared-label analytic branch would become

```text
1-gamma*(1/6+eta/2),                               (8.7)
```

and its crossing with the unchanged support branch would be

```text
gamma_eta = 3/(4+3eta),                            (8.8)
E_eta = (7+3eta)/(8+6eta) < 7/8.                   (8.9)
```

Thus either a positive realized-label sparsity exponent or a positive transverse coefficient gain is sufficient.

---

## 9. Relation to the t-series

Merged t46--t48 reduce the moving squareclass problem to a twist-independent quadratic-character operator and identify the need for signed common-refinement aggregation.  Open t49 is exploring an external Frobenius amplifier / mean-square receiver.

Stage14-4cb does not import open t49 as a theorem.  It only records the exact main-line target that such a future theorem would need to hit:

```text
xi ~ B^(3/4)
```

with a power saving either in realized-label occupancy or in the correlated squareclass incidence over that label family.

### tH status

No new tH task is required at this stage.  tH13 already owns the relevant same-modulus/product-kernel dispersion adapter.  A new tH stage should be triggered only if the next shared-label theorem requires a receiver not expressible through that existing machinery.

---

## 10. Current ledger and next stage

The current unconditional whole-family theorem remains the merged s7-13 result

```text
boxed:
V(B) << B^(7/8+o(1)).                              (10.1)
```

The cumulative saving from the post-local baseline is

```text
41/42 - 7/8 = 17/168.                              (10.2)
```

The remaining gap to square root is

```text
7/8 - 1/2 = 3/8.                                   (10.3)
```

No new power saving is claimed in this stage.

The next main-line target is the critical shared-label family itself:

```text
NEXT=Stage14-4cc
```

with the preferred order:

1. test/prove realized `xi` sparsity near `B^(3/4)`;
2. if ambient label support is genuinely saturated, attack a transverse squareclass mean-square theorem on that family.

---

## Stage boundary

```text
STAGE14_4CB=SHARED_LABEL_COMPRESSION_AND_7_8_CRITICAL_BARRIER
MERGED_S7_13_7_8_IMPORTED=true
SHARED_LABEL=xi=ab=cd
SHARED_LABEL_DYADIC_EXPONENT=gamma
SHARED_LABEL_SUPPORT_EXPONENT=1/2+gamma/2
SHARED_LABEL_TWO_CELL_EXPONENT=1-gamma/6
SHARED_LABEL_RECEIVER_COMBINATION=min
SHARED_LABEL_CRITICAL_EXPONENT=3/4
CRITICAL_SELECTED_COEFFICIENT_EXPONENT=3/8
CRITICAL_SQUAREPART_ROOT_EXPONENT=1/16
SHARED_LABEL_SUPPORT_PLUS_ONE_TWO_CELL_ARCHITECTURE_BARRIER=7/8
REALIZED_LABEL_SPARSITY_POWER_SAVING_PROVED=false
TRANSVERSE_COEFFICIENT_GAIN_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=17/168
CURRENT_GAP_TO_SQRT=3/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH14_NEEDED=false
NEXT=Stage14-4cc
```
