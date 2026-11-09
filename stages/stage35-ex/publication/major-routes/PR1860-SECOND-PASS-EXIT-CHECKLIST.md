# PR #1860｜第２周の有限な終了条件と全件固定台帳

**作成：2026-11-09｜対象はR3-07とR2-01のみ｜状態：NOT COMPLETE / Draft / DO NOT MERGE。**

これまでの「新しい数学原著が見つかったら際限なく探索を広げる」管理は終了条件がなく不適切だった。**第２周を終わらせるための固定母集団と完了条件を定義する。** 本表は後付けの一般研究NEXTでなく、PR #1854から#1860への**数学的原著所在・依存鎖の移植確認**専用。

## 終了の定義（５つ全部PASSなら終了）

| Gate | 何を全件確認するか | 現在 | 完了に必要な残作業 |
|---|---|---|---|
| A | #1854でDriveのみとした**23件すべて**に必要性判定・収載先／不要根拠を付ける | **PASS（23/23）** | なし：12本コピー・11件は移植しない理由付き |
| B | その23件**以外**に見つかった親原著10本＋既知原本の未収載§15証明１本の本文・場所を確定する | **PASS（11/11）** | なし：10本GitHub SHA照合、§15原著区間一致 |
| C | 第１周の**39引用辺全件**に「使った数学命題・実際の原著／後続再証明・適用条件・終端判定」をつける | **PASS（39/39）** | 原著33、後続再証明2、直接不要3、外部Dへ明示移管1。Cには未判定０件 |
| D | 現在の証明に必要な外部定理を、原命題の内容・成立条件・使う式と照合する | **OPEN（明示２ゲート）** | row393のde la Maza、Branch B §15.4のMordell四次式。C187の155/197にBérczes定理を無理に加えない |
| E | R3 row393/row367/368/369/376/C183、R2 C189/C187/S270を起点に**親を端から端まで１回通読照合**する | **PASS（７終端／７終端）** | 著者数学原著の必要本文の未収載０。引用する外部定理の原典照合はDで２件保持 |

**A+B+C+D+Eの全PASSが「PR #1860の第２周を全部しました」の意味。** 定理そのものの独立敵対監査、数値ZIPの全再演、R3の−30全排除、R2の相関上界、完全直方体不存在は第２周の完了要件に**混ぜない**。それらは別の数学研究・検証の対象。

## 今ある有限の一覧と重複を含まない件数

| 原分類 | 件数 | 本台帳の所在 |
|---|---:|---|
| #1854の既収載数学ファイル | **129**（共通23、R3本鎖56、R2本鎖17、条件付き祖先33） | [元一覧](PR1854-PROOF-EVIDENCE-PRESENCE-MATRIX.md) §3 と [全129行JSON](PR1860-SECOND-PASS-EXIT-CHECKLIST.json) |
| それより前にGitHubにあった原著 | **２** | 同元一覧 §2 |
| #1854に無かったDrive原著候補 | **23**＝R3の12＋別扱い11 | 下の23行表 |
| 第１周23件の外から見つけた別個の原数学Drive原著 | **10** | [再帰台帳](PR1860-RECURSIVE-PARENT-AUDIT.md) |
| 以前のDrive原本に含まれたがGitHubに抽出されていなかった数学証明節 | **１**（Branch B §15） | [原証明](proofs/earliest-foundations/BranchB-Section15-torsion.md) |
| PR #1860に追加済み数学本文 | **23ファイル**＝12＋10＋１ | 個々の親原著本文 |
| 第１周の証明引用辺 | **39** | [元39行](PR1854-PROOF-EDGE-AUDIT.json)、本JSONに全39行固定 |
| #1860で追加検討した数学依存辺 | **45** | [再帰監査台帳](PR1860-RECURSIVE-PARENT-AUDIT.json)。39行と同一集合ではない |

## 初回23件：一件も空欄にしない（今回12ファイルのGitHub SHAを実際に再照合）

