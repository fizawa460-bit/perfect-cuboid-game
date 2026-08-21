# Non-Fano characteristic-variety adapter — audited scope

The non-Fano recognition imports a useful arrangement-topology package, but the central/projective convention must be kept explicit.

## Published central-arrangement data

Suciu Example 10.5 records, in the seven-meridian character coordinates,

```text
V1 = C125 ∪ C136 ∪ C246 ∪ C345 ∪ C237 ∪ C567 ∪ Pi1 ∪ Pi2 ∪ Pi3,
Pi1=C(25|36|47),
Pi2=C(17|26|35),
Pi3=C(14|23|56),
V2={1,rho},
rho=(1,-1,-1,1,-1,-1,1).
```

It also records for the **central-arrangement** unbranched congruence cover `X_N`

```text
b1(X_N)=9N^2-3  if N even,
        =9N^2-2  if N odd.
```

The central arrangement group splits as

```text
G_central ~= G_projective x Z.
```

Consequently the endpoint's unbranched degree-64 cover of the **projective** complement is not this central `X_N`; the central cover has the extra `C*` factor.  At `N=2`,

```text
CENTRAL_OPEN_B1=33
PROJECTIVE_ENDPOINT_OPEN_B1=32.
```

The compact Hirzebruch surface formula is unaffected:

```text
b1(M_N)=9(N-1)(N-2),
b1(M_2)=0.
```

## Character restriction to the projective endpoint

The projective character torus is the product-one subtorus of the seven central meridian coordinates.  Therefore every component/character imported into the endpoint ledger must first be restricted to that subtorus.

The distinguished character

```text
rho=(1,-1,-1,1,-1,-1,1)
```

has product `1`, so it does descend to a genuine order-two projective character.  This makes `rho` a valid downstream endpoint receiver.  The nine positive-dimensional components are not blindly copied as nine endpoint components; their product-one intersections are the correct objects.

## Q-form firewall

Characteristic varieties are complex-topological invariants of the arrangement complement.  They survive the constant-sign Q-twist only geometrically; an arithmetic identification of a particular intermediate quotient over `Q` requires the twist character to be carried through explicitly.

## Receivers

```text
R29-NF3A = ProjectiveProductOneRestrictionOfNonFanoOrder2CharacterSupport
R29-NF3B = IdentifyRhoAsExplicitCuboidProjectiveSignCharacterWithQTwist
R29-NF3C = BoundaryAttachmentMapKillingProjectiveOpenH1_32AtN2
R29-NF3D = CompareProjectiveCharacterSubspacesWithK3AndCampedelliSubcovers
```

No rational-point, Brauer, height, or population conclusion follows from these topological statements alone.

```text
CENTRAL_OPEN_B1_IMPORTED_AS_ENDPOINT=false
PROJECTIVE_OPEN_B1_N2=32
RHO_DESCENDS_TO_PROJECTIVE_CHARACTER=true
RATIONAL_POINT_OBSTRUCTION_PROVED=false
BRAUER_OBSTRUCTION_PROVED=false
POPULATION_SAVING_PROVED=false
```
