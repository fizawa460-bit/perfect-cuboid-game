# Stage15-6-cycle — 6bt through 6bx

```text
6bt  quantitative Selberg/large-sieve import       BLOCK
6bu  elementary universal-torsor lattice sum        BLOCK
6bv  Stage14 Type-II/large-sieve cross-promotion    BLOCK
6bw  channel-gcd majorant                           PASS
6bx  physical channel-gcd product first moment      NEW_GATE
```

The cycle rejects three tempting global-sieve shortcuts and replaces the moving actual-core sum by the exact majorant `q|G_S G_O`. The remaining analytic object is the first moment of this explicit gcd product over the ambient physical toric height measure.

```text
STAGE15_6_CYCLE_START=6bt
STAGE15_6_CYCLE_END=6bx
STAGE15_6_CYCLE_AUDIT_LEDGER=BLOCK,BLOCK,BLOCK,PASS,NEW_GATE
STAGE15_6_CYCLE_GENERIC_SELBERG_IMPORT=false
STAGE15_6_CYCLE_ELEMENTARY_TORSOR_B_OVER_Q=false
STAGE15_6_CYCLE_STAGE14_DISPERSION_CROSS_PROMOTION=false
STAGE15_6_CYCLE_CHANNEL_GCD_MAJORANT=true
STAGE15_6_CYCLE_REQUIRED_GLOBAL_OBJECT=PHYSICAL_CHANNEL_GCD_PRODUCT_FIRST_MOMENT
STAGE15_6_CYCLE_CAUSAL_THREE_QUARTERS_PROVED=false
STAGE15_6_CYCLE_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6_CYCLE_EXIT=PHYSICAL_CHANNEL_GCD_PRODUCT_FIRST_MOMENT_THEOREM_GATE
```
