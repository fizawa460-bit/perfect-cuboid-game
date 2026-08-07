# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-1516-JST`
>
> **CURRENT_BASE_COMMIT:** `ba44bd6772e0c3d6d5e4b118886b514c5c46247e`
>
> **CURRENT_STAGE:** `Stage12-N1-3j final self-containment detail; R09`
>
> **STAGE13_STATUS:** `PAUSED_AFTER_STAGE13_2_PENDING_STAGE12_R09_MERGE_FREEZE`
>
> **R06_FULL_REVIEW_VERDICT:** `CLOSED`
>
> **R06_SECOND_INDEPENDENT_REVIEW:** `CLOSED`
>
> **R08_MERGE_COMMIT:** `ba44bd6772e0c3d6d5e4b118886b514c5c46247e`
>
> **LATEST_EXTERNAL_RECALCULATION:** `NO_FATAL_NO_MAJOR_NEW_GAP; ONE_SELF_CONTAINMENT_DETAIL`
>
> **3J_TEXT_STATUS:** `FINAL_SELF_CONTAINMENT_DETAIL_CLOSED_IN_TEXT`
>
> **THEOREM_STATUS:** `SELF_CONTAINED_AT_STATED_EXTERNAL_THEOREM_LEVEL_PENDING_R09_MERGE_FREEZE`

## 0. 60秒で現状復帰する順序

1. `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/stage12-n1-3j-weighted-l1-and-vertical-closure.md`
3. `docs/stage12-n1-2-final-r08-self-contained.md`
4. `docs/review/stage12-n1-2-final-self-contained-manifest-20260807-r09.md`
5. `review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html`
6. `docs/stage12-n1-2-final-r07-self-contained.md`
7. `docs/stage12-n1-3i-final-reference-closure.md`

## 1. 定理の範囲

3d definition sheetで定義された primitive oriented count について

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3.
\]

このStage12定理はperfect cuboidの存在・不存在、canonical count、exact-one-face count、Stage13の最終比率を主張しない。

## 2. これまでの監査

R06全体ゼロベース監査は

```text
VERDICT=CLOSED
FATAL=0
MAJOR=0
NEW_CENTRAL_GAP=NONE
THEOREM_STATUS=CLOSED_FOR_PRIMITIVE_ORIENTED_COUNT
```

を返した。別の独立監査も主要項目を再計算し `CLOSED / FATAL=0 / MAJOR=0` を返した。

その後の厳しい外部再計算では、局所因子、`C_lambda^(0)=8 eta/pi^2`、shallow sector、rectangle exponent、radial `pi/48`、lower-limit boundary、`B_beta(X)<<X`、cross correction の局所代数を独立に追跡し、新しいfatal/major gapは見つからなかった。

R08後の最終指摘は次の一箇所だった。

```text
sum_q ||C_q-1||_delta < infinity
=> global Euler-product coefficient weighted l1 norm < infinity
```

が標準的Banach-algebra事実として一文で省略されていた。またvertical growthについて、functional equationを使う対象が`L(s,chi_4)`であり`J_beta`ではないことを明示するとより自己完結になる、と指摘された。

## 3. Stage12-N1-3j

`docs/stage12-n1-3j-weighted-l1-and-vertical-closure.md`

3jは二変数Dirichlet convolutionについて

\[
\|f*g\|_\delta\le\|f\|_\delta\|g\|_\delta
\]

をTonelliにより直接証明する。weighted空間が通常の`l^1(N^2)`と等長同型で完備であることも明示する。

局所因子を

\[
C_q=1+E_q,
\qquad
\eta_q:=\|E_q\|_\delta
\ll q^{-1-2\delta}
\]

とすると

\[
\sum_q\eta_q<\infty.
\]

有限積

\[
P_Q=\prod_{q\le Q}(1+E_q)
\]

について

\[
\|P_Q\|_\delta
\le
\prod_{q\le Q}(1+\eta_q)
\le
\exp\left(\sum_q\eta_q\right)
\]

