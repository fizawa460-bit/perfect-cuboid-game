# Stage15-5 — survival/thinning theorem under the matched Stage15 denominator

Base: merged Stage15-4 (`PR #831`, merge commit `e1b4837`) and the merged Stage14 Arsenal. Stage15-5 answers roadmap item 6 only: prove the strongest currently certified survival/thinning law for the integral-space-diagonal subpopulation inside the ambient exactly-two population. It does not yet claim a causal derivation of that loss from the Stage15-4 Gaussian squareclass normal form.

## 1. Populations and common cutoff

Use the Stage15-0 notation

\[
\mathcal B_2(B)=\{\text{primitive canonical exactly-two boxes}:R\le B\},
\]

\[
\mathcal A_2(B)=\{C\in\mathcal B_2(B):R\in\mathbf Z\},
\]

with counts

\[
M_2(B)=\#\mathcal B_2(B),\qquad N_2(B)=\#\mathcal A_2(B).
\]

On `A_2`, write the integral space diagonal as `d=R`. Stage15-0 proved the exact cutoff identity

\[
R\le B\iff d\le B.
\]

Therefore the Stage14 `N_2(B)` theorem and the Stage15 ambient `M_2(B)` theorem are already stated on the same physical population convention and the same height cutoff. No new height, denominator, orientation, or measure adapter is required in Stage15-5.

## 2. Two certified inputs

### Input A — Stage14 numerator bound

Stage14 Theorem 2.1 proves that for every `epsilon>0` there are constants `C_epsilon,B_epsilon` such that

\[
N_2(B)\le C_\epsilon B^{1/2+\epsilon}
\]

for every `B>=B_epsilon`. Equivalently,

\[
N_2(B)\ll B^{1/2+o(1)}.
\]

This is exactly the `A_2` numerator, not an ambient theorem.

### Input B — Stage15 ambient denominator

Stage15-2b proves

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}>0.
\]

It also proves, in each shared-edge direction `j in {a,b,c}`,

\[
M_{2,j}(B)\sim C_jB(\log B)^5,
\qquad C_j>0.
\]

## 3. Main survival theorem

Define the survival ratio

\[
S(B)=\frac{N_2(B)}{M_2(B)}.
\]

**Theorem 15.5.1.** For every `epsilon>0`,

\[
\boxed{
S(B)\ll_\epsilon
B^{-1/2+\epsilon}(\log B)^{-5}.
}
\]

In particular,

\[
\boxed{S(B)\longrightarrow0.}
\]

More strongly, for every fixed `delta<1/2`,

\[
\boxed{S(B)\ll_\delta B^{-\delta}.}
\]

Thus imposing an integral space diagonal on the ambient exactly-two family produces a certified polynomial thinning of every exponent strictly below `1/2`, in addition to the explicit denominator factor `(log B)^-5` in the epsilon formulation.

### Proof

Because `C_M2>0` and

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\]

there is `B_0` such that for `B>=B_0`,

\[
M_2(B)\ge \frac{C_{M_2}}2 B(\log B)^5.
\]

For `B>=max(B_0,B_epsilon)`, Stage14 gives

\[
N_2(B)\le C_\epsilon B^{1/2+\epsilon}.
\]

Therefore

\[
\frac{N_2(B)}{M_2(B)}
\le
\frac{2C_\epsilon}{C_{M_2}}
B^{-1/2+\epsilon}(\log B)^{-5}.
\]

This proves the displayed epsilon bound and hence zero density. Given any `delta<1/2`, choose `epsilon` with `0<epsilon<1/2-delta`; then `-1/2+epsilon<-delta`, so the stronger-looking fixed-power statement follows after enlarging the constant. ∎

## 4. Directional survival theorem

Let `N_{2,j}(B)` be the survivor count whose unique shared edge is in canonical direction `j in {a,b,c}`. No directional Stage14 asymptotic or directional square-root theorem is needed: trivially

\[
N_{2,j}(B)\le N_2(B).
\]

Since Stage15-2b proved `M_{2,j}(B)~C_jB(log B)^5` with `C_j>0`, the same argument gives, for every `epsilon>0`,

\[
\boxed{
\frac{N_{2,j}(B)}{M_{2,j}(B)}
\ll_{\epsilon,j}
B^{-1/2+\epsilon}(\log B)^{-5}
}
\]

for `j=a,b,c`.

Hence the integral-space-diagonal survivors have zero relative density in every shared-edge direction separately. This does **not** compare the three survivor constants or prove that one direction thins faster than another.

## 5. Relation to the Stage15-4 exact normal form

Stage15-4 proved the exact survivor condition

