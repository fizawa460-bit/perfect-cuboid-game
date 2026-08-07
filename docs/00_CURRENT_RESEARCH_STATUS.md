# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-STAGE13-RESUME`
>
> **REPOSITORY_LAYOUT:** `STAGE_FIRST`
>
> **CURRENT_STAGE:** `Stage13-3 — Origin of the leading 2`
>
> **STAGE12_STATUS:** `FROZEN_AFTER_R09`
>
> **STAGE13_STATUS:** `ACTIVE_AFTER_STAGE13_2`
>
> **STAGE13_WORKING_POLICY:** `stages/stage13/policy.md`
>
> **STAGE13_CANONICAL_WORKING_FILE:** `stages/stage13/main.md`
>
> **THEOREM_STATUS:** `CLOSED_FOR_PRIMITIVE_ORIENTED_COUNT_AT_STATED_EXTERNAL_THEOREM_LEVEL`

## 0. 現状

Stage12-N1-2 は R09 をもって終了し、この状態で freeze する。

最終対象は primitive oriented count

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3.
\]

この定理の範囲は primitive oriented count のみであり、perfect cuboid の存在・不存在、canonical count、exact-one-face count、または最終 `2:1:1` 比を主張しない。

研究資産は stage-first layout を採用する。Stage 固有の docs / scripts / data / archive は `stages/<stage>/` の下へ置き、stage/task 情報は長い filename suffix ではなく path で表す。

## 1. Stage12 freeze point and active files

```text
BUNDLE_ID=PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09
COMPLETED_THROUGH=Stage12-N1-3j
MERGE_COMMIT=df40358b5e9da66599b70a1c65e71d587f6fca04
FINAL_DOCUMENT=stages/stage12/final.md
MANIFEST=stages/stage12/manifest-r09.md
HTML=review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html
ARCHIVE=stages/stage12/archive/
CONTENT_SHA256=0da06c78bbb546039dbe8d423dcc6ed403fe1af90d777488c2393c0c77c16848
SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
SELBERG_DELANGE_THEOREM=EXTERNAL_PUBLISHED_THEOREM_LEVEL_INPUT
```

`stages/stage12/final.md` is the canonical Stage12 proof text for normal reading. The R09 HTML is the single active external-review page. The R09 manifest remains active for bundle identity.

Earlier derivations, repairs, superseded finals, audit manifests, old HTML pages, old workflows, scripts, and generated audit data are archive-only history under `stages/stage12/archive/`. `stages/stage12/archive/INDEX.md` maps each historical task to its script/data files.

Stage12 は追加の外部 AI 監査を必須ゲートとしない。今後 Stage12 を変更するのは、新しい数学的反例・明確な誤り・Stage13 で発見された genuine dependency conflict・論文化時の編集上の必要が生じた場合に限る。

## 2. Stage13 の確定済み部分

### Stage13-1 — Definition

Initial source:

```text
stages/stage13/initial/definition.md
```

primitive、canonical ordering `a<b<c`、space-diagonal cutoff `d<=B`、exactly-one-face の三方向 count

\[
N_{ab}(B),\quad N_{ac}(B),\quad N_{bc}(B)
\]

を固定済み。

### Stage13-2 — Structural decomposition

Initial source:

```text
stages/stage13/initial/structural-decomposition.md
```

方向別 count を raw incidence / overlap correction、canonical size-order effect、full orientation lift、primitive、parity、representation multiplicity、local density、cutoff / boundary の各 layer へ分ける枠組みを固定済み。

Stage13-2 は `2:1:1` を仮定せず、どの mechanism が比を作るかを後続で分離して検証するための構造分解である。

## 3. Stage13 working-file policy

Stage13 は `stages/stage13/policy.md` に従う。数学本体は原則 `stages/stage13/main.md` 一つを canonical working source とする。

既存の Stage13-1 / Stage13-2 文書は、`main.md` を開始するときに §1 / §2 へ統合し、その後は historical initial source として保持する。修正履歴は Git commit / PR が保持する。

Stage13 固有の scripts / data は

```text
stages/stage13/scripts/<task>/<purpose>.py
stages/stage13/data/<task>/<purpose>.json
```

のように、task context を path へ置く。外部レビューは on demand とする。

## 4. 現在の作業 — Stage13-3

Task 13-3 は **leading `2` の起源を特定すること**。

中心質問は

> なぜ canonical exact-one-face count で `ab_only` が他の二方向のおよそ2倍に見えるのか。

候補を先に結論とせず、raw incidence、exact-one overlap correction、canonical size-order chamber、full orientation multiplicity、parity / primitive / local density / Stage12 parameter-fiber multiplicity を順に切り分ける。

次の実作業は

```text
1. stages/stage13/main.md を作る
2. Stage13-1 を §1 へ統合
3. Stage13-2 を §2 へ統合
4. §3 で Stage13-3 を開始
```

である。

## 5. State codes

```text
REPOSITORY_LAYOUT=STAGE_FIRST
STAGE12_N1_2=FROZEN
STAGE12_FINAL_BUNDLE=R09
STAGE12_CANONICAL_DOCUMENT=stages/stage12/final.md
STAGE12_ACTIVE_MANIFEST=stages/stage12/manifest-r09.md
STAGE12_ACTIVE_REVIEW_HTML=review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html
STAGE12_ARCHIVE=stages/stage12/archive/
STAGE12_THEOREM_SCOPE=PRIMITIVE_ORIENTED_COUNT_ONLY
STAGE12_SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
STAGE13_WORKING_POLICY=stages/stage13/policy.md
STAGE13_CANONICAL_WORKING_FILE=stages/stage13/main.md
STAGE13_DIRECT_SECTION_EDIT=DEFAULT
STAGE13_SUPPORT_LAYOUT=STAGE_FIRST_TASK_SUBDIRECTORY
STAGE13_EXTERNAL_REVIEW=ON_DEMAND
STAGE13_1=COMPLETE
STAGE13_2=COMPLETE
STAGE13_3=ACTIVE
NEXT_TASK=BOOTSTRAP_STAGE13_MAIN_AND_START_SECTION_3
```
