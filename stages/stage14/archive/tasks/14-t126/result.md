# Stage14-t126 — transpose the selected-class count to an exact projective hyperbola incidence

## Status

`COMPLETE_SELECTED_CLASS_NESTED_INTERVAL_TO_PROJECTIVE_HYPERBOLA_TRANSPOSITION`

Consumes Stage14-t125 on the same batch branch together with merged `Stage14-t112/t124`.

Fix all `B^o(1)` packet, exceptional, norm-`k0` factor, and canonical normalization labels.  Let

```text
Omega_nb
```

be the resulting charged-once finite family of nonboundary physical primitive Gaussian cofactors.  For `gamma in Omega_nb` write

```text
n_gamma=N(gamma),
c_gamma=([gamma][a])^(-1) in G(d),
X_U=2B/(h*k0),
L_B=2*sqrt(B).
```

By t125 the accepted dominant primes are exactly the canonical split Gaussian prime labels `pi_ell` satisfying

```text
L_B < ell <= X_U/n_gamma,
[pi_ell]=c_gamma.
```

Define cumulative prime-class counts

```text
Pi_c(y)
 := # {canonical split Gaussian prime labels pi_ell:
        L_B < ell <= y,
        gcd(ell,d)=1,
        [pi_ell]=c}.
```

Then the exact physical completion count on this subpacket is

```text
T
 = sum_{gamma in Omega_nb}
     Pi_{c_gamma}(X_U/n_gamma).
```

Let

```text
F_c(y)
 := # {gamma in Omega_nb:
        n_gamma <= y,
        c_gamma=c},

F(y):=sum_c F_c(y).
```

All sums are finite.  Interchanging the two indicators gives the exact hyperbola transposition

```text
T
 = sum_{pi_ell: ell>L_B}
     F_[pi_ell](X_U/ell),
```

where terms with `X_U/ell` below the smallest cofactor norm vanish automatically.

### Principal baseline under the same transposition

Merged t112 gives the exact uniform-class principal baseline

```text
M
 = 1/|G|
   sum_{gamma in Omega_nb}
     # {canonical split Gaussian pi_ell:
        L_B<ell<=X_U/n_gamma}.
```

Interchanging the same finite incidence yields

```text
M
 = 1/|G|
   sum_{pi_ell: ell>L_B}
     F(X_U/ell).
```

Thus the live t124 depletion problem is exactly the comparison

```text
sum_{pi_ell} F_[pi_ell](X_U/ell)
```

against

```text
1/|G| * sum_{pi_ell} F(X_U/ell).
```

No approximation, prime number theorem, or smoothing is used.

### What the transposition changes and does not change

The selected projective class is no longer attached to a separately moving prime interval; after the swap it is a class-matching condition on one reciprocal hyperbola

```text
n_gamma * ell <= X_U,
ell>2*sqrt(B),
[gamma]*[a]*[pi_ell]=1 in G(d).
```

The cofactor family still carries every nonboundary physical primitive condition inherited from t124.  The prime remains canonical split, and the endpoint modulus remains `d=B^o(1)`.

This is an exact transposition of the same receiver, not a new saving mechanism and not a material receiver change.

```text
SELECTED_CLASS_COUNT_HYPERBOLA_TRANSPOSITION_EXACT=true
COFACTOR_CUMULATIVE_CLASS_COUNTS_DEFINED=true
PHYSICAL_COUNT_EQUALS_CLASS_MATCHED_HYPERBOLA_INCIDENCE=true
PRINCIPAL_BASELINE_TRANSPOSES_EXACTLY=true
PROJECTIVE_HYPERBOLA_RELATION=[gamma][a][pi_ell]=1
PROJECTIVE_HYPERBOLA_BOUND=n_gamma*ell<=X_U
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUNonboundaryPhysicalCofactorSelectedProjectiveClassNearTotalPrimeDepletion
NEXT_INTERNAL_TARGET=CenteredProjectiveHyperbolaFourierCorrelationFreeze
NEXT=Stage14-t127
```
