# Fundamental-group / Chabauty–Kim screen

SOURCE=`arXiv:2310.12710v3`
AUTHORS=Benjamin_Enriquez_David_Jarossay_Francesco_Maria_Saettone_Yotam_Svoray
STATUS=THEOREM_ECOSYSTEM_FOUND_NOT_CURRENT_ENDPOINT_FOUNDATION

## Fresh source lock

The current v3 (2026-07-06), *The fundamental group of surfaces parametrizing cuboids*, proves:

- the projective cuboid surface and its minimal resolution are simply connected;
- the face-cuboid surface and its resolution are simply connected;
- two smooth open face-cuboid loci have fundamental group `F_3 semidirect Z^2`;
- their Malcev completions reduce to the free pro-unipotent group on three generators.

## Routing

For the full projective endpoint, simple connectedness blocks the naive hope that its ordinary topological fundamental group itself supplies a new arithmetic quotient.

For open loci, deleting boundary divisors can create nontrivial fundamental groups. This naturally interfaces with F1/F2/F7, but no effective rational-point theorem has yet been adapted in this project to the relevant two-dimensional cuboid open.

The audit deliberately avoids the overbroad statement that Chabauty–Kim has no higher-dimensional/surface theory at all. The only certified negative statement needed here is narrower:

```text
CUBOID_OPEN_EFFECTIVE_CHABAUTY_KIM_ADAPTER_AVAILABLE=false
```

## Future receiver

```text
R29-PI1-OPEN = ExactOpenEndpointFundamentalGroupAndUnipotentArithmeticAdapter
```

## Verdict

```text
NEW_THEOREM_ECOSYSTEM=true
CURRENT_RATIONAL_POINT_OBSTRUCTION=false
INDEPENDENT_FOUNDATION=false
CUBOID_OPEN_EFFECTIVE_CHABAUTY_KIM_ADAPTER_AVAILABLE=false
```

No existence/nonexistence conclusion follows.
