# Stage14-e7 — secondary-asymptotic boundary and finite crossover

> STATUS: `STAGE14_E7_COMPLETE_FINITE_CROSSOVER_AND_SECONDARY_BOUNDARY`
>
> INPUT: Stage14-e6 explicit leading constant, Stage14-e2 exact ambient census, Batyrev--Tschinkel height-zeta pole theorem, Chambert-Loir--Tschinkel effective Tauberian template.
>
> RESULT: the apparent `B(log B)^3` law through `10^6` is quantitatively explained as a deep pre-asymptotic regime; a full physical-metric secondary polynomial is **not** promoted without the missing effective analytic continuation.

## 1. Frozen leading theorem

Stage14-e6 proves

\[
E_2(B)\sim C_E B(\log B)^5,
\]

with

\[
1.47953102009666\times10^{-6}<C_E<1.47956061101297\times10^{-6}.
\]

Write

\[
L=\log B,
\qquad
R_3(B)=\frac{E_2(B)}{BL^3}.
\]

If a degree-five secondary polynomial is eventually valid, then formally

\[
R_3(B)=c_5L^2+c_4L+c_3+c_2L^{-1}+\cdots,
\]

with `c5=C_E`.

## 2. What the general height-zeta theorem actually gives

For the toric anticanonical height, Batyrev--Tschinkel gives a pole of order

\[
\rho(Y)=6
\]

at `s=1`.  Locally write

\[
Z(s)=\sum_{j=1}^{6}\frac{A_{-j}}{(s-1)^j}+O(1).
\]

The leading coefficient is

\[
\boxed{c_5=\frac{A_{-6}}{5!}=C_E.}
\]

If one also has a sufficiently strong continuation into a strip left of `1`, polynomial vertical growth, and no competing poles, then the residue of

\[
Z(s)\frac{B^s}{s}
\]

gives

\[
B(c_5L^5+c_4L^4+c_3L^3+\cdots),
\]

with

\[
\boxed{c_4=\frac{A_{-5}-A_{-6}}{4!}},
\qquad
\boxed{c_3=\frac{A_{-4}-A_{-5}+A_{-6}}{3!}}.
\]

Chambert-Loir--Tschinkel provides precisely the kind of effective Tauberian theorem needed for this implication when the analytic hypotheses are available.

For the **physical Stage14-e Euclidean metric**, however, e6 did not verify the left-half-plane continuation and vertical Fourier bounds needed to invoke the full polynomial conclusion.  Therefore e7 records

```text
PHYSICAL_METRIC_LEFT_HALF_PLANE_CONTINUATION_VERIFIED=false
PHYSICAL_METRIC_VERTICAL_GROWTH_VERIFIED=false
FULL_SECONDARY_ASYMPTOTIC_PROVED=false
```

rather than silently identifying a finite fit with Laurent coefficients.

## 3. Dense exact finite census

The e7 audit recomputes the exactly-two ambient population at 17 cutoffs

```text
2k, 3k, 5k, 7.5k, 10k, 15k, 20k, 30k,
50k, 75k, 100k, 150k, 200k, 300k, 500k, 750k, 1m.
```

It reproduces every e2 locked cutoff and adds the intermediate values independently.

At `B=10^6`,

\[
E_2(B)=13{,}817{,}725,
\]

and

\[
R_3(10^6)=0.005240053581957176.
\]

The proved `c5 L^2` contribution to this normalized quantity is only

\[
0.0002823984418988266\ldots.
\]

Equivalently, the **proved asymptotic leading term itself** accounts for only

\[
\boxed{5.38917\%<\frac{C_EB(\log B)^5}{E_2(B)}<5.38929\%}
\]

at `B=10^6`.

Thus more than

\[
\boxed{94.61\%}
\]

of the exact count at that cutoff lies outside the eventual leading term.

This quantitatively explains why the finite data can look like a lower logarithmic power without contradicting the `log^5` theorem.

## 4. Anchored three-term finite model

For diagnosis only, fix `c5` to the midpoint of the rigorous e6 interval and fit

\[
R_3(B)\approx c_5L^2+c_4L+c_3
\]

on nested high-`B` windows.

The fitted values are:

```text
min B       effective c4       effective c3      RMS relative error
2,000      -7.02139e-5         0.00586472          0.006956
20,000     -4.37496e-5         0.00554114          0.002653
100,000    -2.80197e-5         0.00533891          0.000957
200,000    -2.21229e-5         0.00526073          0.000485
```

The important fact is not the individual fitted numbers.  It is their **window drift**:

\[
\Delta c_4\approx4.81\times10^{-5},
\qquad
\Delta c_3\approx6.04\times10^{-4}.
\]

Therefore these are not frozen as the true `c4,c3`.

```text
FINITE_EFFECTIVE_COEFFICIENTS_ONLY=true
FINITE_EFFECTIVE_COEFFICIENTS_ARE_LAURENT_COEFFICIENTS=false
```

Still, all nested windows agree on the qualitative mechanism: a contribution numerically of `log^3` scale dominates the available range, while the proved positive `log^5` term is only beginning to emerge.

## 5. Crossover scale is not yet a theorem

If one extrapolates the anchored three-term fits, the point at which the positive `c5L^2+c4L` part becomes comparable to the fitted `c3` occurs only around

```text
log10 B ≈ 29 ... 40
```

depending on the fit window.

This enormous spread is itself the reason not to promote a numerical crossover threshold.  The statement is only:

\[
\boxed{B=10^6\text{ is still extremely pre-asymptotic for the proved }B(\log B)^5\text{ main term}.}
\]

No eventual threshold or monotonicity theorem is claimed.

## 6. What would be required for a true e7 secondary theorem

A genuine proof of

\[
E_2(B)=B\bigl(c_5L^5+c_4L^4+c_3L^3+\cdots\bigr)+O(B^{1-\delta})
\]

for the physical metric requires, at minimum:

1. meromorphic continuation of the exact physical height zeta function into `Re(s)>1-delta`;
2. vertical polynomial bounds in that strip;
3. control of all poles in the shifted region;
4. evaluation of `A_-5,A_-4,...` for the physical real and `p=2` metrics;
5. a transfer showing that removing the third-face-square thin set does not re-enter at a secondary logarithmic order being claimed.

These are materially stronger obligations than e6's leading constant.

## 7. Locked conclusion

```text
STAGE14_E7=COMPLETE_FINITE_CROSSOVER_AND_SECONDARY_BOUNDARY
DENSE_EXACT_CENSUS_MAX_B=1000000
DENSE_EXACT_CENSUS_CUTOFFS=17
PROVED_LOG5_MAIN_SHARE_AT_B1E6_APPROX=0.053892
FINITE_CROSSOVER_DIAGNOSIS_COMPLETE=true
FORMAL_LAURENT_TO_POLYNOMIAL_DICTIONARY_RECORDED=true
FULL_SECONDARY_ASYMPTOTIC_PROVED=false
PHYSICAL_METRIC_LEFT_HALF_PLANE_CONTINUATION_VERIFIED=false
PHYSICAL_METRIC_VERTICAL_GROWTH_VERIFIED=false
FINITE_EFFECTIVE_COEFFICIENTS_ARE_LAURENT_COEFFICIENTS=false
E6_LEADING_CONSTANT_UNCHANGED=true
NEXT_E_SUPPLEMENT=Stage14-e8 quantitative Euler-brick thin-set count
```
