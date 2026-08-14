# Stage23-30 new attack — consecutive-parameter AR-039 slice

Purpose: satisfy checkpoint30 with a genuinely new Stage17-originating attack, distinct from checkpoint20's fixed `n=1` high-genus slice and distinct from the Stage14/15 target-first routes.

Start from the audited AR-039 Stage17 family

\[
x=m^2-n^2,\quad y=2mn,\quad p=m^2+n^2,\quad z=(p^2-1)/2,\quad d=(p^2+1)/2,
\]

with coprime `m>n`, `m=2 mod 14`, `n=1 mod 14`.

## New slice

Take consecutive parameters

\[
n=t,\qquad m=t+1,\qquad t\equiv1\pmod{14}.
\]

Then coprimality and the AR-039 congruence contract hold automatically for every such positive `t`. We obtain

\[
p=2t^2+2t+1,\quad x=2t+1,\quad y=2t(t+1),
\]

\[
z=2t^4+4t^3+4t^2+2t,
\qquad d=(p^2+1)/2.
\]

Thus this is an explicit infinite Stage17 slice before the second-face condition.

## Second-face factorization

Direct expansion gives

\[
x^2+z^2=
(2t^4+4t^3+2t^2+1)
(2t^4+4t^3+6t^2+4t+1).
\]

For the other candidate face there is a stronger degeneration:

\[
y^2+z^2
=4t^2(t+1)^2(t^2+1)(t^2+2t+2).
\]

Since `2t(t+1)` is already an integer square-factor root, the condition that the `yz` face become integral is exactly

\[
\boxed{w^2=(t^2+1)(t^2+2t+2)}.
\]

The right side is a quartic. Its four roots are distinct over characteristic zero, so its smooth projective model is genus 1. Therefore checkpoint30 finds the requested low-genus degeneration: the second-face problem on this natural Stage17 slice drops from checkpoint20's generic genus 2/3 geometry to an elliptic curve problem.

This does not by itself prove positive rank, infinitely many admissible integer `t`, or an infinite primitive Stage19 family. Those are the next arithmetic questions.

## Strict integer attack

A direct exact-square scan was performed on the admissible progression

```text
t = 1 mod 14
1 <= t < 1,000,000
```

for

```text
(t^2+1)(t^2+2t+2) = square.
```

Result:

```text
YZ_SECOND_FACE_HITS=0
```

The zero-hit scan is finite diagnostic evidence only. It is not used to prove that the elliptic curve has rank zero or that admissible integral points are finite.

## Why this is new relative to checkpoint20

Checkpoint20 fixed `n=1` and varied `m`, producing generic genus 3 / genus 2 hyperelliptic conditions. Checkpoint30 instead imposes the moving relation `m=n+1`, preserving an infinite AR-039 source slice while forcing one second-face equation to genus 1. Hence it is a distinct attack and explicitly tests the genus-0/1 escape route required by audit.

```text
ATTACK_ID=AR039_CONSECUTIVE_PARAMETER_SLICE
SOURCE=Stage17_AR039
SLICE=m=n+1
ADMISSIBLE_PROGRESS=t=1_mod_14
SOURCE_SLICE_INFINITE=true
SOURCE_PRIMITIVITY_CONTRACT=PASS
SECOND_FACE_YZ_CURVE=GENUS_1_QUARTIC
GENUS_0_DEGENERATION_FOUND=false
GENUS_1_DEGENERATION_FOUND=true
SCAN_BOUND=1000000
SCAN_HITS=0
INFINITE_STAGE19_FAMILY_PROVED=false
POSITIVE_POWER_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_PROVED=false
FINITE_SCAN_USED_AS_PROOF=false
OLD_STAGE14_15_PRIMARY_ROUTE_REUSED=false
```
