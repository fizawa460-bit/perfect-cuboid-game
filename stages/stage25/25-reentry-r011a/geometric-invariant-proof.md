# Stage25-reentry r011a — geometric invariant proof for the log-power ladder

STATUS=SUBMITTED_PENDING_FRESH_AUDIT
ROUTE_ID=Stage25-um-r011a
PARENT_TASK=Stage25-u21-r005a
PARENT_PR=1009
PARENT_MERGE_COMMIT=8765eb73db07da8afb8ad9b1f9a538ff8cd080ee

## 1. Three raw distinguished-incidence surfaces

The comparison uses the leading raw incidence spaces; the exact-one/exactly-two postfilters are lower order by the already audited E-1e, Stage13, and Stage15-2b interfaces.

### Euler one-face source `X_E`

Use projective coordinates `[e:x:y:u]` with

\[
X_E:\quad u^2=e^2+x^2.
\]

The third edge `y` is free.  This is the split quadric cone.  Its minimal resolution is the Hirzebruch surface `F_2`.  If `S` is the negative section and `F` a ruling, the pullback of the projective hyperplane class is

\[
H=S+2F,
\]

and

\[
K_{F_2}=-2S-4F=-2H.
\]

Hence, for this height line bundle,

\[
a(H)=2,
\]

and because `K+2H=0` the generalized Manin `b` invariant is the Picard rank

\[
b(H)=\rho(F_2)=2.
\]

Thus the geometric invariant pair is

\[
\boxed{(a_E,b_E)=(2,2)}.
\]

The physical cutoff is the homogeneous metric

\[
H_R=\sqrt{e^2+x^2+y^2}=R,
\]

so no polynomial/logarithmic height adapter is needed.  E-1d independently proves the corresponding leading scale `B^2 log B`; its unique source logarithm is the primitive-hypotenuse harmonic sum.

### One-face plus integral-space target `X_S`

Use projective coordinates `[a:b:c:p:d]` with

\[
X_S:\quad p^2=a^2+b^2,\qquad d^2=p^2+c^2.
\]

This is a quartic complete intersection of two quadrics.  Its singular points over `Qbar` are

\[
[1:i:0:0:0],\ [1:-i:0:0:0],\ [0:0:1:0:1],\ [0:0:-1:0:1],
\]

all of type `A_1`.  The first pair is conjugate over `Q(i)` and the second pair is rational.

Over `Q(i)` there is an explicit isomorphism to the Stage15 split shared-edge surface

\[
X_T:\quad U^2=E^2+X^2,\qquad V^2=E^2+Y^2
\]

via

\[
[E:X:Y:U:V]=[p:i b:c:a:d].
\]

Indeed

\[
U^2-E^2-X^2=-(p^2-a^2-b^2),
\]

and

\[
V^2-E^2-Y^2=d^2-p^2-c^2.
\]

Stage15-2a identifies the split minimal resolution as

\[
Y_T=\operatorname{Bl}_4(P^1\times P^1)
\]

at the four torus-fixed corners, with Picard rank six.  Under complex conjugation the displayed twist is `X -> -X`.  In the Stage15 toric parametrization this is induced exactly by

\[
(m:n)\longleftrightarrow(n:m),\qquad (r:s)\text{ fixed},
\]

because this swaps the sign of `m^2-n^2` and leaves `mn`, `m^2+n^2`, and the entire second pair unchanged.

On the Picard basis

\[
F_1,F_2,E_{00},E_{10},E_{01},E_{11},
\]

this Galois action fixes `F_1,F_2` and swaps

\[
E_{00}\leftrightarrow E_{10},\qquad E_{01}\leftrightarrow E_{11}.
\]

Therefore the invariant Picard subspace has basis

\[
F_1,\ F_2,\ E_{00}+E_{10},\ E_{01}+E_{11},
\]

and

\[
\boxed{\rho(Y_S/\mathbf Q)=4}.
\]

The complete intersection adjunction identity gives `K_X=O_X(-1)`.  The `A_1` resolution is crepant, so the pullback of `O_X(1)` is `-K_{Y_S}`.  On positive physical points `d` is the largest projective coordinate, and `d=R`, so the Stage13 cutoff is an anticanonical height with no exponent-changing adapter.

Thus

\[
\boxed{(a_S,b_S)=(1,4)}.
\]

