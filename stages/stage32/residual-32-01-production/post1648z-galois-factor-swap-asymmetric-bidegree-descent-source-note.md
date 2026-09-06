# Stage32 post-1648Z Galois factor-swap / asymmetric-bidegree descent gate

Scope: scratch-only third-perspective diagnostic for the fixed Stage32 class `g1-d186` at
`O=210`, `qprime=4`, `Q=602`. This leaf deliberately does not use the absolute
`delta_0inf` marking, the Cecotti inner conjugator, or a residue-specific commutator.

## Existing exact Stage32 input

The exact post-1484 modular-factor certificate fixes the two resolved `X(4)` factor
degrees of the recovered V6 class as

- first factor: `m_z = 105`;
- second factor: `m_w = 81`.

Source lock:

- `stages/stage32/residual-32-01-production/post1484-v6-modular-factor-bidegree-boundary.json`
  - git blob SHA-1 `072266f2ac5386316adc99e35a6444d2449656c8`
  - canonical SHA-256 `791870c37681702392e1e59d224f494ed791709d467efa68a20cf49bff4ab420`
- recovered V6 witness:
  `stages/stage32/32-21/post1473-v6-witness-body-recovered.json`
  - git blob SHA-1 `dae90ed19395355bebeebe2a6aa6bb1c6e53c244`
  - canonical SHA-256 `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`

The post-1484 source note already locks the complex modular description
`(X(8) x X(8))/G_0` and the two factor maps.

## New external arithmetic source lock

Primary source: Michael Stoll and Damiano Testa, *The surface parametrizing cuboids*,
arXiv:1009.0388, current manuscript dated 2025-02-24, Section 4
("The cuboid surface as a modular surface"), especially the paragraph spanning pp. 8--9.

Canonical source locations used in this leaf:

- https://arxiv.org/abs/1009.0388
- https://www.mathe2.uni-bayreuth.de/stoll/papers/Cuboidi.pdf

Use only the following exact facts from that locator.

1. Over a field containing `sqrt(-1)`, the cuboid surface is described by the
   diagonal quotient of `X(8) x X(8)` by `G_0`, and it maps to
   `X(4) x X(4)`.
2. The sign change `a3 -> -a3` on the cuboid surface lifts to the automorphism
   of `X x X` that switches the two factors.
3. Consequently, over `Q` the cuboid surface is the quotient of
   `Res_{Q(i)/Q}(X_{Q(i)})` by `G_0`; its quadric factor base is
   `Res_{Q(i)/Q}(X(4)_{Q(i)})`.
4. Thus the nontrivial element of `Gal(Q(i)/Q)` interchanges the two geometric
   `X(4)` factor fibrations.

Corroborating computation source: Michael Stoll's verification repository,
`MichaelStollBayreuth/Verification`, file `Cuboids/cuboids.magma`, commit
`51233ed5ef2bf228fac9416c66db9adc0ebcaadd`. That script explicitly sets up
complex conjugation (`i -> -i`) and descends its permutation action to
`Pic(S)`. This leaf does not import its full Picard matrix; it only records
that an exact Picard-Galois adapter exists for the proposed next leaf.

## Derived asymmetric-bidegree obstruction

Let `F_1,F_2` be the two geometric `X(4)` fiber classes, ordered as in the
post-1484 certificate, and let `sigma` be the nontrivial element of
`Gal(Q(i)/Q)`. The new source lock gives

` sigma(F_1) = F_2,   sigma(F_2) = F_1. `

For the fixed V6 class `D`,

`(D.F_1, D.F_2) = (105,81)`.

Intersection pairing is Galois invariant, so

`(sigma(D).F_1, sigma(D).F_2) = (81,105)`.

Since `105 != 81`, this proves

` sigma(D) != D `

in the geometric Picard group. Therefore the fixed V6 divisor class is not
defined over `Q`.

In particular, an integral irreducible curve whose geometric divisor class is
exactly `D` cannot itself be defined over `Q`: a `Q`-defined curve has
Galois-fixed divisor class.

A second bounded consequence is useful for rational-point accumulation. If a
geometrically irreducible curve `C` in class `D` contained infinitely many
`Q`-rational points, then every such point would lie on both `C` and
`sigma(C)`. Two distinct irreducible curves on a surface have finite
intersection, so infinitely many common points force `C=sigma(C)`, contrary to
`sigma(D)!=D`. Hence this class cannot support an irreducible curve with an
infinite `Q`-rational subset.

## What this does not prove

This is not an exclusion of a single isolated rational point. A rational
point on a non-`Q`-defined curve may lie in `C intersect sigma(C)`. Therefore
the current `Q602` residues `[73,97,235]` are not removed and `Q602_excluded`
remains false.

The next exact non-marking route is to compute the Picard class
`sigma(D)` with the Stoll--Testa complex-conjugation action, then compute
`D.sigma(D)` and identify the geometric support of possible
`C intersect sigma(C)` points. Only if the rational part of that intersection
is shown to lie in already-degenerate/boundary loci may the Stage32 carrier be
excluded arithmetically.

## Firewalls

- asymmetric bidegree proves non-`Q`-descent of the fixed geometric class; it
  does not prove nonexistence of geometric curves in that class;
- non-`Q`-descent excludes infinite rational-point accumulation on one
  geometrically irreducible carrier, not isolated rational points;
- no absolute `W`-line, residue-specific commutator, `Q602`, `O210`, receiver,
  route, theorem, endpoint, or perfect-cuboid credit is promoted;
- no global absence claim is made for other third-perspective invariants.
