# Stage35-EX Goal4AE source lock — reject the K-side `C5K` name collision and restore the direct S-side C5 Picard route

Scope: repair only the provisional Goal4AD adapter architecture. This leaf does not materialize any C5 pair coordinate, does not run the class-B target-span test, does not construct `F_B`, and grants no Brauer–Manin or E1 credit.

## Parent and exact source

Parent Stage35-EX state before this repair is V67 at branch head `2604ed2e41817c3adbed5a565d029a74b85e3eb2`.

Pinned external source:

- repository `MichaelStollBayreuth/Verification`;
- commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`;
- path `Cuboids/cuboids.magma`;
- git blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`.

## The two objects called C5 are not source-identified

Early in the pinned source, on the cuboid surface `S`, the retained `C5s` family is defined as 16 curves

`Curve(ReducedSubscheme(Scheme(S, [a1+e2*a2+e3*a3+e4*i*c, (e2*a2+e3*a3)*b1+e1*i*b2*b3])))`

with `e1,e2,e3,e4 in {+1,-1}`. The source labels these explicitly as

`Genus 3 nonhyperelliptic curves of degree 8`.

Much later, in the K3-quotient calculation, the source first enumerates classes with `C^2=-2`, states that these must be `smooth rational normal curves of degree 4`, filters them, and proves that the surviving Aut(K) orbit sizes are `8` and `48`. Only inside that separate calculation does it define

`C5K := Curve(IrreducibleComponents(Scheme(K, B1+B2+B3))[1]);`

and verify that `C5Kp := imageinPicK(C5K)` lies in the size-8 rational-normal-curve candidate orbit.

The pinned source contains no statement identifying this K-side variable `C5K` with the image, quotient, norm, or pair divisor of the earlier S-side genus-3 degree-8 family `C5s`. Therefore the variable-name similarity is not a valid source bridge.

Consequently the Goal4AD route

`surface C5 pair -> K-side C5K -> imageinPicK -> PicKtoPicS`

is unsupported as written. The generation-4 through generation-8 local lattice diagnostics were consistently reconstructing the K-side degree-4 rational-normal-curve orbit; they cannot be promoted as numerical marked classes of the Goal4AC S-side C5 residual pairs.

## Direct S-side Picard route already exists in the same source

The pinned source constructs a primitive `indlist` of length 64 in `Pic(S)` and then defines

`imat := Matrix(Rationals(), [[pairingmat[j,k] : k in indlist] : j in indlist])^-1;`

followed by

`function imageinPic(C)`

`  iseq := [intersection(C, j) : j in indlist];`

`  return PicL!Eltseq(Vector(Rationals(), iseq)*imat);`

`end function;`

This is the source-native route for a curve on `S` not containing one of the retained `Cs` components. The Stage33 compact reconstruction independently recovers the same primitive historical `INDLIST64` marking from the retained H-perp packet.

Therefore the next legal numerical leaf is not another K-side 48+8 enumeration. It is a bounded direct S-side extraction:

`explicit S-side C5s -> intersection(C,j) on the 64 source indlist entries -> imageinPic -> historical Pic(S) -> primitive Stage33 INDLIST64`,

then sum the `e4=+1/-1` classes into the eight sigma_c-pair classes, source-label them by `(e1,e2,e3)`, select the four Goal4AC antipodal residual pairs, and only then run the fixed class-B target-span test.

## Firewall

Still uncomputed/unproved:

- the eight S-side C5 pair marked Picard64 rows and the four Goal4AC residual-pair rows;
- exceptional/total-transform corrections needed for the Stage35 divisor packet;
- target-span after adjoining the four residual-pair rows;
- general graded-coordinate-ring/Riemann–Roch principal-function synthesis;
- explicit `F_B`;
- full `Br_a(U)`, local evaluations, verticality, or a Brauer–Manin obstruction;
- E1, R29-PESCH-E1, R29-FIB2, Stage35 closure, or any perfect-cuboid theorem.

Goal4AE is a route repair only. It retracts no hostile-audited authority because Goal4AD and the attempted Goal4AE numerical route were provisional and unaudited.
