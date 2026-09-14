# Stage32 MAIN GRF-01 — family-level GLOBAL RESIDUAL FEASIBILITY design

Status: **DESIGN / SYMBOLIC SYNTHESIS ONLY — NO MAIN CREDIT — CONCRETE APPLICATION OWNED BY 178**.

This node studies the V24 residual only at family/stratum abstraction level. MAIN does not enumerate FULL178 rows or terminals, does not reopen bounded leaves, does not run incidence/transport or population replay, and does not produce an exact pruning subset. `stage32-01-178-mainbatch` owns concrete target extraction, subset identity, exact subset certificates, overlap accounting, and any eventual consumable pruning evidence.

## Locked mathematical inputs

The design composes already-retained exact interfaces without changing their authority:

- current audited MAIN boundary before GRF-01: `a89580f3fcf42152b47673d2cfec1935c72555c2`;
- corrected HPADJ necessary condition from `hpadj-07/CARRIER-REALIZATION-WALL.json`;
- Stage29 exact `H^perp` encoding `r=gcd(d,16)`, `m=16/r`, `n=d/r`, `v=mC-nH`;
- HPADJ/EX5 selected64 interface with inverse denominator `8`;
- exact retained Picard64/Hperp integral adapter and pairing-prefix HNF machinery;
- consumed CUT finite-ring work only as a **necessary-condition pattern**. No `g1-d008,e=8`-specific incidence/cap inequality is generalized to another family unless a source-locked semantic adapter explicitly proves that generalization.

## 1. Exact common coordinate system

Let `p in Pic(S) ~= Z^64` be retained primitive Picard coordinates, `s in Z^64` the selected64 pairing vector, `G` the retained Picard Gram matrix, and `h` the retained coordinate vector of `H=K_S`.

The selected64 interface gives an integer numerator matrix `Bsel` with

```text
Bsel*s = 8*p.
```

Hence selected64 completion is exact iff `Bsel*s == 0 (mod 8)` coordinatewise.

For even canonical degree `d`, put

```text
r = gcd(d,16),   m = 16/r,   n = d/r,
v = m*p - n*h.
```

Then `v` is integral and `H.v=0`. Because `m in {1,2,4,8}`, the selected64 denominator and the `H^perp` scaling align exactly:

```text
v = (Bsel*s)/(8/m) - n*h.
```

No new rational denominator is introduced. This is the bridge that permits selected64 congruences, parity information, and the `H^perp` quadratic form to be eliminated in one 2-adic system.

## 2. Exact norm ladder, not only an upper bound

Define the positive `H^perp` norm

```text
N = -v^T G v.
```

Using `H^2=16`, `H.C=d`, `md=16n`, and adjunction `C^2+d=2 p_a(C)-2`,

```text
N = 16*n^2 - m^2*C^2
  = 16*n^2 + m^2*(d+2) - 2*m^2*p_a(C).
```

For the genus window `g in {0,1}`, write `p_a(C)=g+k`, `k>=0`. Then every candidate lies on the exact arithmetic norm ladder

```text
N = B_g(d) - 2*m^2*k,
B_g(d) = 16*n^2 + m^2*(d+2-2*g).
```

Thus the Stage29 norm inequality can be strengthened computationally from an interval to one residue class:

```text
N == 16*n^2 + m^2*(d+2)   (mod 2*m^2).
```

For even `d` this simplifies to:

| degree class mod 16 | m | required norm class |
|---|---:|---|
| 2,6,10,14 | 8 | `N == 16 (mod 128)` |
| 4,12 | 4 | `N == 16 (mod 32)` |
| 8 | 2 | `N == 0 (mod 8)` |
| 0 | 1 | `N == 0 (mod 2)` |

In particular the `m=8` and `m=4` classes require `v2(N)=4` for nonzero `N`. This is an exact identity/re-encoding of Picard integrality plus adjunction, not new pruning credit by itself.

## 3. Corrected HPADJ complement inside the same region

For the retained exceptional group sums

```text
a = x103+x102+x101
b = x99+x97+x98
c = x95+x94+x93+x96,
```

an actual target carrier must satisfy the corrected general-type HPADJ complement

