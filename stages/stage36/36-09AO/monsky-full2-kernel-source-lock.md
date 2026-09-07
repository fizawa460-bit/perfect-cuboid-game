# Stage36 36-09AO source lock: Monsky matrix and full-2 class coordinates

Accessed: 2026-09-07

## Primary source lineage

- D. R. Heath-Brown, *The size of Selmer groups for the congruent number problem, II*, Invent. Math. 118 (1994), 331–370, Appendix by P. Monsky.
- Shenxing Zhang, *On non-congruent numbers as multiples of non-congruent numbers*, §2.1 (2025 preprint / author-hosted version): https://zhangshenxing.github.io/publications/Zhang2025.pdf
- Shamik Das and Sudipa Mondal, *Monsky Matrix and 2-Selmer rank*, arXiv:2604.26183 (2026), §3, as a recent explicit restatement of the matrix/rank formula.

The Stage36 verifier locks one convention below; row/column-equivalent conventions in other papers are not silently mixed with it.

## Additive symbol convention

For an odd prime `p`, write

```text
[a/p] = 0 if (a/p)=+1,
[a/p] = 1 if (a/p)=-1
```

in `F_2`.

For odd squarefree `n=p1*...*pk`, define `A_n=(a_ij)` by

```text
a_ij=[p_j/p_i]              (i != j),
a_ii=sum_{j != i} a_ij      in F_2,
```

and

```text
D_l=diag([l/p_1],...,[l/p_k]), l in {-1,2,-2}.
```

## Odd Monsky matrix and class coordinates

For odd `n`, use

```text
M_n = [ A_n + D_2    D_2
        D_2          A_n + D_-2 ].
```

Monsky's pure 2-Selmer group `Sel_2(E_n)/E_n(Q)[2]` is the kernel of this matrix. Every pure Selmer class may be represented by a homogeneous-space triple `(d1,d2,d3)` with positive `d_i|n`, and with

```text
psi_n(d)=(v_{p1}(d),...,v_{pk}(d))^T mod 2,
(d1,d2,d3) |-> ( psi_n(d2), psi_n(d1) )^T in ker M_n.
```

The homogeneous-space convention used by Zhang/Heath-Brown orders the three roots as `(+n,-n,0)`: a generic point `(x,y)` corresponds to squareclasses `(x-n,x+n,x)`.

Stage36 36-09AJ normalized its triple in root order `(0,+n,-n)`. Therefore the exact ordering adapter is

```text
Stage36 (k0,kplus,kminus)
    -> Monsky (d1,d2,d3)=(kplus,kminus,k0).
```

One may multiply componentwise by the Kummer class of a rational 2-torsion point to choose the standard positive-divisor representative; this changes only the representative in the pure Selmer quotient.

For root order `(+n,-n,0)`, the four rational 2-torsion triples are

```text
O        : (1,1,1)
(n,0)    : (2,2n,n)
(-n,0)   : (-2n,2,-n)
(0,0)    : (-n,n,-1).
```

## Even Monsky matrix

For a total twist `N=2n` with odd squarefree `n=p1*...*pk`, the same source convention uses

```text
M_2n = [ A_n^T + D_2    D_-1
         D_2            A_n + D_2 ].
```

A standard representative has its three components supported on the odd part `n`, with the source normalization conditions, and maps by

```text
(d1,d2,d3) |-> ( psi_n(|d3|), psi_n(d2) )^T.
```

36-09AO source-locks this even formula/interface but does not yet execute a Stage36 even-branch class-coordinate example.

## Selmer-rank interpretation

If `N` has `k` odd prime factors, the pure 2-Selmer dimension is the nullity of the corresponding `2k x 2k` Monsky matrix. Equivalently, if `s(N)` denotes the 2-Selmer rank modulo rational 2-torsion,

```text
s(N)=2k-rank_F2(M_N).
```

Full matrix rank therefore proves pure 2-Selmer rank zero. A nonzero kernel vector is only a Selmer-class coordinate after local solubility / Selmer membership is established; it does not decide Mordell-Weil versus Sha by itself.

## Stage36 B=7 exact adapter

Audited Stage36 AL has `n=73073=7*11*13*73` and normalized root-order `(0,+n,-n)` triple

```text
(-143,-1606,1898).
```

Reorder to Monsky roots `(+n,-n,0)`:

```text
(-1606,1898,-143).
```

Multiply by the rational 2-torsion triple for `(-n,0)`, namely `(-2n,2,-n)`, and reduce componentwise modulo rational squares. This gives

```text
(d1,d2,d3)=(91,949,511)
           =(7*13,13*73,7*73),
```

all positive divisors of `n`.

With prime order `(7,11,13,73)`,

```text
psi(d2)=psi(949)=(0,0,1,1),
psi(d1)=psi(91) =(1,0,1,0),
```

so the exact Stage36 pure-Selmer kernel vector is

```text
v_B7=(0,0,1,1 | 1,0,1,0).
```

The 36-09AO verifier reconstructs `M_73073`, checks `M*v_B7=0`, and computes rank `6`, nullity `2`. Combining this with audited AL rank zero shows `dim_F2 Sha(E_73073)[2]=2`; this is a fixed-fiber consequence only.

## Scope firewall

Monsky matrix construction uses actual prime identities and pairwise Legendre symbols. It does not restore a residue-only Stage36 compression. Matrix nullity alone does not decide whether a nonzero kernel class is Mordell-Weil or Sha, and this adapter does not classify all Stage36 branches or close the receiver.