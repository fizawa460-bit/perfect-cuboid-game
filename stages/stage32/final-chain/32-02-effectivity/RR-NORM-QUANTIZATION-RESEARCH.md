# Stage32 32-02 — RR norm quantization research

Status: **RESEARCH ONLY / ZERO CREDIT**

This note strengthens only the scalar interface around the already source-locked
Riemann--Roch sufficient-effectivity gate.  It does **not** create FULL178,
effectivity, pruning, theorem, endpoint, closure, or merge credit.

## Locked input

Use the existing 32-02 notation

- `K^2 = 16`, `chi(O) = 8`,
- `d = K.C`,
- `r = gcd(d,16)`, `m = 16/r`, `n = d/r`,
- `y = m C - n K`,
- `N = -y^2 = 16 n^2 - m^2 C^2`,
- RR sufficient effectivity for `d > 16` is `C^2 >= d-14`, equivalently
  `16 N <= m^2 (d^2 - 16 d + 224)`.

The same source-locked RR identity

`chi(O(C)) = (C^2-d)/2 + 8`

has integral left-hand side, so for integral `C`

`C^2 == d (mod 2)`.

No additional geometric input is used below.

## Quantized norm class

Write `C^2 = d + 2 k`.  Then

`N = 16 n^2 - m^2 d - 2 m^2 k`.

Hence every admissible `N` lies in one residue class

`N == 16 n^2 - m^2 d (mod 2 m^2)`.

Define the RR boundary norm

`T(d) = m^2 (d^2/16 - d + 14)
      = 16 n^2 - m^2 d + 14 m^2`.

Because `14 m^2` is a multiple of `2 m^2`, `T(d)` lies in exactly the
same residue class.  The boundary `C^2=d-14` gives `N=T(d)`, while the
first parity-compatible non-RR value `C^2=d-16` gives

`N = T(d) + 2 m^2`.

Therefore the scalar gate is quantized: there is no admissible norm in

`T(d) < N < T(d) + 2 m^2`.

## Upper-bound interface

A producer need not necessarily expose the exact scalar `N`.
A source-locked certified upper bound `U >= N` is already sufficient whenever

`U < T(d) + 2 m^2`.

Indeed `N` is in the same `2 m^2` residue class as `T(d)`, so the above
strict upper bound forces `N <= T(d)`, which is exactly the existing RR
sufficient-effectivity inequality.

For an integer upper bound this can be written

`U <= T(d) + 2 m^2 - 1`.

This is a strictly weaker producer contract than `exact N`, but it is useful
only if a future source-locked producer can actually certify such a bound.
The current Picard64 source gap is **not** repaired by this note alone.

## Even-degree residue table

For even `d`, the arithmetic specializes to:

| `v2(d)` regime | `m` | modulus `2m^2` | admissible `N` residue |
|---|---:|---:|---:|
| `d == 2 (mod 4)` | 8 | 128 | 16 |
| `d == 4 (mod 8)` | 4 | 32 | 16 |
| `d == 8 (mod 16)` | 2 | 8 | 0 |
| `d == 0 (mod 16)` | 1 | 2 | 0 |

Wolfram exact arithmetic was used as an independent check of these residue
classes and of the transformed norm identity.  The load-bearing argument is
the algebra above, not a finite computation.

## Research consequence

The next 32-02 producer search may target either:

1. the original exact field `negative_hperp_square_N`, or
2. a source-locked certified upper bound satisfying the quantized RR cutoff.

Any such producer still requires the normal source-lock, end-to-end verifier,
and hostile-audit discipline before credit can be consumed.
