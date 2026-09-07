# Stage32 post1648AH — Freitag–Salvati Manni bijective-normalization source note

Scratch-only source note. No theorem / receiver / route credit is granted by this file.

## Primary source

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675–691, DOI `10.1307/mmj/1480734014`.

Author preprint used for the exact locator:
`https://www.mathi.uni-heidelberg.de/~freitag/preprints/box.pdf`

Relevant locators in §3, Theorem 3.1 and its proof (printed pp. 10–11 in the preprint PDF):

- Theorem 3.1 assumes an irreducible curve `C` for which the normalization map `Cbar -> C` is globally bijective, with normalization genus `g` and projective degree `d`, and proves `d <= 176 + 16g`.
- Near a node, the proof uses cusp parameters `p=exp(2*pi*i*z/8)`, `q=exp(2*pi*i*w/8)` and a branch parametrization with positive integers `(a1,a2)` in the translation lattice satisfying `a1 == a2 == 0 (mod 4)` and `a1+a2 == 0 (mod 8)`; hence `a1+a2 >= 8`.
- For the tensor used in the proof, `(dzdw)^(8k)` contributes pole order `16k` and `Delta(z)^k Delta(w)^k` contributes zero order `(a1+a2)k`. Thus the local pole contribution is at most `(16-(a1+a2))k`, and in particular at most `8k` when positive.
- The same proof gives `16(2g-2)k = #zeros - #poles` and `#zeros >= 2kd`.
- The published proof then bounds the number of pole points by all 48 nodes, obtaining its stated global theorem. For a specific curve satisfying the global bijective-normalization hypothesis and meeting only `N` surface nodes, the identical proof gives the sharper bookkeeping bound `#poles <= 8kN`, hence `d <= 16g-16+4N`.

Relevant locator in §2 (printed p. 7): at the standard singular cusp, `p,q` are uniformizing parameters on the product cover and the stabilizer acts by `(p,q) -> -(p,q)`, so the node is the quotient singularity `C^2/{±1}`. The minimal resolution has one exceptional line.

## Local calculation used in AH

For the quotient node write invariant coordinates

`x=p^2, y=pq, z=q^2`, so `xz=y^2`.

Along the FSM cusp branch, with local punctured-disk parameter `Q=exp(2*pi*i*tau)`, the orders are

`ord_Q(x)=a1/4`, `ord_Q(y)=(a1+a2)/8`, `ord_Q(z)=a2/4`.

If `(a1,a2)=(4,4)`, all three invariant coordinates have order one. Blowing up the node at its maximal ideal resolves the `A1` singularity; in any chart where one of `x,y,z` is the exceptional parameter, its pullback to this branch has order one. Therefore the strict transform meets the exceptional curve transversely and has intersection multiplicity exactly `1` with that exceptional curve.

This last paragraph is an elementary local derivation from the source-locked quotient-node model; it is not quoted as a separate theorem from FSM.

## Stage32 scope

AH excludes only an integral geometric-genus-1 V6 carrier whose normalization map `Cbar -> C` is globally bijective. Its contrapositive is only:

`if an integral geometric-genus-1 V6 carrier exists, its normalization map is nonbijective somewhere`.

AH does not localize that noninjectivity to the 47 met box-surface nodes. At least two branches therefore remain open:

1. two or more normalization preimages over an ambient box-surface node (surface-node multibranch behavior);
2. noninjectivity over the smooth ambient locus, for example a self-node or other singularity of the curve itself.

AE/AG do not exclude either branch. Consequently a next route restricted only to surface-node multibranch local types is premature.
