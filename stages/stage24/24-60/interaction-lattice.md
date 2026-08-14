# Stage24-60 — interaction lattice

CHECKPOINT=60
ROLE=INTRINSIC_CONTROL_AND_ALTERNATE_PATH_COMPARISON
STATUS=SUBMITTED_FOR_FRESH_AUDIT

## 1. Four-population square

Use the common physical cutoff `R<=B` and primitive canonical convention. Write

- `M1(B)` for exactly one integral face, no space requirement;
- `N1(B)` for exactly one integral face plus integral space diagonal;
- `M2(B)` for exactly two integral faces, no space requirement;
- `N2(B)` for exactly two integral faces plus integral space diagonal.

The comparison square is

\[
\begin{matrix}
M_1(B)&\xrightarrow{\text{second-face comparison}}&M_2(B)\\
\downarrow\scriptstyle{\text{space subset}}&&\downarrow\scriptstyle{\text{space subset}}\\
N_1(B)&\xrightarrow{\text{second-face comparison}}&N_2(B).
\end{matrix}
\]

The vertical arrows are literal subset transitions. The horizontal arrows compare adjacent disjoint face strata and are **not** conditional-probability subset maps.

## 2. Frozen interfaces

The audited source laws used here are

\[
U(B)\sim \frac{\pi}{36\zeta(3)}B^3,
\qquad
N_S^{all}(B)\sim \frac{1}{32G}B^2,
\]

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B,
\qquad
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\]

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}>0,
\]

and Stage24 checkpoint50 now proves

\[
N_2(B)\gg \sqrt{\log B},
\]
while the inherited target upper remains

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

No stronger lower exponent is imported.

## 3. Intrinsic ambient space baseline

Stage16S gives

\[
\frac{N_S^{all}(B)}{U(B)}
\sim
\frac{9\zeta(3)}{8\pi G}\,B^{-1}.
\]

Thus integral space diagonal intrinsically costs exactly one polynomial power in the ambient primitive/canonical population.

For the exactly-one-face host, Stage21 proves

\[
\frac{N_1(B)}{M_1(B)}
\sim
\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
\]

Therefore

\[
\frac{N_1/M_1}{N_S^{all}/U}
\sim
\frac{4\kappa\pi^2G}{81\zeta(3)}(\log B)^2\to\infty.
\]

So one-face conditioning has a rigorously **positive logarithmic interaction** with space survival, while preserving the same polynomial `B^-1` cost.

Equivalently, the first-face density inside the space host is

\[
\frac{N_1(B)}{N_S^{all}(B)}
\sim
\frac{4\kappa G}{3\pi}\frac{(\log B)^3}{B},
\]
whereas without space

\[
\frac{M_1(B)}{U(B)}
\sim
\frac{27\zeta(3)}{\pi^3}\frac{\log B}{B}.
\]
Their quotient is the same Stage21 `(log B)^2` enhancement.

## 4. Stage22 versus Stage23

Without space, Stage22 has the sharp adjacent-stratum ratio

\[
\frac{M_2(B)}{M_1(B)}
\sim
\frac{4\pi^2C_{M_2}}{3}\frac{(\log B)^4}{B}.
\]

Inside the already space-integral host, Stage23 compares `N2` with `N1`. Checkpoint50 strengthens its quantitative lower side:

\[
\frac{N_2(B)}{N_1(B)}
\gg
\frac{1}{B(\log B)^{5/2}}.
\]

The inherited upper gives

\[
\frac{N_2(B)}{N_1(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-3}.
\]

Hence

\[
\boxed{
B^{-1}(\log B)^{-5/2}
\ll
N_2/N_1
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-3}.
}
\]

This interval does not determine the true polynomial or logarithmic order of the Stage23 comparison. In particular, Stage22's sharp `B^-1(log B)^4` law cannot be transferred unchanged into the space host.

## 5. Stage24 space-survival bracket

