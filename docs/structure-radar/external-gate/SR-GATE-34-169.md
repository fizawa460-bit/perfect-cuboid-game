# StructureRadar external-gate closure 34 — SR-STR-169 normalized Fourier/Gauss reduction

BATCH_ID=SR-BATCH-EXTERNAL_GATE_CLOSURE-34-R01
PHASE=EXTERNAL_GATE_CLOSURE
STRUCTURE=SR-STR-169
MODE=ONE_GATE_DEEP_ATTACK
TARGET=UniformWallSlabMAINArithmeticHostCorrelationPowerDeficit
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE
EXTERNAL_GATE_COUNT_BEFORE=13
EXTERNAL_GATE_COUNT_AFTER=13
BASE_MAIN=c57d29c2628fd14af55ab36cbefa08a9a5ea4539

This batch resumes from audited/merged parallel lane 33A. That lane already proved exact finite Fourier completion of the physical residue coefficient and exposed inverse-frequency geometry on the coprime odd Gauss factor. The remaining restart point was `MAINWallPhysicalResidueFourierCompletionNormAndBadGCDControl`.

The present batch discharges the purely algebraic Fourier-norm and bad-gcd parts of that restart point. It does not claim that a published Kloosterman-fraction theorem is now directly applicable to the full MAIN covariance.

## 1. The normalized Fourier coefficients have no extra q-loss

For one retained MAIN wall packet, keep the lane-33A notation

```text
q = 2UV/gcd(U,V),
W_hat(b) = sum_{f mod q} W(f) e_q(-bf),
c_b = W_hat(b)/q.
```

Then the completed quadratic kernel is

```text
sum_{f mod q} W(f)e_q(a f^2)
 = sum_{b mod q} c_b G_q(a,b).
```

Parseval on `Z/qZ` gives the exact identity

```text
sum_{b mod q} |W_hat(b)|^2 = q sum_{f mod q} |W(f)|^2,
```

hence

```text
sum_b |c_b|^2 = (1/q) sum_f |W(f)|^2.
```

Cauchy then gives

```text
sum_b |c_b|
 <= q^(1/2) (sum_b |c_b|^2)^(1/2)
 = (sum_f |W(f)|^2)^(1/2).
```

Therefore finite Fourier completion itself introduces no additional positive power of `q` into the normalized coefficient `L1` budget, and the normalized `L2` budget is strictly smaller by `q^(-1/2)`. This is an exact norm statement relative to the already-retained physical coefficient `W`; it does not by itself prove that the remaining variable dependencies satisfy an external bilinear/trilinear theorem.

The same identity yields the exact weak-`L2` tail

```text
#{b: |c_b| > T} <= (1/(q T^2)) sum_f |W(f)|^2,
```

for every `T>0`. Thus large Fourier coefficients are automatically sparse relative to the same `W`-energy. No independent sparsity saving is charged.

## 2. Non-coprime frequency strata reduce with zero normalized loss

For the complete quadratic Gauss sum

```text
G_q(a,b) = sum_{r mod q} e_q(a r^2 + b r),
```

put `d=gcd(a,q)`. The standard residue-class grouping gives the exact dichotomy

```text
d does not divide b  =>  G_q(a,b)=0,

d divides b          =>  G_q(a,b)=d G_{q/d}(a/d,b/d).
```

After the `1/q` normalization already present in `c_b=W_hat(b)/q`, the factor `d` cancels exactly:

```text
(1/q) G_q(a,b)
 = (1/(q/d)) G_{q/d}(a/d,b/d).
```

Thus every non-coprime `a` stratum descends to a smaller primitive modulus without a new polynomial loss. Iterating reaches `(a,q)=1`. The divisor stratification has at most `tau(q)=B^o(1)` layers on the existing polynomial-height MAIN modulus range, so this bookkeeping cannot supply or destroy a fixed power by itself.

This removes the old `bad-gcd` branch as a separate algebraic obstruction. It does not remove the physical common-parent weights attached to the descended modulus.

## 3. The 2-primary primitive local factor is explicit, not an unknown gate

Once `(a,q)=1`, `a` is odd on the 2-primary factor. Write `q=2^nu q_odd` and use CRT.

For `nu>=2`, the primitive 2-adic Gauss factor satisfies the exact parity/completion rule

```text
b odd  =>  G_{2^nu}(a,b)=0,

b=2k   =>  G_{2^nu}(a,b)
           = e_{2^nu}(-a^{-1} k^2) G_{2^nu}(a,0).
```

