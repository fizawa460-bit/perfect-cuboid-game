# Stage13-13fp — DeepSeek R06 adversarial review adjudication

> REVIEW_TARGET: `STAGE13-FINAL-SELF-CONTAINED-20260809-R06`
>
> TARGET_SHA256: `ff75730393f8d9895ab85c44313d7bc1b3439697948754e6dc5030c5614bb0c8`
>
> REVIEWER_RAW_CONCLUSION: `R06_NOT_CLOSED_R07_MAJOR_REPAIR_REQUIRED`
>
> REPOSITORY_GATE_VERDICT: `OPEN`

DeepSeek performed a zero-base adversarial review of the immutable R06 bundle. The repository accepts the reviewer's overall conclusion that R06 cannot yet be promoted, but does **not** accept every stated objection as mathematically valid. This file separates genuine proof obligations from false positives so that R07 repairs the proof rather than chasing reviewer misreadings.

## 1. Gate A objection is rejected

DeepSeek claimed that the proof of

\[
I_{ab}+I_{ac}+I_{bc}=\pi^2/8
\]

implicitly divides each individual `I_q` by six or assumes `I_ab=I_ac=I_bc`. R06 does neither.

R06 defines

\[
W=w_{ab}+w_{ac}+w_{bc}.
\]

`W`, unlike the individual summands, is invariant under every coordinate permutation. The positive octant is partitioned into six order chambers, so

\[
\int_{\mathcal O}W\,d\omega
=6\int_{\mathcal R}W\,d\omega
=6(I_{ab}+I_{ac}+I_{bc}).
\]

Separately, symmetry gives

\[
\int_{\mathcal O}w_{ab}
=\int_{\mathcal O}w_{ac}
=\int_{\mathcal O}w_{bc}
=\pi^2/4.
\]

Hence the octant integral of `W` is `3*pi^2/4`, and the stated identity follows. No equality of the three chamber integrals is used; indeed their unequal values are compatible with this argument.

```text
DEEPSEEK_GATE_A_OBJECTION=REJECTED_FALSE_POSITIVE
SUM_IQ_ANALYTIC_PROOF_REMAINS_VALID=true
```

## 2. Fixed finite Hecke/ray-class twists — accepted external-boundary objection

R06 correctly maps the retained Fourier exponent

```text
m=8*ell -> HLR k=2*ell, ell>=1
```

and the untwisted HLR family has nonzero infinity type, entire continuation, and no pole at `s=1`.

However, R06 then states that every fixed finite residue/ray-class twist has the same holomorphy-at-one and fixed-strip polynomial-growth properties without attaching that extension to an equally explicit primary-source theorem or deriving the Hecke-character conductor/infinity-type contract case by case.

The reviewer's suggestion that a finite-order twist might cease to be a Hecke character is not accepted: the product of the angular Hecke character with a finite-order Hecke/ray-class character is again a Hecke character. The valid objection is narrower: the **proof-facing external contract is not sourced/derived at the same explicit level as the untwisted HLR contract**.

R07 must state the actual finite twist family, prove its conductors are independent of `B`, show its infinity type remains nonzero for `ell>=1`, cite/derive the corresponding Hecke `L`-function continuation and functional equation, and then choose common strip-growth exponents over the finite twist family.

```text
R07_BLOCKER_A_FIXED_TWIST_CONTRACT=true
```

## 3. Fixed-S principal sector — accepted theorem-level explicitness gap

The R06 Gate-C supplement improves R05 substantially: it defines an ambient finite abelian group `G_{p,nu}`, an actual constrained subset `Omega_{p,nu}`, the annihilator subgroup

\[
N_{p,\nu}=\{\chi:\chi(\omega)=1\text{ on }\Omega_{p,\nu}\},
\]

and the effective quotient `Xhat/N`. It also states that equivalent characters give the same weighted coefficient system and hence the same reduced five-slot Dirichlet series.

The remaining problem is that `G_{p,nu}`, `Omega_{p,nu}`, and the map from their effective characters to the five pole slots are still **schema-level objects rather than instantiated residue coordinates and congruences**. Consequently an external reviewer cannot independently verify from the bundle alone that:

1. every valuation stratum `U`, `R_b`, `S_c` is represented by the stated finite coordinates;
2. the quotient action really determines the reduced pole signature independently of representative;
3. the principal-residue functional evaluated in those same coordinates factorizes with ratio exactly `lambda_p=(p+5)/(2(p+1))`;
4. no algebraic relation omitted from the abstract ambient encoding changes that conclusion.

