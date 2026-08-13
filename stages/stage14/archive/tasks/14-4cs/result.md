# Stage14-4cs — 5/8 promotion, quotient/root gcd identification, and two-boundary split

## Status

`COMPLETE_FIVE_EIGHTHS_PROMOTION_COMMON_GCD_ROOT_GCD_IDENTIFICATION_AND_TWO_BOUNDARY_SPLIT`

Stage14-4cs consumes merged `14-4cr`, merged `14-s7-31`, and the compatible Gaussian/Cayley factorization of merged `14-X7/14-X8`.

The mainline exponent improves from

```text
2/3
```

to

```text
boxed:
5/8.
```

The new algebraic point is that the common gcd which removed the s7-30 square-root loss is exactly the odd common gcd used in the second common-core peel of 4cq/4cr.  More precisely, with

```text
P=R*X,
Q=J*Y,
X=x_1*x_2,
Y=y_1*y_2,

Q+P=c*p,
Q-P=d*q,
h=gcd(c,d),
g_P=gcd(P,Q),
```

we prove

```text
boxed:
oddpart(h)
 = oddpart(g_P)
 = oddpart(gcd(X,Y)).
```

This identifies the former `common quotient gcd`, `second gcd-square peel`, and `common root-product gcd` as the same odd object.

It follows that the bad part removed from the common core in the dual-Cayley reduction is controlled by `h^2`, not by the square of the full root product.  The surviving 5/8 saturation then splits into two genuinely different components:

```text
upper edge:
  theta=5/16,
  3/16<=phi<=1/4,

lower corner:
  theta=phi=3/16.
```

At the lower corner the common core and `u_res` are both `B^o(1)`, so `h`, `gcd(X,Y)`, and every Cayley common-core factor are `B^o(1)`.  Thus the lower obstruction is no longer a common-core/Gaussian-root problem; it is a nearly coprime two-primitive-pair reciprocal factorization problem.

At the upper edge the second signed quotient pair is already divisor-many, while the first primitive common-core root line remains of exponent `1/8`.  The Cayley good core survives and its size is bounded below by the second-quotient exponent.

No further whole-family saving below `5/8` is claimed in this stage.

---

## 1. Imported balanced strip and the 5/8 theorem

Use the merged common-core strip

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8.
```

Write

```text
C=B^(chi+o(1)),
u_res=B^(mu+o(1)),
c*d<=B^(nu+o(1)).
```

Merged s7-31 proves the exact scale relations

```text
chi=2*theta+2*phi-3/4,
mu<=2*theta-2*phi,
nu<=1/4+2*phi-2*theta,
```

and the charged-once block bound

```text
E_31(theta,phi)
 <= chi+mu+(2phi-chi)+max(0,nu-chi)
 <= max(2theta,1-2theta).
```

Therefore

```text
boxed:
E_31(theta,phi)<=5/8
```

uniformly on the whole strip, and hence

```text
boxed:
V(B) << B^(5/8+o(1)).
```

Since merged 4cr had already promoted `2/3`, the new mainline gain is

```text
2/3-5/8=1/24.
```

Thus

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8
IMPROVEMENT_OVER_PREVIOUS_2_3=1/24
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.
```

---

## 2. Exact 5/8 saturation geometry

The function

```text
max(2theta,1-2theta)
```

can equal `5/8` only when

```text
theta=5/16
```

or

```text
theta=3/16.
```

The strip constraints determine the corresponding `phi` geometry exactly.

### Upper component

If

```text
theta=5/16,
```

then

```text
3/16<=phi<=1/4.
```

This gives the upper saturation edge

```text
boxed:
(theta,phi)=(5/16, phi),
3/16<=phi<=1/4.                                    (2.1)
```

### Lower component

If

```text
theta=3/16,
```

then `theta+phi>=3/8` forces `phi>=3/16`, while `theta-phi>=0` forces `phi<=3/16`.  Hence

