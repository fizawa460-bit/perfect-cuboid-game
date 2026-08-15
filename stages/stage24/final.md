# Stage24 final self-contained interface bundle — R01

```text
BUNDLE_ID=STAGE24-FINAL-SELF-CONTAINED-20260815-R01
STATUS=CANDIDATE_PENDING_FRESH_AUDIT
STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
SOURCE_SNAPSHOT_BASE=9c97d71d9207cc367313105c37d291b3be1f8564
SELF_CONTAINMENT=SELF_CONTAINED_WITH_STATED_EXTERNAL_THEOREMS
STAGE=Stage24
TRANSITION=Stage18 -> Stage19
```

## 1. Executive theorem

Let `M2(B)` count primitive canonical cuboids

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad R=\sqrt{a^2+b^2+c^2}\le B,
\]

with exactly two integral face diagonals and no condition on `R` being integral. Let `N2(B)` count the same objects with the additional condition `R in Z`.

Then Stage24 proves the literal subset relation

\[
\mathcal A_2(B)=\mathcal B_2(B)\cap\{R\in\mathbf Z\},
\]

and the audited theorem stack

\[
\boxed{M_2(B)\sim C_{M_2}B(\log B)^5},
\qquad C_{M_2}>0,
\]

\[
\boxed{\sqrt{\log B}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}},
\]

hence

\[
\boxed{
B^{-1}(\log B)^{-9/2}
\ll
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}
}
\]

and in particular

\[
\boxed{N_2(B)/M_2(B)\to0},
\qquad
\boxed{N_2(B)\to\infty}.
\]

The final qualitative classification is therefore

```text
STAGE24_CLASS=THIN_BUT_INFINITE
GLOBAL_ZERO_DENSITY_PROVED=true
INFINITE_PRIMITIVE_TARGET_CONSTRUCTION_PROVED=true
POSITIVE_POWER_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
```

No perfect-cuboid existence or nonexistence conclusion is drawn.

## 2. Population, cutoff and multiplicity lock

The Stage18 source population and Stage19 target population use the same physical objects and the same height

\[
R=\sqrt{a^2+b^2+c^2}.
\]

The only new predicate is `R in Z`. Therefore

