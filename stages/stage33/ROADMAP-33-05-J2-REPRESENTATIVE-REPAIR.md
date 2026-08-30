# Stage33-05 J2 named-representative repair roadmap

Purpose: make the hostile reopen of Stage33-05 operationally visible and prevent Stage33 MAIN from appearing to drift backward without a finite repair plan.

This repair band does **not** revoke the abstract computation `Br(Kc_bar)[2] ~= (F2)^2` or the abstract quotient label `J2` merely because the previously promoted concrete `ell_J2` failed. What is revoked is the credit that the current Q-defined `ell_J2` is a nonzero geometric CV representative of that abstract class.

## Repair exit target

Stage33-05 may be re-closed only after either:

1. a corrected nonzero CV representative for the abstract `J2` is constructed and independently checked in the actual quotient `L^*/(K^* L^{*2})`, then its explicit Creutz--Viray `E[2]` cocycle is computed; or
2. the abstract finite presentation itself is shown to have misidentified `J2`, in which case the affected Stage33 dependency chain is explicitly revoked and rebuilt.

No Stage33-13 release is allowed during this repair band.

## Finite repair ladder

| Leaf | Question | Exact exit condition | Current state |
|---|---|---|---|
| R0 | Is the promoted `ell_J2` actually nonzero in the geometric CV quotient? | Exact full branch-algebra regression of `ell_J2` modulo `K^*L^{*2}` | **DONE: ZERO** |
| R1 | Does the abstract `J2` basis element remain genuinely nonzero independently of the bad representative? | Recompute the quotient/presentation nonzero statement without using the revoked `ell_J2`; identify exactly what object the symbol `J2` denotes | **DONE: ABSTRACT_J2_NONZERO_CONFIRMED** |
| R2 | Can a correct concrete representative of abstract `J2` be constructed? | Produce `ell_J2_corrected` and certify `[ell_J2_corrected] != 0` in `L^*/(K^*L^{*2})`, with branch/ruling dictionary source-locked | **IN_PROGRESS** |
| R3 | What is its explicit generic-fiber cohomology class? | Apply Creutz--Viray explicit descent to materialize a nonzero cocycle in `H^1(K,E[2])` and fixed rational `E[2]` Kummer coordinates | **BLOCKED_BY_R2** |
| R4 | Which marked Brauer functional is it? | Build the associated 2-cover/torsor or equivalent lattice object and determine `min T(X_J2) in {4,8,12}`, hence `[0,1]`, `[1,0]`, or `[1,1]` | **BLOCKED_BY_R3** |
| R5 | Can Stage33-05/12 credit be restored? | Independent hostile replay of R1--R4; restore only the credits actually re-established; update Stage33 controller and downstream release gates | **BLOCKED_BY_R4** |

## R1 exact closure

R1 was closed without using the revoked `ell_J2`.

In the fixed geometric presentation basis `[J1,J2,q1,q2,q3]`, the exact `x-alpha` image has the four possible normal forms

```text
span{ J1,
      b*J2+q1+q2,
      d*J2+q1+q2+q3 },  b,d in F2.
```

For all four `(b,d)` choices, the image has rank 3 and adjoining the vector `J2=(0,1,0,0,0)` raises the rank to 4. Hence `J2` is not in `im(x-alpha)` in any case. Therefore the abstract class denoted `J2` remains a genuinely nonzero element of `LcE/im(x-alpha)`.

Certificate: `stages/stage33/33-05/j2-abstract-nonzero-reaudit.json`.
Verifier: `stages/stage33/33-05/certify_j2_abstract_nonzero_reaudit.py`.

This restores **only** abstract geometric nonzero-ness. It does not restore the revoked concrete `ell_J2`, its Q-descent, or any marked coordinate.

## Stop / escalation rules

- R1 has only two legitimate outcomes: `ABSTRACT_J2_NONZERO_CONFIRMED` or `ABSTRACT_J2_SURVIVAL_REVOKED`. **Resolved: CONFIRMED.**
- If R1 confirms abstract J2 but R2 fails after two materially different exact constructions, run a bounded breadth audit before adding a third construction.
- If R2 succeeds, the first mandatory regression is quotient nonzero-ness. Norm/divisor/residue checks alone are insufficient.
- R3 must use the actual corrected representative. No relabeling of branch orbit `(1,0)` as marked Brauer `[1,0]` is allowed.
- R4 reads the fixed marked coordinate only through the retained kernel-lattice fingerprints: minimum norm `4 -> [0,1]`, `8 -> [1,0]`, `12 -> [1,1]`.
- Class-3 routes remain dormant unless this finite repair ladder reaches a new exact no-go after the representative issue is resolved.

## User-visible stuckness rule

Every future `Stage33-main-batch` working in this band must report exactly:

`33-05 repair: R?/R5 | state | attempts on current leaf | exact new information | next exit test`

A batch that does not change the current leaf, candidate set, exact invariant, or missing interface increments the current-leaf stagnation count. Two such consecutive batches trigger a route audit rather than another same-form attempt.

## Current authoritative snapshot

```text
R0 = DONE: current promoted ell_J2 is zero in geometric CV quotient
R1 = DONE: abstract J2 nonzero independently reconfirmed
R2 = IN_PROGRESS: construct corrected representative; quotient nonzero is first gate
R3 = BLOCKED
R4 = BLOCKED
R5 = BLOCKED
Stage33 progress = 5/11
Stage33-12 exact closure = false
Stage33-13 release = false
class3 promoted = false
```

Hostile-reopen evidence:
`stages/stage33/33-12/j2-cv-lclass-zero-regression.json`

R1 evidence:
`stages/stage33/33-05/j2-abstract-nonzero-reaudit.json`

Machine-readable repair state:
`stages/stage33/33-05/j2-representative-repair-state.json`
