# Stage32-18AM — one-wall breakthrough scout

Target: p436/s5 only.

Purpose: scout many untried lower48 exact unimodular basis-selection strategies while 18AL performs full-budget attacks. This scout does not choose a winner by runtime. Promotion requires exact COMPLETE within the scout budget.

Budget: 12 parallel modes, 6M nodes, 20 minutes each, max-parallel 15. Coordinates 48..62 are untouched; x1024 shard identity is unchanged. Each transformation is a product of integer determinant-one shears applied consistently to q, cap rows, and symmetry rows.

Modes: window2, window4, window8, global, cap-forward, cap-reverse, sym-forward, sym-reverse, mixed-forward, mixed-reverse, mixed-zigzag, mixed-two-pass.

Previously tried/frozen ideas are not included: baseline scheduler variants, coordinate permutations, pairwise symmetry KKT, pairwise-cached, cap-sym-active, combined-active, and the 18AL forward/reverse/alternating2 basis weapons.

If none COMPLETE, the next redirection is partial-assignment Aut/orbit canonical augmentation or meet-in-the-middle/block enumeration, not another runtime-based promotion.
