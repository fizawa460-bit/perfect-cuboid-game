# Verification receipt

Run from the repository root:

```text
python stages/stage32/final-chain/32-02-effectivity/scalar-producer-research/verify_pairing_scalar_producer.py
PASS_32_02_SELECTED64_TO_HPERP_SCALAR_PRODUCER

python stages/stage32/final-chain/32-02-effectivity/scalar-producer-research/verify_source_locked_known_curve_scalar.py
PASS_32_02_SOURCE_LOCKED_KNOWN_CURVE_SCALAR_REGRESSION 2 -4 272
```

The second check is a real retained-data replay: degree `d=2`, curve square `C2=-4`, and exact negative Hperp square `N=272`. This receipt grants no FULL178, effectivity, pruning, or merge credit.

## Review 5184048998 repair

All three regressions were run locally after the repair with SymPy 1.14.0.
The two commands above still pass. The added command is:

```text
python -B stages/stage32/final-chain/32-02-effectivity/scalar-producer-research/verify_scalar_e2e.py
PASS_32_02_SCALAR_E2E_LOCK_BEFORE_IMPORT_PROTOCOL_REPLAY_RR
KNOWN_CURVE d=2 C2=-4 N=272; RR_INCONCLUSIVE_SOURCE_NOT_AFFIRMED; credit=0
```

This includes dependency drift-before-execution and record-tampering rejection
tests. It is local verification only, not exact-head CI or hostile-audit approval.
