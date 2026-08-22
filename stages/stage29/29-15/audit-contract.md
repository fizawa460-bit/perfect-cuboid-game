# Stage29-15 — adversarial audit contract

Audit the endpoint Arsenal rematch independently. The audit must now test **both** theorem matching and the mandatory OPEN-receiver execution triage. A PASS is forbidden while any receiver that should be class 1 remains unexecuted.

## 1. Reconstruct the authoritative receiver surface

Re-read the final audited states of 29-05 through 29-14, especially 29-10/11/12, Gap Scan C, 29-13 and 29-14. Do not trust the submitted list merely because it is machine-readable.

Confirm the parent baseline:

```text
ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
```

Then reconstruct every still-live named child receiver, all later execution-owner transfers, later-created receivers (`KUM-LOC2-2`, `KUM-LOC3`, `PESCH-E1`, `PESCH2`, `FIB1`, `FIB2`, external A-E dispositions), and the literal terminal `P/M3` frontier. Check for omitted or duplicate residual work.

## 2. Mandatory four-class rule — highest-priority audit

Every residual receiver/frontier must have exactly one class:

```text
1 EXECUTE_NOW_BOUNDED
2 CURRENT_TOOL_LIMIT_EXECUTED
3 NEW_THEOREM_REQUIRED
4 DORMANT_NONDECISIVE
```

Use these semantics strictly:

### Class 1
Finite/bounded, tractable from current exact data/tools, and endpoint-decisive or route-enabling. It must be executed inside 29-15.

```text
CLASS1_PENDING_COUNT must equal 0 for PASS.
```

If audit finds any submitted class 2/3/4 receiver that is actually class 1, **execute it on this same PR**, record the proof/computation, update all ledgers, and re-audit the result. Do not defer it to 29-16.

### Class 2
A real execution/feasibility/model attempt has already reached the current tool boundary. The ledger must identify the exact missing matrix, model, implementation, CAS certificate, or dependency. Merely saying `adapter missing` is insufficient.

For theoretically finite receivers such as `R29-LG2`, verify that the repository genuinely performed the feasibility reduction and that current brute force is not being mislabeled as a theorem gate. If the task is tractable after a modest bounded implementation, promote it to class 1 and execute it.

### Class 3
The first missing statement is genuinely uniform/infinite/global or conjectural theorem input. A large finite computation, missing explicit model, or ordinary implementation gap must not be disguised as `NEW_THEOREM_REQUIRED`.

### Class 4
Even a complete solution of that receiver has no current endpoint-decision or route-enabling consequence. Every class-4 entry must state an explicit reactivation trigger. Mathematical finiteness alone does not override nondecisiveness.

Audit the submitted totals rather than assuming them:

```text
RECEIVER_OR_TERMINAL_FRONTIER_COUNT=44
CLASS1_IDENTIFIED_COUNT=2
CLASS1_EXECUTED_COUNT=2
CLASS1_PENDING_COUNT=0
CLASS2_COUNT=16
CLASS3_COUNT=9
CLASS4_COUNT=17
VAGUE_AMBER_WITHOUT_EXECUTION_CLASS_COUNT=0
```

The authoritative submitted classification is `open-receiver-triage.json`.

## 3. Hostile audit of class-1 execution: R29-BEAU2A

Independently verify the Stage29-02d Beauville tower and the new finite group argument.

For `Gamma=(Z/2)^2`, check that the deck group of

```text
X_B=(C0 x C0)/Delta(Gamma) -> D x D
```

is `(Gamma x Gamma)/Delta(Gamma) ~= Gamma`, and under factor exchange the quotient element is inverted. Since `Gamma` has exponent two, verify that inversion is identity.

Then check that Albanese functoriality gives the corresponding swap action on `A_B -> J_D x J_D`, so the V4 isogeny kernel is swap-stable and the Q(i)/Q swap twist descends as claimed.

Only then accept

