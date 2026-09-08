# Stage32EX6 — rank-4 local-unramified contact wall

Status: **EXPLORATORY EXACT BOUNDED WALL — NO MAIN CREDIT**.

This note sharpens the degree-113 rank-4 adapter wall. It does not reopen Stage32 MAIN and does not claim `O=266` exclusion.

## Question

The previous EX6 preflight found a unique last-four rank-4 fibration class of V6 degree `113`, with six split `G3` bad fibers whose 24 exceptional components carry V6 exceptional mass `140`.

The tempting missing implication was

`every O-contact contributes >= 1 to rank4 ramification`.

The question here is whether that implication is merely unproved, or whether the retained local endpoint model already shows that it is false as a universal local statement.

## Source locks

Primary geometry:

- Michael Stoll and Damiano Testa, *The surface parametrizing cuboids*, Section 5, February 24 2025 version.
- The last four rank-4 quadrics give morphisms on the singular cuboid surface. Their fibrations have six fibers splitting into two curves from `G3` "as above"; the immediately preceding rank-4 case identifies the corresponding split type as two `G3` curves joined by four exceptional curves. The same last-four fibrations also have twelve hyperelliptic genus-3 fibers with two nodes at singular points.

Exact computational source locks:

- Stoll–Testa verification repository `Cuboids/cuboids.magma`, blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`;
- `Cuboids/Section5_fibrations.log`, blob `9cfef75aa58335655d6ae3e78597f5924b6c2433`;
- EX6 exact orbit diagnostic `stages/stage32-ex6/diagnose_stage32_ex6_rank4_fibration_orbit.py`;
- V6 canonical `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`;
- V6 all-140 pairings SHA256 `4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3`;
- exact Hperp all-140 adapter canonical `fc695b9405ec4becfbcf19866c0c70fceed9372186a5aa4974879f302ee8ffe9`.

Endpoint local input:

- `stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md` at consolidation head `82b551d92ad2ef1a86f8303758c7aa17c0a6d960`, blob `512fcc70afb1acf16956fd4b7a2b9b935a052150`;
- EX6 endpoint source lock `stages/stage32-ex6/post1697-o266-endpoint-source-note.md`.

## Exact split-fiber attachment geometry

For the representative last-four split fiber, the exact EX6 diagnostic starts from two `G3` labels and defines `common_exc` to be the exceptional labels pairing `1` with **both** `G3` components. It verifies:

- the two resolved `G3` components have mutual intersection `0`;
- there are exactly four such common exceptional curves;
- every one of those four exceptional curves has intersection `1` with each `G3` component.

The diagnostic then uses the reduced support

`G3_a + G3_b + E_1 + E_2 + E_3 + E_4`

as the split-fiber class and reconstructs its full Aut orbit. For the unique degree-113 fibration class there are six pairwise-disjoint split supports, hence exactly `6*4=24` exceptional components in these six split fibers. Their V6 exceptional mass is exactly `140`.

For any one of these 24 exceptional components `E`, the two `G3` components are disjoint on the resolution while `E.G3_a=E.G3_b=1`. Therefore the two intersections are two distinct attachment points on `E`. Away from those two points, `E` is a smooth reduced component of the split fiber and no other component of that fiber passes through the point.

## Local lemma: a generic unit contact is unramified

Let `f:S -> P1` be this resolved rank-4 fibration and let `q` be a point of one of the 24 split exceptional components `E` away from its two attachment points.

Because the fiber is reduced and smooth at `q`, there are regular local coordinates with

- `E = {x=0}`;
- for a uniformizer `t` at the corresponding base point, `f^*t = u*x` with `u` a unit.

Let a normalization branch of a hypothetical V6 carrier meet `E` at `q` with endpoint multiplicity `m=1`. Then its local intersection with `E` is one, so `x` restricts to a uniformizer on the branch. Consequently

`ord_q((f|_N)^*t)=1`.

Thus the restricted map `f|_N` is **unramified** at that unit exceptional contact.

Positive ramification from this split-fiber mechanism can only be forced after adding extra information that places the branch at an attachment/critical point or otherwise increases the local order of the base parameter.

## Compatibility with the retained O266 local witness

At `O=266`, the endpoint contract gives 266 unit exceptional contacts. The retained AN local model allows the landing parameters on each exceptional curve to be chosen pairwise distinct, and the EX6 endpoint note uses this freedom to realize the full unit-contact profile locally.

On each of the 24 split exceptional curves, only two landing points are forbidden if we want the contact to be away from the `G3` attachments. Since the landing field is infinite and each `M_j` is finite, the pairwise-distinct AN landing parameters can be chosen to avoid those two points.

Therefore the retained endpoint local model can realize **all 140** unit contacts carried by the 24 degree-113 split exceptional components at non-attachment points. By the local lemma, all 140 of those contacts are then unramified for the degree-113 rank-4 fibration.

This is a local realizability statement, not a construction of a global V6 carrier.

## Sharpened decision

The previous status

`RANK4_DEGREE113_TO_O_RAMIFICATION_ADAPTER = MISSING`

can be sharpened for the naive universal adapter to

`NAIVE_EVERY_O_CONTACT_RAMIFIES_UNDER_DEGREE113 = LOCALLY_FALSE`.

In particular, no proof of

`O=266 => R_rank4 >= 266`

can come from endpoint unit multiplicity plus the reduced split-fiber local geometry alone. The retained local endpoint model already permits 140 degree-113 split-exceptional O-contacts with ramification contribution zero.

This does **not** prove that an actual global V6 carrier can choose those landing points independently. A future useful re-entry must supply genuinely global/member-level information forcing sufficiently many landing points into the finite attachment/critical loci, or use a different simultaneous-fibration inequality that avoids the per-contact ramification premise.

## Retained bounded fields

- `DEGREE113_SPLIT_EXCEPTIONAL_CURVE_COUNT = 24`;
- `DEGREE113_SPLIT_EXCEPTIONAL_V6_MASS = 140`;
- `ATTACHMENT_POINTS_PER_SPLIT_EXCEPTIONAL = 2`;
- `ALL_140_SPLIT_EXCEPTIONAL_CONTACTS_LOCALLY_UNRAMIFIED_REALIZABLE = true`;
- `NAIVE_EVERY_O_CONTACT_RANK4_RAMIFICATION_ADAPTER = LOCALLY_FALSE`;
- `O266_ENDPOINT_EXCLUDED = false`.

## Firewalls

- No Stage32 MAIN authority/state edit.
- Q602/O210 and survivors `[73,97,235]` are unchanged.
- This is a bounded local countermodel to one proposed adapter, not a global member construction.
- `O266_ENDPOINT_NOT_CLOSED` remains the EX6 endpoint decision.
- No descent to O264 is authorized.
- No receiver/theorem/endpoint/perfect-cuboid credit.
- No merge is implied.
