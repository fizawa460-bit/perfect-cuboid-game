# Stage21 Arsenal Promotions

Status: candidate promotions materialized for Stage21-70 fresh re-audit.

## S21-W01 — Ambient-control interaction adapter

```text
NAME=ambient-control interaction adapter
TYPE=method
SOURCE_STAGE=Stage21
ASSUMPTIONS=compatible primitive/canonical populations; common cutoff; audited ambient control for the added condition; matched multiplicity
VALID_RANGE=population-transition comparisons satisfying those assumptions
WHAT_IT_DOES=separates intrinsic condition cost from interaction enhancement or suppression after prior arithmetic conditioning
WHAT_IT_DOES_NOT_DO=does not imply stochastic independence, local-factor independence, or factorization of arithmetic events
POTENTIAL_RECEIVERS=Stage24,Stage25,Stage28
AUDIT_STATUS=PENDING_STAGE21_70_REAUDIT
```

Operationally, if an added condition has ambient survival `C0(B)` and survival `C1(B)` inside a conditioned source population, compare `C1(B)/C0(B)` only after population/cutoff/multiplicity matching. A quotient tending to `1` supports ratio-level asymptotic independence; divergence above `1` is enhancement; decay below `1` is suppression. Polynomial and logarithmic effects must be recorded separately to avoid double charging.

For Stage21,

\[
C_1(B)=N_1(B)/M_1(B)\sim \frac{\kappa\pi}{18}\frac{(\log B)^2}{B},
\]

\[
C_0(B)=N_S^{all}(B)/U(B)\sim \frac{9\zeta(3)}{8\pi G}\frac1B,
\]

so

\[
C_1(B)/C_0(B)\sim \frac{4\kappa\pi^2G}{81\zeta(3)}(\log B)^2\to\infty.
\]

## S21-W02 — One-face to space-diagonal transition law

```text
NAME=one-face to space-diagonal transition law
TYPE=theorem
SOURCE_STAGE=Stage21
ASSUMPTIONS=Stage16/17 primitive canonical exactly-one population; common cutoff R<=B; target d=R; E-1e leading source constant; audited Stage17 target law
VALID_RANGE=B->infinity
WHAT_IT_DOES=proves N1/M1~(kappa*pi/18)(log B)^2/B and identifies B^-1 as intrinsic space cost with positive logarithmic interaction compensation
WHAT_IT_DOES_NOT_DO=does not canonically assign the two logarithms to independent pole slots/local factors; does not apply automatically to two-face or Euler populations
POTENTIAL_RECEIVERS=Stage24,Stage25,Stage28,perfect-cuboid endpoint planning
AUDIT_STATUS=PENDING_STAGE21_70_REAUDIT
```

The directionwise refinement is also portable under the same contracts:

\[
N_{1,q}(B)/M_{1,q}(B)\sim \frac{\kappa\pi}{18}\frac{(\log B)^2}{B}
\]

for `q=ab,ac,bc`. The common chamber factor cancels, so the added space-diagonal condition creates no new leading direction-specific interaction.

## Promotion boundary

These are Stage21-derived portable contracts. Their mathematical content is frozen only after Stage21-70 fresh re-audit PASS. Until then, downstream stages may inspect them but must not mark them as audited reusable inputs.
