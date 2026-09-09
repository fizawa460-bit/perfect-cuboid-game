# Stage36 36-09EF fixed-p=2 physical receiver adapter source lock

## Purpose

36-09EE, after external hostile audit PASS `5149991589` and PASS consumption through 36-09EE/V242, proves that the retained-open fixed curve

`C3_2: y^2=(t^2+4)(t^2+1/4)(t^2+9)(t^2+1/9)`

has empty adelic set orthogonal to the full global 2-primary Brauer subgroup. The present leaf proves only the exact semantic adapter needed to transfer that audited fixed-curve obstruction back to the Stage36 **physical receiver sector with base parameter p=2**.

The claim ceiling is fixed-p=2 exclusion. This leaf does not claim that all rational base parameters are excluded, that a finite candidate-parameter set has been shrunk, or that `R29-CAMP2` is empty.

## Locked audited inputs

### 1. Hostile-audited 36-09O physical top-cover adapter

36-09O certificate blob

`6a2678ebedba40e13277100441361039ee47ca28`

was externally hostile-audited on PR #1642, exact head

`be979251c6e3d7a2431fb56537520afd2596c7d9`,

review `5123512777`, exact-head CI `34000052247 / 101397173180`, and later promoted to main by PR #1644 / merge commit `911418e205349e55fb2b4c828a309fbf55afcc47`.

The audited 36-09O notation uses the physical rational base parameter `p`, with exclusions

`p != 0, +1, -1`

and top coordinate exclusions

`t != 0, +1, -1, infinity`.

It defines

`h=p-1/p`,

`c=(p+1)/(p-1)`,

and the exact normalized top genus-3 physical square-lift cover

`C3_p: y^2=(t^2+p^2)(t^2+p^(-2))(t^2+c^2)(t^2+c^(-2))`.

The ordinate normalization is `y=Y/h`; since retained physical parameters satisfy `h != 0`, rational physical square-lift data give rational `(t,y)` on `C3_p`.

36-09O's hostile audit explicitly confirms the physical square-lift formula and the exact reconstruction/top-cover adapter away from the stated boundaries. Therefore this leaf consumes 36-09O as an already-audited semantic edge; it does not reconstruct the Stage29/Stage36 geometry from scratch.

### 2. Fixed-p semantics from 36-09AW

36-09AW certificate blob

`c1970a020803275ba87b249229e319367fa8f811`

uses the same convention: the input is a primitive rational `p=a/b` on the retained physical open, and its `fixed_p_exclusion_rule` speaks literally about emptiness of the retained Stage36 receiver over that fixed `p`.

This confirms that the `p` specialized below is the Stage36 physical base parameter, not a prime-place label.

### 3. Hostile-audited and consumed 36-09EE obstruction

36-09EE certificate blob

`683d52e7cba9e2bd683cc06577fb6913532feb77`

and verifier blob

`5bd144d3fca1ec08112d05e0639d12df9291c0c1`

were hostile-audited on exact head

`6ae4fde45a9665f7a81173e0790006722f9bb1da`

with PASS review `5149991589` and final CI `34312513561 / 102341910787`.

The PASS was merged and separately consumed; receipt blob

`91a047fbffd05ecac51236a94e9d7582347051e2`.

The audited conclusion is

`U_ret(C3_2)(A_Q)^{Br(C3_2)(2)} = empty`,

where the retained top boundary excludes

`t=0, +1, -1, infinity`.

## Exact specialization p=2

Set `p=2`. Then

`p^2=4`,

`p^(-2)=1/4`,

`h=2-1/2=3/2`,

`c=(2+1)/(2-1)=3`,

`c^2=9`,

`c^(-2)=1/9`.

Substitution into the audited 36-09O top model gives exactly

`C3_p|_{p=2} = C3_2`

with equation

`y^2=(t^2+4)(t^2+1/4)(t^2+9)(t^2+1/9)`.

There is no coordinate renaming, quadratic twist, extension of scalars, or extra squareclass branch in this specialization. The normalization factor `h=3/2` is rational and nonzero.

Also `p=2` itself satisfies the physical base exclusions `p != 0,+/-1`.

## Physical receiver implication

Suppose the retained Stage36 physical receiver has a rational point over the fixed base parameter `p=2`.

By the hostile-audited 36-09O physical square-lift/top-cover adapter, its top square-lift coordinate reconstructs a rational point

`P=(t,y) in C3_2(Q)`.

Because the receiver point is retained/physical, the audited top boundary values

`t=0,+1,-1,infinity`

are excluded. Hence

`P in U_ret(C3_2)(Q)`.

Thus there is an exact implication

`RetReceiver_{p=2}(Q) != empty  =>  U_ret(C3_2)(Q) != empty`.

Only this forward implication is required. No converse from arbitrary `C3_2(Q)` points back to physical receiver points is claimed.

## Brauer obstruction implies no retained rational point

For any rational point `P in U_ret(C3_2)(Q)`, its diagonal adelic image `(P)_v` is orthogonal to every global Brauer class: evaluation gives a class in `Br(Q)`, and global reciprocity makes the sum of local invariants zero.

Therefore

`U_ret(C3_2)(Q) subset U_ret(C3_2)(A_Q)^{Br(C3_2)(2)}`.

The right-hand side is empty by hostile-audited 36-09EE. Consequently

`U_ret(C3_2)(Q)=empty`.

Combining with the physical receiver implication gives

`RetReceiver_{p=2}(Q)=empty`.

This is exactly the fixed-p=2 receiver-sector exclusion.

## Credit boundary

36-09EF may claim:

- the audited 36-09EE obstruction transfers to the exact physical Stage36 receiver sector at `p=2`;
- the retained physical receiver over fixed `p=2` is empty;
- `fixed_p_parameter_exclusion_obtained=true` for the single parameter `p=2`.

36-09EF does **not** claim:

- an explicit authority-level finite candidate parameter set containing `p=2` has been shrunk;
- any `p != 2` is excluded;
- the full receiver `R29-CAMP2` is empty;
- `Q11-CAMPEDELLI` is closed;
- endpoint closure;
- a Perfect Cuboid theorem.

Because this is the load-bearing semantic transfer from fixed-curve arithmetic to the physical receiver, the exact-green EF leaf must stop at a fresh hostile-audit checkpoint before any further receiver/theorem promotion.
