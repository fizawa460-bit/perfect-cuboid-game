# Stage34-02 — sequence classification, Route-D audit, and D1 release

Status: `AUDITED_PASS_ROUTE_D_SELECTED_D1_RELEASED_FIRST_LOCAL_FILTER_PASS`.

## Audited classification

The exact EXT-C object has **no Lucas/Lehmer identification that is proved or source-locked**, and it is not identified with the standard elliptic-divisibility denominator object. The load-bearing quantity remains

```text
N_{q,T}(n)=Num(F3(nP_q+T))
```

for rank one and the analogous `N_T(a,b)` on the rank-two lattice.

Therefore no Bilu--Hanrot--Voutier, standard elliptic Zsigmondy, shifted EDS denominator, or arithmetic-dynamical theorem receives direct Stage34 credit merely by topic similarity. Routes A/B/C remain near-miss/background routes; Route D is the audited primary route.

The hostile audit on PR #1480 PASSed the exact Face-3 factorization, genus-5 computation, finite squareclass support, receiver coverage, and conservative theorem funnel on audited head `d54ee6f0eda2814781301cc80ff11a47f92a8c24`. The writeback is recorded in `audit-closure.json`.

## Exact Route-D reduction

On

```text
E_q: y^2=x(x+1)(x+q^2)
```

the Face-3 value factors as

```text
A_q(x)=x^2+q^2
B_q(x)=(1+q^2)x^2+4q^2x+q^2(1+q^2)

F3(Q)=A_q(x)B_q(x)/(q^2-x^2)^2.
```

Away from `x=+/-q`, the square condition is exactly the rational-point problem on

```text
C_q:
  y^2=x(x+1)(x+q^2)
  z^2=A_q(x)B_q(x),
```

and the audited branch calculation gives `g(C_q)=5` for all seven locked `q`.

## Pole hardening after hostile audit

The audit requested an explicit receiver lock for the two Face-3 poles. This is now materialized in `pole-torsion-lock.json`.

For the Weierstrass model

```text
y^2=x^3+(1+q^2)x^2+q^2x,
```

the rational points over `x=q` are `(q, +/-q(q+1))`, and those over `x=-q` are `(-q, +/-q(q-1))`. Exact duplication gives

```text
2Q=(0,0)
```

for every such pole point. Since `(0,0)` is nonzero 2-torsion and all seven locked `q` satisfy `q!=0,+/-1`, every pole point has order 4. Stage34-01's authoritative receiver population is the non-torsion rational population, so excluding the poles from the non-pole Face-3 equivalence creates no receiver hole.

This pole lock gives no cover-point or receiver-closure credit by itself.

## Finite squareclass descent

For reduced `q=a/b`, `x=X/Z`, `gcd(X,Z)=1`, define

```text
A_h=b^2X^2+a^2Z^2,
B_h=b^2(a^2+b^2)X^2+4a^2b^2XZ+a^2(a^2+b^2)Z^2.
```

The audited identity

```text
B_h-(a^2+b^2)A_h=4a^2b^2XZ
```

implies that any square solution has

```text
A_h=d u^2,
B_h=d v^2
```

for one positive squarefree `d|rad(2ab)`.

## D1 first exact local filter

`d1-squareclass-manifest.json` materializes all raw squareclasses and applies the first proof-level local filter.

Because

```text
A_h=(bX)^2+(aZ)^2=d u^2,
```

for every prime `p == 3 mod 4`, the valuation `v_p(U^2+V^2)` is even. If such a prime divided squarefree `d`, the right side would have odd `p`-valuation. Hence no `p == 3 mod 4` may divide `d`.

This reduces the seven raw collections from

```text
104 squareclasses total
```

to

```text
30 surviving necessary local squareclasses total.
```

Per fiber:

```text
20/21 -> {1,2,5,10}
80/39 -> {1,2,5,10,13,26,65,130}
24/7  -> {1,2}
84/13 -> {1,2,13,26}
48/55 -> {1,2,5,10}
20/99 -> {1,2,5,10}
60/11 -> {1,2,5,10}
```

The 74 eliminated squareclasses are impossible. Survival of the remaining 30 is only a necessary local condition and does not imply a rational cover point.

## Current leaf

```text
D1_LOCAL_SOLUBILITY_FILTER_30_SURVIVING_SQUARECLASSES
  -> retain only genuinely locally soluble covers;
  -> define exact reduction maps from the audited full MW bases to finite local groups;
  -> run proof-complete Mordell--Weil sieve;
  -> use D2 genus-5 covering/elliptic-Chabauty only for residual covers.
```

## Credit boundary

```text
STAGE34_02_HOSTILE_AUDIT_PASSED=true
ROUTE_D_SELECTED_AUTHORITATIVE=true
D1_RELEASED=true
D1_FIRST_LOCAL_FILTER_PASS=true
D1_COMPLETE=false
DIRECT_COVER_RATIONAL_POINTS_COMPLETE=false
ALL_MULTIPLES_CLOSED=false
R29_EXT_CHANG_C_closed=false
PARENT_ROUTE_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
