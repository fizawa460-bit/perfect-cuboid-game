stage32audit — F64 範囲限定監査  
2026-10-29 JST / MB104 / Route F

判定  
F64の固定複素モデル内の数学は条件付きPASS。F64凍結ZIPのSHA256照合・通常/最適化再生・F63再生・20負検査の独立実行はPASS。原典F12〜14/C16/Hから実担体へのadapterはHOLD。種数1特殊locus、実marked conductor、coreless/no-clumpは未解決。実候補排除0、一様m上限なし、MB104 OPEN、公式credit0。MAIN昇格・merge許可・実候補排除ではない。

監査範囲と凍結入力  
F64研究正本: https\://docs.google.com/document/d/1fPS0VuKpkawH7btMpvwSdjIIamSp7stNxAFtBYq969k/edit  
F64再現ZIP: https\://drive.google.com/file/d/1Y3LP6INjA-flr-Yp9mcY1xUXJWcHjnYq/view  
ZIP SHA256: 6f85a0e25e8cc715d40230a1a2683299686e53c457261b292b84ddd34247fe8e  
18ファイル。F63同梱ZIP SHA256: c84db83eced17f31fa8467c7c0f9a6bbab652ea569e5e94f0ea2bff7b899cd7c  
監査は保存された凍結パッケージと研究本文のモデル条件に限定。現行GitHub HEADやF12〜14/C16/H原典の完全なsource adapterの独立照合ではない。

検算の実行結果  
python verify\_f64.py: PASS。  
python \-O verify\_f64.py: PASS。  
python verify\_f64.py \--replay-f63: PASS（内部でF63通常・最適化両モード）。  
python negative\_tests.py: PASS（10種類×2モード=20、全拒否、入力不変）。  
64 H節点のうちκ0零32点を28支持＋欠落4に分離。欠落4でF63二証人の一方の非零を再計算。κ0^4 H0(3K\_Y)の108基底について224行×108=24192の有限体jet恒等式を検算。4アフィン/無限遠チャート、交点行列8×8、二点三次jet22×22単位行列・det=1、種数・節点数式の再生PASS。  
負検査は偽種数1存在、偽種数、節点数倍増、交点行列改変、chart欠落、三次monomial改変、同梱F63のバイト改変＋依存ハッシュ差替、F63欠損、偽theorem\_credit、依存ハッシュ表空化。各通常/-Oで拒否を確認した。F61/F62原版のassert問題をF64へ無条件に転嫁しない。

基点自由性の数学監査  
Y=(C8×C8)/H\_diag、S\_Y→Y最小解消、H\_Y=K\_S、指定28例外E\_j、M=7H\_Y−4Σ28E\_j、dim H0(M)=242をF63の条件付き入力とする。  
κ0=(r\_z²−2i)(r\_w²−2)ω\_zω\_w。保持4本の楕円半ファイバーQと欠落4例外Fに対して、div κ0 \=2Σ4Q+Σ28E+Σ4Fという解消上の分解からD0=H\_Y−Σ28E=2Σ4Q+Σ4Fは有効。M=3H\_Y+4D0。  
4本Qは各Q²=−4、異方4組の交点1、4欠落例外F²=−2、各対応Q·F=1。D0²=−24、H\_Y·D0=32、M²=672、H\_Y·M=224、各D0構成成分にM·Q=M·F=0を照合。  
H\_Yが基点自由なのでσ0^4 H0(3H\_Y)はD0外の基点を消す。D0上ではF63の切断Fが欠落4節点で非零、例外Fと4楕円QのM次数0、各Qが対応Fと交わることによりFが全D0成分で非零。したがってMは基点自由。W\_m=im Sym^m H0(M)も非零sectionのm乗により全mで基点自由。  
注意: κ0の無限遠零因子・節点消失・F63の標数0への持上げは研究本文の局所モデルとF63監査条件を入力。今回の有限体再生だけでこれら全幾何学命題の形式証明を得たわけではない。

