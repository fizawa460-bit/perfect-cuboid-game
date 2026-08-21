# Stage29-02d — rational lift / quadratic-twist ledger

```text
STATUS=DERIVED_CANDIDATE_PENDING_FRESH_AUDIT
```

Let

```text
q_cub:X_cub -> S_cub
```

be the Q-form of the Beauville canonical double cover from `q-form-adapter.md`.

## Physical open

Beauville's involution has exactly 48 fixed points and the quotient has exactly the corresponding 48 nodes. Therefore, after deleting the node locus, the degree-two map is unramified. Let `U_phys` be the Stage29 positive nondegenerate physical open, further intersected with the smooth locus of the canonical endpoint surface. Then

```text
q_U:X_U -> U_phys
```

is a finite etale double cover over Q.

The physical endpoint question is **not** equivalent to asking whether `X_U(Q)` is nonempty.

## Fiber class

For every `P in U_phys(Q)`, the fiber `q_U^{-1}(P)` is a degree-two etale Q-scheme, hence a `Z/2`-torsor. It determines a class

```text
delta(P) in H^1(Q,Z/2) ~= Q^*/Q^{*2}.
```

The point `P` lifts over Q exactly when `delta(P)=1`. In general, twisting the cover by `delta(P)` gives a Q-form `X_U^{delta(P)}` with a rational point above `P`.

Thus there is an exact descent decomposition at the level of rational points:

```text
U_phys(Q)
 = union_[delta in Q^*/Q^{*2}]
   image( X_U^delta(Q) -> U_phys(Q) ).
```

This is a covering identity, not a finiteness theorem.

## Why this is useful but not yet decisive

It changes the arithmetic receiver from

```text
study arbitrary Q-points directly on the general-type cuboid surface
```

to

```text
classify the quadratic cover class delta(P),
control locally soluble Beauville twists,
and study rational points on the corresponding irregular covers / Albanese torsors.
```

The remaining issue is that `Q^*/Q^{*2}` is infinite. No theorem currently in the repo bounds the occurring squareclasses uniformly for all physical rational points.

In particular, one must **not** argue that the cover is etale on the physical open and therefore only finitely many quadratic twists occur. The physical open is not proper, and reductions of a rational point may meet deleted boundary/node divisors at primes depending on the point.

## Residual receivers

```text
R29-BEAU1B=ExplicitGenericBeauvilleDoubleCoverSquareclassFunction
R29-BEAU1C=PhysicalEndpointLiftSquareclassLocalRamificationLedger
R29-BEAU2=LocallySolubleBeauvilleTwistsToAlbaneseTorsors
```

Desired output of `R29-BEAU1B`:

- an explicit function-field presentation `Q(X_cub)=Q(S_cub)(sqrt(F))` on a dense open;
- exact divisor/parity data for `F`;
- a formula `delta(P)=F(P) mod Q^{*2}` away from zeros/poles;
- compatibility with the 48-node quasi-etale geometry.

Desired output of `R29-BEAU1C`:

- primes at which `delta(P)` may ramify in terms of primitive cuboid coordinates;
- any reciprocity relations among those local squareclasses;
- proof or disproof of any finite-support reduction.

```text
FINITE_TWIST_SET_PROVED=false
UNTWISTED_LIFT_SUFFICES=false
PERFECT_CUBOID_CONCLUSION=NONE
```
