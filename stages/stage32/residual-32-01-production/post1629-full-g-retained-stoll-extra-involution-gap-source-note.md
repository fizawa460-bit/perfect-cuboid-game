# Stage32 post1629 full-G / retained-Stoll extra-involution interface gap

This leaf is a bounded interface statement, not a repository-wide absence claim.

Exact positive input is retained on both sides:

- `post1473-x8-v4-cusp-quotient.json` gives `H=Gamma'[4]/Gamma[8]` of order 4 inside `G=Gamma[4]/Gamma[8]` of order 8, with `T4` outside `H`, and the degree-2 quotient `C0 -> X4`.
- `post1555-b3-full-g-box-quotient-normalizer.json` proves the principal `b3` lift normalizes the full `G`, chooses an element `g in G-H` lifting the hyperelliptic deck involution `tau`, and proves `b3` commutes with `tau` downstairs.
- `post1532-full-stoll-h-orbit-symmetry-negative.json` gives the retained Stoll realization of `H` itself: `u=g7*g9`, `v=g7*g8`, `uv=g8*g9`.

The missing semantic bridge is narrower: the checked retained chain does not identify the nontrivial `G/H` deck element (`T4`, equivalently a lift of `tau`) with a specific member of the retained Stoll permutation action on the 140 known curves. `post1473` itself keeps the firewall that its abstract cusp orbits are not yet identified with the retained boundary labels. `post1555` uses an existential `choose_g_in_G_minus_H_lifting_tau`; it does not supply a retained Stoll word or 140-class permutation for that `g`.

Therefore the full-`G` normalizer theorem cannot yet be used to select a smaller subset of the 128 retained order-3 Stoll candidates from the post1629 sweep. Choosing an arbitrary retained Stoll involution outside `H` as `T4` would be an unsupported semantic identification. Likewise, the exact action on the abstract character space of `G` must not be promoted to an action on the retained Picard64 basis without an adapter.

No residue-specific commutator is obtained. Q602 survivors remain `[73,97,235]`. There is no Q602/O210 exclusion and no controller promotion.

The next admissible leaf is to source-lock `T4` (or the equivalent nontrivial `G/H` deck involution) as a retained Stoll member/permutation, or to bypass that identification with a direct source-bound marked Picard action.
