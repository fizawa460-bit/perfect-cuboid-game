# Stage14-toolbox-H0 — counterexample catalogue

These are logical countermodels for the connection only. They do not claim that the physical Stage14 family realizes every synthetic configuration.

## CE1 — signed cancellation destroys the collision lower bound
Take two distinct states `z1,z2` with the same `(xi,k)` and identical Gaussian character rows on `P` active primes. Give them coefficients

```text
a1=+1, a2=-1.
```

The combinatorial unit-weight collision energy is

```text
C_off=2
```

(ordered pair count). But the signed Gaussian centered quadratic form is

\[
\sum_{i\ne j}a_i\overline{a_j}\left|\sum_p c_i(p)c_j(p)\right|^2=-2P^2.
\]

Thus an upper bound for the signed form cannot lower-bound the positive collision count. This falsifies the implication unless the collision specialization is nonnegative/common-phase or a separate PSD domination is proved.

## CE2 — same k does not imply Gaussian row coherence
Use split primes `5,13`. Let two states have the same transverse label `k`, but let their Gaussian squareclasses be `1` and `6`. Their Legendre rows are

```text
D=1 : (+1,+1)
D=6 : (+1,-1)
```

because `(6/5)=+1` and `(6/13)=-1`. Their Gaussian row correlation is zero:

\[
1\cdot1+1\cdot(-1)=0.
\]

Hence the Gaussian centered pair contribution is zero although the same-`k` collision count is nonzero. A statewise bridge between `(k/p)` and `chi_p(Ftilde)` is therefore necessary.

## CE3 — raw natural-scale second moment is too weak for the centered s target
Take `H=2` states with identical good character rows on `P=4` primes and unit weights. Then

```text
E_A=H=2,
R_cent=2*P^2=32.
```

The raw natural-scale Gaussian bound allows

```text
P^2*E_A = 32,
```

so it is exactly satisfied. But the s-side centered random scale is

```text
H^2*P = 16,
```

which fails by factor `P/H=2`.

Asymptotically, at the critical s7-15 choice `P=B^(1/7)` and `H<=B^(1/8)`, the same logical gap is `B^(1/56)`.

## CE4 — residue no-alias does not remove principal squareclass coherence
Take `r` pairwise exact/residue-distinct Gaussian labels, all with the same nonzero squareclass and unit weights. Then

```text
E_A=r,
M=P(P-1)r^2.
```

The desired near-linear raw target is only `~P^2 r`. The failure factor is `r`, despite exact-pair near-linearity and zero residue alias. This is the merged tH14 R2 coherent-fiber obstruction in minimal form.

Therefore residue-diagonal closure cannot be used as a substitute for selector/squareclass anti-coherence.

## CE5 — double diagonal subtraction breaks the centered identity
Take a single state good at all `P` primes. The true off-diagonal collision energy is zero. Exact state-diagonal subtraction once gives zero. If the exact state diagonal and the alias-free residue diagonal are both subtracted as if they were independent diagonals, the result becomes negative by the state-diagonal mass. Hence the two labels must be identified only for charging the residue contribution, not subtracted twice.

## CE6 — inert local cancellation is not a split-prime theorem
Suppose a local identity is known only for primes `p=3 mod 4`. A selector-sensitive Gaussian mean square quantified only over split primes `p=1 mod 4` has disjoint auxiliary support. There is no logical implication between the two statements without a transfer theorem or a common-prime reformulation. This blocks direct use of the s7-16 inert Fourier identity inside the t/tH split-prime Gaussian receiver.

## CE7 — the current R2 QLS scale does not certify the rho=1/7 conditional target
The R2 adapter requires `2rho>=d`. With the currently certified safe conductor exponent `d=4`, `rho=1/7` gives

```text
2rho=2/7 < 4.
```

Thus the current QLS adapter has no route to the s7-15 `rho=1/7` conditional scale unless the conductor is sharpened all the way to `d<=2/7` or another theorem replaces the adapter.

## Catalogue verdict

The strongest independent conclusion is negative but precise:

```text
SAME_COEFFICIENT_SPACE_IS_SUFFICIENT_FOR_CONNECTION=false
SIGNED_GAUSSIAN_CENTERED_FORM_AUTOMATICALLY_CONTROLS_UNIT_COLLISIONS=false
SAME_K_AUTOMATICALLY_IMPLIES_GAUSSIAN_ROW_COHERENCE=false
RAW_GAUSSIAN_NATURAL_SCALE_IMPLIES_S_CENTERED_SCALE=false
RESIDUE_DIAGONAL_CLOSURE_IMPLIES_SELECTOR_DISPERSION=false
TH14_R2_QLS_DIRECTLY_CERTIFIES_RHO_1_7=false
```

The connection remains viable only under the explicit hypotheses in `hypothesis-map.md`.
