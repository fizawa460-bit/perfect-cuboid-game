# Stage32 post1648AI — FSM nodewise-unibranch proof adapter

Scratch-only source note. No theorem / receiver / route / endpoint credit is granted by this file.

## Audited parent

- Stage32 PR `#1648`
- hostile re-audit: `PASS`
- hostile review: `5127517046`
- audited exact head: `673e5cdb6ace160f2bc6be00688ad6084cef97ad`
- merged main commit: `24215fa27a631cd3cb370c0dfd76866dd2e916f1`

The prior hostile FAIL at review `5127399479` remains historical and is not overwritten.

## Primary source

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675–691, DOI `10.1307/mmj/1480734014`.

Author preprint:
`https://www.mathi.uni-heidelberg.de/~freitag/preprints/box.pdf`

Exact locator: §3, Theorem 3.1 and its proof, printed pp. 10–11 of the preprint.

The proof constructs
`T = Delta(z)^k Delta(w)^k f(z,w) (dz dw)^(8k)`
on the minimal resolution `Btilde`.

The displayed proof states:

- `T` is holomorphic away from the 48 exceptional curves and may have poles only along those exceptional curves;
- after pullback to the normalization `Cbar`, the tensor has degree `16k`;
- `f` can be chosen not to vanish identically on `C` and not to vanish at any of the 48 nodes;
- the poles of the pullback are intersection points of `Cbar` with the exceptional divisor;
- the proof invokes global bijectivity at the pole-count sentence: because `Cbar -> C` is bijective, `Cbar` meets each exceptional curve at most once;
- at one such branch the translation-lattice data satisfy
  `a1 == a2 == 0 (mod 4)`, `a1+a2 == 0 (mod 8)`, `a1,a2 > 0`,
  and the local pole order is at most `(16-(a1+a2))*k`, hence at most `8k` if positive;
- the zero divisor of `f` contributes at least `2kd` zeros.

## Nodewise-unibranch adapter

For the pole-count step, the stronger global assumption
`normalization_map_is_globally_bijective`
can be replaced by the local condition

`for every box-surface node s, card(nu^{-1}(s)) <= 1`.

Indeed this is exactly what is needed to ensure that the normalization has at most one point over each exceptional curve. The rest of the displayed pole/zero bookkeeping is unchanged.

This weaker hypothesis deliberately allows the normalization to be noninjective over the smooth ambient locus. Such a self-node or other curve singularity does not create an additional pole of the pulled-back tensor because the source-locked tensor is holomorphic away from the exceptional curves.

This is a proof-level adapter extracted from the displayed proof of FSM Theorem 3.1; it is not claimed as a separately stated theorem of Freitag–Salvati Manni.

## V6 specialization

For the retained V6 class:

- geometric genus under test: `g=1`;
- projective degree: `d=186`;
- positive exceptional support: `N=47`;
- exact exceptional mass: `e=266`;
- the unique zero exceptional label is `6`.

Hence the pulled-back tensor satisfies

`#zeros >= 2*k*d = 372k`.

If all 47 met node branches have the minimal positive pole budget, then

`#poles <= 8*k*N = 376k`.

The translation-lattice conditions make `(4,4)` the unique positive pair with `a1+a2 < 16`. Therefore if even one met node branch is nonminimal, its positive pole contribution drops from at most `8k` to `0`, so

`#poles <= 8*k*(N-1) = 368k < 372k <= #zeros`.

For `g=1`, the pulled-back tensor has divisor degree zero, so `#zeros=#poles`. Thus every one of the 47 met node branches must be of cusp type `(4,4)`.

At the `A1` quotient node, the local invariant coordinates
`x=p^2, y=pq, z=q^2`
have orders `[1,1,1]` for `(4,4)`. The strict transform therefore meets the exceptional line transversely with multiplicity `1`. Under nodewise unibranchness the total exceptional mass would consequently be exactly `47`.

The retained V6 mass is instead `266`. Contradiction.

## Exact conclusion and firewall

The exact bounded conclusion is:

`NO_INTEGRAL_GEOMETRIC_GENUS1_V6_CARRIER_UNIBRANCH_OVER_ALL_BOX_SURFACE_NODES`.

Equivalently, if an integral geometric-genus-1 V6 carrier exists, then at least one met box-surface node has two or more normalization preimages.

Smooth-ambient-locus singularities may still coexist with such a multibranch surface node. This adapter does **not** claim that all normalization noninjectivity occurs at surface nodes, and it does not materialize an integral carrier member.

Therefore the previously premature surface-node multibranch route becomes justified only after this adapter:

`QUANTIFY_SURFACE_NODE_MULTIBRANCH_LOCAL_TYPES_USING_EXCEPTIONAL_PAIRINGS_AND_FSM_POLE_BUDGET`.

All Stage32 endpoint firewalls remain closed.
