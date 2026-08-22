# Stage29-15 — ENDPOINT_ARSENAL_REMATCH + mandatory OPEN-receiver execution triage

```text
STAGE=Stage29
ITEM=29-15_ENDPOINT_ARSENAL_REMATCH
STATUS=AUDITED_PASS_AFTER_MATERIAL_POSITIVE_REPAIR
BASE_MAIN_SHA=469996b93fe93650423fb2b4d629f67b1a2998b9
ATTACK_ROUTE_COUNT_RETAINED=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
NEW_DECISIVE_GLOBAL_THEOREM_FOUND=false
NEW_OPEN_RECEIVER_DISCHARGED_COUNT=5
NEW_EXACT_NONAPPLICABILITY_CERTIFICATE_COUNT=1
FRESH_EXTERNAL_CLAIM_REJECTION_COUNT=1
P_OVER_M3_SCALE_KNOWN=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Purpose and audited four-class rule

29-15 rematches the Stage14 Arsenal, StructureRadar corpus, Stage14--28 tools, A2 method species, the 29-02 theorem ecosystems, and current literature against the exact endpoint receivers surviving 29-10 through 29-14.

Every current OPEN residual receiver and the literal terminal frontier is forced into exactly one execution class:

```text
1 EXECUTE_NOW_BOUNDED
2 CURRENT_TOOL_LIMIT_EXECUTED
3 NEW_THEOREM_REQUIRED
4 DORMANT_NONDECISIVE
```

Fresh audit found one extra class-1 receiver beyond the submitted four and executed it on this branch. The authoritative audited state is `audit-state.json`; the submitted `open-receiver-triage.json` remains the submission snapshot and is superseded only in the explicitly repaired rows.

```text
RECEIVER_OR_TERMINAL_FRONTIER_COUNT=44
CLASS1_IDENTIFIED_COUNT=5
CLASS1_EXECUTED_COUNT=5
CLASS1_PENDING_COUNT=0
CLASS2_COUNT=12
CLASS3_COUNT=11
CLASS4_COUNT=16
VAGUE_AMBER_WITHOUT_EXECUTION_CLASS_COUNT=0
```

## 2. Submitted class-1 execution A — Beauville V4 kernel

For `Gamma=(Z/2)^2`, the deck group of

```text
(C0 x C0)/Delta(Gamma) -> (C0/Gamma) x (C0/Gamma)
```

is `(Gamma x Gamma)/Delta(Gamma) ~= Gamma`. Factor exchange acts by inversion; since `Gamma` has exponent two, inversion is trivial. Albanese functoriality therefore preserves the corresponding V4 isogeny kernel under the Q(i)/Q swap descent.

```text
R29-BEAU2A=DISCHARGED_SWAP_EQUIVARIANT_V4_KERNEL
```

This is an adapter closure only. The infinite physical twist problem remains.

## 3. Submitted class-1 execution B — exact p=2 local density

For the seven forms

```text
x,y,z,x+y,x+z,y+z,x+y+z
```

only the three mod-2 projective cylinders with a unique odd coordinate can satisfy the common Q2-squareclass condition. In one surviving chart, the two even affine ratios have states

```text
v2(X)=2a, a>=2,
odd-unit(X)=1 mod 8,
w_a=2^(-2a-2),
sum w_a=1/48.
```

The correlated `X+Z` condition fails exactly for equal or adjacent half-valuations. Thus

```text
one-cylinder success
 = (1/48)^2 - 1/3840 - 1/7680
 = 1/23040,
