stage32audit — F65 範囲限定監査  
2026-10-29 JST / MB104 / Route F

【判定】  
固定複素モデル内の数学：条件付きPASS。  
F65再現用18ファイルの凍結ZIP SHA-256一致、通常・python \-O再生PASS、同梱F64通常・-O再生PASS、10種類×2モードの負検査20/20で拒否PASS。これらは凍結検算と本文の条件付き幾何学的演繹についての範囲限定判定であり、F12〜14/C16/H原典から実担体へのadapter、実source-fixed C/R\_off、実marked conductor、coreless/no-clump、種数1実在・不存在の証明に拡張しない。実候補排除0、一様m上限なし、MB104 OPEN、公式credit0。MAIN昇格・GitHub mergeは未許可。

【対象資料・同一性】  
F65研究正本: https\://docs.google.com/document/d/10q1uHgTxIV-UqE-Czy5wY-7vrK1UHEbH4PUycOW1GfQ/edit  
凍結ZIP: https\://drive.google.com/file/d/1tq3JzlgK4nsgiTIWOGBXX0DH4skJ-xlp/view  
ZIP SHA-256: d52bf5d0adf5b150d3371a98d59a1b8d59901f2cfb46e53c6a1ea3dcefb529ae  
ZIP内18ファイル。F64凍結ZIP: 6f85a0e25e8cc715d40230a1a2683299686e53c457261b292b84ddd34247fe8e。先行するF64固定モデル内の範囲限定監査の条件付きPASSを依存入力にする。

【実行した再現・負検査】  
python3 verify\_f65.py → PASS  
python3 \-O verify\_f65.py → PASS  
python3 verify\_f65.py \--replay-f64 → PASS（内包F64を通常・最適化で再生）  
python3 negative\_tests.py → PASS（20/20拒否、元入力維持）  
検算器はF64ハッシュ、欠落4点のF・τF・even切断非零、YからXへのnull交点行列の商、任意k≥1の消滅に必要な次数不等式、厚化χ再帰、全mの多項式恒等式およびnorm余次元・gluing rankを検査。原証明のBertini/消滅定理/変形論そのものの機械証明ではない。

【数学的監査1：null因子とH¹安定性】  
Y側M=7H\_Y−4Σ28E、X側P=7H\_X−4Σ14E。F64のD\_Y=H\_Y−Σ28E、X側D\_X=H\_X−Σ14E、M=3H\_Y+4D\_Y、P=3H\_X+4D\_Xを用いる。F64の非零切断がD\_Y全体を避け、F63のeven部分がX側欠落例外と楕円Q上で非零という入力から、任意n≥1の形式厚化nD上でmM,mPを自明化できる。「次数0だから厚化でも自明」という誤推論ではない。  
D=2ΣQ+ΣF=R+A。XのQ2本・F2本とYのQ4本・F4本の交点行列からD.Q=−3、D.F=0、R.Q=R.F=−1。k≥1のO\_D(−kD)を右O\_R(−kD)と左O\_A(−R−kD)へ分解。楕円Q上の次数は右3k、左1+3k。Q同士の接合2点を引いた残次数は3k−2\>0、3k−1\>0。付随するP¹葉Fの値は定数切断で合わせられるため、両側H¹=0、よってH¹(D,O\_D(−kD))=0。厚化の短完全列でH¹(O\_nD)はH¹(O\_D)に安定。  
ここは局所配置と正規交叉の仮定が必要であり、検算器にある行列と不等式だけの無条件証明ではない。凍結モデル・F64入力下の演繹として整合。

【数学的監査2：Riemann–Rochと全m切断次元】  
3mH=K+(3m−1)H、H=Kは固定モデル内でbig nef。標数0Kawamata–ViehwegによりH¹,H²(3mH)=0。0→O(3mH)→O(mL)→O\_(4mD)(mL)→0、厚化上の自明化からH¹(mL)=H¹(O\_D)。H²(mL)=0はH·(K−mL)\<0とSerre双対から従う。  
χ(O\_Y)=12、χ(O\_X)=8、m1基底入力h0(M)=242、h0(P)=124よりh1\_Y=6、h1\_X=4。RRから  
h0\_Y(mM)=336m²−112m+18  
h0\_X(mP)=168m²−56m+12  
odd部=168m²−56m+6。  
m1に242/124/118を再現。nD切断次元はYで12n²−16n+6、Xで6n²−8n+4。h1を勝手に0と置かずに扱っている。

