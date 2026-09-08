# Stage32EX6 — cross-node landing/deck-stabilizer wall

Status: `SCRATCH_EXACT_BOUNDED_CROSS_NODE_DECK_SYMMETRY_WALL_NO_ENDPOINT_CREDIT`.

This is the eighth isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` used throughout EX6.

The previous scratch leaf identified the FSM-minimal exceptional landing parameter `lambda` with the local value, up to the fixed deck/trivialization unit, of the ratio of the two X(8) projection differentials. The bounded question here is whether the retained ambient/deck symmetry forces landing values at different node branches of the **same carrier** to lie in finite/sign orbits and hence yields a counting or collision obstruction.

## Retained local symmetry

The retained intermediate quotient source lock uses the resolved node chart

`x=p^2`, `y=pq`, `z=q^2`, `u=y/x`,

with exceptional curve `x=0`. The nontrivial cusp inertia acts

`(x,u) -> (x,-u)`.

Thus at a minimal landing point `u=lambda != 0`, the local inertia sends

`lambda -> -lambda`.

This is an exact ambient local action. It does not by itself say that the two landing points belong to the same curve member.

## The residual H action does not stabilize the carrier

The same retained source lock identifies the residual factor-pair deck group

`H ~= (Z/2)^3`

and the quotient

`q:S -> Y=S/H`.

It further records that the full factor-pair map is birational on the hypothetical carrier `C`, hence

`q|_C : C -> C_Y=q(C)`

is birational.

If a nontrivial element `h in H` stabilized `C` as a curve, then the generic H-orbit of a point of `C` would contain at least two points of `C` mapping to the same point of `C_Y`. Consequently `q|_C` would have generic degree at least two, contradicting the retained birationality.

Therefore

`Stab_H(C) = {1}`.

In particular the node-inertia element that sends `u=lambda` to `u=-lambda` does not globally stabilize the hypothetical carrier. For a minimal landing `lambda != 0`, the point itself is also not fixed by that inertia. Hence the local sign action relates the landing germ on `C` to the corresponding landing germ on the distinct deck translate `hC`; it does not force a second `-lambda` landing branch on the same `C`.

## Independent V4 check on the product-cover/correspondence side

The retained hostile-audited Rosati repair gives a finite etale V4 deck cover and an exact curve `D` with

`D^2 = 3874`,

`D.uD = 3892`,

`D.vD = 4020`,

`D.uvD = 4020`.

If any nontrivial V4 element stabilized `D`, then the corresponding translate would equal `D` and its intersection with `D` would equal `D^2=3874`. None of the three retained deck pairings equals `3874`.

Therefore the nontrivial V4 translates are all distinct from `D` as well.

This independently confirms the same semantic firewall upstairs: deck symmetry transports the member to distinct translates rather than producing internal landing identifications on the same member.

## Why cross-node sign/orbit counting does not close O266

AR supplies at least 186 FSM-minimal branches, with nonzero finite landing parameters. The local ambient action can transport a landing value through a finite deck orbit, including the sign change `lambda -> -lambda`, but because the deck action does not stabilize `C`, those orbit points live on different deck-translated curve members unless an additional member-stabilizing symmetry is supplied.

Therefore one may not conclude any of the following from the retained deck action alone:

- that landing values on `C` occur in `+/-` pairs;
- that two different nodes of `C` have equal or sign-related `lambda`;
- that the 186 minimal branches occupy only finitely many internal landing classes;
- that a pigeonhole collision occurs on `C`;
- or that the degree-192 differential-ratio bundle must vanish at any of those points.

The large translate intersections/conductor contributions retained elsewhere are global intersections among distinct translates and have already been accounted for structurally; they are not automatically internal branch collisions of `C`.

## What would be needed next

A genuine cross-node landing constraint now needs an input stronger than ambient deck symmetry, for example:

1. a nontrivial automorphism proved to stabilize the actual fixed-V6 member;
2. a source-locked invariant/anti-invariant global section whose restriction to `C` identifies landing values across node orbits;
3. an explicit member equation forcing a finite algebraic set of allowed `lambda` values;
4. a higher-jet relation invariant under the deck action that turns translate intersections into internal tangency/collision conditions;
5. or a member-level monodromy/marked-node theorem coupling landing coordinates on distinct exceptional curves.

No such stabilizing/member-level adapter is claimed here.

## Decision

Canonical scratch decisions:

- `LOCAL_NODE_INERTIA_ACTION_ON_LANDING = LAMBDA_TO_MINUS_LAMBDA`;
- `RESIDUAL_H_CARRIER_STABILIZER_IS_TRIVIAL = true`;
- `NONTRIVIAL_V4_PRODUCT_COVER_TRANSLATES_ARE_DISTINCT = true`;
- `DECK_SIGN_ACTION_FORCES_INTERNAL_PLUS_MINUS_PAIR_ON_C = false`;
- `DECK_ACTION_FORCES_CROSS_NODE_LANDING_COLLISION = false`;
- `FINITE_INTERNAL_LANDING_ORBIT_OBTAINED = false`;
- `HIGHER_JET_OR_MEMBER_STABILIZING_SYMMETRY = UNTESTED`;
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- Ambient/deck symmetry is not promoted to symmetry of a hypothetical member.
- The local `lambda -> -lambda` action is not treated as an internal pairing on `C`.
- Distinct deck translates may intersect; distinctness does not claim disjointness.
- Existing translate-intersection/conductor totals are not recharged as landing-collision counts.
- No total RH, delta, conductor, cusp-grid, Picard, Abel, Jacobian, or first-jet datum is double-charged as a new `eta/rho` cap.
- No Stage32 MAIN, O266 endpoint, lower-O, or Perfect Cuboid credit follows.
- This scratch leaf remains non-authoritative until a later retained consolidation and hostile-audit workflow.
