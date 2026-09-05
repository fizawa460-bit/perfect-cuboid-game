# Stage32 post1612 Hperp nonexceptional mod-2 witness authority repair

## Scope

This note repairs one authority defect found by the post-merge hostile audit of PR #1612. The Hperp calculation itself is unchanged: it produces a source-bound known geometric Picard class whose reduction mod 2 is not in the span of the retained exceptional known curves.

PR #1612 incorrectly routed that witness against a sole surviving Q602 residue `73`. The latest hostile-audited Stage32 frontier does not authorize that contraction. The audited survivor set remains `[73,97,235]`, so this repair restores exactly that set and adds no residue exclusion.

## Audited Q602 survivor authority

The authority is source-locked through two retained certificates:

- `post1570-three-involution-q602-exclusion-batch.json`, blob `255fc831031474ba725e5ea188e829afd62473f6`, canonical SHA256 `8af12197316f8d23b7fa94fa7d064fded355a59d5c0cd5adef47e13826643538`, with fixed survivors `[73,97,235]` and `Q602_excluded=false`;
- `post1577-mod2-fiber-divisor-identity.json`, blob `b031d82fe1ccd0324a6fbdf3ea4a096f15661197`, canonical SHA256 `2aff96ee259e895c2acaa1777a9c214b32187fb0a6a4b489708ed544d0111830`, which retains the same three survivors and obtains no residue-specific commutator or Q602 exclusion.

Thus the Hperp witness may be added as a new missing-input object, but it may not silently delete residues 97 or 235.

## Exact retained Hperp source chain

The Hperp computation still uses only the retained chain

`stage33/33-07/stage32_picard_marking_retained.py`
→ `hperp_text`
→ `stages/stage32/residual-32-01-production/hperp_integral_adapter.py`
→ exact all-140 intersection matrix and integral coordinates in the retained Picard64 basis.

The retained Picard bundle is `stages/stage33/33-07/picard_base_rows_retained.py`, canonical SHA256 `d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c`, with upstream git blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`. The retained Hperp text SHA256 is `af373f16d6ab2bb8aed6ca09e0a15c8b28d565cbec6f242a8b76c590df81bb4f`.

`HperpIntegralPairingAdapter` fail-closes the all-140 reconstruction: labels 1..92 are retained normal known curves with self-intersection -4, labels 93..140 are retained exceptional known curves with self-intersection -2, all 140 classes have integral coordinates in Picard64, and the selected geometric 64-class change of basis is unimodular. No newly synthesized Picard vector is promoted to an effective geometric curve.

## Exact F2 calculation

The exact calculation is unchanged from #1612:

- exceptional span rank: 38;
- normal span rank: 44;
- combined all-140 rank: 64;
- normal contribution modulo the exceptional span: 26;
- every normal label 1..92 lies outside the exceptional span;
- deterministic first witness: normal label 1;
- separating functional support in retained Picard coordinates: `[1]`, annihilating all 48 exceptional rows and detecting label 1.

The original Hperp preflight ran at head `493840409aa797141d814de4e46de664fe9f781b`, Actions run `33965268473`, job `101304163848`, conclusion SUCCESS. The #1612 resynced exact-head replay ran at `694a9dfa18b686a3ef1d3046d5b5416ad3939ce3`, run `33968346373`, job `101312335629`, conclusion SUCCESS.

## Credit firewall and next route

Obtained: a source-bound retained known normal curve with nonzero image in `Picard64(F2) / <exceptional known curves>` and an explicit separating F2 functional.

Not obtained: an action of this witness on any of residues 73, 97, or 235; an odd commutator; exclusion of any of those residues; Q602 exclusion; O210 exclusion; controller promotion; receiver/route/theorem/endpoint credit; or perfect-cuboid credit.

The next admissible calculation is therefore to compute an action/correspondence or parity/intersection functional of the source-bound nonexceptional witness on the full hostile-audited survivor set `[73,97,235]`. Any later contraction of that set requires its own exact source-bound certificate and hostile audit.
