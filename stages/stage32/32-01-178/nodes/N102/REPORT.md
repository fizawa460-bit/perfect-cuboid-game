# N102 — Eight hard-tail row structural reduction

## Result

`PASS_NEW_GATE_FROM_STRONGER_VIEW`.

The generation38 hard tail is an exact eight-row family, not eight unrelated pathologies. The rows are
`g0-d008, g0-d010, ..., g0-d022`, equivalently `g=0` and `d=8+2k` for `k=0,...,7`.
The historical 256M diagnostic retained 52 survivors, all 52 stayed in the same exact `e` stratum, and those survivors occupied exactly these 8 rows.

The old obstruction was the cost of enumerating giant individual prefix-DFS strata. That obstruction is now dominated *as a prefix-family enumeration mechanism* by the retained exact indexed-terminal reparameterization. The historical generation38 evidence is not revoked; what is superseded is the traversal mechanism.

## Exact row classification

| row | d | observed current e range | e_max=floor(19d/5) | later e strata |
|---|---:|---:|---:|---:|
| g0-d008 | 8 | 18..22 | 30 | 8 |
| g0-d010 | 10 | 18..23 | 38 | 15 |
| g0-d012 | 12 | 17..22 | 45 | 23 |
| g0-d014 | 14 | 16..22 | 53 | 31 |
| g0-d016 | 16 | 16..23 | 60 | 37 |
| g0-d018 | 18 | 16..21 | 68 | 47 |
| g0-d020 | 20 | 16..21 | 76 | 55 |
| g0-d022 | 22 | 15..21 | 83 | 62 |

For each row the residual-volume checkpoint records
`later_e = e_max - max(current_e_range)`. Summing the eight exact row-local tails gives

`8+15+23+31+37+47+55+62 = 278`,

exactly the checkpoint's `later_e_strata_owned_by_row_tail_sources=278`.

The diagnostic's raw-peak and local-linear remaining-node estimates are not used as theorem input.

## Exact solver-space replacement

The current retained terminal-family implementation uses eleven integer coordinates `x0,...,x10` and the exact predicate

- all `xi >= 0`;
- `sum(xi for i != 4) <= e`;
- `0 <= x4 <= 19*d-5*e`;
- `x0 <= x1`;
- if `x0 == x1`, then `(x5,x6) <=lex (x8,x9)`;
- `x1+x8+x9+x10 == 0 (mod 2)`.

Write `C(e)` for `exceptional_terminal_count(e)`. The exact terminal count of a `(d,e)` stratum is

`T(d,e) = (19*d - 5*e + 1) * C(e)`.

The retained indexed checkpoint records exact symbolic counting, random-access unrank, inverse rank, a small-family full-set bijection check, and `terminal_set_semantics_preserved=true`. Consequently the eight generation38 row tails do not need to be traversed by resuming their historical prefix-DFS cursors. Their prefix-terminal population is represented canonically by the same exact `(d,e,x0,...,x10)` indexed family.

This is a representation/compression theorem, not a numerical Picard closure theorem.

## Per-row replayable diagnosis

Every one of the eight rows has the same reduction:

1. identify the stable row by `(g,d)=(0,d)`;
2. use `e_max=floor(19*d/5)`;
3. replace legacy prefix-DFS enumeration of each `(d,e)` stratum by the exact indexed terminal predicate above;
4. address terminal points by exact rank/unrank rather than materializing the DFS stream;
5. apply future numerical Picard leaf/lift conditions directly in these indexed coordinates.

`verify_n102.py` checks the eight stable row identities, all row-local `e_max` and `later_e` identities, the exact total 278, the 52/8/same-e hard-tail facts, and the retained indexed-semantic-preservation flags.

## Remaining blocker and credit firewall

The current indexed checkpoint explicitly states `numerical_picard_leaf_checks_complete=false`, and the production state names the next leaf
`DIRECT_NUMERICAL_PICARD_LEAF_COMPRESSION_AFTER_PREFIX_REPARAMETERIZATION`.

Therefore N102 closes the *G1 hard-tail prefix-enumeration obstruction* by exact dominance, but discharges none of the eight numerical rows and grants no FULL178, theorem, receiver, existence, or nonexistence credit. Blind 256M/512M prefix-DFS escalation is not a legal next action for this node.