```text
boxed:
theta=phi=3/16.                                   (2.2)
```

There are no other `5/8` saturation blocks.

```text
FIVE_EIGHTHS_SATURATION_COMPONENT_COUNT=2.
```

---

## 3. Imported physical root coordinates

Use the merged s7-31 root coordinates

```text
P_1=(R*S)*x_1^2,
Q_1=(T*J)*y_1^2,

P_2=(R*T)*x_2^2,
Q_2=(S*J)*y_2^2,
```

with reducedness

```text
gcd(P_i,Q_i)=1.
```

In particular

```text
gcd(x_1,y_1)=1,
gcd(x_2,y_2)=1.                                   (3.1)
```

Define

```text
X=x_1*x_2,
Y=y_1*y_2,
P=R*X,
Q=J*Y.                                             (3.2)
```

The common physical z-scale is

```text
z_i=2*x_i*y_i/g_i,
g_i in {1,2},
t=gcd(z_1,z_2).                                    (3.3)
```

Merged 4ci/s7-31 give

```text
boxed:
t^2 | C*u_res.                                     (3.4)
```

The opposite agreement split and signed quotients are

```text
p=L_k^+,
q=L_k^-,
gcd(p,q)=1,

Q+P=c*p,
Q-P=d*q,                                           (3.5)
```

and the physical coprimality statement used in s7-31 is

```text
boxed:
gcd(p*q,P*Q)=1.                                    (3.6)
```

Put

```text
h=gcd(c,d).                                         (3.7)
```

---

## 4. Quotient gcd equals the odd P,Q gcd

We first prove

```text
boxed:
oddpart(h)=oddpart(gcd(P,Q)).                       (4.1)
```

Fix an odd prime `ell`.  By (3.6), `ell|p*q` implies `ell` divides neither `P` nor `Q`; conversely any odd prime contributing to `gcd(P,Q)` is a unit on `p*q`.

From (3.5), for an odd `ell` which is a unit on `p*q`,

```text
v_ell(c)=v_ell(Q+P),
v_ell(d)=v_ell(Q-P).                               (4.2)
```

For odd `ell`, the standard sum/difference identity gives

```text
min(v_ell(Q+P),v_ell(Q-P))
 = min(v_ell(P),v_ell(Q)).                         (4.3)
```

Indeed, if both `Q+P` and `Q-P` are divisible by `ell^e`, then so are `2Q` and `2P`; since `ell` is odd this is equivalent to `ell^e|P,Q`.  The reverse implication is immediate.

Combining (4.2)-(4.3),

```text
v_ell(h)=v_ell(gcd(P,Q))
```

for every odd prime `ell`.  This proves (4.1).

This strengthens the one-way divisibility used in s7-31: at odd primes there is no hidden quotient-gcd support outside the actual common gcd of `P,Q`.

---

## 5. The odd P,Q gcd equals the odd X,Y root gcd

We next prove

```text
boxed:
oddpart(gcd(P,Q))
 = oddpart(gcd(X,Y)).                               (5.1)
```

Merged s7-31 already proves that an odd prime common to `P` and `Q` cannot divide `R` or `J`.  The reason is reducedness: if `ell|R` and `ell|Q=JY`, then `ell` divides one of `y_1,y_2`; the corresponding physical state has `ell` dividing both `P_i` and `Q_i`, contradiction.  The argument for `J` is symmetric.

Thus every odd common valuation of `P=RX` and `Q=JY` is carried entirely by `X,Y`, giving

```text
oddpart(gcd(P,Q)) | oddpart(gcd(X,Y)).              (5.2)
```

Conversely let an odd `ell` divide both `X` and `Y`.  By (3.1), it cannot occur in `x_i` and `y_i` for the same state; its occurrences are crosswise.  If `ell|R`, then because `ell|Y`, it divides some `y_i`, and again the corresponding state would have `ell|P_i,Q_i`.  Therefore `ell∤R`.  Similarly `ell∤J`.

