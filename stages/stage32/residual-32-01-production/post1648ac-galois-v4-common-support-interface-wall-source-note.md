# Stage32 post1648AC Galois V4 common-support interface wall

Status: `PASS_EXACT_COMMON_SUPPORT_INTERFACE_WALL_NONEXCLUSION`.

Scope is the fixed `g1-d186`, `O=210`, `qprime=4`, `Q=602` carrier class only. This scratch leaf carries no MAIN authority, receiver, route, theorem, endpoint, or perfect-cuboid credit.

## Parent exact reduction

Parent post1648AB is source-locked by canonical SHA256
`7b36625f61fd1c2d7868f2f5b5a7deaeb6dc50835cba77b0189e2b676e0cbcf1`.

For a hypothetical integral curve `C` in the exact V6 divisor class `D`, every `Q`-rational point is fixed by both retained Galois involutions `cc` and `ct`. Hence

`C(Q) subset C ∩ cc(C) ∩ ct(C) ∩ ccct(C)`.

AB proves the four divisor classes are pairwise distinct. In particular `C` and `ct(C)` are distinct integral curves, and their proper intersection has total length

`D . ct(D) = 1026`.

Therefore the four-way common intersection is a closed subscheme of `C ∩ ct(C)` and has conditional length at most `1026`. This is an upper bound only; no support point is identified or excluded.

## Exact retained member-level gap

The merged post1556 source-gap certificate `256cbd7d1a3f3667d1558e530293392a3068f52cd8dfa1495f14cb3015caa308` already records that the retained V6 input supplies no:

- defining equation or ideal for the carrier member;
- distinguished defining section;
- uniqueness of an integral carrier in the fixed V6 class.

Thus Picard/class data alone cannot materialize the scheme `C ∩ cc(C) ∩ ct(C) ∩ ccct(C)`.

## Current-main Stage33 locator applicability check

Current main at discovery was `bd1f40297f8dcf79e5bb4ef0b8cdc13fdb844177` (merged PR #1667). Its V91C1V known140 locator starts from already explicit strict-prime ideal generators and tests containment in the pinned known curves. It does not invert an arbitrary positive-square Picard class into a distinguished height-one prime. Therefore it does not fill the V6 member-level gap.

This #1667 check is discovery-only because the asset is outside the AB parent ancestry; it is not promoted to a replayed parent source lock. The conclusion is only category mismatch for this interface, not repository-wide absence of every possible construction.

## Decision

The common three-survivor strategy remains the preferred route, but no survivor is excluded here. Exact next interface:

`SOURCE_LOCK_ACTUAL_V6_CARRIER_MEMBER_IDEAL_OR_DISTINGUISHED_SECTION_OR_EQUIVALENT_LOCAL_GALOIS_V4_COMMON_SUPPORT_ADAPTER`.

Do not infer `Q602_excluded`, `O210_excluded`, or any rational-point nonexistence from the finite length bound alone.
