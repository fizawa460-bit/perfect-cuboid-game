# Stage27-19-r5ap — raw-slope sieve composition barrier and weighted target

```text
TASK_ID=Stage27-19-r5ap
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5ao
STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
```

r5ao proves, on the raw four-slope box,

\[
N_{2,\mathrm{raw}}(B;\kappa\sim K)
\ll_\varepsilon
B^\varepsilon\left(\frac{B^2}{K}+B^{3/2}\right).
\]

r5am separately proves that after fixing the eight outer residual variables

\[
(a,b,\delta,c_0,c_s,c_n,\nu,\sigma),
\]

the remaining Stage19 completion multiplicity is \(B^{o(1)}\).

This route records exactly why these two facts do not yet compose into a strict sub-square-root theorem.

## 1. Raw large-kappa sieve cannot beat the current global wall by itself

For every possible Stage19 squarefree kernel one has \(\kappa\ll B\). Therefore for every dyadic \(1\le K\ll B\),

\[
\frac{B^2}{K}+B^{3/2}\gg B.
\]

In particular the r5ao raw-box estimate is always much larger than the already known global theorem

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Taking the minimum of these two available estimates therefore returns only the existing half-power wall. The local residue density gain has been applied before the physical-height compression that created the half-power theorem, so its saving is lost in an ambient box that is too large.

## 2. Small-kappa Pell compression also needs an outer-support count

For \(\kappa\le K\), r5am gives

\[
\#\{\text{completions for one fixed outer residual cell}\}
\ll B^{o(1)}.
\]

But no current theorem gives a fixed-power saving for the number of admissible outer cells

\[
(a,b,\delta,c_0,c_s,c_n,\nu,\sigma)
\]

subject simultaneously to the residual squareclass system and the exact physical budget

\[
\delta C\mu\rho\nu\sigma\le B.
\]

Thus the small-\(\kappa\) side is a support-count problem, not a fiber-multiplicity problem.

## 3. Exact next interface

Define \(\mathcal W(B;K)\) to be the Stage19 survivor count in a dyadic block \(K\le\kappa<2K\) after retaining all of the following before counting residue classes:

1. the residual chart
   \[
   m=c_0c_s\mu,\quad n=\delta c_n\nu,
   \quad r=c_0c_n\rho,\quad s=\delta c_s\sigma;
   \]
2. the exact edge budget
   \[
   \delta C\mu\rho\nu\sigma\le B;
   \]
3. the coupled residual equations (S1)-(S3);
4. the r5an congruence receiver modulo \(\kappa\).

The next useful theorem must produce a modulus saving **inside this physically weighted population**, for example a bound of schematic form

\[
\boxed{
\mathcal W(B;K)
\ll B^{1/2+o(1)}K^{-\eta}
+\text{controlled boundary term}
}
\]

for some fixed \(\eta>0\), together with a compatible small-\(K\) outer-cell bound. No such theorem is claimed here.

## 4. Barrier conclusion

The r5am and r5ao gains are both genuine but occur on different counting layers:

- r5am: subpower **fiber multiplicity** after fixing eight outer variables;
- r5ao: fixed-power **raw ambient slope density** for growing \(\kappa\).

A strict sub-square-root upper bound requires a theorem transferring the r5an modulus saving through the exact physical residual measure, or an independent fixed-power count for the small-\(\kappa\) outer support.

```text
RAW_KAPPA_SIEVE_COMPOSITION_TO_SUBHALF_PROVED=false
RAW_KAPPA_SIEVE_TOO_EARLY_IN_COUNTING_PIPELINE_PROVED=true
SMALL_KAPPA_PELL_FIBER_SUBPOWER_RETAINED=true
SMALL_KAPPA_OUTER_SUPPORT_FIXED_POWER_BOUND_PROVED=false
PHYSICAL_WEIGHTED_KAPPA_SIEVE_IDENTIFIED_AS_NEXT_TARGET=true
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5aq
NEXT_TARGET=PHYSICAL_WEIGHTED_KAPPA_SIEVE_OR_SMALL_KAPPA_OUTER_SUPPORT_COUNT
```
