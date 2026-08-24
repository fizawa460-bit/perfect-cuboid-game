# Stage33-04 hostile re-audit — PR #1362

Verdict: `PASS_ODD_PRIMARY_RESIDUAL_REJECT_ALL_PRIMARY_CLOSURE_ON_HIGHER_TWO_POWER_GERSTEN_DESCENT`

Re-audited functional head: `078198be1466d5d2c9eb3e0c204b1bee79f5c68e`.

Current-head workflow evidence:

- run `32705824742` — `Stage33-04 physical-boundary residue skeleton` — `success`;
- artifact `9512234314` — `stage33-04-boundary-residue-skeleton`;
- artifact ZIP digest `sha256:19aa8fa2ca3fe137a96865a2cc4dad4fe9e47eae6896904d2bcbf74db37b2792`.

The previous audit remains accepted as an exact prefix. This re-audit specifically tests the new leaf `certify_odd_primary_arithmetic_character_descent.py` and whether it is sufficient to promote Stage33-04 to `CLOSED`.

## Previously accepted exact prefix

The following remain independently accepted:

- physical boundary `72 = 24 side + 48 exceptional`;
- `144` codimension-two crossings;
- connected incidence rank `71`, saturated integral cycle rank `73`;
- `ct=I`, `rank(cc-I)=12`, all twelve nonzero Smith factors equal `1`;
- geometric Galois-fixed permutation-cycle module `(Q/Z)^61`;
- Ford/Kummer source pullback rank `0`;
- exponent-two Q-fixed graph cycle dimension `61`;
- unit-symbol secondary-residue span rank `44` over `F2`;
- explicit exponent-two residual dimension `17`;
- the 17 exponent-two residual directions have exact mod-2 first-residue/function/constant-squareclass descent.

All JSON canonical SHA fields in the current-head artifact were independently recomputed and matched.

## New odd-primary leaf — accepted

The current artifact gives the boundary complex-conjugation orbit counts

```text
geometric boundary components: 48 fixed + 12 conjugate pairs = 72
geometric crossings:           96 fixed + 24 conjugate pairs = 144
```

The source-locked splitting model places the relevant arithmetic boundary prime divisors over `Q` or `Q(i)`. For odd-primary torsion, the crossing Tate-twist invariants vanish because these constant fields contain no nontrivial odd-order roots of unity. Away from crossings a single boundary branch cannot carry a nonzero second residue for a class unramified on the physical open; hence the compatible odd-primary first-residue characters are unramified on the complete boundary `P1`s and reduce to constant-field characters.

The exact odd-primary boundary-character module is therefore accepted parametrically as

```text
Hom_cont(G_Q,Q/Z)_odd^48
  direct_sum
Hom_cont(G_Q(i),Q/Z)_odd^12.
```

This closes the previously named residual

`R33-BR0G-ODD-PRIMARY-ARITHMETIC-CHARACTER-DESCENT`.

It is a parametric residue module, not a finite list of Brauer generators and not a Brauer-Manin conclusion.

## Why BR0G still cannot close

The new odd-primary certificate attempts to promote

`all_primary_physical_open_unramified_kernel_complete_candidate=true`.

That promotion is rejected.

The accepted geometric fixed module contains a full two-primary divisible part

```text
(Q_2/Z_2)^61.
```

But the only arithmetic descent certificate for the intrinsic two-primary residual is explicitly scoped

```text
scope = EXPONENT_TWO_RESIDUAL_ONLY
actual_first_residue_function_descent_complete_mod2 = true
constant_squareclass_descent_complete_mod2 = true.
```

Likewise the unit-symbol calculation is only a mod-2 secondary-residue span (`rank_F2=44`). Therefore the evidence computes the exponent-two layer, not the full `2^n`-primary Gersten character module.

This distinction is material at the actual crossing fields:

- over `Q`, the two-primary Tate-twist invariant contains the order-2 roots of unity;
- over `Q(i)`, it contains roots of unity through order `4`.

Thus the two-primary second-residue targets are not zero. In particular, order-4 compatibility at `Q(i)` crossings and the full continuous two-primary constant-character families are not determined by an `F2` graph computation. No certificate proves that all higher `2^n` classes reduce to, or lift uniquely from, the exponent-two 61=44+17 calculation.

Consequently the Stage29 requirement to compute the boundary Gersten kernel prime-by-prime and the Stage33-04 gate `UNRAMIFIED_PHYSICAL_OPEN_KERNEL_EXACT=true` remain unmet.

## Accepted re-audit state

```text
UNIT_STATUS=BLOCKED_NEW_KERNEL
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR0G=OPEN
ARITHMETIC_ODD_CHARACTER_DESCENT_COMPLETE=true
UNRAMIFIED_PHYSICAL_OPEN_KERNEL_EXACT=false
UNRESOLVED_UNKNOWN_IN_SCOPE=1
NEW_KERNEL_ID=R33-BR0G-TWO-PRIMARY-PRIME-POWER-GERSTEN-CHARACTER-DESCENT
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

The exact next leaf is

`L33-04-COMPUTE-FULL-Q2Z2-BOUNDARY-H1-AND-MU2-MU4-CROSSING-COMPATIBILITY`.

It must compute the full two-primary first-residue character modules on all 60 arithmetic boundary prime divisors, the prime-power second-residue compatibility at the 96 `Q` crossings and 24 `Q(i)` crossing pairs, quotient by proper residues, and certify whether any order-4 or higher-power classes survive. The existing exponent-two result is a locked prefix and must not be recomputed as a substitute.

Stage33 progress remains `2/11`; Stage33-06 is not released. Merge is permitted only as this audited blocked checkpoint, with no downstream or theorem credit.