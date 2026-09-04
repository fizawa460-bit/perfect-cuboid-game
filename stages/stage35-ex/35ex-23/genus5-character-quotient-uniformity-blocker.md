# Stage35-EX 35EX-23 — genus-5 character quotients and nonisotrivial uniformity blocker

## Scope and authority

Continue only after hostile re-audit PASS of 35EX-22 at exact head
`f4276680239bb2b84687f8ba8ac8964de0613552` (review `5111539148`), merged to main as
`2e07dde92fdf270fff1233635a7cb4cea1427080`.

No E1/R29/FIB2/J12/Stage35/perfect-cuboid credit is granted here.

The selected candidate is the already-preserved

```text
E1-GENUS5-MULTIQUADRATIC-FIBER-CHARACTER-DESCENT
```

from hostile-audited 35EX-21B. No fresh breadth audit was required merely to select it.

## 1. Exact generic fiber

Use the audited 35EX-21 generic fiber over

```text
K = Q(B1),  B1: p^2 = 1+x^2.
```

Put

```text
a = x^2,
f1 = y^2+1,
f2 = y^2+a,
f3 = y^2+1+a.
```

Then the normalized generic fiber is

```text
C/K:
q^2 = f1,
z^2 = f2,
w^2 = f3.
```

Generically the six roots of `f1*f2*f3` are distinct, and `C` is the audited genus-5 `(Z/2)^3` cover of `P1_y`.

## 2. All seven nontrivial deck-character quotients

For every nonempty subset `I` of `{1,2,3}`, define

```text
C_I: v_I^2 = product_{i in I} f_i.
```

The quotient map `C -> C_I` is explicit:

```text
v_1=q, v_2=z, v_3=w,
v_12=q*z, v_13=q*w, v_23=z*w,
v_123=q*z*w.
```

It is exactly the quotient by the kernel of the corresponding nontrivial character of the deck group.

Because the product has degree `2*|I|` and distinct roots generically,

```text
|I|=1  => genus(C_I)=0   (3 quotients),
|I|=2  => genus(C_I)=1   (3 quotients),
|I|=3  => genus(C_I)=2   (1 quotient).
```

Thus the positive-genus character content is exactly three genus-one quartics plus one genus-two even sextic.

The three genus-one quotients are

```text
E12: V12^2=(y^2+1)(y^2+a),
E13: V13^2=(y^2+1)(y^2+1+a),
E23: V23^2=(y^2+a)(y^2+1+a).
```

Each has rational points at infinity over `K`, so each is an elliptic curve after choosing one such point.

## 3. The genus-two character quotient splits into two elliptic quotients

The remaining character quotient is

```text
G123: H^2=(y^2+1)(y^2+a)(y^2+1+a).
```

Its even involution `sigma:(y,H)->(-y,H)` and the product of `sigma` with the hyperelliptic involution give two explicit genus-one quotients:

```text
Eplus:
  Yplus^2=(X+1)(X+a)(X+1+a),
  X=y^2,
  Yplus=H;

Eminus:
  Yminus^2=X(X+1)(X+a)(X+1+a),
  X=y^2,
  Yminus=y*H.
```

The pullbacks of invariant differentials are

```text
Eplus:  dX/Yplus  = 2*y*dy/H,
Eminus: dX/Yminus = 2*dy/H.
```

Hence the two elliptic quotients account for the two-dimensional differential space of `G123`.

## 4. Five elliptic factors account for the full genus-5 differential space

The three pair-character elliptic quotients contribute

```text
dy/(q*z),
dy/(q*w),
dy/(z*w),
```

and the two elliptic quotients of `G123` contribute

```text
dy/(q*z*w),
y*dy/(q*z*w).
```

The first three lie in distinct deck-character eigenspaces. The last two lie in the `123` deck-character eigenspace but have opposite parity under `y -> -y`. They are therefore linearly independent. There are five of them, equal to `genus(C)=5`.

Consequently the natural product of the five elliptic quotient Jacobians has full-rank differential and equal dimension to `Jac(C)`; in characteristic zero the induced homomorphism is an isogeny.

This is also consistent with the general Kani-Rosen idempotent-decomposition framework; however the present leaf does not rely opaquely on that theorem because the quotient equations and the full differential span are checked directly.

Background source lock:

```text
E. Kani and M. Rosen,
"Idempotent relations and factors of Jacobians",
Mathematische Annalen 284 (1989), 307-328.
EuDML: https://eudml.org/doc/164555
```

## 5. Exact j-invariants: every elliptic factor moves

