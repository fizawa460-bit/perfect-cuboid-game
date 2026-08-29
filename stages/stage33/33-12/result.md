# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_CV_TO_RULED_SUPPORT_ADAPTER_MATERIALIZED`

This checkpoint continues the exact arithmetic Hochschild--Serre assembly after the audited Stage33-11 exit. It does not close Stage33-12 or Stage33-07.

## Exact receiver state

Stage33-11 has already proved the localization connecting map exact zero on all 26 finite directions. Stage33-12 has independently linearized the full-surface finite-V4 Kummer receiver:

* `P=Br(Sbar)[2]^{G_Q}` has exact F2 dimension 10;
* `H^1(V4,Pic(Sbar)/2)` has exact F2 dimension 75;
* the missing finite restriction is therefore a literal `75 x 10` matrix;
* materialized columns remain `0/10` and finite obstruction cosets remain `0/26`.

Known Q-defined blocks, including J2, have exact HS image zero. Odd-primary global residue-lift completion is exact. The two remaining obstruction blocks are still the two-primary constant-character cokernel and the finite 26-direction block.

## J2/q1 adapter state

The named K3 basis is hostile-audited as `[J2,q1]`, with `d2(J2)=0` and `d2(q1)!=0`. The retained ambiguity witness enumerates all six elements of `GL(2,F2)`: all six survive the currently retained named d2 data, and even after the Kc kernel line `<J2>` is fixed exactly two adapters remain because `q1` and `q1+J2` have the same nonzero d2.

Certificate: `j2-q1-kc-adapter-ambiguity-witness.json`, canonical SHA256 `2d41bf2d5961fa16caf162311974a858329f2714ec1fe3838305c58e6da79ffb`.

## Named J2 Kummer-glue input

The previous exact leaf materialized the named half-divisor

`E_J2 = 2*infinity_minus - P_plus - P_minus`

from

`div(ell_J2)=4*infinity_minus-2*P_plus-2*P_minus`.

Retained certificate: `j2-named-kummer-glue-input.json`, canonical SHA256 `18e320e82c9c975f35413c1fe365889c2fa803f2ac0595609d8c6044aa32f0b5`.

## New exact progress: CV normalization to frozen ruled model

`certify_j2_cv_to_ruled_support_adapter.py` now identifies the Stage33-05 CV branch coordinates with the frozen Stage29 ruled `P1 x P1` coordinates by an exact polynomial identity.

The frozen ruled model is

```text
A1 = v1^2-u1^2
A2 = v2^2-u2^2
X  = u1*v1*A2
Y  = u2*v2*A1
B+ : X+iY=0
```

while the CV branch is

```text
Gplus(t,s)=t*(1-s^2)+i*s*(1-t^2)=0.
```

With

```text
t = u1/v1
s = u2/v2
```

one has the exact identity

```text
v1^2*v2^2*Gplus(t,s) = X+iY.
```

Thus the named J2 support is now located exactly in the frozen ruled coordinates. For `Dplus=t^2-2*t-1` the two finite support points are

```text
P_plus  = ([1+sqrt(2):1],[-i:1])
P_minus = ([1-sqrt(2):1],[-i:1]).
```

At `infinity_minus`, using `u=1/t` and `z/t^2=-1`, the reciprocal of `s` tends to zero, hence

```text
infinity_minus = ([1:0],[1:0]).
```

The finite supports satisfy `X+iY=0` exactly. The infinity support lands at the boundary/base locus of this ruled chart (`X=Y=0`), so no Stoll marked-Kc point or divisor class is assigned there without the resolved ruled-to-Kc morphism. This is an explicit firewall, not an unresolved coordinate guess.

Retained certificate: `j2-cv-to-ruled-support-adapter.json`, canonical SHA256 `63c09f6ac52cef43d529d17a48907b5818cb19d18efcced3aa35e1ccc080b061`.

## Refined exact gap

The CV side of the named bridge is no longer missing. The remaining first adapter problem is now specifically the resolved frozen-ruled-model to pinned Stoll marked-Kc divisor map on the three named supports above.

The next exact route is:

1. resolve/map `P_plus`, `P_minus`, and `infinity_minus` from the frozen ruled `P1 x P1` model into the pinned Stoll Kc marked divisor presentation, including the boundary/base-locus behavior of `infinity_minus`;
2. use the pinned `qPicK` / marked intersection interface to obtain the corresponding PicK divisor data, or an exact equivalent representation of `E_J2`;
3. apply the explicit Picard/transcendental Kummer glue to read the nonzero Kc `Br[2]` line represented by named J2;
4. replay all six `GL(2,F2)` adapters, reducing to the two compatible with the now-fixed J2 line;
5. if the same construction does not identify q1, supply one further named invariant distinguishing `q1` from `q1+J2`.

The Stoll source already supplies `PicK`, the 20-element marked generating interface, `imageinPicK(C)`, `MatStoK`, and `MatKtoS`; those are not to be reimplemented with a giant SymPy Smith computation.

Until the resolved ruled-to-marked-Kc map and Kummer glue are materialized, all six named-to-Kc adapters remain live. J2 is still not assigned to the original proper-Br2 14 coordinates or the retained P10 basis. The abstract J2 zero-defect continues to imply only the exact rank bound `rank <= 9`; it does not materialize a matrix column or a P10 linear relation.

## Current exit state

```text
ARITHMETIC_HS_D2_COMPUTED=false
GLOBAL_Q_BR0G_RESIDUE_LIFTS_COMPLETE=false
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=false
J2_Q1_KC_ADAPTER_UNIQUE=false
J2_NAMED_HALF_DIVISOR_MATERIALIZED=true
J2_CV_TO_RULED_SUPPORT_ADAPTER_MATERIALIZED=true
J2_SUPPORT_IN_RULED_P1XP1_MATERIALIZED=true
RULED_SUPPORT_TO_STOLL_MARKED_KC_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

The next exact leaf is `MATERIALIZE_RESOLVED_RULED_P1xP1_TO_STOLL_MARKED_KC_DIVISOR_MAP_ON_THREE_J2_SUPPORTS_THEN_COMPUTE_J2_KC_KERNEL_LINE`. The known Q-defined prefix, Stage33-11 zero connecting map, and zero boundary scalar adapter must not be recomputed.

All Stage33-07/08/40, theorem, endpoint, receiver, and perfect-cuboid existence/nonexistence firewalls remain closed.
