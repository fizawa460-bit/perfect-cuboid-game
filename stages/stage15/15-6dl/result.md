# Stage15-6dl — BLIND_REDISCOVERY, occupancy route selection, and corrected delta ledger

Base: repaired 6dj and occupancy EXHAUSTIVE_VIEW_AUDIT 6dk. This substage restarts from the exact occupancy residual only:
\[
B_q=\sum_{x\in G(P)}(I_q(x)-\mu_q),
\qquad
I_q(x)=1_{d\mid G_S(x)}1_{e\mid G_O(x)},
\qquad
\mu_q=\Omega(q)/q^2.
\]
No earlier route ranking is used in the rediscovery step.

## 1. Blind rediscovery

### Rediscovery A: orientation cancellation is complete at first moment
The signed error is
\[
E_P(Q_0)=\sum_{q\le Q_0}\lambda_q B_q.
\]
Thus averaging over legal orientations cannot by itself save the small-range error: orientation variance is orthogonal to the first-moment occupancy residual.

### Rediscovery B: occupancy pairs force a square-divisor resultant
If two nodes are both occupied at the same odd `q`, local root choices may agree or disagree. Relative signs force one of
\[
m_xn_y\pm m_yn_x
\]
and one of
\[
r_xs_y\pm r_ys_x
\]
to absorb each prime power of `q`. Hence
\[
q^2\mid
(m_xn_y-m_yn_x)(m_xn_y+m_yn_x)
(r_xs_y-r_ys_x)(r_xs_y+r_ys_x).
\]
This independently rediscovers the orientation-blind pair-resultant receiver.

### Rediscovery C: one-point divisor support is too weak
Every occupied `q` divides `Delta_x=m_x^4-n_x^4`. This makes the modulus list divisor-many for a fixed node but does not stop many graph nodes from sharing the same divisor. It is a bookkeeping compression, not an exponent.

### Rediscovery D: reconstructed completion does not imply modulus equidistribution
The 6da theorem says a fixed base triple has only `B^o(1)` completions. But occupancy is already visible in the fixed `(m,n)` fourth-power difference and the completed `(r,s)` channel form. The completion theorem does not make the resulting divisibility residues uniform.

### Rediscovery E: divisor switching changes the large-modulus coordinates, not the signed mean
Switching `d,e` to complementary cofactors is exact and may be useful after a threshold is imposed. However the occupancy residual remains a centered count of switched divisibility events. No inverse threshold power appears without a new average.

### Rediscovery F: character/Ramanujan expansion is an analytic form of the same gate
The centered indicator `I_q-mu_q` can be expanded using additive or multiplicative characters for the two root-line congruences. This converts occupancy bias into a graph correlation sum over moduli. Such an expansion is legal but requires a new whole-family large-sieve/dispersion estimate; no Stage14 fixed-tag theorem may be inserted without an adapter.

## 2. Blind ranking

1. **Orientation-blind pair-resultant square-divisor occupancy energy**: strongest internal exact route. It uses both toric coordinate pairs and attacks the actual occupancy second moment.
2. **Character/Ramanujan occupancy dispersion on reconstructed graph nodes**: analytic equivalent/backup; potentially strong but needs a new whole-family theorem.
3. **Reconstructed divisor switching plus pair-resultant thresholding**: useful for large `q`, currently no inverse-power theorem.
4. **Pell completion modulo q / recurrence correlation**: LIVE but no uniform modulus-distribution statement yet.
5. **One-point Delta divisor incidence and local p=1 mod 4 support**: supporting layers only.

All materially distinct LIVE/UNTESTED routes from 6dk remain preserved.

## 3. Selected next route

The next internal route is
\[
\boxed{\text{ORIENTATION-BLIND PAIR-RESULTANT OCCUPANCY ENERGY}.}
\]
The precise target is to exploit
\[
q^2\mid\mathcal R(x,y)
\]
inside the reconstructed physical graph and prove a power-saving bound for
\[
\mathfrak B_P(Q_0)
=\sum_{q\le Q_0}\frac{\lambda_q}{\Omega_q}|B_q|^2.
\]
The square-root-scale target is
\[
\boxed{\mathfrak B_P(Q_0)\ll |G(P)|Q_0B^{o(1)}}.
\]
If this route is rigorously blocked, the next LIVE analytic form is the character/Ramanujan occupancy-dispersion route, not the already-separated orientation-variance collision theorem.

