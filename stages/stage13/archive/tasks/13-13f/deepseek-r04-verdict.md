# DeepSeek R04 external review verdict

> PROVENANCE: `USER_RELAYED_EXTERNAL_REVIEW`
>
> TARGET_BUNDLE_ID: `STAGE13-FINAL-SELF-CONTAINED-20260809-R04`
>
> TARGET_CONTENT_SHA256: `789656b5bb2190ae62cf2dcae7a3da06ece4f473780a1229ba7284b10b7f4f1b`
>
> RECORDED_VERDICT: `REPAIRABLE`
>
> R04_IMMUTABLE: `true`

## Overall assessment

DeepSeek judges the principal strategy and theorem claim to be mathematically plausible/correct in structure, but finds the R04 bundle insufficiently self-contained and insufficiently explicit at several proof-critical technical interfaces. The review recommends producing R05 or R06 rather than freezing R04.

This verdict is recorded as `REPAIRABLE`, not `CLOSED`: the reviewer does not identify a direct contradiction proving the theorem false, but does identify proof-completeness defects requiring substantive exposition and possibly proof hardening before final freeze.

## 1. Missing explicit Wiener-norm derivation

The bound

```text
||C_{ell,p}-1||_{5/8} <= 529 p^(-5/4)
```

is stated in R04 without derivation. Because this estimate supports convergence of the mixed correction and the logarithmic-moment argument, DeepSeek requests either an explicit derivation or a fully specified internal lemma/reference showing how the constant and support structure arise.

## 2. Curved-region error accumulation

The review flags the small-height, small-coordinate, core-box, boundary-thickening and power-tail estimates in §7 as insufficiently expanded. In particular, the proof should expose the uniformity needed when summing over `O((log B)^C)` multiplicative boxes and make the dependence on `H0`, `U`, and the mesh parameter explicit.

## 3. Nonzero-harmonic uniformity

DeepSeek requests an explicit bridge from the Hecke bound

```text
sum_{h<=X} a_ell(h) << X^(1-delta') (1+ell)^C
```

to the claimed retained-harmonic error when `ell <= (log B)^4`. The current phrase "polynomial strip/conductor growth" is considered too implicit for a self-contained final-review package.

## 4. Stage12 interface incompletely copied into R04

The review says the frozen Stage12 R09 input should include a complete definition of `C_prim(B)` and the exact counting/orientation convention needed for

```text
C_prim^proj,q(B)=2 A_q(B)
C_prim(B)=2 sum_q A_q(B).
```

R04 currently states the bridge but does not reproduce enough of the upstream counting convention for a reader to audit the factor two without repository browsing.

## 5. External theorem interfaces need precise hypotheses

The reviewer requests a proof-facing statement of the exact external conditions used from:

- Dirichlet/Gaussian-Hecke analytic continuation and functional equation;
- polynomial strip/conductor growth, including the relevant strip and `ell`-dependence;
- Vaaler interval approximation, including the nonzero Fourier coefficient control used in §8.

The complaint is not that such results are unavailable, but that R04 does not state their imported contracts precisely enough.

## 6. Fixed-prime overlap transfer needs expansion

The fixed inert-prime transfer in §13 is considered too compressed. DeepSeek asks for an explicit character decomposition showing why:

- the principal tuple multiplies the raw main term by `prod_{p in S} lambda_p`;
- nonprincipal tuples lose at least one zeta pole and are `o(B(log B)^3)` for fixed `S`;
- the mixed correction remains harmless under the fixed-conductor residue restrictions.

## 7. Notation and local-factor definitions

The review asks to distinguish the spherical coordinate angle `theta` from the later local angular phase, and to make the `p`-dependence of `C_{ell,p}` and substitutions `x=p^{-s_h}`, `y=p^{-s_r}`, `z=p^{-s_s}` explicit.

## 8. Deterministic audit positioning

DeepSeek accepts the finite checks as consistency validators but warns that `PASS` can be overread. It recommends making even clearer that the numerical audit does not validate the asymptotic analysis, infinite-prime argument, or analytic uniformity.

## 9. Kappa and upstream constants

The review requests that the imported `kappa` constant and its Stage12 provenance be defined at least at interface level, even if its internal Euler-product derivation remains frozen upstream.

## 10. Perfect-cuboid nonexistence

No defect is found in the logical use of triple overlaps. DeepSeek agrees that the proof does not assume nonexistence of perfect cuboids; `T(B)` is controlled as a subset of pair overlaps.

## Repair recommendation

DeepSeek recommends that the next immutable review version include at minimum:

1. explicit Wiener-norm derivation;
2. explicit curved-region and box-error accumulation;
3. explicit retained-harmonic conductor/log bookkeeping;
4. complete Stage12 counting-interface statement and factor-two derivation;
5. precise imported Hecke/Vaaler hypotheses;
6. expanded fixed-prime transfer proof;
7. notation cleanup and clearer local-factor definitions.

The review therefore recommends a new immutable R05/R06 rather than freezing R04.

```text
DEEPSEEK_R04_VERDICT=REPAIRABLE
R04_REPAIR_REQUIRED=true
R04_IMMUTABLE=true
PROMOTE_TO_13_13G=false
```
