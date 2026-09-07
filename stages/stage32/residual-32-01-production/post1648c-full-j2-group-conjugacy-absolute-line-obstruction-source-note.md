# Stage32 post1648C — full J[2] group-conjugacy absolute-line obstruction

## Scope

This leaf tests whether the remaining absolute marking can be recovered without choosing named curve/lattice generators: use the complete mod-2 group action on the Bolza Jacobian, together with the principal Weil pairing, and enumerate every symplectic conjugacy to the retained `Z[sqrt(-2)]^2/2` action.

The current arithmetic survivors remain `[73,97,235]`.

## Source J[2]

Use the six Weierstrass points in the retained order

`(+1,-1,+i,-i,0,infinity)`.

Model `J(C0)[2]` by even subsets modulo complements. For an explicit four-dimensional coordinate system use the pair classes

`{+1,-1}, {+1,+i}, {+1,-i}, {+1,0}`.

In this basis the three nonzero Richelot-kernel classes are

- `Z1=delta_pm1 = (1,0,0,0)`;
- `Z2=delta_pmi = (0,1,1,0)`;
- `Z3=delta_0inf = (1,1,1,0)`.

The Weil pairing is reconstructed as parity of intersection of even subsets. The two explicit Cecotti curve maps retained in post1648B induce exact 4x4 F2 matrices. They generate an order-24 subgroup on `J[2]`.

## Target J[2]

Use the retained lattice basis

`(e1,e2,r*e1,r*e2)`, `r^2=-2`.

Modulo 2, `r^2=0`. Reduce the source-locked principal `G12` matrices `b1,b2,b3,b4` entrywise in `Z[r]/2`; they generate an order-24 subgroup of `GL4(F2)`.

The retained principal Riemann form reduces to the exact target Weil form. The already-audited W-plane is

`span_F2(r*e1,r*e2)`

with nonzero lines

`L1=(0,0,1,0)`, `L2=(0,0,0,1)`, `L3=(0,0,1,1)`

corresponding to residues `73,97,235`.

## Exhaustive conjugacy audit

Enumerate all `|GL4(F2)|=20160` invertible 4x4 matrices `P`. Retain exactly those satisfying both:

1. `P * G_source * P^{-1} = G_target`;
2. `P^t E_target P = E_source`.

There are exactly 48 such symplectic group conjugacies.

Every one sends the source Richelot plane `W` to the same retained target plane

`span_F2(r*e1,r*e2)`.

So the full unmarked group action independently recovers the W-plane itself.

However, the induced bijections on its three nonzero lines realize all six permutations:

`(Z1,Z2,Z3)` can map to every permutation of `(L1,L2,L3)`.

In particular `Z3=delta_0inf` occurs as each of `L1,L2,L3` among valid symplectic conjugacies. Thus its possible residues remain exactly

`[73,97,235]`.

## Consequence

This is stronger than a search miss. It proves a finite non-identifiability statement:

> the unmarked full mod-2 Bolza group action plus the principal Weil form determines the Richelot plane, but cannot determine an absolute nonzero line inside it.

Therefore repeating abstract group matching, subgroup-order matching, symplectic conjugacy enumeration, or unmarked full `J[2]` reconstruction cannot close the Stage32 marking gap.

The post1648B conditional result remains valid: a distinguished source binding of the curve generator pair to `S=b4,T=-b3` would select `Z3->L3`, residue `235`. But selecting one of the 48 conjugacies without source-derived marking is forbidden.

## Next exact route

The remaining datum is genuinely marked:

`MATERIALIZE_A_DISTINGUISHED_MARKED_CONJUGACY_G_MOD2_OR_SOURCE_BIND_ONE_CURVE_GENERATOR_TO_ONE_RETAINED_LATTICE_GENERATOR`.

No current residue is removed. `Q602`, `O210`, and `O212+` remain open/blocked as before; no controller, receiver, route, theorem, endpoint, or perfect-cuboid credit is created.
