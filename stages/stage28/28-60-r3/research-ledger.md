# Stage28-60-r3 — final bounded exploration ledger

Checkpoint60 parent + r2 already tested causal decomposition, double-charge control, interaction ladders, normalized interaction curvature, branch-profile comparison, common-host reformulations, local/Huang/K3 symmetry, and bounded branch-sensitive literature rematches. r3 avoids repeating those lanes.

## Materially distinct r3 routes

1. `R21_FIXED_CURVE_SPECTRUM_COMPARISON`: reuse the audited Stage19 physical `M.C=4` void and compare low-degree fixed-curve mechanisms with Stage20.
2. `R22_MCKINNON_REMATCH`: test McKinnon's hyperelliptic-K3 accumulating-curve theorem; direct import fails because the repo physical polarization is big-and-nef non-ample.
3. `R23_QUASIPOLARIZED_LOW_DEGREE_REMATCH`: test quasi-polarized low-degree rational-curve literature; no direct M5/M6 classification at `M^2=8`.
4. `R24_STAGE19_MOVING_MECHANISM_FIREWALL`: retain Stage14-4al; fixed curves cannot be promoted to a whole-population bound while moving first-small-point activation remains live.
5. `R25_FINITE_LATTICE_RECEIVER`: reduce the remaining low-degree source question to exact Shimada lattice/chamber/descent data.
6. `R26_ODD_DEGREE_ANTI_INVARIANT_CONGRUENCE`: reconstruct the physical anti-invariant lattice and eliminate every odd physical M-degree, in particular M5, subject to fresh audit.
7. `R27_DISTINGUISHED_ROOT_M6_DIAGNOSTIC`: evaluate the 40 distinguished Shimada roots; histogram `0:16, 2:24`, with no M6 witness, diagnostic only.
8. `R28_COMMON_PHYSICAL_POLARIZATION_SAUNDERSON_M6_CERTIFICATE`: independently verify that the Stage20 Saunderson curve has physical M-degree exactly six under the same common-base polarization normalization used by Stage19.

## R26 source obstruction

The r3 Shimada reconstruction gives anti-invariant rank `6`, positive determinant `256`, and every integral anti-invariant norm `0 mod 4`. For a physical odd-degree split curve `C`, with `x=C-delta(C)`,

\[
-x^2\equiv2(M\cdot C)\pmod4.
\]

Thus odd physical M-degree is impossible. Combined with the audited Stage14-4ak M4 void, the candidate fixed-curve source floor is M-degree six.

## R28 split certificate

To avoid the long-run timeout, R28 was executed in three independent pieces:

```text
r3A source polarization lock
r3B target physical-polarization adapter
r3C exact Saunderson M-degree-six algebra
```

Stage14-e3 fixes

\[
Y=Bl_4(P^1\times P^1),\qquad L=-K_Y,
\qquad \phi^*O_{P^2}(1)=L.
\]

The two completion K3 surfaces are distinct, but both physical quasi-polarizations are pullbacks of the same base line bundle:

\[
M_{sp}=\pi_{sp}^*L,\qquad M_{face}=\pi_{face}^*L,
\qquad M_{sp}^2=M_{face}^2=8.
\]

Hence their curve degrees use the same physical normalization. For Saunderson,

\[
u=r^2-s^2,\quad v=2rs,\quad w=r^2+s^2,
\]

and `A,B,C,D,E,F` are all homogeneous degree six. The edge forms have no common nonconstant factor. Moreover

\[
E-A=2uw^2,\qquad F-B=2vw^2,
\qquad \frac{s}{r}=\frac{F-B}{2D+E-A}
\]

on a dense open set, so the parametrization is generically birational. Therefore the image curve `C_S` satisfies

\[
\boxed{M_{face}\cdot C_S=6}.
\]

On the audited physical cone this yields `Theta(B^(1/3))`, exactly matching the fixed-curve exponent `2/6`.

This is a genuine new route because it closes the previously implicit polarization/degree adapter rather than merely reusing the construction-height exponent.

## Exact CI support

The existing low-degree workflow already reconstructs the Shimada physical labeling, anti-invariant lattice, mod-four norm law and L40 diagnostic. It has now been extended with

```text
stages/stage28/28-60-r3/saunderson_physical_degree6_probe.py
```

to check the homogeneous degree-six forms, Euler-brick identities, basepoint-free edge map and rational inverse. CI support is evidence only; theorem-level promotion remains subject to fresh Stage28 audit.

## Stop test

The fixed-curve spectra are now asymmetric through degree five and Stage20 attains degree six, but strict M6 separation is not proved because the Stage19 M6 stratum remains open. The only remaining finite receiver is

```text
NEXT_FINITE_RECEIVER=PhysicalLowDegreeRootSpectrumM6
```

and the global bridge still requires a substantially new moving-complement/branch-sensitive theorem controlling `I_face/I_sp` relative to `(log B)^(-2)` without using the deferred endpoint count.

```text
R3_MATERIALLY_DISTINCT_ROUTES=8
NEW_NUMERIC_BRIDGE_BOUND=false
NEW_CAUSAL_DIFFERENTIAL=true
ODD_PHYSICAL_M_DEGREE_OBSTRUCTION_CANDIDATE=true
STAGE19_M5_FIXED_CURVE_ABSENT_CANDIDATE=true
STAGE19_FINITE_FIXED_CURVE_EXPONENT_MAX_CANDIDATE=1/3
STAGE20_SAUNDERSON_PHYSICAL_M_DEGREE6_CANDIDATE=true
COMMON_PHYSICAL_POLARIZATION_ADAPTER_CANDIDATE=PASS
STRICT_SOURCE_TARGET_M6_SPECTRAL_SEPARATION=false
DISTINGUISHED_L40_M6_WITNESS_FOUND=false
MAXIMAL_BOUNDED_EXPLORATION_CANDIDATE=true
FURTHER_ROUTINE_REPO_ALGEBRA_EXPECTED_TO_PROGRESS=false
```
