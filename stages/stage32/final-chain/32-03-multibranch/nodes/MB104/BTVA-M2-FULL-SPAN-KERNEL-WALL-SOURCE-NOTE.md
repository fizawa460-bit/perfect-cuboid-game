# Stage32 MB104 — full-span `m=2` simultaneous-extension kernel wall

Status: **RETAINED EXACT METHOD WALL / NO POPULATION-WIDE FINITE DEGREE WINDOW**.

## Statement

Let `T` be any subset of the 48 singular points of the perfect-cuboid surface over `Q(i)`.  Let

- `rho(T)` be the projective coordinate rank of the node vectors in `Q(i)^7`;
- `V2 = H^0(X_pc^circ,S^2 Omega^1)`, the 13-dimensional reflexive `m=2` space retained in the parent adapter;
- `Ext2(T)` be the subspace of `V2` whose pullbacks extend regularly across every exceptional curve lying over a node of `T`.

The retained finite computation proves

`rho(T)=7  ==>  dim Ext2(T) <= 1`.

Equivalently, any node support spanning `P^6` imposes at least 12 independent regular-extension conditions on the full 13-dimensional `m=2` reflexive space.

This is a method wall, not a curve-exclusion theorem.

## Parent exact data

The exact node coordinates and the exact `3 x 13` local `m=2` extension maps are retained by:

- `BTVA-FULL-M2-NODE-EXTENSION-MAP-SOURCE-NOTE.md`, blob `17d23bacd9a48fc48b92f201b2a14fe038db265e`;
- `BTVA-FULL-M2-NODE-EXTENSION-MAP.json`, blob `690631360de67b0096b0a9530c12fee85669d402`.

Those files source-lock the BTVA Table-1 generators, the local `A_1` extension calculation, the ancillary Magma representatives, and the MB103 exact 48-node model.

For each node `s`, write `L_s: V2 -> Q(i)^3` for its local pole/extension obstruction map.  A section extends at `s` iff it lies in `ker L_s`.

For `T`, let `R(T)` be the row span of all `L_s`, `s in T`.  Then

`dim Ext2(T) = 13 - rank R(T)`.

## Exhaustive low-rank rowspace search

The verifier asks whether a support of coordinate rank 7 can have `rank R(T) <= 11`.

For a fixed split prime, it exhaustively constructs **every rowspace of rank at most 11 reachable by adjoining one of the 48 three-row node obstruction maps**.  For every reachable rowspace `R`, it forms the maximal compatible node set

`C(R) = { s : rows(L_s) subset R }`.

Any node support `T` with obstruction rowspace `R(T)=R` is contained in `C(R)`.  Therefore a counterexample with `rank R(T)<=11` and coordinate rank 7 would force some reachable `R` whose compatible node set has coordinate rank 7.

The search finds no such state.

At each of the two primes below, the reachable-state count is exactly

`611,594`.

The rank histogram is

- rank 0: `1`;
- rank 3: `48`;
- rank 4: `72`;
- rank 5: `204`;
- rank 6: `1,152`;
- rank 7: `2,616`;
- rank 8: `8,934`;
- rank 9: `27,836`;
- rank 10: `118,579`;
- rank 11: `452,152`.

For extension ranks `0,3,4,5,6,7,8,9,10,11`, the maximum coordinate ranks of the corresponding compatible-node sets are respectively

`0,1,2,3,3,4,4,5,6,6`.

So over each finite field every reachable extension rowspace of rank at most 11 is compatible only with a node set of coordinate rank at most 6.

## Why two primes recover characteristic zero

The computation is run at both

- `p=1097`, with `i -> 341`;
- `q=1009`, with `i -> 469`.

The reduced data are retained in

- `BTVA-M2-FULL-SPAN-MOD1097-DATA.hpp`, blob `00c36f67976fb8013314d5a4056be676235f4fa6`;
- `BTVA-M2-FULL-SPAN-MOD1009-DATA.hpp`, blob `63e1df9d7e649152b81fddb902a715d7a782c4c2`.

Suppose a characteristic-zero node support `T` had coordinate rank 7 and obstruction rank at most 11.  Reduction cannot increase obstruction rank, so at each prime its reduced obstruction rowspace occurs in the exhaustive rank-<=11 search.  Hence the reduced coordinate rank of `T` is at most 6 at both primes.

But coordinate rank 7 over `Q(i)` gives a nonzero `7 x 7` Gaussian-integer node minor `Delta`.  Every node coordinate is `0` or a Gaussian unit, so Hadamard gives

`Norm(Delta)=|Delta|^2 <= 7^7 = 823,543`.

If the coordinate rank drops modulo the chosen prime above `1097`, then the corresponding Gaussian prime divides `Delta`, hence `1097 | Norm(Delta)`.  The same argument at `1009` gives `1009 | Norm(Delta)`.  Thus

`1097*1009 = 1,106,873 | Norm(Delta)`,

which is impossible for a nonzero norm bounded by `823,543`.

Therefore coordinate rank 7 in characteristic zero forces obstruction rank at least 12, proving `dim Ext2(T)<=1`.

## Relation to the BTVA genus-0 span theorem

The retained BTVA projective-span input says that a genus-0 curve on the perfect-cuboid surface other than the known plane conics, in particular any such curve with `d>2`, must pass through at least seven singularities spanning `P^6`.

Combining that theorem with the wall above gives:

**For every genus-0 nonconic carrier, the space of `m=2` reflexive differentials that extend across all surface nodes met by the curve has dimension at most one.**

Hence the BTVA-style strategy requiring **two independent simultaneously extending `m=2` differentials** and then taking their resultant cannot close the high-degree genus-0 receiver, even after using the full 13-dimensional Table-1 space rather than only the descended `H^0(O(1))*eta` package.

This does not exclude a genus-0 curve.  A one-dimensional surviving kernel may still define a foliation/integral-curve condition, and higher symmetric degree `m>=3` may behave differently.

The genus-1 branch is not closed by this statement because the retained projective-span condition there only forces coordinate rank at least 6 for `d>16`.

## External enumeration cross-check

The published BTVA ancillary transcript `perfectcuboid.out` at mirror commit `c5a8240aed71ed30c63528a2e8f1411f9cc2e04f`, blob `0e0541c57b6c6a1ad670dc89489b394b66f4e9d1`, independently records the node-span counts

`S1=48, S2=1128, S3=15032, S4=118114, S5=463732, S6=593735`

and `2442` symmetry orbit representatives for node-spanned hyperplanes.  These figures are a cross-check only; the retained kernel-wall proof uses the stronger exhaustive extension-rowspace search above.

## Next leaf

`MB104_M2_ONE_SECTION_FOLIATION_OR_HIGHER_M_OBSTRUCTION`.

Priority inputs:

1. classify the one-dimensional surviving `m=2` kernel lines and their integral/resultant loci;
2. determine whether every genus-0 nonconic support actually has zero, rather than one, simultaneous `m=2` sections;
3. construct actual `m>=3` symmetric-differential spaces and node-extension maps;
4. keep the independent global Picard/member and effective `N<=13` routes available.

## Firewalls

- `dim Ext2(T)<=1` is not a finite degree bound.
- One surviving differential is not interpreted as a curve exclusion.
- No analogous rank-7 conclusion is asserted for genus 1.
- Finite-field rank lower bounds are lifted to characteristic zero only through the explicit two-prime norm argument above.
- No finite Picard enumeration release.
- No `R29-LG2-MB` discharge, receiver/effectivity/theorem/endpoint credit, or Perfect-Cuboid conclusion.
- Merge remains unauthorized.
