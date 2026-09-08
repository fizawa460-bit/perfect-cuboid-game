# Stage32EX6 — rho-coupled minimal-branch count and uniform four-jet threshold

Status: `SCRATCH_EXACT_BOUNDED_RHO_COUPLED_FOURJET_THRESHOLD_NO_ENDPOINT_CREDIT`.

This is an isolated micro-diagnostic on branch `scratch/stage32-ex6-simultaneous-critical-support`, continuing PR #1715 exact retained head `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`. It is not MAIN authority, not a retained consolidation, and does not update `MAIN-STATE.json`.

## Scope

Assume the same hypothetical integral irreducible geometric-genus-one V6 carrier at `O=266`, with normalization `N`, and the same projective-connection scratch adapter chain.

Retained post1648AR gives at O266 (`t=0`):

`52 = q81_node + eta81 + rho81`,

`28 = q105_node + eta105 + rho105`.

Write

- `Q = q81_node + q105_node`;
- `Eta = eta81 + eta105`;
- `Rrho = rho81 + rho105`.

Then exactly

`80 = Q + Eta + Rrho`.

Previous scratch full-H descent gives a nonzero meromorphic quadratic differential `barTheta` on the genus-one normalization `N`, and for the number `B_r` of projectively r-flat FSM-minimal downstairs node branches,

`B_r <= floor((690 + 4*Rrho)/r)`.

A sufficient coefficient condition for projective r-flatness is

`mu1=...=mur=0`.

The question here is whether the number of FSM-minimal branches itself improves as `Rrho` increases, and whether that coupling lowers the previously identified uniform six-jet threshold.

## Exact rho-dependent lower bound for minimal branches

At O266 every node branch has exceptional contact `min(A,B)=1`.

A node branch is nonminimal iff `(A,B)!=(1,1)`. Since `A+B` is even, every such branch has the other local factor order at least 3. Therefore it contributes

`b=|A-B|/2 >= 1`

to exactly one of the two node-boundary resources `q81_node` or `q105_node`.

Let `L` be the number of nonminimal node branches. Then

`L <= Q`.

There are exactly 266 node branches at O266, so if `M` is the number of FSM-minimal branches,

`M = 266-L >= 266-Q`.

Using `Q=80-Eta-Rrho`,

`M >= 186 + Eta + Rrho`.

In particular,

`M >= 186 + Rrho`.

This strictly strengthens the retained AR uniform lower bound 186 whenever off-special ramification is positive. It is still only a necessary branch-count inequality; it does not construct the hypothetical carrier.

## Coupling to the genus-one projective-connection capacity

Suppose every FSM-minimal branch is projectively r-flat. Then

`B_r >= M >= 186 + Eta + Rrho`.

But previous scratch gives

`B_r <= floor((690+4*Rrho)/r)`.

Hence a uniform all-minimal r-flat theorem would be impossible whenever

`r*(186+Eta+Rrho) > 690+4*Rrho`.

### r = 4

For `r=4`, the inequality becomes

`744 + 4*Eta + 4*Rrho > 690 + 4*Rrho`,

which reduces to

`54 + 4*Eta > 0`.

This is automatic.

Therefore:

`ALL_FSM_MINIMAL_BRANCHES_PROJECTIVELY_4_FLAT`

is incompatible with the O266 hypothetical carrier for every allowed O266 slack profile.

Since the local jet adapter gives

`mu1=mu2=mu3=mu4=0 => projectively 4-flat`,

any future source-locked fixed-V6 theorem forcing those four higher odd coefficients to vanish at every FSM-minimal node branch would directly exclude O266 within this scratch adapter chain.

No independent `Rrho<=59` reduction is needed.

### r = 3

For `r=3`, all-minimal projective 3-flatness would contradict O266 only if

`558 + 3*Eta + 3*Rrho > 690 + 4*Rrho`,

i.e.

`3*Eta - Rrho > 132`.

Equivalently, using `80=Q+Eta+Rrho`,

`Q + 4*Eta > 212`.

This is not forced by the retained slack. Hence three-jet flatness is not uniformly sufficient by this divisor route.

Thus four consecutive higher-odd coefficient vanishings are the first uniform threshold obtained from the current exact coupling.

## Cross-check upstairs on D

The same result appears before quotient descent.

A projectively 4-flat minimal branch has four V4-related lifts on `D`, each with `ord Theta>=8`, hence contributes at least

`4*8 = 32`

zero units upstairs.

If every minimal branch were 4-flat, the forced zero degree would be at least

`32*M >= 32*(186+Eta+Rrho)`
`       = 5952 + 32*Eta + 32*Rrho`.

Previous scratch gives for nonzero `Theta`

`deg Zero(Theta) <= 5520 + 32*Rrho`.

The forced amount exceeds capacity by at least

`432 + 32*Eta > 0`.

Hence the four-jet threshold is consistent in both the upstairs and genus-one quotient formulations.

## What this does and does not achieve

This leaf does not prove any coefficient vanishing. It only lowers the strength of the missing member-level theorem.

The projective-connection route no longer needs a uniform six-jet theorem. It would suffice to prove, for every actual FSM-minimal O266 branch of the fixed V6 member,

`mu1=mu2=mu3=mu4=0`,

or directly

`ord(barTheta)>=3`

at every such branch.

The key improvement comes from coupling the same AR slack to two roles without double-counting:

1. `Rrho` enlarges the projective zero-capacity;
2. the same slack identity simultaneously forces more node branches to be FSM-minimal because nonminimal branches require node-boundary resource `Q`.

These are two consequences of one exact identity, used in a single coupled inequality rather than treated as independent savings.

## Decision

Canonical scratch decisions:

- `O266_SLACK_SUM = Q+Eta+Rrho=80`;
- `NONMINIMAL_NODE_BRANCH_COUNT_LTE_Q = true`;
- `FSM_MINIMAL_BRANCH_COUNT_GTE_186_PLUS_Eta_PLUS_Rrho = true`;
- `FSM_MINIMAL_BRANCH_COUNT_GTE_186_PLUS_Rrho = true`;
- `ALL_MINIMAL_PROJECTIVE_4_FLATNESS_INCOMPATIBLE_WITH_O266 = true`;
- `ALL_MINIMAL_COEFFICIENT_FOUR_FLATNESS_WOULD_EXCLUDE_O266 = true`;
- `ALL_MINIMAL_PROJECTIVE_3_FLATNESS_UNIFORMLY_SUFFICIENT = false`;
- `UNIFORM_MEMBER_LEVEL_JET_THRESHOLD_REDUCED_FROM_6_TO_4 = true`;
- `FOUR_JET_FLATNESS_ACTUALLY_PROVED = false`;
- `INDEPENDENT_RRHO_CAP_OBTAINED = false`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`.

## Firewalls

- No global V6 carrier is constructed.
- This leaf depends on the prior scratch projective-connection descent/pole adapters and is not independent retained authority.
- The AR slack is not double-charged as two independent bounds; the branch-count and zero-capacity effects are combined in one inequality.
- No `Rrho<=59` theorem is claimed.
- No four-jet coefficient vanishing theorem is claimed.
- The conditional statement `uniform four-jet flatness on all actual FSM-minimal branches would exclude O266` is not promoted to actual endpoint exclusion.
- No Stage32 MAIN, lower-O, hostile-audit, merge, or Perfect Cuboid credit follows.
