# PR #1854｜R3-07 row393／R2-01 の証明鎖・端から端までの粗い全体図

**今回の作業状態：BROAD_CHAIN_MAP_COMPLETE / SOURCE_TEXT_PARTIAL_REVIEW。** ユーザー指定の2ルートを、細かい数学的必須性の逐一監査より先に、**到達点から最も深く確認できる既存証明本文まで**つないだ。これは「案内・元原著収載の粗い鎖」ができたという意味で、数学的正しさの独立証明や原典仮定の全面PASSではない。計算証拠は後回し。

## 0. C195より前の研究と、時系列／数学的依存の分離

**確認結果：S253が先、C195が後。** 初版ではC195を元source研究の始点に見える場所へ置いたが、それは研究時系列として不正確。日時はGoogle Drive原著の作成時刻または記録済み最終更新時刻を日本時間に換算。

| 原著 | 日時（JST） | GitHub原著と役割 |
|---|---|---|
| S253 | 2026-10-08 17:25 作成 | [保存済み：二つの必要分母役割](proofs/active-ancestors/S253.md) |
| S263 | 2026-10-08 23:35 作成 | [保存済み：元signed軌道の隣接整数Ward条件](../../materials/original-source-exclusions/parents/S263.md) |
| S264 | 2026-10-09 00:10 更新 | [保存済み：偶奇・符号条件](proofs/foundations/S264.md) |
| S268 | 2026-10-09 07:57 更新 | [保存済み：元分母のreduced norm](proofs/C195-upstream/S268.md) |
| S269 | 2026-10-09 08:14 更新 | [保存済み：Gaussian四次式とsigned POINT](proofs/C195-upstream/S269.md) |
| S270 | 2026-10-09 08:24 更新 | [保存済み：4つのTRUE TOP＋全PROPER](proofs/foundations/S270.md) |
| C193 | 2026-10-28 13:54 作成 | [Drive原著のみ確認](https://drive.google.com/file/d/1D8QNpX2k-O36w76ZoTqbVDdUFJClNnLj/view)。補助曲線間generic写像の障壁 |
| C194 | 2026-10-28 14:31 作成 | [保存済み：C193のgeneric non-mapを強める](proofs/C195-upstream/C194.md) |
| C195 | 2026-10-28 15:00 作成 | [保存済み：actual sigma-squareからcanonical整数sourceを後で再構成](proofs/C195-canonical-source.md) |

**時系列の先後と、証明に必要な親は別。** S253は古い独立した条件付き必要定理で、C195がS253を新しく証明したわけではない。C195の直接の正方向入力はS233/237/240、S268/269、R1訂正、C174、S289/290等。C193/C194はgeneric補助曲線写像に関する禁止・障壁を扱い、元sourceの正方向の全証明の必須前提とは自動判定しない。

**収載境界：** Stage35EX公開ツリーの1529個のファイルパスを確認。C195前のS系列、C194は多数保存済みだが、**C193・C192・C124という識別子を持つ独立原著ファイルはGitHub上に未確認**。Driveの原著は[C193](https://drive.google.com/file/d/1D8QNpX2k-O36w76ZoTqbVDdUFJClNnLj/view)、[C192](https://docs.google.com/document/d/1J5VhsT2pPyKuy7ooumpsf--WSoJPWhuCfEIfjx_wPAs/edit)、[C124](https://docs.google.com/document/d/1VLG7UBzuh07DIkkzsO5iL3kseCnCBtgMSSiE3lpu5fU/edit)。いずれも今の2ルートの不可欠親かどうかは未判定。歴史の全C番号を移植義務とはしない。

## 1. R3-07 / LOW / row393

```text
古い研究系列 S253(10/8) → S263/S264 → S268/S269 → S270(10/9)
  ↓ 後日の元source再構成 C195(10/28)
  ※ 矢印は概略の研究時系列。各矢印が数学的な直接依存とは限らない
  ├─ LOW旧マスク C181・C183(+12)・R5-C220／C224訂正
  │     └─ 元LOWの残数表（旧数と現行数は区別）
  ├─ ±18：row339固定 C₂(genus17)
  │     → row342(rank≥6), row343(S36), row345(局所Kummer)
  │     → row350(fake実符号), row351(true→fake), row352(rank≥7)
  │     → row361/363/364(true Selmer 9), row365/366, row367(±18排除)
  ├─ Ward3/5/7：S238(2進) + S263/S264
  │     → S320(周辺 q5/q7)・S321(W5/W7)・S322(K/L)
  │     + C118・C35-11/12(固定曲線有理点)
  │     → row368(Ward3/5) → row369(Ward7)
  └─ ±30：row370–375(元source必要条件・階数・Kummer)
        ├─ row376：+30だけ排除
        └─ −30：row377–384（row381はGRH条件付き排除）
             → row385–388(Selmer4/類群・飽和)
             → row389–392(主関係／不同)
             → row393(B<2^94著者式、形式残余181)
```

**最終結果の適用境界：** R3はLOWで9絶対指数／16 signed枠が残る。**−30は無条件には排除されていない。** row393の181は真の類群Cl/2階数や無条件上界ではない。B<2^94に使用したde la Maza原典Theorem 1と直後の系の条件・正規化の独立照合は未完。全LOW、Branch BはOPEN。

**今すぐ辿れる本文入口：** [R3管理原文](../routes/R3-07.md)、[row393原著](../../materials/classgroup-and-different/proofs/row393.md)、[−30の行別数学本文](../../materials/classgroup-and-different/README.md)、[−30のrow370–384](../../materials/negative30-mw-selmer/README.md)、[LOW採用排除本文](../../materials/original-source-exclusions/README.md)、[±18の数学親群](../../materials/selmer18-parent-chain/README.md)。

**今回接いだ部分：** [S238](proofs/active-ancestors/S238.md) → [S321](proofs/active-ancestors/S321.md) → [S322](proofs/active-ancestors/S322.md)。[S320](proofs/active-ancestors/S320.md)はS321の歴史的親でq5/q7のH素数問題を扱うが、**時間順の「前Section」と数学的必須前提は同一ではない**。[row342](proofs/R3-18-upstream/row342.md)、[row343](proofs/R3-18-upstream/row343.md)、既存の[row345原著](../../materials/selmer18-parent-chain/objects/01d05437afc6fa87-PROOF_C2_TRUE_LOCAL_KUMMER_DIMENSIONS_JA.md)、[row350](proofs/R3-18-upstream/row350.md)、[row351](proofs/R3-18-upstream/row351.md)、既存の[row352原著](../../materials/selmer18-parent-chain/objects/5fd888550f0b7d57-PROOF_C2_INFINITY_RANK7_AND_TRUE_FAKE_KERNEL_JA.md)を直結。[row364以降の継続](PR1854-R3-07-CHAIN.md)へ接続する。

## 2. R2-01 / MID/HIGH / 同じ停止時点

```text
元signed source：旧S253系列・S268/S269を後日C195が統合
  ├─ 旧々祖先 S121–126 → S190–202（finite-oddの範囲は限定）
  │       → S213–235；S230のA/C点だけの付値 → S232
  ├─ 同じ四根：S233・S237・S240 → S243
  │       └─ S242(8,15,17 rank2)は固定例の脇道
  ├─ S232・S243 → S251（S250次数8結果を本文に再述）
  │       → S252（外部Bérczes定理）
  │       → S253–262・S263–267 → S270(TRUE四TOP＋ALL PROPER)
  ├─ S275 / S316 / S318（protected GOOD/critical-Hの補正）
  └─ 旧高さ C174・C175 ＋ C160(旧strong-gcd)・C185
         → R2 C187全基底 155/197 下界
         → C189 R0従属採択
```

矢印は**研究成果が使用・継承する大枠**であり、隣接Sectionをすべて必要十分な数学的親と認定した厳密DAGではない。特にS121は旧Section13の源写像を継承しており、そこから先の物理被覆の全面監査を済ませた意味ではない。

**最終結果の適用境界：** C189採択はTRUE protected四TOP等の**必要下界**。R2-01が目標とする、同じ元sourceで四TOP＋全PROPER uncapped ordinary βを相関させた**strict 75%未満の上界はOPEN**。これまでの下界の移植をMID/HIGH排除の証明と呼ばない。

**今回接いだ部分：** [S230原著](proofs/active-ancestors/S230.md) → [S232](proofs/active-ancestors/S232.md)、[C160原著](proofs/active-ancestors/C160.md) → [C185](proofs/active-ancestors/C185.md) → [C189](proofs/active-ancestors/C189.md)。ただし**C160の旧strong-gcdとC185が必要とするexact係数式の同値性は別の数学チェック**。[S242固定例](proofs/active-ancestors/S242.md)は研究済みとして保存するが全基底定理の必須親とは数えない。[S250の結果はS251本文で再述](proofs/active-ancestors/S251.md)されているので原著の重複は急がない。

**全祖先を辿る先：** [60件の祖先出典・親ID](ACTIVE-ANCESTOR-SOURCE-MAP.json)・[長い依存表](ACTIVE-ANCESTOR-DEPENDENCY-MAP.md)、[2ルート源の接続](PR1854-R2-01-CHAIN.md)、[155/197の原著](proofs/R2-uniform-thresholds.md)、[C195元source原著](proofs/C195-canonical-source.md)。

## 3. 端まで辿って初めて見える境界

| 状態 | 内容 | 何をしないか |
|---|---|---|
| **GITHUB_SOURCE_RETAINED** | 既存原著に加え、今回11本の数学本文をGoogle DriveからGitHubへ保存。[原著・Git blob対応](PR1854-BULK-ORIGINAL-SOURCES.json) | 追加11本を11独立定理・11必須ファイルとは扱わない |
| **ROOT_GRAPH_CLASSIFIED** | R2 C189の従来依存表は79識別子に到達。もとの70収載ID＋残り9識別子を新収載・既存別名・本文内再述・外部境界のいずれかに整理。[対応表](PR1854-ENDTOEND-CHAIN.json) | 79を必要定理数や完了率の分母にしない |
| **OLDER_ORIGINAL_BOUNDARY** | S194が古いSection16の非平方/4位数不在補題を引用。正確な原典位置は未発見。S196の古典的plus-sign降下本文は収載済み | 別のSection16現行K-support定理を誤って同一視しない |
| **PUBLISHED_THEOREM_PENDING** | S252のBérczesの高さ定理、row393のde la Maza定理。適用仮定・記号の原典照合が未完 | 有限数値検算のPASSを外部定理適用のPASSと呼ばない |
| **MATH_SCOPE_REVIEW** | S250のS251内再述、C160→C185の精密適用、R3でさらに深いrow344〜349/証書の原著境界。固定例・歴史・必須親を分ける個別監査は後段 | 未検証を黙って済みにしない |
| **COMPUTATION_DEFERRED** | コード、元ZIP、計算入力と再演証書の全面確認はユーザー指示で保留 | 数学本文の収載数へ混ぜない |

## 4. この回の「完成」の定義

**完了：2ルートの最後の到達点から、既存の最深部資料と今回補った直接欠落までの**粗い研究・原証明の鎖（入口、連結先、適用条件、外部境界）をGitHubで案内できる状態。** 収載済み本文に埋もれた親は必要に応じて後で同値性を点検する。**未完了：数学的必須親の厳密な再帰閉包、外部原典の照合、独立数学監査、計算証拠。** この4点の未完を本書から消してはならない。

PR #1854はDraft・未マージを維持。研究はrow393停止、新たなsource排除・Branch B閉鎖は0。[現行PR入口](PR1854-START-HERE.md)。
