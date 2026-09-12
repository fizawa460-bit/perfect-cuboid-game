# Stage32 MB104 — hard-sector formal infinite-family feasibility

Status: **RETAINED FORMAL FEASIBILITY / ACTUAL CURVES NOT CONSTRUCTED / MB104 INCOMPLETE / NO CREDIT**

## Routing change

By operator instruction on 2026-09-12, direct attempts to prove

```text
R8 <= alpha*d + beta,  alpha < 1/4
```

are frozen until a genuinely new lever appears. MB104 now prioritizes:

1. global classification of genus-zero full-span carriers;
2. global classification of genus-one support-span 5/6 carriers;
3. construction or nonconstruction of formal infinite families satisfying all currently retained MB104 constraints.

This checkpoint executes item 3.

## Common formal packet

Fix an integer `k>=1`. Choose `N=14` distinct box nodes. At each chosen node put exactly `2k` normalization branches, all FSM-minimal

```text
(A,B)=(1,1),  m=1,
```

with pairwise distinct nonzero exceptional landing keys. Formally this gives

```text
r_i=M_i=2k  on the 14 supported nodes,
R=R8=M=r_odd=28k,
N=N_MB=14,
sum_i M_i^2=56k^2.
```

Taking smooth separated strict-transform germs gives `Delta_total=0` on the resolved curve packet. After contracting the A1 exceptional curves, the sharp conductor model permits

```text
Delta_nodes_down = R-N = 28k-14.
```

No claim is made that these local packets glue to an integral curve or an integral Picard class.

## F0-P6: formal genus-zero full-span family

Take

```text
g=0,
d=28k-4.
```

Use 14 explicit box nodes with rank-3 block counts

```text
[3,3,2,2,2,2].
```

An exact Gaussian-integer minor of seven selected support rows has determinant `8+8i`, so the support spans all `P^6`.

The retained constraints become:

```text
FSM:        28k-4 <= -16 + 4(28k),
Beauville:  r_odd=28k=d+4 and is even,
GFU:        -d+M-4 = 0,
rank3:      block masses [6k,6k,4k,4k,4k,4k] <= d,
Hodge:      56k^2 <= 98k^2+28k-2,
D^2:        -28k+2 <= 21k^2-14k+1,
conductor:  R8 <= (R-N)+48.
```

Also `N=14` lies exactly at the first support size not covered by BTVA's `N<=13` finiteness theorem, and the support satisfies the required full-span condition for an unknown rational nonconic. Stoll--Testa's lower exceptional-incidence requirement is automatic because `M=28k>=8`.

Thus the currently retained packet constraints allow unbounded formal degree in the genus-zero full-span sector.

## F1-P5: formal genus-one hyperplane-span family

Take

```text
g=1,
d=28k.
```

Choose 14 nodes in the coordinate hyperplane `c=0`, distributed among the last three rank-3 blocks as

```text
[0,0,0,5,5,4].
```

A `6x6` Gaussian minor has determinant `16i`, so these nodes span that hyperplane, i.e. projective span dimension `5`.

The retained constraints are

```text
FSM:        28k <= 4(28k),
Beauville:  r_odd=28k=d and is even,
GFU:        -d+M = 0,
rank3:      block masses [0,0,0,10k,10k,8k] <= d,
Hodge:      56k^2 <= 98k^2+56k,
D^2:        -28k <= 21k^2,
conductor:  R8 <= (R-N)+48.
```

The BTVA `d<=16` bound applies only for support-span dimension `<=4`, so it does not touch this `s=5` family. Stoll--Testa's genus-one lower exceptional incidence is automatic.

## F1-P6: formal genus-one full-span family

Use the same 14-node full-span support as F0-P6, with

```text
g=1,
d=28k.
```

Then the span is `P^6`, rank-3 block masses are `[6k,6k,4k,4k,4k,4k]`, and the same genus-one Beauville/GFU/Hodge/conductor checks hold. Hence the `s=6` hard sector also admits unbounded formal packets.

## What this proves

Within the exact scope of the retained MB104 adapters, the present constraints do **not** force finiteness in any of the three hard sectors:

```text
g=0, span=P6;
g=1, span=5;
g=1, span=6.
```

The obstruction must therefore use information missing from the present packet. The highest-value next inputs are now:

- a global classification/effectivity theorem for one of these support configurations;
- an integral Picard/divisor-class realizability obstruction;
- a global incidence theorem saying the displayed 14-node support cannot be carried by an integral low-genus curve with the required branch multiplicities;
- another global invariant excluding the asymptotic packet shapes above.

This is exactly why the direct `R8<d/4` search is frozen: the retained inequalities permit `R8~d` formal families at equality boundaries, so continuing to recombine them is unlikely to close MB104 without new geometry.

## Verification and source locks

`verify_mb104_formal_infinite_family_feasibility.py` checks the explicit support minors, block counts, symbolic inequality reductions, credit firewalls, and exact Git blob identities of MB101, MB102, R8 route walls, Hodge, BTVA low-support/span, and Beauville inputs.

## Firewalls

- These are formal packets, not constructed curves.
- No Picard class or effectivity is asserted.
- No claim is made that arbitrary local landing germs globalize simultaneously.
- MB104 remains incomplete and MB105 remains unreleased.
- No receiver, theorem, endpoint, Perfect Cuboid, or merge credit.
