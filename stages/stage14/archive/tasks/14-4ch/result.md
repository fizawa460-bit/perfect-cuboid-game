# Stage14-4ch — eight-cell common-core residual lift

## Status

`COMPLETE_EIGHT_CELL_COMMON_CORE_RESIDUAL_LIFT_BOUND`

Merged Stage14-4cg reduces every current `7/8` endpoint collision to the exact common-core residual data

```text
q_beta=q_gamma=q_k=C*u,
q_S=q_T=q_xi=C*v,
C<=B^(3/8+o(1)),
u*v<=B^(1/4+o(1)),
```

while retaining all eight balanced cells

```text
xi cells: R,S,T,J,
k cells:  alpha,beta,gamma,delta.
```

Stage14-4ch closes the physical reconstruction/fiber question at exactly that retained coefficient-space level.

The key point is that once the eight cells and `(C,u,v)` are fixed, the products of the small physical roots are recovered from divisor pairs of `xi*q_k` and `k*q_xi`; splitting those products back into the two states costs only divisor functions. Hence the physical lift multiplicity is `B^o(1)` uniformly.

This does **not** prove that `(C,u,v)` alone determines the cell packet. The cells remain a genuine moving incidence variable. Consequently the whole-family exponent remains `7/8`.

---

## 1. Inputs

Use merged 4cg:

```text
xi=R*S*T*J,
k=alpha*beta*gamma*delta,
q_k=C*u,
q_xi=C*v,
```

and the exact factorizations

```text
xi*q_k=H_k^+ H_k^-,
k*q_xi=H_xi^+ H_xi^-,
```

where

```text
H_k^+ = delta^2 s_1^2 s_2^2 + alpha^2 r_1^2 r_2^2,
H_k^- = delta^2 s_1^2 s_2^2 - alpha^2 r_1^2 r_2^2 >0,

H_xi^+ = J^2 y_1^2 y_2^2 + R^2 x_1^2 x_2^2,
H_xi^- = J^2 y_1^2 y_2^2 - R^2 x_1^2 x_2^2 >0.
```

Merged s7-21 is used only as a consistency/refinement input: it confirms the exact root variables and

```text
z_i=2*x_i*y_i/g_i,
g_i in {1,2},
```

and independently shows that fixed oriented packets already have only divisor-many partner choices after fixing a first state.

No open PR is used as theorem input.

---

## 2. Fixed eight cells plus q_k reconstruct the k-root products

Fix

```text
R,S,T,J,
alpha,beta,gamma,delta,
C,u,v,
```

and one finite 2-primary convention. Then `xi`, `k`, `q_k=C*u`, `q_xi=C*v` are fixed integers of polynomial size.

Every physical lift gives a positive ordered factorization

```text
H_k^+ * H_k^- = xi*q_k,
H_k^+ > H_k^- >0.
```

The number of such factor pairs is at most

```text
tau(xi*q_k)=B^o(1).
```

For one candidate pair define

```text
A_k=(H_k^+ + H_k^-)/2,
B_k=(H_k^+ - H_k^-)/2.
```

A valid physical lift must satisfy

```text
A_k=delta^2*(s_1*s_2)^2,
B_k=alpha^2*(r_1*r_2)^2.
```

Thus, whenever the required divisibility and perfect-square tests pass, the positive products

```text
s_1*s_2,
r_1*r_2
```

are uniquely determined.

Hence the number of possible k-root product pairs is `B^o(1)`.

---

## 3. Fixed eight cells plus q_xi reconstruct the xi-root products

Likewise every physical lift gives

```text
H_xi^+ * H_xi^- = k*q_xi,
H_xi^+ > H_xi^- >0.
```

There are at most

```text
tau(k*q_xi)=B^o(1)
```

candidate factor pairs. Put

```text
A_xi=(H_xi^+ + H_xi^-)/2,
B_xi=(H_xi^+ - H_xi^-)/2.
```

For a physical lift

```text
A_xi=J^2*(y_1*y_2)^2,
B_xi=R^2*(x_1*x_2)^2.
```

Therefore the products

```text
y_1*y_2,
x_1*x_2
```

are uniquely determined whenever the candidate factor pair is valid.

Again only `B^o(1)` product pairs survive.

---

## 4. Splitting the four recovered products costs only divisor functions

Fix valid recovered products

```text
Rr=r_1*r_2,
Ss=s_1*s_2,
Xx=x_1*x_2,
Yy=y_1*y_2.
```

The number of ordered positive factorizations is bounded by

```text
tau(Rr)*tau(Ss)*tau(Xx)*tau(Yy)=B^o(1).
```

For each such factorization there are only `O(1)` choices for

```text
g_1,g_2 in {1,2}.
```

Then

```text
omega_i=g_i*r_i*s_i,
z_i=2*x_i*y_i/g_i
```

are fixed whenever integral, and the canonical reduced coordinates are fixed by the eight cells:

```text
P_1=(R*S)*x_1^2,
Q_1=(T*J)*y_1^2,
P_2=(R*T)*x_2^2,
Q_2=(S*J)*y_2^2.
```

