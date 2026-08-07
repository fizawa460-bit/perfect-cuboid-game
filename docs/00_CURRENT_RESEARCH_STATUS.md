# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-0958-JST`
>
> **CURRENT_BASE_COMMIT:** `e82668bfe700e02b88019302dfe633244254966a`
>
> **CURRENT_STAGE:** `Stage12-N1-2 repair after full audit R01`
>
> **STAGE13_STATUS:** `PAUSED_AFTER_STAGE13_2`
>
> **SERIES_STATUS:** `STAGE12_REOPENED_REPAIRABLE_NOT_CLOSED`
>
> **AUDIT_VERDICT:** `REPAIRABLE`
>
> **AUDIT_COUNTS:** `FATAL=0, MAJOR=4, MINOR=2, CLARIFICATION=1`
>
> **CENTRAL_OPEN_ITEMS:** `FIXED_CIRCLE_REMAINDER, COUPLED_REGION_TRANSFER`

## 0. 60秒で現状復帰する順序

新しい作業セッションでは次の順に読む。

1. `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/review/stage12-n1-2-full-audit-r01.md`
3. `docs/stage12-n1-2-repair-status-r01.md`
4. `docs/stage12-n1-2-final.md`
5. 必要な箇所だけarchiveの2k、2n、2pを読む

```text
docs/archive/stage12-n1-2/stage12-n1-2k-final-remainder.md
docs/archive/stage12-n1-2/stage12-n1-2n-coupled-region.md
docs/archive/stage12-n1-2/stage12-n1-2p-final-bookkeeping.md
```

Stage13-1とStage13-2の構造的成果は保持するが、Stage13-3以降はStage12修復が終わるまで進めない。

## 1. 現在の判断

独立監査R01は、候補漸近式

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
\]

を否定していない。一方で、現行文書だけから定理を `CLOSED` と判定できないとした。

したがって現在の扱いは次の通り。

```text
THEOREM_STATUS=PLAUSIBLE_BUT_NOT_CLOSED_FROM_PRESENT_DOCUMENTS
VERDICT=REPAIRABLE
```

`docs/stage12-n1-2-final.md` は現行の統合候補稿として残すが、修復と再監査が完了するまで「確定済み完成証明」として扱わない。

## 2. 監査R01の主要指摘

監査原文:

```text
docs/review/stage12-n1-2-full-audit-r01.md
```

### MAJOR-01 — 長方形誤差の指数

2pの大係数領域で得た

\[
R^{3/4+\delta/2}S
\]

を

\[
R^{1/2+\delta}S
\]

へ強化しているが、\(\delta\in(0,1/4)\) では指数比較が成立しない。

修復候補は

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
\]

型へ弱め、kernel適用後のbox誤差を再評価すること。

### MAJOR-02 — fixed-circle remainder

畳み込み誤差中の \(\omega(X/\ell)\) を \(\omega(X)\) として引き出す向きが正当化されていない。

\(\ell\le X^{1/2}\) と \(\ell>X^{1/2}\) の分割、または有限Euler補正を含む直接解析により、\(rs\) 平均で一様なremainderを再証明する必要がある。

### MAJOR-03 — 結合領域移送

係数 \(1/12\) の導出が概要に留まっている。

独立補題として次を完全に書く必要がある。

- divisor variables;
- radial kernel \((r^2+s^2)^{-1}\);
- 二変数Abel／Stieltjes部分和分;
- 境界項;
- parity / orientation front factors;
- MAJOR-01修正後の全box誤差。

### MAJOR-04 — bundleの自己完結性

現行2j〜2p bundleだけでは、次を独立再計算できない。

- `C_prim(B)` の完全定義;
- \(\kappa\) の完全なEuler積とfront factor;
- rawからprimitiveへの対象レベル対応;
- \(\eta_p/\kappa_p\) の監査に必要なlocal factor。

修復時にはdefinition sheetとconstant sheetを追加する。

## 3. 二次指摘

- Tenenbaum II.5.2のhypothesis、parameter、採用remainder caseを一対一で固定する。
- 2j原文中の壊れた `\frac` 2件を修正する。
- Final単体で外部依存となっている記号を定義するか、summary documentと明示する。
- 対角・円弧境界、floor endpointはMAJOR-03の移送補題内で導出を固定する。

## 4. 修復順序

1. **MAJOR-01**を正しい弱い指数へ直す。
2. **MAJOR-02**のfixed-circle remainderを再証明する。
3. **MAJOR-03**の結合領域移送補題を新設する。
4. **MAJOR-04**のdefinition sheetとconstant sheetを作る。
5. Tenenbaum参照条件を固定する。
6. control characterと記号定義を校正する。
7. 新しい自己完結bundle R02を生成する。
8. 独立監査へ再提出する。

詳細な管理文書:

```text
docs/stage12-n1-2-repair-status-r01.md
```

## 5. Stage13の扱い

Stage13-1とStage13-2で確定した次の構造的内容は撤回しない。

- canonical counting convention;
- `N_ab`, `N_ac`, `N_bc`, `N_1` の定義;
- raw incidenceとoverlap correctionの厳密分解;
- full equal-weight `S_3` orientationが `1:1:1` へ対称化すること;
- orientation multiplicity単独ではcanonical `2:1:1` を説明できないこと。

ただし、Stage12の候補漸近式や局所定数を確定済み解析基礎として使う作業は停止する。

```text
STAGE13_1_DEFINITION_COMPLETE
STAGE13_2_STRUCTURAL_LEDGER_COMPLETE
STAGE13_3_PAUSED_PENDING_STAGE12_REPAIR
```

## 6. 現在の禁止事項

- Stage12-N1-2を `CLOSED`, `FINAL_COMPLETE`, `proved` と呼ばない。
- MAJOR-01の誤った指数をそのまま引用しない。
- fixed-circle remainderを一様に閉じたと仮定しない。
- `1/12` の係数を完全導出済みと扱わない。
- 現行bundleを自己完結と呼ばない。
- Stage12からStage13 canonical countへの定数変換を先取りしない。
- ユーザーの明示的な依頼なしにPRをマージしない。

## 7. Stage12再閉包の終了条件

次のすべてを満たした時だけ再びclosedと呼ぶ。

- MAJOR-01〜03が本文上で証明されている;
- MAJOR-04を解消した自己完結bundleがある;
- Tenenbaum適用条件が固定されている;
- control characterと記号定義が修正されている;
- 新しい独立監査が `CLOSED` を返している。

## 8. 状態コード

```text
STAGE12_N1_2_REOPENED_AFTER_AUDIT_R01
STAGE12_N1_2_REPAIRABLE_NOT_CLOSED
STAGE13_1_DEFINITION_COMPLETE
STAGE13_2_STRUCTURAL_LEDGER_COMPLETE
STAGE13_3_PAUSED_PENDING_STAGE12_REPAIR
NEXT_TASK=REPAIR_MAJOR_01_RECTANGULAR_ERROR_EXPONENT
```