The already audited Stage12/13 theorem `N_1(B)~kappa/(24*pi) B(log B)^3` has exactly the predicted exponent pair `B^{a_S}(log B)^{b_S-1}`.  This geometric calculation is an explanation of the exponents, not a replacement proof of the Stage12/13 leading constant.

### Exactly-two no-space target `X_T`

Stage15-2a/2b already prove that the shared-edge surface has split toric minimal resolution

\[
Y_T=\operatorname{Bl}_4(P^1\times P^1),\qquad \rho(Y_T)=6,
\]

and that the physical `R` height is anticanonical.  Hence

\[
\boxed{(a_T,b_T)=(1,6)}
\]

and Stage15-2b proves

\[
M_2(B)\sim C_{M_2}B(\log B)^5.
\]

## 2. Exact exponent ledger

The three existing asymptotics and the geometric invariants align as

| population | geometry | `(a,b)` | leading scale |
|---|---|---:|---|
| `M1` | split quadric cone / `F_2` resolution | `(2,2)` | `B^2(log B)^1` |
| `N1` | `Q(i)`-twisted `4A1` quartic del Pezzo | `(1,4)` | `B(log B)^3` |
| `M2` | split `4A1` quartic del Pezzo | `(1,6)` | `B(log B)^5` |

Therefore the Stage21 transition has

\[
\Delta a=-1,\qquad \Delta b=+2,
\]

which is exactly

\[
N_1/M_1\asymp B^{-1}(\log B)^2,
\]

while the Stage22 transition has

\[
\Delta a=-1,\qquad \Delta b=+4,
\]

which is exactly

\[
M_2/M_1\asymp B^{-1}(\log B)^4.
\]

The cross-target comparison has

\[
\Delta a=0,\qquad \Delta b=+2,
\]

and hence

\[
\boxed{
\frac{M_2(B)}{N_1(B)}
\sim
\frac{24\pi C_{M_2}}{\kappa}(\log B)^2.
}
\]

This is a population-size comparison between different adjacent arithmetic strata, not a conditional probability.

## 3. Meaning of `2+2`

There is now a rigorous additive **geometric-invariant ledger**:

\[
\boxed{
b_T-b_E=(b_S-b_E)+(b_T-b_S)=(4-2)+(6-4)=2+2=4.
}
\]

Thus `2+2` is valid as a decomposition of the Manin `b`-invariant jump.  It is **not** a product of four independent local events or four independent harmonic sums.

The first `+2` is the Picard/face-codimension jump from the Euler one-face source to the twisted nested-Pythagorean surface.  The second `+2` is the additional rational Picard rank present in the split common-leg quartic-del-Pezzo resolution relative to its `Q(i)`-twisted one-face-plus-space form.

This also explains why Stage21 and Stage22 share the same polynomial `B^-1` cost: both targets have `a=1`, whereas the Euler one-face source has `a=2`.

## 4. Analytic slot boundary

Stage12 additionally exposes its target `log^3` through

\[
\iint \frac{\log x\log y}{x^2+y^2}\,dx\,dy
=\frac\pi{48}(\log B)^3+O((\log B)^2),
\]

while E-1d exposes the source `log` through the primitive-hypotenuse harmonic sum.  The present geometric ledger explains the **net exponents** without identifying those analytic summation variables one-for-one.

Therefore the following stronger statements remain false/unproved:

- `H(P)` contributes exactly one independent log and `L_B(P)` exactly one;
- the Euler hypotenuse harmonic log is literally the same analytic pole slot as the Stage12 radial harmonic log;
- the Stage22 four-log enhancement factors into four independent local probabilities;
- four named independent poles have been exhibited in one common Dirichlet series.

The fine mechanism is closed at the geometric Manin-invariant level, not at the independent local-factor/pole-slot level.

```text
GEOMETRIC_MANIN_INVARIANT_LEDGER_PROVED=true
M1_MANIN_A=2
M1_MANIN_B=2
N1_MANIN_A=1
N1_MANIN_B=4
M2_MANIN_A=1
M2_MANIN_B=6
G21_LOG2_FINE_MECHANISM=CLOSED_AT_GEOMETRIC_INVARIANT_LEVEL
G22_LOG4_FINE_MECHANISM=CLOSED_AT_GEOMETRIC_INVARIANT_LEVEL
LOG4_B_INVARIANT_JUMP=4
LOG4_DECOMPOSITION_AS_B_JUMPS=2+2
FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false
COMMON_DIRICHLET_POLE_SLOT_LEDGER_PROVED=false
PERFECT_CUBOID_CONCLUSION=NONE
```
