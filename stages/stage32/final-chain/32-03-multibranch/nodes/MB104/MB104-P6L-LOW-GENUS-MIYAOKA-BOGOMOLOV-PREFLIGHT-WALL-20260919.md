# MB104 P6L — low-genus Miyaoka/Bogomolov preflight wall — 2026-09-19

Status: **PRE-AUDIT SOURCE-COMPLETE ASYMPTOTIC NO-GO / NO CREDIT**

## Target

The hostile P6 ray has hypothetical integral carriers
`C in |lP|` with geometric genus one and

```text
P^2 = 336,
C^2 = 336 l^2,
K_S.C = 112 l.
```

P6L tests whether an unconditional low-genus curve inequality on the smooth minimal
cuboid surface can force an upper bound on `l`.

## Surface Chern numbers

The cuboid surface is a complete intersection of four quadrics in `P^6`, with only
48 rational double points of type A1.  Adjunction gives

```text
K_S = H,
K_S^2 = H^2 = 2^4 = 16.
```

For a smooth `(2,2,2,2)` complete intersection,

```text
c(T_S) = (1+H)^7/(1+2H)^4,
c_2(S) = 5 H^2 = 80.
```

Resolving A1 rational double points is crepant and preserves these Chern-number
values relative to the smoothing model used here, so the minimal resolution has

```text
K^2 = 16,
c_2 = 80,
3c_2-K^2 = 224.
```

These values are also consistent with the retained modular description
(`p_g=7`, `q=0`) and Noether's formula.

## The tempting smooth-elliptic bound is not applicable

Lu--Miyaoka derive for a **nonsingular** genus-`g` curve on a surface with nef
canonical divisor the corollary

```text
K.C <= 3g-3
       + ( sqrt((3c2-K^2)(4g-4+3c2-K^2)) )/2
       + (3c2-K^2)/2.
```

For `g=1` and the cuboid Chern numbers this would read

```text
K.C <= 224,
```

and would formally give `l<=2`.

That inference is invalid here: the MB104 carrier is an integral **singular** curve
whose normalization has genus one.  Its self-intersection grows as `336l^2`; it is
not a smooth elliptic curve satisfying `C^2+K.C=0`.

## The irreducible singular-curve inequality is compatible with every l

The Miyaoka inequality valid for an irreducible curve of geometric genus `g`
(not necessarily smooth) gives, when `C != P1` and `K.C>3g-3`,

```text
2(K.C-3g+3)^2
 - (3c2-K^2)(C^2+3K.C-6g+6) <= 0.
```

Set `g=1`, `3c2-K^2=224`, `K.C=112l`, and `C^2=336l^2`.  The left side becomes

```text
2(112l)^2 - 224(336l^2 + 336l)
 = -50176 l^2 - 75264 l,
```

which is strictly negative for every `l>=1`.

Thus the source-complete irreducible-curve theorem gives no finite window and no
asymptotic pressure on the hostile ray.

The weaker general lower bound

```text
C^2 >= K^2 - 3c2 + 2 - 2g
```

becomes `336l^2 >= -224`, also vacuous.

## Disposition

P6L is closed as an asymptotic no-go.  The smooth-elliptic corollary must not be
misapplied to the singular carrier, and the correct singular-curve inequality is
compatible with all `l`.

A stronger log-BMY route would need genuinely new singularity-type information,
not merely the geometric genus and total self-intersection already used above.

## Next route

```text
MB104-P6M-SINGULARITY-TYPE-LOG-BMY-CORRECTION-PREFLIGHT
```

Shallow target only: determine whether the retained MB104 local data fixes enough
of the carrier's singularity types (ordinary nodes/triples, local orbifold weights,
or equivalent exact corrections) to improve the general Miyaoka inequality at the
quadratic `l^2` coefficient.  If the retained data controls only total delta/contact
mass and not the singularity-type correction, park immediately.

## External sources

- S. S.-Y. Lu and Y. Miyaoka, *Bounding curves in algebraic surfaces by genus and
  Chern numbers*, Math. Res. Lett. 2 (1995), 663--676.
- Y. Miyaoka, later orbibundle Miyaoka--Yau--Sakai formulation; the irreducible-curve
  inequality is valid for geometric genus without a smoothness assumption.
- M. Stoll and D. Testa, *The surface parametrizing cuboids*, for the cuboid surface
  as the four-quadric complete intersection with 48 A1 singularities.

## Firewalls

```text
smooth_elliptic_bound_applied=false
singular_curve_miyaoka_checked=true
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
