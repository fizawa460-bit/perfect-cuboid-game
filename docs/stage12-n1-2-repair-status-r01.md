# Stage12-N1-2 repair status after full audit R01

> **STATUS:** `REPAIRABLE — NOT CLOSED`
>
> **AUDIT_DATE:** `2026-08-07`
>
> **FATAL:** `0`
>
> **MAJOR:** `4`
>
> **MINOR:** `2`
>
> **CLARIFICATION:** `1`
>
> **CENTRAL_OPEN_ITEMS:** `FIXED_CIRCLE_REMAINDER, COUPLED_REGION_TRANSFER`

## 1. Project decision

Stage13-3以降の解析作業を一時停止し、Stage12-N1-2を再オープンする。

現行の漸近式

\[
C_{\rm prim}(B)\sim \frac{\kappa}{12\pi}B(\log B)^3
\]

は、監査R01では「偽と判定された」のではなく、**現行文書だけでは証明完了と判定できない**とされた。したがって、修復が完了して再監査を通るまで `CLOSED`, `FINAL_COMPLETE`, `proved` と扱わない。

監査原文:

```text
docs/review/stage12-n1-2-full-audit-r01.md
```

## 2. Open items

### MAJOR-01 — rectangular error exponent

2pの大係数領域で

\[
R^{3/4+\delta/2}S
\]

から

\[
R^{1/2+\delta}S
\]

への強化が、\(\delta\in(0,1/4)\) では成立しない。

最初の修復では、正しい弱い形

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
\]

へ戻し、kernelを掛けたbox誤差を再計算する。

### MAJOR-02 — fixed-circle remainder

畳み込み誤差中の \(\omega(X/\ell)\) を \(\omega(X)\) として全域から引き出す向きが正当化されていない。

\(\ell\le X^{1/2}\) と \(\ell>X^{1/2}\) の分割、または有限Euler補正を含むDirichlet級数への直接法により、\(rs\) 平均で一様な評価を再証明する必要がある。

### MAJOR-03 — coupled-region transfer

係数 \(1/12\) を得る移送が概要に留まっている。

独立した結合領域移送補題として、divisor variables、radial kernel、二変数Stieltjes積分、境界項、parity/orientation前置因子、全box誤差を明記する。

### MAJOR-04 — review self-containment

レビューbundleに次を追加する。

- `C_prim(B)` の完全なcounting definition;
- \(\kappa\), \(\eta\), local factors, 2-adic / archimedean front factorsのconstant sheet。

これは主に監査可能性の問題であり、単独では数学的矛盾を意味しない。

## 3. Secondary items

- Tenenbaum II.5.2のhypothesisと採用するremainder caseを一対一で固定する。
- 2j原文中のフォームフィード由来の壊れた `\frac` 2件を修正する。
- Final単体で未定義の記号一覧を補うか、Finalをsummary documentと明記する。

## 4. Repair order

1. MAJOR-01を正しい弱い指数へ修正する。
2. MAJOR-02のfixed-circle remainderを再証明する。
3. MAJOR-03の結合領域移送補題を新設する。
4. 定義sheetと定数sheetを作成し、bundleをR02として再生成する。
5. Tenenbaum参照を固定する。
6. 制御文字と記号定義を校正する。
7. 独立監査へ再提出する。

## 5. Exit condition

Stage12-N1-2を再びclosedと呼ぶ条件は次のすべてである。

- MAJOR-01〜03の本文上の証明が完了している;
- MAJOR-04を解消した自己完結bundleが生成されている;
- control characterと参照条件が修正されている;
- 新しい独立監査が `CLOSED` を返している。

それまではStage13の構造的成果（Stage13-1、13-2）は保持するが、Stage12漸近式を確定済み解析基礎として使わない。
