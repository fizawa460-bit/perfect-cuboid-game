# Stage29-02e — V4 cohomology / cross-quotient rematch

```text
ROLE=R29_L2_V4_COHOMOLOGY_AND_CROSS_QUOTIENT_LFUNCTION_ADAPTER
STATUS=REDUCED_PASS_CANDIDATE_PENDING_FRESH_AUDIT
```

## 1. Exact V4 identity inherited from 29-02b

For compatible good odd finite-field models, Stage29-02b proves

```text
#X_joint
 = #X_face + #X_sp + #X_cross - 2#Y.
```

The endpoint/joint object is the full cuboid surface on the relevant normal/canonical model. The extra character in the pointwise identity

```text
(1+chi(f_face))*(1+chi(f_sp))
```

is exactly `chi(f_face*f_sp)`, geometrically represented by `X_cross`.

## 2. Non-Tate decomposition of the endpoint

Horie--Yamauchi give

```text
H2_nonT(endpoint)
 = 3 V_h16 + V_h32 + 3 V_h8.
```

The new exact K3 trace regression identifies the two marginal quotient orbits as

```text
Stage19 / X_sp / K_b -> V_h16,
Stage20 / X_face / K_c -> V_h32
```

at all tested primes, subject to fresh-audit promotion of `R29-L3`.

The base `Y` is rational and contributes no transcendental/non-Tate `H2`.

Therefore the V4 eigenspace subtraction predicts

```text
H2_nonT(X_cross)
 = (3 V_h16 + V_h32 + 3 V_h8)
   - V_h16
   - V_h32
 = 2 V_h16 + 3 V_h8.
```

This is ten-dimensional.

## 3. Independent dimension consistency

Stage29-02b predicts for the cross double cover

```text
pg_cross=5,
q_cross=0.
```

For a surface whose holomorphic two-forms contribute to the non-Tate Hodge piece, `2*pg=10`. The predicted modular piece

```text
2*h16 + 3*h8
```

also has dimension `2*(2+3)=10` because every weight-3 newform representation is two-dimensional.

Thus the V4 subtraction and the independently computed cross-cover Hodge invariant agree exactly at the dimension level.

## 4. What is and is not discharged

At the semisimple non-Tate level, `R29-L2` is reduced to the audit status of `R29-L3`:

```text
if K_b -> h16 and K_c -> h32 is globally certified,
then cross non-Tate motive -> 2 h16 + 3 h8.
```

This does **not** yet supply a complete integral/bad-prime L-function of the cross quotient. Resolution, boundary, algebraic Tate characters, and bad-prime local factors must remain model-explicit.

In particular, subtracting the smooth K3 algebraic traces from the singular endpoint trace without a common resolution/boundary ledger can create meaningless negative character multiplicities. This submission deliberately makes no such full algebraic subtraction claim.

## 5. Joint-local-arithmetic meaning

The Stage29 F4 cross character now has a candidate modular interpretation:

```text
joint covariance character chi(f_face*f_sp)
 <-> cross quotient X_cross
 <-> non-Tate modular package 2*h16 + 3*h8.
```

So the joint local correlation is no longer only an anonymous character sum. It is connected to explicit weight-3 modular representations, pending audit of the quotient-to-newform identification.

## Firewalls

```text
R29_L2_NON_TATE=PASS_CANDIDATE_CONDITIONAL_ON_R29_L3
FULL_CROSS_LFUNCTION_WITH_BAD_PRIMES=OPEN
CROSS_ALGEBRAIC_TATE_LEDGER=OPEN
LOCAL_TRACE_TO_HEIGHT_COUNT=false
EULER_PRODUCT_FOR_P_B_NOT_CLAIMED=true
RATIONAL_POINT_EXISTENCE_DECIDED=false
PERFECT_CUBOID_CONCLUSION=NONE
```
