# Stage20 final — primitive canonical Euler-cuboid population

BUNDLE_ID=STAGE20-FINAL-SELF-CONTAINED-20260814-R01
STATUS=REPAIRED_RESUBMITTED_FOR_FRESH_AUDIT
STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
PREVIOUS_AUDIT_VERDICT=FAIL_REPAIR_REQUIRED
PREVIOUS_AUDIT_PERSISTENCE_STATUS=COMMITTED
CURRENT_AUDIT_STATUS=PENDING_REAUDIT
FRESH_AUDIT_REQUIRED=true

## 1. Executive theorem and population contract

For `B>0`, define

\[
\mathcal E_3(B)=\{(a,b,c)\in\mathbf Z_{>0}^3:
0<a<b<c,\ \gcd(a,b,c)=1,\ R=\sqrt{a^2+b^2+c^2}\le B,
\]
\[
a^2+b^2,\ a^2+c^2,\ b^2+c^2\text{ are all integer squares}\}.
\]

Let

\[
M_3(B)=\#\mathcal E_3(B).
\]

No integrality condition is imposed on `R`. Stage20 is the primitive/canonical Euler-cuboid population, not the perfect-cuboid endpoint.

The strongest certified Stage20 envelope is

\[
\boxed{B^{1/6}\ll M_3(B)\ll B(\log B)^{5-1/50}.}
\]

More generally, for every fixed `eta<1/46`,

\[
\boxed{M_3(B)\ll_\eta B(\log B)^{5-\eta}.}
\]

The lower theorem is proved internally below from an explicit primitive Saunderson family. The upper theorem is imported through the exact frozen Stage14-e11 interface printed below. The true exponent, a matching lower bound, and an asymptotic formula remain open.

## 2. Certified finite baseline

The Stage20 checkpoint20 enumerator gives

```text
B:       50  100  200  400  800  1200  1600  2000
M3(B):    0    0    0    1    3     5     5     7
```

A compatible earlier Stage14-e exact census under the same primitive/canonical Euclidean cutoff extends the finite evidence, including

```text
M3(2000)=7
M3(10000)=18
M3(50000)=42
M3(200000)=82
M3(1000000)=219
```

These are computed facts only. Effective power fits and the visually persistent square-root scale are not asymptotic theorems.

## 3. Frozen upstream interfaces

The Stage14-e8/e10/e11 imports below are frozen earlier-stage theorem interfaces. Their full internal proofs are not reproduced here because the current Stage20 object is literally the same primitive/canonical Euler-brick object under the same Euclidean height and one-object multiplicity. The population/cutoff/multiplicity crosswalk is printed explicitly for audit.

### 3.1 Stage14-e8 / PR #163 — K3 model and divisor envelope

Stage14-e8 writes `R_EB(B)` for primitive Euler bricks satisfying

```text
0<a<b<c
gcd(a,b,c)=1
all three face diagonals integral
D_R=sqrt(a^2+b^2+c^2)<=B
no space-diagonal integrality requirement
```

Thus `D_R=R` identically and `R_EB(B)=M3(B)` object-for-object.

```text
UPSTREAM_STAGE=Stage14-e8_PR163
UPSTREAM_THEOREM=For the primitive canonical Euler-brick population under D_R<=B, R_EB(B)<<B log B exp(O(log B/log log B))=B^(1+o(1)); equivalently R_EB(B)=O_epsilon(B^(1+epsilon)) for every fixed epsilon>0. The third-face double cover of Y=Bl_4(P1xP1) has branch class -2K_Y and resolves to a K3 surface. Physical and projective heights satisfy H_max<=D_R<=sqrt(3)H_max.
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

Quantifier boundary: the `O_epsilon` statement fixes `epsilon>0` before `B->infinity`; e8 does not prove a fixed relative log saving below log-power 5, a fixed power saving in `B`, or a square-root bound.

Role in Stage20: geometric K3 structure and independent weaker upper provenance. It is not the strongest current upper theorem.

### 3.2 Stage14-e10 / PR #184 — local blocker law and nonexplicit thin-cover saving

Stage14-e10 uses the same Euler target `R_EB(B)` and the same physical Euclidean height. Its local law is computed on the exact Stage14-e two-face toric host from which the Stage20 third-face completion locus is selected.

```text
UPSTREAM_STAGE=Stage14-e10_PR184
UPSTREAM_THEOREM=For the same primitive canonical Euler-brick population under the same Euclidean height, R_EB(B)<<B(log B)^(5-eta_EB) for some fixed eta_EB>0. On the matched physical two-face toric host, the exact third-face blocker masses are delta_2=2/9 and delta_p=2(p-chi_4(p))/(p^2+6p+1)=2/p+O(p^-2) for odd p. For each fixed finite prime set the joint limiting law is the product Tamagawa mass; taking B->infinity with the prime set fixed and then enlarging the prime set proves zero density.
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

