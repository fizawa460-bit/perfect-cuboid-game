# Stage28-60-r3 split C — exact Saunderson physical M-degree-six certificate

```text
SPLIT_ID=Stage28-60-r3C
ROLE=TARGET_RATIONAL_CURVE_DEGREE_CERTIFICATE
STATUS=COMPLETE_AS_R3_SUBMISSION_PENDING_FRESH_AUDIT
DEPENDS_ON=Stage28-60-r3B target polarization adapter
```

Split B identifies the Stage20 physical line bundle as

\[
M_{face}=\Phi_{face}^*\mathcal O_{\mathbf P^2}(1),
\]

where `Phi_face` is the physical edge-coordinate map. This split computes the degree of the generalized Saunderson curve with respect to that exact line bundle.

## 1. Homogeneous Saunderson map

For homogeneous Euclid parameters `[r:s]`, put

\[
u=r^2-s^2,\qquad v=2rs,\qquad w=r^2+s^2.
\]

Use the signed algebraic formulas

\[
A=u(4v^2-w^2),\qquad
B=v(4u^2-w^2),\qquad
C=4uvw,
\]

and face diagonals

\[
D=w^3,\qquad
E=u(4v^2+w^2),\qquad
F=v(4u^2+w^2).
\]

Every one of `A,B,C,D,E,F` is homogeneous of degree six in `(r,s)`.

The three edge forms `A,B,C` have no common nonconstant factor. Indeed any common factor must divide

\[
C=4uvw.
\]

The factors `u,v,w` are pairwise coprime over `Q[r,s]`; `u` does not divide `B`, `v` does not divide `A`, and `w` does not divide `A`. Hence

\[
\gcd(A,B,C)=1.
\]

Therefore the physical edge map

\[
[r:s]\longmapsto[A:B:C]\in\mathbf P^2
\]

pulls back `O_{P^2}(1)` to `O_{P^1}(6)`.

## 2. The full K3 parametrization is generically birational

The degree-six forms satisfy the exact identities

\[
E-A=2uw^2,
\qquad
F-B=2vw^2.
\]

Consequently

\[
2D+E-A
=2w^3+2uw^2
=4r^2w^2,
\]

while

\[
F-B=4rsw^2.
\]

On the dense open set `r w != 0`, the original parameter is recovered rationally from the image by

\[
\boxed{
\frac{s}{r}
=
\frac{F-B}{2D+E-A}.
}
\]

Thus the normalization map from `P^1` to the Saunderson image curve on the Stage20 K3 has generic degree one. This removes the possible ambiguity that a degree-six list of coordinate forms might parametrize a lower-degree curve multiple times.

## 3. Exact physical M-degree

Let `C_S` be the Stage20 Saunderson image curve. By split B,

\[
M_{face}=\Phi_{face}^*\mathcal O_{\mathbf P^2}(1).
\]

Because the parametrization is birational and its three edge coordinates are basepoint-free homogeneous degree-six forms,

\[
\deg f^*M_{face}=6.
\]

Hence

\[
\boxed{M_{face}\cdot C_S=6}.
\]

This is the same physical polarization normalization used for the Stage19 source: both are pullbacks of `L=-K_Y` from the same two-face toric base, although they live on different K3 covers.

## 4. Physical counting sector

The already-audited Stage28-50-r2 cone gives `R asymp r^6` and a positive-density primitive opposite-parity Euclid parameter set. If one wants a single sign chamber for the signed algebraic formulas, restrict further to for example

\[
1/3\le s/r\le1/2,
\]

which remains a positive-width subcone. Absolute values then differ from the signed projective coordinates only by fixed coordinate signs.

Rational points on `P^1` of parameter height at most `T` have order `T^2`; with physical height `R asymp T^6`, this fixed rational curve contributes

\[
\boxed{\Theta(B^{1/3})}.
\]

This agrees exactly with the fixed-curve exponent rule `2/(M.C)=2/6=1/3`.

## Route verdict

The previously informal phrase "degree-six Saunderson family" is now promoted, at r3 submission level, to an exact **physical `M_face`-degree-six rational curve** statement under the same Stage28 polarization normalization as the Stage19 `M_sp`-degree spectrum.

What it does and does not show:

```text
STAGE20_SAUNDERSON_PHYSICAL_M_DEGREE=6_CANDIDATE
STAGE20_FIXED_M6_RATIONAL_CURVE=PRESENT_CANDIDATE
STAGE20_FIXED_CURVE_EXPONENT_ONE_THIRD=EXACT_FROM_M_DEGREE_CANDIDATE
STAGE19_M4_VOID=ABSENT_AUDITED
STAGE19_M5_VOID=ABSENT_R3_CANDIDATE
STAGE19_M6_VOID_PROVED=false
STRICT_SOURCE_TARGET_FIXED_CURVE_SPECTRUM_SEPARATION_PROVED=false
NEW_CAUSAL_ROUTE_VALID=true
BRIDGE_ORDERING_RESOLVED=false
```

The new route is therefore real but bounded: the target attains physical degree six, while the source has been pushed up to a candidate floor of six. A strict spectral asymmetry would require the remaining source `M=6` classification to be empty; without that, this route sharpens mechanism comparison but does not place `I_face/I_sp` across the critical `(log B)^(-2)` threshold.

The standard-library exact probe is

```text
stages/stage28/28-60-r3/saunderson_physical_degree6_probe.py
```

and checks the degree-six homogeneity, Euler-brick identities, basepoint-free edge map, and the rational inverse formula above.
