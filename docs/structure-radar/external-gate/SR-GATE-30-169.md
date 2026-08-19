# StructureRadar external-gate closure 30 — SR-STR-169 MAIN-native correlation attack

BATCH_ID=SR-BATCH-EXTERNAL_GATE_CLOSURE-30-R01
PHASE=EXTERNAL_GATE_CLOSURE
STRUCTURE=SR-STR-169
MODE=ONE_GATE_DEEP_ATTACK
TARGET=UniformWallSlabMAINArithmeticHostCorrelationPowerDeficit
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE
EXTERNAL_GATE_COUNT_BEFORE=13
EXTERNAL_GATE_COUNT_AFTER=13

This batch resumes from the post-close triage and attacks the current Stage27-20 checkpoint40 receiver directly in the charged MAIN physical measure. It does not reuse the fixed-U/T-route weight as if it were the MAIN host.

## 1. Exact same-measure two-copy receiver

For each wall fiber `x=(P,U)` retain the audited notation

```text
H_x = H_phys^MAIN(P,U;B),
F_x = F_MAIN(P,U;B),
rho_x = F_x/H_x
```

when `H_x>0`. If `Omega_x` is the corresponding physical-host fiber and `A_x(omega)` is the exact frozen MAIN survivor indicator, then

```text
rho_x = (1/H_x) * sum_{omega in Omega_x} A_x(omega)
```

and therefore the weighted second moment has the exact two-copy identity

```text
sum_x H_x rho_x^2
 = sum_x (1/H_x) * sum_{omega_1,omega_2 in Omega_x}
     A_x(omega_1) A_x(omega_2).
```

Consequently, for any fixed `delta>0`, a bound

```text
sum_x H_x rho_x^2 <= B^(-2 delta+o(1)) * sum_x H_x
```

implies, for every fixed `0<alpha<delta`,

```text
sum_{x: rho_x>B^(-alpha)} H_x
 <= B^(-2(delta-alpha)+o(1)) * sum_x H_x.
```

Thus the r302 high-occupancy theorem is reduced without changing measure to a two-copy physical correlation estimate. This is an exact reduction, not a new saving.

## 2. Import the already-proved CRT normalization, but keep the MAIN weight

Merged `SR-STR-019` deep closure already proves that the two frozen quadratic congruences may be combined exactly. With

```text
N=t_p t_q,
h=gcd(U,V),
q=lcm(2U,2V)=2UV/h,
```

the incompatible cells vanish and every surviving cell is equivalent to one merged quadratic congruence of the recorded form

```text
f^2 = G_- + lambda_h N (mod q),
```

with the nested common-parent divisor allocation retained. This algebraic normalization is reused here only inside the same MAIN physical host.

For a fixed surviving label packet, additive orthogonality gives the exact frequency expansion

```text
1_{f^2-G_--lambda_h N = 0 (mod q)}
 = (1/q) sum_{a mod q} e_q(a(f^2-G_--lambda_h N)).
```

The `a=0` term is the principal mode already internal to the charged host/root ledger. It is not a new density gain and cannot be charged again. Any new fixed-power saving must therefore enter through the nonzero-frequency physical covariance after the two-copy expansion.

This localizes the analytic problem more sharply than the bare statement `same-measure correlation`: the live object is a MAIN-weighted, nonzero-frequency quadratic/projective covariance with all nested-divisor, primitive, chamber, parity and physical masks still attached.

## 3. Focused primary-literature check

The existing q13 radar was rechecked against the most relevant primary sources rather than re-running a broad census.

### Dong--Robles--Zeindler 2026

`arXiv:2601.00292`, *Bilinear forms with Kloosterman fractions and applications*, proves power-saving bounds for bilinear Kloosterman-fraction forms with arbitrary complex coefficient sequences. This removes the older squarefree-support restriction and remains the closest direct analytic engine after a successful projective/complementary-divisor transform.

It is not directly applicable here. The MAIN covariance has a correlated modulus `q=2UV/h`, quadratic frequency `f^2`, nested common-parent coefficients, and a physical host normalization. No audited argument currently converts that exact nonzero-frequency covariance into the paper's inverse-fraction denominator geometry with coefficient `L1/L2` norms and dyadic ranges strong enough to preserve a fixed power.

