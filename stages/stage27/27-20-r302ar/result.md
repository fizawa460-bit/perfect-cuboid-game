# Stage27-20-r302ar — the exact root projector gives a negative certificate against a generic all-coefficient fixed-power norm

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302aq
SOURCE_STAGE=Stage20

The exact recombination in r302aq exposes the local arithmetic selector as multiplication by

```text
P_C(f)=1_{f^2=C (mod q)}.
```

On `ell^2(Z/qZ)`, if `Root_q(C)` is nonempty, the multiplication operator

```text
M_C: W -> P_C W
```

has exactly

```text
||M_C||_{2->2}=1.
```

Indeed `||P_C W||_2<=||W||_2`, while equality holds for every nonzero `W` supported on `Root_q(C)`.

Because finite Fourier transform is an invertible unitary change of coordinates after the standard normalization, the same local negative certificate is present in coefficient space: allowing an arbitrary Fourier coefficient vector is equivalent to allowing an arbitrary residue coefficient `W`. Choosing `W` supported on the quadratic roots prevents any uniform positive power contraction from the congruence projector itself.

Therefore the old strengthened receiver

```text
for every coefficient vector c,
Q_d(c) <= B^{-2delta+o(1)} E_packet ||c||_2^2
```

cannot be justified merely from the completed quadratic selector as a generic local operator theorem. Additional physical structure restricting the admissible coefficient class is essential.

This does not contradict SR-GATE-37A-169, where the all-`c` inequality was recorded as a **sufficient missing theorem** for the full same-measure kernel, not as something already implied by Gauss completion. It instead shows why the coefficient-specific fallback introduced later is not optional bookkeeping: the actual physical origin of `c_b=W_hat(b)/q` must be used.

The negative certificate is also consistent with r302h: changing from first to second moment does not itself create a saving. A fixed power must enter through arithmetic/physical sparsity of the actual survivor coefficient or through exceptional physical mass.

```text
STAGE27_20_R302AR_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
QUADRATIC_ROOT_PROJECTOR_L2_NORM=1
GENERIC_ALL_W_FIXED_POWER_CONTRACTION=false
GENERIC_ALL_C_SELECTOR_FIXED_POWER_CONTRACTION=false
ACTUAL_PHYSICAL_COEFFICIENT_STRUCTURE_REQUIRED=true
R302M_ALL_C_RECEIVER_RETAINED_ONLY_AS_STRONG_SUFFICIENT_TARGET=true
R302M_ALL_C_RECEIVER_CANONICAL_MINIMAL_TARGET=false
NEW_FIXED_POWER_SAVING_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
CURRENT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302as
NEXT_BATCH=Stage27-20-r302-main-batch
```