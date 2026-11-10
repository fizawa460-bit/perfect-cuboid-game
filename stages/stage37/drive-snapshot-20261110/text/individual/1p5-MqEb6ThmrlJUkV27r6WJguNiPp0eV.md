# M3-T11-157 — Zero-free two-prime closure certificate and physical-transfer audit

CARD_ID: M3-T11-157
CANONICAL_CARD_KEY: M3-T11-157
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-157
現行一覧の状態: PROVED_SAME_M3_SECOND_MOMENT_CERTIFICATE / PHYSICAL_CORRELATION_OPEN / GLOBAL_COUNTING_CREDIT=0
種別: CONDITIONAL GLOBAL CERTIFICATE / PHYSICAL TRANSFER AUDIT
要点: 全M3上の二素数相関の平均でP/M3閉鎖が十分。相関評価は未証明。
主張の抜粋: P/M3 <= 1/k + (2/k^2)Σ_{p<q}C_pq。固定素数集合→B極限→k極限。inert terminal zero-free。3,11は全M3自動通過。
対象・測度: Exact primitive M3, R<=B; finite-field Euler local biases are not physical equidistribution. Gate OPEN, E_bal unchanged.
依存関係: M3-DIV-001 reused; LOCAL/PARAM, Stage15 M2, PARAM-NEG-001 scope audit; written proof and exact enumeration PASS.
再開条件の抜粋: 次158: 全physical masks付きinteger divisor pq-kernelに実際の相殺定理を試す。CRT/selector/degreeの自動反復停止。
旧詳細位置: RESULT-LEDGER157; audit 1jYBJzhusn94V7S-AAYqUId8Y16id1ftQ; replay 1riZcgTUDdrJJnnD4puzk1NDmtm51ys74 / 1auHJ3IwvzE-ZUXP0eZbpWoUHL6Gwj1Hz
旧詳細リンク: https://drive.google.com/file/d/1Mi_AVVEkL-xCto-L_ZWa-8IzBCL7rbt6/view?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 28524
SOURCE_END: 42425
SOURCE_SHA256: 87ca9930e4bfe9edbcbe7a56c15d75ef6e28600fad341ad3ee95d266fedbbdbb

CURRENT AUTHORITY CONTROL — M3-T11-157 / TWO-PRIME PHYSICAL CLOSURE CERTIFICATE
PRIMARY_GATE=M3-T11-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE
ACTIVE_ROUTE_DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE
ACTIVE_RESEARCH_CARD=M3-T11-157
LATEST_RESEARCH_CARD=M3-T11-157
ACTIVE_RESEARCH_CARD_FILE_ID=1Mi_AVVEkL-xCto-L_ZWa-8IzBCL7rbt6
NEXT_RESEARCH_CARD=M3-T11-158
CURRENT_ATTACK=ExactPhysicalDivisorTwoPrimeKernelTest
GLOBAL_COUNTING_CREDIT=0
NEW_GLOBAL_OR_NEGLIGIBLE_SECTOR_BOUND=false
CANONICAL_LOCAL_GATE=M3-LOCAL-GATE-001
CANONICAL_LOCAL_GATE_STATUS=PAUSED_PENDING_PHYSICAL_TRANSFER
PHYSICAL_CORRELATION_THEOREM_FOUND_IN_INSPECTED_INPUTS=false
157_RESULT=Proved exact same-M3 second-moment sufficient certificate: P/M3 <= 1/k + (2/k^2) sum_{p<q} C_pq. Fixed prime sets precede B-limit, then k-limit. An averaged two-prime correlation estimate is enough; it is NOT proved here.
157_SCOPE=Terminal characters are zero-free for all inert primes on primitive M3. Primes 3 and 11 automatically pass for ALL M3 and give no thinning. Exact finite-field Euler local biases are not uniform selector half-density and are not physical equidistribution.
157_PHYSICAL_KERNEL=Reuse M3-DIV-001; X odd, a,b|X^2; evaluate integer quotients first; retain Y<Z, primitive, third-face square and exact T<=B^2. Required W_pq(B)/M3(B) cancellation is OPEN.
158_TASK=Attempt an actual cancellation theorem for the displayed physical two-prime divisor kernel with all masks. If no usable mechanism, record that obstruction; do not continue renamed-gate, CRT-identity or degree-ladder loops.
RETAINED=152/153 scoped results; 155 portfolio audit; 156 uniform raw-tail counterexample with restricted small-eta and endpoint-specific tails still OPEN; E_bal unresolved; TI parked;120 retracted;147-149 local curve structure only.
ARTIFACTS=card 1Mi_AVVEkL-xCto-L_ZWa-8IzBCL7rbt6; audit 1jYBJzhusn94V7S-AAYqUId8Y16id1ftQ; verification script 1riZcgTUDdrJJnnD4puzk1NDmtm51ys74; exact results 1auHJ3IwvzE-ZUXP0eZbpWoUHL6Gwj1Hz.
ARTIFACT_READBACK=All four downloaded from Drive and byte-matched to written originals.
The control above supersedes earlier authority controls below. Historical proofs and caveats are retained.


