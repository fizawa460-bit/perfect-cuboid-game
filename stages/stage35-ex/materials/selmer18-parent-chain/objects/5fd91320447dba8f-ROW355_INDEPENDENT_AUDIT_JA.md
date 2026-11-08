# Stage35EX stage35exaudit — R3-07 row355 独立数学監査結果

監査日：2026-11-04。対象：固定 signed ±18、種数17の超楕円曲線 \(C_2:Y^2=h_2(X)\)。

## 総合判定：PASS_SCOPED（固定 \(C_2/\mathbb Q_2\) の局所生成命題に限る）

**認証範囲：** 旧6個の \(\mathbb Q\)-有理除数、新3個の不分岐 \(\mathbb Q_2\)-局所trace除数、新9個のtame \(e=3\) 局所trace除数、旧 \(D_\infty\) が \(J_2(\mathbb Q_2)/2J_2(\mathbb Q_2)\) を生成する。独立なfake方向18と局所で非零な真正核1方向の合計19方向であり、\(\dim_{\mathbb F_2}J_2(\mathbb Q_2)/2J_2(\mathbb Q_2)=19\) に一致。

**除外：** 全球Selmer上界≤16、classgroup 2部分 \(c_S\)、全球座標上の局所制約の独立rank、MW rank≤16、163進全MW Coleman消滅微分、original signed ±18 source排除、P23-LOW/Branch B終了、R0正式昇格は一切認証しない。新しい \(\mathbb Q\)-有理MW点の認証0、source排除0。判定は一般的な2-descent理論の新規性にも及ばない。

## 1. 対象同一性と保存状態

- 原本主証明 `STAGE35EX_R3_07_DYADIC_FULL_KUMMER_20261104.md` SHA-256:
  `b5f1e7a35902bcaa9e1f6d9628c0c9f47d066925fb77744ca8e25aee0359510c`、依頼書と**一致**。
- 元の運用証拠込みZIP SHA-256:
  `25faeb445b8f1911d7af0adbf550cbdee6452cc63373bc2e02ee440f2c47efbe`、依頼書と**一致**。
- 監査ZIP `STAGE35EX_R3_07_ROW355_AUDIT_PACKAGE_20261104.zip` SHA-256:
  `0a2c481ef9b560c91f9ce005c22819184de78fa3410a39a53c5df4aaccd15991`。
- 監査ZIPに61エントリ。`verify_bundle_integrity.py` が自己リスト以外60ファイルすべてのSHA一致を返した。ハッシュ一致だけで数学の正しさを認証しない。
- 親row342/345/352の資料、旧証書、旧検証器を同梱から確認。主証明と証書の \(h_2\) 係数が一致。
- 接続済みGoogle Driveの `R3-研究経緯!A355:J355` および `R3-研究ルート!B8:G8` を実読。両方とも row355 局所成果を「内部PASS、独立監査PENDING」、P23-LOWとBranch BをOPENとしていた。**今回、原本・既存台帳・R0は編集していない**。

## 2. 独立再演

監査ZIPを新規ディレクトリに展開して以下を実行（Python 3、NumPy、Linux）。いずれも終了コード0。

```bash
python3 verify_bundle_integrity.py
python3 verify_dyadic_full_generators.py auditor-normal.json
python3 -O verify_dyadic_full_generators.py auditor-optimized.json
```

通常・最適化ともに **1769 positive checks / 20 negative controls**、単数座標38、Frobenius平方rank24、mod4補正rank12、mod8 Artin–Schreier rank34、`rank(scalar -1, 18 images)=19`、fake18、true19、単数線形制約rank19、norm制約rank2を再現。証書の `global_independent_codimension_computed=false`, `global_Selmer_bound16=false` を確認。

親検証器 `verify_signed18_c2_true_local_kummer_stdlib.py`、`verify_row352_infinity_kernel_rank7_stdlib.py --full-parent` の実行も終了0。後者からrow342の旧6除数とrow351のtrue/fake bridgeまで再演。

**監査者が新作した別検査** `AUDITOR_INDEPENDENT_CHECKS.py`：