For `nu=1`, the two residue classes are explicit directly and contribute only a bounded local factor. Hence the even local component also produces an explicit inverse-`a` quadratic phase (or vanishes) after a parity split; there is no unidentified 2-primary theorem hidden at this algebraic stage.

The exact magnitude of the primitive 2-adic Gauss factor is the classical square-root local size up to an absolute factor, so this local completion does not create a second fixed-power saving. It is merely part of the complete kernel normalization.

## 4. What remains after the algebraic cleanup

Combining lane33A with the identities above, the following parts are now exact:

```text
FINITE_FOURIER_COMPLETION=PROVED
NORMALIZED_FOURIER_L2_IDENTITY=PROVED
NORMALIZED_FOURIER_L1_NO_Q_LOSS=PROVED
FOURIER_WEAK_L2_TAIL=PROVED
NONCOPRIME_GAUSS_DESCENT=PROVED
TWO_PRIMARY_PRIMITIVE_COMPLETION=PROVED
```

The missing step is no longer generic Fourier completion, coefficient norm control caused by the transform, non-coprime frequencies, or the even local factor. The live obstruction is the physical separation/range adapter after the completed inverse-frequency kernels have been exposed.

```text
FIRST_MISSING_LEMMA=MAINWallCompletedInverseFrequencyCoefficientSeparationAndPublishedRangeAdapter
```

A sufficient theorem/adapter must take the exact completed MAIN covariance and produce a bounded/subpolynomial collection of bilinear or trilinear inverse-fraction forms such that:

1. the remaining coefficients are separated in the variables required by the external theorem rather than retaining an arbitrary correlated matrix;
2. the original `H_phys^MAIN` physical masks, nested common-parent divisor weights and quantifier order are preserved;
3. the descended correlated moduli and numerator/denominator ranges fall inside one published power-saving theorem uniformly;
4. the theorem's coefficient norms are charged only against the original MAIN physical energy and the exact normalized Fourier bounds above;
5. no principal/zero mode, selector-side, q17-side, or already-paid support saving is multiplied again.

Dong--Robles--Zeindler remains the first published engine to test once this separation/range adapter exists, because arbitrary complex coefficient sequences are allowed on its genuine bilinear Kloosterman-fraction form. Wright remains secondary only if the completed MAIN geometry really exposes the required modulus average and coefficient hypotheses. The theorem applicability verdict remains unproved until that exact variable/range match is checked.

## 5. Relation to the other post-close gates

- `SR-STR-167` remains the selector-side same-MAIN-measure canonical-correlation decomposition gate.
- `SR-STR-174` remains the q17 weighted witness-incidence exceptional-mass gate.
- `SR-STR-168` remains the same-measure common Gaussian norm-quotient correlation gate.

These are complementary transport/receiver components. This batch does not multiply their hypothetical savings with the SR-STR-169 branch.

## 6. Verdict / firewalls

```text
SR_STR_169_STATUS=EXTERNAL_GATE
GATES_CLOSED=0
EXTERNAL_GATE_COUNT_BEFORE=13
EXTERNAL_GATE_COUNT_AFTER=13
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
NOVELTY_BY_SEARCH_ABSENCE=false
```

The reduction is substantive: two pieces that were previously bundled into `MAINWallPhysicalResidueFourierCompletionNormAndBadGCDControl` are now exact algebra, and the remaining gate is isolated at physical variable separation plus published theorem range compatibility.

```text
WORK_DELEGATION_RECOMMENDED=true
WORK_TARGET=SR-STR-169 / MAINWallCompletedInverseFrequencyCoefficientSeparationAndPublishedRangeAdapter
WORK_REQUEST=Search primary bilinear/trilinear Kloosterman-fraction, dispersion, Kuznetsov/spectral, and inverse-fraction theorems only against the completed MAIN kernel after the exact normalized Fourier and gcd/2-adic reductions in SR-GATE-34-169. Require exact variable separation, coefficient-norm hypotheses, modulus/numerator/denominator ranges, correlated-modulus handling, preservation of H_phys^MAIN masks/common-parent weights/quantifier order, and one uniform positive power. Start from Dong--Robles--Zeindler 2026 and Wright 2026; do not substitute average-modulus results or generic cancellation without an exact same-measure adapter.
CODEX_DELEGATION_RECOMMENDED=false
CODEX_REASON=no repository-mechanical blocker is present in this mathematical reduction
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
REPAIR_REQUIRED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
