# Stage35-EX MAIN batch handoff — Goal4BN common-W ray boundary

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4BN are provisional stacked leaves on PR #1723. No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted.

## Exact-green parent

Goal4BM is exact-green:

- exact head: `a77e75db00874d66025d5924b95e4939b8b67500`
- aggregate: `34316754364`
- `verify-stage35-ex-current`: `102355710268`
- result: `SUCCESS`

Goal4BM completed the primary `lambda^7` ray dual with

```text
(chi_i,chi_lambda): primary ray group -> mu_4^2
```

and identified the locally admissible order-two blind class represented by `5+4*i`.

## Goal4BN provisional exact result

Put

```text
H=h_a*h_b*h_c,
T=W/H.
```

Since the pairwise-coprime reservoirs all divide the common space diagonal,

```text
N(Psi_a)=h_b*h_c*T,
N(Psi_b)=h_a*h_c*T,
N(Psi_c)=h_a*h_b*T.
```

The source therefore gives three common-norm Gaussian ratios

```text
R_a=Psi_b*Psi_c/(h_a*Psi_a),
R_b=Psi_a*Psi_c/(h_b*Psi_b),
R_c=Psi_a*Psi_b/(h_c*Psi_c),
```

with

```text
N(R_a)=N(R_b)=N(R_c)=T.
```

Their pairwise ratios are explicit norm-one quotients of the original equal-norm space factors, so this is genuine common-`W` coupling but not a new reciprocity value.

More importantly, the full face-plus-space equations admit a `41`-adic secondary model with selected primary prime

```text
pi=5+4*i,
(e_i,e_lambda)=(2,0),
```

and the **same selected prime** realizes both

```text
sigma_a=-1
sigma_a=+1
```

by changing the leading sign of `r_BC` while retaining the common `W` system.

An explicit `v_+` certificate modulo `41^4=2825761` is

```text
a=3280,
r_BC=738,
W=3362,
b=363474,
r_AB=1573794,
r_AC=2553440.
```

All three face equations and all three common-`W` equations vanish modulo `41^4`.

Thus:

```text
common-W norm coupling = exact;
order-two class excluded = no;
same selected order-two prime supports both sigma signs = yes;
Xi forced into proper lambda7 ray subset = no;
branch pruning = no.
```

Artifacts:

- `stages/stage35-ex/35ex-35/goal4bn-common-w-primary-space-root-ray-product-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4bn-common-w-primary-space-root-ray-product.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4bn_common_w_primary_space_root_ray_product.py`

## Next exact leaf

```text
35EX-35_GOAL4BO_DEEPER_LAMBDA8_ORDER_LIFT_PREFLIGHT
```

At `pi=5+4*i`, one has `v_lambda(pi^2-1)=7` and `v_lambda(pi^4-1)=9`, so the class lifts from order two at `lambda^7` to order four at `lambda^8`. Test whether this deeper character level yields a source-controlled orientation constraint or only begins an unbounded deeper ray tower.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
