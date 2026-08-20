# StageA1 A1-11 — audited elliptic-adapter firewall, relevance repair, and exact freeze wall

## Scope

A1-8 gives the elliptic quotient

```text
E: Y^2=Q(z),
Q(z)=z^4-20z^2+256z-412,
```

and the genus-2 quotients

```text
G0: W0^2=(z^2-4)Q(z),
G+: W+^2=(z+2)Q(z),
G-: W-^2=(z-2)Q(z).
```

A1-9/A1-10 decomposed the rational points of these quotient curves into squareclasses `delta` via

```text
T_delta: Q(z)=delta*v^2.
```

A1-11 originally attempted to classify ten nontrivial A1-10 twists and proposed a freeze there. Independent audit found that the same-`j` adapter firewall is correct, but the routing was not: a point coming from the original first-two-cover curve already lies on `E`, so `Q(z)=Y^2` is itself a rational square. Therefore every actual first-two-cover lift has squareclass

```text
delta=+1.
```

All `delta != 1` branches are quotient-side rational-point branches only. They are not distinct perfect-cuboid candidate branches.

All statements remain specific to the corrected equation-(6) Hilbert-cube family.

## 1. Exact elliptic adapter firewall — PASS

For

```text
E_delta: W^2=X^3+7668*delta^2*X+489456*delta^3,
```

one has

```text
c4(E_delta)=-368064*delta^2,
c6(E_delta)=-422889984*delta^3.
```

For non-special `j=357911/950`, a claimed Q-isomorphism from a candidate model `E'` to `E_delta` must have one rational scaling `u` with

```text
c4(E_delta)/c4(E')=u^4,
c6(E_delta)/c6(E')=u^6.
```

Thus equality of `j` alone is not a legal rank/torsion adapter.

Independent audit reproduces the five submitted rejections:

```text
32110.x1   is not E_+13,
256880.cx1 is not E_-13,
32490.s1   is not E_+57,
259920.fm1 is not E_-57,
288990.bg1 is not E_-39.
```

For the first two examples the `c4` ratios are respectively

```text
5184 = 2^6*3^4,
324  = 2^2*3^4,
```

neither a rational fourth power. The published ranks of these same-`j` rows must not be imported into StageA1 as ranks of the exact target twists.

This firewall remains useful even though the non-`delta=1` twists are not first-two-cover branches.

## 2. Audit relevance correction: only `delta=1` can lift to `C`

For every rational point on the A1-8 first-two-cover curve `C`, the quotient map gives

```text
Y^2=Q(z).
```

Hence `Q(z)` has squareclass `+1`. Since A1-9/A1-10 define `delta` to be the signed squareclass of `Q(z)`, any point that actually lifts from `C` satisfies

```text
delta=+1.                                             (A1.11.1)
```

The quartic `Q` has no rational root, so there is no rational `Q(z)=0` exception.

Consequences:

- the A1-9 `delta=+19` elimination is mathematically correct as a statement about the quotient torsor `T_19`, but it does not remove a distinct first-two-cover/perfect-cuboid path; such a lift would already require `delta=1`;
- the A1-10 sixteen-squareclass decomposition is an exact decomposition of the finite affine `G0(Q)` locus, but only its `delta=1` component is relevant after intersecting back with `E`;
- the ten A1-11 twists `±13,±39,±57,±247,±741` are not the remaining StageA1 bottleneck.

This is a routing/accounting correction, not a failure of the A1-9/A1-10 algebra.

## 3. New exact 2-adic obstruction on the quotient torsors

Although the nontrivial squareclasses are quotient-side only, audit also found a genuine new exact local reduction.

For reduced `z=a/b`, put

```text
H(a,b)=a^4-20a^2b^2+256ab^3-412b^4.
```

A rational point on `T_delta` gives, over `Q_2`, a primitive pair `(a,b)` and

```text
H(a,b)=delta*V^2.
```

For primitive `(a,b)`, direct residue analysis modulo `32` gives

```text
H(a,b) mod 32 in {1,4,17}.                           (A1.11.2)
```

For odd `delta`, every square unit modulo `8` is `1`; reducing `H=delta*V^2` modulo `32` therefore forces

