# Stage15-6cm — coupled D0 optimization recomputation

Base: Stage15-6cl. Main-batch work unit 3.

The audit-approved coupled receiver remains
\[
\mathcal M(B)=\mathcal M_{\le D_0}(B)+\mathcal M_{>D_0}(B).
\]
Stage15-6ck shows that exact phi-weight resummation alone does not produce a polynomial modulus window; the obstruction is the per-modulus physical root-line error. Stage15-6cl shows that the complementary support shrinks by `D0^-2`, but no corresponding weighted-count decay is yet certified because the reciprocal complementary-product average is open.

Therefore the coupled optimization still has no legal polynomial threshold. A hypothetical pair of future bounds
\[
\mathcal M_{\le D_0}(B)\ll B^{1+o(1)}+B^{1-\delta}D_0^A,
\qquad
\mathcal M_{>D_0}(B)\ll B^{1+o(1)}D_0^{-\sigma}
\]
would permit a polynomial choice of `D0` only when the first error carries genuine `B^{-delta}` room and `sigma>0`. Neither ingredient is currently proved.

The two missing inputs remain coupled through the same threshold, so the split trigger remains false. They are analytically different theorem species, but not independent controller targets until a nonempty polynomial overlap window is certified.

Candidate-ledger update:
- softer per-modulus physical root-line error: LIVE;
- physical reciprocal complementary-product average: LIVE;
- exact phi resummation as sufficient fix: BLOCKED;
- Markov large-range decay: BLOCKED;
- immediate split: BLOCKED pending overlap window.

```text
STAGE15_6_SUBSTAGE=6cm
STAGE15_6CM_COUPLED_OPTIMIZATION_RECOMPUTED=true
STAGE15_6CM_POLYNOMIAL_OVERLAP_WINDOW_PROVED=false
STAGE15_6CM_SPLIT_TRIGGER=false
STAGE15_6CM_SMALL_LIVE_GATE=SOFTER_PER_MODULUS_PHYSICAL_ROOT_LINE_ERROR
STAGE15_6CM_LARGE_LIVE_GATE=PHYSICAL_RECIPROCAL_COMPLEMENTARY_PRODUCT_AVERAGE
STAGE15_6CM_AUDIT_REQUIRED=true
STAGE15_6CM_CODEX_REQUIRED=false
STAGE15_6CM_MERGE_ALLOWED=false
STAGE15_6CM_EXIT=FRESH_AUDIT_OF_TWO_COUPLED_LIVE_THEOREM_SPECIES
```