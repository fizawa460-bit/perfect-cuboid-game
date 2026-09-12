# Stage32 MB104 — balanced16 zero-quartic Pic^0 wall

Status: **RETAINED EXACT NEGATIVE ROUTE / ZERO-QUARTIC PIC^0 CLASS IS TRIVIAL / BALANCED16 OPEN / MB104 INCOMPLETE / NO CREDIT**

## Scope

This leaf continues from the hostile-audited MB104 boundary and the retained finite quotient

```text
uniform genus-one P5 ray
D_l = 7l H - 4l sum_{i in Sigma} E_i,
|Sigma|=14,
l>=1,
```

whose only remaining support configurations are four balanced incidence-16 `Aut(S)` orbits of sizes

```text
48, 48, 768, 768.
```

For every surviving support, each zero-pairing elliptic quartic contains exactly seven supported box nodes. The previous static-landing wall showed that finitely many fixed exceptional landing points can be avoided locally. The present leaf asks whether the degree-zero restriction of `D_l` to a zero-pairing elliptic quartic nevertheless gives a hidden global `Pic^0` obstruction.

It does not.

## Representative elliptic quartic

Use the retained representative in the hyperplane `b1=0`:

```text
a2 = i a3,
c  = a1.
```

Write

```text
x=a1,
y=a3,
z=b2,
w=b3.
```

The quartic is the smooth complete intersection

```text
Q:
  z^2 = x^2+y^2,
  w^2 = x^2-y^2
```

in `P^3`. It has degree four and genus one.

Its eight box nodes are exactly

```text
y=0: [1:0:+-1:+-1]  (four points),
x=0: [0:1:+-1:+-i]  (four points).
```

Hence the full eight-node divisor `B_Q` is the union of the two hyperplane sections `x=0` and `y=0`. Since each hyperplane section has degree four and already contains four distinct points,

```text
B_Q ~ 2 H_Q,
```

where `H_Q=H|_Q`.

## Every box node on Q is a hyperflex

It is enough to check one point after the exact `Aut(S)` replay below. Take

```text
P=[0:1:1:-i].
```

The plane

```text
L_P: -2y + z + i w = 0
```

meets `Q` only at `P`, with scheme length four.

Indeed put `W=i w` and work in the affine chart `y=1`. Then

```text
z^2 = x^2+1,
W^2 = 1-x^2,
z+W = 2.
```

Eliminating `W=2-z` and `x^2=z^2-1` gives

```text
(2-z)^2 - (1-x^2)
= (2-z)^2 - (2-z^2)
= 2(z-1)^2.
```

Set `u=z-1`. The local equations become

```text
u^2=0,
x^2=2u+u^2=2u,
```

hence `x^4=0`. The local plane-section algebra therefore has length four. Since a plane section of the degree-four nondegenerate curve `Q` has total degree four,

```text
L_P . Q = 4P,
H_Q ~ 4P.
```

The exact node-action verifier shows that the 12 retained elliptic quartics form one `Aut(S)` orbit and, more strongly, that the 96 incident pairs

```text
(Q,P),  P a box node on Q,
```

form a single orbit. The generators are projective linear coordinate substitutions, so they preserve the hyperplane class. Therefore for **every** retained elliptic quartic and **every** box node `P` on it,

```text
H_Q ~ 4P.
```

Likewise the relation `B_Q~2H_Q` transports to every quartic.

## Restriction of the balanced uniform ray

Let `Q` be any zero-pairing quartic for one of the four balanced support orbits. By retained finite replay,

```text
#(Sigma cap Q)=7.
```

Since `Q` contains eight box nodes, there is a unique omitted box node `P` and

```text
Sigma cap Q = B_Q - P.
```

The audited capacity interface uses

```text
E_i.Q = 1
```

for a box node on `Q`, so the restriction of the primitive ray class

```text
A = 7H - 4 sum_{i in Sigma} E_i
```

to `Q` is

```text
A|_Q
 ~ 7H_Q - 4(B_Q-P)
 ~ 7H_Q - 8H_Q + 4P
 ~ 4P-H_Q
 ~ 0.
```

Therefore

```text
O_Q(A) ~= O_Q,
O_Q(D_l) ~= O_Q
```

for every `l>=1` and every zero-pairing quartic in all four balanced support orbits.

## Consequence

This closes one tempting continuation **negatively**:

```text
"D_l.Q=0 but O_Q(D_l) is a nontrivial degree-zero line bundle,
so every global section must vanish on Q"
```

is false. The degree-zero class is exactly trivial.

Thus the zero-pairing quartics do not supply a hidden `Pic^0` obstruction beyond the already-retained static landing-value condition. If an effective divisor in `|D_l|` does not contain `Q`, its restriction to `Q` is a nonzero constant and the divisor is disjoint from `Q` on the resolution; locally this is compatible with choosing exceptional landing points away from the one or two quartic landing points.

This does **not** prove that the restriction map

```text
H^0(S,O(D_l)) -> H^0(Q,O_Q)
```

is nonzero, and therefore does not prove that `Q` is absent from the fixed locus of the entire linear system. It also does not construct an irreducible genus-one carrier or close the balanced16 hard core.

The remaining useful questions are genuinely global:

1. determine whether the restriction map above is zero or surjective for the four support orbits;
2. test simultaneous algebraic gluing of the required multibranch jets across all fourteen supported exceptional curves;
3. seek a stronger nef/effective-cone or linear-system obstruction;
4. keep arbitrary unequal exceptional coefficients outside the scope of this uniform-ray leaf.

## Verification

`verify_mb104_balanced16_zero_quartic_pic0.py` source-locks the retained uniform-ray, automorphism, section-geometry, capacity, and four-orbit quotient inputs before replay. It checks:

- the exact 48-node model;
- the order-1536 node action;
- exactly 12 elliptic quartics with eight box nodes each;
- transitivity on all `12*8=96` incident `(Q,P)` pairs;
- the representative eight-node split into `x=0` and `y=0` hyperplane sections;
- the representative hyperflex point/plane data and elimination identity;
- the four balanced support profiles with seven nodes on each zero-pairing quartic.

No MB-specific exact-head CI is required by the active mission contract.

## Firewalls

- `balanced16_closed=false`.
- `whole_span5_closed=false`.
- `arbitrary_unequal_picard_classes_closed=false`.
- `restriction_map_nonzero_proved=false`.
- `irreducible_curve_proved=false`.
- `normalization_genus_one_realized=false`.
- no finite population-wide degree window;
- no receiver/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
