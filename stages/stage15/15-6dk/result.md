# Stage15-6dk — EXHAUSTIVE_VIEW_AUDIT of the modulus-occupancy-bias receiver

Base: repaired Stage15-6dj. The fresh audit exposed a material receiver change: the signed small-range error is controlled by modulus occupancy bias, while same-orientation pair energy controls only orientation variance. Therefore this substage runs the required exhaustive view before selecting a new theorem gate.

For `q=de`, write
\[
I_q(x)=1_{d\mid G_S(x)}1_{e\mid G_O(x)},
\qquad
\mu_q=\frac{\Omega(q)}{q^2},
\]
so
\[
B_q=N_{d,e}(P)-\mu_q|G(P)|
=\sum_{x\in G(P)}(I_q(x)-\mu_q).
\]
The occupancy second moment is
\[
\mathfrak B_P(Q_0)
=\sum_{de\le Q_0}\frac{\lambda(d,e)}{\Omega(d,e)}|B_{de}|^2.
\]
All graph nodes retain `R<=B`, `HMNUV<=B`, `(q,H)=1`, `kg^2|Delta`, exact survivor equations and all masks.

## 1. One-point occupancy structure

If `d|G_S(x)` and `e|G_O(x)`, then
\[
d\mid m_x^2+n_x^2,\qquad e\mid m_x^2-n_x^2.
\]
For the odd part, S/O supports are disjoint, hence
\[
\boxed{q\mid \Delta_x:=m_x^4-n_x^4.}
\]
The second toric pair simultaneously satisfies the complementary channel divisibilities. Thus every occupied modulus is a divisor of an explicit polynomially bounded fourth-power difference.

Stage15-6df also gives
\[
kg^2\mid\Delta_x.
\]
However this does not imply `q|kg`, `kg|q`, or any bounded-index relation between `q` and `kg`. They are two separately generated divisors of the same host `Delta_x`. Therefore `kg^2|Delta` alone does not supply occupancy equidistribution or an inverse power of `q`.

For fixed node `x`, the number of possible occupied `q` is divisor-like, but this is only `B^o(1)` multiplicity. It does not show that a fixed modulus is occupied by fewer than the ambient number of graph nodes.

## 2. Exact orientation-blind pair-resultant lock

Let two graph nodes `x,y` both be occupied by the same odd switched modulus `q=de`. Put
\[
A_-=m_xn_y-m_yn_x,\qquad A_+=m_xn_y+m_yn_x,
\]
\[
B_-=r_xs_y-r_ys_x,\qquad B_+=r_xs_y+r_ys_x.
\]
For every odd prime power `p^nu|q`, both nodes are in the same S/O channel type, but they may choose different legal orientations.

On the Gaussian-root coordinate, the two ratios are `+rho` or `-rho`; hence one of `A_-`, `A_+` is divisible by `p^nu`. On the split coordinate, the two ratios are `+1` or `-1`; hence one of `B_-`, `B_+` is divisible by `p^nu`. The same statement holds with the roles reversed in the O channel.

Therefore every odd prime power of `q` occurs once in an `A` sign factor and once in a `B` sign factor. CRT gives the exact orientation-blind lock
\[
\boxed{
q^2\mid\mathcal R(x,y),
\qquad
\mathcal R(x,y):=A_-A_+B_-B_+.
}
\]
The bounded 2-adic convention remains isolated.

This is strictly different from the same-orientation lock `q|gcd(A_-,B_-)`: occupancy permits opposite orientations, so the four sign factors are essential.

## 3. Safe unconditional occupancy-energy bound

Expanding `mathfrak B_P(Q0)` gives a signed pair kernel. Ignoring signs safely, every positive pair occupancy at `q` satisfies `q^2|mathcal R(x,y)`. Since all coordinates are polynomially bounded, `mathcal R(x,y)` is polynomially bounded. For one pair,
\[
\sum_{\substack{q\le Q_0\\q^2\mid\mathcal R(x,y)}}
\frac{\lambda(q)}{\Omega(q)}B^{o(1)}
\ll Q_0B^{o(1)}.
\]
Thus the current exact structure gives only
\[
\boxed{
\mathfrak B_P(Q_0)
\ll |G(P)|^2Q_0B^{o(1)}
}
\]
after trivial pair summation. This does not certify a fixed power saving.

The desired occupancy scale remains
\[
\boxed{
\mathfrak B_P(Q_0)
\ll |G(P)|Q_0B^{o(1)}.
}
\]
No such theorem is proved in this substage.

