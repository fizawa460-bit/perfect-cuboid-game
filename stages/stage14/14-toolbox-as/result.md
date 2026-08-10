# Stage14-toolbox-as — theorem-source shortlist and adapter gates

Stage14-toolbox-as consumes merged toolbox-ar and audits theorem families against the two current receiver certificates. It does not infer compatibility from a shared phrase such as “bilinear”, “quadratic”, “hyperbolic”, or “trace”.

## Outcome

No currently shortlisted theorem is directly importable.

For `LargeSwitchPrimitivePythagoreanTwoLegIncidence`, Wilson’s Jacobi-symbol bilinear theorem over hyperbolic regions is the closest analytic shape. Its product cutoff is relevant, but Stage14 still lacks an exact bounded-multiplicity conversion from the positive physical Pythagorean lift to separated squarefree Jacobi coefficients. A quadratic large sieve has the same pre-collapse coefficient-energy obligation. Bare Pythagorean divisor counting is structural only because it does not bound physical lift multiplicity. The s route should therefore continue first with direct integer/bilinear geometry in s7-20.

For `SharedUInvisibleCenteredProjectiveSelectorDispersion`, Ping Xi’s arbitrary-set trace-function bilinear theorem is the closest two-variable shape. Direct import is not licensed: the present object is a two-prime centered Frobenius square with a bidegree-`(4,4)` kernel, divisor-coupled hyperbola, moving `delta`, and physical masks. A one-field bounded-conductor sheaf certificate plus selector-support energy transfer and two-prime reassembly are missing. Wilson’s theorem requires a genuine Jacobi-symbol identity, which is also missing. Post-squareclass Goldmakher--Louvel is rejected as circular because its coefficient energy is `E_U`. FI Gaussian-symbol transfer remains invalid by the t39/tH15 separation audit.

The exact promotion gates are recorded in `docs/stage14-toolbox/current-receiver-theorem-shortlist.md`.

## Scheduling

The two missing adapters are receiver-specific. They neither overlap nor modify canonical Stage14 ledgers, so s7-20 and the next t stage may work in parallel. No additional toolbox-H line is justified. Toolbox main does not wait.

```text
STAGE14_TOOLBOX_AS=COMPLETE_THEOREM_SOURCE_SHORTLIST_AND_ADAPTER_GATES
MERGED_TOOLBOX_AR_IMPORTED=true
S_CURRENT_RECEIVER=LargeSwitchPrimitivePythagoreanTwoLegIncidence
FIXED_U_CURRENT_RECEIVER=SharedUInvisibleCenteredProjectiveSelectorDispersion
DIRECT_IMPORTABLE_THEOREM_COUNT=0
S_CLOSEST_SOURCE=WILSON_HYPERBOLIC_JACOBI_BILINEAR
S_WILSON_DIRECT_IMPORT_VALID=false
S_EXACT_JACOBI_ADAPTER_PROVED=false
S_PHYSICAL_LIFT_MULTIPLICITY_BOUND_PROVED=false
S_RECOMMENDED_NEXT_ROUTE=DIRECT_INTEGER_BILINEAR_GEOMETRY
FIXED_U_CLOSEST_SOURCE=PING_XI_ARBITRARY_SET_TRACE_BILINEAR
FIXED_U_PING_XI_DIRECT_IMPORT_VALID=false
FIXED_U_ONE_FIELD_TRACE_SHEAF_CERTIFICATE_PROVED=false
FIXED_U_PHYSICAL_SELECTOR_SUPPORT_ENERGY_TRANSFER_PROVED=false
FIXED_U_TWO_PRIME_REASSEMBLY_WITH_ZERO_FIXED_LOSS_PROVED=false
POST_SQUARECLASS_QUADRATIC_LARGE_SIEVE_NONCIRCULAR=false
DIRECT_FI_GAUSSIAN_SYMBOL_TRANSFER_VALID=false
COMPLETE_TRACE_IMPLIES_SPARSE_SELECTOR_DISPERSION=false
RECEIVER_CROSS_PROMOTION_ALLOWED=false
S_AND_FIXED_U_ADAPTERS_PARALLEL_SAFE=true
TOOLBOX_H_CONTINUATION_NEEDED=false
TOOLBOX_MAIN_BLOCKED_BY_H=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT=Stage14-toolbox-at adapter-obligation ledger and failure-mode tests
```

## Literature checked

- C. Wilson, *General Bilinear Forms In The Jacobi Symbol Over Hyperbolic Regions*, arXiv:2208.14909.
- P. Xi, *Bilinear forms with trace functions over arbitrary sets, and applications to Sato--Tate*, arXiv:2211.14702.
- L. Goldmakher and B. Louvel, *A quadratic large sieve inequality over number fields*, arXiv:1112.1642.
- Friedlander--Iwaniec Gaussian-symbol/spin machinery remains governed by the exact Stage14 t39/tH15 applicability audit.
