# Stage32 post-1473 — source-locked X(8) Satake-boundary marking

## Scope

This note closes only the missing semantic marking requested by the current Stage32 controller:

- identify the Satake-boundary curves inside the retained 92 nonexceptional special curves;
- split those boundary curves by the two `X(8)` factors;
- preserve the exact retained label ordering.

It does **not** exclude any of the three audited `O=188` contact histograms by itself.

## Frozen algebraic source

Stage32 `source-lock.md` fixes

```text
UPSTREAM_REPO=https://github.com/MichaelStollBayreuth/Verification
UPSTREAM_COMMIT=51233ed5ef2bf228fac9416c66db9adc0ebcaadd
UPSTREAM_FILE=Cuboids/cuboids.magma
UPSTREAM_BLOB=0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

In that source the box coordinates are

```text
(a1,a2,a3,b1,b2,b3,c) = (W1,W2,W3,Z1,Z2,Z3,C),
```

as is immediate from the four defining cuboid quadrics. The known nonexceptional curves are concatenated as

```text
Cs := C1s cat C2s cat C3s
```

with exact sizes

```text
#C1s = 32,
#C2s = 12,
#C3s = 48.
```

The three `C2s` blocks are cut out respectively by `b1=0`, `b2=0`, `b3=0`, four irreducible curves per coordinate.

Hence, in the retained Stage32 order,

- labels `1..32` are upstream `C1s`;
- labels `33..44` are upstream `C2s`;
- labels `45..92` are upstream `C3s`;
- labels `93..140` are the 48 exceptional curves.

This also removes a possible naming ambiguity: upstream `C1/C2/C3` means `32/12/48`, respectively.

## Modular source

Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*, arXiv `1303.6495` (v1), gives

```text
Z1 = theta01(z) theta01(w),
Z2 = theta00(z) theta00(w),
Z3 = theta10(z) theta10(w),
```

and Proposition 2.7 identifies the Satake boundary with

```text
Z1 Z2 Z3 = 0.
```

It consists of exactly 12 smooth elliptic curves, namely the images of the two factor-boundary types

```text
{a} x H*    and    H* x {a}.
```

Propositions 2.6, 2.7 and 2.9 split the 92 nonexceptional curves modularly as

```text
32 rational + 12 Satake-boundary elliptic + 48 non-boundary elliptic.
```

Comparing with the frozen Magma construction therefore identifies **upstream `C2s`, retained labels 33..44, exactly with the Satake boundary**.

## Exact factor split

Write

```text
Az = theta00(2z),  Bz = theta10(2z),
Aw = theta00(2w),  Bw = theta10(2w).
```

The theta parametrization gives

```text
W1 = Bz Aw + Az Bw,
W2 = i(Bz Aw - Az Bw),
W3 = Az Aw - Bz Bw,
C  = Az Aw + Bz Bw.
```

For `Z1=0`, a first-factor cusp has `Bz=+-Az`; for `Z2=0`, `Bz=+-i Az`; for `Z3=0`, `Az=0` or `Bz=0`. The analogous statements hold with `z` replaced by `w` for a second-factor cusp.

Substitution into each of the three frozen Magma `C2s` blocks gives the same sign rule:

```text
first-factor cusp (z fixed):  e2 = -e1,
second-factor cusp (w fixed): e2 =  e1.
```

Magma sequence constructors iterate the first range innermost, so each four-curve block ordered by

```text
[e1,e2 in [1,-1]]
```

has sign order

```text
(+,+), (-,+), (+,-), (-,-).
```

Therefore the retained labels split exactly as

```text
first-factor / z-fixed boundary:
  {34,35,38,39,42,43}

second-factor / w-fixed boundary:
  {33,36,37,40,41,44}
```

with two curves of each factor type in each coordinate block `Z1=0`, `Z2=0`, `Z3=0`.

The lightweight checker

`diagnose_stage32_post1473_x8_satake_boundary_marking.py`

verifies these substitutions exactly over Gaussian integers with no floating-point arithmetic or external package.

## Certificate

Machine-readable certificate:

`post1473-x8-satake-boundary-marking.json`

Canonical SHA256, computed after removing its `canonical_sha256` field and serializing with sorted keys and compact separators:

```text
69a2a6d3cdf7b0d5c6162424a8102ec41cd09ac7e303469d30577d454363e31d
```

## Consequence and next exact test

The controller's previously missing semantic bridge is now available at the boundary-family level. The next useful calculation is no longer a search for the marking itself:

1. join the marked `6+6` boundary curves to the 48 exceptional curves using retained exact incidence/intersection data;
2. recover for each exceptional node its first-factor and second-factor boundary labels;
3. test the unique defect-2 branch in histogram `B` or `C` against those marked node pairs and the already-audited equal-ramification-support condition.

If the retained data do not preserve the individual node-to-exceptional identification needed for step 2, pin that as the next exact adapter gap rather than reverting to coarse partition counting.

## Firewall

This result establishes only the source-locked marking above.

Still open:

- exclusion or realization of histograms `A/B/C`;
- all `O=188` profiles;
- analytic/global carrier existence;
- fixed-V6 integral genus-one closure;
- receiver/theorem/route/endpoint credit.

No perfect-cuboid existence or nonexistence claim is made.