1. 旧row342の6個の \(G(\theta)\) から、保存済み `unit_basis_mod256` と38平方類文字を再生成。特に \(D_{1b}\): \(3t-2u^2=(u/2)^2(1+3\theta)\)、 \(F_2\): \(1+6\theta+\theta^2=4u^2(t-u)/t\) を厳密恒等式として確認。前者・後者の平方元とscalarの商を誤用していない。
2. 作者側の `rank` を使用せず独立の純Python GF(2)消去で19本のrank=19を確認。
3. 局所Galoisの慣性3点ブロック12個とFrobenius 4-cycle/8-cycleから、後述の真核の局所非零性を**独立に全4096ブロック集合で検証**。
4. \(F(z)\) のmod8平方恒等式とtame f=1,2,3で \(R(w)R'(w)\ne0\) を別判定。

この別検査と元の再演結果が一致。ただし「作者のコードと別検査の一致」は、外部形式検証そのものではない。

## 3. 命題別の判定

| 論点 | 判定 | 数学的根拠・確認結果 |
|---|---|---|
| 固定曲線・親との接続 | PASS_SCOPED | 係数・SHA・\(h_2(2u-3)=2^{36}F(u)\)一致、旧6除数とD∞親再演成功。 |
| 最大整環、e/f | PASS_SCOPED | \(F\)の単一傾斜\(-1/3\)、平方free residual \(R=q_4q_8\) と親の判別式・整数基底一致。 \(O/(u)=\mathbb F_{16}\times\mathbb F_{256}\) と \(O/2\) の非同一性を保持。 |
| 不分岐3局所点 | PASS_SCOPED | \(F(z)\equiv(z^{18}+2z^{15}+2z^{16})^2\pmod8\)。単数近似根の誤差 \(v_2\ge3>2v_2(2s)=2\) なので真のHensel平方根。 |
| tame 9局所点 | PASS_SCOPED | \(\pi^3=2w\) はEisenstein、特にf=1では \(w=-1\)、\(\pi^3=-2\)。 \(G=F(\pi Z)/2^{12}\) は整、\(\bar G=R(wZ^3)\)、\(\bar G'(1)=wR'(w)\ne0\) を確認。Henselによって指定 \(Y_0\) に真の \(\zeta\equiv1\pmod\pi\) が一意。局所点のtraceはQ₂有理次数0除数。 |
| norm・(x−θ)像 | PASS_SCOPED | traceに対するnorm多項式 \(g_E(u)\)、正規化 \(g_E(u)/2^f\) と \(\bar a_E=m(t)\) の整単数性を確認。前述の旧G再計算も通過。局所点を全球MW点とは数えない。 |
| 精度・整数演算 | PASS_SCOPED | tame初期精度 \(2^{f+9}\)、\(\pi\)除算の1ビット減と \(2^f\)除去後に \(2^8\) を保持。int64安全上界チェック、整数Bareiss determinant/有理係数補間を実行。 |
| 単数38座標・scalar | PASS_SCOPED | \(U_1/U_2,U_3/U_4,U_5/U_6\)の各12方向と \(U_6/U_7\) の2 trace方向、\(U_7\) は平方。\(5\)は両偶数剰余次数で平方、\(-1\)は非平方、\(2\)はunitでない。引くscalarは1方向。 |
| fake18 | PASS_SCOPED | 旧6+新12と−1の19本の純GF(2) rank19。したがってscalarで商を取ったfake像は18。 |
| 真正核1・真正19 | PASS_SCOPED | 下記の独立した偶数部分集合・connecting cocycle議論でD∞の局所非零性を確認。旧row345のdim19と一致して19類が全空間を生成。 |
| 局所制約・全球への接続 | PASS_SCOPED（局所のみ） | 38unit座標中19形式、norm2形式を包含。norm後の単数余次元17＋付値偶奇1＝局所余次元18。**全球候補空間の独立制約rankは未計算**。 |

### 真正核を文献引用に頼りきらず検査した根拠

36個の分岐根の有限Galois集合を \(B\) とすると、標準的なhyperelliptic 2-torsion表現は
\[
J_2[2]=\ker\left(M\xrightarrow{\rm parity}\mathbb F_2\right),\quad M=\mathbb F_2^B/\langle{\bf1}\rangle.
\]
36は偶数なのでparity写像は商で定義できる。したがって完全列 \(0\to J_2[2]\to M\to\mathbb F_2\to0\) を得る。各分岐点 \(W_i\) は \(2[W_i-I_-]=[I_+-I_-]=D_\infty\) を満たすので、\(\kappa_2(D_\infty)=\partial(1)\)。この类は \(H^1(M)\) に写すと0で、fake像0となる。

\(\partial(1)\ne0\) は \(M^{G_{\mathbb Q_2}}\) 内の奇parity不変類が無いことと同値。慣性は位数3であり、\(M\) で補集合との交換（位数2）を起こせない。ゆえ不変集合は12個の3点ブロックの和。Frobeniusは4ブロック周期と8ブロック周期を動かす。Frobeniusが集合を保つ場合、選ぶブロックは0/4＋0/8個で偶数。補集合に写す場合、2＋4=6個で偶数。どちらも元の根の個数は3×偶数で偶数。よって奇parityの不変 \(M\) 類はなく、\(\partial(1)\) は**非零**。これが局所の真正kernel1方向。

同じ全4096ブロック集合の列挙で、Frobenius固定が4パターン、補集合交換が4パターン、\({\bf1}\) で商を取ると4類、すなわち \(\dim J_2(\mathbb Q_2)[2]=2\)。一般の2進Abelian varietyの局所群構造より \(\dim J_2(\mathbb Q_2)/2=17+2=19\)。18本のfake独立類にD∞を加えると19独立類、ゆえ全生成。

**注意する証明文の改善点：** `すべての分岐軌道次数12/24が偶数だから核は非零` という短縮表現**単独**では、一般にはFrobeniusの補集合交換を見落とす。上記の慣性・4/8巡回周期・anti-invariantの偶数性をrow355証明または証書の根拠欄へ明記すること。これは今回の具体例で反例が出たという意味ではない。

## 4. 留保・外部資料の照合範囲

- Poonen–Schaefer著者版PDFの実物とTheorem 11.3の**定理番号・本文の逐語照合は、外部Webアクセスが利用できず未実施**。その箇所の局所的な数学的帰結は上記の具体的な完全列・半分点・Galois作用に基づく直接検証で置換した。文献書誌監査は別の未完項目として残す。本文が直接証明より強い一般命題を引用している場合、その一般化は今回のPASS対象外。
- 旧row342, row344, row345, row352の算術入力はSHA付き親証書と親再演・具体的な局所議論で照合した。全旧研究系列を初期から独立に再証明したという主張はしない。
- 元の`verify_dyadic_full_generators.py`では旧6類について保存済みunit値と文字の検算に留まる。今回、監査側の別検査でrow342の元の \(G(\theta)\) から再計算して補った。以後の内部検証器にも同じ入力直結検査を実装すると監査可能性が上がる。
- 監査の数学的判定は **固定曲線の局所結果に限る**。具体的な全球cohomology条件、\(c_S\)、S類群等の解析は一切通過とみなさない。

## 5. 新規性・判定・更新提案

- **新たな研究成果：0。** 既存row355主張の独立監査であって、旧証明の再登録は行わない。独立監査の検証結果として、局所生成命題を `PASS_SCOPED` として採用可能。
- `R3-研究経緯` row355の監査状態について、**原本を変更せず** `INDEPENDENT_MATH_AUDIT=PASS_SCOPED (2026-11-04; audit record ...); fixed C2 Q2 local result only` とする更新を提案。再現ログと本報告を証拠参照に加える。
- `R3-研究ルート!B8:G8`では局所生成完了の記録を維持し、「独立監査PENDING」をPASS_SCOPEDに置換する提案。ただし旧NEXT「局所Q₂生成系を構成」を復活させない。
- R0 ACTIVEには研究ゴールや正式判定の変更は不要。`P23-LOW OPEN`, `Branch B OPEN`, `S231 formal HOLD`, `C35-200 unchanged` を維持。
- R5統合記録には、本件が**局所限定監査PASS**であり全球Selmer・元sourceの進捗0である旨のみ追加候補。未確認の別ルートと混ぜない。
- **現行NEXT：** 認証済み全球上側空間（\(c_S\) と未知方向を含む）を用意し、局所2進・奇5・実の共通座標上の実際の制約rankを認証する。必要なら真Selmer≤16から全MWの163進消滅微分とsource円盤を別途証明。局所余次元18を全球の18独立制約へ転用しない。

この監査報告と追加スクリプトは**原本とは別ファイル**。原本主証明、主証書、row355、R0は編集していない。