## 4. Candidate ledger after the receiver change

### A. Orientation-blind pair-resultant square-divisor energy — LIVE / UNTESTED
Use `q^2|mathcal R(x,y)` before absolute values and prove that large square divisors of the four-factor pair resultant are rare on the reconstructed graph. This is the most direct exact receiver for occupancy bias.

### B. One-point Delta divisor incidence — LIVE / INSUFFICIENT ALONE
Every occupied `q` divides `Delta_x=m_x^4-n_x^4`. Divisor counting gives only subpolynomial choices per node, not equidistribution at a fixed `q`. No fixed `delta` follows.

### C. Interaction with `kg^2|Delta` — LIVE / INSUFFICIENT ALONE
The charged core/common-square factor and switched modulus share the host `Delta`, but no inclusion between `q` and `kg` is forced. A gcd/square-divisor decomposition may support route A, but produces no current exponent by itself.

### D. Reconstructed Pell graph — LIVE / NO AUTOMATIC OCCUPANCY SAVING
Stage15-6da removes the fourth residual support, but the remaining three-variable graph can still concentrate on divisibility conditions. `B^o(1)` completion multiplicity is not an occupancy-density theorem.

### E. Exact divisor switching — LIVE / UNTESTED FOR OCCUPANCY
The repaired cofactor involution can switch large `d,e`, but it preserves positive occupancy incidences. Without a reciprocal complementary-product average it gives no signed occupancy cancellation and no inverse `D0` power.

### F. Mixed norm / linear-factor incidence — LIVE / SUPPORTING
The channel forms and the four bilinear sign factors can be combined with norm/split factorization. This may refine the square-divisor pair energy but currently supplies no theorem.

### G. Local valuation / p=1 mod 4 support — LIVE / SUPPORTING
Odd channel primes are split primes and have bounded root multiplicity. This controls branching, not the number of occupied graph nodes.

### H. Existing Stage15-6ah / Stage14 energy inputs — ADAPTER NOT PROVED
6ah controls a different Gaussian shared-support modulus. Stage14 t76/tH21/tH22 are fixed-packet/fixed-tag inputs. No exact implication to the present orientation-blind `q^2|mathcal R(x,y)` receiver has been proved, so no exponent is transferred.

## 5. Large side and sigma

For `q>D0`, the exact positive weights remain `phi(d)phi(e)`. The facts `q|Delta_x` and `kg^2|Delta_x` do not imply an inverse power of `D0`; Rankin on `q|Delta` would require higher divisor moments and can worsen the estimate. Exact divisor switching likewise needs an independently proved complementary average.

Hence
\[
\boxed{\sigma>0\text{ remains unproved}.}
\]

## 6. Measure, quantifier and no-double-charge audit

- graph nodes are formed from exact physical survivors before modulus averaging;
- `R<=B` remains primary and `HMNUV<=B` is only its exact product-height consequence;
- `q` is charged only through channel occupancy, `kg` only through the survivor/core structure;
- `q|Delta` and `kg^2|Delta` are simultaneous facts, not permission to identify or recharge them;
- exact `phi(d)phi(e)` weights remain untouched;
- all canonical, primitive, exactly-two and direction masks remain postfilters;
- no Stage14 fixed-packet exponent is imported.

```text
STAGE15_6_SUBSTAGE=6dk
STAGE15_6DK_EXHAUSTIVE_VIEW_AUDIT=true
STAGE15_6DK_OCCUPANCY_BIAS_IS_PRIMARY_ERROR_GATE=true
STAGE15_6DK_OCCUPIED_Q_DIVIDES_DELTA=true
STAGE15_6DK_ORIENTATION_BLIND_PAIR_RESULTANT_SQUARE_LOCK=true
STAGE15_6DK_PAIR_LOCK=q^2_divides_R_pair
STAGE15_6DK_TRIVIAL_OCCUPANCY_SECOND_MOMENT=GRAPH_MASS^2*Q0*B^o(1)
STAGE15_6DK_OCCUPANCY_SQRT_TARGET_PROVED=false
STAGE15_6DK_KG2_DELTA_ALONE_SUFFICIENT=false
STAGE15_6DK_DIVISOR_SWITCH_OCCUPANCY_GAIN_PROVED=false
STAGE15_6DK_STAGE14_FIXED_PACKET_TRANSFER=false
STAGE15_6DK_SIGMA_PROVED=false
STAGE15_6DK_NEXT=BLIND_REDISCOVERY_AND_ROUTE_SELECTION
```