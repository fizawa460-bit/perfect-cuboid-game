# Stage35EX R3-07 row364 — 真正2-Selmer次元9の確定と残余CT一成分への還元

研究日：2026年11月5日。RUN：`R3-20261105-C2-EXACT-SELMER9-RESIDUAL-CT-ENTRY`。

**固定signed ±18の種数17曲線C₂について、row363の上側候補8次元が、全場所のfake局所Kummer条件を実際に満たすことを認証した。さらに真正への持ち上げを証明し、真正2-Selmer次元を「高々9」から「正確に9」へ確定した。既知7 MW類で割ったSelmer商は正確に2次元である。**

**依頼された全MWの163進上側空間Uは今回も未構成。MW階数は7..9のまま、全MW消滅微分のa₀単元も未証明、元source排除0件。** 新結果は内部厳密検算PASS、独立数学監査PENDING／未実施。row363の通常類群・全単数平方類の証明を継承する証明連鎖である。研究中に親row363の限定独立監査PASS_SCOPEDを受領したため、その判定を継承する。今回こちらが親の独立監査を新たに実施したという意味ではない。

## 1. 研究対象と新規性

対象は従来と同一の

\[
C_2:Y^2=h_2(X)=A(X)^2-XB(X)^2,\quad \deg h_2=36,\quad
J=\operatorname{Jac}(C_2),\quad P_0=(0,1),\quad p=163.
\]

K=Q(θ)=Q(V)、θ=V⁴、Gal(h₂/Q)=S₃₆も同じ。全係数、19単数u_i、既知7類の対数は証拠内の親証書に固定する。P23-LOWの一つのsubleafであり、LOW全域の完了とは区別する。

| 内容 | 新旧の区別 |
|---|---|
| 類数1、全単数平方類、2進rank11、上側8次元、κ₁・κ₂ | row363既出。再加点0 |
| 5つの奇数悪素点の全局所生成元、2進全局所生成元 | row353・355既出。再加点0 |
| 真正→fakeの1次元核がδ₂(D∞)に一致 | row351・352既出。再加点0 |
| 既知7類の実際の163進対数・minor137・10本の部分微分 | row361既出。再加点0 |
| **κ₁・κ₂の全場所への適合、fake交差の正確な8次元、真正Selmerの正確な9次元** | **今回の対象固有の新しい計算・証明差分** |
| Cassels–Tate対合の一般理論、有限体・Sturm・線形代数 | 標準理論。新しい一般手法とは主張しない |
| 2次元商上の対合を一成分へ絞り、非零ならU=0となること | 新しい正確なSelmer商に対する従属的な研究還元 |
| 拡張した有限探索、親プログラムの再演 | 計算根拠・探索記録。独立の新定理として数えない |

重複照合は現行R0 ACTIVE、R3の担当行とrow351〜352・359〜363、R5 K04/P23、親証書・旧証明の該当部分を使用した。全アーカイブの意味論監査や世界的新規性は主張しない。

## 2. 具体的な残余候補の全局所適合

row363の19単数座標では

\[
\kappa_1=u_2u_5u_9u_{11}u_{14}u_{16},\qquad
\kappa_2=u_6u_7u_{10}u_{14}u_{15}u_{17}u_{18}.
\]

指数maskは順に0xa512、0x36260。全て平方類および有理scalarを法とする。両者の通常体ノルムは正確に+1である。

### 2.1. 実場所

Vの4実根を、幅2⁻²⁵⁶の相異なる有理区間で固定した。Sturm列でFの実根総数4、各区間の根数1を確かめ、19単数の各実埋め込みの符号を有理区間Horner演算で決定した。探索用の数値近似は証明に使っていない。

両κの実符号は、Vの実根の昇順でそれぞれ

\[
(+,+,+,+),\qquad(+,+,+,+).
\]

従って両者の実fake像は自明であり、実局所Kummer像に含まれる。

### 2.2. 2進場所

row355の18 fake生成元とscalar −1の完全な19次元前像を再利用する。row363の実際の38平方類座標を用いると

| 候補 | 38座標のmask | 旧局所生成元＋scalarにおける係数mask |
|---|---|---|
| κ₁ | 0x4d13d2803 | 0x1cdee |
| κ₂ | 0x3665654ed9 | 0x24809 |

列順と全生成元の意味は`math/local_membership_certificate.json`と親`local2.json`に固定した。これは零条件の検査だけでなく、実在する旧局所Jacobian生成類の和としての明示的な表示である。

