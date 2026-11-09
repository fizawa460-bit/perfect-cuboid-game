# PR #1860 継続中：R3-07 / R2-01 数学原著の再帰的自己完結監査

**状態：IN_PROGRESS / RECURSIVE_PARENT_CLOSURE_UNVERIFIED / DO_NOT_MERGE（2026-11-09）。** これは第２周の作業ログ。23件は第１周の発見候補であり、全不足ではない。**２ルートの依存鎖をこれからも辿り、初回に未発見だった必要原著が出たら本PRに順次加える。** 完了宣言なし。計算証拠の全面移植・独立数学監査PASSは別層。

## 第１周の23候補の外から新規発見した原著

| 原数学原著 | Drive原著 | 第２周GitHub保存 | 論理的役割・注意 |
|---|---|---|---|
| **R2-C160-OWNER-STRONG-GCD** | [Drive](https://drive.google.com/file/d/12zpMA0N4I8FKRyeiiRVpLGELs7ef5_X9/view) | [収載](./proofs/active-ancestors/C160-R2-strong-gcd-original.md) | C160 is R0 integration summary; mathematical owner proof SG.1/SG.2 is a different document, not among original 23.（LOAD_BEARING_DIRECT_PARENT） |
| **R2-C185-OWNER-PRIME-CUT** | [Drive](https://docs.google.com/document/d/11mAxfmwcaGns7H_Za-X59BMN4dYEPmjy_xvV9mEg7M0/edit) | [収載](./proofs/active-ancestors/C185-R2-prime-cut-original.md) | R0 C185 summary only gave sparse lcm/gcd formula; owner source includes its full valuation case split and constants.（LOAD_BEARING_DIRECT_PARENT） |
| **R2-C174-OWNER-HYBRID-HEIGHT** | [Drive](https://docs.google.com/document/d/1XxC52DqQ9E5WZGcqIWcXWuLgUse_XfZ7T0JjV1Y-Sg4/edit) | [収載](./proofs/active-ancestors/C174-R2-hybrid-height-original.md) | R0 C174 uses owner λ4/λ3 exact threshold certificate; full owner proof is distinct from R0 integration text.（LOAD_BEARING_DIRECT_PARENT） |
| **R2-C175-EFFECTIVE-TOP-UPPER** | [Drive](https://docs.google.com/document/d/1WyJgZFJL0XDGFWRGFGBas8SNrdVsUiVRlxZHoBtajiU/edit) | [収載](./proofs/active-ancestors/C175-R2-effective-top-upper-original.md) | R0 accepted scoped numerical effective upper, which is NOT a <75% all-source upper.（CONDITIONAL_UPPER_TOOL_NOT_C189_LOWER_CORE） |
| **R2-C175-OLDER-MOBIUS-UPPER** | [Drive](https://docs.google.com/document/d/1ojhPqu5PynGnDzHnZ8YNCzWEuYUJ-kb_ndk0y_3aOrA/edit) | [収載](./proofs/active-ancestors/C175-R2-older-mobius-upper-original.md) | C175 cites postC136 original subset-Möbius upper; not the all-index strict 75% upper.（CONDITIONAL_UPPER_ANCESTOR_NOT_C189_LOWER_CORE） |

**照合結果：原著５本を直接Driveから取得し、GitHubから読み戻したテキストが全件一致**。第１周の23件とは別に発見した証拠であり、以前の「残り11件」が全不足数だったという考えは成立しない。特にC160のR0要旨とR2オーナーSG.1/SG.2原証明は別文書である。

## 現在点検した依存辺（『存在する』と『数学的に十分』を分離）

| ルート | 子 → 数学親 | 照合した根拠 | 現在の判定 | 次に残す条件 |
|---|---|---|---|---|
| R2-01 | C185 sparse prime-cut → R2-C160-OWNER-STRONG-GCD | C185.md line 24 and C160.md §3; owner proof SG.1/SG.2 | **SOURCE_RETAINED_STATEMENT_MATCHED** | all parent assumptions and computations not independently audited |
| R2-01 | C187 155/197 → R2-C185-OWNER-PRIME-CUT | R2-uniform-thresholds.md cites C185 exact λ-bound and 9/50, 7/50 | **SOURCE_RETAINED_STATEMENT_MATCHED** | prime-cut valuation certificate not independently rerun |
| R2-01 | C187 155/197 → R2-C174-OWNER-HYBRID-HEIGHT | C174.md §1 λ*; C175 R0 height selector; R2-uniform-thresholds.md C174/C175 reference | **SOURCE_RETAINED_STATEMENT_MATCHED** | 20856 base replay and λ* proof not independently rerun |
| R2-01 | C175 R0 §3 upper → R2-C175-EFFECTIVE-TOP-UPPER | C175.md lines 71-97 reference source | **SOURCE_RETAINED_SCOPED_TOOL** | not proof of global strict<75% upper; nonessential to adopted C189 lower |
| R2-01 | R2-C175-EFFECTIVE-TOP-UPPER → R2-C175-OLDER-MOBIUS-UPPER | C175.md §3 explicitly cites postC136 primary | **SOURCE_RETAINED_SCOPED_TOOL** | conditional upper only |
| R2-01 | S232 rank-growth denominator → S230 A/C local lemma | S232.md lines 60-66, 78-81 and S230.md §2-3 | **SCOPED_LEMMA_PRESENT** | S230 overall theorem assumes finite-odd dQ=mP; check that local A/C argument stands without it. Text says it does. |
| R3-07 | row368 Ward5/3 → S321 factorization + S263/S264 | row368.md lines 34-39; S321.md factor W5 proof, S238 old 2-adic conditions | **SOURCE_PRESENT_RECURSIVE_REVIEW_OPEN** | row368 independent certificates and source adapter not reevaluated |
| R3-07 | row369 Ward7 → S322 K/L split + C35-12 + S321 | row369.md lines 63-85; S322.md P(u)Q(u), Q(u)=P(-1-u) polynomial identity | **SOURCE_PRESENT_POLYNOMIAL_EQUALITY_CONFIRMED** | C35-12 genus3 rational point classification certificate and source coverage not reaudited |
| R3-07 | row393 degree105 → de la Maza Theorem 1/corollary | row393.md §2 gives DOI/author and specialized weight | **EXTERNAL_THEOREM_APPLICATION_PENDING** | actual primary theorem assumptions and normalized constants not independently confirmed |
| R2-01 | S252 height → Bérczes et al. Theorem 2.1(i) | S252.md lines 45-74 gives preconditions and specialization | **EXTERNAL_THEOREM_APPLICATION_PENDING** | primary theorem statement/definitions not independently verified |
| COMMON | S194 → old BranchB Section16 | S194.md header and BranchB-Section16.md with Section17 correction | **SOURCE_LOCATION_RESOLVED_MATH_AUDIT_OPEN** | Section17 withdrawn saturation/specialization conclusion must not be revived |

### 個別に確認できた再述・適用範囲

- **R2 C160→C185:** C160は統合・採否要旨、今回追加した[R2 strong-gcd原証明](proofs/active-ancestors/C160-R2-strong-gcd-original.md)は任意の符号付き２指数とnodal Hを含むSG.1/SG.2を展開。C185が必要とする2-adic階層の分母公約数法則と主張レベルで対応する。ただし独立再演PASSとはしない。
- **R2 S232→S230:** S230全体のfinite-odd排除はdQ=mPを仮定するが、§2/3のA,C局所付値評価は式の導出でdQ=mPを使わない。S232はその局所部分だけをrank-independentな前提として利用している。**全体定理を無条件に昇格しない**。
- **R3 row369→S322:** 使用する六次式P,QについてGitHub原著の係数から **Q(u)=P(-1-u)** の恒等式を確認（差が０、終結式−2²⁴×13）。この代数一致のみ確認済み。元sourceの全依存の数学監査ではない。
- **R2 S275→S271〜274:** S275の全指数canonical factorization §2はS243からの積・gcdで本文内に計算を示す。S273/274のtwist構造は§4のNO-GO説明に参照されるが、C187の155/197 lowerを得るには§2/§3の部分が主に使用される。旧側枝の要否を決める際は**命題単位**で扱い、S275の全記述の自己完結を自動認定しない。

## 次に調べる対象（このPRが終わるまで開いておく）

1. R2 C187→C185/C175→C174/S268/S270/S252 の式と数学親をさらに奥へ辿り、別個の著者原証明を探す。
2. R3 row367/368/369/376の各親とrow370→393の−30鎖に戻り、既収載の原著が結論に必要な数学の正確な証明か判定する。
3. C118・C35-11/12の計算を含む数学親、S194の旧Section16適用と撤回、最古E3 physical sourceとの条件同一性を扱う。
4. row393のde la Maza、S252のBérczesは、引用名の存在ではなく使用した定理の正確な仮定・式を独立照合する必要がある。現状PENDING。
5. 論理的親の厳密な再帰閉包が閉じるまで、必要本文の総数・不足数・完了率を確定しない。

**研究の結論は増やさない。** R3 row393停止、R2 strict75% 上界・全LOW・−30無条件排除・Branch B・Stage35はOPEN。R0 / MAIN-STATE / NEXTは不変更。
