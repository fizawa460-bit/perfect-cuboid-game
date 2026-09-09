# Stage35-EX MAIN batch handoff — Goal4AV provisional common coefficient package / non-pruning common-cover verdict

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4AV are a provisional stacked research surface on PR #1723 and grant no E1, Stage35, endpoint, or Perfect Cuboid credit.

## Exact-green parent

Goal4AU is green at:

- head: `2e9972a64cfa31d2116ea70a9728a64cb083b5e3`
- aggregate run: `34292248229`
- `verify-stage35-ex-current`: `102282485273`
- conclusion: `SUCCESS`

Goal4AU proved the exact source-marked relation

```text
K_A*K_B*K_C=S^2,
d_A*d_B*d_C=1 in Q*/Q*^2,
```

with

```text
K_A=z^2*k_A*b0*c0,
K_B=y^2*k_B*a0*c0,
K_C=x^2*k_C*a0*b0,
S=2*x*y*z*a0*b0*c0.
```

## Goal4AV provisional exact result

The three marked Kummer lines can be extracted into the common coefficient group

```text
H^1(Q,mu_2)=Q*/Q*^2,
chi_A=[K_A], chi_B=[K_B], chi_C=[K_C],
chi_A+chi_B+chi_C=0.
```

This gives an exact common coefficient torsor package. If

```text
T_A: t_A^2=K_A,
T_B: t_B^2=K_B,
T_C: t_C^2=K_C,
```

then the product has two sign components because

```text
(t_A*t_B*t_C/S)^2=1.
```

On the positive component,

```text
t_A*t_B*t_C=S,
t_C=S/(t_A*t_B),
```

so

```text
Q(sqrt(K_A),sqrt(K_B),sqrt(K_C))
 = Q(sqrt(K_A),sqrt(K_B))
```

and the common coefficient extension has degree at most four.

This does **not** produce a common endpoint 2-cover obstruction. A physical marked point may carry a nonzero Kummer class. Requiring a rational point on the biquadratic coefficient torsor would be equivalent to requiring

```text
d_A=d_B=d_C=1,
```

which is exactly the unproved conclusion, not an endpoint hypothesis. Formally `(u,v,u*v)` gives arbitrary nontrivial product-one triples, so the relation retains two independent squareclass parameters.

The three cyclic Goal4L elliptic curves / `E_i[2]` modules / local Selmer conditions are not identified, and no inter-curve isogeny or common Selmer complex is source-locked. Hence no Cassels-pairing identity or obstruction is obtained.

Route classification for the concrete Goal4AU product-one mechanism:

```text
NEW_COMMON_SELMER_OR_CASSELS_COUPLING
  -> BLOCKED_NONPRUNING_COEFFICIENT_TORSOR_SHADOW
```

This blocks only the current mechanism; a future revival would require a genuinely new source-compatible transport between the three 2-torsion/Selmer structures.

Artifacts:

- `stages/stage35-ex/35ex-35/goal4av-cross-face-marked-kummer-common-cover-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4av-cross-face-marked-kummer-common-cover.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4av_common_cover.py`

## Freshness

Current `main` observed before Goal4AV is `119e24100dd943cadef39df783a7b5de7b3a5704`. PR #1723 is ahead 38 / behind 7 from merge-base `42f20e47babdfdda068a605e3fec489eeace460c`. The seven main-side commits are Stage32-EX1 / Stage32-EX5 / Stage32 routing and Stage36 changes; no Stage35-EX mathematical source drift was observed. No freshness credit is claimed and no sync is performed in this provisional leaf.

## Next exact leaf

```text
35EX-35_GOAL4AW_MARKED_ELLIPTIC_HEIGHT_LOWER_VS_GOAL4M_UPPER_PREFLIGHT
```

Move to the quantitative marked-point route: compare a source-locked explicit canonical-height lower bound on the physical Goal4L non-torsion point with the exact Goal4M `O(log B)` endpoint upper window, including constants and parameter-height adapters. Only a strict asymptotic/constant win may be credited as eventual elimination.

No merge. No hostile-audit credit is added by this handoff.
