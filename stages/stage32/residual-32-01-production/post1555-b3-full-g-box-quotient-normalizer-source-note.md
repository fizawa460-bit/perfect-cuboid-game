# Stage32 post-1555 principal-b3 full-G / box-quotient normalizer

Scope: fixed recovered V6 class `g1-d186`, `O=210`, `q'=4`, `Q=602`, after hostile-audited and merged #1555.

This leaf resolves the next ambient semantic gate:

> Does the source-locked `b3` lift, already known to normalize `H` and descend to `X=(Z x Z)/H_diag`, also normalize the full order-8 group `G` and therefore descend compatibly through `X -> B=P/G_diag`?

The answer is **yes**. This still does not prove that the hypothetical carrier `N` in `B` is invariant.

## Retained quotient data

The retained quotient chain is

`Z=X(8) -> C0=Z/H -> X4=Z/G`

with

- `H=Gamma'[4]/Gamma[8] ~= V4`, order 4;
- `G=Gamma[4]/Gamma[8]`, order 8;
- `H` normal of index 2 in `G`;
- `C0` has genus 2;
- `C0 -> X4` has degree 2, `X4` has genus 0, and the degree-2 deck involution fixes exactly the six Weierstrass points.

Hence the nontrivial element `tau` of `G/H` is the hyperelliptic involution of `C0`.

The #1555 ambient-normalizer leaf proves that the principal Bolza automorphism `b3` of `C0` admits a semilinear lift

`tilde_b3: Z -> Z`

with `tilde_b3 H tilde_b3^{-1}=H`.

## Hyperelliptic centrality

For a genus-2 curve, the hyperelliptic degree-2 map to genus 0 is unique. Therefore every automorphism of `C0` preserves its fibers and commutes with the hyperelliptic deck involution. In particular,

`b3 tau b3^{-1} = tau`.

This is used only at the curve-quotient level; no Jacobian centralizer assumption is imported.

## Full-G normalizer

Choose any `g in G\H` whose image in `G/H` is `tau`. Since `tilde_b3` normalizes `H`, conjugation by `tilde_b3` is defined on the H-cover. The automorphism

`tilde_b3 g tilde_b3^{-1}`

descends on `C0` to

`b3 tau b3^{-1}=tau`.

Thus `tilde_b3 g tilde_b3^{-1}` differs from `g` by an element of the full deck group `H` of `Z->C0`, so

`tilde_b3 g tilde_b3^{-1} in H g subset G`.

Together with `tilde_b3 H tilde_b3^{-1}=H`, this gives

`tilde_b3 G tilde_b3^{-1}=G`.

Using the same lift on both factors of `P=Z x Z`, the diagonal map `(tilde_b3,tilde_b3)` therefore normalizes both `H_diag` and `G_diag`. It descends simultaneously to

- `beta_X: X=P/H_diag -> X`,
- `beta_B: B=P/G_diag -> B`,

and the quotient map is equivariant:

`pi_XB o beta_X = beta_B o pi_XB`.

So the ambient quotient-normalizer chain is now exact all the way through the box quotient.

## Carrier boundary

The retained common-double-cover identity defines the hypothetical carrier data conditionally as follows:

- `N` is the normalization of a hypothetical integral carrier mapping to `B`;
- `Y` is the normalization of the Beauville pullback `N x_B X`.

Because `X->B` is now `beta_X/beta_B`-equivariant, an additional exact premise

`beta_B(N)=N`

would induce an automorphism `beta:Y->Y` compatible with the two projections to `C0`. That would give `[T,b3]=0` for `T=(f1)_*(f2)^*`. The hostile-audited single-`b3` reduction then gives

`[T,b3]=0 => Q(T)!=602`.

Therefore **carrier invariance would close O210**, but carrier invariance itself is not present in the retained source-locked data.

The current exact blocker is consequently narrower than #1555:

`PROVE_HYPOTHETICAL_CARRIER_N_INVARIANT_UNDER_BETA_B_OR_DIRECT_GAMMA_INVARIANCE`.

## Decision / firewall

Promote only:

`B3_NORMALIZES_FULL_G=true`

`B3_DESCENDS_TO_BOX_QUOTIENT_B=true`

`X_TO_B_B3_EQUIVARIANT=true`.

Do not infer:

- `beta_B(N)=N`;
- `beta_X(Y)=Y`;
- intrinsic `beta:Y->Y`;
- `(b3 x b3)^* Gamma=Gamma`;
- actual `[T,b3]=0` or `[T,b3]!=0`;
- unconditional `Q(T)!=602`;
- exclusion of `O210`;
- authorization of `O212+`;
- effectivity, FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit.

The Stage32 controller remains unchanged.
