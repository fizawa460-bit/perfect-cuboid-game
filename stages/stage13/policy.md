# Stage13 working-file policy

> **STATUS:** `ACTIVE_POLICY`
>
> **SCOPE:** Stage13 structural analysis
>
> **CANONICAL_WORKING_FILE:** `stages/stage13/main.md`

## 1. 基本方針

Stage13 の数学本体は、原則として **一つの canonical working file** に集約する。

```text
stages/stage13/main.md
```

Task 13-1, 13-2, 13-3, ... は、この一つの文書の section として順に育てる。

Stage12 のように、修正ごとに `3a`, `3b`, `3c`, ... 型の patch document を増やす運用は Stage13 では標準にしない。

## 2. 修正方法

数学的な誤り、記述不足、定義変更、補題修正が見つかった場合は、原則として `stages/stage13/main.md` の該当 section を **直接修正する**。

過去版を残す目的で別の repair file を作らない。履歴は Git commit / pull request が保持する。

従って、

```text
current mathematical truth = latest merged stages/stage13/main.md
historical change record    = Git history / PR history
```

と分離する。

## 3. Stage-first support layout

Stage固有の context はファイル名の末尾ではなく path に置く。

新しい Stage13 support asset は原則

```text
stages/stage13/scripts/<task>/<purpose>.py
stages/stage13/data/<task>/<purpose>.json
```

のように配置する。

例:

```text
stages/stage13/scripts/13-3/check_fiber_multiplicity.py
stages/stage13/data/13-3/fiber_multiplicity_report.json
```

`check_fiber_multiplicity_stage13_3.py` のように stage/task 情報を長い suffix として重複させない。

## 4. 分離してよいもの

次は canonical working file から分離してよい。

- 大量の数値データ;
- 列挙結果、JSON、CSV 等の raw data;
- 検証・列挙・可視化用 scripts;
- 長大な補助計算で、主証明から独立に参照できるもの;
- external review 用の manifest / generated HTML;
- publication 用に後から作る LaTeX / polished draft;
- provenance や archive を目的とする固定 snapshot。

ただし、**主張を成立させるために必要な数学的論証そのもの**は、外部レビュー時に canonical file だけでは追えなくならないよう、原則 `main.md` に置く。

## 5. 例外として別 mathematical file を作る条件

別の数学文書を作るのは、次のいずれかを満たす場合に限る。

1. その補題・計算が Stage13 本体から独立した再利用可能な結果である;
2. データ量・式量が大きく、本体へ入れると主要論理が読めなくなる;
3. provenance / frozen archive として固定する必要がある;
4. external review bundle の生成物である。

単に「ここを修正した」という理由だけでは別ファイルを作らない。

## 6. Stage13-1 / Stage13-2 の扱い

既存の完成済み初期 source は

```text
stages/stage13/initial/definition.md
stages/stage13/initial/structural-decomposition.md
```

に保持する。

`stages/stage13/main.md` を開始するときに、この二つの active content を §1, §2 として統合する。その後の修正は `main.md` 側を canonical とし、initial 文書は原則更新しない。

## 7. Task と section の対応

基本対応は次とする。

```text
§1  Task 13-1  Definition
§2  Task 13-2  Structural decomposition
§3  Task 13-3  Origin of the leading 2
§4  Task 13-4  Origin of the two 1s
§5  Task 13-5  Define the deviation
§6  Task 13-6  Classify the deviation
§7  Task 13-7  Asymptotic behaviour
§8  Task 13-8  Stage12 connection
§9  Task 13-9  Main structural theorem
§10 Task 13-10 Final explanation
```

必要なら subsection を増やすが、Task ごとに独立 repair file を増やさない。

## 8. External review policy

外部レビューは毎回の変更で必須としない。

レビューが必要になった時点で、原則として `stages/stage13/main.md` をそのまま渡す。

補助資料が必要な場合のみ、

```text
canonical stages/stage13/main.md
+ explicitly required support sources
=> one generated review HTML / bundle
```

を作る。

review bundle は監査用の生成物であり、数学本体の canonical source にはしない。

## 9. Review で問題が見つかった場合

レビュー指摘に対する標準処理は次とする。

```text
1. 指摘を再計算する
2. true gap か clarification か分類する
3. stages/stage13/main.md の該当 section を直接修正する
4. 必要な補助資料だけ更新する
5. Git/PR に修正理由を残す
6. 必要なときだけ該当箇所を再レビューする
```

全体ゼロベース再監査を、軽微な修正ごとに自動的には要求しない。

## 10. Publication policy

将来論文化する場合も、`stages/stage13/main.md` を技術原稿の母艦として保持する。

投稿用文書は別途生成し、

- 重複削除;
- theorem / lemma 順序の最適化;
- notation 統一;
- bibliography;
- abstract / introduction;
- appendix 分離;
- LaTeX / PDF 組版

を行う。

投稿用の圧縮によって、technical source の情報を失わせない。

## 11. Stage12 freeze boundary

Stage12-N1-2 は R09 で freeze する。Stage12 の active entry point は `stages/stage12/README.md` に記録する。

Stage13 の都合だけで Stage12 を routine に再編集・再監査しない。Stage12 を reopen するのは、

- concrete mathematical error;
- explicit counterexample;
- Stage13 で発見された genuine dependency conflict;
- publication editing

がある場合に限る。

## 12. State codes

```text
STAGE13_CANONICAL_WORKING_FILE=stages/stage13/main.md
STAGE13_DIRECT_SECTION_EDIT=DEFAULT
STAGE13_PATCH_DOCUMENTS=NONDEFAULT
STAGE13_GIT_HISTORY=CHANGE_LOG
STAGE13_SUPPORT_LAYOUT=STAGE_FIRST_TASK_SUBDIRECTORY
STAGE13_SUPPORT_FILES=ALLOWED_WHEN_SEPARABLE
STAGE13_EXTERNAL_REVIEW=ON_DEMAND
STAGE13_REVIEW_BUNDLE=GENERATED_ON_DEMAND
STAGE13_1_2_INITIAL_FILES=HISTORICAL_SOURCE_AFTER_MAIN_IMPORT
STAGE12_R09=FROZEN
```
