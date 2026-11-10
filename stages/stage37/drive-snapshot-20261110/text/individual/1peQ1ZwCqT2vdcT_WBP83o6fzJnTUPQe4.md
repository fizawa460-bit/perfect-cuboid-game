# M3-T11-155 — Same-witness gluing and squarefree local-to-global equivalence audit

CARD_ID: M3-T11-155
CANONICAL_CARD_KEY: M3-T11-155
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-155
現行一覧の状態: PROVED_EXACT_GLUING_AND_SQUAREFREE_CRT_EQUIVALENCE / NO_NEW_COUNTING_SAVING / GLOBAL_COUNTING_CREDIT=0
種別: SAME-WITNESS GLUING / ALL-SQUAREFREE CRT EQUIVALENCE / MECHANISM DECISION
要点: 同じendpointの条件を入れるだけで総和が減るかを監査。任意cofactor・任意指数の共有edge gluingを厳密化。
主張の抜粋: R=p^n q^m hのcompatible shared-unit pairはsigned8D(h)、positive-real4D(h)。全squarefree split Rでは、同一global H_iから作る全primeのpi_p^2|C_pが、正値・原始・odd edge1本の下でsum e_i^2=R^2と同値。任意prime support数を一括扱う。
対象・測度: 重複witnessの整理は151のglobal allocationに既に含まれる。新しいnegligible sector/global upper boundなし。nonsquarefreeはrad(R)^2の整除まで。E_bal全体未解決。
依存関係: 151 Gaussian identity;152 allocation envelope;153 positivity and reconstruction;154 shared-edge equality。155 written proofs＋6gluing/5583triple replay PASS。
再開条件の抜粋: 次156：GlobalAdditiveSphereBudgetSelection。exact sparse-circle Fourier coefficient＋primitive Mobius adapter、または強いdenominator評価の具体的入力を総和budgetで比較。compatibilityだけの自動反復は停止。
旧詳細位置: RESULT-LEDGER155; audit 11U7kh0HHVwBRiSUQwzjWN2SY389TvwKi; replay 1z0R7fLMJVdVVWWhNYOTznV118FZL2LlO / 1eRZrrmKm9axQAMW_dZk_uKeXtwlrt0nP
旧詳細リンク: https://drive.google.com/file/d/15kbKOVjtJIuLNQWhCH-P8KYmBZLiTdyh/view?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 54591
SOURCE_END: 68974
SOURCE_SHA256: eeeaa1b5171dfe0518a1031abf4e0d2db45d083779c6c220ee62be22894f5fa4

