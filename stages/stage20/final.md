# Stage20 final — primitive canonical Euler-cuboid population

BUNDLE_ID=STAGE20-FINAL-SELF-CONTAINED-20260814-R01
STATUS=REPAIR_REQUIRED_AFTER_FRESH_AUDIT_FAIL
AUDIT_VERDICT=FAIL
AUDIT_PERSISTENCE_STATUS=COMMITTED
FRESH_AUDIT_REQUIRED=true

## 1. Population contract

For `B>0`, Stage20 counts

\[
\mathcal E_3(B)=\{(a,b,c)\in\mathbf Z_{>0}^3:
0<a<b<c,\ \gcd(a,b,c)=1,\ R=\sqrt{a^2+b^2+c^2}\le B,
\]
\[
a^2+b^2,\ a^2+c^2,\ b^2+c^2\text{ are all integer squares}\}.
\]

Define

\[
M_3(B)=\#\mathcal E_3(B).
\]

No integrality condition is imposed on `R`. Stage20 is the Euler-cuboid population, not the perfect-cuboid endpoint.

## 2. Certified finite baseline

The Stage20 checkpoint20 enumerator gives

```text
B:       50  100  200  400  800  1200  1600  2000
M3(B):    0    0    0    1    3     5     5     7
```

A compatible earlier Stage14-e exact census under the same primitive/canonical Euclidean cutoff extends the finite evidence, including

```text
M3(2000)=7
M3(10000)=18
M3(50000)=42
M3(200000)=82
M3(1000000)=219
```

These are computed facts only. Effective power fits and the visually persistent square-root scale are not asymptotic theorems.

## 3. Strongest certified upper theorem

Repository-wide reuse preflight identifies Stage14-e11 / PR #188 as the strongest audited exact-population upper theorem.

For every fixed

\[
\eta<1/46,
\]

one has

\[
\boxed{M_3(B)\ll_\eta B(\log B)^{5-\eta}.}
\]

A convenient endpoint-free concrete form is

\[
\boxed{M_3(B)\ll B(\log B)^{5-1/50}.}
\]

The endpoint `eta=1/46` is not claimed.

### Provenance layers

- Stage14-e8: K3 model and independent divisor envelope
  \[
  M_3(B)\ll B\log B\exp(O(\log B/\log\log B))=B^{1+o(1)}
  \]
  as an upper envelope.
- Stage14-e10: degree-two thin-cover theorem gives
  \[
  M_3(B)\ll B(\log B)^{5-\eta_{EB}}
  \]
  for some unspecified `eta_EB>0`.
- Stage14-e11: makes the saving explicit for every fixed `eta<1/46` and independently proves a growing-prime Selberg-sieve bound
  \[
  M_3(B)\ll B(\log B)^5/(\log\log B)^2.
  \]

The e11 thin-cover bound is the strongest currently certified project upper statement.

## 4. Certified lower theorem and infinitude

For every even integer `m>=10`, set

\[
u=m^2-1,\qquad v=2m,\qquad w=m^2+1
\]

and

\[
A=u|4v^2-w^2|,\qquad
B_1=v|4u^2-w^2|,\qquad
C=4uvw.
\]

Checkpoint50a proves internally that:

- all three face diagonals are integral;
- `gcd(A,B_1,C)=1`;
- after canonical sorting, `0<B_1<C<A` for `m>=10`;
- distinct allowed `m` give distinct canonical objects;
- the Euclidean space length satisfies `R<31m^6`.

Therefore, for all sufficiently large cutoff `B`,

\[
M_3(B)\ge
\left\lfloor\frac12(B/31)^{1/6}\right\rfloor-4,
\]

and hence

\[
\boxed{M_3(B)\gg B^{1/6}.}
\]

In particular the Stage20 primitive/canonical Euler population is infinite.

## 5. Current certified envelope

Combining the lower family with Stage14-e11 gives

\[
\boxed{
B^{1/6}\ll M_3(B)\ll B(\log B)^{5-1/50}.
}
\]

More generally, the upper bound may use any fixed `eta<1/46`.

This determines neither the true exponent nor an asymptotic formula. The finite square-root signal remains consistent with the interval but unproved.

## 6. Causal decomposition

The Stage20 third-face condition is not modeled as an independent random-square event.

### 6.1 Two-face host

The source geometry is the shared-edge double-Pythagorean host already resolved in the Stage14-e / Stage18 line.

### 6.2 K3 thin cover

Adding the third-face equation produces a geometrically nontrivial degree-two cover of the toric two-face base. After normalization/minimal resolution the compactified Euler-brick surface is a K3 surface. This explains why the third-face subset is thin but arithmetically rich rather than a naive independent square test.

### 6.3 Exact local blockers

Stage14-e10 proves exact local blocker masses

\[
\delta_2=2/9,
\]

and for odd primes

