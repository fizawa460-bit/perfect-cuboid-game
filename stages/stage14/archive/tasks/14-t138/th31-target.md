# Stage14-tH31 frozen target — Mitsui-safe long-headroom fixed Gaussian residue occupancy

## Immutable parent snapshot contract

This target is emitted by Stage14-t138 and must be audited independently.  Later t-stages must not mutate the target.

```text
REQUESTED_OBJECT=MitsuiSafeLongHeadroomFixedGaussianResiduePrimeOccupancyLowerBound
BASE_FIELD=Q(i)
MODULUS_IDEAL=(d)
MODULUS_NORM=d^2
COFACTOR_SIDE=EXPLICIT_FIXED_SECTOR_FIXED_RESIDUE_PRIMITIVE_GAUSSIAN_SET
PRIME_SIDE=CANONICAL_SPLIT_GAUSSIAN_PRIMES_IN_ONE_FIXED_ORDINARY_RESIDUE
```

## Frozen packet

Fix one t135/t136/t137 packet, including

```text
U, epsilon, k, h, kappa, beta, eta,
k0=eta*k,
a,
d,
rho_*, beta_*,
fixed open D4/canonical sector S,
frozen exceptional local cofactor packet.
```

Put

```text
L_B=2*sqrt(B),
X_U=2B/(h*k0).
```

Let `Z_safe,long` be the actual primitive Gaussian cofactor set

```text
z in Z[i],
z primitive,
z in the fixed open sector S,
z == rho_* (mod d),
z satisfies the frozen exceptional local packet,
R(z):=X_U/(L_B*N(z)) >= B^theta
```

for one fixed `theta>0`.

For every such `z`, define

```text
y_z=X_U/N(z),
y_z>=L_B*B^theta.
```

The modulus satisfies the Mitsui-safe bound

```text
d <= exp(c_safe*sqrt(log B)),
N((d))=d^2 <= exp(c0*sqrt(log y_z))
```

with `c_safe>0` chosen sufficiently small relative to the fixed constants in the applicable `Q(i)` prime-element theorem.

## Physical and principal counts

For each `z`, let

```text
K_z(beta_*)
 := #{canonical split Gaussian prime pi:
      pi == beta_* (mod d),
      L_B<N(pi)<=y_z}.
```

Let

```text
P_z
 := #{canonical split Gaussian prime pi:
      L_B<N(pi)<=y_z}.
```

The safe long-headroom physical and principal masses are

```text
T_safe = sum_{z in Z_safe,long} K_z(beta_*),

M_safe = 1/|(Z[i]/dZ[i])^x|
         * sum_{z in Z_safe,long} P_z.
```

All sums are nonnegative.

## Required theorem conclusion

Audit whether existing unconditional prime-element / Hecke / Mitsui technology gives uniformly on this frozen family

```text
T_safe >= B^(-o(1)) M_safe.
```

This is sufficient: it rules out

```text
T_safe <= B^(-delta) M_safe
```

for every fixed `delta>0`.

A full `(1+o(1))` equidistribution theorem is not required.

## Exceptional-zero requirement

The audit must retain a possible real Hecke/Siegel character.  If the prime-element theorem contains a secondary term, it must show that on the fixed residue/sector class the resulting lower factor is at worst `B^{-o(1)}` in the allowed modulus range.  It is not acceptable to assume GRH or to assume no exceptional zero.

## Interval transposition requirement

The target interval is

```text
(L_B,y_z],
y_z/L_B>=B^theta.
```

It is acceptable to apply a cumulative prime-element theorem at `y_z` and at `L_B` and subtract, provided the fixed-power headroom makes the lower endpoint negligible at exponent level and the secondary exceptional term remains controlled after subtraction.

## Canonical split-prime compatibility

The theorem must genuinely count Gaussian prime elements in the fixed open canonical sector and ordinary residue `beta_* mod d`.  In `Q(i)`, inert rational Gaussian primes lie on the sector boundary/axes and must not be silently introduced into the physical prime family.

## Output contract

Return explicit booleans for

```text
MITSUI_SAFE_LONG_HEADROOM_THEOREM_APPLICABLE
POSSIBLE_SIEGEL_ZERO_RETAINED
SIEGEL_SECONDARY_TERM_FIXED_POWER_DEPLETION_POSSIBLE
SAFE_BRANCH_T_GE_BO_MINUS_O1_M_PROVED
SAFE_BRANCH_FIXED_POWER_DEPLETION_RULED_OUT
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT
NEXT_H_NEEDED
```

and keep the whole-family ledger

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```
