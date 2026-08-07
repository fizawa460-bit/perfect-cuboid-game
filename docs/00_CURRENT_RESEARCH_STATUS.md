# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-1030-JST`
>
> **CURRENT_BASE_COMMIT:** `45da1aad2cbdda443d6157346511d6437b46c520`
>
> **CURRENT_STAGE:** `Stage12-N1-3b completed; Stage12-N1-3c next`
>
> **STAGE13_STATUS:** `PAUSED_AFTER_STAGE13_2`
>
> **SERIES_STATUS:** `STAGE12_REOPENED_REPAIRABLE_NOT_CLOSED`
>
> **AUDIT_VERDICT:** `REPAIRABLE`
>
> **AUDIT_COUNTS:** `FATAL=0, MAJOR=4, MINOR=2, CLARIFICATION=1`
>
> **RESOLVED_AFTER_AUDIT:** `MAJOR-01, MAJOR-02`
>
> **OPEN_MAJOR:** `MAJOR-03, MAJOR-04`
>
> **CENTRAL_OPEN_ITEM:** `COUPLED_REGION_TRANSFER`

## 0. 60秒で現状復帰する順序

新しい作業セッションでは次の順に読む。

1. `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/review/stage12-n1-2-full-audit-r01.md`
3. `docs/stage12-n1-2-repair-status-r01.md`
4. `docs/stage12-n1-3a-rectangular-error-repair.md`
5. `docs/stage12-n1-3b-fixed-circle-remainder.md`
6. 次の作業で必要となるarchiveの2n、2oと現行Final §5〜§6を読む

```text
docs/archive/stage12-n1-2/stage12-n1-2n-coupled-region.md
docs/archive/stage12-n1-2/stage12-n1-2o-analytic-closure.md
docs/stage12-n1-2-final.md
```

Stage13-1とStage13-2の構造的成果は保持するが、Stage13-3以降はStage12修復が終わるまで進めない。

## 1. 現在の判断

独立監査R01は、候補漸近式

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
\]

を否定していない。一方で、監査時点の文書だけから定理を `CLOSED` と判定できないとした。

現在の扱いは

```text
THEOREM_STATUS=PLAUSIBLE_BUT_NOT_CLOSED_FROM_PRESENT_DOCUMENTS
VERDICT=REPAIRABLE
```

である。

`docs/stage12-n1-2-final.md` は旧統合候補稿として残すが、修復と再監査が完了するまで「確定済み完成証明」として扱わない。旧Final §1のfixed-circle remainderはStage12-N1-3b、旧Final §4の長方形誤差はStage12-N1-3aによりsupersedeされている。

## 2. Stage12-N1-3aで閉じた項目

成果物:

```text
docs/stage12-n1-3a-rectangular-error-repair.md
```

### MAJOR-01 — rectangular error exponent

旧2pの不成立な指数強化を撤回し、任意の固定

\[
0<\varepsilon<\frac18
\]

に対して

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

後続kernelが予定する部分和分ノルムを満たす場合、この修正版べき誤差はretained regionで任意の固定対数冪より小さい。kernelノルムそのものと係数 `1/12` はMAJOR-03へ残す。

```text
MAJOR_01_RECTANGULAR_ERROR_EXPONENT=CLOSED_BY_STAGE12_N1_3A
```

## 3. Stage12-N1-3bで閉じた項目

成果物:

```text
docs/stage12-n1-3b-fixed-circle-remainder.md
```

### MAJOR-02 — fixed-circle remainder

旧2kでは

\[
\omega(X/\ell)
\]

を `ω(X)` としてconvolution全域へ引き出していたが、単調性の向きが逆であった。

Stage12-N1-3bではこの操作を撤回し、base remainderの弱い形とfinite Euler correctionの絶対 `1/2`-normから

\[
\boxed{
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1
+O\!\left(
G(rs)H_{\rm abs}(rs)X^{1/2}
\right)
}
\]

を直接証明した。

pointwise `ω(X)` savingは失うが、retained regionでは

\[
X_{r,s}\ge X_0
=
\exp\!\left((\log B)^{1/4}\right)
\]

である。`W(n)=G(n)H_abs(n)` の固定対数次数平均上界とdyadic `q=r^2+s^2` shellを使うと、outer averageは

