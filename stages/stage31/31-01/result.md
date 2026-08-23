# Stage31-01-XL — full closure attempt

```text
STATUS=SUBMITTED_FULL_CLOSURE_PENDING_FINAL_HOSTILE_AUDIT
ROADMAP_PATH=ONE_SHOT_XL_SUCCESS
FALLBACK_UNIT_ACTIVATED=false
```

## 1. Receiver

Stage31 attacks exactly

```text
K16-C2-EXT-E-INTEGRAL-CERTIFICATION
R29-EXT-CHANG-E
parent route: J12-PARAMETRIC
```

The claim is confined to the Paper-E prime-parameter Sophie--Germain thin subfamily. No global endpoint claim follows.

## 2. Source claim repaired rather than assumed

Stage29 rejected Paper E because the committed scripts supplied a bounded point search and sampled height constant, but not a complete integral-point certificate or the load-bearing quartic/elliptic transfer.

Stage31 independently reconstructed the family reduction and then replaced the unsafe implication

```text
elliptic integral points complete => quartic integral points complete
```

by a direct complete computation on the quartic itself.

The frozen curve is

```text
C: 20 Z^2 = Y^4+8Y^3+18Y^2-8Y+1.
```

Set `U=10Z`. Then

```text
Q: U^2 = 5Y^4+40Y^3+90Y^2-40Y+5.
```

`C(Z)` injects into `Q(Z)` by `(Y,Z)->(Y,10Z)`, and the inverse is exactly the divisibility filter `10|U` followed by `Z=U/10`.

## 3. Complete quartic enumeration

GitHub Actions executed the University of Sydney official Magma calculator with Magma V2.29-9.

```text
IntegralQuarticPoints(
  [5,40,90,-40,5],
  [1,10]
)
```

returned the three representatives

```text
(-1,10), (1,-10), (11,370).
```

Restoring the hyperelliptic sign gives exactly six signed integral points, all with `10|U`, hence

```text
C(Z) = {
  (-1,-1), (-1,1),
  ( 1,-1), ( 1,1),
  (11,-37), (11,37)
}.
```

Execution provenance:

```text
workflow run = 32607148918
job         = 97113828969
artifact    = 9484415535
artifact sha256 = 32c6f9ab32b60faa29b7a8cf7cfc3133115ea19ece422facf51ff255089f8a17
Magma = 2.29-9
runtime error = false
```

No sampled height bound, bounded `ellratpoints`, database count, BSD, or GRH is used for this completeness statement.

## 4. Explicit birational map

The missing map was reconstructed exactly. Write

```text
t=Y-1,
W=20Z,
u=(W+20+28t)/t^2.
```

The quartic identity becomes

```text
(u^2-20)t^2-(56u+240)t-(40u+176)=0.
```

Define

```text
v=2(u^2-20)t-(56u+240).
```

Then

```text
v^2=160(u+4)(u^2+20u+68).
```

Putting `U0=u+8`, `x=5U0/2`, `y=5v/16` gives exactly

```text
E: y^2=x^3-275x+1750.
```

On `Y != 1` the forward map simplifies to

```text
x = 10(2Y^2+3Y+5Z)/(Y-1)^2,
y = 25(3Y^3+15Y^2+14YZ+3Y+6Z-1)/(Y-1)^3.
```

For a finite point `(x,y)` on `E`, put

```text
u=2x/5-8,
v=16y/5,
t=(v+56u+240)/(2(u^2-20)),
Y=1+t,
W=u t^2-20-28t,
Z=W/20.
```

Since rational `u` cannot satisfy `u^2=20`, the inverse denominator does not vanish on a finite rational E-point. The exceptional extension is

```text
C(1,1)  -> O,
C(1,-1) -> E(9,2).
```

The independent verifier checks the polynomial derivation and every certified integral-point image.

## 5. Mordell--Weil certificate

Magma independently returned

```text
E(Q) ~= Z/2 + Z
MW_RANK_PROVED=true
MW_FULL_GROUP_PROVED=true
TORSION=Z/2
Magma generators: (10,0), (9,2).
```

