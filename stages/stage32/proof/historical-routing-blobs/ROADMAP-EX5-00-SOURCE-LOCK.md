# Stage32 — LOWGENUS-PICARD-PRODUCTION

```text
STAGE=32
KERNEL=K16-C2-LOWGENUS-PICARD-PRODUCTION
CHILDREN=R29-LG2,R29-LG2-EFF,R29-LG2-MB
PARENT_ROUTE=G10-LOWGENUS-PICARD
EXECUTION_CLASS=2
PERFECT_CUBOID_PROBLEM_STATUS=OPEN
```

## 0. Purpose

Stage32 closes, or reduces to a smaller exact residual, the remaining low-genus Picard-production Class-2 kernel frozen by Stage29.

The exact Stage29 wall is:

```text
symmetry-reduced effectivity-aware multibranch Picard-lattice enumeration
through the audited d<=176 / d<=192 windows
```

This is a finite/computational kernel, not a new-theorem claim.

Completion means a certified bounded census of low-genus positive-dimensional carriers in the audited scope. It does **not** imply that every endpoint rational point lies on such a carrier, does not exclude isolated rational points, and does not solve the Perfect Cuboid problem.

## 1. Why Stage32 is not a single monolithic raw search

Stage29 already proved mathematical finiteness but explicitly rejected naive tractability.

For the published degree-6 route, the upstream lifting kernel has rank 44 and its close-vector volume estimate scales like

```text
const * bound^(44/2) = const * bound^22.
```

Therefore Stage32 must not run a blind `CloseVectors` ball independently for every even degree up to 176/192.

Instead Stage32 uses large, checkpointed units. A single `Stage32-main-batch` invocation is allowed to continue through multiple units automatically when the preceding unit closes. It stops only at:

1. a precise smaller Class-2/tool/CAS wall;
2. a genuinely new-theorem wall that survives hostile classification;
3. the final Stage32 audit gate.

This gives one-command progress without hiding a giant non-resumable computation.

## 2. Frozen mathematical input

Let `S` be the smooth minimal resolution and `H=K_S` the canonical hyperplane class.

```text
Picard rank = 64
H^2 = 16
Aut(S) order = 1536
```

For an integral nonexceptional curve `C` with `d=H.C`, set

```text
r = gcd(d,16)
m = 16/r
n = d/r
y = m*C - n*H.
```

Then `H.y=0`, so `y` lies in the negative-definite `H^perp`, and

```text
C=(y+nH)/m
```

subject to exact divisibility in `Pic(S)`.

Audited finite windows:

```text
G0: geometric genus 0, even 2 <= d <= 176
G1: geometric genus 1, even 4 <= d <= 192
```

Norm bounds:

```text
G0: -y^2 <= m^2*(d^2/16 + d + 2)
G1: -y^2 <= m^2*(d^2/16 + d)
```

The known-curve rank-64 lattice constructed in the upstream Magma code is identified with the full geometric Picard group by the separately audited Testa--Stoll theorem package; the code's rank assertion alone is not the theorem proving fullness.

## 3. Source lock

Internal authoritative inputs:

```text
stages/stage29/29-02c-LG2/result.md
stages/stage29/29-02c-LG2/audit.md
stages/stage29/29-02c-LG2/finite-search-contract.md
stages/stage29/29-02c-LG2/computational-feasibility.md
stages/stage29/29-02c-LG2/upstream-code-lock.md
stages/stage29/29-15/open-receiver-triage.json
stages/stage29/29-16/active-kernel-ledger.json
stages/stage31/controller.json
```

Upstream computation lock:

```text
repo   = MichaelStollBayreuth/Verification
commit = 51233ed5ef2bf228fac9416c66db9adc0ebcaadd
file   = Cuboids/cuboids.magma
blob   = 0422b69847f2afb97cb7b3ed02ebef91279f61b1
license= GPL-3.0
```

Reusable upstream objects include the known curve/node configuration, `PicL`, `HinPicL`, automorphism/Galois actions, low-degree `CloseVectors` templates, K3 quotient/lift machinery, and known intersection filters.

Stage32 must independently reproduce any load-bearing numerical output it imports from this code.

## 4. Execution architecture

### 32-01-XL — production enumerator + complete unibranch numerical census

**Size: XL**

Target receiver:

```text
R29-LG2
```

Build a new production enumerator, rather than extending the degree-6 script blindly.

Required pruning before expensive vector enumeration:

1. exact Picard divisibility/coset restriction;
2. automorphism-orbit reduction using the order-1536 action;
3. exceptional-divisor intersection profiles;
4. Testa--Stoll Lemma 21 incidence bounds before enumeration wherever logically valid;
5. known irreducible-curve intersection inequalities;
6. subtraction of already classified degree <= 6 classes;
7. congruence/modular filters on Picard coordinates;
8. invariant/sign-involution strata where useful;
9. branch-and-bound over intersection coordinates instead of raw full balls;
10. exact orbit-canonicalization and duplicate certificates.

The enumerator must be resumable. At minimum checkpoint by

```text
(genus, degree, symmetry/intersection stratum)
```

and record:

```text
input lattice/hash
bounds
candidate counts before/after every filter
orbit representative counts
runtime
peak search state
code hash/version
completed strata manifest
```

A timeout or large count is not a mathematical result. It must resume from the last certified stratum.

#### 32-01 close criterion

For every even degree in both windows, produce a complete orbit list of every numerical Picard class satisfying the audited necessary conditions, with a machine-checkable completeness certificate.

```text
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=true
R29_LG2=DISCHARGED
```

Effectivity is intentionally **not** credited here.

#### 32-01 stop rule

If the complete enumeration cannot be made tractable with the existing exact lattice and current tools, expose the first precise missing algorithmic reduction as a smaller Class-2 leaf. Do not relabel a CAS/runtime limitation as Class 3.

