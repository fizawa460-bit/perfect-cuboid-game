# Stage33 33-12 V71/V73/V75 J1 torsor / kernel-fingerprint micro-roadmap

```text
ROLE=PLANNING_AND_EXECUTION_CHECKLIST_ONLY
LIVE_GLOBAL_AUTHORITY=stages/stage33/controller.json
BRANCH_EXACT_FRONTIER=stages/stage33/33-12/e3-b1-c22-j1-generic-quotient-discriminator-rejection-v75.json
CURRENT_LOCKED_FRONTIER=V61_THROUGH_V75_WITH_V68_V69_TRANSPORT_REDUCTION
EFFECTIVE_DISCOVERY_ROUTING=V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP
CURRENT_LEAF=D2_2_MATERIALIZE_J1_SPECIFIC_GLOBAL_INTEGRAL_KERNEL
ATOMICITY_RULE=ONE_SMALL_VERIFIABLE_GOAL_PER_COMMIT
MERGE_ALLOWED=false
```

This roadmap supersedes `ROADMAP-33-12-V65-J1-DISCRIMINATOR.md` only for the current branch leaf. Exact certificates, controller firewalls, and `MAIN-STATE.json` remain authoritative over prose.

## Locked frontier

- V61-V64 fix the B1 basis, literal `lambda_A={f_A,g22}`, `kappa_A=J1`, `kappa_D=J2`, and `J2 -> u1=[1,0]`.
- V65 leaves exactly `J1 -> u2=[0,1]` or `J1 -> u1+u2=[1,1]`; target minimum norms are respectively `4` and `12`.
- V67 closes only the #1529 equivariance signal route: it supplies no J1/J2 target action or second transport column.
- V68-V69 reduce the remaining transport to exactly identity versus the unique shear fixing `u1`; one bit remains. V70 replays this reduction immutably.
- V71 materializes the J1-specific Creutz--Viray E[2] cocycle from `(f1,1)`, with splitting field `Kgeom(sqrt(f1))` and `rho_f1 -> Tr`.
- V73 materializes the J1-specific direct translation torsor from that same cocycle:
  `d*V^2=N^4-2*a*d*N^2*Z^2+d^2*q^2*Z^4`, `d=f1`, Jacobian `E`.
  Its bisection is the genus-0 `r1,r4` double cover.
- V75 replays `X=n^2/d`, `Y=-n*v/d` and proves that the generic degree-two quotient is `E'_Tr` independently of `d`. The quotient therefore does not distinguish J1 from the retained J2 route.
- V75 fail-closes transplantation of the J2 R4 lattice conclusion: it would force minimum norm `8` / `u1`, excluded by the locked V65 J1 gate. No underlying mathematical contradiction is claimed; the missing datum is surface-level and J1-specific.
- Stage33 remains `6/11`; Stage33-12 is open; Stage33-13 is unreleased; merge is forbidden.

## Arsenal routing

Use `docs/arsenal/index.json` first. Current cards:
- `S33-PW07` — primary route for torsor -> compactified NS/component glue -> integral/twisted kernel.
- `S33-PW04` — exact marked-source firewall when a fingerprint is transported to the fixed marked Kc frame.

Historical contact/Weil pairing data were reevaluated after V69. They determine the source character frame but do not distinguish identity from shear; do not reopen that route without a materially new target-side datum.

## D2.1 — materialize the J1 translation torsor — PASS V73

Exact object:

```text
d=f1=(t-r1)/(t-r4)
tilde_rho=tau_Tr o rho

d*V^2 = N^4 - 2*a*d*N^2*Z^2 + d^2*q^2*Z^4

a=(t^2+1)^2
b=[2*t*(t^2-1)]^2
a^2-4*b=q^2
```

V73 verifies the semilinear invariants `n=w*y/x`, `u0=x+b/x`, `v=w*(x-b/x)`, the elimination to the quartic, the original Jacobian `E`, and the `r1,r4` bisection. No minimum norm or marked coordinate is selected.

## D2.2a — generic quotient discriminator — REJECTED V75

The exact quotient map

```text
X=n^2/d
Y=-n*v/d
```

eliminates `d` and gives

```text
Y^2=X*(X^2-2*a*X+q^2).
```

This is useful as a method check but not as a J1 fingerprint. Do not transplant the J2 R4 pullback-lattice/index conclusion from this generic quotient alone.

## D2.2b — J1-specific global integral kernel — CURRENT

Exact missing interface:

`J1_SPECIFIC_COMPACTIFIED_SURFACE_INTEGRAL_KERNEL_OR_PRIMITIVE_PULLBACK_IDENTIFICATION`

Acceptance requires one of:
- exact resolved singular-fiber/component configuration and primitive NS/component glue for the V73 J1 compactified torsor;
- equivalent integral transcendental-kernel computation tied specifically to `lambda_A/J1`;
- exact surface-level proof of the relevant degree-two pullback image and primitive index for J1, including bad-fiber/compactification data;
- independent marked transport witness selecting the second column directly.

The final fingerprint must be:
- `4` => `J1 -> u2` => shear transport;
- `12` => `J1 -> u1+u2` => identity transport.

Minimum norm `8` is the retained J2 fingerprint and is not admissible for J1 under V65. Same-generic-quotient, same-j-invariant, and isogeny-cover substitution are insufficient.

## D1 / D3 fallback

D1 exact second transport column and D3 exact source+target automorphism equivariance remain admissible only if a materially new source-locked datum appears. Do not perform open-ended search; the active constructive route is D2.2b.

## D4 — decode marked proper14 column 3

Blocked until the one bit is selected. Then bind J1 to the fixed marked Kc coordinate, construct the exact marked Picard-dual covector/equivalent adapter, and decode proper14 column 3.

## D5 — finish B1 14x4 and mask20 solve

Blocked on D4 and exact conjugate-column transport. Only after all four columns are exact may `M*x=mask20` be solved and membership credit considered.

## Firewalls

Forbidden: direct identification of contact `(L,R)` with marked Kc bits; arbitrary GL2 complement; relabelling J2 torsor/kernel as J1; transplantation of J2 R4 lattice/index from the `d`-independent quotient alone; choosing identity because it is simpler; choosing shear by naming convention; search-miss-to-absence promotion; merge/closure/receiver/endpoint/theorem/perfect-cuboid credit.

## Batch rule

Each `stage33main batch` works the first unfinished leaf, uses Arsenal first, constructs/replays one exact object per commit, and reevaluates this roadmap.