\[
\boxed{
\delta_p=\frac{2(p-\chi_4(p))}{p^2+6p+1}
=\frac2p+O(p^{-2}).
}
\]

Their product has sieve dimension two. These blockers give an independent zero-density mechanism and a growing-prime log-log saving, but they do not identify the true global exponent.

### 6.4 Explicit survival

The Saunderson family proves that the K3/local obstructions do not annihilate the population: infinitely many primitive/canonical Euler objects survive, quantitatively at least on the `B^(1/6)` scale.

### 6.5 No double charge

The thin-cover theorem, local residue blockers, divisor projection, and explicit family play different proof roles. They are not multiplied as if independent probabilities.

## 7. Intrinsic status

```text
POPULATION_INFINITE=true
POSITIVE_POWER_LOWER_BOUND_PROVED=true
CERTIFIED_LOWER_EXPONENT=1/6
STRONGEST_EXPLICIT_UPPER_LOG_SAVING=eta_any_lt_1/46
CONCRETE_UPPER_ETA=1/50
TRUE_EXPONENT_IDENTIFIED=false
MATCHING_LOWER_BOUND_PROVED=false
ASYMPTOTIC_FORMULA_PROVED=false
ASYMPTOTIC_CONSTANT_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
```

Checkpoint30's growth-law OPEN_GATE therefore remains valid but narrower than at submission: the population is known to be infinite and quantitatively growing; only its true asymptotic law remains open.

## 8. Downstream reusable interfaces

Stage20 exports three stable interfaces in `docs/stage20-arsenal.md`:

```text
S20-W01_EXPLICIT_EULER_THIN_COVER_UPPER
S20-W02_PRIMITIVE_SAUNDERSON_LOWER
S20-W03_EULER_LOCAL_BLOCKER_LAW
```

Expected receivers are Stages26, 27, and 28.

Stage26 owns the actual `Stage18 -> Stage20` conditional ratio and independence classification. Stage20 does not pre-claim that transition result, even though the frozen Stage18 asymptotic and the Stage20 upper interface are ready inputs.

## 9. Repository-wide reuse preflight

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=true
STRONGER_PRIOR_RESULT=Stage14-e11_PR188
```

The numerical observatory is not a direct Stage20 population match because its principal census is integral-space-diagonal prefiltered. Its finite triple record is not a Stage20 Euler count and is never used as perfect-cuboid nonexistence evidence.

## 10. Open gates

```text
OPEN_GATE_1=STAGE20_POPULATION_GROWTH_LAW_UNRESOLVED
OPEN_GATE_2=TRUE_EXPONENT_UNRESOLVED
OPEN_GATE_3=MATCHING_LOWER_BOUND_UNRESOLVED
OPEN_GATE_4=ASYMPTOTIC_CONSTANT_UNRESOLVED
OPEN_GATE_5=SQRT_B_SIGNAL_THEOREM_STATUS_UNRESOLVED
```

Resolving these requires genuinely new research beyond bounded Stage20 closeout.

## 11. Frozen nonclaims

Stage20 does **not** prove or assume:

- an integral space diagonal;
- existence or nonexistence of a perfect cuboid;
- `M_3(B)~C B^alpha`;
- `M_3(B)\asymp B^(1/2)`;
- a matching lower bound;
- the thin-cover endpoint `eta=1/46`;
- independence of the third-face condition from prior face conditions;
- a Stage18-to-Stage20 transition law.

## 12. Fresh-audit repair requirement

The Stage20-70 fresh audit found the mathematical synthesis substantively correct but the self-contained bundle incomplete under `SELF_CONTAINED_REVIEW_STANDARD_V1`.

Required bounded repair:

1. transcribe the proof-complete Stage20-50a derivation into this bundle, including the three face-square identities, primitivity, canonical inequalities, injectivity, and `R<31m^6` cutoff proof;
2. print exact frozen-upstream interface contracts for every load-bearing Stage14-e8/e10/e11 import, including theorem statement, population/cutoff/multiplicity match, measure-adapter status, quantifier-adapter status, and any relevant uniformity limitation.

No new theorem or computation is required. The existing OPEN_GATES are not reopened.

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_REVIEW_GATE=FAIL
REPAIR_SCOPE=EMBED_STAGE20_50A_PROOF_AND_PRINT_EXACT_STAGE14_E8_E10_E11_UPSTREAM_INTERFACES
NEW_THEOREM_REQUIRED=false
NEW_COMPUTATION_REQUIRED=false
ARSENAL_PROMOTION_REQUIRED=YES
SYNTHESIS_STOP_RULE_SATISFIED=YES
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
EVIDENCE_LEVELS_COMPLETE=YES
DEPENDENCY_LEDGER_COMPLETE=YES
DOUBLE_CHARGE_CHECK=PASS
AUDIT_VERDICT=FAIL
AUDIT_PERSISTENCE_STATUS=COMMITTED
FRESH_AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_CHECKPOINT=70
NEXT_STAGE=
```
