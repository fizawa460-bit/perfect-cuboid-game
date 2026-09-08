# Stage32EX6 scratch — finite rank4 split-attachment union avoidance wall

Status: `SCRATCH_EXACT_BOUNDED_FINITE_RANK4_SPLIT_ATTACHMENT_UNION_AVOIDANCE_NO_ENDPOINT_CREDIT`.

Scratch only. This does not update `MAIN-STATE`, exclude O266, authorize O264 descent, or create Stage32 MAIN / hostile-audit credit.

## Source locks

- PR #1715 retained head inspected for this batch: `5e8e0cd64a1cb74574f8dff9b43d33ecfbf937e7`.
- `post1697-rank4-local-unramified-contact-wall.md`.
- `post1697-rank4-degree113-adapter-wall.md`.
- exact rank4 orbit runner `diagnose_stage32_ex6_rank4_fibration_orbit.py`.
- exact-head #1697 rank4 workflow run `34181358732`, job `101920955194`, SUCCESS.
- AN local A1 endpoint model `post1648an-a1-strict-transform-delta-feasibility-source-note.md`.

The exact-head workflow replay records the non-isotrivial rank4 degree ranges

- next-six type: degree range `82..104` over 12 fibration classes;
- last-four type: degree range `73..113` over 8 fibration classes;

and the retained local wall proves that on a split exceptional component `E`, a reduced split fiber has exactly two attachment points with its two `G3` components and a unit contact away from those points is unramified for that fibration.

## Finite simultaneous split mechanism

Fix one exceptional curve `E ~= P1` and consider any finite collection `F` of retained rank4 fibrations for which `E` occurs as a reduced split-fiber exceptional component.

For each `f in F`, let `A_f subset E` be the two attachment points of the adjacent `G3` components.  By the retained split-fiber local lemma, a unit normalization branch meeting `E` at

`lambda in E \ A_f`

is unramified for `f` at that contact.

Therefore the landing values that are forced to ramify by the split-attachment mechanism for at least one `f in F` lie in the finite set

`A = union_{f in F} A_f`.

The O266 AN local model permits an arbitrary finite collection of pairwise-distinct nonzero landing values on each exceptional curve.  Over the retained infinite landing field, a finite set of such values can be chosen in

`E \ (A union {0,infinity})`.

Hence every local O266 branch on `E` can simultaneously avoid all split-attachment points for all fibrations in the chosen finite rank4 collection.

This applies in particular to the finite last-four orbit, and equally to the union of the retained finite next-six and last-four non-isotrivial rank4 classes, insofar as the proposed ramification charge uses only their split-exceptional attachment loci.

## What this refutes

The retained local data do **not** support any implication of the form

`unit O-contact => ramifies for at least one fibration in a finite rank4 split-fiber orbit`

when the only positive-ramification mechanism supplied is landing at one of the split-fiber attachment points.

Thus replacing one degree-113 map by all 8 last-four fibrations, or by all 20 non-isotrivial next-six/last-four classes, does not by itself repair the missing landing adapter.

This does not rule out a simultaneous rank4 theorem using a different mechanism: e.g. a global member constraint coupling landing values, a critical point not arising from split attachments, a differential relation among the maps, or a theorem that the actual V6 member cannot make the locally independent avoidance choices.

## Decision

- `FINITE_RANK4_SPLIT_ATTACHMENT_BAD_SET_ON_E = true`;
- `AN_LOCAL_LANDINGS_CAN_AVOID_FINITE_RANK4_SPLIT_ATTACHMENT_UNION = true`;
- `LAST_FOUR_ORBIT_FORCES_AT_LEAST_ONE_SPLIT_ATTACHMENT_RAMIFICATION_PER_O_CONTACT = false`;
- `ALL_20_NONISOTRIVIAL_RANK4_CLASSES_FORCE_SPLIT_ATTACHMENT_RAMIFICATION_PER_O_CONTACT = false`;
- `SIMULTANEOUS_RANK4_SPLIT_ATTACHMENT_ROUTE_CLOSES_O266 = false`;
- `GLOBAL_MEMBER_COUPLING_COULD_CHANGE_THIS = UNTESTED`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- This is a local simultaneous-avoidance statement, not a global V6 carrier construction.
- Only the split-attachment ramification mechanism is refuted; other critical loci are not declared absent.
- No exact enumeration of all attachment coordinates is required: finiteness is sufficient for the local avoidance conclusion.
- No Stage32 MAIN, hostile-audit, merge, endpoint, lower-O, or Perfect Cuboid credit follows.