CURRENT AUTHORITY CONTROL — M3-T11-155 / SAME-WITNESS MECHANISM DECISION
PRIMARY_GATE=M3-T11-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE
ACTIVE_ROUTE_DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE
ACTIVE_RESEARCH_CARD=M3-T11-155
ACTIVE_RESEARCH_CARD_FILE_ID=15kbKOVjtJIuLNQWhCH-P8KYmBZLiTdyh
LATEST_RESEARCH_CARD=M3-T11-155
LATEST_AUDITED_RESEARCH_CARD=M3-T11-155
LATEST_CARD_STATUS=PROVED_EXACT_GLUING_AND_SQUAREFREE_CRT_EQUIVALENCE
LATEST_AUDIT_MODE=WITHIN_SESSION_PROOF_REDERIVATION_AND_EXACT_REPLAY_NOT_EXTERNAL
LATEST_AUDIT_FILE_ID=11U7kh0HHVwBRiSUQwzjWN2SY389TvwKi
LATEST_VERIFICATION_SCRIPT_FILE_ID=1z0R7fLMJVdVVWWhNYOTznV118FZL2LlO
LATEST_VERIFICATION_JSON_FILE_ID=1eRZrrmKm9axQAMW_dZk_uKeXtwlrt0nP
ARTIFACT_READBACK=All four saved artifacts read back exactly; script/JSON raw bytes matched.
NEXT_RESEARCH_CARD_ID=M3-T11-156
CURRENT_ATTACK=GlobalAdditiveSphereBudgetSelection
RESULT_155_GLUING=For R=p^n q^m h, gcd(pq,h)=1, compatible shared-unit edge witnesses have exactly8D(h) signed oriented pairs or4D(h) positive-real pairs, uniformly in n,m and h. Global H allocation already incorporates this compression.
RESULT_155_SQUAREFREE=For ALL squarefree split R and positive primitive circle triples with exactly one odd edge, the full Gaussian test pi_p^2|C_p at every p|R is equivalent to the original sum e_i^2=R^2. This covers arbitrary support size; it is not a density estimate.
RESULT_155_REPEATED_POWERS=For nonsquarefree R the elementary tests yield only rad(R)^2|F, not R^2|F; no closure is inferred.
RESULT_155_GLOBAL_ADAPTER=Exact positive labelled primitive count is a Mobius-weighted Fourier coefficient of the sparse norm-circle exponential polynomial. No cancellation bound has been established.
MECHANISM_DECISION=STOP_AUTOMATIC_SAME_WITNESS_CRT_BOOTSTRAP_AS_NEW_COUNTING_METHOD. Gluing identities alone are not authorization to keep adding prime cases or renamed receivers.
NEXT_LEGAL_ACTION=156 must select a concrete analytic/additive estimate on the exact global circle population, or a stronger denominator input, and test its WHOLE E_bal budget before detailed work. If no input beats the present budget, record blockage; do not issue another compatibility-only progress card.
PHYSICAL_RESIDUAL=E_bal from153 remains: some prime outside152 S_B; R/p^v_p(R)>Y_B for every p|R; Y_B=B^(1/3)/(1+log B)^30.
RETAINED_152_153=true; sector theorems unchanged.
NEW_GLOBAL_OR_NEGLIGIBLE_SECTOR_BOUND=false
GLOBAL_COUNTING_CREDIT=0
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
TI=parked;120=retracted;147-149=retained within scope;automatic curve-degree escalation=paused.
AUDIT_SCOPE=Uniform identities and inference scope PASS; no external hostile audit or global closure.
CLOSURE_FORECAST=No basis for claiming closure within a few cards.
READ_ORDER=This155 control;155 card/audit/replay by IDs above;153 residual definition and154 certificate barriers. Prior snapshots below are historical.


M3-T11-155 — Same-witness gluing and squarefree local-to-global equivalence audit


STATUS=PROVED_EXACT_GLUING_AND_SQUAREFREE_CRT_EQUIVALENCE
DECISION=NO_NEW_COUNTING_SAVING_STOP_AUTOMATIC_WITNESS_BOOTSTRAP
AUDIT_MODE=WITHIN_SESSION_PROOF_REDERIVATION_AND_EXACT_REPLAY_NOT_EXTERNAL
NEW_GLOBAL_OR_NEGLIGIBLE_SECTOR_BOUND=false
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
NEXT=M3-T11-156 GlobalAdditiveSphereBudgetSelection


Starting authority and the test


Fresh MAIN, INDEX, RESULT-LEDGER and active T11 ROUTE all designate154. Its complete card is the current source for the missing same-witness correlation gate.152 and153 remain valid sector theorems. The exact unresolved population is E_bal: primitive canonical positive endpoints at R<=B, some prime outside152's S_B, and R/p^v_p(R)>Y_B for every p|R, with Y_B=B^(1/3)/(1+log B)^30.


155 tests whether enforcing154's shared-edge equality itself supplies a quantitative saving beyond151's original joint Gaussian receiver. It proves an exact gluing formula for arbitrary exponents and cofactors, and an exact equivalence for ALL squarefree split R, with arbitrarily many prime factors. The answer is that compatibility removes independently duplicated witness choices, but the completed local tests reproduce the original sphere equation. No new global or negligible-sector estimate follows. This is not an impossibility theorem for using these representations with a genuinely new analytic estimate.


1. Exact shared-edge gluing, uniformly in the cofactor


Write R=p^n q^m h, p!=q split odd primes, gcd(pq,h)=1, n,m>=1, and all primes of h split. Fix Gaussian primes pi,rho above p,q. Set A=bar(pi)^(2n), D=bar(rho)^(2m), and D(h)=product_(l^a||h)(2a+1). A local p-oriented edge has H_p=A G, Norm(G)=(q^m h)^2; a q-oriented edge has H_q=D L, Norm(L)=(p^n h)^2. The edge is a unit at BOTH p and q.


