# Stage37 — CARD-INDEX全件ルート監査（authority 155）
この文書は研究方針の比較監査であり、新しい数学的閉鎖カード156ではない。数学的current authorityはM3-T11-155、PRIMARY_GATE=OPEN、GLOBAL_COUNTING_CREDIT=0を維持する。

## 結論
既存ルートは多数あるが、閉鎖保証付きの次の一手は確認できない。推奨する再検討順は (1) cross-gcdの同一測度tail、(2) 固定有限素数集合によるM3相対収縮、(3) 既存Gaussian解析adapterの主平方類・physical coefficient評価。これは成功確率の順位ではなく、次の未解決命題を特定し、既存成果に接続できる具体性の順位である。1を解いても全体は閉じない。2は全体に直接届くが、分布定理そのものが未証明。

## 閲覧範囲と限界
CARD-INDEX「カード一覧」A1:L450を取得し、データ383行（382種類のID）を確認。M3-T11-042は異なる二つの主張として2行あり、削除・統合していない。最新は155。全行のID、状態、要点、主張抜粋、対象測度、依存、再開条件、本文位置を保存した。これは383本文すべてを読み直したという意味ではない。MAIN、INDEX、RESULT-LEDGER、active T11 ROUTEを最新155として照合し、候補のcanonical ledger本文およびLOCAL-SIEVE、CROSS-GCD、FIBRATION、GEOMETRY-CURVESのroute本文を追加確認した。索引自体の抜粋が短い場合は元の短さをそのまま残す。
別添JSONは全383行の対応表と原索引値を保持する。分類は監査用の主題別整理であり、各ルートの数学的同値性を証明するものではない。

## 共通予算
目標はP(B)/M3(B)→0。現行の確定下界M3(B)≫B^(1/3)、既存endpoint上界P(B)≪_ε B^(1/2+ε)の間を埋める必要がある。P=o(B^(1/3))は十分だが、相対評価P=o(M3)でもよく、全候補に固定power savingを要求するのは強すぎる。固定packetの評価には全packet総和・係数高さ・content費用が別途必要。
152のfixed alphabet部分と153のmoving-prime/small-cofactor部分のnegligibilityは保持。E_balは未解決。155の平方free全素数テストは元のsphere equationと同値であり、独立密度savingではない。

## 推奨1：M3-XG-GATE-002 — cross-gcd stratified raw-edge tail
既にexact Stage14-4bn dictionaryがある（XG-008）：
c_raw=(X2/gcd(X2,X3))*gcd(H2,H3),   R/c_raw=H3/gcd(H2,H3).
対象はR≤Bの同じphysical raw two-face graph。必要な新しい定理は
E_raw,{c>C}(B) ≪ B^(1/2+o(1))*C^(-1+o(1))
という合計tail。C=B^(1/6+η)なら、その大cross-gcd部分はo(B^(1/3))となる。古い「c² determinant density×既存B^(1/2)」はXG-NEG-001/002で否定済み。exact dictionaryをもう一枚作ることも進歩ではない。
重要な範囲注意：t=R/cならc>Cはt<R/Cと同値。t<B/Cはその必要条件を広げた事象であり、R≤B全域で同値ではない。大きい事象を評価できれば十分だが、その評価が本来のtailから自動で出るわけではない。実際のRまたはRのdyadic shellを保持する。
全体接続の限界：T11-013により小cross-gcd側では大τが残る。大cross-gcd tailだけではP=o(M3)を言えない。再攻撃前にその残差を含む予算表を書くこと。
次の具体的作業：既存Stage14 countの証明で、H3/gcd(H2,H3)またはc_rawを保持したweighted/stratified sumが可能か調べる。新しいmoment・平均評価を得る仕組みが見つからなければ停止。単に対象の名称を変えたり、点ごとのspacingを再証明したりしない。
判断：再攻撃の課題が最も具体的。ただし閉鎖主攻撃としての十分性は未確立。

