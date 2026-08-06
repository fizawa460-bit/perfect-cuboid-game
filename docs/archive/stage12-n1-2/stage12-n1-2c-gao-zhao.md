# Stage12-N1-2c：Gao–Zhao型との対応検証

## 判定

Gao–Zhao の定理は、今回の共有 $p$ 和へ**直接適用できない**。ただし、証明技法の一部は再利用候補である。

Gao–Zhao が扱う対象は

$$
S_N(x)=\sum_{m,n\le x}d(n^2+Nm^2)
$$

であり、固定された二次形式、box領域、通常の約数関数を対象とする。

Stage12-N1-2b の対象は

$$
\sum_{\substack{h(r^2+s^2)\le2B\\r<s,\ (r,s)=1}}
\bigl(G(h)G(r)G(s)K(h,rs)-1\bigr)
$$

であり、次が追加される。

- $h$ という可変スケール
- 円領域と順序条件
- $(r,s)=1$
- 通常の約数関数ではない重み $G$
- $h$ と $rs$ の共有 $1\pmod4$ 素数に支えられる補正 $K$
- 後段のglobal Möbius反転に耐える一様誤差

従って、Gao–Zhao の漸近公式を引用するだけではStage12の和は評価できない。

## 再利用候補

- 約数双曲線分解の設計
- $r^2+s^2$ に対応する二次合同式の根の整理
- dyadic分割後のlarge sieve・指数和評価

## 新たに必要な補題

1. $h(r^2+s^2)\le2B$ 上の $G(h)G(r)G(s)$ の重み付き平均
2. $K(h,rs)$ の総寄与の一様評価
3. coprime・ordered sectorへの制限による誤差評価
4. global Möbius反転後にも総和可能な誤差項

分類は `B_method_template_relevant_theorem_not_directly_applicable` とする。

次は Stage12-N1-2d として、モジュラー双曲線型評価が上記の一様誤差を処理できるか検証する。

## 出典

Peng Gao and Liangyi Zhao, *Mean values of divisors of forms $n^2+Nm^2$*, arXiv:1812.07863.
