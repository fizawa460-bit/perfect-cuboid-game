# Stage35-EX Goal4AL source lock — positive-real receiver component and class-B local evaluation preflight

Scope: continue only after hostile-audited Goal4AK has been synchronized as V74 authority. This leaf evaluates the fixed audited class-B representative `(-1,F_B)` on the positive real component forced by a hypothetical E1 counterexample. It is a local-evaluation preflight only. It does not compute all finite-place images, a Brauer-Manin set, E1, Stage35 closure, receiver/theorem/endpoint credit, or a Perfect Cuboid claim.

## Audited parent

- Goal4AK hostile-audit PASS: PR #1720, review `5142248509`, audited exact head `2d6ec7c836857386b3e5553cc3117295775ca8d4`.
- merged Goal4AK authority: main commit `42f20e47babdfdda068a605e3fec489eeace460c`.
- V74 state releases local evaluation while keeping `open_receiver_local_evaluations_computed=false` and every BM/E1/downstream firewall false.
- fixed representative: `F_B=A31/B31`, class `(-1,F_B)` modulo `Br_0(U)`.
- Goal4AK assembly: `stages/stage35-ex/35ex-35/goal4ak-explicit-fb-assembly.json`, retained blob `5c543b8e5172e19cdb143ba69fcaa55098e5920f`.
- exact loader: `stages/stage35-ex/35ex-35/goal4ak_explicit_fb.py`, retained blob `3c5814fd98375f1eeeefd33f7fb99d9c888fbb9a`.

The fixed affine coordinate adapter is

`(a1,a2,a3,b1,b2,b3,c)=(h,x,y,z,q,p,w)`, with `h=1` on `U`.

## Exact receiver-to-real-component contract

The exact Stage35-EX normalized receiver surface is

```text
p^2 = 1+x^2,
q^2 = 1+y^2,
z^2 = x^2+y^2,
w^2 = 1+x^2+y^2.
```

The retained source adapter in `stages/stage35-ex/35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md` proves that every normalized full-receiver point from the Stage35-EX source chamber maps into

```text
x>0, y>0, p>1, q>1, z>0, w>0.
```

Call this real component `U(R)^+`. For every `x,y>0` there is exactly one point of this sign component,

```text
p=+sqrt(1+x^2),
q=+sqrt(1+y^2),
z=+sqrt(x^2+y^2),
w=+sqrt(1+x^2+y^2).
```

Therefore projection to `(x,y)` identifies `U(R)^+` continuously with `(0,infinity)^2`; in particular it is connected.

For the Brauer route we may enlarge the finite-place population rather than require the still-missing primitive-source reverse adapter. A hypothetical E1 counterexample gives a diagonal rational receiver point whose real component lies in `U(R)^+` and whose finite localizations lie in `U(Q_p)`. Hence it lies in the restricted adelic population

```text
U(R)^+ x product_{p finite} U(Q_p).
```

If this enlarged restricted adelic population is later shown Brauer-Manin empty, every E1 counterexample is excluded. No converse population adapter is needed for that implication.

## Arsenal routing

The matching Arsenal route is provisional card `LIT-PW04`, role `SOURCE_BOUND_BRAUER_LOCAL_EVALUATION_ADAPTER`:

named source-bound Brauer representative + exact model + local point population -> compute `Br(k_v)` evaluation, normalized invariant, and complete local evaluation images.

The card explicitly forbids replacing pointwise evaluation by Gersten/localization columns or treating a nonzero Brauer class alone as an obstruction. Goal4AL follows that firewall.

## Real quaternion evaluation

For a regular real point at which the fixed rational presentation is defined, the quaternion `(-1,F_B(P))` has real invariant

```text
inv_infinity = 0   when F_B(P)>0,
inv_infinity = 1/2 when F_B(P)<0.
```

Because the audited class is a Brauer class on `U`, its evaluation is locally constant on `U(R)`; connectedness of `U(R)^+` reduces the component image to one regular sample.

The first-generation diagnostic at exact head `c94728cc7381caf48c49aab28183607be78530de` (aggregate run `34236284901`, current job `102096461707`) used three symmetric points with `x=y`. Exact evaluation found `regular_sample_count=0`: at each probe the fixed `A31/B31` presentation had numerator or denominator equal to zero. This is a sample/presentation issue, not a Brauer-class or route blocker.

The repaired diagnostic therefore uses six non-diagonal exact algebraic samples, arranged in swap pairs:

1. `(x,y)=(3/4,4/3)` and `(4/3,3/4)`, with `p,q` equal to `5/4,5/3` in the corresponding order, `z=sqrt(337)/12`, `w=sqrt(481)/12`, over `Q(sqrt(337),sqrt(481))`;
2. `(x,y)=(3/4,5/12)` and `(5/12,3/4)`, with `p,q` equal to `5/4,13/12` in the corresponding order, `z=sqrt(106)/12`, `w=5*sqrt(10)/12`, over `Q(sqrt(106),sqrt(10))`;
3. `(x,y)=(5/12,4/3)` and `(4/3,5/12)`, with `p,q` equal to `13/12,5/3` in the corresponding order, `z=sqrt(281)/12`, `w=5*sqrt(17)/12`, over `Q(sqrt(281),sqrt(17))`.

The checker evaluates all 5924 numerator and 1542 denominator terms exactly in the corresponding biquadratic fields. Sign is certified by rational interval enclosures whose square-root endpoints are proved by integer-square comparisons; floating-point sign decisions are not used. Probe rows are emitted before the regular-sample assertion so a second presentation collision remains diagnostically informative rather than opaque.

## Credit firewall

This preflight may certify only the class-B image on `U(R)^+`. It does not certify:

- any finite-prime local evaluation image;
- the class-A local image;
- the full algebraic Brauer group;
- a Brauer-Manin obstruction;
- verticality;
- E1 or any Stage35/receiver/theorem/endpoint/Perfect Cuboid conclusion.

All those flags remain false until their own exact adapters and required audits are complete.
