# Stage35-EX MAIN batch handoff — Goal4BQ y-zero boundary escape depth

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4BQ are provisional stacked leaves on PR #1723. No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted.

## Exact-green parent

Goal4BP is exact-green:

- exact head: `a88fdbad3480f0a6a254a02a001efd179e01528d`
- aggregate: `34319593575`
- `verify-stage35-ex-current`: `102364864481`
- result: `SUCCESS`

Goal4BP executed a fresh blind+Arsenal-deduplicated route audit after the Gaussian ray tower was fail-closed. It selected the fixed `y=0` boundary escape/conductor-depth route and retained the derived fourth-square defect as a distinct untested backup.

## Goal4BQ provisional exact result

Use the rational boundary anchor

```text
P*=(272/225,0,353/225,1,272/225,353/225).
```

At the 2-adic place fix `x=272/225`, `p=353/225`, let `m=v2(y)>=6`, and choose the square-root branches reducing to the anchor. Then

```text
(q-1)(q+1)=y^2,
v2(q+1)=1,
v2(q-1)=2m-1,
v2((q+y)-1)=m.
```

For every `n>=6`, let

```text
X_n=Hom((Z/2^n Z)^*,Q/Z),
F_n={beta(chi,q+y): chi in X_n}.
```

Characters of `(Z/2^n Z)^*` separate unit classes, so all `F_n` evaluations at 2 match the anchor iff

```text
q+y == 1 mod 2^n
iff v2(y)>=n.
```

Hence the exact minimum boundary depth is

```text
D(n)=n.
```

This is sharp and gives a concrete explanation of how finite Brauer-compatible adelic populations can escape toward the removed divisor `y=0` while the full infinite visible-character layer remains endpoint-equivalent.

Conditionally, if a rational realization `y=a/b` in lowest terms existed with `v2(y)>=n`, then `b` is odd, `2^n|a`, and

```text
H(y)>=2^n.
```

But Stage35-EX has no theorem realizing these finite adelic packets by rational endpoints. Therefore no Goal4M/counting contradiction, no compactness closure, and no branch pruning is credited.

Artifacts:

- `stages/stage35-ex/35ex-35/goal4bq-y-zero-boundary-escape-conductor-depth-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4bq-y-zero-boundary-escape-conductor-depth.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4bq_y_zero_boundary_escape_conductor_depth.py`

## Next exact leaf

```text
35EX-35_GOAL4BR_DERIVED_FOURTH_SQUARE_DEFECT_SQUARECLASS_PREFLIGHT
```

Analyze

```text
Q_D=(x*a*b)^2+(y*a*c)^2+(z*b*c)^2
```

using the Goal4AY completion identity and the primitive six-variable gcd/parity dictionary. First reduce the squareclass to its primitive two-square receiver and determine whether any bounded factor/squareclass family exists before invoking S34-W01.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