```text
8*a^2 + 8*b^2 + 6*c^2 <= 3*d^2 + 48*d + 96*(1-g).
```

This condition is imposed simultaneously with the selected64 image lattice and the norm ladder. Historical K3 adjunction is not used.

## 4. GLOBAL RESIDUAL FEASIBILITY REGION

A symbolic family `F` is represented by linear equalities/inequalities on known-curve pairings and aggregate parameters, without listing its members. Its necessary feasibility region is the set of integer solutions to:

```text
Bsel*s = 8*p
H.p = d
y140 = P*p
source-locked family linear constraints on y140 / s
known-curve nonnegativity where the family contract permits it
8*a^2+8*b^2+6*c^2 <= 3*d^2+48*d+96*(1-g)
v = m*p-n*h
H.v = 0
0 <= -v^T G v <= B_g(d)
-v^T G v == required_norm_residue (mod 2*m^2)
source-locked parity/HNF/CUT finite-ring necessary constraints, if semantically valid for F.
```

No terminal identity is part of the definition.

## 5. Symbolic elimination order

MAIN should construct reusable obstruction kernels, not enumerate families.

**A. Linear congruence projection.** Eliminate free selected64/Picard variables by exact HNF/SNF. A contradiction in the projected affine lattice is `LINEAR_CONGRUENCE_EMPTY`.

**B. 2-adic quadratic projection.** Work first modulo `2*m^2` (`128,32,8,2`). Keep selected64 mod-8 and parity constraints in the same local system. After the linear HNF parameterization `v=v0+Tz`, substitute into `-v^T G v`; if its finite-ring image misses the required norm residue, the symbolic family is empty (`QUADRATIC_RESIDUE_EMPTY`). This is a local image calculation on an affine lattice, not a bounded leaf census.

**C. Rational quadratic lower bound.** For exact linear constraints `A v=b(u)` and positive form `Q=-G|Hperp`, minimize over `Hperp tensor Q`. On an independent row set,

```text
rho(u) = b(u)^T * (A Q^-1 A^T)^-1 * b(u).
```

If `rho(u) > B_g(d)` identically over the symbolic family parameter region, every integral point is impossible (`RATIONAL_QUADRATIC_LOWER_BOUND_EMPTY`). This is a Schur-complement strengthening of coarse Cauchy walls; it is valid because the integral minimum is at least the rational minimum.

**D. Odd-prime CUT layer.** Reuse finite-ring column-image obstructions only after a source-locked semantic adapter supplies the relevant family equations. Keep odd primes separate from the 2-adic core unless CRT combination materially simplifies the symbolic system. `SAT` or `UNKNOWN` never grants pruning.

## 6. What MAIN may certify

MAIN may produce a source-locked **global obstruction identity/kernel** proving that a stated symbolic necessary-condition system has no integer point, or supplying an exact projected congruence/quadratic form for downstream use. It must not attach that kernel to a concrete FULL178 subset on this lane.

A future consumable result therefore has two layers:

```text
MAIN: exact symbolic obstruction kernel / theorem schema
178 : concrete target extraction + exact subset certificate + overlap/accounting proof
```

Only the second layer identifies which current V24 residual objects are removed. MAIN may consume such a 178 certificate later under the normal hostile-audit/promotion rules.

## 7. 178 handoff contract

178 receives:

1. the source locks and exact identities above;
2. the modulus schedule by `m` class;
3. the HNF/SNF projection recipe;
4. the modular quadratic residue criterion;
5. the rational Schur-complement emptiness criterion.

178, not MAIN, must choose actual row/stratum/family parameters, avoid leaves already under active 178 study, generate exact identity/subset certificates, and prove disjointness/overlap accounting against consumed authority.

## Firewalls

- no FULL178 row/terminal census here;
- no bounded leaf search;
- no incidence/transport execution;
- no population replay;
- no concrete subset materialization;
- no MAIN pruning/receiver/theorem/effectivity/endpoint credit;
- no change to V24 authority;
- no merge authorization;
- no Perfect Cuboid existence/nonexistence claim.

The immediate research target after this design is **symbolic kernel construction only**: derive projected congruence and quadratic forms that are independent of a concrete FULL178 subset, then hand those kernels to 178 for application.
