# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-CURRENT-20260807-1040-JST`
>
> **CURRENT_BASE_COMMIT:** `f34feb38135ed97283220dfdb659dfeecdc6ab5c`
>
> **CURRENT_STAGE:** `Stage12-N1-3c in progress — geometric kernel lemma open`
>
> **STAGE13_STATUS:** `PAUSED_AFTER_STAGE13_2`
>
> **SERIES_STATUS:** `STAGE12_REOPENED_REPAIRABLE_NOT_CLOSED`
>
> **AUDIT_VERDICT:** `REPAIRABLE`
>
> **RESOLVED_AFTER_AUDIT:** `MAJOR-01, MAJOR-02`
>
> **PARTIALLY_RESOLVED:** `MAJOR-03`
>
> **OPEN_MAJOR:** `MAJOR-03-GEOMETRIC-KERNEL, MAJOR-04`
>
> **MERGE_STATUS:** `DO_NOT_MERGE_CURRENT_3C_BRANCH`

## 0. 60秒で現状復帰する順序

1. `docs/00_CURRENT_RESEARCH_STATUS.md`
2. `docs/review/stage12-n1-2-full-audit-r01.md`
3. `docs/stage12-n1-2-repair-status-r01.md`
4. `docs/stage12-n1-3a-rectangular-error-repair.md`
5. `docs/stage12-n1-3b-fixed-circle-remainder.md`
6. `docs/stage12-n1-3c-coupled-region-transfer.md`
7. 必要に応じてarchiveの2e、2f、2m、2n、2oを参照する

Stage13-1とStage13-2の構造的成果は保持するが、Stage13-3以降はStage12修復が終わるまで進めない。

## 1. 現在の判断

候補漸近式

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
\]

は独立監査R01で否定されていない。しかし、修復と再監査が完了するまで `CLOSED`, `FINAL_COMPLETE`, `proved` と扱わない。

```text
THEOREM_STATUS=PLAUSIBLE_BUT_NOT_CLOSED
VERDICT=REPAIRABLE
```

旧Finalは統合候補稿として保存するが、次の箇所は既にsupersedeされている。

- 旧Final §1 fixed-circle remainder → Stage12-N1-3b;
- 旧Final §4 rectangular error → Stage12-N1-3a;
- 旧Final §5 coupled-region transfer → Stage12-N1-3cで再構成中。

## 2. 閉じた修復

### MAJOR-01 — Stage12-N1-3a

不成立な `R^(1/2+δ)S` 型への指数強化を撤回し、

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
\]

型の正しい一様長方形誤差へ修正した。

```text
MAJOR_01=CLOSED_BY_STAGE12_N1_3A
```

### MAJOR-02 — Stage12-N1-3b

`ω(X/ℓ)` を `ω(X)` として引き出す操作を撤回し、

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1
+O\!\left(G(rs)H_{\rm abs}(rs)X^{1/2}\right)
\]

を証明した。retained regionのouter averageは任意の固定対数冪より小さい。

```text
MAJOR_02=CLOSED_BY_STAGE12_N1_3B
```

## 3. Stage12-N1-3cで今回確定した部分

成果物:

```text
docs/stage12-n1-3c-coupled-region-transfer.md
```

### 3.1 exact variable ledger

residue mainを

\[
\mathcal M(B)
=
\frac{B}{\pi}
\sum_{(b,c)=1}
\beta(b)\beta(c)\mathcal K_B(b,c)
\]

へ戻した。exact kernelは

\[
\mathcal K_B(b,c)
=
\sum_{u,v\ge1\atop
(u,v)=1,(u,c)=1,(v,b)=1,bu<cv}
\frac{\lambda(u,v)}{b^2u^2+c^2v^2}
\mathbf1_{b^2u^2+c^2v^2\le\lambda(u,v)B}.
\]

これにより、元変数 `(r,s)`、divisor variables `(b,c)`、倍数変数 `(u,v)`、radial kernel、height branch、orientationが一つの等式で接続された。

### 3.2 model kernelとlocal constant

local-density / archimedean modelは

