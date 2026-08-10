# Dispatch a balanced reduced-coordinate strip to inert-prime square sieve

```yaml
ID: TB-RECIPE-dispatch-balanced-inert-square-sieve
TYPE: RECIPE
STATUS: CURRENT
TITLE: Route the balanced fixed-quartic receiver to inert-prime character cancellation
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-07
SOURCE_PR: 410
SOURCE_MERGE_SHA: c99aafc834defe32c232615b86cd6b367cf30e2d
SOURCE_FILES:
  - stages/stage14/14-s7-07/result.md
  - stages/stage14/14-4bv/result.md
```

## INPUT

Reduced coprime coordinates in a balanced denominator region satisfying

```text
ker(F(P,Q))=ker(F(R,S)),
F(A,B)=A*B*(B-A)*(B+A),
Q*S << B.
```

## OUTPUT

At inert primes `p=3 mod 4`, use the exact complete trace cancellation for `F`; after product-square descent, use the 4bv square-sieve packet bound

```text
N_packet << M*H^(-1/2)*B^o(1).
```

Thick square-part packets go directly to the square-sieve receiver. Thin packets must switch to squarefree-coefficient/shared-label structure rather than being discarded as exceptional.

## VARIABLE DICTIONARY

- `F(P,Q)` = fixed quartic squareclass label.
- `M` = square-part box volume.
- `H` = minimum square-part thickness.

## USED BY

- Balanced-strip character cancellation.
- Thick square-part packet thinning.
- Deciding when to switch from square-part variables to coefficient variables.

## DO NOT USE FOR

- A single polynomial-size CRT modulus does not give the required fixed power saving by itself.
- Thin square-part packets include abundant squarefree states and are not negligible automatically.

## PROVENANCE NOTES

Merged s7-07 isolates the inert-prime receiver; merged 4bv proves the fixed-packet Fourier completion and `H^(-1/2)` square-sieve saving.