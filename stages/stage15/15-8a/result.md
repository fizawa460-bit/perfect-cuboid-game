# Stage15-8a — R02 self-containment repair and audit handoff

Base: merged Stage15-7 R01 final bundle and the existing Stage15-8 Draft PR #888. Stage15-8 changes presentation/preservation only; it does not add a mathematical theorem or reopen Stage15-6/7 research.

## 1. Why R02 exists

Comparison with the active Stage12 R09, Stage13 R07, and Stage14 R06 review bundles showed that the initial Stage15 HTML was too summary-oriented for the project's established definition of “self-contained”.

The defect was presentation-level, not mathematical: several already-certified Stage15-internal load-bearing arguments were represented by short claims plus repository provenance rather than proof-complete transcription.

R02 repairs that defect under the new project-wide standard:

`docs/self-contained-review-standard.md`

```text
SELF_CONTAINMENT_STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
SUMMARY_ONLY_IS_SELF_CONTAINED=false
```

## 2. R02 artifact

Updated:

`stages/stage15/stage15-final-self-contained.html`

Review bundle:

`STAGE15-FINAL-SELF-CONTAINED-20260813-R02`

The HTML remains a single offline-capable artifact with inline CSS and no required external JavaScript, fonts, images, MathJax, CDN assets, or live repository access.

## 3. Newly embedded load-bearing proof chain

R02 physically embeds the already-proved internal steps that R01 had compressed.

### Stage15-2a / 2b ambient theorem

- shared-edge complete intersection `X`;
- exact four `A1` singularities;
- `Y=Bl_4(P1 x P1)` at the four torus-fixed corners;
- anticanonical morphism and `rho(Y)=6`;
- exact Stage15 `R` as an anticanonical adelic height;
- physical chamber transfer;
- exact incidence identity `A(B)=M_2(B)+3M_3(B)`;
- geometrically integral generic degree-two third-face cover;
- thin-set hypothesis map and subtraction;
- `M_2(B)~C_M2 B(log B)^5`, `C_M2>0`.

### Stage15-4 exact survivor normal form

- raw toric coordinates and primitive gcd `G`;
- multiplicity-one inverse reconstruction;
- direct expansion `G^2 R^2=4AB`;
- both directions of `R in Z <=> AB square`;
- `AB square <=> sf(A)=sf(B)`;
- unique `A=kP^2`, `B=kQ^2` squarefree core.

### Stage15-6dy local density

- same charged physical measure;
- inert-prime acceptance `1`;
- split Gaussian divisor geometry on the resolved toric surface;
- exact residue counts `N00,N10,N01,N11`;
- p-adic valuation-parity probabilities inside divisor/intersection tubes;
- derivation of

`rho_p=(p^4+4p^3+22p^2+4p+1)/((p+1)^2(p^2+6p+1))`.

### Stage15-6dz fixed-S adapter

- fixed-prime adelic refinement on the same `R<=B` physical measure;
- exactly-two subtraction remains lower order;
- fixed finite set tensor `rho_S=prod rho_p`;
- explicit non-uniformity in `S`;
- survivor domination and ordered limit `B->infinity` first, then `S` grows.

## 4. External theorem boundary

R02 does not reproduce published proofs. It prints the exact working interfaces and hypothesis maps for:

- Batyrev–Tschinkel toric anticanonical counting;
- Huang fixed adelic-neighbourhood equidistribution/counting;
- Browning–Loughran thin-subset zero density.

The Stage14 whole-family numerator theorem is treated as a completed upstream frozen interface because the Stage15 population/cutoff/multiplicity match is explicit.

## 5. Project-wide future template

Created:

`docs/self-contained-review-standard.md`

It fixes the Stage12 R09 / Stage13 R07 / Stage14 R06 convention for future final review artifacts. The top-level `review/` directory remains reserved for active rendered review targets; the reusable standard/template belongs under `docs/`.

Also updated:

- `docs/README.md` to expose the standard;
- `docs/00_CURRENT_RESEARCH_STATUS.md` to make the standard part of the active review policy;
- `stages/stage15/15-8-controller.json` so Stage15-8 audit must enforce it;
- `stages/stage15/replay/verify_stage15_8_html.py` so CI checks R02 structural markers and the standard file;
- `stages/stage15/15-8-manifest-r02.md` for immutable review-bundle provenance.

## 6. Mathematical preservation contract

R02 preserves, without strengthening:

- `M_2(B)~C_M2 B(log B)^5`, `C_M2>0`;
- `R in Z <=> sf(A)=sf(B)`;
- `N_2/M_2 <<_eps B^(-1/2+eps)(log B)^(-5)` from Stage14 numerator + Stage15 denominator;
- independently `N_2/M_2 -> 0` from the Stage15-6 fixed-prime squareclass sieve;
- `1-rho_p=4/p+O(p^-2)` at good split primes;
- Stage15-6 internal `delta>0=false` and `sigma>0=false`;
- finite `B=100000` evidence `M2=796698`, `N2=89`, directional survivors `(33,33,23)` with no asymptotic promotion;
- no perfect-cuboid existence/nonexistence conclusion.

## 7. Audit handoff

A fresh `Stage15-8-audit` must now audit R02 against `SELF_CONTAINED_REVIEW_STANDARD_V1`, not merely check claim-level fidelity.

```text
STAGE15_8_SUBSTAGE=8a
STAGE15_8A_REVIEW_BUNDLE=STAGE15-FINAL-SELF-CONTAINED-20260813-R02
STAGE15_8A_R01_SELF_CONTAINMENT_DEFECT_REPAIRED=true
STAGE15_8A_SELF_CONTAINMENT_STANDARD_APPLIED=true
STAGE15_8A_HTML_CREATED=true
STAGE15_8A_HTML_PATH=stages/stage15/stage15-final-self-contained.html
STAGE15_8A_OFFLINE_SELF_CONTAINED=true
STAGE15_8A_EXTERNAL_REQUIRED_ASSETS=false
STAGE15_8A_INTERNAL_LOAD_BEARING_PROOFS_EMBEDDED=true
STAGE15_8A_EXTERNAL_THEOREM_CONTRACTS_MAPPED=true
STAGE15_8A_NEW_MATHEMATICS=false
STAGE15_8A_THEOREM_SPECIES_SEPARATED=true
STAGE15_8A_STAGE15_6_REOPENED=false
STAGE15_8A_AUDIT_REQUIRED=true
STAGE15_8A_MERGE_ALLOWED=false
STAGE15_8A_EXIT=FRESH_AUDIT_OF_R02_SELF_CONTAINED_HTML
```

Controller output:

```text
CURRENT_SUBSTAGE=Stage15-8a
NEXT_GATE=FRESH_AUDIT_OF_R02_SELF_CONTAINED_HTML
ALL_PRIOR_CHECKS_PASS=true
AUDIT_REQUIRED=true
CODEX_REQUIRED=false
MERGE_ALLOWED=false
```
