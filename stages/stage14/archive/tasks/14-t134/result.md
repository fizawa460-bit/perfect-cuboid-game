# Stage14-t134 — lift the fixed cofactor projective class to one Gaussian residue class

## Status

`COMPLETE_FIXED_COFACTOR_PROJECTIVE_CLASS_TO_GAUSSIAN_RESIDUE_LOCALIZATION`

Consumes Stage14-t133 on the same batch branch and merged `Stage14-t110`.

Keep the fixed t133 normalization sector `S`, fixed raw cofactor projective class `c_raw in G(d)`, and fixed exceptional packet.  Merged t90/t109 give

```text
d=B^o(1),
gcd(d,n)=1
```

on the live cofactor family, so every raw Gaussian cofactor is invertible modulo `d`.

Let

```text
R_d=(Z[i]/dZ[i])^x,
H_d=image((Z/dZ)^x -> R_d),
G(d)=R_d/H_d.
```

A projective class is exactly one coset of `H_d`.  Choose one representative `rho_0 in R_d` of `c_raw`.  Then

```text
[z]=c_raw
<=>
z mod d lies in rho_0 H_d.
```

The coset contains exactly

```text
h_d:=|H_d| <= phi(d) <= d = B^o(1)
```

ordinary invertible Gaussian residue classes modulo `d`.

For each residue `rho in rho_0 H_d`, define

```text
W_rho(n)
 := #{z in Z[i] :
       N(z)=n,
       z primitive,
       z in S,
       z == rho (mod d),
       z has the frozen exceptional packet}.
```

Then exactly

```text
W_raw(n)=sum_{rho in rho_0 H_d} W_rho(n).
```

Consequently the localized t133 count and principal baseline split nonnegatively as

```text
T_raw=sum_rho T_rho,
M_raw=sum_rho M_rho,

T_rho=sum_n W_rho(n) K_n(q_*),
M_rho=1/|G| sum_n W_rho(n)|P_n|.
```

If the t133 branch satisfies a fixed-power depletion, another direct nonnegative pigeonhole freezes one exact Gaussian residue `rho_*` with

```text
M_{rho_*} >= B^(-o(1)) M_raw,
T_{rho_*} <= B^(-delta+o(1)) M_{rho_*}.
```

Thus the cofactor weight may be replaced, at only `B^o(1)` charged-once cost, by the exact scalar coefficient

```text
W_*(n)
 = #{z primitive :
      N(z)=n,
      z in S,
      z == rho_* (mod d),
      frozen exceptional packet}.
```

Equivalently, after writing `z=gamma_E z_G`, the only moving cofactor object is a primitive Gaussian integer `z_G` in one fixed broad sector after multiplication by `gamma_E`, one fixed ordinary Gaussian residue class modulo `d`, and coprime to the frozen exceptional support.

This removes projective quotient ambiguity from the cofactor side completely.  No equidistribution theorem is used, and no density factor from the `B^o(1)` residue family is recharged.

The prime selector is still kept as the fixed projective class `q_*`; its ordinary-residue lift is deferred to t135 so both sides can be transposed together.

```text
FIXED_COFACTOR_PROJECTIVE_CLASS_LIFT_TO_GAUSSIAN_RESIDUES_EXACT=true
COFACTOR_PROJECTIVE_COSET_SIZE=Bo1
ONE_COFACTOR_GAUSSIAN_RESIDUE_FREEZABLE_WITHOUT_POWER_LOSS=true
COFACTOR_WEIGHT_IS_FIXED_SECTOR_FIXED_RESIDUE_PRIMITIVE_NORM_COUNT=true
COFACTOR_PROJECTIVE_QUOTIENT_AMBIGUITY_REMAINS=false
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUFixedGaussianSectorResiduePrimitiveCofactorNormWeightAgainstReciprocalFixedProjectivePrimeClassDepletion
NEXT=Stage14-t135
```