と一様評価し、さらにtail productからCauchy estimateを得る。完備性によりglobal coefficient列へ収束し、各固定係数は有限個の素数しか含まないためEuler productの係数と一致する。従って

\[
\boxed{
M_\delta
=
\sum_{a,b\ge1}
\frac{|c(a,b)|}{(ab)^{1/2+\delta}}
<\infty.
}
\]

vertical growthは明確に分離する。

```text
J_beta: absolute convergence => bounded
L(s,chi_4): functional equation + Stirling + Phragmen--Lindelof => polynomial growth
H_beta=L*J_beta: product => polynomial growth
J_BETA_FUNCTIONAL_EQUATION_ASSUMED=false
```

`J_beta`にfunctional equationは仮定しない。

## 4. Final R09 self-contained bundle

```text
BUNDLE_ID=PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09
COMPLETED_THROUGH=Stage12-N1-3j
FINAL_DOCUMENT=docs/stage12-n1-2-final-r08-self-contained.md
MANIFEST=docs/review/stage12-n1-2-final-self-contained-manifest-20260807-r09.md
HTML=review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html
SOURCE_SNAPSHOT_COMMIT=d69a6e2ee352700660776f55a749eebb432552f9
SOURCE_LEDGER_SHA256=800a664bf940e751cb1fafc7758a2692c6950eecb6ef94784738d276a4a0debe
CONTENT_SHA256=0da06c78bbb546039dbe8d423dcc6ed403fe1af90d777488c2393c0c77c16848
```

R09はR08 self-contained proof全文と3j全文を一つのphysical pageへ収録する。

## 5. 外部定理の境界

Selberg--Delange theoremそのものは published theorem-level input として使用し、Stage12内で再証明しない。そのworking formと`beta (z=1)` / `g=1*beta (z=2)`への適用対応はR08本文に収録済みである。

従って現在の自己完結性は

```text
SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
SELBERG_DELANGE_THEOREM=EXTERNAL_PUBLISHED_THEOREM_LEVEL_INPUT
```

という意味で固定する。

## 6. 現在の扱い

追加の外部AIレビューをStage12の必須ゲートにはしない。R09をmainへマージした時点でStage12-N1-2をこの定理レベルでfreezeし、その後Stage13-3へ戻る。

ユーザーの明示依頼なしにPRをマージしない。

## 7. State codes

```text
STAGE12_N1_3A_COMPLETE
STAGE12_N1_3B_COMPLETE
STAGE12_N1_3C_G_COMPLETE
STAGE12_N1_3D_COMPLETE
STAGE12_N1_3E_COMPLETE
STAGE12_N1_3F_COMPLETE
STAGE12_N1_3G_COMPLETE
STAGE12_N1_3H_COMPLETE
STAGE12_N1_3I_COMPLETE
STAGE12_N1_3J_COMPLETE_IN_TEXT
R06_FULL_REVIEW_VERDICT=CLOSED
LATEST_EXTERNAL_NEW_FATAL=0
LATEST_EXTERNAL_NEW_MAJOR=0
WEIGHTED_L1_DIRICHLET_SUBMULTIPLICATIVITY=CLOSED
EULER_PRODUCT_TO_GLOBAL_WEIGHTED_L1=CLOSED
VERTICAL_GROWTH_ROLE_SEPARATION=CLOSED
J_BETA_FUNCTIONAL_EQUATION_ASSUMED=false
OLD_2P_ACTIVE_DEPENDENCY=NONE
FINAL_REFERENCE_DEPENDENCIES=CLOSED_IN_TEXT
SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
THEOREM_STATUS=SELF_CONTAINED_AT_STATED_EXTERNAL_THEOREM_LEVEL_PENDING_R09_MERGE_FREEZE
STAGE13_3_PAUSED_PENDING_STAGE12_R09_MERGE_FREEZE
NEXT_TASK=MERGE_AND_FREEZE_R09_THEN_RESUME_STAGE13_3
```
