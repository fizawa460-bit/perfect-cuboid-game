# Stage32 MB104 — size-48 one-type Beauville equality quotients

Status: **RETAINED CURRENT-FRONTIER GLOBAL CLASSIFICATION / ELLIPTIC OR (2,2,2,2) QUOTIENT GEOMETRY / NO CLOSURE / MB104 INCOMPLETE / NO CREDIT**

## Scope

This leaf applies identically to the two surviving size-48 balanced support orbits

```text
0000770000ff,
00007b0000ff.
```

Each support has fourteen nodes of one and the same Beauville singular stabilizer type:

```text
node-type counts=(14,0,0).
```

For a hypothetical actual uniform-ray genus-one carrier,

```text
d=r_odd=112l,
```

and the equality-rigidity leaf gives a connected product-cover component `Z` whose projections to `C8` are etale of degree `14el`, with

```text
e in {1,2,4}.
```

Let `s` be the single singular stabilizer type occurring in the support.  It stabilizes every product-cover component.

## General component group

Let `K` be the stabilizer in

```text
G ~= (Z/2)^3
```

of one connected component `Z`.  Since `Z->E` has degree `2e`,

```text
|K|=2e,
|K cap G0|=e,
```

where `G0 ~= (Z/2)^2` is the free Beauville subgroup.  The quotient is the original normalization:

```text
E=Z/K,
g(E)=1.
```

The induced map

```text
phi:E -> C8/K
```

has degree `14el`.

The support contributes exactly `112l` distinct normalization points fixed by `s` in the quotient sense.

## Case `e=1`

Here

```text
K=<s>, |K|=2.
```

The involution `s` has eight fixed points on the genus-five curve `C8`.  Riemann--Hurwitz gives

```text
8 = 2(2g(C8/K)-2)+8,
```

so

```text
C8/K has genus one.
```

The induced map

```text
phi:E -> C8/<s>
```

has degree `14l` between genus-one curves, hence is etale.

The eight fixed points of `s` give eight branch values of `C8->C8/<s>`.  The total number of points of `E` over these eight values is

```text
8*(14l)=112l,
```

exactly the number of supported minimal branches.  Therefore the supported branches exhaust all these fibers.

Thus an `e=1` realization forces `E` to be an etale degree-`14l` cover, hence an isogenous elliptic curve, of the fixed elliptic quotient `C8/<s>`.

## Case `e=2`

Now

```text
K=<s,h>,
```

where `1!=h in G0` is fixed-point-free on `C8`.  Put `t=s*h`, the second outside element of `K`.  There are two subcases.

### `t` is the unique free outside involution

Only `s` contributes fixed points.  Hence

```text
8=4(2g(C8/K)-2)+8,
```

so `C8/K` again has genus one.

The eight `s`-fixed points form four `K`-orbits, hence four branch values of `C8->C8/K`.  The induced degree-`28l` map

```text
E -> C8/K
```

is etale.  Its four fibers over those values contain

```text
4*(28l)=112l
```

points, again exactly exhausted by the supported branches.

### `t` is another singular stabilizer involution

Both `s` and `t` have eight fixed points, while `h` is free.  Thus

```text
8=4(2g(C8/K)-2)+8+8,
```

and

```text
C8/K ~= P^1.
```

There are four branch values of type `s` and four of type `t`.  The descended map

```text
phi:E -> P^1
```

has degree `28l`.

For a branch value q write `u_q+2r_q=28l`.  Riemann--Hurwitz on E gives total unramified capacity `112l`.  All `112l` supported branches are of type `s`, so they exhaust this capacity.

The four `s`-type fibers have total degree

```text
4*28l=112l,
```

and therefore each is completely unramified:

```text
u_q=28l, r_q=0   on all four s-values.
```

All four `t`-type fibers are completely ramified:

```text
u_q=0, r_q=14l   on all four t-values.
```

Hence the effective branch datum of `phi` is exactly four points with fixed-point-free involutory monodromy: the Euclidean orbifold signature `(2,2,2,2)`.

## Case `e=4`

Here `K=G`.  The quotient `C8/G` is `P^1` with six order-two branch values, two for each of the three singular stabilizer types.  The induced map

```text
phi:E -> P^1
```

has degree `56l`.

Its total unramified capacity over the six values is `112l`, exactly exhausted by the supported branches.  Since all supported branches have type `s`, the two `s`-type fibers already have total degree

```text
2*56l=112l.
```

Thus

```text
u_q=56l, r_q=0
```

at both `s`-type values, while the four values belonging to the two absent singular types satisfy

```text
u_q=0, r_q=28l.
```

Again the effective branch locus consists of four points with fixed-point-free involutory monodromy, i.e. signature `(2,2,2,2)`.

## Common elliptic/isogeny interpretation

In the `e=1` and elliptic `e=2` subcases, `E` is directly an etale cover of a fixed genus-one quotient of `C8`.

In the two `(2,2,2,2)` subcases, let `B->P^1` be the canonical double cover branched at the four effective branch values.  Then `B` has genus one.  After normalizing the fiber product

```text
E x_(P1) B,
```

the order-two local ramification cancels, producing a common finite etale cover of `E` and `B`.  Therefore `E` is isogenous to this fixed elliptic double cover.

Consequently every possible size-48 equality realization forces the carrier normalization into one of finitely many fixed elliptic isogeny classes determined by the modular cover data.

## Consequence and next lever

The one-type size-48 problem is no longer an arbitrary genus-one singular-curve problem.  It is an isogeny-compatible embedding problem:

```text
Can an elliptic curve in one of the forced modular isogeny classes
occur as the normalization of an integral divisor in |D_l|
with the required fourteen-node / 112l minimal-branch packet?
```

No contradiction is obtained from the quotient geometry alone.

## Firewalls

- No claim that the forced elliptic isogeny class is incompatible with the cuboid surface has yet been proved.
- No actual carrier is constructed.
- Neither size-48 support orbit is closed.
- Whole span5, unequal Picard coefficients, P6 sectors, MB104, receiver, theorem, endpoint, and Perfect-Cuboid credit remain open/zero.
- No merge authorization.
