# Stage14-4bz — freeze the square-sieve dimension barrier beyond 13/14

## Purpose

Merged Stage14-4by and merged Stage14-s7-10 prove

```text
V(B) << B^(13/14+o(1)).
```

using two sharp square-root Fourier receivers:

- thick square-part packet: relative saving `H^(-4/5)`;
- thin shared-`xi` coefficient packet: adjacent two-cell relative saving `A^(-1/3)`.

This stage asks whether the next improvement can come simply by enlarging the character-sum block from one/two cells to three/four cells, or by retuning the same thresholds.

The answer is no.  The current `13/14` is the exact minimax barrier of the proved square-root square-sieve architecture, and naive multicell enlargement is weaker on the thin coefficient branch.

No new whole-family exponent is claimed in this stage.

---

## 1. Merged theorem inputs

Only merged repository results are used.

1. Stage14-4bx:
   `N_thick << B^(1-4*tau/5+o(1))`.
2. Stage14-s7-10 / Stage14-4by:
   adjacent two-cell square sieve
   `N_2cell(R,S) << (RS)^(2/3) B^o(1)`, hence coefficient relative saving `(RS)^(-1/3)`.
3. Stage14-s7-08 / 4bw:
   exact shared-`xi` four-cell factorization.
4. Stage14-4by global ledger:

```text
E1 = 2*lambda,
E2 = 1+nu-lambda,
E3 = 1-4*tau/5,
E4 = 1-(nu-2*tau)/3,
E5 = 1-(lambda-2*tau)/3.
```

Since `nu<=lambda`, `E5<=E4`.

---

## 2. Square-root square-sieve dimension law

Consider an ideal `d`-variable square-sieve block of volume `A`.  Let the auxiliary prime scale be `L`, so an off-diagonal square-sieve correlation uses modulus `m=pq~L^2`.

At the square-root complete-sum scale in `d` variables,

```text
complete mixed transform << m^(d/2) = L^d.
```

The standard square-sieve template therefore has the model form

```text
N_d(A) << B^o(1) * ( A/L + L^d ).                  (2.1)
```

Optimizing gives

```text
L=A^(1/(d+1)),
N_d(A) << A^(d/(d+1)) B^o(1),
relative saving = A^(-1/(d+1)).                    (2.2)
```

Equation (2.2) is used here only as the square-root-completion barrier template.  The two instances actually needed below are already proved in the repository:

- `d=2`: merged s7-10 / 4by gives `A^(2/3)` exactly;
- `d=4`: merged 4bx realizes the corresponding thick-packet `H^(-4/5)` consequence.

No unproved three-cell complete-sum theorem is imported.

---

## 3. Why adding cells does not improve the thin coefficient switch

In the shared-`xi` factorization

```text
a=r*s,
b=t*j,
c=r*t,
d=s*j,
xi=r*s*t*j,
```

a thin numerator square part forces one large coefficient, say

```text
a=r*s >= B^alpha.
```

What is forced large is the product of exactly the two adjacent cells `r*s`.

The proved two-cell receiver gives

```text
relative saving <= a^(-1/3+o(1)).                  (3.1)
```

If one merely enlarges the block to three cells, the third cell is not forced to have any positive power size.  In the worst case it is `B^o(1)`, so the block product is still only `>=B^alpha`.  Even an ideal square-root three-variable receiver would then give only

```text
a^(-1/4+o(1)),                                     (3.2)
```

which is weaker than (3.1).

Similarly a four-cell enlargement would give only `a^(-1/5+o(1))` without an additional lower bound on the two extra cells.

Therefore

```text
NAIVE_MULTICELL_ENLARGEMENT_BEATS_TWO_CELL=false.
```

A future multicell route must first prove an additional structural lower bound on the added cell product, or reduce the effective dimension by an exact relation.  Merely applying a higher-dimensional square-root theorem cannot help.

---

## 4. Why the thick `H^(-4/5)` receiver is already at its square-root dimension limit

For a thick square-part packet there are four moving square-part variables

```text
x,y,z,w
```

with dyadic lengths `X,Y,Z,W` and

```text
H=min(X,Y,Z,W).
```

Merged 4bx proves

```text
N_packet << M*H^(-4/5)B^o(1),
M=XYZW.                                             (4.1)
```

In the balanced worst case `X,Y,Z,W~H`, the packet volume is `M~H^4`.  The four-variable square-root square-sieve law (2.2) gives

```text
M^(4/5)=H^(16/5),
```

which is exactly the relative saving

```text
H^(-4/5).                                          (4.2)
```

Thus merged 4bx already reaches the square-root-completion scale of the four genuinely moving square-part variables.