Combining the new lower theorem with the frozen Stage18 asymptotic gives

\[
\boxed{
B^{-1}(\log B)^{-9/2}
\ll
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}.
}
\]

Together with checkpoint30, `N2/M2 -> 0`. Therefore the Stage24 space predicate is now classified as

```text
ZERO_DENSITY=true
INFINITELY_MANY_SURVIVORS=true
CLASS=THIN_BUT_INFINITE
```

The bracket remains far too wide to identify the true survivor exponent.

## 6. Ambient-relative interaction sign at two faces is unresolved

Define the ambient-relative two-face space interaction quotient

\[
\mathcal J_2(B)
=
\frac{N_2(B)/M_2(B)}{N_S^{all}(B)/U(B)}.
\]

The rigorous bounds above imply

\[
(\log B)^{-9/2}
\ll
\mathcal J_2(B)
\ll_\varepsilon
B^{1/2+\varepsilon}(\log B)^{-5}.
\]

These bounds straddle `1`. Therefore Stage24 cannot currently classify the global two-face space interaction as positive, neutral, or negative relative to the ambient `B^-1` baseline.

This sharply contrasts with Stage21, where the analogous quotient tends to infinity like `(log B)^2`.

```text
ONE_FACE_SPACE_INTERACTION_SIGN=POSITIVE
ONE_FACE_SPACE_INTERACTION_SCALE=(log B)^2
TWO_FACE_SPACE_INTERACTION_SIGN=UNRESOLVED
TWO_FACE_RATIO_INDEPENDENCE_PROVED=false
TWO_FACE_RATIO_INDEPENDENCE_DISPROVED=false
```

## 7. Exact second-order cross-ratio

A useful algebraic interaction observable is

\[
\mathcal I(B)
=
\frac{N_2/M_2}{N_1/M_1}
=
\frac{N_2/N_1}{M_2/M_1}.
\]

The equality is a count identity, not a claim that the horizontal arrows are conditional probabilities.

Using the audited laws and checkpoint50 lower theorem,

\[
\boxed{
(\log B)^{-13/2}
\ll
\mathcal I(B)
\ll_\varepsilon
B^{1/2+\varepsilon}(\log B)^{-7}.
}
\]

Again the certified interval contains `1`. Thus the second-order face/space interaction sign is unresolved at current theorem strength.

## 8. Arithmetic stratum heterogeneity

Checkpoint50 materially changes the qualitative picture of the old Stage15-2 family.

For the historical coprime odd/odd slice,

\[
17(p^4+q^4)\equiv2\pmod{16},
\]
so space survival is identically zero.

After removing the odd/odd specialization, the mixed-parity slice

\[
p^4+q^4=17Z^2
\]
has positive-rank genus-one structure and yields infinitely many primitive exactly-two Stage19 objects after finitely many third-face exceptions are removed.

Therefore the Stage24 space predicate is provably **non-uniform across natural arithmetic strata** of the same algebraic two-face construction. This is a structural dependence statement only; it does not determine the global interaction quotient `J2` or `I`.

```text
EXPLICIT_FORMULA_STRATUM_HETEROGENEITY=PROVED
ODD_ODD_SPACE_SURVIVAL=ZERO
MIXED_PARITY_C17_SPACE_SURVIVAL=INFINITE
GLOBAL_DENSITY_SIGN_INFERENCE_FROM_STRATA=FORBIDDEN
```

## 9. Interaction verdict

The strongest rigorous checkpoint60 classification is:

1. ambient space integrality costs `B^-1`;
2. after exactly one face, space survival is enhanced by `(log B)^2` relative to ambient;
3. after exactly two faces, space survival is zero-density but infinite;
4. the true Stage24 survivor rate is not known sharply enough to compare its global sign with the ambient `B^-1` benchmark;
5. the space predicate is arithmetically stratum-dependent inside an explicit two-face formula;
6. no probabilistic independence or product law is proved.

No perfect-cuboid conclusion is made.
