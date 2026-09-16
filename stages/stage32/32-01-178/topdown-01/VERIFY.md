# TD01 verification boundary

Route: `TD01_GRF02_HPADJ08_TOPDOWN_COMPOSITION`.

This surface starts from Stage32 MAIN PR #1808 exact head `4f7889e79d9d967d410bfcf781ade8e215703a5d` and does not reopen the closed N401-N405 retained-97-block route.

## Retained bounded result

The deterministic bounded probe `probe_td01_grf02_hpadj08_panel.py` reproduces the two retained HPADJ08 low-degree totals exactly before adding the new completion parity:

- old group-Cauchy rejected: `3,257,761,571,005`;
- HPADJ08 exact-square rejected: `25,770,706,503,487`.

On the identical `g in {0,1}`, even `d=8..32`, `HMAX=16` panel, HPADJ08 has `11,531,305,094,786` survivors. Adding the exact GRF-02 primitive completion condition

`x0 + x4 + x8 + x10 == 0 (mod 2)`

rejects `5,765,698,043,645` of those survivors and retains `5,765,607,051,141`.

This is bounded exact evidence only. It grants no FULL178, MAIN pruning, effectivity, receiver, theorem, endpoint, Stage32-closure, or perfect-cuboid existence/nonexistence credit.

## Prepared FULL178 continuation

`FULL178-SCALEOUT-CONTRACT.json` and `td01_full178_b_shard.py` prepare the same one-bit refinement over the retained HPADJ08 178-row domain using the same eight `b` shards. Execution is not armed. Heavy execution requires the repository heavy-workflow authorization gate and an explicit run key/workflow surface before any shard is run.

Acceptance for any future FULL178 aggregate must fail closed unless the replay first reproduces the retained HPADJ08 aggregate baselines exactly:

- old group-Cauchy rejected: `20,713,268,924,714,183,714,810`;
- HPADJ08 exact-square rejected: `40,886,299,509,963,924,857,401`;
- retained HPADJ08 row stream SHA256: `d5d8ab364d122c4b3138d577442b383290ab7878e11629b3673058073690e5a1`.

After a complete exact FULL178 run, any MAIN interaction must use an independently certified combined-survivor upper bound and conservative `MIN_OF_INDEPENDENT_CERTIFIED_UPPER_BOUNDS` composition unless a separate exact current-authority subset/no-double-charge adapter is proved. Additive subtraction of the bounded diagnostic or candidate gain is forbidden.