旧局所生成元にはUNRAM・TAMEの局所類が含まれる。それらを新しいQ上のMW類とは認定しない。

### 2.3. 5つの奇数悪素点

旧θ残余因子q(X)を、gcd(F(V),q(V⁴))で同じV残余因子に移した。次数および重複度を検査し、全因子の積がF mod pと一致することを確かめた。各u_iの有限体平方指標は、正確な有限体ノルムのLegendre指標として計算した。探索側のPARI resultantと、検証側の別のEuclid resultantが一致する。

以下のビットは旧θ因子順で、最初の因子を最下位bitとする。E₄はp=2843の旧局所類[(4,y)−P₀]。

| p | κ₁の指標 | κ₁の旧局所表示 | κ₂の指標 | κ₂の旧局所表示 |
|---|---|---|---|---|
| 2843 | 0x0b | D₁ᵦ+D₂+D₉+E₄ | 0x2c | D₁ₐ+D₂+D₉+E₄ |
| 13963 | 0x02 | D₁ₐ | 0x02 | D₁ₐ |
| 329475607 | 0x03 | D₄ | 0x07 | D₁ᵦ |
| 1034386920659 | 0x05 | D₁ₐ | 0x05 | D₁ₐ |
| 23910039195629 | 0x00 | 0 | 0x07 | D₁ᵦ |

奇数局所体では単数の平方類は残余体の平方指標で決まる。全単数性と上記の表示から、両κは全5場所のfake局所像に入る。

### 2.4. 残る全ての場所

残る有限場所は奇数良還元素点。両κは通常単数なのでそこで不分岐であり、Norm=1である。

良還元かつp≠2では、真正Kummer像はH¹_unr(Q_p,J[2])と一致する。有限体のガロア群に対し

\[
0\longrightarrow J[2]\longrightarrow M\xrightarrow{N}\mu_2\longrightarrow0,
\qquad M=\operatorname{Res}_{K/\mathbf Q}\mu_2/\mu_2
\]

のコホモロジー完全列を適用すると、不分岐なM類でNormが自明なものは不分岐なJ[2]類へ持ち上がる。従って両κは、列挙していない良還元場所でもfake局所Kummer像に入る。これは有限素数の追加探索による推測ではない。

## 3. fake交差が正確に8次元であること

row363は全大域候補を含む

\[
S_{\rm upper}=S_6\oplus\langle[\kappa_1],[\kappa_2]\rangle,
\qquad\dim S_{\rm upper}=8
\]

を既に認証した。S₆は旧6有理除数のfake像であり、当然全局所条件を満たす。前節により残る2基底も全局所条件を満たす。局所Jacobian像は群なので8基底の全ての和も条件を満たす。

従って、通常のfake Jacobian局所交差S_fakeについて

\[
S_{\rm fake}\subset S_{\rm upper}\subset S_{\rm fake},
\qquad\boxed{S_{\rm fake}=S_{\rm upper},\quad\dim S_{\rm fake}=8.}
\]

これはC₂上の点そのもののtwo-cover Selmer**集合**が8次元という主張ではない。対象はJの群である。

## 4. 真正Selmerへ全て持ち上がることの証明

T=Res μ₂、M=T/μ₂とする。固定のS₃₆作用についてM(Q)=0であり、旧row351〜352は

\[
\ker\bigl(H^1(\mathbf Q,J[2])\to H^1(\mathbf Q,M)\bigr)
=\langle\partial(1)\rangle,
\quad\partial(1)=\delta_2(D_\infty)\ne0
\]

を証明済み。D∞=[I₊−I₋]はQ上の有理Jacobian類である。

任意のα∈S_fakeを取る。本節ではαは8基底の積として表し、Norm(α)=+1の通常単数代表を取れる。そのH¹(Q,T)類をH¹(Q,M)へ写したmはN(m)=0を満たす。従って上の短完全列から、mを持ち上げるs∈H¹(Q,J[2])が存在する。

任意の場所vで、fake局所適合により、同じm_vを持つ真正局所Kummer類t_vが存在する。差s_v−t_vは局所完全列の核なので、0または∂_v(1)である。しかし

\[
\partial_v(1)=\operatorname{res}_v\delta_2(D_\infty)
\]

自身が真正局所Kummer像に入る。よってどちらの場合もs_vは局所Kummer像に入る。従ってs∈Sel²(J/Q)。これはfake局所適合を無根拠に真正へ昇格したのではなく、**持ち上げの大域存在と、全場所での差を吸収する既知の有理D∞**を使っている。

