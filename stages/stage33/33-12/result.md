# Stage33-12 arithmetic-HS closure / Stage33-07 recertification

Status: `CURRENT_INTERNAL_33_13_FINITE_V4_KUMMER_MATRIX`

Stage33-12 is the contract-level final repair child for reopened Stage33-07. It remains open until arithmetic HS, global-Q residue lifts, complete relevant Q-defined class inventory, and hostile parent recertification are all exact.

```text
Stage33 progress = 6/11
Stage33-05 reclosed = true
Stage33-09 closed = true
Stage33-10 closed = true
Stage33-11 closed hostile-pass = true
Stage33-12 closed exact = false
Stage33-07 closed = false
Stage33-08 released = false
```

## Closed prerequisite interfaces

### Stage33-09 Picard transport

```text
PICARD_EQUIVARIANT_TRANSPORT_CLOSED=true
canonical_sha256=6c3ff8f7ca7d1bbd4084da0cc77ca6d43b31b32566a3bbb2c2103b7c2e9548b7
```

### Stage33-10 absolute-H1 receiver

```text
absolute_h1_receiver_exact=true
kernel_galois_relevant_contribution_accounted=true
stage33_11_domain_and_codomain_well_defined=true
canonical_sha256=4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f
```

### Stage33-11 arithmetic localization

The independent 33-11g hostile audit gives

```text
ARITHMETIC_LOCALIZATION_CONNECTING_MAP=COMPUTED_EXACT_ZERO_MAP
CONNECTING_COLUMNS_EXACT_AUDITED=26/26
UNRESOLVED_CONNECTING_COLUMNS=0
STAGE33_11_HOSTILE_AUDIT=PASS
STAGE33_11_CLOSED_EXACT=true
canonical_sha256=233be042e92010be169206df1193f25375ee9fd768f7fb3eebb9eb696389632e
```

### Stage33-05 K3 Br[2] arithmetic classification

The corrected named-J2 repair exposed a stronger exact closure route. The complete invariant K3 block is

```text
Br(Kc_bar)[2]^G_Q = span_F2{J2,q1}.
```

Both basis directions have nonzero, independent restricted HS d2 classes. With ct-fixed tests `[CsK[2],CsK[5]]` the pairing matrix is

```text
[[1,1],
 [1,0]]
```

and has determinant `1 mod 2`. Hence

```text
GLOBAL_D2_KERNEL_DIMENSION_F2=0
Q_RELEVANT_SURVIVING_DIM=0
K3_BR2_Q_SURVIVING_CLASS_LIST=[]
EXACT_ZERO_SURVIVAL_CERTIFICATE=true
STAGE33_05_HOSTILE_AUDIT=PASS
STAGE33_05_UNIT_CLOSED=true
canonical_sha256=4e9f20c1f753bb63134207422b097c1985ce3edd6be87f7f41ba8afa316e7dc9
```

Corrected geometric `J2=(f2,1)` remains nonzero, but `d2(J2)!=0`; there is no corrected-J2 Q-defined Brauer preimage. The revoked historical `ell_J2` is not restored.

## What the zero-survival result changes

The old Stage33-12 dependency that demanded

```text
corrected J2 d2=0 -> Q-defined J2 preimage
```

is retired. Stage33-12 consumes the complete K3 arithmetic classification, and exact zero survival is valid.

This closes the K3 contribution only. It does **not** close the independent full-surface/global-Q arithmetic-HS obligations required by the Stage33-12 contract.

## Remaining Stage33-12 contract

Authoritative exit still requires

```text
ARITHMETIC_HS_D2_COMPUTED=true
GLOBAL_Q_RESIDUE_LIFT_COMPLETION=true
COMPLETE_RELEVANT_Q_DEFINED_CLASS_INVENTORY_FOR_FROZEN_STAGE33_BRAUER_SCOPE=true
STAGE33_07_HOSTILE_RECERTIFICATION=PASS
STAGE33_12_EXIT_EXACT=true
```

The next logical internal branch is the finite-V4 Kummer restriction on the remaining proper full-surface receiver:

```text
internal branch = 33-13 FINITE-V4-KUMMER-MATRIX
P = Br(Sbar)[2]^{G_Q}
DIM_F2(P)=10
DIM_F2(H^1(V4,Pic(Sbar)/2))=75
required exact matrix = 75x10
required exact columns = 10/10
```

After that, 33-14 must close the finite HS cosets/two-primary constant block, and 33-15 must assemble global-Q residue lifts, the complete class inventory, and hostile-recertify parent Stage33-07.

## Current exact leaf

```text
MATERIALIZE_CORRECTED_J2_IN_CURRENT_PROPER_BR2_F2_14
THEN_SOLVE_ITS_RETAINED_10D_COORDINATE
THEN_PLACE_THE_LOCKED_WEIGHT15_75D_TARGET
```

## Firewalls

```text
historical ell_J2 reused = false
corrected J2 Q-defined preimage = false
Stage33-05 reclosed = true
Stage33-12 closed exact = false
Stage33-07 closed = false
Stage33-08 released = false
theorem / receiver / endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```

