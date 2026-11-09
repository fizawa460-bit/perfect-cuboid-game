# PR #1860｜R3-07・R2-01 固定７終端の数学原著所在・親鎖最終一巡

**2026-11-09｜Gate E・著者数学原著の所在チェック｜INTERNAL SOURCE CHAIN PASS / EXTERNAL PRIMARY GATE D OPEN**。証明の**収載所在・使う命題・量化子の分岐条件**を点検した結果。**独立数学検証PASS、研究数学の完了、PRマージを意味しない**。

## 固定した７終端と最後の依存鎖

| 終端 | 既存数学原著を再取得／親を照合 | 必要な未収載の**著者**数学本文 | 定理自体の未解決／外部残務 |
|---|---|---|---|
| R3 row393（−30） | [row393](../../materials/classgroup-and-different/proofs/row393.md) → row392/391、row385、row381、row375/374/373/370。row370〜393の**24原著**は[全件保存・監査](PR1860-R3-MINUS30-PARENT-CHECK.md) | **０件** | [de la Maza原典の適用](ROW393-PRIMARY-THEOREM-GATE.md)がGate D未照合。row381 GRH条件付き。row393の181は**形式残余でCl/2ではない**。無条件−30排除は未証明 |
| R3 row367（±18） | [row367](../../materials/original-source-exclusions/row367/REPORT.md) → row364/365/366、[R1-255/256](proofs/R3-18-upstream/R1-255-fourward-cover-original.md)、row339、row340/341/342、row346〜349、row353/355、row363等、[使用命題監査](PR1860-R3-USED-LEMMA-CHAIN-CHECK.md) | **０件** | 固定±18の内部排除の数学独立監査は新たにPASSさせない。全LOW排除ではない |
| R3 row368（Ward3/5） | [row368](../../materials/original-source-exclusions/row368/STAGE35EX_R3_07_ROW368_LOW_WARD3_WARD5_TRANSFER_20261105.md) → S263/264、[S321](proofs/active-ancestors/S321.md)、[C118固定X点分類](../../materials/original-source-exclusions/parents/C35-118/export.txt) | **０件** | 同じ標識付き基底の必要方向。全物理sourceの無条件不存在にはならない |
| R3 row369（Ward7） | [row369](../../materials/original-source-exclusions/row369/STAGE35EX_R3_07_ROW369_LOW_WARD7_TRANSFER_20261106.md) → S321/322、C35-11、[C35-12](../../materials/original-source-exclusions/parents/C35-12/PROOF.md)の４円盤数学、row368の合成式 | **０件** | C35-12に数学本文はあるがColeman計算の独立再演は別ゲート |
| R3 row376（+30） | [row376](../../materials/original-source-exclusions/row376/PROOF.md) → row370/371/372/373/374/375（同じ−30研究基底） | **０件** | **+30限定**。−30は残る |
| R3 C183（+12） | [C183](proofs/foundations/C183.md) → [R5-C220](proofs/foundations/R5-C220.md)、[R5-C224訂正](proofs/foundations/R5-C224-erratum.md)、[C181](proofs/foundations/C181.md)、旧C130の実区間 | **０件** | C220原文の誤曲線式を採用しない。+12 HIGH限定、−12には拡張しない |
| R2 C189（C187・S270） | [C189](proofs/active-ancestors/C189.md) → [C187 155/197](proofs/R2-uniform-thresholds.md)、[S270](proofs/foundations/S270.md)、[C185 owner](proofs/active-ancestors/C185-R2-prime-cut-original.md)、[C160 owner](proofs/active-ancestors/C160-R2-strong-gcd-original.md)、S268/S258/S275/S318、S252§3–4、C174/C175、R5 C157、[R2命題監査](PR1860-R2-PRIMECUT-LEMMA-CHAIN-CHECK.md) | **０件** | C187は**155/197下界**。必要な75%未満の相関上界ではない |

**共通祖先**：[E3と同じlabelled/原signed groupの橋](PR1860-E3-LABEL-INDEXED-BRIDGE-AUDIT.md)、[Branch B §15の追加原証明](proofs/earliest-foundations/BranchB-Section15-torsion.md)、S193/S194、§16/17撤回。これはR2・R3の**indexed原sourceを仮定した条件付き数学**の先祖であって「全物理点がindexed Branch Bへ入る」という別の全域研究命題を証明したものではない。

## 元39依存辺の最終行別決定

[**確定した39行台帳**](PR1860-SECOND-PASS-EXIT-CHECKLIST.json)の分類：
- **33行**：必要な著者数学原著の使用命題と既存GitHub本文を特定。
- **２行**：後続の数学本文が同じ必要命題を再証明／明示しているので旧原著を重複移植しない。
- **３行**：固定された２終端の直接数学親ではない（旧例・別の量化／有限商枝）。
- **１行（旧#37）**：row393→de la Mazaの**原典適用だけGate Dへ明示移管**。row393著者数学本文はGitHubにある。欠けた外部原典の**適用**が未検証なのに「著者数学原著が欠落」と二重計上しない。

**合計39/39に一意の終端分類**。Gate Cは**原著所在・依存命題の裁定としてPASS**。初回外の10新原著＋既知原本§15を収載し、元23は12コピー・11判断というGate A/BもPASS。**Gate Eは７固定終端の内部著者数学原著所在と適用対象の一巡PASS**（GitHubの原著保存・先行監査記録に依存、全計算独立再演ではない）。

## まだ「第２周完了」としない１ゲート：外部数学原典の適用

[外部Gate D](PR1860-SECOND-PASS-EXIT-CHECKLIST.md)の**２件**に限定。

1. **de la Maza Theorem1+系**：row393 `B<2^94` 用。一次文献のadmissible関数、Gamma/Mellin符号・規格化とGRH等の追加条件を原文照合できていない。[既存未確認箇所](ROW393-PRIMARY-THEOREM-GATE.md)に整理済み。
2. **Mordell古典四次式**：最古BranchB §15.4の `u⁴+u²v²+v⁴=w²` 非自明整数解不存在を引用する箇所。最古Branch A原著は`L. J. Mordell, Diophantine Equations, Ch.4 Eq.7′`と書誌を挙げるが**一次原典本文は確認していない**。[監査](PR1860-BRANCHB-PARTITION-AND-TORSION-PARENT-CHECK.md)。

一次本文が取得できない限り、仮定や結論の一致を**推測でPASSにしない**。この２件は別々の有限番号で管理する。無関係な99ルートの探索・新しい数学問題の解決を第２周の完了条件に追加しない。**PR #1860はDraft、DO NOT MERGE、全体第２周未終了**。
