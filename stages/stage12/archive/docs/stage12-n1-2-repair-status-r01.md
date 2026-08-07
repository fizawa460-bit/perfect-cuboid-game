# Stage12-N1-2 repair status after full audit R01

> **STATUS:** `ALL_R01_REPAIRS_COMPLETE_PENDING_INDEPENDENT_REAUDIT`
>
> **AUDIT_DATE:** `2026-08-07`
>
> **AUDIT_COUNTS:** `FATAL=0, MAJOR=4, MINOR=2, CLARIFICATION=1`
>
> **RESOLVED_AFTER_AUDIT:** `MAJOR-01, MAJOR-02, MAJOR-03, MAJOR-04, CLARIFICATION-01, MINOR-01, MINOR-02`
>
> **OPEN_MAJOR:** `NONE`
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_INDEPENDENT_REAUDIT`

## 1. 現在の判断

独立監査R01の全指摘に対する修復文書と自己完結bundleを作成した。

候補漸近式は

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3.
\]

ただし、対象はStage12-N1-3d definition sheetで定義したprimitive oriented countに限る。独立再監査が `CLOSED` を返すまで、project-wideには `proved`, `FINAL_COMPLETE`, `CLOSED` と呼ばない。

## 2. Repair ledger

### MAJOR-01 — rectangular error exponent

**状態:** `CLOSED_BY_STAGE12_N1_3A`

旧2pの不成立な

\[
R^{1/2+\delta}S+RS^{1/2+\delta}
\]

への強化を撤回し、

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
\qquad(0<\varepsilon<1/8)
\]

へ修正した。

### MAJOR-02 — fixed-circle remainder

**状態:** `CLOSED_BY_STAGE12_N1_3B`

`omega(X/l)` を `omega(X)` として畳み込み全域へ引き出す操作を撤回し、

\[
R_{r,s}(X)
\ll
G(rs)H_{\rm abs}(rs)X^{1/2}
\]

を直接証明した。retained regionのouter averageは

\[
O\!\left(BX_0^{-1/2}(\log B)^{O(1)}\right)
\]

で、任意の固定対数冪より小さい。

### MAJOR-03 — coupled-region transfer

**状態:** `CLOSED_BY_STAGE12_N1_3C_G`

3cでexact variable ledgerを復元した後、fixed-`(b,c)` anisotropic kernel lemmaは最終定理より強く不要と判定した。

3c.Gでは

\[
g(n)=\pi\gamma(n)=(1*\beta)(n)
\]

を元変数 `(r,s)` 上で直接平均し、parity-weighted coprime rectangle residue

\[
C_\lambda^{(0)}=\frac8{\pi^2}\eta
\]

を得た。radial kernelを保持したStieltjes transferにより

\[
\mathcal H_\lambda(B)
=
\frac\eta{12\pi}(\log B)^3
+o((\log B)^3),
\]

従って

\[
\mathcal M(B)
\sim
\frac\eta{12\pi^2}B(\log B)^3
=
\frac\kappa{12\pi}B(\log B)^3.
\]

```text
OLD_3C_G_FIXED_DIVISOR_KERNEL=SUPERSEDED_NOT_REQUIRED
NEW_3C_G_RESIDUE_FIRST_RECTANGLE=PROVED
NEW_3C_G_RADIAL_TRANSFER=PROVED
```

### MAJOR-04 — self-containment

**状態:** `CLOSED_BY_STAGE12_N1_3D`

成果物:

```text
docs/stage12-n1-3d-definition-sheet.md
docs/stage12-n1-3d-constant-sheet.md
docs/stage12-n1-3d-selberg-delange-reference-lock.md
docs/stage12-n1-2-final-r02.md
docs/review/stage12-n1-2-repaired-review-manifest-20260807-r02.md
review/PC-N1-2-REPAIRED-PROOF-20260807-R02.html
```

definition sheetは以下を固定する。

- exact raw parameter set;
- multiplicity `G(hrs)-1`;
- raw / primitive Möbius relation;
- primitive-first coefficient `A_{r,s}(m)`;
- parity height factor;
- oriented / canonical distinction;
- `beta`, `gamma`, `g`, `rho`。

constant sheetは以下を固定する。

- `kappa`, `eta` の完全Euler積;
- odd-prime local factors;
- 2-adic / archimedean / orientation ledger;
- prime-by-prime identity `eta=pi*kappa`;
- final coefficient `eta/(12*pi^2)=kappa/(12*pi)`。

### CLARIFICATION-01 — Selberg--Delange reference

**状態:** `CLOSED_BY_STAGE12_N1_3D_REFERENCE_LOCK`

Tenenbaum Third Edition, Chapter II.5, Theorem II.5.2, p.281を主引用として固定した。

採用形は

\[
\sum_{n\le x}\beta(n)
=c_\beta x+O_A(x(\log(2x))^{-A})
\]

と

\[
\sum_{n\le x}g(n)
=x(c_g\log x+d_g)+O_A(x(\log(2x))^{-A}).
\]

旧文書の特定 `3/5` subexponential remainderはclosureに必要なinputとして使用しない。

### MINOR-01 — control characters

**状態:** `CLOSED`

archive 2jの2箇所は正しい `\frac` となっており、新bundleとCIでform-feed不存在を検査する。

### MINOR-02 — Finalの外部記号

**状態:** `CLOSED_BY_SELF_CONTAINED_R02`

旧Finalはsuperseded summaryへ変更し、標準本文を `docs/stage12-n1-2-final-r02.md` とした。

## 3. Bundle integrity

```text
BUNDLE_ID=PC-N1-2-REPAIRED-PROOF-20260807-R02
SOURCE_SNAPSHOT_COMMIT=08a3bc0b8428f9c620269da9b488e8b849cf909c
SOURCE_LEDGER_SHA256=26528cd336fe4b6ce5bc70bdca368ad605f29f711bec71e34a6427d98b3560dc
REVIEW_PAGE=review/PC-N1-2-REPAIRED-PROOF-20260807-R02.html
```

`verify_stage12_n1_review_manifest.py` は、source blob ledger、4重handshake、end marker、control characters、旧Final supersessionを検査する。

## 4. Remaining exit condition

R01で要求された修復作業は完了した。Stage12-N1-2を再び `CLOSED` と呼ぶために残る条件は一つである。

```text
INDEPENDENT_REAUDIT_R02_VERDICT=CLOSED
```

再監査が新しいMAJORまたはFATALを返した場合は、その指摘を新しいrepair cycleとして扱う。

## 5. Current codes

```text
STAGE12_N1_3A_RECTANGULAR_ERROR_REPAIR_COMPLETE
STAGE12_N1_3B_FIXED_CIRCLE_REMAINDER_COMPLETE
STAGE12_N1_3C_G_RESIDUE_FIRST_TRANSFER_COMPLETE
STAGE12_N1_3D_SELF_CONTAINED_BUNDLE_COMPLETE
MAJOR_01=CLOSED
MAJOR_02=CLOSED
MAJOR_03=CLOSED
MAJOR_04=CLOSED
CLARIFICATION_01=CLOSED
MINOR_01=CLOSED
MINOR_02=CLOSED
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_INDEPENDENT_REAUDIT
NEXT_TASK=INDEPENDENT_REAUDIT_OF_R02_BUNDLE
```