# Stage33 33-12 V65 J1 discriminator micro-roadmap

```text
ROLE=PLANNING_AND_EXECUTION_CHECKLIST_ONLY
LIVE_GLOBAL_AUTHORITY=stages/stage33/controller.json
BRANCH_EXACT_FRONTIER=stages/stage33/33-12/e3-b1-j1-marked-kc-discriminator-gate-v65.json
CURRENT_LOCKED_FRONTIER=V61_THROUGH_V65
EFFECTIVE_DISCOVERY_ROUTING=V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP
CURRENT_LEAF=RESOLVE_J1_MARKED_KC_ONE_BIT
ATOMICITY_RULE=ONE_SMALL_VERIFIABLE_GOAL_PER_COMMIT
MERGE_ALLOWED=false
```

This roadmap supersedes `ROADMAP-33-12-MICROGOALS.md` only for the current branch leaf. The older roadmap remains a historical V60 planning checkpoint. Exact certificates, controller firewalls, and `MAIN-STATE.json` remain authoritative over prose.

## What STOP means here

The current STOP is a **leaf gate**, not algorithm exhaustion. `Stage33-main-batch` remains allowed. It means only that no marked proper14 column may be promoted until one exact discriminator selects the image of `J1`.

## Locked frontier

- V61: `Pic0(C22_tilde)[2]` ordered basis is `[kappa_A,kappa_D]`.
- V62: full ordered B1 domain basis is `[cc(kappa_A),cc(kappa_D),kappa_A,kappa_D]`.
- V63: column 3 has a literal surface `mu2`/Cech lift `lambda_A`; its marked proper14 coordinate is still open.
- V64: `kappa_A=J1`, `kappa_D=J2`, and `J2 -> u1=[1,0]`.
- V64 leaves exactly two candidates for J1: `u2=[0,1]` or `u1+u2=[1,1]`.
- V65: target fingerprints distinguish the two candidates by minimum norm: `u2 -> 4`, `u1+u2 -> 12`; no source-locked J1 fingerprint has yet been materialized.
- Stage33 remains `6/11`; Stage33-12 is open; Stage33-13 is unreleased; merge is forbidden.

## Research OS / Arsenal routing

Use `docs/arsenal/index.json` first. Current cards are:
- `S33-PW04` — exact marked-source / Picard-interface adapter.
- `S33-PW07` — torsor/Brauer/integral-kernel adapter.

Cards are PROVISIONAL routing aids only. Live Stage33 source locks win. A bounded search miss is not repository absence or mathematical nonexistence. Additional bounded searches require a materially new mathematical signal and must stop before branch-history archaeology or repository-wide enumeration.

## D1 — exact second transport column

Goal: source-lock the image of `J1` under the named CV/contact frame -> fixed marked Kc frame transport.

Acceptance:
- exact producer or formula, not a basis-complement convention;
- `J2 -> u1` retained;
- second column is mechanically replayable;
- result selects exactly one of `[0,1]`, `[1,1]`.

If this is obtained, skip D2/D3 and proceed to D4.

### V67 — #1529 new-signal scope receipt

The exact #1529 adapter (`post1529-fsm-stoll-diagonal-action-source-lock.json`) was tested as a materially new signal. It source-locks only `U/S -> Stoll word` provenance (`U=g4*g5*g9`, `S=g2*g5`) and explicitly grants no other FSM claims. It does **not** supply a named `J1/J2` source action, a fixed-marked-Kc target action, a second transport column, or transport equivariance. Therefore #1529 by itself satisfies neither D1 nor D3.

This closes only the #1529 signal route; it is not a repository-absence or mathematical-nonexistence claim. Exact receipt: `stages/stage33/33-12/e3-b1-j1-post1529-equivariance-scope-gate-v67.json`.

With no current exact D1 witness from this signal, the next construction leaf is D2: construct a J1-specific translation-valued E[2] cocycle from the V63 `lambda_A={f_A,g22}` literal class, using S33-PW07 as method routing only and without relabelling the J2 cocycle.

## D2 — independent J1 source fingerprint

Goal: construct one source-locked J1 invariant that distinguishes target minimum norm `4` from `12`.

Preferred exact witness:
`J1_TWISTED_KERNEL_MINIMUM_NORM`.

Acceptance:
- J1-specific torsor/kernel construction is source-locked;
- no relabelling of the existing J2-specific twisted kernel;
- computed value is exactly `4` or `12`;
- target lookup is replayed from `j2-cv-d2-semantic-orientation.json`.

A value `4` forces `J1 -> u2`; a value `12` forces `J1 -> u1+u2`.

## D3 — automorphism-equivariant discriminator

Use only if a materially new exact target action appears.

Acceptance:
- exact source automorphism action on named `J1,J2`;
- exact action of the corresponding geometric automorphism in the **fixed marked Kc frame**;
- exact equivariance of the transport.

The source elliptic automorphism alone is insufficient and must not be used to guess the second column.

## D4 — decode marked proper14 column 3

Blocked on D1/D2/D3.

Acceptance:
- selected marked Kc coordinate for J1;
- exact marked Picard-dual covector / equivalent adapter;
- proper14 column 3 decoded and replayed;
- no e3 mask20 membership claim until the required matrix solve is actually performed.

## D5 — finish the B1 14x4 matrix

Blocked on D4 and exact conjugate-column transport.

Acceptance:
- all four proper14 columns exact;
- solve `M*x=mask20`;
- record every preimage if true;
- if false, freeze only the B1 route, not e3 lift existence.

## Firewalls

Forbidden:
- identifying historical contact bits `(L,R)` with marked Kc coordinates;
- choosing an arbitrary GL2(F2) complement to `J2 -> u1`;
- relabelling the J2-specific twisted kernel as J1;
- using the source `x -> -x` automorphism without an exact fixed-marked-Kc target action;
- promoting a search miss to absence;
- merge, closure, receiver, endpoint, theorem, or perfect-cuboid credit.

## Batch rule

Each `stage33main batch` works the first unfinished D-leaf, uses Arsenal first, performs only bounded source-lock search justified by a new signal, constructs/replays one exact object, commits it, and reevaluates this roadmap.