\[
\operatorname{sf}(N(mr+i\,ns))
=
\operatorname{sf}(N(ms+i\,nr)),
\]

or equivalently

\[
A=kP^2,\qquad B=kQ^2
\]

for one common squarefree core `k`.

The theorem above shows how sparse this exact condition is in the physical Stage15 population, but Stage15-5 does **not** claim that the exponent `1/2` has been rederived directly from this squareclass-coincidence equation. The certified half-power loss enters through Stage14 Theorem 2.1.

This distinction matters for the next causal stage:

- **proved now:** the actual Stage15 survival ratio has the displayed half-power upper thinning;
- **not proved now:** a self-contained squareclass/Gaussian argument from the Stage15-4 toric coordinates alone yields the same exponent;
- **not proved now:** `N_2(B)` has order `B^{1/2}` or any matching lower bound;
- **not proved now:** the true survival exponent equals `1/2`;
- **not proved now:** a strict improvement `N_2(B)<<B^{1/2-delta}`.

## 6. Arsenal audit

The merged Stage14 Arsenal makes the theorem bridge explicit and prevents illegal promotion.

### AR-006 — Stage14 whole-family square-root theorem

Classification in Stage15-5: `DIRECT_NUMERATOR_REUSE`.

AR-006 is not promoted to the ambient family. It is applied only to `A_2`, which Stage15-0 identified exactly with the Stage14 physical `N_2` population under the same cutoff. This is precisely the reuse that AR-006 permits.

### AR-001 / AR-003

The primitive/canonical convention and exactly-two gluing/multiplicity contract agree across the two stages. These are already consumed by Stage15-0 and need no new charge.

### AR-023 / AR-024

The scalar/pair and same-kernel/different-measure firewalls pass here because no toric host compression is used in the proof. The numerator and denominator are divided only after both are stated in the same physical object measure.

### AR-028

No support is double charged. Stage14 supplies one numerator bound; Stage15-2b supplies one independent ambient denominator asymptotic. The Stage15-4 core `k` is not counted again to manufacture another saving.

### AR-017 / AR-009 / AR-018

These remain `ADAPTER_REQUIRED` mechanism candidates. They are not needed to prove Theorem 15.5.1, and Stage15-5 does not claim that their Stage14 savings transfer to the ambient toric-pair measure.

### AR-012 / AR-013 / AR-014

Their Stage15-4 classifications are unchanged: AR-012 and AR-013 are not triggered; AR-014 remains a watch item pending a genuine fixed-outer square-divisor lock.

## 7. What the theorem says about the Stage15-3 data

At `B=100000`, Stage15-3 found

```text
M2=796698
N2=89
N2/M2=0.00011171108751371284
```

Those numbers are consistent with strong thinning, but they play no role in the proof above. Stage15-5 therefore upgrades the qualitative numerical observation `N2/M2 is small` to an unconditional asymptotic zero-density theorem with a polynomial upper rate.

No empirical slope from the 89 survivors is used.

## 8. Frozen exit

```text
STAGE15_5_COMMON_CUTOFF_ADAPTER_REQUIRED=false
STAGE15_5_STAGE14_NUMERATOR_REUSE=AR-006_DIRECT_NUMERATOR_REUSE
STAGE15_5_AMBIENT_DENOMINATOR=M2~C_M2*B*(logB)^5
STAGE15_5_SURVIVAL_ZERO_DENSITY=true
STAGE15_5_SURVIVAL_RATIO_BOUND=O_epsilon(B^(-1/2+epsilon)*(logB)^(-5))
STAGE15_5_POLYNOMIAL_THINNING_ANY_DELTA_LT_HALF=true
STAGE15_5_DIRECTIONAL_ZERO_DENSITY=true
STAGE15_5_TRUE_SURVIVAL_EXPONENT_IDENTIFIED=false
STAGE15_5_MATCHING_LOWER_BOUND=false
STAGE15_5_STRICT_SUB_SQRT_NUMERATOR_IMPROVEMENT=false
STAGE15_5_GAUSSIAN_CAUSAL_DERIVATION_PROVED=false
STAGE15_5_EXIT=HALF_POWER_UPPER_THINNING_PROVED
```

## 9. Next roadmap target

Stage15-6 should address causality rather than re-prove the ratio theorem: starting from the exact Stage15-4 paired Gaussian-norm squareclass condition, determine which arithmetic mechanism actually accounts for the observed thinning and whether AR-017/009/018 admit an exact measure-preserving adapter. Any claim of a stronger numerator exponent must remain separate from the already certified Stage15-5 comparison theorem.
