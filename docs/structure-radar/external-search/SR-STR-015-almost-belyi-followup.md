# SR-STR-015 direct missing-lemma follow-up — two-fiber parity almost-Belyi reduction

Date: 2026-08-19
Baseline: merged PR #1188, `SR-STR-015-deep-closure.md`.
Mode: direct proof attack; no broad literature census.
Status: `FIRST_SUBLEMMA_IDENTIFIED`.
Arsenal decision: unchanged (`EXTERNAL_GATE`).

## Correction to the function-field target

The exact deep-closure reduction has

```text
F,R in Qbar(E_s)=Qbar(x,Y),
Y^2=(Ax+B)^4+(Cx+D)^4,
```

not necessarily `F,R in Qbar(x)`. Requiring `F,R in Qbar(x)` literally would produce a nonconstant map `P1 -> E0`, impossible by Riemann-Hurwitz, and would incorrectly erase the already-closed degree-2 locus.

## Fixed-CM normalization of the R504 quotient

Set

```text
t=(Ax+B)/(Cx+D),
w=Y/(Cx+D)^2.
```

Then the quotient elliptic curve is geometrically fixed:

```text
E_*: w^2=t^4+1.
```

On a dense chart with `CD != 0`, write

```text
a=B/D,
b=A/C.
```

After absorbing a constant square into `u`, the R504 double cover is

```text
C_{a,b}: u^2=(t-a)/(t-b).
```

The known reciprocal/commuting-involution divisor becomes

```text
ab=1,
ab=-1,
b=-a,
```

equivalently `(AB-CD)(AB+CD)(AD+BC)=0`.

The anti-invariant map equation becomes

```text
((t-a)/(t-b))*R^2 = F(F-2)(F+2),
F,R in Qbar(E_*).
```

## Exact valuation-parity classification for all degrees

Let `T={0,2,-2,infinity}`. The odd valuation support of `(t-a)/(t-b)` is the four-point divisor

```text
D_{a,b}=t^{-1}(a)+t^{-1}(b).
```

For each `c in T`, there are effective divisors `E_c` and disjoint reduced divisors `D_c subset D_{a,b}` such that

```text
F^*(c)=2E_c+D_c,
D_0 sqcup D_2 sqcup D_-2 sqcup D_infinity = D_{a,b}.
```

If `n=deg F`, then `r_c=deg D_c` satisfies

```text
r_c == n (mod 2),
sum_c r_c = 4.
```

Hence, up to permutation:

```text
n odd:  (r_0,r_2,r_-2,r_infinity)=(1,1,1,1).

n even: (2,2,0,0) or (4,0,0,0).
```

The residual global square obstruction lies in the finite group `Pic^0(E_*)[2] ~= E_*[2]`; it is a finite chart obstruction, not a source of unbounded degree.

## Decomposable maps and primitivity

A nonconstant anti-invariant map cannot factor through the sigma quotient `C_{a,b}->E_*`, because quotient-factorization would make it sigma-invariant.

Target CM-isogeny composition has exact degree multiplication

```text
deg([alpha] o g)=Norm(alpha)*deg(g),
alpha in Z[i].
```

Likewise an intermediate elliptic quotient multiplies degrees. Primitivity should therefore be interpreted through the induced optimal Prym quotient, but primitivity alone does not imply an absolute degree bound.

The CM factor yields a rational idempotent in `End^0(P)` and associated CM endomorphisms, but not in general an integral polarization-preserving involution of the curve. Thus

```text
E0 factor  !=>  extra curve involution
```

without an additional descent/integrality argument. Degree 2 is special because its deck involution exists geometrically.

## Sharp Riemann-Hurwitz reduction

For `F:E_*->P1` of degree `n`, total ramification is `2n`.

Let `s_c` be the number of distinct points over `c in T`. The parity classification gives

```text
s_c <= (n+r_c)/2.
```

Therefore

```text
sum_{c in T} s_c <= 2n+2.
```

Writing `R_out` for total ramification outside `T`, one obtains the uniform bound

```text
0 <= R_out <= 2.
```

Thus every primitive degree `n>=3` candidate is an almost-Belyi map on the fixed CM elliptic curve with at most:

- two extra simple ramification points; or
- one extra ramification point of index 3.

The lifted map `C_{a,b}->E0` still has total ramification 4, and Riemann-Hurwitz alone yields no upper bound on `n`.

## Exact algebraic core at fixed degree

Let `L=F^*O_{P1}(1)`, `deg L=n`, and write `F=P/Q` with `P,Q in H^0(E_*,L)`. Then

```text
div(P)=2E_0+D_0,
div(P-2Q)=2E_2+D_2,
div(P+2Q)=2E_-2+D_-2,
div(Q)=2E_infinity+D_infinity.
```

After fixing one of finitely many `E_*[2]` twists, this becomes a simultaneous four-square-section problem of the schematic form

```text
P = xi_0 r_0^2,
P-2Q = xi_2 r_2^2,
P+2Q = xi_-2 r_-2^2,
Q = xi_infinity r_infinity^2.
```

For fixed `n` this can in principle be converted into finite coefficient elimination. The current obstruction is that `n` is not known to be bounded, so fixed-level elimination does not close the StructureRadar receiver.

## New first missing sublemma

```text
FIRST_MISSING_LEMMA=R504TwoFiberParityAlmostBelyiPrimitiveClassification
SMALLEST_NEXT_PROOF_TARGET=R504TwoFiberParityAlmostBelyiPrimitiveDegreeBound
OBSTRUCTION_TYPE=ALGEBRAIC_CLASSIFICATION
```

Required strongest form:

```text
For
  E_*: w^2=t^4+1,
  C_{a,b}: u^2=(t-a)/(t-b),
classify uniformly in n>=3 all maps F:E_*->P1 such that

  F^*{0,2,-2,infinity}
    == t^{-1}(a)+t^{-1}(b) mod 2,

with zero global E_*[2] squareclass obstruction,
R_out(F)<=2,
and primitive lifted map C_{a,b}->E0.

Prove at least one of:
  (i) n is absolutely bounded;
  (ii) every large-n lift is target-isogeny/intermediate-elliptic decomposable;
  (iii) (a,b) lies on a fixed finite degree-independent proper algebraic locus;
  (iv) a finite lower-dimensional locus sufficient for the StructureRadar receiver.
```

## Current verdict

```text
R504_FIXED_CM_NORMALIZATION=PROVED
ALL_DEGREE_PARITY_CLASSIFICATION=PROVED
OUTSIDE_RAMIFICATION_BOUND=R_out<=2
DEGREE_2_RECIPROCAL_REDUCTION=PROVED
UNIFORM_PRIMITIVE_DEGREE_BOUND=OPEN
DEGREE_INDEPENDENT_EXCEPTIONAL_LOCUS=OPEN
DAW_ORR_APPLICABILITY=NOT_REACHED
SR_STR_015_STATUS=EXTERNAL_GATE
MISSING_LEMMA_VERDICT=FIRST_SUBLEMMA_IDENTIFIED
WORK_FALLBACK_ONLY=true
NEXT_ACTION=PAUSE_UNTIL_INITIAL_STRUCTURERADAR_CAMPAIGN_CLOSE
```

This follow-up should be preserved as the SR-STR-015 restart point for the post-close `EXTERNAL_GATE_CLOSURE` phase. It does not change any current Arsenal decision or whole-family exponent.
