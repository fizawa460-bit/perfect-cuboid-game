# PR #1860｜最古E3 selected sourceからR2/R3 original labelled indexed軌道への厳密な座標・標識接続

**2026-11-09｜R3-07・R2-01限定｜原数学の直接照合／IN_PROGRESS／DO_NOT_MERGE。** R3の±18 original A-even/B-odd標識と最古E3の `A=t²−1,B=2t,C=t²+1` は、**E3のtが有理数**であるため矛盾しない。前回「整数パラメータの向きが不一致／A,Bを交換する橋が必要」という扱いは不正確。本ファイルはその点を算術恒等式として訂正し、他方、全Stage35物理解→indexed Branch Bの**大域網羅**の未検証は厳密に保持する。

## 1. Original Sources（現物）

- [最古E3物理source原著](proofs/earliest-foundations/E3-selected-physical-kummer.md)：「selected diagonal」「t>1」「A=t²−1, B=2t, C=t²+1」および３平方＋残り１平方の物理点定義。原稿は有理関数体および有理 `t>1` を扱う。
- [S193原著 §§Outcome/Direct source/Section13 D](proofs/active-ancestors/S193.md)：**every rational t>1**、`a=(t²−1)/(t²+1),b=2t/(t²+1)`、正規化EとP3、`Qphys=(-r²,+rpq)`、`Qn=-Qphys`、original `Sorig` とS192の同一点 ±、第一枝の**条件付き部分集合**。
- [S231 §0/§4](proofs/active-ancestors/S231.md)：`A²+B²=C²` の**任意のpositive labelled primitive**な積分モデルへの `r,s,p,q` のスケール、`Q,Qsharp` のsame-point relation、有限奇数商の場合だけの`dQ=mP`。
- [S240 §2](proofs/C195-upstream/S240.md)：元`E:y²=x(x−A²)(x+C²)` の`nP`倍算から`-x(D_n), A²−x(D_n), C²+x(D_n)`の３平方を直接導き、残り`σ_n=B²+x(D_n)`を別にする。
- [S263 §1](../../materials/original-source-exclusions/parents/S263.md)：同じ`A,B,C,E,P,R,T0,D_n`、`σ_n`と元の隣接Ward値の必要十分条件（`D_n`が**実際のindexed軌道である条件下**）。
- [R1-239 signed±18原著](../../materials/selmer18-parent-chain/objects/91c82ae590d162c6-R1_239_SOURCE_ADAPTER.txt)、[R1-256原著](proofs/R3-18-upstream/R1-256-signed18-fourward-quotient-original.md)、[row339](../../materials/original-source-exclusions/parents/row339-PROOF.md)：A-even/B-odd `u/v`、４Ward平方因子から`z`および種数17曲線へ**必要方向**。
- [C195原著](proofs/C195-canonical-source.md)：同じ**actual signed nP**で`σ_n`が平方なら元のcanonical Gaussian/整数role/POINTを再構成する（`|n|≥12`の別親条件あり）。自由な補助曲線点からphysical sourceが生じる逆方向ではない。

## 2. 全positive labelled primitive三つ組を有理E3パラメータで表示できる

任意の正数 `A,B,C` で `A²+B²=C²`、`C>A,B>0` とする。**標識を入れ替えず**、有理数
```
τ=(C+A)/B>1,
λ=B²/(2(C+A))>0
```
を定める。直接 `B²=C²−A²=(C−A)(C+A)` により
```
τ²−1=2A(C+A)/B²,
τ²+1=2C(C+A)/B²,
2τ=2(C+A)/B.
```
よって**完全な有理恒等式**
```
(A,B,C)=λ(τ²−1,2τ,τ²+1).
a=(τ²−1)/(τ²+1)=A/C,
b=2τ/(τ²+1)=B/C.
```
これは `A` 偶・`B` 奇も、`A` 奇・`B` 偶も含み、元の`A`と`B`を交換しない。最古原著の `A=τ²−1, B=2τ, C=τ²+1` は*正規化前の有理Pythagorean代表*として正しく、`τ`が整数である必要は**ない**。元の primitive integer base は `λ` による復元。

**±18原著R1-239/255/256固有のEuclidパラメータ**は、`A=2uv, B=u²−v²,C=u²+v²`、`u>v>0`、`gcd(u,v)=1`、逆parity。そちらの `t=u/v>1` に対してE3側は
```
τ=(C+A)/B=(u+v)/(u−v)=(t+1)/(t−1).
a=2uv/(u²+v²), b=(u²−v²)/(u²+v²).
```
したがって **R1のtとE3のτは同じパラメータでなくMöbius変換で接続**。R1のWard正規化も
```
h_R1(t)=B²/(AC)=(t²−1)²/[2t(t²+1)] = b²/a,
z=h_R1²=B⁴/(A²C²)=(b²/a)²,
X=1/z=(AC/B²)².
```
これらはR1-256 §2/3およびrow339の**同じ標識**、**同じ種数17受信X**であり、A/Bの符号付き役割を交換していない。

