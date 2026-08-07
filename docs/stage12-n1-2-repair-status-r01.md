# Stage12-N1-2 repair status after full audit R01

> **STATUS:** `REPAIRABLE — NOT CLOSED`
>
> **AUDIT_DATE:** `2026-08-07`
>
> **AUDIT_COUNTS:** `FATAL=0, MAJOR=4, MINOR=2, CLARIFICATION=1`
>
> **RESOLVED_AFTER_AUDIT:** `MAJOR-01, MAJOR-02`
>
> **OPEN_MAJOR:** `MAJOR-03, MAJOR-04`
>
> **CENTRAL_OPEN_ITEM:** `COUPLED_REGION_TRANSFER`

## 1. Project decision

Stage13-3以降の解析作業を一時停止し、Stage12-N1-2を再オープンする。

現行の候補漸近式

\[
C_{\rm prim}(B)\sim \frac{\kappa}{12\pi}B(\log B)^3
\]

は、監査R01では「偽と判定された」のではなく、**監査時点の文書だけでは証明完了と判定できない**とされた。修復が完了して再監査を通るまで `CLOSED`, `FINAL_COMPLETE`, `proved` と扱わない。

監査原文:

```text
docs/review/stage12-n1-2-full-audit-r01.md
```

修復成果物:

```text
docs/stage12-n1-3a-rectangular-error-repair.md
docs/stage12-n1-3b-fixed-circle-remainder.md
```

## 2. Repair ledger

### MAJOR-01 — rectangular error exponent

**状態:** `CLOSED_BY_STAGE12_N1_3A`

旧2pの不成立な

\[
R^{1/2+\delta}S+RS^{1/2+\delta}
\]

への指数強化を撤回し、任意の固定 `0<ε<1/8` に対する正しい一様長方形誤差

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
\]

へ置き換えた。

後続kernelが予定する部分和分ノルムを満たす場合、修正版べき誤差はretained regionで任意の固定対数冪より小さい。kernelノルムそのものと正確な係数 `1/12` はMAJOR-03に残す。

旧Stage12-N1-2p §3.2〜§3.5および旧Final §4の誤差表示は以後引用しない。

### MAJOR-02 — fixed-circle remainder

**状態:** `CLOSED_BY_STAGE12_N1_3B`

旧2kではconvolution error中の `ω(X/ℓ)` を `ω(X)` として全域へ引き出したが、単調性の向きが逆であった。

Stage12-N1-3bではこの操作を撤回し、base remainderの弱い形

\[
E_0(Y)\ll Y^{1/2}
\]

とfinite Euler correctionの絶対 `1/2`-norm

\[
H_{\rm abs}(rs)
=
\sum_{\ell\ge1}
\frac{|h_{r,s}(\ell)|}{\ell^{1/2}}
\]

を直接使用した。convolution errorとresidue tailを別々に評価して

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1
+O\!\left(
G(rs)H_{\rm abs}(rs)X^{1/2}
\right)
\]

を得た。

\[
W(n)=G(n)H_{\rm abs}(n)
\]

とし、既存の固定対数次数平均上界

\[
\sum_{n\le T}W(n)
\ll T(\log(2T))^K
\]

を使う。retained regionでは

\[
X_{r,s}\ge X_0
=
\exp\!\left((\log B)^{1/4}\right),
\]

したがって `q=r^2+s^2≤2B/X_0` である。dyadic `q` shellによりfixed-circle remainderのouter averageは

\[
\ll
B X_0^{-1/2}(\log B)^{2K}
=
o\!\left(B(\log B)^{-A}\right)
\]

となり、任意の固定 `A>0` に対して十分小さい。

旧2k §2〜§3の

\[
G(rs)H_{\rm abs}(rs)X^{1/2}\omega(X)
\]

型pointwise estimateは以後使用せず、Stage12-N1-3bのpointwise estimateとretained-region averageで置き換える。

### MAJOR-03 — coupled-region transfer

**状態:** `OPEN — NEXT / CENTRAL`

係数 `1/12` を得る移送が概要に留まっている。

次の成果物を

```text
docs/stage12-n1-3c-coupled-region-transfer.md
```

とし、独立した結合領域移送補題として次を明示する。

- divisor variables;
- radial kernel;
- 二変数Abel／Stieltjes部分和分;
- boundary terms;
- parity/orientation front factors;
- Stage12-N1-3aの修正版長方形誤差を全boxで合計した評価;
- Stage12-N1-3bのfixed-circle remainderとの分離;
- 正確な係数 `1/12`。

Stage12-N1-3a §4のkernelノルム仮定は、この段階で本文上の補題として証明する。

### MAJOR-04 — review self-containment

**状態:** `OPEN — DOCUMENTATION/AUDITABILITY`

レビューbundleに次を追加する。

- `C_prim(B)` の完全なcounting definition;
- `κ`, `η`, local factors, 2-adic / archimedean front factorsのconstant sheet。

これは主に監査可能性の問題であり、単独では数学的矛盾を意味しない。

## 3. Secondary items

- Tenenbaum II.5.2のhypothesisと採用するremainder caseを一対一で固定する。
- 2j原文中のフォームフィード由来の壊れた `\frac` 2件を修正する。
- Final単体で未定義の記号一覧を補うか、Finalをsummary documentと明記する。
- 現行Final §1のfixed-circle remainderと§4の長方形誤差は、全修復後の新しい統合稿で3b・3aの補題へ置き換える。

## 4. Repair order

1. ~~MAJOR-01を正しい弱い指数へ修正する。~~ `CLOSED_BY_STAGE12_N1_3A`
2. ~~MAJOR-02のfixed-circle remainderを再証明する。~~ `CLOSED_BY_STAGE12_N1_3B`
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

現在はMAJOR-01とMAJOR-02を閉じた。Stage13の構造的成果（Stage13-1、13-2）は保持するが、Stage12漸近式を確定済み解析基礎として使わない。

## 6. Current codes

```text
STAGE12_N1_3A_RECTANGULAR_ERROR_REPAIR_COMPLETE
STAGE12_N1_3B_FIXED_CIRCLE_REMAINDER_COMPLETE
MAJOR_01=CLOSED
MAJOR_02=CLOSED
MAJOR_03=OPEN_NEXT_CENTRAL
MAJOR_04=OPEN
THEOREM_STATUS=REPAIRABLE_NOT_CLOSED
NEXT_TASK=STAGE12_N1_3C_COUPLED_REGION_TRANSFER
```
