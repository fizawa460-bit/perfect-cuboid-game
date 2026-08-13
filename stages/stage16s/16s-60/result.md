# Stage16S-60 — causal decomposition

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage16S now has fresh-audited population, finite-data, asymptotic, upper-bound, and lower-bound inputs. This checkpoint separates which losses are caused by the integral-space-diagonal condition itself from restrictions that occur only after an integral face is also imposed.

## 1. Intrinsic ambient cost of the space-diagonal condition

Let

\[
U(B)=\#\{0<a<b<c:\gcd(a,b,c)=1,\ R\le B\}
\]

be the ambient primitive/canonical population. Audited Stage16-30 gives

\[
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2).
\]

Audited Stage16S-30 gives

\[
N_S^{all}(B)\sim\frac{B^2}{32G},
\]

hence

\[
\boxed{\frac{N_S^{all}(B)}{U(B)}
\sim \frac{9\zeta(3)}{8\pi G}\frac1B.}
\]

Therefore the integral-space-diagonal condition already has a polynomial one-power thinning cost before any integer-face condition is imposed. This is the certified intrinsic baseline requested by the Stage16-28 roadmap.

Structurally, the target is the primitive Pythagorean-quadruple locus

\[
a^2+b^2+c^2=d^2.
\]

Hürlimann's adapted cumulative theorem counts that locus at quadratic order, whereas the unconstrained primitive/canonical edge population has cubic order. The phrase “one-power loss” here is a consequence of those audited counting laws, not an independence or random-square heuristic.

## 2. Integer faces are sparse inside the space-integral population

Write

\[
C_F(B)=N_S^{all}(B)-N_S^0(B)
\]

for Stage16S objects with at least one integral face. Audited Stage16S-30 proves

\[
C_F(B)=O_\varepsilon(B^{1+\varepsilon})
\]

for every `epsilon>0`, while both `N_S^{all}(B)` and `N_S^0(B)` are asymptotic to `B^2/(32G)`. Thus

\[
\boxed{\frac{C_F(B)}{N_S^{all}(B)}
=O_\varepsilon(B^{-1+\varepsilon})\to0,}
\]

and

\[
\boxed{\frac{N_S^0(B)}{N_S^{all}(B)}\to1.}
\]

The arithmetic mechanism is the nested Pythagorean system produced by marking a face:

\[
a^2+b^2=e^2,\qquad e^2+c^2=d^2.
\]

The divisor-bound argument at checkpoint 30 shows this nested system is lower-order inside the primitive Pythagorean-quadruple population. Hence the zero-face mask is not responsible for the quadratic Stage16S main term or for the ambient `1/B` thinning.

## 3. Comparison interface to Stage17

Audited Stage17 proves, for adding the space diagonal after exactly one integral face,

\[
\frac{N_1(B)}{M_1(B)}\asymp\frac{(\log B)^2}{B}.
\]

Stage16S proves the unconditioned baseline

\[
\frac{N_S^{all}(B)}{U(B)}\sim C_S/B,
\qquad C_S=\frac{9\zeta(3)}{8\pi G}>0.
\]

Both transitions therefore carry the same certified **polynomial** cost of one power of `B`. The one-face-conditioned transition has an additional logarithmic profile. Consequently:

- the polynomial `B^{-1}` loss is already intrinsic to space-diagonal integrality and is not created by first imposing one integral face;
- the different logarithmic profile is a genuine comparison signal that must be handled by Stage21;
- this checkpoint does **not** promote that signal to probabilistic independence, dependence, or a factorization law.

Stage21 remains the owner of the final intrinsic-versus-interaction classification across the two paths.

## 4. What is not a causal source

- `d=R` on Stage16S is an identity, so the cutoff adapter is not a thinning mechanism.
- strict canonical ordering removes only the audited lower-order repeated-edge family from the Hürlimann count; it does not create the quadratic order.
- primitivity is part of both matched source/target contracts and is not newly charged as the space-diagonal loss.
- Stage16S-20 finite ratios are diagnostic only.
- no claim is made that `C_F(B)=Theta(B log^3 B)` or that its current upper bound is sharp.
- no perfect-cuboid existence or nonexistence conclusion is implied.

```text
AMBIENT_ORDER=U(B) ASYM B^3
SPACE_AT_LEAST_ORDER=N_S^all(B) ~ B^2/(32G)
SPACE_ONLY_ORDER=N_S^0(B) ~ B^2/(32G)
INTRINSIC_SPACE_SURVIVAL ~ [9 zeta(3)/(8 pi G)]/B
INTRINSIC_POLYNOMIAL_COST=ONE_POWER_OF_B
PRIMARY_SPACE_MECHANISM=PRIMITIVE_PYTHAGOREAN_QUADRUPLE_LOCUS
FACEFUL_COMPLEMENT=C_F(B) <<_epsilon B^(1+epsilon)
FACEFUL_FRACTION_IN_STAGE16S -> 0
ZERO_FACE_MASK_CHANGES_MAIN_TERM=false
STAGE17_SPACE_SURVIVAL=Theta((log B)^2/B)
POLYNOMIAL_COST_MATCHES_STAGE17=true
LOG_PROFILE_MATCHES_STAGE17=false
FINAL_INDEPENDENCE_OR_INTERACTION_CLASSIFICATION=DEFER_TO_STAGE21
CUTOFF_ADAPTER_CAUSE=false
FINITE_DATA_USED_AS_PROOF=false
EVIDENCE_LEVEL=DERIVED_FROM_AUDITED_STAGE16_30_STAGE16S_30_40_50_STAGE17_30_60
```

Checkpoint 70 is the bounded maximal synthesis / intrinsic-status closeout. Because checkpoint 60 adds a causal interpretation and cross-stage comparison, the main lane stops here for fresh audit.

```text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16S
CURRENT_CHECKPOINT=60
CHECKPOINTS_ATTEMPTED=60
CHECKPOINTS_SUBMITTED=60
NEW_CLAIMS=causal decomposition: intrinsic space-diagonal polynomial cost is B^-1; zero-face exclusion does not change the Stage16S main term; Stage17 shares the same polynomial cost but has a different logarithmic profile
REUSED_WEAPONS=Stage16-30,Stage16S-30,Stage16S-40,Stage16S-50,Stage17-30,Stage17-60,Hurlimann-2015-after-audited-adapter
CODEX_REQUIRED=false
CODEX_REASON=Checkpoint 60 is a compact synthesis of already audited counting laws; no implementation task is needed.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16S-audit
```