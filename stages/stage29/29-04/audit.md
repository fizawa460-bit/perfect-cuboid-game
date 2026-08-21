# Stage29-04 — adversarial audit

```text
AUDITED_PR=1309
AUDITED_SUBMISSION_HEAD=dd42e29ad6b91d532341e357fbd6e89a82e5cc42
AUDIT_VERDICT=PASS_AFTER_MATERIAL_REPAIR
```

## Scope

Fresh audit attacked the common physical host, exact Stage16–20 population masks, literal versus nonliteral survival ratios, theorem provenance, derived condition costs, the physical-Boolean versus F7 sign/Kummer relation, backflow semantics, controller preservation, and current-head CI classification.

## 1. Common physical host — PASS

The host

```text
U(B)={0<a<b<c, gcd(a,b,c)=1, sqrt(a^2+b^2+c^2)<=B}
```

matches the frozen primitive/canonical physical convention. The four predicates

```text
F_ab, F_ac, F_bc, S
```

are exact objectwise predicates on this host.

The exact population identifications survive:

```text
E1=M1, E1∩S=N1
E2=M2, E2∩S=N2
E3=M3, E3∩S=P
```

and in particular

```text
M3=(E3∩not S) disjoint_union P.
```

No global `P=0` assumption is used.

## 2. Material repair: 16 labels are not 16 certified nonempty partition blocks

The submission repeatedly called the `2^4=16` truth assignments "exactly 16 cells" of a partition. That wording is too strong if `cell`/`partition block` is read as nonempty. At least the perfect-cuboid mask is empty for every certified finite cutoff through `10^9`, and global nonemptiness of that mask is unknown. Other truth assignments are not all certified nonempty either.

Correct scope:

```text
FORMAL_BOOLEAN_MASK_COUNT=16
PAIRWISE_DISJOINT_LABELED_FIBERS=true
UNION_EQUALS_U=true
EMPTY_MASKS_ALLOWED=true
NONEMPTY_BOOLEAN_FIBER_COUNT_CERTIFIED=false
```

This is an exact exhaustive Boolean decomposition with possibly empty fibers, not a theorem that all 16 arithmetic types occur.

## 3. Nested-host semantics — PASS

The exact-face strata are disjoint. The legal literal face-survival ladder is

```text
H_ge1=M1 disjoint_union M2 disjoint_union M3
H_ge2=M2 disjoint_union M3
H_ge3=M3
H_ge3 subset H_ge2 subset H_ge1 subset U.
```

The corresponding space intersections are

```text
S∩H_ge1=N1 disjoint_union N2 disjoint_union P
S∩H_ge2=N2 disjoint_union P
S∩H_ge3=P.
```

Thus

```text
N1/M1, N2/M2, P/M3,
H_ge1/U, H_ge2/H_ge1, H_ge3/H_ge2
```

are literal subset ratios, while

```text
M2/M1, M3/M2, N2/N1, M3/N2
```

are not objectwise survival probabilities.

## 4. Theorem-surface provenance — PASS

Fresh source checks confirm the imported current surface:

```text
U(B) ~ pi/(36*zeta(3)) B^3
M1(B) ~ 3/(4*pi^2) B^2 log B
N1(B) ~ kappa/(24*pi) B(log B)^3
M2(B) ~ C_M2 B(log B)^5
B^(1/4) << N2(B) <<_epsilon B^(1/2+epsilon)
liminf M3(B)/B^(1/3) >= 27/(40*pi^2)
M3(B) <<_eta B(log B)^(5-eta), 0<eta<1/46
P(B)=0 through B=10^9 only as exact finite evidence.
```

Stage19 `final.md` independently proves `N2/M2 -> 0` by its fixed-finite-set split-prime parity sieve, in addition to the quantitative half-power upper interface. Stage28 `final.md` supplies the current stronger `N2` and `M3` construction scales.

### Small quantitative repair

Because the current Stage28 lower theorem has a positive liminf at exact scale `B^(1/3)`, division by `H_ge2~M2` gives the stronger current lower corridor

```text
H_ge3/H_ge2 >> B^(-2/3)(log B)^(-5)
```

with no epsilon loss required. The older epsilon-weakened Stage26 form remains true but is not the strongest current ledger entry.

## 5. Material repair: the physical predicates already have an exact pointwise F7 crosswalk

The submission correctly firewalled `16 != 64`, but it went too far by leaving the Boolean-to-F7 relation wholly unproved.

Use the already-audited F7 map

```text
[x:y:z]=[a^2:b^2:c^2]
```

and work on the physical chart `x=a^2 != 0`. The six projective Kummer ratios may be taken as

```text
y/x,
z/x,
(x+y)/x,
(x+z)/x,
(y+z)/x,
(x+y+z)/x.
```

For a physical integer-edge point,

```text
y/x=(b/a)^2          always Q-square
z/x=(c/a)^2          always Q-square
(x+y)/x Q-square     iff F_ab
(x+z)/x Q-square     iff F_ac
(y+z)/x Q-square     iff F_bc
(x+y+z)/x Q-square   iff S.
```

