# Stage25-10 comparison lattice

```text
                 + space
       M1 -----------------> N1
       |                      |
 +2nd  |                      | +2nd
 face  v                      v face
       M2 -----------------> N2
                 + space
```

Stage25 owns the diagonal comparison `M1 -> N2`.

## Counts

- `M1`: primitive canonical exactly-one-face, no space requirement, `R<=B`.
- `N1`: primitive canonical exactly-one-face + integral space, `R=d<=B`.
- `M2`: primitive canonical exactly-two-face, no space requirement, `R<=B`.
- `N2`: primitive canonical exactly-two-face + integral space, `R=d<=B`.

## Frozen transition laws

\[
M_1(B)\sim\frac{3}{4\pi^2}B^2\log B,
\]

\[
\frac{N_1}{M_1}\sim\frac{\kappa\pi}{18}\frac{(\log B)^2}{B},
\]

\[
\frac{M_2}{M_1}\sim\frac{4\pi^2C_{M_2}}{3}\frac{(\log B)^4}{B},
\]

\[
B^{-1}(\log B)^{-5/2}\ll\frac{N_2}{N_1}
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3},
\]

\[
B^{-1}(\log B)^{-9/2}\ll\frac{N_2}{M_2}
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

## Exact identities

\[
\frac{N_2}{M_1}
=
\frac{M_2}{M_1}\frac{N_2}{M_2}
=
\frac{N_1}{M_1}\frac{N_2}{N_1}.
\]

These are count identities only.

```text
PATH_A=Stage22_then_Stage24
PATH_B=Stage21_then_Stage23
PATH_PRODUCTS_EXACT=true
PROBABILISTIC_INDEPENDENCE_INFERRED=false
LITERAL_ENDPOINT_SURVIVAL=false
DOUBLE_CHARGE_FIREWALL=ACTIVE
```

## Interaction object carried into Stage25

\[
\mathcal I(B)=\frac{N_2/M_2}{N_1/M_1}=\frac{N_2/N_1}{M_2/M_1}.
\]

Stage24 closes with

\[
(\log B)^{-13/2}\ll \mathcal I(B)
\ll_\varepsilon B^{1/2+\varepsilon}(\log B)^{-7},
\]

so the sign relative to `1` remains unresolved. Stage25 must not replace this with an independence heuristic.
