# Stage32 MB104 source note — Lu--Miyaoka singular-curve canonical-degree bound

Status: **EXTERNAL PUBLISHED INEQUALITY / RETAINED GLOBAL NECESSARY CONDITION / NO CLOSURE / NO CREDIT**

## Source

Steven Shin-Yi Lu and Yoichi Miyaoka, *Bounding curves in algebraic surfaces by genus and Chern numbers*, Mathematical Research Letters 2 (1995), 663--676, DOI `10.4310/MRL.1995.V2.N6.A1`.

For the exact formulation used here, see Theorem 1(4) as restated in Ciro Ciliberto and Claudio Fontanari, *Variations on the Weak Bounded Negativity Conjecture*, Advances in Geometry 24 (2024), 157--164, DOI `10.1515/advgeom-2023-0027`.

The restatement says: if `C` is an integral curve of geometric genus `g` on a smooth projective surface `X`, some multiple of `K_X+C` is effective, and `n` is the number of ordinary nodes and ordinary triple points of `C`, then

```text
K_X.C <= 4(g-1) + 3*c2(X) - K_X^2 + n.
```

Only this inequality is imported by the present Stage32 leaf.

## Cuboid-surface invariants

On the minimal resolution `S`, the retained Stoll--Testa source adapter gives

```text
K_S=H,
K_S^2=16,
chi(O_S)=8.
```

Noether's formula gives

```text
c2(S)=12*chi(O_S)-K_S^2=96-16=80.
```

For the uniform genus-one P5 ray

```text
D_l=7lH-4l sum_(i in Sigma) E_i,
l>=1,
```

we have

```text
K_S.D_l=H.D_l=112l.
```

If an irreducible effective member `C in |D_l|` has normalization genus `g=1`, then `K_S+C` itself is effective, so the Lu--Miyaoka hypothesis on a multiple of `K_S+C` is automatic.

## Exact necessary condition

Let `n(C)` be the number of ordinary nodes plus ordinary triple points of such a hypothetical integral genus-one carrier on the smooth resolved surface.  Substitution gives

```text
112l <= 3*80 - 16 + n(C) = 224+n(C),
```

hence

```text
n(C) >= max(0,112l-224).
```

In particular,

```text
l=1,2: no positive lower bound from this theorem,
l=3:   n(C)>=112,
l=4:   n(C)>=224,
l>=3:  n(C)>=112(l-2).
```

Thus for `l>=3` the required genus defect cannot be realized solely by one complicated high-multiplicity/unibranch singularity while having no ordinary nodes or ordinary triple points.  Any actual genus-one carrier in this ray must carry a linearly growing population of ordinary double/triple singularities.

## Relation to the adjunction defect

For an integral member of class `D_l`,

```text
p_a(D_l)=1+(D_l^2+K_S.D_l)/2
        =1+168l^2+56l.
```

If the normalization genus is one, the total delta invariant is therefore

```text
Delta_total=168l^2+56l.
```

The Lu--Miyaoka lower bound on `n(C)` is only linear in `l`, while this delta budget is quadratic.  Therefore this inequality by itself does **not** contradict the numerical genus budget and does not close any surviving support orbit.

Its value is structural: it rules out the previously available style of global compatibility witness that concentrates essentially all off-exceptional delta in one complicated cusp for arbitrarily large `l`.  A future closure can now try to charge the forced `Omega(l)` ordinary nodes/triples through the canonical embedding, fibrations, conductor, or global interpolation.

## Firewalls

- This note imports a published necessary inequality; it does not prove a new version of Lu--Miyaoka.
- `n(C)` counts ordinary nodes and ordinary triple points of the hypothetical integral curve on the smooth resolution; it is not the number of box nodes or exceptional branches.
- No contradiction is obtained from the bound alone.
- No surviving balanced support orbit is closed.
- No irreducible genus-one carrier is constructed.
- MB104, receiver, theorem, endpoint, and Perfect-Cuboid credit remain open/zero.
- No merge authorization.
