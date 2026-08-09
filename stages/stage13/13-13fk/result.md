# Stage13-13fk — R06 Gate A result

> STATUS: `COMPLETE_ANALYTIC_CHAMBER_NORMALIZATION`

R05 reviewer feedback identified a proof-facing gap: the normalization

\[
I_{ab}+I_{ac}+I_{bc}=\pi^2/8
\]

was numerically validated but not symbolically derived in the review-facing proof. This stage closes that objection without changing the theorem.

## Exact derivation

On the positive spherical octant `O`, define

\[
W=\frac1{\sqrt{x^2+y^2}}+\frac1{\sqrt{x^2+z^2}}+\frac1{\sqrt{y^2+z^2}}.
\]

`W` is symmetric in the three coordinates. The octant is partitioned, up to measure-zero equality walls, into the six coordinate-order chambers. Hence

\[
\int_O W\,d\omega=6(I_{ab}+I_{ac}+I_{bc}).
\]

For one pair, spherical coordinates

\[
x=\sin\phi\cos\theta,\quad y=\sin\phi\sin\theta,\quad z=\cos\phi
\]

on `0<phi,theta<pi/2` give

\[
\frac{d\omega}{\sqrt{x^2+y^2}}
=\frac{\sin\phi\,d\phi\,d\theta}{\sin\phi}
=d\phi\,d\theta.
\]

Therefore each pair-weight octant integral is exactly `pi^2/4`; the three-pair octant integral is `3pi^2/4`; division by the six order chambers gives

\[
\boxed{I_{ab}+I_{ac}+I_{bc}=\pi^2/8}.
\]

Consequently `sum J_q=pi/4` and `sum P_q=1` follow algebraically.

## Validation boundary

The proof is the symmetry-plus-spherical-coordinate calculation in `analytic-chamber-normalization.md`. The Python audit only checks the exact rational coefficient ledger in units of powers of `pi`; numerical quadrature is not used as proof.

```text
STAGE13_13FK=COMPLETE_ANALYTIC_CHAMBER_NORMALIZATION
R06_GATE_A=COMPLETE
SUM_IQ_ANALYTIC_PROOF_COMPLETE=true
PAIR_WEIGHT_OCTANT_INTEGRAL=pi^2/4
SUM_IQ=pi^2/8
SUM_JQ=pi/4
SUM_PQ=1
NUMERICAL_QUADRATURE_USED_AS_PROOF=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R06_GATE_B_REQUIRED=true
R06_GATE_C_REQUIRED=true
R06_GATE_D_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13fl
```

## Files

- `stages/stage13/13-13fk/analytic-chamber-normalization.md`
- `stages/stage13/13-13fk/result.md`
- `stages/stage13/scripts/13-13fk/analytic_chamber_normalization_audit.py`
- `.github/workflows/stage13-13fk-analytic-chamber-normalization.yml`
