# Stage32 MB104 — full `m=2` hyperplane/outside classification

Status: **RETAINED EXACT FINITE CLASSIFICATION / NONFINAL / NO FINITE DEGREE WINDOW**.

This note continues `BTVA-FULL-M2-NODE-EXTENSION-MAP.json`.  It does not claim that an `m=2` differential exists for every low-genus carrier.  It classifies exactly how the complete 13-dimensional reflexive `m=2` space behaves on node-spanned hyperplanes and after adjoining one node outside the hyperplane.

## Source locks

Primary source: Bruin--Thomas--Várilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*, Algebra & Number Theory 16 (2022), DOI `10.2140/ant.2022.16.1377`, arXiv `1912.08908v3`.

Ancillary mirror, commit `c5a8240aed71ed30c63528a2e8f1411f9cc2e04f`:

- `papers/1912.08908/anc/perfectcuboid_script.m`, blob `7b84650178bd077a9829b51f669c78118b6ce4b9`;
- `papers/1912.08908/anc/perfectcuboid.out`, blob `0e0541c57b6c6a1ad670dc89489b394b66f4e9d1`.

The published ancillary computation gives, for the 48 singular points over `Q(i)`:

- `#S6 = 593735` distinct vector-rank-6 node spans, i.e. node-spanned projective hyperplanes;
- `2442` hyperplane orbits under the ancillary symmetry group used there.

The 48-node coordinates and the 1536-element `Aut(S)` node action are inherited from MB103.  The local `3 x 13` extension maps are inherited from `BTVA-FULL-M2-NODE-EXTENSION-MAP.json`.

## Replay field and exactness

The exhaustive finite replay is performed modulo `p=1097`, with `i=341` (`341^2=-1 mod 1097`).  Reduction modulo a good prime can only lower matrix rank.  Exact ranks over `Q(i)` are recovered as follows.

1. Every node-spanned hyperplane `H=(ell=0)` has the nonzero section `ell*eta` in the simultaneous extension kernel, so its exact extension rank is at most `12`.
2. Mod-1097 rank `12` therefore proves exact rank `12`.
3. The mod-1097 rank-11 hyperplanes form seven `Aut(S)` orbits; one representative of each orbit was replayed directly over `Q(i)` and has exact rank `11`.
4. The three mod-1097 rank-10 hyperplanes are the three `y_j=0` coordinate hyperplanes already replayed exactly by the full-map adapter; their exact rank is `10`.
5. For an outside-node pair, mod-1097 rank `13` proves exact rank `13`.  The rank-12 survivors form 35 `Aut(S)` pair-orbits; one representative of each orbit was replayed directly over `Q(i)` and has exact rank `12`.

Thus the finite counts below are not promoted from a possibly bad modular rank drop.

## All node-spanned hyperplanes

The independent replay reconstructs exactly the ancillary count `593735`.  Their node-incidence sizes are:

| nodes on `H` | number of hyperplanes |
| ---: | ---: |
| 6 | 372608 |
| 7 | 114624 |
| 8 | 61440 |
| 9 | 32256 |
| 10 | 8736 |
| 12 | 1648 |
| 13 | 768 |
| 14 | 1248 |
| 15 | 256 |
| 16 | 27 |
| 19 | 48 |
| 20 | 48 |
| 24 | 28 |

Their exact simultaneous `m=2` extension ranks are:

- rank `12`: `590468` hyperplanes;
- rank `11`: `3264` hyperplanes;
- rank `10`: `3` hyperplanes.

More precisely:

- all `372608` six-node hyperplanes have rank 12;
- among seven-node hyperplanes, `3072` have rank 11 and `111552` have rank 12;
- among twelve-node hyperplanes, `192` have rank 11 and `1456` have rank 12;
- the only rank-10 hyperplanes are three sixteen-node hyperplanes (`y1=0`, `y2=0`, `y3=0`);
- every remaining incidence class has rank 12.

The `3264` rank-11 hyperplanes split into exactly seven `Aut(S)` node-orbits.  In the deterministic MB103 node ordering, representatives are:

