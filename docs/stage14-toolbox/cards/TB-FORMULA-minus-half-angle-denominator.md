# Minus half-angle compact denominator

```yaml
ID: TB-FORMULA-minus-half-angle-denominator
TYPE: FORMULA
STATUS: CURRENT
TITLE: Exact minus-column compact denominator and square-cancellation cofactor
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-06
SOURCE_PR: 360
SOURCE_MERGE_SHA: 42f4315b0659bd402a94adeb8822588ea153305a
SOURCE_FILES:
  - stages/stage14/14-s6-06/result.md
```

## INPUT

The physical compact coordinate

```text
Z_-=-N-/(H2-S2)
```

and uniform partner half-angle normalization

```text
H2+S2=kappa*s^2,
H2-S2=kappa*t^2,
X2=kappa*s*t,
kappa in {1,2}, gcd(s,t)=1.
```

## OUTPUT

If `D_-^2` is the reduced denominator of `Z_-`, then

```text
D_-^2=(H2-S2)/gcd(N-,H2-S2)
     =X2^2/gcd(X2^2,U*V),
D_-^2 | H2-S2,
D_- | X2,
D_- | t.
```

Define

```text
k_-:=t/D_-.
```

Then the cancellation identity is exact:

```text
gcd(N-,H2-S2)=kappa*k_-^2.
```

## VARIABLE DICTIONARY

- `D_-` = the `T0=(0,0)` physical compact denominator selector; this is the `D_T` of s6-05/s6-06 after dual-selector notation is introduced.
- `k_-` = complementary square-cancellation cofactor on the minus half-angle column.

## USED BY

- Physical denominator divisibility.
- Root-sign routing at odd partner-leg primes.
- Dual product identity with the plus selector.

## DO NOT USE FOR

- Do not identify `D_-` with generic witness denominator `D` or abstract packet least denominator `D_min`.
- `D_-<=B^(1/2)` alone is not a whole-family saving.

## PROVENANCE NOTES

Merged Stage14-s6-06 proves both the reduced-denominator formula and the exact half-angle cancellation cofactor.