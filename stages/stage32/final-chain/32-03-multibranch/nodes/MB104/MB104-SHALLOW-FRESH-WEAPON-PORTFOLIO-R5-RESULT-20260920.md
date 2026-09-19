# MB104 — shallow fresh-weapon portfolio R5 — 2026-09-20

Status: **PRE-AUDIT SHALLOW PORTFOLIO / ALL THREE ROUTES FAIL SHALLOW / NO CREDIT**

## Scope

This round is disjoint from the parked log-tangent route, the six-map/fibration classification
work, and the size48 local analytic chain.

Targets on the surviving 000707 balanced hard core:

A. higher adjoint / multiplier-ideal / conductor filtrations;
B. stable-map cosection localization from p_g(S)=7;
C. gonality-two extension from the elliptic normalization.

## A. Higher adjoint / multiplier-ideal filtration

Z48 already identifies the intrinsic conductor/adjoint object and its first adjunction behavior.
For an integral Cartier divisor C on a smooth surface, multiplier ideals have the integer-shift
identity

```text
J((c+1)C) = O_S(-C) * J(cC).
```

On a log resolution, the additional integral total transform of C factors out by projection
formula.  Thus whole-integer coefficient shifts do not create a new growing local filtration.

Literal powers of the conductor ideal are genuinely different objects, but they are not
automatically multiplier ideals of mC.  No source-valid Nadel/adjunction theorem located in this
shallow pass converts their colengths into a uniform contradiction on |lP|.

Disposition:

```text
A = NO NEW l-GROWING ADJOINT FILTRATION AT SHALLOW DEPTH.
```

## B. p_g=7 holomorphic-two-form / stable-map cosection

The resolved cuboid surface has

```text
p_g(S)=7.
```

Kiem--Li localize the virtual stable-map class using a holomorphic two-form.  This is relevant to
the hypothetical normalization map

```text
nu:E -> S,
g(E)=1,
[nu(E)]=lP.
```

But the theorem localizes or kills the **virtual class**, not the underlying point of the stable-map
moduli space.

The expected dimension is already

```text
vdim
=
(1-g)(dim S-3)+c1(T_S).(lP)
=
-K_S.(lP)
=
-112l.
```

So a hypothetical map is massively obstructed.  A surjective cosection can make its local virtual
contribution vanish while the actual isolated map still exists.

Disposition:

```text
B = VIRTUAL LOCALIZATION ONLY;
    NO POINT-SET NONEXISTENCE.
```

## C. Gonality-two extension after resolving the carrier

The normalization E is elliptic and therefore has a degree-two morphism to P1.

Serrano-type extension theorems can extend a degree-d pencil from a smooth curve X on a smooth
surface when X has sufficiently large positive self-intersection.  A standard sufficient condition
is

```text
X^2 > (d+1)^2.
```

For d=2 this asks for X^2>9.

Resolve all singularities of C and let E be the smooth strict transform.  If m_q are the
multiplicities at all proper and infinitely-near resolution centers, the plane-curve delta formula
gives

```text
delta(C) = sum_q m_q(m_q-1)/2.
```

Hence

```text
sum_q m_q^2
=
2 delta(C)+sum_q m_q.
```

Using

```text
C^2=336l^2,
2 delta(C)=336l^2+112l,
```

we get

```text
E^2
=
C^2-sum_q m_q^2
=
-112l-sum_q m_q
<
0.
```

This is the opposite regime from Serrano/Paoletti.

Nor can the normalization g1_2 be treated as a degree-two pencil on the singular curve itself.
For a degree-two line bundle A on E, the torsion-free rank-one sheaf nu_*A on C has degree

```text
deg_C(nu_*A)
=
chi(A)-chi(O_C)
=
2+delta(C)
=
168l^2+56l+2.
```

So the low-degree pencil becomes a quadratic-degree object on C.

Disposition:

```text
C = GONALITY EXTENSION FAILS NUMERICALLY.
```

## R5 verdict

All three routes fail at shallow depth:

```text
A adjoint powers:
  integer multiplier levels are periodic twists; conductor powers lack a vanishing bridge.

B p_g=7 cosection:
  virtual localization does not delete obstructed stable-map points.

C gonality extension:
  the embedded normalization has negative self-intersection;
  the degree-two pencil pushes to degree delta+2 on the singular carrier.
```

No R5 route earns depth.

## Stronger clue exposed by R5

The gonality calculation exposes an exact cancellation:

```text
C^2 = 336l^2,
deg Delta = 2delta = 336l^2+112l.
```

For the equigeneric conductor-normal sheaf

```text
N'_C = conductor_C * O_C(C),
```

its pullback to E has degree

```text
C^2-deg Delta = -112l.
```

The surviving difficulty is therefore intrinsically linear, not quadratic.

This suggests a materially different next theorem species:

```text
equigeneric semiregularity / conductor-normal obstruction
```

Ask whether the O(l) obstruction group can be forced through a fixed-dimensional surface
semiregularity/cohomology receiver, or whether the known P-null contraction supplies the necessary
O(l) kernel.

## External source boundary

- Kiem--Li, *Gromov-Witten invariants of varieties with holomorphic 2-forms*,
  arXiv:0707.2986.
- Serrano's pencil-extension theorem, as quoted in Paoletti,
  *Free pencils on divisors*, arXiv:alg-geom/9303005.
- Multiplier-ideal integer-shift periodicity follows directly from the log-resolution definition
  for an integral Cartier divisor.

## Firewalls

```text
adjoint_power_finite_l=false
cosection_point_nonexistence=false
gonality_extension_applicable=false
R5_deep_winner=false
finite_degree_window_proved=false
dangerous_000707_excluded=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
