# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-0839-JST`
>
> **CURRENT_BASE_COMMIT:** `0fc81f192a1e82cf3fc188230a6a8615ba64f23f`
>
> **COMPLETED_THROUGH:** `Stage13-2`
>
> **CURRENT_STAGE:** `Stage13-3 — origin of the leading 2`
>
> **SERIES_STATUS:** `STRUCTURAL_LEDGER_FIXED_MECHANISM_ANALYSIS_PENDING`
>
> **LATEST_MERGED_RESEARCH_PR:** `#67`

## 0. 60秒で現状復帰する順序

新しい作業セッションでは、次の順に読む。

1. このファイル `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/stage13-roadmap.md`
3. `docs/stage13-1-definition.md`
4. `docs/stage13-2-structural-decomposition.md`
5. Stage12との解析的接続が必要になった時だけ `docs/stage12-n1-2-final.md`

過去のStage12-N1-2導出途中文書は `docs/archive/stage12-n1-2/` に保存されている。通常の現状復帰では読まなくてよい。

## 1. 現在の研究目的

完全直方体そのものの存在証明ではない。

整数空間対角線を持ち、三つの面対角線のうちちょうど一つだけが整数となる primitive な直方体を、辺の大きさ順で三方向に分類し、有限計算で観測される

```text
N_ab : N_ac : N_bc ≈ 2 : 1 : 1
```

について、

- なぜ `2:1:1` に近い形が自然に現れるのか;
- leading `2` と二つの `1` がどの構造から生じるのか;
- 有限範囲のズレがどの機構から生じるのか;

を説明することがStage13の目的である。

厳密な `2:1:1`、その極限、または収束速度を先に仮定しない。

## 2. 固定済みのcounting convention

対象は

\[
(a,b,c,d)\in\mathbf Z_{>0}^4
\]

で、

\[
a<b<c,
\qquad
\gcd(a,b,c)=1,
\qquad
 a^2+b^2+c^2=d^2,
\qquad
d\le B
\]

を満たし、

\[
a^2+b^2,
\qquad
a^2+c^2,
\qquad
b^2+c^2
\]

のうちちょうど一つだけが正整数平方となるもの。

方向別countを

\[
N_{ab}(B),\qquad N_{ac}(B),\qquad N_{bc}(B)
\]

とし、

\[
N_1(B)=N_{ab}(B)+N_{ac}(B)+N_{bc}(B)
\]

とする。

`ab`, `ac`, `bc` は固定座標軸ではなく、canonical ordering `a<b<c` における

- 最小二辺;
- 最小辺と最大辺;
- 最大二辺;

を表す。

## 3. 有限観測

`B=100000` では

```text
(N_ab, N_ac, N_bc) = (84146, 43180, 40704)
```

であり、`bc` を1に正規化すると

```text
2.0673 : 1.0608 : 1
```

総数で正規化すると

```text
(0.50078, 0.25698, 0.24224)
```

である。

これはStage13の動機となる有限観測であり、漸近定理ではない。

## 4. Stage12の確定済み基礎

現行完成稿は

```text
docs/stage12-n1-2-final.md
```

である。

Stage12の主結果は primitive oriented count に対する

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
\]

である。

関連PR:

- `#61` 統合完成稿;
- `#62` 最終校正;
- `#65` 過去文書のarchive整理。

重要な制限:

Stage12の `C_{\rm prim}(B)` は oriented parameter count であり、Stage13の canonical exact-one-face count

\[
N_{ab},\ N_{ac},\ N_{bc},\ N_1
\]

へ定数倍で自動変換できるとは確定していない。

## 5. Stage13の完了状況

### Stage13 roadmap

```text
docs/stage13-roadmap.md
```

PR `#63` でマージ済み。

### Stage13-1 — 定義

```text
docs/stage13-1-definition.md
```

PR `#64`、補足PR `#66` でマージ済み。

確定事項:

- counted object;
- canonical ordering;
- primitive condition;
- cutoff `d<=B`;
- exactly-one-face condition;
- `N_ab`, `N_ac`, `N_bc`, `N_1`;
- observed ratio と proportion vector。

### Stage13-2 — 構造分解

```text
docs/stage13-2-structural-decomposition.md
```

PR `#67` でマージ済み。

