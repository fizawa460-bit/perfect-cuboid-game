# Stage13-13fh — notation cleanup, audit scope, repaired-proof synthesis, and R05 readiness

> STATUS: `STAGE13_13FH_COMPLETE_R05_SYNTHESIS_READINESS`
>
> INPUT: R05 repair Gates A--G.
>
> OUTPUT: one repaired canonical proof candidate and an explicit authorization boundary for building immutable R05.

## Result

Gate H creates the new proof-facing entrypoint

```text
stages/stage13/13-13fh/stage13-r05-canonical-proof.md
```

and makes it the only canonical mathematical proof source for the future R05 bundle. The older `13-13c/stage13-final-proof.md` remains immutable provenance for R04 and is not the R05 proof entrypoint.

The theorem statement and counting convention are unchanged.

## Notation cleanup

The R05 candidate uses:

```text
theta     = geometric spherical polar angle only
alpha     = geometric inner spherical angle
vartheta  = Gaussian local angular phase
phi       = outer Pythagorean polar parameter
psi       = complementary geometric angle
```

The actual split-prime mixed factor is defined at first use as

```text
C_{ell,p}(s_h,s_r,s_s)
:= C_vartheta(p^{-s_h},p^{-s_r},p^{-s_s}).
```

Thus the R04 `theta` collision and the first-use ambiguity of `C_{ell,p}` are removed.

## A--G synthesis

The canonical candidate now contains, in theorem order rather than repair-history order:

1. the complete Stage12 `D_B -> G -> C_raw -> C_prim` interface, explicit `kappa`, `eta=pi*kappa`, and exact factor-two fiber;
2. chamber/Gelfand--Leray geometry and `J_q=2I_q/pi`;
3. primitive split-prime coefficient system with the `theta/vartheta` notation separated;
4. the full `529 p^-5/4` Wiener derivation and explicit `p=5` bound `<432`;
5. exact Hecke/Dirichlet/Vaaler proof-facing contracts and Riesz/Perron smoothing;
6. the explicit `O((log B)^27)` box count, `N=64`, all-box `O(B(log B)^-35)` remainder, boundary/mesh ledger;
7. all-`ell` conductor bookkeeping and removal of logical dependence on fixed `A=48`;
8. non-circular common-`Theta` proof followed only afterwards by Stage12 calibration;
9. the finite `100k -> 5m` discrepancy scope statement, including the explicit nonclaim of an effective convergence rate;
10. exact inert local states and symbolic unit character sum;
11. fixed-`S` finite character orthogonality, principal pole sector including auxiliary-character aliasing, nonprincipal pole loss, and fixed limit order;
12. exactly-one transfer and consolidated theorem lock.

No repair-chain reading is required for the future R05 reviewer.

## Deterministic audit scope

Any `PASS` emitted by Stage13 deterministic scripts means only

```text
DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY
```

It does not certify the mathematical proof. Finite quadrature/enumeration/checksums remain validators, not theorem evidence.

## R04 objection crosswalk after repair

The repair candidate now explicitly addresses:

```text
Claude finite-vector/common-Theta concern        -> Gate A + R05 scope section
DeepSeek 529 black box                           -> Gate B
DeepSeek curved-region/box uniformity             -> Gate C
DeepSeek nonzero-harmonic conductor bookkeeping   -> Gates D/F
DeepSeek Stage12 object/factor-two interface       -> Gate E
DeepSeek Hecke/Vaaler exact assumptions            -> Gate F
DeepSeek fixed-prime transfer/nonprincipal terms   -> Gate G
DeepSeek notation/audit-scope presentation         -> Gate H
```

This is an **internal repair closure**, not a replacement for fresh external review. The R04 verdicts remain attached to R04 and do not automatically count toward R05.

## Readiness decision

No Gate A--H audit found a theorem-level contradiction or changed the theorem constants. Therefore an immutable R05 bundle may now be built from the new canonical proof candidate.

R05 has **not** yet been created by this gate.

The next numeric task is reserved as

```text
13-13fi = build immutable R05 self-contained review bundle and manifest
```

After R05 is frozen, fresh independent reviews are required. Stage13 final freeze remains blocked until the final bundle receives at least two independent `CLOSED` verdicts and has zero unresolved theorem-level objections.

## Completion lock

```text
STAGE13_13FH=COMPLETE_R05_SYNTHESIS_READINESS
R05_CANONICAL_PROOF=stages/stage13/13-13fh/stage13-r05-canonical-proof.md
R05_CANONICAL_PROOF_SINGLE_ENTRYPOINT=true
R04_CANONICAL_PROOF_SUPERSEDED_FOR_R05=true
R03_IMMUTABLE=true
R04_IMMUTABLE=true
NOTATION_THETA_GEOMETRIC_ONLY=true
NOTATION_VARTTHETA_GAUSSIAN_PHASE=true
C_ELL_P_SUBSTITUTION_DEFINED_AT_FIRST_USE=true
DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY
REPAIR_GATES_A_THROUGH_H_COMPLETE=true
R04_OBJECTIONS_REPAIRED_IN_R05_CANDIDATE=true
R04_VERDICTS_CARRY_FORWARD_TO_R05=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R05_SYNTHESIS_READY=true
R05_BUNDLE_CREATED=false
R05_FRESH_EXTERNAL_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13fi
```