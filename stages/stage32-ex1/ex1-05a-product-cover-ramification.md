# EX1-05A — product-cover ramification refinement

Status: provisional same-PR candidate. This note does not grant Stage32EX1 authority or Stage32 MAIN credit.

## Exact source

Michael Stoll and Damiano Testa, *Curves on the surface of cuboids*, Mathematics of Computation (2026), DOI `10.1090/mcom/4238`.

Accepted/current author PDF:
`https://www.mathe2.uni-bayreuth.de/stoll/papers/Cuboidi.pdf`

The source gives the following surface-specific structure over the geometric field used by EX1:

- a smooth genus-5 curve `X` with `G0=(Z/2)^3`;
- `Sbar ≅ (X×X)/diag(G0)`;
- the even-sign subgroup `G0+` has order 4 and `C2=X/G0+` has genus 2;
- `Y=(X×X)/diag(G0+)` is smooth and `Y→Sbar` is a double cover ramified exactly over the 48 nodes;
- `Y` maps to `C2×C2`;
- `K_S` is the pullback of the canonical-model hyperplane class and `K_S^2=16`, while `c2(S)=80`.

The paper itself notes that the Bogomolov regime `K_S^2>c2(S)` does not apply here. Thus the generic Miyaoka/Bogomolov low-genus route is not the selected route.

## Derived finite-cover adapter

The quotient `X→C2` has degree 4. Since

`2g(X)-2 = 8 = 4(2g(C2)-2)`, 

Riemann–Hurwitz forces it to be étale. Hence `X×X→C2×C2` is étale of degree 16. Factoring by the free diagonal `G0+` action gives a finite étale degree-4 map

`phi:Y→C2×C2`.

Therefore

`K_Y = phi^* K_(C2×C2)`.

Also `Y→Sbar` is degree 2 and has no divisorial ramification, since its ramification locus consists only of the 48 points. Because `Sbar` is Gorenstein with A1 singularities,

`K_Y = rho^* K_Sbar`.

## Apply to a hypothetical V6 genus-1 carrier

Let `B⊂Sbar` be the canonical image of a hypothetical integral irreducible V6 carrier, and let

`N→B`

be its normalization. EX1-00 fixes

`g(N)=1`, `K.B=186`.

Normalize the fiber product `N×_Sbar Y` and call the resulting degree-2 cover `D→N`.

If this cover were étale, every connected component would have genus 1. But `Y` contains no genus-1 curve: under the finite map `Y→C2×C2`, every curve has a nonconstant projection to at least one genus-2 factor, impossible from genus 1 by Riemann–Hurwitz. Thus `D` is connected and ramified.

Let `a,b` be the degrees of the two maps `D→C2`. Projection formula through `rho` gives

`K_Y.D = 2 K.B = 372`.

Through `phi`, since `deg K_C2=2`,

`K_Y.D = 2a+2b`.

Hence

`a+b=186`.

At least one of `a,b` is therefore at least 93. Riemann–Hurwitz for that projection gives

`g(D)-1 ≥ 93`.

For the double cover `D→N` with `g(N)=1`,

`deg Ram(D/N)=2g(D)-2 ≥186`.

Every ramification point lies above one of the 48 nodes because `Y→Sbar` is étale off those nodes. If `r_i` is the number of normalization points of `N` lying over node `i`, then

`R_node := Σ_i r_i ≥ 186`.

## Consequences for the retained V6 exceptional contacts

EX1-01/02 already proved `r_i≤m_i`, where the 48 exceptional pairings satisfy

`Σm_i=266`, positive support count `47`.

Therefore

`B_node = Σ_{m_i>0}(r_i-1)=R_node-47 ≥139`,

while the previous contact bound gives `B_node≤219`.

Also

`Σ_i(m_i-r_i)=266-R_node≤80`.

The nine unit-contact nodes already have `r_i=1`, so the remaining 38 nonunit nodes carry at least

`186-9=177`

normalization branches.

Using the exact capacities `m_i-1` of those 38 nodes, the 13 largest capacities sum to `138`, while the 14 largest sum to `145`. Hence at least **14 nonunit nodes must be genuinely multibranch**.

Thus the previous residual branch `NO_NODE_MULTIBRANCH` is eliminated at candidate level. This does not eliminate smooth-locus singularities; it proves only that any hypothetical V6 genus-1 carrier must simultaneously have a very large node-multibranch profile.

## Cycle / Arsenal result

A blind breadth pass generated the product-cover/genus-2 route independently of Arsenal. Comparison afterward found no formal Arsenal card that supplies this receiver. Nearby Stage34 cards remain factor-square/Mordell–Weil/receiver-intersection tools and do not subsume the argument.

Other routes remain recorded as untested: symmetric differentials on the cuboid surface, jet/Seshadri/Reider/equisingular constraints, and actual V6 section materialization. No split is opened yet; EX1-05B continues the product-cover route by resolving inertia/parity and component-stabilizer information.

## Credit firewall

This is an unaudited branch-exclusion candidate only. In particular:

- `R_node≥186` is not `delta=472`;
- `B_node≥139` is not a delta lower bound;
- the argument does not construct a V6 member;
- it does not exclude all V6 genus-1 carriers;
- it does not alter Stage32 MAIN or Perfect Cuboid credit.
