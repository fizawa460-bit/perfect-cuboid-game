# 1. 元のWard軌道からcanonical整数源へ

所有ルート：[R1-01](../routes/R1-01.md)・[R1-09](../routes/R1-09.md)・[R4-25](../routes/R4-ROUTE-25.md)。主要本文は[C195の原著証明](proofs/C195-canonical-source.md)。これは内部PROVISIONALの従属結果として保存し、今回新しい独立監査やR0採択を付与しない。

## 対象と最終形

正の原始標識付き三つ組 A²+B²=C²、C奇数、D=AC と、同じ元曲線・点

$$
E:y^2=x(x-A^2)(x+C^2),\quad P=(D,BD),\quad T_0=(0,0),\quad D_n=T_0+[2n]P
$$

を固定する。signed |n|≥6、実際の点が −B²<x(D_n)<0、y(D_n)<0 を満たし、S268の既約表示 r=BZ/b>0、gcd(Z,b)=1、gcd(b,2ABC)=1、b奇数を使う。この限定の下で、T_n=b²−Z² が正の整数平方であることと、同じb,Zに対応するcanonical S269整数Gaussian・役割・正しいsigned POINTの存在が同値になる。

現行の |n|≥12 では、旧S289とC174/S290による四つのGLOBAL正整数S243根/common c、代数的Kummer、同じQの無限商類まで従う。S270のTRUE四GOOD/actual-critical-H TOP、全PROPER ordinary β、他のHOLD・NEGATIVE・原始性条件は保持する。全ての物理条件を満たす点が存在すると証明した結果ではない。

## 証明の流れ

1. 実際のnPの倍算公式とT0平行移動から、rとp,qは既に正の有理数で、p²=A²+r²、q²=C²−r²を満たす。任意の楕円曲線点にこの三平方を移さない。
2. T_n=Y²>0とするとs=BY/b。R=br、S=bs、U=bp、V=bqは正整数になる。J=UV+RS、K=UV−RSは正で、JK=(Db²)²。
3. 各ℓ|bについてR,S,U,Vはℓ-unitであり、J+K=2UVと積から {vℓ(J),vℓ(K)}={4vℓ(b),0}。元軌道のformal depthを使うと全ℓ|Dで vℓ(J)=vℓ(K)=vℓ(D)。これを全素数で合わせる。
4. 整数の一意分解から J=DM⁴、K=DN⁴、MN=b、gcd(M,N)=1、M>N≥1 が一意に決まる。任意に選んだbの分解ではない。
5. N=1を高さで除く。旧高さ定数 λ>0、432λ≥c_E と同じ元Pの高さを使い、

$$
\log b-\tfrac12\log(C/A)>4n^2\lambda-\tfrac{25}{96}c_E
\ge c_E\left(\tfrac{n^2}{108}-\tfrac{25}{96}\right)>0
$$

となる。一方N=1なら元の役割不等式からb<√(C/A)となり矛盾する。従ってM>N>1。
6. primitive三平方 Z²+Y²=b² からF>G>0を一意に復元する。even nではZ=2FG、odd nではZ=F²−G²。残る脚をYとすると

$$
b=F^2+G^2=MN,\qquad
4B^2FG(F^2-G^2)=D(M^4-N^4).
$$

最後の式はJ−K=2RSそのもので、y(D_n)=−rpqも初めから同じsigned POINTである。

前提を満たす元軌道上の正の補平方から、canonicalな証人を再構成する証明である。有限実験に補平方の成功例が無いことは、この全称証明の根拠に使わない。

## 古い記録への訂正と監査

R1-274、R1-286およびR4の2026-10-26資料には、弱い前提の下でQ無限商が未解決という記述が残る。2026-10-28 C195と[現行R4-25の優先表示](../routes/R4-ROUTE-25.md)は、上記の正確なactual orbit＋正の補平方＋現行 |n|≥12 の下ではS289/C174を継承して自動となることを明記する。従ってH四乗、proper役割、四根、Q∞を別々の新しい未証明目標として数え直さない。

C195はR1-223の訂正を取り消していない。任意のM,N、normだけのGaussian、局所平方、緩和された補助曲線点には同値を適用できない。新たな独立敵対的監査はこの公開では実施していない。

## 残る核心

全許容基底と明示されたsigned指数域で、実際のstrict元軌道のT_nが大域的に正の平方になれないこと、またはその点を有効に全分類することが残る。[R2の真正質量上界](02-mid-high.md)も別の残存方向である。元の整数Gaussianを書き直すこと、Qの古い独立gateを再導入すること、有限素数検査を追加することは、この未証明部分の解消にならない。

[主要ルート入口](README.md) · [原著C195のDrive](https://drive.google.com/file/d/1qI7lyiiJF_5Mf7mevzInxG-HZGRQzqUF/view)

## 原証明本文追補（2026-11-09）

[C195の直接前提11本文](C195-DEPENDENCIES.md)と[C196〜C200の後続本文](MIGRATION-COMPLETION-CHECKLIST.md)を収載。S233/S237/S240のC195内再構成と旧S268/S269/C174/S289/S290の継承を区別する。新監査・新採択・実際の補平方source存在は主張しない。

[C196〜C200後続原証明の論理的連鎖とC197 NEXT失効の限定レビュー](C196-C200-DEPENDENCY-REVIEW.md)。資料間の条件対応は確認したが、個別のisogeny/height/source-coverの数学的独立監査ではない。

[親C195の倍算二恒等式・役割p付値・高さ係数の限定独立検算](MAJOR-PARENT-MATH-PAPER-CHECK.md)。S237の全formal depthとC174の一様高さ入力、S289/S290の全数学的適用はまだ独立再監査していない。
