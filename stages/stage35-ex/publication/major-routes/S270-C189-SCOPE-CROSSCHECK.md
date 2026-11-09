# S270 → R2/C189｜真正四TOP定義と155/197採否の論理照合

2026-11-09 GitHub移植の出典・量化子レビュー。**文献の原証明の再監査や新定理ではない。** 参照先：
[S270原文](proofs/foundations/S270.md)、
[R2一様閾値原文](proofs/R2-uniform-thresholds.md)、
[MID/HIGH説明](02-mid-high.md)、
[R0 C189従属採否](https://docs.google.com/document/d/10MNKZS2aWJ6rZVi1YxgIliuX9kxIJAPlY3EWwhf5d48/edit)。

## 正確な対象

全許容の原始LABELLEDピタゴラス基底A²+B²=C²、実際のsigned元軌道D_n=T0+[2n]P、同じcommon denominator bとS269 Gaussian四次式と同じ正整数S243四根（common c）を持つ**complete source**に限る。S270はS243の根g1..g4を使い、各役割J/Kにつき2本の整数線形形：
L_J±=U4±U3、L_K±=U2±U1 を定義する。
整数根のU1..U4と、四つの「TOP積」U_{J+},U_{J−},U_{K+},U_{K−}は別記号であり同一視しない。

初期プールは各pの正確な指数β_p=v_p(b_m)を使い、GOODあるいは**実際のcritical H**のfull TOPのみを数える。GOODでは指数2mの実際のprimitive indexとcorrected T0 halfを使う。noncritical HをGOODへ移したり、T_eの旧定義を変えない。すべてのPROPER（non-topを含む）のordinary βをuncappedで保持する。旧の半点・次数・原始性HOLDと符号付きPOINT一致を落とさない。

## S270とC189の結果の関係

| 出典 | 位置づけ | 結論 | 転送禁止 |
|---|---|---|---|
| S270 §5–6 | 旧元source上のbase-dependent正確閾値N4/N1 | m>N4で四TOP積がそれぞれ>1、m>N1で各TOPの100乗≥b。追加のH-norm capからGOOD ladder | N4/N1を無条件に155/197と呼ばない |
| R2旧C185 | 共通の高さ/係数を持つ十分条件 | P4=(9/50)λm²−βm−K4>0、P1=(7/50)λm²−βm−K1>0で四TOPの下界 | 旧局所根や別のbetaへ切替不可 |
| R2新一様原証明 | C174/C175から全原始基底で使えるλ*を介した下側評価 | Q4(155)>0、Q1(197)>0、各二次式は以後単調増加 | 一部基底だけの有限実験から外挿不可 |
| R0 C189（採否正本） | ACCEPT_DEPENDENT_UNIFORM_THRESHOLD_EXTENSION、同系列補遺ACCEPT_DEPENDENT_SAME_SERIES | 全complete sourceでm≥155なら四TOP全部>1、m≥197なら各U_i^100>b_m。同系列補遺でjoint protected ≥75%/全体、各role protected ≥50%/自身 | 新しい独立一般方法や敵対的監査、上側証明としない |

式の係数や正確な厳密端点は[02-mid-high.md](02-mid-high.md)で与えたQ4(154)<0<Q4(155)、Q1(196)<0<Q1(197)に一致する。ただしS270固有のN4/N1とR2一様閾値の論理導出は異なるため、「S270のN4=155」といった置換はしない。

## OPENと残余

LOW even 12..154（72絶対）、MID even156..196（21絶対）、HIGH even≥198、許容signed odd n≡1(mod32)で|n|≥7199を現行index-bandsとして記録する。これらは「物理解の実在数」ではない。m≥155の四pool>1という**下界**から、物理的矛盾に必要な「必ず一つのTOPが空」等の**上界**は得られない。m≥197の1%確保もjoint 75%未満の上側を示さない。TRUE四GOOD/actual critical-H TOP、全PROPER ordinary βとactual point/rolesの結合上界は未証明。Branch B OPEN、元の完全直方体問題は未解決。

この文書は条件・量化子・採否の参照を照合したもので、S270/C189の全数学的計算・親高さ証明を再実行していない。成立条件の全面的な敵対的監査は別作業。

[移植完了要件](MIGRATION-COMPLETION-CHECKLIST.md)