## J2 ct six-support full-Pic64 transport

The six support rows required by the corrected-J2 ct defect were extracted
from the pinned Stoll `MatBigKtoBig` preimage map without regenerating the
historical full `20 x 64` Kc map. Each row was independently reconstructed
from the retained Stage32 all-140 known-class marking and transported through
the certified Stage33-09 INDLIST-to-Magma basis bridge.

```text
BIGK_SUPPORT=[26,35,42,47,49,52]
FULLPIC64_PULLBACKS_EXACT=6/6
CT_SUM_INDLIST_MOD2_WEIGHT=24
CT_SUM_HISTORICAL_MAGMA_MOD2_WEIGHT=8
HISTORICAL_FULL_KC20_TO_FULLPIC64_REGENERATED=false
FIRST_EXACT_75D_KUMMER_COLUMN_MATERIALIZED=false
canonical_sha256=592704594d6d26f9e0b0b2ba529d50c34fd801cede779b4e42b1cf775b63a96d
```

## J2 actual cc Cech-overlap parity

The fixed corrected Cech representative supplies the global overlap
zero-cochain `c=B1/(2*t)`, not merely the generic statement that a symbol is a
square. The literal rank-two basis change is

```text
Y=[[0,c],[c,0]]
G=diag(c,1)
G*Y*G^-1=[[0,c^2],[1,0]]
det(G)=c
```

At every prime divisor of the smooth resolved surface, including every
resolution exceptional, the determinant order is `ord_D(c)`. The complete
Cartier divisor is therefore the principal divisor `div(c)`, so the actual cc
class is zero already in integral Pic and hence zero in marked Pic/2 and both
full Pic64 coordinate systems.

```text
ACTUAL_CC_CECH_OVERLAP_MATERIALIZED=true
ACTUAL_CC_INTEGRAL_PIC_CLASS=0
ACTUAL_CC_FULLPIC64_MOD2=0
FIRST_EXACT_75D_KUMMER_COLUMN_MATERIALIZED=false
canonical_sha256=82ac2b6fe8d023c915e9cf3bb8ff38d4782dbec47f98e2593f964ea020ccc6fd
```

## Named J2 finite-V4 H1 target

The exact pair `(cc defect, ct defect)=(0, ct_fullPic64)` satisfies all three
normalized V4 cocycle equations in the retained historical-Magma Pic64 basis.
Reduction modulo the locked coboundary space gives a unique nonzero vector in
the retained 75D H1 quotient basis.

```text
NAMED_J2_V4_H1_TARGET_MATERIALIZED=true
NAMED_J2_V4_H1_TARGET_WEIGHT=15
NAMED_J2_V4_H1_TARGET_NONZERO=true
NAMED_J2_RETAINED_10D_SOURCE_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_COLUMNS_MATERIALIZED=0/10
canonical_sha256=4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3
```

## Named CV `d=2` semantic orientation — exact

The remaining three-way semantic ambiguity is now closed using retained exact
geometric credit rather than a guessed Kc automorphism. Stage33-05 retains the
corrected named-J2 twisted transcendental kernel with Gram `diag(8,16)` and
minimum norm `8`. In the exact kernel fingerprint table for
`T(Kc)=<4> direct_sum <8>`, minimum norms `4,8,12` distinguish the three
nonzero marked Brauer functionals, so minimum norm `8` uniquely selects
`beta1=[1,0]`.

This does **not** canonically identify `Br[2]` with discriminant 2-torsion. In
the shared marked transcendental basis `(t1,t2)`, the explicit coordinate
adapter sends `beta1=[1,0]` to `t1 mod 2T`, and the fixed map
`T/2T -> A_T[2]`, `x -> x/2`, sends it to `t1/2`. Doubling the already-fixed
anti-isometry image of `t1/4` gives exactly the semantic half-lattice vector
`u1/2`. Therefore

```text
NAMED_CV_J2_FIXED_MARKED_KC_COORDINATE_F2=[1,0]
NAMED_CV_J2_SEMANTIC_DISCRIMINANT_LABEL=u1
SEMANTIC_CANDIDATE_COUNT=1
NAMED_J2_SEMANTIC_ORIENTATION_MATERIALIZED=true
NAMED_J2_RETAINED_10D_SOURCE_COORDINATE_MATERIALIZED=false
FIRST_EXACT_75D_KUMMER_COLUMN_MATERIALIZED=false
canonical_sha256=0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e
```

## Semantic `u1` to full-surface Smith normalization — exact boundary

Targeted source tracing fixes the semantic half-lattice numerator without
reopening the named orientation. In the semantic PicK basis, `u1` has support
positions `[1,2,5,6,14,15]`; the locked curve-slot marking sends these exactly
to pinned Stoll rows `BigK[2], BigK[4], BigK[9], BigK[10], BigK[47], BigK[49]`.
This is distinct from the six ct-defect support rows.

For their integral full-surface pullback numerator `n_S`, the Stage33-07 Smith
convention fixes the factor-two normalization:

