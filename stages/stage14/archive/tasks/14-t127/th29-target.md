# Stage14-tH29 immutable target — nonboundary Gaussian cofactor/prime projective hyperbola dispersion

```text
REQUESTED_OBJECT=FixedPacketNonboundaryPrimitiveGaussianCofactorPrimeProjectiveHyperbolaDispersion
SOURCE_SNAPSHOT_STAGE=Stage14-t127
SOURCE_SNAPSHOT_SHA=38ac82435315979d3d0493090d153b4b36163be1
TARGET_FROZEN=true
TARGET_FILE=stages/stage14/14-t127/th29-target.md
```

## Frozen packet

Fix

```text
(U,epsilon,k,h,kappa,beta,eta),
k0=eta*k,
```

one allowed norm-`k0` Gaussian factor `a`, one admissible exceptional packet, endpoint modulus

```text
d=B^o(1),
G(d)=(Z[i]/dZ[i])^x/(Z/dZ)^x,
```

and the t124 charged-once family `Omega_nb` of canonical nonboundary physical primitive Gaussian cofactors.

For `gamma in Omega_nb`, put

```text
n=N(gamma).
```

The dominant Gaussian prime label `pi_ell` has rational prime norm `ell`, is canonical split, is coprime to `d`, and satisfies exactly

```text
ell>2*sqrt(B),
n*ell<=X_U,
X_U=2B/(h*k0),
[gamma]*[a]*[pi_ell]=1 in G(d).
```

The strong fixed-`U` gap already makes the old canonical-LPF and exponent-one conditions automatic; they are not to be recharged as new density factors.

## Exact centered target

Let `g=|G(d)|`.  The physical count is

```text
T=M+D,
```

where `M` is the exact principal projective-class baseline and

```text
D
 = 1/g * sum_{chi != 1 in G(d)^}
       chi([a])
       sum_{
         gamma in Omega_nb,
         pi_ell canonical split,
         ell>2*sqrt(B),
         N(gamma)*ell<=X_U
       }
       chi([gamma]) chi([pi_ell]).
```

The relevant bad event is principal-scale negative correlation:

```text
D <= -(1-B^(-delta)) M
```

for some fixed `delta>0`, equivalently `T<=B^(-delta)M`.

## Audit question

Independently determine whether existing literature proves any theorem that, uniformly over this frozen fixed-packet family and `d=B^o(1)`, either:

1. rules out principal-scale negative correlation by proving `D=o(M)` (or any quantitatively sufficient lower control on `T/M`); or
2. directly gives a fixed positive `B`-power saving for the physical selected-class count relative to the charged principal baseline;
3. supplies a theorem-ready bilinear/dispersion/large-sieve adapter for the exact primitive Gaussian cofactor support `Omega_nb` and the Gaussian-prime factor with the hyperbola `N(gamma)*ell<=X_U`.

Test, as appropriate, Gaussian/Hecke large sieve and bilinear forms, prime-ideal Bombieri--Vinogradov/BDH, Gaussian-sector/ray-class prime distribution, bilinear forms with Kloosterman fractions, Gaussian spin/reciprocity technology, and relevant dispersion results.

The audit must retain:

```text
fixed U packet,
primitive Gaussian cofactor condition,
nonboundary physical canonical support from t124,
fixed exceptional packet,
d=B^o(1) rather than silently fixed/polylog,
canonical split Gaussian prime labels,
ell>2*sqrt(B),
N(gamma)*ell<=X_U,
exact projective relation [gamma][a][pi_ell]=1,
charged-once accounting.
```

Do not reopen the already discharged D4-boundary atomic branch, generic projective-class density, canonical-LPF density, or unmasked projected-norm support.  Do not use any later Stage14-t conclusion in this audit.
