CURRENT ROUTE CONTROL — PARKED BY EXPLICIT USER REQUEST
STATUS=PARKED_RESEARCH_ROUTE / PROVED_RESULTS_RETAINED
PRIMARY_STAGE37_ROUTE=K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE
PRIMARY_STAGE37_ROUTE_DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE
TI_LATEST_CARD=M3-PESCH-TI-005
TI_LATEST_CARD_FILE_ID=1Le8Ljo-NMPpPJ9UCzx38m1FrEqnWYPG2
TI_NEXT_RESERVED_CARD=M3-PESCH-TI-006
ORDINARY_STAGE37MAINBATCH=Resume T11 at audited121 toward122. Do not automatically execute the historical TI continuation instructions below.
OPTIONAL_TI_RESUME=Latest TI005 card/audit/scripts and former section9 remain the parked checkpoint.
TI_1072_AGGREGATE_STATUS=HOLD
GLOBAL_FIXED_POWER_SAVING=false
P_OVER_M3_LIMIT_PROVED=false
HISTORICAL_RECORD_BELOW=Prior active-route instructions are historical; mathematical results and verification artifacts remain valid within audited scope.

# Stage37 主攻撃 — torsion-intersection 二源 weighted receiver

STATUS=PARKED_RESEARCH_ROUTE / USER_REQUESTED_T11_RESTORATION / OPEN_THEOREM_GATE
PRIMARY_GATE=M3-PESCH-TI-GATE-001
LOAD_BEARING_CARD=M3-PESCH-TI-001
LOAD_BEARING_CARD_DOC_ID=1Tmy_8CX29vqVaJah5WhOuTyzDrqveeYOdCvH9MVt-9U
SCOPED_LITERATURE_AUDIT_DOC_ID=1Nc-9HIo6uaqWRTuFfimIzJXwE5d7O5BdAYPwUjSISfA
CHANGE_KIND=研究順序と主gateの変更。新しい数学的closure、rank分布定理、有限fiber認証の昇格ではない。

## 1. ゴールと旧121の位置

ゴールは引き続き P(B)/M3(B)->0。原始canonical M3のexact physical R<=Bを測度とし、一個体を一回数える。完全直方体の不存在をゴールに置き換えない。

M3-T11-121は、phi分岐で評価点とquarticの根の差について整数平方類の素因子支持を制限した補助結果。実際の差の平方類にはSの分母が残り、endpointを消す定理や新しい計数改善には達していない。結果は有効なまま保存するが、主攻撃としての継続を待機させる。

TI-001は、条件を満たす固定Euclid sourceの非退化endpoint fiberを丸ごと消す。source交換後にも適用できるため、endpointは二源の両方がTI-hardである領域に含まれる。こちらを主receiverにする。

旧T11 gate、S4、theta!=0は未解決の予備ルートとして保持する。120撤回と117〜119再監査の結果を変更しない。T11の既存IDは121まで、122は旧系列の次番として保持する。TI側の新規数学カードは独立の番号系列で事前重複確認後に採番する。このroute変更自体で新しい数学カードを作らない。

## 2. current authorityとして使用する既存武器

TI-001のStage37 exact dictionaryを使用する。固定source p=(m,n)に対し、Master上で P_p(t^2)=M/b^4、Q_p(t^2)=f1/b^4。M3ではMが既に非零平方なので、H_pのphysical tでの有理liftはendpointと同値。

TI_CLOSED(p)に使える既存の十分条件は、次のいずれか。
A: E3(Q)のrank=0、torsion点数=4。
B: E_uV(Q)のrank=0、torsion点数=6。
C: E_uV(Q)のrank=0、torsion点数=8、H_pへの有理torsion liftがちょうど8点。
使用範囲と非退化条件はTI-001および既存監査票に従う。E3の条件が失敗しても、B/Cで閉じられる可能性を捨てない。

一般定理・exact adapterは既存のscoped PASSを引き継ぐ。1,072-fiber aggregateはHOLDを維持。本文とAppendixのrank認証経路の食い違いが解消されるまで、一覧の全行を無条件TI_CLOSEDとして使わない。UNKNOWN・GRH条件付き・lift未確認の行はhard側に残す。実workerや証明を検証できないときは、それを新しいclosed認証の代わりにしない。

## 3. 正しいweighted receiver

