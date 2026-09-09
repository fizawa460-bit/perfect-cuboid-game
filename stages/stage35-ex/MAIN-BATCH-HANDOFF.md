# Stage35-EX MAIN batch handoff — Goal4AX provisional split six-norm torus chart

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4AX remain a provisional stacked research surface on PR #1723 and grant no E1, Stage35, endpoint, or Perfect Cuboid credit.

## Exact-green parent

Goal4AW is now exact-green after a verifier-only repair:

- exact head: `a862b3ddea76b21110ba93b0d171e55c22ce6af8`
- aggregate run: `34297319019`
- `verify-stage35-ex-current`: `102298024754`
- result: `SUCCESS`

The repair changed only SymPy structural equality checks for the already-recorded exact `c4` and `j` identities; the Goal4AW mathematical artifact and source lock were unchanged.

Goal4AW therefore retains the exact boundary:

```text
physical Goal4L point is non-torsion;
Petsche explicit lower bound is semantically applicable;
Goal4M still lacks an explicit upper coefficient;
no endpoint-height lower growth for Delta_min is locked;
no uniform Szpiro ratio bound is locked;
no height contradiction / eventual elimination is obtained.
```

## Goal4AX provisional exact result

Goal4AX executes the Goal4AS lens `CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY`.

For a positive endpoint the three face squares and three space-diagonal decompositions become six Gaussian norm equations:

```text
N(A+iB)=D_AB^2,
N(A+iC)=D_AC^2,
N(B+iC)=D_BC^2,
N(D_AB+iC)=W^2,
N(D_AC+iB)=W^2,
N(D_BC+iA)=W^2.
```

For each positive rational Pythagorean triple `U^2+V^2=H^2`, the half-angle parameter

```text
t=V/(H+U)
```

gives

```text
R(t)=2t/(1-t^2),
H0(t)=(1+t^2)/(1-t^2),
(U+iV)/H=(1+i*t)/(1-i*t).
```

Thus every one of the six norm-one phases has an explicit Hilbert–90 lift `1+i*t` once the endpoint is present.

Using

```text
f_AB=B/(D_AB+A),
f_AC=C/(D_AC+A),
f_BC=C/(D_BC+B),
s_AB=C/(W+D_AB),
s_AC=B/(W+D_AC),
s_BC=A/(W+D_BC),
```

the exact cross-face compatibility is

```text
R(f_AC)=R(f_AB)*R(f_BC),
R(s_AB)=R(f_AC)/H0(f_AB),
R(s_AC)=R(f_AB)/H0(f_AC),
R(s_BC)=1/(R(f_AB)*H0(f_BC)).
```

Conversely these four identities reconstruct, up to positive scaling,

```text
A=1,
B=R(f_AB),
C=R(f_AC),
D_AB=H0(f_AB),
D_AC=H0(f_AC),
D_BC=R(f_AB)*H0(f_BC),
W=H0(f_AB)*H0(s_AB),
```

and recover all three face-square equations plus the common space-square equation. Therefore this common six-norm chart is an exact positive-endpoint reparameterization rather than a stricter obstruction receiver.

The primitive pair-gcd dictionary is compatible with the chart, e.g.

```text
B/(D_AB+A)=z*b/(r_AB+y*a),
```

but primitivity/gcd/parity remain integral representative conditions; Goal4AX obtains no new rational norm equation or finite branch pruning from them.

Route decision:

```text
CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY
  -> PASS_EXACT_SPLIT_SIX_NORM_TORUS_CHART
  -> BLOCKED_AS_POSITIVE_ENDPOINT_BIRATIONAL_REPARAMETRIZATION
```

No nontrivial H1 torsor class, local norm obstruction, spinor obstruction, common Selmer complex, individual Kummer trivialization, or E1 closure is claimed.

Artifacts:

- `stages/stage35-ex/35ex-35/goal4ax-cross-face-lattice-norm-torsor-compatibility-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4ax-cross-face-lattice-norm-torsor-compatibility.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4ax_cross_face_norm_torsor.py`

## Freshness

Current `main` observed during this batch is `aab9afa37a136f76a5bf8e6eb146145b7bb853c3`. Relative to merge-base `42f20e47babdfdda068a605e3fec489eeace460c`, the main-side changes are Stage32-EX1 / Stage32-EX5 / Stage32 routing and Stage36 material. No Stage35-EX mathematical source drift was observed. No freshness credit is claimed and no sync is performed in this provisional leaf.

## Next exact leaf

```text
35EX-35_GOAL4AY_GENUINE_NONLINEAR_FULL_ENDPOINT_SELF_MAP_DESCENT_PREFLIGHT
```

Goal4AY must seek a **total** source-locked map from primitive full endpoints to primitive full endpoints that preserves all three face squares and the space square, treats every parity branch/exceptional locus, and strictly decreases a well-founded positive height. It must not reuse the common-scalar `v2` division already closed by Goal4I. Repository/source search miss alone is not a mathematical nonexistence proof.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains at V74 / Goal4AK.
