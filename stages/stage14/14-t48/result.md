# Stage14-t48 — physical row-correlation bridge and diffuse coherence boundary

## Purpose

Stage14-t47 reduced the principal squareclass problem to the Gram row-correlation target

\[
G_{\lambda,\mu}
=\sum_{\kappa}r_\kappa\chi_\kappa(\lambda)\chi_\kappa(\mu),
\]

with the sufficient pair-energy condition

\[
\max_\lambda\sum_{\mu\ne\lambda}|G_{\lambda,\mu}|^2
\ll H^2P B^{-\delta}.
\]

Stage14-t48 identifies this Gram object with the actual normalized four-linear physical character from the earlier Gaussian descent, tests whether the largest frozen correlations come from a small exceptional cell family, and records the aggregation boundary.

## 1. Exact physical-character bridge

For a reciprocal-quotient state `s`, write `F_s` for the t36 four-linear product and `ell_s` for its canonical super-square-root prime. On the visible branch the canonical prime occurs with exact even valuation two, so define

\[
\widetilde F_s=F_s/\ell_s^2.
\]

On the invisible branch define `\widetilde F_s=F_s`.

Then the frozen audit verifies

\[
\boxed{
\chi_{\kappa_s}(\lambda)=\left(\frac{\widetilde F_s}{\lambda}\right)
}
\]

for every physical canonical test prime `lambda`, including the state's own canonical prime. Hence

\[
\boxed{
G_{\lambda,\mu}
=\sum_s
\left(\frac{\widetilde F_s}{\lambda}\right)
\left(\frac{\widetilde F_s}{\mu}\right).
}
\tag{48.1}
\]

All 87 frozen test primes satisfy `lambda=1 mod 4`. Thus (48.1) is exactly in the split-prime orientation used by t32. The t32 two-prime split-torus completion therefore applies to the angular completion of each fixed norm-index/common-refinement cell.

Frozen exact checks:

```text
canonical-square normalization checks       560
product-character checks               2,143,680
split canonical test primes                    87 / 87
```

## 2. Fixed-direction squareclasses are already injective

After the t42 reciprocal quotient, every fixed direction `(a,b)` has pairwise distinct squareclasses. The only fixed-direction multiplicity two in t36 was the exact `p<->q` reciprocal duplication.

Therefore the large Gram correlations are not caused by repeated squareclasses inside one fixed direction.

Frozen:

```text
reciprocal states     560
directions            137
fixed-direction kernel injectivity   exact
```

## 3. Largest frozen correlations are diffuse

The largest off-diagonal entry is

\[
\boxed{G_{229,461}=83.}
\]

For this pair, only `5+1` signed units come from states whose canonical prime equals one of the two test primes; the other `77` come from foreign-canonical states. Its largest fixed-direction contribution has absolute value only `7`, and its largest common-packet contribution only `22`.

Across the top 12 off-diagonal pairs:

```text
largest |G|                                  83
max endpoint-canonical absolute contribution 10
max single direction cell                     9
max single common-packet cell                 24
```

Thus the large frozen row correlations are not explained by one exceptional direction, one common-core packet, or the two endpoint canonical primes. This is a finite diagnosis only, not an asymptotic theorem.

## 4. Why cellwise Cauchy is the wrong aggregation

Let

\[
G_{\lambda,\mu}=\sum_R G_{\lambda,\mu}(R)
\]

for a partition into directions or common-refinement packets. Then

\[
|G_{\lambda,\mu}|^2
\le \#R\sum_R|G_{\lambda,\mu}(R)|^2.
\]

The frozen worst row is `lambda=821`:

```text
actual off-diagonal row L2                 73,273
sum of fixed-direction local row L2        48,163
Cauchy after 137 directions             6,598,331

sum of common-packet local row L2           49,859
Cauchy after 37 common packets            1,844,783
```

So proving a good estimate on every cell and then applying Cauchy loses the number of cells and destroys the useful scale. The signs between cells must be retained.

This is the precise live boundary:

\[
\boxed{
\text{t32 angular completion}
+\text{ signed divisor-coupled norm-index/common-refinement aggregation}.
}
\]

The latter is the same structural receiver already prepared by tH12/tH13; t48 does not create a new independent adapter problem.

## 5. tH decision

**Stage14-tH14 is not needed now.**

The new t48 object is still the existing signed common-refinement / product-kernel dispersion object. A new tH stage should be opened only if the next live arithmetic step reveals a coherent-row family that cannot be represented by the tH12/tH13 receiver.

## Boundary

```text
STAGE14_T48=COMPLETE_PHYSICAL_ROW_CORRELATION_BRIDGE_AND_DIFFUSE_COHERENCE_AUDIT
T47_GRAM_IS_NORMALIZED_PHYSICAL_FOUR_LINEAR_CHARACTER_SUM=true
ALL_CANONICAL_TEST_PRIMES_SPLIT=true
T32_TWO_PRIME_ANGULAR_COMPLETION_REUSED=true
FIXED_DIRECTION_KERNEL_INJECTIVITY_AFTER_RECIPROCAL_QUOTIENT=true
TOP_FROZEN_ROW_CORRELATIONS_SINGLE_CELL_EXCEPTIONAL=false
SIGNED_COMMON_REFINEMENT_AGGREGATION_REQUIRED=true
UNIFORM_PHYSICAL_ROW_CORRELATION_POWER_SAVING_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
CANONICAL_PRIME_SUM_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
TH14_NEEDED=false
NEXT=Stage14-t49 keep the signed common-refinement aggregation and attack the divisor-coupled norm-index row second moment directly, using the t32 split-torus completion plus tH12/tH13 hyperbola/product-kernel machinery; do not Cauchy over direction/common-packet cells first
```
