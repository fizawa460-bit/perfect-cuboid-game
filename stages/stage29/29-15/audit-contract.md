# Stage29-15 — adversarial audit contract

Audit the endpoint Arsenal rematch independently. The audit must test **both** theorem matching and the mandatory OPEN-receiver execution triage. A PASS is forbidden while any receiver that should be class 1 remains unexecuted.

## 1. Reconstruct the authoritative receiver surface

Re-read the final audited states of 29-05 through 29-14, especially 29-10/11/12, Gap Scan C, 29-13 and 29-14. Do not trust the submitted list merely because it is machine-readable.

Confirm the parent baseline unless fresh evidence changes it:

```text
ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
```

Reconstruct every still-live named child receiver, later execution-owner transfer, later-created receiver (`KUM-LOC2-2`, `KUM-LOC3`, `PESCH-E1`, `PESCH2`, `FIB1`, `FIB2`, external A-E dispositions), and the terminal `P/M3` frontier. Check for omitted or duplicate residual work.

## 2. Mandatory four-class rule — highest-priority audit

Every residual receiver/frontier must have exactly one class:

```text
1 EXECUTE_NOW_BOUNDED
2 CURRENT_TOOL_LIMIT_EXECUTED
3 NEW_THEOREM_REQUIRED
4 DORMANT_NONDECISIVE
```

Use these semantics strictly.

### Class 1
Finite/bounded, tractable from current exact data/tools, and endpoint-decisive or route-enabling. It must be executed inside 29-15.

```text
CLASS1_PENDING_COUNT must equal 0 for PASS.
```

If audit finds any submitted class 2/3/4 receiver that is actually class 1, **execute it on this same PR**, record the proof/computation, update all ledgers, and re-audit. Do not defer it to 29-16.

### Class 2
A real execution/feasibility/model attempt has reached the current tool boundary. The ledger must identify the exact missing matrix, model, implementation, CAS certificate, or dependency. Merely saying `adapter missing` is insufficient.

For theoretically finite receivers such as `R29-LG2`, verify that the repository genuinely performed the feasibility reduction and that current brute force is not being mislabeled as a theorem gate. If a modest bounded implementation now makes it tractable, promote to class 1 and execute now.

### Class 3
The first missing statement is genuinely uniform/infinite/global or conjectural theorem input. A large finite computation, missing explicit model, or ordinary implementation gap must not be disguised as `NEW_THEOREM_REQUIRED`.

In particular independently verify that `R29-EXT-CHANG-C` belongs here: its finite windows are already executed, while its unresolved all-multiples continuation explicitly requires a new effective primitive-divisor theorem.

### Class 4
Even a complete solution has no current endpoint-decision or route-enabling consequence. Every class-4 entry must state an explicit reactivation trigger. Mathematical finiteness alone does not override nondecisiveness.

Audit the submitted totals rather than assuming them:

```text
RECEIVER_OR_TERMINAL_FRONTIER_COUNT=44
CLASS1_IDENTIFIED_COUNT=4
CLASS1_EXECUTED_COUNT=4
CLASS1_PENDING_COUNT=0
CLASS2_COUNT=14
CLASS3_COUNT=10
CLASS4_COUNT=16
VAGUE_AMBER_WITHOUT_EXECUTION_CLASS_COUNT=0
```

The authoritative submitted classification is `open-receiver-triage.json`.

## 3. Hostile audit of class-1 execution: R29-BEAU2A

Independently verify the Stage29-02d Beauville tower and the finite group argument.

For `Gamma=(Z/2)^2`, check that the deck group of

```text
X_B=(C0 x C0)/Delta(Gamma) -> D x D
```

is `(Gamma x Gamma)/Delta(Gamma) ~= Gamma`, and under factor exchange the quotient element is inverted. Since `Gamma` has exponent two, verify inversion is identity.

Then check Albanese functoriality gives the corresponding swap action on `A_B -> J_D x J_D`, so the V4 isogeny kernel is swap-stable and the Q(i)/Q swap twist descends as claimed.

Only then accept

```text
R29-BEAU2A=DISCHARGED_SWAP_EQUIVARIANT_V4_KERNEL.
```

Do not promote this to a finite twist set, uniform Selmer theorem, or endpoint obstruction.

## 4. Hostile audit of class-1 execution: exact p=2 density

Independently rederive `R29-KUM-LOC2-2`.

For

```text
x,y,z,x+y,x+z,y+z,x+y+z
```

verify:

1. `P^2(F_2)` has seven equal primitive parity cylinders.
2. Cylinders with at least two odd coordinates fail the common Q2-squareclass condition.
3. In a unique-odd chart, normalize the odd coordinate to 1 and take `X,Z` independently in `2Z_2`.
4. `X` and `1+X` are Q2-squares exactly when `v2(X)=2a`, `a>=2`, with odd unit `1 mod 8`.
5. The conditional state mass is `w_a=2^(-2a-2)` and `sum w_a=1/48`.
6. `X+Z` fails exactly when `|a-b|<=1`.
7. Equal and adjacent masses are `1/3840` and `1/7680`.
8. One-cylinder success mass is `1/23040`.
9. Therefore

```text
Delta_2=(3/7)*(1/23040)=1/53760.
```

Check measure-zero branch hyperplanes separately. Verify `[44^2:117^2:240^2]` is consistent with the accepted state but is not a rational perfect cuboid.

Only then accept

```text
R29-KUM-LOC2-2=DISCHARGED_EXACT_TWO_ADIC_STATE_DENSITY.
```

No global Euler product or population saving follows; `R29-KUM-LOC3` remains separate.

## 5. Hostile audit of class-1 execution: R29-MOD1C

