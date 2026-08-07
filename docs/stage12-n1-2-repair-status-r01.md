# Stage12-N1-2 repair status after full audit R01

> **STATUS:** `REPAIRABLE — NOT CLOSED`
>
> **AUDIT_DATE:** `2026-08-07`
>
> **AUDIT_COUNTS:** `FATAL=0, MAJOR=4, MINOR=2, CLARIFICATION=1`
>
> **RESOLVED_AFTER_AUDIT:** `MAJOR-01, MAJOR-02, MAJOR-03`
>
> **OPEN_MAJOR:** `MAJOR-04`
>
> **NEXT_TASK:** `STAGE12_N1_3D_SELF_CONTAINED_DEFINITION_AND_CONSTANT_SHEETS`

## 1. Project decision

Stage13-3以降を一時停止し、Stage12-N1-2を再オープンして修復している。

候補漸近式

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
\]

は監査R01で否定されていない。ただし、MAJOR-04、二次項目、統合稿、自己完結bundle、独立再監査が完了するまで `CLOSED`, `FINAL_COMPLETE`, `proved` と扱わない。

監査原文:

```text
docs/review/stage12-n1-2-full-audit-r01.md
```

修復成果物:

```text
docs/stage12-n1-3a-rectangular-error-repair.md
docs/stage12-n1-3b-fixed-circle-remainder.md
docs/stage12-n1-3c-coupled-region-transfer.md
docs/stage12-n1-3c-g-residue-first-closure.md
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

を直接証明した。retained regionのouter averageは任意の固定対数冪より小さい。

### MAJOR-03 — coupled-region transfer

**状態:** `CLOSED_BY_STAGE12_N1_3C_G_RESIDUE_FIRST_TRANSFER`

Stage12-N1-3cでは、除数変数 `(b,c)` を固定したexact kernelまで変数台帳を復元し、model kernelと `L^3/12` のStieltjes計算を書いた。その過程で、fixed-`(b,c)` anisotropic kernel remainderを平均する旧補題3c.Gが残った。

Stage12-N1-3c.Gでは、このfixed-divisor statementが最終漸近式に必要な主張より強いことを確認した。除数展開を元へ戻し、

\[
g(n):=\pi\gamma(n)=(1*\beta)(n)
\]

を用いて元変数 `(r,s)` 上のparity-weighted coprime rectangle sumを直接平均する。

二変数Dirichlet級数は

\[
D_\lambda(s_1,s_2)
=
G(s_1)G(s_2)C_\lambda(s_1,s_2),
\]

\[
G(s)=\zeta(s)^2H_g(s),
\]

と分解され、`C_lambda` は `Re(s_1+s_2)>1` で絶対収束する。標準一変数Selberg–Delangeの `z=2` 特殊形を二回適用して、元変数上の長方形和はleading term

\[
C_\lambda^{(0)}RS\log R\log S
\]

を持つ。

local factor計算により

\[
C_\lambda^{(0)}
=
\frac8{\pi^2}\eta.
\]

radial kernel `1/(r^2+s^2)` を元変数上で直接Stieltjes移送すると、full quadrantのleading integralは

\[
\frac\pi{48}(\log B)^3,
\]

orientation `r<s` は対称性により半分となる。従って

\[
\mathcal H_\lambda(B)
=
\frac\eta{12\pi}(\log B)^3
+o((\log B)^3).
\]

外側の `B/pi` を戻して

\[
\mathcal M(B)
\sim
\frac\eta{12\pi^2}B(\log B)^3
=
\frac\kappa{12\pi}B(\log B)^3.
\]

retained boxesではrectangle errorが超対数的に小さく、shallow boxesは `o((log B)^3)`、radial arcとodd–odd cutoff `B`/`2B` の差は `O((log B)^2)` である。

したがってfixed-`(b,c)` kernel lemmaは

```text
OLD_3C_G_FIXED_DIVISOR_KERNEL=SUPERSEDED_NOT_REQUIRED
NEW_3C_G_RESIDUE_FIRST_RECTANGLE=PROVED
NEW_3C_G_RADIAL_TRANSFER=PROVED
```

として処理し、MAJOR-03を閉じる。

### MAJOR-04 — review self-containment

**状態:** `OPEN — NEXT / DOCUMENTATION AND AUDITABILITY`

新しいbundleへ以下を追加する。

- `C_prim(B)` の完全なcounting definition;
- `κ`, `η`, local factors;
- 2-adic / archimedean front factors;
- 3a、3b、3c.Gが旧主張をどこでsupersedeするかの参照表。

MAJOR-04は文書量が大きいが、現時点で新しい中心解析補題は要求しない。

## 3. Secondary items

- Tenenbaumの使用版、定理番号、`z=1` と `z=2` の採用形を一対一で固定する。
- 2j原文中の壊れた `\frac` 2件を修正する。
- Finalをsummary documentと明記するか、未定義記号を補う。
- 現行Final §1、§4、§5を3b、3a、3c.Gで置き換える。
- 自己完結bundleを生成し、独立再監査へ提出する。

## 4. Repair order

1. ~~MAJOR-01 rectangular error~~ `CLOSED_BY_STAGE12_N1_3A`
2. ~~MAJOR-02 fixed-circle remainder~~ `CLOSED_BY_STAGE12_N1_3B`
3. ~~MAJOR-03 coupled-region transfer~~ `CLOSED_BY_STAGE12_N1_3C_G`
4. **MAJOR-04 definition sheet / constant sheet / self-contained bundle**
5. secondary reference and notation repairs
6. new integrated final
7. independent audit

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
STAGE12_N1_3C_G_RESIDUE_FIRST_TRANSFER_COMPLETE
MAJOR_01=CLOSED
MAJOR_02=CLOSED
MAJOR_03=CLOSED
MAJOR_04=OPEN_NEXT
THEOREM_STATUS=REPAIRABLE_NOT_CLOSED
NEXT_TASK=STAGE12_N1_3D_SELF_CONTAINED_DEFINITION_AND_CONSTANT_SHEETS
```