各physical canonical個体Eについて、M3-MASTER-001のsource表現から決まる二源(p1(E),p2(E))を一組固定する。sourceの二方向を各1/2で対称化し、

mu_B(p,q)=1/2 * sum_{E in M3(B)} (1_{(p1,p2)=(p,q)} + 1_{(p2,p1)=(p,q)})

と置く。p1=p2でも二項を合わせてその個体の質量は1。表現の存在やsource交換を、個体の二重計数にしない。source対の裸の個数とmu_Bを同一視しない。

sum_{p,q} mu_B(p,q)=M3(B), mu_B(p,q)=mu_B(q,p)。
無条件にTI_CLOSEDが証明されたsource集合をC_TIとし、H_TI=全primitive source集合からC_TIを除いた集合とする。H_TIは手法でまだ閉じられていない集合で、endpoint sourceが実在するという意味ではない。

R_HH(B)=sum_{p,q in H_TI} mu_B(p,q)
       =#{E in M3(B):p1(E),p2(E) in H_TI}。

TI-001より P(B)<=R_HH(B)。主gateは
R_HH(B)=o(M3(B))。

これを証明すれば P(B)/M3(B)->0。既存のM3(B)>>B^(1/3)を使う強い十分条件として、あるeta>0に対する R_HH(B)<<B^(1/3-eta) も使える。旧T11の局所1/12窓を、そのままこのsource測度の指数予算へ移さない。

F_B(p)=sum_q mu_B(p,q) とすれば R_HH(B)<=sum_{p in H_TI}F_B(p)。したがってweighted hard marginalがo(M3(B))になる一源の定理も十分。marginalが消えなくても、二源のjoint hard質量を直接消す相関定理は別の十分条件になる。二源の独立性は仮定しない。

重要な区別：closed sourceが無重みで多数、有限で1072組、weightedでも一定割合cだけ、という情報だけでは比0を導けない。一定割合だけ閉じても、残る正の割合が消える定理は別途必要。各Bでの有限認証は残差上界を作れるが、その有限値をasymptotic theoremに置き換えない。

## 4. 研究順序と各段階の出口

1. exact M3 source-weight adapterを具体化する。
   Masterのcanonical化・sourceの高さ・gcd scaling・physical R<=Bの条件を保持したsource対へのpullbackを定式化する。上のmu_Bは測度の定義として完成しているが、その重みの有効な上界や分布はまだ未証明。無重みsource boxの計数で代替しない。
   出口：TI_CLOSED familyの情報をR_HH(B)またはweighted marginalの上界へ送れる、具体的な重み評価式。

2. E3 familyのTI_CLOSEDを無条件に扱える範囲を広げる。
   TI-001の E3: y^2=(V2^2*w^2+4U2^2)(W2^2*w^2+4U2^2) を、rank/torsionを追跡できる正確なWeierstrass modelへ移す。primitive source上でtorsion=4の成立範囲・例外を先に把握し、rank-zeroを無条件に証明できる算術familyを探す。E_uVのB/C条件は補助として利用する。全sourceのrank zeroやrank分布の予想を出発仮定にしない。
   出口：証明付きのclosed familyと、そのfamilyを除いたphysical source質量への評価。有限のrank-zero行を追加しただけなら診断結果として保存する。

3. weighted hard領域の漸近縮小を証明する。
   一源weighted hard marginalを消すか、二源joint hard領域を直接消す。閉じたfamilyの無重み密度をそのままphysical密度に読み替えない。実際の残差評価がo(M3(B))または上の固定べき十分条件に達した時点だけgateを閉じる。
   出口：P/M3極限への最終receiver。rank-zero証明と重み評価の同じ効果を二回差し引かない。

1072全件の再現は、主攻撃に必要な重み・family theoremを置き換える作業にしない。ただし選んだfamilyの証明に必要な個別行の無条件認証は行う。

## 5. 次の新規チャットの実行契約

