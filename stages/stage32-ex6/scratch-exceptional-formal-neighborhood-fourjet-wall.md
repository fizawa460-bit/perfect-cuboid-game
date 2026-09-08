# Stage32EX6 — exceptional formal-neighborhood four-jet wall

Status: `SCRATCH_EXACT_BOUNDED_EXCEPTIONAL_FORMAL_NEIGHBORHOOD_FOURJET_WALL_NO_ENDPOINT_CREDIT`.

This is an isolated scratch diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266` and the previous scratch local chart

`y=xu`, `z=xu^2`.

The previous scratch leaf showed that for an FSM-minimal branch

`u(x)=lambda+c1*x+c2*x^2+c3*x^3+c4*x^4+...`

and coefficient four-flatness is exactly

`c1=c2=c3=c4=0`.

This leaf asks whether the geometry of one exceptional curve alone forces or forbids that four-flatness.

## Formal-neighborhood bookkeeping

Let `E` be one exceptional curve of the minimal resolution of an A1 node. Standard A1 resolution geometry gives

`E ~= P1`, `E^2=-2`.

Let `M=C.E`. At O266 all intersections of the hypothetical strict transform with `E` are simple and distinct, so the restriction of a local defining section of `C` to `E` has a reduced zero divisor

`D0=lambda_1+...+lambda_M`

of degree `M`.

Use the ideal filtration by powers of `I_E=O(-E)`. The kth normal graded piece of a section of `O(C)` along `E` lies in

`O_E(C-kE)`

and therefore has degree

`(C-kE).E=M+2k`.

Write the formal defining section schematically as

`s=s0+x*s1+x^2*s2+...`,

where the kth coefficient represents a section of degree `M+2k` on `E`.

At a simple root `lambda_i` of `s0`, implicit solution gives

`c1(lambda_i)=0 iff s1(lambda_i)=0`.

Inductively, once `c1=...=c_{k-1}=0`, one has

`ck(lambda_i)=0 iff sk(lambda_i)=0`.

Hence simultaneous coefficient four-flatness at all `M` branches over this exceptional curve requires

`s_k|_{D0}=0`, `k=1,2,3,4`.

But `deg s_k=M+2k`, so such vanishing is formally compatible: one may have

`s_k=s0*g_k`

with

`g_k in H0(E,O_E(2k))`.

The quotient spaces have dimensions `2k+1`, so no degree obstruction appears for k=1,...,4.

## Decision

The exceptional formal neighborhood by itself neither forces nor forbids four-flatness.

Canonical scratch decisions:

- `A1_EXCEPTIONAL_NORMAL_BUNDLE_DEGREE = -2`;
- `KTH_NORMAL_COEFFICIENT_DEGREE = M+2k`;
- `ALL_BRANCHES_CK_ZERO_IFF_KTH_COEFFICIENT_VANISHES_ON_D0 = true` under the lower-flatness induction;
- `SK_DIVISIBLE_BY_S0_WITH_QUOTIENT_DEGREE_2K_IS_FORMALLY_COMPATIBLE = true`;
- `EXCEPTIONAL_FORMAL_NEIGHBORHOOD_FORCES_FOUR_FLATNESS = false`;
- `EXCEPTIONAL_FORMAL_NEIGHBORHOOD_EXCLUDES_FOUR_FLATNESS = false`;
- `FOUR_JET_FLATNESS_ACTUALLY_PROVED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Consequence for route selection

The missing four-flatness theorem cannot come from `C.E_j=M_j`, the A1 normal bundle, and formal restriction degrees alone. It needs genuinely global member information, a global differential/correspondence identity, or an explicit carrier equation.

## Firewalls

- Formal compatibility is not construction of a global V6 member.
- The local coefficient filtration does not prove simultaneous realizability across all 48 exceptional curves.
- No dimension independence, vanishing theorem, or effectivity upgrade is assumed.
- No Stage32 MAIN, endpoint, lower-O, hostile-audit, merge, or Perfect Cuboid credit follows.
