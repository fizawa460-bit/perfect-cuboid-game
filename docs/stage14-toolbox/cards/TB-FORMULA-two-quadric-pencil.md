# Exact pencil determinant for the fixed witness curve

```yaml
ID: TB-FORMULA-two-quadric-pencil
TYPE: FORMULA
STATUS: CURRENT
TITLE: Exact singular-member polynomial for the fixed two-quadrics pencil
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-02
SOURCE_PR: 348
SOURCE_MERGE_SHA: 1338ee0170a6d92c26a9dd4fa21c886a8125d6db
SOURCE_FILES:
  - stages/stage14/14-s6-02/result.md
```

## INPUT

The fixed-packet quadrics

```text
Q1=d0*u0^2-d1*u1^2-S^2*D^2,
Q2=d2*u2^2-d0*u0^2-X^2*D^2.
```

## OUTPUT

For pencil parameters `[lambda:mu]`, the diagonal coefficients of `lambda Q1+mu Q2` are

```text
u0^2 :  d0*(lambda-mu)
u1^2 : -d1*lambda
u2^2 :  d2*mu
D^2  : -(lambda*S^2+mu*X^2).
```

Hence, up to a nonzero sign,

```text
Det(lambda,mu)
 = d0*d1*d2
   *lambda*mu*(lambda-mu)*(lambda*S^2+mu*X^2).
```

The four singular pencil parameters are exactly

```text
[0:1], [1:0], [1:1], [-X^2:S^2].
```

They are pairwise distinct because `S,X>0` and `S^2+X^2=H^2!=0`.

## VARIABLE DICTIONARY

- `[lambda:mu]` = projective parameter on the pencil of quadrics.
- `Det` = determinant of the diagonal quadratic form in the pencil.

## USED BY

- Fast recognition that the pencil has four distinct singular members.
- Regression tests for the fixed-packet genus-one geometry.
- Good-reduction diagnostics away from coefficient/discriminant primes.

## DO NOT USE FOR

- Four distinct roots are a geometry certificate only in the stated nonzero fixed-packet setting.
- Do not treat `lambda,mu` as witness variables.
- Do not import this determinant into the diagonal-pair quartic model; that is a different genus-one presentation.

## PROVENANCE NOTES

The exact factorization and root separation are proved in merged PR #348 and independently in merged main-track PR #347.