# E-1d — structural explanation of the Euler-side directional profile

> **STATUS:** `E_1D_COMPLETE_AT_RAW_DIRECTIONAL_STRUCTURAL_ASYMPTOTIC_LEVEL`
>
> **COUNTING:** primitive canonical `0<a<b<c`, `a^2+b^2+c^2<=B^2`
>
> **SPACE DIAGONAL:** integrality not required
>
> **RESULT:** the Euler-side raw one-face populations have the same canonical chamber vector as the Stage13 space-diagonal side.

E-1c found numerically that removing the condition that the space diagonal be integral changes the population size dramatically but leaves the directional profile compatible with the Stage13 chamber vector. E-1d explains why.

The mechanism is not an accidental finite coincidence. At the raw one-face level, the two tracks have different radial/arithmetic factors but the **same real-place directional weight**.

## 1. Raw Euler-side populations

Let `A_q(B)` denote the primitive canonical raw incidence count in direction

```text
q in {ab,ac,bc},
```

so the face `q` has an integral diagonal, while the other two faces are not restricted. Thus `A_q` differs from the exactly-one count `N_q` by pair/triple overlaps.

The E-1a convention remains

```text
0<a<b<c
gcd(a,b,c)=1
a^2+b^2+c^2<=B^2.
```

No condition is placed on whether

```text
D=sqrt(a^2+b^2+c^2)
```

is integral.

## 2. Real-place density: the same chamber weight appears immediately

For a distinguished face `q`, introduce its integral face diagonal `p`. For example, for `q=ab`,

\[
F_{ab}=a^2+b^2-p^2=0.
\]

At the positive root

\[
p=\sqrt{a^2+b^2},
\]

eliminating `p` gives the Gelfand--Leray factor

\[
\frac{1}{2p}.
\]

Write

\[
(a,b,c)=r(x,y,z),
\qquad (x,y,z)\in S^2,
\qquad 0<x<y<z.
\]

For direction `q`, put

\[
s_q(x,y,z)=\sqrt{x_i^2+x_j^2}.
\]

Then

\[
p=r s_q,
\qquad da\,db\,dc=r^2\,dr\,d\sigma,
\]

so the induced measure is

\[
\frac{r}{2s_q}\,dr\,d\sigma.
\]

Integrating the radial variable over `0<r<=B` gives

\[
\frac{B^2}{4}\frac{1}{s_q}\,d\sigma.
\]

Therefore the entire directional dependence at the real place is

\[
\boxed{w_q(x,y,z)=\frac1{s_q(x,y,z)}}.
\]

Explicitly,

\[
w_{ab}=\frac1{\sqrt{x^2+y^2}},\qquad
w_{ac}=\frac1{\sqrt{x^2+z^2}},\qquad
w_{bc}=\frac1{\sqrt{y^2+z^2}}.
\]

These are **exactly the Stage13-3b chamber weights**.

This is the central structural explanation.

## 3. Why the Euler-side absolute scale is `B^2 log B`

Every integral face is a positive multiple of a primitive Pythagorean triple:

\[
(x,y,p)=k(u,v,h),
\]

with

\[
\gcd(u,v)=1,
\qquad u^2+v^2=h^2.
\]

For the complementary edge `z`, primitivity of the cuboid becomes

\[
\gcd(ku,kv,z)=1
\iff
\gcd(k,z)=1.
\]

Hence the asymptotic density of admissible third edges for fixed scale `k` is

\[
\frac{\varphi(k)}k.
\]

Use the standard mean

\[
\sum_{k\le X}\frac{\varphi(k)}k
\sim \frac6{\pi^2}X.
\]

The radial third-edge range contributes the semicircle integral

\[
\int_0^1\sqrt{1-t^2}\,dt=\frac\pi4.
\]

Also, the number of primitive Pythagorean triples with hypotenuse at most `H` satisfies

\[
P(H)\sim\frac{H}{2\pi},
\]

and therefore by partial summation

\[
\sum_{h\le B}^{\rm primitive}\frac1h
\sim\frac1{2\pi}\log B.
\]

Combining the two face-leg orientations, scale sum, third-edge density and primitive-face harmonic sum gives the full positive-octant ordered distinguished-face count

\[
\frac{3}{2\pi^2}B^2\log B.
\]

Every canonical raw incidence has exactly two ordered distinguished-face records, corresponding to the two orders of the face legs. Hence

\[
\boxed{
A_{ab}(B)+A_{ac}(B)+A_{bc}(B)
\sim
\frac{3}{4\pi^2}B^2\log B.
}
\]

This confirms the `B^2 log B` scale suggested by E-1c.

## 4. Directional raw asymptotic

Define the same canonical chamber integrals as Stage13:

\[
I_q=\int_{0<x<y<z,\;x^2+y^2+z^2=1}
\frac{d\sigma}{s_q(x,y,z)}.
\]

Numerically,

```text
I_ab = 0.659705248705705
I_ac = 0.3026997526726076
I_bc = 0.2712955487578571
```

