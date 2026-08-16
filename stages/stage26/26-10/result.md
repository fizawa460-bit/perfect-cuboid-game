# Stage26-10 — third-face transition contract

EVIDENCE_LEVEL=PROVED_INTERFACE_ADAPTER
CHECKPOINT=10
STATUS=SUBMITTED_FOR_FRESH_AUDIT
TRANSITION=Stage18->Stage20

## Owned comparison

Under the common primitive canonical cutoff

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad R=\sqrt{a^2+b^2+c^2}\le B,
\]

let \(M_2(B)\) count objects with exactly two integral face diagonals and let \(M_3(B)\) count Euler cuboids, i.e. objects with all three face diagonals integral. Neither population requires an integral space diagonal.

The exact masks are disjoint, so \(M_3/M_2\) is a matched adjacent-stratum population-size ratio, not literal objectwise survival.

```text
LITERAL_SUBSET_TRANSITION=false
RATIO_SEMANTICS=MATCHED_ADJACENT_STRATUM_SIZE_RATIO
OBJECTWISE_SURVIVAL_INTERPRETATION=false
POPULATION_CONTRACT_CHANGED=NO
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
SPACE_DIAGONAL_REQUIRED=false
```

## Literal-host and raw-incidence adapters

Put \(H_{\ge2}(B)=M_2(B)+M_3(B)\) and

\[
\Phi(B)=\frac{M_3(B)}{M_2(B)+M_3(B)}.
\]

This is the literal survival fraction inside the at-least-two-face object host. For the directional raw shared-edge pair counts inherited from Stage25,

\[
P_j=M_{2,j}+M_3,\qquad P=M_2+3M_3,
\]
\[
\Theta_j=\frac{M_3}{P_j},\qquad \Theta=\frac{3M_3}{P}.
\]

Writing \(r=M_3/M_2\), exact algebra gives

\[
\Phi=\frac{r}{1+r},\qquad \Theta=\frac{3r}{1+3r},
\]
and therefore

\[
\boxed{\Theta=\frac{3\Phi}{1+2\Phi}},\qquad
\boxed{\Phi=\frac{\Theta}{3-2\Theta}}.
\]

Thus object counts and raw-pair incidences are not interchangeable, but they are connected by an exact multiplicity adapter. In particular, whenever the inherited corridor implies \(\Theta\to0\), it also gives \(\Phi\to0\) and \(\Theta/\Phi\to3\).

```text
LITERAL_AT_LEAST_TWO_HOST=H_GE2_EQUALS_M2_PLUS_M3
OBJECT_SURVIVAL=Phi_EQUALS_M3_OVER_M2_PLUS_M3
RAW_PAIR_IDENTITIES=Pj_EQUALS_M2j_PLUS_M3;P_EQUALS_M2_PLUS_3M3
EXACT_MEASURE_BRIDGE=true
THETA_EQUALS_3PHI_OVER_1PLUS2PHI
PHI_EQUALS_THETA_OVER_3MINUS2THETA
RAW_PAIR_OBJECT_COUNT_CONFLATION=false
```

## Frozen incoming theorem interfaces

The audited Stage18/22 source law is

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]

The audited Stage20/25-reentry target corridor is

\[
B^{1/6}\ll M_3(B)\ll_\eta B(\log B)^{5-\eta}
\qquad(0<\eta<1/46).
\]

The directional completion interface handed forward is

\[
B^{-5/6}(\log B)^{-5}\ll_j\Theta_j(B)
\ll_{j,\eta}(\log B)^{-\eta},
\]

with \(\Theta_j/\Theta_k\to C_k/C_j\). These are entry data, not a checkpoint30 Stage26 transition theorem. The true \(M_3\) exponent remains open.

## Mechanism and geometry firewall

The raw pair host is the split degree-four del Pezzo surface \(\operatorname{Bl}_4(\mathbf P^1\!\times\!\mathbf P^1)\); imposing the third face passes to a degree-two K3 cover. The geometric Manin ledger describes the raw host only and does not transfer an ambient asymptotic to the K3 target.

Mandatory incoming weapons are `S20-W01`, `S20-W02`, `S20-W03`, `S25-W05`, and `S25-W06`. Checkpoint10 launches no new computation and makes no perfect-cuboid claim.

```text
K3_FIREWALL=ACTIVE
MANIN_HOST_ASYMPTOTIC_TRANSFER_TO_K3=false
TRUE_M3_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
NUM_REUSE_CHECK=PASS
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED_AT_CHECKPOINT10
```

## Discovery and handoff

Repository-scale discovery covered the 824-entry Stage14/15 attack map and the direct Stage18/20/25 receivers. The accepted, deferred, and rejected candidates are recorded in `discovery-ledger.md`; numerical assets routed to Stage26 are retained with population adapters rather than treated as direct theorem evidence.

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSE_MATCH_STATUS=MIXED
DISCOVERY_CHECKPOINT=Stage26-10
DISCOVERY_LEDGER_STATUS=COMPLETE
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDITOR=Codex
DISCOVERY_AUDIT_VERDICT=PASS
MATHEMATICAL_AUDIT_VERDICT=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage26-audit
```
