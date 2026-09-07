# Stage32 post1648B — Cecotti generator-pair absolute-marking preflight

## Scope

This leaf continues the post1648 absolute-marking localization for the fixed Stage32 target `g1-d186`, `O=210`, `q'=4`, `Q=602`.

Current audited arithmetic survivors remain exactly

`[73,97,235]`.

The post1648 leaf already source-binds the geometric source class

`normal label 9 -> chi_u -> Z3=b3 -> retained boundary labels 41..44 -> delta_0inf=[P_0-P_infinity]`

but does not identify `delta_0inf` with one of the three retained nonzero lines

`L1=r*e1`, `L2=r*e2`, `L3=r*(e1+e2)`.

This leaf asks a narrower question: if the explicit Bolza-curve automorphisms displayed by Cecotti are source-bound to his named lattice generators `S=b4` and `T=-b3` on one common marked principally polarized abelian surface, does equivariance uniquely determine the missing line?

The answer is yes. The marked generator binding itself is not supplied by the cited source, so the resulting residue `235` is conditional only and is not promoted.

## Retained source and target objects

The retained abstract `W`-plane is the Richelot kernel attached to

`x^5-x = x*(x^2-1)*(x^2+1)`

with nonzero classes

- `Z1={+1,-1}` -> `delta_pm1`;
- `Z2={+i,-i}` -> `delta_pmi`;
- `Z3={0,infinity}` -> `delta_0inf`.

The retained lattice plane has

- `L1=[1,0]=r*e1`, residue `73`;
- `L2=[0,1]=r*e2`, residue `97`;
- `L3=[1,1]=r*(e1+e2)`, residue `235`.

The source-locked principal actions are

`b4: L1 fixed, L2 <-> L3`,

`b3: L1 -> L3 -> L2 -> L1`.

Since `-1=+1` on 2-torsion, `T=-b3` has the same action as `b3` on the three nonzero lines.

## Cecotti curve-side finite action

Cecotti, arXiv `2509.24605v1`, Appendix B, writes the lattice generators as

`S=b4`, `T=-b3`,

and identifies the invariant ppav with the Jacobian of the Bolza curve

`C0: y^2=x^5-x`.

The same appendix displays an order-2 curve automorphism with x-map

`phi2(x)=-(x+i)/(1+i*x)`

and an order-6 curve automorphism with x-map

`phi6(x)=i*(x-1)/(x+1)`.

Evaluating these maps exactly on the six branch points gives

`phi2:`

- `0 -> -i`, `infinity -> +i`;
- `+1 <-> -1`;
- `+i -> infinity`, `-i -> 0`.

Hence on the three unordered pairs,

`phi2: Z1 fixed, Z2 <-> Z3`.

Similarly,

`phi6:`

- `0 -> -i`, `infinity -> +i`;
- `+1 -> 0`, `-1 -> infinity`;
- `+i -> -1`, `-i -> +1`.

Hence

`phi6: Z1 -> Z3 -> Z2 -> Z1`.

These are exact finite branch-pair calculations; no numerical approximation is used.

## Conditional unique equivariant marking

Assume, only for this finite preflight, that a single marked ppav identification source-binds

`phi2 -> S=b4`

and

`phi6 -> T=-b3`.

Among all `3! = 6` bijections

`{Z1,Z2,Z3} -> {L1,L2,L3}`,

exactly one intertwines both generator actions:

`Z1 -> L1`,
`Z2 -> L2`,
`Z3 -> L3`.

Therefore under that missing marked generator binding,

`delta_0inf = Z3 -> L3 -> residue 235`.

So a genuine source lock of the generator pair would collapse the current three survivors to the single residue `235` at this marking layer.

This is not current arithmetic credit.

## Why the generator binding is still missing

The cited Cecotti appendix places both the named lattice generators and explicit curve automorphisms on the same Bolza ppav discussion, but it does not explicitly identify the displayed order-2 automorphism with `S=b4` or the displayed order-6 automorphism with `T=-b3` in the retained marked lattice basis.

Koziarz--Rito--Roulleau, arXiv `1904.00793v4`, makes the remaining issue explicit. Their curve-induced group `H48` and torus group `G48` are conjugate by an automorphism `g` of the abelian surface,

`H48 = g G48 g^{-1}`,

and the curve embedding may be changed by composing with `g` before the two group actions are identified. At the cited locator they do not provide the required matrix of `g` on the retained `J[2]` coordinates.

Therefore one may not suppress `g`, match generators merely by order or presentation, and promote the conditional map above to an absolute retained marking.

## Decision

New exact credit:

- the Cecotti order-2 and order-6 curve automorphisms have the displayed exact actions on `Z1,Z2,Z3`;
- those actions and the retained `b4,b3` line actions admit a unique equivariant bijection;
- if the named generator pair is source-bound on one marked ppav, that unique bijection sends `delta_0inf` to `L3`, hence to residue `235`.

Still open:

- the marked ppav conjugacy / generator identification itself;
- the matrix of the conjugating `g` on `J[2] mod 2`, or an equivalent exact source-derived adapter;
- absolute `delta_0inf -> Li` credit;
- any residue contraction of `[73,97,235]`;
- `Q602`, `O210`, `O212+`, controller, receiver, route, theorem, endpoint, or perfect-cuboid credit.

Next exact route:

`MATERIALIZE_MARKED_PPAV_CONJUGACY_G_MOD2_OR_AN_EQUIVALENT_SOURCE_LOCK_IDENTIFYING_CECOTTI_B7_B8_WITH_S_B4_T_MINUS_B3`.
