# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-1006-JST`
>
> **CURRENT_BASE_COMMIT:** `e82668bfe700e02b88019302dfe633244254966a`
>
> **CURRENT_STAGE:** `Stage12-N1-3a completed; Stage12-N1-3b next`
>
> **STAGE13_STATUS:** `PAUSED_AFTER_STAGE13_2`
>
> **SERIES_STATUS:** `STAGE12_REOPENED_REPAIRABLE_NOT_CLOSED`
>
> **AUDIT_VERDICT:** `REPAIRABLE`
>
> **AUDIT_COUNTS:** `FATAL=0, MAJOR=4, MINOR=2, CLARIFICATION=1`
>
> **RESOLVED_AFTER_AUDIT:** `MAJOR-01`
>
> **OPEN_MAJOR:** `MAJOR-02, MAJOR-03, MAJOR-04`
>
> **CENTRAL_OPEN_ITEMS:** `FIXED_CIRCLE_REMAINDER, COUPLED_REGION_TRANSFER`

## 0. 60秒で現状復帰する順序

新しい作業セッションでは次の順に読む。

1. `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/review/stage12-n1-2-full-audit-r01.md`
3. `docs/stage12-n1-2-repair-status-r01.md`
4. `docs/stage12-n1-3a-rectangular-error-repair.md`
5. 次の作業で必要となるarchiveの2kを読む

```text
docs/archive/stage12-n1-2/stage12-n1-2k-final-remainder.md
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

現在の扱いは

```text
THEOREM_STATUS=PLAUSIBLE_BUT_NOT_CLOSED_FROM_PRESENT_DOCUMENTS
VERDICT=REPAIRABLE
```

である。

`docs/stage12-n1-2-final.md` は旧統合候補稿として残すが、修復と再監査が完了するまで「確定済み完成証明」として扱わない。特に旧Final §4の長方形誤差表示はStage12-N1-3aによりsupersedeされている。

## 2. Stage12-N1-3aで閉じた項目

成果物:

```text
docs/stage12-n1-3a-rectangular-error-repair.md
```

### MAJOR-01 — rectangular error exponent

旧2pでは、大係数領域で得た

\[
R^{3/4+\delta/2}S
\]

を

\[
R^{1/2+\delta}S
\]

へ強化していたが、\(\delta\in(0,1/4)\) では成立しない。

Stage12-N1-3aでは不成立な強化を撤回し、任意の固定

\[
0<\varepsilon<\frac18
\]

に対し

\[
\boxed{
S(R,S)
=
\mathfrak C RS
+O_\varepsilon\!\left(
RS\{E_*(R^{1/2})+E_*(S^{1/2})\}
+R^{3/4+\varepsilon}S
+RS^{3/4+\varepsilon}
\right)
}
\]

へ修正した。

修復の要点は次の通り。

- 一変数評価から `B_beta(X) << X` を使用する;
- weighted coefficient norm `M_{2ε}` で大係数尾部を評価する;
- 旧指数 `R^(1/2+δ)S` を引用禁止にする;
- 後続kernelが予定する部分和分ノルムを満たすなら、修正版誤差がretained regionで任意の対数冪より小さいことを確認する;
- kernelノルム自体と正確な係数 `1/12` はMAJOR-03へ残す。

状態:

```text
MAJOR_01_RECTANGULAR_ERROR_EXPONENT=CLOSED_BY_STAGE12_N1_3A
```

## 3. 次の作業 — Stage12-N1-3b

次の成果物は

```text
docs/stage12-n1-3b-fixed-circle-remainder.md
```

である。

対象は監査R01のMAJOR-02。

2kでは畳み込み誤差

\[
G(rs)
\sum_{\ell\le X}
|h_{r,s}(\ell)|(X/\ell)^{1/2}\omega(X/\ell)
\]

から \(\omega(X)\) を全域へ引き出していたが、\(X/\ell\le X\) に対する単調性の向きが逆である。

Stage12-N1-3bでは、少なくとも次を比較する。

1. \(\ell\le X^{1/2}\) と \(\ell>X^{1/2}\) の分割評価;
2. finite Euler correctionを含むDirichlet級数への直接Perron／Selberg–Delange法;
3. 得られる依存重みがouter \((r,s)\) 平均で許容されるか。

終了条件は、fixed-\((r,s)\) remainderを単に点wiseに書くことではなく、最終の\((r,s)\)平均へ投入できる一様形を本文上で証明することである。

## 4. その後に残る項目

### MAJOR-03 — coupled-region transfer

独立補題として次を完全に記載する。

- divisor variables;
- radial kernel;
- 二変数Abel／Stieltjes部分和分;
- boundary terms;
- parity / orientation front factors;
- Stage12-N1-3aの修正版誤差を全boxで合計した評価;
- 正確な係数 \(1/12\)。

### MAJOR-04 — bundle self-containment

新しいbundleへ次を追加する。

- `C_prim(B)` の完全なcounting definition;
- \(\kappa\), \(\eta\), local factors, 2-adic / archimedean front factorsのconstant sheet。

### Secondary items

- Tenenbaum II.5.2のhypothesisと採用remainder caseを一対一で固定する;
- 2j原文中の壊れた `\frac` 2件を修正する;
- Finalをsummaryとして明記するか、未定義記号を補う;
- 全修復後に新しい統合稿と自己完結bundle R02を生成する。

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
- 旧2p／旧Finalの `R^(1/2+δ)S + RS^(1/2+δ)` を引用しない。
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
STAGE12_N1_3A_RECTANGULAR_ERROR_REPAIR_COMPLETE
MAJOR_01=CLOSED
MAJOR_02=OPEN_NEXT
MAJOR_03=OPEN_CENTRAL
MAJOR_04=OPEN
THEOREM_STATUS=REPAIRABLE_NOT_CLOSED
STAGE13_3_PAUSED_PENDING_STAGE12_REPAIR
NEXT_TASK=STAGE12_N1_3B_FIXED_CIRCLE_REMAINDER
```
