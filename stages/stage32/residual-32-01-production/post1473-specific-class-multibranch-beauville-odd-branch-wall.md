# Stage32 post-1473 — multibranch Beauville odd-branch burden for the exact V6 class

## Scope

This note applies only to the exact recovered V6 Picard class on the fixed projection

`g1-d186`, `z=(-15,62,-44,26,32)`, `d=186`,

and to a hypothetical **integral curve of geometric genus 1** in that class whose map to the singular box surface is allowed to be non-bijective over the nodes.

It does not assert that such a curve exists. Its purpose is to derive exact necessary branch-count conditions for the still-open multibranch case and to record whether the retained V6 intersection data alone contradict them.

Retained exact locks:

- V6 witness-body canonical SHA256: `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`
- Picard coordinates SHA256: `2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726`
- all-140 pairings SHA256: `4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3`
- exceptional intersection vector: the locked last 48 entries of the all-140 vector
- total exceptional intersection `e=C.E=266`

The previous hostile-audited FSM leaf already excludes the bijective-normalization branch. This note does not weaken or reopen that result.

## Source locks

Primary source:

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675–691, DOI `10.1307/mmj/1480734014`, arXiv `1303.6495`.

The source provides the following ingredients.

1. `H/Gamma[8]` has genus 5.
2. The product `P=(H/Gamma[8]) x (H/Gamma[8])` maps to the box variety with quotient group `(Z/2)^3`; the 48 nodes are quotient singularities locally of type `C^2/(+/-1)`.
3. The subgroup `Gamma'[4]/Gamma[8] ~= (Z/2)^2` acts freely. Its quotient is the Beauville surface `X`, so `P -> X` is an unramified degree-4 cover and `X -> B` is a degree-2 cover.
4. After blowing up the 48 points upstairs and the 48 nodes downstairs, the induced map `Xtilde -> Btilde` is a double cover ramified along the 48 exceptional curves.
5. The canonical map of `Btilde` is the contraction to the singular box surface followed by the original embedding in `P^6`, so the fixed target degree is `K_Btilde.C=d`.
6. In the FSM tensor proof, a local normalized branch at a node has cusp exponents `a1,a2`, both positive multiples of 4 with `a1+a2` divisible by 8. The audited previous leaf identifies its exceptional contact multiplicity as `m=min(a1,a2)/4`, hence `a1+a2>=8m`.

Standard inputs used below are Riemann–Hurwitz, projection formula, the canonical divisor formula on a product of curves, and normalization of a double cover of a smooth curve: for a local equation `y^2=t^m*unit`, the normalized cover ramifies exactly when `m` is odd.

No claim is made that Freitag–Salvati Manni state the multibranch inequalities below in this form.

## Odd-contact branch divisor

Let `N` be the normalization of the hypothetical integral genus-one curve. The map `N -> Btilde` pulls back the total exceptional divisor as

`D_E = sum_P m_P * P`,

where every `m_P` is a positive integer and

`sum_P m_P = C.E = e = 266`.

For each exceptional curve `E_j`, the sum of the `m_P` over points lying on `E_j` equals the locked exact intersection number `C.E_j`.

Define

- `B = #supp(D_E)`, the total number of normalized branch points above the 48 nodes;
- `O = #{P : m_P is odd}`;
- `S1 = #{P : m_P=1}`.

Because the double cover `Xtilde -> Btilde` is ramified along the exceptional divisor, its normalized pullback to `N` is a double cover `Y -> N` ramified at exactly the `O` odd-contact points. Since the locked exceptional totals contain odd entries, `O>0`, so this cover is connected. For `g(N)=1`, Riemann–Hurwitz gives

`2*g(Y)-2 = O`.

## Product-cover projection bound

Blow down the curve from `Xtilde` to `X` and pull it back through the unramified degree-4 cover

`P = X(8) x X(8) -> X`.

Choose an irreducible pullback component `D`. Its normalization maps unramified to `Y` with degree

`q' in {1,2,4}`.

Hence

`2*g(D)-2 = q' * O`.

The composite generic degree from `D` to the original curve on the box variety is `q=2*q'`. Let `n1,n2` be the degrees of the two projections of `D` to the genus-5 modular curve `X(8)`, with a constant projection assigned degree zero. Since the quotient is étale in codimension one and the box hyperplane is canonical, projection formula gives

