# Composite squarefree congruence-line cover

```yaml
ID: TB-LEMMA-composite-squarefree-line-cover
TYPE: LEMMA
STATUS: CURRENT
TITLE: CRT projective-line cover for a quadratic ratio modulo an odd squarefree composite
SCOPE: BOTH
SOURCE_STAGE: Stage14-4bi-L
SOURCE_PR: 349
SOURCE_MERGE_SHA: 658d87f16921b88bc240c144ac2702fa08994c1a
SOURCE_FILES:
  - stages/stage14/14-4bi-L/result.md
```

## INPUT

An odd squarefree modulus `q` and units `A,B mod q`, with the congruence

```text
A*x^2 == B*y^2 (mod q).
```

## OUTPUT

The full solution set modulo `q` is covered by at most

```text
2^omega(q)
```

CRT projective lines. Each line lifts to a rank-two lattice in `Z^2` of index `q`.

For a dyadic rectangle with side lengths `U,V`,

```text
N_q(U,V)
 << 2^omega(q)*(U*V/q + min(U,V) + 1)
 <<_eps B^eps*(U*V/q + min(U,V) + 1)
```

inside the Stage14 polynomial witness box.

## VARIABLE DICTIONARY

- `omega(q)` = number of distinct prime divisors of `q`.
- `N_q(U,V)` = number of integer pairs in the dyadic rectangle satisfying the congruence.
- `projective line` = one linear slope condition modulo every prime divisor, combined by CRT.

## USED BY

- Whole edge-kernel incidence with `q=a,b,c`.
- Full leg-radical incidence with `q=R_S,R_X,R_H`.
- Removing dependence on one selected largest prime.

## DO NOT USE FOR

- The lemma requires `q` odd and squarefree and the displayed coefficients to be units modulo `q`.
- Do not replace packet-existence counts by the rectangle density without a transfer theorem.
- Do not interpret `2^omega(q)` as a fixed constant; it is absorbed only on exponent scale as `q^epsilon`.

## PROVENANCE NOTES

Merged PR #349 proves the composite-modulus replacement of the earlier prime-level two-line incidence bound.