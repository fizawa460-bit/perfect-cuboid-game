# Stage32 MAIN scratch — EX1 h=4 uniform transvection interface candidate

Status: **SCRATCH / UNAUDITED cross-lane adapter candidate**. No MAIN/EX1 authority, claim-DAG, route, or merge state changes.

Snapshot: `f2a89e613cdf91191a0aada9e90c9fc93373a6c6`.

## Result

The historical Stage32 transvection predicate does not intrinsically require the O210 slice or `R105=0`.

For EX1's full h=4 ladder `Q_EX1=210,212,...,266`, the currently source-bound ingredients assemble as follows:

1. EX1-05G re-establishes the same fixed V6 h=4 correspondence arithmetic for all 29 states: `deg(f1),deg(f2)=(105,81)`, `Q_Rosati=602`, and the same 28 common-fixed-plane mod-2 residues.
2. The fixed V6 exceptional multiplicities and the fixed node-to-boundary marking reconstruct the exact grouped pair masses without using the O210 contact histogram.
3. For a branch of positive exceptional contact multiplicity `m`, EX1-05F gives local cusp order `k_i=m+2*ell_i`. Modulo the hyperelliptic fiber class, an odd branch contributes its marked Weierstrass point and an even branch contributes a paired orbit. Thus the parity contribution depends on `m mod 2`, not on `m=1`.
4. For any partition of a fixed exceptional mass `M_p`, the number of odd branch multiplicities satisfies `n_p = M_p (mod 2)`.
5. The specified `C2 -> X(4)` double cover is etale away from the six cusp fibers; smooth-boundary contact has even pulled-back order. Hence the relevant fixed-point parity is exhausted by odd exceptional contacts in this model.
6. The fixed class/marking replay gives the same Weierstrass parity matrix as post1505, namely the branch transposition `(2 4)`, i.e. abstract direction `delta_0inf`.
7. The self-Richelot adapter fixes the retained module basis `(e1,e2,r*e1,r*e2)` and `W=span{(0,0,1,0),(0,0,0,1)}`. It still does not identify `delta_0inf` with one individual retained W-line.

Therefore the basis-independent predicate

`T symplectic`, `rank_F2(T-I)=1`, `0 != im(T-I) subset W`

can be replayed directly against EX1-05G's 28 residues, without first importing the historical O210 `28 -> 16` intermediate filter.

The direct finite replay leaves exactly

`[73,97,235]`.

The three image lines are respectively

- 73 -> `(0,0,1,0)`
- 97 -> `(0,0,0,1)`
- 235 -> `(0,0,1,1)`.

So at scratch-candidate level the coarse EX1 compatibility ledger contracts from

`29 x 28 = 812`

to

`29 x 3 = 87`.

This excludes **0/29 EX1 Q-states**: all 29 still have three mod-2 residue possibilities. It is a cross-lane coupling improvement, not EX1 closure.

## Exact 28-candidate classification

The direct predicate partitions the 28 residues as follows:

- non-symplectic: `[67,75,99,107,193,201,225,233]`;
- symplectic identity (`rank(T-I)=0`): `[65]`;
- desired symplectic rank-one transvections with nonzero image in W: `[73,97,235]`;
- symplectic rank-two with image contained in W: `[105,195,203,227]`;
- symplectic rank-two with image not contained in W: `[20,60,69,77,81,113,150,190,199,207,211,243]`.

Thus the intermediate historical `T|W=T^dagger|W=id` 28->16 step is not needed for this direct finite classification once the uniform transvection geometry is admitted.

## What is new versus historical Stage32

Historical post1505 proved the transvection inside the O210 route using the 210 odd-contact presentation. The new scratch observation is that the parity proof can be rewritten using:

- arbitrary branch multiplicities;
- fixed V6 exceptional mass parity;
- complete cusp fixed-point accounting;
- the fixed marked node incidence.

That removes the apparent dependence on `O=210` and `R105=0`.

The numerical answer `[73,97,235]` itself is not new MAIN credit. The new candidate is the **uniform EX1 adapter across all 29 h=4 ramification states**.

## Promotion boundary

Do not promote this from scratch yet.

Before any retained consolidation, the cross-lane composition should be packaged as one replayable adapter whose source locks explicitly include EX1-05F/05G, the fixed V6 incidence/mass data, the retained self-Richelot W coordinates, the principal Riemann form, and the historical transvection convention. Then hostile audit must check that no O210-only geometric hypothesis has been silently retained.

In particular this scratch result does **not**:

- select one absolute W-line or one residue among `[73,97,235]`;
- exclude any of the 29 EX1 Q-states;
- exclude Q602 or O210;
- establish a genuine V6 carrier or population-wide V6 exclusion;
- change MAIN routing, claim authority, or Stage32 closure;
- authorize merge.
