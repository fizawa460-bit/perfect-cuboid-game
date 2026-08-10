# Kernel packet refinement to the five Euclid columns

```yaml
ID: TB-DICTIONARY-kernel-five-column-refinement
TYPE: DICTIONARY
STATUS: CURRENT
TITLE: Unique refinement of odd edge kernels to the five Euclid support columns
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
```

## INPUT

The s6-oriented primitive Euclid face

```text
S=2mn
X=(m-n)(m+n)
H=m^2+n^2
```

and the edge kernels `a,b,c` from `TB-FORMULA-signed-kernel-edge-packet`.

## OUTPUT

At odd primes the support splits uniquely as

```text
a=a_m*a_n
  a_m | rad(m)
  a_n | rad(n)

b=b_-*b_+
  b_- | rad(m-n)
  b_+ | rad(m+n)

c | rad(m^2+n^2).
```

Thus the global witness kernel uses exactly the same five moving support columns

```text
m, n, m-n, m+n, m^2+n^2
```

as the closed local 2-descent system.

## VARIABLE DICTIONARY

- `a_m,a_n` = `S`-edge pieces on the `m,n` columns in the s6 orientation.
- `b_-,b_+` = `X`-edge pieces on the `m-n,m+n` columns.
- `c` = `H`-edge piece on `m^2+n^2`.

## USED BY

- Moving from local character columns to an actual global witness packet.
- Prime/radical partition arguments without introducing a new support family.
- Cross-route main/s notation checks.

## DO NOT USE FOR

- If historical s5 orientation is used, apply toolbox-ae's orientation adapter before assigning `S/X` roles.
- Do not infer equality between the selected kernel and the full radical of a column.

## PROVENANCE NOTES

Merged PR #345 proves the exact five-column refinement after global witness packetization.