A nonnegative integer is a square in `Q` iff it is an integer square, so there is no rational-versus-integral gap here.

Therefore the same F7 morphism gives an exact pointwise squareclass crosswalk:

```text
R29-KUM4A=DISCHARGED_POINTWISE_PHYSICAL_TO_F7_COORDINATE_SQUARECLASS_CROSSWALK
```

This does **not** identify the 16 Boolean labels with 16 sign sheets or 16 fixed algebraic subcovers. A failed predicate carries an arbitrary nontrivial class in `Q*/Q*^2`, not one universal binary nontrivial value. The 16 labels record only trivial/nontrivial status of four variable squareclasses.

The remaining counting/geometric receiver is therefore split off as

```text
R29-KUM4B=OPEN_PHYSICAL_POPULATION_TO_SUBCOVER_COUNT_ADAPTER
```

and must still control:

```text
common algebraic host
YES-subcover versus NO-complement semantics
map direction
rational lift multiplicity/sign quotient
physical R-height
primitivity
canonical ordering
population multiplicity
```

So the correct audit state is

```text
BOOLEAN_16_EQUALS_SIGN_64=false
BOOLEAN_MASKS_ARE_SIGN_SHEETS=false
POINTWISE_KUMMER_SQUARECLASS_CROSSWALK=true
FULL_POPULATION_SUBCOVER_COUNT_ADAPTER=false
R29-KUM4=PARTIAL_DISCHARGE_KUM4A_DONE_KUM4B_OPEN
```

## 6. Derived condition-cost matrix — PASS after lower-corridor sharpening

The current certified consequences are

```text
H_ge1/U ~ 27*zeta(3)/pi^3 * (log B)/B
H_ge2/H_ge1 ~ (4*pi^2*C_M2/3) * (log B)^4/B
H_ge3/H_ge2 -> 0
H_ge3/H_ge2 >> B^(-2/3)(log B)^(-5)
H_ge3/H_ge2 = o((log B)^(-delta)) for each fixed delta<1/46
N1/M1 ~ (kappa*pi/18)(log B)^2/B
B^(-3/4)(log B)^(-5) << N2/M2 <<_epsilon B^(-1/2+epsilon)(log B)^(-5)
N2/M2 -> 0
P/M3 global scale unknown.
```

No local-sieve saving is multiplied with the separate quantitative upper theorem.

## 7. Backflow — PASS

The new pointwise F7 crosswalk is Stage29 synthesis and does not alter any frozen Stage16–28 theorem contract.

```text
TARGETED_BACKFLOW_REQUIRED_NOW=false
ACTIVE_BACKFLOW_QUEUE_SIZE=0
CONDITIONAL_BACKFLOW_WATCHLIST=[R29-KUM4B]
OLD_STAGE_CONTRACT_REPAIR_PROVED_NECESSARY=false
```

A later targeted addendum remains allowed only if 29-07 proves that a frozen old-stage contract itself must be extended or corrected.

## 8. Controller preservation — PASS

The canonical controller is synchronized at schema 16. PR #1308 is synchronized as merged at commit

```text
cbd02a38a173165228ebd9d062101535e9896115.
```

Fresh PR diff inspection confirms that no unrelated 29-02 audit metadata is deleted or rewritten. The controller changes are limited to current Stage29 state, the audited 29-04 record, the KUM4A/KUM4B refinement, backflow-watch refinement, and #1308 merge synchronization.

## 9. Current-head CI — nonblocking stale lock

The current-head workflow `Stage29-01 audit lock` is red. Fresh job logs show the failure is exactly

```text
assert controller["status"] == "29_01_AUDITED_PASS"
```

inside `stages/stage29/29-01/verify_29_01.py`, while the controller is intentionally at Stage29-04. The workflow does not test or reject the 29-04 population/Kummer content.

```text
CI_RED_CLASSIFICATION=STALE_STAGE29_01_LOCK_FALSE_POSITIVE
CI_CONTENT_BLOCKER=false
```

## 10. Routing

29-04 now supplies both the exact host/mask vocabulary and the pointwise squareclass identity needed for dependency deduplication. The next stage remains 29-05.

```text
CHECKPOINT29_04_AUDIT=PASS
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
BOUNDED_REPAIR=BOOLEAN_NONEMPTY_SCOPE_PLUS_POINTWISE_F7_CROSSWALK_PLUS_KUM4_SPLIT_PLUS_CURRENT_M3_LOWER_CORRIDOR
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
TARGETED_BACKFLOW_REQUIRED_NOW=false
CI_RED_CLASSIFICATION=STALE_STAGE29_01_LOCK_FALSE_POSITIVE
NEXT_ITEM=29-05_DEPENDENCY_EQUIVALENCE_ROUTE_OWNERSHIP_AND_DOUBLE_CHARGE_LEDGER
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
