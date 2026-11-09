# PR #1860｜R3-07 の「実際に使う命題」遡及監査：±18・Ward3/5/7・物理sourceの向き

**2026-11-09／IN_PROGRESS／DO_NOT_MERGE。** この文書はR3-07だけ。本文の実在・式の適用範囲を直接照合した結果であり、算術ZIPの再演・独立敵対数学監査・最古物理forwardの全面検証ではない。元の−30のrow370〜393は[別監査](PR1860-R3-MINUS30-PARENT-CHECK.md)を参照。

## 1. ±18の原著使用鎖を命題で区別

| 実際の数学的主張 | 使っている原著本文（GitHub） | 範囲と判定 |
|---|---|---|
| 元のsigned ±18で必要なWard17/19の**４正整数平方**と163∣A | [既存R1-239原文](../../materials/selmer18-parent-chain/objects/91c82ae590d162c6-R1_239_SOURCE_ADAPTER.txt)、[S263](../../materials/original-source-exclusions/parents/S263.md) | **LOAD_BEARING**：必要方向、物理source存在の逆命題ではない |
| 同じ元原始三つ組の４因子を種数17・22の商と `X=(AC/B²)²` に送る | [R1-255](proofs/R3-18-upstream/R1-255-fourward-cover-original.md)、[R1-256](proofs/R3-18-upstream/R1-256-signed18-fourward-quotient-original.md)、[row339](../../materials/original-source-exclusions/parents/row339-PROOF.md) | **LOAD_BEARING**：R1-256は正の有理`z`から元の`u/v`への逆像条件を明記。自由な補助曲線点を全物理sourceへ同一視しない |
| 既知有理除数のKummer下界・`h₂=A_{poly}²-XB_{poly}²` 恒等式 | [row340](proofs/R3-18-upstream/row340.md)、[row341](proofs/R3-18-upstream/row341.md)、[row342](proofs/R3-18-upstream/row342.md) | **LOAD_BEARING**：row342の６類・rank≥6は前２行の恒等式と類を実際に継承 |
| 次数36数体のS有限素点21とS単数の階数40 | [row343](proofs/R3-18-upstream/row343.md)、[row344](proofs/R3-18-upstream/row344.md)、[row346](proofs/R3-18-upstream/row346.md) | **LOAD_BEARING**：row350・351が`34+c_S` fake ambientをそのまま使用。row346原著は既に#1860に追加済み |
| 12独立整数単数・７つの主S素点付値方向・指数13拡大 | [row347](proofs/R3-18-upstream/row347.md)、[row348](proofs/R3-18-upstream/row348.md)、[row349](proofs/R3-18-upstream/row349.md) | **LOAD_BEARING**：row350はこれらの実際の単数・付値入力を継承。３原著とも#1860に収載済み |
| 実局所の３独立制約、true→fake核１次元 | [row350](proofs/R3-18-upstream/row350.md)、[row351](proofs/R3-18-upstream/row351.md)、[row352既存](../../materials/selmer18-parent-chain/objects/5fd888550f0b7d57-PROOF_C2_INFINITY_RANK7_AND_TRUE_FAKE_KERNEL_JA.md) | **LOAD_BEARING**：fake候補と真正Selmerを同一視しない。row352は有理無限遠差で核を実現 |
| 真の局所Kummer像：５奇悪素点・２進 | [row353](proofs/R3-18-upstream/row353.md)、[row355](proofs/R3-18-upstream/row355.md) | **LOAD_BEARING**：row364が両方の実在局所生成元とglobal座標を使う |
| 全球４局所制約→全有限偶付値還元→新３単数 | [row356](proofs/R3-18-upstream/row356.md)、[row358](proofs/R3-18-upstream/row358.md)、[row359](proofs/R3-18-upstream/row359.md) | **LOAD_BEARING**：row358は完全な有限局所像を単数代表へ還元、row359はその同じ局所条件に新３単数を当てる |
| 類数1、全19整数単数平方類、残余候補２方向 | [row363](../../materials/selmer18-parent-chain/proofs/row363.md) | **LOAD_BEARING**：3,204個の明示主素点、通常Hilbert類体明示公式、20×20平方指標のodd determinantを利用。数学・外部定理の全検算PASSを新規宣言しない |
| 真正2-Selmer次元9と、その２進障害に使う大域・局所母体 | [row364](../../materials/original-source-exclusions/parents/row364/STAGE35EX_R3_07_EXACT_SELMER9_CT_REDUCTION_20261105.md) | **LOAD_BEARING**：row363の類数・全平方類、row353/355局所生成、row351/352 true/fake核を使用 |
| 大域2冪可除性、局所torsion、４分点→16分点の障害 | [row365](../../materials/original-source-exclusions/parents/row365/REPORT.md)、[row366](../../materials/original-source-exclusions/row367/parent_evidence/ROW366_PROOF.md)、[row367](../../materials/original-source-exclusions/row367/REPORT.md) | **FINAL_SCOPED_PROOF**：固定±18に限る内部証明。row367の独立数学監査は原記載どおり保留 |

