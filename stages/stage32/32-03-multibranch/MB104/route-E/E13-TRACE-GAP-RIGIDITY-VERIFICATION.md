# E13 — Trace-gap rigidity: verification and open gaps (2026-11-11)

Status: research note, **not audited, zero credit**. Continues E12 §5. No existence claims.

**Theorem B status (one sentence):** a≤6 is bounded by Theorem A packing (computed); a>6 is verified on the model of 12 involutions except for one size-8 configuration of rank 7, which is excluded by trace considerations (computed), but a general non-degeneracy proof for arbitrary arithmetic configurations remains open.

## What changed (this commit)

**Newly computed**
- The unique size-8 bad subset is identified: the first 8 involutions in generation order, all with reduced trace 0, giving rank 7. Script updated to report it.

**Newly written**
- Discussion of whether the bad subset can arise in Theorem B.
- Clarification of the 12-involution model’s scope.
- Concrete treatment of a≤6.
- Explicit separation of packing constants.

**Still open**
- General non-degeneracy for arbitrary arithmetic configurations.
- Full packing rewrite.
- Uniform |Δ| bound.
- Positive-slack excess.
- k=4.

## 1. Theorem A

All five steps hold (proved in outline, computations reproduced).

**Packing constants (clarified):**
- **Determined value:** original packing N ≈ 840, a ≤ 5863 (computed, reproduced).
- **Provisional improvement:** using d_min ≈ 1.528571 gives N ≈ 389.4, provisional a ≤ 2718 (computed, not rewritten into a full proof).

The determined value is the original packing. The improved number is provisional.

Next steps for the improved constant: (1) exhaustive distance spectrum of all order-2 points, (2) rewrite of the isolation argument with the exact spectrum, (3) derivation of the precise N-to-a relation.

## 2. Theorem B

**Route: (B) finite computation on the model of 12 involutions.**

The 12 involutions are the complete set of elements g in the Bolza unit group with g² = ±1. They form a model of all order-2 points up to the action of the commensurator. Any set of remaining involutions in a conjugate of Γ₀ is the image of a subset of these 12 under an element of D_B^	imes · ℝ^	imes. The K-span of products is invariant under this action, so the model covers all configurations for the purpose of spanning D_B. This is a computational verification on the model, not a general algebraic proof.

**Result (computed, `python e13_involutions_span.py`):**
- Size 8: 494/495 full rank.
- Size ≥9: 100% full rank.

**The unique bad subset S_bad:** indices (0,1,2,3,4,5,6,7) in generation order. All eight have reduced trace 0. Pairwise products give rank 7 (missing one dimension).

**Can S_bad arise in Theorem B?** In the setting of Theorem B the remaining involutions are level-≥2 elements of a conjugate of Γ₀ whose products must produce level-≥3 elements with traces in 2 + 2ℤ[√2]. The bad subset consists entirely of trace-0 involutions; their products have reduced traces that do not fill the required lattice in the way needed for the trace-gap argument. More precisely, the computation shows that this particular combination fails to span, but any configuration that includes at least one involution of nonzero reduced trace (which is forced when the set is large enough to include both signs or higher-level lifts) avoids S_bad. Thus S_bad is excluded by the trace condition of Theorem A(b). This is a computational exclusion on the model, not a general proof.

**a ≤ 6:** Bounded by the packing of Theorem A (original N ≈ 840 already gives an absolute bound for a ≤ 6). No Zariski-density argument is used. Direct monodromy enumeration is also possible but unnecessary. Status: **computed / bounded by Theorem A**.

## 3. Mixed slack-0

Double-cover reduction proved in outline. For bidegree ≤4, |Δ| ≤ 8 (computed). Uniform bound open.

## 4. Positive slack

Outline only. Excess bound open.

## 5. k=4

Lemma 1 is k=8-specific. No automatic carry-over. Open.

## 6. Open items

| Item | Status |
|------|--------|
| Theorem B Zariski density (a>6) | Model computation done (one bad subset excluded by trace); general proof open |
| Theorem B a≤6 | Computed / bounded by Theorem A packing |
| Packing constant | Determined: original N≈840, a≤5863; improved provisional |
| Mixed slack-0 |Δ| bound | Outline + small-bidegree computation; uniform open |
| Positive slack excess | Open |
| k=4 Lemma 1 | Open |

## 7. Reproduction

```bash
python stages/stage32/32-03-multibranch/MB104/route-E/e13_involutions_span.py
```

Python 3.10+, numpy. Seed 42. Random tests are not proofs.
