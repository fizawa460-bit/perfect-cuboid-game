# Stage27-20-r302v — primitive Gauss completion flattens the admissible Gram diagonal

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302u
SOURCE_STAGE=Stage20
STRUCTURE_RADAR_SOURCE=SR-GATE-33A-169,SR-GATE-34-169,SR-GATE-35A-169,SR-GATE-36A-169

The audited r302p-u chain leaves a coefficient-specific diagonal receiver

```text
sum_b |c_b|^2 G_d(b,b),
c_b=W_hat(b)/q.
```

The exact Fourier/Gauss separation gives one further algebraic simplification before any new theorem is requested.

Fix one retained MAIN packet, so the completed modulus `q` is fixed, and fix a Gauss gcd stratum `d=(a,q)`. Put `q'=q/d`, `a'=a/d`, and for surviving frequencies `b=d b'`. In the batch33A-35A completion, all dependence on the newly introduced Fourier variable `b` is carried by the descended primitive Gauss kernel; the physical coefficient itself has already been placed in `c_b=W_hat(b)/q`.

For the odd primitive local factors,

```text
G_{q'_odd}(a',b')
 = G_{q'_odd}(a',0)
   e_{q'_odd}(-b'^2 * inverse(4a')),
```

so its magnitude is independent of the admissible `b'`. On the primitive 2-primary factor the same statement holds after the exact parity split: inadmissible parity frequencies vanish, while admissible frequencies have a magnitude depending only on the fixed local modulus, not on the individual admissible frequency.

Consequently there is an exact local-admissibility set `Adm_d` and a factorization

```text
K_d(x,b)=1_{b in Adm_d} A_d(x) psi_d(x,b),
|psi_d(x,b)|=1,
```

where `A_d(x)` contains the charged physical/common-parent amplitude and all `b`-independent local Gauss magnitudes. Hence

```text
G_d(b,b)
 = 1_{b in Adm_d} D_d,
D_d = ||A_d||^2_{H_phys^MAIN}.
```

Thus the Gram diagonal is frequency-flat on the surviving primitive local class. The previous arbitrary bad-mode picture is therefore stronger than the actual completed kernel geometry: there is no large irregular family of diagonal sizes for Fourier energy to avoid after the exact primitive separation. The only possible coefficient-specific diagonal improvement beyond the scalar physical energy `D_d` is concentration of Fourier energy on locally inadmissible modes, which the kernel already kills.

No fixed-power estimate for `D_d/E_packet` is proved here, and no fixed-power admissible-class Fourier-energy deficit is asserted.

```text
STAGE27_20_R302V_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
PRIMITIVE_GAUSS_FREQUENCY_MAGNITUDE_FLAT=true
LOCAL_ADMISSIBILITY_SPLIT_EXACT=true
GRAM_DIAGONAL_FLAT_ON_ADMISSIBLE_CLASS=true
ARBITRARY_BAD_DIAGONAL_PROFILE_REQUIRED=false
SCALAR_DIAGONAL_PHYSICAL_ENERGY_DEFICIT_PROVED=false
ADMISSIBLE_CLASS_FOURIER_ENERGY_DEFICIT_PROVED=false
ACTUAL_COEFFICIENT_OFFDIAGONAL_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302w
NEXT_BATCH=Stage27-20-r302-main-batch
```