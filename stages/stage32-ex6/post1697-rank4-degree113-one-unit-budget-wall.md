# Stage32EX6 — degree-113 one-unit ramification budget wall

Status: **EXPLORATORY EXACT BOUNDED WALL — NO MAIN CREDIT**.

This note quantifies the consequence of the retained degree-113 local-unramified contact wall. It does not reopen Stage32 MAIN and does not claim `O=266` exclusion.

## Inputs already retained

For the unique last-four rank-4 fibration class of V6 degree `d=113`:

- a hypothetical genus-one V6 normalization `N` restricts to a degree-113 map `N -> P1`;
- Riemann–Hurwitz therefore fixes the total ramification degree at `2d=226`;
- at `O=266`, all 266 exceptional contacts have multiplicity one;
- the six split `G3` bad fibers use 24 exceptional components carrying V6 exceptional mass `140`;
- the retained endpoint local model can place all 140 of those split-exceptional unit contacts away from the attachment loci, where they are unramified for the degree-113 map.

The exact source locks and local proof are retained in:

- `stages/stage32-ex6/post1697-rank4-degree113-adapter-wall.md`;
- `stages/stage32-ex6/post1697-rank4-local-unramified-contact-wall.md`;
- `stages/stage32-ex6/post1697-rank4-local-unramified-contact-contract.json`.

## Exact arithmetic

After allowing the 140 split-exceptional contacts to contribute zero ramification in the retained local endpoint model, the number of remaining O-contacts is

`266 - 140 = 126`.

A Riemann–Hurwitz contradiction would require a forced ramification lower bound strictly larger than the exact total `226`, hence at least

`227`.

Therefore a route which obtains at most one forced ramification unit from each of those 126 remaining contacts can force at most

`126`,

which is short of the contradiction threshold by

`227 - 126 = 101`.

Equivalently, after zero credit is allowed on the locally avoidable 140 contacts, any contact-sum proof must force average ramification contribution at least

`227/126 > 1.80`

from the remaining 126 contacts, or recover positive forced ramification from some of the 140 locally avoidable contacts, or add an independent ramification lower bound not charged to O-contacts.

## What this rules out

The following bounded route is numerically insufficient:

1. use only the retained O266 endpoint/local geometry;
2. allow the 140 degree-113 split-exceptional contacts to use the retained unramified local realizations;
3. extract no independent ramification lower bound away from O-contacts;
4. charge at most one ramification unit to each of the other 126 O-contacts.

Under exactly those premises the strongest possible forced lower bound is `126`, so it cannot contradict the exact Riemann–Hurwitz total `226`.

This is stronger than saying that the original all-266 one-unit adapter is missing: the retained local model leaves a quantitative deficit of 101 ramification units even after maximally charging one unit to every remaining O-contact.

## What this does not rule out

This wall does **not** show that the degree-113 fibration route is globally impossible. In particular it does not exclude a future theorem that:

- globally forces some of the 140 split-exceptional contacts into ramified landing/jet configurations;
- forces ramification contribution greater than one at sufficiently many of the remaining contacts;
- supplies a separate lower bound for ramification away from the O-contact ledger;
- couples several fibrations or correspondences in a way not expressible as this one-unit contact sum.

No actual global V6 carrier is constructed by the local countermodel.

## Retained bounded fields

- `DEGREE113_RH_TOTAL = 226`;
- `O266_CONTACTS = 266`;
- `LOCALLY_ZEROABLE_SPLIT_EXCEPTIONAL_CONTACTS = 140`;
- `REMAINING_O_CONTACTS = 126`;
- `ONE_UNIT_REMAINING_CONTACT_MAX = 126`;
- `CONTRADICTION_THRESHOLD = 227`;
- `ADDITIONAL_FORCED_RAMIFICATION_NEEDED = 101`;
- `LOCAL_ENDPOINT_ONE_UNIT_REMAINING_CONTACT_ROUTE = NUMERICALLY_INSUFFICIENT`;
- `O266_ENDPOINT_EXCLUDED = false`.

## Firewalls

- No Stage32 MAIN authority/state edit.
- Q602/O210 and survivors `[73,97,235]` are unchanged.
- The 140 zero-ramification contacts are a retained local realizability statement, not a global member theorem.
- The 101-unit deficit applies only to the bounded route defined above.
- `O266_ENDPOINT_NOT_CLOSED` remains the EX6 endpoint decision.
- No O264 descent, receiver/theorem/endpoint/perfect-cuboid credit, or merge is authorized.