```text
SOURCE_STAGE=Stage18
TARGET_STAGE=Stage19
SOURCE_COUNT=M2(B)
TARGET_COUNT=N2(B)
CANONICAL=0<a<b<c
PRIMITIVE=gcd(a,b,c)=1
FACE_MASK=EXACTLY_TWO_INTEGRAL_FACE_DIAGONALS
SOURCE_SPACE_REQUIREMENT=NONE
TARGET_SPACE_REQUIREMENT=R_IN_Z
CUTOFF=R<=B
LITERAL_SUBSET_TRANSITION=true
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

This is a literal survival ratio. No distinguished-face incidence multiplicity is introduced in Stage24.

## 3. Frozen upstream interfaces

### 3.1 Stage18 source asymptotic

```text
UPSTREAM_STAGE=Stage18
UPSTREAM_THEOREM=M2(B)~C_M2 B(log B)^5 with C_M2>0
DIRECTIONAL_THEOREM=M2,j(B)~C_j B(log B)^5 for j=a,b,c with C_j>0
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
SOURCE_CONSTANT_EXPLICIT_NUMERIC=false
```

Stage18 uses exactly the source population defined above. The constant exists and is positive, but Stage24 does not claim a numerical closed formula for `C_M2`.

### 3.2 Stage19 / Stage14 target upper

```text
UPSTREAM_STAGE=Stage19 importing Stage14 upper theorem
UPSTREAM_THEOREM=N2(B)<<_epsilon B^(1/2+epsilon)
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
```

This is the strongest certified whole-population upper bound. Stage24 does not identify the half-power as the true exponent.

### 3.3 Stage16S ambient space baseline

For ambient primitive canonical cuboids with no face condition, completed Stage16S gives

\[
\frac{N_S^{all}(B)}{U(B)}
\sim
\frac{9\zeta(3)}{8\pi G}B^{-1}.
\]

This is an interaction comparator only. It is not multiplied into Stage24 counts.

### 3.4 Stage21 one-face space transition

Completed Stage21 gives

\[
\frac{N_1(B)}{M_1(B)}
\sim
\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}.
\]

Relative to the ambient Stage16S baseline, one-face conditioning gives a positive `(log B)^2` enhancement while preserving polynomial order `B^-1`.

### 3.5 Stage22 and audited post-Stage24 Stage23

Completed Stage22 gives

\[
\frac{M_2(B)}{M_1(B)}
\sim
\frac{4\pi^2C_{M_2}}3\frac{(\log B)^4}{B}.
\]

After the Stage24 lower breakthrough, the audited and merged Stage23 reinvestigation gives

\[
B^{-1}(\log B)^{-5/2}
\ll
\frac{N_2(B)}{N_1(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-3}.
\]

It also proves a named overlap lower bound

\[
A_{ac,bc}(B)\gg\sqrt{\log B}.
\]

These are frozen comparison interfaces; Stage24 does not reinterpret them as objectwise conditional probabilities.

## 4. Direct quantitative ratio theorem

Divide the Stage19 upper by the positive Stage18 main term. For every fixed `epsilon>0`,

\[
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
\frac{B^{1/2+\varepsilon}}{B(\log B)^5}
=
B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

Taking `epsilon<1/2` proves

\[
\boxed{N_2(B)/M_2(B)\to0}.
\]

This route supplies the strongest current quantitative upper ratio. It does not prove that exponent `1/2` is sharp.

Directionwise, `N2,j(B)<=N2(B)` and `M2,j(B)~C_jB(log B)^5` with `C_j>0`, so

\[
\frac{N_{2,j}(B)}{M_{2,j}(B)}
\ll_{\varepsilon,j}
B^{-1/2+\varepsilon}(\log B)^{-5}\to0
\]

for `j=a,b,c`.

## 5. Independent space-square thin-cover proof of zero density

The Stage18 shared-edge double-Pythagorean surface on a dense torus has equations

\[
u^2=e^2+x^2,
\qquad
v^2=e^2+y^2.
\]

Its frozen smooth split toric resolution is `Y=Bl_4(P1 x P1)`, and the physical radius `R` is exactly the frozen anticanonical height.

Add the space-square coordinate

\[
w^2=e^2+x^2+y^2.
\]

Let `Z -> Y` be the normalization of the induced quadratic function-field extension. On a primitive integral physical representative, rational `w` is automatically integral because `w^2` is an integer. Thus a Stage18 object lifts rationally exactly when it satisfies the Stage19 space predicate.

### 5.1 Generic non-square calculation

Work over `Qbar` on the dense affine chart `e=1`. Parametrize the two Pythagorean conics independently:

\[
x=\frac{2t}{1-t^2},
\qquad
u=\frac{1+t^2}{1-t^2},
\]

\[
y=\frac{2s}{1-s^2},
\qquad
v=\frac{1+s^2}{1-s^2}.
\]

The space radicand is

\[
f=1+x^2+y^2=u^2+y^2
=
\frac{u^2s^4+(4-2u^2)s^2+u^2}{(1-s^2)^2}.
\]

Set `z=s^2`. The numerator is quadratic in `z`:

\[
Q(z)=u^2z^2+(4-2u^2)z+u^2.
\]

Its discriminant is

\[
\Delta=(4-2u^2)^2-4u^4
=16(1-u^2)
=-16x^2.
\]

At the generic torus point `x != 0`, so `Delta != 0`. The product of the two roots is `1`, so both roots are nonzero. Therefore `Q(s^2)` has four simple roots over the geometric function field. A rational-function square has zeros of even multiplicity, while the denominator `(1-s^2)^2` is already a square. Hence

\[
\boxed{f\notin\overline{\mathbf Q}(Y)^{\times2}}.
\]

Thus `Z` is geometrically integral and `Z -> Y` is generically finite of degree two. Its rational image is a type-II thin subset of `Y(Q)`.

### 5.2 Thin-set conclusion

Apply the external thin-set theorem under the contract printed in Section 9. The number of points in this thin image of height at most `B` is

\[
o(B(\log B)^5).
\]

Every Stage19 object is in that image, hence

\[
\boxed{N_2(B)=o(B(\log B)^5)}
\]

and independently

\[
\boxed{N_2(B)/M_2(B)\to0}.
\]

This route is qualitative only. Its little-o saving is not multiplied with the Stage14 half-power upper.

## 6. Mixed-parity C17 infinite primitive family

Start from the algebraic identities

\[
e=4pq,
\qquad x=4p^2-q^2,
\qquad y=4q^2-p^2.
\]

They imply

\[
e^2+x^2=(4p^2+q^2)^2,
\]

\[
e^2+y^2=(4q^2+p^2)^2,
\]

and

\[
e^2+x^2+y^2=17(p^4+q^4).
\]

Thus an exact space lift is obtained from

\[
\boxed{p^4+q^4=17Z^2},
\qquad
\boxed{D=17Z}.
\]

The historical odd/odd specialization is impossible because its right side is `2 mod 16`; the new family removes only that parity specialization.

### 6.1 Genus-one and positive-rank certificate

Put

\[
t=q/p,
\qquad
z=Z/p^2.
\]

Then

\[
17z^2=t^4+1.
\]

The quartic has four simple roots, so its smooth projective normalization has genus one. It contains `(t,z)=(2,1)` and maps nontrivially to

\[
E:\quad Y^2=X^3-1156X
\]

by

\[
X=-4t^2/z^2,
\qquad
Y=4t(t^4-1)/z^3.
\]

Substitution using `17z^2=t^4+1` verifies the elliptic equation identically. The rational point `(2,1)` maps to

\[
P=(-16,120).
\]

At the good primes `31` and `41`, exact enumeration gives

\[
\#E(\mathbf F_{31})=32,
\qquad
\#E(\mathbf F_{41})=52,
\]

and `P mod 31` has exact order `16`. If `P` were rational torsion, good-reduction injection on prime-to-residue-characteristic torsion would force its order to divide `gcd(32,52)=4` after excluding residue-characteristic factors by the other good prime, contradicting the order-16 reduction. Hence `P` has infinite order.

A nonconstant morphism between the smooth genus-one curves induces an isogeny after choosing rational origins. Therefore the C17 genus-one curve has positive Mordell-Weil rank and infinitely many rational points.

### 6.2 Integral parameters and primitivity

Write a positive rational point with `t=q/p` in lowest terms. Then

\[
17Z^2=p^4+q^4.
\]

If `Z=A/B` in lowest terms, then `B^2|17`. Since `17` is squarefree, `B=1`; therefore `Z in Z`.

The coprime parameters cannot both be even. They cannot both be odd because then `p^4+q^4=2 mod 16`, impossible for `17Z^2`. Hence they have opposite parity.

For any odd prime `ell|e=4pq`, if `ell|p` then

\[
x\equiv-q^2\not\equiv0\pmod\ell,
\]

and if `ell|q` then

\[
y\equiv-p^2\not\equiv0\pmod\ell.
\]

The prime `2` does not divide all three edges because one of `x,y` is odd. Thus

\[
\boxed{\gcd(e,x,y)=1}.
\]

### 6.3 Physical cone and injectivity

Let

\[
\alpha=(1+\sqrt2)/2.
\]

On

\[
1<t=q/p<\alpha,
\]

one has

\[
0<x<y<e,
\]

so the canonical ordering is

\[
\boxed{(a,b,c)=(x,y,e)}.
\]

The cone contains the exact point

\[
(p,q,Z)=(38,43,569),
\]

which gives

\[
(a,b,c,D)=(3927,5952,6536,9673).
\]

Moreover

\[
x+y=3(p^2+q^2),
\qquad
y-x=5(q^2-p^2),
\]

so the parameter squares, and hence the reduced positive ratio, are recoverable from the box. Distinct reduced ratios in the cone give distinct primitive canonical objects.

A non-torsion point on the real elliptic component generates a dense cyclic subgroup of its circle component. Translating by the physical rational point therefore puts infinitely many rational C17 points in the open physical cone.

### 6.4 Exactly-two rather than three faces

The remaining face is square exactly when

\[
w^2=17t^4-16t^2+17.
\]

Together with `17z^2=t^4+1`, this gives a biquadratic degree-four cover of `P1`. The two quartic branch sets each have four simple roots and are disjoint: at a root of `t^4+1`, the second polynomial is `-16t^2`, which is nonzero.

The normalized fiber product is connected with eight simple branch values. At each branch value, two points upstairs ramify with index two, giving total ramification `16`. Riemann-Hurwitz gives

\[
2g-2=4(-2)+16=8,
\]

so

\[
\boxed{g=5}.
\]

By Faltings' theorem this curve has only finitely many rational points. Therefore only finitely many C17 points create a third integral face, and infinitely many physical cone points remain exactly-two.

Hence

\[
\boxed{N_2(B)\to\infty}.
\]

### 6.5 Quantitative lower bound

For a fixed non-torsion translation sequence `Q_n=Q_0+nR` on the genus-one curve, standard elliptic height theory gives

\[
h(t(Q_n))=O(n^2).
\]

Writing `t(Q_n)=q_n/p_n` in lowest terms,

\[
\max(p_n,q_n)\le\exp(Cn^2).
\]

The space diagonal satisfies

\[
D_n=17Z_n
\le\sqrt{34}\max(p_n,q_n)^2
\le\exp(C'n^2).
\]

A fixed positive proportion of indices visit a compact subinterval of the physical cone. The `t` projection has fixed degree and the physical parameter map is injective there, so `gg N` distinct Stage19 objects occur among `n<=N`. Removing the finite genus-five exceptions changes only `O(1)` points.

Taking `N` proportional to `sqrt(log B)` yields

\[
\boxed{N_2(B)\gg\sqrt{\log B}}.
\]

This lower bound has polynomial exponent zero.

## 7. Final two-sided Stage24 ratio

Combining Section 6 with the Stage18 main term gives

\[
\frac{N_2(B)}{M_2(B)}
\gg
\frac{\sqrt{\log B}}{B(\log B)^5}
=
B^{-1}(\log B)^{-9/2}.
\]

Together with Section 4,

\[
\boxed{
B^{-1}(\log B)^{-9/2}
\ll
N_2(B)/M_2(B)
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}.
}
\]

The interval between the exponents is genuine current uncertainty, not notation for an expected law.

## 8. Upper-surgeon negative knowledge

Stage24 checkpoint40 deliberately reopened the half-power upper problem.

A frozen Stage14 geometric interface proves that every fixed physical rational curve has `M·C>=4`, and the only possible `M·C=4` square-root mechanism is absent. Therefore every fixed rational curve has individual count at most

\[
B^{2/5+o(1)},
\]

and every fixed finite collection is strict sub-square-root.

A separate occupancy interface shows that any cell with a fixed power density deficit

\[
\omega(c)=B^{-\delta+o(1)},\qquad\delta>0,
\]

contributes at most

\[
B^{1/2-\delta+o(1)}.
\]

Thus any whole-family square-root saturation must lie in near-maximal-occupancy moving/collective structures. However, no uniform bound in a family growing with `B` is proved. In particular Stage24 explicitly rejects summing fixed-curve `O`-constants over a growing family without uniformity.

The fixed-prime squareclass sieve has local survival

\[
\rho_p=1-4/p+O(p^{-2}),
\]

but even a hypothetical polynomial range of uniform primes in the same tensor would naturally produce logarithmic rather than fixed-power saving. No growing-modulus theorem strong enough for strict sub-square-root is available.

Therefore

```text
STRICT_SUB_SQRT_WHOLE_FAMILY_PROVED=false
MOVING_FAMILY_UNIFORMITY_PROVED=false
GROWING_MODULUS_UNIFORMITY_PROVED=false
HALF_POWER_CAUSAL_MECHANISM_IDENTIFIED=false
```

## 9. External theorem contracts

### 9.1 Thin-set zero-density theorem

```text
THEOREM=Browning-Loughran thin-set zero-density interface as verified on the Stage15/18 toric host
WORKING_FORM=for every type-II thin subset T of the relevant smooth split toric Y under the exact anticanonical height H_R, #T(H_R<=B)=o(B(log B)^5)
OBJECT=the rational image of the geometrically integral degree-two space-square cover Z->Y
HYPOTHESES_CHECKED=Y smooth projective split toric; -K_Y big/anticanonical; required Picard/cohomological conditions; cover generically finite degree>1 and geometrically integral
HEIGHT_OR_MEASURE_MATCH=H_R is exactly the physical R height on the frozen Stage18 host
LOCAL_OR_ARCHIMEDEAN_RESTRICTIONS=dense torus; excluded boundary is already part of the frozen toric counting interface
QUANTIFIERS=the thin cover is fixed before B->infinity
UNIFORMITY_NOT_CLAIMED=no effective power saving and no growing-family uniformity
ROLE=independent qualitative zero-density route
```

### 9.2 Good-reduction torsion injection

```text
THEOREM=standard injectivity of prime-to-p rational torsion under good reduction of an elliptic curve
WORKING_FORM=for good prime p, the prime-to-p part of E(Q)_tors injects into E(F_p)
OBJECT=E: Y^2=X^3-1156X and P=(-16,120)
HYPOTHESES_CHECKED=31 and 41 are good primes; exact finite-field group orders computed
HEIGHT_OR_MEASURE_MATCH=not applicable
QUANTIFIERS=fixed curve and fixed primes
UNIFORMITY_NOT_CLAIMED=none needed
ROLE=prove P is non-torsion and hence positive rank
```

### 9.3 Faltings

```text
THEOREM=Faltings' theorem
WORKING_FORM=a smooth projective curve over Q of genus >1 has finitely many Q-rational points
OBJECT=normalization of 17z^2=t^4+1 and w^2=17t^4-16t^2+17
HYPOTHESES_CHECKED=connected biquadratic cover; eight disjoint simple branch values; Riemann-Hurwitz genus 5
HEIGHT_OR_MEASURE_MATCH=not applicable
QUANTIFIERS=fixed genus-five curve
UNIFORMITY_NOT_CLAIMED=no effective bound on number or height of exceptional points
ROLE=remove the third-face-square sublocus from the infinite C17 family
```

### 9.4 Elliptic height and real-component dynamics

```text
THEOREM=standard canonical-height growth plus density/equidistribution of a non-torsion cyclic subgroup on a real elliptic circle component
WORKING_FORM=for fixed non-torsion R and rational function t, h(t(Q0+nR))=O(n^2); a positive proportion of n visit any fixed open interval in the relevant real circle component
OBJECT=the positive-rank C17 genus-one curve and its physical t=q/p interval
HYPOTHESES_CHECKED=fixed non-torsion point; fixed rational function; physical rational point in the open cone; fixed real component
HEIGHT_OR_MEASURE_MATCH=physical D is bounded by a fixed quadratic function of max(p,q), hence exp(O(n^2))
QUANTIFIERS=curve, point, rational function and cone fixed before B->infinity
UNIFORMITY_NOT_CLAIMED=implied constants and threshold are existential
ROLE=derive N2(B)>>sqrt(log B)
```

## 10. Interaction and double-charge audit

The ambient space baseline is

\[
N_S^{all}/U\asymp B^{-1}.
\]

The Stage24 survivor ratio is currently bracketed by

\[
B^{-1}(\log B)^{-9/2}
\ll
N_2/M_2
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

Relative to the ambient `B^-1` scale, these bounds lie on opposite sides of neutrality. Therefore Stage24 does **not** prove positive interaction, negative interaction, or asymptotic independence between two-face structure and space integrality.

The second-order comparison is

\[
I(B)=\frac{N_2/M_2}{N_1/M_1}
=\frac{N_2/N_1}{M_2/M_1}.
\]

Using the frozen Stage21/22/23 interfaces gives

\[
\boxed{(\log B)^{-13/2}\ll I(B)}
\]

and

\[
\boxed{I(B)\ll_\varepsilon B^{1/2+\varepsilon}(\log B)^{-7}}.
\]

These bounds also straddle `1`, so the second-order interaction sign is unresolved.

Mandatory firewalls:

```text
STAGE16S_BASELINE_MULTIPLIED_INTO_STAGE24=false
STAGE21_LOG2_ENHANCEMENT_TRANSFERRED_TO_STAGE24=false
STAGE23_SPACE_CONDITION_DOUBLE_CHARGED=false
STAGE22_STAGE23_RATIOS_TREATED_AS_OBJECTWISE_PROBABILITIES=false
LOCAL_SIEVE_SAVING_MULTIPLIED_WITH_HALF_POWER_UPPER=false
THIN_COVER_SAVING_MULTIPLIED_WITH_HALF_POWER_UPPER=false
C17_FAMILY_PROMOTED_TO_BULK_MASS=false
DOUBLE_CHARGE_CHECK=PASS
```

## 11. Arithmetic-stratum heterogeneity and Stage23 backflow

Within the same Stage15-derived algebraic formulas:

- coprime odd/odd parameters have no integral-space lifts by the modulo-16 obstruction;
- the mixed-parity C17 slice has infinitely many primitive exactly-two integral-space lifts.

Thus arithmetic strata of one ambient formula can behave qualitatively differently under the space predicate.

On the C17 physical cone, `(a,b,c)=(x,y,e)` and the guaranteed square faces are `ac` and `bc`. Therefore

\[
N_{2,c}(B)\gg\sqrt{\log B}
\]

and the Stage17 pair-overlap channel satisfies

\[
\boxed{A_{ac,bc}(B)\gg\sqrt{\log B}}.
\]

The frozen Stage17 overlap theorem gives

\[
A_{ac,bc}(B)=o(B(\log B)^3),
\]

so this named channel is proved infinite but lower order.

This reinterpretation was separately fresh-audited in the Stage23 post-Stage24 lane before inclusion here.

## 12. Finite computation boundary

The matched exact Stage24 census through `B=1,000,000` is a regression and diagnostic interface only. At `B=10^6`,

```text
M2=13,817,725
N2=255
N2/M2=1.84545574615e-5
N2 directions=(98,101,56)
```

The ratio decreases on the frozen matched grid, but effective fitted slopes change substantially between scale ranges. No finite exponent fit, directional ordering, or leading constant is promoted to theorem status.

The C17 witness `(3927,5952,6536,9673)` is an exact regression anchor only; infinitude is proved by the genus-one argument.

```text
FINITE_DATA_PROMOTED_TO_THEOREM=false
NUM_REUSE_CHECK=PASS
NUM_NEW_COMPUTATION_REQUIRED_AT_CLOSEOUT=false
```

## 13. Negative knowledge / open gates

```text
TRUE_TARGET_POLYNOMIAL_EXPONENT_IDENTIFIED=false
POSITIVE_POWER_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
STRICT_SUB_SQRT_WHOLE_FAMILY_UPPER_PROVED=false
HALF_POWER_INTRINSIC_PROVED=false
HALF_POWER_CAUSAL_MECHANISM_IDENTIFIED=false
MOVING_FAMILY_UNIFORMITY_PROVED=false
GROWING_MODULUS_SIEVE_UNIFORMITY_PROVED=false
SURVIVOR_RATIO_LEADING_CONSTANT_AVAILABLE=false
DIRECTIONAL_STAGE19_ASYMPTOTICS_PROVED=false
STAGE24_GLOBAL_INTERACTION_SIGN=UNRESOLVED
SECOND_ORDER_INTERACTION_SIGN=UNRESOLVED
PERFECT_CUBOID_CONCLUSION=NONE
```

## 14. Lower-stage supersession discipline

Stage24 checkpoint50 changed current knowledge but did not make historical Stage19/23 audits false.

- Stage19 historical `unboundedness unproved` is superseded by a later addendum.
- Stage23 historical odd/odd death remains valid in its stated parity scope.
- Broader formula death is superseded by C17 mixed parity.
- Post-Stage24 Stage23 R01 is independently audited and merged.

No population definition, cutoff, canonicalization or multiplicity convention was invalidated, so no lower-stage recomputation is required.

## 15. Stage-end artifacts and stop rule

```text
SELF_CONTAINED_BUNDLE_REQUIRED=true
SELF_CONTAINED_BUNDLE_DECISION=YES
SELF_CONTAINED_BUNDLE_MATERIALIZED=true
SELF_CONTAINED_BUNDLE_PATH=stages/stage24/final.md
MANIFEST_REQUIRED=true
MANIFEST_PATH=stages/stage24/manifest-r01.md
ARSENAL_PROMOTION_REQUIRED=true
ARSENAL_PROMOTION_DECISION=YES
ARSENAL_PROMOTION_MATERIALIZED=true
ARSENAL_PROMOTION_PATH=docs/stage24-arsenal-promotion.md
AGGRESSIVE_SEARCH_LEDGER_REQUIRED=true
AGGRESSIVE_SEARCH_LEDGER_PATH=stages/stage24/24-70/aggressive-search-ledger.md
```

Further improvement of the Stage24 polynomial exponent, interaction sign, half-power mechanism, moving-family uniformity or positive-power lower bound requires a new theorem or new research sublane. The bounded closeout therefore stops here.

```text
SYNTHESIS_STOP_RULE_SATISFIED=YES
NEXT_CONSUMERS=Stage25,Stage26,Stage27,Stage28
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
```

## 16. Provenance and hostile-review checklist

Canonical Stage24 checkpoint records are under `stages/stage24/24-{10,20,30,40,50,60,70}/`. The current-stage load-bearing proofs from checkpoints30 and50 have been transcribed above rather than replaced by repository-path citations. Frozen completed-stage interfaces are printed explicitly.

Fresh hostile review must check at least:

1. literal Stage18/19 population and cutoff match;
2. ratio exponent algebra;
3. generic non-square proof for the space-square cover;
4. applicability boundary of the thin-set theorem;
5. C17 elliptic-map identity and positive-rank certificate;
6. integrality, parity, primitivity, canonical cone and injectivity of the C17 physical map;
7. genus-five exceptional-curve computation and Faltings boundary;
8. elliptic-height derivation of `sqrt(log B)`;
9. fixed-curve versus growing-family uniformity firewall;
10. interaction cross-ratio algebra and all double-charge firewalls;
11. Stage23 backflow scope;
12. finite-data non-promotion and perfect-cuboid nonclaim.

```text
BUNDLE_ID=STAGE24-FINAL-SELF-CONTAINED-20260815-R01
STATUS=CANDIDATE_PENDING_FRESH_AUDIT
INTERNAL_LOAD_BEARING_PROOFS_EMBEDDED=true
EXTERNAL_THEOREM_WORKING_FORMS_STATED=true
EXTERNAL_HYPOTHESES_MAPPED=true
UPSTREAM_INTERFACES_EXACT=true
POPULATION_AND_CUTOFF_AUDITED=true
MULTIPLICITY_AUDITED=true
MEASURE_AND_EXCEPTIONAL_SETS_AUDITED=true
QUANTIFIERS_AND_UNIFORMITY_AUDITED=true
FINITE_DATA_PROMOTED_TO_THEOREM=false
REMOTE_REQUIRED_ASSETS=false
FRESH_HOSTILE_REVIEW=PENDING
AUDIT_REQUIRED=true
```
