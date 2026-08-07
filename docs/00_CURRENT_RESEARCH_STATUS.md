# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-1433-JST`
>
> **CURRENT_BASE_COMMIT:** `9d4d5e4d292fa5046ac6362bddb5a6a8612e42cc`
>
> **CURRENT_STAGE:** `Stage12-N1-3i final reference closure; R08 self-contained bundle`
>
> **STAGE13_STATUS:** `PAUSED_AFTER_STAGE13_2_UNTIL_STAGE12_R08_IS_MERGED_AND_FROZEN`
>
> **R06_FULL_REVIEW_VERDICT:** `CLOSED`
>
> **R06_SECOND_INDEPENDENT_REVIEW:** `CLOSED`
>
> **LATEST_EXTERNAL_RECALCULATION:** `NO_FATAL_NO_MAJOR_NEW_GAP; LIGHT_REFERENCE_DEPENDENCIES_ONLY`
>
> **3I_TEXT_STATUS:** `FINAL_REFERENCE_DEPENDENCIES_CLOSED_IN_TEXT`
>
> **THEOREM_STATUS:** `SELF_CONTAINED_AT_STATED_EXTERNAL_THEOREM_LEVEL_PENDING_MERGE_FREEZE`

## 0. 60秒で現状復帰する順序

1. `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/stage12-n1-3i-final-reference-closure.md`
3. `docs/stage12-n1-3h-zero-base-provenance-closure.md`
4. `docs/stage12-n1-2-final-r07-self-contained.md`
5. `docs/review/stage12-n1-2-final-self-contained-manifest-20260807-r08.md`
6. `review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R08.html`
7. `docs/stage12-n1-2-final-r05.md`

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

## 2. 監査履歴の要点

R06全体ゼロベース監査は

```text
VERDICT=CLOSED
FATAL=0
MAJOR=0
NEW_CENTRAL_GAP=NONE
THEOREM_STATUS=CLOSED_FOR_PRIMITIVE_ORIENTED_COUNT
```

を返した。別の独立監査も全主要項目を再確認して `CLOSED / FATAL=0 / MAJOR=0` を返した。

その後のより厳しい外部再計算では、局所因子、`C_lambda^(0)=8 eta/pi^2`、shallow sector、rectangle exponent、radial `pi/48`、lower-limit boundary、vertical growthを独立に再計算し、新しいfatal/major gapは見つからなかった。

最後に残ったのは数学的中心gapではなく、次の軽い参照依存だった。

```text
B_beta(X)<<X still referenced to old 2p
M_delta<infinity still referenced to old 2p
Tenenbaum II.5.2 application checklist not collected in one active source
```

## 3. Stage12-N1-3i

`docs/stage12-n1-3i-final-reference-closure.md`

3iは旧2pをactive proofへ戻さず、残った参照依存を直接閉じる。

### 3.1 `B_beta(X)<<X`

prime by primeに

\[
B_\beta(s)=\zeta(s)L(s,\chi_4)J_\beta(s)
\]

を再導出し、`J_beta` の係数 `j_beta` について

\[
\sum_n\frac{|j_\beta(n)|}{n}<\infty
\]

を得る。`a=1*chi_4` の部分和は

\[
\sum_{n\le Y}a(n)\ll Y
\]

であるから convolution により

\[
\boxed{B_\beta(X)\ll X.}
\]

この粗い上界はSelberg--Delangeに依存しない。

### 3.2 coprime cross norm

`q≡1 mod4` で

\[
C_q(s_1,s_2)=1-V_q(s_1)V_q(s_2),
\qquad
V_q(s)=\frac{b_qq^{-s}}{1+(b_q-1)q^{-s}}
\]

を exact に導く。`sigma_i>=1/2+delta` でlocal weighted `l^1` massは

\[
O(q^{-\sigma_1-\sigma_2})=O(q^{-1-2\delta})
\]

なので

\[
\boxed{M_\delta=\sum_{a,b}\frac{|c(a,b)|}{(ab)^{1/2+\delta}}<\infty.}
\]

### 3.3 Selberg--Delange application map

外部定理として使用する finite-order Selberg--Delange 形を明示し、`beta` (`z=1`) と `g=1*beta` (`z=2`) について

- coefficient majorant;
- analytic factor;
- standard Selberg--Delange region;
- polynomial vertical growth;
- nonzero leading factor;

を一項ずつ対応させた。vertical growthは3hで導出済み。

