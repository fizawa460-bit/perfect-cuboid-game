# R2-01：MID/HIGHへ至る数学的証明鎖（PR #1854）

**第2対象：P23-MID/HIGH、R3 row393と同じ研究停止時点。** [R2-01運用記録](../routes/R2-01.md)の到達点と、それを導く実質的な数学親だけを移植する。R1/R4/R5の全研究史を第三の対象にしない。

## 実際に到達している数学

- [155/197の全基底下界の原著](proofs/R2-uniform-thresholds.md)と、後日の[C189従属採択・撤回判定](proofs/active-ancestors/C189.md)。旧C187当時PENDINGと後日の採択を混同しない。
- [S270のTRUE四つGOOD/actual-critical-H TOP＋ALL PROPER ordinary β](proofs/foundations/S270.md)を常に同じ元signed source上で扱う。C189は必要な**下界**であり、R2-01が目標とするjoint strict 75%未満の**上界はまだ存在しない**。したがってMID/HIGHの全体排除は未証明。
- [現行の範囲](02-mid-high.md)、[S270/C189使用条件の照合](S270-C189-SCOPE-CROSSCHECK.md)。

## 現在GitHubにある中核と、使用する可能性がある数学親

- [155/197下界の元原著](proofs/R2-uniform-thresholds.md)
- [C189の従属採択と補遺](proofs/active-ancestors/C189.md)
- [C175高さ係数のR0採用](proofs/active-ancestors/C175.md)
- [C185 protected TOP係数](proofs/active-ancestors/C185.md)
- [S270 TRUE四TOPとALL PROPER](proofs/foundations/S270.md)
- [S275](proofs/active-ancestors/S275.md)
- [S318](proofs/active-ancestors/S318.md)
- [S243](proofs/active-ancestors/S243.md)
- [S251](proofs/active-ancestors/S251.md)
- [S252](proofs/active-ancestors/S252.md)
- [S258](proofs/active-ancestors/S258.md)
- [S267](proofs/active-ancestors/S267.md)

上記12本は独立必須12定理という意味ではない。複数の旧証明が後続に取り込まれたり、例・障壁にしか使われないことがある。**各結果→本当に使う補題→GitHubの完全証明**で判定する。

## R3との共通元source：同じ本文を再利用

- [C195 genuine original source](proofs/C195-canonical-source.md)
- [S268](proofs/C195-upstream/S268.md)
- [S269](proofs/C195-upstream/S269.md)
- [S233](proofs/C195-upstream/S233.md)
- [S237](proofs/C195-upstream/S237.md)
- [S240](proofs/C195-upstream/S240.md)
- [S289](proofs/C195-upstream/S289.md)
- [S290](proofs/C195-upstream/S290.md)
- [R1-223](proofs/C195-upstream/R1-223.md)

C195/S268/S269・同じPOINTとGaussian canonical rolesをR2とR3で二重アップロードしない。旧finite-odd条件の dQ=mP を無限位数の元sourceに無条件転用しない。

## 未判定の親証明・原典

- **C160**：C185のfirst-entry/gcd補題の正確な式。S268+C185に既に完全な証明が含まれるなら旧原著の複製は不要。
- **S230**：S232で利用されるA/C素点の局所付値補題。『監査文書』という題名だけで数学的な親から除外しない。
- **S242**：S243の(8,15,17)固定例には引用がある。全基底四根主定理の成立に必要か切り分ける。
- **S250**：S251に再述された次数8結論との同値性を検証。重複の原著を自動アップしない。
- **S252の外部Bérczes定理**：Theorem 2.1(i)の全仮定・記号・本件代入を一次文献と照合。論文全文の転載は必要としない。
- **Section16のa非平方補題**：S194で参照される正確な命題を特定し、現在の2証明鎖で必要な部分だけ対応付ける。

**現状：中核本文は収載、数学親の完結性はPENDING。計算証拠は後日。** 外部定理の適用監査と数学的独立監査を、本文アップ済みという事実に混ぜない。[二ルートの入口](PR1854-START-HERE.md)。
