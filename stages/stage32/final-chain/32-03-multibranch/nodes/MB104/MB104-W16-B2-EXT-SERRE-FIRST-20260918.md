# Stage32 MB104 — W16-B2 solo: Ext / Serre-first — 2026-09-18

Status: **NO INDEPENDENT EXT BYPASS / ABSORBED BY CB / NO MATHEMATICAL CREDIT**

## Scope

This checkpoint advances W16-B2 only. It starts from the A2 object

`Z=Z_red=(nu(R_phi))_red subset S`,

which is nonempty, reduced, zero-dimensional lci and satisfies `length(Z)<=112l`.

The question is whether normalization/conductor/ramification duality can directly produce a locally-free non-split extension

`0 -> O_S(K) -> E -> I_Z(D_l) -> 0`

without separately proving `CB(|D_l|)`.

## 1. Local-to-global Ext exact sequence

Put

`V=Ext^1(I_Z(D_l),O_S(K))`.

Since `Z` is codimension two lci on the smooth surface,

`Hom(I_Z(D_l),O(K)) = O(K-D_l)`

and local duality gives

`Ext^1_sheaf(I_Z(D_l),O(K)) ~= omega_Z tensor O_Z(-D_l)`.

For reduced `Z` this is one one-dimensional local Ext fibre at every point.

The local-to-global Ext spectral sequence gives the low-degree exact sequence

`0 -> H^1(K-D_l)`
`  -> V`
`  -> H^0(omega_Z tensor O_Z(-D_l))`
`  -> H^2(K-D_l)`.

Reference for the Ext spectral sequence: Stacks Project, tag 0BQP.

By Serre duality, the last arrow is dual to the evaluation map

`ev_Z : H^0(O_S(D_l)) -> H^0(O_Z(D_l))`.

Thus the possible local residue vectors of global extension classes are exactly the annihilator of the evaluation image.

## 2. Local freeness is exactly the CB condition

For a reduced point `p in Z`, a Serre extension is locally free at `p` exactly when its local Ext component at `p` is nonzero.

Hence a globally locally-free extension exists exactly when the annihilator of `im(ev_Z)` contains a vector with every coordinate nonzero.

Over the present characteristic-zero field this has an elementary linear-algebra reformulation.

- If `im(ev_Z)` contains a nonzero vector supported at one point `p`, every annihilating vector has zero `p`-coordinate.
- Conversely, if no such one-point-supported vector occurs, the annihilator is not contained in any coordinate hyperplane. A finite union of proper hyperplanes cannot cover a vector space over an infinite field, so an annihilating vector with all coordinates nonzero exists.

But 'no one-point-supported evaluation vector' is precisely

`every section of |D_l| vanishing on Z\{p} also vanishes at p`

for every `p`, i.e.

`CB(|D_l|)`.

This is exactly the classical Hartshorne–Serre criterion; see Huybrechts–Lehn, Theorem 5.1.1 (also restated in Coskun–Huizenga, *The moduli spaces of sheaves on surfaces*).

Therefore

`locally-free Ext class exists  <=>  CB(|D_l|)`.

Ext-first is not a logically separate bypass.

## 3. Why the ramification divisor does not yet provide the local Ext vector

The retained ramification data supply:

- the finite support `Z`;
- the multiplicities upstairs in `R_phi`;
- the line `O_E(R_phi)=phi^*O_P1(2)`.

The local Serre residues instead live in

`omega_Z tensor O_Z(-D_l)`.

No retained source-complete morphism or trivialization identifies the ramification derivative line with these local Ext fibres.

The numerical coincidence

`deg R_phi =112l = deg nu^*K_S`

is not enough: on an elliptic curve, equal-degree line bundles differ by an arbitrary class in `Pic^0(E)`, and the retained MB104 geometry already exhibits nontrivial torsion ambiguities on `E`.

Thus neither ramification multiplicities nor the degree equality produce the required annihilating residue vector.

## 4. Route consequence

B2 cannot independently advance W16.

Any future 'direct Ext construction' that is actually locally free will, by the exact sequence above, simultaneously prove the CB relation. So the missing information is still the evaluation dependency itself.

This does not close W16 negatively. It only closes

`Ext/Serre-first as an independent bypass of CB`.

A3 remains genuinely different: if the ramification locus can be realized as an ambient differential/determinantal degeneracy scheme, that geometry may itself force the missing evaluation dependency.

## B2 disposition

`W16-B2 = ABSORBED_BY_CB_FIRST`.

Next solo branch: `W16-A3 differential / determinantal degeneracy`.

## Firewalls

- No CB property is proved or disproved for `Z_red`.
- No statement that no locally-free Serre extension exists.
- No `l>=2` exclusion.
- No MB104/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit.
- No merge authorization.
