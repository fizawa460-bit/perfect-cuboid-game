# Stage27-20-r302at — quadratic-root multiplicity is subpower times an explicit singular square-root factor

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302as
SOURCE_STAGE=Stage20

The root multiplicity factor in r302as can be made explicit by local valuation analysis.

Write

```text
q = product_{p^k || q} p^k.
```

For each `p^k||q`, let `v_p(C)` be capped at `k`, and define

```text
s_q(C)
 = product_{p^k || q}
     p^{ min(floor(k/2), floor(v_p(C)/2)) }.
```

For odd `p`, the local congruence

```text
x^2 = C (mod p^k)
```

has:

- at most two roots if `p` does not divide `C`;
- if `v_p(C)=2s<k`, at most `2 p^s` roots;
- if `v_p(C)>=k`, exactly `p^{floor(k/2)}` roots of `x^2=0 mod p^k`.

For the 2-primary factor, the same valuation extraction gives the safe bound

```text
#roots mod 2^k
 <= 4 * 2^{ min(floor(k/2), floor(v_2(C)/2)) }.
```

CRT therefore yields

```text
R_q(C)
 <= 4 * 2^{omega(q_odd)} * s_q(C)
 = B^{o(1)} s_q(C),
```

because every retained MAIN modulus has polynomial height in `B`.

In particular, on the regular/unit-root branch

```text
gcd(C,q)=1,
```

one has `s_q(C)=1` and hence

```text
R_q(C) <= B^{o(1)}.
```

The singular branch cannot be discarded: for example `C=0 mod p^k` has `p^{floor(k/2)}` roots, which may be polynomially large. The exact obstruction is therefore the explicit square-root singularity factor `s_q(C)`, not generic divisor entropy.

Substituting the bound into r302as shows that it is enough to prove

```text
s_q(C) * rho_root(W;C)
 <= B^{-2delta+o(1)}.
```

This absorbs all root-cardinality entropy into `B^{o(1)}` and isolates the only potentially polynomial local multiplicity.

```text
STAGE27_20_R302AT_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
LOCAL_QUADRATIC_ROOT_VALUATION_BOUND_PROVED=true
ROOT_MULTIPLICITY_ENVELOPE=4*2^omega(q_odd)*s_q(C)
REGULAR_UNIT_ROOT_MULTIPLICITY_SUBPOWER=true
SINGULAR_ROOT_MULTIPLICITY_AUTOMATICALLY_SUBPOWER=false
SINGULAR_SQUARE_ROOT_FACTOR_DEFINED=true
SINGULARITY_WEIGHTED_ROOT_ENERGY_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
CURRENT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302au
NEXT_BATCH=Stage27-20-r302-main-batch
```