# Stage32 32-01-178 N355 — special-fibre prefix max cut

Status: `AUDIT_REQUIRED`. This is a terminal-prefix necessary-condition adapter on the externally audited N354 survivor frontier. It does not claim a new global FULL178 census.

## Audited input scope

N354 has external hostile-audit PASS review `5164850548` on exact head `e82a1d2ae6ed3693e5e5e81adfd95b83a6c317b6`. The authoritative post-N354 population is `17128` strata / `38560956534397137634780102` N220-filtered terminals.

The retained Stage32 terminal prefix uses assignment labels

`[95,99,103,102,49,97,94,101,93,98,96]`.

Label `49` is the sole normal prefix variable. The other ten labels are exceptional pairings and are nonnegative.

## Per-special-fibre inequality

For either retained factor fibration, each of its six special fibres has the source-locked form

`F_b = 2 E_b + sum_{j in I_b} E_j`,

where `I_b` is an eight-element exceptional set. In each factor direction the six sets `I_b` partition labels `93..140`.

For a hypothetical retained curve class `D`, write

- `n_i = D.F_i` for the degree in factor direction `i`;
- `q_{i,b}=D.E_b >= 0` for the boundary-elliptic pairing;
- `e_{i,b}=sum_{j in I_{i,b}} D.E_j >= 0` for the full exceptional block mass.

Intersecting the fibre formula gives, for every one of the six fibres,

`n_i = 2 q_{i,b} + e_{i,b}`.

Hence `e_{i,b} <= n_i`.

Let `K` be the ten exceptional labels present in the current terminal prefix and define the known partial block mass

`s_{i,b} = sum_{j in I_{i,b} intersect K} D.E_j`.

All omitted exceptional pairings are nonnegative, so

`s_{i,b} <= e_{i,b} <= n_i`.

Define

`A_i = max_b s_{i,b}`.

The externally audited N352 identity is `n_1+n_2=d`. Therefore every extendable current terminal prefix must satisfy the exact necessary inequality

`A_1 + A_2 <= d`.

Equivalently, all 36 row/column block-pair inequalities `s_{1,b}+s_{2,c}<=d` hold.

## Immediate diagonal consequence

Every exceptional label belongs to exactly one block in each factor partition. Therefore, for each of the ten known exceptional prefix labels `j`, choosing the two blocks containing `j` gives

`2 D.E_j <= A_1+A_2 <= d`.

Thus every extendable current terminal prefix satisfies

`D.E_j <= floor(d/2)`

for all ten known exceptional prefix labels.

This diagonal cap is only a consequence of the stronger `A_1+A_2<=d` cut; it is retained because it is cheap to apply and count.

## Strictness beyond N354

The stratum `(g,d,e)=(0,8,12)` satisfies the audited N354 scalar interval: `e` is even and `2*ceil(e/6)=4 <= 8 <= 8=e+4g-4`.

The current 11-prefix vector

`x=(0,5,0,0,0,0,0,0,0,0,1)`

in assignment order `[95,99,103,102,49,97,94,101,93,98,96]` satisfies the base compressed-terminal predicate and the audited N220 support predicate: its exceptional mass is `6<=12`, its parity is even (`x1+x8+x9+x10=6`), and its known support plus optimistic remaining exceptional support is at least the N220 requirement. But label `99` has pairing `5>d/2=4`, so it violates the N355 diagonal consequence and therefore cannot extend to a retained curve class.

Thus N355 is genuinely stronger than the scalar N354 stratum filter at terminal-prefix level.

## What this does not prove

N355 does not yet provide an exact aggregate count over all `17128` N354 survivor strata. The old/current terminal representation stores only ten of the 48 exceptional pairings; this contract deliberately uses a monotone partial-block relaxation and does not invent the missing 38 values.

A future exact census may count this prefix predicate symbolically or integrate it into a filtered random-access adapter. Until then, the authoritative N354 aggregate remains `17128` strata / `38560956534397137634780102` terminals.

## Firewalls

No N355 MAIN pruning-count credit before external hostile audit. No reduction of the authoritative `17128`/`38560956534397137634780102` aggregate is claimed here. No N350 producer registration, production COMPLETE, N104 release, FULL178 completion, theorem/receiver/endpoint/Stage32 closure, Perfect Cuboid existence/nonexistence claim, heavy-compute authorization, or merge authorization.
