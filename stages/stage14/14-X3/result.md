# Stage14-X3 — primitive-line host multiplicity and the quartic diagonal obstruction

## Status

`COMPLETE_EXACT_QUARTIC_REDUCTION_AND_RELAXED_DIAGONAL_OBSTRUCTION`

Stage14-X2 leaves the receiver

```text
PrimitiveLineCommonCoreNormalizedHostMultiplicity.
```

This stage conditions in the X2 order: first the common-core residual triple,
then the primitive positive physical root line, and finally the endpoint-small
roots and 2-primary data.  It independently obtains the same four-agreement-cell
normal form later recorded by the parallel mainline Stage14-4ck branch.  The
parallel branch was not merged at the source snapshot, so X3 does not import it
as a predecessor theorem.

The outcome is deliberately two-sided.

1. The eight-cell fiber reduces to a scaled equal-value incidence for
   `F(a,b)=a*b*(b-a)*(b+a)`, with divisor-many switched-cell completions.
2. A fixed value of `F` has only `B^o(1)` primitive representations.
3. This fixed-value fact does not bound the equal-value incidence: after
   dropping the physical cross-role locks and switch-product integrality, the
   diagonal coefficient specialization contains a fixed-power family.

Thus the proposed pointwise `B^o(1)` multiplicity is **not proved**, and it
cannot be proved from split-quartic factorization plus within-side
squarefreeness/coprimality alone.  The relaxed counterexample is not promoted
to a counterexample to the physical receiver.

The unconditional endpoint remains

```text
V(B) << B^(7/8+o(1)).
```

## 1. Imported merged boundary

Merged X1 gives `B^o(1)` physical lift multiplicity after fixing the eight
cells and residual data.  Merged 4ci gives the normalized four-host equations
and full `k`-line saturation.  Merged 4cj/s7-24 and X2 give a primitive,
fully saturated, positive `xi` root line.  Hence every remaining fixed-power
fiber is the number of moving balanced cell packets above

```text
(C,u_res,v_res), X_root=(x_1,y_1,x_2,y_2).
```

Put

```text
q_k  = C*u_res,
q_xi = C*v_res,
X=x_1*x_2,
Y=y_1*y_2.
```

Condition also on the endpoint-small roots

```text
r=r_1*r_2, s=s_1*s_2, G=g_1*g_2,
```

whose total cost is `B^o(1)`.

## 2. Exact agreement-cell normal form

Use agreement cells `(alpha,delta,R,J)` and switched cells
`(beta,gamma,S,T)`.  Define

```text
H_k^+  = delta^2*s^2 + alpha^2*r^2,
H_k^-  = delta^2*s^2 - alpha^2*r^2,
H_xi^+ = J^2*Y^2 + R^2*X^2,
H_xi^- = J^2*Y^2 - R^2*X^2.
```

The residual-product equations and the positive cross coupling imply, after
cancelling the positive plus factors,

```text
G*q_k*R*J*H_xi^- = 2*q_xi*alpha*delta*H_k^-.       (2.1)
```

With

```text
F(a,b)=a*b*(b-a)*(b+a),
A=alpha*r, D=delta*s, U=R*X, V=J*Y,
```

(2.1) is exactly

```text
G*q_k*r*s*F(U,V)=2*q_xi*X*Y*F(A,D).                (2.2)
```

Moreover the switched products are forced:

```text
S*T       = H_k^+*H_k^-/(q_k*R*J),
beta*gamma= H_xi^+*H_xi^-/(q_xi*alpha*delta).       (2.3)
```

Once the four agreement cells are fixed, legal splits in (2.3) cost at most
divisor functions, hence `B^o(1)`.  Therefore X2's receiver reduces exactly to

```text
CrossRoleSwitchIntegralQuarticAgreementIncidence.   (2.4)
```

This verifies the parallel 4ck reduction in the X2 quantifier order, but does
not use an unmerged result as an input.

## 3. Fixed-value quartic fibers are subpolynomial

For a primitive positive pair `gcd(a,b)=1`, the four factors

```text
a, b, b-a, b+a
```

are pairwise coprime away from 2.  Their odd pairwise gcds are one, and all
remaining common factors divide two.  For fixed nonzero `N`, allocating each
odd prime power of `N` among the four factors and fixing the finite 2-primary
pattern gives at most

```text
4^omega(N)*B^o(1)=B^o(1)
```

primitive candidates.  The linear relations among the allocated factors only
discard candidates.  Hence

```text
#{(a,b): gcd(a,b)=1, 0<a<b, F(a,b)=N}=B^o(1).       (3.1)
```

The dedicated audit checks this gcd allocation and finite fibers, but (3.1)
is the elementary factor-allocation proof, not a finite inference.

## 4. Why fixed-value control does not close the receiver

