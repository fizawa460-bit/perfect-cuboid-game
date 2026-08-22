# Stage29-15 fresh adversarial audit

```text
AUDITED_PR=1323
AUDITED_SUBMISSION_HEAD=e8ab2d39ceb35fa9aecf4037f3ce0012b90782f6
AUDIT_VERDICT=PASS_AFTER_MATERIAL_POSITIVE_REPAIR
MATERIAL_POSITIVE_REPAIR=ADDITIONAL_BEAU1B_CLASS1_EXECUTION_PLUS_BEAU1C_RECLASSIFICATION_PLUS_EXTERNAL_CLAIM_VETTING
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
```

## 1. Authoritative portfolio reconstruction

The audited 29-10/11/12 attack states plus 29-13/14 additions still reconstruct exactly

```text
ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
```

The sole GREEN parent remains `J12-POP-INTERACTION`. No density statement on `H_ge2` or the incidence hosts implies `P/M3 -> 0`, and no endpoint emptiness theorem is imported.

## 2. Submitted class-1 executions

All four submitted executions survive hostile audit.

### R29-BEAU2A

For `Gamma=(Z/2)^2`, the deck group `(Gamma x Gamma)/Delta(Gamma)` identifies with `Gamma`; factor exchange induces inversion, which is trivial because every element has exponent two. Albanese functoriality preserves the corresponding V4 isogeny kernel under the Q(i)/Q swap descent.

```text
R29-BEAU2A=DISCHARGED_SWAP_EQUIVARIANT_V4_KERNEL
```

### R29-KUM-LOC2-2

The seven parity cylinders in `P2(F2)` have equal mass, exactly three unique-odd cylinders survive, and in one such chart

```text
sum_a>=2 w_a=1/48,
equal valuation mass=1/3840,
adjacent valuation mass=1/7680.
```

Hence the conditional pair mass is `1/23040` and

```text
DELTA_2=(3/7)*(1/23040)=1/53760.
R29-KUM-LOC2-2=DISCHARGED_EXACT_TWO_ADIC_STATE_DENSITY.
```

This is local infrastructure only; `R29-KUM-LOC3` remains a global same-measure theorem gate.

### R29-MOD1C

The upstream marked datum gives `D=diag(1,-1) mod 4`. Every mod-8 lift is congruent to the identity mod 2, hence centralizes

```text
K8={I+4A : A in sl2(F2)}.
```

The exact finite checker enumerates all eight K8 elements and all relevant mod-8 lifts. Sigma transport is trivial on K8. Since K8 is abelian, marked sigma-twisted conjugacy is equality.

```text
R29-MOD1C=DISCHARGED_TRIVIAL_SIGMA_ACTION_ON_K8
MARKED_ARITHMETIC_DEFECT_CLASS_COUNT=8.
```

The ordinary unmarked orbit partition `1+3+3+1` remains a different quotient and no defect class is eliminated.

### R29-MOD1D

On Testa--Stoll's `X(8)` model the cusp locus is `uvw=0`; the G0 sign action is free off it. The cuboid invariants `u1u2=2b1`, `v1v2=2b2`, `w1w2=2b3` and physical `b1b2b3 != 0` force both factors to be noncuspidal and stabilizer-free.

```text
R29-MOD1D=DISCHARGED_PHYSICAL_OPEN_NONCUSP_STABILIZER_FREE.
```

## 3. Material audit discovery: a fifth class-1 receiver

The submission classified `R29-BEAU1B` as class 2, but the already-audited 29-02d product coordinates make the requested squareclass function elementary to construct. The full execution is recorded in `beauville-squareclass-execution.md`.

On `C0 x C0`, with

```text
r0=u0*v0*w0/x0^3,
r1=u1*v1*w1/x1^3,
s=r0+r1,
```

`s` is invariant under the diagonal even-sign group, anti-invariant under the canonical deck involution and symmetric under factor swap. It therefore descends as a Q-rational quadratic generator on the cuboid Q-form.

In Beauville invariant coordinates

```text
F_B=s^2
=[C(A^4-C^4)+B(A^4-B^4)+2UVW A^2]/A^5.
```

After the exact cuboid adapter this becomes

\[
\boxed{
F_{cub}=
\frac{2\left(y(x+t)^4-y^5+10y^3z^2-5yz^4+4uvw(x+t)^2\right)}{(x+t)^5}.
}
\]

The positive physical chamber has `x+t>0`, so every physical endpoint point lies in this chart. For such a rational point `P`, away from a zero of the chosen generator,

```text
delta(P)=F_cub(P) mod Q*^2.
```

Because the Beauville cover is quasi-etale and ramifies only above the 48 codimension-two nodes, every codimension-one valuation of `F_cub` is even. Thus

```text
R29-BEAU1B=DISCHARGED_EXPLICIT_Q_SQUARECLASS_FUNCTION_AND_CODIM1_PARITY.
```