# M3-T11-157 — Zero-free two-prime closure certificate and physical-transfer audit


STATUS=PROVED_SAME_M3_SECOND_MOMENT_CERTIFICATE / PHYSICAL_CORRELATION_OPEN
AUDIT_MODE=WITHIN_SESSION_WRITTEN_PROOF_AND_EXACT_LOCAL_ENUMERATION_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0
NEW_GLOBAL_OR_NEGLIGIBLE_SECTOR_BOUND=false
PRIMARY_GATE_STATUS=OPEN
CANONICAL_GATE=M3-LOCAL-GATE-001 (same route; not a new renamed route)
NEXT=M3-T11-158 ExactPhysicalDivisorTwoPrimeKernelTest


## Decision
Latest156 asks for an actual fixed-finite-prime physical-transfer test. The test finds NO certified distribution input on exact M3 in the inspected corpus. Stage15 fixed-S asymptotics apply to M2; parameter CRT applies before the third-face square condition; PARAM-NEG-001 retracts the earlier fixed-g volume/boundary argument. None supplies the needed M3 moment.


There is nevertheless a useful exact weakening of the closure certificate: one needs only averaged TWO-prime correlations, not exponential contraction of every complete prime block, not growing-modulus uniformity, and not even one-prime mean cancellation. The standard second-moment/square-sieve argument is transcribed below on the correct physical measure. This is a sufficiency theorem and scope audit, not a proved character-sum estimate or a claim of a new sieve method.


## 1. Exact zero-free terminal character
For each primitive Euler brick E, let X be its unique odd edge and Y,Z its even edges, D^2=Y^2+Z^2 and
 T(E)=X^2+Y^2+Z^2=X^2+D^2.
T is an integer even when the physical diagonal sqrt(T) is not integral. For every inert prime p=3 mod4,
 p does NOT divide T(E).                                      (157.1)
Proof: if p|X^2+D^2, anisotropy of a sum of two squares modulo p forces p|X,D. From D^2=Y^2+Z^2 it then forces p|Y,Z, contradicting primitivity. The argument is uniform for all primitive M3, not just endpoints.
Thus chi_p(T(E)) is always +1 or -1; there is no zero-terminal stratum. Divisibility of individual edges by p is still allowed and cannot be discarded as negligible. The inert norm argument is reused elementary structure, not credited as novel.


Every endpoint has T=R^2 and hence chi_p(T)=+1 for every inert p. This is a necessary condition only.


## 2. Whole-M3 second-moment certificate
For a FIXED finite set S of k distinct inert primes, write
 C_pq(B)=M3(B)^(-1) sum_{E in M3(B)} chi_p(T(E))*chi_q(T(E)), p!=q.
Set F_S(E)=sum_{p in S} chi_p(T(E)). Every endpoint contributes k^2 to F_S(E)^2; all other contributions are nonnegative. Therefore
 P(B)/M3(B) <= 1/k + (2/k^2) sum_{p<q in S} C_pq(B).    (157.2)
Proof: k^2 P<=sum_E F_S(E)^2. Expanding the square and using(157.1), each diagonal term is exactly M3(B). No asymptotic, residue uniformity, or independence was used.


For any real weights w_p with W=sum w_p!=0 there is also the exact finite-B bound
 P/M3 <= [sum w_p^2+2sum_{p<q} w_p w_q C_pq]/W^2.       (157.3)
It follows by applying the same argument to sum w_p chi_p(T). Only fixed weights are used in the ordered-limit applications here; no uncontrolled adaptive optimization is promoted.


