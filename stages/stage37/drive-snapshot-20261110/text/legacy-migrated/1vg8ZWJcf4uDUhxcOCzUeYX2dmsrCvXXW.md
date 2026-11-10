# M3-T11-159 — Candidate③: endpoint-conditioned Fourier saturation and coefficient block-rank cost

STATUS=PROVED_SCOPED_COEFFICIENT_FEASIBILITY_CERTIFICATES / CANDIDATE_III_NOT_EXHAUSTED
PRIMARY_GATE_STATUS=OPEN
GLOBAL_COUNTING_CREDIT=0
NEW_GLOBAL_OR_NEGLIGIBLE_SECTOR_BOUND=false
AUDIT_MODE=WITHIN_SESSION_WRITTEN_PROOF_AND_FINITE_ALGEBRA_REPLAY_NOT_EXTERNAL_AUDIT
NEXT_CANDIDATE=M3-T11-160: candidate③, unconditioned physical host and block-energy budget test

## Authority and question answered
Fresh MAIN / INDEX / RESULT-LEDGER / active T11 ROUTE all designate158. User explicitly selects③ of155's portfolio. We read the original T11-024 paired-Gaussian receiver,026 Section27 Fourier coefficient,027 Section28.5 relaxed four-core separation, and031 Section31.6 moving-support firewall. No historical degree ladder is resumed. Goal remains P(B)/M3(B)->0, with original primitive/canonical/positive/physical-height/common-parent/allocation masks and one endpoint one count.

③ contains several distinct receivers, not one already-applicable analytic theorem. This card tests026's literal endpoint coefficient. It proves an exact necessary separation-cost certificate, including approximate separation. It does not supply physical coefficient sparsity or a new endpoint-count saving. It neither exhausts③ nor invalidates026's Fourier/Gauss identities.

## 1. Coefficient population must be stated before invoking cancellation
Let A=Z[i]/M, q=|A|, M the odd fresh oriented squared ideal of026. Fix a content/coefficient packet and this endogenous modulus. Write Q(X,U,V)=X²+αU²+βV², with α,β units. The physical residue weight has nonnegative integer multiplicities; all its parent masks remain.

There are TWO weights to distinguish:
* W_end: pushforward of packets already satisfying the endpoint condition. Then supp(W_end)⊂{Q=0}.
* W_pre: a precisely specified candidate population before imposing this endpoint congruence. For such a host,026's indicator actually filters points. It requires a separate counting and coefficient budget.

Section27 calls its coefficient the physical active-tau packet; the canonical026 ledger population explicitly says endpoint packets. Its identity is valid under either interpretation.159's saturation and block-rank statements apply to W_end, or any weight supported on Q=0, NOT automatically to W_pre. Section28.5 already distinguishes the pre-selector relaxed host and proves product separation there; it also warns that dropping the principal-incidence thinning makes the exponent insufficient.159 does not rebrand that known relaxation as a new result.

Put N=sum W_end. For every additive frequency h∈A,

 A_h=sum W_end(X,U,V) ψ(hQ(X,U,V))=N.                 (159.1)

Indeed Q=0 on every occupied triple. Hence the exact orthogonality decomposition is

 S=N=(1/q)sum_h A_h=N/q+(1-1/q)N.                  (159.2)

All nonzero frequencies restore the mass removed by the principal term. A claim of |sum_{h≠0}A_h|=o(qN) relative to this already-selected population would contradict(159.2), unless it is empty. Neither q^-1 nor an auxiliary half-density can be multiplied into a previous endpoint bound. This does NOT forbid an analytic absolute bound for N from genuinely independent coefficient information; it forbids obtaining relative thinning just by reapplying its own selector.

## 2. Exact block-rank theorem for the ACTUAL endpoint coefficient
Fix X. Form the matrix T_X(U,V)=W_end(X,U,V), padded by zeros outside the physical unit support. For a∈A, collect all rows with U²=a. Their possible nonzero columns obey

 V²=b(a):=β^-1(-X²-αa).

Because α and β are units, b is injective in a. Different occupied a therefore use disjoint column sets. After row/column permutations, T_X is a direct sum of nonempty blocks T_{X,a}, one for each occupied residue-square VALUE a. This is not a global rational squareclass partition.

Let K_X be the number of these blocks and R_X the number of nonzero rows. Then exactly

 rank_C(T_X)=sum_a rank_C(T_{X,a}) ≥ K_X.            (159.3)

Any exact representation T_X(U,V)=sum_{l=1}^J f_l(U)g_l(V) has rank≤J, so J≥K_X. This retains every actual physical mask; weights within a block may be arbitrary and no uniform-residue measure is substituted.

For026's fresh Gaussian ideal, each rational split prime supplies one oriented prime-power factor. Over each odd local factor a unit square has at most2 roots: if u²=v² and both are units, (u-v)(u+v)=0 in the local ring and 2u is a unit, so one factor is a unit and the other is zero. CRT gives at most D=2^{ω(q)} roots. Thus R_X≤D K_X and

 J≥K_X≥R_X/D.                                      (159.4)

