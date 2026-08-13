# Stage15-6cd — candidate ledger + cycle parking audit

Base: Stage15-6cc. Main-batch work unit 3.

Candidate ledger:

| candidate | class | reason |
|---|---|---|
| physical-height-aware gcd-product first moment | LIVE | exact remaining obstruction |
| pointwise domination of `G_S G_O` by already charged physical variables | UNTESTED | would supersede averaging if found |
| raw divisor expansion with fixed-modulus density summation | BLOCKED | moving-normalizer firewall from 6bz |
| generic Selberg / toric equidistribution import | DOMINATED | narrower explicit gcd receiver now exists; prior theorem windows too weak |
| Stage14 t75/t78 divisor-switch packet | EQUIVALENT | same mechanism family after packet conditioning, but no whole-family adapter |
| Stage14 t76 root-line spacing | DOMINATED | local/fixed-packet spacing does not discharge global first moment |
| elliptic / genus-one / twist-height detour | EQUIVALENT | prior cycle returns to same global core/gcd obstruction |

Parking audit:
- blind rediscovery completed;
- Arsenal trigger search completed;
- exact reconstruction search completed;
- measure/quantifier and no-double-charge firewalls retained;
- every generated candidate has one of the five required classes;
- exactly one LIVE obstruction remains, with one UNTESTED stronger-domination possibility explicitly preserved.

Therefore the current normal form may be parked for fresh audit, but not merged before that audit passes.

```text
STAGE15_6_SUBSTAGE=6cd
STAGE15_6CD_CANDIDATE_LEDGER_COMPLETE=true
STAGE15_6CD_REQUIRED_CLASSES_PRESENT=LIVE,UNTESTED,EQUIVALENT,DOMINATED,BLOCKED
STAGE15_6CD_CYCLE_PARKING_AUDIT_COMPLETE=true
STAGE15_6CD_LIVE_GATE=PHYSICAL_CHANNEL_GCD_PRODUCT_FIRST_MOMENT
STAGE15_6CD_UNTESTED_ROUTE=POINTWISE_STRUCTURAL_DOMINATION
STAGE15_6CD_AUDIT_REQUIRED=true
STAGE15_6CD_CODEX_REQUIRED=false
STAGE15_6CD_MERGE_ALLOWED=false
STAGE15_6CD_EXIT=FRESH_STAGE15_6_AUDIT_READY
```