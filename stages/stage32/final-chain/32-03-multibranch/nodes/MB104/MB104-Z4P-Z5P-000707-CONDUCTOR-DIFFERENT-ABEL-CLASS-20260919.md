# MB104 Z4'+Z5' — 000707 conductor/different Abel-class identity — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT ADJUNCTION/ABEL REDUCTION / NO CREDIT**

## Scope

Assume a dangerous normalization-genus-one carrier on

```text
Sigma=000707000f0f,
C in |lP|,
P=7H-4 sum_(i in Sigma)E_i.
```

Let

```text
nu:E->C
```

be the normalization, with g(E)=1.

This note combines:

- the Z33 equality/simple-contact package;
- the exact support-hyperplane divisor;
- the Z5' e=4 two-fiber factorization;
- adjunction for an integral Cartier curve on the smooth cuboid resolution.

## 1. Supported exceptional divisor equals the support-hyperplane divisor on E

Z33 gives

```text
div_E(nu^*h)=B_node
```

where B_node is the reduced divisor of all 112l supported normalization branches.

Every branch has exceptional contact multiplicity one, so also

```text
nu^*(sum_(i in Sigma) E_i)=B_node.
```

Since H is the support-hyperplane class,

```text
nu^*H ~= O_E(B_node).
```

Therefore

```text
nu^*P
 ~= 7 nu^*H -4 B_node
 ~= 3 nu^*H.                                  (P-RESTRICT)
```

This identity uses the exact equality packet and is stronger than a degree computation.

## 2. Normal bundle of the carrier

Because C=lP,

```text
O_E(C)
 = nu^*O_S(lP)
 ~= (nu^*O_S(H))^(3l).                        (NORMAL)
```

Its degree is

```text
3l * deg(H|E)
 =3l*(112l)
 =336l^2
 =C^2,
```

as required.

## 3. Conductor/different divisor by adjunction

Because C is Cartier on the smooth surface S, it is Gorenstein and

```text
omega_C ~= O_C(K_S+C).
```

Let Delta be the normalization conductor/different divisor characterized by

```text
nu^*omega_C ~= omega_E(Delta).
```

Since E is elliptic,

```text
omega_E ~= O_E.
```

Also K_S=H.  Using (NORMAL),

```text
O_E(Delta)
 ~= nu^*O_C(K_S+C)
 ~= nu^*O_S(H) tensor nu^*O_S(lP)
 ~= (nu^*O_S(H))^(3l+1).                     (DIFF)
```

Equivalently,

```text
O_E(Delta) ~= O_E((3l+1) B_node).             (ABEL)
```

The degree checksum is

```text
deg Delta
 =(3l+1)*112l
 =336l^2+112l
 =2 delta(C),
```

with

```text
delta(C)=168l^2+56l.
```

## 4. e=4 half-hyperplane specialization

In the e=4 packet, the exact Z5' grid gives two effective divisors

```text
B_z=phi_1^{-1}(i),
B_w=phi_2^{-1}(1),
```

each of degree 56l, with

```text
B_node=B_z+B_w,
B_z ~ B_w.
```

Write their common line bundle as M.  Then

```text
O_E(B_node) ~= M^2.
```

Hence (DIFF) becomes

```text
O_E(Delta) ~= M^(6l+2)
             = (M^(3l+1))^2.                 (EVEN-DIFF)
```

So the conductor/different line bundle is canonically 2-divisible at the level of its retained
factor line M.

This is a line-bundle statement; no claim is made that the effective different divisor itself is
twice an effective divisor.

## 5. Abel-Jacobi form

Choosing an origin on E, (ABEL) is the exact group-law constraint

```text
AJ(Delta) = (3l+1) AJ(B_node)
```

in Pic(E), with equality understood in the degree-(336l^2+112l) component.

Thus the entire unknown quadratic singularity mass of the strict-transform carrier has a fixed
Abel class determined by the explicit 112l support divisor.

This is a genuine global localization statement unavailable to branch-count-only Z4'.

## 6. Why this does not yet close the carrier

The support of Delta records singularities of the strict-transform curve C on the **smooth**
resolution S.  It is not the same object as the 14 canonical-surface A1 node identifications:
those branches are separated on S by the exceptional curves.

Therefore (ABEL) does not imply that Delta is supported on B_node and does not convert the
quadratic delta mass into ordinary singularities at the fourteen box nodes.

On an elliptic curve, effective divisors of the required large degree can realize the fixed Abel
class.  An exclusion requires extra information about the allowed local conductor coefficients,
support, or a surface-side singularity scheme.

## 7. Route consequence

Z4' is sharpened from

```text
unknown singularity divisor of degree 2 delta
```

to

```text
unknown effective different Delta
with
O_E(Delta)=O_E((3l+1)B_node).
```

Useful future inputs would be:

- a theorem forcing Delta into a controlled subset of E;
- a packet-specific restriction on conductor multiplicities;
- a Cayley--Bacharach / vanishing theorem for the corresponding singularity scheme;
- an independent computation of AJ(Delta) incompatible with (ABEL).

Without one of these, the identity is a structural reduction, not closure.

## Firewalls

```text
conductor_different_Abel_class_exact=true
different_support_localized_to_B_node=false
e4_different_line_bundle_even=true
e4_excluded=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
