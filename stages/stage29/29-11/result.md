# Stage29-11 — quotient descent and modular attack portfolio

```text
STAGE=Stage29
ITEM=29-11_QUOTIENT_DESCENT_AND_MODULAR_ATTACK_PORTFOLIO
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PRIMARY_MECHANISMS=CAMPEDELLI|BEAUVILLE|MODULAR|BRAUER
ATTACK_ROUTE_COUNT_RETAINED=11
NEW_ATTACK_ROUTE_CREATED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Scope

This stage attacks exactly the four 29-11 owners from the audited route registry:

```text
Q11-CAMPEDELLI
Q11-BEAUVILLE
Q11-MODULAR
Q11-BRAUER
```

It consumes the audited 29-02hb/02d/02g/02f foundations and the 29-06 endpoint-hub field/direction firewalls. It does not re-credit 29-10, 29-09 local arithmetic, or the 29-12 joint/parametric mechanisms.

## 2. Q11-CAMPEDELLI — Q-defined compression survives, but no quotient is yet arithmetically empty

For every admissible rank-three kernel `H <= (Z/2)^6`, the same global sign-cover map gives

```text
Sbar --degree 8 etale--> Cbar_H --degree 8--> P2
S    --degree 8 etale--> C_H
```

and every physical endpoint Q-point pushes forward to `C_H(Q)`. Thus emptiness of **one** audited quotient over Q would be endpoint-decisive in the one-way direction; no lifting converse is required for that implication.

The exact kernel census remains ten kernels with

```text
geometric/Q(i) S4 orbits = 8+2
certified Q-defined S3 orbits = 6+2+2
exact Q-isomorphism class count = NOT PROVED.
```

### Involution-quotient refresh

The classical Campedelli literature studies the seven nontrivial `(Z/2)^3` involutions and their bicanonical quotients. The current source lock supports the geometric rational/Enriques dichotomy for the relevant involution quotients, but this is a **geometric/birational** statement. It does not identify which quotient type occurs for each cuboid Q-form, and it does not imply a Q-rational parametrization or Q-point obstruction.

The submission therefore proposes the bounded split

```text
R29-CAMP3-GEOM=DISCHARGED_GEOMETRIC_RATIONAL_OR_ENRIQUES_DICHOTOMY
R29-CAMP3=PARTIAL_GEOMETRIC_DONE_Q_FORM_AND_EXACT_INVOLUTION_ASSIGNMENT_OPEN
```

Fresh audit must source-check this split before accepting it.

The arithmetic receivers remain

```text
R29-CAMP2=OPEN_H_TORSOR_DESCENT_FOR_THREE_CERTIFIED_Q_SYMMETRY_REPRESENTATIVES
R29-CAMP4=OPEN_CAMPEDELLI_BRAUER_TWO_PRIMARY_COMPATIBILITY
```

No current theorem makes any `C_H(Q)` empty.

```text
Q11-CAMPEDELLI=AMBER_Q_DEFINED_COMPRESSION_NO_Q_POINT_OBSTRUCTION
```

## 3. Q11-BEAUVILLE — exact Q-cover, but the twist family remains infinite

The audited Q-form

```text
q_U:X_U -> U_phys
```

is finite etale degree two with constant deck group `Z/2`. Every endpoint point defines

```text
delta(P) in H^1(Q,Z/2) ~= Q*/Q*^2
```

and lifts to the corresponding quadratic twist `X_U^delta`, not necessarily to the untwisted cover. Hence

```text
U_phys(Q)=union_delta image(X_U^delta(Q)->U_phys(Q)).
```

This exact descent identity is useful but does not bound the occurring squareclasses. The open physical boundary allows point-dependent ramification, so proper-cover finiteness heuristics cannot be used to claim finitely many twists.

The Albanese target remains the swap-twisted/Weil-restricted Bolza-Jacobian package. The geometric CM decomposition of `J_D` does not give one fixed Q-elliptic square, and the exact V4-kernel swap equivariance remains open.

```text
R29-BEAU1B=OPEN
R29-BEAU1C=OPEN
R29-BEAU2A=OPEN_BOUNDED
R29-BEAU2=OPEN
R29-BEAU3=OPEN_CM_QCURVE_TWIST_DESCENT
FINITE_TWIST_SET_PROVED=false
```

Modern genus-two 2-Selmer/Cassels--Tate algorithms are a concrete tool for individual induced twists, but no theorem presently supplies uniform control over the infinite physical twist family.

```text
Q11-BEAUVILLE=AMBER_EXACT_Q_COVER_INFINITE_TWIST_FAMILY_NO_UNIFORM_SELmer_CLOSURE
```

## 4. Q11-MODULAR — finite defect compression is real; arithmetic elimination is not

Over `K=Q(i)`, the audited modular presentation is

```text
Sbar_K ~= (X(8)xX(8))/Delta G0,
G0=(Z/2)^3.
```

On the noncuspidal Q-locus an endpoint point yields the conjugate-self level structure

```text
E/K,
(P1,P2) basis of E[4],
psi:E[8] -> E^sigma[8],
psi(P1)=P1^sigma,
psi(P2)=-P2^sigma.
```

The defect

```text
kappa=psi^sigma o psi
```

lies in the eight-element group `K8=ker(SL2(Z/8)->SL2(Z/4))`. Its ordinary symplectic conjugacy classes have exact sizes `1,3,3,1`, but these are not yet proved to be the exact arithmetic endpoint strata under the retained sigma-twisted level-4 sign data.

The generic forgetting quotient has degree 24 and residual abstract `S4`. The base seven-line arrangement also has geometric `S4`, but equality of abstract groups does not identify their actions or Q-descent cocycles. Therefore Gap Scan B's transfer

```text
R29-KUM5 -> Q11-MODULAR
```

remains open rather than being closed by an `S4=S4` name match.

```text
R29-MOD1C=OPEN_TWISTED_SIGMA_ACTION
R29-MOD1D=OPEN_CUSP_STABILIZER_PHYSICAL_OPEN
R29-MOD2B=OPEN_BRANCH_CUSP_STABILIZER_LEDGER
R29-KUM5=OPEN_ACTION_LEVEL_S4_Q_DESCENT_ADAPTER
NAIVE_ORDINARY_8_CONGRUENCE_OBSTRUCTION=RED_AUDITED
```

No K8 class is globally eliminated.

```text
Q11-MODULAR=AMBER_FINITE_DEFECT_COMPRESSION_NO_ARITHMETIC_CLASS_ELIMINATION
```

## 5. Q11-BRAUER — proper odd-primary closure does not close the physical open

For the smooth proper cuboid surface the audited theorem surface already gives

```text
Br_1(S)/Br(Q)=0
proper nonconstant odd-primary Brauer = absent.
```

That is genuine negative knowledge for a naive proper Brauer obstruction, but it does not determine the physical open

```text
U=Sbar intersect D_+(a1*a2*a3).
```

Its 72-component boundary enters the extended Picard complex

```text
UPic(U_Qbar) ~= [Div_D -> Pic(S_Qbar)],
Br_a(U) ~= H^2(Q,UPic(U_Qbar)).
```

The unit kernel can carry absolute-Galois information not killed by the visible `V4` permutation action, and nonextendable Gersten residues plus the two-primary integral/evaluation problem remain open.

```text
R29-BR0A=OPEN
R29-BR0B=OPEN
R29-BR0G=OPEN
R29-BR2A=OPEN
R29-BR2B=OPEN
R29-NF-PHYS2=OPEN_ADAPTER
R29-QWEB-CLIFFORD=AMBER_NEW_THEOREM_REQUIRED
R29-NF7=OPEN_OPTIONAL_TWO_PRIMARY_BOUNDARY_RESONANCE_ADAPTER
```

None of these ownership assignments certifies a Brauer--Manin or Clifford obstruction.

```text
Q11-BRAUER=AMBER_PROPER_ODD_CLOSED_PHYSICAL_OPEN_BOUNDARY_AND_TWO_PRIMARY_OPEN
```

## 6. Submitted classification

```text
Q11-CAMPEDELLI = AMBER
Q11-BEAUVILLE   = AMBER
Q11-MODULAR     = AMBER
Q11-BRAUER      = AMBER
GREEN_ROUTE_COUNT_29_11=0
RED_PARENT_ROUTE_COUNT_29_11=0
ATTACK_ROUTE_COUNT_RETAINED=11
```

Subroute-level negative results are retained: ordinary 8-congruence is RED, and proper odd-primary Brauer obstruction is absent. These do not make their parent portfolios RED because the stronger descent/open-boundary mechanisms remain live.

## 7. Handoff

No new Stage16--28 backflow or roadmap rewrite is proposed. The expected next item after a fresh audit pass is

```text
29-12_JOINT_LOCAL_PARAMETRIC_AND_INTERACTION_ATTACK_PORTFOLIO.
```

```text
AUDIT_REQUIRED=true
AUDIT_VERDICT=PENDING
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
TARGETED_BACKFLOW_REQUIRED=false
ROADMAP_REWRITE_REQUIRED=false
NEXT_ITEM_AFTER_AUDIT_PASS=29-12_JOINT_LOCAL_PARAMETRIC_AND_INTERACTION_ATTACK_PORTFOLIO
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
