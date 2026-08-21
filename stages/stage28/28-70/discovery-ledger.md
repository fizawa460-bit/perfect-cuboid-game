# Stage28-70 — repository-wide reuse / strongest-known discovery ledger

```text
DISCOVERY_CHECKPOINT=70
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=false_AT_CHECKPOINT70_BEYOND_ALREADY_INTEGRATED_STAGE28_SUPERSESSIONS
DISCOVERY_LEDGER_STATUS=COMPLETE
```

## Search surfaces

```text
SEARCHED_PATHS=
  docs/research-arsenal-index.md;
  docs/stage14-num-reuse-index.md;
  docs/stage14-15-bound-attack-map.md;
  docs/stage14-15-bound-attack-ledger/manifest.json;
  docs/stage14-15-bound-attack-ledger/part-0001.jsonl..part-0005.jsonl;
  docs/stage14-15-bound-deep-review-queue.md;
  stages/stage19/19-controller.json;
  stages/stage20/20-controller.json;
  stages/stage26/26-controller.json;
  stages/stage27/27-controller.json;
  stages/stage28/28-10;
  stages/stage28/28-40-r2;
  stages/stage28/28-50-r2;
  stages/stage28/28-60-r2;
  stages/stage28/28-60-r3;
  PRs #1274..#1282

SEARCH_TERMS=N2,M3,M3/N2,space diagonal,third face,Euler,K3,double cover,branch profile,interaction curvature,physical height,moving modulus,fixed curve,M6,Saunderson
STRUCTURAL_SIGNATURES=INTEGRAL_SPACE_DIAGONAL,EXACTLY_TWO_FACES,THREE_FACES_EULER,K3_SURFACE_COVER,MOVING_MODULUS,OVERLAP_INTERSECTION,PAIRED_NORMS
DEPENDENCY_NEIGHBORS=Stage19,Stage20,Stage25,Stage26,Stage27,Stage14-e,Stage14-4,Stage14-num,Stage15
```

## Accepted reusable inputs

| Candidate | Stage28 use | Match |
|---|---|---|
| `AR-006` | `N2(B)<<B^(1/2+o(1))` upper interface | exact downstream population/cutoff interface |
| `S25-W01` | `N2(B)>>B^(1/4)` global/directional construction lower | exact downstream population/cutoff interface |
| `S25-W02` | exact face/space interaction cross-ratio; positive-divergent interaction invariant | exact adapter input |
| `S25-W06` | Manin `(a,b)` transition ledger; explains the two-log normalizer | exact explanatory ledger, not extra density factor |
| `S26-W01` | generalized Saunderson `M3` one-third-scale lower | exact target-population input, strengthened inside Stage28-50-r2 |
| `S26-W02` | `H_ge2=M2+M3`, `H_ge2~M2`, completion-share adapter | exact common-host adapter |
| `S26-W03` | Euler upper `M3<<_eta B(log B)^(5-eta)`, `eta<1/46` | exact target upper interface |
| Stage28-40-r2 | branch profiles `4 x genus0` versus `2 x genus1`; normalized local quotient boundary | exact current-stage causal input |
| Stage28-50-r2 | `liminf M3/B^(1/3)>=27/(40*pi^2)` and injective-cone height adapter | exact current-stage target lower |
| Stage28-60-r2 | `J_28`, `K_28` and bridge-curvature equivalence | exact/asymptotic current-stage adapter |
| Stage28-60-r3 | common physical polarization normalization; Stage19 odd-degree obstruction; Stage20 Saunderson physical M-degree 6 | audited current-stage geometric input |
| `NUM-R04`–`NUM-R08` | inherited finite synthesis/diagnostic panel only | mixed exact-finite/derived-finite; never asymptotic proof |

```text
CANDIDATES_ACCEPTED=AR-006,S25-W01,S25-W02,S25-W06,S26-W01,S26-W02,S26-W03,Stage28-40-r2,Stage28-50-r2,Stage28-60-r2,Stage28-60-r3,NUM-R04..NUM-R08
REUSE_MATCH_STATUS=MIXED
POPULATION_ADAPTERS_PROVED=Stage28 common-host H_ge2 adapter; Stage19 N2 exact-face/space adapter; Stage20 M3 exact-three-face adapter; common physical R<=B cutoff; common-base polarization normalization from checkpoint60-r3
```

## Stage14/15 attack-ledger rematch

The complete 824-record map/manifest and all five shards were inspected as the mandatory Stage21-28 discovery surface. The most relevant Stage14-e records were reread against the Stage28 ratio/measure contract.