STARTUP=MAINの先頭control -> このactive route -> TI-001 -> 既存scoped audit。RESULT-LEDGERとCARD-INDEXは該当ID・新規主張の重複確認に使う。旧T11全文の読み直しは不要。
NEXT_LEGAL_ACTION=最新のTI-005節から再開。TI-006では強化したdescentの残存2進分岐をexact physical partner重みとともに評価する。
FIRST_RESEARCH_DELIVERABLE=TI-001へのfamily-model/torsion addendum、または重複のないTI系列の新しい限定結果。rank-zero familyやsource-weight評価が得られない場合も、失敗条件と次の候補をこのrouteに残す。
NO_NEW_MATHEMATICAL_CREDIT_FOR_ROUTE_SELECTION=true
T11_121_STATUS=RETAINED_PROVED_EXACT_STRUCTURE / PARKED_PRIMARY_RESEARCH
T11_120_STATUS=RETRACTED_PHYSICAL_ADAPTER
TI_1072_AGGREGATE_STATUS=HOLD
M3_PESCH_TI_WEIGHTED_HARD_LOCUS_SAVING_PROVED=false
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false

## 6. TI-002 到達点（最新の再開位置は次節）

CARD_FILE_ID=14sF8_rcDcKza9e6Erxdyw1_y_3qA1F5m
AUDIT_FILE_ID=1qckX74bjeRbALyM73oXdQbYC_ouONxwG
VERIFICATION_SCRIPT_FILE_ID=1bnYdKMoEaaR4LoMSPadARw_aqe-T0Byw
NEXT_CARD=M3-PESCH-TI-003

E3のsplit cubicモデル、全primitive sourceのglobally minimal semistable integral model、order-fourの一律排除を証明した。詳細証明・変換・例外点・独立検証はTI-002にある。

E_min: y^2+xy=x^3+A2 x^2+A4 x, A2=(2(m-n)^4-(m+n)^4-1)/4, A4=-(m-n)^4 VW/4。
c4=U^4+16V^2W^2, Delta=U^8V^2W^2/16, gcd(c4,Delta)=1。

G_tor={some q in {7,11,13,17}: q does not divide UVW}ではtorsion=4。これは全good projective source classの有限体上の完全列挙による証明で、整数sourceの標本検査ではない。X_torは17017|UVWの例外。例外sourceのtorsion=4を否定する結果ではない。

数学的集合G_plus={p in G_tor:actual rank E3(p)>0}に対して、endpoint sourceはX_tor union G_plusに入り、同じmu_Bで
P(B)<=R_plusplus(B)+2 sum_{p in X_tor}F_B(p)。
前者は両sourceがG_plusのjoint mass、後者はtorsion例外のmarginal mass。どちらもo(M3)とは未証明。固定modulusだけで例外重みは消えない。未計算sourceをpositive rankに分類しない。有限認証registryのHARD/UNKNOWNと、この数学的集合を混同しない。

semistabilityは全E3で確定したがrank-zero familyは未取得。EuVのsemistability、504曖昧worker、1072全件認証は確認しておらずHOLD継続。主gate OPEN、global savingとP/M3極限の各flagはfalseを維持。

再開順: MAIN先頭control -> この最新節 -> TI-002 -> 監査とscript -> TI-001のexact adapter（必要な箇所）。旧117〜121全文は再読不要。次にexact 2-descentで閉じられるfamilyを作り、そのcomplementのphysical weightを評価する。有限L_ratio計算は個別認証用で、漸近定理の代替にはしない。

## 7. TI-003 到達点（最新の再開位置は次節）


M3-PESCH-TI-003 — UNCONDITIONAL MODULAR TWO-ISOGENY CERTIFIER / TWO REPLAYED TI-CLOSED FIBERS
CARD_FILE_ID=1gdjqNcIP_GsoJKiQ-mH26WfqxDNAjhbz
AUDIT_FILE_ID=1rr7EwWhURbuvTVqJCQNk2YA18O7PtlYb
PRODUCER_SCRIPT_FILE_ID=13U4Zbhn539OvdT1jqH_zvFAlRAboYx0F
INDEPENDENT_VERIFIER_SCRIPT_FILE_ID=1nTdNz-QuPNF_dKHUogr6u4MjIP0LNdrV
CERTIFICATES_JSON_FILE_ID=1XiyLe2eN3ZzFMGnXtMeqg2EMf5M3d9RM
STATUS=PROVED_PARAMETER_UNIFORM_SUFFICIENT_CERTIFIER / TWO_REPLAYED_TI_CLOSED_SOURCES / NO_INFINITY_DENSITY_OR_GLOBAL_SAVING_CREDIT
E3 split model E has (a,b)=(-2(V^2+W^2),U^4). Two-isogenous E' has (a',b')=(4(V^2+W^2),16V^2W^2), roots 0,-4V^2,-4W^2.
Every descent class gives a primitive integral cover c^2=d z^4+a z^2t^2+(b/d)t^4. Finite prime-power nonsolubility is a sound exclusion, survival UNKNOWN.
If remaining E classes={1} and E' classes={1,-1,sf(VW),-sf(VW)}, explicit rational points plus 2^r=|im alpha|*|im alpha'|/4 prove rank zero. Within G_tor this proves TI_CLOSED.
All 31 primitive m<=12 were tested. Sources (4,1),(9,4) independently certified rank zero and torsion four; other 29 UNKNOWN. No claim these two are new versus the external 1072 list.
Independent full primitive-pair enumerator verified all 22 modular obstruction witnesses and dual-point identities. Producer/chart optimization and verifier/full-pair method differ.
Exact same-physical-measure receiver for certified C: P<=M3-2F_B(C)+R_CC. Joint term restored to avoid double subtraction; no independence or unweighted substitution. No physical weight values or asymptotics obtained.
No infinite rank-zero family cardinality/density theorem. 1072 aggregate HOLD, all global flags false.
NEXT=M3-PESCH-TI-004: extract arithmetic family conditions from these modular obstructions and evaluate the Master physical source-weight complement; avoid blind finite-table expansion.


