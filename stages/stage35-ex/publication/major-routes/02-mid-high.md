# 2. MID/HIGH — 真正四TOPの下界と、未証明の相関上界

所有ルート：[R2-01](../routes/R2-01.md)、横断[R5-K05](../routes/R5-K05.md)・[K06](../routes/R5-K06.md)。[155/197原著証明](proofs/R2-uniform-thresholds.md)と、後日の[C189採否本文](proofs/active-ancestors/C189.md)を合わせて読む。原著のC187時点PENDINGは、C189のACCEPT_DEPENDENT_UNIFORM_THRESHOLD_EXTENSIONより前の履歴である。

## 対象と下界の意味

同じ原始標識付き基底、同じsigned元Ward軌道、S269の同じ整数Gaussian・quartic・POINT、S243のglobal整数根を持つcomplete sourceを対象とする。m=|n|。U_iはS270の四つのTRUE protected GOOD/actual-critical-H TOP積であり、全PROPERとnoncritical Hをordinary βのまま保持する。GOODだけへの切替、βの上限打切り、四枝の独立性は仮定しない。

旧prime-cut表示は、mの奇素因子ℓについて L_m=lcm b_(m/ℓ) とし、各canonical枝z_iに対して

$$
U_i=\frac{z_i}{\gcd(z_i,mL_mT_e)}
$$

と与える。T_eは旧S268/C185で定めた同じdyadic因子を使い、別のcutoffへ置き換えない。完全な定義と親条件は原著・Drive参照に残す。

## 155/197への全基底一様化の証明

旧C185の二つの十分条件は

$$
P_4(m)=\tfrac9{50}\lambda m^2-\beta m-K_4>0\Rightarrow(\forall i)\ U_i>1,
$$
$$
P_1(m)=\tfrac7{50}\lambda m^2-\beta m-K_1>0\Rightarrow(\forall i)\ U_i^{100}>b_m.
$$

ここでβ=1/2+c_E/18、c_E=bit_length(256D⁸H⁴)、H=A²+C²、
Z4=ceil(16C⁷H_o¹⁶/(A³c²))、K4=bit_length(Z4)/8+c_E/24、
K1=bit_length(Z4)/8+13c_E/300。cはA偶なら1、A奇なら2、H_oはHのodd partである。

旧C174/C175の同じPのhybrid高さ下界λ*に対して、0<λ*≤ĥ(P)、c_E<12(25408/727)λ*を継承する。全原始基底でA≥3、C≥5なのでc_E≥60。L=log₂C<(c_E−8)/16とH_o<2C²からbit_length(Z4)<22+39L。従って

$$
K_4<\tfrac{133}{384}c_E+\tfrac5{16},\quad
K_1<\tfrac{3341}{9600}c_E+\tfrac5{16},
$$

さらにβ/λ*<292192/10905、K4/λ*<107190/727、
K1/λ*<2692454/18175を得る。従って十分条件を支配する二次式は

$$
Q_4(m)=\tfrac9{50}m^2-\tfrac{292192}{10905}m-\tfrac{107190}{727},
$$
$$
Q_1(m)=\tfrac7{50}m^2-\tfrac{292192}{10905}m-\tfrac{2692454}{18175}.
$$

正確な有理数評価はQ4(154)=−266408/54525、Q4(155)=104425/4362、
Q1(196)=−1176986/54525、Q1(197)=724039/109050。各二次式は正側の端点以後で単調増加する。これで全許容基底のcomplete sourceに対し、m≥155で四枝すべてU_i>1、m≥197で四枝すべてU_i¹⁰⁰>b_mが従う。有限の基底サンプルからの外挿ではない。

C189は同系列の補遺も従属採択し、m≥155でjoint protected質量が全体の75%以上、各roleのprotected質量がそれぞれのM/Nの50%以上となる下界を保存した。

## 現行の指数帯と未証明の方向

| 帯 | 偶数絶対指数 | 必要下界 | 足りない独立命題 |
|---|---|---|---|
| LOW | 12…154 | 下界だけでは一括排除しない | R3の同じsourceの排除 |
| MID | 156…196 | 四つすべてU_i>1 | 全sourceに少なくとも一枝U_i=1を強制、または同じsourceのglobal排除 |
| HIGH | 198以上 | 四つすべてU_i¹⁰⁰>b_m | 同じsourceに一枝の反対向き上界を強制、またはglobal排除 |

許容signed oddの無限域も残る。表は偶数指数帯の定義であり、物理解の個数ではない。旧LOW/MIDの550/1045、さらに古い閾値やmask数は現行帯へ流用しない。

下界を強くしても、TRUE四GOOD/H TOP＋全PROPER ordinary βの厳密な相関上界は得られない。joint 75%未満の上界、MIDの一枝欠損、HIGHの1%未満の枝は未証明で、Branch BはOPEN。

## 監査と保存

C189のR0採否は内部の従属採択として記録する。155/197の有限Fraction計算の再現と、継承された全基底高さ証明の独立再監査は区別する。今回の公開は新しい数学監査を付与しない。深い高さ証書・原ログはDrive参照に留める。

[主要ルート入口](README.md) · [C189原文](https://docs.google.com/document/d/10MNKZS2aWJ6rZVi1YxgIliuX9kxIJAPlY3EWwhf5d48/edit)

## S270原文（追補）

[四つのTRUE TOPと全PROPER ordinary βの原著S270](proofs/foundations/S270.md)を保存。原稿とC189の定義・採択範囲は[資料間照合済み](S270-C189-SCOPE-CROSSCHECK.md)。ただし、親高さ証明の独立数学再監査は保留。

[補助監査：S270のTRUE四TOPとC189採択155/197の対応](S270-C189-SCOPE-CROSSCHECK.md)。S270のbase-dependent N4/N1を155/197へ同一視しない。すべて**下界**であり、相関**上界**とBranch B排除は未証。

[R2のQ4(154/155), Q1(196/197)の有理端点の独立再計算結果](MAJOR-PARENT-MATH-PAPER-CHECK.md)。主張全体の独立監査ではない。

[今回GitHub化したS232/S243/S251–262/S265–267とC175/C185/C189の直接親補題・採否の図](ACTIVE-ANCESTOR-DEPENDENCY-MAP.md)。[C175](proofs/active-ancestors/C175.md)は旧高さ係数のR0統合、[C185](proofs/active-ancestors/C185.md)はdependent protected係数、[C189](proofs/active-ancestors/C189.md)は155/197の従属採否。TRUE TOPとPROPER ordinary βの共通original sourceの数理親証明は依存継続、相関上界は未証。
