# Stage29 GAP_SCAN_B / ROADMAP_REVIEW_B — fresh adversarial audit

```text
PR=1316
ORIGINAL_SUBMISSION_HEAD=5f4e29f3cfd4f0ddf298c44b57b65a754d809859
AUDIT_VERDICT=PASS_AFTER_MATERIAL_POSITIVE_REPAIR
MATERIAL_POSITIVE_REPAIR=STAGE14_ENDPOINT_COROLLARY_PLUS_COMPLETED_OWNER_LIVENESS_PLUS_LOC1_P2_EXECUTION_OWNERSHIP
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
```

## 1. Stage14 endpoint-bound hostile audit — VALID MISSED COROLLARY

The proposed implication survives from first principles.

Stage14 fixes the primitive canonical physical population

```text
0<a<b<c,
gcd(a,b,c)=1,
a^2+b^2+c^2=d^2,
d<=B,
```

and defines `N_j(B)` by the exact number of integral face diagonals. Hence

```text
T(B)=N_3(B)
```

is already the primitive canonical perfect-cuboid population inside the integral-space host.

### 1.1 The raw graph really contains triples

Stage14 Lemma 3.1 defines one simple graph on all physical raw two-face incidences under `d<=B` and proves exactly

```text
E(B)=N_2(B)+3T(B).
```

The coefficient `3` is objectwise: an exactly-two object has one unordered pair of integral faces, while an all-three-face object has the three distinct unordered pairs. The transcribed multiplicity-one proof shows that primitive normalization and orientation do not introduce an additional gluing multiplicity. Therefore

```text
3T(B)<=E(B)
```

without any assumption on existence or nonexistence.

### 1.2 The same E is the one bounded by the elliptic-fiber bridge

Lemma 3.2 is stated uniformly for every active graph vertex and gives

```text
max_F deg_B(F)=B^o(1)
E(B)<=1/2*V(B)*max_F deg_B(F)<<V(B)B^o(1).
```

This is the same `E(B)` from Lemma 3.1. The lemma explicitly says positivity, canonical chamber, integrality and third-face masks only delete points from the larger bounded-height elliptic set. There is no exactly-two subtraction before this estimate.

### 1.3 Proposition 3.3 and Lemmas 3.4–3.5 do not silently remove triples

Proposition 3.3 is a complete-host statement: every physical active face enters at least one retained decorated cell and all later masks are restrictive. Its prime allocation and dyadic strip are reversible up to only `B^o(1)` decoration/divisor multiplicity. The host is built before candidate fixing.

Lemmas 3.4–3.5 then reconstruct columns/rows inside this complete partition. Their physical-filter statements put parity, orientation, canonical and third-face conditions after reconstruction as rejecting filters. The reverse-reciprocal step is a divisor-many upper bound on the complete surviving cell, not an exactly-two-only count.

Thus an exactly-two mask may be applied when extracting `N_2`, but it is not used to define or shrink the `V(B)` complete host whose upper bound is proved. A perfect cuboid cannot disappear from the raw-incidence inequality merely because the final advertised theorem chooses the `N_2<=E` consequence.

### 1.4 Proposition 3.6 bounds the whole active-face measure

Proposition 3.6 exhausts the proportional/nonproportional balanced cells and concludes

```text
V(B)<<B^(1/2+o(1)).
```

It explicitly states that the cases are exhaustive bounds for the same physical active-face measure. The proof of Theorem 2.1 then combines

```text
E(B)<<V(B)B^o(1)
V(B)<<B^(1/2+o(1)).
```

The document itself adds that no subtraction of `3T(B)` and no assumption on perfect cuboids is required for this upper bound. That sentence is compatible with — and actually exposes — the missed corollary: the proof only *uses* `N_2<=E`, but the stronger positive inequality `3T<=E` is sitting in the same Lemma 3.1.

### 1.5 Exact corollary and quantifiers

Therefore

```text
3T(B)<=E(B)<<B^(1/2+o(1)),
T(B)<<B^(1/2+o(1)).
```

Equivalently, for every `epsilon>0` there exist constants `C_epsilon>0` and `B_epsilon>=1` such that for every real `B>=B_epsilon`,

```text
T(B)<=C_epsilon B^(1/2+epsilon).
```

(The harmless factor `1/3` is absorbed in `C_epsilon`.) This is only an upper bound. It gives neither `T(B)=0` nor existence, nonexistence, a lower bound, or an asymptotic.

```text
STAGE14_ENDPOINT_COROLLARY=VALID_MISSED_COROLLARY
INVALID_HIDDEN_FILTER=false
INVALID_MEASURE_MISMATCH=false
```

## 2. Stage14 T(B) equals Stage29 P(B)

Audited Stage29-04 uses

```text
U(B)={0<a<b<c, gcd(a,b,c)=1, R=sqrt(a^2+b^2+c^2)<=B}
E3 = all three face-square predicates
S  = R is an integer
P  = E3 intersect S.
```

On an endpoint object satisfying `S`, the Stage29 Euclidean radius is literally the integral space diagonal:

```text
R=d.
```

Thus Stage14 `C(B)` and Stage29 `U(B) intersect S` have exactly the same positivity, primitive normalization, canonical representative and cutoff. Adding all three face predicates gives a bijection, not merely a finite-to-one adapter:

```text
P(B)=T(B)
```

for every real `B>=1`. Consequently the strongest audited endpoint statement imported from Stage14 is

```text
FOR_EVERY_EPSILON>0:
P(B)=T(B)<<_epsilon B^(1/2+epsilon).
```

