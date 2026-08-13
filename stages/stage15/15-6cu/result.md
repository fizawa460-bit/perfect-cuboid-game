# Stage15-6cu — small-side normalizer-only delta test

Base: Stage15-6ct. Main-batch work unit 2.

The 6cq one-sided fringe is represented by `mn` or `rs`. In the exact 6ct cells,
\[
mn=HMN,\qquad rs=HUV,
\]
while the physical product-height envelope is
\[
HMNUV\le B.
\]
Therefore product-height geometry alone gives no fixed power saving for either one-sided area: the unbalanced region `UV=O(1)` permits `HMN` at order `B`, and symmetrically `MN=O(1)` permits `HUV` at order `B`.

This is not a counterexample to the desired fringe theorem on the **actual space-diagonal-integral survivor set**. It is a rigorous firewall: a proof of `delta>0` cannot come from the common primitive-normalizer/product-height geometry alone. It must use arithmetic omitted by that envelope, namely the simultaneous S/O channel congruences / Gaussian-square receiver (or an equivalent exact survivor condition).

The transversality `gcd(q,H)=1` strengthens the diagnosis. The modulus cannot be paid for by a common factor already absorbed into `H`; any small-side saving must come from distribution of the residual channel forms modulo `q` inside the product-height hyperbola.

Hence the audit request "prove or disprove fixed delta" resolves at the mechanism level as:
- `delta>0` from normalizer geometry alone: **DISPROVED**;
- `delta>0` on the full exact survivor set: still **LIVE**, but now requires residual channel arithmetic.

The conditional root-line ledger remains `beta=-1`.

```text
STAGE15_6_SUBSTAGE=6cu
STAGE15_6CU_CONDITIONAL_BETA=-1
STAGE15_6CU_NORMALIZER_ONLY_DELTA=false
STAGE15_6CU_FULL_SURVIVOR_DELTA_PROVED=false
STAGE15_6CU_UNBALANCED_PRODUCT_HEIGHT_FIREWALL=true
STAGE15_6CU_REQUIRED_EXTRA_INPUT=RESIDUAL_CHANNEL_ARITHMETIC
STAGE15_6CU_EXIT=LARGE_NORMALIZER_ONLY_SIGMA_TEST_READY
```