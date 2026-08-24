# Stage33-04 hostile audit — PR #1362

Verdict: `PASS_EXACT_PREFIX_BLOCKED_NEW_KERNEL_AFTER_REJECTING_PREMATURE_BR0G_CLOSURE`

Audited functional head: `47cb96b6cd7acaa19f7fc51e9f72a8dc8e36964c`.

Final-head workflow evidence audited:

- run `32701829304` — `Stage33-04 physical-boundary residue skeleton` — `success`;
- artifact `9510818470` — `stage33-04-boundary-residue-skeleton`;
- artifact ZIP digest `sha256:4c2d15df6394004addfb5ae99c40d0161b00174c59f12a5c6069061ca30afb3a`.

The older run/artifact hashes recorded in the pre-audit handoff (`32701473247` / `9510714843`) are superseded by the final functional head and are not the audit authority.

## Independently reproduced exact prefix

The audit downloaded the final artifact and recomputed the following independently of the production summary.

### Boundary/SNC complex

From the 72 stable components and 144 listed codimension-two crossings, the oriented incidence matrix was rebuilt directly.

- vertices: `72 = 24 side + 48 exceptional`;
- crossings/edges: `144`;
- connected components: `1`;
- incidence rank over `Q`: `71`;
- incidence Smith nonzero factors: exactly `71` copies of `1`;
- integral cycle rank: `144 - 71 = 73`;
- stored 73-row cycle basis has rank `73`, annihilates the incidence matrix exactly, and has Smith nonzero factors exactly `73` copies of `1`.

Thus the stored integral cycle lattice is a saturated exact kernel, not a rational-rank surrogate.

### Galois action on the cycle lattice

The source-locked boundary action was independently checked from the artifact matrices.

- `ct = I_73`;
- `cc^2 = I_73`;
- `trace(cc)=49`;
- `rank(cc-I)=12`;
- Smith nonzero invariant factors of `cc-I`: twelve copies of `1`.

Therefore, for the geometric permutation-cycle module with trivial coefficient action used by this adapter,

`ker(cc-I : (Q/Z)^73 -> (Q/Z)^73) ~= (Q/Z)^61`

with no additional finite Smith-kernel factor. The rational V4 character multiplicities `61,12,0,0` are reproduced.

### Two-primary graph residual

The exponent-two linear algebra was independently recomputed.

- Q-fixed cycle dimension: `61`;
- unit-symbol secondary-residue span rank: `44`;
- explicit residual basis rank: `17`;
- combined rank: `61`;
- every one of the 44 unit-image vectors and 17 residual vectors satisfies the graph-cycle parity equations.

Thus the exact graph-level decomposition `61 = 44 + 17` is accepted.

### Seven-line / Kummer pullback

The six affine ratios against `Ls=x+y+z` pull back as

`x/Ls=(a1/c)^2`, `y/Ls=(a2/c)^2`, `z/Ls=(a3/c)^2`,
`(x+y)/Ls=(b3/c)^2`, `(x+z)/Ls=(b2/c)^2`, `(y+z)/Ls=(b1/c)^2`.

Hence every ambient pair 2-symbol in the Ford source pulls back trivially. The recorded endpoint pullback rank `0` is accepted. This gives no endpoint theorem credit.

All canonical SHA fields in the final artifact JSON certificates were independently recomputed and matched.

## Closure rejection

The exact prefix above does **not** justify `UNIT_STATUS=CLOSED` or `BR0G=DISCHARGED` under the authoritative Stage33 contract.

The final functional-head certificates themselves explicitly retain:

- `arithmetic_odd_character_descent_complete=false`;
- `all_primary_physical_open_unramified_kernel_complete=false`;
- `br0g_discharged=false`;
- `new_residual_kernel=R33-BR0G-ODD-PRIMARY-ARITHMETIC-CHARACTER-DESCENT`.

The exponent-two function/constant-squareclass certificate is explicitly scoped `EXPONENT_TWO_RESIDUAL_ONLY` and carries the firewall that odd-primary `H^1(-, Z/l)` character descent remains.

This matters because the authoritative Stage33-04 closure gate requires both

- `UNRAMIFIED_PHYSICAL_OPEN_KERNEL_EXACT=true`, and
- `BR0G=DISCHARGED`,

and the Stage29 BR0G receiver explicitly includes one-variable residue arithmetic/Galois descent in the boundary receiver. No previously audited contract/controller repair reassigns the named BR0G odd-primary residual to a sibling unit. Stage33-03 and Stage33-07 may eventually supply data useful for integration, but a sibling/downstream responsibility cannot be used retroactively to weaken the Stage33-04 closure gate.

Therefore the pre-audit prose claims

`UNRAMIFIED_PHYSICAL_OPEN_KERNEL_EXACT=true`,
`UNRESOLVED_UNKNOWN_IN_SCOPE=0`, and
`BR0G=CLAIMED_DISCHARGED_PENDING_HOSTILE_AUDIT`

are rejected.

## Accepted audited state

`Stage33-04` is retained as an exact, valuable checkpoint but is **not CLOSED**:

```text
UNIT_STATUS=BLOCKED_NEW_KERNEL
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR0G=OPEN
UNRAMIFIED_PHYSICAL_OPEN_KERNEL_EXACT=false
UNRESOLVED_UNKNOWN_IN_SCOPE=1
NEW_KERNEL_ID=R33-BR0G-ODD-PRIMARY-ARITHMETIC-CHARACTER-DESCENT
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

The accepted closed-unit progress therefore remains `2/11` (`33-01`, `33-02`). Stage33-06 is not released by this audit. The exact next work is to discharge the named odd-primary arithmetic-character descent or to make an independently hostile-audited contract repair that proves the dependency belongs elsewhere without dropping any BR0G class.
