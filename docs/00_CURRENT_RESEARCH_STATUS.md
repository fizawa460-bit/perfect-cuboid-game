# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-STAGE13-RESUME`
>
> **CURRENT_BASE_COMMIT:** `df40358b5e9da66599b70a1c65e71d587f6fca04`
>
> **CURRENT_STAGE:** `Stage13-3 — Origin of the leading 2`
>
> **STAGE12_STATUS:** `FROZEN_AFTER_R09`
>
> **STAGE13_STATUS:** `ACTIVE_AFTER_STAGE13_2`
>
> **STAGE13_WORKING_POLICY:** `docs/stage13-working-file-policy.md`
>
> **STAGE13_CANONICAL_WORKING_FILE:** `docs/stage13-main.md`
>
> **THEOREM_STATUS:** `CLOSED_FOR_PRIMITIVE_ORIENTED_COUNT_AT_STATED_EXTERNAL_THEOREM_LEVEL`

## 0. 現状

Stage12-N1-2 は R09 をもって終了し、この状態で freeze する。

最終対象は 3d definition sheet で定義された primitive oriented count

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3.
\]

この定理の範囲は primitive oriented count のみであり、perfect cuboid の存在・不存在、canonical count、exact-one-face count、または最終 `2:1:1` 比を主張しない。

## 1. Stage12 freeze point

```text
BUNDLE_ID=PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09
COMPLETED_THROUGH=Stage12-N1-3j
MERGE_COMMIT=df40358b5e9da66599b70a1c65e71d587f6fca04
FINAL_DOCUMENT=docs/stage12-n1-2-final-r08-self-contained.md
MANIFEST=docs/review/stage12-n1-2-final-self-contained-manifest-20260807-r09.md
HTML=review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html
CONTENT_SHA256=0da06c78bbb546039dbe8d423dcc6ed403fe1af90d777488c2393c0c77c16848
SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
SELBERG_DELANGE_THEOREM=EXTERNAL_PUBLISHED_THEOREM_LEVEL_INPUT
```

Stage12 は追加の外部 AI 監査を必須ゲートとしない。今後 Stage12 を変更するのは、新しい数学的反例・明確な誤り・Stage13 で発見された genuine dependency conflict・論文化時の編集上の必要が生じた場合に限る。

## 2. Stage13 の確定済み部分

### Stage13-1 — Definition

Initial source:

```text
docs/stage13-1-definition.md
```

primitive、canonical ordering `a<b<c`、space-diagonal cutoff `d<=B`、exactly-one-face の三方向 count

\[
N_{ab}(B),\quad N_{ac}(B),\quad N_{bc}(B)
\]

を固定済み。

### Stage13-2 — Structural decomposition

Initial source:

```text
docs/stage13-2-decomposition.md
```

方向別 count を少なくとも次の層へ分解する枠組みを固定済み。

- raw incidence / overlap correction;
- canonical size-order effect;
- full orientation lift;
- primitive layer;
- parity layer;
- representation multiplicity;
- local-density layer;
- cutoff / boundary layer.

Stage13-2 は `2:1:1` を仮定せず、どの mechanism が比を作るかを後続で分離して検証するための構造分解である。

## 3. Stage13 working-file policy

Stage13 は `docs/stage13-working-file-policy.md` に従う。

数学本体は原則

```text
docs/stage13-main.md
```

一つを canonical working source とする。

既存の Stage13-1 / Stage13-2 文書は、`stage13-main.md` を開始するときに §1 / §2 へ統合し、その後は historical initial source として保持する。

修正が必要になった場合は、新しい repair document を増やすのではなく `stage13-main.md` の該当 section を直接修正する。変更履歴は Git commit / PR が保持する。

別ファイルへ分離するのは、data、scripts、長大で独立な support calculation、review manifest / generated HTML、archive snapshot、将来の publication draft などに限る。

外部レビューは on demand とし、必要時のみ canonical file と明示的 support source から一枚の review bundle を生成する。

## 4. 現在の作業 — Stage13-3

Task 13-3 は **leading `2` の起源を特定すること**。

中心質問は

> なぜ canonical exact-one-face count で `ab_only` が他の二方向のおよそ2倍に見えるのか。

候補を先に結論とせず、次を順に切り分ける。

1. raw incidence の段階ですでに `2` が存在するか;
2. exact-one overlap correction が `2` を生成または増幅するか;
3. canonical size-order chamber の幾何が leading asymmetry を作るか;
4. full orientation multiplicity だけでは `1:1:1` に対称化されるという Stage13-2 の事実と整合するか;
5. parity / primitive / local density / Stage12 parameter-fiber multiplicity のどれが方向差を担うか。

次の実作業は

```text
1. docs/stage13-main.md を作る
2. Stage13-1 を §1 へ統合
3. Stage13-2 を §2 へ統合
4. §3 で Stage13-3 を開始
```

である。

## 5. Stage13 の研究原則

- `2:1:1` を厳密な極限比として先取りしない。
- Stage12 の oriented asymptotic を canonical exact-one-face count に定数倍で自動変換しない。
- orientation、canonical ordering、multiplicity、parity、local density を混同しない。
- finite data は動機・診断に使用できるが、漸近定理の代用にしない。
- leading `2` の mechanism と `ac_only` / `bc_only` のズレは分離して扱う。
- Stage13 の数学的修正は canonical working file を直接直す。
- 軽微な修正ごとに全体ゼロベース再監査を自動要求しない。

## 6. State codes

```text
STAGE12_N1_2=FROZEN
STAGE12_FINAL_BUNDLE=R09
STAGE12_MERGE_COMMIT=df40358b5e9da66599b70a1c65e71d587f6fca04
STAGE12_THEOREM_SCOPE=PRIMITIVE_ORIENTED_COUNT_ONLY
STAGE12_SELF_CONTAINMENT=COMPLETE_AT_STATED_EXTERNAL_THEOREM_LEVEL
STAGE13_WORKING_POLICY=ACTIVE
STAGE13_CANONICAL_WORKING_FILE=docs/stage13-main.md
STAGE13_DIRECT_SECTION_EDIT=DEFAULT
STAGE13_EXTERNAL_REVIEW=ON_DEMAND
STAGE13_1=COMPLETE
STAGE13_2=COMPLETE
STAGE13_3=ACTIVE
NEXT_TASK=BOOTSTRAP_STAGE13_MAIN_AND_START_SECTION_3
```
