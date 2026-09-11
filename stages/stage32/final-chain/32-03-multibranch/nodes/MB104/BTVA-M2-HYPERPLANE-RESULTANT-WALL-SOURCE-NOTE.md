# Stage32 MB104 — BTVA `m=2` hyperplane-resultant wall

Status: **RETAINED METHOD-SPECIFIC NONCLOSURE WALL / NO POPULATION-WIDE FINITE WINDOW**.

## Primary source

Nils Bruin, Jordan Thomas, Anthony Varilly-Alvarado,
*Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*,
Algebra & Number Theory 16 (2022), 1377--1405,
DOI `10.2140/ant.2022.16.1377`, arXiv `1912.08908v3`.

Primary locators used here:

- the perfect-cuboid computation in the section on applications to complete intersections of quadrics;
- Table 1 / the displayed degree-two generators;
- the statement that `h^0(X_pc, hat S^2 Omega^1_X)=13`;
- the statement that `omega_7` vanishes on `H: x_1=0` and
  `<omega_7> = H^0(X_pc,(hat S^2 Omega^1_X)(-H))`;
- Corollary `explicit_resultant_locus`, which requires **two linearly independent** sections in
  `H^0(X, hat S^m Omega^1_X(-floor(m/2) H_X))` to obtain the algebraic resultant locus for curves whose allowed nodes lie on `H_X`.

The arXiv record lists the original ancillary files `perfectcuboid_script.m` and `perfectcuboid.out` for Theorem 1.2.

For byte-addressable replay only, the public mirror
`CosmicWill/magic-square-of-squares-3x3` at commit
`c5a8240aed71ed30c63528a2e8f1411f9cc2e04f` contains copies of the arXiv source/ancillary files used in this note:

- `papers/1912.08908/BTVA.tex`, git blob `60a4769e3960675dbb26a6332af72aee93d361a0`;
- `papers/1912.08908/anc/perfectcuboid_script.m`, git blob `7b84650178bd077a9829b51f669c78118b6ce4b9`.

The mirror is used only to lock exact bytes that reproduce the published/arXiv formulas. It is not promoted over the paper/arXiv as mathematical authority.

## Exact `m=2` structure retained

The degree-two reflexive symmetric-differential space has dimension

`h^0(X_pc, hat S^2 Omega^1_X)=13`.

The 13 displayed generators include `omega_7` and its six coordinate multiples. In the affine chart `x_1=1`, the ancillary computation represents

`omega_7 = ((x_3^2+1) dx_2^2 - 2 x_2 x_3 dx_2 dx_3 + (x_2^2+1) dx_3^2)/(y_1 y_2 y_3 z^2)`.

More importantly for the present route, if `H` is the hyperplane class then the paper states

`<omega_7> = H^0(X_pc,(hat S^2 Omega^1_X)(-H))`.

Thus

`dim H^0(X_pc,(hat S^2 Omega^1_X)(-H)) = 1`.

Because every hyperplane section is cut by a section of `O_X(H)`, multiplying the unique (up to scalar) section of the `(-H)` twist by the chosen hyperplane equation gives the corresponding degree-two reflexive differential vanishing along that hyperplane. The relevant vanishing subspace remains one-dimensional.

## Consequence for the BTVA hyperplane-resultant mechanism

For `m=2`, Corollary `explicit_resultant_locus` asks for

`omega_1, omega_2 in H^0(X, hat S^2 Omega^1_X(-H_X))`

that are linearly independent.

On the perfect-cuboid surface this space has dimension exactly `1`. Therefore the hypotheses of that **two-section hyperplane-resultant construction cannot be satisfied at `m=2` for any hyperplane**.

This matters for the current `N>=14` leaf: the existence of 13 degree-two reflexive sections does not by itself give a pair of degree-two sections simultaneously enjoying the hyperplane-vanishing/exceptional-extension property used by that corollary.

## Ancillary scope

The public `perfectcuboid_script.m`:

- constructs `hat S^2 Omega^1_X` via a double dual;
- records 13 degree-zero forms;
- checks the displayed formulas;
- enumerates linear spans of singular points and hyperplane orbits;
- screens hyperplane sections modulo a finite prime and then identifies the low-genus components used in Theorem 1.2.

It does **not** provide, as a retained output, an arbitrary-node-subset extension matrix for the full 13-space, nor a population-wide resultant for node supports of size `N>=14`.

## Decision

Retire the immediate route

`13 reflexive m=2 sections -> choose 2 hyperplane-vanishing sections -> resultant -> close N>=14`.

The obstruction is exact: the hyperplane-vanishing subspace at `m=2` is only one-dimensional.

Re-entry requires genuinely new information, for example:

1. exact extension-condition matrices for the 13-dimensional reflexive `m=2` space at arbitrary subsets of the 48 nodes, showing that some relevant `N>=14` supports retain at least two independent extendable sections;
2. actual `m>=3` symmetric-differential spaces and dependent local extension conditions, not Proposition 3.1 lower bounds alone;
3. explicit differentials/resultants/foliations not requiring two sections in the same `(-H)` twist;
4. independent Picard/jet/member geometry.

## Firewalls

- `dim=1` for the hyperplane-vanishing twist is not interpreted as `h^0(Y,S^2 Omega_Y^1)=1`.
- No claim is made that the full 13-dimensional reflexive space has only one section extendable across an arbitrary node subset.
- Failure of the two-section hyperplane-resultant hypothesis is not failure of all degree-two differential methods.
- No finite degree window or finite Picard release is claimed.
- No `R29-LG2-MB` discharge, receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit is claimed.
- Merge remains unauthorized.