Selberg--Delange theoremそのものはpublished theorem-level inputであり、Stage12内で再証明しない。

### 3.4 3a small-coefficient step

3aのsmall coefficient regionも、3iの `M_delta` とSelberg--Delange remainderだけから式を展開し直した。したがって旧2p §3.1へのactive dependencyはない。

```text
BETA_LINEAR_UPPER_BOUND=CLOSED_DIRECTLY_BY_STAGE12_N1_3I_SECTION_1
BETA_COPRIME_CROSS_WEIGHTED_NORM=CLOSED_DIRECTLY_BY_STAGE12_N1_3I_SECTION_2
SELBERG_DELANGE_APPLICATION_MAP=CLOSED_BY_STAGE12_N1_3I_SECTION_3
RECTANGLE_SMALL_COEFFICIENT_STEP=CLOSED_BY_STAGE12_N1_3I_SECTION_4
OLD_2P_ACTIVE_DEPENDENCY=NONE
```

## 4. Final R08 self-contained bundle

```text
BUNDLE_ID=PC-N1-2-FINAL-SELF-CONTAINED-20260807-R08
COMPLETED_THROUGH=Stage12-N1-3i
FINAL_DOCUMENT=docs/stage12-n1-2-final-r07-self-contained.md
MANIFEST=docs/review/stage12-n1-2-final-self-contained-manifest-20260807-r08.md
HTML=review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R08.html
SOURCE_SNAPSHOT_COMMIT=4fa4c70ad375dc90c5a99cd8d39f4caf4c47ff34
SOURCE_LEDGER_SHA256=77b40002d4534ee5e24f8d7f711e7f12d1ea51994d58affe49e161cf33f71248
```

R08 physical pageは9 sourceを全文収録する。historical sourceは由来確認だけに使用し、superseded error claimをactive proofへ戻さない。

```text
ACTIVE_CURRENT_PROOF=docs/stage12-n1-2-final-r05.md
ACTIVE_RECTANGLE_DERIVATION=Stage12-N1-3a_Lemma_3a.1
ACTIVE_VERTICAL_AND_RADIAL_BOUNDARY=Stage12-N1-3h
ACTIVE_FINAL_REFERENCE_CLOSURE=Stage12-N1-3i
3A_REFERENCES_TO_OLD_2P_INPUTS=SUPERSEDED_BY_3I
2F_FORMAL_RAW_ASYMPTOTIC=PROVENANCE_ONLY
2K_OLD_FIXED_CIRCLE_REMAINDER=SUPERSEDED_BY_3B_AND_3E
2K_OLD_SHALLOW_BOUND=SUPERSEDED_BY_3G
3A_OLD_RETAINED_MIN_RS_APPLICATION=SUPERSEDED_BY_3F
OLD_2P_ACTIVE_DEPENDENCY=NONE
SUPERSEDED_FIXED_BC_KERNEL=NOT_USED
```

## 5. 現在の扱い

追加の外部レビューをStage12の必須手順にはしない。R08は、これまでのCLOSED監査と後続の独立再計算を踏まえて、残った参照依存を本文内で閉じた最終自己完結版とする。

ただしGitHub上の変更はPRで管理し、ユーザーの明示依頼なしにマージしない。Stage13-3はR08をmainへマージしてStage12をfreezeした後に再開する。

## 6. State codes

```text
STAGE12_N1_3A_COMPLETE
STAGE12_N1_3B_COMPLETE
STAGE12_N1_3C_G_COMPLETE
STAGE12_N1_3D_COMPLETE
STAGE12_N1_3E_COMPLETE
STAGE12_N1_3F_COMPLETE
STAGE12_N1_3G_COMPLETE
STAGE12_N1_3H_COMPLETE
STAGE12_N1_3I_COMPLETE_IN_TEXT
R06_FULL_REVIEW_VERDICT=CLOSED
LATEST_EXTERNAL_NEW_FATAL=0
LATEST_EXTERNAL_NEW_MAJOR=0
FINAL_REFERENCE_DEPENDENCIES=CLOSED_IN_TEXT
SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
THEOREM_STATUS=SELF_CONTAINED_AT_STATED_EXTERNAL_THEOREM_LEVEL_PENDING_MERGE_FREEZE
STAGE13_3_PAUSED_PENDING_STAGE12_R08_MERGE_FREEZE
NEXT_TASK=VERIFY_AND_FREEZE_R08
```
