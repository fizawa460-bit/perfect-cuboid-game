# 5. 逆写像・補助幾何・有限局所法の成果と障壁

[R4-25](../routes/R4-ROUTE-25.md)の原始ρ逆判定、[R3-02](../routes/R3-02.md)の固定HCS、[R3-05](../routes/R3-05.md)の固定D18算術、[R5-K18](../routes/R5-K18.md)の局所法停止をまとめる。補助対象の成果を、元signed sourceの全域閉鎖へ移さない。

## 原始標識付き三角形のρ逆判定

ρ=n/d>0を既約分数とする。ρ=B²/(AC)を与える正の原始標識付き三角形A²+B²=C²が存在するための必要十分条件は、nとn²+4d²が整数平方であること。存在すれば三角形は一意である。これは旧C152としてR4-25に保存された判定であり、次はその初等証明の読み直しである。

必要性：原始性よりgcd(B²,AC)=1なのでn=B²、d=AC。また
B⁴+4A²C²=(A²+C²)²。

十分性：B=√n、H=√(n²+4d²)とする。Hとnは同じparityなので
x=(H−n)/2、y=(H+n)/2は正整数で、xy=d²。gcd(n,d)=1からx,yの共通奇素因子は無い。n奇数ならgcd(x,y)=1。n偶数なら平方性より4|n、d奇数、H≡2 mod4なのでx,yは共に奇数となり、やはりgcd(x,y)=1。互いに素な積が平方なのでx=A²、y=C²。従ってC²−A²=B²、AC=dとなり原始性・C奇数も従う。x,yとBが固定されるので一意である。

この判定はρだけの補助点から元のprimitive baseを戻す際に有効。既に原始基底を持つactual Ward点には追加の排除ではなく、signed index、同じPOINT、S270を作る証明にもならない。

## 固定曲線の算術が消す範囲

| 材料 | 保存する成果 | まだ言えないこと |
|---|---|---|
| C117–C119 HCS | 固定genus3のrank1・p=3対数差・四円盤の親資料 | 全指数の元source空性や新外部監査 |
| 固定±18 C2 | 36次数体の類数1・真正Selmer9・局所障害への前提 | 105次数体の類数1、MW=9 |
| 固定D18/N18 | 旧rank≤1を撤回し、依存Selmer/MW上界を保持 | その上界だけでsource不存在 |
| 原曲線のrank下界・Prym/反射商 | 指定した曲線・体・点での算術 | 元Ward全指数へのlossless forward/逆写像 |

HCSの掲載は継承された内部・暫定研究の範囲。[既存HCS資料群](../../materials/hcs-crosslane-c117-119/README.md)と[±18親資料群](../../materials/selmer18-parent-chain/README.md)が証明・監査状態を対応付ける。C2、HCS、D18、C71など同じような名前の曲線を同一視しない。旧K21 rank≤1は現行R3-05のWITHDRAWN/SUPERSEDEDを優先する。

## 任意の有限Sを通る局所必要条件

[C241の原著証明](proofs/C241-finite-local-limit.md)は、全ての有限素数集合Sと指定されたdyadic深さに対し、旧C129四多項式G_iが正で、Sおよび実際のbase-bad素数2ABCの全素点で局所平方となる原始Euclid基底を無限に構成する。七つの指定合同類、旧C131/C132/C133/C153の条件の範囲を保持する。これは内部PROVISIONAL・R0未提出の従属method-limitで、新しい物理排除ではない。

証明は、指定有限素数をAの素因子側へ入れるCRTと、Bの二つの素因子に必要な二次剰余条件を課す構成を使う。指数をEuler周期で動かすことで合同を保ち、二つの素数の対数比の無理性から実parameterを高い領域へ送る。G_iのmonic最高項と定数項の剰余、p=2のmod8条件からHenselで全深さの局所平方を得る。global整数平方やactual sourceの存在は一つも構成していない。

量化子は「全ての有限Sに対し、それを通る基底が存在」であって、「一つの基底が全素数とglobal条件を通る」ではない。旧P108の固定v0版には外部解析定理の依存もあり、その依存を新しい独立監査済み成果へ変えない。

## off-indexの弱いreceiverを物理点にしない

[rank≥2仮定の原著](https://docs.google.com/document/d/1t7hdGOslGnrkNv45v8w5i4YL7wuwXC502UfSOXX8Fws/edit)は、E(Q)/(E(Q)[2]+ZP)で無限類のUを仮定し、有限局所深さを満たすMを取ってV_k=M(U+kP)、X_k=T0+2V_kを作る。局所有限商の指数をMが消すので、全kで有限素点の第四平方検査を通せる。一方無限商類からX_kは元の整数軌道に入らない。

三つの有理根は倍算公式から従い、実円周の回転でstrict実室を通る。しかし第四平方を加えた固定genus2曲線の有理点は有限なので、原稿の議論ではその例外は有限に留まる。rank≥2・無限類Uを仮定した弱receiverの構成であり、物理Q・global四根・S269 source・全基底rank≥2の証明ではない。

有限素数の追加、補助rank下界、genus表示の変更だけでは残るglobal同源点の空性を決められない。[canonical source](01-canonical-source.md)への正確な写像と点の排除が必要となる。

[主要ルート入口](README.md)
