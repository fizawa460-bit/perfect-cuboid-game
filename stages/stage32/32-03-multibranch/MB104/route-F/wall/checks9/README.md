# checks9 — 壁打ち 8（定理 U を混合型へ）の計算

答えの本文は `ANSWER-08.md` です。ここにはスクリプトと出力だけを置きます。credit 0。

リポジトリのルートから実行します（numpy、mpmath）。最後の行が `PASS` なら成功です。

| スクリプト | 確かめること | 時間 | 出力 |
|---|---|---|---|
| `borel9.py [NMAX [DEPTH]]` | 補題 I（Iwahori）：距離ごとの奇素数の表、有限体での全数確認、Γ₀ の対合を mod 𝔭 に落とした確認、隣接する対合のラベル | 約 1〜2 秒 | `borel9.out`（既定）、`borel9_d11.out`（`50 11`） |
| `census9.py` | 型の数え上げ。問題の範囲（混合型で \|Ω\| ≤ 4）について完全な探索。次数 (1,1)、(1,2)、(2,2)、(2,3)、(3,3)、(3,4) | 約 3.5 分 | `census9_default.out` |
| `census9.py --bideg 4,4` | 同じく次数 (4,4) | 約 32 分 | `census9_44.out` |
| `census9.py --bideg 2,2 --first 8 --anylabel --keep 2` | 依頼 7（near.py）の次数 2 の数の再現 | 約 1 分 | `census9_cross22.out` |
| `dcover9.py` | 命題 C の族の欠陥、二重被覆での欠陥の分離、合成の補題、(t², t² + t³) | 約 45 秒 | `dcover9.out` |

例:

    python3 -I stages/stage32/32-03-multibranch/MB104/route-F/wall/checks9/borel9.py

- `census9.py` は `../../f02/maps3.json`、`maps4.json` を読みます（別の場所なら `--f02 DIR`）。
- `borel9.py` の Part C は `route-E/e13/traces.py`、`filt.py` を読みます（なければ飛ばします）。
- `dcover9.py` は同じフォルダの `census9.py` を読み込みます。