```text
R29-BEAU2A=DISCHARGED_SWAP_EQUIVARIANT_V4_KERNEL.
```

Do not promote this to a finite twist set, uniform Selmer theorem, or endpoint obstruction.

## 4. Hostile audit of class-1 execution: exact p=2 density

Independently rederive `R29-KUM-LOC2-2` rather than accepting the geometric series.

For the seven forms

```text
x,y,z,x+y,x+z,y+z,x+y+z
```

verify:

1. `P^2(F_2)` has seven equal primitive parity cylinders under the normalized projective Haar measure.
2. Any cylinder with at least two odd coordinates fails the common Q2-squareclass condition.
3. In a unique-odd chart, after scaling the odd coordinate to 1, `X,Z` are independent normalized Haar variables in `2Z_2`.
4. `X` and `1+X` are both Q2-squares exactly when `v2(X)=2a`, `a>=2`, and the odd unit is `1 mod 8`.
5. The conditional state mass is `w_a=2^(-2a-2)` and `sum w_a=1/48`.
6. For qualifying X,Z, `X+Z` fails exactly when `|a-b|<=1`.
7. The equal and adjacent masses are `1/3840` and `1/7680`.
8. The one-cylinder success mass is `1/23040`.
9. The final normalized density is

```text
Delta_2=(3/7)*(1/23040)=1/53760.
```

Check measure-zero branch hyperplanes separately. Verify the known local point `[44^2:117^2:240^2]` is consistent with the accepted state but is not used as a global perfect-cuboid point.

Run or independently reproduce `verify_bounded_execution.py`.

Only then accept

```text
R29-KUM-LOC2-2=DISCHARGED_EXACT_TWO_ADIC_STATE_DENSITY.
```

Do not infer a global Euler product or population saving; `R29-KUM-LOC3` remains separate.

## 5. Full endpoint surface Chabauty

Verify `q(S)=0`, hence `Alb(S)=0`, and the Albanese universal-property argument. Read the exact hypotheses of Caro--Pasten and Balakrishnan--Caro. If their surface theorem does not require the abelian embedding claimed by the submission, repair the disposition.

Only if the chain survives accept

```text
R29_ARS_SURFACE_CHABAUTY=NONAPPLICABLE_TO_FULL_ENDPOINT_BY_ALBANESE_ZERO.
```

This nonapplicability does not extend automatically to curves or irregular auxiliary covers.

## 6. Class-2 hostile checks

For every class-2 entry, verify that meaningful work was actually done and that the named current limit is real.

In particular:

- `LG2/LG2-EFF/LG2-MB`: read Stage29-02c-LG2 computational feasibility and determine whether a bounded symmetry reduction now makes the 176/192 program actually tractable. If yes, promote to class 1 and run it now.
- `BEAU1B/1C`: check whether existing Beauville/Q-descent equations already suffice to eliminate to an explicit squareclass function `F`. If a bounded elimination is now possible, execute it.
- `MOD1C/KUM5`: check whether 29-06..14 supplied the missing action/cocycle data. Abstract `S4 ~= S4` is never enough.
- `BR0A/B/G`, `BR2A/B`, `NF-PHYS2`: check whether the 72 boundary classes, Picard basis and intersection data already materialize the required finite matrices. If they do, compute them now.
- `EXT-CHANG-E`: verify whether a current explicit birational map plus a certified complete integral-point computation has appeared. If the bounded certification can now be completed, execute it rather than preserving class 2.

## 7. Class-3 hostile checks

Confirm each entry really needs theorem-level input rather than unfinished finite work. At minimum inspect:

```text
R29-PI1-OPEN
R29-CAMP2
R29-BEAU2
R29-BEAU3
R29-QWEB-CLIFFORD
R29-KUM-LOC3
R29-PESCH-E1
R29-FIB2
TERMINAL-P-OVER-M3.
```

Search current literature for an exact theorem that closes any of them. A concrete match must be applied in 29-15; search absence is not a novelty claim.

