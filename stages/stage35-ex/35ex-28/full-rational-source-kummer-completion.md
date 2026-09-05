# Stage35-EX 35EX-28 — full rational-source Kummer completion

Status: `PROVISIONAL_EXACT_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_NO_CREDIT`

This unit starts only after the mandatory post-35EX-27 fresh breadth audit. 35EX-27 remains valid: it absorbed the rational source-lift discriminant `u^2-4=square` into the K3 square. The remaining issue is that the quotient-base condition `h^2=u(u+2)` was still carried outside K1--K3. Before any receiver-restricted local/global exclusion is attempted, that final rational-source gate must be internalized as well.

No E1, Stage35, or perfect-cuboid closure is claimed.

## 1. Audited input from 35EX-27

On the positive nondegenerate chamber retain rational coordinates

```text
A = alpha^2,
A != 0, +/-1,
```

and

```text
u = 2*A*(beta^2-1)/(beta*(A^2-1)),                  (K1)
b^2 = (A*beta+1)/(A+beta),                          (K2)
kappa^2 = (beta-A)*(A*beta-1).                      (K3)
```

The original quotient base still requires

```text
h^2 = u*(u+2).                                      (QB)
```

35EX-27 proved that K3 is exactly the other rational-source condition `u^2-4=square` after removing a certified square prefactor.

## 2. Factor the quotient-base square in the same coordinates

From K1,

```text
u+2
 = 2*(A+beta)*(A*beta-1)/(beta*(A^2-1)).
```

Hence

```text
u*(u+2)
 = 4*A*(beta^2-1)*(A+beta)*(A*beta-1)
   / (beta^2*(A^2-1)^2).                            (H1)
```

Because `A=alpha^2`, the factor `4*A` is already a rational square. K2 gives

```text
A+beta = (A*beta+1)/b^2.
```

Substituting this into H1 gives

```text
u*(u+2)
 = [ 2*alpha/(b*beta*(A^2-1)) ]^2
   * (beta^2-1)*(A^2*beta^2-1).                     (H2)
```

All displayed denominators are nonzero on the retained chamber.

## 3. K4: exact quotient-base Kummer square

Define

```text
lambda = h*b*beta*(A^2-1)/(2*alpha).
```

Then `(QB)` and `(H2)` imply

```text
lambda^2 = (beta^2-1)*(A^2*beta^2-1).               (K4)
```

Conversely, if K1, K2 and K4 hold with `A=alpha^2`, define

```text
h = 2*alpha*lambda/(b*beta*(A^2-1)).
```

Then H2 gives exactly

```text
h^2=u*(u+2).
```

Therefore, on the retained open,

```text
quotient-base square h^2=u(u+2)
<=> K4.
```

This is an exact iff, not a one-way necessary condition.

## 4. Full rational-source Kummer receiver

Combining 35EX-27 with K4, the rational-source receiver may now be represented by the joint system

```text
A=alpha^2,
K1: u = 2*A*(beta^2-1)/(beta*(A^2-1)),
K2: b^2 = (A*beta+1)/(A+beta),
K3: kappa^2 = (beta-A)*(A*beta-1),
K4: lambda^2 = (beta^2-1)*(A^2*beta^2-1),
```

plus the retained positivity/nondegeneracy open.

The converse is exact by composition of audited 35EX-27 with the K4 iff above:

```text
K1+K2+K3+K4
 -> reconstruct h from K4
 -> K1+K2+K3+quotient-base h-square
 -> audited 35EX-27 rational source + descended receiver
 -> audited 35EX-26 / 35EX-25 full four-square receiver.
```

Thus S34-W03-style receiver intersection tests must use K1--K4 jointly. Testing only K1--K3 still tests a larger over-cover.

## 5. Positive-chamber order

For a positive rational source, `x=1` is impossible because it would require `p^2=2` with `p in Q`. Hence `u>2` and the source-lift square is nonzero.

The 35EX-27 coordinates then satisfy

```text
alpha>1,
A>1,
beta>A.
```

Indeed `alpha-alpha^{-1}=2*h*r/u>0`, while K3 has `A*beta-1>0` and a nonzero square on the rational-source chamber.

Using K2,

```text
b^2-1 = (A-1)*(beta-1)/(A+beta) > 0,
A-b^2 = (A^2-1)/(A+beta) > 0,
```

and

```text
b^2 - (A^2+1)/(2*A)
 = (A^2-1)*(beta-A)/(2*A*(A+beta)) > 0.
```

Therefore every retained positive rational-source point obeys the exact strict order

```text
1 < (A^2+1)/(2*A) < b^2 < A < beta.                (ORD)
```

This is a receiver-domain restriction only; it is not an emptiness proof.

## 6. K4 produces a second moving fixed-A genus-one channel

For fixed `A`, K4 is the quartic

```text
H_A: lambda^2
   = (beta^2-1)*(A^2*beta^2-1)
   = A^2*beta^4-(A^2+1)*beta^2+1.
```

Using binary-quartic coefficients

```text
a=A^2,
c=-(A^2+1),
e=1,
```

one gets

```text
I_H = A^4+14*A^2+1,
J_H = 2*(A^2+1)*(A^4-34*A^2+1),
4*I_H^3-J_H^2 = 432*A^2*(A-1)^4*(A+1)^4.
```

So `H_A` is generically smooth on the retained open `A!=0,+/-1`. The absolute invariant ratio `J_H^2/I_H^3` is nonconstant in `A`, so this is another moving genus-one family, not one fixed elliptic curve.

35EX-27 already supplied the first moving fixed-A genus-one channel `G_A` from K2+K3. 35EX-28 therefore exposes a paired moving-genus-one structure, but does **not** prove an isogeny, a complete correspondence of rational points, or any uniform Mordell-Weil statement between the two channels.

## 7. Arsenal routing and firewalls

`S34-W03` is now routed to the exact joint rational-source system K1--K4. Its credit remains receiver-intersection exclusion only: it does not classify the larger factor cover or close the parent route automatically.

`S31-W01` can be used fiberwise if an explicit quartic-to-elliptic adapter is later needed for `G_A` or `H_A`, with its denominator/exceptional-locus obligations. It supplies no uniform moving-family closure.

`S34-W02` remains locked because no full Mordell-Weil group is certified uniformly over `A`.

The preserved next arithmetic candidate is the exact joint-local classification of K1--K4. No local obstruction is asserted in this unit.

## 8. Result

```text
QUOTIENT_BASE_SQUARE_INTERNALIZED=true
K4_EXACT=true
K4_IFF_QUOTIENT_BASE_SQUARE=true
FULL_RATIONAL_SOURCE_KUMMER_SYSTEM_K1_K4=true
POSITIVE_CHAMBER_ORDER_EXACT=true
SECOND_FIXED_A_GENUS_ONE_QUARTIC_EXACT=true
SECOND_FIXED_A_GENUS_ONE_GENERIC_SMOOTH=true
SECOND_FIXED_A_GENUS_ONE_NONISOTRIVIAL=true
PAIRED_GENUS_ONE_ISOGENY_PROVED=false
JOINT_LOCAL_OBSTRUCTION_PROVED=false
RECEIVER_INTERSECTION_CLOSED=false
UNIFORM_FULL_MW_PROVED=false
E1_PROVED=false
STAGE35_CLOSED=false
```

Because K4 completes the rational-source receiver and exposes a materially sharper paired genus-one structure, a fresh breadth audit is required after hostile PASS before selecting another successor.