任意のprimitive sourceのrank-zeroを合同障害証明書で認証する十分条件を確立。これは無限族の存在・密度の証明ではない。TI-002のglobally minimal semistable modelは引き続き有効。新しいrank認証はGRH/BSD/analytic_rank_upper_boundを使わない。

再開順: MAIN先頭control -> この節 -> TI-003 -> certificate JSON -> producerとindependent verifier -> 必要ならTI-002のtorsion screen。Driveだけから再実行可能。次は22の合同障害をパラメータ族の条件に変え、同じphysical R<=B上の重みを評価する。有限認証が主gateを閉じたと読まない。


## 8. TI-004 到達点（最新の再開位置は次節）

M3-PESCH-TI-004 — UNIFORM LEGENDRE RANK BOUND / EXACT MASTER PAIR KERNEL
DATE=2026-09-30
CARD_FILE_ID=1dUz306uHWV6DwqybIGLUUeO6w1fpWcFK
AUDIT_FILE_ID=1EqGhddWUTK8Gn7QmnWyFBrUa6Uo3_RAk
PRODUCER_SCRIPT_FILE_ID=1tJmFcYcFr5S0z2JR6bBT6oQdiU7-gQdK
INDEPENDENT_VERIFIER_SCRIPT_FILE_ID=1DkZ9nC5hBshjJO_g6dIdLWbw5sTt8Ie4
EXAMPLES_JSON_FILE_ID=1RyG0ixHBVJq7BKJArkGsHIqWWFNKQ2YM
VERIFICATION_JSON_FILE_ID=1IbRM6zZt0nVmgTNltC6uooo2dwvkdBAe
STATUS=PROVED / WITHIN_SESSION_SCOPED_ADVERSARIAL_AUDIT_PASS
Three character lemmas give two F2 matrices A,B and rank E3<=delta=(omega(U)-rank A)+(omega(2VW)-1-rank B). delta=0 on G_tor proves TI_CLOSED. delta>0 is UNKNOWN, not positive rank.
K_char is a uniform sufficient arithmetic criterion; no infinitude or density theorem. Existing (4,1),(9,4) independently reverified, no new source count.
Unique primitive canonical Master inverse gives h_B(p,q) equal to the exact face-square indicator times the existing physical R cutoff, and mu_B=h_B/2 off diagonal, zero on diagonal. This is an exact kernel identity, not a weight bound.
P<=R_DD+2F(X_tor), D_char=G_tor intersect {delta>=1}, X_tor=17017|UVW. Both residual weights unbounded here.
Independent full-pair verifier:28 cover obstructions; binary kernel checks; independent primitive edge enumeration maxedge<=300 with2 reconstructed bricks. Diagnostic cutoff does not replace physical R.
NEXT=TI-005: obtain defect/exception weight bounds on this exact square locus. 1072 HOLD; gate OPEN; all asymptotic/nonexistence flags false.


