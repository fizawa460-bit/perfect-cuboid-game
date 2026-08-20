# Stage27-20-r302n — repair the diagonal requirement in the same-measure Gram receiver

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302m
SOURCE_STAGE=Stage20

R302m imports the exact same-`H_phys^MAIN` full quadratic-form receiver

```text
Q_d(c)=sum_{b,b'} c_b conj(c_{b'}) G_d(b,b')
      <= B^{-2delta+o(1)} E_packet ||c||_2^2
```

uniformly for every coefficient vector `c` supported on the retained gcd stratum `d|b`.

The previous r302n formulation allowed a false escape through an unspecified baseline subtraction. That branch is removed. Because the receiver holds for every `c`, one may test the basis vector `c=e_b`. Then

```text
Q_d(e_b)=G_d(b,b),
```

so every successful proof of the r302m theorem necessarily satisfies

```text
sup_b G_d(b,b)
 <= B^{-2delta+o(1)} E_packet.
```

This is the correct reason the Gram diagonal cannot be ignored. Positive semidefiniteness alone does not forbid cancellation between diagonal and off-diagonal terms for a particular vector; the obstruction is the uniform quantifier over all coefficient vectors, which includes every `e_b`.

A clean sufficient two-part receiver is obtained by writing

```text
D_d = diag(G_d),
R_d = G_d-D_d.
```

It is enough to prove fixed `delta_1,delta_2>0`, uniformly on every retained MAIN packet and gcd stratum, such that

```text
||D_d||op = sup_b G_d(b,b)
 <= B^{-2delta_1+o(1)} E_packet,

||R_d||op
 <= B^{-2delta_2+o(1)} E_packet.
```

Then the triangle inequality gives

```text
||G_d||op
 <= ||D_d||op + ||R_d||op
 <= B^{-2 min(delta_1,delta_2)+o(1)} E_packet,
```

with the harmless factor 2 absorbed into `B^{o(1)}`. Hence this simultaneous diagonal/remainder theorem rigorously discharges the full r302m quadratic-form receiver.

No claim is made that this decomposition is necessary as a proof strategy; a direct same-measure full quadratic-form estimate may still prove r302m without separately estimating `R_d`. What is necessary is the basis-vector diagonal consequence above.

STAGE27_20_R302N_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
AUDIT_REPAIR_APPLIED=true
UNIFORM_ALL_C_QUANTIFIER_RETAINED=true
BASIS_VECTOR_DIAGONAL_NECESSITY_PROVED=true
PSD_NO_CANCELLATION_REASON_WITHDRAWN=true
BASELINE_SUBTRACTION_ESCAPE_REMOVED=true
DIAGONAL_DEFICIT_PROVED=false
OFFDIAGONAL_REMAINDER_OPERATOR_DEFICIT_PROVED=false
SAME_MEASURE_QUADRATIC_FORM_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302o
NEXT_BATCH=Stage27-20-r302-main-batch
