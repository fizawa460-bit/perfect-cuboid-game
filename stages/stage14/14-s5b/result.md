# Stage14-s5b — odd-prime reciprocity matrix skeleton

For primitive Euclid parameters `m>n>0`, `gcd(m,n)=1`, `m\not\equiv n (mod 2)`, set

```text
A=m
B=n
C=m-n
D=m+n
E=m^2+n^2.
```

Then

```text
2SXH = 4ABCDE.
```

## Odd-prime separation

The five factors `A,B,C,D,E` are pairwise coprime at every odd prime. Equivalently, each odd bad prime `p|2SXH` belongs to exactly one moving factor.

This follows from the Euclid conditions and the identities

```text
gcd(A,B)=gcd(A,C)=gcd(A,D)=gcd(A,E)=1,
gcd(B,C)=gcd(B,D)=gcd(B,E)=1,
gcd(C,D)|2,
gcd(C,E)|2,
gcd(D,E)|2.
```

Because `C,D` are odd, their odd gcds are 1.

## Full-2-descent parity labels

For the s1 covering interface

```text
d1*u1^2 - d2*u2^2 = S^2
d3*u3^2 - d1*u1^2 = X^2
d1*d2*d3 = square class,
```

write `eps_i(p)=v_p(d_i) mod 2`. At every odd bad prime,

```text
eps_1(p)+eps_2(p)+eps_3(p)=0 mod 2,
```

so the nontrivial local support type is one of exactly three labels

```text
12=(1,1,0), 13=(1,0,1), 23=(0,1,1).
```

Thus the moving odd-prime descent datum is a sparse labelled incidence matrix: rows are odd primes, columns are `A,B,C,D,E`, each row has exactly one nonzero factor column and one label in `{12,13,23}`.

## Reciprocity matrix

For squarefree odd kernels `a,b,c,d,e` of `A,B,C,D,E`, define the off-diagonal quadratic-character matrix

```text
R_ij = (f_i/f_j),  i != j,
```

with `f=(a,b,c,d,e)` and Jacobi symbols interpreted prime-by-prime. Quadratic reciprocity determines the transpose relation

```text
R_ij R_ji = (-1)^(((f_i-1)/2)((f_j-1)/2)).
```

Hence only one triangular half of the odd reciprocity matrix plus the mod-4 residue vector is independent. Any odd-prime local-solubility test for a supported covering class can therefore be expressed using this finite character data together with its `{12,13,23}` support labels.

This stage deliberately does not claim the final Hilbert-symbol sign equations for every covering label. The 2-adic place and the exact label-dependent odd local equations remain the next gate.

```text
STAGE14_S5B=COMPLETE_ODD_PRIME_RECIPROCITY_SKELETON
FIVE_MOVING_FACTORS_ODD_PAIRWISE_COPRIME=true
EACH_ODD_BAD_PRIME_HAS_UNIQUE_FACTOR_COLUMN=true
NONTRIVIAL_DESCENT_SUPPORT_LABELS=12,13,23
ODD_RECIPROCITY_MATRIX_REDUCED_TO_TRIANGULAR_HALF_PLUS_MOD4=true
LABEL_DEPENDENT_LOCAL_HILBERT_EQUATIONS_DERIVED=false
P2_LOCAL_MATRIX_DERIVED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s5c derive label-dependent odd Hilbert equations and the 2-adic local matrix
```
