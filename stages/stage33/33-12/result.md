# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_SPECIAL_BRAUER_PAIRING_ORBITS_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Class-2 decision budget

This is MAIN **batch 1 / 4** under the common-standard-form go/no-go contract committed in `j2-marked-kc-common-standard-form-route-audit.md` / `.json`.

Selected class-2 architecture:

```text
named CV J2
  -> special-Brauer / mu_2 Cech datum on the resolved four-contact model
  -> twisted relative Picard K3 X_J2
  -> T(X_J2)=ker(J2:T(Kc)->Z/2)
  -> minimum norm 4 / 8 / 12
  -> [0,1] / [1,0] / [1,1].
```

The direct-presentation bridge search is no longer the MAIN strategy. The Clifford/Hermite model is used only as the finite construction engine for the special-Brauer/PGL2 lifting datum.

## Fixed marked receiver

```text
T(Kc) ~= <4> direct_sum <8>
Br(Kc)[2] = Hom(T,Z/2)
[1,0] -> kernel minimum norm 8
[0,1] -> kernel minimum norm 4
[1,1] -> kernel minimum norm 12
```

The marked functional is still one of these three nonzero elements.

## Retained split-Clifford data

Write

```text
r=(t^2-1)^2,
q=t^4-6*t^2+1,
M_split=diag(X,X-r,X-q).
```

The normalized ruling-cover fingerprint remains exactly `[q,1,q]`. The four transverse `q=0` intersections have forced glue. The only local glue choices occur at the four even contacts

```text
t=+1,-1 on C0/Cr,
t=0,infinity on Cr/Cq.
```

The `Dplus` support lies among the forced transverse q-root nodes and therefore does not select the remaining theta glue.

## NEW in batch 1/4: local resolution and complete pairing-orbit census

Each even tangency has the local form `y=0` and `y=s^2*u(s)` with `u(0)=4` after the indicated local coordinate choice. One blowup `y=sY` converts it to two transverse branches. At all four contacts the incident normalized ruling covers are unramified (`q(±1)=-4`, `q(0)=1`, and normalized `q(infinity)=1`). Hence each resolved node has exactly two deck-equivariant sheet bijections: identity or crossed.

Therefore the raw pairing space is exactly

```text
F2^4 = {p_+1,p_-1,p_0,p_inf},
raw count = 16.
```

The full component sheet-relabeling action is also exact. In the above bit order, deck flips act by

```text
delta_C0 = 1100
delta_Cr = 1111
delta_Cq = 0011
```

with relation `delta_C0 + delta_Cr + delta_Cq = 0` on pairing bits. Thus the effective relabeling subgroup is

```text
H={0000,1100,0011,1111} ~= F2^2.
```

All 16 predecessors were enumerated before quotienting. They split into exactly four pairwise-disjoint orbits of size four, with complete invariants

```text
L = p_+1 XOR p_-1
R = p_0  XOR p_inf.
```

Representatives and complete member sets are:

```text
(L,R)=(0,0): 0000 -> {0000,0011,1100,1111}
(L,R)=(0,1): 0001 -> {0001,0010,1101,1110}
(L,R)=(1,0): 0100 -> {0100,0111,1000,1011}
(L,R)=(1,1): 0101 -> {0101,0110,1001,1010}
```

So batch 1 closes the finite local/global pairing search itself:

```text
16 raw patterns -> exactly 4 isomorphism orbits -> exactly 2 parity bits.
```

The four-orbit cardinality is **not** used to identify these parity bits with the fixed marked Brauer basis. The named CV J2 orbit is still unknown.

Certificate: `j2-four-even-contact-pairing-orbits.json`.
Verifier: `certify_j2_four_even_contact_pairing_orbits.py`.

## Batch 2 exact target

```text
RESTRICT THE NAMED CV J2 AZUMAYA/PGL2 DATA TO THE SAME FOUR RESOLVED CHARTS,
CONSTRUCT LOCAL SPLITTING MODULES AND TRANSITION MATRICES,
EXTRACT THE mu_2 CECH / SPECIAL-BRAUER PAIRING ORBIT,
AND EITHER SELECT ONE OF THE FOUR (L,R) ORBITS OR CERTIFY NON-SEPARATION.
```

A shared `[q,1,q]` component fingerprint is not sufficient for this selection.

## Firewalls

```text
class-2 budget used = 1/4
Stage33-12 visible progress = 4/5
four even-contact raw pairing count = 16
pairing isomorphism orbit count = 4
named CV J2 pairing orbit selected = false
pairing orbit bits = marked Brauer bits = false
J2 explicit torsor surface materialized = false
J2 marked Brauer functional materialized = false
J2 twisted transcendental kernel identified = false
Stage33-12 exact closure = false
Stage33-13 released = false
heavy actions authorized = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