従って次の列は完全である。

\[
0\longrightarrow\langle\delta_2(D_\infty)\rangle
\longrightarrow\operatorname{Sel}^{(2)}(J/\mathbf Q)
\longrightarrow S_{\rm fake}\longrightarrow0.
\]

ゆえに

\[
\boxed{\dim_{\mathbf F_2}\operatorname{Sel}^{(2)}(J/\mathbf Q)=9.}
\]

旧7有理類はmod2でも独立なので、Gをその生成群とすると

\[
\boxed{\dim\bigl(\operatorname{Sel}^{(2)}(J/\mathbf Q)/\delta_2(G)\bigr)=2.}
\]

κ₁・κ₂の真正Selmer持ち上げがこの商の基底になる。**Selmer類として持ち上がることは、J(Q)の点として実現することではない。** 旧J(Q)[2]=0を用いても、階数は7≤rank J(Q)≤9のままである。一般にdim Sha(J/Q)[2]=9−rank J(Q)であり、今回Shaの値を確定したわけではない。

## 5. Uへ接続する一つの具体的な大域計算

κ_iの真正Selmer持ち上げをs_iとし、Selmer上へ引き戻したCassels–Tate対合を用いる。C₂はP₀を持つので16P₀がQ上の次数g−1の因子であり、標準主偏極の対合は交代的。δ₂(G)は対合の根基に入る。従って上の2次元商上の行列は

\[
\boxed{\begin{pmatrix}0&c\\c&0\end{pmatrix},\qquad
c=\langle s_1,s_2\rangle_{\rm CT}\in\{0,\tfrac12\}.}
\]

持ち上げs_iの二択の差はδ₂(D∞)であり根基に入るので、cはその選択に依存しない。ここでのcは**未計算**である。

c=1/2を認証できれば、対合rank2、Selmer内の根基次元7となる。全MWのKummer像は根基に含まれるのでrank J(Q)≤7。旧下界7と合わせてrank=7、既知Gの有限指数性が従う。すると全MWのQ₁₆₃対数spanは既知7方向に一致し、row361の10本に対して

\[
\boxed{U=\{0\}\subset\mathbf Q_{163}^{10}}
\]

が認証される。row361のω₀*そのものが全MWを消し、a₀=1も正確に維持される。その後に旧row339の同じ元source非零円盤排除補題を適用できる。

一方、c=0ならこの対合による階数改善は得られない。rank=9、rank=7、Sha=0のいずれも自動的には従わず、追加MW類の実現またはさらに深い降下が必要になる。cを1/2と推定してU=0を登録しない。

**次の最初の具体的証明課題：s₁に対する真正4-descent／対応するcoverと局所自明化を構成し、s₂とのCT値cを厳密評価する。** これは同じR3-07のU構成に向けた下位課題である。全MWの有限指数格子を直接構成する経路も引き続き有効。

既存の奇数次数用CT実装を、今回のQ上の偶数次数36モデルへそのまま適用しない。row361の次数35モデルはQ₁₆₃の不分岐6次拡大上の計算chartであり、Q上の奇数次数モデルを与えていない。

## 6. 再演と追加探索

| 項目 | 今回の実行 |
|---|---|
| 新しい全局所適合の正確な検証 | 通常／python -Oとも541検査・7負例PASS |
| 実符号 | 正確なSturmと有理区間Horner。浮動小数不使用 |
| 19単数×全奇数悪素点の因子ごとの指標 | PARI発見計算と別Euclid resultant実装が一致 |
| 親row363の全単数・2進交差 | 精度12で865検査・8負例PASS |
| 親row363の類数1証書 | 24,490検査・5負例PASS |
| 親row361の加法鎖を含む全対数再演 | 1,579検査・11負例PASS |
| 新結果の独立数学監査 | PENDING／未実施 |

検証器はassertによる検査を用いず、最適化実行でも同じ判断を行う。コホモロジー・良還元・CTの標準定理は本稿で証明／適用条件を説明するものであり、541件の有限計算だけでそれらの一般定理を機械証明したとは主張しない。

追加の大域類探索として、2次支持u=aX²+bX+cをa=1..64、|b|,|c|≤1024で走査した。primitive、定数非零、旧線形支持を因子に持たない、判別式非平方の222,522,071組を、24個の小素数によるresultant平方必要条件でふるい、残る120組を正確に検査した。実際の平方根は旧D₂・F₂の2件だけだった。

