# Stage14-4bc — import s5p/s5q and freeze the final local transition kernel

## Result

Merged Stage14-4bb left two reciprocal-local gates:

```text
AUXILIARY_INCIDENCE_UNIFORMITY
+ STATE_SPLIT_E_MULTI_EDGE_ASSEMBLY.
```

Merged Stage14-s5p closes the auxiliary-progression gate. Merged Stage14-s5q then closes the multi-edge tensor-contraction problem itself and proves the exact E-column Walsh collapse.

Therefore the complete local Fourier polynomial is no longer blocked by auxiliary moduli, K4/K5 graph degree, state-label multiplicity, or split-E tensor multiplicity. It is reduced to one scalar signed-root linear--E edge.

The only remaining reciprocal-local analytic object is the explicit **root-sawtooth reciprocal kernel** isolated by s5q.

Stage14-4bc imports these two theorems into the 14-4 mainline, freezes the exact transition atlas, and separates the already-saved region from the final hybrid-estimate band.

## 1. Imported s5p closure

Stage14-s5p proves

```text
AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true
AUXILIARY_PROGRESSION_MODULUS_LOSS_PERSISTS=false
AUXILIARY_STATE_ENERGY_TRANSFER_PROVED=true
HILBERT_QUADRATIC_LARGE_SIEVE_LIFT_PROVED=true.
```

Hence frozen state labels and progression moduli introduce no positive power loss. There is no remaining `delta_aux` parameter.

## 2. Imported s5q tensor closure

Stage14-s5q proves

```text
MULTI_EDGE_DISCREPANCY_TENSOR_CONTRACTION_PROVED=true
LINEAR_ONLY_FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true
STATE_SPLIT_E_TENSOR_MULTIPLICITY_LOSS=false
STATE_SPLIT_E_MULTI_EDGE_TENSOR_CONTRACTION_PROVED=true.
```

The exact local Fourier coefficient energy is bounded prime-by-prime and globally. Other reciprocal edges act as diagonal unitary operators on the s5p auxiliary Hilbert coordinates, so they cannot enlarge the edgewise discrepancy L2 norm.

Thus the old K4 product-conductor and split-E multi-edge tensor obstructions are both closed.

## 3. Exact E-column Walsh collapse

For every odd `E=m^2+n^2` prime, selected and unselected H-prime rows are identical after the product-square relation:

```text
chi_p(d1)=+1.
```

If

```text
e=ker_odd(E),
```

then the complete odd E-column indicator is exactly

```text
I_E(d1;e)
 = product_{p|e}(1+chi_p(d1))/2
 = 2^(-omega(e)) sum_{v|e}(d1/v).
```

So the whole E column has one normalized Walsh subset variable `v|e`, with

```text
ell^1 norm = 1,
ell^2 norm <= 1.
```

Consequently the full local character polynomial reduces, for norm purposes, to a single moving linear--E signed-root edge.

## 4. Scalar E-linear edge and current L2 envelope

Let

```text
u~U
```

be one odd squarefree state modulus on a linear column and

```text
v~V
```

the E-Walsh subset modulus, refined to one signed root pattern `r^2=-1 mod v`.

All remaining state variables are harmless auxiliary Hilbert coordinates. The scalar edge has the schematic form

```text
T_E(U,V)
 = sum_{u~U}
   sum_{v~V,split}
   sum_{r^2=-1 mod v}
   Delta_{i,E,r}(u,v)
   theta_{u,v,r}
   (u/v),
```

with `|theta|<=1`.

On a regular Euclid box of scale `M`, s5m/s5p/s5q give

```text
|T_E(U,V)|
 << M^o(1) UV [1+M/K(U,V)],

K(U,V)=max(V^(1/2),min(U,V)).
```

## 5. Exact exponent atlas

Write

```text
U=M^alpha,
V=M^beta,
0<=alpha<=1,
0<=beta<=2,
```

and

```text
kappa(alpha,beta)
 = max(beta/2,min(alpha,beta)).
```

Relative to the physical `M^2` scale, the current L2/Cauchy exponent is

```text
R_E(alpha,beta)
 = alpha+beta
   + max(0,1-kappa(alpha,beta))
   - 2.
```

Thus

```text
R_E<0  => current theorem saves a power,
R_E=0  => critical transition,
R_E>0  => current theorem is insufficient.
```

The exact critical boundary imported from s5q is

```text
beta<1:  alpha=1;

beta=1:  1/2<=alpha<=1;

beta>1:  alpha+beta/2=1
         in the branch alpha<beta/2.
```

The central critical point is

```text
U~M^(1/2),
V~M.
```

## 6. Main-track 1/200 handoff band

The already-closed linear graph sector has conservative saving

```text
delta_K4=1/200.
```

To combine the scalar E edge with that ledger, define the **transition handoff band**

```text
W_1/200
 = {(alpha,beta): R_E(alpha,beta)>-1/200}.
```

Outside this band,

```text
R_E<=-1/200,
```

