# Stage14-t150 — fixed-residue Gaussian annulus lattice count

## Status

`COMPLETE_FIXED_RESIDUE_GAUSSIAN_ANNULUS_LATTICE_COUNT`

Consumes merged `Stage14-t149`, the exact fixed-residue cofactor formulation from merged `Stage14-t135`, and merged `Stage14-Work-bzX38` from latest main.

The entering endpoint branches already have actual primitive Gaussian cofactors

```text
z in Z[i],
z in one fixed strict broad sector S,
z == rho_* (mod d),
d odd squarefree,
```

and a fixed ordinary prime residue modulo the same selector modulus `d`.

Stages t140--t149 counted the cofactor annulus by first counting possible scalar norms and then using a `B^o(1)` representation bound per norm.  That is safe but loses the fact that the actual cofactors already lie in one two-dimensional lattice coset.  This stage counts that coset directly.

## 1. Exact endpoint-to-norm map

Put

```text
L_B = 2*sqrt(B),
X_U = 2B/(h*k0),
n(H) = X_U/(L_B+H).
```

Thus for a cofactor `z` with endpoint width

```text
H(z)=X_U/N(z)-L_B,
```

we have exactly

```text
N(z)=n(H(z)).
```

Differentiate:

```text
|n'(H)|
 = X_U/(L_B+H)^2
 <= X_U/L_B^2
 = 1/(2*h*k0).
```

Therefore for one dyadic width layer

```text
Z(Y)={z:Y<H(z)<=2Y}
```

the scalar norms `N(z)` lie in an interval of length

```text
Delta_n(Y) <= Y/(2*h*k0).                         (1.1)
```

This derivative estimate is global for `H>=0`; it does not require the auxiliary `H<=sqrt(B)` simplification used in t140.

Also

```text
N(z) <= N_0:=sqrt(B)/(h*k0),
```

so every live endpoint cofactor lies in the disk of radius

```text
r_0:=sqrt(N_0)=B^(1/4)/sqrt(h*k0).                 (1.2)
```

```text
ENDPOINT_NORM_MAP_EXACT=true
ENDPOINT_DYADIC_NORM_THICKNESS_LE_Y_OVER_2HK0=true
ENDPOINT_COFACTOR_RADIUS_LE_BQUARTER_OVER_SQRTHK0=true
```

## 2. The cofactor set is one translated Gaussian lattice

Because `z==rho_* (mod d)`, every cofactor lies in the affine lattice

```text
rho_* + d*Z[i].
```

Its covolume in `R^2` is exactly `d^2`.

Let `A_Y` be the planar annular-sector region obtained by imposing only

```text
Y<H(z)<=2Y,
z in the fixed broad sector S.
```

The primitivity condition and every frozen exceptional/local packet are additional filters, so

```text
#Z(Y)
 <= #((rho_*+d Z[i]) intersect A_Y).               (2.1)
```

The annular-sector area satisfies

```text
area(A_Y) = O(Delta_n(Y))
          = O(Y/(h*k0)),                           (2.2)
```

because planar area between squared radii `n_1,n_2` is a fixed sector fraction times `n_1-n_2`.

Its boundary length is

```text
perimeter(A_Y)=O(r_0)                              (2.3)
```

for the fixed sector: two circular arcs and two radial sides, all inside radius `r_0`.

An elementary square-covering count for a translated lattice of spacing `d` gives, for any such bounded planar region,

```text
#((rho_*+d Z[i]) intersect A_Y)
 <= C_S*( area(A_Y)/d^2
          + perimeter(A_Y)/d
          + 1 ).                                  (2.4)
```

Combining (1.1)--(2.4),

```text
boxed:
#Z(Y)
 <= C_S*(
      Y/(h*k0*d^2)
      + B^(1/4)/(d*sqrt(h*k0))
      + 1 ).                                      (2.5)
```

The constant depends only on the already-fixed broad sector convention.  No divisor-function or `r_2(n)` factor appears.

```text
FIXED_RESIDUE_COFACTOR_IS_SINGLE_AFFINE_GAUSSIAN_LATTICE=true
GAUSSIAN_ANNULUS_LATTICE_AREA_TERM=Y_over_hk0_d2
GAUSSIAN_ANNULUS_LATTICE_BOUNDARY_TERM=Bquarter_over_d_sqrtHK0
GAUSSIAN_ANNULUS_LATTICE_SINGLETON_TERM=1
PER_NORM_BO1_REPRESENTATION_LOSS_REMOVED=true
```

## 3. Relation to t148 sparse/many split

The t148 split remains logically valid, but (2.5) is strictly more geometric:

- the old `B^o(1)*(Y/(h*k0)+1)` bound ignored the fixed cofactor residue;
- the area term now receives an additional exact `d^-2` lattice-density factor;
- the only cost of a very thin annulus is the explicit boundary term `B^(1/4)/(d*sqrt(h*k0))`, not an opaque representation entropy.

Thus later capacity accounting can distinguish the true two-dimensional annulus area from its one-dimensional lattice-boundary error.

This stage is a coordinate/capacity refinement.  The material receiver change is deferred until the prime-residue denominator is combined with (2.5) and the principal-scale consequences are localized.

```text
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH33_NEEDED=false
NEXT_INTERNAL_TARGET=DoubleResidueNormalizedGaussianAnnulusPrincipalCapacity
NEXT=Stage14-t151
```