Writing `L=x+t` and

```text
N=y*L^4-y^5+10*y^3*z^2-5*y*z^4+4*u*v*w*L^2,
```

the same class is `delta(P)=2LN mod Q*^2`. This gives the exact pointwise local ramification formula. The remaining part of `R29-BEAU1C` is now uniform/infinite-family arithmetic: control the support/reciprocity of `2LN` over every physical endpoint point strongly enough to reduce the infinite twist family. It is therefore reclassified from class 2 to class 3.

```text
R29-BEAU1C=NEW_THEOREM_REQUIRED_AFTER_EXACT_POINTWISE_RAMIFICATION_FORMULA.
```

## 4. Corrected execution-class census

No further class-1 receiver was found after rechecking the Stage14 Arsenal, StructureRadar batches 24/25 and pause boundary, 29-02ha/hb/hc/hd, the 29-02f open-Brauer implementation, and the later attack ledgers.

The authoritative audited census is

```text
RECEIVER_OR_TERMINAL_FRONTIER_COUNT=44
CLASS1_IDENTIFIED_COUNT=5
CLASS1_EXECUTED_COUNT=5
CLASS1_PENDING_COUNT=0
CLASS2_COUNT=12
CLASS3_COUNT=11
CLASS4_COUNT=16
VAGUE_AMBER_WITHOUT_EXECUTION_CLASS_COUNT=0.
```

The submitted `4/14/10/16` census is superseded by `audit-state.json`.

### Brauer class-2 scope repair

`R29-BR0A` remains class 2, but the submitted reason was too strong. `29-02f/boundary_module_probe.m` already contains a concrete Magma construction of the 72-component map `Div_D -> Pic`, its kernel and image. What is absent is a committed source-locked execution/output and the downstream saturation/cohomology materialization; the present connected environment does not provide Magma execution. Therefore it is a genuine current-tool execution wall, not a missing theorem and not an unimplemented idea. BR0B/G and BR2A/B remain downstream of this finite computation.

The LG2 rank-44 search remains class 2 for the audited feasibility reasons; no modest replacement enumerator appeared. KUM5 remains an action/cocycle model wall, not an abstract-group problem. `EXT-CHANG-E` remains uncertified after the prior source-level completeness attempt.

## 5. StructureRadar / Arsenal rematch

The exact-measure and moving-family gates in SR-ARSENAL-24/25 remain intact. Stage29 supplies additional endpoint models but not the missing same-measure coefficient separation, uniform moving-family small-point theorem, or global physical-height local-to-global theorem. No StructureRadar `EXTERNAL_GATE` becomes an executable endpoint theorem solely from the new Stage29 adapters.

Surface Chabauty remains exactly nonapplicable to the full smooth projective endpoint resolution: `q(S)=0`, so `Alb(S)=0`; a nonconstant embedding into an abelian variety is structurally impossible. This does not apply to irregular auxiliary covers or individual curves.

```text
R29-ARS-SURFACE-CHABAUTY=NONAPPLICABLE_TO_FULL_ENDPOINT_BY_ALBANESE_ZERO.
```

## 6. Fresh claimed-solution vetting

A fresh search located the 2026 self-published repository `AEjonanonymous/Non-existence-of-Perfect-Cuboids`. Its Lean file does not formalize the universal perfect-cuboid implication. The final theorem assumes a hand-defined torsion restriction `u in {0,1,-1}`, and the modular theorem assumes specific residue classes; neither hypothesis is derived from an arbitrary perfect cuboid in the formal file.

Therefore the Lean kernel verifies conditional lemmas, not a global endpoint theorem.

```text
R29-EXT-REED-2026=REJECTED_AS_GLOBAL_PROOF_MISSING_UNIVERSAL_ENDPOINT_REDUCTION
NEW_ENDPOINT_RECEIVER_CREATED=false.
```

The detailed source check is `external-claim-vetting.md`. This rejection is tracked separately from Arsenal theorem nonapplicability counts.

## 7. Final audit state

No new decisive whole-endpoint theorem was found. The audit does, however, discharge one additional bounded Beauville receiver and convert its dependent local receiver into a sharper theorem-level gate.

```text
ARSENAL_REMATCH_COMPLETE=true
OPEN_RECEIVER_TRIAGE_COMPLETE=true
NEW_DECISIVE_GLOBAL_THEOREM_FOUND=false
NEW_OPEN_RECEIVER_DISCHARGED_COUNT=5
NEW_EXACT_NONAPPLICABILITY_CERTIFICATE_COUNT=1
FRESH_EXTERNAL_CLAIM_REJECTION_COUNT=1
ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
TARGETED_BACKFLOW_REQUIRED=false
ROADMAP_REWRITE_REQUIRED=false
CLASS1_PENDING_COUNT=0
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-16_RESIDUAL_RECEIVER_COMPRESSION_AND_ROUTE_PORTFOLIO
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
