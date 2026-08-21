# Stage28-60-r3 — fixed rational-curve spectrum comparison

```text
ROUTE=R21_FIXED_CURVE_SPECTRUM_PLUS_R26_ODD_DEGREE_PLUS_R28_COMMON_POLARIZATION_M6
CHECKPOINT=60
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## Stage19 source spectrum

Stage14-4ah fixes the physical space-cover quasi-polarization

\[
M_{sp}=\pi_{sp}^*(-K_Y),\qquad M_{sp}^2=8,
\]

and proves every physical rational curve has `M_sp.C>=4`. Stage14-4ak proves the complete physical `M_sp.C=4` stratum empty.

The r3 exact anti-invariant-lattice reconstruction gives every anti-invariant norm divisible by four. For an odd-degree physical split curve `C`, with `x=C-delta(C)`, one has

\[
-x^2\equiv2(M_{sp}\cdot C)\pmod4,
\]

which contradicts the lattice norm law. Subject to fresh audit, every odd physical source M-degree is therefore absent; in particular M5 is impossible. Thus the candidate source fixed-curve floor is degree six.

The 40 distinguished Shimada roots have M-degree histogram `0:16, 2:24`; no M6 root occurs there, but this is not a complete M6 classification.

## Same physical polarization normalization on the Stage20 cover

The common two-face toric base is

\[
Y=Bl_4(P^1\times P^1),\qquad L=-K_Y,
\]

and Stage14-e3 fixes the physical edge-coordinate map `phi:Y->P2` with

\[
\phi^*O_{P^2}(1)=L.
\]

The Stage19 space completion and Stage20 third-face completion are distinct degree-two K3 covers of the same `Y`. Their physical quasi-polarizations are

\[
M_{sp}=\pi_{sp}^*L,\qquad M_{face}=\pi_{face}^*L,
\]

so both have square `8` and both measure curve degree against the same physical edge-coordinate line bundle. This is the exact Stage28 meaning of “same physical polarization”; it does not identify the two K3 surfaces.

## Stage20 Saunderson curve has physical M-degree six

For `[r:s] in P1`, set

\[
u=r^2-s^2,\quad v=2rs,\quad w=r^2+s^2,
\]
\[
A=u(4v^2-w^2),\quad B=v(4u^2-w^2),\quad C=4uvw,
\]
\[
D=w^3,\quad E=u(4v^2+w^2),\quad F=v(4u^2+w^2).
\]

All six forms are homogeneous degree six. The edge forms `A,B,C` have no common nonconstant factor, so the physical edge map pulls `O_{P2}(1)` back to `O_{P1}(6)`.

The full Saunderson map is generically birational because

\[
E-A=2uw^2,\qquad F-B=2vw^2,
\]

and on a dense open set

\[
\frac{s}{r}=\frac{F-B}{2D+E-A}.
\]

Therefore for its Stage20 image curve `C_S`,

\[
\boxed{M_{face}\cdot C_S=6}.
\]

On the audited positive-density physical cone, `R\asymp r^6`, so this curve contributes `Theta(B^(1/3))`. This agrees with the rational fixed-curve height exponent `2/(M.C)=1/3`.

Exact split artifacts:

```text
split-a-source-polarization-lock.md
split-b-target-polarization-adapter.md
split-c-saunderson-mdegree6-certificate.md
saunderson_physical_degree6_probe.py
```

## Spectrum verdict

```text
STAGE19_FIXED_M4_CURVE=ABSENT_AUDITED
STAGE19_FIXED_ODD_M_DEGREE_CURVES=ABSENT_CANDIDATE
STAGE19_FIXED_M5_CURVE=ABSENT_CANDIDATE
STAGE19_FIXED_M6_CURVE_ABSENCE_PROVED=false
STAGE19_FINITE_FIXED_CURVE_EXPONENT_MAX_CANDIDATE=1/3
STAGE20_SAUNDERSON_PHYSICAL_M_DEGREE=6_CANDIDATE
STAGE20_FIXED_M6_RATIONAL_CURVE=PRESENT_CANDIDATE
STAGE20_FIXED_CURVE_EXPONENT_AT_LEAST=1/3
```

Thus Stage20 definitely reaches the degree-six slot at r3 submission level, while Stage19 has been cleared only below six. The finite spectra are asymmetric through degree five, but a strict degree-six separation is not yet proved.

The remaining finite receiver is

```text
NEXT_FIXED_CURVE_FINITE_RECEIVER=PhysicalLowDegreeRootSpectrumM6
```

and the global moving/collective complement theorem is still mandatory. No fixed-curve statement alone resolves `I_face/I_sp` relative to `(log B)^(-2)` or orders `M3` against `N2`.

```text
COMMON_PHYSICAL_POLARIZATION_ADAPTER=PASS_CANDIDATE
SAUNDERSON_PHYSICAL_M6_CERTIFICATE=PASS_CANDIDATE
FIXED_CURVE_SPECTRUM_IS_A_REAL_CAUSAL_DIFFERENTIAL=true
FIXED_CURVE_SPECTRUM_ALONE_RESOLVES_J28_THRESHOLD=false
GLOBAL_COMPLEMENT_RECEIVER_STILL_REQUIRED=true
ENDPOINT_COUNT_USED=false
AUDIT_REQUIRED=true
```
