# Stage12-N1-2 本格監査報告 R01

監査日: 2026-08-07  
対象: `stage12-n1-2-final.txt` および `PC-N1-2J-2P-PROOF-CHAIN-20260807-R01.html`  
対象証明鎖: Stage12-N1-2j から 2p  
判定: **REPAIRABLE**

## 1. 総合判定

提示された証明鎖には、最終漸近式

\[
C_{\rm prim}(B)\sim \frac{\kappa}{12\pi}B(\log B)^3
\]

を支持する一貫した修復方針があります。特に、2lで de la Bretèche の直接適用を撤回し、2mから2pで一変数 Selberg–Delange、coprime cross correction、一様長方形和へ切り替えた判断は論理的に整合しています。

しかし、現状の文書だけから最終定理を `CLOSED` と判定することはできません。理由は、次の3件の実質的な論証不足と、2件の依存資料不足です。

- **MAJOR-01**: 一様長方形補題の大係数領域で、実際に得た指数から最終表示の指数へ不正に強化しています。
- **MAJOR-02**: fixed-\((r,s)\) remainder で、zero-free-region saving を畳み込み全域へ一様に引き出す手順が未証明です。
- **MAJOR-03**: 長方形主項を結合領域へ移送して正確な係数 \(1/12\) を得る部分が概要に留まり、radial kernel、divisor variables、parity/orientation factorを含む完全な Stieltjes 計算がありません。
- **MAJOR-04**: 監査バンドルに `C_prim(B)` の完全な定義元である2bと、\(\kappa\) の完全な定義元である2fが含まれず、自己完結監査ができません。
- **CLARIFICATION-01**: Tenenbaum II.5.2から採用する誤差関数の正確な仮定と結論を、原文に即して引用する必要があります。

現時点では「定理が偽」と判断する根拠はありません。MAJOR-01は弱い上界へ直しても最終主項に対して低次を維持できます。MAJOR-02とMAJOR-03は、修復可能性が高いものの、現在の文章だけでは証明が完了していません。

## 2. 監査対象の読み取り確認

HTMLバンドルは次を満たしています。

- `BUNDLE_ID=PC-N1-2J-2P-PROOF-CHAIN-20260807-R01`
- `SOURCE_SNAPSHOT_COMMIT=2958c330139904bd57c6d2b404dc8f74dd30f75f`
- `CONTENT_SHA256=ebfc3037ffb337c63877f3fc03e1f107e9cbfe414106db0404dbbb899568a766`
- 先頭文書: Stage12-N1-2j
- 末尾文書: Stage12-N1-2p
- `CHECKPOINT=START_OF_MAIN` から `CHECKPOINT=END_OF_MAIN` まで取得済み

ただし、HTML原ファイルの2j内に制御文字が2か所あり、本来の `\frac` がフォームフィード文字と `rac` に分断されています。数学監査では本来の `\frac` として復元して読みました。

## 3. 証明鎖の整合性

### 3.1 de la Bretèche撤回後のルート

証明鎖の最終ルートは、文書上では次のように統一されています。

\[
2j\to2k\to2l\to2m\to2n\to2o\to2p.
\]

2kで未検証の de la Bretèche 直接適用を一度 `CLOSED` としましたが、2lでその判定を撤回し、P2、P3未確認を明示しています。2m以降は直接適用を使わず、

1. 一変数級数 \(B_\beta(s)\)
2. coprime cross correction \(C(s_1,s_2)\)
3. 一様長方形和
4. Abel／Stieltjes移送

を使用しています。Finalも「未検証の de la Bretèche 直接適用は使用しない」としており、旧ルートとの矛盾はありません。

### 3.2 一変数Euler積

\(q\equiv1\pmod4\) で

\[
A_q(s)=1+\frac{b_q q^{-s}}{1-q^{-s}},\qquad b_q=\frac{2(q-1)}{q+1}
\]

とし、

\[
B_\beta(s)=\zeta(s)L(s,\chi_4)J(s)
\]

とする局所分解は整合しています。奇素数局所因子について、

\[
J_q(s)=(1-q^{-s})(1+(b_q-1)q^{-s})
\]

および

\[
J_p(s)=1-p^{-2s}\qquad(p\equiv3\pmod4)
\]

は正しい形です。2-adic因子は明記を推奨しますが、有限因子として処理可能です。

\(b_q-2=-4/(q+1)\) から