```text
delta == 1 (mod 8).                                  (A1.11.3)
```

So `T_delta(Q_2)=empty` whenever odd `delta` is not `1 mod 8`.

Applied to the previously recorded quotient squareclasses:

```text
G-  quotient classes surviving this Q2 test:  {+1}
G+  quotient classes surviving this Q2 test:  {+1,-247}
G0  quotient classes surviving this Q2 test:  {+1,-39,+57,-247}
```

Among the ten twists originally targeted by A1-11, seven are immediately Q2-empty:

```text
+13, -13, +39, -57, +247, +741, -741.
```

Only

```text
-39, +57, -247
```

survive this local test. Again, these nontrivial survivors are quotient-side branches, not separate lifts from `C`.

The earlier `delta=+19` torsor is also Q2-empty by this criterion, so the A1-9 global rank-zero argument remains valid but is stronger than needed for that branch.

## 4. The true remaining StageA1 receiver

After the relevance repair, the actual first-two-cover problem is the `delta=1` branch:

```text
Q(z)=v^2,
z+2=s^2,
z-2=t^2,                                         (A1.11.4)
```

or equivalently the A1-8 exact simultaneous-square reconstruction on `E`.

The elliptic Jacobian/model for `delta=1` is already audited:

```text
E_1: W^2=X^3+7668X+489456
      ~_Q 6080.r1,
rank(E_1(Q))=1,
torsion=trivial.
```

LMFDB gives the minimal model

```text
y^2=x^3+x^2+95x+703
```

with generator `(3,32)`.

The remaining task is therefore not classification of ten nontrivial twists. It is a certified Mordell-Weil sieve / elliptic-Chabauty (or equivalent exact descent) imposing the two square-coordinate conditions in (A1.11.4) on this known rank-one curve.

## 5. Exact computational wall after repair

The current execution path has no SageMath, Magma, PARI/GP, or `mwrank`. The exact `delta=1` model and generator are known, but a proof that determines all rational points satisfying the two extra square conditions is not certified by the current lightweight toolchain.

Returning to the old height search, the saturated A1-6 prime mechanism, or the quotient-only nontrivial `delta` branches would not advance the actual first-two-cover receiver.

The correct freeze is therefore

```text
STAGE_A1_STATUS=FROZEN_EXACT_DELTA1_MW_SIEVE_WALL
STOP_AFTER_AUDIT=true
```

not `FROZEN_EXACT_FINITE_ELLIPTIC_WALL` at ten unclassified twists.

Reopen StageA1 if one of the following becomes available:

- certified Sage/Magma/PARI/mwrank computation on the exact `delta=1` curve;
- certified MW-sieve / elliptic-Chabauty closure of the two square-coordinate conditions;
- a new exact descent or rational-point theorem for (A1.11.4);
- a proved universal reverse map or a valid adapter into another proved project receiver.

## 6. Firewalls

This result does **not** prove:

- that the `delta=1` receiver has no nondegenerate rational point;
- that the equation-(6) family has no anchored member;
- that equation (6) is universal;
- any necessary condition for arbitrary perfect cuboids;
- existence or nonexistence of a perfect cuboid.

The non-`delta=1` quotient eliminations must not be described as eliminating distinct perfect-cuboid paths.

Stage27 and StructureRadar remain unchanged.

```text
A1_11_AUDIT_VERDICT=PASS_WITH_ROUTING_REPAIR
A1_11_SAME_J_ADAPTER_FIREWALL=true
A1_11_FALSE_ADAPTERS_REJECTED=5
A1_11_FIRST_TWO_COVER_RELEVANT_DELTA=1
A1_11_Q2_NECESSARY_CONDITION=delta_congruent_1_mod_8
A1_11_Q2_EMPTY_ORIGINAL_TEN=+13,-13,+39,-57,+247,+741,-741
A1_11_Q2_SURVIVING_ORIGINAL_TEN=-39,+57,-247
A1_11_TRUE_WALL=DELTA1_RANK1_TWO_SQUARE_COORDINATE_MW_SIEVE
STAGE_A1_STATUS=FROZEN_EXACT_DELTA1_MW_SIEVE_WALL
PERFECT_CUBOID_FOUND=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
STOP_AFTER_AUDIT=true
```