For a pair quartic

```text
V^2=(y^2+A)(y^2+B),
```

with generic `A*B*(A-B)!=0`, the branch-point cross-ratio gives

```text
j(A,B)=16*(A^2+14*A*B+B^2)^3 / (A*B*(A-B)^4).
```

Therefore

```text
j12 = 16*(a^2+14*a+1)^3 / (a*(a-1)^4),

j13 = 16*(a^2+16*a+16)^3 / (a^4*(a+1)),

j23 = 16*(16*a^2+16*a+1)^3 / (a*(a+1)).
```

For `Eplus`, translating its three finite branch roots to Legendre form gives

```text
jplus = 256*(a^2-a+1)^3 / (a^2*(a-1)^2).
```

For `Eminus`, the four branch points `{0,-1,-a,-1-a}` give

```text
jminus = 256*(a^4-a^2+1)^3 / (a^4*(a-1)^2*(a+1)^2).
```

All five are nonconstant rational functions of the generic base parameter `a=x^2`. Hence all five elliptic factors are nonisotrivial over the first-source base.

This is the exact uniformity obstruction for the naive character-quotient plan: the genus-5 fiber does split completely into elliptic factors up to isogeny, but it does **not** collapse to one fixed elliptic curve or a fixed finite list of constant elliptic curves on which one global Mordell-Weil computation could be replayed.

## 6. Arsenal routing

Formal Arsenal `S31-W01` is applicable only **fiberwise**: once one of the displayed genus-one quartics is fixed, it can certify an explicit quartic-to-Weierstrass birational adapter with denominator and exceptional-locus accounting.

It does not supply a uniform Mordell-Weil theorem for this nonisotrivial family and explicitly grants no automatic integrality transfer.

Exact card lock:

```text
docs/arsenal/cards/formal/S31-W01.md
blob_sha=122a6c1c5c871c1c7b797017e854de8ec55e7c50
role=GENUS_ONE_QUARTIC_ELLIPTIC_BIRATIONAL_ADAPTER
```

Formal `S34-W02` is not yet unlocked: it requires a certified full Mordell-Weil group for the fixed quotient under study, whereas the current five factors move with `a`.

## 7. What is proved and what is not

Proved in this leaf:

```text
GENUS5_NONTRIVIAL_CHARACTER_QUOTIENTS=7
GENUS0_CHARACTER_QUOTIENTS=3
GENUS1_CHARACTER_QUOTIENTS=3
GENUS2_CHARACTER_QUOTIENTS=1
GENUS2_BIELLIPTIC_SPLIT_PROVED=true
TOTAL_ELLIPTIC_FACTORS_AFTER_SPLIT=5
FULL_GENUS5_DIFFERENTIAL_ACCOUNTING=true
GENERIC_FIBER_JACOBIAN_FIVE_ELLIPTIC_ISOGENY=true
ALL_FIVE_ELLIPTIC_FACTORS_NONISOTRIVIAL=true
FIXED_ELLIPTIC_CURVE_REDUCTION_FROM_CHARACTER_QUOTIENTS=false
UNIFORM_FIXED_MW_COMPUTATION_UNLOCKED=false
```

Not proved:

- that the five elliptic families have no exploitable global section/height/Selmer structure;
- that simultaneous compatibility among the five quotient images is impossible;
- that rational points on the total surface are classified;
- that a primitive-source reverse adapter is complete;
- E1 or any parent/endpoint closure.

Therefore

```text
CURRENT_GENUS5_CHARACTER_QUOTIENT_ROUTE
 = FROZEN_AT_NONISOTRIVIAL_FIVE_ELLIPTIC_COMPATIBILITY_LAYER.
```

A future reopening must supply genuinely uniform arithmetic on the moving elliptic factors, or an exact compatibility theorem coupling their quotient images. Merely applying a fixed-curve Mordell-Weil calculation fiber by fiber is not a uniform closure theorem.

## 8. Cycle consequence and credit firewall

The five-elliptic factorization is a materially new structural view even though the direct fixed-curve route is blocked. Therefore a fresh exhaustive-view/blind-rediscovery audit is required before selecting a successor route.

```text
CYCLE_ROUTE_STATUS=BLOCKED_NEW_PATTERN_ISOLATED
CYCLE_NEW_PATTERN=FIVE_NONISOTRIVIAL_ELLIPTIC_QUOTIENT_FACTORS_WITH_SIMULTANEOUS_COMPATIBILITY
FRESH_BREADTH_AUDIT_REQUIRED=true
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