\[
\ll
B X_0^{-1/2}(\log B)^{O(1)}
=
o\!\left(B(\log B)^{-A}\right)
\]

となり、任意の固定 `A>0` に対して十分小さい。

旧2k §2〜§3の

\[
G(rs)H_{\rm abs}(rs)X^{1/2}\omega(X)
\]

型pointwise estimateは引用禁止とし、3bのpointwise estimateとretained-region averageで置き換える。

```text
MAJOR_02_FIXED_CIRCLE_REMAINDER=CLOSED_BY_STAGE12_N1_3B
```

## 4. 次の作業 — Stage12-N1-3c

次の成果物は

```text
docs/stage12-n1-3c-coupled-region-transfer.md
```

である。

対象は監査R01のMAJOR-03。係数 `1/12` を得るcoupled-region transferを、概要ではなく独立補題として完全に書く。

最低限、次を本文上で固定する。

1. `γ(rs)` のdivisor展開後に現れる元変数、divisor変数、倍数変数の完全な和;
2. radial kernel `(r^2+s^2)^{-1}` とheight lengthを保持した二変数Abel／Stieltjes部分和分;
3. box境界値、一次変分、混合変分をまとめたkernelノルムの証明;
4. Stage12-N1-3aの修正版長方形誤差をkernel適用後に全boxで合計した評価;
5. Stage12-N1-3bのfixed-circle remainderとmain-term transferの分離;
6. odd–odd、opposite-parity、orientationのfront factor表;
7. 対数変数への変換と正確な係数 `1/12`;
8. diagonal、arc、floor endpointの境界評価。

終了条件は、単に

\[
\int_{2\max(y,z)<L}
(L-2\max(y,z))\,dy\,dz
=
\frac{L^3}{12}
\]

を計算することではない。その積分へ至る前のkernel・divisor expansion・front factorを含む等式を本文上で接続することである。

## 5. その後に残る項目

### MAJOR-04 — bundle self-containment

新しいbundleへ次を追加する。

- `C_prim(B)` の完全なcounting definition;
- `κ`, `η`, local factors, 2-adic / archimedean front factorsのconstant sheet。

### Secondary items

- Tenenbaum II.5.2のhypothesisと採用remainder caseを一対一で固定する;
- 2j原文中の壊れた `\frac` 2件を修正する;
- Finalをsummaryとして明記するか、未定義記号を補う;
- 全修復後に新しい統合稿と自己完結bundle R02を生成する。

## 6. Stage13の扱い

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

## 7. 現在の禁止事項

- Stage12-N1-2を `CLOSED`, `FINAL_COMPLETE`, `proved` と呼ばない。
- 旧2p／旧Finalの `R^(1/2+δ)S + RS^(1/2+δ)` を引用しない。
- 旧2k／旧Finalの `X^(1/2)ω(X)` fixed-circle estimateを引用しない。
- `1/12` の係数を完全導出済みと扱わない。
- 現行bundleを自己完結と呼ばない。
- Stage12からStage13 canonical countへの定数変換を先取りしない。
- ユーザーの明示的な依頼なしにPRをマージしない。

## 8. Stage12再閉包の終了条件

次のすべてを満たした時だけ再びclosedと呼ぶ。

- MAJOR-01〜03が本文上で証明されている;
- MAJOR-04を解消した自己完結bundleがある;
- Tenenbaum適用条件が固定されている;
- control characterと記号定義が修正されている;
- 新しい独立監査が `CLOSED` を返している。

## 9. 状態コード

```text
STAGE12_N1_2_REOPENED_AFTER_AUDIT_R01
STAGE12_N1_3A_RECTANGULAR_ERROR_REPAIR_COMPLETE
STAGE12_N1_3B_FIXED_CIRCLE_REMAINDER_COMPLETE
MAJOR_01=CLOSED
MAJOR_02=CLOSED
MAJOR_03=OPEN_NEXT_CENTRAL
MAJOR_04=OPEN
THEOREM_STATUS=REPAIRABLE_NOT_CLOSED
STAGE13_3_PAUSED_PENDING_STAGE12_REPAIR
NEXT_TASK=STAGE12_N1_3C_COUPLED_REGION_TRANSFER
```
