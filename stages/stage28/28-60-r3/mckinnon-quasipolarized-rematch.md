# Stage28-60-r3 — McKinnon / quasi-polarized K3 rematch

```text
ROUTE=R22_MCKINNON_AND_QUASIPOLARIZED_REMATCH
STATUS=NEGATIVE_CERTIFICATE_WITH_NEW_CAUSAL_GUIDANCE
```

David McKinnon, *Counting Rational Points on K3 Surfaces*, J. Number Theory 84 (2000), studies hyperelliptic K3 surfaces admitting a generically two-to-one map to `P1 x P1` branched over a singular `(4,4)` curve.  Theorem 2.1 gives a bounded-height upper on the complement of explicitly identified rational curves for **ample** divisors in a specified cone, and Corollary 2.2 identifies minimal-degree rational curves as the first accumulating layer when its numerical hypothesis holds.

This is structurally close to the Stage19/20 double covers, but Stage14-4ah already locked the decisive height mismatch:

```text
PHYSICAL_POLARIZATION=M=pi^*(-K_Y)
M^2=8
M=big_and_nef_not_ample
M-null boundary curves lie outside the primitive positive physical open
MCKINNON_DIRECT_ASYMPTOTIC_IMPORTED=false
```

Therefore McKinnon's theorem cannot simply be invoked as a whole-population asymptotic under `R<=B`.

The r3 reuse is narrower and legal: McKinnon's mechanism motivates comparing the **minimal physical rational-curve spectrum** on the two covers.  The exact repo computation is stronger than the generic guidance on the Stage19 side because Stage14-4ak proves the `M.C=4` stratum empty.

A fresh literature rematch also checked Rams--Schuett, *Low degree rational curves on quasi-polarized K3 surfaces* (J. Pure Appl. Algebra 229 (2025), 107904).  That paper develops finite bounds for low-degree rational curves on big-and-nef quasi-polarized K3 surfaces, but its strongest general bounds require a high-degree regime relative to the curve-degree cutoff.  The Stage14 physical quasi-polarization has `M^2=8` (`h=4`), so the high-degree hypotheses do not classify the needed `M.C=5,6` strata here.

Thus neither literature input discharges Stage28-60-r2's interaction threshold.

```text
MCKINNON_DIRECT_PHYSICAL_HEIGHT_TRANSFER=false
RAMS_SCHUETT_DIRECT_DEGREE5_6_CLASSIFICATION=false
NEW_USE=motivate_and_bound_fixed_curve_spectrum_only
DIRECT_J28_THRESHOLD_DISCHARGED=false
```

The remaining low-degree finite problem is now concrete: using the already-fixed Shimada rank-20 Neron--Severi lattice and physical vector `M`, enumerate effective/Q-descending/physical rational root classes with `M.C=5` and `M.C=6`, modulo the physical automorphism stabilizer.  This is a bounded finite lattice computation, not an unbounded literature request.

Even a complete degree-5/6 classification would still need a global complement theorem to turn fixed-curve data into the full `N2` versus `M3` ordering.