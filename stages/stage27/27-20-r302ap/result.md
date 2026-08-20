# Stage27-20-r302ap — exact Ramanujan recombination of one additive-frequency gcd stratum

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ao
SOURCE_STAGE=Stage20

Fix one retained MAIN packet, so

```text
q = 2UV/gcd(U,V)
```

and the merged quadratic congruence has the form

```text
f^2 = C (mod q),
C = G_- + lambda_h N.
```

The exact additive projector is

```text
1_{f^2=C (mod q)}
 = (1/q) sum_{a mod q} e_q(a(f^2-C)).
```

For a divisor `d|q`, isolate the whole gcd stratum `(a,q)=d`. Put `Q=q/d`. Every such `a` is uniquely `a=d alpha` with `alpha mod Q` primitive, including `d=q`, `Q=1` for the zero frequency. Therefore, with `z=f^2-C`,

```text
R_{d,C}(f)
 := (1/q) sum_{a mod q:(a,q)=d} e_q(a z)
  = (1/q) sum_{alpha mod Q:(alpha,Q)=1} e_Q(alpha z)
  = c_Q(z)/q,
```

where `c_Q` is the classical Ramanujan sum.

This is the exact full-stratum object that must replace the fixed-`a` magnitude argument in r302v. It performs the complete primitive `a'` sum before any Hilbert-space estimate and hence respects the SR-GATE-35A/36A quantifier order.

No change of physical measure occurs. All common-parent, primitive, chamber, parity, and physical masks remain outside this finite identity exactly as before.

The stratum multiplier can also be written arithmetically as

```text
c_Q(z) = sum_{r | gcd(Q,z)} r * mu(Q/r),
```

or equivalently by the standard closed Ramanujan formula. Thus the stratum kernel is no longer naturally a unit-modulus inverse-frequency phase; after the `a`-sum it is a divisor/valuation-sensitive real arithmetic multiplier.

This explains why the fixed-a phase geometry was useful for external Kloosterman searches but cannot by itself determine the final full-stratum Gram diagonal.

```text
STAGE27_20_R302AP_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
FULL_GCD_STRATUM_RAMANUJAN_RECOMBINATION_PROVED=true
ZERO_FREQUENCY_INCLUDED_AS_Q_EQUALS_1_STRATUM=true
H_PHYS_MAIN_MEASURE_PRESERVED=true
FIXED_A_UNIT_PHASE_NOT_PROMOTED_TO_FULL_STRATUM=true
NEW_FIXED_POWER_SAVING_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
CURRENT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302aq
NEXT_BATCH=Stage27-20-r302-main-batch
```