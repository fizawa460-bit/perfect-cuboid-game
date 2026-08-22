# Stage29-15 — ENDPOINT_ARSENAL_REMATCH

```text
STAGE=Stage29
ITEM=29-15_ENDPOINT_ARSENAL_REMATCH
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
BASE_MAIN_SHA=469996b93fe93650423fb2b4d629f67b1a2998b9
ATTACK_ROUTE_COUNT_RETAINED=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
NEW_DECISIVE_GLOBAL_THEOREM_FOUND=false
NEW_OPEN_RECEIVER_DISCHARGED_COUNT=0
P_OVER_M3_SCALE_KNOWN=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Purpose

This item performs the roadmap-required rematch of the Stage14 Arsenal, StructureRadar corpus, and a fresh 2025–2026 literature sweep against the exact endpoint receivers that survived 29-10 through 29-14.

The classification vocabulary is:

```text
APPLICABLE_NOW
APPLICABLE_AFTER_EXACT_ADAPTER
ALREADY_CONSUMED
REDUNDANT
NONAPPLICABLE
```

A theorem species receives `APPLICABLE_NOW` only when its stated hypotheses already match the exact Stage29 receiver, including field, map direction, physical height/measure where relevant, and rational-point versus counting semantics.

## 2. Whole endpoint / general-type route

The strongest certified whole-endpoint input remains the Stage14 consequence

```text
P(B) <<_epsilon B^(1/2+epsilon).
```

It is `ALREADY_CONSUMED` and gives sparsity rather than emptiness.

### Surface Chabauty: exact nonapplicability to the endpoint surface

Caro–Pasten's surface Chabauty–Coleman theorem, and the 2025 Balakrishnan–Caro refinement, require a hyperbolic surface embedded in an abelian variety whose relevant Mordell–Weil rank is at most one (the refinement treats the special surface W_2 inside a genus-3 Jacobian).

The resolved cuboid endpoint has

```text
q(S)=h^1(O_S)=0.
```

Hence `Alb(S)` is zero-dimensional. Every morphism from the smooth projective `S` to an abelian variety factors through `Alb(S)`, so there is no nonconstant morphism, much less an embedding, of `S` into an abelian variety. Therefore this theorem species is not merely missing a rank calculation:

```text
R29-ARS-SURFACE-CHABAUTY=NONAPPLICABLE_TO_FULL_ENDPOINT_BY_ALBANESE_ZERO
```

This does not rule out Chabauty on curves, covers, or other positive-irregularity auxiliary varieties.

The existing `R29-PI1-OPEN` nonabelian/higher-dimensional Kim receiver remains open; no current cuboid-specific effective Kim function was found.

## 3. Low-genus / slice arithmetic

The following theorem species remain genuinely useful after a concrete Q-defined curve receiver is produced:

```text
rank-zero elliptic quotient enumeration
classical Chabauty-Coleman
elliptic curve Chabauty
Mordell-Weil sieve
quadratic/bielliptic quadratic Chabauty
```

A 2025 rank-zero-quotient treatment explicitly formulates the elementary principle that a genus >=2 curve mapping over Q to a genus-one curve with rank-zero Jacobian has its Q-points obtained from finitely many fibers of the quotient. This is the same method species already realized in 29-13 for Saunderson, so it is not new attack credit.

For the unresolved Testa–Stoll genus-5 endpoint fibrations, these methods are

```text
APPLICABLE_AFTER_EXACT_ADAPTER
```

not `APPLICABLE_NOW`, because Stage29 still lacks a per-fibration Q-definition ledger, exact Jacobian/rank/Selmer data for the relevant physical fibers, and a global theorem saying finitely many fibers or sections cover all endpoint Q-points.

The degree-<=6 curve classification and the finite Picard reduction are `ALREADY_CONSUMED`. The residual receivers remain

```text
R29-LG2
R29-LG2-EFF
R29-LG2-MB.
```

Even their completion would classify positive-dimensional low-genus carriers, not isolated surface points.

## 4. K3 / coordinate-sign quotients

The seven Q-defined coordinate-sign quotient maps remain globally valid in the pushforward direction. K3 arithmetic theorems found in the refresh are mostly family-specific Brauer computations, density constructions, or potential-density results; none gives a theorem that the relevant cuboid K3 quotient has no Q-points.

The 2024/2025 Tawfik–Newton transcendental Brauer results are for explicit singular Kummer surfaces `Kum(E x E')` with CM hypotheses and do not automatically identify or compute the cuboid quotient Brauer classes. They are

```text
APPLICABLE_AFTER_EXACT_ADAPTER
```

only if a specific coordinate-sign K3 is placed in their exact Kummer/CM model and the physical image locus is tracked.

Recent K3 rational-point work supplies examples with many or Zariski-dense rational points and reinforces the existing firewall that K3 structure by itself is not an emptiness theorem.

Thus

```text
G10-K3-SIGN=AMBER
```

is unchanged.

## 5. Campedelli / involution route

The Calabri–Mendes Lopes–Pardini / Mendes Lopes–Pardini–Reid involution and quotient classification is already consumed in 29-11. The fresh literature sweep found later work using those classifications for Chow/Bloch questions, not a new arithmetic theorem forcing Q-point emptiness on the exact cuboid Campedelli forms.

```text
R29-CAMP3-GEOM=ALREADY_CONSUMED
R29-CAMP3=APPLICABLE_AFTER_EXACT_ADAPTER
```

The missing component remains the exact Q-form / involution assignment and arithmetic use of the resulting quotient, not another geometric rational-or-Enriques dichotomy.

## 6. Beauville / twist descent

The exact Q-defined Beauville double cover and its infinite quadratic-twist decomposition are already consumed.

Fresh twist literature includes strong statistical results such as Browning–Chan's theorem that almost all quadratic twists of a fixed elliptic curve have no integral points under stated hypotheses (with a conditional component in the partial-2-torsion case). This does not give what the cuboid Beauville route needs:

```text
all relevant twists, rational rather than integral points,
a finite physically allowed twist set,
or a uniform Selmer/rank-zero closure.
```

Hence it is `NONAPPLICABLE` as a direct closure theorem and does not change

```text
Q11-BEAUVILLE=AMBER_EXACT_Q_COVER_INFINITE_TWIST_FAMILY_NO_UNIFORM_SELMER_CLOSURE.
```

StructureRadar's generalized-Jacobian/Prym/2-descent interface (`SR-STR-163`) remains `APPLICABLE_AFTER_EXACT_ADAPTER` on an individual twist or curve once the exact covering packet is materialized.

## 7. Modular / 8-congruence route

The modular `X(8)` / 8-congruence ecosystem is already structurally consumed. Existing twist-of-X(8) constructions demonstrate that rational points on 8-congruence twists can occur and provide explicit families; they do not uniformly eliminate the sigma-twisted arithmetic classes relevant to the endpoint.

No fresh theorem was found that discharges

```text
R29-KUM5=OPEN_ACTION_LEVEL_S4_Q_DESCENT_ADAPTER
```

or turns the finite ordinary defect-class compression into arithmetic class elimination.

```text
Q11-MODULAR=AMBER
```

is unchanged.

## 8. Brauer / open physical locus

29-11 already certifies the proper algebraic Brauer group as trivial modulo `Br(Q)` and eliminates nonconstant proper odd-primary contribution at the audited level.

Fresh K3/transcendental Brauer papers show that odd transcendental Brauer classes can matter on special Kummer K3 surfaces, but they do not supply an endpoint-open two-primary class or an obstruction for the cuboid physical open.

The outstanding receiver is still the boundary-sensitive open-surface computation:

```text
UPic / Gersten / two-primary physical-open Brauer data.
```

General Brauer–Manin formalism is therefore `APPLICABLE_AFTER_EXACT_ADAPTER`; no class has been found whose evaluation makes the cuboid adelic set empty.

## 9. Local squareclass / sieve / thin-set route

StructureRadar cards `SR-STR-161,164,165,166,169,170,171,173,174` and Stage14 counting weapons remain valuable only under their exact measures/adapters.

For the full endpoint local route, 29-09/12 already has exact odd-prime squareclass data and a positive Q2 lift cylinder. The missing step `R29-KUM-LOC3` is a physical-height/measure transfer. Ambient large sieve, thin-set, toric equidistribution, and Gaussian-Hecke results do not automatically preserve the selected endpoint measure.

Thus these theorem species are classified as either `ALREADY_CONSUMED` for existing sparsity results or `APPLICABLE_AFTER_EXACT_ADAPTER` for `R29-KUM-LOC3`; none is promoted to an endpoint-emptiness theorem.

## 10. Parametric / fibration route

The global Master-Hit coverage theorem is `ALREADY_CONSUMED` and remains the strongest exact global parametrization result.

The decisive exponent-one statement remains

```text
R29-PESCH-E1=AMBER_CONJECTURAL_GLOBAL_ENDPOINT_BLOCKER.
```

No theorem converting the current finite verifications into the global exponent-one statement was found.

StructureRadar `SR-STR-162` and `SR-STR-223` remain especially close theorem species for moving elliptic/genus-five fibers, but both were already classified as family-level external gates. 29-08/14 did not supply the missing uniform small-point/rank/lift theorem or all-Q-defined fiber ledger.

The individual curve tools above are useful, but fiber-by-fiber Chabauty does not become a uniform proof over an infinite parameter base without a separate theorem.

## 11. Population interaction

The population route remains the sole GREEN route:

```text
J12-POP-INTERACTION=GREEN_RELATIVE_ENDPOINT_DENSITY_THEOREM_NO_EMPTINESS.
```

Stage14/StructureRadar counting machinery is already consumed in its proof and in the endpoint upper theorem. No rematched counting theorem currently controls

```text
P(B)/M3(B).
```

The Saunderson closure additionally proves an explicit `B^(1/3)` lower population inside `M3-P`, but this still does not determine `P/M3`.

## 12. 29-15 rematch verdict

The arsenal is useful primarily in three ways:

1. it prevents repeating already-consumed counting/descent work;
2. it supplies concrete curve-level methods as soon as an exact low-dimensional receiver appears;
3. it removes attractive but structurally impossible whole-endpoint routes, most notably abelian surface Chabauty on `S` because `q(S)=0`.

It does not presently supply a theorem that closes any of the ten AMBER primary attack routes.

```text
ARSENAL_REMATCH_COMPLETE=true
NEW_DECISIVE_GLOBAL_THEOREM_FOUND=false
NEW_OPEN_RECEIVER_DISCHARGED_COUNT=0
NEW_EXACT_NONAPPLICABILITY_CERTIFICATE_COUNT=1
NEW_EXACT_NONAPPLICABILITY_CERTIFICATE=FULL_ENDPOINT_SURFACE_CHABAUTY_BY_ALBANESE_ZERO
ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
TARGETED_BACKFLOW_REQUIRED=false
ROADMAP_REWRITE_REQUIRED=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM_AFTER_AUDIT_PASS=29-16_RESIDUAL_RECEIVER_COMPRESSION_AND_ROUTE_PORTFOLIO
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
