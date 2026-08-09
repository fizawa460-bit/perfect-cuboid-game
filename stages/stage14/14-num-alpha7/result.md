# Stage14-num-α7 — matched end-to-end crossover benchmark

> STATUS: `STAGE14_NUM_ALPHA7=PENDING_GITHUB_ACTIONS_FINAL_LOCK`
>
> CLASSIFICATION: finite engineering benchmark; exact census semantics retained; no asymptotic complexity claim.

## Goal

Decide whether the diagonal-first alpha engine has practical value over the ordinary Stage14-num3 engine, rather than merely optimizing one internal kernel.

## Matched benchmark contract

At

```text
B = 200,000; 500,000; 1,000,000; 2,000,000
```

run both complete census paths three times on the same GitHub runner:

1. alpha5: primitive-safe outer diagonal sieve -> Gaussian representations -> compressed collisions -> exact canonical object set -> num3 summary;
2. ordinary num3: one full shared-hypotenuse index -> streamed outer Pythagorean triples -> exact canonical object set -> num3 summary.

The execution order alternates by repeat (`alpha -> ordinary`, then `ordinary -> alpha`, then `alpha -> ordinary`). Every timed pair must produce exactly the same raw `(a,b,c,d,mask)` set and summary.

The ordinary comparator uses one chunk because the tested B<=2m range fits in memory. This is conservative for alpha in total single-process work: production num3 chunking reduces peak memory but repeats scans, while parallel chunk execution can reduce wall time using more workers.

## Speed verdict rule

Use median wall time over the three runs. Define a meaningful speed advantage as ordinary/alpha >= 1.25x (alpha at least 20% faster in elapsed time).

A formal tested crossover exists only if:

- two consecutive tested cutoffs satisfy >=1.25x; and
- the largest tested cutoff B=2m also satisfies >=1.25x.

The reported crossover is the first cutoff of that sustained run.

## Boundary

This benchmark may justify Stage14-num-alpha8 scaling, but it does not prove an asymptotic runtime exponent and does not change any mathematical Stage14 theorem claim.

```text
MEANINGFUL_END_TO_END_SPEEDUP_PROVED=PENDING_ACTIONS
FIRST_TESTED_SUSTAINED_20PCT_CROSSOVER_BOUND=PENDING_ACTIONS
NEXT_AFTER_SUCCESSFUL_CROSSOVER=Stage14-num-alpha8
```