```text
z=(n_S*pmPic)/2
D,U,V=SmithForm(pmPic)
y=z*V
mods=[2,2,2,2,4,4,4,4,4,4,8,8,8,8]
bit_i=(y_i/(mods_i/2)) mod 2
```

Thus neither an arbitrary factor two nor an arbitrary 14D adapter remains.
The current branch retains the required rows 47 and 49, but not rows 2, 4, 9,
or 10. The historical full `MatKtoS` artifact and the retained full-surface
Magma Smith right transform `V` are also unavailable. Therefore the exact
14D source coordinate cannot yet be materialized locally.

```text
SEMANTIC_U1_BIGK_SUPPORT=[2,4,9,10,47,49]
REQUIRED_PULLBACK_ROWS_RETAINED=[47,49]
REQUIRED_PULLBACK_ROWS_MISSING=[2,4,9,10]
NORMALIZATION_FORMULA_EXACT=true
PROPER_BR2_14D_COORDINATE_MATERIALIZED=false
RETAINED_10D_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_COLUMNS_MATERIALIZED=0/10
canonical_sha256=9a8c9bcc420a7ad60bb6d71326bc04000da676ec4bb222e0cc4266c2aadf3d7f
```

At this checkpoint the next exact datum was the four missing pinned pullback
rows together with the retained Smith `V`. The replay below resolves that
numeric blocker and records the newly exposed dual-functional interface. This
is not the superseded 103D adapter ambiguity. No guessed coordinate, fake zero
column, Stage33-12 closure, parent reclosure, or downstream release is claimed.

## Semantic `u1` full-surface Smith source — exact

The six pinned pullback rows and literal retained Magma Smith transform have
now been materialized in one source-locked Actions replay. The normalization
above gives

```text
FULL_SURFACE_A_T_2_COORDINATE_F2=[0,0,0,0,0,0,0,1,0,1,0,1,1,0]
FULL_SURFACE_A_T_2_COORDINATE_WEIGHT=4
REQUIRED_PULLBACK_ROWS_MISSING=[]
RETAINED_MAGMA_SMITH_V_MATERIALIZED=true
canonical_sha256=ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec
```

The ordered proper-Br2 basis is the dual of the ordered `T/2T` basis; it is
not the same vector space. Copying the 14 `A_T[2]` coefficients into that dual
basis fails `cc` invariance with exact defect
`[1,0,1,1,0,0,0,0,0,0,0,0,0,0]`. The finite discriminant pairing also sends
this `A_T[2]` element to the zero covector, so that pairing cannot be promoted
as the named J2 functional or as a zero Kummer column.

```text
PROPER_BR2_14D_COORDINATE_MATERIALIZED=false
RETAINED_10D_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_COLUMNS_MATERIALIZED=0/10
NEXT=MATERIALIZE_CORRECTED_KC_BRAUER_FUNCTIONAL_PULLBACK_EVALUATIONS_ON_RETAINED_FULL_SURFACE_T_MOD_2_SMITH_BASIS
canonical_sha256=f5d1336e21dd5563ec6466811b5e1c3cacc6def17e4dbe4968023d9bd3756399
```

This supersedes only the prior numeric rows/Smith-V blocker. It does not
reopen the named orientation or the historical 103D ambiguity, and it restores
no Q-defined descent, closure, release, theorem, receiver, or endpoint credit.


## Named J2 order-4 Brauer lift reduction — exact

The remaining proper-Br2 adapter is lift-sensitive. The marked class is `beta1=t1/8`, so the relevant transported discriminant datum is the order-4 generator `t1/4`, not only its doubled order-2 class `u1=t1/2`. In the semantic PicK basis, `t1/4` uses BigK rows `[2,4,9,10,20,35,39,47,49,67]`; the prior u1 replay already materialized `[2,4,9,10,47,49]`. The only new rows are therefore `[20,35,39,67]`. Each has coefficient `2/4=1/2`, so doubling makes it integral and it disappears modulo PicK, exactly explaining why the previous order-2 replay could not see this lift parity.

```text
ORDER4_REQUIRED_BIGK_ROWS=[2,4,9,10,20,35,39,47,49,67]
ORDER4_REUSE_BIGK_ROWS=[2,4,9,10,47,49]
ORDER4_MISSING_BIGK_ROWS=[20,35,39,67]
CANDIDATE_ROUTE=n4 -> z4=(n4*pmPic)/4 -> y4=z4*V -> y4_nontrivial mod2
PROPER_BR2_14D_COORDINATE_MATERIALIZED=false
RETAINED_10D_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_COLUMNS_MATERIALIZED=0/10
canonical_sha256=a524121930e1c712bd8d8220415ef1836b11cd6eb11f2bb44f70dc844f6d85b0
```

Promotion remains blocked until `z4` is integral, the resulting 14-bit parity vector is fixed by the current proper-Br2 `cc/ct` actions, and it lies in the retained 10D domain. No closure, release, theorem, receiver, or endpoint credit is restored here.
