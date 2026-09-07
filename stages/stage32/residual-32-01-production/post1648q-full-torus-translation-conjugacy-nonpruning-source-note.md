# Stage32 post1648Q scratch source note — full-torus translation conjugacy nonpruning

This leaf is scratch-only and grants no MAIN or arithmetic credit.

post1648N fixes the exact KKK/Bolza order-8 homology action for `mu1: x -> i*x`, and post1648O checks at `A[2]` that every one of the six retained B9 linear images can absorb its Deraux affine translation by conjugating with a translation.

The full lattice calculation is stronger and removes any concern that the mod-2 result is accidental. In the KKK coordinate action,

`det(I - mu1) = 2`.

Hence `I-mu1` has no eigenvalue 1 and defines a nonzero isogeny of the Bolza Jacobian. An isogeny of a complex abelian variety is surjective. For any polarized ppav isomorphism `M`, the retained linear image `A=M mu1 M^-1` therefore also satisfies `det(I-A)=2`, so `I-A` is surjective on the target torus.

For an affine action `(A,t)`, conjugation by translation `tau_s` changes the translation part by `(I-A)s`. Surjectivity gives an `s` for every `t`. Therefore no affine translation datum attached to B9 can select one of the six retained linear images, and in particular cannot select one of the three retained Richelot lines.

This exactly closes the route “use zero/nonzero B9 translation as the missing absolute marking.” The remaining load-bearing datum must preserve more marking than an arbitrary affine conjugacy: an origin-preserving marked ppav identification, a marked theta divisor / half-period normalization, or the actual KRR conjugating map together with its linear marking.
