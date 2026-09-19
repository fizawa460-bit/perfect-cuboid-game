# MB104 P6D2 — automatic odd-contact equality upgrade — 2026-09-19

Status: **PRE-AUDIT EXACT NECESSARY GEOMETRY / NO CREDIT**

## Purpose

The preceding P6D note was deliberately conditional on an equality-shaped packet. On the hostile full-span ray, part of that equality is in fact forced by the class and the already-retained Beauville/FSM inequalities.

Fix

```text
Sigma = 0000093f442e
|Sigma| = 14,
P = 7H - 4 sum_(i in Sigma) E_i,
C in |D_l|, D_l=lP, l>=1,
g(normalization(C))=1.
```

The class gives

```text
d = H.C = 112l,
M_i = E_i.C = 8l  (i in Sigma),
M = sum_i M_i = 112l = d.
```

## 1. R8 is nonzero

The retained branchwise Freitag--Salvati Manni inequality is

```text
d <= 16g-16 + 4 R8.
```

For g=1 this becomes `d<=4R8`. Since `d=112l>0`,

```text
R8 >= 28l > 0.
```

Hence the restricted Beauville double cover is branched and connected, so the retained Beauville odd-contact inequality applies.

## 2. Odd-contact equality is automatic

For genus one the retained Beauville wall gives

```text
r_odd >= d.
```

Always

```text
R8 <= r_odd <= R <= M.
```

On the present ray `M=d`. Therefore every inequality is forced to equality from `r_odd` onward:

```text
r_odd = R = M = d = 112l.
```

Since `M` is the sum of positive exceptional contacts `m_b` over the `R` normalization branches, `R=M` forces

```text
m_b=1
```

for every branch over every supported box node. In particular

```text
r_i=M_i=8l
```

at each of the fourteen supported nodes.

Important firewall: `m_b=1` does **not** imply `(A,B)=(1,1)`. Therefore this upgrade does not claim `R8=d`; the retained information is only `28l<=R8<=112l`.

## 3. Product-cover equality and full deck are therefore automatic

The archived Beauville equality-rigidity argument uses `g=1` and `r_odd=d`, not the stronger assertion `R8=d`. Thus any actual genus-one carrier on this hostile ray has a connected Beauville pullback `Y` with

```text
g(Y)=56l+1,
```

and every connected component of the pullback to `C8 x C8` has two etale projections to `C8`.

The present support has the three singular-stabilizer type counts

```text
(b1=0,b2=0,b3=0) = (6,2,6).
```

All three outside involutions occur, and every supported branch is odd. The archived full-deck stabilizer argument therefore applies without an extra equality-packet hypothesis and forces

```text
e=4,
Z connected,
g(Z)=224l+1,
deg(Z -> C8)=56l on each factor,
Z/G = E
```

for the genus-one normalization `E`.

## 4. Six-value passport becomes necessary, not merely conditional

For either factor quotient `C8/G ~= P1`, the induced map

```text
phi:E -> P1
deg(phi)=56l
```

has six order-two branch values. The `112l` odd/simple exceptional branches exhaust the unramified capacity over those six values.

Because the support type counts are `(6,2,6)` and each supported node contributes exactly `8l` branches, the pair totals are forced:

```text
type pair      sum u_q      sum r_q
b1=0            48l          32l
b2=0            16l          48l
b3=0            48l          32l
```

with `u_q+2r_q=56l` at each of the six values.

The old U12 full-fiber saturation still does not follow: even the largest node-type total is `48l<56l`.

## 5. What this changes

P6D should no longer be read as saying that the full-deck/six-value geometry requires the extra hypothesis `R8=r_odd=M=d` with all `(A,B)=(1,1)`. On this exact hostile ray, the class plus retained inequalities already force the needed `r_odd=M=d` and `m=1` package.

What remains unproved is the diagonal A1 type `(A,B)=(1,1)` for every branch, and no carrier is constructed.

## Source locks

Historical MB104 archive exact head:

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- `R8-BOUND-ROUTE-LEDGER.md` blob `548cbf714900cbab3b775ce2bfa2a362b7107960`;
- `BEAUVILLE-ODD-BRANCH-COVER-WALL.md` blob `1afa8398a337b58256fa05af8f3013688d7d7cae`;
- `GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY.md` blob `a20547082b1ea2f786b1272d1b76af3527508e9b`;
- `GENUS1-P5-FULL-DECK-STABILIZER-RIGIDITY.md` blob `cb05a7a187c9dd7495ee1f4af3b92fb776900422`.

Current compact source:

- `MB104-P6D-FULL-DECK-EQUALITY-PASSPORT-20260919.md` blob `efd3334a22603a971d72ab2d858be4e5d25f4b99`.

## Firewalls

```text
finite_degree_window_proved=false
MB104_complete=false
R29_LG2_MB_discharged=false
receiver_credit=false
effectivity_final_milestone_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
