# Stage25-60 R504 explicit nonsplit rank-jump hostile audit

Status: **PASS; CHECKPOINT60 CONTINUES**

ROUTE=R504
CHECKPOINT=60
PR=993

## Verdict

The explicit nonsplit base change

\[
\phi(u)=\frac{u^2+4u-3}{7-u^2}
\]

is accepted as a genuine generic rank-jump mechanism for the pulled-back R504 elliptic surface. The global Stage19 population lower is not changed because the second section has not yet been materialized with a physical height/primitive/exactly-two/multiplicity adapter.

## Hostile checks

1. `phi(v)=phi(u)` factors with the nontrivial source deck
   \[
   \delta(u)=-\frac{u+7}{u+1}.
   \]
2. The derivative is
   \[
   \phi'(u)=\frac{4(u^2+2u+7)}{(u^2-7)^2},
   \]
   so the critical divisor is genuinely nonsplit, in squareclass `-6`.
3. `epsilon_2=(5-u)/(u+1)` is a second involution with `phi(epsilon_2)=1/phi`, and the lift identity on
   \[
   C:Y^2=F(u),\qquad F=(u^2+4u-3)^4+(7-u^2)^4
   \]
   is exact.
4. `F` is squarefree of degree eight, so the smooth cover has genus three.
5. The `epsilon_2` quotient is the genus-one quartic
   \[
   V^2=2(x^4+8x^3-64x-64),
   \]
   with binary-quartic invariants `I=3072`, `J=0`; its Jacobian is
   \[
   y^2=x^3-82944x
   \]
   and is Q-isomorphic to `E0:y^2=x^3-4x` by the rational `12^4` scaling.

## Independent quotient-factor check

The submission's V4/genus-zero argument is correct in spirit, but the hostile audit also checks independence directly on
\[
H^0(C,\Omega^1)=\langle du/Y,\;u\,du/Y,\;u^2du/Y\rangle.
\]

For the `+36/(u+1)^4` lifts, the invariant differential lines are

\[
\omega_\delta=(u^2+2u+7)\frac{du}{Y},
\qquad
\omega_{\epsilon_2}=(u^2+2u-5)\frac{du}{Y}.
\]

Direct substitution gives

\[
\delta^*\omega_\delta=\omega_\delta,
\qquad
\epsilon_2^*\omega_{\epsilon_2}=\omega_{\epsilon_2},
\]

and the two lines are distinct. Hence the two elliptic quotient maps induce independent homomorphisms from `J(C)` to `E0`. Combined with the previously hostile-audited twist-descent interface, this gives

\[
\boxed{\operatorname{rank}E_\phi(\mathbf Q(u))\ge2}.
\]

Thus the original-base audited rank `1` genuinely jumps after this nonsplit degree-two base change.

## Full-split scope correction

The full split reciprocal/commuting-involution locus classification is accepted. The complementary quotient calculations with `J != 0` show that those checked complementary elliptic curves are not Q-isomorphic to the `j=1728` curve `E0`.

They do **not** prove absence of a Q-isogeny to `E0`, since isogeny does not preserve `j`. Therefore:

```text
R504_FULL_SPLIT_RECIPROCAL_LOCUS_CLASSIFICATION_ACCEPTED=true
R504_FULL_SPLIT_NO_Q_ISOMORPHIC_E0_ON_CHECKED_COMPLEMENTS=true
R504_FULL_SPLIT_NO_E0_ISOGENY_PROVED=false
R504_FULL_SPLIT_PRYM_ISOGENY_RESIDUAL=OPEN
```

No stronger full-split closure is accepted.

## Discovery audit

The Stage14/15 bound-attack ledger and all `review_required=true` source artifacts used here were opened. The binding is persisted in `r504-rank-jump-discovery-ledger.md`:

- `S1415-ATTACK-0522`: accepted structural genus-three/involution predecessor;
- `S1415-ATTACK-0544`: accepted V4 elliptic-quotient predecessor and physical-lift warning;
- `S1415-ATTACK-0583`: not a blocker; it concerns a different frozen direction family and left higher isogenies open. The present exact nonsplit equation is materially new;
- `S1415-ATTACK-0748`: rejected as a direct population adapter because its physical `Y=S` height and moving-denominator measure do not match this generic function-field rank statement.

```text
ATTACK_LEDGER_SEARCH=PASS
REVIEW_REQUIRED_SOURCE_READS=PASS
NEW_MECHANISM_DISCOVERY_AUDIT_EVIDENCE=COMPLETE
DISCOVERY_AUDIT_VERDICT=PASS
```

## Population firewall

The second section is not yet an explicit rational-function section with controlled physical cuboid height. No primitive gcd, exactly-two-face exception theorem, or parameter multiplicity theorem has been attached to it. Therefore the new rank-jump theorem is **not** a new Stage19 counting theorem yet.

```text
R504_EXPLICIT_SECOND_SECTION_MATERIALIZED=false
R504_SECOND_SECTION_PHYSICAL_HEIGHT_DEGREE=UNKNOWN
PHYSICAL_STAGE19_ADAPTER_PROVED=false
GLOBAL_STAGE25_LOWER_CHANGED=false
GLOBAL_STAGE25_LOWER=N2(B)>>B^(1/4)
```

## Audit footer

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
R504_NONSPLIT_RANK_JUMP_ACCEPTED=true
R504_NONSPLIT_GENERIC_MW_RANK_LOWER=2
R504_DIFFERENTIAL_EIGENSPACE_INDEPENDENCE=PASS
R504_DELTA_INVARIANT_DIFFERENTIAL=(u^2+2u+7)du/Y
R504_EPSILON2_INVARIANT_DIFFERENTIAL=(u^2+2u-5)du/Y
R504_FULL_SPLIT_RECIPROCAL_LOCUS_CLASSIFICATION_ACCEPTED=true
R504_FULL_SPLIT_NO_E0_ISOGENY_PROVED=false
PHYSICAL_STAGE19_ADAPTER_PROVED=false
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
NEXT_EXPECTED_COMMAND=merge PR #993; then Stage25-main-batch at checkpoint60
```