CURRENT AUTHORITY CONTROL — TI-004 Legendre matrix bound and exact Master kernel
PRIMARY_GATE=M3-PESCH-TI-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=M3-PESCH-TI-ROUTE-MAIN
ACTIVE_ROUTE_FILE_ID=198IsZ3zb1FRRbnO3BLiyqCJglDFw_4AU
LOAD_BEARING_CARD=M3-PESCH-TI-001
LOAD_BEARING_CARD_DOC_ID=1Tmy_8CX29vqVaJah5WhOuTyzDrqveeYOdCvH9MVt-9U
ACTIVE_RESEARCH_CARD=M3-PESCH-TI-004
ACTIVE_RESEARCH_CARD_FILE_ID=1dUz306uHWV6DwqybIGLUUeO6w1fpWcFK
LATEST_RESEARCH_CARD=M3-PESCH-TI-004
LATEST_AUDITED_RESEARCH_CARD=M3-PESCH-TI-004
LATEST_AUDIT_FILE_ID=1EqGhddWUTK8Gn7QmnWyFBrUa6Uo3_RAk
LATEST_PRODUCER_SCRIPT_FILE_ID=1tJmFcYcFr5S0z2JR6bBT6oQdiU7-gQdK
LATEST_INDEPENDENT_VERIFIER_SCRIPT_FILE_ID=1DkZ9nC5hBshjJO_g6dIdLWbw5sTt8Ie4
LATEST_EXAMPLES_JSON_FILE_ID=1RyG0ixHBVJq7BKJArkGsHIqWWFNKQ2YM
LATEST_VERIFICATION_JSON_FILE_ID=1IbRM6zZt0nVmgTNltC6uooo2dwvkdBAe
LATEST_CARD_STATUS=PROVED_UNIFORM_CHARACTER_RANK_BOUND_AND_EXACT_MASTER_PAIR_KERNEL / WITHIN_SESSION_SCOPED_AUDIT_PASS
E3_UNIFORM_MINIMAL_SEMISTABLE_MODEL_PROVED=true
E3_TORSION_FOUR_ON_G_TOR_PROVED=true
UNCONDITIONAL_MODULAR_RANK_ZERO_CERTIFIER_PROVED=true
UNIFORM_LEGENDRE_RANK_UPPER_BOUND_PROVED=true
EXACT_MASTER_PAIR_KERNEL_PROVED=true
E3_RANK_ZERO_ARITHMETIC_CRITERION_PROVED=true
E3_INFINITE_RANK_ZERO_FAMILY_PROVED=false
E3_RANK_ZERO_ARITHMETIC_FAMILY_PROVED=false
FAMILY_FLAG_SCOPE=The uniform K_char criterion is proved; existence of an infinite family or density theorem is not.
M3_PESCH_TI_1072_AGGREGATE_STATUS=HOLD
M3_PESCH_TI_WEIGHTED_HARD_LOCUS_SAVING_PROVED=false
NEXT_RESEARCH_CARD_ID=M3-PESCH-TI-005
NEXT_T11_RESEARCH_CARD_ID=M3-T11-122
PROVISIONAL_FRONTIER_CARD=NONE
PROVISIONAL_FRONTIER_AUDIT_STATUS=NOT_APPLICABLE
CURRENT_ATTACK=MatrixDefectOnExactMasterSquareLocus|PhysicalExceptionalMarginal
NEXT_LEGAL_ACTION=Read active route latest TI-004 section, card, audit and replay files. Study delta>0 on the exact Master pair kernel with unchanged physical R cutoff; bound joint D_char mass and X_tor marginal. Do not relabel delta>0 as positive rank or finite tests as an infinite family.
CHARACTER_RECEIVER=P(B)<=R_DD(B)+2 sum_{p in X_tor}F_B(p); D_char={p in G_tor:delta(p)>=1}, X_tor={17017|UVW}. Neither physical weight is evaluated.
PAIR_KERNEL=mu_B(p,q)=h_B(p,q)/2 for distinct primitive sources; diagonal zero. h_B requires exact Master face square and existing canonical physical R<=B. Unique oriented source pair proved.
PRIMARY_RECEIVER=P(B)<=R_HH(B); weighted o(M3) remains unproved.
WEIGHT_FIREWALL=No raw source density transfer, no independence, no numerical physical mass, no new finite-source count versus TI-003 or external1072.
GOAL_UNCHANGED=P(B)/M3(B)->0 on exact primitive canonical physical R<=B.
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
T11_121_RESEARCH_STATUS=RETAINED_PROVED_EXACT_STRUCTURE / PARKED_PRIMARY_RESEARCH
T11_120_STATUS=RETRACTED_PHYSICAL_ADAPTER
HISTORICAL_MAIN_RECORD_BELOW=Lower historical continuation pointers are superseded by this control; audited mathematical scopes remain.

