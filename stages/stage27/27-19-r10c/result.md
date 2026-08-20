# Stage27-19-r10c — Peschmann route arbitration

```text
TASK_ID=Stage27-19-r10c
PARENT_ROUTE=Stage27-19-r10b
ROUTE_KIND=LOWER_ROUTE_ARBITRATION
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
CURRENT_LOWER_EXPONENT=1/4
CURRENT_UPPER_MU=1/2
```

The targeted external search materially improved the lower receiver: the remaining construction problem is no longer generic 'find another parametrization', but the explicit square-lift geometry of the Master-Hit elliptic/genus-3 framework.

However, the currently located literature does not provide a moving section/multisection with automatic square lift, nor a low-height cross-cancellation specialization satisfying the Stage27 progress ledger. Continuing by merely enumerating more Mordell-Weil points or more fixed fibers would not establish polynomial family growth and would violate the anti-loop policy.

Therefore the Peschmann lane should be frozen after audit unless one of the following fresh inputs appears:

- an explicit rational section/multisection with function-field square `tau`;
- a theorem proving a positive-dimensional rational square-lift locus with controlled height and multiplicity;
- a new quartic cross-divisibility specialization giving `h_alg<=7`;
- an independent construction family not already reduced to a fixed high-genus square condition.

The whole Stage19 problem remains open. This is only a bounded route freeze.

```text
PESCHMANN_TARGETED_SEARCH_COMPLETED=true
PESCHMANN_LANE_CURRENT_VERDICT=AMBER_GATE_THEN_FREEZE
BLIND_MORDELL_WEIL_ENUMERATION_FORBIDDEN=true
FIXED_FIBER_EXPANSION_FORBIDDEN_AS_LOWER_PROOF=true
LOW_HEIGHT_CROSS_CANCELLATION_STILL_OPEN=true
NEW_LOWER_EXPONENT_PROVED=false
CURRENT_LOWER_EXPONENT=1/4
CURRENT_UPPER_MU=1/2
ADVANCE_TO_CHECKPOINT50=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage27-19-r10-audit
POST_AUDIT_ROUTE=NEW_EXTERNAL_CONSTRUCTION_INPUT_OR_RETURN_TO_UPPER_GATE
```
