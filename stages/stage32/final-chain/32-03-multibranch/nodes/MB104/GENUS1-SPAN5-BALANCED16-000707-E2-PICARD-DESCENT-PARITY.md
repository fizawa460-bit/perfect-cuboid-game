# MB104 000707, e=2: exact Picard/2 descent parity

Status: retained exact necessary condition; no e=2 closure and no credit change.

## Question and exact model

For the fourteen supported nodes, test

`D' = 7*l*H + sum_j (x_j - 8*l)*E_j`

in the quotient of `Pic(S)/2 Pic(S)` by the span of the sixteen absent-type exceptional classes.  The verifier does **not** reduce the displayed `H,E_j` coefficients in a naive ambient basis.  It reconstructs every class in the saturated rank-64 retained Picard basis using the Stage33/33-07 marking and only then reduces those integral coordinates modulo two.

The retained payload files are permanent-denylist material.  They are imported inside the repository, source-locked, and hashed; neither this note, the certificate, nor verifier stdout contains their matrices or encoded payload.

## Exact result

- `dim_F2 Pic(S)/2Pic(S) = 64`.
- The sixteen absent exceptional classes span rank `15`.
- The quotient by that span has dimension `49`.
- The hyperplane class maps to zero in the relevant quotient, so the `l` term disappears.
- The membership map on the fourteen supported exceptional classes has rank `14`.

In support order

`(0,1,2,3,8,9,10,11,24,25,26,32,33,34)`,

the independent conditions are exactly

`x_0=x_1=x_2=x_3=x_8=x_9=x_10=x_11=x_24=x_25=x_26=x_32=x_33=x_34=0 (mod 2)`.

The two seven-node saturation equations and two four-node determinant-passport equations have rank `4`.  They are consequences of the exact descent conditions.  The combined rank is `14`, so descent contributes `10` new independent parity equations.

Thus the answer to “does `D' mod 2` give new independent branch-allocation parity information?” is **YES**.  The remaining affine parity dimension is `0`, hence there is exactly one parity class: all fourteen allocations are even.

## Why this does not close e=2

The unique parity class is not contradictory.  In particular, the already retained formal balanced allocation `x_j=4*l` is even at every supported node.  Therefore this route supplies a strong necessary condition but does not by itself close `e=2` or support any theorem, receiver, endpoint, or MAIN credit.

## Obstruction witnesses and replay

The compact certificate stores fourteen 64-bit dual covectors in hexadecimal.  For condition `x_j=0`, its covector annihilates every absent exceptional class and `H`, and pairs as a Kronecker delta with the fourteen supported exceptional classes.  An odd `x_j` is therefore an exact non-membership witness.

Run:

`python stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_000707_e2_picard_descent_parity.py`

The verifier is fail-closed on every retained/dependency blob hash and on both retained canonical hashes.  Standard output is restricted to two bounded lines: the PASS token and rank/verdict summary.  It starts no workflow, changes no authority or credit, and authorizes no merge.
