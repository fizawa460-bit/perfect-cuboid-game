# Stage14-sH44 literature / theorem applicability note

Target:

```text
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreDualRootLineCompatibilityEnergyPowerSaving
```

This note records only theorem families checked for direct applicability to the exact s7-44 receiver.  Similar-looking phases or congruences are not imported without a charged-once adapter preserving all physical masks.

## 1. Generic determinant method / reciprocal Edwards curve

The earlier Stage14 genus-one audit already certified a degree-four Segre determinant-method bound for a **fixed** reciprocal Edwards parameter `lambda`.

For the present theta-quarter band the same height calculation gives

```text
E_det,fixed-lambda <= 3/16 + phi/2.
```

The fixed-C dual-root-line count is

```text
E_dual,fixed-C = 3/4 - 2phi.
```

These cross at `phi=9/40`.  Thus even before the moving-lambda average is paid, the generic determinant estimate is not better on the upper part of the required band.  In addition, no charged-once average over the moving physical `lambda=4M/N` family is proved.

More specifically, the active full Cayley core satisfies

```text
lambda == +/-4 mod p^e
```

for every `p^e` in that core.  Hence the full common core is bad-reduction support for the reciprocal Edwards curve and cannot be reused as a fresh nonsingular p-adic determinant modulus.

Verdict:

```text
FIXED_LAMBDA_DETERMINANT_METHOD_APPLICABLE=true
FIXED_LAMBDA_DETERMINANT_METHOD_UNIFORM_WHOLE_BAND_SAVING=false
MOVING_PHYSICAL_LAMBDA_AVERAGE_CONTROLLED=false
COMMON_CORE_REUSABLE_AS_GOOD_REDUCTION_DETERMINANT_MODULUS=false
```

## 2. Quadratic-root equidistribution / modular-root energy

Hieu T. Ngo, *On roots of quadratic congruences*, arXiv:2107.13301, develops Weyl-form bounds for equidistribution of roots of quadratic congruences.

Stephan Baier's 2026 series on bilinear sums with modular square roots develops additive-energy and exponential-sum estimates where a modular square root such as

```text
k^2 == j*m mod r
```

moves with the residue variable `m`; see in particular arXiv:2601.15448, arXiv:2603.00768, and arXiv:2603.25814.

The s7-44 local roots are instead fixed roots of

```text
rho^2=-1,
sigma^2=1
```

for each active prime power.  Their total CRT label entropy is already `B^o(1)`.  The polynomial support comes from integer lifts along the two fixed primitive lines, not from a large family of modular square roots of moving residues.

No exact map to the modular-root-energy coefficient spaces preserves the reciprocal completion equations without reopening an already charged variable.

Verdict:

```text
QUADRATIC_ROOT_EQUIDISTRIBUTION_DIRECT_ADAPTER=false
MODULAR_SQUARE_ROOT_ENERGY_DIRECT_ADAPTER=false
```

## 3. Multiplicative congruence energy

Ayyad--Cochrane--Zheng (J. Number Theory 59 (1996), 398--413) prove asymptotic formulas and fourth-moment bounds for box solutions of

```text
x1*x2 == x3*x4 mod p.
```

Cochrane--Shi extend the multiplicative-congruence framework to general positive integer modulus (J. Number Theory 130 (2010), 767--785), and later work refines error terms in prime-modulus cases.

These results are valuable for discrepancy/energy of multiplicative congruences, but the s7-44 physical compatibility receiver is not yet a single multiplicative congruence in four independently weighted box variables.  It carries the two reciprocal difference-of-squares equations, canonical squarefree cells, orientation masks, and X13 post-column reconstruction.

More fundamentally, modular-energy asymptotics retain their expected-density main term.  The two s7-44 root-line expected densities already sum to exponent `1/2`, so an error-term theorem alone cannot break the barrier.

Verdict:

```text
MULTIPLICATIVE_ENERGY_DIRECT_ADAPTER=false
MULTIPLICATIVE_ENERGY_PRINCIPAL_TERM_REMOVES_SQRT_BARRIER=false
```