Hence the full common odd valuation of `X,Y` survives unchanged in `P=RX,Q=JY`, proving the reverse divisibility in (5.1).

Combining Sections 4 and 5 gives the central identification

```text
boxed:
oddpart(h)
 = oddpart(gcd(P,Q))
 = oddpart(gcd(X,Y)).                               (5.3)
```

We denote this common odd gcd by

```text
H := oddpart(h).                                    (5.4)
```

---

## 6. H is simultaneously a fixed-outer square divisor and a root-product square divisor

Merged s7-31 proves

```text
H | t.
```

Together with (3.4),

```text
boxed:
H^2 | C*u_res.                                      (6.1)
```

By (5.3), `H|X` and `H|Y`, so also

```text
boxed:
H^2 | X*Y.                                          (6.2)
```

Therefore

```text
boxed:
H^2 | gcd(C*u_res, X*Y).                            (6.3)
```

This is the exact common interface between the s7-31 fixed-outer gcd argument and the 4cq/4cr dual-Cayley root product.

Since the balanced root product has

```text
X*Y=B^(1/4+o(1)),                                  (6.4)
```

we obtain the global physical size guard

```text
boxed:
H <= B^(1/8+o(1)).                                 (6.5)
```

The stronger point for counting remains that after `(C,u_res)` is fixed, `H` has only `B^o(1)` possibilities as a square-divisor root of `C*u_res`.

---

## 7. The 4cq second gcd peel is exactly the H peel at odd primes

Merged 4cq defines

```text
g_A=gcd(A,D),
g_P=gcd(P,Q),

C_1=C/gcd(C,g_A^2),
C_*=C_1/gcd(C_1,g_P^2),
C_bad=C/C_*.                                       (7.1)
```

It also proves

```text
g_A | r*s,
```

with `r,s=B^o(1)`.

By (5.3),

```text
oddpart(g_P)=H.                                     (7.2)
```

From the sequential definition (7.1),

```text
C_bad | g_A^2*g_P^2.
```

Since `C` is odd, we may state the useful odd bound as

```text
boxed:
C_bad | oddpart(r*s)^2 * H^2.                      (7.3)
```

up to the endpoint-small divisor decoration already absorbed throughout Stage14.

Using (6.2), this sharpens the older coarse 4cq guard

```text
C_bad | (r*s*X*Y)^2
```

to

```text
boxed:
C_bad <= B^(1/4+o(1)).                             (7.4)
```

at exponent scale.

The point is structural rather than merely numeric: the only non-small moving support that can be removed from the common core is the square of the actual common root gcd `H`, not an arbitrary divisor of the full root product.

```text
SECOND_COMMON_CORE_GCD_PEEL_IDENTIFIED_WITH_QUOTIENT_COMMON_GCD=true.
```

---

## 8. Upper 5/8 edge: exact scale profile

Set

```text
theta=5/16,
3/16<=phi<=1/4.                                    (8.1)
```

Then

```text
chi =2phi-1/8,
mu  <=5/8-2phi,
nu  <=2phi-3/8.                                    (8.2)
```

The first primitive xi-agreement pair count has exponent

```text
2phi-chi=1/8.                                      (8.3)
```

For the second quotient pair,

```text
nu-chi <= -1/4,                                    (8.4)
```

so merged s7-31 gives

```text
boxed:
fixed earlier outer data
=> #(c,d)=B^o(1).                                  (8.5)
```

Thus upper-edge saturation comes entirely from

```text
C support              : chi,
u_res support          : mu,
first primitive pair   : 1/8,
second quotient pair   : 0,
```

with

```text
chi+mu+1/8=5/8.                                    (8.6)
```

The new gcd identification adds

```text
H^2 | X*Y,
C_bad | B^o(1)*H^2,
```

so

```text
C_bad <= B^(1/4+o(1)).                             (8.7)
```