so the existing signed-root L2 theorem already gives at least the same `M^(-1/200)` saving as the closed graph sector.

Inside `W_1/200`, the existing L2 estimate is too weak to freeze the complete reciprocal exponent at `1/200`; it becomes neutral on the critical boundary and worse on the supercritical side.

Therefore all remaining reciprocal work may be restricted to the explicit root-sawtooth kernel on `W_1/200`.

## 7. Final root-sawtooth kernel

Stage14-s5q derives an exact floor decomposition in integral linear coordinates. For a signed root `r^2=-1 mod v`, the E condition becomes a transverse congruence

```text
y=c_r x (mod v).
```

Writing `x=u*a`, the discrepancy after subtraction of the density term is a finite linear combination of sums

```text
R(U,V)
 = sum_{v~V,split}
   sum_{r^2=-1 mod v}
   sum_{u~U}^*
   (u/v)
   sum_{a in I_u}
   b_{u,v,r,a}
   psi((A_r*u*a+B)/v),
```

where

```text
psi(t)={t}-1/2,
|b_{u,v,r,a}|<=M^o(1),
|I_u|~M/U.
```

Fourier expansion of `psi` produces hybrid additive/quadratic-character sums of the schematic form

```text
sum_u (u/v) exp(2*pi*i*h*A_r*a*u/v),
```

averaged simultaneously over `u,v,r,a`.

At the central scale `U~M^(1/2), V~M`, one-variable completion is exactly neutral. The next theorem must therefore be genuinely bilinear/hybrid.

## 8. Conditional reciprocal exponent contract

Let `delta_saw>0` denote a future uniform saving for the root-sawtooth kernel throughout the handoff band `W_1/200`.

Then the complete nonconstant reciprocal error would satisfy

```text
E_rec(M)
 << M^(2-delta_rec+o(1)),

delta_rec=min(1/200,delta_saw).
```

This is now the exact remaining reciprocal contract. There is no auxiliary, K4-core, state-label, or E-tensor exponent parameter left.

Until `delta_saw>0` is proved, a complete positive reciprocal exponent is not claimed.

## 9. rho_loc remains a separate diagonal/local-density problem

The local domination remains

```text
S_W<=D_loc+E_rec.
```

The stages through 4bc concern `E_rec`. The constant/diagonal local-density contribution `D_loc` has not yet been assigned against `A_W` with a positive retainer exponent.

Therefore even after the root-sawtooth kernel is closed, the final `rho_loc` must still be read from a separate diagonal/local-density calculation. It is invalid to set `rho_loc=1/200` from reciprocal cancellation alone.

## Boundary

```text
STAGE14_4BC=S5P_S5Q_IMPORTED_AND_FINAL_ROOT_SAWTOOTH_GATE_FROZEN
S5P_AUXILIARY_UNIFORMITY_IMPORTED=true
AUXILIARY_INCIDENCE_UNIFORMITY_PROVED=true
AUXILIARY_PROGRESSION_MODULUS_EXPONENT_LOSS=0
S5Q_FOURIER_TENSOR_CONTRACTION_IMPORTED=true
MULTI_EDGE_DISCREPANCY_TENSOR_CONTRACTION_PROVED=true
LINEAR_ONLY_FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=true
E_SELECTED_UNSELECTED_H_ROW_IDENTICAL=true
E_COLUMN_SINGLE_WALSH_SUBSET_EXACT=true
E_WALSH_L1_NORMALIZED=true
E_WALSH_L2_CONTRACTIVE=true
STATE_SPLIT_E_TENSOR_MULTIPLICITY_LOSS=false
STATE_SPLIT_E_MULTI_EDGE_TENSOR_CONTRACTION_PROVED=true
FULL_LOCAL_CHARACTER_POLYNOMIAL_REDUCED_TO_SINGLE_E_LINEAR_EDGE=true
E_LINEAR_EXISTING_L2_POWER_SAVING_REGION_CLASSIFIED=true
E_LINEAR_TRANSITION_WEDGE_PERSISTS=true
FINAL_ROOT_SAWTOOTH_KERNEL_EXPLICIT=true
MAIN_TRACK_RECIPROCAL_TARGET_SAVING=1/200
ROOT_SAWTOOTH_HANDOFF_BAND=R_E>-1/200
CONDITIONAL_RECIPROCAL_EXPONENT_FORMULA=min(1/200,delta_saw)
COMPLETE_POSITIVE_RECIPROCAL_EXPONENT_PROVED=false
FULL_LOCAL_CHARACTER_POLYNOMIAL_AVERAGED=false
EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED=false
EXPLICIT_COMPLETE_E_LOC_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

```text
NEXT=Stage14-4bd prove a hybrid bilinear power saving for the explicit root-sawtooth reciprocal kernel on the handoff band R_E>-1/200, with first priority U~M^(1/2), V~M; then freeze the first complete reciprocal E_rec exponent and return to the D_loc/rho_loc assignment
```
