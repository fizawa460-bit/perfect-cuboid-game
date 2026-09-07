# Stage35-EX Goal4U — Picard-rank-64 source lock

This file freezes the exact external/internal facts used by Goal4U. It does not promote any Stage35-EX theorem credit by itself.

## Exact surface adapter

Stage35-EX uses the projective cuboid surface in coordinates `(h,x,y,z,q,p,w)` with equations

```text
p^2 = h^2 + x^2
q^2 = h^2 + y^2
z^2 = x^2 + y^2
w^2 = h^2 + x^2 + y^2
```

The pinned Stoll source uses `(a1,a2,a3,b1,b2,b3,c)` and

```text
a1^2 + a2^2 = b3^2
a2^2 + a3^2 = b1^2
a1^2 + a3^2 = b2^2
a1^2 + a2^2 + a3^2 = c^2
```

The exact coordinate identification is

```text
(a1,a2,a3,b1,b2,b3,c) = (h,x,y,z,q,p,w).
```

Thus this is the same projective surface, not merely a birationally related model.

## Pinned sources

Stage35-EX model source:

```text
path: stages/stage35-ex/35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md
blob: 6a8d8c71d50d9667330badca914a8967b4f87577
```

Stage33 compact marked-Picard source:

```text
path: stages/stage33/33-09/marked-picard-basis-source.json
blob: c9eb0e195e95263f6753fb29099ffa6d5d74dc13
result path: stages/stage33/33-09/result.md
result blob: 820543c4778851f5b7487e6d09a6274ee0cceed3
```

Pinned upstream verification source:

```text
repo: MichaelStollBayreuth/Verification
commit: 51233ed5ef2bf228fac9416c66db9adc0ebcaadd
path: Cuboids/cuboids.magma
blob: 0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

## Exact retained rank fact

The pinned source constructs `C1s`, `C2s`, `C3s`, then appends the 48 exceptional divisors represented by the singular points to form the intersection matrix. The source asserts

```text
assert #pts eq 48;
assert Rank(pairingmat) eq 64;
```

The explicit family sizes are:

```text
#C1s = 32
#C2s = 12
#C3s = 48
#pts  = 48
#(C1s cat C2s cat C3s cat pts) = 140.
```

Hence actual divisor classes on this exact projective surface span a numerical lattice of rank 64, so `rho(Xbar) >= 64`.

Goal4T independently gives `h^(1,1)=64`, hence `rho(Xbar) <= 64`. Therefore Goal4U may conclude exactly

```text
rho(Xbar) = 64.
```

This conclusion does not use the later upstream comment/assumption that the known curves generate the full Picard group. Rank 64 plus the independent Hodge cap is sufficient.

## Coordinate/ramification interpretation

Under the exact coordinate adapter, the four blocks of `C1s` are the 8 conics above each of

```text
h=0, x=0, y=0, w=0,
```

respectively. The first block `h=0` is the boundary-conic family already present in Goal4Q. Goal4U does not claim that these 32 coordinate conics alone have rank 64; the rank-64 lower bound uses the complete source-locked 140-divisor configuration.

## Firewall

Goal4U determines only the geometric Picard rank. It does not yet certify a full integral marked Picard isomorphism for Stage35-EX, the full Galois action on Picard, `H^1(Q,Pic)`, the algebraic Brauer group, a nonconstant Brauer class, a Brauer-Manin obstruction, E1, `R29-PESCH-E1`, Stage35 closure, or a perfect-cuboid theorem.
