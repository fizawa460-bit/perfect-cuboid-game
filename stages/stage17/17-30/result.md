# Stage17-30 — ratio / thinning law

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## Population lock

Stage17 keeps the audited Stage17-10 contract unchanged:

- `0<a<b<c`;
- `gcd(a,b,c)=1`;
- exactly one of `a^2+b^2`, `a^2+c^2`, `b^2+c^2` is a square;
- `R=sqrt(a^2+b^2+c^2)<=B`;
- `R` is integral, so the positive space diagonal is exactly `d=R`.

Write `M_1(B)` for the Stage16 source count and `N_1(B)` for the Stage17 survivor count.

## Frozen numerator theorem from Stage13

Stage13 uses the same primitive/canonical exactly-one population with integral space diagonal and cutoff `d<=B`. Its final theorem proves

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\]

with positive leading constant. The Stage17 adapter is identity-only: on the target `d=R`, hence `d<=B` iff `R<=B`. No population, cutoff, primitivity, canonicalization, or face-multiplicity conversion is required.

Primary source: `stages/stage13/final.md`, especially the Stage13-7 exactly-one transfer and Stage13-8 object/cutoff/primitivity compatibility ledger. Stage14 R06 independently records the same Stage13 interface in `stages/stage14/final.md`.

Therefore

\[
N_1(B)\asymp B(\log B)^3.
\]

## Frozen denominator theorem from Stage16

The audited Stage16 closeout proves on the literal source population

\[
M_1(B)\asymp B^2\log B.
\]

No leading constant for `M_1(B)` is certified.

## Survivor ratio

Dividing the two matched-measure laws gives

\[
\boxed{
\frac{N_1(B)}{M_1(B)}\asymp \frac{(\log B)^2}{B}\to0.
}
\]

Equivalently, the integral-space-diagonal condition leaves a zero-density subset of the Stage16 exactly-one population, with ratio `B^{-1+o(1)}` and the sharper proved logarithmic profile `(log B)^2/B` at Theta resolution.

This is a **PROVED** ratio/thinning law, not an inference from Stage17-20 finite data.

## Exact claim boundary

Checkpoint 30 does **not** claim

- `N_1(B)/M_1(B) ~ C (log B)^2/B` for any explicit constant `C`;
- a leading constant for `M_1(B)`;
- that the space-diagonal constraint is probabilistically independent of the one-face condition;
- a causal explanation for the lost power of `B`;
- a stronger upper or lower bound than the inherited matched theorems;
- any perfect-cuboid existence or nonexistence conclusion.

The finite ratios from Stage17-20 remain diagnostic only. Their decrease is consistent with the proved zero-density law but is not used in the proof.

## Dependency ledger

```text
SOURCE_POPULATION=Stage16 B_1(B)
TARGET_POPULATION=Stage17 B_{1,d}(B)
COMMON_CUTOFF=R<=B; on target d=R exactly
NUMERATOR_THEOREM=Stage13 N_1(B) ~ (kappa/(24*pi)) B(log B)^3
DENOMINATOR_THEOREM=Stage16 M_1(B) asymp B^2 log B
SURVIVOR_RATIO=N_1(B)/M_1(B) asymp (log B)^2/B
RATIO_LIMIT_STATUS=PROVED_ZERO_DENSITY
EVIDENCE_LEVEL=PROVED
LEADING_RATIO_CONSTANT=NOT_CERTIFIED
FINITE_DATA_USED_AS_PROOF=false
POPULATION_ADAPTER=IDENTITY_ONLY
```

Checkpoint 40 must wait for fresh `Stage17-audit` of this theorem transfer and ratio derivation.