Additional host lock:

```text
LOCAL_HOST_MATCH=true
LOCAL_HOST=the_same_two-face_shared-edge_toric_population_used_as_the_Stage20_pre-completion_host
LOCAL_BLOCKER_ROLE=causal_obstruction_not_an_independent_probability_factor
```

Quantifier boundary: e10's elementary local-sieve zero-density proof is a two-limit statement, `B->infinity` for a fixed finite prime set followed by enlargement of the prime set. E10 itself does not justify a growing prime cutoff `z=z(B)`. Its thin-cover theorem gives only existence of some positive `eta_EB`; it does not evaluate that constant.

Role in Stage20: exact causal local blocker law plus the first fixed log-saving upper theorem.

### 3.3 Stage14-e11 / PR #188 — strongest explicit upper theorem and growing-prime sieve

Stage14-e11 retains exactly the e8/e10 Euler population and height. It substitutes `rho(Y)=6` and `dim Y=2` into Huang's explicit proof bounds for the degree-two K3 cover and separately closes the growing-prime sieve uniformity gap.

```text
UPSTREAM_STAGE=Stage14-e11_PR188
UPSTREAM_THEOREM=For the same primitive canonical Euler-brick population under the same Euclidean height, for every fixed eta<1/46 one has R_EB(B)<<_eta B(log B)^(5-eta). In particular R_EB(B)<<B(log B)^(5-1/50). The endpoint eta=1/46 is not claimed. Independently, the matched local blocker system admits a growing-prime uniform Selberg sieve of dimension 2 and gives R_EB(B)<<B(log B)^5/(log log B)^2.
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

Exact object identification:

\[
R_{EB}(B)=M_3(B),\qquad D_{\mathbf R}=R=\sqrt{a^2+b^2+c^2}.
\]

Quantifier boundary: choose a fixed `eta<1/46` first, then let `B->infinity`; the endpoint `1/46` is excluded because epsilon losses remain in the external theorem proof. The growing-prime sieve is a separate, weaker global upper theorem and is not multiplied with the thin-cover bound.

Role in Stage20: strongest certified same-population upper interface. Therefore

\[
\boxed{M_3(B)\ll_\eta B(\log B)^{5-\eta}\quad(\eta<1/46),}
\]

and the fixed convenient choice `eta=1/50` gives

\[
\boxed{M_3(B)\ll B(\log B)^{5-1/50}.}
\]

## 4. Internal load-bearing proof: primitive Saunderson lower family

This section transcribes the proof-complete Stage20-50a derivation because the lower theorem and infinitude are current-Stage load-bearing results.

### 4.1 One-parameter primitive Pythagorean input

For every even integer `m>=10`, put

\[
u=m^2-1,\qquad v=2m,\qquad w=m^2+1.
\]

Then

\[
u^2+v^2=(m^2-1)^2+4m^2=(m^2+1)^2=w^2.
\]

Because `m` is even, `u,w` are odd and `v` is even. Also

\[
\gcd(u,v)=\gcd(m^2-1,2m)=1,
\]

and the Pythagorean identity then gives pairwise coprimality of `u,v,w`; hence `gcd(u,v,w)=1`.

Define

\[
A=u|4v^2-w^2|,\qquad
B_1=v|4u^2-w^2|,\qquad
C=4uvw.
\]

For `m>=10`,

\[
4v^2-w^2=16m^2-(m^2+1)^2=-(m^4-14m^2+1)<0,
\]

while

\[
4u^2-w^2=4(m^2-1)^2-(m^2+1)^2=3m^4-10m^2+3>0.
\]

Therefore

\[
A=(m^2-1)(m^4-14m^2+1)
=m^6-15m^4+15m^2-1,
\]

\[
B_1=2m(3m^4-10m^2+3)=6m^5-20m^3+6m,
\]

\[
C=8m(m^4-1)=8m^5-8m,
\]

and all three are positive.

### 4.2 All three face diagonals are integral

Using `u^2+v^2=w^2`, expand

\[
\begin{aligned}
A^2+B_1^2
&=u^2(4v^2-w^2)^2+v^2(4u^2-w^2)^2\\
&=u^2(16v^4-8v^2w^2+w^4)
 +v^2(16u^4-8u^2w^2+w^4).
\end{aligned}
\]

Collecting terms and substituting `u^2+v^2=w^2` gives

\[
A^2+B_1^2=w^6.
\]

Hence the first face diagonal is the integer `w^3`.

For the second face,

\[
\begin{aligned}
A^2+C^2
&=u^2(4v^2-w^2)^2+16u^2v^2w^2\\
&=u^2\bigl[(4v^2-w^2)^2+16v^2w^2\bigr]\\
&=u^2(4v^2+w^2)^2.
\end{aligned}
\]

Thus its diagonal is `u(4v^2+w^2)`.

Similarly,

\[
\begin{aligned}
B_1^2+C^2
&=v^2(4u^2-w^2)^2+16u^2v^2w^2\\
&=v^2\bigl[(4u^2-w^2)^2+16u^2w^2\bigr]\\
&=v^2(4u^2+w^2)^2,
\end{aligned}
\]

so the third face diagonal is `v(4u^2+w^2)`.

Therefore `(A,B_1,C)` is an Euler cuboid for every even `m>=10`.

### 4.3 Primitivity

Suppose a prime `p` divides all three of `A,B_1,C`.

If `p=2`, this is impossible because `u,w` are odd, `v` is even, and

\[
4v^2-w^2\equiv -1\pmod2,
\]

so `A=u|4v^2-w^2|` is odd.

Now let `p` be odd. Since

\[
p\mid C=4uvw,
\]

and `u,v,w` are pairwise coprime, `p` divides exactly one of `u,v,w`.

If `p|u`, then

\[
B_1=v(4u^2-w^2)\equiv -vw^2\not\equiv0\pmod p,
\]

because `p` divides neither `v` nor `w`, contradiction.

If `p|v`, then

\[
A=u(4v^2-w^2)\equiv -uw^2\not\equiv0\pmod p,
\]

contradiction.

If `p|w`, then

\[
A=u(4v^2-w^2)\equiv4uv^2\not\equiv0\pmod p,
\]

again a contradiction.

Thus no prime divides all three edges and

\[
\boxed{\gcd(A,B_1,C)=1.}
\]

No primitive reduction after construction is required.

### 4.4 Canonical ordering

For `m>=10`, direct subtraction gives

\[
C-B_1=2m^5+20m^3-14m=2m(m^4+10m^2-7)>0,
\]

so `B_1<C`.

Also

\[
A-C=m^4(m^2-8m-15)+15m^2+8m-1.
\]

For `m>=10`, `m^2-8m-15>=5`, hence the right-hand side is positive. Therefore `C<A`.

Likewise

\[
A-B_1=m^4(m^2-6m-15)+20m^3+15m^2-6m-1.
\]

At `m>=10`, `m^2-6m-15>=25`, so this is positive as well. Consequently

\[
\boxed{0<B_1<C<A.}
\]

Thus the constructed triple is already in a fixed strict size order, and its Stage20 canonical representative is `(B_1,C,A)`.

### 4.5 Injectivity

The largest edge is

\[
A(m)=m^6-15m^4+15m^2-1.
\]

Its derivative is

\[
A'(m)=6m(m^4-10m^2+5).
\]

For `m>=10`, `m^4-10m^2+5>0`, hence `A'(m)>0`. Therefore `A(m)` is strictly increasing on the allowed parameter range.

