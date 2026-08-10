# Dispatch a thin shared-xi packet to a one-cell square sieve

```yaml
ID: TB-RECIPE-dispatch-shared-xi-cell-switch
TYPE: RECIPE
STATUS: CURRENT
TITLE: Resolve thin square-part packets by exact shared-xi four-cell switching
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-08
SOURCE_PR: 417
SOURCE_MERGE_SHA: 29e08fea3ebc1838fde2418957b9c0490456e1b1
SOURCE_FILES:
  - stages/stage14/14-s7-08/result.md
  - stages/stage14/14-4bv/result.md
```

## INPUT

A product-square packet

```text
P=a*x^2, Q=b*y^2, R=c*z^2, S=d*h^2,
ab=cd=xi,
```

in the hard thin square-part branch.

## OUTPUT

Factor the common squarefree label exactly:

```text
r=gcd(a,c), s=gcd(a,d), t=gcd(b,c), j=gcd(b,d),
a=rs, b=tj, c=rt, d=sj, xi=rstj.
```

A forced large coefficient gives a forced large cell. Vary that cell `q~T`; the residual condition becomes a nondegenerate one-variable quartic

```text
(A^2-B^2 q^2)(C^2-D^2 q^2)=square,
```

and the square sieve gives `O(T^(1/2)B^o(1))`, i.e. relative saving `T^(-1/2)`.

## VARIABLE DICTIONARY

- `r,s,t,j` = pairwise-coprime shared-`xi` cells.
- `q` = canonically selected large cell.
- `T` = dyadic size of the selected cell.

## USED BY

- Closing the thin square-part branch left by 4bv.
- Converting a large squarefree coefficient into a genuine counting receiver.
- Recombining the architecture at exponent `18/19`.

## DO NOT USE FOR

- The quartic square-polynomial degeneration must first be excluded by the physical open inequalities.
- A large coefficient is not a saving until a large cell is selected and the cell sieve is applied.

## PROVENANCE NOTES

Merged s7-08 proves the exact four-cell factorization, nondegeneracy, cell square-sieve saving, and the exhaustive `18/19` recombination.