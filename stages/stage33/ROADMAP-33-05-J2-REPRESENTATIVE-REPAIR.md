# Stage33-05 J2 named-representative repair roadmap

Purpose: make the hostile reopen of Stage33-05 operationally visible and prevent Stage33 MAIN from appearing to drift backward without a finite repair plan.

This repair band does **not** revoke the abstract computation `Br(Kc_bar)[2] ~= (F2)^2` or the abstract quotient label `J2`. The historical Q-defined `ell_J2` remains revoked because it is zero in the geometric Creutz--Viray quotient. The corrected geometric class has now been rebuilt independently.

## Finite repair ladder

| Leaf | Question | Exact exit condition | Current state |
|---|---|---|---|
| R0 | Is the promoted historical `ell_J2` nonzero? | Exact full branch-algebra regression modulo `K^*L^{*2}` | **DONE: ZERO / revoked** |
| R1 | Does abstract `J2` survive independently? | Exact quotient nonzero statement without historical `ell_J2` | **DONE: PASS** |
| R2 | Can a correct concrete representative be built? | Corrected `ell_J2=(f2,1)` nonzero in the actual geometric quotient | **DONE: PASS** |
| R3 | What is its generic-fiber class? | Explicit CV cocycle plus named Brauer→WC/Sha adapter | **DONE: PASS + fresh-super-hostile bridge PASS** |
| R4 | Which marked Brauer functional is it? | Compute primitive `NS/T` of named `X_J2`, determine minimum norm in `{4,8,12}` | **IN_PROGRESS** |
| R5 | Can Stage33-05/12 credit be restored? | Hostile replay of valid R1–R4 and restore only re-established credit | **NOT RUN / BLOCKED BY R4** |

## Current authoritative R3→R4 bridge

The corrected pair is

```text
J2=(f2,1),
f2=(t+1+sqrt(2))/(t-1+sqrt(2)).
```

Fresh super-hostile audit at head

```text
b569159aced79d4038399e11fde2924d0a69c52e
```

returned

```text
PASS_FRESH_SUPER_HOSTILE_MATHEMATICALLY.
```

The hardened exact chain is

```text
abstract J2=(f2,1)
 -> gamma(f2,1)
 -> h0(gamma(f2,1))=d(f2,1)          [Creutz–Viray Prop. 5.1]
 -> d(f2,1) represented by xi         [Creutz–Viray Lemma 4.6]
 -> xi(rho)=Tr                        [R3 exact]
 -> standard <Tr> phi-descent, d=f2
 -> X_J2 attempt4 quartic.
```

The load-bearing bridge certificate is

```text
stages/stage33/33-05/j2-r3-r4-brauer-sha-bridge.json
canonical SHA256 = 3dff502b69bbee725abfe7e1f5580837410f1a8552a7b4cae31dd85c9b34bb28
```

It explicitly source-locks the CV surface-to-generic presentation, the Ogg–Shafarevich `Br(K3) ~= Sha` identification, and the standard 2-isogeny homogeneous-space formula. It also records

```text
generic_weil_chatelet_class_nonzero=true
named_J2_torsor_authoritative_credit=true
```

at the geometric `Kgeom=Qbar(t)` layer. This does **not** restore Q-defined arithmetic descent.

## Authoritative geometric torsor for R4

Together with the audited bridge, attempt4 is the named geometric torsor

```text
X_J2:
N^2=f2*U^4-2*(t^2+1)^2*U^2*V^2+((t^4-6*t^2+1)^2/f2)*V^4,
Jac(X_J2)=E_Kc.
```

Attempt4 alone remains only the orientation/phi-cover certificate; the named-class identity is supplied by the audited bridge.

Historical attempt1/attempt2 are **not valid current named-torsor evidence**. Their retained algebra/component data may be used only in the explicitly audited limited scope recorded by `j2-r4-historical-attempts-semantic-status.json`.

## R4 fixed receiver and exact exit

The fixed marked receiver is

```text
T(Kc)=diag(4,8).
```

The three nonzero order-2 functionals have distinct kernel minima:

```text
[0,1] -> 4
[1,0] -> 8
[1,1] -> 12
```

No candidate is selected yet. The current exact leaf is

```text
R4_COMPUTE_PRIMITIVE_NS_DISCRIMINANT_GROUP_AND_QUADRATIC_FORM_OF_X_J2
AND_SELECT_MINIMUM_NORM_4_8_12.
```

Do not infer the marked coordinate from the E[2] cocycle bits, branch orbit bits, old attempt1/2 component data, or the squareclass alone.

## Current firewalls

```text
historical_Q_defined_ell_J2_current_credit=false
Q_defined_descent_credit_restored=false
named_J2_torsor_authoritative_credit=true   # geometric layer only
primitive_NS_T_discriminant_form_materialized=false
minimum_norm_selected=false
marked_brauer_coordinate_selected=false
Stage33-05 reclosed=false
Stage33-12 closed exact=false
Stage33-13 released=false
R5 run=false
class3 promoted=false
theorem/receiver/endpoint credit=false
perfect cuboid existence/nonexistence claim=false
merge_allowed=false
Stage33 progress=5/11
```

## User-visible stuckness rule

Every future `Stage33-main-batch` in this band reports:

`33-05 repair: R?/R5 | state | attempts on current leaf | exact new information | next exit test`

A batch that does not change the current leaf, candidate set, exact invariant, or missing interface increments stagnation count. Two consecutive stagnant batches require a route audit instead of another same-form attempt.
