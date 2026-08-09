# Euclid five-column normalization

```yaml
ID: TB-DICTIONARY-euclid-five-columns
TYPE: DICTIONARY
STATUS: CURRENT
TITLE: Euclid five-column normalization for Stage14 main/s
SCOPE: BOTH
SOURCE_STAGE: Stage14-s6-01
SOURCE_PR: 345
SOURCE_MERGE_SHA: 86b91ffcd8bae79452ef75f187c8570a3819d386
SOURCE_FILES:
  - stages/stage14/14-s6-01/result.md
```

## INPUT

- A primitive Pythagorean first-face base in the normalized Euclid chart used by the s5/s6 support decomposition.
- `m>n>0`, `gcd(m,n)=1`, and `m,n` have opposite parity.

## OUTPUT

```text
S = 2mn
X = m^2-n^2 = (m-n)(m+n)
H = m^2+n^2

five odd support columns:
A-column = m
B-column = n
C-column = m-n
D-column = m+n
E-column = m^2+n^2
```

At odd primes these five factors have pairwise disjoint support in the normalized primitive chart.

For the global witness edge divisors of s6-01,

```text
a = a_A a_B,   a_A|rad(m),     a_B|rad(n)
b = b_C b_D,   b_C|rad(m-n),   b_D|rad(m+n)
c = c_E,       c_E|rad(m^2+n^2).
```

## VARIABLE DICTIONARY

- `S` = normalized even leg of the primitive first-face Pythagorean triple.
- `X` = normalized odd leg.
- `H` = primitive face hypotenuse.
- `m,n` = Euclid parameters.
- `a,b,c` = odd squarefree edge-kernel divisors from the global witness packet, not cuboid-edge names.
- `A`/`B`/`C`/`D`/`E`-column = historical s5 support-column labels; they are not the rational-coordinate variables `A,D` used in `Z=A/D^2`.

## USED BY

- Stage14 `s5*` local-state support bookkeeping.
- Stage14 `s6*` global witness packetization.
- Stage14 `14-4*` when importing the same supported kernel state.

## DO NOT USE FOR

- Do not identify the `A`-column with the rational numerator `A`.
- Do not identify the `D`-column with a rational-point denominator `D`, `D_min`, or `D_T`.
- Do not transfer a statement from one face orientation to another without explicitly applying the route's normalization/swap convention first.
- Pairwise-disjoint support here is the odd-prime support statement in the primitive normalized Euclid chart; it does not remove separate 2-adic bookkeeping.

## PROVENANCE NOTES

- Stage14-s6-01 proves that the global witness odd edge packet refines exactly to the same five moving support columns previously used by s5.
- Main-route Stage14-4bg independently freezes the same supported integral witness model; the normalized five-column refinement is most explicit in the merged s6-01 source.
