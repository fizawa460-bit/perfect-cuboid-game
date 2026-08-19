# SR-STR-015 deep closure attempt

Date: 2026-08-19
Status: `FIRST_MISSING_LEMMA_IDENTIFIED`
Arsenal decision: unchanged (`EXTERNAL_GATE`).

## Closed reduction

For the R504 full-split family

```text
C_s: Y^2=((A*u^2+B)^4+(C*u^2+D)^4)
sigma(u,Y)=(-u,Y)
E_s: Y^2=((A*x+B)^4+(C*x+D)^4), x=u^2
E0: v^2=z^3-4z
```

`Hom_{Qbar}(P_s,E0) != 0` is equivalent to a nonconstant anti-invariant map `f:C_s -> E0` with `f∘sigma=[-1]∘f`. Writing

```text
z∘f = F in Qbar(E_s)
v∘f = u*R
```

gives the exact function-field equation

```text
x*R^2 = F^3-4F.
```

Equivalently `[F(F-2)(F+2)]=[x]` in the squareclass group of `Qbar(E_s)`.

Primitive degree 2 is completely reduced: the deck involution commutes with `sigma`, hence the parameter lies on the already classified reciprocal/commuting-involution divisor

```text
(AB-CD)(AB+CD)(AD+BC)=0.
```

## First missing lemma

```text
FIRST_MISSING_LEMMA=R504PrimitiveAntiInvariantE0SubcoverRigidity
```

Needed strongest form:

```text
For every smooth full-split parameter with AD-BC != 0,
every primitive solution F,R of x*R^2=F^3-4F
forces (AB-CD)(AB+CD)(AD+BC)=0,
or a fixed finite degree-independent alternative divisor list.
```

A weaker sufficient form is an absolute bound on primitive degree followed by explicit fixed-level elimination.

Current inputs do not give such a bound: higher-degree elliptic quotients need not produce a deck involution; Riemann-Hurwitz gives total ramification 4 independently of the degree; fixed-level Humbert/Hecke loci do not control the union over unbounded primitive degree; Gaudron–Rémond gives height-dependent complexity rather than a global finite-level reduction.

```text
DEGREE_2_RECIPROCAL_REDUCTION=PROVED
UNBOUNDED_PRIMITIVE_DEGREE_CONTROL=OPEN
DAW_ORR_APPLICABILITY=NOT_REACHED
SR_STR_015_STATUS=EXTERNAL_GATE
ADAPTER_CLOSURE_VERDICT=FIRST_MISSING_LEMMA_IDENTIFIED
```
