# Stage32 MB104 — BTVA symmetric-power vanishing-budget wall

Status: **RETAINED NEGATIVE ROUTE / MB104 INCOMPLETE / NO CREDIT**

## Question

The degree-two BTVA form `omega_7` vanishes along one hyperplane and Corollary 3.4 uses exactly that hyperplane vanishing to make the pullback regular across an `A1` exceptional curve. Could one take high symmetric powers and distribute the larger zero divisor among many hyperplanes, thereby regularizing a low-genus curve at arbitrary node support and forcing a global foliation constraint?

For the pure-power architecture, no. The local regularization cost scales at exactly the same rate as the available hyperplane-vanishing budget.

## Source-locked BTVA inputs

For an `A1` point `s`, BTVA Corollary 3.4 states that a symmetric differential of order `m` with twist

```text
-floor(m/2) H
```

for a hyperplane `H` through `s` extends regularly across the exceptional component over `s`.

On the perfect cuboid surface they explicitly find a degree-two reflexive symmetric differential `omega_7` with

```text
omega_7 in H^0(X, SymHat^2 Omega_X^1(-H_0))
```

for a hyperplane `H_0`; by linear equivalence they move this vanishing hyperplane in the proof of Corollary 6.5 / Theorem 1.2.

Thus the `k`-th symmetric power has order

```text
m=2k
```

and total movable hyperplane vanishing budget

```text
k H_0.
```

## Exact budget obstruction

Suppose one replaces `kH_0` by a linearly equivalent effective divisor

```text
D_H = sum_l a_l H_l,
```

where the `H_l` are hyperplanes, `a_l` are nonnegative integers, and

```text
sum_l a_l = k.
```

At a node `s`, Corollary 3.4's sufficient regularization condition for order `m=2k` requires vanishing multiplicity at least

```text
floor(m/2)=k
```

along a hyperplane through `s`. In the split divisor architecture, the total available vanishing through `s` is at most

```text
v_s = sum_{l:s in H_l} a_l <= k.
```

To meet the same `k`-unit local cost one must have

```text
v_s = k.
```

Because the entire global budget is also `k`, equality means **every positive-multiplicity hyperplane in `D_H` contains s**.

If the same construction is to regularize at every node in the support of a curve, every hyperplane occurring in `D_H` must therefore contain every supported node. Consequently the node support must already lie in a common hyperplane.

So taking powers does not allow the BTVA hyperplane-regularization budget to be spread among different node subsets.

## Ratio formulation

The obstruction is the exact ratio

```text
available hyperplane vanishing / symmetric order = k/(2k) = 1/2,
required A1 regularization vanishing / symmetric order = floor(2k/2)/(2k) = 1/2.
```

There is zero asymptotic slack.

A genuinely stronger symmetric-differential route would need at least one of:

- a section whose movable node/hyperplane vanishing grows faster than `m/2`;
- a section intrinsically regular at a large prescribed subset of exceptional components, lowering the local cost there;
- a different local cancellation mechanism not paid from the same hyperplane-zero budget.

Simply taking powers or products of copies of the same `omega_7` architecture cannot do it.

## Relation to the retained BTVA partial finiteness result

This explains why the published low-genus argument naturally depends on the linear span of the **distinct node support**. When the support lies in a hyperplane, the full regularization cost is paid by that one hyperplane. When it spans the ambient `P^6`, pure symmetric-power amplification does not provide a way around the span barrier.

This wall does not rule out other independent symmetric differentials with different exceptional valuations or stronger vanishing. Those remain legitimate new-theorem targets.

## Firewalls

No new `R8` upper bound is claimed. MB104 remains incomplete; finite Picard enumeration is not released. No receiver, effectivity, final-milestone, theorem, endpoint, Perfect Cuboid, or merge credit is granted.
