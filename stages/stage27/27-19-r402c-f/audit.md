# Stage27-19-r402c-f hostile batch audit

```text
AUDIT_VERDICT=PASS
MATHEMATICAL_AUDIT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
STAGE27_19_R402C_F_STATUS=INTERMEDIATE_AUDITED_PASS_AWAITING_MERGE
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
CONTINUE_UPPER_EXPLORATION_AFTER_PASS=true
MERGE_ALLOWED=true
```

## Scope

This hostile audit covers the four-route checkpoint40 batch `Stage27-19-r402c` through `Stage27-19-r402f` in PR #1040. It accepts exact algebra/combinatorics and restart contracts only. It does not promote any contract to a strict sub-square-root theorem.

## r402c — reduced tau core scale

Accepted exactly:

\[
A=s^2(m^2+n^2)=pg,\qquad D=n^2(r^2-s^2)=qg,
\]

for reduced \(\tau=p/q\) and \(g=\gcd(A,D)\). Since the already-audited physical cutoff gives \(A,D<2B^2\),

\[
gH(\tau)=\max(A,D)<2B^2,
\]

hence

\[
\boxed{g<2B^2/H(\tau)}.
\]

On \(T\le H(\tau)<2T\), \(g\ll B^2/T\). No divisor, representation, support, independence, or fixed-power saving is inferred from this inequality alone.

```text
TAU_CORE_HEIGHT_TRADEOFF_ACCEPTED=true
CORE_TRADEOFF_FIXED_POWER_SAVING_PROVED=false
```

## r402d — full-energy diagonal barrier

With occupied-fiber weights \(w_t\), support \(S\), total \(N=N_2(B)\), ordered off-diagonal collisions

\[
C_\tau=\sum_t w_t(w_t-1),
\]

and full energy \(E_\tau=\sum_t w_t^2\),

\[
\boxed{E_\tau=N+C_\tau\ge N}.
\]

Therefore at the present half-power support wall, a raw full-energy theorem with exponent strictly below \(1/2\) already contains the desired strict upper through its diagonal term. The scoped conclusion `RAW_SECOND_MOMENT_SHORTCUT_CLOSED_AT_HALFWALL=true` is accepted. Off-diagonal/bandwise energy remains open.

```text
TAU_FULL_ENERGY_DIAGONAL_BARRIER_ACCEPTED=true
RAW_SECOND_MOMENT_SHORTCUT_CLOSED_AT_HALFWALL_ACCEPTED=true
OFFDIAGONAL_COLLISION_ROUTE_REMAINS=true
```

## r402e — support/off-diagonal hybrid

For every integer \(w\ge1\), \(w-1\le w(w-1)/2\), so

\[
N-S\le C_\tau/2.
\]

Also Cauchy gives

\[
N^2\le S(N+C_\tau),
\]

hence

\[
\boxed{N\le S+\sqrt{SC_\tau}}.
\]

Thus from same-measure estimates

\[
S\ll B^{\sigma+o(1)},\qquad C_\tau\ll B^{\kappa+o(1)},
\]

one gets

\[
\mu\le\max\{\sigma,(\sigma+\kappa)/2\}.
\]

The stated sufficient strict-subhalf gate

\[
\boxed{\sigma<1/2,\qquad \sigma+\kappa<1}
\]

is correct. The heavy-fiber count and mass inequalities are also correct:

\[
\#\{t:w_t\ge L\}\le C_\tau/[L(L-1)],
\qquad
\sum_{w_t\ge L}w_t\le C_\tau/(L-1).
\]

Off-diagonal collision control alone cannot remove the surviving support term at the half wall.

```text
TAU_OFFDIAGONAL_HYBRID_GATE_ACCEPTED=true
TAU_HEAVY_FIBER_INTERFACES_ACCEPTED=true
OFFDIAGONAL_ALONE_BREAKS_HALFWALL=false
```

## r402f — dyadic restart contract

Because \(1\le H(\tau)<2B^2\), powers-of-two dyadic bands give only \(O(\log B)\) nonempty bands. On each band,

\[
N_T\le S_T+\sqrt{S_TC_T},
\qquad g\ll B^2/T.
\]

If one fixed \(\delta>0\) and a uniform-in-\(T\) estimate give

\[
S_T+\sqrt{S_TC_T}\ll B^{1/2-\delta+o(1)}
\]

for every dyadic band, with the \(o(1)\) uniform across the bands, then the logarithmic band count is absorbed into \(B^{o(1)}\) and

\[
N_2(B)\ll B^{1/2-\delta+o(1)}.
\]

This is accepted as a sufficient restart contract only. The informal observation that low-height bands have fewer available rational labels is not itself credited as a fixed-power survivor-support saving.

```text
TAU_DYADIC_BAND_CONTRACT_ACCEPTED=true
TAU_DYADIC_UNIFORMITY_REQUIRED=true
TAU_DYADIC_BAND_THEOREM_PROVED=false
```

## CI / lifecycle audit

Dedicated `Stage27-19-r402c-f collision batch` CI on submission head `661aef2b799160f07176c80fe8c2aafb42d0e7d7` is SUCCESS. The historical `Stage27-19-r402b` regression is successor-lifecycle verifier debt only: its verifier still requires r402b to be `SUBMITTED_PENDING_FRESH_AUDIT`, while this batch correctly synchronizes r402b to hostile-audited PASS/merged PR #1039. Older r402/r401 red regressions are the same historical-state-freeze class and do not contradict this batch mathematics.

## Final boundary

No strict sub-square-root theorem, no new \(\mu<1/2\), and no true \(N_2\) exponent are proved. Checkpoint40 remains active and checkpoint50 remains blocked.

The next non-formal task is arithmetic: obtain uniform dyadic representation bounds for

\[
s^2(m^2+n^2)=pg,\qquad n^2(r^2-s^2)=qg,
\]

or an equivalent same-measure support/off-diagonal-collision theorem.

```text
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
AUDIT_CLOSE_STAGE=false
NEXT_DERIVED_ROUTE=27-19-r402g
```
