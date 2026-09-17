# Stage32 MB104 — uniform-closure restart ledger — 2026-09-17

Status: **RESEARCH RESTART / NO NEW MATHEMATICAL CREDIT / OLD PR SPLIT / DO NOT REPEAT SEARCHED ROUTES**

## 0. Why this file exists

The previous retained research PR `#1791` (`stage32mb-mainbatch-20260912`) grew to 443 commits / 324 changed files. Its final retained head before this split is

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

The old PR is retained only as an immutable research archive. This new branch starts from repository `main`

```text
c6284abbb29930255892d56f800da0ea1e34734b
```

and intentionally does **not** copy the old 324-file surface. Instead this file preserves the load-bearing mathematical boundary, the already-searched route ledger, and exact immutable references needed to avoid rediscovery.

No MAIN/STATE/receiver/effectivity/theorem/endpoint credit is changed by this split.

Important startup warning at split time: the live repository `main` ref above does not match the embedded `MAIN-STATE.json` field `authority_sync.current_repository_main=4c51b4ea90a84f9a22a90f194c6d8ecadd9f0d1c`. Treat that as authority drift; do not perform new credit-bearing mathematics until ordinary startup resolves it.

## 1. Immutable archive references

Old research archive:

```text
PR: #1791
branch: stage32mb-mainbatch-20260912
retained head: ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
most recent intermediate hostile-audit PASS boundary recorded in MB104:
  e269761fbe82c56cdcc8d4870584952dc2d800a3
review: 5187369070
```

Primary old-head restart sources, to be fetched by exact commit rather than rediscovered:

```text
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GLOBAL-CLASSIFICATION-CHECKPOINT.md
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-UNIFORM-RAY-COMPONENT-CAPACITY.md
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-FEASIBILITY.md
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY.md
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESEARCH-CHECKPOINT-20260917.md
```

The old head contains the detailed certificates/verifiers/source notes. Do not copy them wholesale into this PR unless the active replacement theorem actually consumes them.

## 2. Load-bearing survivor to preserve

The displayed genus-one span-five arithmetic ray is

```text
D_l = 7*l*H - 4*l*sum_(p in Sigma) E_p,
|Sigma|=14,
d=112*l,
l>=1.
```

For the dangerous balanced packet:

```text
r_i=M_i=8*l on the 14 supported nodes,
all branches FSM-minimal,
R=R8=M=r_odd=d=112*l.
```

The retained Picard calculation gives

```text
D_l^2 = 336*l^2,
Delta_total = 168*l^2 + 56*l.
```

This ray is an honest integral Picard-class ray. What is *not* proved is effectivity, irreducibility, or existence of an actual low-normalization-genus carrier realizing the prescribed singularity packet.

The fixed-component test already closes several support-hyperplane incidence types. For the displayed ray:

```text
incidence 24: closed;
incidence 20: closed;
incidence 19: closed;
incidence 14 orbit-size 96: closed;
incidence 16: exactly 32 + 64 balanced N=14 supports survive in the two analyzed orbits.
```

Do not redo these enumerations unless an input/source lock changes.

## 3. Already-searched / parked route ledger

The following routes have already been explored far enough that a future mainbatch must not restart them as fresh ideas without a new exact input.

### BLOCKED / PARKED: local conductor-sheet recovery

The e=2 work reduced the conductor ambiguity to the canonical relative bit

```text
chi_ij=(r_i*r_j)/h,
chi_ij=+1 <=> [lambda_(p;i,j)]=0,
chi_ij=-1 <=> [lambda_(p;i,j)]=[gamma_Q].
```

Downstairs invariant A1 branch data determine only the unordered pair of lifts and do not select the residual-sheet gluing. `eta=0`, common-cover existence, `E[2]` compression, determinant bits, and absolute square-root labels do not supply the missing pointwise conductor transition.

Status: `BLOCKED` as primary route. Re-enter only with a new source-locked normalization-preimage/trivialization adapter.

### BLOCKED / PARKED: Armstrong ambient H1/Picard route

The `X_H=(C8 x C8)/H_diag` route reduced the candidate fixed-element relations to 128 representatives and isolated source-completeness as the missing proof. Even if the H1 calculation succeeds, prior exploration did not by itself determine the singular-carrier conductor gluing.

Status: `BLOCKED` as primary route. Do not redo the rank/minor computation. Re-enter only if a new theorem/source proves the fixed-element completeness *and* gives a new bridge to the active global receiver.

### BLOCKED: cusp-width shortcut

The needed equality

```text
f1^{-1}(Cusps)=f2^{-1}(Cusps)
```

was not established. Divisor-class/product/Jacobian information does not imply equality of those effective supports.

Status: `BLOCKED` until that exact support equality is source-locked.

### DOMINATED / EXHAUSTED: counting-only recombinations

Already pushed without closing the balanced survivor:

```text
allocation/Hodge-A1 energy,
mod-4 parity,
determinant one-bit,
raw/special-grid Bezout capacities,
ordinary delta bounds,
adaptive-jet dimension bounds,
formal pair-sign cocycle constraints,
summed Riemann-Hurwitz / unit charging,
correlated 28-fibration capacity at the shallow level.
```

