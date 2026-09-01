# Stage32 post-21bl — Freitag–Salvati Manni node-support refinement

Status: `PROVISIONAL_PASS_PENDING_FRESH_AUDIT`

Scope: the audited representative Picard64 class `g1-d186` only. This note does **not**
close FULL178, multibranch-at-node curves, `R29-LG2-EFF`, the parent route, or the
perfect-cuboid problem.

## Locked inputs

Representative evidence:

- `stages/stage32/32-21/post-21bl-picard64-witness-adapter.json`
- canonical SHA256 `ef3f21e4166d4bfcacce3503213b0a72afee5f5002ab7145de01fc9c54d47038`
- target `g=1`, `d=186`
- Picard self-intersection `C^2=858`
- 140 exact nonnegative pairings with the Testa–Stoll known-curve/exceptional configuration.

Primary theorem source:

- Eberhard Freitag and Riccardo Salvati Manni,
  *Parametrization of the box variety by theta functions*, Theorem 3.1 and its proof.
- Author PDF: `https://www.mathi.uni-heidelberg.de/~freitag/preprints/box.pdf`
- Theorem/proof locators: PDF pages indexed 9–10 (printed pp. 10–11).

Immutable computation source:

- repo `MichaelStollBayreuth/Verification`
- commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`
- file `Cuboids/cuboids.magma`
- blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`

That source constructs `Cs := C1s cat C2s cat C3s` with `32+12+48=92` known
nonexceptional curves, then `48` singular points, and explicitly states that the pairing
matrix takes the curves first and the exceptional divisors second. Therefore rows
`93..140` of the Stage32 all-140 pairing vector are exactly the 48 exceptional-divisor
pairings.

## Refinement of Theorem 3.1

Freitag–Salvati Manni assume an irreducible curve `C` whose normalization
`Cbar -> C` is bijective. Their proof constructs a pulled-back tensor and uses

```text
16(2g-2)k = #zeros - #poles.
```

The proof gives at least `2kd` zeros. At a node met by `C`, the pole order is at most
`8k`. The published theorem then uses the worst-case bound of all 48 nodes, obtaining
total pole order at most `384k`.

Let `n` be the actual number of nodes of the box variety lying on `C`. Under the same
bijective-normalization hypothesis the normalization meets each exceptional divisor at
most once, so the identical proof gives the sharper bound

```text
#poles <= 8kn.
```

Hence

```text
16(2g-2)k >= 2kd - 8kn,
d <= 16g - 16 + 4n.
```

Putting `n=48` recovers the published bound `d <= 176 + 16g`.

The proof excludes the special horizontal/vertical Satake-boundary curves from this
tensor argument because the theorem is direct for them. They are among the 92 known
curves. In the immutable Magma source every one of those 92 rows has self-intersection
`-4`; the representative class has `C^2=858`, so it is not one of those special curves.

## Apply the refinement to the representative

The exceptional part of the audited all-140 pairing vector is

```text
[5,0,1,1,3,0,0,0,5,3,6,6,6,7,10,9,6,8,8,5,4,1,8,10,
 5,9,7,4,5,12,9,5,3,1,9,4,11,1,16,1,9,12,1,11,1,3,1,14].
```

It has:

```text
sum = 266
positive support = 44
zero support = 4
zero exceptional indices = 2,6,7,8
```

For an effective integral strict transform not containing an exceptional divisor,
intersection number zero with that exceptional divisor means disjointness. Thus a
bijective-normalization integral curve in this Picard class can pass through at most
`n=44` of the 48 nodes.

For `g=1`, the refined inequality becomes

```text
d <= 4n.
```

So this class would require

```text
n >= ceil(186/4) = 47,
```

but its exceptional support permits at most `44`. Equivalently,

```text
d <= 4*44 = 176 < 186.
```

Contradiction margin: `10`.

## Exact conclusion

Subject to fresh audit, there is **no integral irreducible curve in this representative
Picard class whose normalization has genus 1 and maps bijectively to its image on the
box variety**.

This does not contradict the already-audited Riemann–Roch result `h^0(O(C)) >= 344`.
That result guarantees effective divisors in the class; the divisors may be reducible,
nonreduced, or fail the required normalization/carrier semantics.

## Firewalls

```text
REPRESENTATIVE_ONLY=true
BIJECTIVE_NORMALIZATION_GENUS1_REPRESENTATIVE_EXCLUDED_PROVISIONAL=true
MULTIBRANCH_AT_NODE_EXCLUDED=false
FULL178_NUMERICAL_CENSUS_CLOSED=false
R29_LG2_EFF_FULL_RECEIVER_CLOSED=false
ROUTE_CREDIT=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
