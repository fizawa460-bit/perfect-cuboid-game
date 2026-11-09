# C195 → C196–C200｜actual signed 元sourceへの依存チェーンの限定レビュー

2026-11-09 GitHub収載文書間の成立条件・失効NEXTを突合した。**正確な量化子・論理適用先のレビューであり、5稿の数体/楕円曲線計算の独立監査ではない。** 研究自体はrow393で停止、Branch B OPEN、指数排除の追加0。

## 全段を通じて必須の前提

正の原始LABELLED A²+B²=C²（C odd）、E:y²=x(x−A²)(x+C²)、P=(D,BD)、T0=(0,0)、D=AC、実際のsigned D_n=T0+[2n]P、strict −B²<x(D_n)<0かつy(D_n)<0が固定される。actual nで **GLOBAL sigma-square** を仮定して初めて[C195](proofs/C195-canonical-source.md)のcanonical F,G,M,N、同じ負yのPOINT等が自動再構成される。sourceのない補助曲線上の有理点や任意のGaussian分解では適用不可。残存|n|≥12の下でS289/C174/S290から四GLOBAL整数根/common cと同じQの無限商を継承する。index帯および全TRUE S270四GOOD/critical-H TOP・PROPER ordinary βとHOLDは継続する。

## 段階別の結果と直後の修正

| 時点 | GitHub原証明 | 追加された限定結論 | 解決していない点・旧NEXTの修正 |
|---|---|---|---|
| C196 | [次数8対応](proofs/post-C195/C196.md) | C2、Γ2二種数2曲線のJacobian間にdegree8対応 Φ=g_*f^*。元actual sourceに適用するチャートを明示 | 曲線同型・rank equalityのみで2-Selmer/local Kummerを転送できない。Gの任意有理点から元sourceを作れない |
| C197 | [cyclic8核・降下](proofs/post-C195/C197.md) | Φの有理cyclic8 kernel、faithful ε8、actual sourceに対してeven n→[1]、odd n→[16]（Q*/Q*8） | この[1]/[16]だけからodd sourceを排除できない。2進の障害とglobal membership差の証拠が必要としたNEXTは後のC198により訂正 |
| C198 | [boundary/Prym・dual4](proofs/post-C195/C198.md) | 境界上の有理divisorが[16]を実際にglobal imageで実現し、[1]も自明。actual sourceから一意のPrym点R_nとdual4前像S_nへの関係 | C197の「この二値のglobal-image非所属で落とす」だけのgateは**不成立（DOMINATED）**。境界点はstrict physical sourceではなく、sourceの実在証明ではない |
| C199 | [一様高さ比較](proofs/post-C195/C199.md) | same actual signed-indexからR_n/S_nのcanonical heightの下界・一様誤差を接続 | 外部からsource高さの**上界**を与える命題は未証。新しいtail指数上限・質量上界は得ていない |
| C200 | [明示dual4 source-cover](proofs/post-C195/C200.md) | 同じS_nの座標に対して次数16の平方receiver、quotients、r/s/p/qへの正確な復元式を提示 | 逆方向には必ず**同じ基底と実際のsigned POINT完全一致**を確認する。x・height・n parityだけの一致では不可。新規のMW/Selmer上限・点の完全列挙・無条件指数排除0 |

## 連鎖の構造と二重計上の防止

C197のε8が見つけた二つのclassのうちodd側[16]はC198により**大域像に存在**するので、C197の裸のmembership filterを独立savingとして復活できない。C199のlower boundはC200のsource-coverにより上側の矛盾が証明された訳ではない。C200のdegree16-square receiverは、C195の元軌道sigma-squareと独立な新条件ではなく、同じsourceを表す従属チャートである。C200はC198のtorsion ambiguityを同じactual indexで解決するための符号・torsion補正を記録し、任意のE1(Q)からsourceと呼ぶ推論を拒絶する。

この5原著は互いの親入力を参照しており、C195以降の原文を保存する必要は満たす。一方、計算の実行ログ・原始多項式証書の全バイト照合や、親最大整環/楕円因子・高さの独立数学監査を今ここで実施した訳ではない。成立条件と失効NEXTの資料間照合は今回実施したが、数理完全性の敵対的監査はPENDING。

[元Ward入口](01-canonical-source.md) · [移植完了要件](MIGRATION-COMPLETION-CHECKLIST.md) · [主要ルート](README.md)