The 28-fibration shallow test would need aggregate branch charge `q>112`; one charge in every 28 maps gives only `q=28`, and the free first jet can generically avoid finitely many critical-slope conditions.

Status: `DOMINATED/BLOCKED` unless genuinely new coupled geometry is supplied.

### BLOCKED as direct compression: Stage34 / StageA2 fixed finite-cover pattern

The useful *design principle* survives: close the exact receiver by a replacement theorem rather than enumerating every descendant branch. But a direct fixed finite-cover compression is not presently available because the relevant cover degree and section space grow with `l`.

Status: direct transplant `BLOCKED`; replacement-theorem methodology remains `LIVE`.

### BLOCKED as sole obstruction: integral Picard realizability

Infinite arithmetic subsequences of all three hard sectors admit honest integral Picard classes compatible with the retained numerical interfaces. Therefore

```text
"the skeleton is not even an integral class in Pic(S)"
```

cannot be the closure theorem.

Status: `BLOCKED` as sole route. The remaining wall is effectivity/irreducibility/global low-genus realizability.

### HOLD: product-correspondence/common-cover compression

The old `1024 -> 128` compression counts Picard labels, not divisors; each surviving class still has a moving section space with size growing with `l` (recorded old estimate `h0(A box B)=(28*l-4)^2`).

Status: `HOLD`, not a uniform closure by itself.

## 4. Current replacement-theorem target

Do **not** return to a fixed finite cover whose size grows with `l`.

The active research target is one of the following two exact theorem shapes.

### Target A — all-l uniform exclusion

Prove that no effective irreducible curve in the displayed MB104 ray can have normalization genus one and the required balanced singularity/equality packet for **every** `l>=1`.

Preferred proof species include a genuinely global equisingular/Severi obstruction, effective-cone/Mori obstruction, global incidence theorem, or another invariant whose contradiction is uniform in `l`.

### Target B — large-l uniform exclusion plus finite remainder

Prove an explicit `L` such that

```text
l>L  => impossible
```

for the exact MB104 receiver, leaving only the finite range `1<=l<=L` for exact bounded verification.

This is acceptable even if no all-l theorem is found. It is the preferred fallback because it converts the growing family into an auditable finite backend without pretending the cover is fixed.

## 5. Quantitative leverage checkpoint

For the balanced uniform ray the retained shallow dimension/equality comparison was

```text
dim |lA| approximately 168*l^2 - 56*l + 7,
required delta/equality defect = 168*l^2 + 56*l,
nominal deficit approximately 112*l - 7.
```

This is only a leverage signal. Naive independent-jet counting is insufficient because superabundance may recover conditions. The next legitimate use is an **exact global** codimension/equisingular computation or theorem that controls superabundance uniformly.

Small `l=1,2,3` checks are allowed only as a cheap falsification/preflight for a proposed global model; they are not theorem credit.

## 6. Candidate ledger after the split

```text
LIVE:
  U1 = exact global equisingular/Severi codimension for the displayed ray, with superabundance controlled;
  U2 = effective-cone / Mori / nef test that becomes strictly negative for all l or all l>L;
  U3 = global incidence/singularity theorem forcing impossibility of Delta_total=168*l^2+56*l with normalization genus 1 on the exact support;
  U4 = replacement theorem giving explicit finite l<=L after a uniform large-l argument.

UNTESTED:
  U5 = asymptotic vanishing/stability theorem for the relevant ideal-sheaf linear systems on S;
  U6 = orbifold/log-surface inequality applied to the exact equality packet rather than only to node counts;
  U7 = a degeneration argument that preserves the MB104 receiver while making the linear system computable.

BLOCKED/PARKED:
  conductor residual-sheet recovery as primary route;
  Armstrong H1/Picard as primary route;
  cusp-width without exact support equality;
  counting-only/recharged RH/Bezout/jet arguments;
  direct Stage34/A2 fixed finite-cover compression;
  Picard integrality as the sole obstruction.

HOLD:
  product-correspondence/common-cover label compression.
```

Under the Cycle Exploration Safety Protocol, do not erase the `UNTESTED` candidates merely because one live route is selected.

## 7. Required next mainbatch behavior

1. Run ordinary `stage32mb-mainbatch` startup and resolve the current-main / embedded-authority drift before any credit-bearing research.
2. Use this ledger before repository or literature search.
3. Search only for the exact global theorem species U1–U7 or a genuinely distinct new candidate; do not repeat the parked searches above.
4. Prefer a route that can yield either an all-`l` contradiction or an explicit large-`l` bound.
5. If a candidate reduces to an already-blocked route, record the reduction and rotate immediately.
6. Keep this PR small; do not copy the archived 324-file history.

## 8. Firewalls

```text
MB104_complete=false
finite_degree_window_proved=false
receiver_credit=false
effectivity_credit=false
final_milestone_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```

This split is operational/research-state cleanup only.