# Stage29-15 post-Work audit — `R29-K3-RULED2` bounded execution

This file records the renewed audit's mandatory class challenge for the Creutz--Viray ruled-double-cover receiver.  It sharpens the provisional class-2 wall without promoting the receiver beyond what is actually materialized.

## 1. Exact `K_c` model already in the repository

The audited coordinate-sign quotient `K_c` is the smooth K3 resolution of the normal complete intersection with coordinates

```text
(a1,a2,a3,b1,b2,b3)
```

and equations

```text
b1^2 = a2^2+a3^2,
b2^2 = a1^2+a3^2,
b3^2 = a1^2+a2^2.
```

Forgetting `b1` gives exactly the two-face degree-four surface used in Stage29-07:

```text
T2bar : e^2+x^2=p^2,
        e^2+y^2=q^2
```

under

```text
e=a1, x=a3, y=a2, p=b2, q=b3.
```

The remaining quadratic extension is

```text
b1^2=x^2+y^2.
```

Thus `K_c` is not merely cohomologically related to the Stage29-07 two-face floor: its function field is the literal third-face quadratic extension of that floor.

## 2. Explicit geometrically ruled base

Stage29-07 gives the rational anticanonical parametrization of `T2bar` from `P1 x P1`.  Write

```text
A1=v1^2-u1^2,
A2=v2^2-u2^2,

e=A1*A2,
x=2*u1*v1*A2,
y=2*u2*v2*A1,
p=(u1^2+v1^2)*A2,
q=(u2^2+v2^2)*A1.
```

Pulling back the quadratic extension and dividing the square factor `4` gives the Q-defined double-cover function field

```text
w^2 = F,
F = (u1*v1*A2)^2 + (u2*v2*A1)^2.
```

Here `F` is a bihomogeneous `(4,4)` form on

```text
S0 = P1 x P1,
```

which is a geometrically ruled rational surface over either factor.  This supplies the explicit ruled model that the post-Work submission had left as the first class-2 wall.

## 3. Branch divisor: reduced, flat, simple singularities

Over `Q(i)` the branch divisor factors as

```text
B0 = B+ union B-,
B+ : u1*v1*A2 + i*u2*v2*A1 = 0,
B- : u1*v1*A2 - i*u2*v2*A1 = 0.
```

Each component has bidegree `(2,2)`.

On the affine chart `v1=v2=1`, put `t=u1`, `s=u2`.  A component has equation

```text
G_e(t,s)=t*(1-s^2) + e*i*s*(1-t^2),  e in {+1,-1}.
```

If `G_e=G_e,t=G_e,s=0`, then

```text
G_e - t*G_e,t = e*i*s*(1+t^2)=0,
G_e - s*G_e,s = t*(1+s^2)=0.
```

The cases `t=0` or `s=0` immediately contradict one of the first derivatives.  Otherwise `t^2=s^2=-1`; substituting into a derivative would require `st` to be `+- i`, whereas `t,s in {+- i}` give `st in {+-1}`.  Hence there is no singular point on this chart.  The three reciprocal charts have the same calculation after `t -> 1/t` and/or `s -> 1/s`, so both `B+` and `B-` are smooth globally.

Their intersection is the simultaneous zero locus of

```text
X=u1*v1*A2,
Y=u2*v2*A1.
```

It consists of exactly eight points:

- four points `A1=A2=0`, i.e. `(u1:v1)=(+-1:1)` and `(u2:v2)=(+-1:1)`;
- four corner points with `u1*v1=u2*v2=0`.

At the four finite `A1=A2=0` points, in local coordinates the Jacobian determinant of `(X,Y)` is `-4`; at `(t,s)=(0,0)` it is `1`, and the other three corners are identical in reciprocal charts.  Thus all eight intersections are transverse ordinary nodes.

Consequently

```text
BRANCH_REDUCED=true
BRANCH_GEOMETRIC_COMPONENTS=2
BRANCH_COMPONENT_TYPES=(2,2)+(2,2)
BRANCH_INTERSECTION_NODES=8
BRANCH_AT_WORST_SIMPLE_SINGULARITIES=true
```

No component is a ruling fiber; hence the branch Cartier divisor is flat over either `P1` ruling.

## 4. Creutz--Viray theorem application

Creutz--Viray, *On Brauer groups of double covers of ruled surfaces*, Theorem I / Corollary 5.4 applies to a desingularization of this double cover: the base is geometrically ruled, the branch is reduced and flat, and its singularities are simple.

For the dimension check, Corollary 6.3 / Example 6.4 applies to a `(4,4)` double cover of `P1 x P1`.  The audited Stage29-02e coordinate-eigenspace argument gives

```text
rank T(K_c)=2,
rank NS(K_c)=20.
```

Therefore

```text
dim_F2 Br(K_c_Qbar)[2]
 = 22-rank NS(K_c)
 = 2.
```

This is consistent with the known singular-K3 transcendental rank and is now independently recovered from the ruled-double-cover theorem.

```text
KC_RULED_MODEL=DISCHARGED_EXPLICIT_P1xP1_4_4_MODEL
KC_BRANCH_HYPOTHESES=DISCHARGED
KC_GEOMETRIC_BR2_DIMENSION=2
```

## 5. Why the full receiver remains class 2

The post-Work receiver was deliberately stronger than a dimension computation: it asks for the **explicit finite Creutz--Viray presentation** needed for arithmetic use, including central-simple-algebra representatives and the Q/Galois action.

The theorem presents `Br(K_c_Qbar)[2]` as the quotient of `L_{c,E}` by the image of the `x-alpha` map from the Neron--Severi group.  The repository does not yet contain, on this chosen `(4,4)` ruled model,

```text
- an explicit basis of L_{c,E},
- the x-alpha relation matrix for a certified NS(K_c) basis,
- two explicit surviving symbol representatives,
- the Q(i)/Q Galois action on those representatives,
- local evaluation on the physical endpoint lift image.
```

The first two geometric prerequisites are now executed; the remaining wall is a finite explicit divisor/NS/symbol computation.  It is not a theorem gate.

```text
R29-K3-RULED2=2_CURRENT_TOOL_LIMIT_EXECUTED
R29-K3-RULED2_CORE=DISCHARGED_RULED_MODEL_BRANCH_AND_GEOMETRIC_BR2_DIMENSION
EXACT_REMAINING_LIMIT=CV_LCE_AND_XALPHA_RELATION_MATRIX_PLUS_EXPLICIT_SYMBOL_BASIS_AND_Q_GALOIS_ACTION
NEW_THEOREM_REQUIRED=false
ENDPOINT_OBSTRUCTION_PROVED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