### Accepted provenance/components

- `S1415-ATTACK-0215` / Stage14-e1: exact two-face ambient/gluing dictionary and multiplicity discipline.
- `S1415-ATTACK-0219` / Stage14-e3: toric base `Y=Bl_4(P1xP1)` and anticanonical physical-height model.
- `S1415-ATTACK-0224` / Stage14-e8: Euler-brick degree-two K3 cover and branch-class geometry.
- `S1415-ATTACK-0216` / Stage14-e10 and `S1415-ATTACK-0217` / Stage14-e11: Euler local blocker / Huang thin-cover interfaces, used only through their already-audited later adapters.
- `S1415-ATTACK-0225` / Stage14-e9: exact gcd/lcm and local blocker structure.

### Rejected as direct Stage28 ordering theorems

- `S1415-ATTACK-0216` / e10 and `S1415-ATTACK-0217` / e11 control the Euler marginal/generic degree-two cover but do not compare the Stage19 and Stage20 marginals on the same physical measure; they cannot order `M3/N2`.
- `S1415-ATTACK-0221` / e5 compares the no-space two-face ambient host with the integral-space filter. It is useful causal context but does not supply the relative third-face-versus-space theorem required for `J_28`.
- `S1415-ATTACK-0224` / e8 gives K3 structure and an unconditional envelope, while its finite square-root signal is explicitly non-theorem; no Stage28 ordering follows.
- Stage14-num attacks including `S1415-ATTACK-0226`, `0240`, `0248`–`0253` are exact finite/regression assets only and cannot decide an asymptotic bridge ratio.

The curated deep-review clusters were also checked. The Stage19-relevant Q03–Q11 clusters retain either reusable components, precise external future gates, or later exhausted internal routes:

```text
Q03=S1415-ATTACK-0259,0260
Q04=S1415-ATTACK-0522,0544,0583,0204
Q05=S1415-ATTACK-0724,0728,0729,0731
Q06=S1415-ATTACK-0748
Q07=S1415-ATTACK-0791,0793,0794,0796,0800
Q08=S1415-ATTACK-0771,0772
Q09=S1415-ATTACK-0796,0804,0807,0809,0811
Q10=S1415-ATTACK-0811,0812,0814,0816,0817
Q11=S1415-ATTACK-0817,0818,0819,0820
```

None supplies a same-measure theorem comparing the Stage19 space-cover moving complement to the Stage20 third-face cover at the required `(log B)^(-2)` relative-interaction scale. Reopening the exhausted Q07-Q10 algebra/dispersion clusters without a materially new equation or theorem would violate their recorded reopen conditions.

```text
CANDIDATES_REJECTED_WITH_REASON=
  S1415-ATTACK-0216,0217: target-marginal/generic-cover only, no relative same-measure comparison;
  S1415-ATTACK-0221: ambient-to-space comparison, wrong bridge target;
  S1415-ATTACK-0224: K3/envelope plus finite-only signal, no relative ordering;
  Stage14-num finite assets: finite evidence only;
  deep-review Q03-Q11: component/external-gate/exhausted-route status, no direct Stage28 relative theorem
```

## Numerical preflight

Checkpoint70 opens no new computation. The Stage28 finite panel is inherited only as labeled finite evidence, and the Stage14 numerical reuse index explicitly routes `NUM-R04`–`NUM-R08` to Stage28 synthesis.

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R04,NUM-R05,NUM-R06,NUM-R07,NUM-R08
NUM_POPULATION_MATCH=ADAPTER_PROVED_OR_DIAGNOSTIC_ONLY_AS_RECORDED
NUM_EVIDENCE_LEVEL=EXACT_FINITE+DERIVED_EXACT_FINITE+FINITE_DIAGNOSTIC_ONLY
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
```

## Strongest-known conclusion

No repository result found in the required surfaces improves the Stage28 bridge corridor, resolves `M3/N2`, or controls `J_28` at its critical `(log B)^(-2)` scale beyond the already-integrated checkpoint60 work. The remaining global receiver is therefore stable and research-request-ready:

```text
OPEN_GATE_PRIMARY=MovingComplementOrBranchSensitiveInteractionThresholdTheorem
TARGET=J_28=I_face/I_sp relative to (log B)^(-2)
HEIGHT=physical R<=B
ENDPOINT_COUNT_FORBIDDEN=true
RESEARCH_REQUEST_READY=true
```

The finite `PhysicalLowDegreeRootSpectrumM6` classification remains an optional refinement; even a complete M6 answer does not by itself control the moving complement.