# Stage32 MB104 — aggregate 28-fibration Riemann--Hurwitz capacity wall

Status: **RETAINED NEGATIVE ROUTE / MB104 INCOMPLETE / NO CREDIT**

## Purpose

The previous local-jet wall showed that the minimal cusp packet `(A,B)=(1,1)` does not by itself force ramification for even one incident genus-5 fibration. This note asks a stronger optimistic question: suppose a future global jet theorem were maximally favorable and forced **every** minimal cusp branch to contribute at least one ramification unit to **all 28** genus-5 fibrations. Could the summed Riemann--Hurwitz budget then be strong enough to close MB104?

The answer is no. Even this unrealistically favorable unit-charging hypothesis gives an asymptotic `R8` slope `1`, whereas MB104 requires a slope strictly below `1/4`.

## Fibration-degree budget

Let `D` be a nonexceptional integral carrier of normalization genus `g<=1`, with canonical degree

```text
d = H.D.
```

Stoll--Testa Section 5 gives 28 genus-5 fibrations:

- 22 fibrations arising in 11 complementary pairs from rank-4 quadrics; for each pair the sum of the two fiber classes is `H`;
- 6 fibrations from the six rank-3 quadrics; for each such fiber class `F_Q`,

```text
2F_Q = H - sum_{i in B_Q} E_i.
```

For any rank-4 complementary pair `(F,F')`, if the restrictions to the normalization of `D` are nonconstant, their map degrees satisfy

```text
n_F+n_F' = D.(F+F') = d.
```

Therefore the 22 rank-4 maps contribute total degree at most `11d`.

For a rank-3 class,

```text
2 n_Q = 2D.F_Q = d - sum_{i in B_Q} D.E_i <= d,
```

because every exceptional intersection is nonnegative for a nonexceptional integral curve. Thus the six rank-3 maps contribute total degree at most `3d`.

Hence, under the optimistic assumption that all 28 restrictions are nonconstant,

```text
sum_{j=1}^{28} n_j <= 14d.                    (RH-DEGREE-BUDGET)
```

If some fibration restriction is constant, it supplies no nonconstant-map Riemann--Hurwitz budget and cannot improve the simple summed-charging route considered here.

## Total ramification capacity

For a nonconstant morphism from the normalization `Cbar` of genus `g` to `P^1` of degree `n_j`, Riemann--Hurwitz gives total ramification multiplicity

```text
B_j = 2g - 2 + 2 n_j.
```

Summing the 28 maps and using `RH-DEGREE-BUDGET`,

```text
B_total = sum_j B_j
        <= 28(2g-2) + 28d.
```

Now impose the deliberately over-optimistic charging hypothesis

```text
every one of the R8 minimal cusp branches contributes >=1 ramification unit
in every one of the 28 fibrations.
```

Then

```text
28 R8 <= B_total <= 28d + 56(g-1),
```

so at best

```text
R8 <= d + 2g - 2.                             (MAXIMAL-UNIT-CHARGE)
```

For the two relevant genera this is

```text
g=0: R8 <= d-2,
g=1: R8 <= d.
```

The coefficient of `d` is still `1`, four times too large even to reach the threshold `1/4`, and MB104 needs it **strictly below** `1/4`.

## Required aggregate charge

More generally, suppose a future theorem guaranteed aggregate ramification multiplicity at least `q` across the 28 fibrations for every minimal cusp branch. Then

```text
q R8 <= 28d + 56(g-1),
R8 <= (28/q)d + 56(g-1)/q.
```

To obtain the MB104-required asymptotic slope `<1/4`, one would need

```text
q > 112.
```

Thus a mere `one unit per branch per fibration` theorem has aggregate charge `q<=28` and is structurally incapable of closing MB104. One would need average forced ramification multiplicity greater than four per fibration per minimal branch, or a different global inequality whose degree budget is substantially smaller.

The retained local-jet wall is stronger still in the opposite direction: current local data do not force even one unit of ramification for one incident fibration.

## Consequence

The live route

```text
"multi-fibration global tangent/jet constraint forcing criticality"
```

must now be interpreted narrowly. Simple unavoidable-criticality or unit-ramification charging is dominated even under the impossible best case that all 28 fibrations charge every branch. A viable multi-fibration theorem would need **high ramification order**, a much cheaper global degree budget, or an additional cancellation mechanism.

This does not prove that every conceivable fibration-based argument is impossible. It closes only the standard summed Riemann--Hurwitz unit-charging architecture.

## Firewalls

No `R8` bound with slope `<1/4` is proved. MB104 remains incomplete. No finite Picard enumeration, receiver, effectivity, final-milestone, theorem, endpoint, Perfect Cuboid, or merge credit is released.
