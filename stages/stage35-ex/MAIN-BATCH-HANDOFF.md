# Stage35-EX MAIN batch handoff — Goal4BD simultaneous three-marked receiver endpoint equivalence

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4BD are provisional stacked research leaves on PR #1723. No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted here.

## Exact-green parent

Goal4BC is exact-green:

- exact head: `d10024852a7f32605e769edf3c2b57406ea1175e`
- aggregate: `34303815379`
- `verify-stage35-ex-current`: `102317031982`
- result: `SUCCESS`

Goal4BC exhausted the old Goal4AS seven-lens ledger and selected the materially new simultaneous three-marked Goal4L fiber-product receiver.

## Goal4BD provisional exact result

Use cyclic orientations

```text
p_A=-B/C, z_A=D_AB/D_AC,
p_B=-C/A, z_B=D_BC/D_AB,
p_C=-A/B, z_C=D_AC/D_BC.
```

Each lies on the Goal4L quartic/elliptic receiver. The common physical endpoint imposes four generically independent cross equations:

```text
p_A*p_B*p_C=-1,
z_A*z_B*z_C=1,
z_A^2*p_C^2*(1+p_B^2)=1+p_C^2,
z_B^2*p_A^2*(1+p_C^2)=1+p_A^2.
```

The third cyclic face-ratio equation follows. An exact Jacobian witness from `(A,B,C)=(44,117,240)` gives cross rank 4. The product of the three quartic surfaces has dimension 6, hence the joint receiver has generic dimension 2, equal to the normalized endpoint surface.

After imposing the face-ratio equations, the A quartic simplifies exactly to

```text
eta_A^2
 = [A*(B^2-C^2)/(B*C*(A^2+C^2))]^2
   * (A^2+B^2+C^2),
```

and cyclic analogues hold. Therefore a rational joint receiver point forces the space-square condition.

The rational `z_i` also force

```text
[A^2+B^2]=[A^2+C^2]=[B^2+C^2]=delta.
```

After primitive integer scaling, `delta` must be trivial:

- an odd prime in the squarefree representative of `delta` divides all three face sums, hence by `2A^2=R_AB+R_AC-R_BC` and cyclic identities divides all three edges, contradicting primitivity;
- the only remaining nontrivial class is `2`; that would make all three face sums even, force all primitive edges odd, and give `W^2=3 mod 8`, impossible.

Thus `delta=1`. All three face diagonals are rational, and the quartic already recovered the rational space diagonal. Conversely every physical endpoint gives the three marked points and cross equations.

Exact result:

```text
simultaneous three-marked Goal4L joint receiver
<=> positive rational perfect-cuboid endpoint
```

on the retained positive/source open, modulo the already controlled scaling/relabel/sign/exceptional conventions.

So B1 is **endpoint-equivalent**, not a smaller receiver and not a pruning theorem. `S34-W03` is not triggered because no independently simpler receiver intersection remains.

Artifacts:

- `stages/stage35-ex/35ex-35/goal4bd-simultaneous-three-marked-rankjump-endpoint-equivalence-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4bd-simultaneous-three-marked-rankjump-endpoint-equivalence.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4bd_three_marked_endpoint_equivalence.py`

## Freshness

No freshness credit. Main-side drift observed in this batch is Stage32 / Stage36 only; no Stage35-EX mathematical source drift was found. No rebase/sync is performed for this provisional leaf.

## Next exact leaf

```text
35EX-35_GOAL4BE_GCD_RESERVOIR_QUADRATIC_RECIPROCITY_CYCLE_PREFLIGHT
```

Test whether AU's exact reservoirs `h_a,h_b,h_c` and the three primitive Pythagorean faces force a non-tautological Jacobi/quadratic-reciprocity cycle beyond the already-known relation `d_A*d_B*d_C=1`.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
