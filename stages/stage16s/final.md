# Stage16S final self-contained interface bundle — R01

```text
BUNDLE_ID=STAGE16S-FINAL-SELF-CONTAINED-20260814-R01
STATUS=AUDITED_PASS_CLOSED
STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
SOURCE_SNAPSHOT_BASE=ed47f22d516d80d4a1a66288962c1a646282854f
SELF_CONTAINMENT=SELF_CONTAINED_WITH_STATED_EXTERNAL_THEOREMS
```

## Executive theorem

Let `R=sqrt(a^2+b^2+c^2)`. For primitive canonical positive triples `0<a<b<c`, `gcd(a,b,c)=1`, `R<=B`, define

- `S_all(B)`: `R` integral;
- `S_0(B)`: `R` integral and none of `a^2+b^2`, `a^2+c^2`, `b^2+c^2` is a square.

Write `N_S^all=#S_all`, `N_S^0=#S_0`. Then, with Catalan's constant `G=L(2,chi_4)`,

\[
N_S^{all}(B)\sim B^2/(32G),\qquad N_S^0(B)\sim B^2/(32G).
\]

For the ambient count

\[
U(B)=\#\{0<a<b<c:\gcd(a,b,c)=1,R\le B\},
\]

completed Stage16 gives

\[
U(B)=\pi B^3/(36\zeta(3))+O(B^2).
\]

Hence

\[
\frac{N_S^{all}(B)}{U(B)}\sim\frac{9\zeta(3)}{8\pi G}B^{-1},
\qquad
\frac{N_S^0(B)}{U(B)}\sim\frac{9\zeta(3)}{8\pi G}B^{-1}.
\]

If `C_F(B)=N_S^all(B)-N_S^0(B)`, then for every `epsilon>0`,

\[
C_F(B)=O_\varepsilon(B^{1+\varepsilon}),
\qquad N_S^0(B)/N_S^all(B)\to1.
\]

Thus the integral-space-diagonal condition intrinsically costs one power of `B` in the ambient population, while deleting all integral-face cases does not change the quadratic main term.

## Population and cutoff lock

On every target object the positive space diagonal `d` satisfies `d^2=a^2+b^2+c^2=R^2`, so `d=R` and `d<=B` iff `R<=B`. No height adapter is needed.

Stage16 is a frozen upstream interface:

