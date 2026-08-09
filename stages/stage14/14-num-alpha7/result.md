# Stage14-num-α7 — matched end-to-end crossover benchmark

> STATUS: `STAGE14_NUM_ALPHA7=COMPLETE_MATCHED_END_TO_END_CROSSOVER_BENCHMARK`
>
> CLASSIFICATION: finite engineering benchmark; exact census semantics retained; no asymptotic complexity claim.

## Goal

Decide whether the diagonal-first alpha engine has practical value over the ordinary Stage14-num3 engine, rather than merely optimizing one internal kernel.

## Matched benchmark contract

At

```text
B = 200,000; 500,000; 1,000,000; 2,000,000
```

both complete census paths were run three times on the same GitHub Actions runner, with alternating execution order:

1. alpha5: primitive-safe outer diagonal sieve -> Gaussian representations -> compressed collisions -> exact canonical object set -> num3 summary;
2. ordinary num3: one full shared-hypotenuse index -> streamed outer Pythagorean triples -> exact canonical object set -> num3 summary.

Every timed pair produced exactly the same raw `(a,b,c,d,mask)` set and the same summary.

The ordinary comparator uses one chunk because B<=2m fits in memory. This is conservative for alpha in total single-process work: production num3 chunking reduces peak memory but repeats scans, while parallel chunk execution can trade extra workers for lower wall time.

## Successful benchmark

Dedicated Actions run `31313797646` succeeded.

Median wall times over three repeats:

```text
B           alpha       ordinary     ordinary/alpha
200,000     0.77094 s   1.19282 s       1.547x
500,000     2.14000 s   4.12647 s       1.928x
1,000,000   4.67145 s   9.73921 s       2.085x
2,000,000  10.16144 s  22.69447 s       2.233x
```

All four tested cutoffs exceed the predeclared `1.25x` meaningful-speed threshold. Therefore the first tested sustained crossover is already `B=200,000`, and the advantage increases across this tested range.

At B=2m the exact output remained the frozen Stage14-num1 census:

```text
objects=356
N_a^(2),N_b^(2),N_c^(2)=142,134,80
T=0
raw edges=356
active oriented faces=490
max degree=9
```

## Decision

Alpha has demonstrated a real end-to-end single-process acceleration while preserving the exact census. This clears the roadmap gate for Stage14-num-alpha8 scaling beyond the ordinary rolling cutoff.

This remains an environment-specific finite engineering benchmark. It does not prove an asymptotic runtime exponent, and it does not by itself prove how alpha compares with a many-worker parallel ordinary-num deployment.

```text
STAGE14_NUM_ALPHA7=COMPLETE_MATCHED_END_TO_END_CROSSOVER_BENCHMARK
EXACT_EQUALITY_PRESERVED_IN_ALL_TIMED_RUNS=true
MEANINGFUL_END_TO_END_SPEEDUP_PROVED=true
FIRST_TESTED_SUSTAINED_20PCT_CROSSOVER_BOUND=200000
B200K_MEDIAN_SPEEDUP=1.547231744186713
B500K_MEDIAN_SPEEDUP=1.9282538104814864
B1M_MEDIAN_SPEEDUP=2.0848385194570214
B2M_MEDIAN_SPEEDUP=2.2333912566158074
FINITE_ENGINEERING_BENCHMARK_ONLY=true
ASYMPTOTIC_COMPLEXITY_CLAIM=false
NEXT=Stage14-num-alpha8 scale exact alpha census beyond ordinary rolling cutoff
```
