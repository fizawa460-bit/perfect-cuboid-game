# Stage32 MB104 — U1 equigeneric superabundance wall — 2026-09-17

Status: **U1 SIMPLE SEVERI-CODIMENSION ROUTE BLOCKED / EQUIGENERIC CURVES RIGID BUT NOT EXCLUDED / NO CREDIT**

## Receiver

Assume a hypothetical integral curve

```text
C in |D_l|,
D_l=7lH-4l sum_(p in Sigma)E_p,
|Sigma|=14,
l>=1,
```

with normalization

```text
nu:E -> C,
g(E)=1.
```

Retained numerical data are

```text
C^2=336l^2,
K_S.C=112l,
p_a(C)-g(E)=Delta=168l^2+56l.
```

The restart ledger observed the nominal comparison

```text
chi(O_S(C))-1 = 168l^2-56l+7,
Delta - [chi(O_S(C))-1] = 112l-7.
```

The question was whether an exact global equigeneric/Severi codimension theorem could turn that linear deficit into an all-`l` or large-`l` exclusion.

## Conductor deformation formula

Let

```text
A = Hom(nu_* O_E, O_C)
```

be the conductor ideal. Standard equigeneric deformation theory identifies the tangent cone of the local delta-constant locus with the conductor image. The global adjunction/conductor identity is

```text
A tensor O_S(C)
  = nu_* (omega_E tensor nu^* omega_S^{-1}).
```

This is the standard formula used, for example, in Kleiman--Shende, *On the Goettsche Threshold*, Lemma 8, together with the classical conductor description of the equigeneric tangent cone.

For `g(E)=1`, `omega_E` has degree zero. Therefore

```text
deg(omega_E tensor nu^*omega_S^{-1})
 = -K_S.C
 = -112l.
```

Hence

```text
H^0(E, omega_E tensor nu^*omega_S^{-1}) = 0.
```

So a genus-one member is **equigenerically rigid** inside the surface: the conductor tangent space contributes no nonzero first-order genus-preserving deformation.

But on an elliptic normalization, Riemann--Roch/Serre duality gives exactly

```text
h^1(E, omega_E tensor nu^*omega_S^{-1})
 = 112l.
```

Thus the global conductor restriction has a linearly growing obstruction/superabundance space of the same size as `K_S.C`.

## Why the nominal dimension deficit does not close the ray

The local equigeneric stratum has codimension `Delta`, but the map from the complete linear system to the product of local deformation spaces need not be transverse. Here the natural conductor sheaf already exhibits superabundance

```text
112l,
```

while the restart ledger's nominal deficit is only

```text
112l-7
```

before any additional `H^1(O_S(C))` contribution to `dim |C|` is counted.

Therefore a proof of the form

```text
Delta > expected dim |D_l|
=> no genus-one member
```

is not available. The exact deformation package has enough `H^1` to absorb that entire linear deficit.

The correct conclusion is weaker but exact:

```text
if such a genus-one curve exists, it is isolated in the equigeneric locus;
```

isolation does not imply nonexistence, and isolated low-genus curves may occur in arbitrarily large divisor classes on special surfaces.

## Consequences for restart candidates

```text
U1_NAIVE_GLOBAL_SEVERI_CODIMENSION = BLOCKED
U5_CONDUCTOR_IDEAL_VANISHING = BLOCKED
```

The second status means specifically that an asymptotic-vanishing strategy applied to the **equigeneric conductor sheaf** cannot work: its normalization pullback has degree `-112l`, and its `H^1` grows as `112l` rather than vanishing.

A genuinely stronger U1/U5 route would need extra geometry not contained in ordinary equigeneric deformation theory, for example a product-cover constraint, a global incidence condition, or another condition cutting the `112l` superabundance itself.

## Firewalls

- No genus-one curve is constructed or excluded.
- No all-`l` or large-`l` cutoff is proved.
- No claim is made that every possible equisingular/global deformation method is blocked.
- Only the conductor/standard-Severi codimension mechanism is blocked as a standalone replacement theorem.
- No receiver, effectivity, theorem, endpoint, merge, or Perfect-Cuboid credit.
