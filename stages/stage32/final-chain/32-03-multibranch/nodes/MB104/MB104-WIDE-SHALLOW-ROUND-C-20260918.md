# Stage32 MB104 — wide shallow closure scan Round C — 2026-09-18

Status: **ROUND C COMPLETE / W14 ONLY SECOND-SCAN SURVIVOR / NO MATHEMATICAL CREDIT**

## Result

```
W7   cyclic/abelian-cover BMY       DROP
W9   finite-characteristic route    DROP
W12  explicit degeneration          DROP
W13  stable factorization           DROP / MERGED INTO W14
W14  zero-quartic restriction map   PASS-TO-SECOND-SCAN
```

No route is DEEP.

## W7 — cyclic/abelian-cover BMY: DROP

For a smooth cyclic `n`-fold cover branched along a smooth divisor `C=nL` on `S`,

```
K_Y^2=n(K_S+(n-1)L)^2,
c2(Y)=n c2(S)-(n-1)e(C).
```

Using

```
K_S^2=16,
c2(S)=12 chi(O_S)-K_S^2=80,
C^2=336l^2,
K_S.C=112l,
```

the BMY slack is

```
3c2(Y)-K_Y^2
 =224n
  +112(n-1)l
  +336 (n-1)(2n+1)/n * l^2.
```

It is strictly positive for every `n>=2,l>=1`.

Thus cover amplification does not naturally reverse the H8 sign. A contradiction would have to come from detailed singular branch-cover corrections of quadratic size, not from the native cyclic-cover Chern slope.

**DROP.**

## W9 — finite-characteristic specialization: DROP

The exact ray is already effective in characteristic zero for every `l>=1`.

For a flat model, dimensions of section spaces can jump upward on special fibers, not provide a new zero-section obstruction against this known generic effectivity.

More importantly, the actual MB104 target is not mere effectivity: it is an integral curve with normalization genus one and an exact multibranch packet. Under specialization an integral curve may acquire reducible/nonreduced components and the normalization branches may collide. Nonexistence of the same geometric shape on one special fiber is therefore not reversible without a proper compactified receiver.

That would be adapter construction, which wide-scan mode forbids.

**DROP.**

## W12 — explicit degeneration: DROP

A flat degeneration preserves the Hilbert polynomial/arithmetic genus, but does not preserve:

```
integrality,
geometric genus of normalization,
the 14-node / 8l-branch packet,
distinct exceptional landing data.
```

So a hypothetical carrier may have a reducible or nonreduced stable limit. Proving that the special fiber has no *integral carrier of the same shape* would not exclude the original curve.

Again, repairing this needs a dedicated stable-map/packet compactification rather than a native closing theorem.

**DROP.**

## W13 — stable factorization: DROP / MERGED INTO W14

For the active balanced support, the retained explicit curve library gives

```
known conic:           D_l.Q >= 6l >0,
elliptic quartic:      D_l.Q >=0.
```

Equality occurs precisely on the active zero-pairing quartics.

Therefore among the source-complete known low-degree curves, the only plausible fixed components not already forced by negative intersection are exactly the W14 zero quartics.

A different universal fixed divisor would require a new effective-cone theorem.

So W13 is not an independent route at this stage.

**DROP / merge into W14.**

## W14 — zero-quartic restriction map: PASS TO SECOND SCAN

The historical size-48 computation had already settled the two size-48 orbits, but intentionally left active `000707` open.

The same exact degree-7 A1 four-jet algorithm was applied to

```
Sigma=000707000f0f
```

over the good prime

```
p=1097, i=341.
```

Result:

```
rank(jet)=220
rank(jet+Q0 evaluation)=221
rank(jet+Q1 evaluation)=221
rank(jet+Q0+Q1)=221.
```

The good-prime minor gives

```
rank_0(jet)>=220.
```

On the other hand

```
chi(O(A))=120,
h2(A)=0,
h1(A)>=3
```

from the retained connected null-union cohomology, so

```
h0(A)>=123,
rank_0(jet)<=344-123=221.
```

Hence the entire direct restriction problem is now:

```
rank_0(jet)=220 or 221?
```

If it is `220`, the augmented rank lower bound `221` proves a nonzero restriction. The support stabilizer is transitive on `Q0,Q1`, so both zero quartics are nonfixed; powers propagate this to every `l>=1`.

If it is `221`, the present preflight does not decide.

The same `220/221/221/221` pattern appeared at ten tested primes, but that repetition is exploratory and is not used as a characteristic-zero proof.

**PASS TO ONE SECOND SHALLOW TEST.**

## Round C disposition

Round C leaves exactly one narrow direct question, not an adapter:

```
exact characteristic-zero primitive jet rank = 220 or 221?
```

W14 gets one second shallow test in Round D, while Round D must still screen several new routes in parallel.
