# Stage12-N1-2 repair status after full audit R01

> **STATUS:** `REPAIRABLE — NOT CLOSED`
>
> **AUDIT_DATE:** `2026-08-07`
>
> **AUDIT_COUNTS:** `FATAL=0, MAJOR=4, MINOR=2, CLARIFICATION=1`
>
> **RESOLVED_AFTER_AUDIT:** `MAJOR-01`
>
> **OPEN_MAJOR:** `MAJOR-02, MAJOR-03, MAJOR-04`
>
> **CENTRAL_OPEN_ITEMS:** `FIXED_CIRCLE_REMAINDER, COUPLED_REGION_TRANSFER`

## 1. Project decision

Stage13-3以降の解析作業を一時停止し、Stage12-N1-2を再オープンする。

現行の候補漸近式

\[
C_{\rm prim}(B)\sim \frac{\kappa}{12\pi}B(\log B)^3
\]

は、監査R01では「偽と判定された」のではなく、**現行文書だけでは証明完了と判定できない**とされた。修復が完了して再監査を通るまで `CLOSED`, `FINAL_COMPLETE`, `proved` と扱わない。

監査原文:

```text
docs/review/stage12-n1-2-full-audit-r01.md
```

最初の修復成果物:

```text
docs/stage12-n1-3a-rectangular-error-repair.md
```

## 2. Repair ledger

### MAJOR-01 — rectangular error exponent

**状態:** `CLOSED_BY_STAGE12_N1_3A`

2pの大係数領域で

\[
R^{3/4+\delta/2}S
\]

から

\[
R^{1/2+\delta}S
\]

へ強化した箇所は不成立だった。

Stage12-N1-3aではこの強化を撤回し、任意の固定

\[
0<\varepsilon<\frac18
\]

に対する正しい一様長方形誤差

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
\]

へ置き換えた。

修復では一変数評価から得られる

\[
B_\beta(X)\ll X
\]

を使い、不要な対数因子を除いたうえで大係数尾部を再評価した。また、後続kernelが

\[
\|K_B\|_{\rm PS,\mathcal B}
\ll
\frac{B(\log B)^C}{R^2+S^2}
\]

を満たす場合、修正版べき誤差がretained regionで任意の対数冪より小さいことを確認した。

ただし、このkernelノルムそのものと正確な主定数の導出はMAJOR-03で証明する。したがってMAJOR-01の閉包は、rectangular lemmaとその予定用途への適合性に限定する。

旧Stage12-N1-2p §3.2〜§3.5および旧Final §4の

\[
R^{1/2+\delta}S+RS^{1/2+\delta}
\]

は以後引用しない。

### MAJOR-02 — fixed-circle remainder

**状態:** `OPEN — NEXT`

畳み込み誤差中の \(\omega(X/\ell)\) を \(\omega(X)\) として全域から引き出す向きが正当化されていない。

\(\ell\le X^{1/2}\) と \(\ell>X^{1/2}\) の分割、または有限Euler補正を含むDirichlet級数への直接法により、\(rs\) 平均で一様な評価を再証明する必要がある。

次の成果物を

```text
docs/stage12-n1-3b-fixed-circle-remainder.md
```

とする。

### MAJOR-03 — coupled-region transfer

**状態:** `OPEN — CENTRAL`

係数 \(1/12\) を得る移送が概要に留まっている。

独立した結合領域移送補題として、次を明示する。

- divisor variables;
- radial kernel;
- 二変数Abel／Stieltjes部分和分;
- boundary terms;
- parity/orientation front factors;
- Stage12-N1-3aの修正版誤差を全boxで合計した評価。

Stage12-N1-3a §4のkernelノルム仮定は、この段階で本文上の補題として証明する。

### MAJOR-04 — review self-containment

**状態:** `OPEN — DOCUMENTATION/AUDITABILITY`

レビューbundleに次を追加する。

- `C_prim(B)` の完全なcounting definition;
- \(\kappa\), \(\eta\), local factors, 2-adic / archimedean front factorsのconstant sheet。

これは主に監査可能性の問題であり、単独では数学的矛盾を意味しない。

## 3. Secondary items

- Tenenbaum II.5.2のhypothesisと採用するremainder caseを一対一で固定する。
- 2j原文中のフォームフィード由来の壊れた `\frac` 2件を修正する。
- Final単体で未定義の記号一覧を補うか、Finalをsummary documentと明記する。
- 現行Final §4の誤差表示は、全修復後の新しい統合稿でStage12-N1-3aの補題へ置き換える。

## 4. Repair order

1. ~~MAJOR-01を正しい弱い指数へ修正する。~~ `CLOSED_BY_STAGE12_N1_3A`
2. **MAJOR-02**のfixed-circle remainderを再証明する。
3. **MAJOR-03**の結合領域移送補題を新設する。
4. **MAJOR-04**の定義sheetと定数sheetを作成する。
5. Tenenbaum参照を固定する。
6. 制御文字と記号定義を校正する。
7. 新しい統合稿と自己完結bundle R02を生成する。
8. 独立監査へ再提出する。

## 5. Exit condition

Stage12-N1-2を再びclosedと呼ぶ条件は次のすべてである。

- MAJOR-01〜03の本文上の証明が完了している;
- MAJOR-04を解消した自己完結bundleが生成されている;
- control characterと参照条件が修正されている;
- 新しい独立監査が `CLOSED` を返している。

現在はMAJOR-01のみ閉じた。Stage13の構造的成果（Stage13-1、13-2）は保持するが、Stage12漸近式を確定済み解析基礎として使わない。

## 6. Current codes

```text
STAGE12_N1_3A_RECTANGULAR_ERROR_REPAIR_COMPLETE
MAJOR_01=CLOSED
MAJOR_02=OPEN_NEXT
MAJOR_03=OPEN_CENTRAL
MAJOR_04=OPEN
THEOREM_STATUS=REPAIRABLE_NOT_CLOSED
NEXT_TASK=STAGE12_N1_3B_FIXED_CIRCLE_REMAINDER
```
