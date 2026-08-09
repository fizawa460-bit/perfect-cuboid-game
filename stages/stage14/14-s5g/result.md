# Stage14-s5g — first centered global character-sum candidate

## Purpose

Stage14-s5f completed the full local 2-descent character system. The next analytic problem is to average the resulting moving reciprocity conditions over primitive opposite-parity Euclid pairs without discarding the Stage14-s3 small-point window.

This step formulates the first prime-level large-sieve input and stress-tests its indispensable local centering. It does **not** prove a family large-sieve theorem.

## Five-factor system

For a primitive opposite-parity pair ((m,n)), use

[
F=(m, n, m-n, m+n, m^2+n^2).
]

For an odd prime (p) and a nonempty mask (ein{0,1}^5), put

[
P_e(m,n)=prod_{i=1}^5 F_i(m,n)^{e_i}.
]

The raw trace is the Legendre symbol (chi_p(P_e(m,n))), with value zero when (pmid P_e).

## Necessary local centering

Define the exact finite-field mean

[
eta_{p,e}=
rac{sum_{(u,v)inmathbf F_p^2setminus{(0,0)}}chi_p(P_e(u,v))}
{#{(u,v)
e(0,0):p
mid P_e(u,v)}},
]

and the centered trace

[
C_{p,e}(m,n)=chi_p(P_e(m,n))
-eta_{p,e},1_{p
mid P_e(m,n)}.
]

The uncentered formulation is false as a cancellation statement. Exact local resonances occur for the tested range at:

- (p=3), masks (21,22,25,26);
- (p=5), masks (15,19,21,22,25,26,28);
- (p=17), mask (31).

On those rows the nonzero raw trace is identically (+1) or (-1). These are finite local main terms, not evidence against a centered global inequality.

## First candidate inequality

For a dyadic box (mathcal B(R,S)) of primitive opposite-parity pairs and arbitrary coefficients (a_{m,n}), the first prime-level target is

[
sum_{substack{ple Q\p {m odd}}}
sum_{e
e0}
left|
sum_{(m,n)inmathcal B(R,S)}
a_{m,n}C_{p,e}(m,n)
ight|^2
ll_arepsilon
(RS+Q^4)(RSQ)^arepsilon
sum_{(m,n)inmathcal B(R,S)}|a_{m,n}|^2.
]

The (Q^4) scale is a deliberately conservative two-variable target, not an optimized or proved exponent. Even a proof of this prime-level statement would not yet average the reciprocal off-diagonal divisor interactions in the full s5 admissibility expansion, global solubility/Sha, or the s3 height window.

## Finite stress test

The deterministic audit checks all 31 nonempty masks, every odd prime (ple97), and all primitive opposite-parity pairs with (m^2+n^2le B).

| (B) | pairs | tested sums | worst centered normalized absolute sum | centered mean square / pair |
|---:|---:|---:|---:|---:|
| 2,000 | 319 | 744 | 0.4357366771 | 1.1315463110 |
| 5,000 | 792 | 744 | 0.3308080808 | 1.1797132235 |
| 10,000 | 1,593 | 744 | 0.2433460076 | 0.9751898151 |
| 20,000 | 3,186 | 744 | 0.1628944852 | 0.7469014146 |

At (B=20,000), the worst centered row is (p=83), mask (4), i.e. the single factor (m-n), with centered sum (511) over (3137) nonzero terms. This is finite diagnostic evidence only; it supplies no uniform estimate in (p,Q,R,S).

The audit also rechecks that the five factor values have pairwise disjoint odd-prime support for every enumerated primitive opposite-parity pair.

## What s5g settles

```text
STAGE14_S5G=FIRST_GLOBAL_CHARACTER_SUM_CANDIDATE_AND_FINITE_STRESS_TEST
RAW_UNCENTERED_CHARACTER_SUM_CANDIDATE_VALID=false
EXACT_LOCAL_MEAN_SUBTRACTION_REQUIRED=true
ODD_FACTOR_SUPPORT_PAIRWISE_DISJOINT_RECHECKED=true
NONTRIVIAL_FACTOR_MASKS_TESTED=31
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_WINDOW_AVERAGED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5h isolate reciprocal off-diagonal forms and prove a first dyadic bilinear bound or exhibit the obstruction
```

## Boundary

The finite decay above is not promoted to a theorem, power saving, density, or square-root law. The next step must expand the actual s5 local indicator, isolate the reciprocal off-diagonal bilinear forms between squarefree pieces of the five factors, and either prove a dyadic estimate for one such form or identify a precise obstruction.
