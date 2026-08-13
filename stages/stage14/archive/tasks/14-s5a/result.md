# Stage14-s5a — Euclid-parameter 2-descent sieve target

## Family coordinates

For primitive opposite-parity Euclid parameters

\[
m>n>0,\qquad (m,n)=1,\qquad m\not\equiv n\pmod 2,
\]

set

\[
S=m^2-n^2,\qquad X=2mn,\qquad H=m^2+n^2.
\]

The Stage14 elliptic fiber is

\[
E_{m,n}:\quad W^2=Z(Z-S^2)(Z+X^2).
\]

The full rational 2-torsion points are at `Z=0,S^2,-X^2`.

## Moving bad-prime support

The discriminant support is contained in

\[
2SXH=4mn(m-n)(m+n)(m^2+n^2),
\]

so every full-2-descent/Kummer class relevant to a rational point can be represented by square classes supported on primes dividing the five moving factors

```text
m, n, m-n, m+n, m^2+n^2
```

plus the fixed prime 2.

This is the structural reason Stage14-s2 could not be converted into a product over fixed auxiliary primes: the local support moves with `(m,n)`.

## Physical small-point window

Merged Stage14-s3 gives the implication

```text
mu(F) <= B
=>
there exists a non-torsion P in E_{m,n}(Q)
with canonical height hhat(P) <= C1 log B + C2 log H + C3.
```

The exact constants are not frozen here; s5a only fixes that the family sieve must count descent classes together with this logarithmic physical-height window rather than count all Selmer classes indiscriminately.

## Exact theorem target

Define `Q_B` to be the set of primitive opposite-parity pairs `(m,n)` with `m^2+n^2<=B` for which there exists a full-2-descent class satisfying all of:

1. its three Kummer square classes are supported on `2SXH`;
2. the corresponding 2-cover is locally soluble at every place;
3. it is represented by a rational non-torsion point on `E_{m,n}`;
4. that point lies in the Stage14 physical logarithmic small-point window.

Every active Stage14 first face belongs to `Q_B`. Therefore a theorem

\[
|Q_B|\ll B^{1/2+o(1)}
\]

would imply the desired upper-bound scale for `V(B)`.

A weaker bound `|Q_B| << B^{1-delta}` with any explicit `delta>0` would already be a genuine family-level advance beyond s5.

## Character-sieve shape

The desired proof should not enumerate all divisor-supported square classes independently. It should expose the local-solubility conditions as quadratic characters / Hilbert-symbol constraints coupling the moving factors

```text
m, n, m-n, m+n, m^2+n^2
```

and then average those constraints over primitive Euclid pairs. The natural next object is a reciprocity matrix whose entries are Legendre/Jacobi symbols between squarefree pieces of these five factors.

The intended analytic interface is therefore a bilinear/large-sieve estimate for sums schematically of the form

\[
\sum_{(m,n)\in\mathcal E(B)} w(m,n)
\prod_j \chi_j(F_j(m,n)),
\]

where `E(B)` is the primitive opposite-parity Euclid region, `F_j` are the moving factors above, and the characters arise from the 2-cover local conditions.

## What is and is not proved

This stage formulates the theorem target only. It does **not** prove that every locally soluble supported class is globally soluble, does not identify Selmer rank with Mordell--Weil rank, does not prove the required character cancellation, and does not prove the square-root asymptotic.

```text
STAGE14_S5A=EUCLID_PARAMETER_DESCENT_SIEVE_TARGET_FORMULATED
EUCLID_PARAMETERS_FIXED=true
MOVING_FACTORS=m,n,m-n,m+n,m^2+n^2
FULL_2_DESCENT_SUPPORT_ON_2SXH=true
PHYSICAL_SMALL_POINT_WINDOW_INCLUDED=true
FIXED_PRIME_PRODUCT_SIEVE_SUFFICIENT=false
LOCAL_SOLUBILITY_CHARACTER_MATRIX_DERIVED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5b derive explicit local characters / reciprocity matrix for the moving square classes
```
