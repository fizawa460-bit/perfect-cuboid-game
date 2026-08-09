# Stage14-num-α6 — independent equality matrix and regression pack

> STATUS: `STAGE14_NUM_ALPHA6=COMPLETE_INDEPENDENT_EQUALITY_MATRIX_AND_REGRESSION_PACK`
>
> CLASSIFICATION: exact finite-enumeration validation; no asymptotic claim.

## Successful Actions audit

Dedicated Actions run `31313405668` succeeded.

### Direct algorithm-vs-algorithm raw-set checks

The merged alpha5 diagonal-first engine and the ordinary Stage14-num3 shared-hypotenuse / outer-Pythagorean enumerator produced exactly the same canonical `(a,b,c,d,mask)` sets at:

```text
B=1,000       objects=2
B=5,000       objects=15
B=20,000      objects=42
B=100,000     objects=89
B=200,000     objects=116
B=500,000     objects=188
```

Every row also matched when summarized through the ordinary num3 summarizer, and census nesting was checked.

### Large independent frozen matrix

Alpha5 was streamed once through `B=10,000,000`; its nested subsets matched independent frozen data in every checked field:

```text
B=2,000,000   source=num1   objects=356   (a,b,c)=(142,134,80)   T=0
B=5,000,000   source=num3   objects=531   (a,b,c)=(207,211,113)  T=0
B=10,000,000  source=num3   objects=720   (a,b,c)=(293,286,141)  T=0
```

For each row the following all matched:

- directional counts and total object count;
- object-key SHA-256;
- object+mask SHA-256;
- raw-edge count, active-vertex count and max degree;
- vertex-ledger SHA-256;
- edge-ledger SHA-256.

The B=10m alpha5 stream retained 482,002 diagonals from 10,000,000 scanned and completed in 80.37 s on this GitHub runner. This is an environment-specific engineering observation only, not yet the formal crossover comparison.

## Interpretation

Alpha is no longer supported only by one B=2m regression. It now agrees with a genuinely different enumerator on six direct raw-set cutoffs and with independently frozen num1/num3 ledgers through B=10m.

This validates exactness, not an asymptotic theorem and not yet a speed victory over the production ordinary-num workflow.

```text
STAGE14_NUM_ALPHA6=COMPLETE_INDEPENDENT_EQUALITY_MATRIX_AND_REGRESSION_PACK
SMALL_RAW_OBJECT_MASK_SETS_EQUAL_NUM3=true
B2M_NUM1_ALL_HASHES_AND_GRAPH_MATCH=true
B5M_NUM3_ALL_HASHES_AND_GRAPH_MATCH=true
B10M_NUM3_ALL_HASHES_AND_GRAPH_MATCH=true
CENSUS_NESTING_CHECKED=true
INDEPENDENT_NUM3_SUMMARIZER_USED=true
FINITE_DIAGNOSTIC_ONLY=true
MEANINGFUL_END_TO_END_SPEEDUP_PROVED=false
NEXT=Stage14-num-alpha7 benchmark ordinary num versus alpha end-to-end crossover
```
