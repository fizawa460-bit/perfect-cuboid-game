# Stage14-e supplement roadmap — post-control-track refinements

## Purpose

Stage14-e1 through Stage14-e5 form a completed control experiment. They are not reopened here. This supplement track sharpens the solved ambient theory without changing the main Stage14 integer-space-diagonal problem.

The literature-first rule remains mandatory: every supplement must refresh primary literature before promoting a constant, secondary term, effective error, or novelty claim.

## 14-e6 — explicit Peyre/Tamagawa constant

Status: [x] Complete.

Stage14-e6 replaces the e4 placeholder

\[
E_q(B)\sim \Lambda_E M_q B(\log B)^5
\]

by the explicit physical-height arithmetic factor

\[
\boxed{
\Lambda_E
=
\frac1{81920}
\prod_{p\ge3}
\left(1-\frac1p\right)^6
\left(1+\frac6p+\frac1{p^2}\right).
}
\]

Locked components:

```text
alpha(Y)=1/2880
beta(Y)=1
archimedean scale relative to e4 M_q = 1/4
odd-prime factor=(1-1/p)^6*(1+6/p+1/p^2)
physical p=2 factor=9/64
```

A deterministic prime product through `10^6` plus a rigorous tail estimate gives

\[
8.60794782429708\times10^{-7}
<\Lambda_E<
8.60811998497517\times10^{-7},
\]

and therefore

\[
1.47953102009666\times10^{-6}
<C_E<
1.47956061101297\times10^{-6}
\]

for

\[
E_2(B)\sim C_EB(\log B)^5.
\]

The e4 thin-set theorem transfers the same coefficient from raw ambient points to the exactly-two population.

Canonical artifacts:

```text
stages/stage14/14-e6/result.md
stages/stage14/14-e6/literature-constant-audit.md
stages/stage14/scripts/14-e6/explicit_peyre_constant_audit.py
stages/stage14/data/14-e6/explicit_peyre_constant_audit.json
```

Historical handoff retained for e6 compatibility:

```text
NEXT_E_SUPPLEMENT=Stage14-e7 secondary asymptotics / finite crossover
```

## 14-e7 — secondary-asymptotic boundary / finite crossover

Status: [x] Complete as a rigorous crossover diagnosis; full secondary polynomial remains open.

Batyrev--Tschinkel gives the order-six leading pole at `s=1`. Formally, if

\[
Z(s)=\sum_{j=1}^{6}A_{-j}(s-1)^{-j}+O(1),
\]

then an effective contour shift would produce

\[
B(c_5\log^5B+c_4\log^4B+c_3\log^3B+\cdots)
\]

with

\[
c_5=A_{-6}/5!,
\qquad
c_4=(A_{-5}-A_{-6})/4!,
\qquad
c_3=(A_{-4}-A_{-5}+A_{-6})/3!.
\]

Stage14-e6 evaluates `c5=C_E`. Stage14-e7 records that the physical Euclidean metric still lacks the verified left-half-plane continuation and vertical growth bounds required to promote the full polynomial via the effective Chambert-Loir--Tschinkel Tauberian framework.

The finite side is nevertheless settled diagnostically. A dense exact census at 17 cutoffs through `B=10^6` shows that the proved `B(log B)^5` leading term contributes only about

\[
\boxed{5.3892\%}
\]

of the exact count at the ceiling. More than `94.61%` is still pre-asymptotic/lower-order mass at that scale.

Anchored finite fits

\[
E_2(B)/(B\log^3B)\approx c_5\log^2B+c_4\log B+c_3
\]

fit the observed range very well, but their `c4,c3` drift materially as the fitting window moves. They are therefore locked only as finite effective coefficients, not Laurent coefficients.

Canonical artifacts:

```text
stages/stage14/14-e7/result.md
stages/stage14/14-e7/literature-secondary-audit.md
stages/stage14/scripts/14-e7/secondary_crossover_audit.py
stages/stage14/data/14-e7/secondary_crossover_audit.json
```

Locked boundary:

```text
FINITE_CROSSOVER_DIAGNOSIS_COMPLETE=true
FULL_SECONDARY_ASYMPTOTIC_PROVED=false
PHYSICAL_METRIC_LEFT_HALF_PLANE_CONTINUATION_VERIFIED=false
PHYSICAL_METRIC_VERTICAL_GROWTH_VERIFIED=false
FINITE_EFFECTIVE_COEFFICIENTS_ARE_LAURENT_COEFFICIENTS=false
```

