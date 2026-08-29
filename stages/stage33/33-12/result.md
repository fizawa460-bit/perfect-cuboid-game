# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_MARKED_KC_BRANCH_AND_RESOLUTION_ATTACHMENT_MATERIALIZED`

This checkpoint continues the exact arithmetic Hochschild--Serre assembly after the audited Stage33-11 exit. It does not close Stage33-12 or Stage33-07.

## Exact receiver state

Stage33-11 has already proved the localization connecting map exact zero on all 26 finite directions. Stage33-12 has independently linearized the full-surface finite-V4 Kummer receiver:

* `P=Br(Sbar)[2]^{G_Q}` has exact F2 dimension 10;
* `H^1(V4,Pic(Sbar)/2)` has exact F2 dimension 75;
* the missing finite restriction is a literal `75 x 10` matrix;
* materialized columns remain `0/10` and finite obstruction cosets remain `0/26`.

Known Q-defined blocks, including J2, have exact HS image zero. Odd-primary global residue-lift completion is exact. The two remaining obstruction blocks are still the two-primary constant-character cokernel and the finite 26-direction block.

## J2/q1 adapter state

The named K3 basis remains `[J2,q1]`, with `d2(J2)=0` and `d2(q1)!=0`. All six elements of `GL(2,F2)` still survive the currently retained named d2 data. Fixing the Kc line `<J2>` would reduce this to two; one further named orientation invariant would then distinguish `q1` from `q1+J2`.

Ambiguity certificate: `j2-q1-kc-adapter-ambiguity-witness.json`, canonical SHA256 `2d41bf2d5961fa16caf162311974a858329f2714ec1fe3838305c58e6da79ffb`.

## Named J2 input retained

The exact branch half-divisor is

`E_J2 = 2*infinity_minus - P_plus - P_minus`,

with `div(ell_J2)=2E_J2`.  The CV-to-ruled adapter is also exact:

```text
t=u1/v1,
s=u2/v2,
v1^2*v2^2 Gplus(t,s)=X+iY.
```

Its certificate is `j2-cv-to-ruled-support-adapter.json`, canonical SHA256 `63c09f6ac52cef43d529d17a48907b5818cb19d18efcced3aa35e1ccc080b061`.

## New exact progress: frozen ruled model to pinned Stoll Kc

The audited Stage29-07 anticanonical map supplies the missing geometric bridge. Put

```text
D1=v1^2-u1^2,
D2=v2^2-u2^2,
e=D1*D2,
x=2*u1*v1*D2,
p=(u1^2+v1^2)*D2,
y=2*u2*v2*D1,
q=(u2^2+v2^2)*D1.
```

Then `e^2+x^2=p^2` and `e^2+y^2=q^2`. Adding the Kc square `z^2=x^2+y^2`, comparison with the pinned Stoll equations gives the exact coordinate identification

```text
(A1,A2,A3,B1,B2,B3)_Stoll = (e,x,y,z,q,p).
```

The prior frozen coordinates satisfy `x=2X`, `y=2Y`, `z=2w`. Therefore the CV component `B+ : X+iY=0` becomes

```text
B1=0,
i*A2-A3=0.
```

This is exactly the second curve in Stoll's first `C2sK` pair, hence `C2sK[2]=CsK[22]`. The named CV branch itself is now a pinned marked Stoll Kc curve; this is no longer an unnamed birational image.

The three J2 support images are exact:

```text
P_plus_K  = [-1:1:i:0:0:sqrt(2)],
P_minus_K = [-1:1:i:0:0:-sqrt(2)],
P_inf_K   = [1:0:0:0:-1:-1].
```

The first two have Kc Jacobian rank 3 and are smooth. `P_inf_K` has rank 2 and is one of the Kc A1 singularities.

## New exact progress: resolution attachment at J2 infinity

In the affine chart `A1=1` around `P_inf_K`, write

```text
a=A2,
b=A3,
c=B1.
```

The local tangent cone is

```text
c^2=a^2+b^2.
```

The marked B+ branch has `c=0` and `i*a-b=0`; consequently its strict transform meets the exceptional conic over `P_inf_K` in the exact tangent direction

```text
[a:b:c]=[1:i:0].
```

Thus the geometric exceptional attachment is materialized. What is not yet materialized is the algorithmic `ptsK` order index used by the pinned Magma presentation and therefore the corresponding explicit `qPicK` exceptional coordinate.

Certificate: `j2-ruled-to-stoll-marked-kc-support.json`, canonical SHA256 `881d2637c83bcae5d7bdfe9cf534baea7ad15b983719f7a482d3b7240fe8c510`.

## Important Kummer-glue firewall

`E_J2` is a degree-zero divisor on the genus-one branch normalization. Its support points are not divisors on the K3 surface and must not be inserted directly into `PicK` as though they were K3 divisor classes.

The exact marked-curve/support bridge now reduces the remaining first orientation problem to the genuine Kummer glue:

1. identify the exceptional divisor over `P_inf_K=[1:0:0:0:-1:-1]` in the pinned `ptsK`/`qPicK` ordering;
2. combine that resolved branch data with `CsK[22]` and the branch Jacobian 2-torsion class `E_J2`;
3. materialize the exact map from this named branch-Jacobian 2-torsion datum to the Kc Picard discriminant/Brauer `2`-torsion coordinate;
4. fix the Kc line represented by named J2 and replay the six `GL(2,F2)` adapters (`6 -> 2` expected once the line is fixed);
5. then provide one additional named orientation invariant for `q1` versus `q1+J2` unless the same glue computation identifies q1 too.

The historical `derive_kc_discriminant_from_split.py` confirms the Kc discriminant carrier is `Z/4 direct_sum Z/8` and records the audited 2-dimensional invariant Br[2] / one-dimensional HS kernel interface, but it does not itself identify named J2 with one discriminant coordinate. Its deleted transient `kc-picard-maps.json` is not treated as available evidence.

## Current exit state

```text
ARITHMETIC_HS_D2_COMPUTED=false
GLOBAL_Q_BR0G_RESIDUE_LIFTS_COMPLETE=false
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=false
J2_Q1_KC_ADAPTER_UNIQUE=false
J2_NAMED_HALF_DIVISOR_MATERIALIZED=true
J2_CV_TO_RULED_SUPPORT_ADAPTER_MATERIALIZED=true
J2_BRANCH_IDENTIFIED_WITH_STOLL_CSK22=true
J2_THREE_STOLL_KC_SUPPORT_IMAGES_MATERIALIZED=true
J2_INFINITY_EXCEPTIONAL_GEOMETRIC_ATTACHMENT_MATERIALIZED=true
J2_INFINITY_STOLL_PTSK_ORDER_INDEX_MATERIALIZED=false
J2_INFINITY_QPICK_EXCEPTIONAL_COORDINATE_MATERIALIZED=false
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

The next exact leaf is `MATERIALIZE_STOLL_PTSK_INDEX_AND_QPICK_COORDINATE_FOR_J2_INFINITY_EXCEPTIONAL_THEN_BRANCH_JACOBIAN_2TORSION_TO_KC_PICARD_DISCRIMINANT_KUMMER_GLUE`. No giant SymPy Smith recomputation is authorized or needed.

All Stage33-07/08/40, theorem, endpoint, receiver, and perfect-cuboid existence/nonexistence firewalls remain closed.
