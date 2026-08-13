# Stage14-s4 — arithmetic/Kummer bisection bridge

## Current upstream state

Stage14-4ah is merged and proves that every physical rational curve has `M.C>=4`, with the unique extremal square-root candidate an `M`-degree-4 rational bisection. Stage14-s3 is merged and proves the necessary small-point gate

`physical hit d<=B => non-torsion point with canonical height O(log B + log H)`.

At the start of s4, no merged `14-4ai+` artifact containing an explicit or classified `Q`-rational `M`-degree-4 bisection exists on `main`. Therefore s4 cannot honestly claim a completed class-by-class comparison yet.

## Exact bridge contract

When a main-track bisection `C` is supplied, s4 will normalize it and require the following data:

- a rational parameter `z` on the normalization `C~=P1`;
- the degree-two map `r(z)` to the Pythagorean base;
- the Stage14 physical coordinates `(e(z),x(z),y(z),d(z))` with `H_M=d`;
- the induced elliptic point `P_C(z)` on `E_F: W^2=Z(Z-S^2)(Z+X^2)` via the frozen Stage14-4ad/s3 birational map;
- the full-2-torsion Kummer class `(Z,Z-S^2,Z+X^2)` in `(Q(z)^*/Q(z)^{*2})^3`;
- the physical-open and non-torsion exclusions.

The comparison is then mechanical: reduce the three Kummer coordinates modulo squares, record their divisor support, specialize to primitive Pythagorean bases, and compare first-hit heights against the exact active ledger.

## Height compatibility

For an extremal bisection,

`deg(C->P1_r)=2` and `M.C=4`.

Thus for a rational parameter of height `T`, functorial height gives `H(r(z))=T^{2+o(1)}` and `H_M(P(z))=T^{4+o(1)}` away from finitely many exceptional points. Hence a single such rational curve contributes at most the expected fixed-curve scale `B^{2/4+o(1)}=B^{1/2+o(1)}`. This is compatible with the finite Stage14 signal but does not prove existence, dominance, or an asymptotic.

## What can already be concluded

The arithmetic and geometric pictures are compatible at the level required for a future merge:

1. an extremal `M`-degree-4 bisection automatically supplies a degree-two rank-jump multisection;
2. every physical point on it enters the s3 logarithmic canonical-height window;
3. its induced Kummer square classes are the exact s1 descent coordinates to be compared;
4. domination of `V(B)` cannot be decided without explicit/classified bisections from `14-4ai+`.

## Decision

```text
STAGE14_S4=BRIDGE_READY_WAITING_FOR_14_4AI
BISECTION_TO_SELMER_COMPARISON_INTERFACE_LOCKED=true
M_DEGREE4_HEIGHT_EXPONENT_COMPATIBILITY_LOCKED=true
EXPLICIT_M_DEGREE4_BISECTION_IMPORTED=false
BISECTION_CLASSIFICATION_IMPORTED=false
FINITE_BISECTION_COVERAGE_MEASURED=false
BISECTION_DOMINANCE_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=resume Stage14-s4 immediately after merged 14-4ai+ explicit bisection/classification artifact
```
