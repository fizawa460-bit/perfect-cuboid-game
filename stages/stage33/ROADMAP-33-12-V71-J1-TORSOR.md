# Stage33 33-12 V71/V73 J1 torsor / kernel-fingerprint micro-roadmap

```text
ROLE=PLANNING_AND_EXECUTION_CHECKLIST_ONLY
LIVE_GLOBAL_AUTHORITY=stages/stage33/controller.json
BRANCH_EXACT_FRONTIER=stages/stage33/33-12/e3-b1-c22-j1-translation-torsor-v73.json
CURRENT_LOCKED_FRONTIER=V61_THROUGH_V73_WITH_V68_V69_TRANSPORT_REDUCTION
EFFECTIVE_DISCOVERY_ROUTING=V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP
CURRENT_LEAF=D2_2_COMPUTE_J1_TWISTED_KERNEL_MINIMUM_NORM
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
- V73 does not reuse the J2 squareclass, J2 minimum norm `8`, or J2 marked coordinate.
- Stage33 remains `6/11`; Stage33-12 is open; Stage33-13 is unreleased; merge is forbidden.

## Arsenal routing

Use `docs/arsenal/index.json` first. Current cards:
- `S33-PW07` — primary route for torsor -> NS/component glue -> integral/twisted kernel.
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

## D2.2 — compute an independent J1 twisted-kernel fingerprint — CURRENT

Acceptance:
- use the V73 J1 torsor, not the J2 torsor;
- compute the resolved singular-fiber/component configuration and the primitive NS lattice, or an equivalent integral kernel invariant;
- identify the J1 twisted transcendental/kernel lattice integrally;
- obtain exactly minimum norm `4` or `12`;
- replay the target lookup from `j2-cv-d2-semantic-orientation.json`;
- source-lock every bridge from the quartic to the lattice fingerprint.

Decision:
- `4` => `J1 -> u2` => shear transport;
- `12` => `J1 -> u1+u2` => identity transport.

No use of the retained J2 minimum norm `8` except as method/reference data. Same-j-invariant or isogeny-cover substitution is forbidden.

## D1 / D3 fallback

D1 exact second transport column and D3 exact source+target automorphism equivariance remain admissible only if a materially new source-locked datum appears. Do not perform open-ended search; the active constructive route is D2.

## D4 — decode marked proper14 column 3

Blocked until the one bit is selected. Then bind J1 to the fixed marked Kc coordinate, construct the exact marked Picard-dual covector/equivalent adapter, and decode proper14 column 3.

## D5 — finish B1 14x4 and mask20 solve

Blocked on D4 and exact conjugate-column transport. Only after all four columns are exact may `M*x=mask20` be solved and membership credit considered.

## Firewalls

Forbidden: direct identification of contact `(L,R)` with marked Kc bits; arbitrary GL2 complement; relabelling J2 torsor/kernel as J1; choosing identity because it is simpler; choosing shear by naming convention; search-miss-to-absence promotion; merge/closure/receiver/endpoint/theorem/perfect-cuboid credit.

## Batch rule

Each `stage33main batch` works the first unfinished leaf, uses Arsenal first, constructs/replays one exact object per commit, and reevaluates this roadmap.
