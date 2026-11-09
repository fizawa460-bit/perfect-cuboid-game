# PR #1860｜Branch B 原分岐・S194奇数商・S232無限商の数学原著再帰監査

**2026-11-09｜R3-07/R2-01のためだけの祖先監査｜IN_PROGRESS｜DO_NOT_MERGE。** このファイルは、最古の大容量原著から、**どの章が真に数学的な親か**を特定する。Stage35/Branch Bを新たに証明するものでも、R2/R3以外の全ルートを再調査するものでもない。

## 1. 第１周未発見だった独立の数学証明節を追加

最古[Drive原本](https://docs.google.com/document/d/1CKLon3eRKjsEVuIwgpSTV4DKHQ5GRWsfDw2SA6T5vNI/edit)の「**15. Hostile-audit repair: specialized torsion growth is uniformly absent**」の§15.1–15.5（抽出原原著行1286–1446）に、次の数学的連鎖がある。

- **§15.2**：`E'_t:y²=x(x²−2b²x+(1+a²)²)` の二次因子の判別式が `−16a²`、唯一の非零有理2-torsionと有理4-torsion `Q4=(1+a²,2a(1+a²))` を持つ。Mazurの分類により可能な有理torsionは `Z/4,Z/8,Z/12`。
- **§15.3**：`Z/8` は双対2-isogenyで`E_t`の有理4-torsionを強制する。しかしフル2-torsionの半分割条件と「1はcongruent numberでない」古典的Fermat定理により除外。
- **§15.4**：`Z/12` は`E_t(Q)[3]≠0`を強制。`ψ3=3x⁴+4(1−a²)x³−6a²x²−a⁴`を`α=a²`の二次式として見た判別式は`16x³(x+1)³`。有理3torsionから`w²=z⁴+z²+1`を得て、参照された古典的Mordell四次式 `u⁴+u²v²+v⁴=W²` の非自明解不存在を使って除外。
- **§15.5**：`E'_t(Q)_tors=Z/4Z` for **all rational `t>1`** が結論。これは「§15.6の自由群飽和index-two-only」という別の撤回済み主張とは**独立**。

[**今回の追加原著：BranchB-Section15-torsion.md**](proofs/earliest-foundations/BranchB-Section15-torsion.md)は§15.1–15.5の著者数学本文を原本から正確に切り出して保存したもの。§15.6は取り込まない。[§16の残る`a(t)`非平方補題と§17撤回](proofs/earliest-foundations/BranchB-Section16.md)はすでに別ファイルで保存。したがって**同じDrive原本の既収載§13/§16を別の新発見Driveファイルと偽って二重計上しない**。

**なぜ数学的な直接親か**：既収載[S194 §3](proofs/active-ancestors/S194.md)は`E'_t(Q)_tors=Z/4Z`を明記して、`E_t(Q)_tors=E_t[2]`、`E_t(Q)/(E_t[2]+ZP)`の有限非自明位数の奇数性、`dQ=mP+T`での`gcd(d,m)=1`に利用する。S194はこの一様torsion**を引用していて、8/12除外の元証明本文自体は再記述しない**。また[S121](proofs/active-ancestors/S121.md)にも一様torsionが親として出る。第１周の§13/§16とS194の所在が既知でもこの§15.2–15.5の原証明が自動的に揃ったことにはならなかった。

[**機械可読な原著抽出区間・依存命題・暫定監査判定**](PR1860-BRANCHB-PARTITION-AND-TORSION-PARENT-CHECK.json)を同梱した。

**古典四次式の出典照合**：最古Branch Aの[別原稿 §3/§9](https://docs.google.com/document/d/1smWIX2pkMdKEou0soUVj9_o9opg-z_JPRT4MwxSROHE/edit)も調査し、そこで `L. J. Mordell, Diophantine Equations, Chapter 4, Equation 7′` と出典指定していることを確認。ただしその原稿も**古典定理の証明自体は載せていない**。したがって§15.4のMordell引用の一次原典照合は`OPEN`。重複する古いBranch A原著を１本増やして「自己完結」とはしない。

**独立監査境界**：`ψ3`のα判別式`16x³(x+1)³`は独立記号計算で再確認。ただしMazur分類、Fermat「1は非congruent」、Mordell四次式の古典定理の原典・仮定・独立証明は今回未監査。§15全証明の数学的PASSを付与しない。

## 2. 最古Section14.5 → 15.5 → 17 → 19 と後続S193/194を原文比較

| 旧原著の章 | 数学的に使える命題 | 既存GitHubでの必要本文 | 今回の判定 |
|---|---|---|---|
| §14.5 | 物理 reciprocal `S=φ(Q)` は`φ_t(E_t(Q))`に入る。**specialized generic subgroup**に入るとは限らない | [S193](proofs/active-ancestors/S193.md)、[S194 §1](proofs/active-ancestors/S194.md) | isogeny像とgeneric-imageを区別し利用 |
| §15.1–15.5 | 全有理特殊化で`E'_t(Q)_tors=Z/4Z`。8・12-torsion除外の実数学親 | **[今回追加§15原証明](proofs/earliest-foundations/BranchB-Section15-torsion.md)** | **FIRST_ROUND_MISSING_MATH_SECTION_RECOVERED** |
| §15.6 | source P3の全特殊化primitivityを仮定したindex-two saturation排除 | [Section16/17](proofs/earliest-foundations/BranchB-Section16.md) | **§17が撤回、現行数学親には使わない** |
| §16 | `a(t)=(t²−1)/(t²+1)`が有理平方でない古典的Fermat降下 | [Section16/17](proofs/earliest-foundations/BranchB-Section16.md)、[S194](proofs/active-ancestors/S194.md) | **非平方補題だけ保持**、全飽和昇格禁止 |
| §17 | 三分岐`GENERIC_IMAGE_MULTIPLE`、`FREE_ISOGENY_SATURATION_GROWTH`、`RANK_GROWTH`を残す | [Section16/17](proofs/earliest-foundations/BranchB-Section16.md) | 旧2分岐の断定を使わない |
| §19.1–19.3 | `Q−Qsharp=Qn, Q+Qsharp=Qtau, 2Q=nR+Ptau`、`Ptau`のsubgroup/saturation/rank-growth三分岐 | [S194 §§0–4](proofs/active-ancestors/S194.md)、[S231](proofs/active-ancestors/S231.md)に同じ物理点・群法則と必要な商群証明 | **自足的再導出が既存なので元§19全章の大量コピー不要** |
| §13 | 元物理D quotient/2-isogeny座標 | [既収載§13](proofs/earliest-foundations/BranchB-Section13.md)、[S193](proofs/active-ancestors/S193.md) | 既存で一致、重複収載しない |

## 3. R3-07 と R2-01 の正確な条件付き対象：全物理点をindexedと誤認しない

[最古物理座標→同じラベルへの橋](PR1860-E3-LABEL-INDEXED-BRIDGE-AUDIT.md)は`35EX-21`の正の４平方から`Q−Qsharp=(-r²,-rpq)`を与える。しかし**その点が`Qn=T0+2nP`に属すること**までは無条件に導かない。これがouter Branch Aとinner Branch Bを分ける**元sourceの定義**。

**Inner indexed Branch Bに既に所属するという仮定の下で**、[S194 §§1–3](proofs/active-ancestors/S194.md)は
```
M=E_t(Q), K=E_t[2]+ZP, I=φ(M), H=φ(K);
I/H ≅ M/K.
Q−Qsharp=Qn=T0+nR, 2Q=nR+Ptau.
[Ptau]=2[Q] in M/K.
```
を示す。さらに**`K`は2-saturated**（S194 §2：`a(t)`非平方、Eに4-torsionなし）なので`M/K`には2-torsionがなく、同じ物理点の商位数`d=ord([Q])`に応じて以下が成立する。

1. `d=1`：**generic-image multiple**の元の二重部分群交叉、[S193](proofs/active-ancestors/S193.md)が**この限定分岐を排除**。S193の結論は外側の全物理点がindexedであるという定理ではない。
2. `1<d<∞`：S194により**奇数`d≥3`**。`dQ=mP+T, T∈E[2]`と`dPtau=kR,k=m−dn`を要するfinite-odd/saturation分岐。[S232](proofs/active-ancestors/S232.md)には**user-accepted research-routing PASS**とあるが、外部査読・Stage35全体の閉鎖認定ではない。この「Route2 finite-odd」は**R2-01というレーンの名称と別**。
3. `d=∞`：`[Q]`は無限位数で`P,Q`独立、特殊化ランク≥2。ただしランク≥2の曲線の全物理点が無限類になるわけではない。[S232 §B](proofs/active-ancestors/S232.md)がこの条件を実際の元sourceで明記。R2-01の[C187のSOURCE LOCK](proofs/R2-uniform-thresholds.md)は「**SAME Q/Qsharp infinite quotient**」を前提にした**条件付き155/197下界**。R3-07の固定指数受信も「元のlabelled`D_n`が存在するなら」の必要方向であり、全Stage35物理点への逆向き一般化を認めない。

したがって「すべてのE3 selected物理点を特定のindexed軌道へ送り込む定理が証明されていない」ことは、**R2/C187・R3の明記された条件付き対象の自己完結に必須の空白原著ではない**。これは**Stage35全体を結論するには別途必要な外側・分岐網羅の問題**。この２つのレベルを二度と混同しない。

## 4. 最古原著§1–12の「古いから必要」誤判定を防ぐ精密切分け

同じ[巨大Drive原著](https://docs.google.com/document/d/1CKLon3eRKjsEVuIwgpSTV4DKHQ5GRWsfDw2SA6T5vNI/edit)の**元行23〜644**を新たに直接確認した。第１周の§13/§16の前に存在することと、現行R2/R3の**使用する数学親**であることを別々に判定する。

| 旧原著の数学箇所 | 実際に記載された結論 | 現行２ルートの近接原著と判定 |
|---|---|---|
| §1 行23–77 | `A²+B²=C²` の任意labelled積分E/P/R、`C1=B,C2=2ABC`（B偶の旧表示） | [S231](proofs/active-ancestors/S231.md)、[S240](proofs/C195-upstream/S240.md)、[S263](../../materials/original-source-exclusions/parents/S263.md)にE/Pと元sourceの必要式が**明記済み**。旧§1だけを別必須証明として複製しない |
| §2 行78–169 | `p|A,C,B,H`のbad-support局所付値 | S263の全odd+2 formal valuationと[S258](proofs/active-ancestors/S258.md)、[S268](proofs/C195-upstream/S268.md)の実際の`b_m`とH first-entryが後で個別に証明される。旧root denominator `C_k`と新しい`b_m`を**無条件に同一視しない** |
| §§3–4 行170–269 | 旧`C_{n−1}^{odd}C_{n+1}^{odd}`平方および奇素数の強整除・parity別旧基底 | [S263 §3, §5–7](../../materials/original-source-exclusions/parents/S263.md)の真のsigned Ward平方・例外twist固定に置換済み。C160のSG.1/SG.2も正確な2-adic階層とnodal Hを扱う。旧`C_k`式を新`W_j`に証明なしに流用せず、**現在のC187/row367の直接必須親とは認定しない** |
| §5 行270–314 | primitive Pythagorean parameter と基底の正規化 | [R1-255/256](proofs/R3-18-upstream/R1-255-fourward-cover-original.md)、[C195](proofs/C195-canonical-source.md)が同じ原始三つ組を明記しsource forwardの必要式を証明。古い標準パラメータ形式の元原稿を重複しない |
| §6–9 行315–406 | 外部標準定理、研究上の残障壁と当時のNEXT | 新たに採用された数学結論ではない。§6の外部定理の出典・仮定は親が現在も必要な時だけ監査する |
| §10 行407–537 | p=2におけるB偶/B奇２モデルの局所計算と`C_{n−1}C_{n+1}`平方 | 現行主張は[後のS263](../../materials/original-source-exclusions/parents/S263.md)の元`W_j`とδ_nについて別の全素数付値証明を使用。旧C_k計算がなくてもその必要条件は証明されると原著に明記。**旧全`C_k`定理を新`W_j`定理と等号で結ばない** |
| §11 行538–605 | 完全基底`B`、`2ABC`、`4ABC`を使った旧根分母`C_{n±1}`の平方形 | 同じ要約だけではS263/C160の全符号・H込みの数学が足りないが、**それらの新原著はGitHubに既収載**。旧§11の数式が後のR2 C185/R3 row370に直接必要だとは確認されないため一括追加しない |
| §12 行606–643 | 保存・研究routing | 当時のNEXTであり現行主要２ルートの数学親ではない |

**判定**：旧§1–12は全面数学監査PASSではない。しかし、今回実際に使う`E,P`、元の`σ_n`→signed Ward平方、`b_m` first entry、primitive sourceについては後の原著に直接証明本文があるため、**古い節１つにつき１本ずつ機械的に追加する必要は確認されない**。一方、旧§15.2–15.5のE'一様torsionは後続S194の引用だけで実排除証明が無かったので今回追加した。この差を保持する。

## 5. 今回のファイル所在・数学監査の状態

| 対象 | 状態 |
|---|---|
| 新しい数学原著Driveファイル | **0**。最古Drive原著を再読した |
| 第１周の23件の外にあった新しい数学本文**箇所** | **1：§15.1–15.5**。新規GitHub本文ファイル1本 |
| これまで第１周23候補から収載した著者本文ファイル | 12（変わらず） |
| 第１周23件外の**別個のDrive文書**から回収した原著本文 | 10（変わらず） |
| #1860で追加した数学本文ファイルの累計 | **23**（12+10+1）。ファイル≠独立定理数・独立原本数 |
| 原証明の独立数学監査 | **未了**。§15のMazur・Fermat・Mordell四次式は外部古典入力として明示 |
| 全必要親の再帰的数学十分性 | **NOT_CLOSED**。不足数・全親数未確定 |
| 原Stage35の全物理点がinner indexed Branch Bに属するか | **主張しない**。outer Branch A・finite-odd・infinite分岐を分離する |

**次の必要な検査**：S194 §2の「2-saturation」の証明に現れる古典Fermat入力と§15の8/12torsion証明が正しく適用されているか、R2の旧S268/C160とC187が実際に同じconditional domainを受けるか、R3 row367の±18内部排除からrow393までの数体・外部定理の仮定。原計算ZIPと独立数学監査を本人確認なしにPASSへ昇格しない。**PR #1860 Draft / DO_NOT_MERGE。**
