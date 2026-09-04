# Stage32 post-1547 H-orbit-sum stabilizer negative

Scope: fixed recovered V6 class `g1-d186`, retained `O=210`, `q'=4`, `Q=602`, after the hostile-audited #1534 single-`b3` reduction and #1536 direct ambient cusp-profile negative.

This leaf tests a weaker ambient symmetry condition that was not the object of #1532: preservation of the **sum class** of the four V4 deck translates, rather than preservation of the four-element H-orbit as a set.

## Exact retained class identity

The hostile-audited post-1500 Rosati repair source-locks, for an actual carrier and the finite-etale V4 quotient `q:X->Q=C0 x C0`,

`q^*Gamma = D + uD + vD + uvD`.

The recovered V6 witness gives the exact 140 retained intersection pairings of `D`, and the hostile-audited H-deck adapter gives

`u=g7*g9`, `v=g7*g8`, `uv=g8*g9`

inside the retained source-locked Stoll action. Intersection pairing is additive, so the coordinate-wise sum of the four transformed 140-vectors is exactly the retained numerical-Picard pairing vector of the pullback sum class `q^*Gamma` on this interface.

This is strictly weaker than asking one Stoll element to preserve the H-orbit of `D` setwise. An outside-H element could in principle fail to preserve the four individual components while still fixing their sum class; #1532 did not use that weaker condition as its tested object.

## Order-three branch condition

The hostile-audited #1536 certificate source-locks the six second-factor boundary labels

`[33,36,37,40,41,44]`

and their bijection with the six Bolza Weierstrass points. A nontrivial order-three automorphism of the Bolza curve descends to cycle type `(3,3)` on these six branch points. Therefore any retained ambient Stoll realization of that order-three branch action must preserve this six-label set and induce two 3-cycles on it.

This condition is necessary only for the **retained ambient realization** tested here. It does not assert that the Jacobian automorphism `b3` must lift to the retained ambient Stoll action.

## Exact finite result

Using the retained nine Stoll generators, the diagnostic reconstructs the full group of order `1536` and the H-deck subgroup of order `4`.

For the H-orbit-sum pairing vector:

- full stabilizer size: `4`;
- stabilizer outside H: `0`;
- stabilizer elements are exactly `1`, `g7*g8`, `g7*g9`, `g8*g9`.

For the six second-factor Weierstrass representatives:

- setwise stabilizer size inside the retained Stoll group: `768`;
- elements inducing cycle type `(3,3)`: `256`;
- elements that both induce `(3,3)` and fix the H-orbit-sum class: `0`.

Thus even after weakening #1532 from H-orbit setwise preservation to mere preservation of the numerical pullback sum class `D+uD+vD+uvD`, there is no retained ambient Stoll candidate carrying the required nontrivial order-three action on the six Weierstrass representatives.

## Decision and firewalls

Closed subroute only:

`RETAINED_AMBIENT_STOLL_B3_ORBIT_SUM_INVARIANCE_FOR_Q_PULLBACK_GAMMA`.

This does **not** prove `[T,b3]=0` or `[T,b3]!=0` for `T=(f1)_*(f2)^*`. In particular:

- it does not prove that the principal Bolza `b3` action lifts to the retained cover `X`;
- it does not rule out an intrinsic automorphism of the hypothetical carrier `Y` acting equivariantly on `f1,f2` without extending to the retained ambient Picard action;
- it does not rule out direct equality/commutation of Jacobian endomorphisms without a geometric ambient lift;
- it does not exclude `Q(T)=602` or `O=210`;
- O212+ remains blocked and the Stage32 controller is unchanged;
- no effectivity, FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit follows.

Re-entry to the actual #1534 commutator target still requires genuinely new semantic information: an intrinsic carrier automorphism with exact action on `f1,f2`, an exact divisor/correspondence-to-endomorphism commutator identity strong enough to decide `[T,b3]`, or an independent valence/scalarity argument.
