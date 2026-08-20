# Stage27-18b — parametric normal-form extraction

```text
TASK_ID=Stage27-18b
ROLE=PARAMETRIC_NORMAL_FORM_EXTRACTION
STATUS=COMPLETE_EXACT_INTERFACE
STAGE18_ABSOLUTE_LAW_REOPENED=false
```

Stage18 and Stage19 use the literal same primitive canonical exactly-two physical population before the additional predicate `R in Z` is imposed.  Thus the source measure needs no height, orientation, incidence, or multiplicity adapter.

Choose the unique shared edge of the two successful faces and call the physical edges `(e,x,y)`.  Before primitive scaling use the positive toric Pythagorean coordinates

`E=4mnrs`,
`X=2rs(m^2-n^2)`,
`Y=2mn(r^2-s^2)`,

with `G=gcd(E,X,Y)` and `(e,x,y)=(E,X,Y)/G`, subject to the frozen chamber/coprimality/parity conditions and the exactly-two mask `x^2+y^2 not square`.

Define

`A=m^2 r^2+n^2 s^2`,
`D=m^2 s^2+n^2 r^2`.

(The second Gaussian norm is denoted `D` here to avoid collision with the global cutoff `B`.) Direct expansion gives

`E^2+X^2+Y^2 = 4 A D`,

hence on the primitive physical object

`G^2 R^2 = 4 A D`.

Therefore the Stage19 survivor predicate inside the Stage18 source measure is exactly

`R in Z <=> A D is a square <=> sf(A)=sf(D)`.

Equivalently there is a unique squarefree `k>0` with

`A=k P^2`, `D=k Q^2`.

This is the required zero-loss Stage18 -> Stage19 parametric interface.  It introduces no polynomial parameter multiplicity: the physical shared-edge incidence is intrinsic and the frozen positive chamber is reconstructible from the physical object as recorded in the Stage19 interface.

The remaining Stage27-18 problem is therefore not parameter extraction but localization of the settled Stage18 mass in these coordinates and estimation of the squareclass-equality survivor mass on the same source measure.

```text
POPULATION_MATCH=true
CUTOFF_MATCH=true
PHYSICAL_MULTIPLICITY_MATCH=true
SPACE_DIAGONAL_PREDICATE=sf(A)==sf(D)
PARAMETRIC_INTERFACE_LOSS=B^o(1)_AT_WORST_AND_NO_POLYNOMIAL_LOSS
NEW_STAGE19_UPPER_EXPONENT_PROVED=false
NEW_STAGE19_LOWER_EXPONENT_PROVED=false
NEXT_DERIVED_ROUTE=Stage27-18c_and_27-18d
```
