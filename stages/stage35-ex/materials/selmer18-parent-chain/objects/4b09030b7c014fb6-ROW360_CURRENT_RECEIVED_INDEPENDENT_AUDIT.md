# Stage35EX row360 独立数学監査報告書

- 実施日：2026年11月5日
- 監査対象：R3-07 / P23-LOW / row360（固定 signed ±18、種数17の \(C_2\) のみ）
- **監査判定：PASS_SCOPED（限定合格）**
- 数学的新規性：監査済みrow359のMW階数上界14と既知のsource順方向写像から、固定対象の163進円盤内の点数・正の原始標識基底数を数値上界14で制限する従属系。
- 親成果：row359の真正2-Selmer次元≤14、\(7\le\operatorname{rank}J_2(\mathbf Q)\le14<g=17\)。親成果の全証明の再監査ではない。

## 1. 承認した定理

\(C_2:Y^2=h_2(X)\)、\(h_2(0)=1\)、\(\deg h_2=36\)、\(P_0=(0,1)\)、\(p=163\) とする。

\[
D=\{(X,Y)\in C_2(\mathbf Q):X\in163\mathbf Z_{163},\,Y\equiv1\bmod163\}.
\]

固定曲線上の全 \(J_2(\mathbf Q)\) に対する消滅空間を利用して

\[
\#D\le15,\quad \#(D\setminus\{P_0\})\le14,
\]

\[
\#\{(X,Y)\in C_2(\mathbf Q):0\ne X\in163^2\mathbf Z_{163},\,Y\equiv1\bmod163\}\le14
\]

が成立する。旧row339・R1-239の必要方向で同じ円盤に送られる、正の原始標識付き \(A^2+B^2=C^2\) の固定signed ±18 source基底は、両有効符号の**和集合**で高々14個となる。

これは元source不存在の証明ではなく、14個の候補の存在や列挙も意味しない。

## 2. 証拠の取得・再演