\[
\mathcal K_B^{\rm main}(b,c)
=
\frac{\rho(bc)}{\pi bc}
[L-2\max(\log b,\log c)]_+.
\]

`α=βρ` と置くと、density-corrected rectangle residue constantはlocal factorごとに `η` と一致する。

### 3.3 Stieltjes transferと係数 `1/12`

model kernelへ到達した後の二変数Stieltjes移送を完全に書き、

\[
\int_{2\max(y,z)<L}
(L-2\max(y,z))\,dy\,dz
=
\frac{L^3}{12}
\]

を得た。従ってmodel mainは

\[
\frac{\eta}{12\pi^2}B(\log B)^3
=
\frac{\kappa}{12\pi}B(\log B)^3.
\]

Stage12-N1-3a型rectangle errorがmodel Stieltjes kernelに適合することも確認した。

## 4. 発見した中心残件

exact kernelとmodel kernelとの差

\[
\mathcal R_B(b,c)
=
\mathcal K_B(b,c)-\mathcal K_B^{\rm main}(b,c)
\]

について

\[
\sum_{(b,c)=1}
\beta(b)\beta(c)\mathcal R_B(b,c)
=o((\log B)^3)
\]

を示す必要がある。

これは単なる表示補正ではなく、次を同時に制御する平均格子点問題である。

- anisotropy `b/c`;
- primitive condition `(u,v)=1`;
- side exclusions `(u,c)=1`, `(v,b)=1`;
- odd–odd / opposite-parity cutoff;
- orientation boundary `bu=cv`;
- radial arc boundary;
- `(b,c)` weighted average。

素朴なper-`(b,c)` perimeter estimateではdivisor-lossが主項と同次数へ戻る危険がある。従って、現時点でMAJOR-03をclosedとは呼ばない。

```text
MAJOR_03=PARTIAL
SUBITEM_03_EXACT_REDUCTION=CLOSED
SUBITEM_03_MODEL_STIELTJES=CLOSED
SUBITEM_03_GEOMETRIC_KERNEL_AVERAGE=OPEN_CENTRAL
```

## 5. 次の作業

Stage12-N1-3cの必要補題 `3c.G` を閉じる。

候補経路:

1. anisotropic primitive lattice discrepancyのmodulus平均;
2. smooth radial partition + Poisson / large sieve;
3. Möbius variablesとdivisor variablesの先行再編成;
4. exact kernelのMellin表示とcontour平均。

この経路選定と証明が終わるまで、現在の3c branch / PRはマージしない。

## 6. その後

### MAJOR-04

自己完結bundleへ

- `C_prim(B)` の完全定義;
- `κ`, `η`, local factors;
- 2-adic / archimedean front factors

を追加する。

### Secondary

- Tenenbaum II.5.2の使用形を原典と一対一で固定;
- 2jの壊れた `\frac` 2件を修正;
- Final再統合;
- self-contained bundle R02生成;
- 独立再監査。

## 7. 禁止事項

- Stage12-N1-2を `CLOSED`, `FINAL_COMPLETE`, `proved` と呼ばない。
- exact kernel remainderを評価済みと扱わない。
- model `L^3/12` 計算だけでMAJOR-03を閉じない。
- 現在の3c branchをマージしない。
- 現行bundleを自己完結と呼ばない。
- Stage12からStage13 canonical countへの定数変換を先取りしない。

## 8. 状態コード

```text
STAGE12_N1_3A_RECTANGULAR_ERROR_REPAIR_COMPLETE
STAGE12_N1_3B_FIXED_CIRCLE_REMAINDER_COMPLETE
STAGE12_N1_3C_EXACT_REDUCTION_AND_MODEL_STIELTJES_COMPLETE
MAJOR_01=CLOSED
MAJOR_02=CLOSED
MAJOR_03=PARTIAL_GEOMETRIC_KERNEL_OPEN
MAJOR_04=OPEN
THEOREM_STATUS=REPAIRABLE_NOT_CLOSED
MERGE_STATUS=DO_NOT_MERGE
NEXT_TASK=STAGE12_N1_3C_GEOMETRIC_KERNEL_LEMMA
```