The reviewer is therefore correct that the fixed-S argument remains too abstract at this point, although several of the reviewer's subsidiary criticisms are already addressed in the Gate-C supplement.

R07 must instantiate the residue model for each valuation stratum, give the exact character expansion, and prove the reduced signature and principal-residue ratio from those coordinates.

```text
R07_BLOCKER_B_CONCRETE_FIXED_S_RESIDUE_MODEL=true
```

## 4. Nonprincipal-sector "pole restoration" objection is rejected

DeepSeek suggested that summing nonprincipal sectors might somehow restore a lost principal pole. This cannot happen once every summand has pole order strictly below the principal order. A finite sum cannot acquire a Laurent coefficient of an order absent from every summand; cancellation may remove existing poles, but cannot create a higher-order pole.

The genuine Gate-C issue is upstream: R06 must first justify concretely that every class outside the correctly defined kernel really loses at least one pole slot. Once that termwise statement is proved, finite summation is harmless.

```text
DEEPSEEK_NONPRINCIPAL_SUM_RESTORES_POLE=REJECTED_FALSE_POSITIVE
```

## 5. Tagged injection objection is rejected

The included `13-13fm` Gate-C supplement already defines

\[
\mathcal T_q(B)=\{(X,t):t\text{ is one of the two }q\text{-face legs}\}
\]

and proves that for a fixed ordered pair `(q,r)` the unique shared edge is a `q`-leg, supplies the second-face square condition, and therefore passes every selected local test `W_p`. The map is injective, including on triple-face objects.

Thus the requested `S`-compatibility argument is already present in the R06 bundle.

```text
DEEPSEEK_TAGGED_INJECTION_OBJECTION=REJECTED_ALREADY_PROVED
```

## 6. Curved-region accumulation — accepted self-containedness/proof-facing gap

The R06 canonical proof states the box count, all-box finite remainder, power tail, boundary, mesh, and mixed-log-shift bounds, but the immutable R06 bundle does not embed the full `13-13fc` curved-region derivation. In particular, the claims

```text
per-box finite remainder -> all-box O(B Lambda^-35)
boundary and mesh -> O(B Lambda^-5)
```

are compressed enough that a zero-base reviewer cannot reconstruct their uniformity from the bundle alone.

DeepSeek's statement that a crude `O(Lambda^27)` product box count is itself invalid is not accepted; an overcount is safe when the per-box estimates are uniform. The valid concern is that the bundle does not expose enough of the proof that those estimates are uniform on the curved core and boundary boxes.

R07 must either inline the full curved-region lemma into the canonical proof or embed the complete audited lemma in the review bundle and make the dependency explicit.

```text
R07_BLOCKER_C_CURVED_REGION_SELF_CONTAINED_CLOSURE=true
```

## 7. Hardening items accepted for R07

These are not independent theorem-level blockers, but they should be made explicit:

- replace decimal-only displays by exact integer inequalities
  `3465625 < 529*6561` and `10799919009 < 432*25000000`;
- spell out why the phase-uniform Wiener majorant gives logarithmic-moment constants uniform in retained `ell`;
- spell out the epsilon proof of the fixed-`S` squeeze: choose `k` first from epsilon, then choose `B_0(k)`;
- keep the Vaaler interval endpoint convention distinct from the physical cutoff `d<=B`;
- retain the oriented-record explanation of the Stage12 two-element projection fiber.

DeepSeek's concern that `(x,y)` and `(y,x)` must both be canonical triples is a category error: they are two **oriented Stage12 distinguished-face records lying over one canonical Stage13 incidence**, not two canonical triples.

## 8. Repository verdict

The accepted unresolved theorem-level/proof-facing obligations are:

```text
1. fixed finite Hecke/ray-class twist contract
2. concrete fixed-S constrained residue / pole-signature / principal-residue calculation
3. curved-region self-contained uniform-error closure
```

Therefore R06 cannot be promoted.

```text
DEEPSEEK_R06_VERDICT=OPEN
DEEPSEEK_R06_REVIEWER_LABEL=R07_MAJOR_REPAIR_REQUIRED
R06_INDEPENDENT_CLOSED_VERDICTS=0
R06_REQUIRED_INDEPENDENT_CLOSED_VERDICTS=2
R06_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=3
R06_PROMOTION_ALLOWED=false
R07_REQUIRED=true
R06_IMMUTABLE=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
```
