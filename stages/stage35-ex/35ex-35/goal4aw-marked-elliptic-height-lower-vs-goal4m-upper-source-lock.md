# Stage35-EX Goal4AW source lock — marked elliptic canonical-height lower bound versus Goal4M upper window

Scope: consume exact-green Goal4AV and test the blind-audit candidate `EXPLICIT_CANONICAL_HEIGHT_LOWER_VS_GOAL4M_UPPER_CONSTANTS`. The only allowed target is the **physical marked Goal4L point**. Audited Stage35-EX authority remains V74 / Goal4AK; this leaf is provisional and grants no hostile-audit, E1, Stage35, endpoint, or Perfect Cuboid credit.

## Exact-green parent

Goal4AV is exact-head green at

```text
head = 47338365100fc73dee2f82cf9a2025230620ae22
aggregate = 34294868746
verify-stage35-ex-current = 102290540930
```

Goal4AV classified the concrete product-one common-Kummer mechanism as a non-pruning coefficient-torsor shadow. Goal4AW therefore changes lens rather than iterating that squareclass relation.

## Repository source chain

Goal4L supplies the elliptic family and, crucially, the physical non-torsion condition:

```text
E_q: Y^2=X*(X-1)*(X+q^2),
1+q^2=h_q^2,
every physical endpoint maps to a non-torsion E_q(Q) point.
```

Goal4M / historical Stage14-s3 supply only the upper window

```text
physical hit with space-diagonal cutoff B_cut
  -> hhat(P_q)=O(log B_cut).
```

The historical proof obtains this from fixed-degree birational formulas plus a Weil-height/canonical-height comparison whose curve-invariant contribution is `O(log H)`. It does **not** freeze a numerical coefficient `C_up` in

```text
hhat(P_q) <= C_up*log(B_cut)+C0.                     (AW-UP)
```

The Stage14 literature audit explicitly did not import Lang/Szpiro or any uniform positive lower bound.

Goal4AT gives, on a source-marked endpoint orientation,

```text
q=(C_edge^2-B_edge^2)/(2*B_edge*C_edge).
```

This supplies an upper parameter-height adapter because `B_edge,C_edge < B_cut`, but it supplies no lower bound forcing the height of `q` to grow proportionally to `log B_cut`.

## Exact integral model on a reduced Pythagorean base

Write

```text
q=r/s,  gcd(r,s)=1, s>0.
```

Since `1+q^2` is a rational square, there is an integer `t>0` with

```text
r^2+s^2=t^2,
gcd(r,s)=gcd(r,t)=gcd(s,t)=1.
```

After

```text
x=s^2*X,
y=s^3*Y,
```

Goal4L becomes the integral model

```text
E_{r,s}: y^2=x*(x-s^2)*(x+r^2).                    (AW-1)
```

Its exact invariants are

```text
a2=r^2-s^2,
a4=-r^2*s^2,
Delta_raw=16*r^4*s^4*t^4,                           (AW-2)
c4=16*(r^4+r^2*s^2+s^4),                            (AW-3)
j=256*(r^4+r^2*s^2+s^4)^3/(r^4*s^4*t^4).           (AW-4)
```

For every odd prime `ell | r*s*t`, `(AW-3)` is an `ell`-adic unit:

- if `ell|r`, then the bracket is `s^4 mod ell`;
- if `ell|s`, then the bracket is `r^4 mod ell`;
- if `ell|t`, then `r^2=-s^2 mod ell`, so the bracket is `s^4 mod ell`.

Thus the displayed integral model is minimal and multiplicative at each such odd prime. Consequently

```text
v_ell(Delta_min)=4*v_ell(r*s*t),
ord_ell(N_E)=1                                      (AW-5)
```

for odd `ell|rst`. Goal4AW does not need or claim a complete 2-adic minimal-model classification.

This is useful source arithmetic, but it still does not relate `log|Delta_min|` **from below** to the physical endpoint cutoff `log B_cut`.

## External explicit lower-bound theorem

External source lock:

```text
author=Clayton Petsche
title=Small rational points on elliptic curves over number fields
journal=New York Journal of Mathematics 12 (2006), 257-268
arxiv=math/0508160v2
theorem=Theorem 2
```

For `k=Q`, Petsche's Theorem 2 gives every non-torsion `P in E(Q)` the explicit bound

```text
hhat(P) >= log|Delta_min(E)| /
  (10^15 * sigma(E)^6 * log^2(104613*sigma(E)^2)),  (AW-P)
```