## 4. Corrected quantitative delta formula

More generally, suppose for some `0<=kappa<=1`
\[
\mathfrak B_P(Q_0)
\ll |G(P)|^{1+\kappa}Q_0B^{o(1)}.
\]
Then
\[
|E_P(Q_0)|
\ll |G(P)|^{(1+\kappa)/2}Q_0^{3/2}B^{o(1)}.
\]
After summing physical packets without polynomial loss, using total reconstructed graph mass `B^{1+o(1)}` and `Q0=B^theta`,
\[
E(Q_0)
\ll B^{(1+\kappa)/2+3\theta/2+o(1)}.
\]
Compared with the small-side profile `B^{1-delta+o(1)}Q0`, this permits only
\[
\boxed{
\delta<\frac{1-\kappa}{2}-\frac\theta2.
}
\]
For the desired square-root occupancy target `kappa=0`,
\[
\boxed{\delta<\frac12-\frac\theta2.}
\]
For the current trivial pair bound `kappa=1`, no positive `delta` is available for any `theta>0`.

Therefore
\[
\boxed{\delta>0\text{ is still unproved}.}
\]
The prior conditional numerical formula is retained only with the corrected occupancy hypothesis.

## 5. Sigma and split eligibility

The large receiver still needs
\[
M_{>D_0}\ll B^{1+o(1)}D_0^{-\sigma}
\]
with `sigma>0`. Neither `q|Delta`, `kg^2|Delta`, exact divisor switching, nor the current occupancy pair-resultant identity proves such an inverse-threshold estimate.

Hence
\[
\boxed{\sigma>0\text{ is unproved}.}
\]
Because neither exponent is independently certified, there is no executable polynomial overlap window and no reason to split the coupled small/large problem yet.

## 6. Arsenal and firewall audit

- AR-009/t76: local root-line engine only; does not control occupancy mean.
- AR-017/6ah: pair-resultant/common-support language is relevant, but the exact current orientation-blind square-divisor energy adapter is not proved.
- t75/t78: divisor switching remains a LIVE refinement, no whole-family exponent transfer.
- tH21/tH22: fixed-U/fixed-tag Type-II/spectral results are not promoted.
- AR-023/024: physical measure remains the exact survivor graph under `R<=B`.
- AR-028: `q`, `kg`, completion labels and cell normalizer are each charged once.

```text
STAGE15_6_SUBSTAGE=6dl
STAGE15_6DL_BLIND_REDISCOVERY=true
STAGE15_6DL_LIVE_CANDIDATES_PRESERVED=true
STAGE15_6DL_SELECTED_ROUTE=ORIENTATION_BLIND_PAIR_RESULTANT_OCCUPANCY_ENERGY
STAGE15_6DL_OCCUPANCY_SQRT_TARGET_PROVED=false
STAGE15_6DL_GENERAL_CONDITIONAL_DELTA=(1-kappa)/2-theta/2
STAGE15_6DL_SQRT_OCCUPANCY_CONDITIONAL_DELTA=1/2-theta/2
STAGE15_6DL_DELTA_PROVED=false
STAGE15_6DL_SIGMA_PROVED=false
STAGE15_6DL_EXECUTABLE_OVERLAP_WINDOW=false
STAGE15_6DL_SPLIT_TRIGGER=false
STAGE15_6DL_AUDIT_REQUIRED=true
STAGE15_6DL_CODEX_REQUIRED=false
STAGE15_6DL_MERGE_ALLOWED=false
```

Controller output:
```text
CURRENT_SUBSTAGE=Stage15-6dl
NEXT_GATE=FRESH_AUDIT_OF_OCCUPANCY_MEAN_REPAIR_AND_PAIR_RESULTANT_SELECTION
ALL_PRIOR_CHECKS_PASS=true
AUDIT_REQUIRED=true
CODEX_REQUIRED=false
MERGE_ALLOWED=false
SPLIT_TRIGGER=false
```
