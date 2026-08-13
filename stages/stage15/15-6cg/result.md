# Stage15-6cg — two-range gcd-moment audit

Base: Stage15-6cf. Main-batch work unit 3.

Audit the two-range receiver produced by the physical divisor switch.

- The small-modulus side is genuinely narrower than the prior whole-family theorem gate, but still needs a physical-height count uniform in `de` beyond the logarithmic Huang window.
- The large-modulus side is no longer a moving-level equidistribution problem, but its complementary-divisor average requires a new inequality coupling the four channel-form sizes to the primitive physical height after normalization.

These are two distinct live inputs: one is a moderate-modulus physical congruence estimate, the other is a complementary-divisor / form-size average. They depend on different inputs, so the controller split trigger is now met.

Blind-rediscovery and candidate-ledger status from 6cd remains valid; 6ce closes the only UNTESTED pointwise route as BLOCKED in the current normal form. No Codex trigger is present: the obstruction is mathematical, not repository-mechanical.

```text
STAGE15_6_SUBSTAGE=6cg
STAGE15_6CG_SMALL_MODULUS_GATE=PHYSICAL_ROOT_LINE_COUNT_UNIFORM_IN_de
STAGE15_6CG_LARGE_MODULUS_GATE=COMPLEMENTARY_DIVISOR_FORM_SIZE_AVERAGE
STAGE15_6CG_TWO_NON_EQUIVALENT_LIVE_OBSTRUCTIONS=true
STAGE15_6CG_SPLIT_TRIGGER=true
STAGE15_6CG_AUDIT_REQUIRED=true
STAGE15_6CG_CODEX_REQUIRED=false
STAGE15_6CG_MERGE_ALLOWED=false
STAGE15_6CG_EXIT=FRESH_AUDIT_BEFORE_SPLIT_EXECUTION
```