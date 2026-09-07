# Stage36 36-09AL source lock: Tunnell non-congruence, full-2 Kummer image, and Selmer-to-Sha exact sequence

Accessed: 2026-09-07

This leaf uses three standard ingredients and applies them only to the explicit audited/provisional Stage36 branch with `n=73073`.

## A. Tunnell's unconditional necessary condition for odd squarefree congruent numbers

Source:
- Andrew Sutherland, MIT 18.737 Algebraic Groups / Arithmetic Geometry notes (Spring 2020), Theorem 3.26.7:
  https://math.mit.edu/~setia/7370sp20.pdf

The notes state that for an odd squarefree positive integer `n`, if `n` is congruent then

```text
#{(x,y,z) in Z^3 : n = 2*x^2 + y^2 + 32*z^2}
  = (1/2) * #{(x,y,z) in Z^3 : n = 2*x^2 + y^2 + 8*z^2}.
```

The same notes state the standard congruent-number equivalence: `n` is congruent iff the elliptic curve

```text
E_n : Y^2 = X^3 - n^2 X
```

has positive Mordell-Weil rank over `Q`.

Stage36 uses only the unconditional direction. A failure of the displayed count equality proves `n` is not congruent and hence `rank E_n(Q)=0`. No BSD converse is used.

For `n=73073=7*11*13*73`, the verifier exhaustively counts all signed integer triples and obtains

```text
A32 = #{73073 = 2*x^2+y^2+32*z^2} = 480,
A8  = #{73073 = 2*x^2+y^2+8*z^2}  = 896.
```

Since `2*A32=960 != 896=A8`, Tunnell's necessary condition fails.

## B. Full rational 2-descent Kummer map

Source:
- Bjorn Poonen, *The Selmer group, the Shafarevich-Tate group, and the Weak Mordell-Weil Theorem*, §10:
  https://math.mit.edu/~poonen/f01/weakmw.pdf

For

```text
E : y^2=(x-e1)(x-e2)(x-e3)
```

with full rational 2-torsion, the Kummer map to `H^1(Q,E[2]) ~= (Q*/Q*^2)^2` sends a nonexceptional point `(x,y)` to

```text
([x-e1],[x-e2]).
```

The symmetric three-coordinate version is `([x-e1],[x-e2],[x-e3])` with product one; at a 2-torsion point the missing component is determined by the product-one rule. The same notes give the fundamental exact sequence

```text
0 -> E(Q)/2E(Q) -> Sel^2(E/Q) -> Sha(E/Q)[2] -> 0.
```

Stage36 applies this to the ordered normalized roots

```text
(e1,e2,e3)=(0,n,-n),  n=73073.
```

The four rational 2-torsion Kummer pairs are exactly

```text
O            -> (1,1),
(0,0)        -> (-1,-n),
(n,0)        -> (n,2),
(-n,0)       -> (-n,-2*n).
```

The nonzero 2-torsion classes are nontrivial in `E(Q)/2E(Q)`, so none of the three nonzero 2-torsion points is twice a rational point. Therefore there is no rational 4-torsion. Since Tunnell gives rank zero, odd-order torsion contributes nothing modulo 2 and absence of rational 4-torsion implies that these four classes exhaust `E(Q)/2E(Q)`.

## C. Stage36 normalized covering class

Audited/provisional Stage36 36-09AJ identifies the raw full-2 class for the `B=7` branch as

```text
[-143, 1898, -1606]
```

on ordered raw roots `(0,T,-T)` with `T=-4*n`. Rational square scaling to `E_n` sends the ordered roots to `(0,-n,+n)`. Reordering to the standard normalized root order `(0,+n,-n)` therefore transposes components 2 and 3, giving normalized pair

```text
(-143,-1606).
```

This pair differs in `Q*/Q*^2` from each of the four Mordell-Weil Kummer pairs above.

## Scope firewall

36-09AK separately proves that this exact covering is everywhere locally soluble, hence its full-2 class lies in `Sel^2(E_73073/Q)`. Combining that local result with the rank-zero/Kummer-image calculation and the Selmer exact sequence proves that this **one explicit class** maps to a nonzero element of `Sha(E_73073)[2]` and that this covering has no rational point.

This does not classify all branches, all of `Sel^2(E_73073)`, all of `Sha(E_73073)[2]`, or any uniform Stage36 parameter family. It does not by itself shrink the Stage36 parameter set or close R29-CAMP2/Q11/the endpoint.