Same positive edge and complementary-diagonal magnitude means H_p=H_q or H_p=bar(H_q). These pairs have the following complete parametrization:


 H_p=H_q:       G=D K,       L=A K;
 H_p=bar(H_q):  G=bar(D) K,  L=bar(A) bar(K);
 Norm(K)=h^2.                                                (155.1)


Proof: A and D are coprime in Z[i]. In the first equality A G=D L, unique factorization forces D|G and A|L. In the second equality A G=bar(D) bar(L), it forces bar(D)|G and A|bar(L). Substitution gives the displayed K and its norm. Conversely every such K satisfies the required equality and norms. Its p/q valuations are automatically zero because gcd(h,pq)=1.


The two branches are disjoint. Otherwise the common H_q would be real, whereas its q-valuations are0 and2m, impossible for a nonzero real Gaussian integer. Norm(h)>0 excludes zero. The shared H also cannot have zero real part, since a pure imaginary integer has equal valuations at a Gaussian prime and its conjugate.


There are4D(h) Gaussian integers K of norm h^2. Thus the EXACT number of signed oriented pairs is8D(h), and imposing positive common real part leaves4D(h), by the fixed-point-free K->-K involution. This counts oriented representations of one edge, not cuboid endpoints or canonical triples. For h=1 there are8 signed pairs and4 with positive real part, regardless of p,q,n,m.


This replaces the false independent product (8D(h))^2 of two shared-unit cofactor lists by8D(h). It is a genuine removal of duplicate choices. However151 already encodes a triple using a SINGLE global H_i per edge. Those original allocations already contain this compatibility. Since D(h)=h^o(1), the displayed compression supplies no new fixed power of R compared with that original receiver. No such asymptotic estimate is imported as a theorem needed for the gluing proof; the standard divisor-size observation is only explanatory.


2. All squarefree split diagonals: full Gaussian local tests equal the sphere gate


Let R be ANY odd squarefree product of split primes. Select three pairs H_i=e_i+i f_i with positive integer e_i,f_i, Norm(H_i)=R^2, gcd(e_1,e_2,e_3)=1, and exactly ONE odd e_i. These are the original edge/complementary-face circles, before imposing the sphere equation. Any original physical endpoint satisfies these conditions. Define


 F=sum_i(H_i^2+bar(H_i)^2)+2R^2
  =4(sum_i e_i^2-R^2).                                    (155.2)


For p|R choose pi above p. Let I_p={i:p does not divide e_i}. For each i in I_p orient H_i by independently conjugating it so that H_i'=bar(pi)^2 G_i^(p), and put C_p=sum_(i in I_p)(G_i^(p))^2. This orientation exists: if p does not divide e_i, one of the two Gaussian valuations of H_i is0 and the other2. All terms H_i^2+bar(H_i)^2 are unchanged by the conjugations.


The FULL local Gaussian condition obeys


 pi^2 | C_p  iff  pi^2 | F  iff  p^2 | F.                 (155.3)


To see this, modulo pi^2 the conjugates of the oriented unit edges vanish, leaving bar(pi)^4 C_p. For i outside I_p, p divides both e_i and f_i: the norm equation implies p|f_i, so H_i and its conjugate are each divisible by pi and their squares vanish modulo pi^2. Also pi^2|R^2. The factor bar(pi)^4 is invertible modulo pi^2. Finally F is an ordinary integer, so conjugation converts pi^2|F to bar(pi)^2|F, and together these imply p^2|F. This reasoning also handles |I_p|=1; such a tuple cannot pass the local test, because its lone G is a pi-unit.


Taking ALL p|R, squarefreeness and the Chinese remainder theorem yield R^2|F, equivalently R^2|sum e_i^2. Since 0<e_i<R, this sum is strictly between0 and3R^2. Its quotient by R^2 is therefore1 or2. Exactly one odd edge gives sum e_i^2=1 modulo4, while R^2=1 modulo4; quotient2 is impossible. Consequently


 [pi_p^2|C_p for EVERY p|R]  iff  sum_i e_i^2=R^2.       (155.4)