## 推奨2：M3-LOCAL-GATE-001 — fixed finite block relative contraction
任意に大きい固定有限集合S（inert primes）について、
limsup_{B→∞} #{E∈M3(B): [X:D]_p∈Ω_p, ∀p∈S}/M3(B) ≤ ρ^|S|, ρ<1
を得られれば全体目標が閉じる。順序はSを固定→B→∞→|S|を大きくする。Bとともに素数集合を増やす定理やB^(-δ)の絶対savingは、この十分条件には不要。
既存LOCAL-001/XD-LOCAL-001の局所半数公式は保持。欠けているのはexact physical M3 measureへのjoint transferであり、有限体の一様分布、parameter-side CRT、単一素数での半数収縮だけからは出ない。零・bad residueに載るM3質量も含めて処理する必要がある。
155で潰れたp|Rのendpoint条件の独立性とは別問題：ここは外部の固定素数で、分母M3上の相対分布を問う。
LOCAL-GATE-002/003、TERM-GATE-002、FOUR-GATE-001、TWIST-GATE-001等は関連するphysical character-transfer問題。観測量・joint条件が異なるので互いに同値とは宣言しない。一つのreceiverを選んで必要な全block theoremを試す。
判断：全体目標への論理距離は短い。適用可能な分布定理は本監査では確認できず、成功見込みの高い既知武器とは言えない。

## 推奨3：directional centered correlation / paired-Gaussian analytic receiver
M3-A-001のwhole directional receiver：|ρ_j(B)|≪B^(-1/12-δ)を同一height・測度で得れば閉鎖する。既存の非零周波数結果とphysical centered selectorを接続できるかが課題。
T11-024はexact paired Gaussian common-core packetを与え、tH3/tH4/tH5およびtH14の適用adapterがある。しかし主平方類への全体集中はtH14 residue collision cleanupで解消されない。
T11-026はfresh squared-modulusのexact inverse-frequency kernelを与えるが、correlated endogenous modulusでphysical coefficientを定理適合するbilinear/trilinear形に分離することが未解決。
T11-024/026のfixed content target #active τ≪B^(1/12-δ)はwhole directional targetと同一ではない。content総和の費用を含める必要がある。
TQ-GATE-002の別のwhole receiverはQ_H=o(B^(2/3))、9P²≤Q_H。T11-011の小方向部分は有効だが、T11-012でlarge similarity contentを新しい制限として数える方法は撤回された。large-direction off-diagonal energyは未評価。
判断：既存解析の蓄積が使えるreserve。主項・主平方類・係数分離を解く新しい入力がなければ、completionやGauss algebraを増やしても前進しない。A、T11、TQはadapterなしに同じ定理とは扱わない。