---

### 32-02-L — rigorous effectivity certification

**Size: L**

Target receiver:

```text
R29-LG2-EFF
```

Consume only the complete survivor/orbit ledger from 32-01.

For every surviving numerical class, produce exactly one audited status:

```text
INEFFECTIVE_PROVED
KNOWN_BOUNDARY_OR_DEGENERATE
EXPLICIT_EFFECTIVE_CARRIER
```

Allowed evidence may include exact linear-system computation, Riemann--Roch plus certified vanishing where sufficient, ideal/elimination computation for an explicit carrier, decomposition against the known curve configuration, or another exact certificate. Necessary intersection inequalities alone are never an effectivity proof.

Every explicit carrier must include:

```text
field of definition
class in Pic(S)
degree
genre/genus data
irreducibility/integrality status
normalization behavior
physical-chamber status when meaningful
reconstruction locator
```

#### 32-02 close criterion

```text
UNKNOWN_EFFECTIVITY_SURVIVOR_COUNT=0
R29_LG2_EFF=DISCHARGED
```

If some finite classes remain undecided after all exact current methods are exhausted, replace `R29-LG2-EFF` by the smallest explicit Class-2 effectivity leaf; do not claim closure.

---

### 32-03-L — multibranch-at-node carrier ledger

**Size: L**

Target receiver:

```text
R29-LG2-MB
```

Freitag--Salvati Manni Theorem 3.1 applies only when normalization is bijective onto the singular image. Therefore multibranch curves at a node are outside the 176/192 cap and must be treated separately.

Stage32 must materialize the exact multibranch correction rather than silently reuse the unibranch bound.

Required work:

1. classify allowable normalization branch profiles above the 48 nodes for geometric genus 0 and 1 carriers;
2. express the arithmetic-genus / delta / node-incidence correction in the Picard and canonical-degree data;
3. quotient branch profiles by the exact surface automorphism action;
4. derive every finite degree or intersection restriction actually justified by the existing theorems;
5. run the corresponding symmetry-reduced Picard enumeration where finite;
6. apply the same effectivity/carrier certificate discipline as 32-02;
7. record explicitly any branch pattern not covered by a finite current theorem.

#### 32-03 close criterion

Either:

```text
MULTIBRANCH_LOW_GENUS_LEDGER_COMPLETE=true
R29_LG2_MB=DISCHARGED
```

or expose a strictly smaller residual and classify it honestly as Class 2 or Class 3 according to the first missing statement.

A genuinely missing uniform theorem may become Class 3 only after all finite branch/Picard work has been exhausted and the exact theorem-shaped wall is stated.

---

### 32-04-M — low-genus carrier synthesis and final certificate

**Size: M**

Combine the outputs of 32-01 through 32-03.

Produce:

```text
complete unibranch numerical census
complete effectivity disposition
complete multibranch ledger or exact smaller residual
explicit surviving carrier catalogue
physical-chamber annotations
independent verification scripts
reproducibility manifest
frontier delta
```

Permitted kernel outcomes:

```text
CLOSED_CERTIFIED_BOUNDED_LOWGENUS_CENSUS
SMALLER_CLASS2_RESIDUAL
CLASS3_EXPOSED
```

If all three receivers close:

```text
K16_C2_LOWGENUS_PICARD_PRODUCTION=CLOSED
```

But even in that case:

```text
G10_LOWGENUS_PICARD=AMBER
ENDPOINT_NONEXISTENCE_PROVED=false
ISOLATED_RATIONAL_POINTS_EXCLUDED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

No route recolor is authorized merely by completing the carrier census.

---

### 32-05 — final hostile audit and close

**Size: audit**

Freshly reconstruct:

1. exact Stage29 receiver semantics;
2. all degree/genus windows and norm formulas;
3. Picard divisibility/coset handling;
4. automorphism group action and orbit canonicalization;
5. filter soundness and completeness;
6. checkpoint coverage of every degree/stratum;
7. effectivity evidence for every survivor;
8. multibranch coverage and theorem scope;
9. independent checker outputs;
10. frontier accounting and all global firewalls.

Only this unit may set

```text
STAGE32_CLOSED=true
```

## 5. Main-batch continuation rule

`Stage32-main-batch` is deliberately not tied one-to-one to a unit.

Within one user invocation it may execute:

```text
32-01 -> 32-02 -> 32-03 -> 32-04
```

as far as time/tool limits permit, provided each completed unit writes its own immutable/reproducible checkpoint before continuing.

It must stop before 32-05 and request:

```text
Stage32-audit
```

It must also stop immediately if a precise residual wall is found.

This is the Stage32 version of the user's preferred "one-shot if possible" workflow, without turning a potentially large lattice computation into an unauditable monolith.

## 6. Firewall

The following implications are forbidden:

```text
finite numerical Picard list => effective curves classified
necessary intersection filters => effectivity
unibranch 176/192 census => multibranch census
low-genus carrier census => every rational point lies on a carrier
no low-genus carrier => no perfect cuboid
runtime exhaustion => Class3 theorem wall
```

Historical Stage29 artifacts remain frozen snapshots and are not rewritten when Stage32 closes a kernel.

## 7. Expected post-close frontier

Stage31 left:

```text
ACTIVE_KERNEL_COUNT=11
CLASS2_KERNEL_COUNT=2
CLASS3_KERNEL_COUNT=9
```

If Stage32 closes with no replacement residual:

```text
ACTIVE_KERNEL_COUNT=10
CLASS2_KERNEL_COUNT=1
CLASS3_KERNEL_COUNT=9
```

The sole remaining Class-2 kernel would then be the Brauer explicit DAG/chain kernel.

This frontier update is prospective until Stage32 final hostile audit passes.
