# Stage36 36-09AM source lock: parity-complete Tunnell necessary test and rank-zero full-2 Kummer image

Accessed: 2026-09-07

This leaf generalizes the hostile-audited 36-09AL single branch into a conditional uniform classifier. It does **not** use the BSD converse to Tunnell's theorem.

## A. Tunnell necessary conditions, odd and even squarefree n

Primary theorem species: Jerrold Tunnell, *A classical Diophantine problem and modular forms of weight 3/2*, Invent. Math. 72 (1983), 323-334.

Accessible statement checked against:
- Andrew Sutherland / MIT congruent-number notes used already by 36-09AL;
- *The Congruent Number Problem*, Theorem 3.4: https://l-series.github.io/CNP.pdf

For positive squarefree `n`:

- if `n` is odd and congruent, then

```text
2 * #{n = 2*x^2 + y^2 + 32*z^2}
  = #{n = 2*x^2 + y^2 + 8*z^2};
```

- if `n` is even and congruent, then equivalently with `m=n/2` odd squarefree,

```text
2 * #{m = 4*x^2 + y^2 + 32*z^2}
  = #{m = 4*x^2 + y^2 + 8*z^2}.
```

Only the necessary direction is used. Therefore failure of the parity-appropriate equality proves `n` is non-congruent. By the standard congruent-number equivalence, `E_n : Y^2=X^3-n^2 X` then has Mordell-Weil rank zero over `Q`.

## B. Rank-zero Kummer image

The full-rational-2-torsion Kummer map and Selmer exact sequence are source-locked in hostile-audited 36-09AL via Poonen's weak Mordell-Weil notes.

For ordered roots `(0,+n,-n)`, when `rank E_n(Q)=0`, the mod-2 Kummer image is exhausted by the four rational 2-torsion classes

```text
O       -> (1,1)
(0,0)   -> (-1,-n)
(n,0)   -> (n,2)
(-n,0)  -> (-n,-2*n).
```

The three nonzero 2-torsion classes are nontrivial in `E(Q)/2E(Q)`, hence there is no rational 4-torsion; odd torsion is 2-divisible and contributes nothing modulo 2.

## C. Stage36 squareclass algebra

Hostile-audited 36-09AE gives positive odd squarefree, pairwise coprime `A,B,C,D`, and bits `e,f in {0,1}`, `eta in {+1,-1}`. Put

```text
g = (e+f) mod 2,
n = 2^g * A*B*C*D.
```

Hostile-audited 36-09AJ/AL give the normalized full-2 pair:

```text
eta=+1 : ([2^g*C*D], [2^f*A*D])
eta=-1 : ([-2^g*C*D], [-2^e*A*C])
```

(the `eta=-1` formula includes the audited transposition of the two nonzero ordered roots).

Because `A,B,C,D` are positive odd squarefree with pairwise disjoint prime support, equality of these Stage36 squareclasses with one of the four rank-zero torsion Kummer classes is an exact support/sign/2-adic comparison. The exhaustive result is exactly four sectors, with overlaps allowed when several of `A,B,C,D` equal `1`:

```text
T0/O sector:
  eta=+1, e=f=0, A=C=D=1, B arbitrary       -> (1,1)

T+ sector:
  eta=+1, A=B=D=1, f=1, C arbitrary, e arbitrary -> (n,2)

Tzero sector:
  eta=-1, e=f=0, B=C=D=1, A arbitrary       -> (-1,-n)

T- sector:
  eta=-1, A=B=D=1, f=1, C arbitrary, e arbitrary -> (-n,-2n)
```

Outside the union of these four sectors, a Stage36 everywhere-locally-soluble class with a failed parity-appropriate Tunnell equality cannot lie in `E_n(Q)/2E_n(Q)`. The Selmer exact sequence then forces a nonzero `Sha(E_n)[2]` class, so the corresponding projective full-2 covering has no rational point.

## Scope firewall

- Passing Tunnell's equality is **not** used to infer positive rank; that converse is BSD-conditional.
- Membership in one of the four torsion-shaped sectors does not by itself prove a retained-open Stage36 receiver point. It only means the rank-zero Kummer-image test does not exclude that sector; coordinate/open-boundary compatibility still has to be checked.
- The classifier is conditional on everywhere-local solubility of the full covering and on failure of the parity-appropriate Tunnell necessary equality.
- No global enumeration of all variable `n`, no uniform Selmer computation, no candidate-parameter shrink, receiver emptiness, R29/Q11/endpoint closure, or perfect-cuboid claim is granted here.