## その他の全ルートの判断
| ルート群 | 保持する成果 | 優先を上げない理由・再開条件 |
|---|---|---|
| PAIR-GATE-001 | fixed (X,D) multiplicity B^o(1)、pair support deficitというwhole十分条件 | deficitを示す機構が未特定。LOCAL/Aの別表現として使えるが独立の完成武器ではない |
| ONE / NORM / COMMON / XD / CROSSCORE / GAUSS / PHYS-SQ / EULERIAN | exact one-factor receiver、recoverable common core、root lines、squareclass structure | M3での相対頻度・moving core populationが未評価。root densityの二重計上やordinary integer ω-distribution輸入を禁止。必要な平均定理が出た時だけ再開 |
| FOUR / FOURIER / PARAM / TERM / TWIST | local cancellation、Fourier coefficients、exact divisor encoding | FOUR-NEG-001のelementary square sieveは4/5指数で不足。PARAM-NEG-001のphysical lattice transferも未認証。fixed external prime relative法は推奨2に含めて一つずつ検証 |
| FIBRATION / transverse fibration / ETA / DELTA / CM | fixed fibers B^o(1)、exact height・curve models | moving-base weighted energyとoccupancyが未評価。二つのfibrationは既知double coverにmerge、CM local二点条件は従属、descent/automorphismも既知no-goを尊重 |
| GEOMETRY-CURVES、T11 138–149 | 固定degree群の評価、149の任意degree・≤2共役root-pair structure theorem | accumulating family総和とresidualの二層が未制御。150/154のglobal auditを越える新しいfamily/height theoremなしにdegree6,8,…を主攻撃にしない |
| 分母増強 | HIST28のM3≫B^(1/3)、既存構成 | 現在のP上界だけで閉じる単独入力はM3≫B^(1/2+δ)。1/3より少し改善するだけでは単独閉鎖しない。rational surface dominanceはDEN-NEG-001、固定rank-positive fibersのpower生成はFIB-NEG-001で止まる |
| T11 theta / ordinary Kummer / local depth / S4 / phi / psi / 非局所squareclass（036–137） | exact physical incidence・branch排除・moving conductor部分評価 | 各カードのno-goと120撤回を尊重。117 coarse carrierはτのpower budgetを圧縮せず、122 supportは新独立条件を作らない。123以降の粗いnorm fiberも普遍非空。130/134の枝排除後に残るglobal質量の定理が必要 |
| PESCH-TI | fixed-source killer、rank-zero十分条件、認証済みsource | 2つのsourceがTI-hardであるM3 weighted massをo(M3)とするTI-GATE-001が未解決。保留を覆す全体評価の根拠なし。今回自動再開しない |
| HIST14 | exact allocation・reciprocal/character adapters、collision整理 | 最終PARKカードと各外部gateを尊重。ここに多数の名称があっても多数の完成武器ではない。推奨1/3とexact measureで再接続できる部分だけ使う |
| HIST15–28 | ambient stratified asymptotics、下界、height/multiplicityと比較firewall | M2/N2の定理をM3に無adapterで移さない。上下界と測度の入力として保持 |
| GOAL / ROOT / MASTER / GCD / HEIGHT・sampling firewalls | 目標、辞書、cost、無効推論を止める証明 | 新しい全体savingとは数えない |
| T11 150–155 direct support | globalization audit、152/153 negligible sectors、155 exact all-squarefree equivalence・Fourier count adapter | Fourier係数表示だけではcancellationなし。全E_balでbudgetを改善する定理が必要 |

## 全383行の主題別件数
- goal・構造・counting firewall: 15行
- 局所分布・physical transfer: 12行
- geometry・fibration・curve: 38行
- one-factor・norm・character・Fourier: 41行
- cross-gcd: 12行
- directional correlation・pair support: 4行
- 分母増強: 2行
- TQ：second-squareclass energy: 7行
- Stage14：既存解析・外部ゲート: 50行
- Stage15–28：比較・上下界・測度: 44行
- T11 036–075：対称incidence・conductor: 37行
- T11 001–014：energy・cross-gcd: 14行
- T11 015–035：Gaussian解析adapter: 21行
- T11 076–108：theta・local/descent: 33行
- T11 109–122：phi/psi moving-support: 14行
- TI：固定source排除・全体質量: 6行
- T11 123–137：非局所squareclass・残存枝: 15行
- T11 138–149：curve構造: 12行
- T11 150–155：global接続監査・direct support: 6行

## 次のチャットの入口
数学的authority155を先に確認し、この監査と全行対応表を読む。156を自動発行せず、まずcross-gcd tailのstratified countが既存証明に本当に接続するか、一つの具体命題を試す。必ずsmall-c/large-τ残差の予算も併記する。新しい同一測度平均入力がないなら、その事実を記録してfixed finite S joint transferを次の比較候補にする。新しいnegligible sectorまたはglobal estimateが証明されるまでGLOBAL_COUNTING_CREDIT=0。
本監査は既存Drive corpusの比較であり、新しい文献探索・利用可能定理の網羅的否定・あと数回で閉じる予測を行っていない。

## 永続参照
全383行対応表（JSON）：https://drive.google.com/file/d/1LcO45FpoH1jbq9IYZDPa7wH2uF2CyKJJ/view?usp=drivesdk
Source CARD-INDEX spreadsheet ID: 1skBS4TxofX8A25cnhfoxO5VZZjfBRlW_sfzHkSTNiL4
Source MAIN ID: 1gMO3D7hK2C4WgmpTz9RqeYEhvqAeKMqa0xOTxYW8TTE
Source INDEX ID: 1bH-BLHdqsF0bi7qgg9365TT99VOIDiWSTmBVeb91ZDk
Source RESULT-LEDGER ID: 1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA
Source active ROUTE ID: 1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE

