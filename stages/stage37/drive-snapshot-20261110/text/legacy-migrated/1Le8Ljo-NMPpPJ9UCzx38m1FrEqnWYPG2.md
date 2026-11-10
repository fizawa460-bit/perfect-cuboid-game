# M3-PESCH-TI-005 — Forced-kernel barrier, 2-adic repair and exact physical receiver

DATE=2026-09-30
STATUS=PROVED_CHARACTER_ONLY_BARRIER_AND_UNIFORM_TWO_ADIC_ENHANCEMENT
DEPENDENCIES=TI-004 matrices/exact Master kernel; TI-003 descent image normalization; TI-002 torsion screen and VW nonsquare; TI-001 endpoint detector.
PRIMARY_GATE=M3-PESCH-TI-GATE-001 / OPEN
PARTIAL_EXIT=Uniform rank-zero criterion strengthened; requested asymptotic physical weight bound still not obtained.

## 1. A structural ceiling in the TI-004 criterion

Keep U=m²−n², V=2mn, W=m²+n² and A,B,k,l,delta from TI-004. For any q|U with q=1 mod4, m≡±n modq, so
2V=4mn≡±4n² and 2W=2(m²+n²)≡4n² modq.
Both are squares because −1 is square. Consequently the exponent vectors
v=sf(2V)=sf(mn), w=sf(2W)
ALWAYS lie in ker B. Here sf denotes positive squarefree representative, with its parity vector in the B columns. The vector w is nonzero since W is odd and2W has odd 2-adic valuation. Their product is sf(VW), nontrivial by TI-002's Fermat descent.

If mn is not a square, v is nonzero; v,w are distinct because their product is nontrivial. Thus dim ker B>=2, rank B<=l−2, and delta_dual>=1. In particular **TI-004's delta=0 criterion can close only sources with mn square**, equivalently m=a²,n=b² by gcd(m,n)=1.
This is a barrier of that particular character matrix. It does NOT prove positive rank, local solubility of either cover, failure of full two-descent, or rarity in the physical M3 measure. The known sf(VW) image need not split into actual image classes v,w.
The two existing TI-004 fixtures (4,1),(9,4) both have square mn, consistently with this theorem. No TI-004 statement is withdrawn; its sufficient criterion and upper bound remain correct.

## 2. Uniform 2-adic repair when nu_2(V)=2

Let E': y²=x³+4Sx²+16V²W²x, S=V²+W². Suppose V=4v0 with v0 odd. For EVERY signed squarefree descent representative d with2|d, its integral cover
c²=d z⁴+4S z²t²+(16V²W²/d)t⁴, gcd(z,t)=1,
is insoluble over Q_2. Hence every E' image class is odd in this range.

Proof. Write d=2d0, d0 odd (possibly negative); S≡1 mod8 and constant coefficient16V²W²/d=128 v0²W²/d0 has valuation7. The divisions by d0 below take place in Z_2; the full cover coefficients are integers.
If z odd, RHS has valuation1, impossible for a square. Otherwise t odd and a=nu_2(z)>=1:
- a=1: divide RHS by16. Mod8 it is S z0²t²+2d0 z0⁴≡1+2d0, which is3 or7, never a square unit.
- a=2: divide by64. Mod8 it is S z0²t²+2v0²W² t⁴/d0≡1+2/d0, again3 or7.
- a>=3 (including z=0): constant term alone has minimum valuation7; the other terms have valuations>=8 and>=13. Impossible.
This also proves nonsolubility modulo512 on primitive residue pairs. t=0 is in the z-odd case. Sign and odd prime support do not affect the proof.

TI-003 tested2^6, which is too weak to reveal every such obstruction. The deeper modulus here was selected from a universal valuation proof, rather than enlarging a rank table blindly.

## 3. Enhanced matrix bound and replayed certificates

Define B_star=B with the unit row on its prime2 column appended when nu_2(V)=2; otherwise B_star=B. Then
rank E3(Q)<=delta_star=(k−rank A)+(l−1−rank B_star),
0<=delta_star<=delta.
Proof: TI-004 image/kernel inclusion plus the new parity row. The known sf(VW) image is odd when nu_2(V)=2, so its nonzero vector stays in ker B_star. Sign remains a free coordinate counted exactly as in TI-004. No positive-rank inference from delta_star>0.

C_star={p in G_tor:delta_star=0} is TI_CLOSED, with C_char subset C_star.
The former square-mn ceiling is bypassed in the branch nu_2(mn)=1. Outside that branch, the old forced-kernel barrier persists: delta_star=0 requires mn square. This is a limitation of the enhanced criterion, not a rank distribution theorem.

