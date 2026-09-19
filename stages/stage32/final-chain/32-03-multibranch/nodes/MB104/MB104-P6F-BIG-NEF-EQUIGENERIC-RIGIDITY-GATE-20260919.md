# MB104 P6F — big-nef genus-one equigeneric rigidity gate — 2026-09-19

Status: **PRE-AUDIT SOURCE-COMPLETE GLOBAL RIGIDITY / NO CREDIT**

## Target

P6E proves that the hostile full-span ray

```text
P = 7H - 4 sum_(i in Sigma) E_i,
Sigma = 0000093f442e,
P^2=336,
H.P=112
```

is big and nef. The next question was whether positivity plus a T-smoothness/equisingular theorem could force enough independent singularity conditions to exclude an integral genus-one member of `|lP|`.

The deformation-theoretic gate goes in a different direction: any such genus-one member would be equigenerically rigid.

## Published deformation-theory input

Thomas Dedieu and Edoardo Sernesi, *Equigeneric and equisingular families of curves on surfaces*, Publicacions Matematiques 61 (2017), 175--212, DOI `10.5565/PUBLMAT_61117_07`.

For an integral curve `C` on a smooth surface `X`, with normalization

```text
nu:Cbar -> C,
phi:Cbar -> X,
```

and adjoint/conductor ideal `A`, their Lemma 3.1 gives

```text
H^0(C, A tensor O_C(C))
  ~= H^0(Cbar, omega_Cbar tensor phi^* omega_X^{-1}).
```

Their Proposition 3.2(iii) states that this space contains the reduced tangent cone to the equigeneric locus at `[C]`. Hence

```text
dim_[C] V_g <= h^0(Cbar, omega_Cbar tensor phi^* omega_X^{-1}).
```

Proposition 3.2(ii), together with the inclusion of the equisingular ideal `I` into `A`, also puts the equisingular tangent space inside the same vector space.

## Exact substitution for the hostile ray

Assume only that an integral curve

```text
C in |lP|, l>=1
```

has normalization `E` of genus one.

Then

```text
omega_E ~= O_E,
K_S.C = H.(lP) = 112l.
```

Therefore

```text
deg(phi^* omega_S^{-1}) = -K_S.C = -112l < 0.
```

A line bundle of negative degree on the elliptic normalization has no nonzero global section, so

```text
H^0(E, omega_E tensor phi^*omega_S^{-1}) = 0.
```

Consequently

```text
H^0(C, A tensor O_C(C)) = 0.
```

The reduced tangent cone to the genus-one equigeneric locus is zero, and the local equigeneric dimension at `[C]` is zero. The equisingular tangent space is also zero.

Thus:

```text
any hypothetical integral genus-one carrier in |lP| is locally isolated
inside the equigeneric locus,
and admits no nonzero first-order equisingular deformation.
```

This conclusion does not use the diagonal A1 condition `(A,B)=(1,1)` and does not assume the P6D product-cover packet beyond the class and genus.

## Interaction with the retained singularity bounds

The retained Lu--Miyaoka adapter gives for the same hypothetical genus-one curve

```text
n_ordinary_node_or_triple >= max(0,112l-224).
```

So for `l>=3`, a carrier would simultaneously have a linearly growing population of ordinary nodes/triples and nevertheless be equigenerically isolated.

This is a stronger structural description than a bare expected-dimension heuristic, but it is not a contradiction.

## Why generic T-smoothness does not close P6 here

The P6E plan asked whether big-nef positivity could turn the singularity count into a regular/T-smooth family and hence an emptiness statement. The Dedieu--Sernesi calculation shows the relevant genus-one locus, if nonempty, has no nonzero reduced equigeneric tangent direction at all.

Therefore a positive-dimensional-family argument is the wrong target. A successful theorem must exclude isolated genus-one members themselves; it cannot merely show that general equigeneric deformations are regular or nodal.

The retained Miyaoka 2008 canonical-degree theorem also does not supply such an exclusion: its uniform genus-one degree bound requires `K_S^2>c2(S)`, whereas here

```text
K_S^2=16 < c2(S)=80.
```

The archive already verifies that the all-singularity orbibundle inequality is strictly satisfied for every `l` on this ray.

## Disposition

```text
big-nef negative-curve route       = CLOSED NEGATIVE by P6E
positive-dimensional equigeneric route = CLOSED NEGATIVE by P6F
hypothetical genus-one carrier     = EQUIGENERICALLY ISOLATED
carrier existence                  = OPEN
```

The next useful gate must attack isolated carriers using packet-specific global structure. The strongest retained extra structure is now P6D2: automatic odd-contact equality, connected full-deck product pullback, and two degree-`56l` etale factor maps. A one-factor scalar Hurwitz count is not enough; the next probe should test genuinely two-factor/common-cover coupling.

## Source locks

Historical MB104 archive exact head:

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- `LU-MIYAOKA-GENUS1-SINGULARITY-COUNT-SOURCE-NOTE.md` blob `82e247159d736f92aa1382a469fa1d46a81dbae0`;
- `MIYAOKA2008-ORBIBUNDLE-GENUS1-WALL.md` blob `f59898039325b8a919f195ed9b0a491885e8232d`.

Current compact source:

- P6E certificate blob `9579b0c2b909310b426cd4a1539b3d4c2ede0248`.

External publication lock:

```text
Dedieu--Sernesi, Publ. Mat. 61 (2017), 175--212,
DOI 10.5565/PUBLMAT_61117_07,
Lemma 3.1 and Proposition 3.2.
```

## Firewalls

```text
finite_degree_window_proved=false
MB104_complete=false
R29_LG2_MB_discharged=false
receiver_credit=false
effectivity_final_milestone_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