Paper E used `(-15,50)` as a free generator; exactly

```text
(-15,50)=-(9,2)-(10,0),
```

so this is also a valid free generator modulo torsion.

Magma's integral-point representatives are

```text
(-15,-50), (9,2), (10,0), (46,294),
```

which restore to seven signed E-integral points.

This MW result is a cross-check and repairs the Paper-E generator/saturation requirement, but the quartic completeness proof does not depend on transferring quartic integrality to E.

## 6. Independent elementary check of E integral points

There is also a short independent check of the seven elliptic integral points.

Translate `X=x-10`. Then

```text
y^2 = X(X^2+30X+25),
gcd(X,X^2+30X+25)=gcd(X,25).
```

For every prime other than 5, the valuation of `X` is even. If `v5(X)=1`, writing `X=5a` with `5∤a` gives valuation 2 for the second factor because `a^2+6a+1` has no root mod 5, making the product valuation 3, impossible. If `v5(X)>=2`, the second factor again has valuation 2, so `v5(X)` must be even. Therefore

```text
X = +/- s^2.
```

For `X=s^2`, the remaining square condition is

```text
v^2=(s^2+15)^2-200,
(s^2+15-v)(s^2+15+v)=200,
```

whose factor pairs give `s^2=0,36`.

For `X=-s^2`,

```text
v^2=200-(s^2-15)^2,
```

so `s<=5`, and exact checking gives `s^2=1,25`.

Thus

```text
x in {-15,9,10,46}
```

and exactly seven signed integral points, agreeing with Magma.

## 7. Exhaustive Paper-E reconstruction

Paper E's frozen branch dictionary is

```text
Case II: Y=p,  q=(p^2+2p-1)/2,
Case I:  Y=-p, q=(p^2-2p-1)/2,
```

under the odd coprime `p<q`, prime-`p` family hypotheses.

The complete quartic list has only one negative Y-value, `Y=-1`, so Case I has no prime parameter. Positive Y-values are `1` and `11`; only `11` is prime. Hence Case II has one nondegenerate candidate before the third-face test:

```text
p=11,
q=71,
(a,b,c)=(3124,4557,9840).
```

Exact tests give

```text
a^2+b^2 = 30,525,625 = 5525^2,
a^2+c^2 = 106,584,976 = 10324^2,
a^2+b^2+c^2 = 127,351,225 = 11285^2,
b^2+c^2 = 117,591,849.
```

But

```text
10843^2 = 117,570,649
10844^2 = 117,592,336,
```

so `117,591,849` is not a square. The unique nondegenerate prime-family candidate fails the third face.

Therefore, submitted for audit:

```text
QUARTIC_ELLIPTIC_BIRATIONAL_MAP=VERIFIED
DIRECT_QUARTIC_INTEGRALITY_TRANSFER=VERIFIED
MW_BASIS_COMPLETE_AND_SATURATED=VERIFIED_BY_MAGMA_FULL_GROUP
INTEGRAL_POINT_COMPLETENESS_CERTIFIED=TRUE_DIRECT_QUARTIC
QUARTIC_INTEGRAL_POINTS=COMPLETE_6_SIGNED_POINTS
PULLBACK_RECONSTRUCTION=COMPLETE
PRIME_SOPHIE_GERMAIN_SUBFAMILY_EXCLUSION=VERIFIED
R29_EXT_CHANG_E=PROPOSED_DISCHARGED_INTEGRAL_CERTIFICATION
K16_C2_EXT_E_INTEGRAL_CERTIFICATION=PROPOSED_CLOSED
FALLBACK_UNIT_ACTIVATED=false
```

## 8. Firewall

Always:

```text
COVERAGE=THIN_PRIME_SUBFAMILY_ONLY
J12_PARAMETRIC=AMBER
ROUTE_COLOR_CHANGED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
STAGE31_CLOSED=false
```

Stage31 closes only after `Stage31-audit` independently reconstructs this certificate.
