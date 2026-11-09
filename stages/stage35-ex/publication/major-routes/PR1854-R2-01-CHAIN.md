# R2-01：MID/HIGHへ至る数学的証明鎖（PR #1854）

> **旧数学親の入口:** [E3物理source・MW・Section13/16と依存範囲](PR1854-EARLIEST-MATH-FOUNDATIONS.md)。S121のgeneric-image枝はS232–270のrank-independent主鎖すべての数学的必須親ではない。

> **現行の粗い鎖は [**2ルートの端から端までの粗い証明鎖（今回の最新全体図）**](PR1854-ENDTOEND-CHAIN.md) を優先**。以下には段階的整理の履歴も残る。今回追加した著者原証明11本と、以前から収載された原証明の所在を合わせたもので、個々の数学的必須性・外部定理適用は未監査。

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

- **C160**：[R0原著の§3 strong-gcd本文を収載](proofs/active-ancestors/C160.md)。C185が使うexact protected係数とその完全な数学的適用の同一性はなお要監査。
- **S230**：[A/C素点付値を実際に再導出した元著者本文](proofs/active-ancestors/S230.md)を収載。これはS232のrank-independent部分が利用する数学的入力であり、敵対的独立監査PASSの主張ではない。
- **S242**：[固定(8,15,17) rank2例の原著](proofs/active-ancestors/S242.md)を**参考枝として収載**。全基底四根主定理の必須親には自動昇格させない。
- **S250**：S251に再述された次数8結論との同値性を検証。重複の原著を自動アップしない。
- **S252の外部Bérczes定理**：Theorem 2.1(i)の全仮定・記号・本件代入を一次文献と照合。論文全文の転載は必要としない。
- **Section16のa非平方補題**：S194で参照される正確な命題を特定し、現在の2証明鎖で必要な部分だけ対応付ける。

**現状：中核本文は収載、数学親の完結性はPENDING。計算証拠は後日。** 外部定理の適用監査と数学的独立監査を、本文アップ済みという事実に混ぜない。[二ルートの入口](PR1854-START-HERE.md)。

## 第2回整理で追加した、既存の旧原著への導線

- [C174の旧高さ入力](proofs/C195-upstream/C174.md)、[R1-228の四乗標準形](proofs/C195-upstream/R1-228.md)。
- [S232のA/C素点付値引用](proofs/active-ancestors/S232.md#L61)：実際にS230局所補題を使う箇所。S230の[元数学本文](proofs/active-ancestors/S230.md)は今回収載した。
- [S194の有限奇数位数／無限類の区別](proofs/active-ancestors/S194.md)：古いSection16非平方補題の出典・現行主鎖への必要性が未確定。

この**4本文はGitHub既存**で、数学の新規アップはしていない。[39件の原著引用辺と未判定ゲート](PR1854-PROOF-EDGE-AUDIT.md)を優先。未証明のR2相関上界を証明済みに変更しない。

## 旧々祖先までの粗い到達図

[C189](proofs/active-ancestors/C189.md)←[155/197原著](proofs/R2-uniform-thresholds.md)←C175/C185/S318←[S270](proofs/foundations/S270.md)←S258～267/S251/S252/S243/S232←[S230](proofs/active-ancestors/S230.md)およびS121～126の古い数学本文。C160は[原著](proofs/active-ancestors/C160.md)、固定例S242は[参考枝](proofs/active-ancestors/S242.md)。あくまで利用関係の概観であり、全ての矢印が厳密な直接論理依存ではない。Bérczes等外部原典とSection16の旧出典は未照合。[全体図](PR1854-ENDTOEND-CHAIN.md)。
