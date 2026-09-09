# Stage35-EX MAIN batch handoff — Goal4AY derived-cuboid involution / nonlinear-descent boundary

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4AY are provisional stacked research leaves on PR #1723. No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted here.

## Exact-green parent

Goal4AX is exact-green:

- exact head: `0d620e70ff36b5c508fa3c59f6fde995eda25c90`
- aggregate: `34298150005`
- `verify-stage35-ex-current`: `102300427187`
- result: `SUCCESS`

Goal4AX's six Gaussian norm / Hilbert–90 chart is exact but endpoint-equivalent and non-pruning.

## Goal4AY provisional exact result

Goal4AY executes the Goal4AS lens `GENUINE_NONLINEAR_FULL_ENDPOINT_SELF_MAP_DESCENT` against the currently available source-locked candidates.

The strongest classical candidate is the derived-cuboid pair-product construction

```text
(A,B,C) -> (AB,AC,BC).
```

It exactly preserves the three face-square equations. Through the primitive Stage35-EX decomposition

```text
A=x*y*a,
B=x*z*b,
C=y*z*c,
```

one obtains

```text
gcd(AB,AC,BC)=x*y*z,
```

so the primitive derived edges are

```text
A_D=x*a*b,
B_D=y*a*c,
C_D=z*b*c.
```

Their pair gcds are exactly `a,b,c`, and their residual variables are exactly `x,y,z`. Therefore

```text
D : (x,y,z ; a,b,c) -> (a,b,c ; x,y,z),
D^2=id.
```

The reduced face hypotenuses transform as

```text
r_D_AB=r_BC,
r_D_AC=r_AC,
r_D_BC=r_AB.
```

So the classical derived construction is an exact nonlinear self-map of the **three-face Euler-brick population**.

The fourth square is a separate gate:

```text
original:  W^2=(x*y*a)^2+(x*z*b)^2+(y*z*c)^2,
derived:   W_D^2=(x*a*b)^2+(y*a*c)^2+(z*b*c)^2.
```

No implication from the original fourth square to the derived fourth square is obtained. In raw variables, the exact completion identity is

```text
(D_AB*D_AC*D_BC)^2+(A*B*C)^2
  = W^2*(A^2*B^2+A^2*C^2+B^2*C^2).
```

Even under the stronger hypothetical assumption that the derived operator preserved the fourth square for every endpoint, its involutivity rules out universal strict descent for **any** height: `H(D(P))<H(P)` and the same inequality at `D(P)` would give `H(P)<H(D(P))`.

Thus the classical derived operator is closed as a universal strict-descent candidate without claiming that all nonlinear self-maps are impossible.

Other current candidates:

```text
elliptic multiplication -> no full-endpoint reconstruction;
AX torus symmetries -> chart symmetry / no proved strict compatible endomorphism;
AU/AV Kummer package -> relation, not a self-map;
common scalar v2 -> already closed by Goal4I.
```

A scoped literature check also recovered the classical pair-product construction in Spohn (1974) / Leech (1981). Current arXiv `2602.00239v2` discusses a divisor-propagation descent only as an exploratory gluing mechanism and explicitly does not claim resolution of the perfect-cuboid problem; no full-endpoint map is imported from it.

Route decision:

```text
GENUINE_NONLINEAR_FULL_ENDPOINT_SELF_MAP_DESCENT
  -> FAIL_CLOSE_CURRENT_SOURCE_LOCKED_NONLINEAR_DESCENT_CANDIDATES
  -> exact new fact: primitive derived cuboid = pair-gcd/residual involution
```

Firewall:

```text
ALL_POSSIBLE_NONLINEAR_DESCENT_MAPS_PROVED_IMPOSSIBLE=false
INFINITE_DESCENT_PROVED=false
E1_PROVED=false
```

Artifacts:

- `stages/stage35-ex/35ex-35/goal4ay-derived-cuboid-involution-nonlinear-descent-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4ay-derived-cuboid-involution-nonlinear-descent.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4ay_derived_cuboid_involution.py`

## Freshness

No freshness credit is claimed. The main-side drift observed in this batch was confined to Stage32 / Stage36 material and did not change Stage35-EX mathematical sources. No rebase/sync is performed in this provisional leaf.

## Next exact leaf

```text
35EX-35_GOAL4AZ_SUPER_SQRT_DISTINCT_CLASS_AMPLIFICATION_PREFLIGHT
```

Question: can one hypothetical endpoint force quantitatively many **distinct** endpoint classes or marked receiver points below controlled height, enough to contradict Goal4M's `O(B^(1/2+o(1)))` population ceiling? Symmetry or a finite orbit alone is insufficient; distinctness and height-growth constants must be exact.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