- 証拠ZIP: `STAGE35EX_R3_07_ALLMW_P163_DISK_BASECOUNT14_EVIDENCE_20261105.zip`
- ZIP全体のSHA-256: `3351c193b842316d4cb6ca4f70b0b3199dedbece41ec2bd138b3b268ce6c23b4`
- 37エントリ（manifestを除く36ファイル）のSHA-256照合：PASS 36/36
- 通常実行：5,622検査・負例8件 PASS
- `python -O` 実行：5,622検査・負例8件 PASS
- 保存済み正本変更スナップショットの整合性検証：PASS
- 独立SymPyでの \(\gcd(h_2,h_2')\bmod163=1\) とBezout恒等式：PASS
- 独立した有理数漸化式からの \(1/(2\sqrt{h_2})\) の先頭17係数 mod163：
  `[82,152,127,116,23,148,5,74,95,148,78,106,150,40,152,134,124]`（原証書と一致）
- 17×17と15×15のjet三角行列の単元対角・階数17/15：PASS
- 各 \(0\le n\le14\)、\(e=1,2\)、\(m\le99999\) の尾項の付値不等式：PASS。無限部分は別途下記の数学的証明で確認。
- 正の原始基底からの比の復元：5組の厳密対照でPASS。

## 3. 数学監査

全 \(J_2(\mathbf Q)\) を消す \(\mathbf Q_{163}\) 上の微分空間 \(\mathcal A\) は、階数上界14により次元が少なくとも3。係数表示で \(M=\mathcal A\cap\mathbf Z_{163}^{17}\) と置けば、\(\mathcal A\) が体上の線形空間であるため \(M\) は飽和し、\(\dim_{\mathbf F_{163}}(M/163M)\ge3\)。

先頭15係数が消える \(\mathbf F_{163}^{17}\) の部分空間は次元2であり、ある**全MWを消す**積分微分 \(\omega=\sum_{j=0}^{16}a_jX^j\,dX/(2Y)\) の最初の単元係数番号は \(0\le n\le14\) となる。実際の \(n\) や \(a_0\) の単元性はここでは判らない。

\(b(X)=1/(2\sqrt{h_2(X)})\in\mathbf Z_{163}[[X]]\)、\(b(0)=1/2\) は単元。\(c(X)=(\sum a_jX^j)b(X)\) とすると \(c_m\in163\mathbf Z_{163}\)（\(m<n\)）、\(c_n\in\mathbf Z_{163}^{\times}\)。全MWの消滅から円盤内の有理点のColeman積分

\[
F_\omega(X)=\sum_{m\ge0}\frac{c_mX^{m+1}}{m+1}
\]

は0になる。

\(e=1,2\) について \(G_e(Z)=F_\omega(163^eZ)/(163^eZ)\) を考える。\(n\) 項の付値は \(en\)。\(m>n\) なら
\[
v_{163}\Big(\frac{c_m163^{em}}{m+1}\Big)\ge em-v_{163}(m+1)>en.
\]
実際 \(k=v_{163}(m+1)\ge1\) なら \(m\ge163^k-1\) なので \(m-k\ge163^k-1-k\ge161>14\ge n\)。\(k=0\) は自明。従ってStrassmannの最大係数が最後に現れる添字は高々 \(n\le14\)。**先行する \(m<n\) の係数が単元より大きい可能性は排除しておらず、その場合も「最後の最大添字≤n」は変わらない。** 非零有理点は高々14、\(P_0\) を加えて高々15。

元sourceの必要な\(X=(AC/B^2)^2\)は非零の163²倍、\(Y\equiv1\bmod163\)。正の比\(r=A/B,s=C/B\)は \(s^2-r^2=1,\ r^2s^2=X\) から一意に復元でき、原始正標識を固定すれば整数基底も一意。両有効符号の基底和集合が高々14個となる。

## 4. 成立条件と未解決事項

今回認めるのは**既存親成果の正しい範囲での従属数値上界**であり、新しい一般的Strassmann定理ではない。親row339とR1-239に依存するsource順方向対応を逆同値に拡張していない。

未証明：
- 具体的な全MWを消す163進微分とその誤差保証
- \(a_0\in\mathbf Z_{163}^{\times}\) を満たす消滅微分の存在
- 既知7つのMW類が有限指数部分群を生成すること
- 候補点の座標一覧、明示的な高さ上界、元signed ±18のsource不存在
- P23-LOW全体、Branch Bの閉鎖

新しいMW点は0、元source排除0。前回row355〜359の各PASS_SCOPEDは維持。正式R0 C35-200は変更しない。

## 5. 現行NEXT

**R3-07 / P23-LOWを継続する。** 固定 \(C_2\) で全MWの163進対数像を含む認証済み上側、または全MWを直接消す具体微分を構成する。有限指数性や追加の真正MW類が必要なら証明し、p進精度・係数格子飽和を監査する。その上で \(a_0\) の単元性を立証し、元sourceが入る非零163²円盤を排除する。

階数＜種数という入口、旧S付値14方向の構成、既知15単数の反復は再研究しない。固定±18だけをP23-LOW全体の完成とみなさない。

## 6. 原典・正本

- [row360原典](https://drive.google.com/file/d/1P0FB4LbFqFp7kx88i04NzAehKi-g8eXW/view?usp=drivesdk)
- [row360証拠フォルダ](https://drive.google.com/drive/folders/1yedr8zg5sTAukE9q29cnrTU3wTsuySjm)
- [P0/P2監査正本](https://docs.google.com/document/d/14TkdbXFBBtJmaJhFeSeEfOhx2G-DsTJTtoj9GSQKdHo/edit)
- [R0現行研究正本](https://docs.google.com/document/d/1UKVlpL0CmAEAIpRN_eE63JllyN1RjqbBaGIG2o4UH4Q/edit)
- [R3研究索引](https://docs.google.com/spreadsheets/d/17BQc6iakGQ7tdxMAVORnOPGa6KjH0uiaiAbbVMO2kRs/edit)
- [R5共同攻略索引](https://docs.google.com/spreadsheets/d/1SLRGqevuQs8RSkhOWhHO67vcpcmC0F304E9ClYB89ag/edit)

保存後再読検証：監査正本4項目、R0 ACTIVE5項目、R3現行8セル、R5現行3セルを確認。研究ルートR3-07とR2-01の分担は維持。
