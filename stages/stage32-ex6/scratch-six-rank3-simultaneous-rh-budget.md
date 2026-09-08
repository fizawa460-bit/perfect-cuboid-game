# Stage32EX6 scratch — six rank-3 simultaneous RH budget

Status: `SCRATCH_EXACT_BOUNDED_SIX_RANK3_SIMULTANEOUS_RH_BUDGET_NO_ENDPOINT_CREDIT`

Scratch only. This leaf does not update `MAIN-STATE`, exclude O266, authorize O264 descent, create hostile-audit credit, or advance Stage32 MAIN.

## Source locks

- PR #1715 retained EX6 head used for authority context:
  `5e8e0cd64a1cb74574f8dff9b43d33ecfbf937e7`.
- O266 fixed target: `d=186`, `e=266`, geometric genus one, V6.
- Retained AR slack at O266:
  `80 = Q + Eta + Rrho`, where
  `Q=q81_node+q105_node`, `Eta=eta81+eta105`, and
  `Rrho=rho81+rho105`.
- Scratch rank-3 ruling leaf:
  `scratch-rank3-fibration-ruling-fourjet-adapter-wall.md`.
- Scratch standard-cusp theta adapter:
  `scratch-standard-cusp-r3-theta-fourjet-adapter.md`.
- Pinned Stoll--Testa verification/source as recorded in those leaves.
- Replay verifier:
  `scratch_verify_six_rank3_simultaneous_rh_budget.py`.

## 1. Six rank-3 base blocks can be used without numbered EXC mapping

The six rank-three fibrations have six disjoint eight-node base sets whose union is the 48 singular points. Therefore this leaf needs only the six-block partition, not an explicit `EXC_001,...,EXC_048` numbering adapter.

For block `j`, let `M_j` be the total exceptional intersection mass of the O266 carrier on its eight nodes. At O266 every branch has exceptional contact one, so `M_j` is also the number of node branches belonging to that block.

The six blocks partition the node contacts, hence

`sum_j M_j = 266`.

The rank-three pencil relation is

`2F_j = H - sum_{P in block j} E_P`.

Thus the induced genus-one normalization map has degree

`n_j = C.F_j = (186-M_j)/2`.

Consequently every `M_j` is even. The retained V6 exceptional support has only one zero exceptional index; together with parity this gives the safe block lower bound `M_j>=8`. Nonconstancy of the rank-three map gives `M_j<=184`.

Therefore the exact scalar partition domain used below is

- six even integers `M_j`;
- `8 <= M_j <= 184`;
- `sum M_j = 266`.

No sampled six-block mass ordering is used.

## 2. Required nonminimal branches for rank3-r-flatness

Let `L_j` be the number of nonminimal node branches in block `j`. Then the number of FSM-minimal branches in that block is `M_j-L_j`.

Define rank3-`r`-flat to mean that the global rank-three fibration parameter has local degree at least `r+1`; each such minimal branch consumes at least `r` Riemann--Hurwitz units.

The full RH degree of the block map is

`deg R_j = 2n_j = 186-M_j`.

If every minimal branch in block `j` were rank3-`r`-flat, necessarily

`r*(M_j-L_j) <= 186-M_j`.

Hence

`L_j >= max(0, M_j-floor((186-M_j)/r))`.

Minimizing the sum of these requirements over the exact six-block partition domain gives:

| r | minimum total nonminimal branches required |
|---:|---:|
| 2 | 0 |
| 3 | 0 |
| 4 | 54 |
| 5 | 96 |
| 6 | 125 |
| 7 | 145 |

The verifier recomputes these values by finite dynamic programming. Example minimizing partitions are also emitted by the verifier; they are witnesses for the minima, not asserted actual V6 block masses.

## 3. Coupling to the O266 AR slack

Every nonminimal O266 node branch has `(A,B)!=(1,1)` and, since `min(A,B)=1` with the same parity constraint, contributes at least one unit to exactly one of `q81_node,q105_node`. Thus the total number `L` of nonminimal node branches satisfies

