# Stage35 35-08 — González-Jiménez 2015 source note

```text
SOURCE_KIND=external_primary_paper
AUTHOR=Enrique Gonzalez-Jimenez
TITLE=Covering Techniques and Rational Points on Some Genus 5 Curves
PUBLICATION=Contemporary Mathematics 649 (2015), 89-105
DOI=10.1090/conm/649/13021
ARXIV=1311.5759
STAGE35_USE=exact five-elliptic-quotient formulas for a diagonal genus-5 model
```

The paper treats a smooth diagonal genus-5 curve

```text
a X0^2 + b X1^2 = X2^2
c X0^2 + d X1^2 = X3^2
e X0^2 + f X1^2 = X4^2
```

and records five elliptic curves, each the Jacobian of the genus-one quotient obtained by removing one coordinate:

```text
E4: y^2=x(x+a*d)(x+c*b)
E3: y^2=x(x+a*f)(x+e*b)
E2: y^2=x(x+c*f)(x+e*d)
E1: y^2=x(x-d*(a*f-e*b))(x-f*(a*d-c*b))
E0: y^2=x(x+c*(a*f-e*b))(x+e*(a*d-c*b)).
```

The induced isogeny is `Jac(C) -> E0 x ... x E4`, coming from the five forgetful quotient maps. The paper then develops covering-collection and elliptic-Chabauty methods for fixed curves under additional arithmetic hypotheses.

## Stage35 specialization

For `TS-S-R3-Q1`, normalize `d=1` only for coefficient bookkeeping and write

```text
alpha=((t^2-1)/(t^2+1))^2
beta=4*t^2/(t^2+1)^2=1-alpha.
```

Using Stage35 coordinates

```text
[X0:X1:X2:X3:X4]=[d:x:p:y:q],
```

the fiber is in the standard form with

```text
(a,b,c,d,e,f)=(alpha,1,beta,-1,1,-1).
```

Substitution into the five published formulas gives

```text
E4: Y^2 = X (X-alpha) (X+beta)
E3: Y^2 = X (X-alpha) (X+1)
E2: Y^2 = X (X-beta)  (X-1)
E1: Y^2 = X (X-(alpha+1)) (X-1)
E0: Y^2 = X (X-(1-alpha^2)) (X-1).
```

All five have full rational 2-torsion over `Q(t)`. Their discriminants are nonzero for every physical rational `t>1`; this is independently checked in the Stage35 35-08 structure certificate/verifier.

These formulas supply exact quotient structure only. They do not imply that the generic function-field Mordell-Weil group surjects onto every specialized Mordell-Weil group, and therefore do not close `T35-R3-PHYS-EMPTY`.
