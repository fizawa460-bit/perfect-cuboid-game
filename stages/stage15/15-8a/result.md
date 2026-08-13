# Stage15-8a — self-contained Stage15 final HTML and audit handoff

Base: merged Stage15-7 R01 final bundle and its fresh audit PASS. Stage15-8 changes presentation only; it does not add a mathematical theorem or reopen Stage15-6/7 research.

## 1. Artifact

Created:

`stages/stage15/stage15-final-self-contained.html`

The file is a single offline-capable HTML review artifact with inline CSS and no required external JavaScript, fonts, images, MathJax, or CDN assets.

It contains the final Stage15 implication chain in human-review order:

1. primitive/canonical exactly-two population and exact `R<=B` cutoff;
2. ambient theorem `M_2(B)~C_M2 B(log B)^5`;
3. exact Gaussian norm squareclass survivor condition `sf(A)=sf(B)`;
4. Stage15-5 quantitative survival theorem with its Stage14 numerator provenance;
5. Stage15-6 independent fixed-prime causal zero-density theorem and exact split-prime density;
6. explicit theorem-species separation and no-double-charge firewall;
7. Stage15-3 finite matched evidence as diagnostic only;
8. provenance and inherited external theorem interfaces;
9. negative knowledge and external future gates;
10. explicit firewall separating the exactly-two Stage15 population from the perfect-cuboid problem;
11. audit checklist and machine-readable lock.

## 2. Mathematical preservation contract

The HTML preserves, without strengthening:

- `M_2(B)~C_M2 B(log B)^5`, `C_M2>0` from Stage15-2b;
- `R in Z <=> sf(A)=sf(B)` from Stage15-4;
- `N_2/M_2 <<_eps B^(-1/2+eps)(log B)^(-5)` from Stage15-5 using Stage14 Theorem 2.1;
- independently `N_2/M_2 -> 0` from Stage15-6 fixed-prime squareclass sieving;
- `1-rho_p=4/p+O(p^-2)` at good split primes;
- Stage15-6 internal `delta>0=false` and `sigma>0=false`;
- finite `B=100000` evidence `M2=796698`, `N2=89`, directional survivors `(33,33,23)` with no asymptotic promotion;
- no perfect-cuboid existence/nonexistence conclusion.

The Stage15-5 half-power rate is not attributed to Stage15-6. The Stage15-6 local parity factors are not multiplied into the Stage15-5 bound.

## 3. Offline/self-contained contract

The dedicated verifier rejects required remote assets. The HTML contains:

- no `<script src=...>`;
- no stylesheet `<link>`;
- no remote `src=` resources;
- no `@import`;
- no MathJax/CDN dependency;
- all layout and typography in inline `<style>`;
- only internal fragment navigation links.

Repository paths are printed only as provenance labels. The final mathematical verdict remains readable without opening them.

## 4. Audit handoff

This is an audit candidate, not yet the frozen human-facing Stage15 artifact. A fresh `Stage15-8-audit` must compare the HTML claim-by-claim against the canonical Stage15 final bundle and immediate sources, verify theorem-species separation, population/cutoff, local-density transcription, ordered limits, finite-evidence discipline, perfect-cuboid firewall, and offline self-containment.

```text
STAGE15_8_SUBSTAGE=8a
STAGE15_8A_HTML_CREATED=true
STAGE15_8A_HTML_PATH=stages/stage15/stage15-final-self-contained.html
STAGE15_8A_OFFLINE_SELF_CONTAINED=true
STAGE15_8A_EXTERNAL_REQUIRED_ASSETS=false
STAGE15_8A_NEW_MATHEMATICS=false
STAGE15_8A_THEOREM_SPECIES_SEPARATED=true
STAGE15_8A_STAGE15_6_REOPENED=false
STAGE15_8A_AUDIT_REQUIRED=true
STAGE15_8A_MERGE_ALLOWED=false
STAGE15_8A_EXIT=FRESH_AUDIT_OF_SELF_CONTAINED_HTML
```

Controller output:

```text
CURRENT_SUBSTAGE=Stage15-8a
NEXT_GATE=FRESH_AUDIT_OF_SELF_CONTAINED_HTML
ALL_PRIOR_CHECKS_PASS=true
AUDIT_REQUIRED=true
CODEX_REQUIRED=false
MERGE_ALLOWED=false
```
