# Stage32 post1577 direct mod-2 fiber-divisor identity preflight

## Scope

This leaf starts only after the merged #1577 terminal negative for the ambient-symmetry / orbit-sum / parity detector. The fixed target remains `g1-d186`, `O=210`, `qprime=4`, `Q=602`, with surviving residues `73,97,235`.

The purpose is narrow: test the first allowed #1577 reentry species, a **direct mod-2 divisor identity**, using already retained geometry. No arithmetic exclusion or controller promotion is authorized here.

## Exact retained divisor identity

The exact source is `post1484-v6-modular-factor-bidegree-source-note.md`, locked by blob SHA-1 `deeecac5599f3b542b445cd87c2070dae488bc85`.

That source proves on the resolved box surface that, for each retained first-factor boundary line `L` in labels `34,35,38,39,42,43`,

`F_z(L) = 2 L + sum_{E_j incident to L} E_j`,

and for each retained second-factor boundary line `L` in labels `33,36,37,40,41,44`,

`F_w(L) = 2 L + sum_{E_j incident to L} E_j`.

It also records that every retained boundary label `33..44` has exactly eight incident exceptional curves. These are integral divisor identities; this leaf does not reconstruct or strengthen their geometry.

Reducing the exact identities modulo 2 gives

`F_z(L) = sum_{E_j incident to L} E_j (mod 2)`,

`F_w(L) = sum_{E_j incident to L} E_j (mod 2)`.

Thus a genuine direct mod-2 divisor identity is available after #1577.

## Exceptional-quotient preflight

The right-hand side of each mod-2 identity is, by construction, in the span of exceptional classes. Therefore the image of every one of these mod-2 fiber classes in the quotient of Picard mod 2 by the exceptional span is exactly zero.

This is the bounded conclusion of this leaf. The direct identity exists, but these particular fiber classes do **not** provide a nonexceptional mod-2 class capable by themselves of repairing the #1577 blow-down obstruction or forcing a residue-specific commutator for `73,97,235`.

The next admissible input must therefore be a direct mod-2 correspondence/divisor identity with a proved nonexceptional component, or an independent primitive/odd commutator invariant. Repeating the closed ambient-symmetry / orbit-sum / parity detector is not authorized.

## Firewalls

- The retained factor-map degrees `105` and `81` are not promoted to divisor identities or correspondence eigenvalues.
- The degree-two common-cover push-pull relation is not promoted to mod-2 injectivity.
- An exceptional-supported mod-2 identity is not promoted to a nonzero blow-down class.
- No residue-specific commutator nonvanishing is obtained.
- `Q602_excluded=false`, `O210_excluded=false`, and `O212+` advance remains unauthorized.
- No controller, receiver, route, theorem, endpoint, or perfect-cuboid credit follows.
