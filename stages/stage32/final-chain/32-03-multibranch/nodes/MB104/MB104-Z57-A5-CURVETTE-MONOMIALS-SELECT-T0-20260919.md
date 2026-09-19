# MB104 Z57 — A5 curvette monomials select tangent type T0 — 2026-09-19

Status: **PRE-AUDIT EXACT TANGENT-BIT SELECTION / T0 PROVED / NO DOWNSTREAM CREDIT**

## Input

Z50/Z51 identify the canonical-cover resolution chain

```
E_L -- C1 -- C2 -- C3 -- C4 -- C5 -- E_R
```

with all self-intersections -2, elliptic endpoints, and fixed rational-double-point chain

```
Gamma=C1+...+C5
```

of Dynkin type A5.

The maximal ideal cycle is

```
F=(1,2,2,2,2,2,1).
```

Z54/Z55 reduce the tangent cone to

```
T0=(x^2,yz)
or
T1=(x^2,yz+xw).
```

Z56 identifies x as the first-normal tangent generator.

## 1. Contract only the A5 chain

Contract Gamma while leaving the two elliptic endpoint curves uncontracted.

By the analytic classification of rational double points, the resulting A5 germ has coordinates

```
u v = s^6.                                      (A5)
```

The strict transforms of the two endpoint elliptic curves meet opposite end components C1 and C5
transversely once.  Hence, after analytic coordinate choice, their images are the two opposite
curvettes

```
U: u=s=0,
V: v=s=0.
```

At a generic point of U, v is a unit and u=s^6/v, so

```
ord_U(s,u,v)=(1,6,0).
```

At V,

```
ord_V(s,u,v)=(1,0,6).
```

On the A5 exceptional chain the standard divisorial valuations are, after orienting C1 adjacent
to U,

```
ord_Ci(s)=1,
ord_Ci(u)=6-i,
ord_Ci(v)=i,
i=1,...,5.
```

Therefore the full seven-component valuation vectors are

```
val(s)  =(1,1,1,1,1,1,1),
val(u)  =(6,5,4,3,2,1,0),
val(v)  =(0,1,2,3,4,5,6).
```

They satisfy `val(u)+val(v)=6 val(s)`, as required by uv=s^6.

## 2. Four explicit functions descending to the final contraction

Consider

```
y = u s,
z = v s,
w = s^2,
x = s^3.
```

Their valuations are

```
val(y)=(7,6,5,4,3,2,1),
val(z)=(1,2,3,4,5,6,7),
val(w)=(2,2,2,2,2,2,2),
val(x)=(3,3,3,3,3,3,3).
```

Each vector dominates F, so all four functions vanish on every component contracted by the final
map.  They are therefore holomorphic functions on the final singularity germ.

None lies in `m^2`, because none of the four valuation vectors dominates

```
2F=(2,4,4,4,4,4,2).
```

Their leading restrictions are independent:

- y survives on the right arm;
- z survives on the left arm;
- w survives on the central reduced A5 strip;
- x is the unique first-normal direction of Z56.

Since `dim m/m^2=4`, their classes form a basis of the tangent space.

## 3. Quadratic products

The A5 equation gives exact identities

```
x^2 = s^6 = uv,
yz  = (us)(vs) = uv s^2 = s^8.
```

Now

```
3F=(3,6,6,6,6,6,3).
```

The valuation vectors are

```
val(s^6)=(6,6,6,6,6,6,6) >= 3F,
val(s^8)=(8,8,8,8,8,8,8) >= 3F.
```

Konno Lemma 5.6 for type (II), m=1 gives the maximal-ideal-adic identification

```
m^n = pi_* O_X(-nF)
```

for every n>0.

Hence

```
x^2 in m^3,
yz  in m^3.
```

Therefore in degree two of the associated graded ring,

```
in_2(x^2)=0,
in_2(yz)=0.
```

Since Z52 already proves that the tangent cone is a codimension-two complete intersection of two
quadrics, these are the two independent quadratic initial relations.

Thus

```
gr_m O
  has quadratic ideal (x^2,yz).
```

## 4. T0/T1 decision

Comparing with Z54,

```
T0=(x^2,yz),
T1=(x^2,yz+xw),
```

we obtain

```
actual tangent type = T0.
```

Equivalently:

```
DET_PENCIL_IDENTICALLY_ZERO = true,
rank-four tangent quadric exists = false,
embdim at the two-line intersection point = 3.
```

The mixed coefficient is exactly

```
c=0.
```

## 5. Why this is not a symmetry inference

No sign-change symmetry is used to force c=0.

The decision comes from:

1. the source-classified A5 fixed chain;
2. the standard analytic A5 equation uv=s^6;
3. the opposite-end curvette geometry of the actual elliptic endpoints;
4. explicit divisorial valuations;
5. Konno's exact identification of the m-adic filtration by nF.

## 6. New next interface

The tangent-cone ambiguity is closed.

The size48 canonical cover now has exact leading algebra

```
C[x,y,z,w]/(x^2,yz)
```

with total Milnor number 31.

The next useful task is not another tangent-cone classification.  It is to determine the first
higher-order terms that make the ICIS isolated and carry the canonical mu_3 action.

A bounded target is:

```
MB104-Z58-T0-HIGHER-JET-MU3-EQUIVARIANT-ICIS
```

Compute the defining relations modulo m^4/m^5 using the A5 monomial basis above and the deck
character.  Test whether this already determines the mu_3 representation on the Tjurina/Milnor
algebra sufficiently for a downstairs local correction.

## Firewalls

```
actual_tangent_type_T0=true
mixed_coefficient_c_zero=true
tangent_pencil_determinant_identically_zero=true
higher_order_ICIS_terms_known=false
mu3_vanishing_character_known=false
downstairs_local_correction_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