**整数の厳密チェック（恒等式の例、全域証明は上記代数）：**
```
(A,B,C)=(4,3,5):   t_R1=2,   τ=3,   λ=1/2;
(A,B,C)=(20,21,29): t_R1=5/2, τ=7/3, λ=9/2;
(A,B,C)=(3,4,5):   τ=2, λ=1.
```

## 3. 正規化E3の曲線・基準点・２torsion・signed indexを同一モデルへ移す

正規化原著の
```
E_0: y²=x(x−a²)(x+1),  P3=(a,ab), T0=(0,0),
```
に対し、正の `C` を用いて
```
ι_C:E_0(Q)→E(Q), (x,y)↦(C²x,C³y).
E: Y²=X(X−A²)(X+C²), P=(AC,ABC).
```
これは**Q上の群同型**で、`ι_C(P3)=P`、`ι_C(T0)=T0`、`ι_C(T0+[2n]P3)=T0+[2n]P` をすべての整数`n`で満たす。曲線係数は`a=A/C,b=B/C`を代入するだけで一致する。

E3の選択した物理根を`(r_0,s_0,p_0,q_0)`とすると、`(r,s,p,q)=C(r_0,s_0,p_0,q_0)`は
```
r²+s²=B², p²=A²+r², q²=C²−r².
```
原著の `Qphys=(-r_0²,+r_0 p_0 q_0)` は `ι_C` で `(-r²,+rpq)` へ。**曲線上の負号**を取ると
```
Qn=(-r²,−rpq).
```
S193が明示するように`Qphys=T0+[2j]P3`という**第一枝の仮定**がある時に限り`Qn=T0+[2n]P`、`n=−j`といえる。この符号変換は双方向で、有効な両signed indexを保持する。**どの物理点も何らかの整数jの枝に入る、と証明したのではない。**

## 4. SAME Q/Qsharp と実際のD_n：群法の直接恒等式

S231/S240にある元の４正平方から
```
ρ=rs+pq>0,    (pq)²−(rs)²=A²C²=D²,
B²=r²+s².
Q=(ρ,(r+s)ρ), Qsharp=(−ρ,(s−r)ρ).
```
`ρ(ρ−2rs)=D²` なので、代入して`Q,Qsharp∈E(Q)`（r,s,p,q有理なら）を得る。

`Q−Qsharp` を計算する際は`−Qsharp=(−ρ,(r−s)ρ)`。弦の傾きは
```
m=[(r−s)ρ−(r+s)ρ]/(−ρ−ρ)=s.
```
従ってEの`x³+B²x²−D²x`の加法公式から
```
x(Q−Qsharp)=m²−B²−ρ−(−ρ)=s²−B²=−r²,
y(Q−Qsharp)=−(r+s)ρ+m(ρ+r²)=−r(ρ−rs)=−rpq.
```
**Q−Qsharp=Qn=(-r²,−rpq)**が同じr,s,p,q、同じラベル・符号のもとで恒等的に従う。この計算に `dQ=mP` もspecialized rank=1も使わない。ただし**`Qn=T0+[2n]P`は、indexed original branchの追加の部分群条件**であり、物理４平方だけでは帰結しない。

## 5. 35EX-21／35EX-31の正の完全直方体座標からselected E3の４平方まで

**重複・新規性判定（重要）**：positive `S_PC`からE3のselected４平方への置換自体は、すでに[PR1854最古原著接続整理・Equation-level crosswalk](PR1854-EARLIEST-MATH-FOUNDATIONS.md)に書かれている**既知成果**。本回の差分は、E3のパラメータが有理数であることを使いR1-239の`A偶B奇`との**誤判定を解消**し、`τ=(t+1)/(t−1)`、元楕円`P,T0`のスケール、`Q−Qsharp`とsigned点の符号を同じ条件で再点検し、未解決ゲートを**indexed subgroupへの所属**に絞った点。既知置換を新定理として登録しない。


[35EX-21原著](../../35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md)§§1–2の**正の有理完全直方体面**`S_PC`では、辺`(1,x,y)`、面対角線`(p,q,z)`、立体対角線`w`は
```
p²=1+x², q²=1+y², z²=x²+y², w²=1+x²+y²;
x,y,p,q,z,w>0.
```
その**同じ物理点**に対し
```
A=1, B=z, C=w;   r=x, s=y, p0=p, q0=q
```
を選ぶと
```
A²+B²=C²,
p0²=A²+r²,
s²=B²−r²,
q0²=C²−r²,
r,s,p0,q0>0.
```
をすべて恒等的に満たす。したがって、[E3最古selected物理原著](proofs/earliest-foundations/E3-selected-physical-kummer.md)§1の**四つの平方条件へ全てのpositive rational cuboid点から一方向に送れる**（選んだ辺A=1、反対の面対角線B=z、空間対角線C=w）。逆向きも、この４平方点を辺`(A,r,s)`・面対角線`(p0,q0,B)`・空間対角線`C`と解釈することで成り立つ。物理根・符号・同じ点を保った純代数的な往復である。境界点や任意符号componentは含めない。

