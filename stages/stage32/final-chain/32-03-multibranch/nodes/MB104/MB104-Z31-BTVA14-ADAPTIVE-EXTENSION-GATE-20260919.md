# MB104 — Z31 / BTVA-14 adaptive extension gate

Status: **RESEARCH CHECKPOINT / PRE-AUDIT / NO CREDIT**

## Why this checkpoint exists

The revived-Z pass moved the explicit Miyaoka/Hodge finite window through node support
`N<=9`, leaving `N=10` as the first support size not controlled by that particular
composition. That is not, however, the sharp boundary for the existence of an
**unbounded family**.

Bruin--Thomas--Várilly-Alvarado (BTVA), *Explicit computation of symmetric
differentials and its application to quasi-hyperbolicity* (ANT 16 (2022),
arXiv:1912.08908), applies its local-Euler-characteristic estimate to the perfect-cuboid
surface, a complete intersection of four quadrics in `P^6` with 48 `A_1` points.
Their partial-information criterion implies that there are only finitely many
geometric-genus `0` or `1` curves meeting at most 13 of the 48 singularities.

Therefore, independently of whether an explicit numerical degree cap has been
materialized,

```
unbounded genus <=1 family  =>  N >= 14.                 (Z31-ENTRY)
```

This is an **abstract finiteness** statement. It does not provide an effective `Dmax`,
does not release Picard enumeration, and receives no Stage32 theorem/receiver credit in
this checkpoint.

## 1. Why 14 is the exact BTVA threshold

For an `A_1` point, BTVA Proposition 3.3 has leading local extension cost

```
chi0(A1, Sym^m Omega) = (11/108)m^3 + O(m^2).
```

For the perfect-cuboid complete intersection, the global Euler contribution has leading
coefficient

```
chi(Y, Sym^m Omega) = -(32/3)m^3 + O(m^2)
                    = -(1152/108)m^3 + O(m^2).
```

If a carrier meets `N` box nodes, it avoids `r=48-N` exceptional components.
Using those `r` components in the BTVA partial-information lower bound gives leading
coefficient

```
C_N = -32/3 + (48-N)*(11/108)
    = (144-11N)/108.
```

Hence

```
N <= 13  => C_N > 0,
N = 13   => C_N = 1/108,
N = 14   => C_N = -10/108 = -5/54.
```

So the ordinary BTVA asymptotic mechanism stops **exactly** at `N=14`.

This is structurally notable because the retained hostile balanced formal family
`000707` also has

```
N=14,
M=d=112l,
M_i=8l on its support,
```

and saturates the retained Hodge/Cauchy architecture. The first support size outside
the BTVA finite region is therefore also where the known equality-shaped obstruction
lives.

## 2. Compatibility with the revived-Z branch-density calculation

For genus one, combine the retained/pre-audit asymptotic ingredients

```
M/d <= sqrt(3N/28) + o(1),
R >= O >= d,
S1 >= 2R-M,
Delta_total <= d/2 + ((N-8)/(32N))d^2 + o(d^2),
Delta_exc >= T^2/(4N)-T/2.
```

Here `S1` is the number of contact-one branches and `T` is the number of
non-diagonal branches. The number `F` of diagonal FSM-minimal
`(A,B)=(1,1)` branches then has the asymptotic lower coefficient

```
F/d >= f(N)+o(1),

f(N)=2-sqrt(3N/28)-sqrt((N-8)/8).
```

Numerically,

```
f(10) = 0.464901660986...
f(11) = 0.302007267621...
f(12) = 0.158999799786...
f(13) = 0.029236896254...
f(14) = -0.090770275176...
```

Thus the current Z6+Z14+Z16+Z21 composition also loses a positive forced-minimal
density at the same `13/14` boundary.

This coincidence does **not** prove a new theorem by itself. It identifies `N=14` as
the natural first unbounded support gate rather than `N=10`.

## 3. Ordinary BTVA cannot be rescued at N=14 by choosing a clever finite order

The exact BTVA lower bound at `r=34` (equivalently `N=14`) was replayed
residue-class by residue-class in symmetric order `m`.

For every `m>=3` the ordinary BTVA lower bound remains negative. Thus the failure at
`N=14` is not merely an asymptotic artifact with a small exceptional useful order.
The supplied verifier records this exact sign check.

Therefore the active problem is not

```
find a lucky fixed m.
```

It must change the extension accounting itself.

## 4. Fixed finite local jet depth cannot change the cubic sign

The local `A_1` extension defect is cubic in `m`.

In the BTVA local model, imposing one additional divisibility/principal-part layer has
dimension cost

