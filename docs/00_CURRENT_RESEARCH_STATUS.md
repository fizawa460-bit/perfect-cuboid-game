# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-1051-JST`
>
> **CURRENT_BASE_COMMIT:** `f34feb38135ed97283220dfdb659dfeecdc6ab5c`
>
> **CURRENT_STAGE:** `Stage12-N1-3c.G completed; Stage12-N1-3d next`
>
> **STAGE13_STATUS:** `PAUSED_AFTER_STAGE13_2`
>
> **SERIES_STATUS:** `STAGE12_REOPENED_REPAIRABLE_NOT_CLOSED`
>
> **AUDIT_VERDICT:** `REPAIRABLE`
>
> **RESOLVED_AFTER_AUDIT:** `MAJOR-01, MAJOR-02, MAJOR-03`
>
> **OPEN_MAJOR:** `MAJOR-04`

## 0. 60秒で現状復帰する順序

1. `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/review/stage12-n1-2-full-audit-r01.md`
3. `docs/stage12-n1-2-repair-status-r01.md`
4. `docs/stage12-n1-3a-rectangular-error-repair.md`
5. `docs/stage12-n1-3b-fixed-circle-remainder.md`
6. `docs/stage12-n1-3c-coupled-region-transfer.md`
7. `docs/stage12-n1-3c-g-residue-first-closure.md`

Stage13-1とStage13-2の構造的成果は保持するが、Stage13-3以降はStage12修復と独立再監査が終わるまで進めない。

## 1. 現在の判断

候補漸近式

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
\]

は独立監査R01で否定されていない。監査で指摘された中心解析項MAJOR-01〜03は修復文書上で閉じた。

ただし、MAJOR-04、参照・記号修正、新しい統合稿、自己完結bundle、独立再監査が残るため、まだ

```text
THEOREM_STATUS=REPAIRABLE_NOT_CLOSED
```

である。

旧Finalは統合候補稿として保存するが、次の箇所はsupersedeされている。

- 旧Final §1 fixed-circle remainder → Stage12-N1-3b;
- 旧Final §4 rectangular error → Stage12-N1-3a;
- 旧Final §5 coupled-region transfer → Stage12-N1-3c.G。

## 2. 閉じた修復

### MAJOR-01 — Stage12-N1-3a

不成立な `R^(1/2+δ)S` 型への指数強化を撤回し、

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
\]

型の正しい一様長方形誤差へ修正した。

### MAJOR-02 — Stage12-N1-3b

`ω(X/ℓ)` を `ω(X)` として引き出す操作を撤回し、

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1
+O\!\left(G(rs)H_{\rm abs}(rs)X^{1/2}\right)
\]

を証明した。retained regionのouter averageは任意の固定対数冪より小さい。

### MAJOR-03 — Stage12-N1-3c / 3c.G

3cでexact variable ledger、fixed-divisor model、model Stieltjes calculationを復元した。その結果残ったfixed-`(b,c)` anisotropic kernel lemmaは、最終漸近式に必要な主張より強いと判明した。

3c.Gでは除数展開を元へ戻し、

\[
g(n)=\pi\gamma(n)=(1*\beta)(n)
\]

を用いて元変数 `(r,s)` 上のparity-weighted coprime rectangle sumを直接平均した。

二変数Dirichlet級数は

\[
D_\lambda(s_1,s_2)
=
G(s_1)G(s_2)C_\lambda(s_1,s_2),
\]

\[
G(s)=\zeta(s)^2H_g(s),
\]

と分解される。`C_lambda` は `Re(s_1+s_2)>1` で絶対収束し、標準一変数Selberg–Delangeの `z=2` 特殊形を二回使うことで、長方形leading coefficientは

\[
C_\lambda^{(0)}
=
\frac8{\pi^2}\eta
\]

となる。

元変数上でradial kernelをStieltjes移送すると

\[
\mathcal H_\lambda(B)
=
\frac\eta{12\pi}(\log B)^3
+o((\log B)^3).
\]

したがってresidue mainは

\[
\mathcal M(B)
\sim
\frac\eta{12\pi^2}B(\log B)^3
=
\frac\kappa{12\pi}B(\log B)^3.
\]

orientationは係数とkernelの対称性で正確に半分となり、primitive diagonalは `(1,1)` だけである。odd–odd cutoff `2B` とcommon cutoff `B` の差、radial arc、shallow boxesはすべてlower orderである。

```text
OLD_3C_G_FIXED_DIVISOR_KERNEL=SUPERSEDED_NOT_REQUIRED
MAJOR_03=CLOSED_BY_STAGE12_N1_3C_G
```

## 3. 次の作業 — Stage12-N1-3d

対象はMAJOR-04。

成果物は次を予定する。

```text
docs/stage12-n1-3d-definition-sheet.md
docs/stage12-n1-3d-constant-sheet.md
```

最低限、次を自己完結にする。

1. `C_prim(B)` の完全なcounting definition;
2. raw / primitive / oriented / canonical の区別;
3. `β`, `γ`, `g`, `ρ`, `η`, `κ` の定義;
4. odd-prime local factors;
5. 2-adic front factor;
6. archimedean sector / radial factors;
7. `η=πκ` のlocal comparison;
8. 3a、3b、3c.Gが旧文書をsupersedeする参照表。

MAJOR-04は文書量が大きいが、現時点では新しい中心解析補題ではなく、監査可能性と自己完結性の修復である。

## 4. Secondary items

- Tenenbaumの使用版、定理番号、`z=1` と `z=2` の採用形を固定する;
- 2j原文中の壊れた `\frac` 2件を修正する;
- Finalを3a〜3c.Gで再統合する;
- self-contained bundleを生成する;
- 独立再監査へ提出する。

## 5. 禁止事項

- Stage12-N1-2をまだ `CLOSED`, `FINAL_COMPLETE`, `proved` と呼ばない。
- fixed-`(b,c)` kernel lemmaを証明済みと主張しない。これは不要としてsupersedeした。
- 現行旧Finalを確定稿として配布しない。
- 現行bundleを自己完結と呼ばない。
- Stage12からStage13 canonical countへの定数変換を先取りしない。
- ユーザーの明示依頼なしにPRをマージしない。

## 6. 再閉包条件

次のすべてを満たした時だけStage12-N1-2を再びclosedと呼ぶ。

- MAJOR-01〜03の本文上の修復が完了している; `DONE`
- MAJOR-04を解消した自己完結bundleがある;
- control characterと参照条件が修正されている;
- 新しい統合稿がある;
- 独立監査が `CLOSED` を返している。

## 7. 状態コード

```text
STAGE12_N1_3A_RECTANGULAR_ERROR_REPAIR_COMPLETE
STAGE12_N1_3B_FIXED_CIRCLE_REMAINDER_COMPLETE
STAGE12_N1_3C_G_RESIDUE_FIRST_TRANSFER_COMPLETE
MAJOR_01=CLOSED
MAJOR_02=CLOSED
MAJOR_03=CLOSED
MAJOR_04=OPEN_NEXT
THEOREM_STATUS=REPAIRABLE_NOT_CLOSED
STAGE13_3_PAUSED_PENDING_STAGE12_REPAIR
NEXT_TASK=STAGE12_N1_3D_SELF_CONTAINED_DEFINITION_AND_CONSTANT_SHEETS
```