埋込みと二点jetの数学監査  
Y上K\_Yの11基底（r\_z^j r\_w^k（0≤j,k≤2）9本、U'=u\_z u\_w、V'=v\_z v\_w）を用い、4つの基底チャートでr\_z/1/r\_z、r\_w/1/r\_w、U'/frame、V'/frameが復元可能。H\_diag不変の被覆座標環はこれらで生成されるので、固定Yのcanonical mapは閉埋込み。この点は一般型曲面一般のvery amplenessを無条件に仮定したものではない。  
埋込みY⊂P10に対し、P10の相異なる2点の値・一次jetを三次式22本が分離する明示的行列を検証。滑らかなYの2点では各点長3、合計長6の一次jet分離が3K\_Yで得られる。D0外・τ固定16点外のx,τxは独立2点であり、σ0^4H0(3H\_Y)からUの二点一次jet全射を得る。W\_mもa^(m−1)Uの部分系で同様。  
固定xでs(x)=s(τx)=0は2独立条件、d s\_xとd(τs)\_xが従属する条件はさらに余次元1。悪い切断の固定x余次元3に対しxの移動は2次元なので、一般切断ではΩ上交差横断。支持例外上はF63 norm接線錐squarefree・互いに素、非支持例外・D0・τ固定点は一般切断が避ける。この範囲では全交点は滑らかな自由τ軌道上で単純。  
この推論は代数幾何のBertini/二点jet次元議論でありverify\_f64.pyの出力だけから機械的に証明された命題ではない。

一般曲線の種数・節点数  
基点自由＋F63像次元2、標数0Bertiniを用いると一般strict D\_m∈W\_mは滑らかな整曲線で、同時に14支持の局所条件・τ非不変・34点回避を保てる。随伴公式よりg(D\_m)=1+(672m²+224m)/2=336m²+112m+1。  
D\_m·τD\_m=672m²、全部自由τ二点軌道をなす横断交点なので、X側B\_m=q(D\_m)のstrict支持外のordinary nodeは336m²個。q\|D\_mは有限双有理で、正規化種数はg(D\_m)。X側strict p\_a=672m²+112m+1とも一致。m=1ではg=449、ordinary node=336、strict p\_a=785。672m²をそのまま節点数にしたり、14支持A1の収縮δをこの336m²へ加えたりしない。

未解決と次の作業  
一般D\_mが滑らかなことは、特殊な種数1の存在・不存在を示さない。種数1なら半次数strict D\_m自身にδ=336m²+112m（m=1で448）が必要。全δ条件の独立性は未証明。F42のmarked conductorに実sourceの位置を同定できず、coreless/no-clumpもHOLD。任意に選んだモデルBのnorm成立を実source-fixed BのPASSとして流用しない。  
NEXT: F65以降では半次数strict D\_mの高δ特異化、種数1特殊locus、実marked conductor/corelessの同時制約が優先。一般元計算の反復だけで一様m排除を主張しない。候補排除0、MB104 OPEN、credit0維持。F53循環訂正も維持。

参照  
F63監査: https\://docs.google.com/document/d/1GpajcDb4\_Uh-bj4gRCDsudPMLcw7PN1CJhO\_rcG4zgU/edit  
F64研究記録: https\://docs.google.com/document/d/1fPS0VuKpkawH7btMpvwSdjIIamSp7stNxAFtBYq969k/edit  
研究台帳: https\://docs.google.com/document/d/10QAZSl5Qjic\_gnsGzpRtNaD1TmG7JNZlau7gzQTu3vs/edit

分類: SOURCE\_CONDITIONAL\_COMPLEX\_MODEL\_MATH / F64\_SCOPE\_AUDIT\_CONDITIONAL\_PASS / VERIFIER\_NEGATIVE\_20\_PASS / ZERO\_CREDIT  