## 8. Class-4 hostile checks

Verify nondecisiveness, not merely inconvenience. In particular test the submission's dormancy of:

```text
R29-G1b-EXC
R29-X1
R29-CAMP3
R29-MOD1D
R29-MOD2B
R29-NF7
R29-L2-ALG
R29-L2-BAD
R29-PESCH2
R29-FIB1
R29-TERA1
R29-NF1QISO
R29-NF3..NF6
R29-EXT-CHANG-D.
```

If completing one would immediately enable an already-available decisive theorem, it is not class 4; reclassify and execute/route correctly.

## 9. StructureRadar / Arsenal rematch

Read at least:

```text
docs/stage14-arsenal.md
docs/structure-radar/arsenal/SR-ARSENAL-24.md
docs/structure-radar/arsenal/SR-ARSENAL-25.md
docs/structure-radar/PAUSE_AND_RETURN_STAGE27_2026-08-20.md
```

Determine whether Stage29-06..14 supplied an adapter absent when a StructureRadar card was classified `EXTERNAL_GATE`. If yes, reopen only the exact endpoint receiver and test the theorem now.

Check curve Chabauty/MW-sieve, K3 Brauer, Campedelli, Beauville twist, modular/8-congruence, physical-open Brauer, local/sieve and parametric theorem ecosystems. Do not re-credit already-consumed Stage14/29-08/11/12/13/14 results.

## 10. Population firewall

Recheck the exact Stage14/29-12 identities and the current M3 information. No current inference may assert

```text
P/(M2+M3)->0  =>  P/M3->0
```

or convert endpoint density zero on a larger host into emptiness.

The literal `P(B)/M3(B)` frontier must remain unknown unless a genuinely new theorem is proved.

## Required audit output

Create `stages/stage29/29-15/audit.md`. Repair this same PR if needed.

```text
AUDIT_VERDICT=PASS|PASS_AFTER_REPAIR|FAIL
ARSENAL_REMATCH_COMPLETE=true|false
OPEN_RECEIVER_TRIAGE_COMPLETE=true|false
RECEIVER_OR_TERMINAL_FRONTIER_COUNT=<integer>
CLASS1_IDENTIFIED_COUNT=<integer>
CLASS1_EXECUTED_COUNT=<integer>
CLASS1_PENDING_COUNT=<integer>
CLASS2_COUNT=<integer>
CLASS3_COUNT=<integer>
CLASS4_COUNT=<integer>
VAGUE_AMBER_WITHOUT_EXECUTION_CLASS_COUNT=<integer>
R29_BEAU2A=<audited disposition>
R29_KUM_LOC2_2=<audited disposition>
DELTA_2=<audited value or INVALID>
R29_ARS_SURFACE_CHABAUTY=<audited disposition>
NEW_DECISIVE_GLOBAL_THEOREM_FOUND=true|false
NEW_OPEN_RECEIVER_DISCHARGED_COUNT=<integer>
NEW_EXACT_NONAPPLICABILITY_CERTIFICATE_COUNT=<integer>
ATTACK_ROUTE_COUNT=<integer>
GREEN_ROUTE_COUNT=<integer>
AMBER_ROUTE_COUNT=<integer>
P_OVER_M3_SCALE_KNOWN=true|false
TARGETED_BACKFLOW_REQUIRED=true|false
ROADMAP_REWRITE_REQUIRED=true|false
MERGE_ALLOWED=true|false
ADVANCE_ALLOWED=true|false
NEXT_ITEM=<item or blocker>
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

A PASS requires

```text
CLASS1_PENDING_COUNT=0
VAGUE_AMBER_WITHOUT_EXECUTION_CLASS_COUNT=0.
```

If the submission survives, only classes 2/3/4 may pass to

```text
29-16_RESIDUAL_RECEIVER_COMPRESSION_AND_ROUTE_PORTFOLIO.
```
