# Stage15-6bg — integral-point second-moment audit and minimal admissible-diagonal support gate

Base: Stage15-6bf in the current cycle. Stages 6bd–6be eliminated the explicit global `k` sum and proved `B^o(1)` multiplicity above each fixed physical diagonal product `S`. Stage15-6bf then proved that the corresponding congruent-number points have genuinely moving rational denominators.

Audit verdict: `NEW_GATE`.

The direct integral-point / second-moment literature is **not** the minimal or directly applicable receiver. The exact remaining problem is the support of admissible `S` values.

## 1. Chan's congruent-number integral-point theorem: direct reuse blocked

Stephanie Chan, *Integral points on the congruent number curve*, Trans. AMS 375 (2022), arXiv:2004.03331, proves strong bounds for **integral points** on

\[
\mathcal E_D:y^2=x^3-D^2x,
\]

including per-coset bounds, bounded average number of non-torsion integral points, and a simultaneous-Pell application.

Stage15-6bf gives instead

\[
X=U^2,
\qquad
\operatorname{den}(U)=ce\text{ or }2ce,
\]

with point-dependent `c,e`. Thus a generic retained point is not an integral point on the minimal twist model. Chan's integral-point theorem and its integer simultaneous-Pell corollary cannot be directly substituted.

```text
CHAN_2022_DIRECT_REUSE=false
REASON=STAGE15_POINTS_HAVE_MOVING_RATIONAL_DENOMINATORS
```

## 2. Choi's general twist integral-point theorem: same mismatch

Seokhyun Choi, *Number of integral points on quadratic twists of elliptic curves*, arXiv:2509.03274 (revised 2026), proves a rank-dependent bound for integral points on general quadratic twists and derives bounded average integral-point count in a fixed twist family.

Again, the counted objects are integral points. The Stage15 denominator support varies with the point, so this theorem does not count the Stage15 packet without a new denominator adapter.

```text
CHOI_2026_DIRECT_REUSE=false
```

## 3. Alpöge–Ho second moment: quantifier and S-integrality mismatch

Levent Alpöge and Wei Ho, *The second moment of the number of integral points on elliptic curves is bounded*, arXiv:1807.03761, prove bounded moments for `S`-integral points on the family of all integral short Weierstrass curves ordered by height, and on positive-density subfamilies, for a **fixed finite set of places S**.

Two mismatches prevent direct Stage15 reuse:

1. the denominator prime set of a Stage15 point varies with `ce`, so there is no fixed finite set of allowed denominator primes over the whole physical family;
2. the congruent-number quadratic-twist family is a thin one-parameter family, not automatically a positive-density subfamily of all short Weierstrass curves ordered by height.

Therefore the bounded second moment cannot be promoted to the Stage15 host measure.

```text
ALPOGE_HO_DIRECT_REUSE=false
AR-027=FAIL_FOR_DIRECT_PROMOTION
```

## 4. Why these blocks no longer hurt

Stage15-6be already proved

\[
\boxed{\#\{\text{physical survivors over fixed }S\}=B^{o(1)}}.
\]

Thus an external point-count second moment is no longer needed to control packet multiplicity. The old 6bc gate was a correct conditioned formulation, but 6bd–6be found a more global disintegration.

Define

\[
\mathcal S(B)=\left\{S\le2B:\begin{array}{l}
F_1F_2=S^2\text{ for two primitive coordinate states},\\
\operatorname{sf}(f_1g_1)=\operatorname{sf}(f_2g_2),\\
\text{and the reconstructed point passes the physical masks}
\end{array}\right\}.
\]

Then

\[
\boxed{N_2(B)\ll |\mathcal S(B)|B^{o(1)}}
\]

and conversely every `S` in the support comes from at least one retained physical point (up to the absolute `gamma` branch decoration). Hence the exponent problem is equivalent, up to `B^o(1)`, to the support exponent.

## 5. Exact algebraic support receiver

For fixed coordinate-squareclass allocations, the support condition is the integral product-square equation

\[
\boxed{
Y^2=
(\kappa_{f,1}^2c_1^4+\kappa_{g,1}^2e_1^4)
(\kappa_{f,2}^2c_2^4+\kappa_{g,2}^2e_2^4),
\qquad Y=S\le2B.
}
\]

with primitive/coprime masks and the equality of the two aggregate coordinate cores. Projectively this is a `(4,4)` double-cover / Kummer-type receiver; the relevant arithmetic height is **not** ordinary box height but the physical coordinate `Y=S`.

The Stage15 target is now the support theorem

\[
\boxed{|\mathcal S(B)|\ll B^{1/2+o(1)}}.
\]

Proving this would causally recover the half-power numerator exponent because the fixed-`S` fiber is already `B^o(1)`.

Stage14 AR-006 of course implies the same support bound indirectly via the already-proved whole-family theorem, but importing AR-006 here would merely reproduce Stage15-5 and would not explain the Gaussian/coordinate mechanism. It is therefore kept as a correctness backstop, not counted as a new causal derivation.

## 6. Audit ledger

```text
CHAN_2022_INTEGRAL_POINT_SECOND_MOMENT=DIRECT_REUSE_BLOCKED
CHOI_2026_TWIST_INTEGRAL_POINT_AVERAGE=DIRECT_REUSE_BLOCKED
ALPOGE_HO_S_INTEGRAL_SECOND_MOMENT=DIRECT_REUSE_BLOCKED
FIXED_S_PACKET_MULTIPLICITY_ALREADY_CLOSED=true
OLD_WEIGHTED_TWIST_SECOND_MOMENT_GATE=SUPERSEDED
NEW_MINIMAL_GATE=ADMISSIBLE_PHYSICAL_DIAGONAL_SUPPORT_COUNT
AUDIT_VERDICT=NEW_GATE
```

## 7. Frozen exit

```text
STAGE15_6_SUBSTAGE=6bg
STAGE15_6BG_AUDIT_VERDICT=NEW_GATE
STAGE15_6BG_INTEGRAL_POINT_THEOREM_DIRECT_REUSE=false
STAGE15_6BG_S_INTEGRAL_SECOND_MOMENT_DIRECT_REUSE=false
STAGE15_6BG_WEIGHTED_TWIST_SECOND_MOMENT_GATE_SUPERSEDED=true
STAGE15_6BG_FIXED_S_FIBER=B^o(1)
STAGE15_6BG_SUPPORT_RECEIVER=Y^2=F1*F2;Y<=2B
STAGE15_6BG_TARGET_SUPPORT_BOUND=B^(1/2+o(1))
STAGE15_6BG_SUPPORT_BOUND_PROVED=false
STAGE15_6BG_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6BG_EXIT=ADMISSIBLE_DIAGONAL_KUMMER_SUPPORT_THEOREM_GATE
```

Next cycle: audit the `(4,4)` product-square/Kummer-type receiver under the **Y-height** `Y<=2B`. Do not return to integral-point second moments unless a new exact denominator adapter changes the host measure.