さらに3次支持u=aX³+eX²+bX+cをa=1..8、|e|,|b|,|c|≤64で、同じprimitive・旧線形支持除外条件の15,704,500組について20素数でふるい、37組が残った。うち既約35組の正確な体内平方検査では新支持0件。小さい別範囲の計3,093組について、C++ふるいと独立のPARI整数resultantの条件が完全一致した。

これら計238,226,571組は**有限探索**であり、曲線やJacobian全体の完全性証明に使わない。新しい独立MW類0件という今回の探索結果だけを記録する。

再演：

```bash
python -m pip install -r requirements.txt
python math/verify_exact_selmer9.py
python -O math/verify_exact_selmer9.py
python verify_manifest.py
```

親の全再演用には同梱`parent_evidence`を展開して、その親の手順を用いる。PARIが必要な親の対数再演と探索にはcypari2==2.2.4を使用した。新局所検証本体はcypari2に依存しない。

## 7. 現行記録と監査境界

R3担当C8:G8、経緯row364、R5 K04/P23、R0唯一ACTIVEを同じ状態に同期する。row355〜361の限定監査PASS、row362の監査PENDINGとrow363の限定監査PASS_SCOPED、旧証明を保持する。新row364を独立監査PASSや正式R0採択へ変更しない。

現行NEXTは「κ₂本を通常のJの2-Selmer局所条件でさらに切る」から、上記の**真正2次元Selmer商のCT一成分c、または追加MW生成格子を認証し、実際のUへ進む**へ具体化する。初期2-descentの局所交差自体は尽きたが、source固有のcover／曲線点条件や高次descentを停止させるものではない。

P23-LOW全域even signed12..154（残余最大36絶対指数／72signed）、全原始標識基底・両有効符号というGOALは維持する。R2のMID/HIGH、S231 formal HOLD、Bwide/E1別境界、Branch B OPEN、正式R0 C35-200も維持する。

### 保存後の確認

正本の更新と再読は64検査でPASS。R0の履歴領域は全文不変、現行ルートとNEXTはそれぞれ一つであり、親row363の受領限定監査PASSと新row364の監査PENDINGを区別して保持した。

| 更新先 | 箇所 |
|---|---|
| [R0研究再開管理正本](https://docs.google.com/document/d/1UKVlpL0CmAEAIpRN_eE63JllyN1RjqbBaGIG2o4UH4Q/edit) | ACTIVE内の5段落を直接置換 |
| [R3索引](https://docs.google.com/spreadsheets/d/17BQc6iakGQ7tdxMAVORnOPGa6KjH0uiaiAbbVMO2kRs/edit) | 担当C8:G8、経緯row364 A:J |
| [R5統合記録](https://docs.google.com/spreadsheets/d/1SLRGqevuQs8RSkhOWhHO67vcpcmC0F304E9ClYB89ag/edit) | 継続管理K04 E6:G6、採否P23 M6 |

## 8. 原典

- 親row363：<https://drive.google.com/file/d/1AvOVaX_dtxl7g2YqHnzV3B_qXzM0E7Bp/view?usp=drivesdk>。全域上側と基底の定義。研究中に受領した限定独立監査PASS_SCOPED：<https://drive.google.com/file/d/1u14bzc6pc482zTxfzgKvw5MPcyggtTWR/view>。
- 旧row352：<https://drive.google.com/file/d/1RP2ZOYouXNKOVTuXvOWmFrJy9NXTDbG7/view>。D∞のKummer類が∂(1)である証明を継承。
- 旧row351：<https://drive.google.com/file/d/1g1eKCb_tyFaesTyqbWAh2tiz7fWpIf7G/view>。真正／fakeコホモロジーの枠組み。
- Poonen–Stoll, *The Cassels–Tate pairing on polarized abelian varieties*, Corollary 4、Theorem 5、§12：<https://math.mit.edu/~poonen/papers/sha.pdf>。Q上の次数g−1因子による交代性と対合の標準理論。
- Stoll, *Selmer groups and descent*：<https://people.maths.bris.ac.uk/~matyd/Trieste2017/Stoll.pdf>。良還元での不分岐局所Kummer、真正／fakeを区別する標準枠組み。
- Shukla, *On computation of the Cassels-Tate pairing*, 2024 thesis／2025 deposit、§4・§7：<https://epub.uni-bayreuth.de/id/eprint/8348/1/thesis.pdf>。奇数次数手法と偶数次数への適用を区別して参照。今回cを計算済みとする根拠には用いない。
