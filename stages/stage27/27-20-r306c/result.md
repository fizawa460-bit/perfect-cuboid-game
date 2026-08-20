# Stage27-20-r306c — rematch the low-core slice to StructureRadar reserve

STATUS=SUBMITTED_PENDING_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_LOW_CORE_ARSENAL_REMATCH
PARENT_ROUTE=Stage27-20-r306b

The low-core cutoff changes the receiver enough to justify a selective StructureRadar re-entry. The relevant reserve cards are:

- SR-STR-170: divisor-in-an-interval geometry for the reciprocal squareclass divisor window;
- SR-STR-171: localized unitary-divisor shadow;
- SR-STR-161: separated quadratic/Jacobi large sieve;
- SR-STR-166: charged-once eliminant routing.

The cutoff alone does not discharge SR-STR-170/171. Their external-gate objections remain unless the low-core physical selector can be transported to the ambient divisor window with only B^o(1) distortion and without recharging canonical/reverse-completion conditions.

However the cutoff does sharpen the required adapter: instead of a theorem on the entire balanced wall, it is enough to prove a bounded-distortion map

  P_lo(kappa) -> D_lo(kappa)

into a divisor-window or unitary-divisor model, with fibers B^o(1), such that the transported window and physical masks are retained and a known ambient sparsity theorem gives a fixed-power deficit uniform in the low-core range.

Likewise, SR-STR-161 becomes legal only if elimination after fixing the small core produces genuine one-variable coefficient separation. The low-core hypothesis by itself does not imply this.

Thus the best next receiver is not another analytic estimate but a concrete transport/elimination adapter:

  MAINWallLowCoreDivisorWindowBoundedDistortionAdapter

or, failing that,

  MAINWallLowCoreSeparatedCoefficientAdapter.

This is a materially weaker and more targeted gate than the old all-wall same-measure operator theorem.

LOW_CORE_STRUCTURE_RADAR_REMATCH_EXECUTED=true
SR_STR_170_DIRECTLY_APPLICABLE=false
SR_STR_171_DIRECTLY_APPLICABLE=false
SR_STR_161_DIRECTLY_APPLICABLE=false
NEW_TARGET=MAINWallLowCoreDivisorWindowBoundedDistortionAdapter
ALTERNATE_TARGET=MAINWallLowCoreSeparatedCoefficientAdapter
NEXT_DERIVED_ROUTE=27-20-r306d
STRICT_SUB_SQRT_UPPER_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
