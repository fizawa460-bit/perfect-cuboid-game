# Stage32 LGS × MB101/102 re-entry preflight

Status: REOPENED_FOR_SOURCE_LOCKED_PREFLIGHT_ONLY

This leaf reopens exactly one historical EX5 breadth-cycle blocker:

`LGS_MISSING_POPULATION_WIDE_GLOBAL_TO_LOCAL_DEFECT_ADAPTER`

It does not reopen the frozen EX5 breadth cycle as a whole and does not duplicate current EX5 BC2, FULL178/178, CUT, MB104, HPADJ, or MAIN GRF work.

## Historical blocker

The audited EX5 breadth-cycle-1 terminal classified LGS as BLOCKED because no population-wide exact adapter connected retained global Stage32 carrier data to a local defect/genus ledger.

## New input that did not exist at that terminal

The retained 32-03 multibranch lane now contains:

- MB101: exact `R29-LG2-MB` population / normalization-profile adapter, with branch counts `r_i`, exceptional masses `M_i`, exact multibranch predicate `some r_i >= 2`, and global inequalities `N <= R <= M`.
- MB102: exact local branch/delta/global genus-correction ledger, including
  `delta_P = sum_a delta(beta_a) + sum_{a<b} I_P(beta_a,beta_b)`
  and
  `D^2 + d = 2g - 2 + 2*Delta_total`, with `Delta_total=Delta_exc+Delta_off`.

These inputs materially change the historical LGS blocker state: the old route is no longer blocked merely by absence of a multibranch population adapter or by absence of a typed local-defect/global-genus ledger.

## Exact question for this re-entry

Determine whether MB101+MB102 supply an exact semantic crosswalk for the historical LGS target population and, if so, identify the *next* smallest load-bearing missing statement needed to turn the ledger into a population-wide obstruction.

Allowed outcomes are only:

1. `DIRECT_RECONNECT` — exact population/object/quantifier identity is source-locked and LGS may continue from the post-adapter frontier;
2. `FINITE_EXCEPTION_REDUCTION` — the new adapters reduce LGS to an explicitly bounded residual family;
3. `SEMANTIC_ADAPTER_GAP` — MB101/102 are structurally relevant but do not identify the exact historical LGS objects/population;
4. `NO_NEW_INFORMATION` — the historical blocker remains substantively unchanged.

## What this leaf must not do

- no FULL178 row/terminal enumeration;
- no EX5 BC2 solver replay;
- no CUT finite-ring rerun;
- no MB104 conductor/monodromy continuation;
- no new heavy compute;
- no Stage32 MAIN authority or pruning mutation;
- no receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.

This is a source-lock/crosswalk preflight only. Any mathematical continuation after `DIRECT_RECONNECT` or `FINITE_EXCEPTION_REDUCTION` requires a separate retained checkpoint and hostile audit.