# Stage32 32-02 — conditional Riemann–Roch effectivity sufficient lemma

This is a **pointwise sufficient classifier**, not a FULL178 census and not an irreducibility theorem.

## Assumptions

For the smooth projective desingularized surface `S`, assume:

- `K_S^2 = 16`;
- `chi(O_S) = 8`;
- `K_S` is nef;
- Serre duality and surface Riemann–Roch apply to the integral divisor class `C`.

This checkpoint does **not** newly prove or source-lock those surface invariants. Until a retained source for them is attached, the classifier is conditional and receives preparation credit only.

Write

- `d = K_S . C`;
- `C2 = C . C`.

For an integral divisor class, Riemann–Roch gives

`chi(O_S(C)) = 8 + (C2 - d)/2`,

so `(C2-d)` must be even.

## Sufficient criterion

If

1. `d > 16`, and
2. `C2 >= d - 14`,

then `C` contains an effective divisor.

Indeed,

`K_S . (K_S-C) = 16-d < 0`.

Since `K_S` is nef, an effective divisor `K_S-C` would have nonnegative intersection with `K_S`; therefore `K_S-C` is not effective. By Serre duality,

`h^2(O_S(C)) = h^0(O_S(K_S-C)) = 0`.

The second inequality gives

`chi(O_S(C)) = 8 + (C2-d)/2 >= 1`.

As `h^1 >= 0`,

`h^0(O_S(C)) = chi(O_S(C)) + h^1(O_S(C)) >= 1`.

Thus the linear system of `C` is nonempty.

## Exact boundary

The classifier returns `RR_INCONCLUSIVE` rather than a negative statement whenever:

- `d <= 16`;
- `C2 < d-14`;
- required assumptions are not affirmed.

Odd `(C2-d)` is treated as an invalid/incompatible integral-class input, not as non-effectivity.

## Regression

For the retained historical target label `g1-d186`, the proposed regression pair `d=186`, `C2=858` gives

`chi(O(C)) = 8 + (858-186)/2 = 344`,

hence `RR_EFFECTIVE_DIVISOR_CERTIFIED` under the assumptions above.

At `d=186`, the exact sufficient threshold is `C2=172`, where `chi=1`; `C2=170` gives `chi=0` and is deliberately inconclusive.

## Credit ceiling

An effective divisor is not automatically an integral irreducible representative and does not automatically have the required genus. This lemma therefore grants none of:

- low-genus carrier credit;
- receiver credit;
- FULL178 pruning/completion credit;
- theorem or endpoint credit;
- Stage32 closure;
- perfect-cuboid existence/nonexistence credit.

The point of this leaf is to provide a cheap, exact, fail-closed effectivity filter that can be applied when the current FULL178 survivor/Picard ledger is eventually source-locked.
