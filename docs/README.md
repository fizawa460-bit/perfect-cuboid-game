# Documentation

Stage16-29 の研究プログラムは **CLOSED** です。完全直方体問題そのものは **OPEN** のままです。

`docs/` の現役入口は意図的に少数に絞っています。

## 最優先の実行規約

GitHub Actions・大量並列・長時間計算・大量artifactを伴う作業を始める前に、root [`../AGENTS.md`](../AGENTS.md) の **CRITICAL repo-wide rule: bounded Actions storage before compute** と [`research-os/policies/actions-storage-and-evidence-safety.md`](research-os/policies/actions-storage-and-evidence-safety.md) を先に読んでください。

計算時間や並列数だけでなく、**peak artifact storage を事前見積りし、安全容量を超える可能性があるbatchは投げない**ことがrepo全体の最優先運用ルールです。raw exhaustive evidenceは原則runner内で検証し、永続化はcompact deterministic certificateを優先します。

### GitHub Actions の絶対運用上限

- **Actions artifact/storage の運用予算は 500 MB を hard ceiling として扱う。** 明示的にrepo policyを改訂しない限り、余裕があると仮定して超過方向へ設計してはならない。
- **重いActionsを作成・改修するとき、1つのStageが同時に使用し得る heavy compute job は合計18並列以下とする。絶対遵守。** workflowを複数に分けても同一Stageの協調実行なら合算する。
- 複数のmatrix/jobが同時実行可能なら、それぞれの `max-parallel` を別々に見るのではなく、**同時に走り得るheavy jobの合計が18以下**になるよう設計する。例: `10 + 10 = 20` は禁止。
- **18は目標値ではなく上限値。** 他Stageの調査・監査・軽量Actionsが使えるrunner余力を常に残すこと。Stage-localな速度向上、早期完走、空き枠の有効利用を理由にこの上限を破ってはならない。
- 新しいheavy workflowをlaunchする前に、artifact peakと同時に **planned effective concurrency <= 18** をpreflightで確認する。
- **`pull_request.paths` だけでheavy再実行を許可してはならない。** `synchronize` では `github.event.before` からcurrent headまでの実際のcommit差分に専用run-keyの変更があることをcheap gateで確認し、generation/revisionが進んでarmedである場合だけheavy jobを許可する。
- audit/controller/docs/status/README/sourceだけの更新ではheavyを再実行しない。`reopened` もcold startとし、再開後に明示的なrun-key更新を別commitで入れるまでheavy jobはskipする。
- 既存heavy workflowは、**次回armする前に**このcommit-range authorization gateへ移行する。現時点でrepo全体がmechanically enforced済みとは扱わない。

この並列上限・storage上限・heavy再発火防止は同じrepo-wide mandatory ruleであり、Stage固有の都合では上書きできません。

## まず読む

- [`stage16-29-overview.md`](stage16-29-overview.md) — Stage16-29で何を行い、何が閉じ、何が残ったかの最終俯瞰。人間・初見AIの第一入口。
- [`frontier/13-active-kernels.md`](frontier/13-active-kernels.md) — Stage29-close後に残った13 kernelを、分類②/③・exact wall・既知入力・再開条件つきで一覧化。
- [`frontier/11-route-to-13-kernel-map.md`](frontier/11-route-to-13-kernel-map.md) — 歴史的11 routeと現在の13 kernelの対応関係。
- [`frontier/dormant-16-vault.md`](frontier/dormant-16-vault.md) — Class-4 dormant 16件の再起動条件つき保管庫。
- [`arsenal/README.md`](arsenal/README.md) — 再利用可能な定理・構成・adapter・探索武器の入口。
- [`arsenal/deep-source-index.md`](arsenal/deep-source-index.md) — Stage14巨大Arsenal/Toolbox/数値ログ、StructureRadar、Stage20-28 promotionを「何を探したいか」から辿る深掘り索引。
- [`research-os/README.md`](research-os/README.md) — 問題固有でない研究運用ルールの入口。
- [`archive/README.md`](archive/README.md) — 旧CURRENT、roadmap、reentry、運用メモなどの履歴。

## 入口の役割

```text
何をやった／何が分かった？ -> stage16-29-overview.md
今なにが残っている？       -> frontier/
使える武器は？               -> arsenal/
巨大な旧武器庫を掘る？       -> arsenal/deep-source-index.md
どう研究を再開する？         -> research-os/
昔の経緯を追う？             -> archive/
```

## 大きな武器庫

次の2ディレクトリは既存参照を壊さないため場所を維持しています。

- [`stage14-toolbox/`](stage14-toolbox/) — Stage14由来の theorem / formula / receiver toolbox。
- [`structure-radar/`](structure-radar/) — 外部文献・StructureRadar・weapon classification の蓄積。

これらは現役の参照武器庫ですが、内部の古い `CURRENT` / controller / progress 表示を現在状態として読まないでください。入口には [`arsenal/deep-source-index.md`](arsenal/deep-source-index.md) を使います。

## 数学的な一次資料

証明・監査・計算の一次資料は `stages/` 側に残します。特にStage29の最終状態は:

- [`../stages/stage29/29-17/result.md`](../stages/stage29/29-17/result.md)
- [`../stages/stage29/29-17/final-handoff.json`](../stages/stage29/29-17/final-handoff.json)
- [`../stages/stage29/29-17/audit.md`](../stages/stage29/29-17/audit.md)

です。

## Authority rule

`archive/` 内のファイルが `CURRENT`, `NEXT`, `OPEN`, `PENDING` などを名乗っていても、それは作成当時の履歴です。StructureRadar/Stage14の巨大参照群についても、ローカルな古い状態ラベルは現在のStage29-close後の状態を上書きしません。

現在地は `stage16-29-overview.md`、再開対象は `frontier/` とStage29 final handoff、再利用武器は `arsenal/` を優先してください。
