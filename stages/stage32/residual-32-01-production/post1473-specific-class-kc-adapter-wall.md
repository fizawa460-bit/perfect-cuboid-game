# Stage32 post-1473 specific-class K_c adapter wall

Status: `SOURCE_LOCKED_PARTIAL_KC_ADAPTER_WALL`

Scope: one fixed projection only, `g1-d186`, target `(d,e,a,u,v)=(186,266,592,-44,32)`, `z=(-15,62,-44,26,32)`. No FULL178, route, theorem, receiver, endpoint, or perfect-cuboid credit.

## Exact class retained

V6/V7/V8 fix the support-47 class `C`:

- V6 run `33463183505`, artifact `9783951367`, canonical `76730cd865b4e63791c185636e49202e6e8a4a7e33cf4686d2ac038a3c036417`.
- support `47/48`, unique zero exceptional index `5`.
- Picard SHA256 `2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726`.
- all140 SHA256 `4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3`.
- `C^2=758`, `K.C=186`, `h^0(O(C))>=294`.
- `p_a(C)=473`; an integral normalization-genus-one member would need total defect `472`.

Effectivity still does not imply an integral irreducible normalization-genus-one carrier.

## Testa-Stoll 2026 source lock

Primary source: Michael Stoll and Damiano Testa, **Curves on the surface of cuboids**, *Mathematics of Computation*, DOI `10.1090/mcom/4238`, electronically published `2026-08-10`. Existing repository source lock: `stages/stage29/29-02a/source-lock.md`.

Relevant statements:

1. Section 6 defines `pi:S->K_c` from the sign change `sigma_c` of the long-diagonal coordinate `c`. The second factor contracts exceptional curves over singular points with `c=0`; call this set `E_pi`.
2. Lemma 11 gives
   `pi^*pi_*C = C + sigma_c(C) + sum_{E in E_pi}(C.E)E`.
3. Lemma 12 gives the explicit Picard lattice of `K_c` and, in particular, no odd-degree curves on `K_c`.
4. Theorem 17 / Corollary 18 classify only through canonical degree `6`; the present class has degree `186`.
5. Question 19 leaves the general geometric-genus<=1 classification open.

## Newly recovered repository geometry

The first inventory understated what is already retained. Targeted follow-up found:

- `stages/stage29/29-02ha/coordinate-k3-subcover-adapter.md` is audited and identifies the seven deck involutions `g_T`, `T in {a1,a2,a3,b1,b2,b3,c}`. The quotient by `g_c` is exactly the distinguished `K_c`; over `Q`, `C` is the singleton orbit in the audited `3*K_a + 3*K_b + 1*K_c` split.
- `stages/stage33/33-07/extract_endpoint_coordinate_sign_discriminant_actions.py` constructs the seven exact Picard sign actions from the pinned Testa-Stoll geometry in coordinate order `[a1,a2,a3,b1,b2,b3,c]`; its seventh action is therefore the `sigma_c` action. The script verifies the seven involutions commute and multiply projectively to identity.
- `stages/stage33/33-07/retained-q256-geometric-sign-endpoint.json` non-expiringly retains the seven exact induced actions on the endpoint Picard discriminant module, with the same coordinate order. Thus the geometric identity of `sigma_c` and its retained discriminant action are already source-locked.
- `stages/stage33/33-07/exceptional-p1-tangent-coordinates.json` retains exact ambient `P^6` coordinates of all 48 nodes. Hence `E_pi` is in principle extractable without guessing by the Testa-Stoll rule: select exactly the exceptional IDs whose retained node has seventh (`c`) coordinate zero.
- `stages/stage32/residual-32-01-production/aut_equivariant_pairing_adapter.py` can reconstruct the full 140x140 intersection pairing exactly from the retained 64x64 Gram plus the retained `Aut(S)` action.

Important distinction: the retained seven-sign endpoint certificate stores the action on the discriminant module, not by itself the full 64x64 integral Picard action needed to evaluate `C.sigma_c(C)`. The historical extraction script did construct that integral action, but the current Stage32 hot path does not yet retain/replay the seventh full Picard matrix in the exact Stage32 basis.

The finite Reynolds quotient in `direct_picard_reynolds_rank2_quotient_class_map.py` remains unrelated to the geometric quotient `S->K_c` and must not be substituted.

## Sharpened specific-class test

The useful test is not generic `pi^*Pic(K_c)` membership: Lemma 11 holds for every Picard class and membership alone would not exclude this class.

For a hypothetical integral normalization-genus-one curve in class `C`, use Lemma 11 to form

`P = C + sigma_c(C) + sum_{E in E_pi}(C.E)E = pi^*pi_*C`.

Because `pi` is generically degree two,

`(pi_*C)^2 = P^2 / 2`.

If the curve is not `sigma_c`-invariant, its image on `K_c` is birational to it, hence has geometric genus one. On a K3 surface an integral geometric-genus-one curve has arithmetic genus at least one, so its self-intersection must satisfy `(pi_*C)^2 >= 0`. Therefore an exact negative value would exclude this support-47 class as a genus-one carrier.

If the curve itself were `sigma_c`-invariant and mapped generically two-to-one, its image would have degree `186/2=93`, which is impossible by Lemma 12's even-degree condition on `K_c`. This excludes only the invariant-curve case, not all members of a `sigma_c`-stable divisor class.

## Exact current wall

The route is now narrower than the original four-lock wall. Geometry-level `sigma_c` identification and a discriminant-level retained action are available. What is still missing for the exact single-class self-intersection test is:

1. materialize/replay the **full integral Picard64 action of the seventh sign `sigma_c` in the retained Stage32 basis**, source-locked to the audited coordinate order;
2. extract the exact `E_pi` exceptional IDs from the retained 48 node coordinates using `c=0`, and lock them to the Stage32 exceptional ordering;
3. replay Lemma 11 on the exact V6 witness and calculate `P^2/2`.

A full marked embedding of `pi^*Pic(K_c)` is **not required** for this first necessary-condition test.

Current status:

`BLOCKED_MISSING_FULL_PICARD64_SIGMA_C_AND_EPI_REPLAY`

This is not a mathematical exclusion of `C` and not evidence for carrier existence.

## Next safe action

Build only the three lightweight exact locks above and compute the K3 pushforward self-intersection for this one support-47 class. Do not rerun V1-V8, do not use remote CAS blindly, and do not arm FULL178 heavy production from this fixed projection.
