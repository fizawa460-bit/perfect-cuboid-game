# Stage25-60 R504 full-split generic Prym hostile audit

Status: **PASS; GENERIC Q-DEFINED E0 PRYM FACTOR EXCLUDED; EXCEPTIONAL LOCUS REMAINS OPEN**

ROUTE=R504
CHECKPOINT=60
PR=997
HOSTILE_AUDIT=true

## Verdict

The submitted specialization obstruction is accepted, with one field-of-definition firewall made explicit by this audit.

What is proved is the generic-base-field statement

\[
\operatorname{Hom}_{K}(P_\eta,E_{0,K})=0,
\qquad K=\mathbf Q(A,B,C,D),
\]

on the smooth full-split parameter locus.  Equivalently, the generic Prym has no **K-defined** elliptic isogeny factor K-isogenous to the constant curve

\[
E_0:y^2=x^3-4x.
\]

This is exactly the statement needed to rule out a generic Q-defined Prym rank-jump mechanism in the present Stage25 degree-two base-change route.

This audit does **not** promote the calculation to the stronger geometric statement

\[
\operatorname{Hom}_{\overline K}(P_{\bar\eta},E_{0,\overline K})=0.
\]

That geometric field-of-definition question is not needed for the accepted rational rank-jump conclusion and remains outside the theorem claimed here.

## 1. Full-split specialization and smoothness

The hostile-audited split normal form is

\[
\phi(u)=\frac{Au^2+B}{Cu^2+D},\qquad AD-BC\ne0,
\]

with genus-three cover

\[
C:Y^2=Q(u^2),
\qquad
Q(x)=(Ax+B)^4+(Cx+D)^4,
\]

and genus-one quotient `E:Y^2=Q(x)`.  Its Jacobian gives the dimension-two Prym complement `P` in `J(C)`.

At

\[
(A,B,C,D)=(1,1,1,2)
\]

we have

\[
AD-BC=1,
\qquad
(AB-CD,AB+CD,AD+BC)=(-1,3,3),
\]

so the specialization is nondegenerate and outside the previously audited reciprocal/commuting-involution loci.

The specialized polynomials are

\[
Q(x)=2x^4+12x^3+30x^2+36x+17,
\]

\[
Q(u^2)=2u^8+12u^6+30u^4+36u^2+17.
\]

The verifier checks both are squarefree modulo `5`.  Since `p=5` is odd, this gives smooth good hyperelliptic reduction for the genus-one quotient and genus-three cover.  The corresponding Jacobian/Prym factors therefore have the required good reduction for the Frobenius test.

## 2. Independent point-count replay

The submitted deterministic `F5/F25` enumeration was replayed independently.

It gives exactly

\[
\#C(\mathbf F_5)=4,
\qquad
\#E(\mathbf F_5)=4,
\]

and

\[
\#C(\mathbf F_{25})=36,
\qquad
\#E(\mathbf F_{25})=32.
\]

The infinity-point convention is correct: the even-degree leading coefficient `2` is nonsquare over `F5`, so there are no `F5`-rational infinity points, while every nonzero `F5` element becomes a square in `F25`, giving two infinity points over `F25`.

Hence

\[
S_1(C)=2,
\quad S_1(E)=2,
\quad S_1(P)=0,
\]

and

\[
S_2(C)=-10,
\quad S_2(E)=-6,
\quad S_2(P)=-4.
\]

For an abelian surface, Newton identities together with the weight-one functional equation give

\[
\boxed{L_{P,5}(T)=1+2T^2+25T^4}.
\]

This reconstruction is accepted.

## 3. E0 Frobenius obstruction

Direct counting on

\[
E_0:y^2=x^3-4x
\]

over `F5` gives trace `a_5(E0)=2`, hence

\[
L_{E_0,5}(T)=1-2T+5T^2.
\]

Exact division gives remainder

\[
\frac45-\frac85T\ne0,
\]

so

\[
\boxed{L_{E_0,5}\nmid L_{P,5}}.
\]

