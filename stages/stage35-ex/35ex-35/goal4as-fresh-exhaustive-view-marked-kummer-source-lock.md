# Stage35-EX Goal4AS source lock — fresh exhaustive-view audit after full Brauer endpoint-equivalence

Scope: execute the Cycle Exploration Safety Protocol trigger raised by Goal4AR. Audited authority remains V74 / Goal4AK. Goal4AS is a provisional breadth-audit leaf: it performs the required blind rediscovery, compares the generated views against the frozen Stage35-EX history, proves one new exact marked-point Kummer restriction, and selects only one next active route. It does not promote Goal4AL–Goal4AR to hostile-audited authority and does not prove E1, Stage35, or any Perfect Cuboid theorem.

## Exact current inputs

Goal4AR is exact-head green at

```text
head = 17be899d6d236f899492fda650fd506ab5a96cf0
aggregate = 34282922559
verify-stage35-ex-current = 102253438874
```

and proves on the exact source-marked local relaxation

```text
(A_src^loc)^(Br(U)) != empty
iff U_PC(Q)^src,+ != empty
iff Stage35 E1-counterexample population != empty.
```

Therefore the complete Brauer–Manin condition is endpoint-equivalent on this relaxation. A finite specially chosen additional Brauer class is not ruled out, but "compute more of Br(U)" is no longer allowed to masquerade as a strictly smaller complete obstruction.

The exact physical elliptic receiver from Goal4K/Goal4L is retained. With

```text
U=u^2, V=v^2,
F_plus  = (1+V)^2*(U^2+1) + 2*(V^2-6V+1)*U,
F_minus = (1+V)^2*(U^2+1) - 2*(V^2-6V+1)*U,
R^2=F_plus, S^2=F_minus, z=R/S,

p=(v^2-1)/(2v),
q=(p^2-1)/(2p),
h_q=(p^2+1)/(2p),
c=(p^2-1)/(2p^2),
```

Goal4L transports every physical endpoint to a non-torsion point

```text
P=(X,Y) in E_q(Q),
E_q: Y^2=X*(X-1)*(X+q^2),
X=c*(z-p)/(z+1/p).
```

The retained physical open has `u*v*(u^2-1)*(v^2-1) != 0` and excludes all rational torsion listed by Goal4L.

## BLIND_REDISCOVERY pass

Before consulting Arsenal route recommendations or historical route names, the exact endpoint equations, physical masks, Goal4K receiver, Goal4L marked elliptic point, Goal4M height scale, and Goal4AR endpoint-equivalence were viewed through the following independent lenses:

1. marked elliptic 2-descent / Kummer squareclasses of the specific physical Goal4L point;
2. explicit canonical-height lower bound versus the Goal4M `O(log B)` endpoint upper window;
3. nonlinear full-endpoint self-map / genuine infinite descent, distinct from common scalar division;
4. finite explicit Brauer-class shortcut, despite the complete Brauer condition being endpoint-equivalent;
5. linked Selmer/Cassels/common-cover coupling beyond individual face Selmer membership;
6. distinct-class amplification or analytic/sieve strengthening of the Stage14/Goal4M square-root population ceiling;
7. cross-face norm/lattice/spinor/torsor compatibility not equivalent to one already represented face form.

Only after this list was generated was it compared with the historical ledger.

## Historical comparison

- Goal4I blocks common-scalar 2-adic descent and has no nonlinear full-system self-map. Therefore candidate 3 remains `UNTESTED` only in the genuinely nonlinear form; the scalar form is `BLOCKED`.
- Goal4J proves that the three separate congruent-number twists and their individual Kummer/Selmer memberships give no cross-twist pruning. Candidate 5 remains `UNTESTED` only if a new common covering, inter-twist isogeny, or Cassels-pairing identity is actually constructed.
- Goal4M supplies the square-root population ceiling and an endpoint `O(log B)` canonical-height upper window; Goal4N proves the current assets do not convert those facts to eventual zero. Candidate 2 is therefore genuinely new only on the missing explicit lower-bound/constant-comparison side. Candidate 6 remains `UNTESTED` only as a new amplification or stronger counting theorem.
- Goal4O blocks the obvious single ternary spinor forms because the endpoint already supplies their representations. Candidate 7 remains `UNTESTED` only for a new cross-face lattice/norm/torsor object.
- Goal4AR makes the complete Brauer route endpoint-equivalent. Candidate 4 remains `UNTESTED` only as a finite explicit shortcut; full-group computation is `EQUIVALENT` to the endpoint problem on the retained relaxation.

No split is justified: these candidates do not yet carry two independent exact obstructions requiring parallel branches.

## Blind internal derivation: a marked one-dimensional Kummer slice

The Goal4L formulas give

```text
X+q^2 = q*h_q*(p*z-1)/(p*z+1).                                (AS-1)
```

Using `z=R/S`,

```text
(X+q^2)*(p*R+S)^2
 = q*h_q*(p*R-S)*(p*R+S)
 = q*h_q*(p^2*F_plus-F_minus).                                (AS-2)
```

The right side is not merely a squareclass consequence. Direct substitution of `U=u^2`, `V=v^2`, and `p=(v^2-1)/(2v)` yields the literal rational square identity

```text
q*h_q*(p^2*F_plus-F_minus)
 =
[
 (u^2+1)*(v^2+1)^2*(v^2-2v-1)*(v^2+2v-1)
 /
 (8*v^2*(v^2-1))
]^2.                                                           (AS-3)
```

