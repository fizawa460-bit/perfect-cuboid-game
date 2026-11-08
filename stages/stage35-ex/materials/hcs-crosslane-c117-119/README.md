# C117–C119 HCSとR1/R4の関連資料 — 第5移植群

2026-11-09 JST。研究はrow393で停止中。[PR #1854](https://github.com/fizawa460-bit/perfect-cuboid-game/pull/1854)へだけ追記し、新しいPRは作らない。

C118が参照する固定HCS曲線の親資料を補完し、同時期のR1・R4の議論も保存する。**当時の内部・暫定研究の範囲を保持し、新しい独立敵対的監査PASSや正式採択にはしない。** 無条件−30・全LOW・Branch BはOPEN。row393定理原典の照合待ちも維持する。

## 何を保存したか

| 材料 | 本文・原データ | 再演コードと限定 |
|---|---|---|
| HCSのrank1に関する独立有限算術チェーン | [原証明](sources/R3_rank1_proof.txt)、[当時のREADME](sources/R3_rank1_readme.txt)、[期待JSON](expected/r3_rank1.json) | [コード](code/r3_rank1.py)。標準2-descent・S-unit完全性・局所から大域への定理と、歴史的な暫定研究の採用範囲を保持。 |
| p=3の対数差 | [原証明](sources/R3_p3_proof.txt)、[元44D入力](inputs/prior44D.json) | [コード](code/r3_p3_logdiff.py)。単独でrank1を証明するものではない。 |
| 固定genus3 HCSの四円盤 | [原証明](sources/R3_all4_proof.txt)、[期待JSON](expected/r3_all4.json) | [コード](code/r3_all4.py)。継承された暫定rank1とColeman/Strassmann論証を用いる固定曲線の結果。全物理母集団の決定ではない。 |
| R1の全奇指数・第3の2-isogeny指標 | [原カード](sources/R1_third_isogeny_card.txt)、[期待JSON](expected/r1_odd_gate.json) | [元パケットから抽出したコード](code/r1_odd_gate.py)。同じ完全な元physical packetへの必要条件。全奇指数の一括排除や逆向きの十分条件ではない。 |
| R4のB-even Eplus Tamagawa | [原証明](sources/R4_tamagawa_proof.txt)、[原README](sources/R4_tamagawa_readme.txt) | [コード](code/r4_tamagawa.py)。有限回帰と、一様な成分群の紙面論証を区別する。 |
| R4のrank>=2を仮定するoffcycle族 | [原カード](sources/R4_offcycle_card.txt)、[期待JSON](expected/r4_offcycle.json) | [元パケットから抽出したコード](code/r4_offcycle.py)。Uの独立性を仮定し、点は元のindexed軌道やphysical packetとして構成されていない。有限局所の平方を大域の第4平方と同一視しない。 |

## 原資料と変換

24件のnative Google Docsをtext/plainで保存し、[SOURCE-INVENTORY.json](SOURCE-INVENTORY.json)で現在の原URL・更新日時・全バイト・SHA256を対応させる。C118の原統合パケットは第1群の保存済み本文とバイト一致し、共有参照する。大きいC117/C119パケットはgzipで原バイトを保持する。

Google Docs書出しと当時の元ZIPのバイトは区別する。コード6本はBOM除去・CRLF→LFと、明示したNATIVE SOURCE区間の切出しだけで得る。JSONは型・値を保持して整形する。変換は検証器が原書出しから再構成して全件照合する。コードのアルゴリズムは編集しない。

44Dの親JSONは、元の二つのチェックサム文書と元検証器が要求するSHA256 `d84545a9f0a002f218e525978d75203a31fd455bbbbb9645eb0f40168ccfc0a7` と一致する4595バイトを復元できた。元の全ZIPを取得・復元したという主張ではない。

C118中の旧C117 CURRENTリンクは、現在は別タイトルのSECTION334を指す。[SOURCE-LINK-NOTE.json](SOURCE-LINK-NOTE.json)で記録し、凍結されたC117祖先と混同せず、専用の歴史的証明文書を使う。共有controllerや正式状態は編集していない。

当時の提出前表示、後続の内部統合COMPLETE、外部hostile audit=falseはそれぞれ履歴として保持する。古いNEXTは現在の研究指示ではない。全99管理IDの本文移植、全上流写像・被覆、全親鎖の独立監査を完了したとは表示しない。

## 再演

```bash
python verify_migration.py
python -O verify_migration.py
python -m pip install -r requirements.txt
python replay.py --output /tmp/stage35ex-materials05-replay.json
python replay.py --resume --output /tmp/stage35ex-materials05-replay.json
```

六つの歴史的計算を独立した一時フォルダで再演し、5件は宣言されたJSONと完全一致を要求する。Tamagawaの回帰は元のassertと範囲フィールドを検査する。元コードはassertを使うため、算術を-Oで成功扱いにせず、再現器は-Oを明示拒否する。[REPLAY-JOBS.json](REPLAY-JOBS.json)、[CLAIMS.json](CLAIMS.json)、[LOCAL-REPLAY.json](LOCAL-REPLAY.json)で実施範囲を確認できる。

[全99管理ID](../../publication/CATALOGUE.md) · [資料全体](../README.md) · [移植進捗](../MIGRATION-STATUS.json)
