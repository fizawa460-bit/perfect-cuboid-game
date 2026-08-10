# Pairwise gcd support of integral witness factors

```yaml
ID: TB-LEMMA-witness-pairwise-gcd-support
TYPE: LEMMA
STATUS: CURRENT
TITLE: Exact pairwise gcd support on the three Pythagorean edges
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
```

## INPUT

The integral witness factors

```text
G0=A
G1=A-S^2D^2
G2=A+X^2D^2
```

with `gcd(A,D)=1` and primitive Pythagorean `(S,X,H)`.

## OUTPUT

Every prime dividing `D` is coprime to all three `Gi`, and

```text
gcd(G0,G1) | S^2
gcd(G0,G2) | X^2
gcd(G1,G2) | H^2.
```

Thus at odd primes the three possible overlap supports are

```text
01 -> S
02 -> X
12 -> H
```

and are pairwise disjoint for a primitive face.

## VARIABLE DICTIONARY

- `01,02,12` refer to the pairs `(G0,G1)`, `(G0,G2)`, `(G1,G2)`.
- `D` contributes no prime to any `Gi` overlap.

## USED BY

- The next-stage odd squarefree-kernel edge packet.
- Separating the three moving bad-prime supports.
- Preventing uncontrolled shared factors in the two-quadrics system.

## DO NOT USE FOR

- This card does not yet state the complete signed squarefree-kernel factorization.
- Do not move an odd overlap prime from one Pythagorean edge to another.

## PROVENANCE NOTES

Merged PR #345 proves the divisibility from the exact factor differences and `gcd(A,D)=1`.