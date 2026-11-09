# R5-C224-erratum｜Stage35EX 原著研究記録（歴史的テキスト）

> 出典：R5-C224-CARD-C220-ERRATUM-HIGH-Q1MOD4-ROLE-CRT-NONCONVERSE  
> URL：https://docs.google.com/document/d/1I3TUEBmk_cgsXUhw-hTrhIrGvnPK5WCj0DE0Zf9KRfM/edit  
> 更新：2026-10-24T01:23:46.552Z  
> 取得：Google Docs paragraph text（改行連結）。原文の数式表示/表レイアウトのバイト同一性は未認証。  
> 原文中の当時のPROVISIONAL・条件付き・誤記は歴史資料として保存する。特にR5-C220の曲線式の誤記はR5-C224とR0-C183の訂正文を優先し、R5-C220単独を正本とみなさない。R5-P112の歴史的マスク残数を2026-11時点のLOW生存数とみなさない。

---

STAGE35EX-E / R5 C224 / MATHEMATICAL ERRATUM + HIGH ROLE NONCONVERSE
DATE 2026-10-24 JST. BASE R0 C35-182 COMPLETE (paired C182 receipt checked).
STATUS OWNER R5 INTERNAL SCOPED PROOF / NEGATIVE METHOD CONTROL; NOT A NEW FULL SOURCE EXCLUSION; NOT OWNER COMMITTED; NOT R0 ACCEPTED. BranchA USER_PAUSED, indexed BranchB OPEN, Bwide outside indexed unbridged, Stage35 OPEN, E1 UNPROVEN.
Original SAME source retains ONE positive primitive labelled A²+B²=C²,C odd, E:y²=x³+B²x²−(AC)²x,P=(AC,ABC),T0=(0,0), actual signed D_n=T0+[2n]P; strict original r/s/p/q, SAME Q/Qsharp, 4 GLOBAL S243 integer roots/common c, ONE actual primitive integer S269 Gaussian f,g, SAME odd role M>N and true parity signed POINT, actual W_n/W_2m and b_m, TRUE S270 all four GOOD/H TOP+PROPER ordinary beta uncapped, and all NEGATIVE/HOLD/retractions.
I. IMPORTANT C220 CORRECTION.
R5 C220 prose erroneously printed the scaled curve as E_z:Y²=X³+zX²−z. This is not the original scaled curve: its X=0 value is −z and loses original rational T0=(0,0). With D=AC>0, λ=D/B>0, x_original=λ²X, y_original=λ³Y, z=B⁴/D², direct substitution into true E gives EXACT
   E_z:Y²=X³+zX²−zX.
On THIS correct curve the true original [2]P corresponds to Q=(1,−1), and T0 stays (0,0). Division-polynomial base values at Q are ψ2=−2, ψ3=3−2z−z², ψ4=4(z+1)(z²+4z−1). They match the OLD C220 native CODE and full local verifier, both of which used a4=−z,a6=0 as required by the CORRECT model. The previously stated (missing X) E_z string in C220 CARD is mathematically incorrect and must be replaced in an eventual R0-adopted proof. Full C220 verifier rerun here: f24 degree143, H(T)=f24(18+T) has ALL 144 strictly positive coefficients, min24, SHA256 of descending canonical coefficient list a57b53d8e7075f49a032d276bcd2b1b15882e4f5dafa059f45bd79e350d2ef8c. Its scoped +12 HIGH ordinate verdict survives this erratum under the correct curve, subject to R0 full history acceptance.
This is a CORRECTION not new math credit or additional exclusion. R5 C220 remains PREPARED, no retrospective COMMITTED/ACCEPTED claim.
II. NEW EXPLICIT HIGH NEGATIVE CONTROL ON FIXED 12 RANK-3 ROLE DEPTH.
Take primitive Euclid (u,v)=(22,1), so
  (A,B,C)=(44,483,485), D=AC=21340, z=B⁴/D²=54423757521/455395600>19.
R0 C130 proves upper γ<1006/55<19, thus this genuine primitive labelled base lies in the FIXED |n|12 admissible HIGH REAL ENVELOPE. Admissible REAL sign/four-Ward-factor positivity is a NECESSARY envelope, NOT a proof sigma square or original physical source.
The exact GOOD odd rank3 support integer is
 H0=B⁴−D²=53968361921=(211949)(89)(2861),
 with 211949≡5(mod8),2861≡5(mod8),89≡1(mod8). ALL q divide H0 with q≡1(mod4); H0 is squarefree, q∤2ABC. Thus C213's specific q≡3(mod4) conclusion q^e|M−N is VACUOUS at this HIGH base. C214's two GOOD q≡3/5(mod8) witnesses can still exist, but C214 assumes 3∤n and therefore does not cover n=±12.