The reverse implication is immediate from F=0 and(155.3). After(155.4), primitivity forces |I_p| in {2,3}, and the positive-edge argument retained in153 gives C_p!=0. Thus requiring these two extra witness filters does not change the equivalence.


Equation(155.4) covers ALL squarefree support sizes at once. It demonstrates why multiplying local probabilities is unjustified here: once the local witnesses reconstruct the same global H_i, demanding all the exact tests is precisely the original physical sphere equation. It does not prove those solutions are frequent, rare, or absent. The weaker integer condition p^2|Norm(C_p) used for candidate upper bounds in153/154 is NOT substituted for the full Gaussian condition.


For nonsquarefree R the same modulo-pi^2 argument still supplies p^2|F, but only rad(R)^2|F after gluing. It does not give R^2|F. Hence(155.4) is not silently extended to repeated-prime-power diagonals. Those remain part of E_bal and still require a bound.


3. What the total budget actually says


Let D(R)=product_(p^a||R)(2a+1). There are4D(R) signed Gaussian circle points per edge. Global triples before the sphere filter therefore cost at most64D(R)^3, exactly the old151/152 allocation envelope. Gluing local orientations into one global triple pays this envelope once; it does not replace it by a proved smaller count of successful sphere triples.


155 provides neither sum_(R<=B,R in E_bal) J(R)=o(M3(B)) nor a negligible new physical sector.154's scalar alphabet-cover obstruction is untouched. Its O(B^(1/2)/log B) balanced semiprime upper budget has not been improved. The prime directions must be consistent, but mere consistency is not a new sparse-population theorem.


Decision: the elementary same-witness/CRT bootstrap FAILS AS A NEW COUNTING MECHANISM. Stop generating successive cards that only add more compatible primes or rewrite the same joint receiver.152/153 remain retained;154's firewalls remain retained; global credit stays0 and the main gate staysOPEN. A future estimate of the already-glued sphere population would reopen this mechanism, but another gluing identity alone does not.


4. Concrete alternative: test additive counting on the exact circle population


For odd split R and d|R define the finite exponential polynomial


 A_(R,d)(theta)=sum_(0<e<R, R^2-e^2=f^2 with f>0, d|e)
                    exp(2*pi*i*e^2*theta).


Orthogonality gives the exact labelled primitive positive cuboid count


 N_prim(R)=sum_(d|R) mu(d) integral_0^1
               exp(-2*pi*i*R^2*theta) A_(R,d)(theta)^3 dtheta. (155.5)


Proof: the integral selects precisely sum e_i^2=R^2 with positive integer complementary diagonals. Each e has one positive f. On such a triple any common divisor g of the edges divides R because g^2 divides R^2; it also divides every f_i. The sum of mu(d) over common divisors d|R of all edges is1 exactly for primitive triples, and0 otherwise. Thus the formula preserves primitivity rather than quietly counting scaled copies. Original canonical masks select a subpopulation, so their physical count is at most N_prim(R). One may retain those masks explicitly for an equality on the original population.


This formula is an EXACT ADAPTER, not a new bound and not a claim of novelty. Dropping phases or taking only absolute-value/divisor bounds returns the old envelope. A useful next study must identify cancellation, additive structure, or a separate stronger denominator estimate that changes the TOTAL exponent on the exact moving-R population. Generic random residues or parameter-side CRT estimates cannot be transferred without a theorem on these sparse circles and their endogenous R.


NEXT156=GlobalAdditiveSphereBudgetSelection: compare actual available bounds for(155.5), and the retained denominator's possible strengthening, against the whole-E_bal budget BEFORE constructing another receiver. PASS requires a concrete theorem and a valid adapter whose total cost improves the present bound toward o(M3), including moving R, primitivity and all residual support types. If no such input exists, record that these candidate mechanisms are presently blocked; do not proceed to infinite case classification. No promise of closure within a few cards is warranted.


Audit, dedupe and replay


Sources: current154 card and current native MAIN/INDEX/LEDGER/ROUTE;151 Gaussian identity;152 allocation envelope;153 reconstruction and positive C!=0 argument. Targeted ledger review found historical CRT statements on parameter and Stage14 populations, but none is imported onto the present circle measure.154's shared-edge equality is the starting point, not claimed as new. New here are its exact arbitrary-cofactor gluing count and the explicit whole-squarefree support equivalence(155.4), used to terminate an unproductive elementary bootstrap. No literature-wide novelty or external hostile audit is claimed.