On the polynomial physical modulus range D=B^{o(1)}. This last elementary divisor estimate changes no moving-support count. No lower bound for actual R_X or K_X has been proved here, so(159.4) is a necessary cost, not proof that the actual coefficient has polynomial rank.

## 3. Approximate separation also has a physical energy cost
Let E_{X,a}=||T_{X,a}||_F², E_X=sum_a E_{X,a}, and order block energies nonincreasingly as E_X^(1),E_X^(2),.... For ANY matrix L_X of rank≤J,

 ||T_X-L_X||_F² ≥ E_X-sum_{j≤J}E_X^(j).             (159.5)

Proof: a direct-sum matrix has the union of the blocks' singular values. Its optimal rank-J approximation removes the J largest squared singular values. They belong to at most J blocks, whose entire energy is at most the sum of the J largest block energies. Every other block's energy remains. This also covers zero blocks and J≥K_X.

Consequently a B^{o(1)}-term approximate product adapter with small relative L2 error needs energy concentrated in B^{o(1)} occupied blocks. Parseval does not establish this concentration. The rigorous proof concerns arbitrary weights on the actual shell, not an assumption that physical packets occupy many blocks.

For a full tensor approximation L(X,U,V)=sum_{l≤J}a_l(X)b_l(U)c_l(V), each X slice has rank≤J, giving the summed bound

 ||W_end-L||_2² ≥ sum_X [E_X-sum_{j≤J}E_X^(j)].      (159.6)

Fourier transforms in U,V are invertible row/column operations, preserving rank. A separated full Fourier tensor in X,U,V inverse-transforms to a tensor of the same product length. With026's normalized c=q^-3 Fourier(W), Parseval gives ||c-c_L||_2²=q^-3||W-L||_2², so completion cannot eliminate this approximation cost by changing coordinates.

Scope: these results test exact or approximate products of ONE-VARIABLE sequences. They do not rule out theorem-compatible bilinear forms with a legitimate multivariable coefficient, cancellation across moving moduli, an unconditioned host, or a different centering argument. Any such receiver must state its own admissible coefficient and norm/range hypotheses.

## 4. What this changes for③
| Existing receiver |159 outcome | Still needed |
|---|---|---|
|026 endpoint-conditioned Fourier coefficient | Exact saturation; block-rank and approximation-energy costs proved | Actual K_X/energy control or independently budgeted pre-endpoint host; endogenous modulus theorem match |
|027 relaxed pre-selector product host | Known exact separation retained, not new | Enough retained principal-incidence thinning to meet target |
|024 paired Gaussian | O(1) reconstruction and tH3/4/5/14 residue cleanup retained | Global principal rational selector class incidence |
|M3-A-001 whole directional centered correlation | Not evaluated by this card | Actual whole-measure correlation estimate at sufficient rate |
|TQ-GATE-002 first-cover H energy | Not evaluated by this card | Q_H=o(B^(2/3)) on its original first-cover population; not terminal energy of158 |

There is no justification to mark③ complete or hopeless. There is justification to stop treating026's Parseval identity as a cost-free B^{o(1)} coefficient decomposition. Section31's existing fixed-modulus/moving-support distinction is retained;159 adds coefficient rank and approximation-energy certificates, not another pointwise CRT root count.

## 5. Global budget and next concrete decision
Per-content active-tau B^(1/12-δ) would still need the complete content/coefficient/cyclic-family sum.159 proves no such bound, no residual-population saving, and no improvement on E_bal.152/153 sector theorems and155–158 results remain unchanged;120 retracted, TI parked,147–149 local structural results frozen.

Next160 should remain within③: select an ACTUAL pre-endpoint physical host, identify exactly which selector has been removed, and quantify its total mass, occupied-block energy, reconstruction multiplicity, modulus dependence, and full content/family budget. If it is only Section28.5's enlarged product box, record the already-known exponent failure and stop that branch. No new card should merely rename the missing estimate or add more frequencies. An alternative③ receiver is TQ-GATE-002's pre-H-square first-cover population, whose physical selection order is explicit. Its energy must not be identified with158 terminal energy without a proved adapter. Only after these distinct receivers are assessed should the portfolio's other routes be ranked again.

## 6. Verification and limitations
The written proof applies to arbitrary q and weights under its stated unit and shell hypotheses. verify159.py replays20 finite algebra models at q=13,17,25,65,169, both full unit and square-unit restrictions, flat and masked integer weights. It checks exact rational matrix rank, shell-frequency saturation, and singular-value approximation inequalities. These are algebra models, NOT actual physical endpoints, NOT an asymptotic census, and NOT evidence of global density. Replay results are in verify159-result.json. Audit is within this session, not external independent review.

PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
GLOBAL_FIXED_POWER_SAVING=false
CANDIDATE_III_EXHAUSTED=false
M3_T11_ENDPOINT_FREQUENCY_SATURATION_PROVED=true
M3_T11_PHYSICAL_SHELL_BLOCK_RANK_COST_PROVED=true
M3_T11_PHYSICAL_SHELL_APPROXIMATION_ENERGY_COST_PROVED=true
M3_T11_ACTUAL_BLOCK_COUNT_OR_CONCENTRATION_ESTIMATE_PROVED=false
