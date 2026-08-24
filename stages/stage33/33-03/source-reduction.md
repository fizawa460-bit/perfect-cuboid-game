# Stage33-03 — BR0B absolute-Galois UPic / Gersten execution reduction

```text
STAGE33_UNIT=33-03
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
PREREQUISITE_UNITS=[33-02]
PREREQUISITES_ALL_CLOSED=true
BR0A=DISCHARGED
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Frozen exact input

Stage33-02 hostile audit closed `R29-BR0A` and certified the exact physical-boundary compactification complex

```text
C_D = [ Div_D(S_Qbar) -> Pic(S_Qbar) ]
```

with `Div_D` in degree 0 and `Pic` in degree 1.  The exact integral data are

```text
rank Div_D             = 72
rank Pic(S_Qbar)       = 64
rank im(Div_D -> Pic)  = 58
rank U_D               = 14
Pic(U_Qbar)            ~= Z^6 + Z/2 + Z/2
```

where

```text
U_D = ker(Div_D -> Pic) = O(U_Qbar)^*/Qbar^*.
```

The source-locked Testa--Stoll model is defined over

```text
L = Q(i,sqrt(2)),
Gal(L/Q) ~= V4,
```

and contains exact matrices `ccPic`, `ctPic` and exact permutations `permcc`, `permct` on all known curves and exceptional components.  The Stage29 boundary selector is exactly

```text
boundary = C1s[1..24] + exceptional[1..48]
         = upstream indices 1..24,93..140.
```

## Why Stage33-03 is not merely finite V4 H^1

The audited Stage29 repair identifies

```text
Br_a(U) = Br_1(U)/im Br(Q) ~= H^2(Q,UPic(U_Qbar)).
```

Although the visible integral complex is split by `L`, the rank-14 unit lattice creates absolute-Galois character terms.  Therefore

```text
finite V4 hypercohomology alone != complete BR0B.
```

For odd primes, the free lattices and the quotient action factor through the 2-group `V4`; consequently the finite-quotient correction terms are 2-primary.  The odd-primary part is controlled by the absolute-Galois `H^2(Q,U_D)` character term.  Using

```text
0 -> U_D -> U_D tensor Q -> U_D tensor Q/Z -> 0
```

and vanishing of positive continuous cohomology for the rational lattice gives the standard conversion

```text
H^2(Q,U_D) ~= H^1(Q,U_D tensor Q/Z).
```

Thus an exact `V4` action on the integral unit lattice permits a complete parametric inventory of all odd-primary character families by the four quadratic characters of `V4`; no odd-primary survivor may be silently discarded.

## Current bounded sub-DAG

```text
03A  materialize exact cc/ct action on Div_D and Pic(S_Qbar)
 |
 v
03B  verify equivariance of the audited 72x64 differential
 |
 v
03C  induce exact integral cc/ct action on U_D=ker(d)
 |
 +----> compute V4 rational-character multiplicities of U_D
 |
 v
03D  induce exact action on Pic(U_Qbar)=coker(d), including its (Z/2)^2 torsion
 |
 v
03E  compute finite V4 hypercohomology / 2-primary correction data
 |
 v
03F  combine finite quotient with absolute character families
      -> complete all-primary BR0B inventory or exact smaller residual kernel
```

`03A--03C` are the immediate exact Class-2 leaf executed by this PR.  No claim about `Br_a(U)` is made until `03E--03F` are complete.

## Current leaf

```text
LEAF_ID=L33-03-UPIC-V4-INTEGRAL-ACTION
CLASS=2
NEW_THEOREM_REQUIRED=false
TARGETS=
  exact boundary cc/ct permutations;
  exact Picard cc/ct matrices;
  equivariance certificate;
  exact rank-14 unit-lattice cc/ct matrices;
  V4 character multiplicities over Q;
  exact Pic(Ubar) quotient-action adapter.
```

## Source locks

- `stages/stage33/33-02/audit-state.json`
- `stages/stage33/33-02/handoff.json`
- `stages/stage29/29-02f/boundary_module_probe.m`
- `stages/stage29/29-02f/open-algebraic-brauer-adapter.md`
- `MichaelStollBayreuth/Verification@51233ed5ef2bf228fac9416c66db9adc0ebcaadd`
- `Cuboids/cuboids.magma` blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`

```text
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