【数学的監査3：F37導手降下の正確な余次元】  
仮定された実source-compatible C∈\|2mP\|の正規化Eが種数1で、ν\*O\_C(mP)が次数672m²の線束ならh0(E,L)=672m²。F37の曲面からCへの切断同型と正規化降下を仮定する。降下核次元はh0\_X(mP)なので、  
rank\_glue=672m²−h0\_X(mP)=504m²+56m−12（m1:548）。  
gluing quotientの総長δ(C)=672m²+112mなので評価cokernel=168m²+56m+12。実際のR\_offや局所ringを入力した評価ではないためNOT\_EVALUATED、候補排除なし。

【数学的監査4：均等norm像】  
V\_m=H0\_Y(mM)、二次norm \[s\]↦\[sτs\]は射影空間P(V\_m)から\|2mP\|への全域射。F64の一般整D≠τDについて同normの別切断の零因子はDかτDのいずれかで、一般fiberは2点。従って像dim=h0\_Y(mM)−1=336m²−112m+17、target dim=h0\_X(2mP)−1=672m²−112m+11。余次元336m²−6（m1:330）は整合。F56の支持未指定norm像と異なる対象なので余次元を同一視しない。  
一般fiberの数2はF64の整性・非不変性を使う幾何学的推論で、ハッシュ検査や多項式恒等式だけから導いたものではない。

【数学的監査5：種数1の孤立性と節点平滑化】  
種数1の固定m孤立性は既存Route C/F08の再利用でありF65の新しい候補排除成果として認定しない。正規化Eが種数1の仮想D∈\|mM\|なら、conductorを介する双対から対応次数−224m、h0=0、h1=224mを得る。特にδ=336m²+112m個のordinary nodeのみという追加仮定があれば、局所平滑化評価のsourceはh0\_Y(mM)−1=336m²−112m+17、kernel0、cokernel224m−17（m1:207）。長完全列でh1(O\_D(D))=h1(mM)+p\_g(Y)=6+11=17も整合。種数1のnodal曲線の実在やすべての特殊曲線のnodal性を証明していない。

【残る境界・引継ぎ】  
種数1を実現する半次数strict Dのδ=336m²+112mを課した特殊locusと、実marked conductor/coreless/no-clumpを満たすsource bridgeが最大未解決。m1の548（gluing rank）、330（norm像余次元）、207（仮想nodal平滑化cokernel）を独立条件として加算しない。負の期待次元から空集合とは結論しない。  
NEXT: 実C/R\_offの枝付き位置と局所環を取得して降下評価を実施するか、種数1特殊locusとcorelessを結ぶ新たな独立制約の数学的証明を優先。F48/F49の固定B判定とF53循環訂正は維持。原典adapter HOLD、実候補排除0、MB104 OPEN、credit0。  
GitHub/STATE/A–E未変更。この報告は既存Route Fの監査記録として保存し、研究台帳F65の「独立監査前」を対象範囲限定PASSへ更新する。

【参照】  
F64監査 https\://docs.google.com/document/d/1O2JToNo\_shsteuKoyXkBpXSxSvFt5oxDUb8behDrLQA/edit  
既存C孤立性監査 https\://docs.google.com/document/d/1\_mdXU3y6HkUMmCY0APH9IeJXEyATj4d\_nUx-fwF7fgk/edit  
研究台帳 https\://docs.google.com/document/d/10QAZSl5Qjic\_gnsGzpRtNaD1TmG7JNZlau7gzQTu3vs/edit  
分類: SOURCE\_CONDITIONAL\_COMPLEX\_MODEL\_MATH / F65\_SCOPE\_AUDIT\_CONDITIONAL\_PASS / VERIFIER\_NEGATIVE\_20\_PASS / ZERO\_CREDIT  
