# Stage32 MB104 — BTVA projective-span filter

Status: **RETAINED GLOBAL MEMBER-LEVEL NECESSARY CONDITION / NONCLOSING**.

This note imports the cuboid-specific theorem of Bruin--Thomas--Várilly-Alvarado only at its exact published strength and converts it into a node-support filter for `R29-LG2-MB`.

## Source lock

Primary reference:

Nils Bruin, Jordan Thomas, Anthony Várilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasihyperbolicity*, Algebra & Number Theory 16 (2022), no. 6, 1377--1405, DOI `10.2140/ant.2022.16.1377`, arXiv `1912.08908`.

Theorem 1.2 for the perfect-cuboid surface states:

- every genus-0 curve passes through at least six distinct surface singularities;
- every genus-0 curve other than the 32 known plane conics passes through at least seven singularities spanning `P^6`;
- every genus-1 curve lies in a linear space of dimension at most one larger than the span of the singularities it passes through; in particular it is a component of a hyperplane section or passes through at least six singularities spanning a hyperplane.

Stoll--Testa, *Curves on the surface of cuboids*, Math. Comp. (2026), DOI `10.1090/mcom/4238`, explicitly recalls these conclusions in its low-genus literature discussion.

## Adapter to the Stage32 canonical model

Stage32 source-locks that `H=K_S` is the pullback of the canonical hyperplane class and `H^2=16`.

If an integral curve `D` is contained in any proper linear subspace of `P^6`, then it is contained in some hyperplane. Hence it is a component of an effective canonical hyperplane section. Since `H` is nef and the total canonical degree of that section is `H^2=16`, every such component satisfies

`d=H.D<=16`.

Therefore every integral carrier with `d>16` spans all of `P^6`.

Combining this with BTVA gives the exact support filters:

- `g=0`, non-conic: the image curve meets at least seven distinct box nodes and those nodes span `P^6`;
- `g=1`, `d>16`: the image curve meets at least six distinct box nodes and those nodes span at least a hyperplane `P^5`.

For the multibranch receiver, write `N=# {i : r_i>0}`. Then the corresponding necessary cardinality consequences are

- `g=0`, `d>2`: `N>=7`;
- `g=1`, `d>16`: `N>=6`.

The stronger content is the projective-span condition, not merely the cardinality.

## Interaction with the retained MB104 scaling wall

The retained analytic/effective scaling profile `D_k=6kH-k*sum E_i` has positive exceptional support at all 48 nodes. Hence the BTVA support/span filter does not by itself eliminate that arbitrary-degree profile.

The filter is nevertheless exact and useful for any future fixed-degree Picard/node enumeration: MB103 canonical node profiles with support failing the required projective span can be rejected before effectivity work.

## Why this does not close MB104

The theorem gives a lower bound on distinct surface-node support. It does not give an upper bound on ordinary self-nodes/triple points of the strict transform, an upper bound on exceptional mass, or a subunit-slope upper bound on Beauville ramification. In particular it does not contradict Lu--Miyaoka's linear ordinary-singularity debt.

## Firewalls

- Surface singularities traversed by the curve are not identified with ordinary self-nodes of the strict transform.
- The BTVA support count is not identified with total delta.
- No unibranch `176/192` cap is imported.
- No finite degree window, finite Picard release, `R29-LG2-MB` discharge, receiver, theorem, endpoint, or Perfect-Cuboid credit is claimed.
- Merge remains unauthorized.