```

and

```text
Delta_2=(3/7)*(1/23040)=1/53760.
```

Therefore

```text
R29-KUM-LOC2-2=DISCHARGED_EXACT_TWO_ADIC_STATE_DENSITY
DELTA_2=1/53760.
```

Together with the already-audited odd-prime and real-place work, the local-place arithmetic is complete as infrastructure. The global physical-height/measure transfer `R29-KUM-LOC3` remains theorem-level.

## 4. Submitted class-1 execution C — exact sigma action on the modular K8 defect

29-02g proved

```text
K8=ker(SL2(Z/8)->SL2(Z/4))={I+4A : A in sl2(F2)},
|K8|=8,
```

and the ordinary unmarked conjugacy orbit sizes `1,3,3,1`, but left `R29-MOD1C` for the sigma-twisted retained-level-4 action.

The retained sign datum is `D=diag(1,-1) mod 4`. Every mod-8 lift `M` of it is congruent to `I` modulo 2, so for every `I+4A in K8`

```text
M(I+4A)M^-1 = I+4A mod 8.
```

Hence sigma transport acts trivially on K8. Because K8 is abelian, sigma-twisted conjugacy on the marked datum is equality.

```text
R29-MOD1C=DISCHARGED_TRIVIAL_SIGMA_ACTION_ON_K8
MARKED_ARITHMETIC_DEFECT_CLASS_COUNT=8
ORDINARY_UNMARKED_CONJUGACY_CLASS_COUNT=4.
```

No defect class is eliminated. The result sharpens the modular route to eight exact marked defect cases.

## 5. Submitted class-1 execution D — physical modular noncusp/stabilizer removal

The Testa--Stoll `X(8)` model is

```text
u^2=xy,
v^2=x^2-y^2,
w^2=x^2+y^2.
```

Its 24 cusps lie over `0,infinity,+/-1,+/-i`, equivalently on `uvw=0`. `G0~=(Z/2)^3` acts by sign changes of `u,v,w` and is free off that locus.

In the cuboid diagonal quotient,

```text
U=u1*u2=2*b1,
V=v1*v2=2*b2,
W=w1*w2=2*b3.
```

A physical endpoint has `b1*b2*b3!=0`; hence both X(8) factors are noncuspidal and no nontrivial G0 stabilizer survives.

```text
R29-MOD1D=DISCHARGED_PHYSICAL_OPEN_NONCUSP_STABILIZER_FREE.
```

`R29-MOD2B` remains dormant unless a future arithmetic theorem needs compactified boundary extension.

## 6. Audit-found class-1 execution E — explicit Beauville squareclass

The submitted triage placed `R29-BEAU1B` in class 2. Fresh audit reconstructs it directly from the already-audited Beauville product coordinates.

On `C0 x C0`, define

```text
r0=u0*v0*w0/x0^3,
r1=u1*v1*w1/x1^3,
s=r0+r1.
```

`s` is invariant under the diagonal even-sign group, anti-invariant under the canonical deck involution, and symmetric under factor swap. It therefore descends to a Q-rational quadratic generator on the cuboid Q-form. In standard cuboid coordinates,

\[
\boxed{
F_{cub}=s^2=
\frac{2\left(y(x+t)^4-y^5+10y^3z^2-5yz^4+4uvw(x+t)^2\right)}{(x+t)^5}.
}
\]

The physical positive chamber has `x+t>0`. Away from a zero of the chosen generator,

```text
delta(P)=F_cub(P) mod Q*^2.
```

The cover is quasi-etale with ramification only over the 48 codimension-two nodes, so every codimension-one valuation of `F_cub` is even.

```text
R29-BEAU1B=DISCHARGED_EXPLICIT_Q_SQUARECLASS_FUNCTION_AND_CODIM1_PARITY.
```

Writing `L=x+t` and

```text
N=y*L^4-y^5+10*y^3*z^2-5*y*z^4+4*u*v*w*L^2,
```

the torsor class is `delta(P)=2LN mod Q*^2`. This gives the exact pointwise ramification formula. Consequently the remaining `R29-BEAU1C` is no longer finite model work: it asks for a uniform theorem controlling the support/reciprocity of these point-dependent classes over every physical endpoint point.

```text
R29-BEAU1C=class 3 NEW_THEOREM_REQUIRED_AFTER_EXACT_POINTWISE_RAMIFICATION_FORMULA.
```

Full execution record: `beauville-squareclass-execution.md`.

## 7. Whole endpoint theorem rematch

The strongest certified whole-endpoint count remains the already-consumed Stage14 consequence

```text
P(B)<<_epsilon B^(1/2+epsilon).
```

The resolved endpoint surface has `q(S)=0`, hence `Alb(S)=0`. Every morphism from smooth projective `S` to an abelian variety factors through its Albanese, so the full endpoint surface cannot satisfy the abelian-embedding hypothesis of the Caro--Pasten surface Chabauty--Coleman method or the Balakrishnan--Caro refinement.

```text
R29-ARS-SURFACE-CHABAUTY=NONAPPLICABLE_TO_FULL_ENDPOINT_BY_ALBANESE_ZERO.
```

This does not rule out Chabauty on curves or irregular auxiliary covers. `R29-PI1-OPEN` remains class 3: no effective cuboid-open nonabelian/Chabauty--Kim theorem is certified.

## 8. Low-genus, quotient and Brauer receivers after audit triage

Rank-zero quotient enumeration, classical/elliptic/quadratic Chabauty and Mordell--Weil sieves remain useful after a concrete Q-defined curve and reconstruction map exist. The full `d<=176/192` Picard program is mathematically finite, but the 29-02c-LG2 feasibility audit records rank-44 close-vector growth and no symmetry-reduced effectivity-aware production enumerator. Thus `R29-LG2/LG2-EFF/LG2-MB` remain class 2.

Campedelli: `R29-CAMP2` is class 3 because its H-torsor problem is infinite without a uniform finite ramification/Selmer theorem; `R29-CAMP3` is class 4 because the remaining finite Q-form/type ledger alone has no current endpoint consequence; `R29-CAMP4` is class 2 finite model work.

Beauville gains both `BEAU2A` and the audit-found `BEAU1B` closure. `BEAU1C`, `BEAU2` and `BEAU3` are theorem-level because the surviving problem is uniform control of an infinite physical twist family.

Modular: `MOD1C` and `MOD1D` are discharged. The parent remains AMBER because none of the eight marked defects is eliminated and `R29-KUM5`, the action/cocycle-level identification between arrangement and modular S4 structures, remains class 2. Abstract `S4 ~= S4` remains forbidden as an adapter.

Brauer: proper algebraic and proper odd-primary work remains consumed. `29-02f/boundary_module_probe.m` already implements the finite `Div_D -> Pic` extraction, so `BR0A` is not an unimplemented idea; however no committed source-locked Magma execution/output and downstream saturation/cohomology result exists. Therefore BR0A/B/G, BR2A/B and NF-PHYS2 remain class 2 current-tool computation walls. `R29-QWEB-CLIFFORD` remains class 3.

## 9. Local, parametric and population frontiers

The local route now has exact odd-prime laws, the real-place result and exact `Delta_2=1/53760`. Its load-bearing remainder is

```text
R29-KUM-LOC3=class 3 NEW_THEOREM_REQUIRED,
```

namely a same-physical-measure height/primitivity/canonical/multiplicity local-to-global transfer. StructureRadar large-sieve/Hecke tools do not supply this automatically.

Master-Hit global coverage remains consumed. The universal exponent-one blocker is still conjectural:

```text
R29-PESCH-E1=class 3 NEW_THEOREM_REQUIRED.
```

`R29-EXT-CHANG-C` remains class 3 because its finite windows were already executed and the residual all-multiples statement explicitly needs a new effective odd-multiplicity primitive-divisor theorem. Paper D is class 4. Paper E remains class 2 because the prior certification attempt reached an explicit completeness/transfer wall.

The population route remains the sole GREEN parent. Existing larger-host density/survival results and the Saunderson `M3-P` lower population do not control

```text
P(B)/M3(B),
```

which remains class 3 and globally unknown.

## 10. Fresh claimed-solution vetting

The audit located the 2026 self-published repository `AEjonanonymous/Non-existence-of-Perfect-Cuboids`. Its Lean file proves conditional statements but does not derive its special mod-8 residue hypotheses or the assumed `u in {0,1,-1}` torsion condition from an arbitrary perfect cuboid. It is therefore not a global endpoint theorem.

```text
R29-EXT-REED-2026=REJECTED_AS_GLOBAL_PROOF_MISSING_UNIVERSAL_ENDPOINT_REDUCTION.
```

This is tracked separately from theorem-applicability counts. See `external-claim-vetting.md`.

## 11. Final audited verdict

The Arsenal rematch found no decisive whole-endpoint theorem. The audit found and executed one additional bounded receiver, sharpened the dependent Beauville twist gate, and found no further class-1 work after a second pass through Stage14 Arsenal, StructureRadar and 29-02 foundations.

```text
ARSENAL_REMATCH_COMPLETE=true
OPEN_RECEIVER_TRIAGE_COMPLETE=true
RECEIVER_OR_TERMINAL_FRONTIER_COUNT=44
CLASS1_IDENTIFIED_COUNT=5
CLASS1_EXECUTED_COUNT=5
CLASS1_PENDING_COUNT=0
CLASS2_COUNT=12
CLASS3_COUNT=11
CLASS4_COUNT=16
VAGUE_AMBER_WITHOUT_EXECUTION_CLASS_COUNT=0

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
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS_AFTER_MATERIAL_POSITIVE_REPAIR
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-16_RESIDUAL_RECEIVER_COMPRESSION_AND_ROUTE_PORTFOLIO
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
