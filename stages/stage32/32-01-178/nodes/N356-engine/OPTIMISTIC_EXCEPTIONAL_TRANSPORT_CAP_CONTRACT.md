# Stage32 32-01-178 N356 — optimistic exceptional transportation capacity

Status: `AUDIT_REQUIRED`. This node starts from the externally hostile-audited N355 full known-prefix authority and derives one further necessary condition. It is not a production-leaf certificate and does not complete FULL178.

## Audited input

N355 full known-prefix hostile audit review `5165895301` passed exact candidate head
`3f3aadd2e5ada2a0a02a69490d6d659c02762682`.

The authoritative residual is therefore

- `17128` strata;
- `66462870551188628549910` compressed terminals.

The ten stored exceptional coordinates lie in three nonempty known special-fibre cells:

- `a = E101+E102+E103`;
- `b = E97+E98+E99`;
- `c = E93+E94+E95+E96`.

N355 already enforces `max(a,b,c) <= floor(d/2)`.

## The 6x6 transportation relaxation

For each factor direction the 48 exceptional labels `93..140` are partitioned into six eight-element special-fibre blocks. Intersecting the two partitions gives three disjoint `2 x 2` components. Each nonempty row/column cell contains four exceptional labels.

The current ten-coordinate prefix has the following exact occupancy pattern.

- The `a` cell contains labels `101..104`: three are known and label `104` is still omitted.
- The `b` cell contains labels `97..100`: three are known and label `100` is still omitted.
- The `c` cell contains exactly labels `93..96`: all four are already known, so this is the unique occupied cell into which no omitted exceptional mass can be placed.
- Every other nonempty cell contains omitted labels.

For a hypothetical extension, let `n1,n2` be the two factor degrees. N352 gives

`n1+n2=d`.

Every full exceptional block mass is at most the corresponding factor degree. To make the extension problem *easier*, N356 forgets all omitted-coordinate arithmetic except nonnegative integrality and allows the missing exceptional mass to be distributed arbitrarily among every cell containing at least one omitted label. Any genuine extension gives a feasible point of this relaxed transportation problem. Therefore infeasibility of the relaxation is a valid necessary obstruction.

## Exact optimistic capacity

Put `h=floor(d/2)` and `m=min(n1,n2)`. The first two `2 x 2` components have all four transportation edges available after the fixed prefix values, so together they carry at most `4m` total exceptional mass.

In the third component the fixed masses are `b` and `c` in opposite cells, but the `c` cell has no omitted label. After subtracting the fixed masses, the allowed-edge max-flow is

`min(2 n1-b-c, 2 n2-b-c, d-2b)`.

Hence the total exceptional-mass capacity of the relaxed completion is

`C(n1,n2)=min(6m, 4m+d+c-b)`.

Both terms are monotone in `m`, so subject to `n1+n2=d` the optimistic maximum occurs at `m=h`. Thus every genuine extension must satisfy

`e <= Cmax := min(6h, 4h+d+c-b)`.

Equivalently, in addition to the already-audited scalar side `e<=6h`, the new prefix-sensitive condition is

`b-c <= 4h+d-e`.

For the actual FULL178 row set the verifier also checks the degree parity rather than assuming it. If all retained degrees are even, this specializes to

`b-c <= 3d-e`.

## Why this is zero-loss

The transportation model is deliberately optimistic: omitted exceptional coordinates are allowed to take any nonnegative integral values compatible only with total mass and block capacities. It discards, rather than adds, genuine Picard/integrality constraints. Therefore a prefix rejected by the transportation relaxation cannot have a genuine completion.

The exact census must additionally replay the already-audited N220 support condition and the already-audited N355 full known-prefix predicate before counting any incremental rejection.

## Firewalls

Before external hostile audit, N356 has zero MAIN pruning credit. No N350 producer registration, production COMPLETE, N104 release, FULL178 completion, theorem/receiver/endpoint/Stage32 closure, Perfect Cuboid existence/nonexistence claim, heavy-compute authorization, or merge authorization is created by this contract.
