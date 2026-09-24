# Stage32EX5 HPADJ23 — exact feasible-t support producer

Status: **BOUNDED STRUCTURAL STRICTNESS RETAINED / PRODUCER ONLY / ZERO MAIN CREDIT**

## Why this leaf exists

V48 consumes a 384-coordinate support-qBC refinement, but that consumer deliberately replaces the true feasible `t` set by a parity interval hull. The 32-01-178 research note already records preserving feasible `t` holes as `UNTESTED`; therefore EX5 must not duplicate the 178 consumer computation.

EX5 instead owns the producer refinement: retain exact `t` in the HPADJ22 joint BC state, producing a histogram keyed by `(b,c,support,required_parity,qBC,t)`.

## Retained bounded gate

The independent H=4 replay proves the proposed producer is genuinely stricter than the current hull representation:

- 686 valid canonical BC tuples;
- 151 exact bins with required parity; 91 are strict against the current hull;
- 146 hull-only `t` points are removed across those strict bins;
- after marginalizing required parity, 101 bins remain and 52 are still strict;
- 74 hull-only `t` points remain removable after that marginalization;
- witness: `(b,c,support,qBC)=(0,4,1,16)` has exact `t={0}`, while the current safe hull is `{0,2,4}`.

This is structural producer evidence only. No V48 coordinate was recomputed and no global numerical tightening is claimed.

## Ownership / anti-duplication

- producer: Stage32EX5;
- producer output: exact joint BC/t histogram interface;
- downstream consumer: `32-01-178`, which retains ownership of any V48-or-successor same-population intersection;
- EX5 does not run the 178 consumer or claim its savings;
- MAIN promotion requires a later source/target adapter and hostile audit.

## Next exact gate

The scalable source-locked builder is now retained and bounded-replayed through H=16. It reproduces the HPADJ22 qBC/required-parity marginals exactly at H=4 and H=16, while the H=4 exact-t histogram also matches literal brute force. At H=16 there are 47,667 exact bins; 39,995 are strict versus the current hull and 196,035 hull-only t-points are removed. After required-parity marginalization, 20,599 of 26,674 bins remain strict and 90,022 hull-only t-points are removed.\n\nThe next gate is a compact serialization/handoff contract for 32-01-178. Heavy/FULL178 scaleout remains cold.

Merge is not authorized.

## Bounded producer handoff retained

The H=16 producer is now serialized deterministically as UTF-8 JSONL records `[b,c,support,required_parity,qBC,[[t,multiplicity],...]]`. The retained stream identity is 47,667 records, 207,474 exact-t entries, 2,248,811 bytes and SHA-256 `fa84df0ba610c8afec76599a93abe46ed0e494cc3544568f03e6669131d1b4f8`.

The bounded handoff is ready for a 32-01-178 consumer preflight only. It is not a FULL178 producer handoff, does not compute a V48 saving, and does not alter MAIN authority. The next EX5 gate is a cold FULL178 producer-scaleout preflight: partitioning, resume semantics and resource estimates only; no heavy run is armed.

## FULL178 scaleout preflight retained — cold

The producer does **not** need 178 independent BC/t histogram builds. FULL178 uses even degrees 8..192, hence 93 distinct `H=d/2` values 4..96, and the HPADJ23 BC/t histogram is independent of genus `g`. More strongly, fixed `(b,c)` data is prefix-invariant once the ambient `H >= max(b,c)`; an H=8 versus H=16 exact regression is retained. Therefore one universal `HMAX=96` producer can serve every FULL178 row by prefix restriction.

The universal producer is partitioned provisionally into the same eight b-bands used by HPADJ22: `[0,11]...[84,96]`. A bounded H=16 four-shard test has exact disjoint union equality with the full builder: 47,667 bins, 207,474 exact-t entries, multiplicity 1,305,021.

Production remains cold. Before any H=96 arm, the retained gate requires exactly one representative measurement target `H=32, b=0..11` to record wall/CPU time, peak RSS, raw/compressed bytes, bin count and t-entry count. The measurement runkey is generation 0 / `armed=false`; ordinary mainbatch is not authorized to arm it. No MAIN or theorem credit is granted.
