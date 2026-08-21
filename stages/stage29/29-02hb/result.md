# Stage29-02hb — Campedelli quotient foundation

## Status

```text
STATUS=SUBMISSION_READY_AUDIT_REQUIRED
NOVELTY_IN_REPO=HIGH_VALUE_NEW_QUOTIENT_FOUNDATION
LITERATURE_NOVELTY_CLAIM=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Main result

Stage29-02ha identifies the resolved perfect-cuboid surface `S~` as the degree-64 sign/Kummer cover of `P^2` attached to the seven lines

```text
A1: x=0
A2: y=0
A3: z=0
B3: x+y=0
B2: x+z=0
B1: y+z=0
C : x+y+z=0.
```

Its geometric sign deck group is

```text
Gamma = F2^7 / <(1,1,1,1,1,1,1)> ~= (Z/2)^6.
```

This stage finds exact rank-3 subgroups `H <= Gamma` for which the quotient

```text
S~ -> S~/H
```

is the degree-8 universal-cover presentation of a classical Campedelli surface.

Equivalently, choose a quotient map

```text
q: Gamma -> F2^3
```

such that the seven branch inertia classes map bijectively to the seven nonzero elements of `F2^3`. At every triple point of the seven-line arrangement we additionally require the three labels to sum nontrivially. This is exactly the Campedelli-arrangement branch condition from the source literature.

## Exact finite classification

A dependency-free exact `F2` checker enumerates all admissible labelings.

```text
raw admissible labelings                   = 1680
GL(3,F2) relabelings                       = 168
rank-3 kernels H in Gamma                  = 10
Aut_P2(D)                                  = S4, order 24
S4-orbits on the 10 kernels                = 2
orbit sizes                                = 8 + 2
```

Thus the full sign surface has exactly ten Campedelli quotient kernels of this type, and only two geometric kernel types modulo the audited arrangement symmetry.

```text
R29-CAMP0=ExactCampedelliQuotientKernelClassification
STATUS=PASS_CANDIDATE
```

## Why the quotient is the right surface class

For every admissible kernel, local inertia injects into `Gamma/H` at every branch stratum:

- one branch line: its nonzero label survives;
- a double point: two distinct nonzero labels are independent over `F2`;
- a triple point: the Campedelli condition makes the three labels independent.

Hence `H` has trivial intersection with every local inertia subgroup. On the minimal resolutions this gives a free degree-8 action candidate. The quotient has

```text
K^2 = 16/8 = 2,
chi(O) = 8/8 = 1,
```

and the source theorem identifies the corresponding `(Z/2)^3` seven-line cover with the canonical model of a classical Campedelli surface. Mendes Lopes--Pardini--Reid prove that an etale degree-8 cover of a Campedelli surface is a complete intersection of four quadrics in `P^6` and is its universal cover.

The exact freeness-on-resolution adapter is deliberately left for fresh audit rather than self-certified.

```text
R29-CAMP1=ResolvedFreeActionAndUniversalCoverAdapter
STATUS=PASS_CANDIDATE
```

## Arithmetic routing

Every admissible `H` is a subgroup of the rational coordinate-sign deck group, so the quotient construction is defined over `Q` at the group-action level.

A rational perfect-cuboid point maps to a rational point on every such quotient. Therefore

```text
C_H(Q)=empty for any one audited quotient H
=> perfect-cuboid rational locus empty.
```

The converse is false without descent: a rational point on `C_H` need not lift to `S~(Q)`. Its lifting class is an `H`-torsor.

This creates a genuinely new arithmetic compression route:

```text
R29-CAMP2 = ArithmeticHTorsorDescentForTheTwoS4QuotientTypes
R29-CAMP3 = SevenCampedelliInvolutionQuotientsRationalVsEnriquesLedger
R29-CAMP4 = CampedelliBrauerAndTwoPrimaryDescentCompatibilityWith29_02f
```

No rational-point obstruction is claimed here.

## Relation to earlier Stage29 foundations

This is not another K3 quotient. It compresses the full `K^2=16, pg=7` endpoint surface by a free order-8 sign subgroup to a `K^2=2, pg=q=0` Campedelli surface.

So the new view is

```text
full endpoint S~
  -- / H, |H|=8 --> classical Campedelli surface
  -- bicanonical --> P^2 with the same seven-line branch arrangement.
```

It complements rather than duplicates:

- `29-02ha`: full 64-sheet sign/Kummer cover;
- `29-02e`: seven rank-two K3 motives;
- `29-02f`: physical-open Brauer route;
- `29-02g`: modular level-4 / 8-congruence route.

## Routing

The mining stop condition remains unsatisfied because `02hb` is a second post-`g` HIGH_VALUE foundation.

```text
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
STAGE29_02_MINING_STOP_CONDITION_SATISFIED=false
NEXT_ITEM_AFTER_PASS=29-02hc
NEXT_EXPECTED_COMMAND=Stage29-audit
```
