# Stage13-13f — Grok R04 review verdict

> REVIEWER: `Grok`
>
> VERDICT: `CLOSED`
>
> TARGET_BUNDLE_ID: `STAGE13-FINAL-SELF-CONTAINED-20260809-R04`
>
> TARGET_CONTENT_SHA256: `789656b5bb2190ae62cf2dcae7a3da06ece4f473780a1229ba7284b10b7f4f1b`
>
> PROVENANCE: `USER_RELAYED_EXTERNAL_REVIEW`
>
> RECEIVED_DATE_JST: `2026-08-09`

## Reviewer conclusion

R04 の正準証明は、R01–R03 で指摘された全ギャップを構造的に解消し、外部依存を最小限に切り詰めた自己完結した形になっている。敵対的に追っても、中央の定理レベルに致命的・重大な欠陥は残らない。

## Adversarial checks reported by reviewer

### 1. 非循環性と共通 Θ

正準証明は厳密に順序を固定している：

- `j=0` 局所係数系 → 純因子 → 混合補正（weighted-Wiener）→ 矩形主項 → 曲領域移行。
- ここで初めて共通算術スカラー `Θ` が得られ、カテゴリは `J_q` のみを通じて入る。
- Stage12 総定理は共通性確立後にのみ使用される（§9）。
- Vaaler 誤差での Stage12 使用は正の majorant に限定され、方向比例を製造しない。

Reviewer assessment: 循環の再導入はない。

### 2. 解析的 `J_q = 2I_q/pi`

§3 の変数変換

```text
psi = 2 phi - pi/2
d psi = 2 d phi
k_q = (4/pi) ell_q
```

から厳密に導出されており、数値積分は検証子に限定される。Fubini/Tonelli の条件も非負性と有限測度で内部的に処理されている。

### 3. 混合補正と誤差予算

明示的 Wiener 評価

```text
||C_{ell,p}-1||_{5/8} <= 529 p^{-5/4}  (p >= 13)
```

が全角周波数に一様。log-moment も一様有限で、畳み込みシフトが leading 次数を変えないことを保証する。

固定パラメータ

```text
H0 = U = exp((log B)^(1/4))
eta = (log B)^(-8)
L = (log B)^4
A = 48
```

のもとで、全誤差項が `o(B(log B)^3)` の台帳として明示されている。

### 4. 特殊 Perron/residue 補題

pole order `0/1/2` のみを扱う内部補題により、一般 Selberg–Delange black-box は不要。非零調和では

```text
A_ell(s) = L(s, xi_{8ell}) E
```

で zeta 極がなく、零点は contour を妨げない。Merikoski の零領域は「有効だが論理的に冗長」と正しく位置付けられている。

### 5. inert 局所状態と `lambda_p`

- primitivity により `v_p(h)=0` を強制。
- 残存状態は正確に `U / R_b / S_c`。
- 単位状態の受理
  `alpha_p=(p+1)/(2(p-1))`
  を Jacobi 和と二次指標の初等計算で記号的に導出。
- `lambda_p=(p+5)/(2(p+1)) <= 3/4` (`p>=7`) が明示。
- 固定集合 `S_k` を先に固定し、`B->infinity`、その後 `k->infinity` の順序が明確。
- tag 因子 `2` は安全な上界。

### 6. 外部依存の最小化

13-13b crosswalk により必要最小限は：

```text
Stage12 R09 total theorem
Hecke/Dirichlet analytic continuation + functional equation + polynomial growth
Vaaler 1985 interval approximation
```

一般 Selberg–Delange、Gaussian-Hecke 零領域、Dirichlet 等差定理は内部化または冗長化。成長する modulus の定理は使用されていない。

### 7. 決定論的一貫性監査

chamber 積分、正規化ベクトル、`J_q` bridge、factor-2 bridge、inert 受理数が独立に再現され、superseded 公式の core scan も zero hit。

## Minor-or-lower observations

Reviewer explicitly classified the remaining observations as `MINOR` or below:

- constants such as `529` and `48` are loose but sufficiently separated from the main scale;
- Hecke polynomial growth is treated as standard, and no issue is identified in the fixed-field/fixed-conductor setting used here;
- no perfect-cuboid nonexistence assumption is used.

None is an actionable theorem-level objection.

## Final reviewer decision

```text
VERDICT=CLOSED
FATAL_DEFECTS=0
MAJOR_DEFECTS=0
UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=0
REPAIR_REQUIRED=false
```

The wording above is a repository transcription of a review result relayed by the user. It does not claim direct machine authentication of the external reviewer identity.