```
D1(m) =
  3m^2/4                         if m is even,
  (m-1)(3m+1)/4                  if m is odd.
```

Hence one layer is `O(m^2)`. Any fixed number `k=O(1)` of such layers can alter the
dimension count by only `O(m^2)), while the `N=14` deficit is

```
(5/54)m^3 + O(m^2).
```

More generally any `k(m)=o(m)` depth contributes only `o(m^3)` at this scale and
cannot reverse the leading sign.

This gives a quantitative version of the retained archive wall:

```
fixed finite landing values       -> insufficient,
fixed finite jet depth            -> insufficient,
fixed local principal-part rank   -> insufficient.
```

A BTVA-type repair at `N=14` must therefore have an **adaptive depth proportional
to m**, or an equivalent global mechanism that contributes cubic-order extension
credit.

## 5. Z31: weighted/adaptive BTVA branchwise extension route

The new route is deliberately narrower than a generic “try more symmetric
differentials” instruction.

At a met exceptional component `E_i`, ordinary BTVA pays the full cost required for
a reflexive symmetric differential to extend holomorphically across all of `E_i`.
For the Stage32 carrier problem, the section only needs enough regularity along the
actual normalization branches/landing jets of the carrier to force its pullback to
vanish or to constrain the carrier globally.

The 32-03 data provide exactly the extra structure ordinary BTVA ignores:

- the number of branches on `E_i`;
- their `(A,B,m)` types;
- their landing parameters `lambda`;
- their higher landing jets when retained;
- collision cost through `Delta_exc`;
- global constraints on `R`, `O`, `M`, and `Delta_total`.

The proposed Z31 gate asks whether this branchwise information can save enough of the
full-extension codimension to recover more than

```
5/54 * m^3
```

at `N=14`.

### Legal success shapes

Any one of the following is useful:

1. construct a carrier-adapted subspace of global reflexive symmetric differentials
   whose branchwise regularity conditions have cubic saving `>5/54*m^3+O(m^2)`;
2. prove that the required local depth can be taken
   `k(m)>=c*m` on enough met exceptional components, from global branch/landing data;
3. turn repeated high-order landing agreement into a global conductor/intersection
   charge whose cubic dimension effect replaces the missing extension credit;
4. prove that every `N=14` unbounded sequence enters a stricter algebraic sublocus
   (for example a finite union of foliated/resultant carriers), reducing the problem
   without an explicit degree cap;
5. prove that no branchwise/adaptive BTVA refinement can obtain cubic credit from the
   retained MB data, and route away with an exact obstruction rather than another
   finite-jet experiment.

### Forbidden replays

Do not spend another cycle on:

- a finite forbidden set of `lambda`;
- any fixed jet order;
- one fixed local principal-part matrix;
- ordinary BTVA with `r=34` and another fixed `m`;
- an assumption that distinct landing values automatically give full holomorphic
  extension across `E_i`;
- a formal replacement of 34 by a nonintegral “effective number of nodes” without a
  proved extension-codimension statement.

## 6. Relation to newer A_n extension work

Recent work on quotient singularities gives precise extension criteria for symmetric
differentials across `A_n` exceptional loci. It supports the scale fact relevant
here: the pole/vanishing order needed for full extension grows linearly with symmetric
order `m`.

This is useful as a consistency check for Z31's adaptive-depth requirement, but it does
not supply the missing **carrier-adapted global dimension theorem**. No credit is taken
from it here.

## Decision

```
BTVA_ABSTRACT_FINITE_SUPPORT_RANGE = N<=13
UNBOUNDED_SUPPORT_LOWER_BOUND = N>=14
EXPLICIT_DMAX_FOR_N10_TO_N13 = NOT_SUPPLIED_BY_BTVA
N14_ORDINARY_BTVA_CUBIC_COEFFICIENT = -5/54
ORDINARY_BTVA_FIXED_ORDER_RESCUE_N14 = NO_FOR_ALL_M>=3
FIXED_FINITE_JET_DEPTH_CAN_CHANGE_CUBIC_SIGN = NO
ADAPTIVE_DEPTH_SCALE_REQUIRED_FOR_BTVA_REPAIR = OMEGA(m)
NEW_ROUTE = Z31_WEIGHTED_ADAPTIVE_BTVA_BRANCHWISE_EXTENSION
BALANCED_000707_SITS_AT_FIRST_UNCONTROLLED_SUPPORT = YES
MB104_FINITE_WINDOW_PROVED = false
R29_LG2_MB_DISCHARGED = false
RECEIVER_CREDIT = false
THEOREM_CREDIT = false
ENDPOINT_CREDIT = false
MERGE_AUTHORIZED = false
```