Since the canonical representative has largest edge `A(m)`, distinct even integers `m>=10` produce distinct primitive canonical Stage20 objects.

### 4.6 Exact common cutoff comparison

For `m>=10`, crude uniform bounds suffice:

\[
u<m^2,\qquad v=2m,\qquad w<2m^2.
\]

From the explicit formulas,

\[
A<20m^6,\qquad B_1<16m^6,\qquad C<16m^6.
\]

Therefore the Stage20 Euclidean height satisfies

\[
\begin{aligned}
R&=\sqrt{A^2+B_1^2+C^2}\\
&<\sqrt{20^2+16^2+16^2}\,m^6\\
&=\sqrt{912}\,m^6\\
&<31m^6.
\end{aligned}
\]

Hence every even `m>=10` satisfying

\[
m\le(B/31)^{1/6}
\]

produces a distinct primitive canonical Euler cuboid counted by `M_3(B)`.

The number of even integers in `[10,(B/31)^{1/6}]` is at least

\[
\left\lfloor\frac12(B/31)^{1/6}\right\rfloor-4
\]

for sufficiently large `B`. Thus

\[
\boxed{
M_3(B)\ge
\left\lfloor\frac12(B/31)^{1/6}\right\rfloor-4,
}
\]

and consequently

\[
\boxed{M_3(B)\gg B^{1/6}.}
\]

