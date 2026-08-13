# Stage14-4bx — reoptimize the merged thick-packet square sieve and obtain 15/16

## Purpose

Merged Stage14-s7-08 and Stage14-4bw give the current whole-family bound

```text
V(B) << B^(18/19+o(1)).
```

The `18/19` minimax used the thick-packet consequence of merged Stage14-4bv in the simplified form

```text
N_packet << M * H^(-1/2) * B^o(1),
H=min(X,Y,Z,W).
```

Stage14-4bx goes back one line further, to the stronger rectangle square-sieve inequality already proved in 4bv, and reoptimizes the auxiliary prime scale.  No new external character-sum theorem is used.

The key point is that the historical choice `L=H^(1/2)` was convenient but not optimal.  The exact optimum of the existing packet inequality is

```text
L=H^(4/5),
```

which gives

```text
N_packet << M * H^(-4/5) * B^o(1).
```

Reoptimizing the denominator, numerator, and square-part cutoffs with this stronger **already-available** thick saving improves the unconditional whole-family exponent to

```text
boxed:
V(B) << B^(15/16+o(1)).
```

The square-root upper bound is still not proved.

---

## 1. Merged inputs

Only merged results are used.

1. Stage14-4bv: for one fixed product-square coefficient packet and square-part boxes of lengths `X,Y,Z,W`, with

```text
M=XYZW,
```

the square sieve gives, for an inert auxiliary-prime scale `L`,

```text
N_packet
<< B^o(1) * [
     M/L
     +(XY/L^2+X+Y+L^2)
      (ZW/L^2+Z+W+L^2)
   ].                                               (1.1)
```

2. Stage14-4bv: summed unsieved packet volume is

```text
sum M << UV*B^o(1) << B^(1+o(1)).                 (1.2)
```

3. Stage14-s7-08 / Stage14-4bw: shared-`xi` four-cell switch, one-cell relative saving `T^(-1/2)`, fixed-coordinate partner multiplicity `B^o(1)`, and the general denominator/numerator/thin-cell decomposition.

4. Stage14-s7-09 is merged, but its unproved two-cell mixed Fourier estimate is **not** used.  Thus every theorem in 4bx is unconditional relative to the already merged Stage14 inputs.

---

## 2. Reoptimize the 4bv packet inequality

Put

```text
H=min(X,Y,Z,W),
A=XY,
C=ZW,
M=AC.
```

Because each side is at least `H`,

```text
X+Y <= 2XY/H = 2A/H,
Z+W <= 2ZW/H = 2C/H.                              (2.1)
```

Also

```text
A>=H^2,
C>=H^2.                                            (2.2)
```

Divide the two correlation brackets in (1.1) by `A` and `C`.  From (2.1)--(2.2),

```text
XY/L^2+X+Y+L^2
<= A * (L^(-2)+2H^(-1)+L^2/H^2),                 (2.3)
```

and the same bound holds with `A` replaced by `C`.

Now choose

```text
boxed:
L=H^(4/5).                                         (2.4)
```

Then

```text
L^(-2)   = H^(-8/5),
H^(-1)   = H^(-1),
L^2/H^2  = H^(-2/5).                              (2.5)
```

Hence each bracket in (1.1) is

```text
<< A*H^(-2/5)
```

or

```text
<< C*H^(-2/5),
```

respectively.  Their product is therefore

```text
<< M*H^(-4/5).                                     (2.6)
```

The square-sieve diagonal term is simultaneously

```text
M/L = M*H^(-4/5).                                  (2.7)
```

Thus the exact merged 4bv inequality yields the strengthened theorem

```text
boxed:
N_packet << M*H^(-4/5)*B^o(1).                    (2.8)
```

No new Fourier estimate is required: this is only a better choice of the auxiliary prime scale inside the already proved 4bv adapter.

### 2.1 Why `4/5` is the packet-level optimum of (1.1) from `H` alone

Write `L=H^a`.  In the worst balanced geometry `A,C~H^2`, the relative exponents in (1.1) are

```text
diagonal:    H^(-a),
correlation: H^(2*max(-2a,-1,2a-2)).
```

For `a>=1/2`, the correlation term is controlled by `H^(4a-4)`.  Balancing it with `H^(-a)` gives

```text
-a=4a-4,
```

hence

```text
a=4/5.
```

So (2.8) is the sharp uniform `H`-only consequence of the merged packet inequality (1.1).

---

## 3. New thick-sector exponent

If a sector has

```text
H>=B^tau,
```

then summing (2.8) over all coefficient packets and using (1.2) gives

```text
boxed:
N_thick(B;tau)
<< B^(1-4tau/5+o(1)).                              (3.1)
```

This replaces the historical thick exponent

```text
1-tau/2
```

by

```text
boxed:
1-4tau/5.                                          (3.2)
```

The thin-cell theorem itself is unchanged.

---

## 4. Reoptimized whole-family ledger

Use three cutoff exponents:

```text
lambda : small-denominator threshold,
nu     : small-numerator threshold,
tau    : square-part threshold.
```

Assume

```text
0<2tau<nu<=lambda<1/2.
```

The exhaustive sectors now have exponents

### Small denominator

```text
E1=2lambda.                                        (4.1)
```

### Balanced denominator, small numerator

```text
E2=1+nu-lambda.                                    (4.2)
```

### Thick square parts

By (3.1),

```text
E3=1-4tau/5.                                       (4.3)
```

### Thin numerator square part -> shared cell

Merged s7-08/4bw gives

```text
E4=1-(nu-2tau)/4.                                  (4.4)
```

