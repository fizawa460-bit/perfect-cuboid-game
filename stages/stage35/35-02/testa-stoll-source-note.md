# Stage35 35-02 — Testa--Stoll source note for the selected direct endpoint fibration

```text
SOURCE_KIND=external_primary_paper
AUTHORS=Michael Stoll; Damiano Testa
TITLE=The surface parametrizing cuboids
SOURCE_URL=https://www.mathe2.uni-bayreuth.de/stoll/papers/Cuboidi.pdf
SOURCE_DATE_IN_PDF=2025-02-24
SOURCE_SECTION=5 Fibrations in curves of genus 5
STAGE35_USE=selected Q-defined rank-3 direct full-endpoint genus-5 fibration
NEW_THEOREM_CREDIT=false
```

This note records only the source facts needed by Stage35. It does not import the full paper.

## Source model and Stage29 dictionary

The paper uses projective coordinates

```text
[a1:a2:a3:b1:b2:b3:c]
```

where `a1,a2,a3` are the three sides, `b1,b2,b3` the three face diagonals, and `c` the long diagonal. Its equivalent cuboid equations include

```text
a1^2+a2^2=b3^2
a1^2+a3^2=b2^2
a2^2+a3^2=b1^2
a1^2+a2^2+a3^2=c^2.
```

Against the exact Stage29 endpoint coordinates `[e:x:y:p:q:z:d]`, fix the physical dictionary

```text
[a1:a2:a3:b1:b2:b3:c]=[e:x:y:z:q:p:d].
```

This dictionary is equation-preserving:

```text
e^2+x^2=p^2
e^2+y^2=q^2
x^2+y^2=z^2
e^2+x^2+y^2=d^2.
```

## Rank-3 fibration source facts

Section 5 states that exactly six rank-3 quadrics contain the cuboid surface. For a rank-3 quadric, projection maps the cuboid surface to a conic; eight singular points lie in the base locus, so they are blown up to obtain a morphism. The paper then states that the conic-to-`P1` isomorphism is always available already over `Q`. Each rank-3 quadric gives one fibration whose generic fiber is a smooth canonical genus-5 curve. Together with the rank-4 constructions, the geometric total is `6+2*11=28`.

The paper gives the representative rank-3 quadric

```text
a1^2+b1^2=c^2
```

with parameter

```text
t=(a1+c)/b1.
```

The first two displayed fiber equations are

```text
(t^2+1)a1-(t^2-1)c=0
(t^2+1)b1-2tc=0.
```

Under the Stage29 dictionary this selected fibration is therefore

```text
SOURCE_QUADRIC=e^2+z^2=d^2
PARAMETER=t=(e+d)/z
(t^2+1)e-(t^2-1)d=0
(t^2+1)z-2td=0.
```

For a nondegenerate physical endpoint all lengths are positive, hence `z>0`, `e>0`, `d>0`; consequently this parameter is finite and satisfies `t>1`.

## Field and coverage boundary

For this rank-3 construction the paper explicitly gives the conic-to-`P1` isomorphism over `Q`. Thus the selected fibration is a direct full-endpoint genus-5 fibration over `Q`; no rank-4 splitting field is needed for this selected route.

The eight base points are singular points of the canonical cuboid surface. The paper also notes that a point with all three side coordinates nonzero is smooth. Therefore nondegenerate physical endpoints do not lie in this rank-3 base locus.

This means every nondegenerate physical endpoint `Q`-point is in the domain of the selected rational parameter and lies on one of its fibers with `t in Q`, indeed `t>1`. This is a fibration/coverage adapter only; it is not a rational-point exclusion theorem.

## Global geometric field firewall retained

Stage35 does not infer that all 28 geometric genus-5 fibrations are over `Q`. Section 5 says rank-4 quadrics yield two fibrations only after passing to a field that splits the quadric, and explicitly identifies the first rank-4 pair as defined over `Q(i)`. The paper's general convention is geometric (`Qbar`/`C`) unless otherwise stated.

Accordingly:

```text
SELECTED_RANK3_FIBRATION_Q_DEFINED=true
SELECTED_RANK3_PHYSICAL_ENDPOINT_COVERAGE=true
ALL_28_FIBRATIONS_Q_DEFINED_CERTIFIED=false
ALL_15_EULER_K3_FIBRATIONS_Q_DEFINED_CERTIFIED=false
R29_FIB1_GLOBAL_LEDGER_CLOSED=false
R29_FIB2_CLOSED=false
```

The selected route is sufficient for Stage35 to formulate a global moving-family theorem over one exact `Q`-defined genus-5 fibration; it does not close the historical all-fibration field ledger.