A sufficient global theorem is: for fixed sets S_k with |S_k|=k,
 lim_{k→infinity} limsup_{B→infinity}
 [1/k+(2/k^2)sum_{p<q in S_k} C_pq(B)] =0.             (157.4)
Then P/M3→0. All primes in S_k are fixed before taking B→infinity. No theorem uniform in a B-dependent modulus is required. A sufficient stronger version is pairwise C_pq(B)→0 for every distinct pair in an infinite inert-prime sequence. More generally only the averaged positive correlations need decay; exact zero for every fixed pair is unnecessary.


One-prime marginals alone cannot establish(157.4): an abstract population with probability1/2 at the all-plus sign vector and1/2 at all-minus has zero marginal means, pair correlations1, and all-plus mass1/2 at every k. This is a logical countermodel to inferring joint contraction from marginals, not a construction of actual Euler bricks.


The original rho^k full-block contraction remains a sufficient theorem. It is stronger than what is needed for this particular closure mechanism. We do NOT claim(157.4) implies exponential block contraction, or that the certificates are mathematically equivalent.


## 3. Automatic primes and the local measure
At p=3, the nonzero squares are {1}; two nonzero edges would have a face norm2, a nonsquare. Thus at most one edge is nonzero modulo3, and chi_3(T)=1 on every primitive M3 object.
At p=11, nonzero square values are {1,3,4,5,9}. Two such values can have square sum exactly along the five-cycle
 1—3—9—5—4—1.
There are no loops because2 is a nonsquare, and no triangles. Hence three nonzero edge squares cannot have all pair sums square: every Euler brick has an edge divisible by11. With that edge zero modulo11, T is an existing face square and is nonzero by(157.1). Consequently
 chi_11(T)=1 on ALL primitive M3.                       (157.5)
These primes supply no terminal selection. Small-prime divisibility facts are treated as elementary reused/scoped checks, not a literature-wide discovery. A theorem claiming zero character means at EVERY inert prime is false; sufficiently good selected primes may omit3 and11. No claim is made that these are the only automatic primes.


The exact half-set size |Omega_p|=(p+1)/2 is on uniform P1(Fp). It is NOT the same as conditional uniform Euler/K3 reduction. We checked the latter explicitly as a CANDIDATE local model:
 normalize the first nonzero edge coordinate to1;
 sum over edge residues (a,b,c);
 w_p(a,b,c)=product_{pairs}(1+chi_p(a_i^2+a_j^2)).
This is the exact number of face-root lifts in the projective six-coordinate Euler model. Put Z_p=sum w_p and A_p=sum w_p chi_p(a^2+b^2+c^2), delta_p=A_p/Z_p.


| p | Z_p | A_p | delta_p |
|---|---:|---:|---|
|3|12|12|1|
|7|92|28|7/23|
|11|108|108|1|
|19|396|12|1/33|
|23|668|92|23/167|


For example, in this finite model the terminal pass fraction at7 is15/23, not1/2; at11 it is1. The projective selector half-set formula is retained; only a mistaken identification of measures is excluded.
These finite field values are exact exhaustive certificates at the displayed primes. They are NOT measurements or asymptotics of M3(B), do not prove equidistribution, and are not used to extrapolate delta_p→0.
Uniform finite CRT product models have pair means delta_p delta_q, not necessarily0. Thus even if an eventual physical transfer matches this model, demanding EXACT zero for each fixed pair can be too strong. A valid bias-aware statement C_pq=delta_p delta_q+o(1), coupled with proved Cesaro-small biases, would suffice for(157.4). Neither physical transfer nor the infinite-prime bias theorem is established here.


## 4. A concrete integer kernel preserving the physical masks
Reuse M3-DIV-001. For positive odd X, choose divisors a,b of X^2 with0<a,b<X and define
 Y=(X^2/a-a)/2, Z=(X^2/b-b)/2.
Retain Y<Z, gcd(X,Y,Z)=1, Y^2+Z^2=square, and T<=B^2. The two X-face squares are automatic, while the remaining third-face square is an essential mask. The unique odd edge and ordering of even edges give multiplicity one for the canonical M3 object, independent of where X falls in sorted physical order.
Let
 K(X,a,b)=4X^2+(X^2/a-a)^2+(X^2/b-b)^2=4T.             (157.6)