\[
J_q(s)-1=O(q^{-1-\sigma})+O(q^{-2\sigma})
\]

となり、\(\sigma>1/2+\varepsilon\) での局所一様絶対収束は妥当です。各局所因子がこの半平面で零を持たないことも直接確認できます。

### 3.3 cross correction

局所因子

\[
C_q(s_1,s_2)=1-\frac{u_q(s_1)u_q(s_2)}{(1+u_q(s_1))(1+u_q(s_2))}
\]

から

\[
C_q(s_1,s_2)-1=O(q^{-\sigma_1-\sigma_2})
\]

を得る構造は妥当です。したがって \(s_1=s_2=1/2+\delta\) での weighted absolute convergence

\[
M_\delta=\sum_{a,b\ge1}\frac{|c(a,b)|}{(ab)^{1/2+\delta}}<\infty
\]

も、局所絶対収束を明示すれば導けます。

## 4. 指摘事項

## MAJOR-01: 長方形補題の大係数領域の指数が不正

2p §3.2では、\(A=R^{1/2}\)、\(a>A\) に対して

\[
a^{-1}\le R^{-1/4+\delta/2}a^{-1/2-\delta}
\]

を用い、まず

\[
R^{3/4+\delta/2}S(\log 2R)(\log 2S)M_\delta
\]

を得ています。ここまでは整合します。

しかしその直後に、対数を小べきへ吸収することで

\[
R^{1/2+\delta}S
\]

へ強化しています。この強化は、文書の前提 \(\delta\in(0,1/4)\) では成立しません。必要な指数比較は

\[
\frac34+\frac\delta2\le\frac12+\delta,
\]

すなわち \(\delta\ge1/2\) であり、前提と両立しません。

### 修復案

最終補題を、任意の固定 \(\varepsilon>0\) に対して

\[
S(R,S)=\mathfrak C RS+O\left(RS\{E_*(R^{1/2})+E_*(S^{1/2})\}+R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}\right)
\]

と弱めます。この誤差でも \(R,S\ll B^{1/2}\) なら

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}\ll B^{7/8+\varepsilon/2},
\]

となり、適切な小さい \(\varepsilon\) に対して \(o(B(\log B)^3)\) を維持します。

ただし結合領域で使用するときは、raw rectangular errorではなく、kernelを掛けた後のbox誤差を再計算してください。

判定: **MAJOR / REPAIRABLE**

## MAJOR-02: fixed-circle remainderの \(\omega(X)\) 引き出しが未証明

2k §2では

\[
A^+_{r,s}=G(rs)(a_0*h_{r,s})
\]

とし、base partial sumの誤差

\[
O(X^{1/2}\omega(X))
\]

から

\[
R_{r,s}(X)=O\left(G(rs)H_{\rm abs}(rs)X^{1/2}\omega(X)\right)
\]

を主張しています。

畳み込み後の誤差は実際には概略

\[
G(rs)\sum_{\ell\le X}|h_{r,s}(\ell)|(X/\ell)^{1/2}\omega(X/\ell)
\]

です。\(\omega(t)\) は大きい \(t\) ほど小さくなるため、\(X/\ell\le X\) から

\[
\omega(X/\ell)\le\omega(X)
\]

とはできません。向きは逆です。したがって \(\omega(X)\) をそのまま全域へ引き出すことはできません。

### 修復候補

\(\ell\le X^{1/2}\) と \(\ell>X^{1/2}\) に分け、前半では \(\omega(X^{1/2})\) を用います。後半は finite Euler correctionの係数尾部を別の重みで評価する必要があります。必要なのは、\(rs\) 平均時にも制御できる形、たとえば

\[
R_{r,s}(X)\ll G(rs)\widetilde H(rs)X^{1/2}\omega(X^{1/2})+\text{tail}_{r,s}(X)
\]

とし、\(\sum_{r,s}\text{tail}_{r,s}(X)\) が最終主項より低次になることを示すことです。

別案として、有限Euler補正を含むDirichlet級数にPerron／Selberg–Delangeを直接適用し、依存定数を明示的な乗法重みで制御する方法があります。ただし、その場合も \(rs\) 平均一様性を別途示す必要があります。

2k §3の総和評価はこのremainder評価に依存するため、現状のままではfixed-circle remainder閉包は完了していません。

判定: **MAJOR / REPAIRABLE BUT PROOF REQUIRED**