verify155.py independently enumerates Gaussian norm circles, compares the complete pair list with both gluing branches, and checks every selected triple's Gaussian divisibility against the real integer defect and the sphere predicate. Six gluing cases and5583 squarefree triples, including2-,3-prime and r=2/r=3 branches, pass. Finite absence of cuboids in those checks is not used for any universal nonexistence claim. The written proofs provide the uniform statements.


TI remains parked,120 remains retracted,147–149 remain retained within scope, automatic degree escalation remains paused. GLOBAL_FIXED_POWER_SAVING=false; PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false.




HISTORICAL AUTHORITY SNAPSHOTS — latest control above supersedes the following prior heads.

## Retained standalone source — M3-T11-155-research-card.md
SOURCE_FILE_ID: 15kbKOVjtJIuLNQWhCH-P8KYmBZLiTdyh
SOURCE_URL: https://drive.google.com/file/d/15kbKOVjtJIuLNQWhCH-P8KYmBZLiTdyh/view?usp=drivesdk

# M3-T11-155 — Same-witness gluing and squarefree local-to-global equivalence audit

STATUS=PROVED_EXACT_GLUING_AND_SQUAREFREE_CRT_EQUIVALENCE
DECISION=NO_NEW_COUNTING_SAVING_STOP_AUTOMATIC_WITNESS_BOOTSTRAP
AUDIT_MODE=WITHIN_SESSION_PROOF_REDERIVATION_AND_EXACT_REPLAY_NOT_EXTERNAL
NEW_GLOBAL_OR_NEGLIGIBLE_SECTOR_BOUND=false
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
NEXT=M3-T11-156 GlobalAdditiveSphereBudgetSelection

## Starting authority and the test

Fresh MAIN, INDEX, RESULT-LEDGER and active T11 ROUTE all designate154. Its complete card is the current source for the missing same-witness correlation gate.152 and153 remain valid sector theorems. The exact unresolved population is E_bal: primitive canonical positive endpoints at R<=B, some prime outside152's S_B, and R/p^v_p(R)>Y_B for every p|R, with Y_B=B^(1/3)/(1+log B)^30.

155 tests whether enforcing154's shared-edge equality itself supplies a quantitative saving beyond151's original joint Gaussian receiver. It proves an exact gluing formula for arbitrary exponents and cofactors, and an exact equivalence for ALL squarefree split R, with arbitrarily many prime factors. The answer is that compatibility removes independently duplicated witness choices, but the completed local tests reproduce the original sphere equation. No new global or negligible-sector estimate follows. This is not an impossibility theorem for using these representations with a genuinely new analytic estimate.

## 1. Exact shared-edge gluing, uniformly in the cofactor

Write R=p^n q^m h, p!=q split odd primes, gcd(pq,h)=1, n,m>=1, and all primes of h split. Fix Gaussian primes pi,rho above p,q. Set A=bar(pi)^(2n), D=bar(rho)^(2m), and D(h)=product_(l^a||h)(2a+1). A local p-oriented edge has H_p=A G, Norm(G)=(q^m h)^2; a q-oriented edge has H_q=D L, Norm(L)=(p^n h)^2. The edge is a unit at BOTH p and q.

Same positive edge and complementary-diagonal magnitude means H_p=H_q or H_p=bar(H_q). These pairs have the following complete parametrization:

 H_p=H_q:       G=D K,       L=A K;
 H_p=bar(H_q):  G=bar(D) K,  L=bar(A) bar(K);
 Norm(K)=h^2.                                                (155.1)

Proof: A and D are coprime in Z[i]. In the first equality A G=D L, unique factorization forces D|G and A|L. In the second equality A G=bar(D) bar(L), it forces bar(D)|G and A|bar(L). Substitution gives the displayed K and its norm. Conversely every such K satisfies the required equality and norms. Its p/q valuations are automatically zero because gcd(h,pq)=1.

