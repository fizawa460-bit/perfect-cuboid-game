# PR #1860｜Gate D：外部一次文献２件の限定照合（2026-11-09）

**対象はR3-07／R2-01だけ。Gate A/B/C/EはPASS、Gate Dは２件OPEN、PRはDraft・未マージ。** これまで第２周の終了条件を変えていない。「引用している著者数学原稿がある」と「外部の原定理が実際に適用可能」は別のチェック。

## 1. 今回、どこを探したか

- 接続済みGoogle Driveの文書タイトル・テキスト検索：`de la Maza`、題名 `Bounds for the smallest norm in an ideal class`、DOI末尾`01373-4`、`Mordell Diophantine Equations`、`Mordell.pdf`、`Diophantine Equations.pdf`、四次式の文字列。**該当する引用を載せたStage35EX著者原稿はあるが、両外部原典の本文ファイルを特定できなかった**。
- 同じGitHubリポジトリの`de la Maza`、`Mordell`、題名／四次式検索：移植済み元原稿・過去監査の引用はある。**出版社の原論文・Mordellの本の当該ページを収録したものとは同定できなかった**。
- プロジェクト・Libraryファイル検索では両外部原典のファイルは返らなかった。**検索結果ゼロは不存在の証明ではない**。この回の接続範囲で直接取得できた一次本文がなかったという限定判定。

一般Webからの全文取得ができたとは記録しない。一次原文を読めていない事実を明確に保存する。

## D-1：row393で使うde la Maza Theorem 1 + corollary

**著者が示した原論文**：Ana-Cecilia de la Maza, *Bounds for the smallest norm in an ideal class*, *Mathematics of Computation* 71(240) (2002), 1745–1758、Theorem 1と直後の系、DOI `10.1090/S0025-5718-01-01373-4`。[著者の示したAMS PDFリンク](https://www.ams.org/mcom/2002-71-240/S0025-5718-01-01373-4/S0025-5718-01-01373-4.pdf)（**原PDFは未取得・未読**）。

- [row393の数学原著](../../materials/classgroup-and-different/proofs/row393.md)には、数体署名`(7,49)`・次数105、`R(s)=(s+α)/((s+β)(s+λ)^2)`、`α=13/1000,β=77/1000,γ=107/500,λ=83/250`、`F(y)≤0`、`B<2^94`の計算がある。
- [前回までの定数・数値独立確認](ROW393-PRIMARY-THEOREM-GATE.md)では、`0<α<β<γ<λ`、有理関数分解、`|T(-γ+it)|=1`、提示公式を**仮定した場合**の`y0,t0,B`の数値整合を確認した。
- 今回のDrive・GitHub一次原文探索は不成功。**原論文のadmissible (4)の全定義、Mellin変換の線方向／符号、`B=sqrt(|Δ|)/(t0 exp(y0))`の正規化、zero/GRH仮定、通常／狭義類の別を直接照合できない**。

**状態：`D1_PRIMARY_THEOREM_TEXT_NOT_FOUND__APPLICATION_HOLD`。** 数値式が一致しても無条件理論の引用元までPASSではない。row393の無条件−30排除も元から未証明。

## D-2：Branch B §15.4で使うMordell四次方程式

**著者が引用する典拠**：L. J. Mordell, *Diophantine Equations*, Chapter 4, Equation 7′。`x^4+x^2 y^2+y^4=z^2` の原始整数解が`xy=0`に限るという命題。[元Branch-A原稿](https://docs.google.com/document/d/1smWIX2pkMdKEou0soUVj9_o9opg-z_JPRT4MwxSROHE/edit)の447行に書誌・命題を**引用として**記載している。しかしMordellの本の**Chapter4原文ページは見つかっていない**。

[初回に欠けていて追加したBranch B §15](proofs/earliest-foundations/BranchB-Section15-torsion.md)の§15.4を、今回SymPy有理記号計算で**原文の式に直接照合**：

1. `ψ3(x)=3x^4+4(1−α)x^3−6αx²−α²`をαの二次式と見た判別式は**`16x³(x+1)³`**。特異そうに見える例外`x=0`では`ψ3=−α²`、`x=−1`では`ψ3=−(α+1)²`。元の`α=a²>0`では両方とも3-torsion座標でない。
2. `x=r²/(1−r²)`と原著の二式 `α_+=−r³(r+2)/((r−1)(r+1)³)`, `α_−=−r³(r−2)/((r−1)³(r+1))`をそれぞれ代入すると、**`ψ3=0`の分子は恒等的に０**。両式の平方因子の取り出しも一致。
3. αが有理平方であれば、`z²=−r(r+2)/(r²−1)`または`z²=−r(r−2)/(r²−1)`。各`r`の二次方程式の判別式は同じ**`4(z⁴+z²+1)`**。元原著のMordell四次式へ正確に帰着する。
4. `z=m/n`（既約、有理、n≠0）に対し`w²=z⁴+z²+1`なら`(n²w)²=m⁴+m²n²+n⁴∈Z`。**有理数の平方が整数なら自身は整数**なので`W=n²w∈Z`。仮にMordellの「原始整数で`mn=0`」が真なら`m=0`、`z=0`。そのときプラス枝は`r=0,-2`、マイナス枝は`r=0,2`。`r=0`は上記x=0で不可、`r=±2`は`α=0`で不可。**原定理を仮定すれば§15.4の適用論理に欠けた特殊ケースはない**。

ここまでの代数部分は `D2_SYMBOLIC_APPLICATION_PASS`。しかし**「非自明な整数解がない」古典定理自体の証明・一次本の該当命題を検証したわけではない**ので、`D2_MORDELL_PRIMARY_THEOREM_TEXT_NOT_FOUND`は引き続きOPEN。数式を検証した事実から書籍を読んだことにしない。

## 残数・停止条件（変更なし）

| 事項 | 状態 |
|---|---|
| 著者数学本文23追加／元39辺の所在判定／固定７終端 | **A/B/C/E PASS（変更なし）** |
| D-1 原定理の原文とrow393への適用 | **OPEN 1** |
| D-2 原定理の原文と§15.4への適用 | **OPEN 1（代数帰着のみPASS）** |
| **第２周全体** | **NOT COMPLETE、残２外部原典** |

**今後必要なのは、上記２つの原典本文または当該ページの信頼できる複製への実際のアクセスと、列挙した成立条件の一対一照合**。これは固定Gate Dの残務であり、新数学定理・99ルート・独立ZIP再演を第２周に追加しない。原著PDF等がなくとも原定理の内容・仮定を創作してPASSにしない。PR #1860はDraft／未マージ。
