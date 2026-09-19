# MB104 Z4'+Z3 — global forbidden support locus for the conductor/different — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT GLOBAL SUPPORT REDUCTION / NO CREDIT**

## Input

For a hypothetical integral genus-one carrier on one of the three surviving balanced supports,

```text
C in |lP|, l>=1,
P = 7H - 4 sum_(i in Sigma) E_i,
|Sigma|=14,
nu:E -> C,
```

use only:

1. the complete P-null locus from Z3/Z40B;
2. the exact supported exceptional contact multiplicity one from Z33;
3. the Z4' local-intersection consequence that every supported exceptional contact is a smooth
   point of C and hence is outside the different support.

## 1. Unsupported exceptional curves are not met by C

For every unsupported exceptional curve `E_j`,

```text
P.E_j=0.
```

Since `C~lP` and `C` is integral and distinct from `E_j`,

```text
C.E_j=0.
```

Intersection multiplicities of two distinct effective integral curves on the smooth surface are
nonnegative.  Therefore

```text
C cap E_j = empty
```

for all 34 unsupported exceptional curves.

## 2. Supported exceptional curves are met only at smooth carrier points

For every supported `E_i`, Z33 gives total contact multiplicity one at each normalization branch.
The Z4' local-intersection lemma gives

```text
I_p(C,E_i)=1 => C is smooth at p.
```

Hence the different has no support over any supported exceptional contact.

There are 14 supported and 34 unsupported exceptional curves, so every point of
`Supp(Delta)` lies away from the full 48-curve exceptional locus.

## 3. Zero-pairing elliptic quartics are also disjoint from C

Every zero-pairing elliptic quartic `Q` in the complete null locus satisfies

```text
P.Q=0.
```

Again, `C~lP` is integral and is not one of these quartics, so

```text
C.Q=0
```

and positivity of local intersection multiplicities gives

```text
C cap Q = empty.
```

Thus the carrier itself misses every nonexceptional component of `Null(P)`.

## 4. Exact forbidden locus

Let

```text
Exc_48 = union of all 48 exceptional curves,
Q_null = union of the zero-pairing elliptic quartics.
```

Then

```text
Supp(Delta) subset
S \ (Exc_48 union Q_null).
```

More precisely:

- C is disjoint from the 34 unsupported exceptional curves;
- C meets the 14 supported exceptional curves, but only at smooth points of C;
- C is disjoint from every null elliptic quartic.

Therefore every singular point of the strict-transform carrier, and every point carrying
conductor/different mass, lies in the smooth open surface obtained by deleting the entire
exceptional locus and the null quartics.

## 5. Blowdown interpretation

Let `pi:S -> Sbar` be the resolution morphism of the cuboid surface.  Since `pi` is an
isomorphism away from the exceptional curves, every singular point of C lies in the locus where
`pi` is an isomorphism.

Consequently the unknown quadratic singularity scheme is not a resolution-node phenomenon:
it lives on the smooth locus of the original cuboid surface.

This is stronger than merely saying that the different is not supported on `B_node`.

## 6. Consequences for the candidate routes

### Conductor / adjoint ideal

Any adjoint-ideal or conductor-ideal argument intended to capture the quadratic mass may be
worked on the smooth open locus of the original surface.  Exceptional-node local algebra cannot
supply the missing quadratic mass.

### Cayley--Bacharach / singularity-scheme postulation

The relevant zero-dimensional singularity scheme, if one can source-lock it, is supported away
from all 48 resolved nodes and away from the complete P-null quartic boundary.  Thus any future
postulation theorem should be formulated for an interior zero-scheme, not for fat points on the
exceptional boundary.

### Z12/BTVA

The 112l explicit supported contacts are boundary data but are not singularity-scheme points.
No part of the BTVA cubic deficit may be repaired by simply charging those contacts as conductor
length.

## Firewalls

```text
different_avoids_all_exceptional_curves=true
carrier_disjoint_from_unsupported_exceptionals=true
supported_exceptional_contacts_smooth=true
carrier_disjoint_from_null_quartics=true
different_supported_on_original_surface_smooth_locus=true
positive_singularity_locus_finite_description=false
quadratic_mass_localized_to_controlled_finite_locus=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
