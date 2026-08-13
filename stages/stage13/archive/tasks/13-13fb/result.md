# Stage13-13fb — R05 Gate B result

> STATUS: `COMPLETE_EXPLICIT_WIENER_BOUND`
>
> INPUT: `13-13fa` complete; R04 immutable.
>
> NEXT: `13-13fc` — curved-region / box-error accumulation.

## Question

R04 reviewers objected that the bound

\[
\|C_{\ell,p}-1\|_{5/8}\le529p^{-5/4}
\]

was presented too much like a black-box quantitative assertion. Gate B asks whether the constant, exponent, phase uniformity and exceptional prime can be exposed line by line.

## Result

Yes. The full derivation is now written in

```text
stages/stage13/13-13fb/wiener-bound-lemma.md
```

For `p>=13`, put `rho=p^{-5/8}`. Since `rho<1/4`, the coefficientwise phase-uniform bounds are

\[
\|a\|_\rho\le\frac83\rho,
\qquad
\|b\|_\rho\le\frac{44}{9}\rho,
\qquad
\|M\|_\rho\le\frac{32}{9}\rho^2,
\]

and

\[
\|A^{-1}\|_\rho\le\frac53,
\qquad
\|B^{-1}\|_\rho\le\frac{25}{12}.
\]

The exact pure-axis cancellation gives

\[
E=(M_{xy}-ab_y)+(M_{xz}-ab_z)-b_yb_z-ab_yb_z.
\]

The four contributions to the `rho^2` majorant are

\[
\frac{64}{9},\quad
\frac{704}{27},\quad
\frac{1936}{81},\quad
\frac{3872}{243},
\]

so

\[
\boxed{
\|E\|_\rho\le\frac{17744}{243}\rho^2.
}
\]

Multiplying the inverse bounds gives the exact constant

\[
\frac{17744}{243}\cdot\frac53\cdot
\left(\frac{25}{12}\right)^2
=\frac{3465625}{6561}
=528.2159731748209\ldots<529.
\]

Since `rho^2=p^{-5/4}`,

\[
\boxed{
\|C_{\ell,p}-1\|_{5/8}
\le529p^{-5/4}
\qquad(p\ge13,\ p\equiv1\pmod4).
}
\]

The proof is uniform for every real local angular phase, hence uniform in every retained harmonic index.

## Exceptional split prime `p=5`

Gate B no longer leaves `p=5` as an unexplained “finite harmless factor”. Since

\[
5^{-5/8}<3/8,
\]

the same coefficient argument gives

\[
\|C_{\ell,5}-1\|_{5/8}
\le\frac{10799919009}{25000000}
=431.99676036<432,
\]

again uniformly in the phase.

Thus the complete split-prime correction is quantitatively controlled at `sigma=5/8`: one explicit finite `p=5` factor and an absolutely summable tail bounded by `529 p^{-5/4}`.

## Consequence

Because

\[
\sum_p p^{-5/4}<\infty,
\]

the mixed Euler product converges absolutely in the weighted Wiener algebra with a norm uniform over the retained harmonic range. Fixed logarithmic moments then follow from the `5/8` weighted summability.

This closes only the Wiener/local-product objection. It does **not** yet close:

- accumulation of rectangle and curved-boundary errors (`13-13fc`);
- the exact conductor/logarithmic bookkeeping for retained nonzero harmonics (`13-13fd`).

## Deterministic audit

The audit

```text
stages/stage13/scripts/13-13fb/wiener_bound_audit.py
```

recomputes with exact rational arithmetic:

```text
E bound                  = 17744/243
exact final constant     = 3465625/6561
exact decimal            = 528.2159731748209...
rounded majorant         = 529
prime exponent           = 5/4
p=5 finite bound         = 10799919009/25000000 < 432
```

The corresponding committed report is

```text
stages/stage13/data/13-13fb/wiener_bound_audit.json
```

The audit is reproducibility/consistency evidence; the proof is the written coefficientwise argument in `wiener-bound-lemma.md`.

## Theorem status

No theorem constant or counting convention changes in Gate B. No defect requiring reopening of the theorem contract was found.

```text
STAGE13_13FB=COMPLETE_EXPLICIT_WIENER_BOUND
WIENER_SIGMA=5/8
SPLIT_PRIME_TAIL_START=13
WIENER_E_BOUND=17744/243
WIENER_EXACT_CONSTANT=3465625/6561
WIENER_ROUNDED_CONSTANT=529
WIENER_EXPONENT=5/4
P5_EXPLICIT_FINITE_BOUND_LT=432
PHASE_UNIFORM=true
RETAINED_HARMONIC_UNIFORM=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
NEXT=13-13fc
```