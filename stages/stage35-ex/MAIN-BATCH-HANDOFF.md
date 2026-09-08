# Stage35-EX MAIN batch handoff — Goal4AU provisional cross-face marked Kummer coupling

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4AU are a provisional stacked research surface on PR #1723 and grant no E1, Stage35, endpoint, or Perfect Cuboid credit.

## Exact-green parent

Goal4AT verifier repair is green at:

- head: `f499b3e8b4f3e723b1046e2eff0e9f8ac3be24a5`
- aggregate run: `34291537497`
- `verify-stage35-ex-current`: `102280319029`
- conclusion: `SUCCESS`

Goal4AT reduced the physical marked Kummer class to

```text
d=[(2BC)/G],
G=gcd(D_AB*D_AC-BC,D_AB*D_AC+BC),
G|2BC.
```

## Goal4AU provisional exact result

Using the primitive pair-gcd decomposition

```text
A=x*y*a,
B=x*z*b,
C=y*z*c
```

and reduced primitive face hypotenuses `r_AB,r_AC,r_BC`, define

```text
h_a=gcd(a,r_BC),
h_b=gcd(b,r_AC),
h_c=gcd(c,r_AB).
```

For the three cyclic Goal4AT relabelings:

```text
G_A=x*y*epsilon_A*h_b*h_c,
G_B=x*z*epsilon_B*h_a*h_c,
G_C=y*z*epsilon_C*h_a*h_b,
```

where each `epsilon_i` is `1` or `2`, and the primitive parity dictionary forces **exactly one** `epsilon_i=2`. Therefore `epsilon_A*epsilon_B*epsilon_C=2`.

Put

```text
a0=a/h_a, b0=b/h_b, c0=c/h_c,
k_A=2/epsilon_A, k_B=2/epsilon_B, k_C=2/epsilon_C.
```

The canonical positive Goal4AT representatives factor literally as

```text
K_A=(2BC)/G_A=z^2*k_A*b0*c0,
K_B=(2AC)/G_B=y^2*k_B*a0*c0,
K_C=(2AB)/G_C=x^2*k_C*a0*b0,
```

with `k_A*k_B*k_C=4`, hence

```text
K_A*K_B*K_C=(2*x*y*z*a0*b0*c0)^2.
```

Thus the three source-marked residual Kummer squareclasses satisfy the exact cross-face relation

```text
d_A*d_B*d_C=1 in Q*/Q*^2.
```

The associated reservoir map has rows

```text
0 1 1
1 0 1
1 1 0
```

and rank two over `F_2`, with diagonal kernel `(1,1,1)`. So this is a new exact source-marked coupling, but it does **not** force any `d_i=1` and gives no branch pruning by itself. It is not yet a common 2-cover, Selmer complex, or Cassels-pairing obstruction.

Artifacts:

- `stages/stage35-ex/35ex-35/goal4au-three-direction-marked-kummer-gcd-allocation-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4au-three-direction-marked-kummer-gcd-allocation.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4au_three_direction_marked_kummer.py`

## Freshness

Current `main` observed before the Goal4AU commit is `119e24100dd943cadef39df783a7b5de7b3a5704`. PR #1723 is ahead 37 / behind 7 from merge-base `42f20e47babdfdda068a605e3fec489eeace460c`. The seven main-side commits inspected change Stage32-EX1 / Stage32-EX5 / Stage32 routing and Stage36 material; no Stage35-EX mathematical source drift was observed. No freshness credit is claimed and no sync is performed in this provisional leaf.

## Next exact leaf

```text
35EX-35_GOAL4AV_CROSS_FACE_MARKED_KUMMER_COMMON_COVER_PREFLIGHT
```

Test whether `d_A*d_B*d_C=1` lifts to a source-derived common 2-cover / fiber product / Cassels-pairing constraint that excludes the physical marked triple. If the relation remains only a rank-two squareclass shadow, freeze it as non-pruning before switching route.

No merge. No hostile-audit credit is added by this handoff.