The two branches are disjoint. Otherwise the common H_q would be real, whereas its q-valuations are0 and2m, impossible for a nonzero real Gaussian integer. Norm(h)>0 excludes zero. The shared H also cannot have zero real part, since a pure imaginary integer has equal valuations at a Gaussian prime and its conjugate.

There are4D(h) Gaussian integers K of norm h^2. Thus the EXACT number of signed oriented pairs is8D(h), and imposing positive common real part leaves4D(h), by the fixed-point-free K->-K involution. This counts oriented representations of one edge, not cuboid endpoints or canonical triples. For h=1 there are8 signed pairs and4 with positive real part, regardless of p,q,n,m.

This replaces the false independent product (8D(h))^2 of two shared-unit cofactor lists by8D(h). It is a genuine removal of duplicate choices. However151 already encodes a triple using a SINGLE global H_i per edge. Those original allocations already contain this compatibility. Since D(h)=h^o(1), the displayed compression supplies no new fixed power of R compared with that original receiver. No such asymptotic estimate is imported as a theorem needed for the gluing proof; the standard divisor-size observation is only explanatory.

## 2. All squarefree split diagonals: full Gaussian local tests equal the sphere gate

Let R be ANY odd squarefree product of split primes. Select three pairs H_i=e_i+i f_i with positive integer e_i,f_i, Norm(H_i)=R^2, gcd(e_1,e_2,e_3)=1, and exactly ONE odd e_i. These are the original edge/complementary-face circles, before imposing the sphere equation. Any original physical endpoint satisfies these conditions. Define

 F=sum_i(H_i^2+bar(H_i)^2)+2R^2
  =4(sum_i e_i^2-R^2).                                    (155.2)

For p|R choose pi above p. Let I_p={i:p does not divide e_i}. For each i in I_p orient H_i by independently conjugating it so that H_i'=bar(pi)^2 G_i^(p), and put C_p=sum_(i in I_p)(G_i^(p))^2. This orientation exists: if p does not divide e_i, one of the two Gaussian valuations of H_i is0 and the other2. All terms H_i^2+bar(H_i)^2 are unchanged by the conjugations.

The FULL local Gaussian condition obeys

 pi^2 | C_p  iff  pi^2 | F  iff  p^2 | F.                 (155.3)

To see this, modulo pi^2 the conjugates of the oriented unit edges vanish, leaving bar(pi)^4 C_p. For i outside I_p, p divides both e_i and f_i: the norm equation implies p|f_i, so H_i and its conjugate are each divisible by pi and their squares vanish modulo pi^2. Also pi^2|R^2. The factor bar(pi)^4 is invertible modulo pi^2. Finally F is an ordinary integer, so conjugation converts pi^2|F to bar(pi)^2|F, and together these imply p^2|F. This reasoning also handles |I_p|=1; such a tuple cannot pass the local test, because its lone G is a pi-unit.

Taking ALL p|R, squarefreeness and the Chinese remainder theorem yield R^2|F, equivalently R^2|sum e_i^2. Since 0<e_i<R, this sum is strictly between0 and3R^2. Its quotient by R^2 is therefore1 or2. Exactly one odd edge gives sum e_i^2=1 modulo4, while R^2=1 modulo4; quotient2 is impossible. Consequently

 [pi_p^2|C_p for EVERY p|R]  iff  sum_i e_i^2=R^2.       (155.4)

The reverse implication is immediate from F=0 and(155.3). After(155.4), primitivity forces |I_p| in {2,3}, and the positive-edge argument retained in153 gives C_p!=0. Thus requiring these two extra witness filters does not change the equivalence.

Equation(155.4) covers ALL squarefree support sizes at once. It demonstrates why multiplying local probabilities is unjustified here: once the local witnesses reconstruct the same global H_i, demanding all the exact tests is precisely the original physical sphere equation. It does not prove those solutions are frequent, rare, or absent. The weaker integer condition p^2|Norm(C_p) used for candidate upper bounds in153/154 is NOT substituted for the full Gaussian condition.

For nonsquarefree R the same modulo-pi^2 argument still supplies p^2|F, but only rad(R)^2|F after gluing. It does not give R^2|F. Hence(155.4) is not silently extended to repeated-prime-power diagonals. Those remain part of E_bal and still require a bound.

