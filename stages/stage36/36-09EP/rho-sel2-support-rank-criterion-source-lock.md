# Stage36 36-09EP — exact support/Legendre-symbol rank criterion for rho Sel2

## Purpose

36-09EO gives a point-search-free evaluator for

```text
E_rho,p: y^2=X(X-P^2)(X-Q^2).
```

The evaluator is already finite, but it is still described as localization of rational squareclasses. This leaf extracts the smaller arithmetic datum that actually determines the matrix and proves an exact rank criterion for `Sel2_dim=2`.

No new bounded search is needed.

## Labelled radical support datum

For primitive positive `p=a/b`, `a!=b`, put

```text
P=a^2+2ab-b^2,
Q=a^2-2ab-b^2,
D=P^2-Q^2=8ab(a^2-b^2).
```

By 36-09EL, `gcd(P,Q) in {1,2}`. Hence the odd bad primes split disjointly into

```text
S_P={odd q:q|P},
S_Q={odd q:q|Q},
S_D={odd q:q|D and q does not divide P*Q}.
```

Let

```text
S_f={2} union S_P union S_Q union S_D.
```

Retain only the following finite datum:

1. the actual primes in the three labelled sets `S_P,S_Q,S_D`;
2. for every odd support prime, its residue modulo 8;
3. the dyadic branch bit `epsilon_2 in {shallow,deep}` from 36-09EN;
4. the pairwise Legendre-symbol bits `(r/q)` for distinct odd support primes `q,r`.

Call this the **labelled radical Legendre datum** `R(a,b)`.

Crucially, no valuation exponent of `P`, `Q`, or `D` appears.

## Localization matrix from R(a,b) alone

Use global generators

```text
G=[-1,2] followed by the odd primes in S_f in increasing order.
```

For an odd place `q`, the localization bits of a global generator are determined as follows:

- `-1`: valuation bit zero; unit bit is the quadratic character of `-1 mod q`, hence determined by `q mod4`;
- `q`: valuation bit one and unit bit zero;
- an odd prime `r!=q`: valuation bit zero and unit bit is the Legendre-symbol bit `(r/q)`;
- `2`: valuation bit zero and unit bit is determined by `q mod8`.

At `Q_2`:

- `[-1]=(0,1,0)`;
- `[2]=(1,0,0)`;
- every odd prime `r` has its three-bit squareclass determined by `r mod8`.

At infinity only the generator `-1` has nontrivial sign.

Thus every localization matrix `L_v` is determined by `R(a,b)`.

## Local Kummer blocks from R(a,b) alone

36-09EM proves that every odd local Kummer subspace is determined only by the label `P/Q/D` and `q mod8`. 36-09EN proves that the dyadic subspace is determined only by `epsilon_2`, and the real subspace is uniform.

Therefore every block

```text
W_v^perp L_v
```

and hence the entire Sel2 matrix is determined by `R(a,b)`.

Write the resulting purely combinatorial matrix as

```text
M_R(R(a,b)).
```

It is equal, entry for entry after the same canonical ordering, to the matrix `M_Sel2(a,b)` of 36-09EL/EO.

## Exact rank criterion

Let

```text
n=|G|=1+|S_f|.
```

The ambient full-2 descent space has dimension `2n`, so

```text
dim_F2 Sel^2(E_rho,p/Q)=2n-rank_F2 M_R(R(a,b)).
```

Consequently

```text
Sel2_dim=2
iff
rank_F2 M_R(R(a,b))=2n-2.
```

This is an exact necessary-and-sufficient arithmetic criterion. It is not a statistical classifier and contains no local point search.

For use with the exact-green 36-09EH physical exclusion criterion, one then adds the independent no-rational-4-torsion and no-rational-3-torsion conditions.

## Exponent erasure

Because both localization squareclasses and the EM/EN branch formulas use only support membership, residues, Legendre symbols, and the dyadic branch, changing any positive valuation exponent while preserving `R(a,b)` leaves `M_R` unchanged.

Thus the rho Sel2 dimension is controlled by labelled **radical** support plus quadratic reciprocity data, not by the full integers `P,Q,D`.

This is the exact compression that the false D-squareclass-only model in 36-09EL was missing: the P/Q/D labels and pairwise residue graph must be retained, but exponent data can be discarded.

## Exact replay

The verifier independently constructs `M_R` using only the labelled radical datum and compares it with the EO localization evaluator on all 1546 ordered primitive rows in the exact EO 50-box.

It checks entry-space rank equality and identical Sel2 dimensions on every row, including the exact 24 `Sel2_dim=2` rows. The replay is a regression check; the theorem follows from the entry formulas above.

## Next obligation

The exact criterion still requires an F2 rank computation. The next useful step is to derive checkable sufficient conditions for maximal rank `2n-2` from graph structure / quadratic reciprocity, without evaluating the whole matrix row-by-row:

```text
36-09EQ_RHO_LEGENDRE_GRAPH_MAXIMAL_RANK_PREFLIGHT.
```

## Credit firewall

This leaf adds no fixed-p exclusions beyond the exact 24-value EO registry. It does not prove maximal rank uniformly. Therefore all remain false:

```text
uniform_Sel2_dimension_2_theorem,
candidate_parameter_set_shrunk,
receiver_emptiness_proved,
R29_CAMP2_closed,
Q11_CAMPEDELLI_closed,
endpoint_closed,
perfect_cuboid_nonexistence_claim.
```
