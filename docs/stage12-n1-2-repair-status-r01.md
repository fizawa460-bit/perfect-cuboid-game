# Stage12-N1-2 repair status after full audit R01

> **STATUS:** `REPAIRABLE — NOT CLOSED`
>
> **AUDIT_DATE:** `2026-08-07`
>
> **AUDIT_COUNTS:** `FATAL=0, MAJOR=4, MINOR=2, CLARIFICATION=1`
>
> **RESOLVED_AFTER_AUDIT:** `MAJOR-01, MAJOR-02`
>
> **PARTIALLY_RESOLVED:** `MAJOR-03`
>
> **OPEN_MAJOR:** `MAJOR-03-GEOMETRIC-KERNEL, MAJOR-04`
>
> **CENTRAL_OPEN_ITEM:** `WEIGHTED_ANISOTROPIC_GEOMETRIC_KERNEL_REMAINDER`

## 1. Project decision

Stage13-3以降を一時停止し、Stage12-N1-2を再オープンして修復している。

候補漸近式

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
\]

は監査R01で否定されていないが、修復と再監査が完了するまで `CLOSED`, `FINAL_COMPLETE`, `proved` と扱わない。

監査原文:

```text
docs/review/stage12-n1-2-full-audit-r01.md
```

修復成果物:

```text
docs/stage12-n1-3a-rectangular-error-repair.md
docs/stage12-n1-3b-fixed-circle-remainder.md
docs/stage12-n1-3c-coupled-region-transfer.md
```

## 2. Repair ledger

### MAJOR-01 — rectangular error exponent

**状態:** `CLOSED_BY_STAGE12_N1_3A`

旧2pの不成立な

\[
R^{1/2+\delta}S+RS^{1/2+\delta}
\]

への指数強化を撤回し、任意の固定 `0<ε<1/8` に対する

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
\]

型の一様長方形誤差へ置き換えた。

### MAJOR-02 — fixed-circle remainder

**状態:** `CLOSED_BY_STAGE12_N1_3B`

旧2kの `ω(X/ℓ)` から `ω(X)` を引き出す操作を撤回し、

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1
+O\!\left(G(rs)H_{\rm abs}(rs)X^{1/2}\right)
\]

を直接証明した。retained regionのouter averageは

\[
O\!\left(BX_0^{-1/2}(\log B)^{O(1)}\right)
\]

で、任意の固定対数冪より小さい。

### MAJOR-03 — coupled-region transfer

**状態:** `PARTIAL — EXACT REDUCTION AND MODEL STIELTJES CLOSED; GEOMETRIC KERNEL OPEN`

Stage12-N1-3cで、residue mainを次のexact sumへ戻した。

\[
\mathcal M(B)
=
\frac{B}{\pi}
\sum_{(b,c)=1}
\beta(b)\beta(c)\mathcal K_B(b,c),
\]

\[
\mathcal K_B(b,c)
=
\sum_{u,v\ge1\atop
(u,v)=1,(u,c)=1,(v,b)=1,bu<cv}
\frac{\lambda(u,v)}{b^2u^2+c^2v^2}
\mathbf1_{b^2u^2+c^2v^2\le\lambda(u,v)B}.
\]

これにより、元変数 `(r,s)`、divisor variables `(b,c)`、倍数変数 `(u,v)`、radial kernel、height branch、orientationを一つの等式に接続した。

local-density / archimedean modelは

\[
\mathcal K_B^{\rm main}(b,c)
=
\frac{\rho(bc)}{\pi bc}
[L-2\max(\log b,\log c)]_+.
\]

`α=βρ` と置いたdensity-corrected rectangle constantはlocal factorごとに `η` と一致する。二変数Stieltjes移送を完全に書くことで

\[
\int_{2\max(y,z)<L}
(L-2\max(y,z))\,dy\,dz
=
\frac{L^3}{12}
\]

およびmodel main

\[
\frac{\eta}{12\pi^2}B(\log B)^3
=
\frac{\kappa}{12\pi}B(\log B)^3
\]

を得た。Stage12-N1-3a型rectangle errorがこのmodel Stieltjes kernelへ適合することも確認した。

ただし、exact kernelとの差

\[
\mathcal R_B(b,c)
=
\mathcal K_B(b,c)-\mathcal K_B^{\rm main}(b,c)
\]

について必要な

\[
\sum_{(b,c)=1}
\beta(b)\beta(c)\mathcal R_B(b,c)
=o((\log B)^3)
\]

は未証明である。

この残件は以下を同時に含む。

- anisotropy `b/c`;
- primitive condition `(u,v)=1`;
- side exclusions `(u,c)=1`, `(v,b)=1`;
- parity-dependent radial cutoff;
- orientation boundary `bu=cv`;
- arc boundary;
- `(b,c)` weighted average。

素朴なper-`(b,c)` perimeter errorではdivisor-lossにより主項と同次数へ戻る可能性があるため、現在の文書だけで閉じたとは扱わない。

**現在のPRは `DO_NOT_MERGE`。**

### MAJOR-04 — review self-containment

**状態:** `OPEN — DOCUMENTATION/AUDITABILITY`

新しいbundleへ以下を追加する。

- `C_prim(B)` の完全なcounting definition;
- `κ`, `η`, local factors, 2-adic / archimedean front factorsのconstant sheet。

## 3. Secondary items

- Tenenbaum II.5.2のhypothesisと採用remainder caseを一対一で固定する。
- 2j原文中の壊れた `\frac` 2件を修正する。
- Finalをsummary documentと明記するか、未定義記号を補う。
- 全修復後に現行Final §1、§4、§5を3b、3a、3cの成果で置換する。

## 4. 次の作業

Stage12-N1-3cを閉じるため、必要補題 `3c.G` を扱う。

候補経路:

1. congruence-restricted primitive lattice pointsのanisotropic familyに対する平均discrepancy;
2. smooth radial partition後のPoisson / large-sieve平均;
3. divisor variablesとMöbius variablesを先にまとめるEuler–Stieltjes再編成;
4. exact kernelの二変数Mellin表示とcontour errorの平均評価。

経路を選ぶまではMAJOR-04へ進まない。

## 5. Exit condition

Stage12-N1-2を再びclosedと呼ぶ条件は次のすべてである。

- MAJOR-01〜03の本文上の証明が完了している;
- MAJOR-04を解消した自己完結bundleが生成されている;
- control characterと参照条件が修正されている;
- 新しい独立監査が `CLOSED` を返している。

## 6. Current codes

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