In particular the Stage20 population is infinite.

### 4.7 Lower-proof boundary

This construction proves infinitude and a positive-power lower bound only. It does not prove that exponent `1/6` is intrinsic, does not match the upper bound, does not prove a square-root law, and imposes no integral space-diagonal condition.

## 5. Current certified envelope

Combining the internal lower family with the frozen Stage14-e11 upper interface gives

\[
\boxed{B^{1/6}\ll M_3(B)\ll B(\log B)^{5-1/50}.}
\]

More generally, the right side may use any fixed `eta<1/46`.

This determines neither the true exponent nor an asymptotic formula. The finite square-root signal remains consistent with the interval but unproved.

## 6. Causal decomposition

The Stage20 third-face condition is not modeled as an independent random-square event.

### 6.1 Two-face host

The source geometry is the shared-edge double-Pythagorean host resolved in the Stage14-e / Stage18 line. A third-face square is a completion condition on this already-coupled host.

### 6.2 K3 thin cover

By the frozen e8 interface, adding the third-face equation produces a geometrically nontrivial degree-two cover of the toric two-face base `Y=Bl_4(P1xP1)` with branch class `-2K_Y`. After normalization/minimal resolution the compactified Euler-brick surface is a K3 surface. This is structural geometry, not an independent-probability model.

### 6.3 Exact local blockers

By the frozen e10 interface,

\[
\delta_2=2/9,
\]

and for odd primes

\[
\boxed{
\delta_p=\frac{2(p-\chi_4(p))}{p^2+6p+1}
=\frac2p+O(p^{-2}).
}
\]

The local system has sieve dimension two. E10 gives the exact fixed-prime law and a two-limit zero-density argument; e11 supplies growing-prime uniformity. These local blockers explain a concrete arithmetic source of rarity but do not determine the true global exponent.

### 6.4 Explicit survival

The internal Saunderson family proves that the K3/local obstructions do not annihilate the population: infinitely many primitive/canonical Euler objects survive, quantitatively at least on the `B^(1/6)` scale.

### 6.5 No double charge

The thin-cover theorem, local residue blockers, divisor projection, and explicit family have different logical roles. They are not multiplied as if they were independent probabilities. The strongest global upper theorem is used once; the local law is causal explanation and a separate weaker sieve certificate.

## 7. Intrinsic status

```text
POPULATION_INFINITE=true
POSITIVE_POWER_LOWER_BOUND_PROVED=true
CERTIFIED_LOWER_EXPONENT=1/6
STRONGEST_EXPLICIT_UPPER_LOG_SAVING=eta_any_lt_1/46
CONCRETE_UPPER_ETA=1/50
TRUE_EXPONENT_IDENTIFIED=false
MATCHING_LOWER_BOUND_PROVED=false
ASYMPTOTIC_FORMULA_PROVED=false
ASYMPTOTIC_CONSTANT_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
```

Checkpoint30's growth-law OPEN_GATE therefore remains valid but narrower than at submission: the population is known to be infinite and quantitatively growing; only its true asymptotic law remains open.

## 8. Downstream reusable interfaces

Stage20 exports three candidate reusable interfaces in `docs/stage20-arsenal.md`:

```text
S20-W01_EXPLICIT_EULER_THIN_COVER_UPPER
S20-W02_PRIMITIVE_SAUNDERSON_LOWER
S20-W03_EULER_LOCAL_BLOCKER_LAW
```

