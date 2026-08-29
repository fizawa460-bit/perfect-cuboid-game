# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_NAMED_SPECIAL_BRAUER_ORBIT_SELECTED_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Class-2 decision budget

This is MAIN **batch 2 / 4** under the common-standard-form go/no-go contract.

```text
named CV J2
  -> special-Brauer / mu_2 Cech datum
  -> twisted relative Picard K3 X_J2
  -> T(X_J2)=ker(J2:T(Kc)->Z/2)
  -> minimum norm 4 / 8 / 12
  -> [0,1] / [1,0] / [1,1].
```

Batch 1 closed the four-even-contact local search: exactly 16 raw pairings, exactly four isomorphism orbits, classified by

```text
L = p_+1 XOR p_-1
R = p_0  XOR p_inf.
```

The orbit bits are not the fixed marked Brauer bits.

## Fixed marked receiver

```text
T(Kc) ~= <4> direct_sum <8>
Br(Kc)[2] = Hom(T,Z/2)
[1,0] -> kernel minimum norm 8
[0,1] -> kernel minimum norm 4
[1,1] -> kernel minimum norm 12
```

The marked coordinate remains unselected in this batch.

## Batch 2: exact named-CV orbit adapter

Stage33-05 already presents the named geometric class as the Jacobian two-torsion element

```text
J2=(1,0) on E: y^2=x^3-x,
```

with the common branch normalization `z^2=t^4-6*t^2+1`. The same Stage33-05 normalization records distinguished B+ nodes

```text
P1 = e1 at t=0,
P3 = e3 at t=1,
P5 = e5 at t=-1,
P7 = e7 at t=infinity.
```

Under the exact normalization map to `E:y^2=x^3-x`, direct elliptic group-law calculation gives

```text
P3-P5 = J1+J2 = (-1,0)
P3+P5 = J1     = (0,0)
P1-P7 = J2     = (1,0)
P1+P7 = J1     = (0,0).
```

The two batch-1 pairing parities are therefore the two special-Brauer/Kummer sheet-holonomy characters on the exact contact cycles

```text
D_L = P3-P5 = J1+J2,
D_R = P1-P7 = J2.
```

For an elliptic curve identified with `Pic^0(E)`, the Kummer character of a two-torsion line bundle `T` on a two-torsion cycle `D` is the Weil pairing `e_2(T,D)`. We encode `+1 -> bit 0` and `-1 -> bit 1`.

For the named `T=J2`, alternating nondegeneracy of the Weil pairing gives

```text
e_2(J2,J1+J2) = -1 -> L=1
e_2(J2,J2)     = +1 -> R=0.
```

Hence the named CV J2 datum selects the unique orbit

```text
(L,R) = (1,0)
raw representatives = {0100,0111,1000,1011}.
```

As a complete regression, the four Jacobian two-torsion classes map bijectively to the four pairing orbits:

```text
0       -> (0,0)
J1      -> (1,1)
J2      -> (1,0)
J1+J2   -> (0,1).
```

This is not a cardinality argument: the two exact contact cycles form an independent `E[2]` basis and the Weil/Kummer character evaluates the named class on them.

Certificate: `j2-named-cv-special-brauer-pairing-orbit.json`.
Verifier: `certify_j2_named_cv_special_brauer_pairing_orbit.py`.

## Semantic firewall

The notation `(L,R)=(1,0)` is **not** identified with the fixed marked Kc coordinate `[1,0]`. The former is the finite resolved-contact special-Brauer orbit coordinate; the latter is the fixed functional on `T(Kc)`.

Thus batch 2 closes the named-orbit selection interface but does not close Stage33-12.

## Batch 3 exact target

```text
CONSTRUCT A HERMITE / TWISTED-RELATIVE-PICARD GENUS-ONE K3 X_J2
REALIZING THE SELECTED ORBIT (L,R)=(1,0),
THEN COMPUTE T(X_J2) OR ITS MINIMUM NORM.
```

If the resulting minimum norm is `4`, `8`, or `12`, the already certified kernel fingerprints select `[0,1]`, `[1,0]`, or `[1,1]` respectively. If the selected orbit cannot be promoted to such a torsor/lattice without a new global marked-cohomology theorem, batch 3 must record formal class-2 failure rather than reopen local bridge search.

## Firewalls

```text
class-2 budget used = 2/4
Stage33-12 visible progress = 4/5
named CV J2 pairing orbit selected = true
selected special-Brauer orbit = (1,0)
pairing orbit bits = marked Brauer bits = false
J2 explicit torsor surface materialized = false
J2 marked Brauer functional materialized = false
J2 twisted transcendental kernel identified = false
Stage33-12 exact closure = false
Stage33-13 released = false
heavy actions authorized = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
