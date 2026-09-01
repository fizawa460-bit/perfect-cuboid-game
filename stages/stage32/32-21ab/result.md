# Stage32-21ab — exact quotient class map

Status: `CLOSED_CHECKPOINTED`

## Result

`PASS_STAGE32_21AB_EXACT_QUOTIENT_CLASS_MAP`

The rank-2 projected Smith affine coordinates are attached exactly to the same Reynolds projection residue convention certified by 32-21aa.

Let `B` be the exact 64x5 Z-basis of `im(N)` used by 32-21aa and let `T` be the unimodular Smith-right transform of the projected slice system. For

`y=(y0,y1,y2,u,v)` and `z=T*y`,

the canonical projection residue is exactly

`r = (B*T*y) mod 64`.

Exact CI run `33308996594`, job `99250520551` certified:

- projection classes: `16384`;
- full Smith-coordinate image equals the 32-21aa projection image;
- the free `(u,v)` directions generate an exact subgroup of order `128`;
- therefore the 16384 projection classes split into exactly `128` free-subgroup cosets;
- canonical certificate SHA256: `07bf0aff16a344ad68fe7179ff797057fca562fd6bafbdaf418155ba0995c8b4`.

This leaf is an exact adapter only. It does not itself prune any candidate and does not run the FULL178 population.

## Firewalls

- terminal-family materialization: false;
- 59-dimensional anti-fixed CVP: false;
- legacy prefix DFS re-arm: false;
- numerical row complete: false;
- theorem / receiver / route credit: false;
- perfect-cuboid existence/nonexistence claims: false.

Next tightly coupled leaf in the same PR: `32-21ac`.
