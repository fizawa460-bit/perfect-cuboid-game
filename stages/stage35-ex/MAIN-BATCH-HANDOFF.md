# Stage35-EX MAIN batch handoff — Goal4BR derived fourth-square defect

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4BR are provisional stacked leaves on PR #1723. No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted.

## Exact-green parent

Goal4BQ is exact-green:

- exact head: `930c649ed32104c3faf1f22074423707ad2c6a40`
- aggregate: `34322296008`
- `verify-stage35-ex-current`: `102373228786`
- result: `SUCCESS`

Goal4BQ proves that for the fixed 2-adic slice near the rational boundary anchor `y=0`, the finite visible-character packet of conductor `2^n` forces exact boundary depth `D(n)=n`. Any rational realization would satisfy `H(y)>=2^n`, but no retained theorem realizes those adelic packets by rational endpoints, so no counting or endpoint credit follows.

## Goal4BR provisional exact result

For the primitive six-variable endpoint

```text
A=x*y*a,
B=x*z*b,
C=y*z*c,
```

Goal4AY's derived Euler brick has edges

```text
A_D=x*a*b,
B_D=y*a*c,
C_D=z*b*c,
```

and fourth-square defect

```text
Q_D=(x*a*b)^2+(y*a*c)^2+(z*b*c)^2.
```

Put

```text
P=r_AB*r_AC*r_BC,
R=x*y*z*a*b*c.
```

The exact completion identity is

```text
P^2+R^2=W^2*Q_D.
```

Let `G=gcd(P,R)`, `p=P/G`, `r=R/G`. Since every reduced face hypotenuse is odd and primitive endpoint parity makes `R` even,

```text
gcd(p,r)=1,
p odd,
r even,
[Q_D]=[p^2+r^2].
```

Hence the squarefree support of `Q_D` contains no factor `2` and no prime `3 mod4`; every squarefree prime is `1 mod4`.

Retaining the Goal4AU reservoirs

```text
h_a=gcd(a,r_BC),
h_b=gcd(b,r_AC),
h_c=gcd(c,r_AB)
```

and defining

```text
j_x=gcd(x,r_AB),
j_y=gcd(y,r_AC),
j_z=gcd(z,r_BC),
```

one gets valuation-exactly

```text
G=h_a*h_b*h_c*j_x*j_y*j_z.
```

Under the Goal4AY involution

```text
(x,y,z ; a,b,c) -> (a,b,c ; x,y,z),
```

the two reservoir triples swap:

```text
(h_a,h_b,h_c) <-> (j_x,j_y,j_z).
```

However the original perfect endpoint does **not** imply `Q_D` is a square. Imposing `Q_D=S^2` would additionally require the derived Euler brick itself to be perfect, which is unsupported population narrowing. Therefore the primitive Pythagorean equation obtained under that extra hypothesis is not a legal receiver for the original endpoint population.

Consequently:

```text
Q_D squareclass restriction = exact;
derived reservoir two-cycle = exact;
finite exhaustive squareclass family = no;
S34-W01 triggered = no;
strict descent = no;
branch pruning = no.
```

Artifacts:

- `stages/stage35-ex/35ex-35/goal4br-derived-fourth-square-defect-squareclass-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4br-derived-fourth-square-defect-squareclass.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4br_derived_fourth_square_defect_squareclass.py`

## Next exact leaf

```text
35EX-35_GOAL4BS_POST_BOUNDARY_DERIVED_BACKUP_PARKING_AUDIT
```

Goal4BQ's selected boundary-depth route is blocked at the missing rational-realization/global-height adapter, and Goal4BR closes its distinct derived-defect backup as non-obstructive. Run a fresh breadth/parking audit before reusing either route. Admit only a genuinely new source-fixed invariant or an exact adapter that discharges one of the frozen missing objects.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
