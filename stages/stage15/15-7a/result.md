# Stage15-7a — theorem-species separation and final claims matrix

Base: Stage15-7 controller on main after closed Stage15-6. This substage reconciles the two Stage15 thinning theorems without changing either theorem.

## 1. One physical comparison problem

Let
\[
\mathcal B_2(B)=\{\text{primitive canonical exactly-two boxes}:R\le B\},
\qquad
\mathcal A_2(B)=\{C\in\mathcal B_2(B):R\in\mathbf Z\},
\]
with
\[
M_2(B)=\#\mathcal B_2(B),\qquad N_2(B)=\#\mathcal A_2(B).
\]
Both Stage15-5 and Stage15-6 use this same object measure and the same exact geometric cutoff `R<=B`.

## 2. Quantitative comparison theorem

Stage15-2b proves
\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]
Stage14 Theorem 2.1 proves on the integral-space-diagonal exactly-two numerator
\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]
Stage15-5 combines only those two inputs to obtain
\[
\boxed{\frac{N_2(B)}{M_2(B)}\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5}.}
\]
Hence for every fixed `delta<1/2`, the survival ratio is `O_delta(B^{-delta})`.

This theorem is quantitatively stronger than qualitative zero density, but its fixed-power numerator loss is inherited from Stage14. Stage15-5 does not claim to derive the exponent from the Stage15 Gaussian squareclass mechanism.

## 3. Independent causal theorem

Stage15-4 proves the exact survivor normal form
\[
R\in\mathbf Z
\iff
\operatorname{sf}(A)=\operatorname{sf}(B),
\]
where
\[
A=m^2r^2+n^2s^2,\qquad B=m^2s^2+n^2r^2.
\]
Stage15-6 then works on the same physical measure and proves independently, by the fixed-prime local squareclass sieve,
\[
\boxed{\frac{N_2(B)}{M_2(B)}\longrightarrow0.}
\]
Its proof does not use the Stage15-5 half-power ratio estimate as the source of zero density.

The local split-prime acceptance profile is
\[
1-\rho_p=\frac{4p(p-1)^2}{(p+1)^2(p^2+6p+1)}=\frac4p+O(p^{-2}),
\]
so the internal primewise mechanism is naturally logarithmic. Stage15-6 proves neither an internal fixed `delta>0` nor `sigma>0`.

## 4. Logical relation

The two conclusions are compatible but are different theorem species.

| Item | Certified conclusion | Source of saving | Role in final verdict |
|---|---|---|---|
| Stage15-5 | fixed-power upper thinning for every `delta<1/2` | Stage14 numerator theorem + Stage15 ambient denominator | strongest quantitative comparison |
| Stage15-6 | `N_2/M_2 -> 0` | local squareclass parity sieve on Stage15 toric measure | independent causal explanation |
| Stage15-6 internal rate | no fixed `delta`, no `sigma` | exact local density profile | quantitative boundary of causal mechanism |

The quantitative theorem implies zero density as a logical consequence, but that does not make Stage15-6 redundant: Stage15-6 supplies an independent mechanism-level proof and identifies what the Stage15 squareclass condition itself explains.

## 5. Non-circularity and firewalls

- Stage15-5 depends on Stage14 Theorem 2.1 and Stage15-2b; it does not depend on Stage15-6.
- Stage15-6 causal zero density depends on Stage15-2b, Stage15-4, and its fixed-prime local analysis; it does not use Stage15-5 as its proof.
- The Stage14 `B^{1/2+o(1)}` numerator bound is not re-labeled as a Stage15-6 internal exponent.
- The Stage15-6 local product is not promoted to a polynomial rate.
- The two savings are never multiplied together or charged twice.

## 6. Final claims matrix

The final Stage15 bundle may claim:

1. `M_2(B)~C_M2 B(log B)^5`, `C_M2>0`.
2. `R in Z` is exactly the paired Gaussian-norm squareclass coincidence.
3. `N_2/M_2 <<_eps B^{-1/2+eps}(log B)^-5` by Stage15-5 using Stage14 numerator input.
4. independently, `N_2/M_2 -> 0` by the Stage15-6 fixed-prime local squareclass sieve.
5. Stage15-6 did not internally prove a fixed-power thinning exponent.
6. finite census evidence is diagnostic only.
7. none of these statements proves perfect-cuboid existence or nonexistence.

```text
STAGE15_7_SUBSTAGE=7a
STAGE15_7A_THEOREM_SPECIES_SEPARATED=true
STAGE15_7A_QUANTITATIVE_SOURCE=STAGE14_NUMERATOR_PLUS_STAGE15_2B_DENOMINATOR
STAGE15_7A_CAUSAL_SOURCE=STAGE15_4_SQUARECLASS_PLUS_STAGE15_6_LOCAL_SIEVE
STAGE15_7A_STAGE15_6_INTERNAL_FIXED_DELTA=false
STAGE15_7A_DOUBLE_CHARGE=false
STAGE15_7A_CIRCULARITY=false
STAGE15_7A_FINAL_CLAIMS_MATRIX_FROZEN=true
STAGE15_7A_EXIT=POPULATION_CUTOFF_AND_PROVENANCE_LOCK
```