E3原著の`t>1`は有理数。例えば上記の`A=1,B=z,C=w`では`τ=(w+1)/z>1`を選び、§2の`λ`で戻す。`A,B,C`が有理三つ組なら、正の有理一括スケールで３つを整数にし、共通最大公約数で割って**同じ標識のpositive primitive integer base**を得る。同じ一括スケールを`r,s,p0,q0`にも適用するので、元の物理square packetを失わない。

[35EX-31原著](../../35ex-31/primitive-source-marking-endpoint-equivalence.md)§§5,7は、正の有理完全直方体で２進付値が最小の辺を選び、残りを`v₂(x),v₂(y)>0`とする正規化から、元の**primitive Euclid source**とMaster/E1受信条件を再構成する。この`source marking`と上記の`A=1`選択は、正のスケールと辺の置換を法とした**同一の物理点の異なるゲージ**であり、いずれもselected E3の４平方を正確に与える。

**解消した範囲**：`35EX-21 positive S_PC ↔ E3 selected positive four squares`および`35EX-31 primitive marking ↔ positive S_PC`の**物理座標・標識の橋**。ここでやったのは原著の式の直接組合せで、新たな完全直方体不存在や数学独立監査PASSではない。

**未解消で残る核心**：selected positive physical packetは`Qn=(-r²,-rpq)`という有理点を与えるが、一般には`Qn∈T0+2\mathbf Z P`を**主張しない**。最古selected physicalからS193のgeneric-image-multiple第一枝、S194の有限奇数障害、無限class／rank-growthをどう排他的・網羅的に分け、R2/R3が実際に扱うinner indexed BranchBがどの範囲を覆うかは別の命題。ここを閉じていないため、Stage35・Branch B全体はOPEN。

## 6. source→R3／R2との関係と厳密な未閉鎖境界

**解決済み（命題の成立範囲）**：
1. `positive labelled primitive A,B,C ↔ positive rational τ>1` の正規化。向きA-even/B-oddに問題なし。R1のtとのMöbius写像・`z,X`が一致。
2. 同じ正規化楕円曲線・P/T0・有理physical rootsの標識とsigned `n`の保存。S193`Qphys`を負にするj→−j、S231`Q−Qsharp=(-r²,−rpq)`の再導出。
3. 元のindexed仮定が確かにある場合、S240・S263の`σ_n`とR1-239/256・row339の必要的Ward平方/曲線受信へ矛盾なく進む。C195のS269-Gaussian復元は**actual nP とσ_n平方**という別の十分条件を要する。

**依然OPEN、勝手に解決しない**：
- 全正の有理完全直方体→35EX-21 S_PC→selected E3物理４平方の**座標的包含は§5で解決**。残るのは、全selected physicalから**特定のindexed inner BranchB**へどう分岐・受信するかの網羅性であり、これをsource全体の不存在証明に昇格しない。
- selected physical４平方点から**必ず**Branch Bの`Qn=T0+[2n]P`に属すると推論すること。S193の第一枝とS194有限奇商／無限独立枝の区別を保存。R2/R3が対象とするのは、元の**indexed inner Branch B**に入った対象の条件付き数学。
- S194の古いSection16からSection17で**撤回済み**の特殊化飽和性を復活させること、C195の元のindexed sourceとR3自由な補助曲線点を逆対応させること。
- row367真2-Selmer／局所障害の独立数学監査、row393外部定理の仮定、R2 C187の155/197 **LOWER**から相関４枝`strict<75%` **UPPER**を導くこと。

**本回の分類**：`LABELLED_CHART_BRIDGE_RESOLVED_ALGEBRAICALLY`、`EXACT_ELLIPTIC_P_TORSION_AND_ORBIT_SCALING_RESOLVED`、`Q_QSHARP_SAME_SOURCE_IDENTITY_REDERIVED`、`GLOBAL_POSITIVE_CUBOID_TO_SELECTED_PHYSICAL_COORDINATES_RESOLVED`、`GLOBAL_PHYSICAL_TO_INDEXED_SUBGROUP_COVERAGE_OPEN`。既存原著の独立全文検証・原計算ZIP再演のPASSではない。数学原著の追加収載は０、新規一般定理として台帳登録しない。PR #1860はDraft、DO_NOT_MERGE。
