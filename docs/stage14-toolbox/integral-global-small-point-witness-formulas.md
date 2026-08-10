# Stage14 toolbox — integral global-small-point witness formulas

Reusable entrypoint for the exact integerization proved in merged Stage14-s6-01.

## Core chain

```text
rational non-torsion small point
 -> Z=A/D^2, W=Y/D^3, gcd(A,D)=1
 -> Y^2=A(A-S^2D^2)(A+X^2D^2)
 -> G0=A, G1=A-S^2D^2, G2=A+X^2D^2
 -> exact three factor differences
 -> pairwise gcd support on S/X/H
 -> fixed polynomial witness box
```

This stage intentionally stops before the full signed squarefree-kernel edge packet; that is the next toolbox theme.

## 1. Square/cube denominator

For

```text
E_F: W^2=Z(Z-S^2)(Z+X^2),
```

every rational witness has

```text
Z=A/D^2
W=Y/D^3
D>0
gcd(A,D)=1.
```

The reason is valuation-theoretic: at every denominator prime all three monic cubic factors have the same negative valuation, and their product is a square.

## 2. Exact integral equation

```text
Y^2=A(A-S^2D^2)(A+X^2D^2)
```

with

```text
G0=A
G1=A-S^2D^2
G2=A+X^2D^2
```

gives

```text
G0-G1=S^2D^2
G2-G0=X^2D^2
G2-G1=H^2D^2
G0G1G2=Y^2.
```

For a non-torsion witness all three `Gi` are nonzero.

## 3. Pairwise gcd support

Because `gcd(A,D)=1`, primes of `D` divide none of the `Gi`. Hence

```text
gcd(G0,G1)|S^2
gcd(G0,G2)|X^2
gcd(G1,G2)|H^2.
```

At odd primes the overlap edges are therefore exactly of types `S`, `X`, and `H`; for a primitive Pythagorean face these odd supports are disjoint.

## 4. Polynomial box

For a witness in the merged logarithmic canonical-height window and `H<=B`, a fixed `K_C` satisfies

```text
H_Z(Q)<=B^K_C
|A|<=B^K_C
D^2<=B^K_C.
```

All derived witness variables lie in a fixed polynomial box. This permits dyadic bookkeeping at `B^epsilon` cost, but does not itself prove a counting saving.

## 5. Safe majorant direction

A physical active base supplies a non-torsion point in the height window. Repeated 2-halving selects a nonzero class modulo `2E_F(Q)` without increasing canonical height. Thus

```text
physical hit
 -> global small-point witness
 -> integral witness.
```

At count level:

```text
V(B)<=J_C(B)<=N_local(B).
```

The chosen maximally-halved representative need not reconstruct the original physical point; reconstruction is dropped only for this upper-majorant direction.

## Hard warnings

```text
integral witness => physical reconstruction        false
local admissible => global witness                 false
polynomial box => positive power saving            false
D = D_T                                           false in general
G_i=0 is an allowed non-torsion witness            false
```

Use the next toolbox stage for the signed squarefree-kernel packet and full radical/edge incidence structure.