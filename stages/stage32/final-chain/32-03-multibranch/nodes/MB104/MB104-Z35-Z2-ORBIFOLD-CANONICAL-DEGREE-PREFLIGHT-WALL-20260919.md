# MB104 Z35 / Z2 — orbifold/open canonical-degree theorem preflight wall — 2026-09-19

Status: **PRE-AUDIT SOURCE-VALID THEOREM PREFLIGHT / NUMERICAL-HYPOTHESIS WALL / NO CREDIT**

## Target

Z2 asks for a population-wide canonical-degree inequality strong enough to control an arbitrary integral multibranch genus-one carrier on the 48-A1 cuboid surface.

Two published theorem shapes are relevant:

1. Langer-type orbifold BMY for normal log pairs;
2. Sabatino's singularity-unrestricted log-canonical-degree bound on a smooth open surface.

The retained Miyaoka 2008 single-curve inequality has already been checked and is strictly satisfied for every multiple of the hostile ray.

## 1. Langer normal-pair route

Langer's logarithmic orbifold Euler-number theorem applies to a normal surface with a boundary Q-divisor under log-canonical / positivity hypotheses and expresses the BMY correction through local orbifold Euler numbers.

This is formally broad enough to include quotient singularities such as A1 points.

For the current carrier, however, a useful specialization must know the local orbifold contribution of the boundary pair at:

- the box-node multibranch passages; and
- the off-exceptional singularities carrying the quadratic delta budget.

The retained MB104 packet does not source-lock the latter analytic singularity types. P6M records exactly this wall:

```text
delta(C)=168 l^2+56 l
```

is exact, while source-locked exceptional contact data are only linear and do not classify the quadratic singularity mass.

Therefore a Langer local-orbifold calculation cannot presently be evaluated at the required quadratic coefficient without adding singularity-type assumptions.

This is not a theorem failure; it is a missing local-input interface.


## 1b. Exact log-canonicity scaling on the contracted A1 model

There is an additional structural obstruction to extracting a degree bound from the normal-pair route.

Let

```text
pi : S -> Sbar
```

be the crepant minimal resolution and let `C_l` be a balanced carrier with strict-transform class

```text
C_l = 7l H - 4l sum_(i in Sigma) E_i.
```

Its image `Cbar_l` on the canonical model is Cartier-linearly equivalent to

```text
Cbar_l ~ 7l H.
```

At every supported A1 point the total transform is

```text
pi^* Cbar_l = C_l + 4l E_i.
```

Because the A1 resolution is crepant,

```text
K_S = pi^* K_Sbar.
```

Hence for the boundary pair `(Sbar, alpha Cbar_l)` the discrepancy of the exceptional divisor is

```text
a(E_i; Sbar, alpha Cbar_l) = -4 alpha l.
```

Log canonicity therefore forces

```text
alpha <= 1/(4l).
```

Write `beta=alpha*l`, so `0<=beta<=1/4`. Since `K_Sbar=H` and `H^2=16`,

```text
(K_Sbar + alpha Cbar_l)^2
 = (1+7 alpha l)^2 H^2
 = 16 (1+7 beta)^2.
```

Thus the left-hand side of a log/orbifold BMY inequality is **scale-invariant in l** throughout the admissible log-canonical range. A fixed positive `alpha` cannot be used as `l->infinity`.

Consequently any degree-cutting strength would have to come from the local orbifold Euler corrections of the pair. Those corrections depend on the actual multibranch/tangent singularity package and on the off-exceptional singularities, exactly the data not source-locked by P6M.

This strengthens the interface wall:

```text
ambient orbifold Chern positivity alone
  does not produce an l-growth contradiction
  on the current balanced ray.
```


## 2. Sabatino open-surface route

Pietro Sabatino,
*An Explicit Bound for the Log-Canonical Degree of Curves on Open Surfaces*,
PRIMS 58 (2022), 817--853, DOI 10.4171/PRIMS/58-4-6,
proves a canonical-degree bound for an arbitrary irreducible curve `C` on a smooth pair `(X,D)` without imposing a singularity classification on `C`.

