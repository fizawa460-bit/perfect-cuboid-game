# PR #1860｜第２周の有限な終了条件と全件固定台帳

**作成：2026-11-09｜対象はR3-07とR2-01のみ｜状態：NOT COMPLETE / Draft / DO NOT MERGE。**

これまでの「新しい数学原著が見つかったら際限なく探索を広げる」管理は終了条件がなく不適切だった。**第２周を終わらせるための固定母集団と完了条件を定義する。** 本表は後付けの一般研究NEXTでなく、PR #1854から#1860への**数学的原著所在・依存鎖の移植確認**専用。

## 終了の定義（５つ全部PASSなら終了）

| Gate | 何を全件確認するか | 現在 | 完了に必要な残作業 |
|---|---|---|---|
| A | #1854でDriveのみとした**23件すべて**に必要性判定・収載先／不要根拠を付ける | **PASS（23/23）** | なし：12本コピー・11件は移植しない理由付き |
| B | その23件**以外**に見つかった親原著10本＋既知原本の未収載§15証明１本の本文・場所を確定する | **PASS（11/11）** | なし：10本GitHub SHA照合、§15原著区間一致 |
| C | 第１周の**39引用辺全件**に「使った数学命題・実際の原著／後続再証明・適用条件・終端判定」をつける | **OPEN** | 前回の45件の追加点検を39行へ割り当て、未判定行を**０件**にする。45という件数だけでは全件完了ではない |
| D | 現在の証明に必要な外部定理を、原命題の内容・成立条件・使う式と照合する | **OPEN（明示２ゲート）** | row393のde la Maza、Branch B §15.4のMordell四次式。C187の155/197にBérczes定理を無理に加えない |
| E | R3 row393/row367/368/369/376/C183、R2 C189/C187/S270を起点に**親を端から端まで１回通読照合**する | **OPEN** | 使用中の必須原著で「本文がない」「同等証明不明」「条件が違う」を**０件**にする |

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

## 第１周39辺の終端判定表と終了させる具体的方法

[機械可読チェックリスト](PR1860-SECOND-PASS-EXIT-CHECKLIST.json)には、**元の39行を番号・親・子・元ファイル・元分類ごと固定収録**。その１行ごとに次のいずれかを**根拠つき**で付ける：

- **PROOF_SOURCE_PRESENT**：必要命題と数学原著がこのGitHubのどの本文・節にあるか特定。
- **EQUIVALENT_PROOF_PRESENT**：旧数学は後続で再導出済み。後続の実際の証明箇所を特定。
- **NOT_LOAD_BEARING**：研究履歴・撤回・固定例・別受信枝など、現行の２終端では使用しない根拠を示す。
- **EXTERNAL_THEOREM_VERIFIED**：引用する外部定理の**原文命題・必要仮定・この使用箇所での適用**を確認し出典を記す。
- **BLOCKED_MISSING_MATH**：必要なのに数学本文・同等証明が無い。原著を収載するか証明が不足と明記。**この状態が１件でもあれば第２周は終われない**。

今回の既存45件の監査を使って39行に割り当てる。**当該39行全部の終端記録を現在はまだ作っていないので、Gate CはOPEN**。これは「39件の証明が全部欠けている」という意味ではなく、**チェック済みと未チェックを区別する最後の突合せが未実施**という意味。

## 追加原著が見つかった場合の厳密な停止規則

起点をR3-07のrow393到達・既知LOW排除とR2-01のC189/C187/S270に**固定**する。新たな文書が見つかっても、**この起点の既に使っている数学命題の親であることが本文の式から示せる場合のみ**追加する。その場合、**具体的な依存辺を１行だけ増やして閉じる**。旧番号順、99研究ルート、旧NEXT、個別の研究史の横展開では増やさない。

最後に起点から１回通して、使用している数学親の**未判定０・必要本文の未収載０・外部定理の必要条件未照合０**になったら、**その時点で第２周を完了と宣言**する。翌日新しい無関係文書を見つける可能性を理由に終わらない、という扱いはしない。残った数学研究のOPENとは区別する。

**この文書作成段階では Gate A/B がPASS、C/D/E がOPEN。したがって第２周はまだ完了ではない。** 以後はこの有限のゲートの残数と該当IDで報告する。