- research commit: `5f31f283e0614ea55963b60c0104dff19957a6f1`;
- merge commit: `0fc81f192a1e82cf3fc188230a6a8615ba64f23f`。

exactly-one countを、raw directional incidenceとoverlap correctionへ厳密に分解した。

\[
N_{ab}
=
A_{ab}-A_{ab,ac}-A_{ab,bc}+A_3,
\]

\[
N_{ac}
=
A_{ac}-A_{ab,ac}-A_{ac,bc}+A_3,
\]

\[
N_{bc}
=
A_{bc}-A_{ab,bc}-A_{ac,bc}+A_3.
\]

以後は、raw incidence `A_ab, A_ac, A_bc` と exact-one overlap correction を分離して解析する。

## 6. Stage13-2で得た重要な制約

canonical objectを全 `S_3` orientationへ同じ重みで展開すると、exactly-one integer faceは固定座標面の各方向へ2回ずつ現れる。

```text
2 : 2 : 2 = 1 : 1 : 1
```

したがって、full orientation multiplicity単独では canonical な `2:1:1` を説明できない。

leading ratioを説明する候補は、少なくとも次の層へ分けて監査する。

- canonical size-order geometry;
- primitive reduction;
- parity / 2-adic branch;
- representation multiplicity;
- odd-prime local density;
- cutoff and boundary;
- exact-one overlap correction;
- Stage12 bridge mapのfiber multiplicity。

これらが加法的または独立に因子分解できるとは、まだ主張しない。

## 7. 現在の未解決点

未確定なのは次の点である。

1. raw incidence `A_ab:A_ac:A_bc` の段階ですでに `2:1:1` に近い形が現れるか。
2. leading `2` が canonical size-order、parity、local density、representation multiplicityのどこで初めて現れるか。
3. `A_ac` と `A_bc` の主構造が同一か。
4. exact-one overlap correctionが主比率を生成するのか、有限ズレだけを生成するのか。
5. Stage12 parameter recordsからcanonical directional objectsへのbridge map `Pi_12` とfiber multiplicity `m_12`。
6. Stage12の `kappa`, `eta` またはEuler factorsを三方向の共通因子として抽出できるか。
7. proportion vectorが `(1/2,1/4,1/4)` へ収束するか。

## 8. 次の作業 — Stage13-3

次に作成する成果物は

```text
docs/stage13-3-origin-of-two.md
```

である。

開始点は raw incidence

\[
A_{ab}(B),\qquad A_{ac}(B),\qquad A_{bc}(B)
\]

と canonical size-order layer。

最初に行うべきこと:

1. exact-one sieve前の方向別 raw incidenceを有限データまたは再現可能な列挙で測る。
2. raw ratioとexact-one ratioを比較し、leading `2` がoverlap前に存在するかを判定する。
3. canonical orderingを外したaxis-labelled countが対称化されることと、canonical chamber内の差を分離する。
4. parity class別countを切り、2-adic branchが方向差を作るかを監査する。
5. この段階ではEuler積、Stage12との定数変換、`2:1:1`の漸近証明を先取りしない。

Stage13-3の終了条件は、leading `2` の候補を列挙するだけではなく、どのlayerで差が初めて観測・導出されるかを特定し、残る未証明部分を明記することである。

## 9. 作業時の禁止事項

- `2:1:1` を先に真と仮定しない。
- 有限比率を漸近比率と呼ばない。
- orientation multiplicityだけでleading `2` を説明しない。
- Stage12の `C_prim` とStage13の `N_1` の間に未監査の定数倍関係を置かない。
- local factorの独立性やEuler積収束を定義前に主張しない。
- `proof`, `closed`, `complete` は、文書・PR・commitを実際に確認した場合だけ使う。
- ユーザーの明示的な依頼なしにPRをマージしない。

## 10. GitHub作業ルール

GitHub上の作成・更新・commit・branch・PR作成を依頼された場合は、説明より先にGitHub連携を実行する。

完了報告には実際に取得した

- PR URL / PR番号;
- commit SHA;
- branch名;

を含める。

GitHub連携を確認せずに「利用できない」と判断しない。

## 11. 状態コード

```text
STAGE12_FINAL_COMPLETE
STAGE13_1_DEFINITION_COMPLETE
STAGE13_2_STRUCTURAL_LEDGER_COMPLETE
STAGE13_3_ORIGIN_OF_LEADING_TWO_PENDING
```