`q*d = K_P.D = 8*(n1+n2)`.

Thus

`n1+n2 = q'*d/4`.

For the exact target `d=186`, integrality already forces `q'` to be even, so `q' in {2,4}`.

For every nonconstant projection `D -> X(8)`, Riemann–Hurwitz gives

`2*g(D)-2 >= 8*n_i`.

At least one projection is nonconstant, and

`max(n1,n2) >= (n1+n2)/2`.

Therefore

`q'*O >= 8*max(n1,n2) >= 4*(n1+n2) = q'*d`,

so the multibranch carrier must satisfy the exact necessary condition

`O >= d`.

For the fixed V6 target:

`O >= 186`.

This is a branch-ramification burden, not an exclusion by itself.

## Consequences for the exact V6 exceptional mass

Since every odd-contact branch has positive multiplicity,

`B >= O >= 186`.

Among the `O` odd-contact branches, a branch not counted by `S1` has multiplicity at least 3. Hence

`e >= S1 + 3*(O-S1) = 3*O - 2*S1`,

so

`S1 >= ceil((3*O-e)/2)`.

With `O>=186` and `e=266` this forces

`S1 >= 146`.

Thus any surviving genus-one carrier in this exact class must have at least 186 odd-contact normalization branches above the box nodes, at least 146 of them with exceptional contact multiplicity exactly one.

## Cross-check with the branchwise FSM tensor order

For one normalized branch with exceptional contact `m`, the previous audited local calculation gives `a1+a2>=8m`. The FSM tensor has local signed order at least

`(8*m-16)*k`.

Summing over all `B` normalized branch points gives a local signed contribution at least

`(8*e-16*B)*k`.

The auxiliary modular form contributes at least `2*k*d` zeros away from the nodes. Therefore

`16*(2g-2)*k >= 2*k*d + (8*e-16*B)*k`.

For `g=1`, `d=186`, `e=266`, this implies

`B >= ceil((d+4e)/8) = 157`.

The Beauville/product-cover condition `B>=O>=186` is strictly stronger for this exact class.

## Exact finite-state partition check

The current Picard evidence determines each total `m_j=C.E_j`, but it does not determine how `m_j` splits among distinct normalized branches above that node.

At the valuation level, a local split is represented by an integer partition

`m_j = m_{j,1}+...+m_{j,r_j}`

with positive parts. The FSM cusp congruences do not rule out a positive integer contact multiplicity at this coarse level: for any `m>=1`, the choice `a1=a2=4m` satisfies the required congruences and realizes the minimal valuation pattern used by the inequalities above.

Using the Arsenal `S32-PW01` exact finite-family compression pattern, one can aggregate the 48 independent local partition state sets by dynamic programming without materializing a Cartesian product of all partitions.

For the locked V6 last-48 vector, the compressed state calculation gives:

- total exceptional mass: `266`;
- nodes with odd total intersection: `26`;
- reachable total odd-contact counts: every even integer from `26` through `266`;
- `O=186` is combinatorially reachable at this coarse valuation level;
- among states with `O>=186`, the exact minimum `S1` is `146`;
- a state with `(B,O,S1)=(186,186,146)` is reachable.

Therefore the presently retained intersection vector does **not** by itself contradict the new `O>=186` condition. This is an exact nonexclusion wall at the branch-partition layer, not evidence that a geometric carrier exists.

## Firewalls

- `O>=186` is a necessary condition only.
- A coarse integer partition of `C.E_j` is not a proof that compatible analytic branches exist simultaneously.
- A locally admissible valuation pattern is not a global integral curve.
- The branch-partition DP does not prove effectivity, irreducibility, genus one, or global modular compatibility.
- The audited bijective-normalization exclusion remains closed.
- The non-bijective/multibranch carrier remains open unless a further source-locked geometric constraint rules out every admissible branch profile.
- No FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit follows from this note.

## Next exact datum

The next useful input must constrain the **geometry of the branch splitting**, not merely the total exceptional intersections. Examples include a source-locked restriction on marked inertia/branch directions in the Beauville/product cover, a global compatibility condition on the two `X(8)` projection maps, or an independent low-genus carrier obstruction that consumes the exact V6 branch profile.