**途中結果を最終排除の必須親と混同しない：** [row357](proofs/R3-18-upstream/row357.md)のh_S≤13は、後段のrow358/363で類群上界が強化される前の数値段階（数値主張・監査履歴には継承関係がある）。[row360](proofs/R3-18-upstream/row360.md)の163進円盤**高々14**は[ row363 ](../../materials/selmer18-parent-chain/proofs/row363.md)§6で個数を高々９へ改良する際に使用されるが、row367の**別方式の2進障害**にその数値個数命題を仮定する必要は確認されない。[row361/362](../../materials/selmer18-parent-chain/proofs/row361.md)の163進既知７類・飽和も163進代替路線の成果であり、row367の２進排除へ無断で必須条件としない。この分類は番号の時系列でなく命題の使用先に基づく。

**row354**は既存格子`Γ1`に対する`ζ6,ζ6′`の従属性と誤ったrank14計上の撤回を扱う[Drive訂正ZIP](https://drive.google.com/file/d/1m7Z0PKSNdkPR7Qt37STDSOpU3esgL7nc/view)。後段の独立単数・rankを増やす親としては扱わない。誤ったrank主張の復活も禁止。

## 2. row368のWard3/5降下で使う数学親

[実際のrow368原著](../../materials/original-source-exclusions/row368/STAGE35EX_R3_07_ROW368_LOW_WARD3_WARD5_TRANSFER_20261105.md)§1–3は、**同じ**元の`(A,B,C)`から`D=AC,V=B⁴,z=V/D²`を作り、[S263](../../materials/original-source-exclusions/parents/S263.md)の隣接Ward平方条件、[S321](proofs/active-ancestors/S321.md)のW5分解と結果式、[C118統合原著](../../materials/original-source-exclusions/parents/C35-118/export.txt)にある固定`\mathcal X(\mathbf Q)=\{(0,\pm1,\pm1)\}`を使う。原sourceから受信点への`x=D/B²>0`は本文中に明記され、**別の三つ組から平方を勝手に取っていない**。合同式による例外素数23の処理と残表の一致は原著内にあり、検算ZIP・完全監査は別途未実施。

## 3. row369のWard7降下とC35-12の内容照合

[実際のrow369原著](../../materials/original-source-exclusions/row369/STAGE35EX_R3_07_ROW369_LOW_WARD7_TRANSFER_20261106.md)§2–3は、S263/S264、[S321](proofs/active-ancestors/S321.md)のW7分解と[S322](proofs/active-ancestors/S322.md)の`H1=K L`、さらに[既存C35-12原数学証明](../../materials/original-source-exclusions/parents/C35-12/PROOF.md)の`C3'(\mathbf Q)=\{\infty,(0,0)\}`を使用する。ここで`u=(A/B)²>0`、`(x,y)=(-u,(A/B)k/B⁶)`なので`x<0`。これは**元の同じprimitive base**からの一方向の必要写像で、自由な補助曲線点の逆方向を必要としない。C35-12のrank1入力は[既存C35-11](../../materials/original-source-exclusions/parents/C35-11/PROOF.md)。

**C35-08を新たな未収載「必須数学原著」として重複計上しない理由：** 別の[Drive C35-08著者原稿](https://docs.google.com/document/d/1m6OYk1ldDpAXUZM299UdL2Oxw51GunQGna2nvKP1_DY/edit)は実在し、当時`GLOBAL_C3_RATIONAL_POINTS...HOLD`と記載する。一方、後の**[C35-12のGitHub数学原著](../../materials/original-source-exclusions/parents/C35-12/PROOF.md)**には４残余円盤の位相・局所Coleman積分の基点、誤差・無限尾、mod243の共通零点不存在、`C3'(\mathbf Q)`分類が**詳細に再導出**されている。C35-08の元検証器もGitHub [Coleman保存群](../../materials/original-source-exclusions/parents/C35-11-12/coleman/README.txt)にある。したがってこの**固定曲線の点分類命題**に対する原数学本文は既収載C35-12で足りるという**本文レベルの重複判定**であり、原計算の独立再演がPASSしたという意味ではない。

## 4. 最古の元物理source：A偶・B奇の有理パラメータ接続は解決（2026-11-09訂正）

前回「E3はB偶チャートなので±18のA偶B奇と不一致、A/B標識を交換する橋が必要」と記したのは、**E3のtを整数と誤解したため**。実際には[S193 §§Outcome/Direct source](proofs/active-ancestors/S193.md)は**rational t>1**を用いる。

任意の正のlabelled primitive三つ組に`τ=(C+A)/B>1`, `λ=B²/[2(C+A)]`を適用すれば、`(A,B,C)=λ(τ²−1,2τ,τ²+1)`、`a=A/C,b=B/C`。R1-239の生き残る`A=2uv,B=u²−v²,C=u²+v²`,`t_R1=u/v`には`τ=(t_R1+1)/(t_R1−1)`が対応し、`z=(B²/AC)²=(b²/a)²`、row339の`X=1/z`まで一致する。**label swapは行わない**。

正規化`E₀:y²=x(x−a²)(x+1)`から`(x,y)↦(C²x,C³y)`は同型で、`P3=(a,ab)↦P=(AC,ABC)`、`T0↦T0`、全signed `T0+2nP3↦T0+2nP`を保存。S193はselected physical `Qphys=(-r₀²,+r₀p₀q₀)`を負に取り`Qn=(-r²,−rpq)`へ移すが、これは整数指数の符号を`j→−j`とするだけ。さらにS231の`Q=(ρ,(r+s)ρ),Qsharp=(-ρ,(s−r)ρ),ρ=rs+pq`から弦の傾き`s`を使い`Q−Qsharp=(-r²,-rpq)`を直接再導出できる。

**厳密な式・算術チェック・原著所在：** [E3 label/indexed bridge独立監査](PR1860-E3-LABEL-INDEXED-BRIDGE-AUDIT.md)。`LABELLED_ORIENTATION=RESOLVED`、`EXACT_CURVE_AND_POINT_SCALING=RESOLVED`。さらに[35EX-21](../../35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md)の正の完全直方体`S_PC`では、辺`(1,x,y)`から`A=1,B=z,C=w,r=x,s=y,p0=p,q0=q`を取れば**selected E3の４平方を満たす**。[35EX-31](../../35ex-31/primitive-source-marking-endpoint-equivalence.md)はこの正の有理点からprimitive source markingをスケール／置換を法に再構成する。**positive cuboid→selected物理点の座標的橋は確認済み**。ただし**selected physical４平方だけで**`Qn∈T0+2\mathbf ZP`とはいえない。S193第一枝等の元の**部分群条件**と、物理点全体→inner indexed BranchBの**分岐網羅**は引き続きOPEN。

[S231](proofs/active-ancestors/S231.md)と[S263](../../materials/original-source-exclusions/parents/S263.md)、[S268](proofs/C195-upstream/S268.md)、[C195](proofs/C195-canonical-source.md)には一般の正の**labelled** baseと実際のindexed点を前提にした数学がある。これは元source**必要条件の内部計算**を支えるが、**すべてのselected物理点が同一のprimitive labelled indexed軌道に属する**という命題は今回証明していない。正の完全直方体→selected physicalの座標的対応は上記で確認したが、残りは`GLOBAL_PHYSICAL_TO_INDEXED_SUBGROUP_COVERAGE_OPEN`として固定する。

[Section16＋Section17訂正](proofs/earliest-foundations/BranchB-Section16.md)・[S194](proofs/active-ancestors/S194.md)の使用可能部分は`a(t)`非平方と、それに依存する2-saturation・有限奇数商の必要条件。Section17が撤回した**全specializationの同階数飽和二分法は復活させない**。

## 5. 未完了

- 各既存原著の証明の正しさ（classfield explicit formula、局所H¹/true-fake、2進RR・Coleman等）の独立監査は別のゲート。
- R3の第１周12候補（row344/346–349/353/355–360）は**実際にPR #1860の差分に存在**する。新たな９件を追加したと二重計上しない。
- 数学原著の必要十分な再帰閉包はまだ証明していない。**本PRはDraftのまま。** 無条件−30、全LOW、Branch Bの閉鎖やrow393以降の研究進展を主張しない。
