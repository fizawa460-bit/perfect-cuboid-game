# Stage12-N1-2：共有面対角線畳み込みの双曲線座標化

## 確定した恒等式

第二の直角三角形

\[
p^2+c^2=d^2
\]

に対し

\[
u=d-c,\qquad v=d+c
\]

と置く。\(uv=p^2\) であり、\(h=\gcd(u,v)\) とすれば一意に

\[
u=hr^2,\qquad v=hs^2,\qquad 1\le r<s,\qquad \gcd(r,s)=1
\]

と書ける。したがって

\[
p=hrs,\qquad c=\frac{h(s^2-r^2)}2,\qquad d=\frac{h(r^2+s^2)}2.
\]

整数性と高さ条件は

\[
h(r^2+s^2)\equiv0\pmod2,\qquad h(r^2+s^2)\le2B
\]

に一致する。

\[
G(n)=2H(n)+1=\prod_{q\mid n,\ q\equiv1\ (4)}(2v_q(n)+1)
\]

と置くと、\(G\) は乗法的であり、raw oriented chain数は厳密に

\[
\boxed{
C_{\mathrm{raw}}(B)=
\sum_{\substack{h\ge1,\ 1\le r<s,\ (r,s)=1\\
h(r^2+s^2)\le2B\\
h(r^2+s^2)\equiv0\ (2)}}
\bigl(G(hrs)-1\bigr)
}
\]

となる。

これにより、Stage12-N1dで障害となった \(B\) 依存関数 \(L_B(p)\) は被加重関数から消え、すべての \(B\) 依存性が明示的な二次高さ領域へ移った。

## 有限監査

| \(B\) | Stage11 raw oriented | 双曲線重み和 | \((h,r,s)\)点数 |
|---:|---:|---:|---:|
| 1,000 | 3,180 | 3,180 | 1,762 |
| 2,000 | 8,396 | 8,396 | 3,962 |
| 5,000 | 29,446 | 29,446 | 11,024 |
| 10,000 | 74,414 | 74,414 | 23,744 |
| 20,000 | 185,206 | 185,206 | 54,350 |

全閾値で完全一致した。有限値を漸近密度とは解釈しない。

## 解析上の現在地

判定は `A_reparameterization_progress_new_mean_value_lemma_needed` とする。

進展：

- \(L_B(p)\) の非乗法的な高さ切断を消去した。
- 算術重みを固定乗法関数 \(G(hrs)\) へ変換した。
- 高さ \(B\) を二次領域 \(h(r^2+s^2)\le2B\) に隔離した。

未証明：

- \(h\) と \(rs\) が素因数を共有し得る状況での \(G(hrs)\) の平均評価。
- 等辺chainの一般的除外または別評価。
- global Möbius反転に耐える一様誤差項。

## 文献候補

以下は方法論上の候補であり、直接適用や新規性は未確認である。

- Peng Gao and Liangyi Zhao, *Mean values of divisors of forms \(n^2+Nm^2\)*：二次形式値上の約数平均。
- Igor Shparlinski, *Modular Hyperbolas*：双曲線合同条件の格子点分布と誤差評価。
- Fernando Chamizo, *The additive problem for the number of representations as a sum of two squares*：二平方表現数の相関評価。
- Konstantine Zelator, *A Non-Existence Property of Pythagorean Triangles with a 3-D Application*：連結Pythagorean triangleの関連構造。ただし漸近計数ではない。

現時点で、今回の具体的な畳み込みを扱った直接の先行研究は確認できていない。ただし網羅的な新規性監査は未完了である。