Therefore the specialized Prym cannot have a Q-defined `E0` isogeny factor: any nonzero Q-homomorphism between the specialized Prym and `E0` extends over good integral models and reduces to a nonzero homomorphism; over the finite field this would force the `E0` Frobenius isogeny factor to occur in the Prym Frobenius polynomial.  The observed non-divisibility rules this out.

## 4. Generic specialization step

Let `S` be the regular connected smooth open of the full-split parameter space on which the cover, quotient Jacobian, and Prym are abelian schemes and which contains the chosen rational specialization.

The standard extension/rigidity theorem for homomorphisms of abelian schemes over a regular integral base gives an injective specialization map from the generic Hom group to the Hom group of every good fiber.  Thus a nonzero

\[
P_\eta\longrightarrow E_{0,K}
\]

would specialize nontrivially at `(1,1,1,2)`, contradicting Section 3.

Therefore

\[
\boxed{\operatorname{Hom}_{K}(P_\eta,E_{0,K})=0}.
\]

The submitted generic obstruction is accepted in this precise field-of-definition scope.

## 5. Scope firewall

Accepted consequences:

- the generic full-split Prym does not contribute an additional **K-defined/Q-defined** `E0` direction;
- the previously open generic non-bielliptic rational Prym mechanism is closed;
- any remaining rational full-split Prym rank jump must occur by specialization, i.e. on an exceptional Hom/isogeny-jump locus;
- no claim is made that this exceptional locus is empty, finite, effectively enumerable, or bounded in isogeny degree;
- no population exponent changes in this round;
- the global Stage25 lower remains `N2(B)>>B^(1/4)`;
- checkpoint60 remains open and Stage70 remains blocked.

Not accepted / not claimed:

- `Hom_{Kbar}(P_eta,E0)=0`;
- absence of all geometric `E0` factors after algebraic extension of the parameter field;
- emptiness or finiteness of the exceptional rational specialization locus;
- a new Stage19 family or a stronger Stage25 lower bound.

## 6. Discovery / reuse audit

The current result attacks the residual explicitly left open by the audited PR #993 through PR #996 chain.  No stronger compatible repository theorem was found.  The finite-field calculation is not empirical population evidence; it is an exact good-specialization obstruction to a generic Hom.

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=false
DISCOVERY_AUDIT_VERDICT=PASS
FINITE_DATA_USED_AS_PROOF=false
```

## Audit footer

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
R504_FULL_SPLIT_SPECIALIZATION_ACCEPTED=(1,1,1,2)
R504_FULL_SPLIT_SPECIALIZATION_GOOD_REDUCTION_P5_ACCEPTED=true
R504_FULL_SPLIT_POINT_COUNTS_ACCEPTED=(4,4,36,32)
R504_FULL_SPLIT_PRYM_LPOLY_P5_ACCEPTED=1+2*T^2+25*T^4
R504_E0_LPOLY_P5_ACCEPTED=1-2*T+5*T^2
R504_FULL_SPLIT_PRYM_E0_FROBENIUS_FACTOR_P5=false
R504_FULL_SPLIT_GENERIC_PRYM_E0_HOM_OVER_K=0
R504_FULL_SPLIT_GENERIC_PRYM_E0_FACTOR_SCOPE=GENERIC_BASE_FIELD_ONLY
R504_FULL_SPLIT_GEOMETRIC_E0_FACTOR_OVER_KBAR_CLASSIFIED=false
R504_FULL_SPLIT_EXCEPTIONAL_PRYM_E0_ISOGENY_LOCUS=OPEN
R504_FULL_SPLIT_EXCEPTIONAL_PRYM_E0_ISOGENY_DEGREE=UNBOUNDED_NOT_CLASSIFIED
R504_FULL_SPLIT_PRYM_RESIDUAL=NARROWED_TO_EXCEPTIONAL_RATIONAL_ISOGENY_JUMP_LOCUS_AUDITED_PASS
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
NEXT_EXPECTED_COMMAND=merge PR #997; then Stage25-main-batch at checkpoint60
```
