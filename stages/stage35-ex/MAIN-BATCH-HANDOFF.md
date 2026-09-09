# Stage35-EX MAIN batch handoff — Goal4AW provisional marked-height lower-vs-upper audit

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4AW are a provisional stacked research surface on PR #1723 and grant no E1, Stage35, endpoint, or Perfect Cuboid credit.

## Exact-green parent

Goal4AV is green at:

- head: `47338365100fc73dee2f82cf9a2025230620ae22`
- aggregate run: `34294868746`
- `verify-stage35-ex-current`: `102290540930`
- result: `SUCCESS`

Goal4AV froze the exact `d_A*d_B*d_C=1` mechanism as a genuine degree-at-most-four **coefficient** package but not a rational endpoint common 2-cover / Selmer / Cassels obstruction.

## Goal4AW provisional exact result

The physical marked point does satisfy the key applicability condition: Goal4L proves every physical endpoint maps to a **non-torsion** point on

```text
E_q: Y^2=X*(X-1)*(X+q^2).
```

Write the reduced Pythagorean base as

```text
q=r/s,
r^2+s^2=t^2.
```

After `x=s^2 X`, `y=s^3 Y`, the exact integral model is

```text
y^2=x*(x-s^2)*(x+r^2),
Delta_raw=16*r^4*s^4*t^4,
c4=16*(r^4+r^2*s^2+s^4).
```

For every odd prime `ell|rst`, `c4` is an `ell`-adic unit, so this model is minimal and multiplicative there:

```text
v_ell(Delta_min)=4*v_ell(r*s*t),
ord_ell(N_E)=1.
```

External literature check: Petsche, *Small rational points on elliptic curves over number fields*, Theorem 2, gives over `Q`

```text
hhat(P) >= log|Delta_min| /
  (10^15*sigma^6*log^2(104613*sigma^2))
```

for non-torsion rational points, so it is semantically applicable to the physical Goal4L point.

However the comparison needed for eventual elimination is not available. Current exact sources lack all three required numerical adapters:

```text
1. Goal4M has only hhat(P)=O(log B_cut), not an explicit C_up;
2. no lower bound log|Delta_min(E_q)| >= c_Delta*log B_cut - O(1);
3. no uniform source-locked Szpiro bound sigma(E_q)<=Sigma.
```

Therefore the required strict coefficient inequality cannot be evaluated or proved. The height candidate is frozen as

```text
EXPLICIT_CANONICAL_HEIGHT_LOWER_VS_GOAL4M_UPPER_CONSTANTS
  -> BLOCKED_MISSING_UNIFORM_HEIGHT_DISCRIMINANT_SZPIRO_ADAPTERS.
```

This is not a proof that no future family-specific height argument can work; it is the exact boundary of current sources.

Artifacts:

- `stages/stage35-ex/35ex-35/goal4aw-marked-elliptic-height-lower-vs-goal4m-upper-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4aw-marked-elliptic-height-lower-vs-goal4m-upper.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4aw_height_lower_vs_upper.py`

## Freshness

At the exact-green Goal4AV parent, current `main` is `119e24100dd943cadef39df783a7b5de7b3a5704`; PR #1723 is ahead 39 / behind 7 from merge-base `42f20e47babdfdda068a605e3fec489eeace460c`. The main-side changes remain Stage32-EX1 / Stage32-EX5 / Stage32 routing and Stage36 material; no Stage35-EX mathematical source drift was observed. No freshness credit is claimed and no sync is performed in this provisional leaf.

## Next exact leaf

```text
35EX-35_GOAL4AX_CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY_PREFLIGHT
```

The fresh Goal4AS exhaustive-view ledger still contains `CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY` as a distinct untested lens. Assemble the three primitive face Pythagorean structures and three space-diagonal couplings into one exact norm/lattice torsor and test whether it imposes anything not already equivalent to endpoint equations, primitivity, the marked-Kummer product-one relation, or the full Brauer route.

No merge. No hostile-audit credit is added by this handoff.