with

\[
I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}.
\]

The primitive Euclid-parameter lattice is equidistributed in fixed angular sectors, while the scale/primitivity factor above is independent of which canonical position the distinguished face occupies. Thus the common arithmetic factor multiplies the three chamber integrals uniformly.

Matching the total constant gives

\[
C_E\frac{\pi^2}{8}=\frac{3}{4\pi^2},
\]

hence

\[
C_E=\frac6{\pi^4}.
\]

Therefore, at the standard primitive-lattice / partial-summation level,

\[
\boxed{
A_q(B)
\sim
\frac{6I_q}{\pi^4}B^2\log B,
\qquad q\in\{ab,ac,bc\}.
}
\]

The numerical leading constants are

```text
ab: 0.04063513425920931
ac: 0.018645061736605968
bc: 0.016710691735938064
```

and sum to

```text
3/(4*pi^2) = 0.07599088773175333.
```

## 5. The normalized raw limit is exactly the Stage13 chamber vector

Dividing by the total removes the common Euler-side factor `6/pi^4`:

\[
\frac{A_q(B)}{A_{ab}(B)+A_{ac}(B)+A_{bc}(B)}
\longrightarrow
\frac{8I_q}{\pi^2}.
\]

Thus

\[
\boxed{
P_\infty^{E,\rm raw}
=
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913).
}
\]

Equivalently,

\[
\boxed{
A_{ab}:A_{ac}:A_{bc}
\longrightarrow
2.431684750178191:1.115756428951881:1.
}
\]

This is the same chamber vector proved on the space-diagonal side.

## 6. Why imposing an integral space diagonal does not change the leading direction ratio

The two raw theorems now have the parallel forms

Euler / no integral-space-diagonal condition:

\[
\boxed{
A_q^E(B)
\sim
\frac{6I_q}{\pi^4}B^2\log B.
}
\]

Stage13 / integral space diagonal:

\[
\boxed{
A_q^S(B)
\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

So imposing

\[
a^2+b^2+c^2=\square
\]

changes both the global density and the logarithmic scale:

```text
Euler side:    B^2 log B
Stage13 side:  B (log B)^3
```

but it changes them through a factor that is common to `ab/ac/bc` at leading order. The **directional factor remains `I_q`**.

Geometrically this is natural. The one-face equation already inserts the factor `1/p`, and canonical sorting converts that into the three weights `1/s_q`. Requiring the complementary Pythagorean extension to an integral space diagonal changes how frequently a radial/arithmetic shell survives, but does not change which canonical face has which `1/s_q` real density.

So the surprising numerical observation from E-1c has a structural explanation:

> **integral-space-diagonal filtering changes the amount of population far more than it changes its leading canonical direction.**

## 7. Finite E-1c data move toward the predicted chamber

Although E-1c recorded exactly-one counts rather than raw incidences, their normalized `L1` distance to the chamber vector decreases at every audited cutoff:

```text
B=10,000   L1 = 0.0858618
B=20,000   L1 = 0.0794553
B=50,000   L1 = 0.0720708
B=100,000  L1 = 0.0673185
B=200,000  L1 = 0.0631441
B=500,000  L1 = 0.0584037
```

The total exactly-one count divided by the raw predicted main term also rises

```text
0.8909 -> 0.9242
```

over the same range.

These are consistency diagnostics only because E-1d has not yet proved that the pair-overlap correction is lower order.

## 8. Remaining exact-one gap

Write pair overlaps as

```text
O_ab_ac
O_ab_bc
O_ac_bc
```

and triple overlap as `T`.

To transfer the raw theorem to exactly-one it is enough to prove

\[
\boxed{
O_{qr}(B)=o(B^2\log B)
}
\]

for all three pairs. Then `T` is automatically lower order and exact inclusion-exclusion gives

\[
N_q(B)=A_q(B)+o(B^2\log B).
\]

The natural E-1e route is a fixed-prime quadratic-residue sieve inside the Euler raw population, analogous in architecture to Stage13-7jf but technically simpler because there is only one Pythagorean face condition in the starting population.

## 9. Decision

```text
E_1D=COMPLETE_AT_RAW_DIRECTIONAL_STRUCTURAL_ASYMPTOTIC_LEVEL
RAW_SCALE=B^2_LOG_B
RAW_TOTAL_CONSTANT=3/(4*pi^2)
RAW_DIRECTIONAL_CONSTANT_q=6*I_q/pi^4
RAW_NORMALIZED_LIMIT_EQUALS_STAGE13_CHAMBER=true
SPACE_DIAGONAL_INTEGRALITY_CHANGES_ABSOLUTE_SCALE=true
SPACE_DIAGONAL_INTEGRALITY_CHANGES_LEADING_Iq_FACTOR=false
PAIR_OVERLAP_LOWER_ORDER_PROVED=false
EXACT_ONE_DIRECTIONAL_LIMIT_PROVED=false
NEXT=E-1e fixed-prime overlap sieve and exact-one synthesis
```