Selected proof fixtures, no survey of all sources:
| source | nu_2(V) | delta | delta_star | result |
|---|---:|---:|---:|---|
| (2,1) |2|1|0|rank0 + torsion4, TI_CLOSED|
| (6,1) |2|1|0|rank0 + torsion4, TI_CLOSED|
| (11,2) |2|1|0|rank0 + torsion4, TI_CLOSED|
| (8,5) |4|1|1|UNKNOWN|
| (18,7) |2|2|1|UNKNOWN|
| (4,1) |3|0|0|previous TI-003/004 closure|
| (9,4) |3|0|0|previous TI-003/004 closure|

The first three extend this Stage37 replayed registry beyond the two TI-003 fixtures. No claim they are absent from the paper's external1072 list. No unconditional credit to that aggregate; HOLD continues. Exact rows and column sets are in ti005_examples.json. Their rank-zero certificates follow the proved universal matrix theorem, not a numerical analytic-rank calculation.

## 4. Physical connection and remaining weight problem

Use exactly TI-004's h_B, mu_B=h_B/2 off diagonal, F_B and existing R_phys cutoff. Put
D_star={p in G_tor:delta_star>=1}, X_tor={17017|UVW}.
Then endpoint sources lie in D_star union X_tor, and
P(B)<=R_DstarDstar(B)+2 F_B(X_tor).
The union-bound RHS can exceed M3; use min(M3,R_DstarDstar+2F(X_tor)) when desired. Neither term has an asymptotic bound here.

For an exact partition form, H_star=all primitive sources minus C_star, so P<=R_HstarHstar. Let N=C_star minus C_char, H_char=all sources minus C_char. The measurable improvement is the exact identity
R_HcharHchar−R_HstarHstar=2 sum_{p in N,q in H_star}mu_B(p,q)+sum_{p,q in N}mu_B(p,q).
This uses disjoint N,H_star and same physical cutoff, with no independent-source assumption. It counts each removed physical object once in total; it is not an additional saving to add on top of the same exclusions.

A concrete physical witness: Master p=(11,2),q=(8,5),g=39 gives (X,Y,Z)=(117,44,240). p has delta_star0, q remains UNKNOWN. Thus this primitive Euler brick lies outside H_starH_star, and the difference above is at least1 for every B>=R_phys(canon(117,44,240)). Its actual numerical physical height is not replaced by max edge. No endpoint exists in that fixed p fiber by the general detector. This is a nonempty physical exclusion, not a density or o(M3) estimate.

Attempted weighted exit: TI-004's character-only residual cannot be made small merely by asserting generic random full rank, since it has the forced kernel in section1. The 2-adic row repairs one branch, but no proof controls the physical weights of the remaining branches or X_tor. Raw source-box sparsity of square-mn sources says nothing about F_B without a transfer theorem. Therefore no weighted-hard-locus or fixed-power-saving claim is issued.

## 5. Audit and continuation

Independent ti005_audit.py enumerates ALL primitive residue pairs mod512 for8 signed covers from the selected fixtures; verifies forced kernels and independent binary kernels; reconstructs the physical witness. These finite tests supplement the universal proofs. Scripts use standard Python only, no GRH/BSD/analytic rank. Save both scripts and JSON outputs with this card and audit; same-directory replay: python ti005_rank_bound.py; python ti005_audit.py.

NEXT=M3-PESCH-TI-006. Keep TI as the active route. Study the surviving 2-adic branches together with exact Master partner weights; prioritize a provable weight bound or a further uniform obstruction that reaches a genuinely weighted region. Do not spend batches expanding an undirected rank table. The character-only closure ceiling is now known, so a full-rank-randomness premise for old B is prohibited. Higher valuations require a new proof before adding a 2-adic row. T11-121 remains valid parked auxiliary structure; TI superiority is still undecided.

FLAGS: CHARACTER_MATRIX_FORCED_KERNEL_BARRIER_PROVED=true; UNIFORM_TWO_ADIC_ROW_AT_V2_2_PROVED=true; ENHANCED_RANK_BOUND_PROVED=true; NONSQUARE_MN_REPLAYED_TI_CLOSED_SOURCES=3; E3_INFINITE_RANK_ZERO_FAMILY_PROVED=false; WEIGHTED_HARD_LOCUS_SAVING_PROVED=false; GLOBAL_FIXED_POWER_SAVING=false; PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false; PERFECT_CUBOID_NONEXISTENCE_CREDIT=false; TI_1072_AGGREGATE_STATUS=HOLD.
