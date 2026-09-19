# MB104 P6P — elliptic two-pencil Wronskian rigidity preflight wall — 2026-09-19

Status: **PRE-AUDIT EXACT INPUT-STRENGTH WALL / NO CREDIT**

## Input

P6H/P6K leave two degree-`56l` maps

```text
psi_1,psi_2:E -> P1
```

on the same elliptic normalization with

```text
M_1 ~= M_2 =: M,
deg M = 56l,
```

and, for the three inertia types,

```text
O_E(R_(1,j)) ~= O_E(R_(2,j)).
```

The actual ramification divisors are not proved equal.

## Wronskian level

For a base-point-free pencil `V subset H^0(E,M)`, the Wronskian is a section of

```text
M^2 tensor K_E.
```

Since `E` is elliptic, `K_E ~= O_E`, so every degree-`56l` pencil in `M` has full ramification divisor in the same complete linear system

```text
Ram(V) in |M^2|.
```

Thus equality of the line bundle `M` already makes the **class** of the full ramification divisor identical for every pencil. This carries no rigidity toward equality of pencils.

A Wronskian reconstruction/finite-fibre statement would require the actual Wronskian section or actual ramification divisor, not merely its line-bundle class.

## Typewise retained data

P6H gives more than the full class: three partial ramification divisor classes match between the two pencils. But these are still points of Picard varieties, not actual divisors or Wronskian sections.

No retained adapter upgrades

```text
O_E(R_(1,j)) ~= O_E(R_(2,j))
```

to

```text
R_(1,j)=R_(2,j)
```

pointwise. P6K explicitly shows that its square-class reformulation reproduces only the same line-bundle equalities.

Therefore the hypotheses needed for a Wronskian-rigidity attack are absent.

## Disposition

```text
same pencil line bundle M                = exact,
same full ramification divisor class     = automatic,
same typewise ramification classes       = exact,
same actual Wronskian divisor            = not proved,
finite/automorphism-related pencil pair  = not derived.
```

P6P is parked. No Brill--Noether/Wronski-map classification is launched.

## Next shallow invariant

The remaining exact structure is not linear-series class data but the fact that both maps reconstruct the **same labelled full-G cover** `Z->E`. The next gate is

```text
MB104-P6Q-TWO-PENCIL-NIELSEN-COUPLING-PREFLIGHT.
```

Target: determine whether the two six-branch monodromy systems can be coupled through the same `G`-extension strongly enough to produce a finite simultaneous Nielsen class beyond P6G. Stop if the common-cover condition reduces only to the already-retained character square classes.

## Firewalls

```text
actual_wronskian_divisors_equal=false
pencils_equal=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
