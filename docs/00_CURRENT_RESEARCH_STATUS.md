# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-1205-JST`
>
> **CURRENT_BASE_COMMIT:** `341ed4719af88cb5967e890e6760392ae7f46dbf`
>
> **CURRENT_STAGE:** `Stage12-N1-3e prepared; R03 limited re-review next`
>
> **STAGE13_STATUS:** `PAUSED_AFTER_STAGE13_2`
>
> **SERIES_STATUS:** `STAGE12_R02_LIMITED_REVIEW_REPAIR_PENDING_R03`
>
> **R01_RESOLVED:** `MAJOR-01, MAJOR-02, MAJOR-03, MAJOR-04, CLARIFICATION-01, MINOR-01, MINOR-02`
>
> **R02_LIMITED_REVIEW_VERDICT:** `REPAIRABLE`
>
> **R02_REMAINING_LOCAL_GAPS:** `OUTER_AVERAGE_LEMMA,PARITY_WEIGHTED_LOCAL_FACTOR_IDENTITY`
>
> **3E_TEXT_STATUS:** `BOTH_LOCAL_GAPS_CLOSED_IN_TEXT_PENDING_LIMITED_REAUDIT`
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_LIMITED_REAUDIT`

## 0. 60秒で現状復帰する順序

1. `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/stage12-n1-3e-local-gap-closure.md`
3. `docs/review/stage12-n1-2-limited-rereview-manifest-20260807-r03.md`
4. `review/PC-N1-2-LIMITED-REREVIEW-20260807-R03.html`
5. `docs/stage12-n1-2-final-r02.md`
6. `docs/stage12-n1-3d-definition-sheet.md`
7. `docs/stage12-n1-3d-constant-sheet.md`
8. `docs/stage12-n1-3d-selberg-delange-reference-lock.md`
9. `review/PC-N1-2-REPAIRED-PROOF-20260807-R02.html`

必要に応じて修復原文を読む。

```text
docs/stage12-n1-3a-rectangular-error-repair.md
docs/stage12-n1-3b-fixed-circle-remainder.md
docs/stage12-n1-3c-coupled-region-transfer.md
docs/stage12-n1-3c-g-residue-first-closure.md
```

## 1. 現在の候補定理

3d definition sheetで定義したprimitive oriented countについて

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3.
\]

R01の中心修復は文書上完了した。R02修正箇所限定レビューも、中心経路を再びopenとはせず、二つの局所的な明記不足だけを指摘した。

ただし、R03限定再監査が `CLOSED` を返すまでは「証明済み完成定理」と扱わない。

## 2. R02修正箇所限定レビュー

判定は

```text
VERDICT=REPAIRABLE
CLOSED=MAJOR_01,MAJOR_04,MINOR_01,MINOR_02
CONDITIONALLY_CLOSED=CLARIFICATION_01
PARTIALLY_CLOSED=MAJOR_02,MAJOR_03
REMAINING_LOCAL_GAPS=OUTER_AVERAGE_LEMMA,PARITY_WEIGHTED_LOCAL_FACTOR_IDENTITY
FATAL=0
OPEN_CENTRAL_ROUTE=0
```

であった。

重要なのは、次の旧中心問題は修復方向が承認されたことである。

- 不正な長方形誤差指数の強化は撤回済み;
- `omega(X/ell)` の不正な引き出しは撤回済み;
- radial kernelを落とした模式的移送は撤回済み;
- fixed-`(b,c)` anisotropic kernel lemmaは不要としてsupersede済み。

残った二点は、既存の結論をbundle内で再計算できる形にする局所補題である。

## 3. Stage12-N1-3e — local gap closure

```text
docs/stage12-n1-3e-local-gap-closure.md
```

### Part I — outer average

次を定義から表示した。

\[
W(n)=G(n)H_{\rm abs}(n).
\]

prime powersでは

\[
W(p^t)=1
\quad(p=2\text{ or }p\equiv3\pmod4),
\]

\[
W(q^t)=2t+1+\frac{4t}{\sqrt q-1}
\quad(q\equiv1\pmod4).
\]

Dirichlet級数を

\[
\mathcal W(s)=\zeta(s)^2L(s,\chi_4)E_W(s)
\]

と分解し、`E_W` が `Re s>1/2` の固定内側半平面で絶対収束することを示した。locked `z=2` Selberg--Delangeから

\[
M_W(T)=\sum_{n\le T}W(n)\ll T\log(2T)
\]

を得る。

これにより

\[
\sum_{\substack{r<s,(r,s)=1\\Q<r^2+s^2\le2Q}}W(rs)
\ll Q(\log(2Q))^2
\]

およびretained regionの総誤差

\[
O\!\left(BX_0^{-1/2}(\log B)^2\right)
=o\!\left(B(\log B)^{-A}\right)
\]

を任意の固定 `A>0` について導いた。

### Part II — parity-weighted local constant

odd-prime coprime factor、2-adic parity factor、両合同類のnormalized local factorsを明示した。

\[
D_{\lambda,p}(s_1,s_2)
=1+U_p(s_1)+U_p(s_2),
\]

\[
D_{\lambda,2}(s_1,s_2)
=2+\frac{x}{1-x}+\frac{y}{1-y},
\qquad
C_{\lambda,2}(1,1)=1.
\]

prime-by-primeに積を比較して

\[
C_\lambda^{(0)}
=\eta\prod_{\ell\text{ odd prime}}(1-\ell^{-2})
=\frac8{\pi^2}\eta
\]

を導いた。

現在の文書上の状態は

```text
OUTER_AVERAGE_LEMMA=CLOSED_BY_STAGE12_N1_3E_PART_I
PARITY_WEIGHTED_LOCAL_FACTOR_IDENTITY=CLOSED_BY_STAGE12_N1_3E_PART_II
R02_REMAINING_LOCAL_GAPS=NONE_IN_TEXT
```

である。

## 4. R03限定再監査bundle

```text
BUNDLE_ID=PC-N1-2-LIMITED-REREVIEW-20260807-R03
MANIFEST=docs/review/stage12-n1-2-limited-rereview-manifest-20260807-r03.md
HTML=review/PC-N1-2-LIMITED-REREVIEW-20260807-R03.html
SOURCE_SNAPSHOT_COMMIT=bd8fe51b4466ddc91276f9f7699f3a8bdb490f4c
SOURCE_LEDGER_SHA256=a752f5f42c17944c09d2d8ebff6432f74d772b88d5463d2aa3af0fbd5069b774
```

R03 HTMLは次を一つの物理ページへ埋め込む。

1. 親R02 self-contained proof bundleの全main content;
2. Stage12-N1-3e supplementの全文。

限定レビュー対象は次の二点だけである。

```text
OUTER_AVERAGE_LEMMA
PARITY_WEIGHTED_LOCAL_FACTOR_IDENTITY
```

## 5. 重要な証明戦略

3cで設定したfixed-`(b,c)` anisotropic kernel lemmaは、最終定理より強く不要だった。

```text
OLD_3C_G_FIXED_DIVISOR_KERNEL=SUPERSEDED_NOT_REQUIRED
```

最終ルートは除数展開を元へ戻して

\[
g(n)=\pi\gamma(n)=(1*\beta)(n)
\]

を元変数 `(r,s)` 上で平均するresidue-first routeである。Stage12-N1-3eもこの経路を変更していない。

## 6. 次の作業

1. PR #77をCI成功状態でマージする;
2. `PC-N1-2-LIMITED-REREVIEW-20260807-R03` を限定再監査へ渡す;
3. 二項目とも `CLOSED` なら、R02限定レビューを閉じる;
4. その後にStage12全体の最終状態を更新する。

R03で要求する判定は

```text
CLOSED
REPAIRABLE
OPEN
STALE_SOURCE
UNREADABLE_SOURCE
```

である。

## 7. Stage13の扱い

Stage13-1とStage13-2の構造的成果は保持するが、Stage13-3以降はStage12再監査まで停止する。

- canonical counting convention;
- raw incidence / overlap ledger;
- equal-weight `S_3` orientationが `1:1:1` へ対称化すること;
- orientation multiplicity単独ではcanonical `2:1:1` を説明できないこと。

Stage12のoriented asymptoticからcanonical定数への自動変換は行わない。

## 8. 禁止事項

- R03限定再監査前に `CLOSED`, `FINAL_COMPLETE`, `proved` と呼ばない。
- R02の `REPAIRABLE` 判定を無視しない。
- fixed-`(b,c)` kernel lemmaを証明済みまたは必要と扱わない。
- specific `3/5` remainderをreference lock済みinputとして引用しない。
- Stage12からStage13 canonical countへ固定係数変換しない。
- ユーザーの明示依頼なしにPRをマージしない。

## 9. State codes

```text
STAGE12_N1_3A_COMPLETE
STAGE12_N1_3B_COMPLETE
STAGE12_N1_3C_G_COMPLETE
STAGE12_N1_3D_COMPLETE
STAGE12_N1_3E_COMPLETE_IN_TEXT
R02_LIMITED_REVIEW_VERDICT=REPAIRABLE
R02_LOCAL_GAPS_CLOSED_IN_TEXT_PENDING_R03
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_LIMITED_REAUDIT
STAGE13_3_PAUSED_PENDING_STAGE12_REAUDIT
NEXT_TASK=LIMITED_REREVIEW_OF_PC_N1_2_R03
```