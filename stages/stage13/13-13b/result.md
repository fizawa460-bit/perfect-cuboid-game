# Stage13-13b — result

> STATUS: `STAGE13_13B_COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_AUDIT`
>
> PURPOSE: close the external-theorem boundary identified by Stage13-13a before canonical proof resynthesis.

## Decision

The 13-13a theorem contract survives unchanged.  Every external dependency used by the active R03 + `13-12ag` proof chain has now been mapped to a precise source/hypothesis/conclusion interface or discharged internally.

```text
UNMAPPED_EXTERNAL_INPUTS=0
FAILED_EXTERNAL_HYPOTHESES=0
THEOREM_CHANGED=false
R03_MUTATED=false
STAGE12_R09_REOPENED=false
```

## Minimal external boundary

The final Stage13 proof needs only:

1. the frozen Stage12 R09 total primitive-oriented asymptotic;
2. standard analytic continuation, functional equation and polynomial strip/conductor growth for the relevant fixed-field Dirichlet/Hecke `L`-functions;
3. Vaaler's periodic interval trigonometric majorant/minorant.

The historical general Selberg--Delange invocation is compatible with the Stage13 factors, but it is not required as an additional black-box gate: the only pole orders used are `0,1,2`, the residual factors are already holomorphic in a fixed half-plane, and the needed summatory formulas follow from a direct finite Perron/residue contour argument.

Likewise, the Merikoski/Coleman Gaussian-Hecke zero-free input quoted in R03 is valid in the retained polylogarithmic angular range, but it is stronger than necessary for the actual nonzero-harmonic coefficient sum.  Since

\[
A_\ell(s)=L(s,\xi_{8\ell})E_{h,\ell}(s)
\]

contains `L` itself rather than `1/L`, `L'/L`, or a fractional power, zeros do not obstruct the contour shift.  Analytic continuation plus strip/conductor growth suffices.

## Internalized steps

The following are not left as hidden external assumptions in the final resynthesis:

```text
special Perron/residue pole-order lemma
nonzero-harmonic contour cancellation
fixed-character orthogonality and CRT
coarea/Tonelli/Fubini justification
weighted Wiener norm algebra
Pythagorean parameterization/parity bookkeeping
infinitude of primes 3 mod 4 by the elementary Euclid argument
```

In particular, no modulus depending on `B` appears in the overlap proof: the finite prime set is fixed first, then `B -> infinity`, and only afterwards is the number of fixed primes increased.

## Source lock

The crosswalk records the following primary references:

```text
Hecke 1918/1920                  Hecke L analytic continuation / functional equation
Huang--Liu--Rudnick 2019         modern Gaussian-angular normalization/restatement
Merikoski 2025 Lemma 2.13        Gaussian-Hecke Landau--Page zero-free region
Coleman 1990                     general Hecke zero-free-region context
Delange 1954                     classical Selberg--Delange/Ikehara lineage
de la Bretèche--Tenenbaum 2021   modern Selberg--Delange hypothesis discussion
Vaaler 1985                      interval trigonometric majorant/minorant
```

The first and last items are part of the minimal final logical boundary; the Selberg--Delange and zero-free references remain valid context/provenance rather than extra gates.

## Frozen theorem contract

No constant, counting convention or asymptotic statement changes:

```text
N_q(B) ~ kappa I_q/(3 pi^3) B(log B)^3
N1(B)  ~ kappa/(24 pi) B(log B)^3
P_q    = 8 I_q/pi^2
sum I_q = pi^2/8
J_q    = 2 I_q/pi
O_qr(B)=o(B(log B)^3)
T(B)   =o(B(log B)^3)
lambda_p=(p+5)/(2(p+1))
```

## Handoff to 13-13c

The canonical proof should:

- inline the special Perron/residue lemma instead of saying only “standard Selberg--Delange machinery”;
- use Hecke analytic continuation/functional equation and polynomial strip/conductor bounds as the nonzero-harmonic external input;
- retain Merikoski's zero-free theorem only as an optional stronger reference, not a logical dependency;
- state Vaaler's approximation input explicitly;
- replace the historical invocation of Dirichlet's theorem for infinitely many `3 mod 4` primes by the elementary Euclid proof;
- preserve the 13-13a theorem statement exactly.

```text
STAGE13_13B=COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_AUDIT
UNMAPPED_EXTERNAL_INPUTS=0
FAILED_EXTERNAL_HYPOTHESES=0
MINIMAL_EXTERNAL_BOUNDARY_LOCKED=true
HECKE_ANALYTIC_CONTINUATION_FUNCTIONAL_EQUATION_REQUIRED=true
VAALER_INTERVAL_MAJORANT_REQUIRED=true
GENERAL_SELBURG_DELANGE_BLACK_BOX_REQUIRED=false
GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED_FOR_FINAL_PROOF=false
MERIKOSKI_ZERO_FREE_CITATION_VALID=true
GROWING_MODULUS_INPUT_USED=false
DIRICHLET_AP_THEOREM_REQUIRED=false
THEOREM_CHANGED=false
R03_MUTATED=false
STAGE12_R09_REOPENED=false
NEXT=13-13c
```
