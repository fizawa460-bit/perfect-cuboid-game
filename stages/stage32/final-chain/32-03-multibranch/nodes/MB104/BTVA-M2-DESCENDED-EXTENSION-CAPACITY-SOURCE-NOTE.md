# Stage32 MB104 — `m=2` descended extension-capacity adapter

Status: **RETAINED EXACT SUBSPACE ADAPTER / NONCLOSING FOR THE HIGH-DEGREE RECEIVER**.

## Parents / sources

Primary mathematical source is Bruin--Thomas--Varilly-Alvarado (BTVA),
*Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*,
Algebra & Number Theory 16 (2022), DOI `10.2140/ant.2022.16.1377`, arXiv `1912.08908v3`.

This note consumes two retained Stage32 MB104 parents:

- `BTVA-M2-HYPERPLANE-RESULTANT-WALL.json`, blob `ce7928cc6df4aa7c911175ae685d03d42ee02098`;
- `BTVA-PROJECTIVE-SPAN-FILTER.json`, blob `4ee8e6061a7cc2a54b54786fd065923434381bde`.

The degree-two parent source-locks the BTVA statement

`H^0(X_pc, hat S^2 Omega^1_X(-H)) = <eta>`

with dimension one (the paper's `omega_7` after choosing a hyperplane), and the 13-dimensional reflexive `m=2` space. The BTVA ancillary Table-1 package explicitly contains the seven coordinate multiples of this descended generator.

The projective-span parent source-locks the exact node-support consequences:

- genus 0, nonconic (`d>2`): met surface nodes have coordinate-vector rank `7`, i.e. span `P^6`;
- genus 1, `d>16`: met surface nodes have coordinate-vector rank at least `6`.

## The seven-dimensional descended package

Let

`eta in H^0(X_pc, hat S^2 Omega^1_X(-1))`

be a nonzero generator. Multiplication by linear forms gives

`U := H^0(P^6,O(1)) * eta`.

Since `X_pc` is nondegenerate and `eta != 0`, multiplication is injective on the seven-dimensional space of ambient linear forms. Hence

`dim U = 7`.

The seven coordinate multiples appearing in the BTVA computation are an explicit realization of this package.

## Node-set extension subspace

Let `T` be a set of surface nodes and let `r(T)` be the vector-space rank of their homogeneous coordinate vectors in the ambient 7-dimensional coordinate space.

Define

`U_T := { l*eta in U : l(P)=0 for every P in T }`.

The linear forms vanishing on `T` are exactly the annihilator of the span of the node coordinate vectors. Therefore

`dim U_T = 7-r(T)`.

For every `l*eta in U_T`, the hyperplane `H_l : l=0` contains every node in `T`. BTVA Corollary `vanishing_on_hyperplane` at `m=2` therefore implies that `l*eta` extends regularly across every exceptional component over `T`.

Thus `U_T` is an explicit, exactly computed subspace of the full degree-two reflexive space whose members are simultaneously extendable across all nodes in `T`.

Critical firewall: this proves an exact dimension for **this descended seven-dimensional package**. It does not assert that the full 13-dimensional reflexive space has no additional sections extendable across `T`.

## Consequence for two-section resultants

Within this package, two independent simultaneously extendable sections exist iff

`dim U_T >= 2`, equivalently `r(T)<=5`.

One such section exists iff `r(T)<=6`.

Now combine with the retained BTVA projective-span filter.

### Genus 0

For every unknown/nonconic genus-0 carrier with `d>2`, BTVA gives `r(T)=7`. Therefore

`dim U_T=0`.

So the descended `O(1)*eta` package supplies **no** degree-two section simultaneously extendable across all met surface nodes of such a carrier.

### Genus 1

For every genus-1 carrier with `d>16`, BTVA gives `r(T)>=6`. Therefore

`dim U_T<=1`.

So this package never supplies the two independent sections needed for the BTVA two-section resultant mechanism on the high-degree genus-1 population.

## Decision

The most explicit known degree-two descended package is completely understood at arbitrary node support through the single invariant `r(T)`, but it cannot close the remaining high-degree `R29-LG2-MB` population:

- high-degree genus 0: package capacity `0`;
- high-degree genus 1: package capacity at most `1`.

This sharpens the preceding `dim H^0(-H)=1` wall from one fixed hyperplane to **every arbitrary node set**, inside the seven-dimensional descended package.

The next useful computation must leave this package. Preferred routes are:

1. compute the local extension maps of the other six directions in the full 13-dimensional reflexive `m=2` space at the 48 nodes and their intersections for MB103 node-orbits;
2. compute actual `m>=3` symmetric-differential spaces and extension maps, not just Proposition 3.1 lower bounds;
3. use independent Picard/jet/member geometry.

## Firewalls

- `U_T` is not identified with the full extendable subspace of the 13-dimensional reflexive space.
- No claim is made that `H^0(Y,S^2 Omega^1_Y)=0`.
- Failure of the descended package does not retire all `m=2` symmetric-differential methods.
- No finite degree window or finite Picard release is claimed.
- No `R29-LG2-MB` discharge, receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit is claimed.
- Merge remains unauthorized.