No height power is lost.

## 3. Why the corollary was missed in the ledgers

The relevant historical entries were inspected separately.

- `AR-004` records the exact identity `E=N_2+3T`, including that triples are retained.
- `AR-005` records the same raw-edge estimate `E<<VB^o(1)`.
- `AR-006` records only the advertised output `N_2<<B^(1/2+o(1))` and warns that it is not a perfect-cuboid existence theorem. It does not record the immediate upper bound on `T`.
- `AR-038` records a different exact shared-hypotenuse convolution with `C_prim=2N_1+4N_exact2+6N_3`; it does not supply or record the Stage14 endpoint upper bound.
- Stage28 does not record a global perfect-cuboid upper exponent.
- Audited Stage29-04 lists `P(B)=0` only through the finite census cutoff and explicitly leaves `P/M3` global scale unknown; its theorem-surface list contains no global `P(B)` upper bound.
- Stage29-07 supplies the exact primitive/canonical/population adapter but does not import this Stage14 consequence.

Hence this is not `ALREADY_RECORDED`. The proof was present, but the endpoint corollary was not promoted into the theorem surface.

## 4. Gap Scan B consequence — targeted backflow/addendum executed

The previous `GAP_SCAN_B_RESULT=NONE_FOUND` cannot survive unchanged. This is a material theorem-surface omission in a frozen old stage, so under the Stage29 anti-loop policy it is handled by a targeted addendum rather than rerunning Stage14.

The addendum is committed in this PR as

```text
stages/stage14/addenda/stage14-endpoint-corollary.md
```

and the Stage29 theorem-surface correction is recorded by

```text
stages/stage29/29-04/stage14-endpoint-upper-addendum.md
stages/stage29/gap-scan-b/stage14-endpoint-theorem-ledger.json
```

Therefore the scan result becomes

```text
GAP_SCAN_B_RESULT=FOUND_TARGETED_BACKFLOW_REQUIRED
TARGETED_BACKFLOW_TARGET=Stage14
TARGETED_BACKFLOW_ACTION=ENDPOINT_COROLLARY_ADDENDUM
TARGETED_BACKFLOW_EXECUTED=true
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
```

This does not require a roadmap reorder or a twelfth route. The certified theorem is an input to the existing `G10-FULL-ENDPOINT` portfolio at 29-10.

```text
ROADMAP_REVIEW_B=STILL_VALID
ROADMAP_REWRITE_REQUIRED=false
ATTACK_ROUTE_COUNT=11
ROUTE_COUNT_CHANGE=0
```

## 5. Previously found ownership repairs remain valid

The earlier Gap Scan B ownership audit is retained:

```text
R29-KUM5 -> Q11-MODULAR
R29-NF7  -> Q11-BRAUER
R29-NF3..NF6 -> DORMANT_INTERNAL_NOT_REQUIRED_FOR_CURRENT_ATTACK_ENTRY
R29-KUM-LOC1-P2 -> SUBSUMED_BY_R29-KUM-LOC2-2
R29-KUM-LOC2-2 -> J12-LOCAL-SQUARECLASS
```

After both the ownership repairs and the endpoint theorem import,

```text
POST_AUDIT_UNOWNED_ACTIVE_RECEIVER_COUNT=0
DUPLICATE_PRIMARY_EXECUTION_OWNER_COUNT=0
```

## 6. External mod 7 / mod 19 novelty check

The standard observations are not new.

Tim S. Roberts, *Some constraints on the existence of a perfect cuboid*, Australian Mathematical Society Gazette 37(1) (2010), 29–31, proves explicitly:

```text
Theorem 1: at least one edge of a perfect cuboid is divisible by 7.
Theorem 2: at least one edge of a perfect cuboid is divisible by 19.
```

The paper says these were previously unpublished at the time, and gives the modulo-square residue checks on page 30. Therefore any recent reviewer claim whose content is exactly those two divisibility statements is classified

```text
MOD7_STANDARD_EDGE_DIVISIBILITY=KNOWN_ROBERTS_2010
MOD19_STANDARD_EDGE_DIVISIBILITY=KNOWN_ROBERTS_2010
```

If the reviewer intended a stronger statement (for example, a prescribed edge, simultaneous divisibility, valuation, or residue-class refinement), that stronger wording was not supplied in the present audit request and remains `UNCERTAIN_UNTIL_EXACT_CLAIM_SUPPLIED`; it must not inherit novelty from the standard statement.

Source locator and bibliographic note are recorded in `mod7-mod19-literature.md`.

## 7. Final routing

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS_AFTER_MATERIAL_POSITIVE_REPAIR
CHECKPOINT_GAP_SCAN_B_AUDIT=PASS
STAGE14_ENDPOINT_COROLLARY=VALID_MISSED_COROLLARY
STAGE14_ENDPOINT_THEOREM=P(B)=T(B)<<_epsilon B^(1/2+epsilon)_FOR_EVERY_EPSILON>0
GAP_SCAN_B_RESULT=FOUND_TARGETED_BACKFLOW_REQUIRED
TARGETED_BACKFLOW_EXECUTED=true
TARGETED_BACKFLOW_REQUIRED_NOW=false
ROADMAP_REVIEW_B=STILL_VALID
ROADMAP_REWRITE_REQUIRED=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
ATTACK_ROUTE_COUNT=11
POST_AUDIT_UNOWNED_ACTIVE_RECEIVER_COUNT=0
NEXT_ITEM=29-10_GLOBAL_AND_K3_ATTACK_PORTFOLIO
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
