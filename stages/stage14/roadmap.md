# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain primitive canonical exactly-two-face cuboids with integer space diagonal under `d<=B`.

## Completed foundation

- `14-1`: definition/counting interface.
- `14-2`: two independent exact finite enumerators through `B=2,000,000`.
- `14-3`: finite directional reconnaissance only.
- `14-4aa`: common shared-edge parametrization.
- `14-4ab`: exact face-pair bijection, multiplicity one.
- `14-4ac`: rational slope/lcm height envelope.
- `14-4ad`: elliptic reduction `E_t:Y^2=X(X-1)(X+t^2)`.
- `14-4ae`: physical fiber height `v asymp sqrt(Bg/S1)` and generic rank zero.
- `14-4af`: actual Pythagorean base is a six-`I4` K3; torsion is nonphysical; physical pair implies positive rank; fixed-base triple genus 5.

Frozen Stage13 upstream remains `R03 + Stage13-12ag`, in particular

\[
N_2(B)=o(B(\log B)^3),
\]

with no imported growing-modulus power saving.

## 14-4ag — Kummer identification and rank-jump graph

Status: [x] Complete.

### Exact geometry

For the Pythagorean Euclid parameter `r`,

\[
t=\frac{2r}{1-r^2},
\qquad
\boxed{\sigma=i\frac{1+r}{1-r}}
\]

identifies the Stage14 K3 over `Q(i)` with the classical level-4 elliptic modular surface. Over `C` it is `Km(E_i x E_i)`.

The symmetric two-face model is

\[
\boxed{Z^2=(1+r^2)^2(1+s^2)^2-16r^2s^2.}
\]

### Exact active graph

Let `V(B)` be the number of active primitive oriented first-face states and `E(B)` the raw-pair edge count. Then

\[
\boxed{E(B)=N_2(B)+3T(B)=\frac12V(B)\bar d(B)}
\]

and

\[
\boxed{N_2(B)=\frac12V(B)\bar d(B)-3T(B).}
\]

Active vertices are exactly positive-rank genuine Pythagorean specializations ordered by their first physical hit height.

### Uniform multiplicity theorem

Dujella's bounded-height theorem applies to every Stage14 fiber because it has rational 2-torsion. Physical `d<=B` gives elliptic point height `B^O(1)`, hence uniformly

\[
\boxed{\Delta(B)=\max_F\deg_B(F)=B^{o(1)}.}
\]

Therefore raw edges and active vertices have identical polynomial growth exponents.

### Finite signal

At `B=200k,500k,1m,2m`, active vertex counts are

```text
155, 254, 347, 490
```

and `V(B)/sqrt(B)` is

```text
0.34659, 0.35921, 0.34700, 0.34648.
```

The `200k -> 2m` effective vertex exponent is

```text
0.4998643818582221
```

but this remains finite evidence.

Decision:

```text
STAGE14_4AG=COMPLETE
LEVEL4_MODULAR_K3_IDENTIFIED_OVER_QI=true
KUMMER_EI_SELF_PRODUCT_GEOMETRY_IMPORTED=true
RANK_JUMP_GRAPH_IDENTITY_LOCKED=true
DUJELLA_SUBPOLYNOMIAL_DEGREE_BOUND=true
RAW_PAIR_AND_ACTIVE_VERTEX_POWER_EXPONENT_EQUAL=true
FINITE_ACTIVE_VERTEX_SQRTB_SIGNAL=true
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
T_O_SQRT_B_PROVED=false
```

## 14-4ah — Kummer height / accumulating multisections + relative triple thinness

Status: [>] Next.

Purpose:

- identify the Stage14 primitive/lcm physical height as a divisor/height on the level-4 Kummer surface;
- classify the low-degree rational curves or multisections that can create small first-hit points;
- test whether the finite `sqrt(B)` active-vertex signal is explained by accumulating Kummer strata rather than generic rank-jump heuristics;
- use McKinnon's product-Kummer counting framework only after the physical height is matched;
- express the triple condition as a relative degree-two cover of the Kummer surface and seek a bound strong enough to compare `T(B)` with the raw count;
- promote a `sqrt(B)` power law only after the active-vertex count is proved.

## 14-5 — Directionwise asymptotic structure

Status: pending Stage14-4.

## Scope boundary

No true Stage14 growth exponent, leading constant, limiting directional vector, perfect-cuboid existence/nonexistence theorem, or `T=o(sqrt(B))` theorem is established yet.

```text
NEXT=Stage14-4ah Kummer height/accumulating-multisection and relative triple-thin analysis
```
