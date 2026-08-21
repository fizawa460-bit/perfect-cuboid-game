# Stage29-02e — exact good-prime Frobenius trace oracle

```text
ROLE=ENDPOINT_FINITE_FIELD_TRACE_ORACLE
STATUS=DERIVED_PENDING_FRESH_AUDIT
```

Let `p` be a good odd prime for the Horie--Yamauchi representations and choose `ell!=p`.  Write

```text
a_p(h8), a_p(h16), a_p(h32)
```

for the `p`-th Fourier coefficients / Frobenius traces of the three weight-3 newforms, and write

```text
chi_-1(p)=chi_{Q(i)}(p),
chi_-2(p)=chi_{Q(sqrt(-2))}(p),
chi_2(p)=chi_{Q(sqrt(2))}(p).
```

## H2 trace on the canonical endpoint surface

Theorem 1.1 gives the semisimple `H2(Sbar)` factorization

```text
h16^3 + h32 + h8^3
+ 10 Tate-trivial characters
+ 2 chi_-1 Tate characters
+ 1 chi_-2 Tate character
+ 3 chi_2 Tate characters.
```

Since geometric Frobenius acts on `Q_l(-1)` by `p`, the exact good-prime trace is

\[
\boxed{
T_{\bar S}(p)
=3a_p(h_{16})+a_p(h_{32})+3a_p(h_8)
+p\bigl(10+2\chi_{-1}(p)+\chi_{-2}(p)+3\chi_2(p)\bigr).
}
\]

## Canonical-model point count

The source proves `H3(Sbar)=0`; the Stoll--Testa/Hodge interface gives `q=0`, hence no `H1` term.  For a good proper two-dimensional model, `H0` contributes `1` and `H4` contributes `p^2`.  Therefore Grothendieck--Lefschetz gives

\[
\boxed{
\#\bar S(\mathbf F_p)
=1+p^2+T_{\bar S}(p).
}
\]

This is an exact finite-field endpoint point-count oracle at good primes, not a rational-cuboid count over `Q`.

## Smooth-resolution trace

The resolution adds 48 exceptional curves: Theorem 1.1 packages them as

```text
24 trivial Tate characters + 24 chi_-1 Tate characters.
```

Hence

\[
\boxed{
T_S(p)=T_{\bar S}(p)+24p+24p\chi_{-1}(p)
}
\]

and

\[
\boxed{
\#S(\mathbf F_p)=\#\bar S(\mathbf F_p)+24p(1+\chi_{-1}(p)).
}
\]

This matches the geometry that 24 nodes are rational and 24 are strictly defined over `Q(i)`: split primes see all 48 exceptional conics/lines over the residue field, inert primes only the rational half contribute to the Frobenius trace in the same way.

## Stage29 use

This gives a much stronger local regression oracle than recomputing endpoint square conditions from scratch prime by prime.  It can be used later to audit exact finite-field counts of the joint V4 model and to isolate the cross quotient trace by subtraction.

```text
S29-L01_CANDIDATE=EXACT_ENDPOINT_FROBENIUS_TRACE_ORACLE
GOOD_PRIME_ENDPOINT_POINT_COUNT_EXACT=true
GLOBAL_Q_RATIONAL_POINT_COUNT_INFERRED=false
LOCAL_DENSITY_PRODUCT_TO_PHYSICAL_COUNT=false
```

Bad primes, choice of integral model and local-factor conventions must be kept explicit whenever the oracle is applied outside the good odd-prime range.
