# Stage14-s7-148 — joint filtered-tau3 / q17 reciprocal-CRT incidence normal form

## Status

`COMPLETE_POSITIVE_FIRST_MOMENT_JOINT_INCIDENCE_NORMAL_FORM`

Consumes Stage14-s7-147 and the exact first-layer filtered-tau3 witness models from merged Stage14-s7-126..131, together with the q17 reciprocal-CRT kernel reidentification consumed through Stage14-s7-135..146.

## 1. First-layer witness coordinate

For a scalar A/C principal cell, a retained first-layer witness can be written in the already-frozen form

```text
lambda = (z; g,x,y; frozen labels),
g*x*y = c_C*z,
R_mult(lambda)=1.
```

For polynomial branch D retain instead

```text
lambda = (E,m; g,x,y; frozen labels),
g*x*y = c_C*E*m,
R_mult^pair(lambda)=1,
```

with `(E,m)` kept as the charged outer coordinates.

No new multiplicity estimate is introduced here.

## 2. q17 good witness coordinate

For each retained `lambda`, the complete q17 packet `theta=pi(lambda)` determines the already-frozen second-reverse product `W1(lambda)` and fixed coprime agreement pair `(U,V)`.

After the exact cancellation from Work-cfX44 / s7-135, a reciprocal-CRT witness can be parameterized by positive integers `(f,n)` satisfying

```text
f*n = W1(lambda),
n+f == 0 (mod 2U),
n-f == 0 (mod 2V),
```

together with every already-frozen q17 kernel-side positivity, parity, endpoint-small, divisor-allocation, orientation and packet-label predicate. Denote their conjunction by

```text
R_q17(lambda;f,n)=1.
```

The residual root/canonical/post-column mask is not part of `R_q17`.

Hence exactly

```text
N_G(pi(lambda))
 = sum_{f*n=W1(lambda)} R_q17(lambda;f,n).
```

## 3. Exact joint incidence sum

Substituting into the witness first moment of s7-147 gives the nonnegative incidence count

```text
J1_G
 = sum_{lambda in Lambda}
     sum_{f*n=W1(lambda)} R_q17(lambda;f,n).
```

For scalar A/C this can be written as

```text
J1_scalar
 = sum_z
   sum_{g*x*y=c_C*z}
   R_mult(z;g,x,y)
   sum_{f*n=W1(z;g,x,y)} R_q17(z;g,x,y;f,n).
```

For branch D it is

```text
J1_pair
 = sum_{(E,m)}
   sum_{g*x*y=c_C*E*m}
   R_mult^pair(E,m;g,x,y)
   sum_{f*n=W1(E,m;g,x,y)} R_q17(E,m;g,x,y;f,n).
```

These are exact nonnegative sums on the charged cells. The pair sum is not scalarized through `Em`.

## 4. What has and has not been reduced

The q22 positive-first-moment normal-form test therefore passes structurally:

```text
Q22_POSITIVE_FIRST_MOMENT_NORMAL_FORM_TEST=PASS_JOINT_NONNEGATIVE_DIVISOR_CRT_INCIDENCE
S_JOINT_FILTERED_TAU3_Q17_CRT_INCIDENCE_NORMAL_FORM_EXACT=true
```

However no merged theorem supplies a uniform positive lower bound for these joint incidence sums. The filters `R_mult` and `R_q17` remain coupled through the retained witness labels and `W1(lambda)`.

Thus this is not promoted to an unfiltered `tau_3`, fixed-shift divisor correlation, or ordinary AP average.

```text
S_JOINT_INCIDENCE_POSITIVE_LOWER_BOUND_PROVED=false
UNFILTERED_TAU3_PROMOTION_PROVED=false
FIXED_SHIFT_PROMOTION_PROVED=false
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-149
```