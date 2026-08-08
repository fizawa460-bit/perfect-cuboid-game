# Stage13 R04 external review — Claude

> PROVENANCE: `USER_RELAYED_EXTERNAL_REVIEW`
>
> TARGET_BUNDLE_ID: `STAGE13-FINAL-SELF-CONTAINED-20260809-R04`
>
> TARGET_CONTENT_SHA256: `789656b5bb2190ae62cf2dcae7a3da06ece4f473780a1229ba7284b10b7f4f1b`
>
> RECORDED_VERDICT: `OPEN`

## Reviewer text

R04を通読しました。全体は非常に精密に組まれていますが、一つ看過できない構造的な問題があります。

**最大の問題:数値監査が主張する漸近比率を裏付けていない**

証明の核心(§7〜9)は「Θ(算術定数)がqに依存しない」ことを示し、方向比はアルキメデス的重みJ_qだけで決まると結論しています。理論上の極限比率は

- I_ab : I_ac : I_bc ≈ 0.5347 : 0.2454 : 0.2199(direction_vector)

一方、同じ文書内のB=100000での実測(exactly_one = 84146, 43180, 40704)を比率にすると

- 0.5008 : 0.2570 : 0.2423

これは理論極限よりも明らかに「2:1:1」に近い値です。文書自体も§2で「limiting directional proportions are not 2:1:1」と明言しているので、理論とユーザーの元々の発見(d≤10^6でもほぼ2:1:1を維持)は正面から矛盾しています。

この乖離について文書はどこにも言及・調和させていません。log収束が遅い(誤差項がO(1/log B)オーダー)ことで説明可能ではありますが、それは「たぶん収束が遅いだけ」という仮説であって検証されていません。もし収束が遅いだけでないなら、Θがqに独立という中心主張自体に、まだ捕捉されていないq依存の算術因子が残っている可能性があります。これは「FINAL」と銘打つには致命的な未処理のギャップです。

**その他の弱点**
- §5の`‖C_{ℓ,p}−1‖_{5/8} ≤ 529p^{-5/4}`という定数529が導出過程なしに天下り的に提示されている。
- §7の境界・小成分誤差評価("smaller than every fixed negative power of log B"等)は定性的主張のみで、O((log B)^C)個の箱にわたる一様性の実際の証明がない。

**検証したい点があれば**
外部文献(Merikoski 2025、Huang–Liu–Rudnick等)の実在性確認、あるいはセクション2/3(crosswalk/ledger)の残り部分の精査が必要なら指示してください。今回は上記の数値矛盾が最も重大だと判断し、そこに焦点を当てました。

## Gate interpretation

The review does not logically disprove an asymptotic theorem merely from finite-`B` disagreement. However, it raises an unresolved theorem-level challenge to the canonical proof/finalization package:

1. the finite directional counts remain substantially closer to `2:1:1` than to the claimed limiting vector;
2. R04 contains no quantitative convergence analysis demonstrating that the observed discrepancy is compatible with the proved remainder;
3. a direction-dependent secondary arithmetic contribution or an omitted direction-dependent leading factor has not been independently excluded by this review;
4. the reviewer also flags two proof-explicitness issues: the origin of the constant `529` and uniform accumulation of the curved-region box errors.

Accordingly this review is recorded as `OPEN`, not `CLOSED` and not merely stylistic.

## Required resolution before freeze

A repair/closure pass under `13-13f` must at minimum:

- audit finite directional data over all currently available cutoffs and compare convergence to the claimed vector;
- distinguish rigorously between an allowed finite-`B` secondary term and a missing direction-dependent leading term;
- trace the proof of q-independence of the top arithmetic coefficient through the local Euler/Wiener factors without using finite fitting;
- expose the derivation of the `529 p^{-5/4}` bound or replace it by a directly auditable bound;
- make the box-count/uniform error accumulation in the curved-region argument explicit enough to verify after summing `O((log B)^C)` boxes.

If these checks require substantive changes to the reviewed canonical proof, R04 must remain immutable and a new R05 bundle must be generated.

```text
CLAUDE_R04_VERDICT=OPEN
THEOREM_LEVEL_OBJECTION_RECEIVED=true
UNRESOLVED_THEOREM_LEVEL_OBJECTIONS>=1
R04_REPAIR_OR_CLOSURE_AUDIT_REQUIRED=true
PROMOTE_TO_13_13G=false
```
