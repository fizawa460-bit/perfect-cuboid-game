# Stage36 36-09DX global Phi-Selmer intersection source lock

## Exact-green inputs

36-09DV gives the finite global ambient

`H^1_S(Q,ker(Phi)) = Q(S,2)^3`,

with `S={infinity,2,3,5,7}` and squareclass basis

`[-1],[2],[3],[5],[7]`.

Hence the ambient is an F2-vector space of dimension 15 and cardinality 32768.

36-09DW gives the exact local Kummer images `L_v=image(delta_Phi,v)` at every place in `S` in fixed squareclass bit coordinates.

## Localization maps

For each global squareclass generator, localization is computed directly in the fixed local bases.

At infinity:

- `[-1] -> [1]`, and positive prime generators map to `[0]`.

At `Q_2`, in basis `[v2 mod2,-1 bit,5 bit]`:

- `[-1]=(0,1,0)`;
- `[2]=(1,0,0)`;
- `[3]=(0,1,1)`;
- `[5]=(0,0,1)`;
- `[7]=(0,1,0)`.

At odd `Q_p`, in basis `[vp mod2,nonsquare-unit bit]`, the localization bits are obtained from valuation parity and the Legendre symbol of the unit part. The verifier recomputes all entries for `p=3,5,7` rather than trusting a retained table.

## Selmer intersection

The global `Phi`-Selmer group is exactly the kernel of the linear localization/quotient map

`H^1_S(Q,ker(Phi)) -> product_{v in S} H^1(Q_v,ker(Phi))/L_v`.

No theorem beyond the defining Selmer local-condition intersection is used here; after DV/DW this is finite F2 linear algebra.

The resulting constraint matrix has rank 13. Therefore

`dim_F2 Sel^Phi(A/Q)=2`,

with convenient global squareclass basis

- `s1=([-1],[-1],[1])`;
- `s2=([6],[3],[1])`.

Thus the four classes are

`([1],[1],[1])`,
`([-1],[-1],[1])`,
`([6],[3],[1])`,
`([-6],[-3],[1])`.

In particular the third DU/Phi coordinate is trivial on the entire global Phi-Selmer group.

## Credit boundary

This computes the finite `Phi`-Selmer group only. It does not by itself compute the exponent-two defect between `T_2 Sel(A)` and `T_2 Sel(J)`, does not identify either full pro-Selmer group, and does not determine the retained-open Abel-Jacobi intersection or any Brauer-Manin/fixed-p/receiver/endpoint credit.
