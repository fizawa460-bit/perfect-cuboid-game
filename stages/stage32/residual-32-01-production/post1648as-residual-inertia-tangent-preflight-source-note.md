# Stage32 post1648AS — residual cusp inertia and exceptional tangent-action preflight

Scratch-only source-lock/diagnostic leaf. This leaf combines AQ's source-identified residual deck group with AR's lower bound of 186 FSM-minimal node branches. It identifies which residual involutions are the inertia elements of the 12 target cusp points and records their exact action on the exceptional tangent coordinate. The action does **not** force opposite landing collisions, so V6 remains unexcluded and shared MAIN authority is unchanged.

## Parent locks

- AQ finalized scratch head: `1dfb1fb463b3ace0b36354677b6fcbd20a5513ae`.
- AQ canonical SHA256: `1831162e6f270b461d63fbdfda57b61711aacd49b85fe40e37fb5d5b3634088e`.
- AR finalized scratch head: `87bfff81cf7723848650fbc9a50d011328bf8a21`.
- AR canonical SHA256: `dba5756e4b10c8bd6e412f1027b8edf693fb74f9ea90f9b591cc99437746a8dd`.

The permanent retained Picard payload modules remain runner-side imports only.

## Source geometry

The geometric source remains Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), DOI `10.1307/mmj/1480734014`, as source-locked by AM/AQ.

AQ identifies the residual factor-pair deck group

`H ~= (G x G)/G_diag ~= (Z/2)^3`

inside the retained full automorphism action as the pointwise stabilizer of the 12 Satake-boundary elliptics.

Near a box cusp, before the diagonal quotient, use local product parameters `(p,q)`. The diagonal central involution gives the `A1` quotient

`x=p^2, y=pq, z=q^2`, `xz=y^2`.

For a target cusp of the factor-pair quotient, the nontrivial inertia element can be represented modulo the diagonal subgroup by changing sign in one factor, e.g.

`(p,q) -> (-p,q)`.

Therefore on the `A1` invariants it acts by

`(x,y,z) -> (x,-y,z)`.

On the minimal resolution, in the `x`-chart `u=y/x`, this is

`u -> -u`.

Its two fixed points on the exceptional `P1` are `u=0` and `u=infinity`; these are precisely the two boundary-intersection directions. An FSM-minimal branch has exponent type `(A,B)=(1,1)` and lands at a finite nonzero exceptional ratio `u=lambda in C*`, hence it is **not** fixed by the cusp inertia involution and is sent to the opposite landing `-lambda`.

This local action is a source-derived consequence of the already locked quotient model. It is not inferred from abstract group type alone.

## Exact retained residual-inertia classification

The retained residual group has order 8 and seven nonidentity involutions. Exactly three of them fix exceptional curve labels. They are the three cusp-inertia classes for the 12 residual target cusp orbits:

- fingerprint `114d7929431cc3ac`: `C.gC=1360`, fixes 16 exceptional labels, boundary inertia labels `[33,34,35,36]`, four target cusp orbits with V6 masses `[35,24,18,19]`, total 96;
- fingerprint `4a99da505a8c0bdc`: `C.gC=1286`, fixes 16 exceptional labels, boundary inertia labels `[37,38,39,40]`, masses `[28,21,25,34]`, total 108;
- fingerprint `b6abf273dd0daaf4`: `C.gC=1498`, fixes 16 exceptional labels, boundary inertia labels `[41,42,43,44]`, masses `[20,5,5,32]`, total 62.

The 48 exceptional labels split into 12 residual-`H` orbits of size four, and the three inertia involutions account for four such target cusp orbits each.

The remaining four nonidentity elements fix no exceptional labels. Their `C.gC` values are `1112,1266,1284,1480`. Thus the node-inertia/non-node split also partitions the seven AQ pairwise intersections into

- node-inertia sum `1360+1286+1498 = 4144`;
- non-node-element sum `1112+1266+1284+1480 = 5142`;

with total `9286`, agreeing with AQ.

## Interaction with AR's 186 minimal branches

AR proves that any hypothetical integral geometric-genus-1 V6 carrier has at least 186 node branches of FSM-minimal type `(1,1)`. Each such branch lands at some `lambda in C*` on its exceptional curve.

Pigeonhole alone gives only:

- at least 16 minimal branches above some one of the 12 target cusp orbits;
- at least 4 minimal branches on some one of the 48 exceptional curves.

Neither statement forces a pair of landings `{lambda,-lambda}`. A finite subset of `C*` may avoid all opposite pairs, and the retained class/action data do not contain the actual member-level landing values or first jets.

Therefore the residual tangent action alone does not turn the large class intersections `C.gC` into a local contradiction. To control the exceptional part of `C intersect gC`, one needs actual landing/jet constraints; alternatively one needs a global bound separating exceptional and off-exceptional contributions to `C.gC`.

## Firewalls

- Scratch only; shared `MAIN-STATE.json` and Stage32 authority remain unchanged.
- `Q602_excluded=false`.
- `O210_excluded=false`.
- `O212_plus_advance_allowed=false`.
- `V6_carrier_excluded=false`.
- No claim that opposite landing collisions exist.
- No receiver, route, theorem, endpoint, or perfect-cuboid credit.
