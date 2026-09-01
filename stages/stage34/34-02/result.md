# Stage34-02 — audited Route D with StageA2 successive factor-cover descent

Status: `ACTIVE_D1_92_FACTOR_BRANCH_QUOTIENT_CLASSIFICATION`.

## Locked foundation

- Stage34-01 exact object/global population: hostile-audited CLOSED.
- Stage34-02 Route-D algebraic reduction: hostile-audited PASS on `d54ee6f0eda2814781301cc80ff11a47f92a8c24`.
- Exact direct cover, fourteen `d=1,2` split quartics, their seven common Jacobians, full MW bases, fourteen global Q-isomorphisms and exact receiver-x pullbacks remain locked.
- Earlier four-prime and fixed-quotient MW panels are retained as exact nonclosing diagnostics.

## StageA2 method import

Closed/audited StageA2 A2-4/A2-5 supplies an applicable method, not a family-specific theorem import:

```text
factor square condition
 -> finite exact squareclass covers
 -> elementary/local branch obstructions
 -> remaining reconstruction square as a genus-one quartic
 -> binary-quartic invariants / Jacobian
 -> complete pullback only when the auxiliary point set is complete.
```

StageA2's concrete rank-zero `15.a5` result is **not** imported.

## Common four-factor template

For `q=a/b`, put

```text
A=aU+bV,
B=bU+aV.
```

For d=1:

```text
U=T^2-S^2,
V=2TS.
```

For d=2:

```text
U=2T^2-S^2,
V=2T^2-4TS+S^2.
```

Every exact factor branch has

```text
U=delta1*r1^2,
V=delta2*r2^2,
A=delta3*r3^2,
B=delta4*r4^2.
```

Odd squareclass support is confined to primes dividing `2ab(a^2-b^2)`.

## Exact branch compression

The certified finite descent now reads

```text
29,952  exact squareclass over-approximation
 -> 1,946  good support-external prime survivors
 -> 1,214  d=2 Legendre-2 support refinement
 -> 1,024  after unconditional rank-zero reconstruction-quotient closure
 ->    92  after complete odd support-prime projective reduction.
```

The final support-prime step uses the primitive integral reduction lemma: a rational branch point can be scaled to coprime integral `[T:S]`, all four auxiliary square roots are p-integral at an odd support prime, and therefore a rational point must reduce to a projective `F_p` point satisfying all four square equations. Absence of such a reduction is a rigorous global branch obstruction.

Generation-1 replay:

```text
run      33512504700
job      99871456739
head     eec7478aac11151986be5df00487b464389eed10
artifact 9802225387
digest   sha256:eee10b6d11542422a1f8fbda84a091ebd1208353a31841bc969f812827cbe18b
```

Result:

```text
d=2: 20 -> 0
d=1: 1004 -> 92
```

Thus **all d=2 factor branches are globally excluded**. This is not yet receiver closure because the d=1 side remains.

The 92 d=1 survivors are:

```text
20/21 : 24   reconstruction species 210
80/39 : 12   species 390
24/7  :  8   species 21
84/13 :  8   species 546
48/55 :  8   species 330
20/99 : 16   species 110 or 30
60/11 : 16   species 330
```

Evidence:

- `d2-stageA2-full-support-projective-lock.json`
- `run_d2_stageA2_full_support_projective.py`
- `d2-stageA2-reconstruction-rank-lock.json`
- `d2-stageA2-reconstruction-diagonal-lock.json`

## Current exact leaf

Each surviving d=1 branch already passed the `U*V` reconstruction genus-one quotient. It also forces five further genus-one pair-product quotient conditions:

```text
U*A,
U*B,
V*A,
V*B,
A*B.
```

The next task is to build those quotient quartics for all 92 branches, deduplicate their Jacobians, certify the required MW ranks, and prioritize every rank-zero quotient for complete point enumeration and exact pullback. Positive rank alone earns no point or closure credit.

## Credit boundary

```text
D2_STAGEA2_D2_FACTOR_BRANCHES_CLOSED=true
D2_STAGEA2_D1_FACTOR_BRANCH_SURVIVORS=92
D2_ALL_FACTOR_BRANCHES_CLOSED=false
DIRECT_COVER_RATIONAL_POINTS_COMPLETE=false
ALL_MULTIPLES_CLOSED=false
R29_EXT_CHANG_C_closed=false
PARENT_ROUTE_CLOSED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