再開順: MAIN先頭control -> この節 -> TI-004 -> 監査と2 scripts/JSON -> 必要なTI-001/002/003のみ。Driveのscriptを同じdirectoryにdownloadし python ti004_legendre.py と python ti004_audit.py を実行可能。TIの優位性は未確定。T11-121は停滞認定せず有効な補助として保持。5–10 substantive batchは比較見直しの目安で証明予測ではない。


## 9. 最新到達点 — TI-005（この節から研究を再開）

M3-PESCH-TI-005 — FORCED KERNEL BARRIER / UNIFORM TWO-ADIC REPAIR
CARD_FILE_ID=1Le8Ljo-NMPpPJ9UCzx38m1FrEqnWYPG2
AUDIT_FILE_ID=19WVrkNMOA564BZIgtBTu71lAWYb_BlFU
PRODUCER_SCRIPT_FILE_ID=1IN6NL9U6MGQih_hju49rgVbS7HB47QSy
INDEPENDENT_VERIFIER_SCRIPT_FILE_ID=1J-xV5Dxc-LWfanEGAGs_1Ix1P1DSllQT
EXAMPLES_JSON_FILE_ID=1KUXMpGudDlkx4w2oPdP1lPj-W5KjXSp2
VERIFICATION_JSON_FILE_ID=1TghMDDrGwbu-Ch9qJYM5M9PBJNK323mY
STATUS=PROVED / WITHIN_SESSION_SCOPED_ADVERSARIAL_AUDIT_PASS
Old B always kills the vectors sf(mn),sf(2W); nonsquare mn makes them independent. Thus old delta=0 implies m,n both squares. This is a criterion barrier, not positive rank or physical density.
If nu2(V)=2, every signed even E' descent representative has an insoluble cover over Q2 (primitive mod512 proof). Add a prime2 unit row to B and obtain rank<=delta_star.
Selected nonsquare-mn sources(2,1),(6,1),(11,2) now independently certified TI_CLOSED, extending the TI-003 replayed registry. External1072 novelty not claimed; HOLD.
Physical brick(117,44,240) has sources(11,2),(8,5), with first now closed. Exact same-physical-measure partition difference and residual receiver recorded. No weight bound achieved.
Independent replay:8 signed covers by all primitive pairs mod512;7 forced-kernel/binary-kernel fixtures; exact physical Master witness.
NEXT=TI-006 surviving 2-adic branches plus physical partner weights. Gate OPEN and global flags false.

