# SR-STR-021 deep closure attempt

Date: 2026-08-19
Status: `FIRST_MISSING_LEMMA_IDENTIFIED`
Arsenal decision: unchanged (`EXTERNAL_GATE`).

## Closed reduction

The pre-Work residue/sector adapter can be pushed further than PR #1112 suggested.

Using the primary Gaussian generator normalization, finite Gaussian/ray characters `chi`, angular Hecke characters `xi_k`, and a fixed positive-width sector minorant:

- ordinary residue + primary normalization + fixed D4 sector reduce to finitely many `xi_k*chi` twists;
- the angular frequency set is `O(1)` for a fixed sector;
- unit/conjugation/2-primary bookkeeping is fixed-cost;
- a short-interval explicit-formula architecture can be written directly for the interval difference, avoiding naive subtraction of two global PNT estimates;
- the possible exceptional zero belongs only to the `k=0` finite-order character.

The principal-plus-exceptional main term for the worst target class still has relative factor at least `X^{-o(1)}` when `N(d)=X^{o(1)}`. Thus the Siegel zero itself does not destroy the required lower ratio.

## First missing lemma

```text
FIRST_MISSING_LEMMA=ExceptionalZeroRepelledLogFreeZeroDensityForGaussianAngularRayCharacters
```

Needed form: for `K=Q(i)`, one modulus `d` with `D=N(d)=X^{o(1)}`, and a fixed finite angular set `k`, after removing the possible exceptional zero `beta_1` at `(chi_1,k=0)`, prove a log-free zero-density estimate for the joint family `L(s,xi_k chi*)` carrying a Deuring–Heilbronn factor

```text
nu(U)=min(1,(1-beta_1) log U).
```

The required error after residue orthogonality is

```text
o(lambda_w * H / phi_Z[i](d)),
```

not merely `o(H/phi(d))`, because the worst exceptional target class may have `lambda_w=X^{-o(1)}`.

Merikoski supplies the joint `(chi,k)` density without the `nu` factor. Thorner–Zaman supplies the needed repulsion factor for finite-order Hecke characters, but not the nonzero-infinity-type `xi_k*chi` family. This is the first genuine proof gap.

```text
RESIDUE_SECTOR_ADAPTER=PROVED_AT_FIXED_COST
SHORT_INTERVAL_EXPLICIT_FORMULA_ARCHITECTURE=PROVED_AT_STRUCTURAL_LEVEL
EXCEPTIONAL_MAIN_LOWER_RATIO=X^{-o(1)}
EXCEPTIONAL_SENSITIVE_JOINT_ZERO_REPULSION=OPEN
SR_STR_021_STATUS=EXTERNAL_GATE
ADAPTER_CLOSURE_VERDICT=FIRST_MISSING_LEMMA_IDENTIFIED
```
