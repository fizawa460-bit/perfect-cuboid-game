# Stage35EX 独立数学監査｜row359

- 実施日：2026-11-05（JST）
- 対象：R3-07 / P23-LOW / 固定signed ±18・種数17の曲線 C₂
- 判定：**PASS_SCOPED（限定合格）**
- 研究提出原典：[row359 主証明](https://drive.google.com/file/d/1CXLvx5rApWdr8hyzsx5YjL2Vl3T2BG6Y/view)
- 原証拠：[Google Drive ZIP](https://drive.google.com/file/d/1VTkt7pkdzPrtUMAAkogGGXl3Zi6bpVVd/view)

## A. 証拠監査

- 証拠ZIP SHA-256：`a6022eb5e0e4c89a5f760c326cd72e37b49777efb18565538681cf3b842b2cf6`
- 42/42ファイルのSHA-256 manifest：PASS。
- `python math/verify_three_new_units.py`：248検査・10負例 PASS。
- `python -O math/verify_three_new_units.py`：248検査・10負例 PASS。
- `python math/verify_three_new_units.py --precision=10`：248検査・10負例 PASS。
- 2進精度10/12の主要平方類・障害値一致を確認。
- 別実装による独立計算：原検証器をimportせずSymPy整数多項式/resultant・二項係数整数比較・GF(2)消去を実施。

## B. 数学的検証

1. **同じK内のVの同定。** 旧定義 V=N(θ)/D(θ) に対し N⁴−θD⁴≡0 (mod h₂)、61進θ≡47・V≡32で `V²B+A=0` を選び、F(X)F(−X)=A(X⁴)+X²B(X⁴)、F(32)=0/F(−32)≠0からF(V)=0。V∈Kとθ=V⁴によりQ(V)=K、deg F=36。旧row349の親範囲を継承する。
2. **整数基底と単数性。** F(1)=4096=2¹²、2上の(e,f)=(3,4),(3,8)とV≡1の剰余情報を用いると、w=V−1の二素点での付値はいずれも1。従って b_j=w^j/2^⌊j/3⌋ は整数。明示Q_i(V)/d_iをb_jへ変換した各36係数の整除性108件を独立確認した。
3. **ノルム。** 独立SymPy計算の厳密なresultant `Res(F,Q_i)/d_i^36` が順に **+1, −1, +1**。3元とも通常の全球単数である。元証書のSylvester/Bareiss計算・36×36乗法行列式との整合も確認した。
4. **局所条件と追加独立性。** 旧row355の38単数平方類座標/19障害線形式は親監査済みインターフェースとして継承。新3元の障害値は `0x7300, 0x410c6, 0x0a8e1`、旧12単数の障害rank6を**rank9**にする（独立GF(2)再計算）。既知Γ₁の単なる再表現ではない。
5. **norm・実局所条件に適合する7証人。** 既存w₁…w₄に、ν₁γ₈、ν₂ε、ν₃を追加。旧実符号・normと整合し、すべて有限付値0、norm平方・実局所条件に適合。2進障害7×7小行列（行0,1,2,4,5,6,10）の整数行列式 **−1** を別計算で確認。従って全域の適合候補空間V₀上でrank≥7。
6. **上界。** 独立PASS_SCOPED済みrow358の有限偶付値空間はdim Ebar=19+c_K、norm・実条件2本の後dim V₀≤17+c_K。今回7本を引きfake Selmer≤10+c_K。row351/352の真正→fake比較の核≤1を**一度だけ**加えて真正≤11+c_K≤14。c_K≤3は通常類群でありc_Sと混同しない。

\[
\dim_{\mathbf F_2}\operatorname{Sel}_{\rm fake}\le10+c_K\le13,
\quad\dim_{\mathbf F_2}\operatorname{Sel}^{(2)}(J_2/\mathbf Q)\le11+c_K\le14,
\quad7\le\operatorname{rank}J_2(\mathbf Q)\le14<17=g.
\]

## C. 新規性・継承範囲

**新規限定成果**：明示全球単数3方向、障害rank6→9、norm・実適合証人rank4→7、および従来17から14への真正2-Selmer数値上界強化。

**新規計上しない**：既存VとV⁴=θ、旧12単数、既存4証人、局所Kummer全生成、最大整環、古典LLL、全有限偶付値還元、通常c_K≤3、旧MW下界7。row355〜358の限定監査合格は各元scopeに限って継承する。

## D. 未解決と現行NEXT

- 上界14<種数17により、全MWログに対する163進消滅微分の**存在次元**は少なくとも3。ただし具体的な全MW消滅微分は未構成。
- 既知7 MW類の有限指数性は未証明。単数部分群自由rank15はMW階数ではない。
- 積分的a₀単元、signed ±18の元source非零円盤X=(AC/B²)²∈163²Z₁₆₃\{0},Y≡1の矛盾は未証明。元source排除：**0件**。
- P23-LOWの残余even signed12..154（全原始標識付き基底・両有効符号）、R2-01 MID/HIGH、Branch BはOPEN。
- R0正式C35-200、S231正式HOLD、B_wide/E1との区別は不変。
- **唯一の現行NEXT**：固定±18で全MWに有効な163進ログ上側または具体的消滅微分を認証し、積分a₀単元および同じ元source非零円盤排除へ接続。必要なら新真正MW類、有限指数証明、または残る通常単数4＋通常類群由来≤3方向の安全な全域被覆を行う。
- 旧「追加1本の独立制約あるいはc_K≤2を証明して≤16へ」という必須ゲートは今回で**失効**。既知15単数の同じrank9/kernel6再計算はSTOP。

## E. 監査記録の更新

P0/P2既存現行監査4項目、R0現行管理5項目、R3研究ルート・row359計7セル、R5研究系列とP23採否計4セルを差分更新。歴史本文と既存親監査は保持。所有ルート・P23分担・正式R0採否は変更しない。保存後の読み直しで監査状態・次の研究障壁・ルート固定を照合する。

**判定境界**：PASS_SCOPEDは証拠付きの当該数学命題に限る。すべての親定理を今回再形式化したものではなく、完全直方体問題や元sourceの解決宣言ではない。