CURRENT AUTHORITY CONTROL — TI-005 forced-kernel barrier and 2-adic repair
PRIMARY_GATE=M3-PESCH-TI-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=M3-PESCH-TI-ROUTE-MAIN
ACTIVE_ROUTE_FILE_ID=198IsZ3zb1FRRbnO3BLiyqCJglDFw_4AU
LOAD_BEARING_CARD=M3-PESCH-TI-001
LOAD_BEARING_CARD_DOC_ID=1Tmy_8CX29vqVaJah5WhOuTyzDrqveeYOdCvH9MVt-9U
ACTIVE_RESEARCH_CARD=M3-PESCH-TI-005
ACTIVE_RESEARCH_CARD_FILE_ID=1Le8Ljo-NMPpPJ9UCzx38m1FrEqnWYPG2
LATEST_RESEARCH_CARD=M3-PESCH-TI-005
LATEST_AUDITED_RESEARCH_CARD=M3-PESCH-TI-005
LATEST_AUDIT_FILE_ID=19WVrkNMOA564BZIgtBTu71lAWYb_BlFU
LATEST_PRODUCER_SCRIPT_FILE_ID=1IN6NL9U6MGQih_hju49rgVbS7HB47QSy
LATEST_INDEPENDENT_VERIFIER_SCRIPT_FILE_ID=1J-xV5Dxc-LWfanEGAGs_1Ix1P1DSllQT
LATEST_EXAMPLES_JSON_FILE_ID=1KUXMpGudDlkx4w2oPdP1lPj-W5KjXSp2
LATEST_VERIFICATION_JSON_FILE_ID=1TghMDDrGwbu-Ch9qJYM5M9PBJNK323mY
LATEST_CARD_STATUS=PROVED_UNIFORM_KERNEL_BARRIER_AND_TWO_ADIC_ENHANCEMENT / WITHIN_SESSION_SCOPED_AUDIT_PASS
E3_UNIFORM_MINIMAL_SEMISTABLE_MODEL_PROVED=true
E3_TORSION_FOUR_ON_G_TOR_PROVED=true
UNCONDITIONAL_MODULAR_RANK_ZERO_CERTIFIER_PROVED=true
UNIFORM_LEGENDRE_RANK_UPPER_BOUND_PROVED=true
EXACT_MASTER_PAIR_KERNEL_PROVED=true
E3_RANK_ZERO_ARITHMETIC_CRITERION_PROVED=true
CHARACTER_MATRIX_FORCED_KERNEL_BARRIER_PROVED=true
UNIFORM_TWO_ADIC_ROW_AT_V2_2_PROVED=true
ENHANCED_RANK_UPPER_BOUND_PROVED=true
REPLAYED_NEW_VERSUS_TI003_TI_CLOSED_SOURCES=(2,1),(6,1),(11,2); no external1072 novelty claim.
E3_INFINITE_RANK_ZERO_FAMILY_PROVED=false
E3_RANK_ZERO_ARITHMETIC_FAMILY_PROVED=false
M3_PESCH_TI_1072_AGGREGATE_STATUS=HOLD
M3_PESCH_TI_WEIGHTED_HARD_LOCUS_SAVING_PROVED=false
NEXT_RESEARCH_CARD_ID=M3-PESCH-TI-006
NEXT_T11_RESEARCH_CARD_ID=M3-T11-122
PROVISIONAL_FRONTIER_CARD=NONE
PROVISIONAL_FRONTIER_AUDIT_STATUS=NOT_APPLICABLE
CURRENT_ATTACK=EnhancedDescentOnPhysicalPartnerWeights|SurvivingTwoAdicBranches
NEXT_LEGAL_ACTION=Read latest route section and TI-005. Evaluate exact Master partner weights for surviving branches or prove a further uniform descent obstruction reaching a weighted region. Do not expand an undirected finite rank table. Additional 2-adic rows outside nu2(V)=2 require new proof.
STRUCTURAL_BARRIER=Old B has forced sf(mn),sf(2W) kernel vectors. Nonsquare mn forces old delta>=1. Full-rank-randomness for that old B is prohibited. Kernel vectors are not rational descent images.
ENHANCED_BOUND=Append prime2 unit row exactly when nu2(V)=2. rank E3<=delta_star<=delta. G_tor and delta_star=0 imply TI_CLOSED; delta_star>0 remains UNKNOWN.
CHARACTER_RECEIVER=P<=R_DstarDstar+2F_B(X_tor), exact physical measure; no asymptotic bounds. Exact partition receiver P<=R_HstarHstar also retained.
PHYSICAL_WITNESS=Primitive brick(117,44,240) has source(11,2) now TI_CLOSED; excluded for B>=its existing physical R. No replacement by maxedge cutoff.
PAIR_KERNEL=TI-004 exact h_B face-square and existing physical R cutoff; mu=h_B/2 off diagonal, zero diagonal.
PRIMARY_RECEIVER=P(B)<=R_HH(B); weighted o(M3) remains unproved.
WEIGHT_FIREWALL=No raw source density transfer, independence, infinite family, positive-rank inference or double-saving credit.
GOAL_UNCHANGED=P(B)/M3(B)->0 on exact primitive canonical physical R<=B.
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
T11_121_RESEARCH_STATUS=RETAINED_PROVED_EXACT_STRUCTURE / PARKED_PRIMARY_RESEARCH
T11_120_STATUS=RETRACTED_PHYSICAL_ADAPTER
HISTORICAL_MAIN_RECORD_BELOW=Lower continuation pointers are superseded; audited mathematical scopes retained.

再開順: MAIN先頭control -> この節 -> TI-005 card/audit -> ti005_rank_bound.py, ti005_audit.py とJSON。両scriptを同じdirectoryに保存して実行できる。TI-004 exact kernelは維持、旧117〜121全文は不要。今回のweighted exitは未達だが、行列の必然的な障害とその一分岐の2進repairを証明。TIの優位性は未確定。T11-121有効・待機。