| No | 初回未収載の数学原著 | 今の第２周の判定 | GitHub／Driveの場所・根拠 |
|---:|---|---|---|
| 1 | row344（R3-07 ±18） | **移植・現物再検証済み** | [`row344`のGitHub原数学本文](./proofs/R3-18-upstream/row344.md). sha台帳一致 |
| 2 | row346（R3-07 ±18） | **移植・現物再検証済み** | [`row346`のGitHub原数学本文](./proofs/R3-18-upstream/row346.md). sha台帳一致 |
| 3 | row347（R3-07 ±18） | **移植・現物再検証済み** | [`row347`のGitHub原数学本文](./proofs/R3-18-upstream/row347.md). sha台帳一致 |
| 4 | row348（R3-07 ±18） | **移植・現物再検証済み** | [`row348`のGitHub原数学本文](./proofs/R3-18-upstream/row348.md). sha台帳一致 |
| 5 | row349（R3-07 ±18） | **移植・現物再検証済み** | [`row349`のGitHub原数学本文](./proofs/R3-18-upstream/row349.md). sha台帳一致 |
| 6 | row353（R3-07 ±18） | **移植・現物再検証済み** | [`row353`のGitHub原数学本文](./proofs/R3-18-upstream/row353.md). sha台帳一致 |
| 7 | row355（R3-07 ±18） | **移植・現物再検証済み** | [`row355`のGitHub原数学本文](./proofs/R3-18-upstream/row355.md). sha台帳一致 |
| 8 | row356（R3-07 ±18） | **移植・現物再検証済み** | [`row356`のGitHub原数学本文](./proofs/R3-18-upstream/row356.md). sha台帳一致 |
| 9 | row357（R3-07 ±18） | **移植・現物再検証済み** | [`row357`のGitHub原数学本文](./proofs/R3-18-upstream/row357.md). sha台帳一致 |
| 10 | row358（R3-07 ±18） | **移植・現物再検証済み** | [`row358`のGitHub原数学本文](./proofs/R3-18-upstream/row358.md). sha台帳一致 |
| 11 | row359（R3-07 ±18） | **移植・現物再検証済み** | [`row359`のGitHub原数学本文](./proofs/R3-18-upstream/row359.md). sha台帳一致 |
| 12 | row360（R3-07 ±18） | **移植・現物再検証済み** | [`row360`のGitHub原数学本文](./proofs/R3-18-upstream/row360.md). sha台帳一致 |
| 13 | S250（R2-01） | **直接の必須親ではない／再証明あり** | [Drive原著](https://docs.google.com/document/d/10NtB8i-f1WVC7NPm4bpM5KxXGnPnjfn_LxPSw8jqas8/edit). RESTATED_IN_GITHUB_S251: S251 explicitly says 'This is precisely S250, reiterated only for a unified statement.' |
| 14 | S271（R2-01周辺） | **直接の必須親ではない／再証明あり** | [Drive原著](https://docs.google.com/document/d/1eJxTmBp0-X0vEc3ccE9C-cdhOn7Gk5rLwI9OWuy3OcM/edit). OLD_CONDITIONAL_SIDE_BRANCH: S275 refers to S271 special dyadic setup; C187's retained proof uses S275 global canonical and S |
| 15 | S272（R2-01周辺） | **直接の必須親ではない／再証明あり** | [Drive原著](https://docs.google.com/document/d/1UWQOece3VQt447Y7mdQxxOdcizNpEQ_EqDNjE8_gMIA/edit). OLD_CONDITIONAL_SIDE_BRANCH: S275 discusses S272 genus33 geometry but no new finiteness/exclusion; C187 uses current source a |
| 16 | S273（R2-01周辺） | **直接の必須親ではない／再証明あり** | [Drive原著](https://docs.google.com/document/d/1zwv674vrXnkmFzySToYW8bt-SdrWCV3U0N5YeniamGU/edit). OLD_CONDITIONAL_SIDE_BRANCH: S275 invokes S273 for historical twist interpretation and derives its own global factorization. |
| 17 | S274（R2-01周辺） | **直接の必須親ではない／再証明あり** | [Drive原著](https://docs.google.com/document/d/1obXBSopay9GAnLqc9gEOXz8zG9Oy3cCcrwOIeJUZ-Ew/edit). OLD_CONDITIONAL_SIDE_BRANCH: S275 includes an all-index no-go for relying on the union of the S274 twists; this isn't the C18 |
| 18 | S280（R2-01周辺） | **直接の必須親ではない／再証明あり** | [Drive原著](https://docs.google.com/document/d/1WdOKrD2JQ7F6VRKlUx04aDsqIPlNF8NinXM7dtAINrg/edit). HISTORICAL_MENTION_ONLY_IN_C189: C189 mentions S280 only inside the R1 withdrawal-reconciliation 'dominate' sentence; current |
| 19 | S283（R2-01周辺） | **直接の必須親ではない／再証明あり** | [Drive原著](https://docs.google.com/document/d/1CWG97DLy6JJ5MYtJrb4Q7J5IGPVV4WGnWtyqnv5Utu0/edit). OTHER_SCOPE_NONUNIFORM: S283 states fixed-base positive-density sign obstacle, not all-index correlated ordinary-beta upper;  |
| 20 | C188（R3/R2歴史） | **直接の必須親ではない／再証明あり** | [Drive原著](https://docs.google.com/document/d/1gNnTh4AbS_xHcG6dZY4XvUcaqXtiadDslpLK_1ih8wM/edit). OTHER_FIELD_HISTORICAL_R0_INTAKE: C188 addresses K21 classgroup and withdrawn old rank; R3 signed±18 uses distinct degree36 C |
| 21 | C191（R3/R2現行範囲） | **直接の必須親ではない／再証明あり** | [Drive原著](https://docs.google.com/document/d/1FrUqVQdUdC2WbhdwAYlMxzEq1YTi5SHqHRVjq-tsTWc/edit). POST_C189_RECONCILIATION: C191 BASE=C35-190; R4 universal a>=21 correction; explicitly retains C189 bands rather than proving |
| 22 | BranchB §1–12（共通歴史） | **節単位で代替・要否整理済み** | [Drive原著](https://docs.google.com/document/d/1CKLon3eRKjsEVuIwgpSTV4DKHQ5GRWsfDw2SA6T5vNI/edit). DEFERRED_OLD_FOUNDATION_SCOPE_CHECK: Historical Drive manuscript >120k chars. GitHub has E3 physical and generic MW originals |
| 23 | C193（共通歴史） | **直接の必須親ではない／再証明あり** | [Drive原著](https://drive.google.com/file/d/1D8QNpX2k-O36w76ZoTqbVDdUFJClNnLj/view). NEGATIVE_BARRIER_NOT_POSITIVE_PARENT: C193 establishes genus3→genus4 non-map warning and C194 later refines it; not a mathema |
| | **計23件** | **移植12／見送る根拠11** | **初回一覧の空欄０件** |

## 第１周39辺の最終判定：39行すべてに根拠

**2026-11-09最終照合：原著あり33、同等証明２、現行終端に非必須３、外部原典の適用だけGate Dへ移管１、合計39/39。** [機械可読チェックリスト](PR1860-SECOND-PASS-EXIT-CHECKLIST.json)では各辺の**子の本文・親の本文の実ファイル・使った命題の正確な範囲**を保持する。

| # | 子→親 | 判定 | 根拠の数学本文・限定 |
|---:|---|---|---|
| 1 | `C189→C175` | **原著あり** | [原数学本文](./proofs/active-ancestors/C175.md)：C189 §adoption directly retains C175 hybrid constant c_E, κ=25408/727; current C175 original contains certified bound; not R2 |
| 2 | `C189→C185` | **原著あり** | [原数学本文](./proofs/active-ancestors/C185-R2-prime-cut-original.md)：C189 §adoption directly retains R0 C185 exact sparse protected 9/50 and 7/50; owner math text separately retained and not mis |
| 3 | `C189→S270` | **後続再証明** | [原数学本文](./proofs/foundations/S270.md)：C189 does not literally cite S270 as a mathematical prerequisite in this adoption paragraph; C187 SOURCE LOCK and C185 protec |
| 4 | `C189→C187` | **原著あり** | [原数学本文](./proofs/R2-uniform-thresholds.md)：C189 adopts C187's 155/197 lower bound; C187 explicitly states conditional original signed packet and C189 dependent adoption |
| 5 | `C187→C185` | **原著あり** | [原数学本文](./proofs/active-ancestors/C185-R2-prime-cut-original.md)：C187 formula P4/P1 uses C185 owner exact sparse prime-cut coefficient. True canonical z_i versus protected U_i is distinguish |
| 6 | `C187→C175` | **原著あり** | [原数学本文](./proofs/active-ancestors/C175.md)：C187 all-base hybrid λ* and κ=25408/727 use R0 C175 height; separate owner C174 and R5 C157 older height proof also retained. |
| 7 | `C185→C160` | **原著あり** | [原数学本文](./proofs/active-ancestors/C160-R2-strong-gcd-original.md)：C185 owner explicitly states C160 original SG.1/SG.2 with same v2, b_(m/ell)/b_m at odd prime ell and nodal H formal smooth i |
| 8 | `C185→S268` | **原著あり** | [原数学本文](./proofs/C195-upstream/S268.md)：C185 owner §§2-5 uses S268 §4 h_p odd first-entry and β_p, T_e. Same indexed b_m as S270, no free auxiliary packet substituti |
| 9 | `C185→S275` | **原著あり** | [原数学本文](./proofs/active-ancestors/S275.md)：C185 exact four z_i uses S275 §2–3 canonical four integral coprime factors, distinguishing canonical factors from S270 protec |
| 10 | `C185→S318` | **原著あり** | [原数学本文](./proofs/active-ancestors/S318.md)：C185 H_noncritical protection uses S318 §§2-3 exact original first-entry and actual-top vs noncritical H correction. S258 T_e |
| 11 | `S318→S316` | **現行終端に非必須** | [原数学本文](./proofs/active-ancestors/S316.md)：S316 moving-base marked-family floor is used only for S318's separate prime-index/family quantitative conclusion §3; C185/C18 |
| 12 | `S232→S230` | **現行終端に非必須** | [原数学本文](./proofs/active-ancestors/S230.md)：S232 finite-odd exclusion A/C formal valuation cites S230 (which exists). Current C187 155/197 and R3 fixed-index results ass |
| 13 | `S251→S250` | **後続再証明** | [原数学本文](./proofs/active-ancestors/S251.md)：S251 explicitly says 'This is precisely S250, reiterated only for a unified statement'; SAME good denominator Kummer/order8 r |
| 14 | `S243→S242` | **現行終端に非必須** | [原数学本文](./proofs/active-ancestors/S242.md)：S242 supplies only the fixed (8,15,17) rank-two example cited within S243; C185→S275→S243 all-base four roots are derived ind |
| 15 | `S194→SECTION16_NONSQUARE` | **原著あり** | [原数学本文](./proofs/earliest-foundations/BranchB-Section16.md)：S194 §2 uses a(t) nonsquare to prove K=E[2]+ZP 2-saturated and §3 relies on uniform E' torsion. BranchB original §16 nonsquar |
| 16 | `R367→row364` | **原著あり** | [原数学本文](../../materials/original-source-exclusions/parents/row364/STAGE35EX_R3_07_EXACT_SELMER9_CT_REDUCTION_20261105.md)：row367 §inputs imports row364 true Selmer dim9, fake8, and exact H2=loc Sel2. Source row364 includes old row363 class/units a |
| 17 | `R367→row365` | **原著あり** | [原数学本文](../../materials/original-source-exclusions/parents/row365/REPORT.md)：row367 uses row365 local σ2 injectivity, J(Q2)[2], H2∩π(T)=0, and global 2-power divisibility; row365 scopes fixed ±18 genus1 |
| 18 | `R367→row366` | **原著あり** | [原数学本文](../../materials/original-source-exclusions/row367/parent_evidence/ROW366_PROOF.md)：row367 uses row366 genuine local 4-division β4 constant on v2 X=4 annulus; row367 computes β4=0, β8=0, and 16-half obstructio |
| 19 | `R368→S321` | **原著あり** | [原数学本文](./proofs/active-ancestors/S321.md)：row368 §2 directly invokes S321 W5=D^12 F G factor and coprimality under SAME D=AC,V=B^4; the full original S321 text is GitH |
| 20 | `R368→C118` | **原著あり** | [原数学本文](../../materials/original-source-exclusions/parents/C35-118/export.txt)：row368 uses C118 fixed rational-point classification X(Q)={(0,±1,±1)} to exclude positive x=D/B². R0 C118 integrated mathemat |
| 21 | `R368→S263` | **原著あり** | [原数学本文](../../materials/original-source-exclusions/parents/S263.md)：row368 uses S263 actual signed indexed D_n original sigma_n square iff adjacent Ward W_{n−1},W_{n+1} with exact δ_n; S263 is  |
| 22 | `R368→S264` | **原著あり** | [原数学本文](./proofs/foundations/S264.md)：row368 uses S264 B-even restriction n divisible by 8 and A-even mod2 status; S264 exact signed label/δ source present, no unp |
| 23 | `R369→S321` | **原著あり** | [原数学本文](./proofs/active-ancestors/S321.md)：row369 §2 explicitly uses S321 W7 H1H2 factor for same original indexed base; S321 §Exact original packet has complete explic |
| 24 | `R369→S322` | **原著あり** | [原数学本文](./proofs/active-ancestors/S322.md)：row369 §Ward7 uses S322 exact H1=K L decomposition, resultant −2^24·13 and gcd/sign facts to force two −squares; source S322  |
| 25 | `R369→C35-12` | **原著あり** | [原数学本文](../../materials/original-source-exclusions/parents/C35-12/PROOF.md)：row369 forces x=−(A/B)^2<0 on C3′ and applies fixed rational points C3′(Q)={∞,(0,0)} from C35-12. Full C35-12 mathematical te |
| 26 | `R369→row368` | **原著あり** | [原数学本文](../../materials/original-source-exclusions/row368/STAGE35EX_R3_07_ROW368_LOW_WARD3_WARD5_TRANSFER_20261105.md)：row369 §2 adopts row368's composite division polynomial Φ7=w7²−w6w8 and Ward factor/resultant descent; row368's source includ |
| 27 | `R376→row370` | **原著あり** | [原数学本文](../../materials/original-source-exclusions/parents/row370-PROOF.md)：row376 concludes signed +30 exclusion by row370 six-square/real interval base, then row374 even valuations + row375 all-real  |
| 28 | `R376→row374` | **原著あり** | [原数学本文](../../materials/original-source-exclusions/parents/row374-PROOF.md)：row376 needs row374 all finite places even valuations and maximal-order/discriminant. The fixed number field and local condit |
| 29 | `R376→row375` | **原著あり** | [原数学本文](../../materials/original-source-exclusions/parents/row375-PROOF.md)：row376 narrows real interval via row375 surjective signs at all 7 real embeddings and narrow=ordinary Hilbert class field. ro |
| 30 | `R381→row373` | **原著あり** | [原数学本文](../../materials/original-source-exclusions/parents/row373-PROOF.md)：row381 true 2-Selmer complete unit part and local 2-adic/real membership directly uses row373 53-dim local Kummer model and 5 |
| 31 | `R381→row374` | **原著あり** | [原数学本文](../../materials/original-source-exclusions/parents/row374-PROOF.md)：row381 uses row374 even valuations and all finite unrestricted except 2, explicit maximal order. The full unit Selmer 9+c_Cl  |
| 32 | `R381→row375` | **原著あり** | [原数学本文](../../materials/original-source-exclusions/parents/row375-PROOF.md)：row381 uses row375 unit sign full rank and 8 independent rational classes; source row375 says rank≥8 and required rank≥10 if  |
| 33 | `R385→row381` | **原著あり** | [原数学本文](../../materials/negative30-mw-selmer/row381/PROOF.md)：row385 imports row381 full 55-dimensional unit image, Selmer space 9+c_Cl and Hecke GRH conditional c_Cl=0 but concludes 4-li |
| 34 | `R385→row384` | **原著あり** | [原数学本文](../../materials/negative30-mw-selmer/row384/PROOF.md)：row385 imports row384 fixed δ★ representative and two-character conditional upper, and then proves class functional/4-lift ne |
| 35 | `R392→row391` | **原著あり** | [原数学本文](../../materials/classgroup-and-different/proofs/row391.md)：row392 uses row391's already present principal relations and finite remaining directions; row392 adds 222→193, different and  |
| 36 | `R393→row392` | **原著あり** | [原数学本文](../../materials/classgroup-and-different/proofs/row392.md)：row393 explicitly inherits row392's 193 formal residual directions and different δ, then computes a smaller norm bound. 181 i |
| 37 | `R393→EXTERNAL_DE_LA_MAZA` | **外部Gate Dへ移管** | [原数学本文](./ROW393-PRIMARY-THEOREM-GATE.md)：row393 uses de la Maza Math Comp 71(240)(2002) Theorem 1 and corollary to claim universal class representative norm B<2^94. E |
| 38 | `C183→R5-C220` | **原著あり** | [原数学本文](./proofs/foundations/R5-C220.md)：C183 §4 accepts R5 C220 fixed signed +12 HIGH real y-sign veto only after original C220 curve equation typo is corrected via  |
| 39 | `C220→C181` | **原著あり** | [原数学本文](./proofs/foundations/C181.md)：R5 C220 §Theorem B uses C181 inherited LOW-empty/high-only envelope and older C130 two real windows to upgrade z≥18 sign veto |

**１行だけの移管は旧#37 `R393→EXTERNAL_DE_LA_MAZA`**。row393の著者数学本文は保存済み。外部定理の**原文の条件を未確認**なので「数学原著あり＝外部定理適用PASS」という扱いはしない。Gate C（原著の所在と親の分類）は**PASS**、[Gate Dの原典監査](ROW393-PRIMARY-THEOREM-GATE.md)だけ**OPEN**にする。前回の45追加点検は参考の別の命題辺であり、今回の元39行の代用品ではない。

## Gate E：末端７つから原著を一巡（著者数学本文の所在はPASS）

[**R3-07六終端・R2-01一終端の原数学本文所在と使用条件を通した最終記録**](PR1860-SEVEN-TERMINAL-SOURCE-CHAIN-CHECK.md)と[機械可読版](PR1860-SEVEN-TERMINAL-SOURCE-CHAIN-CHECK.json)。R3 row393（−30）、row367（±18）、row368（Ward3/5）、row369（Ward7）、row376（+30）、C183（+12）、R2 C189/C187/S270の**７／７**で、現行で必要な**著者数学原著本文の未収載は０件**。これは原著の所在・条件付き命題の通し照合であって、算術証書・外部標準定理を全て独立再現した数学監査ではない。

## Gate DだけOPEN：有限２つの外部定理

- **D-1 / de la Maza**：row393のノルム上界`B<2^94`に使うTheorem1・系の原文と`admissible`、Gamma/Mellin規約、追加仮定の照合。[未確認ゲート](ROW393-PRIMARY-THEOREM-GATE.md)。
- **D-2 / Mordell**：最古Branch B§15.4に必要な整数四次式 `u⁴+u²v²+v⁴=w²` の非自明解不存在。歴史原稿の引用は `L. J. Mordell, Diophantine Equations, Chapter4 Eq.7′` までだが、**一次定理原文の照合は未了**。[§15移植・分岐監査](PR1860-BRANCHB-PARTITION-AND-TORSION-PARENT-CHECK.md)。

**Gate A/B/C/E=PASS。Gate D=OPEN（２件）。全体の第２周はまだ完了ではない。** 外部原典が読めない場合、推測でPASSを付けない。必要文献の原命題を照合する以外の新しいR2/R3研究、99ルート、外部の無関係定理をGate Dへ増やさない。

## 追加原著が見つかった場合の厳密な停止規則

起点をR3-07のrow393到達・既知LOW排除とR2-01のC189/C187/S270に**固定**する。新たな文書が見つかっても、**この起点の既に使っている数学命題の親であることが本文の式から示せる場合のみ**追加する。その場合、**具体的な依存辺を１行だけ増やして閉じる**。旧番号順、99研究ルート、旧NEXT、個別の研究史の横展開では増やさない。

最後に起点から１回通して、使用している数学親の**未判定０・必要本文の未収載０・外部定理の必要条件未照合０**になったら、**その時点で第２周を完了と宣言**する。翌日新しい無関係文書を見つける可能性を理由に終わらない、という扱いはしない。残った数学研究のOPENとは区別する。

**最新：Gate A/B/C/E=PASS、DだけOPEN（外部一次定理２件）。したがって第２周はまだ完了ではない。** この２件が一次原典の成立条件まで確認できれば、固定第２周を終了判定する。
