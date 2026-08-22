# Stage30-06 — hostile audit

```text
AUDITED_PR=1332
AUDITED_SUBMISSION_HEAD=d4f33bde6f0c05c181f19a20c71bbb13782160d4
AUDIT_VERDICT=PASS_AFTER_BOUNDED_SOURCE_ACTION_LIFT_REPAIR
```

## Independent checks that pass

The audited common-model source supports

```text
Sbar_Q(i) ~= (X(8)xX(8))/Delta G0,
G0=ker(PSL2(Z/8)->PSL2(Z/4)),
```

with the exact invariant/cuboid coordinates already frozen at Stage30-05. Testa--Stoll also explicitly identify factor exchange with `a3 -> -a3`, so

```text
c_sigma=delta_a3
```

is source-compatible.

The retained level-4 sign matrix gives exactly

```text
theta(g)=D4*g*D4^-1,
theta(S)=S,
theta(T)=T^-1,
theta|V_mod=id.
```

The submitted generator-level calculation correctly identifies

```text
V_mod={g04,g06,g12,g14}
```

and the four sign-deck patterns

```text
g04 -> identity
g12 -> negate {a2,a3,b1}
g06 -> negate {a1,a3,b2}
g14 -> negate {a1,a2,b1,b2}.
```

## Bounded source-action lift repair

The original submission chose endpoint lifts with the correct branch-square action and S4 relations, but it did not derive those lifts from the diagonal modular action on the Testa--Stoll `X(8)xX(8)` model. That omission is material because Stage30 forbids replacing the common-model adapter by an arbitrary abstract/action-compatible S4 embedding.

Audit derives the diagonal action directly from the X(8) equations and the Stage30-05 X(4) gauge. The source-derived endpoint generators are

```text
S0:
a1->-a2, a2->-a1, a3->-a3,
b1->-b2, b2->-b1, b3->b3, c->c,

T0:
a1->-c, c->-a1,
a2->i*a2, a3->i*a3, b1->i*b1,
b2->-b3, b3->-b2.
```

The pre-audit submitted section differs by

```text
S_submitted = delta_{b1,b2} * S0
T_submitted = delta_{b2,b3} * T0.
```

So it was a sign-deck-twisted splitting. The repair replaces the frozen 30-06C input by the literal source-derived diagonal action.

This changes no load-bearing downstream value. With `S0,T0`:

```text
S0^2=1
T0^4=1
(S0*T0)^3=1

j(V_mod) = same four sign patterns as submitted

sigma(S0)=c_sigma*S0*c_sigma^-1
sigma(T0)=c_sigma*T0^-1*c_sigma^-1.
```

The repaired checker and `semilinear-spec.json` now freeze these source-derived lifts. The Codex 30-06C prompt has also been repaired to require independent reconstruction of the X(8) diagonal quotient action before the all-24 verification.

## Scope

No 30-06C all-element certificate is granted by this audit. The remaining machine gate is still

```text
SEMILINEAR_ALL24_VERIFIED=false
```

until external Codex output is produced and separately audited.

The arithmetic defect objects remain separate:

```text
c_sigma != kappa
V_mod != K8
K8_DEFECT_CLASSIFICATION_EXECUTED=false
DEFECT_ELIMINATION_COUNT=0
R29_KUM5_DISCHARGED=false
```

No new Class-3 theorem gate is exposed.

## Final audit state

```text
SOURCE_DERIVED_DIAGONAL_MODULAR_LIFTS=true
V4_SIGN_DECK_LIFT_DERIVED=true
Q_GALOIS_COCYCLE_DERIVED=true
Q_GALOIS_COCYCLE_EXHAUSTIVELY_VERIFIED=false
CODEX_30_06C_PROMPT_AUDIT_APPROVED=true
WAITING_EXTERNAL_CODEX_RESULT_C=true
AUDIT_REQUIRED=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=30-06C_EXTERNAL_CODEX_SEMILINEAR_VERIFICATION
NEXT_EXPECTED_COMMAND=EXTERNAL_CODEX_TASK_C_THEN_STAGE30_MAIN_BATCH
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
