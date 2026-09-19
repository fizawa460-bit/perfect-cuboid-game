# MB104 Z4' — conductor/different disjointness from supported exceptional contacts — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT LOCAL-INTERSECTION REDUCTION / NO CREDIT**

## Scope

Assume the retained dangerous packet

```text
Sigma = 000707000f0f,
C in |lP|,
P = 7H - 4 sum_(i in Sigma) E_i,
nu:E -> C,
g(E)=1.
```

Retain the already exact Z33/Z4'+Z5' facts:

```text
B_node = div_E(nu^*h)
       = nu^*(sum_(i in Sigma) E_i)
```

and every supported exceptional contact has multiplicity one.

Let `Delta` be the normalization conductor/different divisor defined by

```text
nu^* omega_C ~= omega_E(Delta).
```

The existing Abel-class identity is

```text
O_E(Delta) ~= O_E((3l+1) B_node).
```

This note determines what can and cannot happen at the support points of `B_node`.

## 1. Local intersection lemma

Let `S` be a smooth surface, `C subset S` an integral Cartier curve, and `D subset S`
a smooth curve not contained in `C).  At a point `p in C intersect D`, if

```text
I_p(C,D)=1,
```

then `C` is smooth at `p`.

Reason: choose regular parameters `(x,y)` in the two-dimensional regular local ring
`O_{S,p}` with `D=(x)`.  Write `C=(f)`.  Then

```text
I_p(C,D)=length k[[x,y]]/(x,f)=ord_y f(0,y).
```

If this length is one, the image of `f` modulo `(x)` has a nonzero linear term in `y`.
Hence `f notin m_p^2`, so the Cartier curve `C` has multiplicity one and is regular at `p`.

Equivalently, a singular Cartier curve on a smooth surface has local multiplicity at least two,
and its intersection multiplicity with any smooth test curve through that point is at least two.

## 2. Apply to every supported exceptional contact

For every point `q in Supp(B_node)`, the image `p=nu(q)` lies on one supported exceptional
curve `E_i`, and the retained equality packet gives local exceptional contact multiplicity one:

```text
I_p(C,E_i)=1.
```

The exceptional curve `E_i` is smooth and is not a component of the integral carrier `C`.
Therefore the local lemma gives

```text
C is smooth at p.
```

Thus normalization is an isomorphism near `p), the conductor is the unit ideal there, and the
different coefficient at `q` is zero.

Hence the exact support statement is

```text
Supp(Delta) cap Supp(B_node) = empty.
```

In particular, the previously open possibility

```text
Supp(Delta) subset Supp(B_node)
```

is not merely unproved: it is impossible unless `Delta=0`, which cannot occur for `l>=1`
because `deg Delta = 336l^2+112l > 0`.

## 3. Combined Abel-class constraint

The retained Z4'+Z5' identity therefore sharpens to the pair

```text
O_E(Delta) ~= O_E((3l+1) B_node),
Supp(Delta) cap Supp(B_node) = empty.
```

So `Delta` is a large effective divisor in the Abel class of a positive multiple of the explicit
node divisor, but all of its support is forced away from those node-preimage points.

This does not contradict elliptic divisor theory by itself: a positive-degree line bundle on an
elliptic curve has many effective representatives, and a representative linearly equivalent to
`(3l+1)B_node` can avoid the finite set `Supp(B_node)`.

## 4. e=4 specialization

For the exact e=4 packet,

```text
B_node = B_z + B_w,
O_E(B_z) ~= O_E(B_w) ~= M,
O_E(Delta) ~= M^(6l+2).
```

The disjointness upgrades this to

```text
Supp(Delta) cap (Supp(B_z) union Supp(B_w)) = empty.
```

Thus neither saturated distinguished half-fiber carries conductor/different mass.

This is a useful negative localization theorem: any future simultaneous-invariant or
Cayley--Bacharach route must act on singularities away from the 112l explicit supported contacts,
not on those contacts themselves.

## 5. Consequence for Z4' / Z12 routing

The exact conductor mass is therefore split as follows:

```text
degree known exactly:      deg Delta = 336l^2+112l,
Abel class known exactly:  [Delta] = (3l+1)[B_node],
forbidden support known:   Supp(B_node),
positive support location: still unknown.
```

Hence a successful surface-side localization theorem must produce a **second controlled locus**
away from the supported exceptional contacts.  Adjoint/conductor ideals restricted only to the
supported exceptional divisor cannot carry the quadratic mass.

For Z12/BTVA this is also a firewall: the explicit 112l supported branches cannot be charged as
singularity-scheme length merely from the conductor identity, because the carrier is smooth at
all of them.

## Firewalls

```text
conductor_different_Abel_class_exact=true
supported_exceptional_contacts_smooth=true
different_disjoint_from_B_node=true
different_disjoint_from_Bz_Bw_in_e4=true
different_support_localized_positive_locus=false
e4_excluded=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```

## Source note

The local argument is elementary in the regular local ring of the smooth surface and does not
depend on an analytic classification of the carrier singularities.  It is compatible with the
standard intersection-multiplicity formalism for proper intersections on nonsingular varieties
and with the standard fact that the normalization/conductor is trivial over the normal (hence
smooth, for an integral curve) locus.
