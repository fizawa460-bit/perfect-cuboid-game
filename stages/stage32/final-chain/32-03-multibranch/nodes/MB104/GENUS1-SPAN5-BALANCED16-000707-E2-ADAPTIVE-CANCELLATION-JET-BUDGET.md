# Stage32 MB104 — `000707000f0f` e=2 adaptive cancellation jet budget

Status: **RETAINED EXACT LOCAL JET-TARGET DIMENSION / GLOBAL RAW-RANK OBSTRUCTION REDUCED TO HIGH-ENERGY SHELL / e=2 OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

For even `l=2m`, the preceding allocation-sensitive wall writes the invariant and anti-invariant eigensections after their common supported-exceptional vanishing as sections of

```text
A_mu=7mH-sum_j mu_jE_j,
B_mu=7mH-L_abs-sum_j mu_jE_j,

mu_j=4m-|b_j|,
q_j=2|b_j|.
```

At node `j`, one of the two combinations `s_+ +/- s_-` must vanish an additional `q_j` normal orders along the supported exceptional `E_j`. This note computes the exact local jet-target size and the strongest conclusion available from dimension counting alone.

## 1. The half-line is formally trivial along a supported exceptional

Fix one supported exceptional

```text
E=E_j ~= P1,
E^2=-2.
```

The residual double cover is branched only on the absent-type exceptionals, so

```text
L_abs.E=0.
```

Hence

```text
L_abs|_E ~= O_E.
```

Let `I=O_S(-E)`. Since

```text
I^k/I^(k+1) ~= O_E(-kE) ~= O_P1(2k),
```

we have

```text
H^1(E,I^k/I^(k+1))=0
```

for every `k>=0`. Inducting through the exact unit sequences on successive infinitesimal neighborhoods shows that a trivialization of `L_abs|_E` extends to every finite thickening `qE`.

The extension is not claimed canonical; existence is enough. Therefore, for any fixed finite `q`, the invariant and anti-invariant eigensections can be compared as sections of the same line bundle on `qE`. Changing the trivialization by a unit does not change vanishing order or the target dimension below.

## 2. Exact target dimension for an extra cancellation of order q

After removing the common multiplicity `mu=mu_j`, put

```text
N=7mH-mu E
```

near `E`; other supported exceptionals are disjoint and do not affect the local calculation. Since `H.E=0`,

```text
N.E=2mu.
```

Requiring one chosen combination `s_+ +/- s_-` to vanish an additional `q` orders along `E` is exactly the vanishing of its image in

```text
H^0(qE, N|_(qE)).
```

The quotient has the standard filtration with layers

```text
(N-kE)|_E,  k=0,...,q-1.
```

Each layer has degree

```text
(N-kE).E=2mu+2k >=0,
```

so its `H^1` vanishes and its `H^0` dimension is

```text
2mu+2k+1.
```

Therefore the exact local jet-target dimension is

```text
dim J(mu,q)
 =sum_(k=0)^(q-1)(2mu+2k+1)
 =q(2mu+q).                                    (JET-DIM)
```

For the active allocation

```text
mu=4m-|b|,
q=2|b|,
```

this collapses to

```text
dim J_j = 16m |b_j|.                          (LOCAL-16)
```

The cancellation depth grows with imbalance, so this is outside the standalone fixed-finite-jet wall.

## 3. Simultaneous target on the fourteen disjoint exceptionals

The fourteen supported exceptionals are pairwise disjoint. Put

```text
R1=sum_j |b_j|,
Q=sum_j b_j^2.
```

For a fixed sign choice determined by the allocation, the simultaneous cancellation map has target

```text
J_b = direct_sum_j J_j,

dim J_b = 16m R1.                             (TARGET)
```

No independence or surjectivity of the global evaluation map is assumed; `(TARGET)` is only the exact dimension of the full local target.

## 4. Riemann--Roch source dimension and cancellation of the L1 term

The preceding effectivity wall gives

```text
h0(A_mu)+h0(B_mu)
 >= chi(A_mu)+chi(B_mu)
 =784m^2-112m+12-2 sum_j mu_j^2.
```

Using

```text
sum_j mu_j^2
 =sum_j(4m-|b_j|)^2
 =224m^2-8mR1+Q,
```

we obtain

```text
source_dim
 >=336m^2-112m+12+16mR1-2Q.                  (SOURCE)
```

Subtracting the exact target dimension `(TARGET)` makes the entire `L1` term cancel:

```text
source_dim-dim J_b
 >=336m^2-112m+12-2Q.                          (SLACK)
```

Thus whenever

```text
Q <= 168m^2-56m+5,                            (UNDER)
```

the source dimension is strictly larger than the full local target dimension. For **every** linear simultaneous jet-evaluation map with that target, its kernel is then nonzero.

This is not a construction of the required carrier: a kernel pair can still be degenerate, can vanish deeper than prescribed, and the open nonvanishing/exact-order conditions are not encoded by the homogeneous rank count. It does prove that a raw dimension/rank argument cannot show injectivity in the region `(UNDER)`.

## 5. Only a thin high-energy shell can be attacked by raw jet rank

The retained energy identity for `l=2m` is

```text
delta_same
 =336m^2+112m-2Q.                              (SAME)
```

If a raw source-versus-target rank obstruction is even to be possible, `(SLACK)` must fail to be positive, so necessarily

```text
Q >= 168m^2-56m+6.
```

Equivalently,

```text
delta_same <= 224m-12.                        (THIN-SHELL)
```

Therefore plain adaptive jet rank can only possibly act in a shell where the same-sheet defect has already collapsed from quadratic size to a linear `O(m)` budget.

The retained nonnegativity bound only gives

```text
delta_same>=0,
```

so this shell is not empty by the current evidence. But the search target is now sharply localized:

```text
0 <= delta_same <= 224m-12.
```

Outside that shell, raw linear rank counting is structurally underdetermined before any detailed matrix is computed.

## Route consequence

The adaptive jet route splits into two regimes.

1. **Bulk regime** `Q<=168m^2-56m+5`: source dimension exceeds the complete local target; injective rank obstruction is impossible.
2. **High-energy shell** `Q>=168m^2-56m+6`: a global evaluation matrix could in principle be injective and remains worth computing, especially because this is equivalent to the linear same-sheet budget `(THIN-SHELL)`.

A useful next asset is therefore not a full arbitrary-allocation matrix. It is a source-locked evaluation model specialized to the thin shell, or an independent lower bound on `delta_same` exceeding `224m-12`, which would close the raw adaptive-jet rank route entirely.

## Firewalls

- Formal-neighborhood trivialization of `L_abs` is used only to compare finite normal jets near supported exceptionals; no global trivialization is asserted.
- `dim J_b` is target dimension, not proven global evaluation rank.
- Nonzero kernel of the homogeneous jet map does not prove existence of a matched geometric carrier or exact-order realization.
- No conductor pair is assigned a residual sheet.
- No weighted-cut upper bound is proved.
- The eigensection framework inherits the candidate status of the retained ambient-H1 linearization.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- Active leaf remains unchanged.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