### Thin denominator square part -> shared cell

```text
E5=1-(lambda-2tau)/4.                              (4.5)
```

Since `nu<=lambda`, `E5<=E4`.  Therefore the active minimax is

```text
E(lambda,nu,tau)
=max(
  2lambda,
  1+nu-lambda,
  1-4tau/5,
  1-(nu-2tau)/4
).                                                  (4.6)
```

---

## 5. Exact minimax: 15/16

The optimum is

```text
boxed:
lambda=15/32,
nu=13/32,
tau=5/64.                                         (5.1)
```

Indeed,

```text
2lambda                    = 15/16,
1+nu-lambda                = 15/16,
1-4tau/5                   = 15/16,
1-(nu-2tau)/4              = 15/16.                (5.2)
```

The denominator-thin branch is smaller:

```text
1-(lambda-2tau)/4
=59/64
<15/16.                                            (5.3)
```

### 5.1 Exact lower bound inside the current architecture

Suppose every active term in (4.6) were at most `E`.  Then

```text
lambda <= E/2,                                    (5.4)
nu <= E-1+lambda <= 3E/2-1,                       (5.5)
tau >= (5/4)(1-E),                                (5.6)
nu >= 2tau+4(1-E) >= (13/2)(1-E).                (5.7)
```

Combining (5.5) and (5.7),

```text
(13/2)(1-E) <= 3E/2-1,
```

which is equivalent to

```text
boxed:
E>=15/16.                                          (5.8)
```

Equality is attained by (5.1).  Therefore `15/16` is the exact threshold-tuning barrier for the current **optimized thick + one-cell thin** architecture.

---

## 6. New unconditional whole-family bound

The sector decomposition is exhaustive, so (5.1)--(5.3) give

```text
boxed:
V(B) << B^(15/16+o(1)).                            (6.1)
```

This strictly improves the merged `18/19` theorem.

The gain over `18/19` is

```text
18/19-15/16 = 3/304.                               (6.2)
```

The gain over the earlier `20/21` theorem is

```text
20/21-15/16 = 5/336.                               (6.3)
```

Relative to the post-local baseline `41/42`, the cumulative proved post-local saving is

```text
41/42-15/16 = 13/336.                              (6.4)
```

The remaining exponent gap to square root is

```text
15/16-1/2 = 7/16.                                  (6.5)
```

---

## 7. Interaction with merged s7-09

Merged s7-09 isolates a conditional adjacent-two-cell theorem:

```text
N_2cell(R,S) << (RS)^(2/3)B^o(1),
```

which would replace the one-cell coefficient saving exponent `1/4` by `1/3`.  Its published conditional global ledger `16/17` used the older thick exponent `1-tau/2`.

After the unconditional 4bx thick improvement, the same **still-unproved** two-cell theorem would instead lead to the conditional minimax

```text
boxed conditional:
lambda=13/28,
nu=11/28,
tau=5/56,
E=13/14.                                           (7.1)
```

Thus s7-09 remains highly relevant, but its `16/17` conditional ledger is no longer the correct forward target.  The updated conditional target is `13/14`.

No part of (7.1) is used to prove (6.1).

---

## 8. Stage boundary

Proved in Stage14-4bx:

- the merged 4bv rectangle square-sieve inequality admits the stronger uniform packet consequence `M*H^(-4/5)`;
- the optimal auxiliary prime scale is `L=H^(4/5)`;
- the thick-sector exponent improves from `1-tau/2` to `1-4tau/5`;
- exact whole-family minimax cutoffs are `lambda=15/32`, `nu=13/32`, `tau=5/64`;
- the unconditional whole-family upper bound improves to `15/16`;
- `15/16` is the exact barrier of the current optimized-thick + one-cell-thin threshold architecture;
- if the still-unproved s7-09 two-cell mixed Fourier theorem is later established, the updated conditional target is `13/14`, not `16/17`.

Not proved:

- the s7-09 uniform two-cell mixed Fourier bound;
- a whole-family exponent below `15/16`;
- the square-root upper bound.

```text
STAGE14_4BX=REOPTIMIZED_THICK_PACKET_SQUARE_SIEVE_AND_15_16_WHOLE_FAMILY_BOUND
MERGED_4BV_RECTANGLE_SQUARE_SIEVE_REUSED=true
NEW_EXTERNAL_CHARACTER_SUM_THEOREM_USED=false
OPTIMAL_THICK_AUXILIARY_PRIME_SCALE=H^(4/5)
THICK_PACKET_RELATIVE_SAVING=H^(-4/5)
THICK_SECTOR_EXPONENT=1-4*tau/5
OPTIMAL_DENOMINATOR_CUTOFF_EXPONENT=15/32
OPTIMAL_NUMERATOR_CUTOFF_EXPONENT=13/32
OPTIMAL_SQUAREPART_THRESHOLD_EXPONENT=5/64
OPTIMIZED_THICK_ONE_CELL_ARCHITECTURE_BARRIER=15/16
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=15/16
IMPROVEMENT_OVER_18_19=3/304
IMPROVEMENT_OVER_20_21=5/336
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=13/336
CURRENT_GAP_TO_SQRT=7/16
S7_09_TWO_CELL_MIXED_FOURIER_BOUND_PROVED=false
UPDATED_CONDITIONAL_TWO_CELL_WHOLE_FAMILY_EXPONENT=13/14
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4by use the new 15/16 ledger; if s7-10 proves the adjacent two-cell mixed Fourier O(p) theorem, import it and target 13/14, otherwise correlate the active small-denominator/small-numerator branches with the shared-cell packet
```