## 4. Bettin--Chandee Kloosterman fractions

Sandro Bettin and Vorrapan Chandee, *Trilinear forms with Kloosterman fractions*, arXiv:1502.00769, bound trilinear forms of the shape

```text
sum_{a,m,n} nu_a alpha_m beta_n e(a*inv(m)/n)
```

with genuinely moving denominator variables.

The s7-44 receiver conditions a full common core `C` and retains two primitive line lifts plus a positive physical completion indicator.  No identity currently converts that count to the Bettin--Chandee moving-denominator quantifier structure without losing a physical mask or reopening a charged support.

Verdict:

```text
BETTIN_CHANDEE_DIRECT_ADAPTER=false
```

## 5. Partially fixed Kloosterman fractions

Thomas Wright, *Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions*, arXiv:2604.25177, improves the Kloosterman-fraction technology when a denominator has a fixed factor, but a genuinely moving denominator factor remains part of the theorem's coefficient/range structure.

The full s7-44 common core is already fixed at the packet level.  No proved transformation creates Wright's required moving factor while retaining the canonical physical reconstruction.

Verdict:

```text
WRIGHT_PARTIALLY_FIXED_DENOMINATOR_DIRECT_ADAPTER=false
```

## 6. Fixed-modulus complete Kloosterman bilinear forms

Valentin Blomer and Alexandru Pascadi, *Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311, prove new bounds for bilinear forms in complete Kloosterman sums for all moduli.  Their abstract records a `c^(-1/32)` saving in the critical range where the summation length is `sqrt(c)`.

This is the closest modern fixed-modulus black box found.  However its input is already a bilinear form in complete sums

```text
S(a*m,n;c).
```

The s7-44 object is not such a sum.  It is a positive incomplete count of physical pairs on two primitive root lines.  A new Poisson/completion step would have to produce the complete Kloosterman family and simultaneously prove the transformed length range and coefficient norms while retaining every physical cutoff.

That adapter is not currently available, so no `c^(-1/32)` or corresponding `B^{-delta}` factor can be imported.

Verdict:

```text
BLOMER_PASCADI_COMPLETE_KLOOSTERMAN_THEOREM_RELEVANT_AFTER_ADAPTER=true
FIXED_MODULUS_COMPLETE_KLOOSTERMAN_ADAPTER_PROVED=false
BLOMER_PASCADI_DIRECTLY_APPLICABLE=false
```

## 7. Relation to contemporaneous tH23

The t-route `t80/t81/t82` coefficient space fixes a projective `U` before its hard analytic sum and reduces to a one-frequency inverse-fraction/Kloosterman-type receiver.  The s7-44 coefficient space instead has `(U,V)` itself as one of the two moving primitive root-line lifts.

The contemporaneous tH23 audit independently identifies a missing physical completion/Poisson adapter before fixed-modulus Kloosterman technology can be applied there.  That conceptual similarity is useful but does not furnish a bridge.

Verdict:

```text
T80_T81_T82_COEFFICIENT_SPACE_IDENTICAL_TO_SH44=false
TH23_CROSS_PROMOTED_TO_SH44=false
```

## 8. Final literature verdict

No checked theorem directly supplies

```text
sum_C I_C << B^(1/2-delta+o(1)), delta>0,
```

with all s7-44 masks retained.

The most concrete next analytic target is therefore not a generic large sieve but the adapter

```text
physical dual-root-line compatibility
 -> mean-zero dispersion / completed Kloosterman family mod C
```

on the bad-reduction full-core branch.

```text
OFF_THE_SHELF_DUAL_ROOT_LINE_POWER_SAVING_PROVED=false
CERTIFIED_DUAL_ROOT_LINE_DELTA=0
MINIMAL_REMAINING_OBSTRUCTION=SquareRootThetaQuarterGloballyOddPrimitiveFullCoreBadReductionDualRootLinePhysicalCompletionDispersion
```
