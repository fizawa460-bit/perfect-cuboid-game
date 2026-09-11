# Stage32 MB104 — BTVA low-support finiteness

Status: **RETAINED GLOBAL FINITENESS PARTITION / NON-EFFECTIVE DEGREE BOUND / NONCLOSING**.

## Primary source

Nils Bruin, Jordan Thomas, Anthony Várilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasihyperbolicity*, Algebra & Number Theory 16 (2022), 1377–1405, DOI `10.2140/ant.2022.16.1377`, arXiv `1912.08908`.

Section 7, perfect-cuboid example, immediately after introducing the 48 `A1` singularities, applies Proposition 3.1 with

`r = 48 - 13 = 35`

and records

`h^0(Y-(E_1 union ... union E_r), S^m Omega^1_Y) = (1/108)m^3 + O(m^2)`.

The paper then explicitly concludes that there are only finitely many curves of genus `0` or `1` on the perfect-cuboid surface that pass through at most `13` singularities.

Anthony Várilly-Alvarado's Notices article *The Geometric Disposition of Diophantine Equations* (Notices AMS 68 (2021), DOI `10.1090/noti2335`, Section 4.2) independently states the same consequence and attributes it to the García-Fritz–Urzúa / Bruin–Thomas–Várilly-Alvarado symmetric-differential program.

## Adapter to R29-LG2-MB

For a nonexceptional integral carrier let

`N = # { surface nodes met by the image curve }`.

The published conclusion applies to the singular canonical image, so it does not require bijective normalization at the nodes. Therefore it applies to the multibranch receiver as well.

The subpopulation

`g in {0,1}, N <= 13`

is a finite set of integral curves.

Consequently there exists an absolute integer `D_13` such that every carrier in this subpopulation has `d <= D_13`. Equivalently, any sequence of pairwise distinct genus-0/1 carriers with unbounded canonical degree must eventually satisfy `N >= 14`.

## Effectivity firewall

The cited argument is asymptotic. In the same paragraph the authors note that the Euler-characteristic lower bound only becomes positive at a large symmetric power and that this is outside their explicit-computation range. The conclusion retained here is **finiteness**, not an explicit list and not a computed numerical value of `D_13`.

Therefore this result does **not** release finite Picard enumeration for `N<=13`: the current computational backend still lacks a certified numerical degree cutoff for that subpopulation.

It also does not control the `N>=14` subpopulation, and the retained scaling profile meets all 48 nodes.

## Firewalls

- `N` counts distinct surface nodes, not ordinary self-nodes of the strict transform.
- Finiteness is not identified with an explicit/effective degree bound.
- No unibranch `176/192` cap is imported.
- No `R29-LG2-MB` discharge, receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit is claimed.
- Merge remains unauthorized.
