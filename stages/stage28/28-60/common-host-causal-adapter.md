# Stage28-60 — common-host causal adapter

Stage28 compares disjoint exact-face strata, so causal language must be routed through matched hosts rather than a false literal `Stage19 subset Stage20` transition.

Let

\[
S_{sp}(B)=\frac{N_2(B)}{M_2(B)}
\]

be the literal Stage18 -> Stage19 space-survival rate on the exactly-two-face host. Let

\[
F_3(B)=\frac{M_3(B)}{M_2(B)}
\]

be the matched adjacent-stratum population ratio for third-face completion. `F_3` is not an objectwise survival probability.

Then, whenever `N2(B)>0`,

\[
\boxed{\frac{M_3(B)}{N_2(B)}=\frac{F_3(B)}{S_{sp}(B)}}.
\]

Equivalently on the common physical host `H_ge2=M2+M3`, with

\[
\Phi_{20}=\frac{M_3}{M_2+M_3},\qquad
\Sigma_{19}=\frac{N_2}{M_2+M_3},
\]

one has

\[
\frac{M_3}{N_2}=\frac{\Phi_{20}}{\Sigma_{19}},
\qquad
F_3=\frac{\Phi_{20}}{1-\Phi_{20}},
\qquad
\Sigma_{19}=S_{sp}(1-\Phi_{20}).
\]

These identities compare two condition costs without pretending the endpoint populations are nested.

Current certified scale information is

\[
B^{-3/4}(\log B)^{-5}\ll S_{sp}(B)
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5},
\]

and, using the Stage28-50-r2 liminf plus `M2~C_M2 B(log B)^5`,

\[
\liminf_{B\to\infty}
B^{2/3}(\log B)^5F_3(B)
\ge \frac{27}{40\pi^2 C_{M_2}}>0.
\]

Stage26 also gives `F_3(B)->0`. Thus both the space-survivor population and the three-face population are lower order than the two-face scale, while both remain polynomially infinite.

The known lower floors place

```text
SPACE_SURVIVAL_CONSTRUCTION_FLOOR_EXPONENT=-3/4
THIRD_FACE_ADJACENT_CONSTRUCTION_FLOOR_EXPONENT=-2/3
LOWER_FLOOR_GAP=1/12
```

but this is only a comparison of certified lower floors. It does not prove `F3>S_sp`, `M3>N2`, or a limiting bridge ratio.

```text
COMMON_M2_CAUSAL_ADAPTER=PROVED
M3_OVER_N2_AS_RELATIVE_CONDITION_COST=PROVED_ALGEBRAIC_IDENTITY
M3_OVER_M2_IS_LITERAL_SURVIVAL=false
N2_OVER_M2_IS_LITERAL_SURVIVAL=true
LOWER_FLOOR_GAP_ORDERS_FULL_POPULATIONS=false
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
```