## 3. What the total budget actually says

Let D(R)=product_(p^a||R)(2a+1). There are4D(R) signed Gaussian circle points per edge. Global triples before the sphere filter therefore cost at most64D(R)^3, exactly the old151/152 allocation envelope. Gluing local orientations into one global triple pays this envelope once; it does not replace it by a proved smaller count of successful sphere triples.

155 provides neither sum_(R<=B,R in E_bal) J(R)=o(M3(B)) nor a negligible new physical sector.154's scalar alphabet-cover obstruction is untouched. Its O(B^(1/2)/log B) balanced semiprime upper budget has not been improved. The prime directions must be consistent, but mere consistency is not a new sparse-population theorem.

Decision: the elementary same-witness/CRT bootstrap FAILS AS A NEW COUNTING MECHANISM. Stop generating successive cards that only add more compatible primes or rewrite the same joint receiver.152/153 remain retained;154's firewalls remain retained; global credit stays0 and the main gate staysOPEN. A future estimate of the already-glued sphere population would reopen this mechanism, but another gluing identity alone does not.

## 4. Concrete alternative: test additive counting on the exact circle population

For odd split R and d|R define the finite exponential polynomial

 A_(R,d)(theta)=sum_(0<e<R, R^2-e^2=f^2 with f>0, d|e)
                    exp(2*pi*i*e^2*theta).

Orthogonality gives the exact labelled primitive positive cuboid count

 N_prim(R)=sum_(d|R) mu(d) integral_0^1
               exp(-2*pi*i*R^2*theta) A_(R,d)(theta)^3 dtheta. (155.5)

Proof: the integral selects precisely sum e_i^2=R^2 with positive integer complementary diagonals. Each e has one positive f. On such a triple any common divisor g of the edges divides R because g^2 divides R^2; it also divides every f_i. The sum of mu(d) over common divisors d|R of all edges is1 exactly for primitive triples, and0 otherwise. Thus the formula preserves primitivity rather than quietly counting scaled copies. Original canonical masks select a subpopulation, so their physical count is at most N_prim(R). One may retain those masks explicitly for an equality on the original population.

This formula is an EXACT ADAPTER, not a new bound and not a claim of novelty. Dropping phases or taking only absolute-value/divisor bounds returns the old envelope. A useful next study must identify cancellation, additive structure, or a separate stronger denominator estimate that changes the TOTAL exponent on the exact moving-R population. Generic random residues or parameter-side CRT estimates cannot be transferred without a theorem on these sparse circles and their endogenous R.

NEXT156=GlobalAdditiveSphereBudgetSelection: compare actual available bounds for(155.5), and the retained denominator's possible strengthening, against the whole-E_bal budget BEFORE constructing another receiver. PASS requires a concrete theorem and a valid adapter whose total cost improves the present bound toward o(M3), including moving R, primitivity and all residual support types. If no such input exists, record that these candidate mechanisms are presently blocked; do not proceed to infinite case classification. No promise of closure within a few cards is warranted.

## Audit, dedupe and replay

Sources: current154 card and current native MAIN/INDEX/LEDGER/ROUTE;151 Gaussian identity;152 allocation envelope;153 reconstruction and positive C!=0 argument. Targeted ledger review found historical CRT statements on parameter and Stage14 populations, but none is imported onto the present circle measure.154's shared-edge equality is the starting point, not claimed as new. New here are its exact arbitrary-cofactor gluing count and the explicit whole-squarefree support equivalence(155.4), used to terminate an unproductive elementary bootstrap. No literature-wide novelty or external hostile audit is claimed.

verify155.py independently enumerates Gaussian norm circles, compares the complete pair list with both gluing branches, and checks every selected triple's Gaussian divisibility against the real integer defect and the sphere predicate. Six gluing cases and5583 squarefree triples, including2-,3-prime and r=2/r=3 branches, pass. Finite absence of cuboids in those checks is not used for any universal nonexistence claim. The written proofs provide the uniform statements.

TI remains parked,120 remains retracted,147–149 remain retained within scope, automatic degree escalation remains paused. GLOBAL_FIXED_POWER_SAVING=false; PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false.
