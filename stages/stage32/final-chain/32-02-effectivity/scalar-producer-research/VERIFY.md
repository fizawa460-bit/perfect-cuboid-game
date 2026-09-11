# Verification receipt

Run from the repository root:

```text
python stages/stage32/final-chain/32-02-effectivity/scalar-producer-research/verify_pairing_scalar_producer.py
PASS_32_02_SELECTED64_TO_HPERP_SCALAR_PRODUCER

python stages/stage32/final-chain/32-02-effectivity/scalar-producer-research/verify_source_locked_known_curve_scalar.py
PASS_32_02_SOURCE_LOCKED_KNOWN_CURVE_SCALAR_REGRESSION 2 -4 272
```

The second check is a real retained-data replay: degree `d=2`, curve square `C2=-4`, and exact negative Hperp square `N=272`. This receipt grants no FULL178, effectivity, pruning, or merge credit.
