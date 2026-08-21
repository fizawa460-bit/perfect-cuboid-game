# Stage29-num audit — PR #1291

```text
AUDIT_TARGET=Stage29-num1 extension through B=10^9
PR=1291
AUDITED_CONTENT_HEAD=f6070e3eab91dffa3861d523e122d5c77d536b3a
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM=true
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Scope

Fresh hostile audit of the exact finite primitive canonical Euler-cuboid census extension from `R<=5*10^8` to `R<=10^9`, including the complete enumerator, exact arithmetic range, regression/independent checks, `P(B)` finite endpoint test, numerical-ledger synchronization, and the correction of the inherited provisional `N2` comparison series.

## Population and completeness audit

Accepted population:

```text
M3(B) = primitive canonical physical cuboids with all three face diagonals integral,
        no space-diagonal integrality requirement,
        R^2=a^2+b^2+c^2<=B^2.
```

The repository canonical convention is strict physical ordering `0<a<b<c` after sorting. The enumerator internally uses `a` for the unique odd edge rather than the smallest sorted edge; this is only an internal coordinate choice.

Completeness proof checked:

1. In an Euler cuboid, two odd edges cannot share an integral face diagonal because their squared sum is `2 mod 4`; a primitive cuboid cannot have all three edges even. Hence every primitive Euler cuboid has exactly one odd edge.
2. For fixed odd edge `a`, every even partner `y` with `a^2+y^2=h^2` satisfies `(h-y)(h+y)=a^2`. Writing `d=h-y<a` gives uniquely
   `y=(a^2/d-d)/2`, so enumerating all proper divisors `d<a` of `a^2` enumerates every possible even partner.
3. Pairing the two even partners once, testing their mutual face diagonal by an exact square test, and imposing `gcd(a,b,c)=1` therefore counts each physical permutation class exactly once.
4. Equal even partners cannot be an accepted Euler cuboid because `2b^2` is not a nonzero integer square, so the strict canonical chamber loses no object.

Verdict:

```text
COMPLETE_ENUMERATION_ROUTE_AUDIT=PASS
KNOWN_FAMILY_ONLY=false
PRIMITIVE_AUDIT=PASS
CANONICAL_MULTIPLICITY_AUDIT=PASS
```

## Integer-safety audit at B=10^9

- every edge is at most `10^9`, hence each edge square is at most `10^18` and fits `uint64_t`;
- `b^2+c^2<=2*10^18 < 2^64`, so the third-face square-test input is safe in `uint64_t`;
- `R^2` is accumulated in `__uint128_t` and compared exactly with `B^2`;
- once accepted under `R^2<=B^2`, conversion back to `uint64_t` for the exact space-diagonal square test is safe because `R^2<=10^18`;
- the square routine uses floating `sqrt` only as an initial guess and adjusts using exact `__uint128_t` products before acceptance;
- for factoring odd `a<=10^9`, every composite has a smallest prime factor below `sqrt(10^9)<31623`, so the `uint16_t` SPF entries are sufficient.

```text
INTEGER_ARITHMETIC_AUDIT=PASS
OVERFLOW_AUDIT=PASS_AT_B_LE_1E9
CUTOFF_AUDIT=PASS_EXACT_R2
SPACE_DIAGONAL_TEST_AUDIT=PASS_EXACT
```

## Count and independent-validation audit

Accepted exact cumulative checkpoints:

```text
M3(10^4)=18
M3(5*10^4)=42
M3(2*10^5)=82
M3(10^6)=219
M3(5*10^6)=480
M3(10^7)=656
M3(5*10^7)=1298
M3(10^8)=1757
M3(2*10^8)=2339
M3(5*10^8)=3331
M3(10^9)=4362
```

The independent Resta/Helenius/OEIS aligned-table checker revalidates 3556 records and all committed checkpoints through `5*10^8`. It is correctly not claimed as an independent completeness certificate for the new `10^9` endpoint.

The `10^9` endpoint is instead certified by the mathematically audited complete enumerator and repeated current-head CI execution.

Final repaired current-head numerical CI:

```text
WORKFLOW=Stage29 num1 M3 census
RUN=32446320974
HEAD=f6070e3eab91dffa3861d523e122d5c77d536b3a
CONCLUSION=SUCCESS
PRODUCTION_ASSERT=M3(10^9)==4362
PRODUCTION_ASSERT=P(10^9)==0
PRODUCTION_ARTIFACT=9434207157
PRODUCTION_ARTIFACT_SHA256=42d918f0192b9494cd3224f2aa13ed93faa520987767a0f3a11b58dcdfa0d675
CROSSCHECK_ARTIFACT=9434206918
CROSSCHECK_ARTIFACT_SHA256=ffc97f0c0ee45fe18db14037298edb3314d61a3950fec6abd86272ed81cabe2b
```

`Stage29-01 audit lock` remains red on Stage29-wide changes because its historical verifier still asserts the old 29-01 top-level controller state. This is the already-classified stale-lock false positive and is unrelated to the numerical census.

## Bounded repairs made by this audit

### Repair 1 — production endpoint regression strength

The submitted workflow recomputed `B=10^9` but only asserted `M3>=3331`. That would allow a future regression to change the exact endpoint while CI stayed green.

Repaired to require exactly:

```text
algorithm=stage29-num1-odd-edge-divisor-v2
B=1000000000
M3=4362
P=0
```

The repaired workflow then passed a fresh full `10^9` census.

### Repair 2 — strict canonical wording

The manifest said `a<=b<=c`, while the repository physical canonical convention is `0<a<b<c`. Equality is impossible for a nondegenerate Euler cuboid, so no count changed, but the contract wording was restored exactly. The manifest now also states that the enumerator's internal `a` is the unique odd edge, not necessarily the smallest sorted edge.

## N2 diagnostic correction audit

The extension correctly retracts the inherited provisional series

```text
N2 = 5,8,10,15,17,18,27
```

because it is not the frozen Stage19 population. `stages/stage19/final.md` certifies

```text
N2(500000000)=3495
```

for primitive canonical exactly-two-face cuboids with integral space diagonal under the same `R<=B` cutoff.

Therefore removing the provisional `N2` values and all derived `M3/N2` diagnostics is required. This correction does not affect any `M3` count.

```text
N2_PROVISIONAL_SERIES_RETRACTION_AUDIT=PASS
M3_COUNTS_AFFECTED=false
MATCHED_N2_PANEL_DEFERRED=true
```

## Endpoint firewall

The complete M3 census finds no object with integral space diagonal through the audited cutoff, so

```text
P(B)=0 for B<=10^9
```

is accepted as exact finite exhaustive evidence only. It is not a theorem that perfect cuboids do not exist.

```text
P_FINITE_ZERO_THROUGH_B=1000000000
P_GLOBAL_ZERO_THEOREM=false
ASYMPTOTIC_M3_EXPONENT_INFERRED=false
EVENTUAL_M3_N2_ORDERING_INFERRED=false
```

## Final verdict

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
BOUNDED_REPAIRS=2
CONTENT_DEFECT_REMAINING=false
M3_1E9=4362
P_1E9=0
N2_PROVISIONAL_SERIES_RETRACTED=true
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_NUM_ACTION=dedicated canonical N2 matched-cutoff panel if desired
```
