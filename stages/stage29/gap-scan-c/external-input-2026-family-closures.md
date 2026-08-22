# Gap Scan C — 2026 external family/method input ledger

```text
STATUS=AUDIT_DISCOVERED_EXTERNAL_INPUT_PENDING_INDEPENDENT_CERTIFICATION
PRIMARY_EXECUTION_OWNER=29-13_A2_METHOD_TRANSFER_ACROSS_SURVIVING_ROUTES
NEW_ATTACK_ROUTE_CREATED=false
STAGE16_28_BACKFLOW_REQUIRED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Provenance and trust level

Fresh Gap Scan C audit found a public self-hosted 2026 source set that was not present in the current `perfect-cuboid-game` theorem/receiver ledgers:

```text
Lightman Chang, Independent Researcher
site=https://perfect-cuboid-problem.proof.weiqi.kids/
repo=https://github.com/weiqi-kids/perfect-cuboid-problem
repo_created=2026-05-27
repo_pushed_through=2026-07-30
```

These are **not** promoted here to certified theorem inputs. They are self-hosted preprints with reproducibility material, not source-locked peer-reviewed results in the current repository. The surrounding site also contains statements that conflict with the already-audited cuboid-surface ledger (for example describing the four-quadric cuboid model as smooth, whereas the audited canonical model has 48 `A1` nodes). Paper A's introduction also calls `(240,252,275)` the smallest Euler brick, while the standard smaller brick `(44,117,240)` is already used elsewhere in this project. Those issues do not by themselves refute the family arguments, but they make independent proof reconstruction mandatory.

Therefore every item below has status

```text
EXTERNAL_THEOREM_OR_METHOD_CANDIDATE_PENDING_INDEPENDENT_AUDIT
```

unless a narrower status is stated.

## 2. Paper A — Saunderson family closure candidate

Source:

```text
No perfect cuboid in the Saunderson family of Euler bricks
Lightman Chang
2026-05-27
https://perfect-cuboid-problem.proof.weiqi.kids/paper-a/paper.pdf
```

Claimed chain:

```text
Saunderson Euler-brick family
 -> square space-diagonal condition
 -> genus-3 palindromic curve
 -> rational lifting condition W^2-4=square
 -> C0: S^2=T0^4+72*T0^2+16
 -> Jac(C0): y^2=x^3-7*x+6 (Cremona 80a1)
 -> rank 0, torsion (Z/2)^2
 -> four rational C0-points only
 -> all reconstruct to T0=0/infinity degeneracies
 -> no perfect cuboid in the Saunderson family.
