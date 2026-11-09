# Stage35EX研究開始からP23現行2ルートへの最小研究系譜

> **PR #1854の概要固定版（2026-11-09）。** Stage35EXをGoogle Driveで開始した地点から、研究史上どの成果を経由してR3-07（LOW、row393）とR2-01（MID/HIGH、同時点）に至ったかを、**最短で読める研究成果のまとまり**として案内する。既存原著はそのまま残す。**本書は新しい数学的証明・厳密な最小依存DAG・独立監査PASSではない。**
>
> **今回（1周目）：概要と既存GitHub/Drive所在だけを保存。** 証明原著・計算証書の新たな一括収載はしない。**2周目：本書のクリティカルパスで必要と確定した欠落原著だけを、原則として別PRに収載。** 別PRはこの段階では作成しない。

## 1. 研究の起点と時系列の節目

| 節目（日本時間） | 史料により確認した事項 | このPRへの扱い |
|---|---|---|
| **2026-09-26 07:27頃** | Google Driveに`35ex-01`〜`35ex-29`等の初期フォルダが作成された。Stage35EXという管理単位の**確認できた開始地点**。 | 研究史の起点を記録。全フォルダ移植は不要 |
| **2026-09-26 20:50** | 確認できた最初期の原稿 [three-direction common E[2] adapter](https://drive.google.com/file/d/1iK0lKzTSQd_8IIQ7TAJsRF0A8YiHKKCI/view)。旧Goal4系を継承する初期検討。 | 歴史上の分岐。**現行の必須数学親とは未認定** |
| **2026-09-29** | E3 generic MW・物理Kummer原著、Branch Bの旧原著へ進む。 | **現行sourceの共通基礎候補** |
| **2026-10-03以降** | S121/Section13のgeneric・finite odd側と、物理四根/分母の側が分岐して進展。 | generic/finite odd枝を無条件に主鎖へ混ぜない |
| **2026-10-08〜09** | S253、S263、S268、S269、S270等。signed Ward・四根・Gaussian・TOPが現在の形に接近。 | **両ルート共通の主鎖** |
| **2026-10-21** | R1/R2/R3の個別レーン索引へ分割。後日C195で既存source条件を再構成。 | 主鎖から現在の担当ルートへ分岐 |
| **2026-11-08時点** | R3-07 LOW row393、R2-01 MID/HIGH C189等の使用状態。 | **PR #1854の終点。R3 row394以降へ進まない** |

開始日時は[Driveの最初期原稿](https://drive.google.com/file/d/1iK0lKzTSQd_8IIQ7TAJsRF0A8YiHKKCI/view)および初期フォルダの作成メタデータに基づく。これは「Stage35EXより前に研究がなかった」ことを意味しない。先行Stage35・Goal4系は**引用が必要な具体的命題だけ**辿る。

## 2. 最短の研究系譜（歴史の全件目録ではない）

```text
[2026-09-26] Stage35EX開始
  ├─ E2 / Prym / Brauer / 別の降下・旧障壁：研究史の側枝
  │       └─ 現在の2ルートに直接必要な命題を使わない限り移植不要
  └─ 完全直方体の正の有理source・正規化・原始標識
       └─ [2026-09-29] 物理E3 / 選択四平方 / Branch B
             ├─ generic MW / Section13 / Section16 / S121〜
             │     └─ 特定の後続命題が実際に引用するときだけ回収
             └─ 四根・分母・元signed source
                   S230/S231/S232 → S233/S237/S240/S243
                      → S251/S252/S253 → S263/S264/S268/S269
                      → S270、後日のC195 source再構成
                              │
                 ┌────────────┴─────────────────┐
                 ▼                              ▼
          [R3-07 / LOW]                   [R2-01 / MID/HIGH]
          旧LOW mask・±18               protected四TOP+ALL PROPER
          Ward3/5/7・±30                C174/C175/C185等の高さ入力
          row367/368/369/376            155/197必要下界 → C189
          → row393                      strict相関上界はOPEN
          −30無条件排除はOPEN
```

**読み方：** これは研究の成果を必要最小限の塊に圧縮した**ナビゲーション**であり、各隣接番号間に独立の論理的依存が必ず存在すると主張しない。とくにC195は2026-10-28の**後日の再構成**で、S253等の発祥点ではない。S121/Section13のgeneric枝やSection16のfinite-odd枝は、rank-independentなS232〜S270主鎖の全命題に不可欠とは限らない。

## 3. 共通の幹：優先して保護する原証明

| 役割 | GitHubにある代表原著・参照 | 2周目の判断 |
|---|---|---|
| 研究対象・正の有理曲面 | [35EX-21](../../35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md) | **既存再利用**。初期探索全原稿は不要 |
| 原始source・標識 | [35EX-31](../../35ex-31/primitive-source-marking-endpoint-equivalence.md) | **既存再利用**。E3との標識・signed軌道の移送は未証明 |
| 選択物理四平方→E3 | [E3 physical original](proofs/earliest-foundations/E3-selected-physical-kummer.md)、[S231](proofs/active-ancestors/S231.md) | **既存再利用**。generic rankの特殊化を勝手に導入しない |
| 四根の整数liftと分母条件 | [S230](proofs/active-ancestors/S230.md)・[S232](proofs/active-ancestors/S232.md)・[S243](proofs/active-ancestors/S243.md) | **共通中核**。直接使用補題単位で判定 |
| signed Ward / Gaussian / source再構成 | [S253](proofs/active-ancestors/S253.md)・[S263](../../materials/original-source-exclusions/parents/S263.md)・[S268](proofs/C195-upstream/S268.md)・[S269](proofs/C195-upstream/S269.md)・[C195](proofs/C195-canonical-source.md) | **共通中核**。同じ原著をR2/R3に二重保存しない |
| 四TOP＋ALL PROPER | [S270](proofs/foundations/S270.md)・[S251](proofs/active-ancestors/S251.md)・[S252](proofs/active-ancestors/S252.md) | **R2主鎖に必須の入力**。外部Bérczes定理の適用は別途確認 |
| 最古の枝の原著 | [Branch B Section13](proofs/earliest-foundations/BranchB-Section13.md)・[Section16（訂正を含む）](proofs/earliest-foundations/BranchB-Section16.md)・[E3 generic MW](proofs/earliest-foundations/E3-generic-MW.md) | **既存再利用**。現行結論の実際の引用なしに必須親と数えない |

[35EX-21からE3への式レベルの対応と未確定の標識・符号bridge](PR1854-EARLIEST-MATH-FOUNDATIONS.md)は別紙。ここでの「既存再利用」は**原著の所在**であり、完全数学監査の成功を意味しない。

## 4. 現行の二股：終点と必要な最新側枝

### A. R3-07（P23-LOW、row393まで）

- 共通source → [元source排除](../../materials/original-source-exclusions/README.md) → **±18**の[Selmer原著群](../../materials/selmer18-parent-chain/README.md)、**Ward3/5/7**の使用補題、**±30**の[MW/Selmer原著群](../../materials/negative30-mw-selmer/README.md) → [row393を含む後段](../../materials/classgroup-and-different/README.md)。
- **残すべき最新側枝**：row367（±18）、row368/369（Ward3/5/7）、row376（+30のみ）、row377〜393（−30の最新研究、特に使われる訂正・適用範囲）。各行を全部複写するのではなく**現行主張に必要な原証明・訂正・引用先**を優先する。
- **停止位置**：[R3原著案内](PR1854-R3-07-CHAIN.md)、[row393](../../materials/classgroup-and-different/proofs/row393.md)。**−30の無条件排除・全LOWの排除は未証明。** row393の形式残余181を真の類群階数とみなさない。de la Maza外部定理の適用原典照合は未完。

### B. R2-01（P23-MID/HIGH、同時点）

- 共通source＋S270 → [C175](proofs/active-ancestors/C175.md)・[C185](proofs/active-ancestors/C185.md)等 → [155/197必要下界の原著](proofs/R2-uniform-thresholds.md) → [C189の従属採択](proofs/active-ancestors/C189.md)。
- **残すべき最新側枝**：S275/S318等の**現在のprotected GOOD/critical-Hへの適用を変える補正**、C160→C185 exact係数の引用範囲、C189の採択・撤回・条件を示す必要部分。
- **停止位置**：[R2原著案内](PR1854-R2-01-CHAIN.md)。**同じoriginal sourceの四TOP＋全PROPERを同時に扱うstrict 75%未満の相関上界は未証明**。下界をMID/HIGH排除と扱わない。

## 5. 2周目の収載ルール：ファイル数ではなく「必要な主張」を数える

**P0：クリティカルパスの原証明**。現在の有効なR3/R2命題を一つ選び、その成立に実際に使用する定理・補題を逆向きに確認する。**既存GitHubに原文または完全に同値な証明があれば再アップしない。** 欠けている数学原著だけを2周目の別PR候補にする。

**P1：現行の正確な範囲を守る訂正資料**。撤回、正誤、量化子、符号、primitive/source同一性、条件付き/無条件の違いを**現在の結論が誤用されない範囲だけ**付ける。最新の重要な障壁はここに入り得るが、「新しいから」だけで追加しない。

**P2：外部の数学定理・大容量の根拠**。S252のBérczes原典、row393のde la Maza原典は**正確な定理番号・使用命題・適用仮定・出典リンク**を記録。大容量の計算ZIP・入力・ログ・証書はGoogle Driveを参照してよい（必要な検算状態と所有元を明記）。論文やDrive全文の無断コピーを前提にしない。

**原則対象外**：古い探索で失敗したPrym、Brauer、generic非写像、未使用の有限奇数位数枝、枝分かれした旧Section全体、C124/C192/C193等の「歴史的には存在するが現行引用がない」原著、昔の壁・旧NEXT・運用ログ。**古い障壁であっても現在の採用命題がその否定/訂正を使う場合だけ該当箇所を再評価する**。

### 2周目の1件ごとの最低記録

| 項目 | 必要内容 |
|---|---|
| 採用先 | R3-07 rowまたはR2-01の**どの有効命題**に必要か |
| 依存の形 | 「命題Aが補題Bのどの部分を使うか」。単なる前後関係なら**歴史のみ** |
| 原著 | GitHubパス、またはGoogle Driveの原著URL・題名・作成日 |
| 状態 | **既存GitHubで充足／Drive参照で足りる／数学本文の新規収載が必要／外部原典検証待ち／不要** |
| 防火壁 | 条件付き、未検証、撤回、符号、同一source、未排除部分 |
| 容量 | 本文は必要時GitHubへ。計算現物は原則Drive参照可能 |

ファイルの件数・C/S番号の連番・過去の監査数は必要親の数ではない。**「GitHubにない」だけでアップせず、現在の定理に必要な証明が欠けているときだけアップする。**

## 6. このPRと次回の境界

- **PR #1854（現段階）**：本概要を追加し、既収載の資料・元原著・索引を**そのまま維持**。新たな数学原稿や計算現物の一括搬入はしない。Draft/open/unmerged維持。
- **2周目（別PRを作る場合）**：現在のP0/P1だけについて、①現行主張を固定→②原著使用箇所確認→③GitHub既存重複確認→④必須欠落だけ収載→⑤Drive/GitHub対応表と読戻し、の順で行う。**別PRは今は作らない。**
- **研究停止**：R3 row394以降、新しい数学証明、Google Drive研究R0/NEXT、正式GitHub MAIN-STATE、mainを変更しない。主張をPASSへ昇格させない。

**中心原則：研究史の時系列を保存するために古い「壁」を全部再生産しない。現行の正しい数学結論を再構成するために必要な、最短のsource＋定理＋最新の適用条件を優先する。**
