# Stage27-20-r302az — exact Parseval decomposition of the residue collision statistic

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ay
SOURCE_STAGE=Stage20

The fourth-moment collision index from r302ax has an exact Fourier interpretation that separates a deterministic baseline from the genuinely correlated residue-energy modes.

Put

```text
u(f)=|W(f)|^2,
E=sum_f nu(f),
nu_hat(h)=sum_{f mod q} nu(f)e_q(-hf).
```

For `E>0`, Parseval on `Z/qZ` gives

```text
Lambda(W)
 = [sum_f nu(f)^2]/E^2
 = (1/q) sum_{h mod q} |nu_hat(h)|^2/E^2.
```

Since

```text
nu_hat(0)=E,
```

one has the exact decomposition

```text
Lambda(W)
 = 1/q
   + (1/q) sum_{h!=0} |nu_hat(h)|^2/E^2.
```

Therefore the singularity-normalized statistic is

```text
Z(W,C)
 = s_q(C)^3/q
   + [s_q(C)^3/q]
     sum_{h!=0}|nu_hat(h)|^2/E^2.
```

The first term is an unavoidable uniform-residue baseline. The second term is a nonnegative normalized nonzero-frequency energy of the **physical residue energy** `|W|^2`.

This yields an immediate necessary condition for a packet-level fixed-power collision deficit:

```text
s_q(C)^3/q
```

must itself be power-small. No Fourier cancellation can remove this zero-frequency baseline.

On the regular branch `s_q(C)=1`, the baseline is exactly `1/q`. On highly singular squarefull packets, `s_q(C)^3/q` can be much larger, so those packets must either be exceptional in the physical measure or be treated by a different local argument.

This is another substantive use of the StructureRadar Fourier normalization: the missing positive moment theorem is now split into a structural modulus/singularity baseline and a normalized nonzero-frequency energy, with no invented descended Parseval identity.

```text
STAGE27_20_R302AZ_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
RESIDUE_COLLISION_PARSEVAL_IDENTITY_PROVED=true
COLLISION_ZERO_MODE_BASELINE=s_q(C)^3/q
COLLISION_NONZERO_FREQUENCY_ENERGY_EXPOSED=true
ZERO_MODE_CANCELLATION_AVAILABLE=false
REGULAR_BASELINE_EQUALS_1_OVER_Q=true
ZERO_MODE_FIXED_POWER_DEFICIT_PROVED=false
NONZERO_ENERGY_FIXED_POWER_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
CURRENT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302ba
NEXT_BATCH=Stage27-20-r302-main-batch
```