For the explicit boundedness consequence used here the hypotheses include:

```text
K_X+D big and nef,
(K_X+D)^2 > e(X\D).
```

This avoids the P6M singularity-type problem, so it is the strongest clean Z2 candidate to test.

## 3. Exact cuboid exceptional-boundary substitution

Let `S` be the smooth minimal cuboid resolution. Retained invariants are

```text
K_S^2=16,
c2(S)=e(S)=80.
```

Take any reduced exceptional boundary

```text
D_r = E_1+...+E_r
```

consisting of `r` pairwise disjoint A1 exceptional curves.

Since

```text
K_S.E_i=0,
E_i^2=-2,
E_i.E_j=0  (i!=j),
e(E_i)=2,
```

we get exactly

```text
(K_S+D_r)^2 = 16-2r,
e(S\D_r)   = 80-2r.
```

Hence for every `0<=r<=48`,

```text
(K_S+D_r)^2 - e(S\D_r) = -64.
```

The strict inequality required by Sabatino's canonical-degree bound therefore fails uniformly.

There is an additional failure whenever `r>0`:

```text
(K_S+D_r).E_i = -2
```

for each boundary component, so `K_S+D_r` is not nef.

Thus no choice of a reduced subset of the 48 exceptional curves activates the theorem.

For `r=0`, this reduces to the familiar closed-surface inequality

```text
K_S^2=16 < c2(S)=80.
```

## 4. Why contraction does not repair this shallowly

Contracting the exceptional curves returns to the singular canonical model and removes the explicit nef failure, but then the usable BMY quantity is the orbifold/log-pair Euler number. Its local terms depend on the analytic pair `(X,alpha C)`.

At the 48 A1 points the surface singularity is controlled, but the carrier's full singularity package is not. In particular the quadratic off-exceptional delta mass remains analytically unclassified.

So the contraction route returns to the Langer/P6M missing-correction interface rather than producing a source-complete canonical-degree inequality.

## Disposition

The currently located source-valid Z2 theorem shapes split cleanly:

```text
Miyaoka 2008 one-curve orbibundle:
    applicable on smooth resolution, strictly satisfied for all l.

Sabatino 2022 open-surface bound:
    singularity-flexible for C,
    but numerical positivity fails by constant gap -64
    for every exceptional boundary subset,
    and nefness fails for nonempty exceptional boundary.

Langer normal log-pair BMY:
    suitable ambient generality,
    but required local orbifold correction is not source-complete
    for the current singular carrier.
```

No population-wide degree bound is obtained.

## Next route

With Z3-specific, Z12 and Z2 all at exact/interface boundaries, return to the active-composition package and ask for a new equality-breaking global fact rather than another aggregate inequality:

```text
MB104-Z36-Z4P-FORCED-ORDINARY-SINGULARITY-LOCALIZATION-PREFLIGHT
```

Use the retained Lu--Miyaoka requirement

```text
n_ordinary_node_or_triple >= max(0,112l-224)
```

together with P6F equigeneric isolation and the exact N14 contact equality. Test whether the forced ordinary singularities can be localized by a source-complete projective/adjoint condition. Stop if only their total count is known.

## Source locks

Historical archive head:
```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- `MIYAOKA2008-ORBIBUNDLE-GENUS1-WALL.md`
  blob `f59898039325b8a919f195ed9b0a491885e8232d`;
- `LU-MIYAOKA-GENUS1-SINGULARITY-COUNT-SOURCE-NOTE.md`
  blob `82e247159d736f92aa1382a469fa1d46a81dbae0`.

Current compact branch:
- P6M singularity-type correction wall blob
  `f1b0037a7207c6bb137a72ab1f337f2f2eb52e18`.

External theorem anchors:
- A. Langer, *Logarithmic orbifold Euler numbers of surfaces with applications*, PLMS 86 (2003), 358--396.
- P. Sabatino, *An Explicit Bound for the Log-Canonical Degree of Curves on Open Surfaces*, PRIMS 58 (2022), 817--853.

## Firewalls

```text
population_canonical_degree_bound=false
finite_degree_window_proved=false
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
