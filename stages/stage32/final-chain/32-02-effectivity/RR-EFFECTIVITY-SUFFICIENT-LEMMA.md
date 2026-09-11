# Stage32 32-02 — source-locked Riemann–Roch effectivity sufficient lemma

This is a **pointwise sufficient classifier**, not a FULL178 census and not an irreducibility theorem.

## Retained surface source lock

The surface data required by this lemma are retained downstream evidence, not new assumptions invented by this checkpoint.

`stages/stage29/29-02a/source-lock.md` has `SOURCE_AUDIT=PASS` and identifies the minimal desingularization of the cuboid surface with

- `K_S^2 = 16`;
- `p_g = 7`;
- `q = 0`;
- canonical divisor big and nef;
- exact Stage29 projective endpoint-model match to the Testa--Stoll cuboid surface.

Hence

`chi(O_S) = 1-q+p_g = 8`.

The retained historical Stage32 evidence

- `stages/stage32/32-21/post-21bl-riemann-roch-divisor-effectivity.json`, and
- `stages/stage32/residual-32-01-production/audit_stage32_post21bl_divisor_effectivity.py`

already uses these same surface invariants and explicitly identifies the Stage32 target degree with `K_S.C`. The exact local lock is recorded and replayed by `SURFACE-INVARIANT-SOURCE-LOCK.json` and `verify_surface_invariant_source_lock.py`.

The classifier still requires explicit invocation affirmation (`assumptions_affirmed=True` / `--assumptions-affirmed`) so a caller cannot bypass the source-lock verifier accidentally. In the retained verification path that affirmation occurs only after the source locks pass.

Write

- `d = K_S . C`;
- `C2 = C . C`.

For an integral divisor class, surface Riemann--Roch gives

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

The classifier returns `RR_INCONCLUSIVE` rather than a negative statement whenever

- `d <= 16`, or
- `C2 < d-14`.

Without explicit source/hypothesis affirmation it returns `RR_INCONCLUSIVE_ASSUMPTIONS_NOT_AFFIRMED` fail-closed. Odd `(C2-d)` is treated as an invalid/incompatible integral-class input, not as non-effectivity.

## FULL178 degree gate

The retained FULL178 manifest is independently source-locked by `FULL178-RR-DEGREE-GATE.json`:

- 168 of the 178 rows have `d>16`;
- exactly 10 rows have `d<=16`.

This is only a degree partition. It does not state that those rows survive the numerical census and does not provide `C2` values for final survivors.

## Regression

For the retained historical target label `g1-d186`, `d=186`, `C2=858` gives

`chi(O(C)) = 8 + (858-186)/2 = 344`,

hence `RR_EFFECTIVE_DIVISOR_CERTIFIED`. This is consistent with the retained historical RR certificate whose canonical SHA256 is `6e02dfa2f29ebdd218aa869e1994776abc6bd068be9f138e1dd1980789e2483b`.

At `d=186`, the exact sufficient threshold is `C2=172`, where `chi=1`; `C2=170` gives `chi=0` and is deliberately inconclusive.

## Credit ceiling

An effective divisor is not automatically an integral irreducible representative and does not automatically have the required normalization genus. This lemma therefore grants none of

- low-genus carrier credit;
- receiver credit;
- FULL178 pruning/completion credit;
- theorem or endpoint credit;
- Stage32 closure;
- perfect-cuboid existence/nonexistence credit.

The remaining execution dependency is the final FULL178 survivor/Picard ledger, including exact `C2` for each survivor, followed by the integral/irreducible/normalization-genus disposal required by 32-02.