Consequently the good Cayley core satisfies

```text
C_*=C/C_bad
 >= B^(max(0,chi-1/4)-o(1))
 = B^(max(0,2phi-3/8)-o(1)).                       (8.8)
```

On this edge `phi>=3/16`, so the right-hand side equals the maximal second-quotient exponent `nu`:

```text
boxed:
C_* >= B^(nu-o(1)).                                (8.9)
```

Merged 4cr splits

```text
C_*=C_-*C_+,
gcd(C_-,C_+)=1,
```

with opposite/same Gaussian root orientations on `C_-`/`C_+`.  Therefore at least one orientation component has scale

```text
max(C_-,C_+)
 >= B^(nu/2-o(1)).                                 (8.10)
```

This does not by itself produce an additional spacing factor: the orientation split is reconstructed from the same physical point.  Charging it independently would violate the X7 self-generated-modulus guard.

The minimal upper-edge receiver is therefore

```text
UpperFiveEighthsCayleyGaussianOuterSupportPrimitiveRootLineIncidence.  (8.11)
```

It must exploit the fixed outer `(C,u_res,H)` together with the already divisor-many second quotient pair and the same/opposite Gaussian orientation relation, without multiplying `C_+C_-` as a new independent modulus.

---

## 9. Lower 5/8 corner: common-core machinery collapses

Now set

```text
theta=phi=3/16.                                    (9.1)
```

Then

```text
chi=0,
mu<=0,
nu<=1/4,
2phi-chi=3/8.                                      (9.2)
```

Thus

```text
C=B^o(1),
u_res=B^o(1).                            (9.3)
```

By (6.1),

```text
H^2 | C*u_res=B^o(1),
```

so

```text
boxed:
H=B^o(1).                                          (9.4)
```

Using (5.3),

```text
boxed:
oddpart(gcd(X,Y))=B^o(1).                          (9.5)
```

The second quotient common gcd is also endpoint-small:

```text
boxed:
oddpart(gcd(c,d))=B^o(1).                          (9.6)
```

Since `C=B^o(1)`, every 4cr common-core factor is small:

```text
C_bad=B^o(1),
C_*=B^o(1),
C_-=B^o(1),
C_+=B^o(1).                                        (9.7)
```

Therefore the lower `5/8` obstruction is not a Cayley-Gaussian common-core orientation problem at fixed-power scale.

After dividing `(c,d)` by their `B^o(1)` gcd, the second signed quotient pair is primitive up to endpoint decoration and has product range

```text
B^(1/4+o(1)).
```

The first primitive agreement pair has support

```text
B^(3/8+o(1)).
```

These two supports multiply to the lower `5/8` boundary.

The minimal lower-corner receiver is

```text
LowerFiveEighthsCoprimeRootProductTwoPrimitiveReciprocalFactorizationIncidence.  (9.8)
```

It retains

```text
oddpart(gcd(X,Y))=B^o(1)
```

and the exact reciprocal reconstruction between the two primitive pairs.  Generic common-core determinant spacing cannot improve this corner because the common-core modulus itself is only `B^o(1)`.

---

## 10. Why the two components must not be merged prematurely

The upper and lower saturation components lose `5/8` for different reasons.

Upper edge:

```text
large outer C/u_res support
+ B^(1/8) first primitive root line,
```

while the second quotient pair is divisor-many.

Lower corner:

```text
B^(3/8) first primitive pair
+ B^(1/4) second nearly primitive pair,
```

while `C`, `u_res`, and the common root gcd are all endpoint-small.

A single generic `FiveEighthsTwoBoundaryCommonCoreReciprocalIncidence` hides this distinction.  Stage14-4cs therefore replaces it by the ordered pair

```text
UPPER_RECEIVER=
UpperFiveEighthsCayleyGaussianOuterSupportPrimitiveRootLineIncidence

LOWER_RECEIVER=
LowerFiveEighthsCoprimeRootProductTwoPrimitiveReciprocalFactorizationIncidence.  (10.1)
```

