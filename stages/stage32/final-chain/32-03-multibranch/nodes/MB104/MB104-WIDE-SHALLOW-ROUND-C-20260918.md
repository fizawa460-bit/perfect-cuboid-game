# Stage32 MB104 — wide shallow closure scan Round C — corrected — 2026-09-18

Status: **ROUND C COMPLETE / ALL FIVE DROP / NO MATHEMATICAL CREDIT**

## Corrected result

```
W7   cyclic/abelian-cover BMY       DROP
W9   finite-characteristic route    DROP
W12  explicit degeneration          DROP
W13  stable factorization           DROP / merged into W14
W14  zero-quartic restriction map   DROP / already retained and resolved
```

No route is DEEP and no second-scan survivor remains.

## W7

The smooth cyclic-cover BMY slack is

```
3c2(Y)-K_Y^2
 =224n
  +112(n-1)l
  +336 (n-1)(2n+1)/n * l^2 >0
```

for every `n>=2,l>=1`. A contradiction would need new singular cover corrections of quadratic size. DROP.

## W9

The exact ray is already effective in characteristic zero. Bare specialization does not preserve the integral normalization-genus-one multibranch receiver strongly enough; an exclusion would need a compactified receiver/stable-map adapter. DROP.

## W12

Flat degeneration preserves Hilbert polynomial, not integrality, normalization genus, or the exact branch packet. Nonexistence of the same integral carrier shape on a special fiber is not reversible. DROP.

## W13

In the retained low-degree curve library, known conics pair positively with the active ray and the only null curves are the zero-pairing elliptic quartics. Thus stable factorization reduces to W14 unless a new effective-cone theorem is introduced. DROP as an independent route.

## W14 correction — already solved in retained archive

The initial wide scan independently reproduced the old modular pattern and temporarily left

```
rank_Q(i)(jet_4) in {220,221}.
```

An archive-wide semantic check then found the retained leaf

```
GENUS1-SPAN5-BALANCED16-000707-PRIMITIVE-RANK.md
```

at archive head

```
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11.
```

It already proves exactly

```
h0(A)=124,
h1(A)=4,
rank_Q(i)(jet_4)=220.
```

Two explicit characteristic-zero degree-seven sections `F,G` supplement the 122-dimensional support-hyperplane multiple space.  Moreover `F|Q0` is explicitly nonzero.  By the support-stabilizer symmetry, both active zero quartics are nonfixed; powers give this for every `l>=1`.

Therefore W14 is completely exhausted and is **not** a second-scan candidate.

## Process correction

Before any future wide-scan candidate is promoted, perform a semantic archive check against retained MB104 leaves. Filename-only recall was insufficient here and caused one rediscovery.

Round D must contain only genuinely untested direct-closing mechanisms.