Hence every physical marked point satisfies

```text
[X+q^2] = 1 in Q*/Q*2.                                        (AS-4)
```

Because Goal4L excludes the 2-torsion exceptional points, all three factors
`X`, `X-1`, `X+q^2` are nonzero. The elliptic equation gives

```text
[X]*[X-1]*[X+q^2] = 1,
```

so there is one residual squareclass `d` with

```text
delta(P) = ([X],[X-1],[X+q^2]) = (d,d,1).                     (AS-KUMMER)
```

This is a new exact invariant of the **specific physical marked point**, not a claim that the entire 2-Selmer group has dimension one.

## Why the unmarked slice is not itself a new closure theorem

Translate the third rational 2-torsion root to zero:

```text
x0 = X+q^2,
E0: y^2 = x0*(x0-q^2)*(x0-h_q^2),
h_q^2=q^2+1.
```

Writing `E0` as `y^2=x^3+a*x^2+b*x` gives

```text
a=-(2*q^2+1),
b=q^2*(q^2+1),
a^2-4*b=1.
```

The standard 2-isogenous curve with kernel `(0,0)` is therefore

```text
E1: y^2=x^3+(4*q^2+2)*x^2+x
    =x*(x+(h_q-q)^2)*(x+(h_q+q)^2).                            (AS-ISO)
```

For the dual isogeny `hat_phi:E1 -> E0`, the translated x-coordinate has the form

```text
x0(hat_phi(Q)) = y1^2/(4*x1^2).
```

Thus `x0` square is exactly the natural one-isogeny-image condition. As an **unmarked existence statement** it is not enough to improve the Goal4L positive-rank receiver. The new information worth retaining is instead the physical marked point together with its residual class `d` and the original source masks.

Goal4AS therefore does not claim that `(AS-KUMMER)` alone excludes any rank-jump specialization.

## Candidate ledger and selected route

Classifications after blind generation and historical comparison:

```text
LIVE:
  PHYSICAL_MARKED_POINT_RESIDUAL_KUMMER_CLASS_D_LOCAL_SUPPORT

UNTESTED:
  EXPLICIT_CANONICAL_HEIGHT_LOWER_VS_GOAL4M_UPPER_CONSTANTS
  GENUINE_NONLINEAR_FULL_ENDPOINT_SELF_MAP_DESCENT
  FINITE_ADDITIONAL_BRAUER_CLASS_SHORTCUT
  NEW_COMMON_SELMER_OR_CASSELS_COUPLING
  SUPER_SQRT_DISTINCT_CLASS_AMPLIFICATION_OR_STRONGER_COUNTING
  CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY

EQUIVALENT:
  COMPLETE_BRAUER_MANIN_GROUP_AS_A_COMPLETE_OBSTRUCTION
  UNMARKED_XPLUSQ2_SQUARE_EXISTENCE_AS_A_CLOSURE_RECEIVER

BLOCKED:
  COMMON_SCALAR_V2_DIVISION
  THREE_SEPARATE_TWIST_SELMER_MEMBERSHIP_PRUNING
  CURRENT_SQRT_BOUND_TO_EVENTUAL_ZERO_CONVERSION
  OBVIOUS_SINGLE_TERNARY_SPINOR_FORMS
```

The next active route is the `LIVE` item because it is closest to the exact physical marked receiver and has a concrete finite question:

```text
compute d=[X]=[X-1] exactly enough to classify its local prime support;
test whether physical primitivity/valuation constraints force d=1,
force d into a finite squareclass family, or isolate a new obstruction.
```

If `d=1` were forced, the physical marked point would be 2-divisible on the full-rational-2-torsion curve and a genuine descent leaf would become available. Goal4AS does **not** assert that this happens.

## Required cycle exit

```text
CYCLE_ROUTE_STATUS=PASS_NEW_GATE_FROM_STRONGER_VIEW
CYCLE_ACTIVE_RECEIVER=PHYSICAL_GOAL4L_MARKED_POINT_WITH_KUMMER_CLASS_(d,d,1)
CYCLE_LIVE_CANDIDATES=1
CYCLE_UNTESTED_CANDIDATES=6
CYCLE_EXHAUSTIVE_VIEW_AUDIT=true
CYCLE_BLIND_REDISCOVERY=true
CYCLE_SPLIT_TRIGGERED=false
CYCLE_PARKING_AUDIT_COMPLETE=false
CYCLE_NEW_VIEW=PHYSICAL_MARKED_POINT_RESIDUAL_KUMMER_CLASS_D
CYCLE_NEW_VIEW_SOURCE=BLIND
```

## Credit firewall

Certified provisionally only:

- the required exhaustive-view audit and blind pass were executed;
- the exact square identity `(AS-3)`;
- the physical marked Kummer restriction `(AS-KUMMER)`;
- the candidate ledger/classification above;
- selection of the residual marked Kummer squareclass as the next single active route.

Not certified:

- `d=1`;
- finite support for `d`;
- a 2-Selmer computation;
- a 2-divisibility or infinite-descent theorem;
- an explicit canonical-height contradiction;
- a finite Brauer shortcut;
- any Brauer–Manin obstruction;
- E1, R29-PESCH-E1, Stage35, endpoint, or Perfect Cuboid existence/nonexistence closure.