## MAJOR-03: 結合領域への移送と係数 \(1/12\) の導出が不足

2nおよびFinal §5では、長方形和をdyadic boxesへ分割し、二変数 Abel／Stieltjes部分和分を適用した結果として

\[
\int_{2\max(y,z)<L}(L-2\max(y,z))\,dy\,dz=\frac{L^3}{12}
\]

を提示しています。

この積分自体の値は正しいです。しかし、直前の主項は概略

\[
B\sum_{r<s}\frac{\gamma(rs)}{r^2+s^2}
\]

であり、長方形補題は

\[
\sum_{r\le R,s\le S}\beta(r)\beta(s)1_{(r,s)=1}
\]

に対するものです。現在の文書では、次の変換が完全には書かれていません。

1. \(\gamma(rs)\) のdivisor展開後、どの変数を長方形補題の \(r,s\) としているか。
2. 元の辺変数、divisor変数、倍数変数を積分した後、radial kernel \((r^2+s^2)^{-1}\) がどのように消え、\(dy\,dz\) の一様測度になるか。
3. fixed-ratio box内で「定数倍比較」するだけでなく、正確な先頭係数を保持するStieltjes積分。
4. odd–odd、opposite-parity、orientationの前置因子が \(\eta/(12\pi^2)\) へなる完全な表。
5. boxごとの誤差がkernelと変分を掛けた後に `o(B(log B)^-A)` となること。

固定比dyadic boxで \(r^2+s^2\) を単にbox scaleと比較するだけでは、上下界は得られても正確な先頭定数は得られません。正確な定数には、meshを細分化して極限を取るか、kernelを保持したStieltjes積分を明記する必要があります。

### 修復案

「結合領域移送補題」を独立に作り、次を式として記載してください。

- divisor展開後の完全な有限または絶対収束和
- その各項に対する長方形主項の代入
- 二変数部分和分の境界項と二階混合Stieltjes項
- radial kernelとheight lengthの導関数
- 主項積分を対数変数へ変換するヤコビアン
- parity/orientationを含む前置定数
- MAJOR-01修正後の誤差を全boxで合計した評価

判定: **MAJOR / CENTRAL GAP**

## MAJOR-04: バンドルは自己完結ではない

レビューHTMLは「自己完結レビューHTML」としていますが、Finalの定理を第三者が検証するために必要な次の定義が含まれていません。

- Stage12-N1-2bで定義された \(C_{\rm prim}(B)\) の完全な集合・重複度・orientation・height定義
- Stage12-N1-2fで定義された \(\kappa\) の完全なEuler積とfront factor
- raw countからprimitive countへの対象レベルでの対応
- \(\eta_p/\kappa_p\) を監査するための \(\kappa_p\) の明示式

2kには一部の三法局所因子が記載されていますが、\(\kappa\) 全体の正規化がないため、

\[
\eta=\pi\kappa
\]

をこのバンドルのみで完全再計算できません。

### 修復案

2bと2f全体を追加する必要はありません。レビュー用に次の2ページを追加すれば足ります。

- `Definitions and counting convention`: \(C_{\rm prim}(B)\) の完全定義
- `Constant sheet`: \(\kappa\)、\(\eta\)、各local factor、2-adic／archimedean front factor

判定: **MAJOR FOR SELF-CONTAINMENT / NOT A MATHEMATICAL CONTRADICTION**

## CLARIFICATION-01: Tenenbaum定理の使用形

Tenenbaum II.5.2がSelberg–Delangeの一般形として参照されること自体は妥当です。ただし、現在の文書は

\[
B_\beta(X)=c_\beta X+O(XE(X)),\quad E(X)=\exp\{-c(\log X)^{3/5}(\log\log X)^{-1/5}\}
\]

という特定のzero-free-region誤差を採用しています。最終稿では、Theorem II.5.2のどのhypothesis、parameter、remainder caseを用いたかを引用し、\(H(s)=L(s,\chi_4)J(s)\) がその領域で必要条件を満たすことを項目別に照合してください。

特に「\(J\)が \(\Re s>1/2+\varepsilon\) で正則」という事実だけでなく、採用するzero-free region上での一様有界性、\(L(s,\chi_4)\) を含むgrowth、係数majorant条件を具体的に接続する必要があります。

判定: **CLARIFICATION / REFERENCE LOCK REQUIRED**

## MINOR-01: HTML内の制御文字

