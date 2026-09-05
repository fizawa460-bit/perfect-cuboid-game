# Stage32 post1588 Hperp nonexceptional mod-2 witness source note

## Scope

This note freezes one narrow subgoal authorized after #1588: produce a source-bound known geometric Picard class whose reduction mod 2 is not in the span of the retained exceptional known curves. It does **not** exclude the surviving Q602 residue 73.

## Exact retained source chain

The computation uses only the already-retained chain

`stage33/33-07/stage32_picard_marking_retained.py`
→ `hperp_text`
→ `stages/stage32/residual-32-01-production/hperp_integral_adapter.py`
→ exact all-140 intersection matrix and integral coordinates in the retained Picard64 basis.

The retained Picard bundle is `stages/stage33/33-07/picard_base_rows_retained.py`, canonical SHA256 `d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c`, with upstream git blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`. The retained Hperp text SHA256 is `af373f16d6ab2bb8aed6ca09e0a15c8b28d565cbec6f242a8b76c590df81bb4f`.

`HperpIntegralPairingAdapter` fail-closes the all-140 reconstruction: labels 1..92 are the retained normal known curves with self-intersection -4, labels 93..140 are the retained exceptional known curves with self-intersection -2, all 140 classes have integral coordinates in Picard64, and the selected geometric 64-class change of basis is unimodular. This is why the present witness is not an arbitrary lattice vector such as the earlier post21bl diagnostic sample.

No claim beyond the retained known-curve geometry is introduced here; in particular, this note does not infer effectivity for a newly synthesized Picard vector.

## Exact F2 calculation

Reduce the 140 integral Picard64 coordinate rows modulo 2. Exact bit Gaussian elimination gives

- exceptional span rank: 38;
- normal span rank: 44;
- combined all-140 rank: 64;
- therefore the normal known curves contribute 26 dimensions modulo the exceptional span.

Testing all 92 normal rows individually shows that every label 1..92 lies outside the exceptional span.

The deterministic first witness is normal known curve label 1. It is itself a member of the selected geometric 64-class basis. A dual separator exists with retained-Picard-coordinate support `[1]`; direct replay verifies that it annihilates all 48 exceptional rows and evaluates to 1 on normal label 1.

The exact preflight that produced these values ran at head `493840409aa797141d814de4e46de664fe9f781b`, Actions run `33965268473`, job `101304163848`, conclusion SUCCESS.

## Credit firewall

Obtained: a source-bound retained known normal curve with nonzero image in `Picard64(F2) / <exceptional known curves>` and an explicit separating F2 functional.

Not obtained: an action of this witness on the surviving Q602 residue, an odd commutator, Q602 exclusion, O210 exclusion, controller promotion, receiver/route/theorem/endpoint credit, or perfect-cuboid credit.

The next admissible calculation is therefore to determine whether the source-bound nonexceptional witness supplies a computable action/correspondence or parity/intersection functional on residue 73. Only that additional bridge could advance the finite Q602 leaf.
