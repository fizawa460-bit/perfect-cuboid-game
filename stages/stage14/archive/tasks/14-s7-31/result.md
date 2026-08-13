# Stage14-s7-31 — fixed-outer common-gcd square divisibility and the 5/8 bound

## Status

`COMPLETE_FIXED_OUTER_COMMON_GCD_SQUARE_DIVISIBILITY_AND_5_8_BOUND`

Stage14-s7-31 consumes merged `s7-30` (PR #517) on the same charged-once common-core packet.  The merged theorem is

```text
V(B) << B^(11/16+o(1)),
```

and its unique `11/16` saturation is

```text
theta=5/16,
phi=1/4.
```

The only `1/16` loss left there comes from the `sqrt(M)` term in the nonprimitive second-root-pair lemma.  That term arose by summing the common gcd

```text
h=gcd(c_k^+,c_k^-)
```

over all integers up to `sqrt(M)`.

The physical packet is much more rigid.  The odd part of this common quotient gcd divides the common physical `z` scale, and merged `4ci` proves that the square of that scale divides the already-fixed outer residual norm `q_k=C*u_res`.  Hence

```text
oddpart(h)^2 | C*u_res.
```

For fixed `(C,u_res)`, there are only divisor-many possible odd parts of `h`; the 2-primary part has only logarithmically many possibilities.  Re-running the second root-line count with this fixed-outer restriction removes the entire `sqrt(M)` term:

```text
#(c_k^+,c_k^-)
 << B^o(1) * (1+M/C).
```

The resulting whole-strip ledger is

```text
E(theta,phi)
 <= max(2*theta,1-2*theta)
 <= 5/8.
```

Therefore

```text
boxed:
V(B) << B^(5/8+o(1)).
```

No external incidence theorem, determinant method, large sieve, genus-one theorem, or H/tH theorem is used.

---

## 1. Imported s7-30 quantifier order

Keep the merged balanced strip

```text
alpha,delta = B^(theta+o(1)),
beta,gamma  = B^(1/2-theta+o(1)),
3/16 <= theta <= 5/16,

R,J = B^(phi+o(1)),
S,T = B^(3/8-phi+o(1)),
1/8 <= phi <= 1/4,

0 <= theta-phi <= 1/8,
theta+phi >= 3/8.
```

Write

```text
q_k  = C*u_res,
q_xi = C*v_res,
```

and use the signed quotients

```text
a=c_x^+,
b=c_x^-,
c=c_k^+,
d=c_k^-.
```

The primitive xi-agreement pair is

```text
U=L_x^+,
V=L_x^-,
gcd(U,V)=1,
UV=oddpart(RJ).
```

After fixing `(C,u_res)` and a divisor-many first quotient pair `(a,b)`, merged s7-29/s7-30 counts `(U,V)` on one of divisor-many Gaussian root lines modulo essentially all of `C`:

```text
#(U,V) <= B^(2phi-chi+o(1)),
```

where the common-core exponent is scale-pinned by s7-30:

```text
C=B^(chi+o(1)),
chi=2theta+2phi-3/4.                              (1.1)
```

The first reciprocal equation then reconstructs the opposite agreement product

```text
p*q=L_k^+L_k^-
=((aU)^2-(bV)^2)/(4*r*s*epsilon_k),
```

and an ordered coprime split `(p,q)` is divisor-many.

The second signed quotient pair remains moving and satisfies

```text
Q+P=c*p,
Q-P=d*q,                                           (1.2)
```

with

```text
P=R*X,
Q=J*Y,
X=x_1*x_2,
Y=y_1*y_2.                                         (1.3)
```

The same common core gives

```text
C | p^2*c^2+q^2*d^2,
gcd(C,p*q)=1.                                      (1.4)
```

Finally

```text
c*d <= B^(nu+o(1)),
nu <= 1/4+2phi-2theta.                              (1.5)
```

Stage14-s7-30 counted (1.4)-(1.5) by the general bound

```text
B^o(1)*(M^(1/2)+M/C).
```

Stage14-s7-31 removes the first term using physical root structure already present in the same packet.

---

## 2. Physical root coordinates and the common z scale

For the two reduced physical states, merged s7-20/s7-21 use

```text
P_1=(R*S)*x_1^2,
Q_1=(T*J)*y_1^2,

P_2=(R*T)*x_2^2,
Q_2=(S*J)*y_2^2,                                  (2.1)
```

where the four xi cells `R,S,T,J` are pairwise coprime and squarefree.

Reducedness gives

```text
gcd(P_i,Q_i)=1,
```

hence

```text
gcd(x_1,y_1)=gcd(x_2,y_2)=1.                     (2.2)
```

The k-side physical roots are

```text
z_i=2*x_i*y_i/g_i,
g_i in {1,2}.                                      (2.3)
```

Put

```text
t=gcd(z_1,z_2).                                    (2.4)
```

Merged 4ci proves exactly

```text
boxed:
t^2 | q_k=C*u_res.                                 (2.5)
```

This is an outer-data statement: `(C,u_res)` is fixed before the second quotient pair `(c,d)` is counted.

---

## 3. Odd common quotient gcd divides the common z scale

Let

```text
h=gcd(c,d).                                         (3.1)
```

We prove

```text
boxed:
oddpart(h) | t.                                     (3.2)
```

It is enough to compare odd prime valuations.

Fix an odd prime `ell|h`.  From (1.2),

```text
ell | Q+P,
ell | Q-P,
```

provided `ell` is a unit on `p*q`.  This unit condition is physical: `p*q` divides the k label, while merged 4ci gives

```text
gcd(k,xi*z_1*z_2)=1.
```

An odd prime of `p*q` therefore divides none of `x_i,y_i`; it also divides neither xi cell `R,J`.  Hence

```text
gcd(p*q,P*Q)=1.                                    (3.3)
```

Thus for every odd `ell`, division by `p,q` does not alter the common valuation, and

```text
v_ell(h)
 = min(v_ell(Q+P),v_ell(Q-P))
 = min(v_ell(P),v_ell(Q)).                         (3.4)
```

Now use

```text
P=R*x_1*x_2,
Q=J*y_1*y_2.                                       (3.5)
```

An odd prime contributing to the minimum in (3.4) cannot divide `R`.  Indeed, if `ell|R` and `ell|Q`, then `ell` does not divide `J`, so `ell|y_1` or `ell|y_2`.  In the first case `ell` divides both `P_1` and `Q_1`; in the second it divides both `P_2` and `Q_2`, contradicting reducedness.  The same argument with the roles interchanged shows

```text
ell not|J.                                         (3.6)
```

Therefore the common odd valuation in (3.4) is carried entirely by the root products:

```text
v_ell(h)
 <= min(v_ell(x_1*x_2),v_ell(y_1*y_2)).            (3.7)
```

By (2.2), an odd prime cannot occur in `x_i` and `y_i` for the same state.  Hence any odd prime present on both sides of (3.7) must occur crosswise:

```text
x_1 with y_2,
or
x_2 with y_1.                                      (3.8)
```

Using (2.3), the same crosswise valuation occurs in both `z_1` and `z_2`.  Therefore

```text
v_ell(h) <= min(v_ell(z_1),v_ell(z_2))=v_ell(t).
```

This proves (3.2).

The reverse divisibility is neither needed nor claimed: the common z scale may contain primes that lie in the same root type across the two states and therefore do not enter `h`.

---

## 4. Fixed-outer square-divisor lock for h

Combine (3.2) with merged 4ci (2.5).  Since `C*u_res` is an integer,

```text
boxed:
oddpart(h)^2 | C*u_res.                            (4.1)
```

Consequently, once `(C,u_res)` is fixed,

```text
# { oddpart(h) }
 <= tau(C*u_res)=B^o(1).                           (4.2)
```

The 2-adic valuation of `h` is at most `O(log B)`, so it contributes only

```text
O(log B)=B^o(1)
```

possibilities.  Hence

```text
boxed:
fixed (C,u_res)
=> # { h=gcd(c,d) } <= B^o(1).                     (4.3)
```

This is the missing quantifier correction in the s7-30 square-root term.  The gcd is not a free integer up to `sqrt(M)`; it is a square-divisor root of data already fixed before `(c,d)` is counted.

---

## 5. Fixed-outer nonprimitive quadratic root-pair lemma

We sharpen the s7-30 lemma in the exact form needed here.

Let `Q` be odd, let `A,B` be units modulo `Q`, and fix an outer integer `W`.  Count positive pairs `(x,y)` satisfying

```text
x*y <= M,
A^2*x^2+B^2*y^2 == 0 (mod Q),
oddpart(gcd(x,y))^2 | W.                           (5.1)
```

Then

```text
boxed:
N_{Q,W}(M;A,B)
 << B^o(1)*(1+M/Q),                                (5.2)
```

when all parameters are polynomially bounded in `B`.

### Proof

Write

```text
h=gcd(x,y),
x=h*x_0,
y=h*y_0,
gcd(x_0,y_0)=1.
```

By the fixed-outer square-divisor condition, the odd part of `h` has only divisor-many possibilities; its 2-primary part has only `O(log B)` possibilities.  Thus the total number of admissible `h` is `B^o(1)`.

For fixed `h`, put

```text
Q_h=Q/gcd(Q,h^2).
```

Then `(x_0,y_0)` lies on one of divisor-many primitive quadratic root lines modulo `Q_h`.  The merged s7-29 primitive determinant-spacing lemma, summed over dyadic product boxes, gives

```text
#(x_0,y_0)
 << B^o(1)*(1+M/(h^2*Q_h)).                        (5.3)
```

But

```text
M/(h^2*Q_h)
 = M*gcd(Q,h^2)/(Q*h^2)
 <= M/Q.                                           (5.4)
```

Summing over the `B^o(1)` possible `h` proves (5.2).

The `M^(1/2)` term in the general s7-30 lemma came solely from summing the `1` in (5.3) over all `h<=sqrt(M)`.  The fixed-outer square-divisor lock removes exactly that source and nothing else.

```text
FIXED_OUTER_NONPRIMITIVE_ROOT_PAIR_LEMMA_PROVED=true.
```

---

## 6. Apply the sharpened lemma to the opposite signed quotients

Apply Section 5 with

```text
Q=C,
A=p,
B=q,
W=C*u_res,
x=c,
y=d,
M=B^(nu+o(1)).                                     (6.1)
```

The hypotheses are supplied by (1.4), (4.1), and `gcd(C,pq)=1`.  Therefore

```text
boxed:
# {(c,d)}
 <= B^(max(0,nu-chi)+o(1)).                        (6.2)
```

This replaces the s7-30 exponent

```text
max(nu/2,nu-chi)
```

by

```text
max(0,nu-chi).                                     (6.3)
```

At the old `11/16` corner

```text
theta=5/16,
phi=1/4,
chi=3/8,
nu<=1/8,
```

so

```text
nu-chi<=-1/4
```

and the entire second quotient pair has only

```text
B^o(1)
```

possibilities after the earlier outer choices.

Thus the former `B^(1/16)` saturation loss disappears completely.

---

## 7. New whole-strip exponent ledger

Dyadically write

```text
C=B^(chi+o(1)),
u_res=B^(mu+o(1)),
c*d<=B^(nu+o(1)),
```

with

```text
chi=2theta+2phi-3/4,
mu<=2theta-2phi,
nu<=1/4+2phi-2theta.                               (7.1)
```

The charged-once count is now

```text
C support:                         B^chi
u_res support:                     B^mu
first primitive pair (U,V):        B^(2phi-chi)
opposite signed quotient pair:     B^max(0,nu-chi)
remaining reconstruction:          B^o(1).          (7.2)
```

Therefore

```text
E(theta,phi)
 <= chi+mu+(2phi-chi)+max(0,nu-chi).               (7.3)
```

Using the maximal allowed `mu,nu`,

```text
nu-chi
 <= (1/4+2phi-2theta)
    -(2theta+2phi-3/4)
 = 1-4theta.                                       (7.4)
```

Hence

```text
boxed:
E(theta,phi)
 <= 2theta+max(0,1-4theta)
 = max(2theta,1-2theta).                            (7.5)
```

For

```text
3/16 <= theta <= 5/16,
```

both branches are at most `5/8`:

```text
2theta <= 5/8,
1-2theta <= 5/8.                                   (7.6)
```

Thus uniformly on the full merged common-core strip,

```text
boxed:
E(theta,phi)<=5/8.                                 (7.7)
```

---

## 8. Whole-family promotion

Merged s7-30 already promotes the same two-sided common-core packet to the whole-family theorem chain and proves `11/16`.  Stage14-s7-31 changes only one internal count in that same charged-once quantifier order:

```text
general common-gcd sum
 -> physical fixed-outer square-divisor gcd sum.
```

No new relaxed family is introduced and no old support is multiplied twice.  Therefore the strengthened block ledger promotes directly:

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8
IMPROVEMENT_OVER_11_16=1/16
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.          (8.1)
```

Equivalently,

```text
V(B) << B^(5/8+o(1)).                               (8.2)
```

The current gap to the square-root scale is

```text
5/8-1/2=1/8.                                       (8.3)
```

Merged 4cq and X7 are compatible with this promotion.  Their local `3/4` certificates predate the stronger s7-30 count and do not downgrade it; neither supplies an independent modulus that is charged here.

---

## 9. Exact 5/8 saturation geometry

Equation (7.5) has two different saturation mechanisms.

### 9.1 Upper-theta edge

The branch

```text
2theta
```

reaches `5/8` exactly when

```text
theta=5/16.                                        (9.1)
```

The strip conditions then allow

```text
3/16 <= phi <= 1/4.                                (9.2)
```

On this edge the sharpened second quotient count is already `B^o(1)`; the remaining `5/8` comes from the outer common-core/`u_res`/first primitive-pair support.

### 9.2 Lower symmetric corner

The branch

```text
1-2theta
```

reaches `5/8` exactly when

```text
theta=3/16.                                        (9.3)
```

The strip conditions `phi<=theta` and `theta+phi>=3/8` force

```text
phi=3/16.                                          (9.4)
```

Here `C=B^o(1)`, so the second common-core congruence itself cannot provide a fixed-power modulus saving; the first primitive pair and the remaining reciprocal quotient support saturate instead.

Thus the next obstruction is not one corner but the union

```text
upper edge:
  theta=5/16, 3/16<=phi<=1/4,

lower corner:
  theta=phi=3/16.                                  (9.5)
```

Define the next receiver

```text
FiveEighthsTwoBoundaryCommonCoreReciprocalIncidence.
```

A useful s7-32 should split these two mechanisms immediately rather than treating them as one homogeneous endpoint.

---

## 10. H / tH decision

No s-side auxiliary H is needed for s7-31.

The saving uses only:

- reducedness of the two physical states;
- exact four-cell root factorization;
- the s7-30 charged-once quantifier order;
- merged 4ci square-divisibility `t^2|C*u_res`;
- the primitive determinant-spacing lemma already proved in s7-29;
- elementary divisor counting.

The t/tH18 route remains a different fixed-U Cayley coefficient space and is not cross-promoted.  The completed generic genus-one audit remains nonminimal here.

```text
TH18_CROSS_PROMOTED_TO_S7_31=false
T69_CROSS_PROMOTED_TO_S7_31=false
GENERIC_GENUS_ONE_H_USED_BY_S7_31=false
S7_31_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.                (10.1)
```

Reconsider an s-specific H only after s7-32 has separately exhausted the upper-edge and lower-corner exact arithmetic.

---

## Stage boundary

```text
STAGE14_S7_31=COMPLETE_FIXED_OUTER_COMMON_GCD_SQUARE_DIVISIBILITY_AND_5_8_BOUND
MERGED_S7_30_IMPORTED=true
MERGED_4CI_COMMON_Z_SCALE_IMPORTED=true
MERGED_4CQ_COMPATIBLE=true
MERGED_X7_DOUBLE_CHARGE_GUARD_COMPATIBLE=true
OPPOSITE_QUOTIENT_COMMON_GCD_ODDPART_DIVIDES_COMMON_Z_SCALE=true
OPPOSITE_QUOTIENT_COMMON_GCD_ODDPART_SQUARE_DIVIDES_QK=true
OPPOSITE_QUOTIENT_COMMON_GCD_ODDPART_SQUARE_DIVIDES_C_URES=true
FIXED_OUTER_COMMON_GCD_MULTIPLICITY=Bo1
FIXED_OUTER_NONPRIMITIVE_ROOT_PAIR_LEMMA_PROVED=true
FIXED_OUTER_NONPRIMITIVE_ROOT_PAIR_BOUND=1+M/C
OPPOSITE_SIGNED_QUOTIENT_PAIR_EXPONENT=max(0,nu-chi)
DYADIC_FIXED_OUTER_BLOCK_EXPONENT=max(2theta,1-2theta)
FIXED_OUTER_COMMON_CORE_STRIP_UPPER_BOUND_EXPONENT=5/8
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8
IMPROVEMENT_OVER_11_16=1/16
CURRENT_GAP_TO_SQRT=1/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
FIVE_EIGHTHS_UPPER_EDGE_THETA=5/16
FIVE_EIGHTHS_UPPER_EDGE_PHI_RANGE=[3/16,1/4]
FIVE_EIGHTHS_LOWER_CORNER=(theta,phi)=(3/16,3/16)
REMAINING_RECEIVER=FiveEighthsTwoBoundaryCommonCoreReciprocalIncidence
TH18_CROSS_PROMOTED_TO_S7_31=false
T69_CROSS_PROMOTED_TO_S7_31=false
GENERIC_GENUS_ONE_H_USED_BY_S7_31=false
S7_31_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-32
```
