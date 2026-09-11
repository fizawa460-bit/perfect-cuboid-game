# MB104 post-V8 handoff

Parent main checkpoint remains `STAGE32_MB104_FINITE_WINDOW_COEFFICIENT_BARRIER_V8`.  MB104 is still open and has no receiver/theorem/endpoint credit.

## Retained low-support side

Bruin--Thomas--Varilly-Alvarado implies that genus-0/1 curves meeting at most 13 box nodes form a finite set.  An abstract maximum degree `D_13` exists, but no numerical cutoff is certified.

## Full `m=2` node-extension classification

The complete 13-dimensional reflexive `m=2` space has now been evaluated at all 48 cuboid nodes.

The BTVA ancillary count of node-spanned hyperplanes is independently reproduced:

`593735`.

Their exact simultaneous extension ranks are

- rank 12: `590468`;
- rank 11: `3264`;
- rank 10: `3`.

The rank-11 hyperplanes form seven exact `Aut(S)` node-orbits.  Across all `24538032` pairs `(H,p)` with `p` outside a node-spanned hyperplane,

- `24509616` have extension rank 13;
- `28416` have extension rank 12.

The survivor pairs form 35 `Aut(S)` pair-orbits.

All survivor kernel lines extend at exactly 16 nodes.  There are only 24 such 16-node supports, forming one node orbit.  A representative kernel is

`omega* = omega1 - i*omega2 - omega3 + i*omega4 + i*omega5 + omega6`.

Retained files:

- `BTVA-M2-HYPERPLANE-ORBIT-CLASSIFICATION-SOURCE-NOTE.md`
- `BTVA-M2-HYPERPLANE-ORBIT-CLASSIFICATION.json`
- `verify_mb104_btva_m2_hyperplane_orbit_classification.py`

## Special 24-support foliation closes at degree 16

On `x1=1`, put

`u=x2/(z+1)`, `w=x3/(z+1)`, `t=u+i*w=(x2+i*x3)/(z+x1)`.

Direct substitution of the BTVA Table-1 formulas gives

`omega*=(2-2i)/(t*(t-1)*(t+i))*(dt)^2`.

Hence every integral curve of the representative surviving section is contained in a fiber

`x2+i*x3=lambda*(z+x1)`,

a hyperplane section.  Since the hyperplane class is `H=K_S` and `H^2=16`, every nonexceptional irreducible component has

`d<=16`.

The same bound holds on all 24 automorphic special supports.

Therefore any projective-rank-7 carrier with a nonzero simultaneous `m=2` extension section has `d<=16`.  Any unbounded rank-7 carrier must belong to the complementary **zero-extension** branch.

Retained files:

- `BTVA-M2-SPECIAL-24-WEB-FIBRATION.md`
- `BTVA-M2-SPECIAL-24-WEB-FIBRATION.json`

## Current leaf

`MB104_RANK7_M2_ZERO_EXTENSION_OR_HIGHER_M_GLOBAL_MEMBER_OBSTRUCTION`.

Priority routes:

1. compute `m>=3` symmetric differentials and node-extension maps on rank-7 supports where `m=2` has kernel zero;
2. find a different sheaf/cover whose sections survive those supports; or
3. use actual Picard linear-system / global-member geometry to obstruct the zero-extension population.

Do **not** reinterpret `m=2` kernel zero as curve nonexistence.  No finite Picard release, `R29-LG2-MB` discharge, receiver/effectivity/theorem/endpoint credit, or merge authorization.
