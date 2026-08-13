# Stage15-6cb — exploration-safety protocol repair

Base: merged PR #859. Main-batch work unit 1.

This substage repairs the process gap identified by fresh audit. The prior 6ca mathematical reduction is retained, but its parking claim is not accepted until the controller-required exploration-safety protocol is explicit.

Required protocol now frozen:

```text
BLIND_REDISCOVERY_REQUIRED=true
CANDIDATE_LEDGER_REQUIRED=true
CANDIDATE_LEDGER_CLASSES=LIVE,UNTESTED,EQUIVALENT,DOMINATED,BLOCKED
CYCLE_PARKING_AUDIT_REQUIRED=true
```

No mathematical claim is strengthened here.

```text
STAGE15_6_SUBSTAGE=6cb
STAGE15_6CB_PROTOCOL_REPAIR=true
STAGE15_6CB_PREVIOUS_6CA_PARKING_ACCEPTED=false
STAGE15_6CB_EXIT=BLIND_REDISCOVERY_READY
```