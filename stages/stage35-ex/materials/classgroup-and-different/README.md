# 類群・非分岐部分・不同・有限上界の資料 — 第3移植群

2026-11-09 JST。既存のrow385–393の9記録を保存する。研究はrow393で停止中。

**この移植は[PR #1854](https://github.com/fizawa460-bit/perfect-cuboid-game/pull/1854)だけで継続する。新しいPRは作らない。** 旧PR #1855・#1857は閉じ、内容と検証記録を同じPRに統合した。

**小因子基底のCl/2全尽生成、c_Cl、q★、真Sel4所属、無条件−30排除、全LOW、Branch Bは未解決。** 181は有限関係商の形式残余であり、真の類群階数・無条件上界ではない。

## 最終状態と監査限定

- row392は、親の最大整環基底を前提に、不同の主生成元δ=G′(ρ)/(ρ−1)^102と余不同を105次整数トレース行列のdet=1で認証した別の証書を持つ。全類群の決定ではない。
- row393の著者は有限105次での類代表上界B<2^94を提出した。**独立監査はPASS_SCOPED_DEPENDENT / SOURCE_THEOREM_VERIFICATION_PENDING。** 提出式の有限算術・厳密区間計算と、外部定理の原典における仮定・正規化の直接照合は別である。原典照合待ちを解除していない。
- 上界までの全素点処理、6768小基底の全尽2生成、c_Cl=0、q★の値、MW≤9を証明した資料として扱わない。
- row385の無条件H1(J[4])リフトは真Sel4所属を決めない。row386の三類は曲線点のKummer像の範囲であり、全Jacobianの三類分類ではない。簡便conic法の不適合はSel4非リフトを意味しない。
- row390–393の解析的障壁は、指定した有限資料・全帯一律非負性・未知項の追加正下界無しという方式に限定する。

## 記録と原資料

| row | 内容と限定 | 著者本文 | 独立監査報告 |
|---|---|---|---|
| 385 | H1(J[4])リフトと抽象q★への還元。q★・Sel4は未判定。 | [本文](proofs/row385.md) | [報告](audits/row385.txt) |
| 386 | 曲線点Kummerの三H_nr剰余類、256代表の簡便conic法の不適合。 | [本文](proofs/row386.md) | [報告](audits/row386.txt) |
| 387 | good集合の三H_nr剰余類とη第一引数CT経路。認証類群基底・CT値は未構成。 | [本文](proofs/row387.md) | [報告](audits/row387.txt) |
| 388 | 既存乗法閉包の飽和・H_nr交差零、形式332。全類群生成は未証。 | [本文](proofs/row388.md) | [報告](audits/row388.txt) |
| 389 | 新1047元・820独立関係、54半イデアル証人、形式332→264。 | [本文](proofs/row389.md) | [報告](audits/row389.txt) |
| 390 | 新676元・578関係、41証人、形式264→231、指定方式の障壁。 | [本文](proofs/row390.md) | [報告](audits/row390.txt) |
| 391 | 分数イデアル関係169元・139関係・12証人、形式231→222、全帯方式の障壁。 | [本文](proofs/row391.md) | [報告](audits/row391.txt) |
| 392 | 新594元・535関係・21証人、形式222→193、主不同・余不同の別証書。 | [本文](proofs/row392.md) | [報告](audits/row392.txt) |
| 393 | 新314元・268関係・12証人、形式193→181。B<2^94の定理原典照合待ち。 | [本文](proofs/row393.md) | [報告](audits/row393.txt) |

正確な元台帳の要約・監査表示・方法・障壁・当時のNEXTは[R3-SOURCE-RECORDS.json](R3-SOURCE-RECORDS.json)に保存する。当時のNEXTや原READMEのPENDINGは履歴であり、現在の研究実行指示ではない。[CLAIMS.json](CLAIMS.json)で今回の掲載範囲を固定する。

## 重複を除いた保存

9個の原証拠ZIPのSHA256と全529メンバー、本文・監査18件の対応は[SOURCE-INVENTORY.json](SOURCE-INVENTORY.json)。ZIPコンテナ自体の再作成は主張せず、全メンバーを元の名前・元のバイトへ復元する。

同一内容は一度だけ保存し、第2群と同じ入力も参照して共有する。大きい生成表は決定的gzipと元SHA256で保存する。元の発見記録・有限探索・停止理由も含め、探索を新しく実行することはない。

## 検証と復元

標準Pythonで保存整合性と監査限定を検査する。

```bash
python verify_migration.py
python -O verify_migration.py
```

全529メンバーを元のSHA256SUMSに照合し、指定した9記録のいずれかを新しいディレクトリへ復元できる。

```bash
python restore_package.py --row 393 --destination /tmp/stage35ex-row393-original
```

固定された既存証書の再演にはPython 3.12、python-flint 0.9.0、mpmath 1.3.0を使う。[17ジョブ](REPLAY-JOBS.json)を実行し、完了済みジョブは同一の凍結資料に対して再利用できる。

```bash
python -m pip install -r requirements.txt
python replay.py --output /tmp/stage35ex-materials03-replay.json
python replay.py --resume --output /tmp/stage35ex-materials03-replay.json
python replay.py --job 392-verify_different392 --output /tmp/stage35ex-different-replay.json
```

算術の元検証器にはassertとその副作用があるため、**算術は通常モードだけで実行する**。この再現器は-Oを明示拒否する。保存整合性検査の-O成功と混同しない。

数体原始算術の重いrebuildスクリプトは原資料として保存し、上の17ジョブとは別である。実行した範囲と未実行の範囲は[LOCAL-REPLAY.json](LOCAL-REPLAY.json)に記録する。再演は独立数学監査や新規採択を意味しない。

[全99管理ID](../../publication/CATALOGUE.md) · [第1群](../original-source-exclusions/README.md) · [第2群](../negative30-mw-selmer/README.md) · [移植進捗](../MIGRATION-STATUS.json)
