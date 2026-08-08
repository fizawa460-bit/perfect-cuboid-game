# Stage14-s2 — Pythagorean-base local Selmer sieve boundary

## Purpose

Stage14-s2 asks whether the exact full-2-torsion descent interface from s1 can thin primitive Pythagorean first-face states strongly enough to explain the sparse active population.

For a primitive oriented face

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

the locked integral family is

\[
E_F:Y^2=Z(Z-S^2)(Z+X^2),
\qquad
\Delta=16S^4X^4H^4.
\]

The main s2 result is structural: the nontrivial local 2-descent information lives on a **moving bad-prime set** depending on `SXH`. This prevents a direct reuse of the Stage13 fixed-auxiliary-prime product sieve.

## 1. Exact odd-prime bad-density law

Write a primitive Pythagorean triple in Euclid coordinates

\[
(S,X,H)=\{m^2-n^2,2mn,m^2+n^2\},
\qquad (m,n)=1,
\]

with opposite parity. For an odd prime `p`, reduction of `[m:n]` lies in `P^1(F_p)` of size `p+1`.

The condition

\[
p\mid SXH
\]

occurs exactly at the projective slopes

```text
0, infinity, +1, -1
```

and, when `p=1 mod 4`, additionally at the two roots of

\[
r^2+1=0.
\]

Therefore the exact projective bad-prime density is

\[
\boxed{\delta_p=\frac4{p+1}\quad(p\equiv3\pmod4)},
\]

and

\[
\boxed{\delta_p=\frac6{p+1}\quad(p\equiv1\pmod4)}.
\]

The deterministic audit verifies the projective counts for every audited prime and compares them with primitive Euclid pairs through `H<=200000`.

## 2. Good primes do not supply an independent fixed-prime rejection

If

\[
p\nmid2SXH,
\]

then `E_F` has good reduction at the odd prime `p`. In the 2-descent, the local Kummer condition is the unramified local condition. Thus a fixed good auxiliary prime does not create a new base-dependent square-class coordinate.

This is fundamentally different from the Stage13 overlap sieve, where one could fix an inert prime and obtain a nontrivial acceptance multiplier for the entire population before sending `B` to infinity.

For Stage14-s, the relevant finite primes are instead

\[
\boxed{\Sigma_F=\{p:p\mid2SXH\}},
\]

which moves with the base.

## 3. Uniform square-class complexity envelope

Let

\[
k=\omega(2SXH).
\]

The square classes supported on `Sigma_F`, including the sign coordinate, form an `F_2`-space of dimension at most `k+1`. The split full-2-torsion Kummer triple has three coordinates with the product-square relation, hence the ambient pre-local-solubility search space has dimension at most

\[
\boxed{2(k+1)}.
\]

Consequently the number of candidate covering classes is at most

\[
\boxed{4^{k+1}}.
\]

By the standard maximal order of `omega(n)`, uniformly for `S,X,H<=R`,

\[
4^{\omega(2SXH)+1}=R^{o(1)}.
\]

Thus s2 proves a useful complexity statement:

\[
\boxed{\text{the local 2-cover search multiplicity is subpolynomial per Pythagorean base}.}
\]

This is **not** a power saving in the number of bases.

## 4. Why a product local-density theorem does not follow

Positive-rank candidacy is not the event that a base independently passes one test at each fixed auxiliary prime. It is determined by a global `F_2` compatibility problem among square classes supported on the moving primes dividing `2SXH`.

Accordingly s2 does not manufacture multipliers `lambda_p<1` and multiply them over a growing set of fixed primes. No independence of Legendre/Hilbert-symbol conditions is assumed.

The strongest unconditional conclusion from the current interface is therefore:

```text
per-base 2-cover candidate multiplicity = R^o(1)
fixed-prime product sieve power saving   = not obtained
positive-rank density                    = unresolved
```

## 5. Average-Selmer literature boundary

Strong average and distribution theorems exist for large families and for quadratic twists, including full rational 2-torsion settings. They are not imported here without a family match.

The Stage14 Pythagorean-base family has nonconstant `j` and is not a quadratic-twist family of one fixed elliptic curve. It also has rational `Z/2 x Z/4` torsion on every genuine physical fiber, whereas some powerful full-2-torsion twist results explicitly assume the absence of a rational cyclic subgroup of order four.

Therefore

```text
AVERAGE_SELMER_THEOREM_FOR_THIS_PYTHAGOREAN_BASE_CHANGE=false
```

remains the correct theorem boundary.

## 6. Finite audit

`local_selmer_sieve_audit.py` enumerates primitive Euclid pairs through

```text
H <= 200000
```

and records:

- exact versus finite bad-prime frequencies for `p<=47` in the audit list;
- the mean and maximum `omega(2SXH)` at nested hypotenuse cutoffs;
- the resulting `2*(omega+1)` ambient square-class dimension cap.

These values are diagnostics only. They do not supply an asymptotic Selmer distribution.

## Decision

```text
STAGE14_S2=COMPLETE_LOCAL_SUPPORT_ARCHITECTURE_AND_FIXED_PRIME_SIEVE_BOUNDARY
PYTHAGOREAN_BAD_PRIME_DENSITIES_LOCKED=true
SELMER_SQUARECLASS_SUBPOLYNOMIAL_PER_BASE_ENVELOPE=true
FIXED_AUXILIARY_PRIME_PRODUCT_SIEVE_PROVES_POWER_SAVING=false
AVERAGE_SELMER_THEOREM_IMPORTED=false
POSITIVE_RANK_DENSITY_PROVED=false
LOCAL_CONDITIONS_POWER_SAVING_PROVED=false
```

The s1 finite result already found 54/96 certified positive-rank inactive controls. Combined with the s2 failure of a fixed-prime product thinning mechanism, the next priority is now the first-small-point gate rather than another heuristic rank-density fit.

```text
NEXT=Stage14-s3 first-small-point / regulator gate
```

## Artifacts

```text
stages/stage14/14-s2/result.md
stages/stage14/14-s2/literature-local-selmer-audit.md
stages/stage14/scripts/14-s2/local_selmer_sieve_audit.py
stages/stage14/data/14-s2/local_selmer_sieve_audit.json
.github/workflows/stage14-s2-local-selmer.yml
```
