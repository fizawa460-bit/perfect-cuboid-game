# Stage34-02 — audited Route D and active D1 descent

Status: `AUDITED_PASS_ROUTE_D_SELECTED_D1_ACTIVE_22_SQUARECLASSES_REMAIN`.

## 34-02 hostile audit

PR #1480 hostile audit PASSed the exact Face-3 factorization, genus-5 cover, finite squareclass support, receiver coverage, and conservative theorem funnel on audited head `d54ee6f0eda2814781301cc80ff11a47f92a8c24`.

The exact writeback is `audit-closure.json`.

The audit's wording hardening is applied: Stage34 claims only that **no Lucas/Lehmer identification is proved or source-locked**. This is sufficient to deny BHV credit; it is not a proof that the sequence can never admit such an identification.

## Audited direct cover

On

```text
E_q: y^2=x(x+1)(x+q^2)
```

we have

```text
A_q=x^2+q^2,
B_q=(1+q^2)x^2+4q^2x+q^2(1+q^2),
F3=A_q B_q/(q^2-x^2)^2.
```

Away from `x=+/-q`, `F3(Q)` is a square exactly when the corresponding point lifts to

```text
C_q:
  y^2=x(x+1)(x+q^2),
  z^2=A_q(x)B_q(x).
```

The audited branch computation gives `g(C_q)=5` for all seven locked `q`.

## Pole lock

`pole-torsion-lock.json` exact-replays the Face-3 poles. The rational points above `x=+q` are `(q,+/-q(q+1))`, those above `x=-q` are `(-q,+/-q(q-1))`, and every one doubles to `(0,0)`. Since `(0,0)` is nonzero 2-torsion and the seven locked `q` satisfy `q!=0,+/-1`, the pole points have order 4.

Stage34-01's authoritative receiver population is non-torsion, so the non-pole equivalence has no receiver hole.

## D1 squareclass materialization

For reduced `q=a/b`, `x=X/Z`, a square candidate has

```text
A_h=b^2X^2+a^2Z^2=d u^2,
B_h=b^2(a^2+b^2)X^2+4a^2b^2XZ+a^2(a^2+b^2)Z^2=d v^2,
```

with one positive squarefree `d|rad(2ab)`.

`d1-squareclass-manifest.json` materializes all `104` raw squareclasses.

### Exact filter 1 — sum of two squares

Because

```text
A_h=(bX)^2+(aZ)^2=d u^2,
```

any prime `p==3 mod 4` has even valuation on the left. Such a prime cannot occur in squarefree `d`, where the right side would have odd valuation. This eliminates `74` classes:

```text
104 -> 30.
```

### Exact filter 2 — good-prime projective residues

For a good prime

```text
p ∤ 2ab(a^2-b^2)(a^2+b^2)d,
```

a rational point in squareclass `d` must reduce to some `[X:Z] in P^1(F_p)` for which all three quantities

```text
E_h = X Z (X+Z)(b^2X+a^2Z),
A_h/d,
B_h/d
```

are quadratic residues modulo `p` (zero allowed).

`verify_d1_good_prime_residue_filter.py` exhausts `P^1(F_p)` for eight candidate covers and finds no residue at the stated good prime. `d1-good-prime-residue-filter.json` records the proof-level eliminations:

```text
20/21: d=5,10 blocked mod 23
84/13: d=13,26 blocked mod 31
48/55: d=5,10 blocked mod 23
20/99: d=5,10 blocked mod 23
```

Thus

```text
30 -> 22
```

necessary local squareclasses remain.

Current survivors:

```text
20/21 -> {1,2}
80/39 -> {1,2,5,10,13,26,65,130}
24/7  -> {1,2}
84/13 -> {1,2}
48/55 -> {1,2}
20/99 -> {1,2}
60/11 -> {1,2,5,10}
```

Survival of this finite residue test is **not** Q_p-solubility and is not a rational-point claim.

## Current leaf

```text
D1_CERTIFY_QP_LOCAL_SOLUBILITY_OR_OBSTRUCTION_FOR_22_SURVIVORS
  -> define exact reduction maps from the audited full MW bases to finite local groups;
  -> run proof-complete Mordell--Weil sieve;
  -> send only genuine residual covers to D2 covering / elliptic-Chabauty.
```

## Credit boundary

```text
STAGE34_02_HOSTILE_AUDIT_PASSED=true
ROUTE_D_SELECTED_AUTHORITATIVE=true
D1_RELEASED=true
D1_LOCAL_ELIMINATIONS=82_OF_104
D1_SURVIVING_SQUARECLASSES=22
D1_COMPLETE=false
DIRECT_COVER_RATIONAL_POINTS_COMPLETE=false
ALL_MULTIPLES_CLOSED=false
R29_EXT_CHANG_C_closed=false
PARENT_ROUTE_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