### Wright 2026

`arXiv:2604.25177`, *Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions*, proves improved dispersion estimates with a fixed denominator factor and gives arithmetic-progression distribution averaged over a polynomial modulus family, assuming a Siegel--Walfisz input for one sequence.

This is not a direct MAIN theorem: the r302 receiver allows a weighted exceptional-mass formulation but still requires the exact `H_phys^MAIN` measure. The current physical coefficient has no proved Siegel--Walfisz factorization, and averaging an external modulus family does not by itself control the correlated MAIN wall fibers.

### Pascadi 2024 and de la Bretèche--Tenenbaum 2024

Pascadi `arXiv:2404.04239` becomes relevant only after an explicit Kuznetsov/spectral transform with a verified sparse-Fourier physical coefficient. De la Bretèche--Tenenbaum `arXiv:2403.19320` gives strong nonnegative multivariable polynomial-value mean bounds, useful for multiplicity envelopes, but does not supply the signed same-measure covariance deficit.

No checked source directly closes the exact MAIN receiver.

## 4. New precise missing lemma

The normal ChatGPT attack therefore reaches the following smaller bridge:

```text
FIRST_MISSING_LEMMA=MAINWallPhysicalCenteredFrequencyToKloostermanFractionTransfer
```

A sufficient form is:

> On every retained fixed-width MAIN wall dyadic/decorative block, transform the exact nonzero-frequency two-copy covariance obtained from the merged CRT quadratic congruence into `B^o(1)` bilinear/trilinear Kloosterman-fraction forms whose coefficient norms are dominated by the original `H_phys^MAIN` energy, whose correlated modulus/common-core variables remain in their actual quantifier order, and whose parameter ranges fall in a published power-saving theorem with one uniform positive exponent.

If this transfer is proved, Dong--Robles--Zeindler is the first theorem to test term-by-term on the resulting bilinear pieces; Wright is a secondary option only if a genuine polynomial modulus average plus Siegel--Walfisz factorization is exposed.

The first failure point is therefore no longer generic `same-measure correlation`; it is the exact physical-frequency-to-inverse-fraction transform and its coefficient/range control.

## 5. Firewalls and verdict

- The two-copy identity and additive-frequency localization are exact, but they do not themselves give a power saving.
- The principal/zero mode is already charged and is not reused as a new factor.
- Fixed-U/T-route weights remain distinct from `H_phys^MAIN`.
- Average-modulus theorems cannot replace the required same-measure transfer without a proved physical exceptional-mass adapter.
- `SR-STR-169` remains `EXTERNAL_GATE`.
- `CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2`.
- `STRICT_SUBSQRT_POWER_SAVING_PROVED=false`.
- No perfect-cuboid existence/nonexistence claim is made.

```text
MAIN_NATIVE_TWO_COPY_IDENTITY=PROVED
GENERALIZED_CRT_NORMALIZATION_REUSED=true
NONZERO_FREQUENCY_LOCALIZATION=PROVED
DIRECT_FULL_TARGET_THEOREM_COUNT=0
DRZ_EXACT_MAIN_TRANSFER_PROVED=false
WRIGHT_MAIN_SIEGEL_WALFISCH_ADAPTER_PROVED=false
FIRST_MISSING_LEMMA=MAINWallPhysicalCenteredFrequencyToKloostermanFractionTransfer
SR_STR_169_STATUS=EXTERNAL_GATE
GATES_CLOSED=0
WORK_FALLBACK_RECOMMENDED=true
WORK_TARGET=SR-STR-169 / MAINWallPhysicalCenteredFrequencyToKloostermanFractionTransfer
WORK_REQUEST=Search and test primary-source bilinear/trilinear Kloosterman-fraction, dispersion, and spectral theorems only against the exact MAIN nonzero-frequency covariance after the merged CRT normalization. Require a theorem or transform that preserves the H_phys^MAIN weighted measure, correlated q=2UV/gcd(U,V), nested common-parent divisor coefficients, physical masks, coefficient L1/L2 norms and a uniform fixed-power saving. Start from Dong--Robles--Zeindler arXiv:2601.00292 and Wright arXiv:2604.25177; do not redo broad generic divisor/correlation literature and do not substitute average-modulus results without an exceptional-mass adapter.
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
