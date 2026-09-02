# Stage32 post-1490 O210 q'=4 Bolza principal-polarization / Rosati source lock

Scope: fixed recovered V6 class only, target `g1-d186`, at the retained
`O=210`, `q'=4` simultaneous-correspondence frontier. This note supplies the
exact principal polarization/Rosati datum that the preceding Bolza frontier
left open. It does not enumerate correspondences and it does not exclude O210.

## Retained target

The retained frontier identifies the fixed genus-two target with the Bolza
curve

`C0 : y^2 = x^5 - x`

and fixes, as an unpolarized complex Abelian variety,

`J(C0) ~= E^2`,  `E = C / Z[sqrt(-2)]`.

Write `s=sqrt(-2)`, so `O=Z[s]` and conjugation sends `s` to `-s`.

## External principal-polarization source lock

Use Alexandre Gelin, Everett W. Howe, and Christophe Ritzenthaler,
*Principally polarized squares of elliptic curves with field of moduli equal
to Q*, Open Book Series 2 (2019), 257-274, DOI
`10.2140/obs.2019.2.257`, arXiv `1806.03826v2`.

Only the following exact facts are imported.

1. Proposition 3.1 identifies principal polarizations on `E^2` with positive
   definite unimodular Hermitian matrices over `End(E)`, relative to the
   product polarization. In the product coordinates the product Rosati
   involution is conjugate transpose.
2. Table 4, row `Delta=-8`, gives the genus-two curve
   `y^2=x^5+x` with polarization matrix

   `H = [[2, omega+1],[-omega+1,2]]`.

   For even discriminant the table uses `omega=sqrt(Delta)/2`; hence for
   `Delta=-8`, `omega=sqrt(-2)=s`.

The individual `Delta=-8` Table-4 row and Proposition 3.1 are unconditional
inputs. The GRH qualification in the article concerns completeness of the
global list and is not used here.

The Table-4 curve `y^2=x^5+x` is complex-isomorphic to the retained Bolza
model `y^2=x^5-x`: choose `a,c in C^*` with `a^4=-1` and `c^2=-a`, and put
`X=a*x`, `Y=c*y`. Therefore the principal polarization of the retained Bolza
Jacobian can be represented in the chosen unpolarized `E^2` coordinates by

`H = [[2,1+s],[1-s,2]]`.

## Exact Hermitian arithmetic

The matrix is Hermitian and

`det(H) = 4 - (1+s)(1-s) = 4-3 = 1`.

Thus its inverse is integral:

`H^{-1} = [[2,-1-s],[-1+s,2]]`.

If `T in M_2(O)` and `T^*` denotes conjugate transpose, then the Rosati
involution for the Bolza principal polarization is

`T^dagger = H^{-1} T^* H`.

For the coordinate order

`(t11.a,t11.b,t12.a,t12.b,t21.a,t21.b,t22.a,t22.b)`

with `tij=tij.a+tij.b*s`, the resulting Z-linear involution is the exact
8-by-8 matrix

```
[ 4,  0, -2, -4,  2, -4, -3,  0]
[ 0, -4, -2,  2, -2, -2,  0,  3]
[ 2,  4,  1, -4,  4,  0, -2, -4]
[ 2, -2, -2, -1,  0, -4, -2,  2]
[-2,  4,  4,  0,  1,  4,  2, -4]
[ 2,  2,  0, -4,  2, -1, -2, -2]
[-3,  0,  2,  4, -2,  4,  4,  0]
[ 0,  3,  2, -2,  2,  2,  0, -4]
```

Direct exact multiplication gives `dagger^2=1`.

## Correspondence bound in explicit coordinates

The preceding frontier defines

`T=(f1)_*(f2)^*`

for the simultaneous degree-105 and degree-81 maps and gives the necessary
Rosati inequality

`T^dagger T <= 8505`.

With the exact matrix above this is equivalently

`8505 H - T^* H T >= 0`

in the Hermitian positive-semidefinite cone.

This is now an explicit integral rank-eight lattice inequality. It is a finite
frontier, but this note deliberately does not materialize all integral points.
The next step must first estimate/count or orbit-reduce that frontier
lightweightly, respecting the repository compute/storage policy.

## Firewalls

- `O=210` remains OPEN.
- No integral `T` is claimed to be geometrically realizable.
- No absence of an integral `T` is claimed here.
- The product polarization is not substituted for the Bolza polarization.
- The already-principal Abel-Jacobi divisor is not reopened.
- O186/O188 remain closed.
- FULL178 remains inactive.
- No receiver, route, theorem, endpoint, or perfect-cuboid credit follows.
