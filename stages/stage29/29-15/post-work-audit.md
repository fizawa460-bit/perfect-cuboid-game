# Stage29-15 — post-Work adversarial re-audit

```text
AUDITED_PR=1323
POST_WORK_SUBMISSION_HEAD=67df05af974d8b737b0e7616e0cb5d4e21dda2ab
AUDIT_VERDICT=PASS_AFTER_REPAIR
REPAIR_KIND=FORD_SOURCE_PROMOTION_PLUS_K3_RULED_MODEL_EXECUTION_AND_CLASS2_WALL_NARROWING
POST_WORK_INPUT_AUDITED=true
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
```

This audit covers only the material input added after the earlier 29-15 audit. The previous five bounded discharges remain retained and are not re-credited.

## 1. Cao--Demarche--Xu / Cao descent compression

Primary-source recheck confirms the exact scope used by the Work input.

Cao--Demarche--Xu, *Comparing descent obstruction and Brauer--Manin obstruction for open varieties*, Trans. AMS 371 (2019), Theorem 1.5 / 7.5, proves for smooth quasi-projective geometrically integral varieties over a number field that

```text
X(A)^descent = X(A)^{et,Br}.
```

Yang Cao, *Sous-groupe de Brauer invariant et obstruction de descente iteree*, Algebra & Number Theory 14 (2020), Corollary 1.2, gives in the same scope

```text
X(A)^{descent,descent} = X(A)^descent.
```

The already-audited physical algebraic open `U/Q` is smooth, quasi-projective and geometrically integral, so the hypotheses apply.

Therefore

```text
ONE_STEP_DESCENT_ETALE_BRAUER_EQUIVALENCE=VERIFIED
ITERATED_DESCENT_ON_PHYSICAL_OPEN=MERGED
ONE_STEP_DESCENT_ETALE_BRAUER_COMPUTED=false
FINITE_OPEN_TWIST_SET_INFERRED=false
```

This is a route-compression theorem, not an emptiness theorem. It does not close Beauville twist support or the physical-open Brauer calculations.

## 2. `R29-BR-LINE9` — source-certified class-1 execution

The finite checker and an independent reconstruction both give exactly

```text
TRIPLE_POINTS=6
DOUBLE_POINTS=3
INCIDENCE_GRAPH_VERTICES=16
INCIDENCE_GRAPH_EDGES=24
INCIDENCE_GRAPH_CONNECTED=true
FORD_B1_GAMMA=9.
```

Primary-source audit of Timothy J. Ford, *The Brauer Group of an Affine Double Plane Associated to a Hyperelliptic Curve*, Theorem 1.1 plus the line-arrangement specialization, confirms that after choosing one of the seven projective lines as the line at infinity, over `Qbar`

```text
Br(P2_Qbar - D)[2] ~= H1(Gamma,Z/2) ~= (Z/2)^9.
```

Hence the Work precursor is promoted to an exact geometric theorem application:

```text
R29_BR_LINE9=DISCHARGED_SOURCE_CERTIFIED_GEOMETRIC_ARRANGEMENT_COMPLEMENT_BR2
FORD_B1_GAMMA=9
```

It is intentionally **not** identified with `Br(U)/Br(Q)`. The endpoint multiquadratic cover, exceptional divisors, absolute-Galois descent, the 72-component physical boundary and local evaluation remain separate.

## 3. `R29-K3-RULED2` — bounded positive execution, class 2 retained

The provisional Work state said that an explicit geometrically ruled model for `K_c` was still missing. The renewed audit constructs it from already-audited repository equations.

The exact coordinate quotient is

```text
b1^2=a2^2+a3^2,
b2^2=a1^2+a3^2,
b3^2=a1^2+a2^2.
```

Forgetting `b1` is exactly the Stage29-07 two-face floor `T2bar`. Pulling the residual equation `b1^2=x^2+y^2` back through the audited `P1 x P1` parametrization gives the Q-defined `(4,4)` double cover

```text
w^2=(u1*v1*(v2^2-u2^2))^2
    +(u2*v2*(v1^2-u1^2))^2.
```

Over `Q(i)` the branch splits into two `(2,2)` components

```text
u1*v1*(v2^2-u2^2) +/- i*u2*v2*(v1^2-u1^2)=0.
```

The audit checks both components are smooth and meet transversely in exactly eight points. Thus the branch is reduced, flat over either ruling, and has only simple singularities. Creutz--Viray Theorem I / Corollary 5.4 applies.

Using the already-audited `rho(K_c)=20`, their `(4,4)` `P1 x P1` dimension formula gives

```text
KC_RULED_MODEL=DISCHARGED_EXPLICIT_P1xP1_4_4_MODEL
KC_BRANCH_HYPOTHESES=DISCHARGED
KC_GEOMETRIC_BR2_DIMENSION=2.
```

The full receiver remains class 2 because the arithmetic-useful finite presentation is not yet materialized on this model. The exact missing finite data are

