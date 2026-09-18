# Stage32 MB104 — W4 third-depth solo: exact K3 root-wall closure — 2026-09-18

Status: W4 THIRD-DEPTH COMPLETE / ROOT-WALL ROUTE CLOSED NEGATIVELY / NO MB104 CREDIT

## Scope

This checkpoint deepens W4 only. W5, W20 and W16 are intentionally not advanced here.

The primitive coordinate-quotient pushdown P has H_K^2=8, H_K.P=112 and squares:
a1 1344; a2 1344; a3 1376; b1 1152; b2 1152; b3 736; c 1312.

## Universal root-degree bound

Put V=P-14H_K. Then H_K.V=0 and V^2=P^2-1568=-M.
For an effective (-2)-curve R of positive hyperplane degree d=H_K.R, put W=R-(d/8)H_K.
Inside the negative-definite H_K-perpendicular space, -W^2=2+d^2/8 and -V^2=M.
If P.R<0, then |V.W|>14d. Cauchy-Schwarz therefore gives

d^2 < 16(1568-P^2)/P^2.

The exact bounds are:
a1,a2: d^2<8/3; a3: d^2<96/43; b1,b2: d^2<52/9; b3: d^2<416/23; c: d^2<128/41.

Exceptional roots have d=0 and nonnegative intersection with P.

## K_c-type quotients: a1,a2,a3,c

Stoll-Testa Section 6 and the immutable verification source construct Pic(K_c) of rank 20 and prove every Picard class has even hyperplane degree. The K_a quotients are isomorphic to K_c over the stated source-field extension.
All four root-degree bounds force d<2. No positive even d exists, so no effective (-2)-root has negative intersection with the a1,a2,a3,c pushdowns.

Important correction: the rank-20 K_c lattice must not be silently used for the K_b quotients. The paper states only that the three K_bj are mutually isomorphic; they are a different quotient type.

## K_b has no lines

Use K_b1 coordinates (a1,a2,a3,b2,b3,c) with equations
b3^2=a1^2+a2^2, b2^2=a1^2+a3^2, c^2=a1^2+a2^2+a3^2.

For linear forms u,v,w on a hypothetical line, w^2=u^2+v^2 factors as (u+iv)(u-iv)=w^2 in C[s,t]. Unique factorization forces u,v,w to be proportional.
Apply this to (a1,a2,b3) and (a1,a3,b2). If a1 is nonzero, all first five coordinates are proportional and then so is c. If a1 is zero, b3=+-a2 and b2=+-a3, and applying the same factorization to c^2=a2^2+a3^2 again makes all coordinates proportional.
Either case gives a constant projective map, so K_b contains no degree-one integral curve.

## b1 and b2

The degree bound leaves only d=1 or2. The no-line lemma removes d=1.
The exact support projection to either quotient has nonzero singular-node weights 2,2,2,1, of total weight 7.
An integral degree-two curve is a smooth conic, hence has exceptional multiplicity one at each node it meets. Therefore P.R >= 28-4*7 = 0.
No negative root exists for b1 or b2.

## b3 special hyperplane

Use K_b3 coordinates (a1,a2,a3,b1,b2,c) with equations
b1^2=a2^2+a3^2, b2^2=a1^2+a3^2, c^2=a1^2+a2^2+a3^2.

The active support projects to eight weighted singular points of weights 2,2,2,2,2,1,2,1. Exact node replay shows all eight lie on
L: c-a1-a2-i*a3=0.

For any integral curve not contained in L, the pullback of L gives sum R.E_q <= d over the weighted nodes. Since every weight is at most 2, sum n_q(R.E_q)<=2d, so P.R>=14d-8d=6d>0.

Inside L, substituting c=a1+a2+i*a3 factors the third equation as
a1^2+a2^2+a3^2-c^2 = -2(a1+i*a3)(a2+i*a3).

The reduced support of K_b3 intersect L is exactly two smooth conics:
Q_A: a1+i*a3=0, b2=0, c=a2, b1^2=a2^2+a3^2;
Q_B: a2+i*a3=0, b1=0, c=a1, b2^2=a1^2+a3^2.

The weighted-node mass on each conic is exactly 7, so P.Q_A=P.Q_B=28-4*7=0.
Thus b3 has no negative root wall either.

## W4 final disposition

All seven primitive coordinate pushdown rays are nonnegative on every effective (-2)-root relevant to the root-wall test.
The proposed all-l fixed-component obstruction therefore does not exist.

W4 THIRD-DEPTH DISPOSITION = CLOSED_NEGATIVE.

This closes only W4. It does not prove existence of a carrier, MB104 closure, a finite degree window, receiver/effectivity/theorem/endpoint credit, or any Perfect-Cuboid claim. No merge is authorized.

Remaining user-selected solo routes: W5, W20, W16.
