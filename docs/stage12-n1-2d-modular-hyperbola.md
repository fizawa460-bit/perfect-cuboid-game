# Stage12-N1-2d：モジュラー双曲線型評価の一様誤差監査

## 判定

Shparlinski のモジュラー双曲線評価は、今回の共有 \(p\) 和へ**直接適用できない**。局所的な合同条件の処理、Kloosterman 和による完備化、box から正則領域への discrepancy 移行は再利用候補だが、必要な重み付き平均と全法平均の一様誤差は供給しない。

対象は

\[
\sum_{\substack{h(r^2+s^2)\le 2B\\r<s,\ (r,s)=1}}
\left(G(h)G(r)G(s)K(h,rs)-1\right).
\]

Shparlinski の Theorem 13 は、\(\gcd(a,m)=1\) に対するモジュラー双曲線

\[
xy\equiv a\pmod m
\]

の区間内点数を

\[
\frac{\varphi(m)}{m^2}XY+O\!\left(m^{1/2+o(1)}\right)
\]

で評価する。discrepancy を介した四分円領域では誤差が \(O(m^{3/4+o(1)})\) になる。

## 適合しない核心

Stage12 の約数展開から現れる合同条件は

\[
r^2+s^2\equiv0\pmod m
\]

であり、\((s,m)=1\) の部分では \(t=rs^{-1}\) として

\[
t^2\equiv-1\pmod m
\]

へ落ちる。これは二次元のモジュラー双曲線全体ではなく、薄い二次合同根の問題である。さらに法 \(m\) は合成数を含み、Theorem 13 は \(G(h)G(r)G(s)\) や \(K(h,rs)\) を伴わない。

coprime 条件は Möbius 反転で形式的に入れられるが、Stage12 ではその後に primitive 化の global Möbius 反転がさらに控えている。したがって、各 \(h\)・各法に対する点ごとの誤差ではなく、法と \(h\) を同時平均した総和可能な誤差が必要である。

## 素朴な誤差予算

\(h\)-slice の半径を

\[
R_h=(2B/h)^{1/2}
\]

とし、法 \(m\le R_h\) ごとの誤差を \(m^{\theta+o(1)}\) と仮定する。絶対値で足すと

\[
\sum_{h\le2B}\sum_{m\le R_h}m^\theta
\asymp
B^{(\theta+1)/2}
\sum_{h\le B}h^{-(\theta+1)/2}.
\]

\(-1<\theta<1\) ではこれは \(B^{1+o(1)}\) 級になる。従って、box の \(\theta=1/2\) でも、曲線領域の \(\theta=3/4\) でも、素朴な全法・全 \(h\) 加算から冪節約は残らない。

これは真の誤差が \(B\) 級であるという主張ではない。点ごとの評価だけでは不足し、次のいずれかが必要だという障害判定である。

- dyadic 範囲間の cancellation
- 法の有効範囲を狭める正確な約数双曲線分解
- 法または \(h\) に関する averaged large sieve / Kloosterman 評価
- 二平方表現数の相関定理

## 再利用可能な部分

- unweighted な逆元・積合同に対する Kloosterman 完備化
- box から正則な平面領域への discrepancy 移行
- 独立に総和可能な誤差が得られた後の visible-point Möbius reduction

## 未解決の部分

1. 合成法上の \(t^2\equiv-1\pmod m\) の根を重み付き総和へ組み込むこと
2. \(G(h)G(r)G(s)\) の法・\(h\) 同時平均
3. \(K(h,rs)\) の共有素因子相関
4. global Möbius 反転後にも残る一様誤差

分類は `B_local_distribution_template_relevant_not_sufficient` とする。

次は Stage12-N1-2e として、\(G\) を約数指示関数へ展開し、実際に必要な dyadic \(h\)・法範囲と誤差予算を確定する。その後に large sieve と二平方相関定理のどちらが適合するかを再判定する。

## 出典

Igor E. Shparlinski, *Modular Hyperbolas*, arXiv:1103.2879, Theorem 13、式 (10)、四分円領域への帰結、Questions 15 and 31.