where `sigma(E)=log|Delta_min(E)|/log N_E` is the Szpiro ratio (with the usual convention at everywhere-good reduction). Goal4L's physical point is non-torsion, so the theorem is semantically applicable to each physical specialized curve.

The paper itself stresses that the coefficient depends on the Szpiro ratio; a uniform bound on that ratio is not part of this theorem. The repository contains no source-locked uniform Szpiro-ratio theorem for the Goal4L moving family.

## Exact comparison contract

To turn `(AW-P)` and `(AW-UP)` into eventual physical-endpoint elimination, the retained route would need all of the following numerical statements on the same population:

```text
(AW-C1) hhat(P_q) <= C_up*log B_cut + C0,
        with explicit source-locked C_up,C0;

(AW-C2) log|Delta_min(E_q)| >= c_Delta*log B_cut - C_Delta,
        with explicit c_Delta>0;

(AW-C3) sigma(E_q) <= Sigma,
        with explicit uniform Sigma;
```

and then a strict coefficient win

```text
c_Delta /
(10^15*Sigma^6*log^2(104613*Sigma^2)) > C_up.       (AW-C4)
```

Current exact sources provide none of `(AW-C1)` as a numerical constant, `(AW-C2)`, or `(AW-C3)`. Therefore `(AW-C4)` cannot even be evaluated, let alone proved.

The absence of `(AW-C2)` is not repaired by the formula for `q`: Goal4AT gives only an upper size bound for the numerator/denominator of `q` in terms of `B_cut`; no current theorem prevents a large endpoint from mapping to a comparatively small-height base parameter.

The absence of `(AW-C3)` is not repaired by `(AW-5)`: the odd part of the conductor records the radical of `rst`, whereas the discriminant records prime exponents. Goal4AW does not assume a radical/Szpiro/ABC estimate absent from the source chain.

## Verdict

Positive progress:

```text
GOAL4AW_PHYSICAL_NONTORSION_APPLICABILITY=true
GOAL4AW_EXACT_INTEGRAL_PYTHAGOREAN_MODEL=true
GOAL4AW_ODD_PRIME_MINIMAL_DISCRIMINANT_CONDUCTOR_ADAPTER=true
GOAL4AW_PETSCHE_EXPLICIT_LOWER_BOUND_SOURCE_LOCKED=true
```

But the elimination comparison is blocked:

```text
EXPLICIT_GOAL4M_UPPER_COEFFICIENT_LOCKED=false
DISCRIMINANT_LOWER_GROWTH_VS_ENDPOINT_HEIGHT_PROVED=false
UNIFORM_SZPIRO_RATIO_BOUND_PROVED=false
STRICT_LOWER_VS_UPPER_COEFFICIENT_WIN_PROVED=false
EVENTUAL_ENDPOINT_ELIMINATION_PROVED=false
```

Route classification:

```text
EXPLICIT_CANONICAL_HEIGHT_LOWER_VS_GOAL4M_UPPER_CONSTANTS
  -> BLOCKED_MISSING_UNIFORM_HEIGHT_DISCRIMINANT_SZPIRO_ADAPTERS.
```

This is a current-source verdict, not a theorem that no future family-specific height argument can work.

## Candidate-ledger consequence and next exact leaf

The fresh exhaustive-view ledger in Goal4AS listed `CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY` as a distinct untested lens. The marked-height route is now frozen at a precise missing-adapter boundary, while the common-Selmer product-one mechanism was frozen by Goal4AV.

Next exact leaf:

```text
35EX-35_GOAL4AX_CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY_PREFLIGHT
```

Bounded question:

```text
can the three primitive face Pythagorean structures and the three space-diagonal
couplings be assembled into one exact cross-face norm/lattice torsor whose local
compatibility imposes a condition not already equivalent to the endpoint equations,
primitivity dictionary, marked Kummer product-one relation, or full Brauer route?
```

If every such candidate collapses to already-retained endpoint identities, record that equivalence rather than manufacturing a new obstruction.

## Credit firewall

Not certified:

- a numerical Goal4M canonical-height upper constant;
- a uniform lower discriminant-growth constant in endpoint height;
- a uniform Szpiro-ratio bound for the moving family;
- a Lang/Szpiro/ABC conjectural input;
- a canonical-height contradiction or eventual endpoint elimination;
- a finite-height exhaustive reduction;
- E1, R29-PESCH-E1, Stage35, endpoint, or Perfect Cuboid existence/nonexistence closure.
