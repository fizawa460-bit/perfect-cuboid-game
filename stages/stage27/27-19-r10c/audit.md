# Stage27-19 r10a-c fresh audit

```text
AUDIT_VERDICT=PASS_WITH_ROUTE_FREEZE
AUDITED_PR=1265
AUDITED_SUBMISSION_HEAD=5cff562669f3816eb82ea0d1e6b8d523ddfe84b3
PESCHMANN_SEQUENCE_RELEVANCE_AUDIT=PASS
POINTWISE_TAU_SQUARE_FILTER_AUDIT=PASS
MOVING_SECTION_NOT_PROVED_AUDIT=PASS
MOVING_MULTISECTION_NOT_PROVED_AUDIT=PASS
POSITIVE_DIMENSIONAL_PERFECT_SUBFAMILY_NOT_PROVED_AUDIT=PASS
FIXED_FIBER_ENUMERATION_NOT_LOWER_PROOF_AUDIT=PASS
LOW_HEIGHT_CROSS_CANCELLATION_STILL_OPEN=true
PESCHMANN_LANE_STATE=THEOREM_CONSTRUCTION_GATE_PAUSED
AUTOMATIC_R10D=false
CURRENT_LOWER_EXPONENT=1/4
CURRENT_UPPER_MU=1/2
ADVANCE_TO_CHECKPOINT50=false
SUBMITTED_HEAD_CI=NOT_CONFIGURED
MERGE_ALLOWED=true
NEXT_DERIVED_ROUTE=NONE_UNTIL_NEW_EXTERNAL_CONSTRUCTION_INPUT
```

The targeted Peschmann rematch legitimately sharpens the remaining lower-construction problem. The published Mordell-Weil procedure filters individual points by the condition that the lift function `tau(P)` be a positive rational square. That does not imply a function-field identity making `tau` square on a moving section, nor a finite-degree multisection, nor a positive-dimensional rational square-lift locus with controlled physical height.

Consequently the reported generation of many Euler-brick points or further fixed-fiber computations cannot by themselves yield the Stage19 polynomial lower receiver. The alternate low-height cross-cancellation route remains mathematically open, but the repository currently contains no new identity that improves the certified 1/4 lower exponent.

Under the anti-loop policy, automatic r10d would only rename this construction gate. Freeze the Peschmann lane until a genuinely new external construction input appears: an explicit square-lift section/multisection, a positive-dimensional square-lift theorem with height control, a new cross-divisibility specialization of algebraic height at most seven, or an independent moving family not already reduced to a fixed high-genus square condition.

This is a route freeze only. It is not a perfect-cuboid nonexistence claim and does not close the overall Stage19 problem.
