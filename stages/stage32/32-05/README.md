# Stage32-05 — fixed-weight MITM feasibility benchmark

This stage is an engineering benchmark only. It carries **no theorem credit** and **no receiver credit**.

Goal: test whether the 48 exceptional binary selected-intersection coordinates are small enough, after fixed-Hamming-weight splitting and exact linear completion bounds, to justify implementing a full exact meet-in-the-middle backend.

Initial benchmark parents:

- `d6-g1-e2-a39`
- `d6-g1-e10-a15`

The benchmark reconstructs the exact 64 selected-intersection coordinate map from the source-locked Stage32 Picard core and checks:

- selected determinant `2^38`;
- inverse denominator `8`;
- Smith invariant factors `1^40, 2^14, 4^6, 8^4`;
- all fixed-weight splits `j + (e-j)` of the 24+24 exceptional partition;
- exact completion interval pruning from all 140 transformed pairing bounds;
- exact degree / first-46 mass / total-nonexceptional mass completion bounds;
- denominator-8 residue-bucket statistics on a deterministic uniform sample for large weight layers.

For large layers, pruning rates and bucket statistics are sampled and therefore are **performance evidence only**. The benchmark never declares UNSAT, never closes a residual parent, and never changes any Stage29/32 receiver status.

Hard firewalls:

```text
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
UNSAT_CLAIM=false
LOW_DEGREE_PREFIX_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
```

Stop rule: if the e=10 benchmark predicts multi-million viable half tables with weak residue/aggregate bucket discrimination after the exact interval bounds, do not build the full MITM backend from this layout; redesign the key/projection first.
