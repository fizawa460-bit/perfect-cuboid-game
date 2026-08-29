# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_FULL_E2_COCYCLE_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Fixed marked receiver

```text
T(Kc) ~= <4> direct_sum <8>
Br(Kc)[2] = Hom(T,Z/2)
[1,0] -> kernel minimum norm 8
[0,1] -> kernel minimum norm 4
[1,1] -> kernel minimum norm 12
```

The marked Brauer functional is still one of the three nonzero functionals.

## Revocation retained: constant d=2 is not the named J2 torsor

The previous promotion `partial norm squareclass 2 => named Leray/Sha d=2` is invalid. J2 is geometrically nontrivial, whereas constant `2` becomes a square over `Qbar` and its single-isogeny covering becomes geometrically trivial.

Exact rejection certificate: `j2-d2-geometric-nontriviality-rejection.json`.

## Half-divisor pushforward remains support data, not the Sha coordinate

On the branch normalization

```text
C: z^2=q, q=t^4-6*t^2+1,
E_J2=2*infinity_minus-P_plus-P_minus,
```

we have exactly

```text
pi_*(E_J2)=-div(Dplus),
Dplus=t^2-2*t-1.
```

This identifies the base support/trivialization forced by the named half-divisor, but it is not by itself the Leray/Ogg-Shafarevich edge map. Therefore `Dplus` is not promoted to a named torsor coordinate.

Certificate: `j2-geometric-halfdivisor-base-squareclass.json`.

## NEW: recover the nonconstant Hilbert-90 datum

Stage33-05 already contains the exact identity

```text
ell_z = f2 * g90^2,
f2=(t+1+sqrt(2))/(t-1+sqrt(2)).
```

Thus the geometric squareclass retained by the Hilbert-90 reduction is `f2`, not the arithmetic partial norm `2`.

Under the constant-field conjugation `sqrt(2)->-sqrt(2)`, exact multiplication gives

```text
f2 * ct(f2) = Dminus/Dplus,
Dminus=t^2+2*t-1,
q=Dplus*Dminus,
(Dminus/Dplus)*q=Dminus^2.
```

Hence

```text
[Dminus/Dplus]=[q] in Q(t)^*/Q(t)^{*2}.
```

This gives a Q-rational nonconstant norm/corestriction squareclass candidate `q`. It survives over `Qbar(t)`, unlike constant `2`.

Certificate: `j2-hilbert90-geometric-squareclass-candidate.json`; verifier: `certify_j2_hilbert90_geometric_squareclass_candidate.py`.

## NEW exact rejection: q is also not a single-isogeny J2 coordinate

For the standard single-2-isogeny homogeneous-space template

```text
C_d: N^2=d*U^4-2*H*U^2*V^2+(D/d)*V^4,
H=t^4-4*t^2+1,
D=(t^2-1)^2*q,
```

setting `d=q` gives

```text
C_q: N^2=q*U^4-2*H*U^2*V^2+(t^2-1)^2*V^4.
```

But this has the explicit K-rational point

```text
[U:V:N]=[0:1:t^2-1].
```

Therefore the `q` projection is a trivial torsor and cannot equal the named geometrically nontrivial J2 Weil-Chatelet class.

Certificate: `j2-q-single-isogeny-projection-rejection.json`; verifier: `certify_j2_q_single_isogeny_projection_rejection.py`.

## Exact consequence

The failed scalar projections now explain the obstruction cleanly:

```text
constant 2 projection -> geometrically trivial
q norm/corestriction projection -> explicitly trivial
Dplus pushforward -> support/trivialization datum only
```

So the named J2 class cannot be recovered by taking one scalar norm and calling it a 2-isogeny coordinate. Since

```text
E: Y^2=X*(X-r1)*(X-r2),
r1=(t^2-1)^2,
r2=q,
```

has full rational 2-torsion, the next exact object is the **full two-coordinate** class in

```text
H^1(Q(t),E[2]) ~= (Q(t)^*/Q(t)^{*2})^2
```

before projection to any one rational 2-isogeny.

Next exact leaf:

`COMPUTE_THE_TWO_KUMMER_SQUARECLASS_COORDINATES_OF_THE_NAMED_HILBERT90_COCYCLE_IN_H1(Q(t),E[2])_THEN_MAP_THE_PAIR_TO_THE_WEIL_CHATELET_CLASS`.

## Firewalls

```text
Stage33-12 visible progress = 4/5
J2 marked Brauer functional materialized = false
J2 twisted transcendental kernel identified = false
J2 2-isogeny squareclass selected = false
J2 torsor equation materialized = false
Stage33-12 exact closure = false
Stage33-13 released = false
heavy actions authorized = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
