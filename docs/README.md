# Documentation

Stage16-29 の研究プログラムは **CLOSED** です。完全直方体問題そのものは **OPEN** のままです。

`docs/` の現役入口は意図的に少数に絞っています。

## まず読む

- [`stage16-29-overview.md`](stage16-29-overview.md) — Stage16-29で何を行い、何が閉じ、何が残ったかの最終俯瞰。人間・初見AIの第一入口。
- [`frontier/13-active-kernels.md`](frontier/13-active-kernels.md) — Stage29-close後に残った13 kernelを、分類②/③・exact wall・既知入力・再開条件つきで一覧化。
- [`frontier/11-route-to-13-kernel-map.md`](frontier/11-route-to-13-kernel-map.md) — 歴史的11 routeと現在の13 kernelの対応関係。
- [`frontier/dormant-16-vault.md`](frontier/dormant-16-vault.md) — Class-4 dormant 16件の再起動条件つき保管庫。
- [`arsenal/README.md`](arsenal/README.md) — 再利用可能な定理・構成・adapter・探索武器の入口。
- [`research-os/README.md`](research-os/README.md) — 問題固有でない研究運用ルールの入口。
- [`archive/README.md`](archive/README.md) — 旧CURRENT、roadmap、reentry、運用メモなどの履歴。

## 入口の役割

```text
何をやった／何が分かった？ -> stage16-29-overview.md
今なにが残っている？       -> frontier/
使える武器は？               -> arsenal/
どう研究を再開する？         -> research-os/
昔の経緯を追う？             -> archive/
```

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

現在地は `stage16-29-overview.md`、再開対象は `frontier/` とStage29 final handoff、再利用武器は `arsenal/` を優先してください。
