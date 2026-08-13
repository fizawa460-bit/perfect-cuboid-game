# Stage14-num-α2 — reference implementation and exact overlap

> STATUS: `PENDING_GITHUB_ACTIONS_FINAL_LOCK`
>
> CLASSIFICATION: exact finite cross-validation only; no asymptotic or performance claim.

## 1. What was implemented

`stages/stage14/scripts/14-num-alpha2/alpha_reference_overlap.py` is a deliberately simple implementation of the α1 dictionary.

It builds, for each space diagonal `d<=B`, the table of all positive Pythagorean representations

```text
d^2 = u^2 + v^2,
```

retains both ordered role assignments `(edge, opposite-face-diagonal)`, tests every pair of ordered roles for a positive-square residual

```text
c^2 = d^2-a^2-b^2,
```

then canonicalizes the reconstructed edge triple and recomputes the full three-face mask.

No perfect-cuboid-only mod-11/mod-19 pruning or historical incomplete Face-cuboid filter is used.

## 2. Independent overlap target

For small cutoffs the script calls the ordinary `14-num3` enumerator with one chunk and compares the **full canonical object set** rather than counts only.

Frozen small cutoffs:

```text
B=1,000      objects=2
B=5,000      objects=15
B=20,000     objects=42
B=100,000    objects=89
```

At each cutoff the required comparison is exact set equality of `(a,b,c,d,mask)` records.

The two algorithms enumerate in different orders:

```text
ordinary num3:
  shared face hypotenuse -> outer Pythagorean triple -> second-face gate

num-alpha2:
  fixed space diagonal -> representation table -> ordered-role collision
```

so the overlap is a useful architectural cross-check.

## 3. Frozen B=2,000,000 regression target

The α reference output at the frozen num1 cutoff is required to reproduce:

```text
N_a^(2)=142
N_b^(2)=134
N_c^(2)=80
N2=356
T=0
active oriented faces=490
raw pair edges=356
max graph degree=9
```

and all four frozen hashes:

```text
object key        1869ce6d30b661a3ea53049f2c86ffda5dd3d23b14aa9511301d72b1d4e8a89a
object + mask     84ce4239d482207ef8d961514c06b966f2eb9043fbbd5be3a7aea83d779314ce
active face       0c91e088324a703253cf7c100569eb25971135a4481512de1f63aa7657396e5b
raw edge          cd8f0ffa7d26ce38e316b65644bb25d39857b5d074a8bb1b96db2e05e8714a1f
```

These are read directly from the merged `14-num1` baseline manifest by the audit script.

## 4. What α2 does and does not establish

If the dedicated Actions audit passes, α2 establishes a finite implementation-level lock that the α1 collision dictionary reproduces the existing Stage14 `>=2-face` census semantics, including graph/face ledgers, at the tested ranges and at the frozen B2m hash anchor.

It does **not** yet establish that α is faster in the intended large range. The α2 representation generator deliberately uses a simple Euclid/scaling table. Generation strategy and asymptotic engineering belong to α3 and α7.

## 5. Decision pending CI

```text
STAGE14_NUM_ALPHA2=PENDING_GITHUB_ACTIONS_FINAL_LOCK
ALPHA_REFERENCE_EQUALS_EXISTING_NUM_OBJECT_KEYS=PENDING_CI
ALPHA_REFERENCE_EQUALS_EXISTING_FACE_MASKS=PENDING_CI
ALPHA_REFERENCE_EQUALS_EXISTING_RAW_EDGES=PENDING_CI
ALPHA_REFERENCE_EQUALS_EXISTING_ACTIVE_FACES=PENDING_CI
ALPHA_REFERENCE_B2M_FOUR_HASH_LOCKS_MATCH=PENDING_CI
MEANINGFUL_SPEEDUP_PROVED=false
FINITE_DIAGNOSTIC_ONLY=true
NEXT=Stage14-num-alpha3 after CI success
```
