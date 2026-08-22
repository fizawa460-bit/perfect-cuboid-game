# Stage31 source lock — EXT-E-INTEGRAL-CERTIFICATION

## Internal audited authority

The Stage31 receiver is inherited from the audited Stage29 records:

```text
kernel = K16-C2-EXT-E-INTEGRAL-CERTIFICATION
receiver = R29-EXT-CHANG-E
parent = J12-PARAMETRIC
execution class = 2
```

Exact wall:

```text
integrality-preserving quartic-to-elliptic birational maps
plus a source-locked complete IntegralPoints/elliptic-logarithm certificate
```

Primary internal records:

```text
stages/stage29/29-13/external-source-audit.md
stages/stage29/29-13/theorem-dependency-ledger.json
stages/stage29/29-15/open-receiver-triage.json
stages/stage29/29-16/active-kernel-ledger.json
```

## External Paper-E snapshot

Repository:

```text
weiqi-kids/perfect-cuboid-problem
```

Pinned commit:

```text
bd3018b896c8ac15b56cadc382af1477dca9e97a
```

Pinned blobs:

```text
paper-e/paper.tex
  1ff42f5a657ab9edafcfd6060f015a19e4322a83

paper-e/scripts/01_identity_and_reduction.gp
  a117cf78176d6818d6dca99388e827bcc1e2269e

paper-e/scripts/01b_case_I_recheck.gp
  9db55907129920b96c7175419145a703271d0e5b

paper-e/scripts/02_curve_rank_label.gp
  b0c30169a920ef7ab6ba7040875ab8d99de5aa18

paper-e/scripts/03_integral_points.gp
  80a113d42641e474de01c1cbe1b15c06a9744892

paper-e/scripts/04_height_completeness.gp
  ba372d9c0a4f6fad2884ad192f5f64f85244396a
```

## Frozen starting equations

Paper E and the Stage29 audit agree on the target models:

```text
C_anom:
20 Z^2 = Y^4 + 8Y^3 + 18Y^2 - 8Y + 1

E_anom:
y^2 = x^3 - 275x + 1750
```

Stage29 audited database/model facts:

```text
Cremona = 800a3
LMFDB = 800.d2
rank = 1
torsion = Z/2
```

These do not by themselves certify the complete quartic integral-point set.

## Source claim under test

The external paper claims the complete quartic integral points are

```text
(-1,+/-1)
( 1,+/-1)
(11,+/-37)
```

and that the only nondegenerate prime-family reconstruction is `(p,q)=(11,71)`, which fails the remaining face-square condition.

Stage31 treats this as a claim to reconstruct, not as an input theorem.

## Frozen repair contract

Stage31 may grant closure credit only after all four are certified:

```text
1 explicit quartic <-> elliptic birational maps
2 rigorous integral/S-integral transfer
3 complete proof-capable IntegralPoints/elliptic-logarithm certificate
4 exhaustive pullback and cuboid reconstruction
```

No source update, database count, bounded search, sampled height constant, or CAS output without a completeness theorem may substitute for these four items.
