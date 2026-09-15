# Stage32 MB104 — `000707000f0f` e=2 gamma_Q orientation / numerical wall

Status: **RETAINED EXACT NEGATIVE ROUTING RESULT / EXPLICIT AMBIENT GENERATOR ALONE ADDS NO ALLOCATION EQUATION / CONDUCTOR COMPARISON STILL REQUIRED / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The preceding zero-quartic-union leaf fixes an explicit nonzero ambient generator

```text
[gamma_Q] in H_1(U,Z) ~= Z/2
```

and, through the two intersections `R_+,R_-`, fixes the relative residual-sheet orientation between the split components of `Q0` and `Q1`.

This note asks whether that orientation fact alone strengthens the retained branch-allocation equations. It does not.

## 1. The orientation reversal on the Q1 allocation block

The exact residual-node table uses seven Q1 variables

```text
x8,x9,x10,x11,x32,x33,x34,
```

where `x_j` counts the displayed simultaneous-sign residual representative among the `8l` branches over node `Pj`.

Reversing the displayed residual representative on the whole Q1 block acts by

```text
x_j' = 8l-x_j.                                  (FLIP)
```

For centered variables

```text
d_j=2x_j-8l,
```

this is exactly

```text
d_j'=-d_j.                                      (D-FLIP)
```

The new `gamma_Q` leaf chooses which of these two Q1 orientations is compatible with the fixed Q0 `+` component. The question is whether the retained numerical/congruence package distinguishes the two choices.

## 2. Q1 boundary saturation is invariant

The exact Q1 saturation equation is

```text
x8+x9+x10+x11+x32+x33+x34 = 28l.               (SAT)
```

Under `(FLIP)`, its left side becomes

```text
7*(8l)-28l = 28l.
```

Equivalently the centered equation

```text
d8+d9+d10+d11+d32+d33+d34=0
```

is sent to its negative and is unchanged as an equation.

## 3. Exact Picard parity and zero-quartic mod-4 constraints are invariant

The Picard64 descent requires every `x_j` to be even. Since `8l` is even, `(FLIP)` preserves this condition.

The retained Q1 mod-4 constraints may be written

```text
x8+x9+x10+x11 == 0 mod 4,
x32+x33+x34     == 0 mod 4.                    (MOD4)
```

After `(FLIP)` the two sums are respectively

```text
32l-(x8+x9+x10+x11),
24l-(x32+x33+x34).
```

Both constants are divisible by four. Hence `(MOD4)` is preserved exactly.

## 4. The A1 energy package is invariant

Every retained aggregate formula depends on the Q1 centered block through squares. In particular

```text
sum_j d_j^2,
y/2 = 84l^2 + (1/8) sum_j d_j^2,
delta_same = 84l^2+56l-(1/8)sum_j d_j^2
```

are unchanged by `(D-FLIP)`.

The Q0 equations are untouched by a Q1 block flip. Therefore the complete currently retained package

```text
Q0/Q1 saturation
+ all-even Picard64 parity
+ two zero-quartic mod-4 constraints
+ A1 square energy / same-sheet defect
```

is invariant under reversing the entire Q1 residual orientation.

An exact Wolfram replay gives

```text
SAT' = -SAT,
d_j'+d_j=0,
energy'-energy=0,
MOD4_first' + MOD4_first = 32l,
MOD4_last'  + MOD4_last  = 24l.
```

## 5. Routing consequence

The explicit generator `gamma_Q` is genuine new geometric information: it removes the ambiguity about what the nonzero ambient homology class is and fixes the relative `Q0/Q1` sheet orientation.

But **orientation fixing alone does not reduce the formal allocation solution set under the retained numerical/congruence constraints**. Those constraints cannot tell the two Q1 orientations apart.

Therefore the next load-bearing step cannot be

```text
materialize gamma_Q
 -> simply choose the global Q1 plus sign
 -> derive a new saturation/parity/energy equation.
```

A genuine advance must compare the actual carrier conductor loop with the ambient generator:

```text
lambda_(p;i,j) = 0 or gamma_Q in H_1(U,Z),
```

or supply an equivalent conductor descent / bounding-chain / square-root transition computation. Only that comparison couples `gamma_Q` to the branch-pair data.

## Firewalls

- The block flip is an algebraic symmetry of the retained constraint package; it is **not** claimed to be an automorphism sending one actual geometric carrier to another.
- No conductor loop is assigned to `0` or `gamma_Q`.
- No branch allocation is claimed geometrically realizable.
- No weighted-cut upper bound is proved.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
