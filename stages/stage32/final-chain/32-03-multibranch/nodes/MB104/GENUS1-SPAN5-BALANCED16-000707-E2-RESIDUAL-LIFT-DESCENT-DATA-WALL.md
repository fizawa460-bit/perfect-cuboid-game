# Stage32 MB104 — `000707000f0f` e=2 residual-lift descent-data wall

Status: **RETAINED EXACT INFORMATION WALL / RESIDUAL-LIFT TRANSITION DATA MISSING / e=2 OPEN / NO CREDIT**

## Scope

The active MB104 leaf is

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP
```

for the dangerous equality packet on `000707000f0f`. The retained ambient Kummer chain gives a fixed character

```text
alpha_abs : pi_1(U) -> Z/2,  U=S\B_abs,
```

and, in the `e=2` case, the exact weighted conductor identity

```text
y/2 = sum_p sum_(i<j) I_p(beta_i,beta_j) * alpha_abs(lambda_(p;i,j)).
```

The Hodge obstruction requires this weighted sum to be at least `84*l^2`.

## Exact information boundary

The retained data determine the double-cover square class and its split pullback to the normalization in the `e=2` case, but they do **not** yet materialize the relative transition datum at conductor-identified normalization preimages.

Equivalently, the current retained boundary does not provide any one of the following source-locked objects:

1. an explicit lift/morphism from the normalization to `R=C8/H` with conductor-preimage coordinates;
2. a source-locked choice/evaluation of `sqrt(h o phi)` at the relevant conductor preimages, including the relative signs needed after conductor identification;
3. an equivalent descent/transition cocycle, commensurator action, or fibre-transport computation evaluating `alpha_abs(lambda_(p;i,j))`.

The existence of a square root on the normalization when `eta=0` is not enough: changing the global split section flips all labels simultaneously, while the load-bearing quantity is the **relative** transition between two normalization preimages identified by the conductor.

The retained local A1/product-lift information also does not supply this residual `G/H` bit. It gives an unordered local lift pair; it does not identify which member is carried to which residual sheet under the conductor gluing.

## Consequence

No new upper bound for

```text
sum_p sum_(i<j) I_p(beta_i,beta_j) * alpha_abs(lambda_(p;i,j))
```

is justified from the retained boundary alone. In particular, this wall does **not** assert that identity gluing or deck-twisted gluing occurs geometrically; it records only that the current retained invariants do not determine the transition.

Therefore `e=2` remains open. The correct next input is explicit residual-lift descent data of one of the three equivalent forms above, after which the fixed character can be evaluated and compared with the retained `84*l^2` threshold.

## Firewalls

- no conductor sign is assigned;
- no weighted-cut upper bound is claimed;
- no actual carrier existence is claimed;
- `e=2`, `e=4`, and `000707000f0f` remain open;
- MB104/span5/finite-window/receiver/theorem/endpoint/Perfect-Cuboid credit remains zero;
- no heavy compute is armed;
- no merge authorization.
