# Stage27-19-r5aw — independent hostile audit

```text
AUDIT_VERDICT=PASS_WITH_CI_LIFECYCLE_REPAIR
AUDITED_PR=1246
AUDITED_SUBMISSION_HEAD=8cc2cd381160a2f58bb06fad7c0cb27972b14f6d
BASE_MAIN=4045fc9a613e7c9582b586e8151bce5a371d3942
MATHEMATICAL_AUDIT=PASS
FIXED_R_PHYSICAL_FIBER_AUDIT=PASS
R2_TAU_BOUND_AUDIT=PASS
NO_GLOBAL_RECHARGE_AUDIT=PASS
R5AN_PRIMITIVITY_INPUT_AUDIT=PASS
DIFFERENCE_FACTOR_SPLIT_AUDIT=PASS
GAUSSIAN_NORM_FACTOR_SPLIT_AUDIT=PASS
KAPPA_ALLOCATION_ENTROPY_AUDIT=PASS
WITNESS_AUDIT=PASS
R5AT_R5AV_LIFECYCLE_RECONCILIATION_AUDIT=PASS
STRUCTURE_RADAR_FREEZE_RELEASE_AUDIT=PASS
CONTROLLER_SIDECAR_FIREWALL_AUDIT=PASS
SUBMITTED_HEAD_CI=FAIL_LIFECYCLE_DEBT_ONLY
SUBMITTED_HEAD_CI_RUN=32343958038
CI_REPAIR_PERFORMED=true
CI_REPAIR=make inherited r5at-r5av verifier successor-aware and run r5aw verifier/JSON checks in the fixed-R workflow
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
ADVANCE_TO_CHECKPOINT50=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=false
NEXT_DERIVED_ROUTE_AFTER_MERGE=27-19-r5ax
```

## 1. Fixed-R physical fiber

For one exactly-two physical cuboid with fixed space diagonal `R`, let the two integral faces share edge `e`, with remaining edges `x,y` and integral face diagonals `D_x,D_y`. Then

```text
R^2=D_x^2+y^2=D_y^2+x^2.
```

Thus each physical object determines two sum-of-two-squares representations of `R^2`. Forgetting orientation/canonical data and retaining only the shared-edge choice gives the safe overcount

```text
N_{2,R} <= 3 r_2(R^2)^2.
```

The classical identity `r_2(n)=4 sum_{d|n} chi_4(d)` gives `r_2(n)<=4 tau(n)`, hence

```text
N_{2,R} <= 48 tau(R^2)^2 = R^o(1).
```

This is a theorem about the actual fixed-`R` physical fiber, not the pre-quotient Stage19 parameter host. Summing it naively over `R<=B` gives only `B^(1+o(1))`; it cannot be recharged on top of the already stronger whole-family half-power bound. The PR preserves this firewall.

## 2. Difference-factor allocation

Audited r5an supplies the needed primitive hypotheses:

```text
kappa | m^2-n^2,
kappa odd and squarefree,
(kappa,mnrs)=1,
(m,n)=1.
```

Since `gcd(m-n,m+n)|2`, no odd prime of `kappa` divides both factors. Therefore

```text
kappa_- = gcd(kappa,abs(m-n)),
kappa_+ = kappa/kappa_-
```

is a coprime exact allocation satisfying

```text
kappa_- | m-n,
kappa_+ | m+n.
```

Writing `A=(m-n)/kappa_-` and `B=(m+n)/kappa_+` gives the exact inverse formulas

```text
m=(kappa_- A+kappa_+ B)/2,
n=(kappa_+ B-kappa_- A)/2.
```

The prime-allocation count is at most `2^omega(kappa)=kappa^o(1)`. This is an entropy collapse only; no negative power of the dyadic `K` follows automatically.

## 3. Gaussian norm allocation

Audited r5an also gives

```text
kappa | r^2+s^2,
(r,s)=1,
(kappa,rs)=1,
p=1 mod 4 for every p|kappa.
```

For each `p|kappa`, write `p=pi_p conjugate(pi_p)` in `Z[i]`. Exactly one of the two primes above `p` divides `r+i s`; if both did, then `p` would divide both `r` and `s`. Multiplying the selected factors yields, up to a unit,

```text
r+i s=lambda eta,
N(lambda)=kappa,
N(eta)=(r^2+s^2)/kappa.
```

The choice count is at most `4*2^omega(kappa)=kappa^o(1)`. Together with the audited r5at fact `kappa|R`, this remains subpower at fixed `R`.

## 4. Witness

For

```text
(m,n,r,s)=(21,16,27,14),
kappa=185=5*37,
R=7585,
```

one has

```text
kappa_-=5,
kappa_+=37,
A=B=1,
lambda=11-8i,
eta=1+2i,
(11-8i)(1+2i)=27+14i.
```

The physical edges `(6048,1665,4264)` and face diagonals `(6273,7400)` satisfy both face-square equations and the space-diagonal equation at `R=7585`.

## 5. Lifecycle / StructureRadar boundary

PR #1072 is independently confirmed merged with head `02a56737ff56046d1c60523663b2d70c9a7b9d1f` and merge commit `a38d6e782718ed01bb813c477f3f021afbf3d47d`; its mathematical content head and CI records match the r5aw reconciliation.

Merged StructureRadar PR #1244 explicitly pauses normal StructureRadar deepening and returns work to Stage27-19/20. Therefore the old conditional `DO_NOT_START_R5AW` freeze is legitimately lifted without treating any unresolved external gate as mathematically closed.

The monolithic Stage27 controller contains parallel Stage27-20 history. The submitted sidecar `controller-sync-delta.json` is therefore accepted as the pending reconciliation record; this audit does not overwrite the monolithic controller from a partial view.

## 6. CI repair

The submitted head's only triggered workflow failed because the inherited r5at-r5av verifier hard-coded the historical pre-merge state `AUDITED_PASS_PENDING_MERGE`. The PR correctly reconciles that predecessor to `AUDITED_PASS_MERGED`, so the failure is lifecycle debt rather than a mathematical regression.

The audit repairs the old verifier to accept and validate the finalized #1072 lifecycle, including merge/lifecycle-CI/freeze-release fields. The same fixed-R workflow is extended to trigger on r5aw changes, execute `verify_27_19_r5aw.py`, and validate both new r5aw JSON contracts.

No theorem surface is strengthened by the CI repair.
