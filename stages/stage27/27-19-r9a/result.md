# Stage27-19-r9a — Saunderson space-diagonal locus

For the generalized Saunderson family

A=u(4v^2-w^2), B=v(4u^2-w^2), C=4uvw, with u^2+v^2=w^2,

the space diagonal satisfies

R^2=A^2+B^2+C^2=w^6+16u^2v^2w^2=w^2(w^4+16u^2v^2).

Hence the space diagonal is integral exactly when

Y^2=w^4+16u^2v^2.

Using primitive Euclid parameters u=r^2-s^2, v=2rs, w=r^2+s^2 gives

Y^2=r^8+68r^6s^2-122r^4s^4+68r^2s^6+s^8.

After t=r/s this is

y^2=t^8+68t^6-122t^4+68t^2+1.

The degree-eight polynomial is squarefree, so the normalized hyperelliptic curve has genus 3.

Thus imposing the space-diagonal condition does not leave a two-dimensional thick parameter surface: projectively, the Saunderson family is already a one-dimensional rational parameter, and the extra square condition produces a genus-3 double cover.

```text
SAUNDERSON_SPACE_DIAGONAL_EQUATION_PROVED=true
HYPERELLIPTIC_MODEL_DEGREE=8
HYPERELLIPTIC_MODEL_GENUS=3
THICK_TWO_PARAMETER_LOCUS_SURVIVES=false
NEW_LOWER_EXPONENT_PROVED=false
NEXT_DERIVED_ROUTE=27-19-r9b
```