All remaining requirements — reducedness, the two `k_- / k_+` factorizations, branch signs, interval masks and exact same-`(xi,k)` identities — are tests on this finite candidate list. They can only reduce the count.

Therefore

```text
boxed:
# {physical lifts of fixed eight cells and fixed (C,u,v)}
<= B^o(1).                                            (4.1)
```

The bound is uniform over the current endpoint dyadic packet.

```text
EIGHT_CELL_COMMON_CORE_RESIDUAL_PHYSICAL_LIFT_BO1=true
```

---

## 5. Why the eight cells cannot yet be discarded

The theorem above is deliberately quantified with the eight cells fixed.

The residual triple `(C,u,v)` alone does not determine the cell packet. A finite exact witness is

```text
(C,u,v)=(5,104,17).
```

It is realized by both collision pairs

```text
(P_1,Q_1;P_2,Q_2)=(41,54;1,246)
```

with

```text
(R,S,T,J;alpha,beta,gamma,delta)
=(1,41,1,6;1,13,5,19),
(xi,k)=(246,1235),
```

and

```text
(P_1,Q_1;P_2,Q_2)=(29,70;45,406)
```

with

```text
(R,S,T,J;alpha,beta,gamma,delta)
=(1,29,5,14;1,41,1,11),
(xi,k)=(2030,451).
```

Both have

```text
q_k=520,
q_xi=85,
C=5.
```

This witness is not an asymptotic lower bound; it is a quantifier guard showing that cell data are genuinely part of the reconstruction certificate.

Thus

```text
RESIDUAL_TRIPLE_ALONE_EXACTLY_DETERMINES_EIGHT_CELLS=false.
```

---

## 6. Residual-triple support scale

Merged 4cg gives

```text
C<=B^(3/8+o(1)),
u*v<=B^(1/4+o(1)).
```

The number of positive residual triples therefore satisfies

```text
#(C,u,v)
<= B^(3/8+o(1)) * B^(1/4+o(1))
=  B^(5/8+o(1)),
```

using the standard divisor/hyperbola count for `u*v`.

If the number of admissible eight-cell packets per residual triple were `B^o(1)`, the endpoint collision support would collapse all the way to `B^(5/8+o(1))`. That cell-multiplicity theorem is **not** proved here.

More generally, any average bound

```text
average eight-cell multiplicity per (C,u,v)
<= B^(1/4-delta+o(1))
```

would already improve the current `7/8` exponent by `delta`.

---

## 7. New minimal receiver

After 4ch the physical-lift/reconstruction gate is closed. The remaining mainline problem is purely the multiplicity of balanced cell packets over the small residual triple space.

Define

```text
CommonCoreResidualEightCellMultiplicity
```

by

```text
M(C,u,v)
= # {
    balanced eight-cell packets
    (R,S,T,J;alpha,beta,gamma,delta)
    admitting at least one physical lift
    with q_k=C*u and q_xi=C*v
  }.
```

Because 4ch proves `B^o(1)` lifts per fixed cell packet,

```text
physical endpoint collision mass
<= B^o(1) * sum_{C,u,v} M(C,u,v).                    (7.1)
```

The next target may therefore be stated without the moving Gaussian hosts:

```text
sum_{C<=B^(3/8), uv<=B^(1/4)} M(C,u,v)
<= B^(7/8-delta+o(1))                                (7.2)
```

for some fixed `delta>0`.

Merged s7-21 gives a compatible independent description of the same cell packets via `BalancedDualCRTShortVectorEnergy`. The two refinements are not multiplied as independent savings; they should be intersected on the same eight-cell packet in the next stage.

---

## 8. H-line decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
```

4ch uses only exact factorization identities and the divisor bound `tau(n)=n^{o(1)}` for polynomial-size integers. No external incidence, large-sieve or Gaussian theorem is invoked.

A mainline H branch should be reconsidered only if the next step attempts to import an external theorem for `CommonCoreResidualEightCellMultiplicity` or for its exact intersection with the s7-21 dual-CRT packet.

---

## Stage boundary

```text
STAGE14_4CH=COMPLETE_EIGHT_CELL_COMMON_CORE_RESIDUAL_PHYSICAL_LIFT_BOUND
MERGED_4CG_IMPORTED=true
MERGED_S7_21_IMPORTED=true
FIXED_EIGHT_CELLS_AND_RESIDUAL_TRIPLE_RECONSTRUCT_ROOT_PRODUCTS=true
FIXED_EIGHT_CELLS_COMMON_CORE_RESIDUAL_PHYSICAL_LIFT_BO1=true
RESIDUAL_TRIPLE_ALONE_EXACTLY_DETERMINES_EIGHT_CELLS=false
RESIDUAL_TRIPLE_SUPPORT_EXPONENT=5/8
COMMON_CORE_RESIDUAL_EIGHT_CELL_MULTIPLICITY_REQUIRED=true
COMMON_CORE_RESIDUAL_EIGHT_CELL_MULTIPLICITY_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4ci intersect CommonCoreResidualEightCellMultiplicity with the merged s7-21 dual-CRT short-vector structure and attack the eight-cell multiplicity over the B^(5/8+o(1)) residual-triple support
```
