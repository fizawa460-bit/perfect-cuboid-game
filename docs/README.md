# Documentation

Stage16-29 の研究プログラムは **CLOSED** です。完全直方体問題そのものは **OPEN** のままです。

`docs/` の現役入口は意図的に少数に絞っています。

## まず読む

- [`stage16-29-overview.md`](stage16-29-overview.md) — Stage16-29で何を行い、何が閉じ、何が残ったかの最終俯瞰。人間・初見AIの第一入口。
- [`arsenal/README.md`](arsenal/README.md) — 再利用可能な定理・構成・adapter・探索武器の入口。
- [`research-os/README.md`](research-os/README.md) — 問題固有でない研究運用ルールの入口。
- [`archive/README.md`](archive/README.md) — 旧CURRENT、roadmap、reentry、運用メモなどの履歴。

## 大きな武器庫

次の2ディレクトリは既存参照を壊さないため場所を維持しています。

- [`stage14-toolbox/`](stage14-toolbox/) — Stage14由来の theorem / formula / receiver toolbox。
- [`structure-radar/`](structure-radar/) — 外部文献・StructureRadar・weapon classification の蓄積。

これらは現役の武器庫です。過去の進行状況を表すものではありません。

## 数学的な一次資料

証明・監査・計算の一次資料は `stages/` 側に残します。特にStage29の最終状態は:

- [`../stages/stage29/29-17/result.md`](../stages/stage29/29-17/result.md)
- [`../stages/stage29/29-17/final-handoff.json`](../stages/stage29/29-17/final-handoff.json)
- [`../stages/stage29/29-17/audit.md`](../stages/stage29/29-17/audit.md)

です。

## Authority rule

`archive/` 内のファイルが `CURRENT`, `NEXT`, `OPEN`, `PENDING` などを名乗っていても、それは作成当時の履歴です。現在状態の判定には使用しません。

現在地は `stage16-29-overview.md`、再開点はStage29 final handoff、再利用武器は `arsenal/` を優先してください。
