# Stage32 post-1563 ambient-symmetry exhaustion batch

Scope: fixed recovered V6 class `g1-d186`, `O=210`, `q'=4`, `Q=602`, after hostile-audited and merged PR #1563.

This is deliberately a **batch** rather than another one-gap localization leaf.  It tests the same blocker through the formal Arsenal action-identification route, the full box-surface automorphism theorem, the retained Stoll 1536-action, the principal-`b3` quotient lift, and bounded direct-correspondence / valence source checks.  A failed subroute is recorded as such; no new "missing adapter" is promoted merely because a source does not contain one.

## Route A — Research OS / Arsenal routing

The current Arsenal index routes finite-action semantic identification to the formal Stage30 card

`S30-W01 = FINITE_EQUIVARIANT_ACTION_IDENTIFICATION`.

Its audited contract is exactly the present situation: reconstruct the concrete finite actions, freeze conventions, exhaust finite candidates (or use an exact replacement proof), and then require a source-locked common geometric/moduli/algebraic anchor before adapter credit.  It explicitly forbids `abstract G ~= H => semantic adapter`.

The same index also exposes:

- formal `S30-W02 = SEMILINEAR_GALOIS_DESCENT_ADAPTER`, useful only on the semilinear-lift side;
- provisional `S32-PW05 = FINITE_GROUP_EQUIVARIANT_RECONSTRUCTION`, which consumes a proved action/invariance and explicitly does not supply semantic/geometric identification.

So the relevant new weapon after #1563 is **S30-W01**, not a re-run of S32-PW05.

## Route B — exact replacement for the missing marked-Picard word

Two independent source families meet on the same box surface.

### Freitag–Salvati Manni common modular anchor

Primary source:

- Eberhard Freitag and Riccardo Salvati Manni,
  *Parametrization of the box variety by theta functions*,
  arXiv:1303.6495v1, Section 2, Theorem 2.4 and the immediately following automorphism-group paragraph.

Exact facts used here:

1. Theorem 2.4 identifies the complex box variety with
   `Hbar x Hbar / Delta(4,8)` via the seven displayed theta products.
2. `Delta(4,8)` is normal in `Delta(1,2)` with index `768`.
3. Adding factor swap gives a subgroup of order `1536`.
4. By Stoll–Testa the automorphism group itself has order `1536`; hence this is the **full automorphism group of the box variety**.

Section 4, Lemma 4.1 additionally gives
`Gamma'[4]/Gamma[8] ~= (Z/2)^2`, free on `X(8)`, exactly the retained `H` used by Stage32.

This is the common modular/geometric anchor required by formal Arsenal card S30-W01.

### Stoll–Testa concrete box-coordinate action

Public verification source:

- repository `MichaelStollBayreuth/Verification`;
- main commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`;
- file `Cuboids/cuboids.magma`;
- Git blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`;
- locator: comment `// The automorphism group (see Proposition 4)`.

The code defines the same box surface in coordinates
`(a1,a2,a3,b1,b2,b3,c)`, constructs the 92 known curves plus 48 exceptional classes, and gives nine explicit coordinate substitutions:

1. swap `(a1,a2)` together with `(b1,b2)`;
2. swap `(a1,a3)` together with `(b1,b3)`;
3. the non-obvious `i`-linear Stoll automorphism;
4–9. the six independent sign changes of `a1,a2,a3,b1,b2,b3`.

It computes their permutations on all 140 known curve/exceptional labels, descends them to the rank-64 Picard group, and defines `AutS` from those matrices.

The retained Stage32/33 Picard interface is source-locked to this same nine-generator Stoll action.  The hostile-audited post1532 finite certificate closes that retained action to exactly `1536` elements.

Therefore there is no abstract-group identification here:

- the Stoll generators are actual automorphisms of the **same source-locked box surface**;
- their retained action has exactly `1536` distinct elements;
- the full box-surface automorphism group has exactly `1536` elements.

Hence the retained 1536-element Stoll action **is the full box-surface automorphism group**.  This is the exact-replacement proof allowed by S30-W01; an explicit word for every future automorphism is not needed to know membership in the exhausted action.

## Route C — place the principal-b3 box lift inside the exhausted action

Merged #1556 source-locks an actual automorphism