2j内の次の2か所で `\frac` が制御文字と `rac` に壊れています。

\[
1+\frac{2t(p-1)}{p+1}
\]

同式の \(\gamma(rs)\) 局所積とlocal identityです。原Markdown生成前またはHTML生成時にフォームフィードへ変換されたものと見られます。

判定: **MINOR**

## MINOR-02: Final内の記号定義

Final単体では、次が外部依存です。

- \(A_{r,s}(m)\)
- \(G(n)\)
- \(\beta(n)\) の「それ以外は0」
- \(E_*(X)\)
- retained regionの完全定義

Finalを概要として使うなら問題ありません。単独提出するなら定義一覧を追加してください。

判定: **MINOR FOR SUMMARY / MAJOR IF CLAIMED SELF-CONTAINED**

## 5. 境界項の評価

shallow領域のformal mass比

\[
3\tau^2-2\tau^3,\qquad \tau=L^{-3/4}
\]

から

\[
O(BL^{3/2})
\]

を得る計算は整合しています。

一方、対角・円弧境界の

\[
O(BL^{2+o(1)})
\]

およびfloor endpointの

\[
O(BL^{1+o(1)})
\]

は安全側上界として記載されていますが、完全な導出は示されていません。これらはMAJOR-03の結合領域移送補題の中で一緒に証明するのが適切です。現時点では矛盾とは判定しませんが、独立証明済みとも判定しません。

## 6. 局所定数の監査可能範囲

奇素数積

\[
\prod_{p\ \mathrm{odd}}(1-p^{-2})^{-1}=\frac{\pi^2}{8}
\]

は正しいです。したがってfront factor比を \(8/\pi\) とし、全奇素数で

\[
\eta_p/\kappa_p=(1-p^{-2})^{-1}
\]

が成立するなら、

\[
\eta/\kappa=\pi
\]

は従います。

ただし、front factor比と \(\kappa_p\) の完全定義がバンドル内にないため、前提部分は独立再計算できません。これはMAJOR-04に含めます。

## 7. 管理側へ返す修復優先順位

1. **2pの長方形誤差を弱い正しい指数へ修正する。**
2. **2k fixed-circle remainderの畳み込み誤差を分割評価で再証明する。**
3. **結合領域移送補題を完全な式で新設する。**
4. **Cprim定義sheetとκ定数sheetをレビューbundleへ追加する。**
5. **Tenenbaum II.5.2の適用条件を原典と一対一で照合する。**
6. HTML内のフォームフィード2件を修正する。

## 8. 最終判定コード

```text
VERDICT=REPAIRABLE
FATAL=0
MAJOR=4
MINOR=2
CLARIFICATION=1
CENTRAL_OPEN_ITEMS=FIXED_CIRCLE_REMAINDER,COUPLED_REGION_TRANSFER
THEOREM_STATUS=PLAUSIBLE_BUT_NOT_CLOSED_FROM_PRESENT_BUNDLE
```

## 9. 管理チャッピー向け短縮メッセージ

```text
Stage12-N1-2 j〜pを独立監査した結果、定理を否定するFATALは見つからなかったが、現状はREPAIRABLE。主要修正は3点。
(1) 2p §3.2で R^(3/4+δ/2)S を R^(1/2+δ)S に吸収しているが、δ<1/4では指数比較が成立しない。R^(3/4+ε)S型へ弱めても最終的には低次。
(2) 2k fixed-circle remainderで ω(X/l) を ω(X) として全畳み込みから引き出すのは向きが逆。l≤√X / l>√X分割などで一様平均誤差を再証明する必要あり。
(3) 2n〜Final §5の結合領域移送は、radial kernel・divisor variables・Stieltjes積分・parity/orientation factorを完全に書かないまま L^3/12へ飛んでいる。正確な主定数のため独立補題が必要。
またbundleにCprim定義元2bとκ定義元2fがなく、自己完結監査不能。定義sheetと定数sheetを追加すること。
判定: REPAIRABLE / FATAL 0 / MAJOR 4。
```

## 10. 参照文献

- Gérald Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, Third Edition, Chapter II.5.
- Régis de la Bretèche and Gérald Tenenbaum, *Remarks on the Selberg–Delange method*, Acta Arithmetica 200 (2021), 349–369.
- Wenguang Zhai, *On primitive lattice points in planar domains*, Acta Arithmetica 109 (2003), 1–26.
