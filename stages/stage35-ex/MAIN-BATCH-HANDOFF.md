# Stage35-EX MAIN batch handoff — Goal4BF source-oriented Gaussian quartic lift

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4BF are provisional stacked research leaves on PR #1723. No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted here.

## Exact-green parent

Goal4BE is exact-green:

- exact head: `c44909b47f00091da6229d60304786dc446f6a37`
- aggregate: `34305612045`
- `verify-stage35-ex-current`: `102322719891`
- result: `SUCCESS`

Goal4BE proved that every reservoir prime is `1 mod 4` and obtained the new Jacobi cycle

```text
L_a*L_b*L_c=1,
```

while the pairwise-symbol system remains rank 2 with one free Jacobi bit.

## Goal4BF provisional exact result

For `ell|s_a`, the source-selected root

```text
iota_a(ell)=x*b/(y*c) mod ell,
iota_a(ell)^2=-1
```

selects one Gaussian prime ideal

```text
p_{a,ell}=(ell,i-iota_a(ell)).
```

It divides `x*b-i*y*c`, while its conjugate does not. Since

```text
N(x*b-i*y*c)=r_BC^2,
```

the selected valuation is exactly

```text
v_{p_{a,ell}}(x*b-i*y*c)=2*v_ell(r_BC).
```

Choose the unique primary generator `pi_{a,ell} == 1 mod (1+i)^3` and form

```text
Sigma_a=product_{ell|s_a} pi_{a,ell},
```

cyclically. Then

```text
N(Sigma_a)=s_a,
s_a=Sigma_a*bar(Sigma_a),
```

and likewise for `b,c`. Thus the source canonically chooses an oriented Gaussian half of every squarefree reservoir kernel.

At each selected prime,

```text
[x*b/(y*c) / pi_{a,ell}]_4=[i/pi_{a,ell}]_4,
```

so this is a genuine quartic lift of Goal4BE; squaring recovers its quadratic character.

Standard quartic reciprocity exchanges oriented factors such as

```text
[Sigma_a/Sigma_b]_4 <-> [Sigma_b/Sigma_a]_4
```

up to the explicit norm correction. But the rational reservoir is

```text
s_b=Sigma_b*bar(Sigma_b),
```

so the canonical quartic lift

```text
U_ab=[s_b/Sigma_a]_4
```

contains both oriented and cross-conjugate phases. Define, for example,

```text
G_ab=[bar(Sigma_b)/Sigma_a]_4.
```

The current source equations supply no independent relation fixing all such `G_ij`. Hence

```text
U_ab^2=(s_b/s_a)
```

recovers the BE bit, but quartic reciprocity alone does not determine the lift or eliminate the remaining Jacobi freedom.

Goal4BE's `ell=5` local witness also preserves the same source root/orientation while interchanging the individual quartic contributions of `x` and `b`, confirming the phase boundary locally.

Exact consequence:

```text
source-oriented Gaussian lift = yes;
quartic reciprocity applicable = yes;
cross-conjugate mu_4 phase gauge remains = yes;
BE free bit closed = no;
branch pruning = no.
```

This does not reopen Goal4AX's rational norm-torus route; the new datum is integral prime orientation plus quartic phase.

Artifacts:

- `stages/stage35-ex/35ex-35/goal4bf-oriented-gaussian-quartic-reciprocity-reservoir-lift-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4bf-oriented-gaussian-quartic-reciprocity-reservoir-lift.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4bf_oriented_gaussian_quartic_lift.py`

## Freshness

Current main observed: `b4357252bf492a0934fe47812ffa2421a342f954`. Main-side changes since the audited Stage35-EX merge base are Stage32 / Stage36 only; no Stage35-EX mathematical source drift was observed. No freshness credit and no rebase/sync.

## Next exact leaf

```text
35EX-35_GOAL4BG_GAUSSIAN_SQUARE_ROOT_FACE_PHASE_COMPATIBILITY_PREFLIGHT
```

Write each primitive Pythagorean face factor as a unit times a Gaussian square, source-lock its unit and conjugation choice, and test whether the three face square roots together with the common space diagonal provide enough cross-phase equations to fix the `G_ij` gauge left by Goal4BF.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
