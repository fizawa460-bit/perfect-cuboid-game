# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-1113-JST`
>
> **CURRENT_BASE_COMMIT:** `5495551f890d054761ebe9798408fefd828a9dac`
>
> **CURRENT_STAGE:** `Stage12-N1-3d completed; independent re-audit next`
>
> **STAGE13_STATUS:** `PAUSED_AFTER_STAGE13_2`
>
> **SERIES_STATUS:** `STAGE12_R01_REPAIRS_COMPLETE_PENDING_REAUDIT`
>
> **R01_RESOLVED:** `MAJOR-01, MAJOR-02, MAJOR-03, MAJOR-04, CLARIFICATION-01, MINOR-01, MINOR-02`
>
> **OPEN_R01_ITEMS:** `NONE`
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_INDEPENDENT_REAUDIT`

## 0. 60秒で現状復帰する順序

1. `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/stage12-n1-2-final-r02.md`
3. `docs/stage12-n1-3d-definition-sheet.md`
4. `docs/stage12-n1-3d-constant-sheet.md`
5. `docs/stage12-n1-3d-selberg-delange-reference-lock.md`
6. `docs/stage12-n1-2-repair-status-r01.md`
7. `docs/review/stage12-n1-2-repaired-review-manifest-20260807-r02.md`
8. `review/PC-N1-2-REPAIRED-PROOF-20260807-R02.html`

必要に応じて修復原文を読む。

```text
docs/stage12-n1-3a-rectangular-error-repair.md
docs/stage12-n1-3b-fixed-circle-remainder.md
docs/stage12-n1-3c-coupled-region-transfer.md
docs/stage12-n1-3c-g-residue-first-closure.md
```

## 1. 現在の候補定理

3d definition sheetで定義したprimitive oriented countについて

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3.
\]

R01の全修復は文書上完了した。ただし、独立再監査が `CLOSED` を返すまでは「証明済み完成定理」と扱わない。

## 2. Stage12-N1-3dで完了した内容

### Counting definition

```text
docs/stage12-n1-3d-definition-sheet.md
```

次を自己完結に固定した。

- admissible `(h,r,s)` parameter set;
- `G(hrs)-1` multiplicity;
- raw / primitive exact Möbius relation;
- primitive-first `A_{r,s}(m)`;
- odd--odd / opposite-parity height factor;
- `beta`, `gamma`, `g`, `rho`;
- oriented / canonical distinction。

### Constant normalization

```text
docs/stage12-n1-3d-constant-sheet.md
```

次を完全表示した。

- `kappa` と `eta` のEuler積;
- `p=3 mod 4`, `q=1 mod 4` local factors;
- front ratio `8/pi`;
- `eta_p/kappa_p=(1-p^-2)^-1`;
- `eta=pi*kappa`;
- parity、radial、orientation、outer `B/pi` のfactor ledger。

### Reference lock

```text
docs/stage12-n1-3d-selberg-delange-reference-lock.md
```

Tenenbaum Third Edition, Chapter II.5, Theorem II.5.2, p.281を主引用に固定した。

- `z=1` for `beta`;
- `z=2` for `g=1*beta`;
- arbitrary fixed log-power remainderを採用;
- specific `3/5` subexponential remainderは必須inputから外した。

### Integrated Final R02

```text
docs/stage12-n1-2-final-r02.md
```

3a、3b、3c.G、3dを一つの証明鎖へ統合した。旧 `docs/stage12-n1-2-final.md` はsuperseded summaryへ変更済み。

### Self-contained review bundle

```text
BUNDLE_ID=PC-N1-2-REPAIRED-PROOF-20260807-R02
MANIFEST=docs/review/stage12-n1-2-repaired-review-manifest-20260807-r02.md
HTML=review/PC-N1-2-REPAIRED-PROOF-20260807-R02.html
SOURCE_SNAPSHOT_COMMIT=08a3bc0b8428f9c620269da9b488e8b849cf909c
SOURCE_LEDGER_SHA256=26528cd336fe4b6ce5bc70bdca368ad605f29f711bec71e34a6427d98b3560dc
```

## 3. R01 repair summary

```text
MAJOR_01=CLOSED_BY_STAGE12_N1_3A
MAJOR_02=CLOSED_BY_STAGE12_N1_3B
MAJOR_03=CLOSED_BY_STAGE12_N1_3C_G
MAJOR_04=CLOSED_BY_STAGE12_N1_3D
CLARIFICATION_01=CLOSED_BY_STAGE12_N1_3D_REFERENCE_LOCK
MINOR_01=CLOSED
MINOR_02=CLOSED_BY_SELF_CONTAINED_R02
```

## 4. 重要な証明戦略

3cで設定したfixed-`(b,c)` anisotropic kernel lemmaは、最終定理より強く不要だった。

```text
OLD_3C_G_FIXED_DIVISOR_KERNEL=SUPERSEDED_NOT_REQUIRED
```

最終ルートは除数展開を元へ戻して

\[
g(n)=\pi\gamma(n)=(1*\beta)(n)
\]

を元変数 `(r,s)` 上で平均するresidue-first routeである。未証明のfixed-divisor kernel statementは仮定していない。

## 5. 次の作業

次は新しい数学段階ではなく、R02 bundleの独立再監査である。

要求判定:

```text
CLOSED
REPAIRABLE
OPEN
STALE_SOURCE
UNREADABLE_SOURCE
```

再監査が `CLOSED` を返した場合だけ、Stage12-N1-2を再びclosedへ変更する。

## 6. Stage13の扱い

Stage13-1とStage13-2の構造的成果は保持するが、Stage13-3以降はStage12再監査まで停止する。

- canonical counting convention;
- raw incidence / overlap ledger;
- equal-weight `S_3` orientationが `1:1:1` へ対称化すること;
- orientation multiplicity単独ではcanonical `2:1:1` を説明できないこと。

Stage12のoriented asymptoticからcanonical定数への自動変換は行わない。

## 7. 禁止事項

- 独立再監査前に `CLOSED`, `FINAL_COMPLETE`, `proved` と呼ばない。
- 旧Finalを数学的標準本文として配布しない。
- fixed-`(b,c)` kernel lemmaを証明済みまたは必要と扱わない。
- specific `3/5` remainderをreference lock済みinputとして引用しない。
- Stage12からStage13 canonical countへ固定係数変換しない。
- ユーザーの明示依頼なしにPRをマージしない。

## 8. State codes

```text
STAGE12_N1_3A_COMPLETE
STAGE12_N1_3B_COMPLETE
STAGE12_N1_3C_G_COMPLETE
STAGE12_N1_3D_COMPLETE
ALL_R01_REPAIRS_COMPLETE
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_INDEPENDENT_REAUDIT
STAGE13_3_PAUSED_PENDING_STAGE12_REAUDIT
NEXT_TASK=INDEPENDENT_REAUDIT_OF_PC_N1_2_REPAIRED_PROOF_R02
```