Historical handoff retained for e7 compatibility:

```text
NEXT_E_SUPPLEMENT=Stage14-e8 quantitative Euler-brick thin-set count
```

## 14-e8 — quantitative Euler-brick thin-set count

Status: [x] Complete as a K3 identification plus an independent subpower-multiplicity upper envelope; a fixed relative saving remains open.

Let `R_EB(B)` count primitive unordered Euler bricks under the same physical Euclidean height.  The projective equations

\[
U^2=E^2+X^2,
\qquad
V^2=E^2+Y^2,
\qquad
Z^2=X^2+Y^2
\]

form a three-quadric model in `P^5`.  In the e4 toric presentation the third-square double cover has branch divisor class

\[
D\sim-2K_Y,
\]

so after normalization/minimal resolution the compactification is a K3 surface.  The physical height remains comparable to the projective max height:

\[
H_{\max}\le D_{\mathbf R}\le\sqrt3 H_{\max}.
\]

An independent elementary projection gives

\[
\boxed{
R_{\rm EB}(B)
\ll
B\log B
\exp\!\left(O\!\left(\frac{\log B}{\log\log B}\right)\right)
=B^{1+o(1)}.
}
\]

The proof projects to the Pythagorean triple formed by the two largest edges and bounds the remaining-edge multiplicity by `tau(n^2)`.  This controls the polynomial upper exponent but does not improve e4 to a fixed logarithmic or power saving relative to the ambient main term.

The e4 theorem is retained independently:

\[
R_{\rm EB}(B)=o(B(\log B)^5).
\]

At `B=10^6`, the exact Euclidean-height census has

\[
R_{\rm EB}=219,
\qquad
R_{\rm EB}/\sqrt B=0.219,
\]

and the third-square incidence fraction inside the raw ambient is about `4.75454e-5`.  Nested finite power fits drift substantially, so the square-root scale remains a finite candidate only.

Canonical artifacts:

```text
stages/stage14/14-e8/result.md
stages/stage14/14-e8/literature-euler-brick-count-audit.md
stages/stage14/scripts/14-e8/euler_brick_thin_count_audit.py
stages/stage14/data/14-e8/euler_brick_thin_count_audit.json
```

Locked boundary:

```text
EULER_BRICK_K3_MODEL_LOCKED=true
E8_INDEPENDENT_QUANTITATIVE_ENVELOPE_PROVED=true
EULER_BRICK_POWER_EXPONENT_UPPER_ENVELOPE=1+o(1)
QUANTITATIVE_RELATIVE_SAVING_PROVED=false
FIXED_POWER_SAVING_PROVED=false
SQRT_B_FINITE_CANDIDATE_ONLY=true
```

## 14-e9 — gcd/lcm and local-statistics decomposition

Status: [>] Next.

Resolve the ambient distribution of the common-edge gcd/lcm strata and finite-local statistics as a control object for the main Stage14 arithmetic.  In particular, use the e8 gap between the one-leg divisor envelope and the observed Euler-brick population to identify which simultaneous local/gcd/lcm constraints actually suppress completions.

```text
STAGE14_E_CONTROL_TRACK_E1_TO_E5=COMPLETE
STAGE14_E_SUPPLEMENT_TRACK=DEFINED
STAGE14_E6=COMPLETE_EXPLICIT_PEYRE_TAMAGAWA_CONSTANT
GLOBAL_ARITHMETIC_CONSTANT_LAMBDA_E_EVALUATED=true
STAGE14_E7=COMPLETE_FINITE_CROSSOVER_AND_SECONDARY_BOUNDARY
FINITE_CROSSOVER_DIAGNOSIS_COMPLETE=true
FULL_SECONDARY_ASYMPTOTIC_PROVED=false
STAGE14_E8=COMPLETE_K3_AND_SUBPOWER_MULTIPLICITY_ENVELOPE
EULER_BRICK_K3_MODEL_LOCKED=true
E8_INDEPENDENT_QUANTITATIVE_ENVELOPE_PROVED=true
QUANTITATIVE_RELATIVE_SAVING_PROVED=false
NEXT_E_SUPPLEMENT=Stage14-e9 gcd/lcm and local-statistics decomposition
```
