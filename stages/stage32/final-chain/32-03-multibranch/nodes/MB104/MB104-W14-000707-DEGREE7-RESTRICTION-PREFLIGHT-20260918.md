# Stage32 MB104 — W14 active `000707` primitive restriction-map preflight — correction — 2026-09-18

Status: **DROP / ALREADY RESOLVED IN RETAINED ARCHIVE / NO CREDIT**

The initial wide-scan preflight independently reproduced the old finite-field pattern

```
rank_1097(jet)=220,
rank_1097(jet+Q0)=221,
rank_1097(jet+Q1)=221,
rank_1097(jet+Q0+Q1)=221,
```

and temporarily reduced the characteristic-zero problem to `rank=220 or 221`.

A subsequent archive-wide check found that this exact ambiguity had already been resolved at retained archive head

```
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

in

```
GENUS1-SPAN5-BALANCED16-000707-PRIMITIVE-RANK.md.
```

That retained leaf proves, over characteristic zero,

```
h0(A)=124,
h1(A)=4,
rank(jet_4)=220.
```

It does so by constructing the support-hyperplane multiple subspace of dimension `122` and two explicit Gaussian-integer degree-seven sections `F,G` outside it.

Moreover `F|Q0` is explicitly nonzero. Since `O_Q0(A)` is trivial, `Q0` is not fixed. The support stabilizer exchanges `Q0,Q1`, so both are nonfixed. Taking powers gives:

```
Q0,Q1 are nonfixed in |lA| for every l>=1.
```

Therefore W14 is not a live second-scan candidate.

The new p=1097 preflight is retained only as an independent reproduction of the modular rank pattern; it carries no new mathematical credit.

This correction also records the process error: wide-scan generation must check the retained archive by semantic keyword before promoting a rediscovered route.