Any strict uniform improvement of the exponent `4/5` therefore requires at least one of:

1. an exact dimension reduction among the four variables;
2. an additional structural sparsity theorem before the square sieve;
3. a family-level active-direction theorem that bypasses packet volume counting.

Simple auxiliary-prime retuning cannot improve (4.2).

---

## 5. Exact global 13/14 barrier certificate

The four active exponents of the current architecture are

```text
E1 = 2*lambda,
E2 = 1+nu-lambda,
E3 = 1-4*tau/5,
E4 = 1-(nu-2*tau)/3.                               (5.1)
```

Suppose all four were `<=E`.  Then

```text
lambda <= E/2,                                     (5.2)
nu <= E-1+lambda <= 3E/2-1,                        (5.3)
tau >= (5/4)*(1-E),                                (5.4)
nu >= 2*tau+3*(1-E) >= (11/2)*(1-E).               (5.5)
```

Combining (5.3) and (5.5),

```text
(11/2)*(1-E) <= 3E/2-1,
```

hence

```text
13 <= 14E,
boxed: E>=13/14.                                   (5.6)
```

Equality is attained by merged 4by at

```text
lambda=13/28,
nu=11/28,
tau=5/56.
```

Therefore

```text
CURRENT_SQUARE_ROOT_SQUARE_SIEVE_ARCHITECTURE_BARRIER=13/14.
```

This is stronger than saying that one particular threshold choice is optimal: the barrier is caused by the simultaneous square-root dimension limits of the thick four-variable block and the thin adjacent two-cell block, together with the small-denominator / small-numerator envelope.

---

## 6. Slack branch and exact next obstruction

The denominator-thin coefficient branch is

```text
E5=1-(lambda-2*tau)/3.
```

At the current optimum,

```text
E5=19/21,
13/14-E5=1/42.                                     (6.1)
```

So `E5` is not yet the obstruction.  The active equality set is exactly

```text
E1=E2=E3=E4=13/14.                                 (6.2)
```

A strict improvement below `13/14` therefore requires a genuinely new theorem that changes at least one active receiver formula, not another threshold retuning.

The two preferred routes are:

### Route A — family-level active-direction / small-coordinate sparsity

Improve the envelope behind `E1` or `E2`, i.e. prove that primitive reduced coordinates with a small denominator or numerator are not all capable of carrying a physical nonboundary partner.  This is a first-small-point / active-direction statement, not a fixed-fiber multiplicity statement.

### Route B — exact dimension reduction before the square sieve

Find a new physical identity that reduces the effective dimension of either

- the four square-part variables in the thick packet, or
- the two forced adjacent shared-`xi` cells in the thin coefficient packet,

before invoking square-root Fourier cancellation.

Naive three-/four-cell expansion is explicitly ruled out by Section 3.

---

## 7. Stage boundary

Proved in Stage14-4bz:

- the general square-root square-sieve optimization law `(A/L+L^d) -> A^(d/(d+1))` as the relevant barrier template;
- the merged two-cell `A^(-1/3)` receiver is optimal among naive multicell enlargements when only a two-cell product is forced large;
- the merged thick `H^(-4/5)` receiver already matches the four-variable square-root dimension limit;
- the current four active global exponent formulas force the exact minimax lower bound `13/14`;
- denominator-thin branch `19/21` has exact slack `1/42`;
- any next whole-family improvement requires a new structural receiver, not threshold retuning or naive multicell enlargement.

Not proved:

- any exponent below `13/14`;
- a dimension-reducing physical identity;
- family-level active-direction sparsity at the new critical scales;
- the square-root bound.

```text
STAGE14_4BZ=SQUARE_ROOT_SQUARE_SIEVE_DIMENSION_BARRIER_AND_NEXT_RECEIVER_LOCK
MERGED_4BY_13_14_IMPORTED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=13/14
THIN_TWO_CELL_RELATIVE_SAVING=A^(-1/3)
THICK_FOUR_VARIABLE_RELATIVE_SAVING=H^(-4/5)
NAIVE_MULTICELL_ENLARGEMENT_BEATS_TWO_CELL=false
THICK_SQUARE_ROOT_DIMENSION_LIMIT_REACHED=true
CURRENT_SQUARE_ROOT_SQUARE_SIEVE_ARCHITECTURE_BARRIER=13/14
DENOMINATOR_THIN_EXPONENT=19/21
DENOMINATOR_THIN_SLACK_BELOW_CURRENT_CEILING=1/42
THRESHOLD_RETUNING_BEATS_13_14=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4ca attack a genuinely new receiver: active-direction small-coordinate sparsity or an exact pre-sieve dimension reduction
```