`beta_B : B -> B`

obtained from the principal Bolza `b3` semilinear lift after normalizing full `G = Gamma[4]/Gamma[8]`.

The retained principal matrix is

`b3 = [[-1,-1],[1,0]]`

and has exact order `3`.  On the genus-two quotient `C0 -> X4` the only deck kernel is the hyperelliptic involution `tau` of order `2`.  Therefore the order-three `b3` descends nontrivially to `X4`.

By contrast, the retained four-element relative-`H` actions are represented by `(h,1)` with `h in H subset G`; they are trivial after passing either affected `X(8)` factor to `X4 = X(8)/G`.

Consequently the #1556 automorphism `beta_B` is **not** one of the four retained `H` elements.

Combining this with Route B gives

`beta_B in Aut(B) = retained_Stoll_1536`, but `beta_B notin H`.

This closes the exact #1563 membership/exhaustion gap without guessing a Stoll word or a 140-label permutation.

## Route D — consume the already exhaustive H-orbit computation

The hostile-audited `post1532-full-stoll-h-orbit-symmetry-negative.json` proves, over all `1536` retained Stoll elements, that:

- exactly four elements send the recovered V6 base numerical class `C` into its four-element `H` orbit;
- those four are exactly `H`;
- the setwise stabilizer of the whole `H` orbit is also exactly `H`.

Since `beta_B` is in the exhausted action but outside `H`,

`beta_B(C) notin H.C`

and `beta_B(H.C) != H.C`.

This also survives every retained `H` deck ambiguity: for every `h in H`, `h*beta_B` is still outside `H`, so no deck-adjusted principal-`b3` lift sends `C` into `H.C`.

For a hypothetical integral carrier `N` in the exact recovered V6 divisor class, setwise equality `beta_B(N)=N` would force equality of divisor classes `beta_B(C)=C`.  The finite result forbids even the weaker condition `beta_B(C) in H.C`.  Hence

`N exists in exact V6 class  =>  beta_B(N) != N`.

This is a conditional non-invariance theorem about any such hypothetical carrier; it is **not** an existence or nonexistence theorem for the carrier itself.

The old re-entry condition

`SYMMETRY_OUTSIDE_RETAINED_STOLL_FINITE_ACTION`

is now closed: the retained Stoll action is the full box-surface automorphism group.

## Route E — direct Gamma / valence source check

The batch also inspected the three source families that actually govern the current geometry:

1. Freitag–Salvati Manni, arXiv:1303.6495v1 (theta/modular box quotient and automorphisms);
2. Stoll–Testa / `Cuboids/cuboids.magma` (box automorphisms and Picard action);
3. Cecotti, arXiv:2509.24605v1, Appendix B (principal Bolza/G12 matrices and explicit Bolza automorphisms).

They provide the modular quotient, full automorphism action, and principal-`b3` data used above.  In the inspected locators they do **not** provide either

`(b3 x b3)^* Gamma = Gamma`

for the Stage32 hypothetical `(105,81)` correspondence, or an integral valence/scalarity theorem for that correspondence.

This is only a bounded source statement about the inspected contracts.  It is not a literature-wide nonexistence claim and it grants no negative theorem about `Gamma`.

## Batch decision / anti-loop boundary

Promote the following exact conclusions only:

- `retained_Stoll_1536 = Aut(box surface)`;
- `beta_B` belongs to that exhausted action;
- `beta_B` is outside retained `H`;
- `beta_B(C) notin H.C`;
- the entire ambient box-automorphism / "symmetry outside retained Stoll action" re-entry lane is exhausted;
- any hypothetical exact-V6 carrier is not setwise invariant under this principal-`b3` box lift.

Do **not** infer:

- actual `[T,b3]=0` or an unconditional `[T,b3]!=0`;
- direct `Gamma` invariance or non-invariance;
- integral valence/scalarity of `Gamma`;
- exclusion of `Q=602` or `O=210`;
- authorization of `O212+`;
- effectivity, FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit.

There is no further "ambient symmetry adapter gap" leaf after this batch.  Re-entry requires genuinely new **direct correspondence/divisor information** or an **independent valence/scalarity theorem**, not another search for a box automorphism outside the retained 1536 action.
