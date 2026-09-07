# Stage35-EX Goal4AD source lock — C5 pair marked-Picard adapter preflight

Scope: continue only the Goal4AC class-B `Q(i)/Q` cyclic principalization route. This leaf determines the correct source route for the four C5 residual-pair divisor classes before any target-span calculation. It does not materialize the pair classes, does not construct `F_B`, and grants no Brauer–Manin or E1 credit.

## Exact parent and freshness lock

- parent live Stage35-EX head: `62bef97cbbac1ca6b12aa52abc6299f2a63587fa`;
- current main/base: `f8522bd1a38fa551186ad370f51d17c73c7927e2`;
- compare at Goal4AD entry: ahead 84 / behind 0, merge-base exactly current main;
- Goal4AC artifact: `stages/stage35-ex/35ex-35/goal4ac-c5-individual-quadratic-residual.json`, blob `ef451544bce4aaafc14d24081e22ce997977a861`;
- Goal4AC source lock: `stages/stage35-ex/35ex-35/goal4ac-c5-individual-quadratic-residual-source-lock.md`, blob `788c8030cbb9cd99eb3252685877d0f1789fcd5c`;
- Goal4AC verifier: `stages/stage35-ex/verify_stage35_ex_35_goal4ac.py`, blob `a635727e2ae48288afb29977fa7464821fc2347d`.

Pinned external source remains:

- repository `MichaelStollBayreuth/Verification`;
- commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`;
- path `Cuboids/cuboids.magma`;
- git blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.

## Known-140 route is not a C5 locator

The pinned Stoll source builds the retained source curve list as

`CsK := C1sK cat C2sK cat C3sK;`

and only afterwards constructs the C5 family separately. The retained Stage33 reconstruction script

`stages/stage33/33-07/certify_two_coordinate_swap_picard_rows.py`

locks

- `KNOWN_COUNT = 140`,
- `CURVE_COUNT = 92`,
- 48 exceptional classes after those 92 curve classes,
- the primitive `INDLIST` basis of length 64,
- exact recovery of all 140 retained classes in that basis.

Therefore the existing known-140 recovery is a complete bridge for the retained `C1/C2/C3 + exceptional` packet, but it is not by itself a source-bound C5 class locator.

This is consistent with the newly merged Stage33 V91C1U preflight

`stages/stage33/33-12/e3-v91c1u-a2-02-known140-locator-preflight.json`

which explicitly distinguishes `known140` Picard recovery from the still-missing geometric locator into that packet. Goal4AD does not reinterpret that preflight as a C5 locator.

## Direct upstream C5 Picard route exists

The same pinned Stoll source constructs a C5 curve on `K` and computes its Picard class directly:

`C5K := Curve(IrreducibleComponents(Scheme(K, B1+B2+B3))[1]);`

`C5Kp := imageinPicK(C5K);`

`assert PicKL!C5Kp in cands4p0;`

It then grows the explicit C5 orbit and verifies

`until #C5sK eq 8;`

The source also constructs the exact homomorphism

`PicKtoPicS := hom<PicK -> Pic | ... >;`

from the `K` Picard lattice into the cuboid-surface Picard lattice. Thus the correct source route for Goal4AD is not

`C5 -> known140 index -> INDLIST64`,

but directly

`C5K / its orbit -> imageinPicK -> PicKtoPicS -> historical Pic(S) -> INDLIST64 marking`.

The final step must still be materialized numerically and source-locked. No numeric `C5Kp` orbit coordinates or `PicKtoPicS(C5Kp)` images are retained in the current Stage35-EX working set.

## Exact consequence

Goal4AD therefore resolves the adapter architecture but not the adapter values:

- the known-140 index-locator route is inapplicable as the primary C5 route;
- upstream direct C5 Picard computation exists;
- upstream `PicK -> Pic(S)` transport exists;
- the Stage33 historical `INDLIST64` reconstruction exists;
- the missing object is the source-bound numeric C5 orbit image through `PicKtoPicS` into the historical `INDLIST64` marking.

The target-span calculation remains illegal until those numeric pair classes are materialized.

## Firewall

Still uncomputed/unproved:

- exact marked Picard-64 coordinates of the four Goal4AC residual C5 pair divisors;
- exact exceptional/total-transform correction for those pair divisors in the Stage35 divisor packet;
- target-span test after adjoining the pair classes;
- general graded-coordinate-ring/Riemann–Roch principal-function synthesis;
- explicit `F_B`;
- full `Br_a(U)`, local evaluations, verticality, Brauer–Manin obstruction;
- E1, R29-PESCH-E1, R29-FIB2, Stage35 closure, or any perfect-cuboid theorem.

The next smallest exact leaf is direct source extraction of the C5 `PicK` orbit and its `PicKtoPicS` images, followed by transport into the already-certified historical `INDLIST64` marking.
