# Five-column local routing with orientation adapter

```yaml
ID: TB-DICTIONARY-five-column-local-routing
TYPE: DICTIONARY
STATUS: CURRENT
TITLE: Five Euclid columns and orientation-aware S/X/H routing
SCOPE: BOTH
SOURCE_STAGE: Stage14-s5b
SOURCE_PR: 213
SOURCE_MERGE_SHA: f0e78817a65527cfb348df5f7f3ed66289afa2da
SOURCE_FILES:
  - stages/stage14/14-s5b/result.md
  - stages/stage14/14-s5c/result.md
  - stages/stage14/14-s6-01/result.md
```

## INPUT

A primitive opposite-parity Euclid pair `m>n>0`, `gcd(m,n)=1`.

## OUTPUT

```text
A=m
B=n
C=m-n
D=m+n
E=m^2+n^2
```

At odd primes these five columns are pairwise coprime.

Historical s5 local orientation:

```text
S=CD=m^2-n^2
X=2AB=2mn
H=E
A,B -> X
C,D -> S
E   -> H
```

Later swapped orientation used by s6-01:

```text
S=2AB
X=CD
H=E
A,B -> S
C,D -> X
E   -> H
```

## VARIABLE DICTIONARY

- `A,B,C,D,E` = orientation-free Euclid support columns.
- `S,X,H` = oriented covering legs/hypotenuse; `S/X` are not permanently attached to a given column pair.
- `12,13,23` = selected odd-prime valuation-parity labels attached to `S,X,H` respectively.

## USED BY

- Translating historical s5 local Hilbert rows into current main/s notation.
- Reusing the same five moving support columns after s6-01 global witness packetization.
- Avoiding repeated prime-by-prime gcd checks.

## DO NOT USE FOR

- Do not infer `m,n -> label13` unless the covering uses the historical s5 orientation.
- Do not infer `m,n -> label12` unless the covering uses the swapped orientation.
- Do not identify a five-column equality with equality of oriented `S/X` semantics.

## PROVENANCE NOTES

- PR #213 proves odd pairwise coprimality of the five columns.
- PR #218 fixes the historical s5 routing `m,n -> X`, `m±n -> S`, `m^2+n^2 -> H`.
- PR #345 later uses the swapped `S/X` orientation while retaining the same five columns; toolbox-ae makes that adapter explicit rather than silently choosing one convention.
