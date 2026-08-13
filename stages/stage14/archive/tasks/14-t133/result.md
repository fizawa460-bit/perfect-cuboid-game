# Stage14-t133 — open the fixed-projective-class scalar norm weight into one canonical-sector fiber

## Status

`COMPLETE_FIXED_CLASS_WEIGHT_CANONICAL_SECTOR_FIBER_OPENING`

Consumes merged `Stage14-t132`, merged `Stage14-t91/t118/t119/t121/t122/t124/t125`, and merged `Stage14-Work-btX32`.

Fix the t132 localized packet, including the already frozen exceptional multiplier/orientation data, with

```text
c_* in G(d),
q_* = c_*^(-1)[a]^(-1),
T_* = sum_n W_{c_*}(n) K_n(q_*),
M_* = 1/|G| sum_n W_{c_*}(n)|P_n|,
T_* <= B^(-delta) M_*
```

for some fixed positive depletion exponent after the t132 localization.

The only cofactor weight is

```text
W_{c_*}(n)
 = #{gamma physical nonboundary primitive : N(gamma)=n, [gamma]=c_*}.
```

Merged t121--t124 prove that, off the rejected D4 boundary, the remaining ell-independent physical selector is exactly finite Gaussian sign/canonical normalization and that every primitive D4 orbit has exactly one representative in the frozen strict physical chamber.

Let `D` be the finite set of D4 normalization states (`|D|=O(1)`).  For each physical canonical cofactor gamma there is a unique state `nu in D` which maps a raw primitive Gaussian representation `z` to gamma.  Define

```text
W_{c_*,nu}(n)
 := #{gamma counted by W_{c_*}(n) whose normalization state is nu}.
```

Then exactly

```text
W_{c_*}(n)=sum_{nu in D} W_{c_*,nu}(n),
T_*=sum_nu T_nu,
M_*=sum_nu M_nu,
```

with all pieces nonnegative and with the same prime count `K_n(q_*)` / principal prime mass attached to each norm.

Because `|D|=O(1)`, the same nonnegative localization used in t132 freezes one state `nu_*` such that

```text
M_{nu_*} >= M_*/O(1),
T_{nu_*} <= B^(-delta+o(1)) M_{nu_*}.
```

No fixed exponent is lost.

For this fixed normalization state, the raw representation lies in one fixed open D4 sector `S_{nu_*}`.  The D4 action on projective classes is explicit: multiplication by a Gaussian unit and optional conjugation.  Therefore the canonical condition `[gamma]=c_*` becomes one fixed raw projective class condition

```text
[z]=c_raw
```

for a fixed `c_raw in G(d)` determined only by `(c_*,nu_*)`.

Hence, after freezing `nu_*`, the scalar weight is exactly

```text
W_raw(n)
 = #{z in Z[i] :
       N(z)=n,
       z primitive,
       z in S_{nu_*},
       [z]=c_raw,
       z has the already frozen exceptional packet}.
```

The exceptional packet may equivalently be written as

```text
z=gamma_E z_G,
N(z)=m*N(z_G),
gcd(N(z_G),E_U)=1,
```

with every odd prime of `N(z_G)` split automatically by Gaussian primitivity.

This is an exact arithmetic opening of `W_{c_*}(n)`: the weight is not arbitrary.  It is a primitive Gaussian norm-representation multiplicity in one fixed broad sector and one fixed projective residue class, with only frozen exceptional local data.

The stage does not yet lift the projective class to ordinary Gaussian residue classes, so the receiver is sharpened but not declared materially changed until that lift and the reciprocal hyperbola are frozen.

```text
FIXED_CLASS_WEIGHT_DECOMPOSES_BY_D4_NORMALIZATION_STATE=true
ONE_NORMALIZATION_STATE_FREEZABLE_WITHOUT_POWER_LOSS=true
FIXED_NORMALIZATION_STATE_GIVES_FIXED_OPEN_GAUSSIAN_SECTOR=true
CANONICAL_PROJECTIVE_CLASS_BECOMES_FIXED_RAW_PROJECTIVE_CLASS=true
FIXED_CLASS_WEIGHT_IS_PRIMITIVE_GAUSSIAN_SECTOR_PROJECTIVE_REPRESENTATION_COUNT=true
ARBITRARY_SCALAR_WEIGHT_MODEL_SUPERSEDED=true
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
PREFERRED_RECEIVER=SharedUFixedGaussianSectorProjectiveCofactorNormWeightAgainstReciprocalFixedProjectivePrimeClassDepletion
NEXT=Stage14-t134
```
