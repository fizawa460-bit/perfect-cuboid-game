# Stage29-12 adversarial audit contract

Audit this submission from the underlying theorem statements. Do not accept the proposed first GREEN route merely because the algebra looks plausible.

## 1. New population-interaction theorem — highest-priority hostile check

Re-read Stage14, Gap Scan B, 29-04 and 29-07 and determine whether the objects and cutoffs really match.

Verify or refute, object-for-object,

```text
Stage14 E(B) = Stage29 I2^S(B) = N2(B)+3P(B).
```

Check raw unordered two-face incidence multiplicity, primitive normalization, canonical ordering, integral-space condition and the `d=R` cutoff. A hidden ordered-pair or exact-two filter invalidates the proposed identification.

Then verify the asymptotic denominator:

```text
I2=M2+3M3,
M2~C_M2 B(log B)^5 with C_M2>0,
M3=o(M2),
```

and audit the claimed conclusion

```text
I2^S/I2 <<_epsilon B^(-1/2+epsilon)(log B)^(-5).
```

Separately verify

```text
H_ge2=M2 disjoint_union M3,
P subset H_ge2,
P/H_ge2 <<_epsilon B^(-1/2+epsilon)(log B)^(-5).
```

If both survive, decide independently whether `J12-POP-INTERACTION=GREEN` is justified under the existing route-color semantics. If GREEN is too strong, repair the color but keep any valid theorem.

Do not infer anything about `P/M3` from these ratios.

## 2. Double-charge audit

The new relative theorem may consume Stage14's endpoint/incidence upper bound, but it must not re-credit that old bound as new mathematics. New 29-12 credit, if any, is only the exact normalization onto the legal Stage29 incidence/nested hosts and the resulting relative-rate theorem.

Likewise:

```text
29-09 odd-prime exact local laws -> input only
29-08 Master-Hit global coverage -> input only
29-07 V4 geometry -> input only unless new joint information is proved
```

## 3. Joint-V4 route

Verify the residual cells

```text
M2-N2, N2, 3(M3-P), 3P
```

and attack whether any existing theorem actually controls a genuinely joint conditional such as `P/M3` or `3P/(N2+3P)`. If such a theorem exists, the AMBER classification is wrong.

Re-evaluate whether closing `R29-X1` has any current endpoint rational-point consequence. Do not promote a complete ADE ledger to an obstruction by itself.

## 4. Two-adic child

Check the proposed point

```text
[x:y:z]=[44^2:117^2:240^2]
```

and all seven values exactly. Verify that each is a nonzero Q2-square, including `x+y+z=73225` via the odd-unit square criterion.

Then verify the topology step: simultaneous squareclass conditions are locally constant away from zeros because `Q2^{*2}` is open. If valid, accept only

```text
R29-KUM-LOC2-2A=DISCHARGED_POSITIVE_Q2_LIFT_CYLINDER
```

and keep the exact Q2 density/state automaton parent open. Positive local measure is not a global point theorem.

## 5. Local-to-global route

Recheck that `Delta_p=1/64+O(1/p)` is on the full endpoint P2(Qp) host and that Stage19/20 marginal laws are on different selected hosts. No multiplication is permitted without `R29-KUM-LOC3`.

Search the repo for any already-proved physical-height equidistribution/large-sieve adapter that would close LOC3. If found, repair materially; otherwise keep AMBER.

## 6. Parametric route

Reverify global primitive Euler-brick / endpoint coverage by Master-Hits and do not replay it as new credit. Determine whether `R29-PESCH-E1` has become a theorem since 29-08 anywhere in the repo/source locks. If not, keep it conjectural.

Check whether bounded Mordell-Weil enumeration or a parameter-height comparison is sufficient for global endpoint coverage. Do not infer this from geometric fibration coverage.

## 7. Route colors / ownership

Reclassify independently:

```text
J12-JOINT-V4
J12-LOCAL-SQUARECLASS
J12-PARAMETRIC
J12-POP-INTERACTION
```

as GREEN/AMBER/RED/MERGED. Preserve the total route count 11 unless a genuinely new primary mechanism appears.

A GREEN classification must name a new certified theorem produced in this attack stage and state its exact endpoint consequence. It need not be a nonexistence theorem, but density-zero language must remain separate from emptiness.

## Required output

Create `stages/stage29/29-12/audit.md` and repair this same PR branch if necessary.

```text
AUDIT_VERDICT=PASS|PASS_AFTER_REPAIR|FAIL
J12_JOINT_V4=GREEN|AMBER|RED|MERGED
J12_LOCAL_SQUARECLASS=GREEN|AMBER|RED|MERGED
J12_PARAMETRIC=GREEN|AMBER|RED|MERGED
J12_POP_INTERACTION=GREEN|AMBER|RED|MERGED
R29_POP_I2S=<audited disposition>
R29_POP_H2=<audited disposition>
R29_KUM_LOC2_2A=<audited disposition>
R29_KUM_LOC2_2=<audited disposition>
R29_KUM_LOC3=<audited disposition>
R29_PESCH_E1=<audited disposition>
P_OVER_M3_SCALE_KNOWN=true|false
ATTACK_ROUTE_COUNT=<integer>
TARGETED_BACKFLOW_REQUIRED=true|false
ROADMAP_REWRITE_REQUIRED=true|false
MERGE_ALLOWED=true|false
ADVANCE_ALLOWED=true|false
NEXT_ITEM=<item or blocker>
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

If the audit passes, expected next item is `GAP_SCAN_C_ROADMAP_REVIEW_C`.
