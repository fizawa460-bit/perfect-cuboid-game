# Stage32 MB104 — wide shallow closure scan Round B — 2026-09-18

Status: **ROUND B COMPLETE / 5 ROUTES SCREENED / ALL DROP / NO MATHEMATICAL CREDIT**

## Result table

```
W4-second  K3 quotient lattice/fibration     DROP
W5         higher symmetric differentials   DROP
W8         simultaneous sign-quotient RH    DROP
W10        ambient fat-point Hilbert         DROP
W11        elliptic normalization series     DROP
```

No route becomes DEEP.

## W4 second scan — K3 quotient: DROP

Round A showed that the seven coordinate-sign K3 pushdowns satisfy degree parity, positive square and Hodge.

The second cheap test uses the fixed fibration inventory.

For the active support `000707000f0f`, the six eight-node block counts are

```
[4,4,0,3,3,0].
```

For every Stoll--Testa rank-3 genus-five fiber on the cuboid surface,

```
2F_Q=H-sum_(p in B_Q)E_p,
```

hence

```
D_l.F_Q=(56-4 n_Q)l.
```

The six values are

```
40l, 40l, 56l, 44l, 44l, 56l,
```

all strictly positive. In particular the rank-3 part of the K3 elliptic-fibration inventory produces no negative-fiber obstruction after pullback.

The published K3 result supplies a rank-20 Picard group, 15 elliptic fibrations and low-degree integral-curve classification in degrees 2 and 4. The active pushdowns have degree `112l`. The published low-degree theorem therefore does not touch them.

A further continuation would require expanding each of the seven high-degree rays in the full rank-20 lattice and performing a dedicated nef/effective-cone calculation. That is no longer a second shallow consequence of the published K3 structure.

**Disposition: DROP from the wide scan.**

This does not say K3 methods can never help; it says they failed both scheduled shallow kill-tests.

## W5 — higher symmetric differentials: DROP

This is more exhausted than the initial portfolio suggested.

The retained explicit BTVA 13-form calculation proves that the order-two principal-part map has rank three at every one of the 48 A1 nodes. For one minimal branch, pole cancellation is one binary-quadratic evaluation condition. Three distinct landing directions already force the full principal part to vanish; every further branch at the same node contributes no new order-two condition.

The separate finite-jet wall proves the same structural problem for any fixed finite family of bounded-order jets: arbitrarily many distinct minimal branches can agree through that finite jet depth.

The active packet has

```
8l
```

minimal branches at each of 14 nodes. The known BTVA asymptotic theorem gives finiteness only for low-genus curves through at most 13 singularities, while this support has 14.

Thus the existing symmetric-differential arsenal does not scale with the branch multiplicity that MB104 must kill. An unbounded-order differential construction growing with `l` would be a genuinely new theorem, not a shallow continuation.

**Disposition: DROP.**

## W8 — simultaneous coordinate-sign quotient genus budget: DROP

For a coordinate-sign involution `sigma` to induce an involution on the normalization of the hypothetical carrier, the carrier must be `sigma`-invariant. In particular its exact box-node support must satisfy

```
sigma(Sigma)=Sigma.
```

For the seven coordinate sign changes, the exact overlaps are

```
a1 7
a2 7
a3 8
b1 13
b2 13
b3 12
c  6
```

against `|Sigma|=14`.

Thus **none** of the seven coordinate sign involutions preserves the active support. None acts on the hypothetical carrier normalization, so there is no simultaneous family of seven Riemann--Hurwitz formulas on that genus-one curve.

Using the quotient maps only as maps from `C` to their images is W4, not W8.

**Disposition: DROP.**

## W10 — ambient fat-point Hilbert function: DROP

Any exact ambient fat-point model for the ray must reproduce the line bundle `O_S(D_l)`.

But retained Riemann--Roch gives

```
h0(O_S(D_l))
 >= chi(O_S(D_l))
 =168l^2-56l+8.
```

So already

```
l=1: h0 >=120,
l=2: h0 >=568.
```

The exact ray has nonzero sections for every `l>=1`. Therefore no Gröbner/initial-ideal computation that is genuinely equivalent to the active divisor problem can prove that the corresponding graded piece vanishes.

It could still study irreducibility or genus-one members, but that would be a different route from W10's proposed Hilbert-vanishing closure.

**Disposition: DROP.**

## W11 — elliptic-normalization linear-series collapse: DROP

Let `E` be the genus-one normalization and let

```
L=nu^*O_S(H).
```

Then

```
deg L=H.C=112l.
```

The unique ambient hyperplane spanned by the active node support contains all fourteen supported nodes. Every one of the `14*8l=112l` minimal normalization branches contributes at least one zero to that hyperplane section. Since the total degree is also `112l`, the section is saturated exactly by those supported normalization points.

This sounds rigid, but on an elliptic curve it is numerically ordinary:

```
h0(E,L)=deg L=112l.
```

One section with that prescribed effective divisor is exactly what the line bundle `O_E(B_Sigma)` provides, and the ambient coordinate subsystem has dimension at most seven, tiny relative to the full `112l`-dimensional section space.

The retained global refinements also show no hidden easy contradiction: the primitive ray restricts trivially in `Pic^0` to every zero-pairing elliptic quartic, and the even half-hyperplane invariant/anti-invariant ambient eigensection systems are automatically nonzero.

So the bare elliptic linear-series/Abel--Jacobi route does not collapse. A successful continuation would need an additional special product-cover or coordinate relation, returning to already parked routes.

**Disposition: DROP.**

## Round B conclusion

Round A + Round B have now shallow-screened ten route instances without a DEEP candidate.

Next is **Round C**, still in broad mode:

```
W7  cyclic/abelian-cover BMY amplification
W9  finite-characteristic specialization
W12 receiver-preserving explicit degeneration
+ 2--3 newly generated direct-closing mechanisms
```

Do not reopen dropped routes unless a genuinely new theorem changes their cheap-test conclusion.
