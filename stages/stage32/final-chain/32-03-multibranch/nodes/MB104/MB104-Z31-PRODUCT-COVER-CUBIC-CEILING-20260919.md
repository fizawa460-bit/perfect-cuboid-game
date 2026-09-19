# MB104 — Z31 product-cover cubic ceiling

Status: **RESEARCH CHECKPOINT / PRE-AUDIT / NO CREDIT**

## Purpose

The preceding Z31/BTVA-14 gate isolates an exact cubic deficit at the first
BTVA-uncontrolled support size:

```
N=14:
ordinary BTVA cubic coefficient = -5/54.
```

One possible escape was that the BTVA lower bound discards a global cohomology term
and therefore might underestimate the actual cubic growth of reflexive symmetric
differentials on the perfect-cuboid surface.

The fixed modular/product presentation rules out that escape at cubic order.

## 1. Fixed product presentation

Over the geometric/complex field, the cuboid surface has the quotient presentation

```
X_pc = (X(8) x X(8)) / G0,
G0 ~= (Z/2)^3,
|G0|=8,
genus(X(8))=5,
```

with the diagonal `G0` action.  This is the Testa--Stoll / Beauville modular
presentation already used by the Stage32 product-cover routes.

The nontrivial group elements act nontrivially on the genus-five curve, hence have
only finitely many fixed points.  The quotient is quasi-etale in codimension one; the
isolated fixed-point quotient singularities are the box-surface nodes.

For a finite quasi-etale quotient, reflexive symmetric differentials downstairs are
the invariant symmetric differentials upstairs.  Thus at the level relevant to the
cubic Hilbert coefficient,

```
H0(X_pc, (Sym^m Omega_Xpc)^^)
  = H0(X(8)xX(8), Sym^m Omega)^{G0}.
```

This equality is used here only geometrically over C; no Q/Q(i) arithmetic descent
credit is asserted.

## 2. Exact total product dimension before invariants

Let `C=X(8)`, with `g(C)=5`.  On `P=CxC`,

```
Omega_P = p1^* K_C direct_sum p2^* K_C,
Sym^m Omega_P
 = direct_sum_{i=0}^m p1^*K_C^i tensor p2^*K_C^(m-i).
```

Set

```
a_0=1,
a_1=5,
a_k=h0(C,K_C^k)=8k-4   for k>=2.
```

Therefore

```
h0(P,Sym^m Omega_P)=sum_{i=0}^m a_i a_{m-i}.
```

For every `m>=4`, direct summation gives

```
h0(P,Sym^m Omega_P)
 = (32/3)m^3 - 32m^2 + (208/3)m - 48.       (PC-PROD)
```

In particular the total cubic coefficient upstairs is exactly

```
32/3.
```

## 3. Taking G0 invariants fixes the cubic coefficient at 4/3

For any nonidentity finite-order automorphism `g` of the genus-five curve, equivariant
Riemann--Roch / holomorphic Lefschetz expresses the trace on
`H0(C,K_C^k)` by contributions from finitely many fixed points.  Hence, as `k`
varies,

```
Tr(g | H0(C,K_C^k)) = O(1)
```

(periodic in the finite-order eigenvalues, up to the finitely many low powers).

For the diagonal action on `CxC`,

```
Tr(g | H0(P,Sym^m Omega_P))
 = sum_{i=0}^m
   Tr(g|H0(K^i)) Tr(g|H0(K^(m-i)))
 = O(m)
```

for `g != 1`.

Burnside/character averaging therefore yields

```
dim H0(P,Sym^m Omega_P)^{G0}
 = (1/8) h0(P,Sym^m Omega_P) + O(m)
 = (4/3)m^3 - 4m^2 + O(m).                  (PC-INV)
```

Thus the cubic coefficient of the full reflexive symmetric-differential space on the
cuboid quotient is **exactly 4/3**.

There is no hidden positive cubic contribution from the global `H^1` term omitted in
the coarse BTVA inequality.

## 4. N=14 deficit survives even with the full reflexive space

BTVA Proposition 3.3 gives the full-extension codimension at one A1 node:

```
chi0(A1,Sym^m Omega)
 = (11/108)m^3 + O(m^2).
```

A curve meeting `N=14` nodes leaves only 34 exceptional components removable from
the ambient open surface.  If one asks for full holomorphic extension across all 14
met components, the cubic cost is

```
14*(11/108) = 77/54.
```

But the entire reflexive supply has coefficient

```
4/3 = 72/54.
```

The exact shortfall is therefore still

```
77/54 - 72/54 = 5/54.
```

So the N=14 wall is not an artifact of the BTVA proof discarding a cubic-sized global
cohomology contribution.

## 5. Consequence for Z31

This closes one attractive bypass:

```
GLOBAL_H1_CUBIC_SURPLUS_RESCUES_N14 = NO.
```

Any successful N=14 refinement must instead reduce the **extension cost at the met
nodes** or prove dependencies among those extension conditions.

The retained branchwise FSM inequality supplies an important carrier-side resource:

```
d <= 16g-16+4R8,
```

hence

```
g=1: R8 >= d/4,
g=0: R8 >= d/4+4,
```

where `R8` counts FSM-minimal `(A,B)=(1,1)` branches over the box nodes.

Thus every unbounded MB sequence already carries linearly many minimal branches.
The missing bridge is not their existence.  It is to convert their actual landing/jet
configuration into a **cubic-order saving in the 14-node extension codimension**.

This sharpens Z31 to:

> determine the codimension of the subspace of reflexive symmetric differentials whose
> pullback is regular/vanishing on the actual normalization branches, and compare it
> with the full `chi0` cost.  Any saving capable of closing N=14 must recover more
> than `(5/54)m^3+O(m^2)`.

The archived finite-jet wall remains binding.  A fixed finite amount of branch-jet
information can only change lower-order terms; the needed saving must be adaptive or
come from a global dependence among the full extension conditions.

## Decision

```
PRODUCT_COVER = X8xX8_DIAGONAL_G0_ORDER8
PRODUCT_TOTAL_SYM_DIFF_CUBIC = 32/3
QUOTIENT_REFLEXIVE_SYM_DIFF_CUBIC = 4/3
HIDDEN_GLOBAL_H1_POSITIVE_CUBIC_SURPLUS = NO
N14_FULL_EXTENSION_COST_CUBIC = 77/54
N14_CUBIC_SHORTFALL = 5/54
FSM_MINIMAL_BRANCH_RESOURCE = R8>=d/4+O(1)
NEXT_TARGET = DEPENDENCE_OR_CARRIER_ADAPTED_SAVING_IN_14_NODE_EXTENSION_CONDITIONS
MB104_COMPLETE = false
R29_LG2_MB_DISCHARGED = false
RECEIVER_CREDIT = false
THEOREM_CREDIT = false
ENDPOINT_CREDIT = false
MERGE_AUTHORIZED = false
```
