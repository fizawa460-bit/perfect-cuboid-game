# Stage25-60 R504 second-section hostile audit

Status: **PASS; CHECKPOINT60 CONTINUES**

ROUTE=R504
CHECKPOINT=60
PR=994

## Verdict

The explicit physical family obtained from `P+2R` is accepted. The family-specific count is

\[
\boxed{N_{R504,P+2R}(B)=\Theta(B^{1/12})}.
\]

This does not improve the already audited global lower `N2(B)>>B^(1/4)` and does not close checkpoint60.

## Hostile algebra checks

Let

\[
N=u^2+4u-3,\qquad M=7-u^2,\qquad H=N^4+M^4.
\]
The verifier checks

\[
H=2FG,\qquad F^2+G^2=2S^2,
\]
and therefore the polynomial point

\[
R=(4S^2,4S(F^2-G^2))
\]
lies on

\[
E_H:y^2=x^3-4H^2x.
\]

For the physical quartic 2-cover, the recovered squares for `P+R` and `P-R` are respectively rational squares times `1/32` and `1/128`, so these two combinations do not give Q(u)-rational physical lifts.

For `P+2R`, exact group-law simplification gives polynomials `A,B,C` satisfying

\[
x(P+2R)=-4(A B/C)^2
\]
and
\[
\boxed{A^4+B^4=HC^2}.
\]
Thus

\[
t=A/B,\qquad z=M^2C/B^2
\]
solves the physical quartic identity exactly.

## Stage19 adapter

The integer family

\[
E=2NMAB,
\quad X=N^2B^2-M^2A^2,
\quad Y=N^2A^2-M^2B^2,
\quad D=HC
\]
satisfies

\[
E^2+X^2=H_X^2,
\quad E^2+Y^2=H_Y^2,
\quad E^2+X^2+Y^2=D^2.
\]

At `u=3` all four physical coordinates are positive and strictly ordered `0<E<X<Y<D`; hence a small compact rational interval around `3` has fixed physical order. The homogenized physical height has degree `24`.

## Primitive-gcd certificate

The direct edge resultants are

```text
Res(E/2,X)=2^688*3^256
Res(E/2,Y)=2^656*3^272*7^8.
```

For reduced homogeneous parameters, any common prime of `E,X,Y` must lie in the intersection of these supports. The case `p|b` is excluded for odd `p` by the leading coefficients, and the explicit factor `2` in `E` accounts for one extra dyadic power. Therefore the deliberately coarse absolute bound

\[
\boxed{\gcd(E,X,Y)\le2^{689}3^{256}}
\]
is accepted. Primitive reduction cannot create a polynomial height drop.

## Exactly-two-face and multiplicity checks

The missing face factors as

\[
X^2+Y^2=256(u+1)^2Q_{44}(u).
\]
The verifier checks `deg Q44=44`, preservation of degree modulo `11`, and

\[
\gcd(Q_{44},Q'_{44})=1\pmod{11}.
\]
Thus `Q44` is squarefree over Q and `w^2=Q44(u)` has genus `21`; Faltings gives only finitely many rational third-face exceptions.

On the fixed ordered interval, `E/X` is a nonconstant rational function of degree at most `24`, so the parameter-to-canonical-family multiplicity is `O(1)`. Reduced rationals of height at most `T` in the interval number `Theta(T^2)`, while primitive physical height is `Theta(T^24)`. Hence the exact family growth is `Theta(B^(1/12))`.

## Independence scope firewall

The preceding hostile audit already proves a generic rank jump `rank E_phi(Q(u))>=2` by two independent E0 quotient maps. This round verifies that `R` is an explicit polynomial section and that `P+2R` yields the stated physical family.

A new standalone proof that this displayed `R` is exactly a chosen primitive generator of the second free Mordell-Weil line is not required for the `Theta(B^(1/12))` family theorem and is not promoted as a new theorem here. The family theorem depends only on the exact section/group-law/physical-cover identities checked above.

## Discovery / reuse audit

The required checkpoint60 discovery fields and reuse handoff are materialized in `r504-rank-jump-discovery-ledger.md` for this second-section round. No new route ID is created: this is a direct continuation of the already audited R504 nonsplit rank-jump mechanism. The prior Stage14/15 attack-ID binding `0522,0544,0583,0748` remains applicable.

```text
REPO_REUSE_PREFLIGHT=PASS
DISCOVERY_LEDGER_STATUS=COMPLETE
POPULATION_ADAPTERS_PROVED=R504_P_PLUS_2R_EXACT_STAGE19_FAMILY_THETA_B_1_12
DISCOVERY_AUDIT_VERDICT=PASS
```

## Remaining live work

The current explicit family is weaker than the audited R504 `3P` family `Theta(B^(1/10))`, and both are weaker than the global R501/R502 quarter-power lower. The full physical rank-two coset lattice `(2m+1)P+2nR` has not been height-classified, and the full-split Prym/E0-isogeny residual remains open.

```text
R504_RANK_TWO_PHYSICAL_COSET_HEIGHT_CLASSIFICATION_PROVED=false
R504_FULL_SPLIT_NO_E0_ISOGENY_PROVED=false
R504_FULL_SPLIT_PRYM_ISOGENY_RESIDUAL=OPEN
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```

## Audit footer

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
R504_SECOND_POLYNOMIAL_SECTION_ACCEPTED=true
R504_P_PLUS_R_PHYSICAL_LIFT=false
R504_P_MINUS_R_PHYSICAL_LIFT=false
R504_P_PLUS_2R_PHYSICAL_LIFT=true
R504_P_PLUS_2R_PHYSICAL_HEIGHT_DEGREE=24
R504_P_PLUS_2R_PRIMITIVE_GCD_BOUND=2^689*3^256
R504_P_PLUS_2R_THIRD_FACE_EXCEPTION_GENUS=21
R504_P_PLUS_2R_PARAMETER_MULTIPLICITY=O(1)
R504_P_PLUS_2R_EXACT_FAMILY_GROWTH=Theta(B^(1/12))
R504_PHYSICAL_STAGE19_ADAPTER_PROVED=true
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=60
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #994; then Stage25-main-batch at checkpoint60
```