```text
UPSTREAM_STAGE=Stage16
UPSTREAM_THEOREM=U(B)=pi/(36*zeta(3))*B^3+O(B^2)
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

## External theorem contract

The theorem-level external input is Werner Hürlimann, JIS 18 (2015), Article 15.2.5.

```text
THEOREM=Hurlimann 2015 Theorem 7 plus repeated-edge N_2(x;2)
WORKING_FORM=N_3^H(x) ~ x^2/(32G) for distinct primitive positive Pythagorean cuboids with odd diagonal <=x; repeated-edge family N_2(x;2)=O(x)
OBJECT=x^2+y^2+z^2=t^2 modulo edge permutation
HYPOTHESES_CHECKED=positive; primitive; odd diagonal; diagonal cutoff; unordered edge convention
HEIGHT_OR_MEASURE_MATCH=exact after d=R and the strict-order correction proved below
QUANTIFIERS=x->infinity; no growing project parameter
UNIFORMITY_NOT_CLAIMED=no effective error term imported
ROLE=SPACE_AT_LEAST main term and lower-order equality correction
```

The published proof remains external. The project-specific adapters follow.

## Adapter proofs

**Odd diagonal.** If primitive `a^2+b^2+c^2=d^2` had even `d`, then the sum of three squares would be `0 mod 4`. Since squares are `0` or `1 mod 4`, all three edges would be even, contradicting `gcd(a,b,c)=1`. Thus every primitive Stage16S object has odd `d`.

**Primitivity.** If `g=gcd(a,b,c)`, then `g^2|d^2`, hence `g|d`. Therefore on the space equation

\[
\gcd(a,b,c)=1\iff\gcd(a,b,c,d)=1.
\]

**Strict canonical ordering.** An all-equal positive solution would give `3a^2=d^2`, impossible. Any repeated-edge object therefore has exactly two equal edges and, after permutation, satisfies `x^2+2y^2=d^2`. This is Hürlimann's repeated-edge term. Consequently

\[
N_S^{all}(B)=N_3^H(B)-N_2(B;2).
\]

Since `N_2(B;2)=O(B)`,

\[
N_S^{all}(B)\sim B^2/(32G).
\]

Combining this with the exact Stage16 ambient interface gives the printed `B^-1` ratio constant by direct division.

## Faceful complement proof

Mark one integral face, say `a^2+b^2=e^2`. Together with the space diagonal,

\[
a^2+b^2=e^2,\qquad e^2+c^2=d^2,\qquad d\le B.
\]

Dropping primitivity and canonical filters only enlarges the count. For fixed `d`, the number of `(e,c)` is at most `r_2(d^2)<=4 tau(d^2)`. For each `e`, the number of `(a,b)` is at most `r_2(e^2)<=4 tau(e^2)`. The standard divisor bound `tau(n)<<_eta n^eta`, with `eta` chosen small relative to a prescribed `epsilon`, gives `O_epsilon(B^epsilon)` marked-face objects for each `d`. Summing `d<=B` and then over three faces gives

\[
C_F(B)=O_\varepsilon(B^{1+\varepsilon}).
\]

Since `N_S^all(B)~B^2/(32G)`, the complement is `o(B^2)`, so

\[
N_S^0(B)\sim B^2/(32G),\qquad N_S^0(B)/N_S^all(B)\to1.
\]

No sharp order for `C_F` is claimed.

## Causal and Stage17 interface

The ambient population has cubic order, while the primitive Pythagorean-quadruple locus has quadratic order. Therefore `a^2+b^2+c^2=d^2` itself supplies the certified one-power loss.

Audited Stage17 gives

\[
N_1(B)/M_1(B)\asymp(\log B)^2/B.
\]

Stage16S therefore proves that Stage17's polynomial `B^-1` cost is not created only by first imposing one integral face. The differing logarithmic profile is real but is not interpreted as independence, correlation, or factorization here. Stage21 owns that final interaction classification.

```text
INTRINSIC_POLYNOMIAL_SPACE_COST=ONE_POWER_OF_B
STAGE17_POLYNOMIAL_COST_MATCH=true
STAGE17_LOG_PROFILE_MATCH=false
FINAL_INTERACTION_CLASSIFICATION=DEFER_TO_STAGE21
DOUBLE_CHARGE_CHECK=PASS
```

## Finite verification boundary

Stage16S-20 froze counts through `B=2000`: at the maximum cutoff `SPACE_AT_LEAST=136060`, `SPACE_ONLY=134621`, `face1=1434`, `face2=5`, `face3=0`. The optimized enumerator matched direct brute force through `B=200`, regenerated the frozen CSV, and matched Stage17's exactly-one counts at every shared threshold. These are `COMPUTED` diagnostics only and are not asymptotic proof input.

## Non-claims and stop rule

Stage16S does not prove a sharp asymptotic for `C_F`, separate asymptotics for face multiplicities 1/2/3, an effective Hürlimann error term, probabilistic independence/correlation, the meaning of Stage17's logarithmic enhancement, or any perfect-cuboid existence/nonexistence statement.

Further refinement needs a new theorem, sharper arithmetic analysis, new literature work, or Stage21 transition analysis, so the bounded-synthesis stop rule is satisfied.

## Provenance and hostile-review lock

Canonical records are `stages/stage16s/16s-{10,20,30,40,50,60}/`, `stages/stage16s/16s-70/result.md`, this bundle, `stages/stage16s/manifest-r01.md`, and the controller. Policy is `docs/stage16-28-population-roadmap.md`, `docs/stage16-28-stage70-policy.md`, and `docs/self-contained-review-standard.md`.

A fresh auditor must check the population/cutoff lock, Stage16 frozen interface, Hürlimann working form, odd-`d` proof, gcd adapter, repeated-edge subtraction, ratio algebra, divisor-bound complement proof, finite-data boundary, and Stage21 deferral.

```text
BUNDLE_ID=STAGE16S-FINAL-SELF-CONTAINED-20260814-R01
STATUS=AUDITED_PASS_CLOSED
PRIMARY_THEOREM=N_S^all(B) ~ B^2/(32G); N_S^0(B) ~ B^2/(32G)
AMBIENT_RATIO=N_S^all(B)/U(B) ~ [9 zeta(3)/(8 pi G)]/B
SPACE_ONLY_RATIO=N_S^0(B)/N_S^all(B) -> 1
FACEFUL_COMPLEMENT=C_F(B) <<_epsilon B^(1+epsilon)
EXTERNAL_THEOREM_WORKING_FORM_STATED=true
EXTERNAL_HYPOTHESES_MAPPED=true
INTERNAL_LOAD_BEARING_ADAPTERS_EMBEDDED=true
UPSTREAM_INTERFACES_EXACT=true
FINITE_DATA_PROMOTED_TO_THEOREM=false
INTRINSIC_POLYNOMIAL_SPACE_COST=ONE_POWER_OF_B
FINAL_INTERACTION_CLASSIFICATION=DEFER_TO_STAGE21
PERFECT_CUBOID_CONCLUSION=NONE
SYNTHESIS_STOP_RULE_SATISFIED=YES
FRESH_HOSTILE_REVIEW=PASS
AUDIT_REQUIRED=false
```

## Certified closeout status

This artifact was submitted as an audit candidate and was subsequently certified by [stages/stage16s/16s-70/audit.md](../stage16s/16s-70/audit.md) in PR #918. Current canonical status: `AUDITED_PASS_CLOSED`. Frozen mathematical claims and nonclaims are unchanged.