Re-read Stage29-02g's exact conjugate-self level-4 datum and K8 checker.

Verify

```text
K8=ker(SL2(Z/8)->SL2(Z/4))={I+4A : A in sl2(F2)}, |K8|=8.
```

The retained conjugate-self level-4 sign matrix is `D=diag(1,-1) mod 4`. Prove that every mod-8 lift `M` of this datum has `M mod 2=I`, and therefore for every `I+4A in K8`

```text
M(I+4A)M^-1 = I+4A mod 8.
```

Check the exact finite enumeration in `verify_bounded_execution.py`. Since K8 is abelian, verify that the resulting sigma-twisted conjugacy relation on the **marked** datum is equality.

Only then accept

```text
R29-MOD1C=DISCHARGED_TRIVIAL_SIGMA_ACTION_ON_K8
MARKED_ARITHMETIC_DEFECT_CLASS_COUNT=8.
```

Do not confuse this with the four ordinary `1,3,3,1` unmarked symplectic conjugacy classes, and do not infer any defect class is impossible.

## 6. Hostile audit of class-1 execution: R29-MOD1D

Check the exact Testa--Stoll `X(8)` model

```text
u^2=xy,
v^2=x^2-y^2,
w^2=x^2+y^2.
```

Verify that the 24 cusps lie over the six base branch values `0,infinity,+/-1,+/-i`, equivalently on `uvw=0`, and that the `G0~=(Z/2)^3` sign action is free where `uvw!=0`.

Then verify the cuboid quotient invariants

```text
U=u1*u2=2*b1,
V=v1*v2=2*b2,
W=w1*w2=2*b3.
```

Since the physical endpoint has nonzero face diagonals, prove that every physical endpoint preimage has both X(8) factors noncuspidal and no nontrivial G0 stabilizer.

Only then accept

```text
R29-MOD1D=DISCHARGED_PHYSICAL_OPEN_NONCUSP_STABILIZER_FREE.
```

This does not automatically close the compactification receiver `R29-MOD2B`.

## 7. Full endpoint surface Chabauty

Verify `q(S)=0`, hence `Alb(S)=0`, and the Albanese universal-property argument. Read the exact hypotheses of Caro--Pasten and Balakrishnan--Caro. If their surface theorem does not require the abelian embedding claimed by the submission, repair the disposition.

Only if the chain survives accept

```text
R29_ARS_SURFACE_CHABAUTY=NONAPPLICABLE_TO_FULL_ENDPOINT_BY_ALBANESE_ZERO.
```

This does not extend automatically to curves or irregular auxiliary covers.

## 8. Class-2 hostile checks

For every class-2 entry verify meaningful work was actually done and the named current limit is real.

In particular:

- `LG2/LG2-EFF/LG2-MB`: inspect Stage29-02c-LG2 computational feasibility. If bounded symmetry reduction now makes the 176/192 program tractable, promote and execute.
- `BEAU1B/1C`: test whether existing Beauville/Q-descent equations already suffice for an explicit squareclass function `F` and divisor. If yes, execute.
- `KUM5`: check whether 29-06..15 supplied the missing arrangement/modular action-cocycle identification. Abstract `S4 ~= S4` is never enough.
- `BR0A/B/G`, `BR2A/B`, `NF-PHYS2`: determine whether the 72 boundary classes, Picard basis and intersections already materialize the finite matrices. If yes, compute them now.
- `EXT-CHANG-E`: check whether explicit integrality-preserving birational maps plus a certified complete integral-point computation now exist. If bounded certification is possible, execute.

## 9. Class-3 hostile checks

Confirm each really needs theorem-level input rather than unfinished finite work. At minimum inspect:

```text
R29-PI1-OPEN
R29-CAMP2
R29-BEAU2
R29-BEAU3
R29-QWEB-CLIFFORD
R29-KUM-LOC3
R29-PESCH-E1
R29-FIB2
R29-EXT-CHANG-C
TERMINAL-P-OVER-M3.
```

Search current literature for an exact theorem that closes any of them. A concrete match must be applied in 29-15; search absence is not a novelty claim.

## 10. Class-4 hostile checks

Verify nondecisiveness, not merely inconvenience. In particular test:

```text
R29-G1b-EXC
R29-X1
R29-CAMP3
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

## 11. StructureRadar / Arsenal rematch

Read at least:

```text
docs/stage14-arsenal.md
docs/structure-radar/arsenal/SR-ARSENAL-24.md
docs/structure-radar/arsenal/SR-ARSENAL-25.md
docs/structure-radar/PAUSE_AND_RETURN_STAGE27_2026-08-20.md
```

Determine whether Stage29-06..15 supplied an adapter absent when a StructureRadar card was classified `EXTERNAL_GATE`. If yes, reopen only the exact endpoint receiver and test the theorem now.

Check curve Chabauty/MW-sieve, K3 Brauer, Campedelli, Beauville twist, modular/8-congruence, physical-open Brauer, local/sieve and parametric theorem ecosystems. Do not re-credit already-consumed Stage14/29-08/11/12/13/14 results.

## 12. Population firewall

Recheck Stage14/29-12 identities and current M3 information. No inference may assert

```text
P/(M2+M3)->0  =>  P/M3->0
```

or convert endpoint density zero on a larger host into emptiness.

`P(B)/M3(B)` remains unknown unless a genuinely new theorem is proved.

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
R29_MOD1C=<audited disposition>
MARKED_ARITHMETIC_DEFECT_CLASS_COUNT=<integer or INVALID>
R29_MOD1D=<audited disposition>
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

If the submission survives, only classes 2/3/4 may pass to `29-16_RESIDUAL_RECEIVER_COMPRESSION_AND_ROUTE_PORTFOLIO`.