Expected receivers are Stages26, 27, and 28. Their Stage20 promotion remains pending the fresh checkpoint70 re-audit.

Stage26 owns the actual `Stage18 -> Stage20` conditional ratio and independence classification. Stage20 does not pre-claim that transition result.

## 9. Repository-wide reuse preflight

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=true
STRONGER_PRIOR_RESULT=Stage14-e11_PR188
```

The numerical observatory is not a direct Stage20 population match because its principal census is integral-space-diagonal prefiltered. Its finite triple record is not a Stage20 Euler count and is never used as perfect-cuboid nonexistence evidence.

## 10. Quantifier, measure, multiplicity and evidence audit

```text
POPULATION_CONTRACT_CHANGED=NO
STAGE14_E8_POPULATION_MATCH=true
STAGE14_E10_POPULATION_MATCH=true
STAGE14_E11_POPULATION_MATCH=true
CUTOFF_MATCH=D_R_equals_R_exactly
MULTIPLICITY_MATCH=one_primitive_canonical_object_counted_once
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
EVIDENCE_LEVELS_COMPLETE=YES
FINITE_DATA_PROMOTED_TO_THEOREM=false
DOUBLE_CHARGE_CHECK=PASS
```

The e11 statement fixes `eta<1/46` before `B->infinity`. The endpoint `eta=1/46` is not claimed. The e10 fixed-prime product law is not silently promoted to growing primes; only e11 provides that uniformity.

## 11. Open gates

```text
OPEN_GATE_1=STAGE20_POPULATION_GROWTH_LAW_UNRESOLVED
OPEN_GATE_2=TRUE_EXPONENT_UNRESOLVED
OPEN_GATE_3=MATCHING_LOWER_BOUND_UNRESOLVED
OPEN_GATE_4=ASYMPTOTIC_CONSTANT_UNRESOLVED
OPEN_GATE_5=SQRT_B_SIGNAL_THEOREM_STATUS_UNRESOLVED
```

Resolving these requires genuinely new research beyond bounded Stage20 closeout.

## 12. Frozen nonclaims

Stage20 does **not** prove or assume:

- an integral space diagonal;
- existence or nonexistence of a perfect cuboid;
- `M_3(B)~C B^alpha`;
- `M_3(B)\asymp B^(1/2)`;
- a matching lower bound;
- the thin-cover endpoint `eta=1/46`;
- independence of the third-face condition from prior face conditions;
- a Stage18-to-Stage20 transition law.

## 13. Repair record and fresh-audit gate

The first Stage20-70 audit found the mathematical synthesis substantively sound but failed the self-contained bundle on two presentation/proof-boundary defects:

1. the current-Stage Stage20-50a load-bearing construction had been summarized instead of embedded proof-completely;
2. the frozen Stage14-e8/e10/e11 load-bearing imports lacked the exact upstream-interface contract required by V1.

This repaired bundle now embeds the complete construction proof in Section 4 and prints the three exact frozen interfaces in Section 3. No theorem, population, cutoff, bound, OPEN_GATE, Stage26 deferral, or nonclaim was changed by the repair.

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_REVIEW_REPAIR_COMPLETED=true
INTERNAL_LOAD_BEARING_PROOFS_EMBEDDED=true
UPSTREAM_INTERFACES_EXACT=true
EXTERNAL_THEOREM_WORKING_FORMS_STATED_VIA_FROZEN_UPSTREAM_INTERFACES=true
POPULATION_AND_CUTOFF_AUDITED=true
MULTIPLICITY_AUDITED=true
MEASURE_AND_EXCEPTIONAL_SETS_AUDITED=true
QUANTIFIERS_AND_UNIFORMITY_AUDITED=true
FINITE_DATA_PROMOTED_TO_THEOREM=false
REMOTE_REQUIRED_ASSETS=false
FRESH_HOSTILE_REVIEW=PENDING
ARSENAL_PROMOTION_REQUIRED=YES
SYNTHESIS_STOP_RULE_SATISFIED=YES
PREVIOUS_AUDIT_VERDICT=FAIL
PREVIOUS_AUDIT_RECORD=stages/stage20/20-70/audit.md
CURRENT_AUDIT_STATUS=PENDING_REAUDIT
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_CHECKPOINT=70
NEXT_STAGE=
NEXT_EXPECTED_COMMAND=Stage20-audit
```
