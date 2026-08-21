# Stage29-02f — exact physical-open boundary ledger

```text
OBJECT=U = nondegenerate rational-box open
COMPACTIFICATION=S = minimal smooth cuboid surface
```

## Minimal algebraic deletion

For the standard cuboid equations

```text
a1^2+a2^2=b3^2
a1^2+a3^2=b2^2
a2^2+a3^2=b1^2
a1^2+a2^2+a3^2=c^2,
```

a rational point is a nondegenerate box exactly when

```text
a1*a2*a3 != 0.
```

No separate deletion of `b1*b2*b3*c` is needed on `Q`-points.  If, for example, `b3=0`, then `a1^2+a2^2=0`; over `Q` this forces `a1=a2=0`.  Likewise `c=0` forces all three rational sides to vanish.

The positive ordered physical chamber is a real connected/chamber selection after this algebraic open is fixed; it is not used to define the Brauer scheme.

## Smoothness on the open

Testa--Stoll Lemma 3 states that a point with `a1*a2*a3 != 0` (or with all `b` coordinates nonzero) has full Jacobian rank.  Hence

```text
Ubar = Sbar intersect D_+(a1*a2*a3)
```

contains no one of the 48 `A1` nodes.  The minimal resolution `b:S->Sbar` therefore restricts to an isomorphism over `Ubar`.

## Side-boundary decomposition

Each side hyperplane section `ai=0` splits over `Q` into eight conics.  At `a1=0`, the eight components are

```text
a1=0
b3=e3*a2
b2=e2*a3
c=e1*b1
a2^2+a3^2=b1^2
```

for `(e1,e2,e3) in {+1,-1}^3`; cyclically permute for `a2=0` and `a3=0`.

Thus the strict-transform side boundary contains exactly

```text
24 geometric conics, all individually Q-defined.
```

This matches the first three groups of eight in Testa--Stoll Definition 6 / Stoll's `C1s`; the fourth group of eight comes from `c=0` and is not needed in the minimal rational physical-open deletion.

## Exceptional boundary

All 48 nodes lie outside `Ubar`, hence every exceptional curve in `S->Sbar` is contained in `D=S\U`.

The Testa--Stoll field-of-definition ledger is

```text
24 exceptional curves over Q,
24 exceptional curves strictly over Q(i).
```

Therefore `D_Qbar` has

```text
24 side conics + 48 exceptional curves = 72
```

geometric irreducible components.

## Galois permutation module

Let

```text
K=Q(i,sqrt(2)),
G=Gal(K/Q) ~= V4,
H_i=Gal(K/Q(i)).
```

The 48 Q-defined components are fixed individually.  The 24 exceptional components not defined over Q occur in 12 conjugate pairs.  Hence

```text
Div_D(S_Qbar) ~= Z^48 direct_sum (Z[G/H_i])^12.
```

This exact permutation-lattice description is the input for the boundary/Picard cohomology computation.

## Firewalls

- `U(Q)` equality is a rational-point statement; over `Qbar`, the diagonal-coordinate hyperplanes may have points not forced by side vanishing.
- We intentionally use the minimal algebraic open sufficient for rational boxes, not the larger deletion of all seven coordinate hyperplanes.
- Positivity/canonical ordering is not encoded in the algebraic Brauer calculation.