Any future whole-family improvement below `5/8` must save both components.

---

## 11. Relation to X7/X8 and t70

Merged X7 proves that the real/twisted four-root moduli are self-generated and cannot be recharged as independent determinant spacing.  Stage14-4cs preserves that guard.

At the upper edge, `C_+,C_-` are divisor allocations of the already-fixed outer common core; their same/opposite Gaussian orientation can be retained as a filter, but not multiplied into `C` as a second modulus charge.

At the lower corner, `C=B^o(1)`, so X7/X8 common-core Gaussian orientation has no fixed-power leverage at all.  The useful X7 information is instead the exact root-product/resultant dictionary for a later pair-energy attack.

Merged t70 operates in the fixed-U private-largest-prime Cayley coefficient space.  Its common-support root line is not cross-promoted to the present s/mainline packet.

```text
T70_CROSS_PROMOTED_TO_MAINLINE=false.
```

---

## 12. H / tH decision

No new mainline H request is justified at 4cs.

Both surviving components still have unused exact arithmetic structure:

- upper: fixed-outer `H`, sharpened `C_bad`, divisor-many second quotient pair, and same/opposite Gaussian orientation;
- lower: endpoint-small common gcd, nearly coprime `X,Y`, and two primitive reciprocal pairs.

The correct next move is to attack the two components separately before asking for an external incidence theorem.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH18_CROSS_PROMOTED_TO_MAINLINE=false
T70_CROSS_PROMOTED_TO_MAINLINE=false.
```

If a later H audit becomes necessary, it must be receiver-specific; a generic genus-one or generic large-sieve request is not minimal here.

---

## Stage boundary

```text
STAGE14_4CS=COMPLETE_FIVE_EIGHTHS_PROMOTION_COMMON_GCD_ROOT_GCD_IDENTIFICATION_AND_TWO_BOUNDARY_SPLIT
MERGED_4CR_IMPORTED=true
MERGED_S7_31_IMPORTED=true
MERGED_X7_X8_GUARDS_IMPORTED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8
IMPROVEMENT_OVER_PREVIOUS_2_3=1/24
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
FIVE_EIGHTHS_SATURATION_COMPONENT_COUNT=2
FIVE_EIGHTHS_UPPER_EDGE_THETA=5/16
FIVE_EIGHTHS_UPPER_EDGE_PHI_RANGE=[3/16,1/4]
FIVE_EIGHTHS_LOWER_CORNER=theta=phi=3/16
ODDPART_QUOTIENT_GCD_EQUALS_PQ_GCD=true
ODDPART_PQ_GCD_EQUALS_XY_GCD=true
ODDPART_H_EQUALS_ODDPART_GCD_XY=true
H_SQUARED_DIVIDES_C_URES=true
H_SQUARED_DIVIDES_X_TIMES_Y=true
C_BAD_CONTROLLED_BY_SMALL_RS_AND_H_SQUARED=true
C_BAD_EXPONENT_MAX=1/4
UPPER_SECOND_SIGNED_QUOTIENT_PAIR_MULTIPLICITY=Bo1
UPPER_GOOD_CAYLEY_CORE_EXPONENT_LOWER_BOUND=2phi-3/8
LOWER_COMMON_CORE_EXPONENT=0
LOWER_ODDPART_GCD_XY=Bo1
LOWER_CAYLEY_GAUSSIAN_COMMON_CORE_FIXED_POWER_LEVERAGE=false
UPPER_RECEIVER=UpperFiveEighthsCayleyGaussianOuterSupportPrimitiveRootLineIncidence
LOWER_RECEIVER=LowerFiveEighthsCoprimeRootProductTwoPrimitiveReciprocalFactorizationIncidence
REMAINING_RECEIVER=FiveEighthsUpperCayleyLowerCoprimeBoundaryPair
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT=Stage14-4ct
```
