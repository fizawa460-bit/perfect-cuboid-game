# Stage35-EX MAIN batch handoff — Goal4BB arbitrary finite Brauer subgroup nonobstruction

Audited authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4AL–Goal4BB are provisional stacked leaves on PR #1723. No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted here.

## Exact-green parent

Goal4BA is exact-green:

- exact head: `540721b4046a0849fc6fe162025e6c8d46898850`
- aggregate: `34301954559`
- `verify-stage35-ex-current`: `102311776547`
- result: `SUCCESS`

Goal4BA proved that every finite truncation of the visible three-unit character family together with the known A/B classes is non-obstructing on `A_src^loc`.

## Goal4BB provisional exact result

Goal4BB removes the visible-family restriction. Let

```text
F={alpha_1,...,alpha_r} subset Br(U)
```

be any fixed finite set, with no algebraicity or explicit-symbol assumption.

Use the rational smooth anchor

```text
P*=(272/225,0,353/225,1,272/225,353/225).
```

For a common finite bad set containing infinity, 2, primes `<173`, denominator/model primes, and all primes needed to spread out every `alpha_j`, local constancy gives one common neighborhood of `P*` for all classes. Choose nonzero-y local deformations there, imposing at 2

```text
v2(y)>4=v2(x)
```

and at infinity `y>0`.

Outside the bad set, use the 35EX-22 integral smooth `U_PC(Z_ell)` points. Every `alpha_j` extends over the common smooth model after enlarging the finite bad set; evaluation at an integral point lands in

```text
Br(Z_ell)=Br(F_ell)=0.
```

Hence every local invariant of the constructed adele equals the corresponding local invariant of the diagonal rational anchor `P*`. Global reciprocity then gives

```text
(A_src^loc)^F != empty
```

for every finite `F subset Br(U)`. Equivalently every finite subgroup `B0 subset Br(U)` is non-obstructing.

This includes arbitrary fixed transcendental classes. It does **not** imply nonemptiness for the full infinite intersection `(A_src^loc)^Br(U)`. Goal4AR's full-Brauer endpoint equivalence remains intact. Therefore any Brauer obstruction capable of closing E1 on this local population must be genuinely infinite; no finite Brauer shortcut remains.

Artifacts:

- `stages/stage35-ex/35ex-35/goal4bb-arbitrary-finite-brauer-subgroup-nonobstruction-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4bb-arbitrary-finite-brauer-subgroup-nonobstruction.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4bb_arbitrary_finite_brauer_subgroup.py`

## Freshness

Current main observed: `9346a1b0cfdb6f2e8abe93b4aef9987698eeeb47`. Main-side drift since audited merge base is confined to Stage32 / Stage36 files. No Stage35-EX mathematical source drift was observed. PR #1723 currently reports `mergeable=false`; no freshness credit is claimed and no rebase/sync is performed for this provisional leaf.

## Route consequence

Goal4AS candidate ledger is now exhausted under the currently materialized exact views:

- marked Kummer/common-cover: AT/AU/AV;
- canonical height: AW;
- cross-face norm/torsor: AX;
- nonlinear endpoint descent: AY;
- super-sqrt amplification: AZ;
- finite Brauer shortcut: BA/BB.

Next exact leaf:

```text
35EX-35_GOAL4BC_POST_GOAL4AS_LEDGER_EXHAUSTION_FRESH_VIEW_AUDIT
```

Perform a fresh blind plus arsenal-deduplicated breadth audit. Do not recycle an exhausted view unless a materially new invariant appears.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains V74 / Goal4AK.
