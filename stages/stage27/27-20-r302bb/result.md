# Stage27-20-r302bb — exact division of labor: gcd-degeneracy baseline versus nonzero residue-energy correlation

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ba
SOURCE_STAGE=Stage20
STRUCTURE_RADAR_SOURCE=SR-STR-019,SR-STR-169,SR-STR-173

From r302az write

```text
Xi(W)
 = (1/q) sum_{h!=0}|nu_hat(h)|^2/E^2,
nu(f)=|W(f)|^2,
E=sum_f nu(f).
```

Then exactly

```text
Z(W,C)
 = tau(C,q) + Y(W,C),

tau(C,q)=s_q(C)^3/q,
Y(W,C)=s_q(C)^3 Xi(W).
```

Both terms are nonnegative. Therefore the weighted theorem in r302ay may be discharged either directly for `Z`, or by proving separately on the same physical packet measure

```text
sum H_packet tau(C,q)
 <= B^{-gamma_0+o(1)} sum H_packet,

sum H_packet Y(W,C)
 <= B^{-gamma_1+o(1)} sum H_packet
```

for fixed positive `gamma_0,gamma_1`. The combined exponent is the minimum; the two are not multiplied as independent savings.

The two pieces require different mathematics:

### Structural baseline `tau`

By r302ba,

```text
tau <= gcd(C,q)^{3/2}/q.
```

This is a local generalized-CRT / valuation degeneracy problem. The SR-STR-019 algebra is already legitimately imported to define the exact merged `C mod q`, but its frozen every-cell incidence theorem is not required merely to state or aggregate this bad mass.

### Nonzero energy `Y`

`Y` is the normalized nonzero Fourier energy of the positive physical residue-energy distribution `|W|^2`, multiplied by the explicit singularity scale. This is the same-measure correlation side. SR-STR-169 supplies the already-audited Fourier/Gauss architecture and SR-STR-173 supplies the support/moment/no-scalarization firewall, but neither currently proves this exact weighted `Y` deficit.

This split is useful because a future arithmetic argument for singular gcd packets need not solve the nonzero Fourier correlation problem, and a future spectral/moment argument need not manufacture cancellation in the unavoidable zero mode.

```text
STAGE27_20_R302BB_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
COLLISION_STATISTIC_SPLIT_INTO_TWO_NONNEGATIVE_PARTS=true
STRUCTURAL_BASELINE_TARGET=tau=s_q(C)^3/q
NONZERO_ENERGY_TARGET=Y=s_q(C)^3*Xi(W)
SR_STR_019_IMPORTED_ONLY_AS_EXACT_CRT_NORMALIZATION=true
SR_STR_169_IMPORTED_AS_NONZERO_FOURIER_ARCHITECTURE=true
SR_STR_173_IMPORTED_AS_MOMENT_SUPPORT_FIREWALL=true
ZERO_AND_NONZERO_SAVINGS_MULTIPLIED=false
ZERO_MODE_WEIGHTED_DEFICIT_PROVED=false
NONZERO_ENERGY_WEIGHTED_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
CURRENT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302bc
NEXT_BATCH=Stage27-20-r302-main-batch
```