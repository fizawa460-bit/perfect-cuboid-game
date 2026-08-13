# Stage15 R01 provenance manifest

Bundle: `STAGE15-FINAL-SELF-CONTAINED-20260813-R01`

Review target: `stages/stage15/final.md`

Status: candidate pending fresh `Stage15-7-audit`.

## Load-bearing dependency lock

| ID | Role | Canonical path | Frozen interface used by R01 |
|---|---|---|---|
| S15-2B | ambient theorem | `stages/stage15/15-2b/result.md` | `M_2(B)~C_M2 B(log B)^5`, `C_M2>0`; exact anticanonical height `R`; directional ambient asymptotics; third-face thin subtraction |
| S15-3 | finite evidence | `stages/stage15/15-3/result.md` | exact matched census through `B=100000`; no empirical asymptotic promotion |
| S15-4 | exact survivor normal form | `stages/stage15/15-4/result.md` | `R in Z <=> AB square <=> sf(A)=sf(B)`; unique squarefree core; multiplicity-one toric reconstruction |
| S14-FINAL | quantitative numerator theorem | `stages/stage14/final.md` | whole-family physical `N_2(B)<<_eps B^(1/2+eps)` under `d<=B`; no lower bound/asymptotic/perfect-cuboid claim |
| S15-5 | quantitative comparison | `stages/stage15/15-5/result.md` | exact cutoff adapter and survival ratio `<<_eps B^(-1/2+eps)(log B)^-5`; directional zero density |
| S15-6-FINAL | causal theorem | `stages/stage15/15-6-final.md` | exact split-prime local density; fixed-finite-set refined count; ordered-limit proof `N_2/M_2->0`; no internal fixed `delta` or `sigma` |
| S15-7-CTRL | synthesis contract | `stages/stage15/15-7-controller.json` | theorem-species firewall, bundle sections, audit and closure rules |

## External literature interfaces

R01 does not independently reopen the literature. It inherits only the already-certified Stage15-2b interfaces:

1. Batyrev--Tschinkel: anticanonical asymptotic on smooth projective toric varieties.
2. Huang: Manin--Peyre equidistribution/counting in adelic neighbourhoods for smooth proper split toric varieties.
3. Browning--Loughran: zero density of thin subsets under the stated almost-Fano/equidistribution hypotheses.

The Stage15 final bundle does not invoke a K3 counting theorem.

## Claim-to-source map

- `M_2(B)~C_M2 B(log B)^5`: S15-2B.
- directional ambient asymptotics: S15-2B.
- exact finite values `M2=796698`, `N2=89` at `B=100000`: S15-3.
- `R in Z <=> sf(A)=sf(B)`: S15-4.
- `N_2(B)<<B^(1/2+o(1))`: S14-FINAL.
- survival ratio fixed-power upper bound: S15-5 using S14-FINAL + S15-2B.
- exact split-prime `rho_p` and rejection `4/p+O(p^-2)`: S15-6-FINAL.
- independent causal `N_2/M_2->0`: S15-6-FINAL.
- `Stage15-6 internal fixed delta=false`, `sigma=false`: S15-6-FINAL.

## Forbidden promotions

R01 must not:

- attribute the Stage14 half-power numerator saving to the Stage15-6 local parity sieve;
- convert the Stage15-6 ordered-limit theorem into a quantitative growing-modulus rate;
- infer the true exponent of `N_2` from the Stage14 upper bound;
- infer a directional survivor-rate hierarchy from `(33,33,23)`;
- infer any asymptotic theorem from the finite census;
- infer perfect-cuboid existence or nonexistence;
- reopen a closed Stage15-6 route because an external strengthening might exist.

## Self-containment level

The final bundle states every load-bearing population, cutoff, principal theorem statement, survivor normal form, local density formula, ordered-limit rule, theorem-species separation, finite-evidence status, and non-claim needed for the final verdict.

The manifest supplies the exact canonical source for auditing proofs and external interfaces without requiring a chronological replay of Stage15-6.

```text
STAGE15_MANIFEST_VERSION=R01
STAGE15_BUNDLE_ID=STAGE15-FINAL-SELF-CONTAINED-20260813-R01
STAGE15_REVIEW_TARGET=stages/stage15/final.md
STAGE15_LOAD_BEARING_DEPENDENCIES_LOCKED=true
STAGE15_EXTERNAL_INTERFACES_LOCKED=true
STAGE15_FORBIDDEN_PROMOTIONS_LISTED=true
STAGE15_MANIFEST_AUDIT_REQUIRED=true
```