```text
- a concrete basis of Creutz--Viray L_{c,E};
- the x-alpha relation matrix for a certified NS(K_c) basis;
- two explicit surviving Brauer-symbol representatives;
- Q(i)/Q Galois action on those symbols;
- later local evaluation on the physical endpoint lift image.
```

Therefore

```text
R29_K3_RULED2=2_CURRENT_TOOL_LIMIT_EXECUTED_AFTER_RULED_MODEL_AND_BR2_DIMENSION_DISCHARGE
R29_K3_RULED2_CORE=DISCHARGED_RULED_MODEL_BRANCH_AND_GEOMETRIC_BR2_DIMENSION
NEW_THEOREM_REQUIRED_FOR_K3_RULED2=false
```

This is a narrowed finite matrix/symbol wall, not a theorem gate and not an endpoint obstruction.

## 4. Other Work leads — anti-proliferation audit

The remaining Work matches do not create an additional independent receiver or a hidden class-1 task.

- Dimitrov--Gao--Habegger supplies a powerful uniform Mordell--Lang bound conditional on the relevant Mordell--Weil rank data; it does not supply the moving-family rank theorem missing in `R29-FIB2`.
- de Grey--Gibbs--Helm fixed-aspect filters do not cover all endpoint points.
- Luca/Li Heron/bisector reformulations supply a model lead but no uniform theorem for the physical bisector sublocus.
- Balestrieri--Johnson--Newton singular-K3 Brauer effectivity remains quotient/model dependent and does not control the endpoint lift locus.
- Creutz--Viray two-primary Kummer results still require an exact Kummer/physical adapter.
- Stoll finite descent is a proper-variety theorem and does not make the nonproper physical-open twist support finite.
- Bauer--Stoll Burniat results concern their specific etale-product geometry; no exact cuboid Q-form adapter is present.
- Browning--Loughran/Huang ambient sieve statements do not preserve the exact conditional `M3` physical measure.

```text
ADDITIONAL_HIDDEN_CLASS1_FOUND=false
ADDITIONAL_NEW_WORK_RECEIVER_FOUND=false
```

## 5. Audited receiver census

The two Work additions are legitimate children:

```text
R29-BR-LINE9      class 1, executed and discharged
R29-K3-RULED2     class 2, current finite-tool wall after bounded core execution
```

No further new receiver is warranted. Therefore the provisional census survives audit:

```text
NEW_WORK_RECEIVER_COUNT=2
RECEIVER_OR_TERMINAL_FRONTIER_COUNT=46
CLASS1_IDENTIFIED_COUNT=6
CLASS1_EXECUTED_COUNT=6
CLASS1_PENDING_COUNT=0
CLASS2_COUNT=13
CLASS3_COUNT=11
CLASS4_COUNT=16
VAGUE_AMBER_WITHOUT_EXECUTION_CLASS_COUNT=0
```

The six class-1 closures are the retained five from the first 29-15 audit plus `R29-BR-LINE9`.

## 6. Parent routes and endpoint firewalls

None of the new theorem inputs empties a physical endpoint locus or changes the parent color ledger.

```text
ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
NEW_DECISIVE_GLOBAL_THEOREM_FOUND=false
TARGETED_BACKFLOW_REQUIRED=false
ROADMAP_REWRITE_REQUIRED=false
```

In particular, geometric `Br(P2_Qbar-D)[2]`, geometric `Br(K_c_Qbar)[2]`, descent/etale-Brauer equivalence and iterated-descent idempotence are structural inputs only until the exact endpoint lift/Galois/local-evaluation receivers are solved.

## 7. Final post-Work state

```text
POST_WORK_INPUT_AUDITED=true
R29_BR_LINE9=DISCHARGED_SOURCE_CERTIFIED_GEOMETRIC_ARRANGEMENT_COMPLEMENT_BR2
FORD_B1_GAMMA=9
R29_K3_RULED2=2_CURRENT_TOOL_LIMIT_EXECUTED_AFTER_RULED_MODEL_AND_BR2_DIMENSION_DISCHARGE
ITERATED_DESCENT_ON_PHYSICAL_OPEN=MERGED
ONE_STEP_DESCENT_ETALE_BRAUER_EQUIVALENCE=VERIFIED
NEW_WORK_RECEIVER_COUNT=2
RECEIVER_OR_TERMINAL_FRONTIER_COUNT=46
CLASS1_IDENTIFIED_COUNT=6
CLASS1_EXECUTED_COUNT=6
CLASS1_PENDING_COUNT=0
CLASS2_COUNT=13
CLASS3_COUNT=11
CLASS4_COUNT=16
VAGUE_AMBER_WITHOUT_EXECUTION_CLASS_COUNT=0
AUDIT_VERDICT=PASS_AFTER_REPAIR
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-16_RESIDUAL_RECEIVER_COMPRESSION_AND_ROUTE_PORTFOLIO
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