| orbit | representative mask | orbit size | nodes on H | outside rank-12 survivors per H |
| ---: | ---: | ---: | ---: | ---: |
| 0 | `318849034` | 768 | 7 | 9 |
| 1 | `318849184` | 384 | 7 | 9 |
| 2 | `319033354` | 768 | 7 | 9 |
| 3 | `319033504` | 384 | 7 | 9 |
| 4 | `469843978` | 384 | 7 | 9 |
| 5 | `470028298` | 384 | 7 | 9 |
| 6 | `1593905322` | 192 | 12 | 4 |

The orbit sizes sum to `3264`.

## Adjoin one node outside the hyperplane

Across all node-spanned hyperplanes there are exactly

`24538032`

ordered pairs `(H,p)` with `p` a surface node not lying on `H`.

The full `m=2` extension rank distribution is:

- rank `13`: `24509616` pairs;
- rank `12`: `28416` pairs.

There are no rank-10 or rank-11 outside pairs.

The previous tentative statement “every outside node raises the rank to 13” is therefore **false** and is explicitly retired.

All `28416` rank-12 survivors come from the rank-11 hyperplanes above:

- each of the `3072` seven-node rank-11 hyperplanes has exactly `9` outside survivor nodes;
- each of the `192` twelve-node rank-11 hyperplanes has exactly `4` outside survivor nodes.

The survivor pairs split into exactly `35` `Aut(S)` orbits.  Their orbit-size distribution is

- `12` orbits of size `384`;
- `15` orbits of size `768`;
- `8` orbits of size `1536`.

The weighted sum is `28416`.

## Twenty-four special `m=2` web-supports

For every rank-12 survivor pair the simultaneous kernel is one-dimensional.  The unique kernel section extends at exactly `16` of the 48 nodes.

Even more strongly, the `28416` survivor pairs produce only **24 distinct 16-node extension supports**, and these 24 masks form one orbit under the exact 1536-element MB103 node action.

A representative support mask is

`4278538410`,

corresponding to zero-based node indices

`[1,3,5,7,12,14,16,18,24,25,26,27,28,29,30,31]`.

For the representative survivor `(H,p)=(318849034,5)`, the exact `Q(i)` kernel section in the retained basis

`(omega1,...,omega6,x1*eta,x2*eta,x3*eta,y1*eta,y2*eta,y3*eta,z*eta)`

is

`omega1 - i*omega2 - omega3 + i*omega4 + i*omega5 + omega6`.

Direct exact substitution shows that this section extends at precisely the 16 nodes above.  The remaining 23 support masks are its node-support orbit.  This is a finite **web-support residual**, not a proof that every rank-7 carrier is governed by one of these webs.

## Consequence for full-span node supports

Let `T` be any set of surface nodes of projective coordinate rank `7`.  Choose seven independent points in `T`; the first six span a unique node-spanned hyperplane `H`, and the seventh is outside `H`.  The exhaustive pair classification gives extension rank at least `12` on `H union {p}`, hence also on `T`.

Therefore

`dim H0_m2(extending over every node of T) <= 1`.

In particular, for the BTVA rational nonconic regime (`d>2`, node rank `7`), the standard two-section `m=2` resultant mechanism cannot be available on the entire node support.  This is a **method-capacity wall**, not an exclusion of the curve.

If a full-span support has a nonzero simultaneous `m=2` section and the chosen basis pair lands in the rank-12 residual, that section is constrained to the 24-support residual described above.  No claim is made here that every possible full-span support with a nonzero section has already been globally classified without checking consistency across all bases; that stronger statement remains a follow-up obligation.

## Next obligation

`MB104_M2_SPECIAL_24_WEB_INTEGRAL_CURVE_CLASSIFICATION_OR_HIGHER_M`.

Priority:

1. classify the integral curves of the representative special quadratic web and transport through the 24-support orbit; or
2. prove that any full-span support retaining an `m=2` section is contained in one of the 24 special supports; or
3. move to `m>=3` / actual global-member geometry for the rank-13 no-section population.

## Firewalls

- Hyperplane/outside extension rank is not a degree bound.
- Rank 13 means “no retained `m=2` section extends across that node support”; it is not a contradiction to existence of a curve.
- One surviving section does not by itself give a finite resultant locus; its integral curves must be classified.
- Modular rank drops were not promoted without exact `Q(i)` representative checks.
- No unibranch `176/192` cap is imported.
- No finite Picard enumeration release.
- No `R29-LG2-MB` discharge or receiver/effectivity/theorem/endpoint credit.
- Merge remains unauthorized.
