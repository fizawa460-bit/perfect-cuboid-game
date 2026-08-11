# Stage14-t135 — transpose to a fixed-residue Gaussian cofactor/prime reciprocal hyperbola

## Status

`COMPLETE_FIXED_GAUSSIAN_RESIDUE_COFACTOR_PRIME_HYPERBOLA_FREEZE`

Consumes Stage14-t134 on the same batch branch together with merged `Stage14-t109/t110/t125/t126` and completed merged `Stage14-tH29` as the previous negative theorem boundary.

Keep the t134 fixed cofactor sector/residue coefficient

```text
W_*(n)
 = #{z primitive :
      N(z)=n,
      z in fixed open sector S,
      z == rho_* (mod d),
      frozen exceptional packet}.
```

The selected prime projective class is the fixed `q_* in G(d)`.  With

```text
R_d=(Z[i]/dZ[i])^x,
H_d=image((Z/dZ)^x),
h_d=|H_d|,
g=|G(d)|,
```

choose one representative `beta_0` of `q_*`.  Then

```text
[pi]=q_*
<=>
pi mod d lies in beta_0 H_d,
```

an exact coset of `h_d=B^o(1)` invertible Gaussian residue classes.

For `beta in beta_0 H_d`, put

```text
K_n(beta)
 := #{canonical split pi_ell :
       ell>2*sqrt(B),
       ell<=X_U/n,
       pi_ell == beta (mod d)}.
```

Then exactly

```text
K_n(q_*)=sum_beta K_n(beta).
```

## 1. Freeze one ordinary prime residue without losing the depletion exponent

The t134 localized physical count is

```text
T_* = sum_beta T_beta,
T_beta := sum_n W_*(n) K_n(beta).
```

Split its principal baseline artificially but exactly into equal coset pieces

```text
M_beta
 := 1/(g*h_d) * sum_n W_*(n)|P_n|.
```

Because `g*h_d=|R_d|` and there are exactly `h_d` residues in the projective coset,

```text
sum_beta M_beta
 = 1/g * sum_n W_*(n)|P_n|
 = M_*.
```

If

```text
T_* <= B^(-delta) M_*,
```

then averaging the nonnegative ratios over the `h_d` equal baselines gives at least one exact residue `beta_*` with

```text
T_{beta_*}
 <= B^(-delta) M_{beta_*},

M_{beta_*}=B^(-o(1))M_*.
```

Thus both the cofactor and dominant-prime projective selectors may be frozen to ordinary Gaussian residue classes at subpolynomial charged-once cost.

## 2. Remove the scalar norm weight by transposition

Let `Z_*` be the actual primitive Gaussian cofactor set

```text
Z_* := {z in Z[i] :
        z primitive,
        z in S,
        z == rho_* (mod d),
        frozen exceptional packet,
        N(z) in the live nonboundary norm range}.
```

By definition of `W_*(n)`, regrouping by `n=N(z)` is exact.  Therefore

```text
T_{beta_*}
 = # {(z,pi_ell) :
       z in Z_*,
       pi_ell canonical split,
       pi_ell == beta_* (mod d),
       ell>2*sqrt(B),
       N(z)*ell<=X_U}.
```

No arbitrary scalar coefficient remains.

The corresponding principal baseline is

```text
M_{beta_*}
 = 1/|R_d|
   * sum_{z in Z_*}
       #{canonical split pi_ell :
         2*sqrt(B)<ell<=X_U/N(z)}.
```

So the residual fixed-U obstruction is an explicit bipartite incidence between

```text
primitive Gaussian cofactors
  in one fixed broad sector and one fixed residue rho_* mod d,

and canonical split Gaussian primes
  in one fixed residue beta_* mod d,
```

under the reciprocal norm hyperbola

```text
N(z)*N(pi_ell)<=X_U,
N(pi_ell)>2*sqrt(B).
```

The frozen exceptional multiplier/local packet on `z` remains explicit and must be retained; it has no polynomial label multiplicity.

## 3. Fresh H audit is now justified

Completed tH29 audited a broader target in which the physical cofactor family was retained as an opaque/nonmultiplicative coefficient.  Stages t132--t135 have removed that opacity:

- one cofactor projective class was localized nonnegatively;
- one D4 normalization sector was frozen;
- one ordinary cofactor residue was frozen;
- one ordinary prime residue was frozen;
- the scalar weight was unfolded back to an unweighted primitive Gaussian cofactor set.

The remaining target is therefore materially different for theorem applicability, even though it is the same fixed-class depletion mechanism.  A fresh independent audit should test Gaussian prime progression / Hecke ray-class / bilinear hyperbola / lattice-sector technology on this exact fixed-residue incidence, retaining unrestricted endpoint headroom, `d=B^o(1)`, the canonical prime convention, primitivity, and the frozen exceptional local packet.

This stage is treated as a theorem-ready coordinate freeze rather than a new saving mechanism; the receiver-change decision is deferred until the H verdict is consumed.

```text
FIXED_PRIME_PROJECTIVE_CLASS_LIFT_TO_GAUSSIAN_RESIDUES_EXACT=true
ONE_PRIME_GAUSSIAN_RESIDUE_FREEZABLE_WITHOUT_POWER_LOSS=true
COFACTOR_SCALAR_WEIGHT_UNFOLDED_TO_ACTUAL_GAUSSIAN_POINTS=true
FIXED_RESIDUE_GAUSSIAN_COFACTOR_PRIME_HYPERBOLA_EXACT=true
OPAQUE_COFACTOR_WEIGHT_REMAINS=false
TH29_TARGET_STRICTLY_BROADENED_RELATIVE_TO_NEW_TARGET=true
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=true
T_ROUTE_H_REQUEST=FixedPacketFixedGaussianResiduePrimitiveSectorCofactorPrimeReciprocalHyperbolaOccupancy
T_ROUTE_H_TARGET=stages/stage14/14-t135/th30-target.md
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUFixedGaussianResiduePrimitiveSectorCofactorPrimeReciprocalHyperbolaDepletion
NEXT=Stage14-tH30
```