`L <= Q`.

Using `Q=80-E`, where

`E := Eta+Rrho >=0`, we have

`L <= 80-E`.

Now allow some minimal branches to fail rank3-`r`-flatness. Let `F_r` be the number of such failures. Replacing a required flat minimal branch by either one nonminimal branch or one flatness failure can relieve at most one branch-count requirement, so

`L + F_r >= N_r`,

where `N_r` is the six-block minimum from the table.

Therefore

`F_r >= max(0, N_r-Q)`.

Substituting `Q=80-E` yields the exact lower bounds

- `F_4 >= max(0,E-26)`;
- `F_5 >= 16+E`;
- `F_6 >= 45+E`;
- `F_7 >= 65+E`.

In particular, independently of the unknown eta/rho split, at least sixteen FSM-minimal O266 branches fail rank3-five-flatness.

This is a branch-level necessary statement. It does not identify which coefficient fails, prescribe a landing value, or produce an eta/rho upper bound.

## 4. Relation to the standard-cusp theta adapter

The standard-cusp scratch adapter gives

`T = u + u*(1-u^8)*x^4 + O(x^8)`

and, for a minimal AN branch,

`d4 = c4 + lambda*(1-lambda^8)`.

Therefore rank3-four-flatness is not the same as raw AN four-flatness unless the fourth coefficient satisfies the corrected relation. The six-block RH budget here charges only genuine rank3-flatness of the global pencils; it does not silently replace it by AN coefficient flatness.

The new lower bounds sharpen the next member-level target: a fixed-V6 theorem forcing rank3-five-flatness on all minimal branches is impossible under O266, because at least `16+E` minimal branches must fail it. To turn that anti-flatness into endpoint exclusion one would need an independent theorem forcing the opposite behavior on a population larger than the allowed failure set.

## Canonical scratch decisions

- `SIX_RANK3_BASE_BLOCKS_PARTITION_48_NODES = true`;
- `NUMBERED_EXC_TO_BLOCK_ADAPTER_REQUIRED_FOR_THIS_SCALAR_OPTIMIZATION = false`;
- `SIX_BLOCK_MASS_SUM = 266`;
- `SIX_BLOCK_MASSES_EVEN = true`;
- `SIX_BLOCK_SAFE_DOMAIN = even M_j in [8,184], sum=266`;
- `ALL_MINIMAL_RANK3_R4_FLAT_REQUIRES_NONMINIMAL_AT_LEAST = 54`;
- `ALL_MINIMAL_RANK3_R5_FLAT_REQUIRES_NONMINIMAL_AT_LEAST = 96`;
- `ALL_MINIMAL_RANK3_R6_FLAT_REQUIRES_NONMINIMAL_AT_LEAST = 125`;
- `ALL_MINIMAL_RANK3_R7_FLAT_REQUIRES_NONMINIMAL_AT_LEAST = 145`;
- `RANK3_R4_FLAT_FAILURES_GTE = max(0,E-26)`;
- `RANK3_R5_FLAT_FAILURES_GTE = 16+E`;
- `RANK3_R6_FLAT_FAILURES_GTE = 45+E`;
- `RANK3_R7_FLAT_FAILURES_GTE = 65+E`;
- `UNIFORM_RANK3_FIVE_FLATNESS_ON_ALL_MINIMAL_BRANCHES = impossible_under_O266`;
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No actual six-block V6 mass vector is claimed.
- The prior sampled vector `[10,46,42,54,62,52]` is not used.
- Rank3-r-flatness is a global-pencil local-degree condition; AN coefficient flatness is not substituted without the theta adapter.
- The AR scalar identity is coupled once; it is not double-charged as an independent eta/rho saving.
- No member equation forcing flatness or anti-flatness is claimed.
- No hostile audit, retained consolidation, Stage32 MAIN, lower-O, or Perfect Cuboid credit follows.