Equation (2.2) is not a fixed-value equation.  Both `(U,V)` and `(A,D)` move.
Bounding the number of representations after fixing the left side gives

```text
#incidence <= B^o(1) * #left candidates,
```

and the symmetric estimate merely replaces `left` by `right`.  Neither is a
fixed-power saving at the endpoint.

This loss is real for the relaxed coefficient problem.  Take equal scale
coefficients in (2.2), set

```text
(U,V)=(A,D),
```

and let `(A,D)` range over coprime squarefree positive pairs in a dyadic box.
Every pair is a solution.  There are a fixed positive proportion on the
power-exponent scale (elementary squarefree/coprime density is more than is
needed; the audit only records finite growth).  Thus

```text
split quartic equation
+ squarefree/coprime inside each side
does not imply pointwise B^o(1) incidence.            (4.1)
```

Even the small collision

```text
F(1,6)=F(2,5)=210
```

shows that primitive fixed-value representations need not be unique.

The diagonal family in (4.1) is a counterexample only to the **relaxed
analytic shortcut**.  A physical packet must additionally satisfy:

```text
- the canonical cross-role prime allocation between k and xi cells;
- both positive integral switched products in (2.3);
- legal squarefree coprime splits of those products;
- the residual, orientation, primitive, interval, and reconstruction masks.
```

X3 does not construct a growing family satisfying all these masks.  Therefore

```text
PHYSICAL_RECEIVER_COUNTEREXAMPLE_PROVED=false.
```

## 5. Exact remaining receiver

The only route by which a pointwise or average saving can now arise is the
failure of the relaxed diagonal family under the omitted physical constraints.
Define

```text
OffDiagonalCrossRoleSwitchIntegralQuarticEnergy
```

to count (2.2) after:

1. separating coefficient-diagonal/proportional configurations;
2. imposing the cross-role prime locks;
3. imposing both integrality conditions (2.3) before absolute values;
4. retaining the common-core residual and primitive-line quantifiers.

The next sufficient theorem is either:

```text
diagonal physical branch = empty or B^o(1),
```

plus a fixed-power average saving for the off-diagonal energy, or a direct
fixed-power bound for their union.  The four factors of `F` alone are no
longer an adequate receiver.

## 6. Finite diagnostics

The dedicated audit performs three independent checks.

```text
- exhaustive primitive squarefree pairs a<b<=300;
- exact grouping by F(a,b), including non-unique value fibers;
- relaxed diagonal counts for cutoffs 50,100,200,300.
```

It also imports the merged X2 finite physical enumeration through `Q<=600`
and confirms:

```text
residual+primitive-line maximum physical fiber = 1.
```

That physical injectivity is useful evidence but remains a finite diagnostic;
it is not an asymptotic proof.

## 7. Decision and route safety

X3 closes the ambiguity in the phrase "quartic multiplicity": fixed-value
fibers are harmless, while equal-value energy is not.  It proves no new whole
family saving and modifies no canonical index or exponent ledger.

X4 has concrete value.  It should test the coefficient-diagonal/proportional
branch against (2.3) and the primewise cross-role locks, then either eliminate
that branch or freeze a genuine physical parametric counterexample.  Only if
the off-diagonal branch survives that exact test should an external quartic
energy/H-line audit be considered.

All ordinary routes may continue.  No X3-specific H line is needed.

```text
STAGE14_X3=COMPLETE_EXACT_QUARTIC_REDUCTION_AND_RELAXED_DIAGONAL_OBSTRUCTION
PRIMITIVE_LINE_HOST_MULTIPLICITY_PROVED=false
EIGHT_CELL_TO_FOUR_AGREEMENT_CELL_REDUCTION_PROVED=true
SPLIT_BINARY_QUARTIC_FORM=F(a,b)=a*b*(b-a)*(b+a)
FIXED_VALUE_PRIMITIVE_QUARTIC_FIBER=Bo1
RELAXED_EQUAL_VALUE_QUARTIC_INCIDENCE_BO1=false
RELAXED_DIAGONAL_FIXED_POWER_OBSTRUCTION=true
PHYSICAL_RECEIVER_COUNTEREXAMPLE_PROVED=false
REMAINING_RECEIVER=OffDiagonalCrossRoleSwitchIntegralQuarticEnergy
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
X3_AUXILIARY_H_NEEDED=false
MAIN_ROUTE_BLOCKED_BY_X3=false
S_ROUTE_BLOCKED_BY_X3=false
T_TH_ROUTE_BLOCKED_BY_X3=false
TOOLBOX_ROUTE_BLOCKED_BY_X3=false
X4_CONTINUATION_VALUE=true
NEXT_RECOMMENDED=Stage14-X4 eliminate or realize the coefficient-diagonal physical branch using both switch-product integrality conditions and cross-role prime locks
```
