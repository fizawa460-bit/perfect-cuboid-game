# Symmetric full-2-descent covering coordinates

```yaml
ID: TB-FORMULA-local-covering-coordinates
TYPE: FORMULA
STATUS: CURRENT
TITLE: Symmetric local covering coordinates and support labels
SCOPE: BOTH
SOURCE_STAGE: Stage14-s5c
SOURCE_PR: 218
SOURCE_MERGE_SHA: ea0c8b56c9c3bc080dce76e050185d33212fae46
SOURCE_FILES:
  - stages/stage14/14-s5c/result.md
```

## INPUT

An oriented primitive Pythagorean face `(S,X,H)` and one supported full-2-descent class.

## OUTPUT

```text
z1=d1*u1^2
z2=d2*u2^2
z3=d3*u3^2

z1-z2=S^2
z3-z1=X^2
z3-z2=H^2

d1*d2*d3 = square class.
```

At an odd bad prime the only nontrivial valuation-parity labels are

```text
12=(1,1,0)
13=(1,0,1)
23=(0,1,1).
```

If the odd bad prime is selected, valuation parity forces

```text
p|S -> 12
p|X -> 13
p|H -> 23.
```

## VARIABLE DICTIONARY

- `di` = squareclass coefficients of the three covering coordinates.
- `ui` = local square variables.
- `zi` = symmetric coordinates `di ui^2`.
- `12,13,23` = parity support labels for `(d1,d2,d3)`.

## USED BY

- Dispatching selected odd-prime Hilbert rows.
- Comparing local covering notation with integral global witness packets.
- Building character matrices across the five Euclid columns.

## DO NOT USE FOR

- Do not assign a nontrivial label to an unselected bad prime; all `di` are units there.
- Do not infer local solubility merely from the three difference identities.
- Do not erase the oriented meaning of `S` and `X` when transporting between s5 and later s6 notation.

## PROVENANCE NOTES

- The symmetric coordinate rewrite and selected-prime routing are the merged theorem of PR #218.