```

The elliptic-curve database datum is independently checkable, but the load-bearing issue for Stage29 is the complete algebraic map and reconstruction/boundary coverage from every Saunderson parameter to `C0`. This is exactly the kind of receiver to which the StageA2 method species could apply.

```text
R29-EXT-CHANG-A=EXTERNAL_FAMILY_CLOSURE_CANDIDATE_PENDING_RECONSTRUCTION_AUDIT
candidate_consumer=J12-PARAMETRIC
execution_owner=29-13
```

If verified, this would close one already-known thin family; it would not close the full endpoint or create a twelfth primary route.

## 3. Paper B — Case B at p=1 candidate

Source:

```text
No Perfect Cuboid in Case B at p=1, and the rank obstruction on the associated genus-five curve
Lightman Chang
2026-05-27
https://perfect-cuboid-problem.proof.weiqi.kids/paper-b/paper.pdf
```

The paper studies the one-parameter family

```text
(4q, q^2-4, 2(q^2-1)).
```

Its asserted endpoint exclusion uses the necessary space condition

```text
g^2=5*q^4+20.
```

Writing `Y=q^2` reduces this to a Pell/Lucas sequence. The paper cites the theorem that the only square Lucas numbers are `1,4`, leaving `q=1,2`, both degenerate. The same paper also records a genus-5 joint curve and claims `rank Jac = 5 = genus`, explaining why ordinary Chabauty--Coleman does not close that curve.

The family exclusion is plausible enough to require audit, but the Pell orbit, exact parameter domain, cited Lucas-square theorem, and reconstruction walls must all be source-checked before certification. The genus-5 isogeny decomposition also needs stronger proof checking than finite Frobenius agreement alone.

```text
R29-EXT-CHANG-B=EXTERNAL_FAMILY_CLOSURE_AND_METHOD_OBSTRUCTION_CANDIDATE_PENDING_AUDIT
candidate_consumer=J12-PARAMETRIC
execution_owner=29-13
```

## 4. Paper C — finite-window result only

Source:

```text
Rational-point obstructions on rank-positive fibers, with the resolution of Peschmann's open case (5,2)
Lightman Chang
2026
https://perfect-cuboid-problem.proof.weiqi.kids/paper-c/paper.pdf
```

Hostile source inspection finds an essential scope firewall. The paper's Theorem 6.1 explicitly proves only finite windows; Remark 6.2 says the all-multiples extension remains conjectural:

```text
rank-1 windows: 1 <= n <= 200
rank-2 windows: |a|,|b| <= 12
all-multiples statement = Conjecture 5.2
missing input = effective odd-multiplicity primitive-divisor theorem for the Face-3 numerator
```

Hence the title must not be read as unconditional global closure of the `(5,2)` fiber.

```text
R29-EXT-CHANG-C=FINITE_WINDOW_COMPUTATIONAL_METHOD_INPUT_ONLY
GLOBAL_FIBER_CLOSURE_CERTIFIED=false
candidate_consumer=J12-PARAMETRIC
execution_owner=29-13
```

This scope mismatch is itself a useful firewall for later source rematches.

## 5. Paper D — Szpiro/height structure candidate

Source:

```text
The Szpiro ratio of the perfect-cuboid elliptic family and the Z[sqrt(2)] location of its exceptional locus
Lightman Chang
2026-05-27
https://perfect-cuboid-problem.proof.weiqi.kids/paper-d/paper.pdf
```

The paper presents exact minimal-model/discriminant/conductor and `Z[sqrt(2)]` factorization claims for a cuboid elliptic family, plus Szpiro-ratio statements and an explicit warning that no Szpiro-free positive canonical-height lower bound is obtained. It explicitly claims no perfect-cuboid existence/nonexistence result.

This may be useful to the parametric/height theorem search, but every minimal-model and analytic-number-theory hypothesis must be independently checked before import.

```text
R29-EXT-CHANG-D=EXTERNAL_HEIGHT_STRUCTURE_CANDIDATE_PENDING_AUDIT
candidate_primary_consumer=J12-PARAMETRIC
secondary_relevance=G10-FULL-ENDPOINT
execution_owner=29-13
```

## 6. Paper E — Sophie–Germain prime subfamily closure candidate

Source:

```text
The Sophie-Germain sub-family of perfect cuboids contains no solution: a single-curve closure for all prime parameters
Lightman Chang
2026-05-27
https://perfect-cuboid-problem.proof.weiqi.kids/paper-e/paper.pdf
```

Theorem 1 claims unconditional exclusion of the two Sophie--Germain Case-B branches for every prime parameter `p`. The stated reduction reaches a genus-one quartic with Jacobian

```text
y^2=x^3-275*x+1750
Cremona 800a3
rank 1,
```

then uses a claimed complete integral-point enumeration. The only nondegenerate integral candidate decodes to `(p,q)=(11,71)` and fails the remaining third-face square condition.

The source itself limits the theorem to prime `p`; composite parameters are not closed. Before certification, 29-13 must verify the branch derivation, the complete integral-point computation rather than the displayed finite sieve, the elliptic-logarithm/height bounds, and the final reconstruction.

```text
R29-EXT-CHANG-E=EXTERNAL_PRIME_SUBFAMILY_CLOSURE_CANDIDATE_PENDING_AUDIT
candidate_consumer=J12-PARAMETRIC
execution_owner=29-13
```

## 7. Paper H and surrounding repository

The rank survey is empirical and receives no theorem status. The external GitHub repository also contains many exploratory proof notes and conjectural/failed routes. Those files are not bulk-imported as foundations merely because they are public or recent.

```text
R29-EXT-CHANG-H=EMPIRICAL_REFERENCE_ONLY
BULK_EXTERNAL_REPO_IMPORT=false
```

## 8. Gap Scan C consequence

The external set is material enough that the submitted `NONE_FOUND_SCOPE=...NO...EXTERNAL_INPUT...` cannot survive literally. It does **not** justify a new attack route, Stage16--28 backflow, or a roadmap reorder. The existing next item `29-13_A2_METHOD_TRANSFER_ACROSS_SURVIVING_ROUTES` is the natural place to source-audit and attempt exact adapters for A/B/D/E, with C retained at finite-window scope.

```text
GAP_SCAN_C_RESULT=FOUND_EXTERNAL_INPUT_REQUIRED
EXTERNAL_INPUT_CERTIFIED_THEOREM_COUNT_AT_GAP_SCAN_C=0
EXTERNAL_INPUT_PENDING_AUDIT_COUNT=5
NEW_PRIMARY_ROUTE_COUNT=0
ROADMAP_REVIEW_C=STILL_VALID
ROADMAP_REWRITE_REQUIRED=false
TARGETED_BACKFLOW_REQUIRED_NOW=false
NEXT_ITEM=29-13_A2_METHOD_TRANSFER_ACROSS_SURVIVING_ROUTES
```
