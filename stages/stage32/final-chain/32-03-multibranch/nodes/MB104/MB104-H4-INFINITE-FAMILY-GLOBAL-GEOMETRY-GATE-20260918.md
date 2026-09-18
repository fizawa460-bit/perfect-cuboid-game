# Stage32 MB104 — H4 infinite-family-to-global-geometry bridge gate — 2026-09-18

Status: **H4 SHALLOW GATE FAIL / PARKED / CYCLE 1 COMPLETE / NO MATHEMATICAL CREDIT**

## Question

Assume exact integral normalization-genus-one carriers exist for an unbounded sequence of integers `l` in

```
D_l=lD_1
   =7lH-4l sum_(p in Sigma)E_p.
```

Does this alone force one fixed component, one bounded Hilbert/Chow stratum, one positive-dimensional subsystem, or one genus-one fibration carrying the exact balanced packet?

The H4 roadmap requires this implication before any fibration computation.

## 1. The sequence is not bounded in Hilbert/Chow data

For an integral member of `|D_l|`,

```
D_l^2=336l^2,
K_S.D_l=112l,
p_a(D_l)=1+168l^2+56l.
```

Fix any very ample divisor `A` on `S`. The Hilbert polynomial of the curve is

```
P_l(n)
 = chi(O_{C_l}(nA))
 = (A.D_l)n + 1-p_a(D_l)
 = l(A.D_1)n -168l^2-56l.
```

Both the polynomial and the Chow degree

```
A.D_l=l(A.D_1)
```

change without bound as `l` grows.

Therefore an infinite sequence with unbounded `l` does not lie in one fixed projective Hilbert scheme `Hilb^P(S)` or one bounded Chow-degree stratum. The ordinary compactness/specialization step required by H4 is absent.

## 2. A common curve component cannot be the bridge

Each hypothetical carrier is integral. If a fixed irreducible curve `Gamma` were a positive-dimensional component of both `C_l` and `C_m`, integrality would force

```
C_l=Gamma=C_m.
```

But their divisor classes are `lD_1` and `mD_1`, distinct for `l!=m`. Thus a literal common fixed curve component is impossible.

## 3. Same-class deformation does not supply a subsystem

The retained U1 conductor calculation gives equigeneric rigidity for a hypothetical genus-one member: the genus-preserving tangent space contributed by the conductor vanishes, while the obstruction/superabundance is `112l`.

Thus the present data do not even provide a positive-dimensional equigeneric subsystem inside one `|D_l|`. Isolated carriers in different numerical classes cannot be joined into one flat projective family because their Hilbert polynomials differ.

This is exactly the situation H4 had to rule out, not a route to a fixed global object.

## 4. A fixed fibration is not forced

If the carriers themselves were fibers of one fixed fibration, their self-intersection would be zero. Instead

```
C_l^2=336l^2>0.
```

So they are not fibers of one fixed fibration.

They could hypothetically be multisections of some fixed fibration, but no retained theorem derives such a fibration from the existence of isolated genus-one curves in the unbounded classes `lD_1`, and no exact packet-inheritance adapter is available. Starting a fibration calculation here would assume the missing H4 bridge.

## 5. Finite generation does not repair H4

The other natural bridge is a finitely generated graded subsystem. H2 tested precisely the required compatibility and failed: exact carrier semantics are destroyed by ordinary section-ring multiplication. H4 cannot reuse finite generation without a new operation or theorem.

## Decision

The H4 first gate fails.

```
bounded Hilbert/Chow stratum: NO
common fixed curve component: NO
same-class positive-dimensional genus-one subsystem: not supplied; retained tangent space is rigid
fixed fibration with carriers as fibers: NO
fixed fibration with carriers as multisections: NOT FORCED
graded finite-generation bridge: H2 adapter failed
```

The strongest safe conclusion is not that an unbounded carrier sequence exists, nor that no stronger theorem could ever control it. It is:

> the retained MB104 data do not imply the H4 compactness/specialization bridge, and each standard bridge named in H4 either fails numerically or requires a new theorem.

Therefore H4 is parked and no fibration computation is released.

## Cycle-1 rescore

H1, H2, and H4 have now all received one shallow gate and are parked. H3 remains unreleased because its exact incidence prerequisite failed with H2.

The next cycle is registered in the Class-3 roadmap:

1. H8 logarithmic boundary inequality;
2. H5 exact etale-correspondence quotient rigidity;
3. H6 finite monodromy / Nielsen-passport obstruction.

No route is DEEP after cycle 1.

No MB104, receiver, effectivity, theorem, endpoint, Perfect-Cuboid, or merge credit changes.