The quotients X^2/a and X^2/b are evaluated as INTEGERS before reduction; do not invert a or b modulo a prime, since they may be divisible by it.


For m=pq, p!=q inert, the exact required numerator in(157.2) is
 W_m(B)=sum_{odd X,a,b|X^2, ALL physical masks above} chi_m(K(X,a,b)),
 C_pq(B)=W_pq(B)/M3(B).                                (157.7)
Here chi_m is the Jacobi product chi_p chi_q and chi_m(4)=1. This adapter has no fixed-power loss and preserves the denominator, cutoff, primitive/canonical weighting and square locus. The divisor encoding itself is reused, not new counting credit.


The obstacle is now explicit: obtain cancellation for(157.7) on the physical THIRD-FACE-SQUARE locus. Ambient complete sums or ordinary divisor correlations before that mask do not evaluate this numerator. Boundary estimates for a continuous parameter region alone do not resolve the square mask. The old corrected-frozen Davenport argument cannot be cited.


## 5. Available-input audit and actual budget
- M3-LOCAL-001 / PARAM-001/002: exact local/ambient CRT laws, no M3 physical transfer.
- M3-LOCAL-GATE-002/003 and TERM-GATE-002: remain theorem gates; prime means alone do not supply the off-diagonal pq sums in(157.2).
- HIST15-FIXEDS-001: certified M2 ordered-limit law; its proof architecture is reusable, its count is on a different measure.
- S20-W03: controls third-face completion on the two-face toric host; it does not supply terminal correlations conditional on having completed M3. Do not multiply its existing sieve cost by a terminal half-density.
- PARAM-NEG-001: earlier fixed-g volume model omitted gcd-divisibility density and was retracted; no certified replacement was located.
These are targeted Drive-source findings, not a claim that no theorem exists anywhere.


A sufficient absolute substitute is W_pq=o(B^(1/3)), using the retained M3 lower bound. Relative W_pq=o(M3) or the averaged form(157.4) is enough and can be weaker. An absolute generic square-root bound O(B^(1/2)) does not certify this relative target against the presently available lower bound. Likewise, fixed local constants cannot close by multiplying the existing half-power P bound.


Feasibility verdict: global connection PASS as a conditional second-moment implication; certified physical-distribution input NOT FOUND; LOCAL route remains PAUSED at the same canonical gate. No global or new negligible-sector estimate is proved. This card is the completed preflight requested by156, not authorization for an infinite sequence of character-identity cards.


## 6. Next legal research and persistence
Next158 should attempt one concrete theorem/proof match for(157.7), with fixed modulus pq and full physical masks, including summation over odd X and both divisor partners. If no actual cancellation mechanism or valid transfer is obtained, record the blockage and do not issue another renamed-gate/CRT/local-law progress card. Full higher-order block enumeration is unnecessary for(157.2), and one-prime marginals are insufficient.
Retain152/153,155 identities,156 raw-tail obstruction and its restricted-threshold firewall. TI parked,120 retracted,147–149 scoped curves retained; automatic degree and witness-prime escalation paused. E_bal unresolved; gateOPEN; credit0.


## Provenance and replay
Current native MAIN/INDEX/LEDGER/activeROUTE read through156; LOCAL route and ledger entries LOCAL001/GATE001-003, TERM-GATE002, PARAM-NEG001, HIST15-FIXEDS001, HIST20-W03 checked. Stage20 Arsenal source file1Hp3OQpJ9GEZ515voUaRIOuzep78ILpwa.
The standard second-moment/Cauchy method and odd-edge divisor dictionary are reused. The contribution here is their zero-free, whole-M3 ordered-limit certificate, explicit bias-aware measure audit, and exact physical pq kernel. No general novelty or external hostile audit is claimed.
verify157.py enumerates normalized projective Euler residues at14 inert primes (3 through103, selected list), checks terminal nonvanishing, finite biases/CRT moments, the marginal countermodel, and integer-kernel recovery for3 known primitive Euler bricks. Exact enumeration proves only those finite-model results; the written arguments prove(157.1)–(157.3)/(157.5)/(157.6). The required physical correlation theorem is explicitly unproved.
GLOBAL_FIXED_POWER_SAVING=false; PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false.




END M3-T11-157 WRITTEN RESEARCH CARD — earlier record follows