III. GENERAL CRT LEMMA (DEPTH CONDITIONS ALONE CANNOT FORCE A COLLISION).
Let an original primitive positive labelled base satisfy H0=B⁴−(AC)²>0, gcd(H0,2ABC)=1 (old R0 C181), and every q|H0 has q≡1(mod4). Let e_q=v_q(H0)>0.
THEN there are INFINITELY MANY pairs of ODD coprime positive integers M>N>1, with M=N+2, gcd(MN,2ABC)=1, 1<M/N<sqrt(C/A), such that FOR EACH q|H0:
  v_q(M⁴−N⁴)=e_q,
  v_q(M²+N²)=e_q,
  v_q(M−N)=v_q(M+N)=0.
PROOF. M=N+2 gives M⁴−N⁴=8(N+1)[(N+1)²+1]. Since q≡1(mod4), −1 admits a square root i mod q; the derivative of (N+1)²+1 is 2(N+1), nonzero at N=i−1 mod q. Hensel gives a unique root modulo q^e and exactly one lift modulo q^{e+1} that continues the root. Choose ANY OTHER lift N modulo q^{e+1}; it gives exact valuation e of ((N+1)²+1), while q∤(N+1) and q∤8, proving all q depth claims. The q^{e+1} congruences are pairwise coprime. At every p|2ABC prescribe an N residue with p∤N(N+2), possible: N≡1 mod2, N≡2 mod3, N≡1 modp for p≥5. All these moduli are coprime to H0, so CRT yields one positive arithmetic progression of N. For every sufficiently large N in it, M=N+2>N>1 and (M/N)²<C/A since C>A>0. gcd(M,N)=gcd(N,2)=1. QED.
This construction satisfies the exact q-depth values that are NECESSARY under true same S269 source at signed n multiple3 and the role bound/coprimality. It does NOT satisfy or imply the ACTUAL Ward denominator b_12=MN, primitive Gaussian f²+g²=MN, exact S269 original quartic/POINT, any S243 global integer roots, nor S270 TRUE4TOP. It is a formal NONCONVERSE, NOT A PERFECT CUBOID OR SOURCE WITNESS.
IV. INDEPENDENT EXACT NUMERICAL CONTROL FOR THE DISPLAYED HIGH BASE.
CRT/Hensel replay for q=89,2861,211949 plus 2ABC coprimality produces
 N=2575092160959083295910231391,
 M=2575092160959083295910231393.
gcd(M,N)=gcd(MN,2ABC)=1, all odd, 1<M/N<sqrt(485/44); for all q in {89,2861,211949} v_q(M⁴−N⁴)=v_q(M²+N²)=1 while v_q(M−N)=v_q(M+N)=0.
The huge role pair is NOT the original actual Ward b12 roles and no f,g integer source has been constructed. Source FULL packet exclusion credit0. Mathematical scope is a negative control on rank3-only proof strategies, not an R1/R2/R3 closure lemma. R0 should not treat the role-depth congruences alone as sufficient to eliminate FIXED −12 HIGH.
REPLAY local:
 /mnt/data/r5_c224/r5_c224_exact_erratum_countercontrol.py SHA256 7170ad981609ed63c11b0fdb7e98ab12f37b41da5710e8027b948d325a7f9414
 /mnt/data/r5_c224/r5_c224_rank3_role_depth_countercontrol.py SHA256 41637cec0422eba3ece87c50433fc66cf519331eacf3a2eba46a685c077059ba
 /mnt/data/r5_c224/r5_c224_evidence.json SHA256 46a1e81ad35af26b02876109616c8095ec27ca9ee0feef79dc4977d37af64619
 /mnt/data/r5_c224/r5_c224_role_countercontrol.json SHA256 b0f4388d91e8ba31187a63396b07957304da7c700ded72fe9e2690249759ac2b
C220 original https://docs.google.com/document/d/18xv9GV1CB0T28lcLttuNPo6WZaLCZcOyuweP_gtoux0/edit
C213 original https://docs.google.com/document/d/1X0ceWppl7T6MUGQoj_RMQfx8XmKgmp5O_-gfksADQ5g/edit
C214 original https://docs.google.com/document/d/1EZLuercgML8ZKOx6HJ4ftPAEsw3MBHlz3ofkdX9emg4/edit
R0 C181 https://docs.google.com/document/d/1gBT0cVA2pfJogF928voazcyvzQIh4Fr7NLBr-pPzqe8/edit
C130 root interval https://docs.google.com/document/d/1Z5gxDgSs3Gx8VTeymZShhMesRaoascgXbqm6ekkRxDQ/edit
K04 fixed −12 HIGH, all other indexed moving bases and indices, and Bwide outside indexed remain OPEN. NEW PHYSICAL FULL SOURCE EXCLUSIONS=0; REDUCTION OF GLOBAL CLOSURE LEMMAS=0; R0 SUBMIT FOR NEW MATH=NONE. No owner canonical STATE update or R0 acceptance fabricated.
END R5 C224 CARD ERRATUM NEGATIVE CONTROL.
