# Stage15-6af — genuine two-point cross-resultant audit

Base: merged Stage15-6ae (`PR #837`, merge commit `dc570ee`). Stage15-6ae reduced the low-core branch, after all legal outer/core/gcd/orientation charges, to one primitive Gaussian parameter `z=a+ib` and the exact transfer

\[
T(z):=h_\alpha\bigl(m^2Y(z)+i n^2X(z)\bigr)=mn h_\beta K_\beta w^2,
\]

where

\[
K_\alpha z^2=X(z)+iY(z).
\]

Stage15-6af asks only whether this one-point receiver contains a new exact factorization or whether two distinct retained points expose a genuine shared-prime resultant. It does not open a genus-one/character route and does not derive a new global thinning exponent.

## 1. Frozen verdict

There is no new one-point spacing modulus. The useful new structure appears only after introducing two distinct primitive retained points `z_1,z_2` in the same fixed physical outer/core/gcd/orientation fiber.

Write

\[
U_j:=K_\alpha z_j^2=X_j+iY_j,
\qquad
T_j:=T(z_j)=h_\alpha(m^2Y_j+i n^2X_j).
\]

The transfer-coordinate determinant is

\[
\Delta_T(T_1,T_2)
:=\det\begin{pmatrix}m^2Y_1&m^2Y_2\\ n^2X_1&n^2X_2\end{pmatrix}
=m^2n^2(Y_1X_2-Y_2X_1).
\]

Since multiplication by the fixed `K_alpha` scales oriented area by `N(K_alpha)=k`,

\[
Y_1X_2-Y_2X_1
=-k\,\Im(\overline{z_1^2}z_2^2).
\]

Put

\[
L_+(z_1,z_2):=a_1a_2+b_1b_2=\Re(\overline z_1z_2),
\]

\[
L_-(z_1,z_2):=a_1b_2-b_1a_2=\Im(\overline z_1z_2).
\]

Then

\[
\Im(\overline{z_1^2}z_2^2)=2L_+L_-,
\]

hence the exact factorization

\[
\boxed{
\Delta_T(T_1,T_2)=-2m^2n^2k\,L_+(z_1,z_2)L_-(z_1,z_2).
}
\]

This is genuine cross-point information: `L_+` and `L_-` depend on two distinct retained points and are not private moduli manufactured from one point.

## 2. Shared Gaussian primes transfer to the cross-resultant

Let `pi` be a Gaussian prime of odd rational norm `p`, with

\[
p\nmid 2mnkh_\alpha.
\]

If the same Gaussian orientation `pi` divides both transfer values `T_1,T_2`, then the two transfer coordinate vectors are linearly dependent modulo `p`, so

\[
p\mid\Delta_T(T_1,T_2).
\]

By the factorization above,

\[
\boxed{p\mid L_+(z_1,z_2)L_-(z_1,z_2).}
\]

Thus every good shared transfer prime must be paid for by one of two explicit bilinear cross-resultants. Bad primes dividing the fixed coefficient package `2mnkh_alpha` are outer data and are not a new spacing source.

The same conclusion applies to the conjugate/cross-role case after replacing one transfer value by its Gaussian conjugate: the relevant determinant becomes the corresponding same-role/cross-role resultant already anticipated by Arsenal AR-017. Stage15-6af records the exact Stage15 factorization but does not convert it into an energy saving.

## 3. Degenerate branches are exact and visible

The two factors have clear geometry:

- `L_-=0` iff the primitive vectors `(a_1,b_1)` and `(a_2,b_2)` are rationally proportional; with primitive sign conventions this is a finite diagonal/antipodal coincidence branch.
- `L_+=0` iff they are orthogonal, equivalently `z_2` is a rational multiple of `i z_1`; under primitive sign conventions this is another finite rotation branch.

Therefore the resultant is not identically zero on genuinely distinct nonparallel/nonorthogonal pairs. These degenerate branches must be separated before any pair-energy estimate, not hidden inside a generic determinant bound.

## 4. Arsenal verdict

`AR-017` is now genuinely triggered in its two-point role:

```text
AR-017=EXACT_STAGE15_CROSS_RESULTANT_ADAPTER_PROVED_ENERGY_COUNT_OPEN
```

The exact adapter is the shared-prime implication

```text
shared good Gaussian prime between two transfer values
-> p divides Delta_T
-> p divides 2*m^2*n^2*k*L_plus*L_minus
-> after removing fixed coefficient primes, p divides L_plus*L_minus.
```

`AR-028` remains active: a prime is charged once, through the shared-prime/cross-resultant relation. It may not also be counted as an independent private modulus of either point.

`AR-016` applies only to fixed coefficient-prime and finite orientation decorations. `AR-009` is not reactivated pointwise on the low-core branch. `AR-010` remains consumed. `AR-012/013/014` remain untriggered/not needed.

## 5. What Stage15-6af does not prove

The factorization does not by itself bound the number of pairs sharing primes. In particular Stage15-6af does not prove:

- a pair-energy estimate;
- low-core negligibility;
- a low-core square-root bound;
- a self-contained recovery of Stage15-5;
- a strict sub-square-root numerator bound;
- a matching survival exponent.

The new object is an exact energy receiver, not an automatic saving.

## 6. Frozen exit

```text
STAGE15_6_SUBSTAGE=6af
STAGE15_6AF_ONE_POINT_NEW_FACTOR_MODULUS=false
STAGE15_6AF_TWO_POINT_CROSS_RESULTANT=true
STAGE15_6AF_TRANSFER_DETERMINANT_FACTORIZATION=true
STAGE15_6AF_CROSS_FACTORS=LPLUS_DOT,LIMINUS_DETERMINANT
STAGE15_6AF_SHARED_GOOD_PRIME_TRANSFERS_TO_CROSS_RESULTANT=true
STAGE15_6AF_DEGENERATE_PARALLEL_ORTHOGONAL_BRANCHES_IDENTIFIED=true
STAGE15_6AF_AR017_EXACT_STAGE15_CROSS_RESULTANT_ADAPTER=true
STAGE15_6AF_PAIR_ENERGY_BOUND_PROVED=false
STAGE15_6AF_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AF_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AF_EXIT=GENUINE_TWO_POINT_CROSS_RESULTANT_RECEIVER_READY
```

## 7. Next narrow gate

Stage15-6ag should count the new two-point receiver in the same physical outer fiber: separate `L_+=0` and `L_-=0`, then ask whether shared-prime mass can be bounded through the product `L_+L_-` without recharging private Gaussian roots. Only if that exact pair-energy gate fails should a new analytic theorem species be opened.
