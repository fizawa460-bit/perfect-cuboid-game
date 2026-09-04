# Stage35-EX 35EX-17 — product-hypotenuse successor or no self-map

## Scope

Continue from hostile-audited 35EX-15/16 and the exact 35EX-14 product-hypotenuse receiver. This leaf tests only whether a hypothetical E1 counterexample canonically generates a **same-type** Stage35 counterexample with a strictly smaller well-founded height.

No E1, receiver, Stage35 MAIN, Stage29-parent, infinite-descent, or endpoint credit is claimed.

Use the primitive Euclid data

```text
T1=(U1,V1,W1),  T2=(U2,V2,W2),
p=gcd(W1,V2),   d=gcd(V1,W2),
```

and assume the full 35EX-14 receiver

```text
Lminus=(W1*W2-V1*V2)/(p*d)=x^2,
Lplus =(W1*W2+V1*V2)/(p*d)=y^2.
```

Put

```text
R=(y+x)/2,
S=(y-x)/2,
E=sqrt(W1^2*W2^2-V1^2*V2^2).
```

Then 35EX-14 proves the primitive product-hypotenuse triple

```text
P=(U3,V3,W3)
U3=R^2-S^2=E/(p*d),
V3=2*R*S=V1*V2/(p*d),
W3=R^2+S^2=W1*W2/(p*d).                 (PH)
```

This leaf asks whether `(PH)` is a descent map rather than merely a receiver coordinate.

## 1. Same-type successor requires more than one primitive triple

The Stage35 counterexample species is not one Pythagorean triple. It requires two primitive Euclid triples together with the Master square, the E1 square, and the canonical cross-gcd normalization for that new pair.

`(PH)` canonically produces only the single triple `P`. The visible inherited product splittings are

```text
W3=(W1/p)*(W2/d),
V3=(V1/d)*(V2/p).
```

They do not reconstruct two primitive Pythagorean triples. In particular the would-be factor pairs would require new square conditions such as

```text
(W1/p)^2-(V1/d)^2 is a square,
(W2/d)^2-(V2/p)^2 is a square,
```

and no current Stage35 identity proves these conditions. The cross-gcd normalization therefore entangles the two source triples rather than transporting them separately.

Hence

```text
PRODUCT_HYPOTENUSE_CANONICAL_TWO_TRIPLE_RECONSTRUCTION=false.
```

This is a statement about the current exact identities, not an impossibility theorem for all future constructions.

## 2. Natural source-preserving candidate A: `(P,T2)`

Keep the original second triple and pair it with `P`. The raw Master-square expression for this candidate is

```text
(V3*U2)^2+(U3*V2)^2
 = (V2/(p*d))^2 * ((V1*U2)^2+E^2)
 = (V2/(p*d))^2 * ((U1*W2)^2+2*(V1*U2)^2).    (A-M)
```

Thus same-type Master admissibility requires the fresh square obligation

```text
(U1*W2)^2+2*(V1*U2)^2 is a square.             (A-M-NEW)
```

The corresponding raw E1 expression is

```text
(W3*U2)^2+(U3*V2)^2
 = 1/(p*d)^2 * ((W1*W2*U2)^2+(E*V2)^2)
 = 1/(p*d)^2 * ((W1*W2^2)^2-(V1*V2^2)^2).    (A-E1)
```

Its squareness is also a fresh obligation. Neither `(A-M-NEW)` nor `(A-E1)` is supplied by the original Master square plus E1 square.

Therefore `(P,T2)` is not a proved same-type successor.

## 3. Natural source-preserving candidate B: `(T1,P)`

Keep the original first triple and pair it with `P`. Its raw Master-square expression is

```text
(V1*U3)^2+(U1*V3)^2
 = (V1/(p*d))^2 * (E^2+(U1*V2)^2)
 = (V1/(p*d))^2 * ((W1*U2)^2+2*(U1*V2)^2).    (B-M)
```

Thus Master admissibility requires the fresh square obligation

```text
(W1*U2)^2+2*(U1*V2)^2 is a square.             (B-M-NEW)
```

The corresponding raw E1 expression is

```text
(W1*U3)^2+(U1*V3)^2
 = 1/(p*d)^2 * (W1^2*E^2+U1^2*V1^2*V2^2)
 = 1/(p*d)^2 * ((W1^2*W2)^2-(V1^2*V2)^2).    (B-E1)
```

Again the needed square conditions are new and are not consequences currently proved from the source counterexample identities.

Therefore `(T1,P)` is not a proved same-type successor.

## 4. Height test does not rescue the map

The new receiver hypotenuse is exactly

```text
W3=W1*W2/(p*d).
```

The current hypotheses do not prove `p*d>1`. In the legal case `p=d=1`,

```text
W3=W1*W2,
```

so even the single product-hypotenuse coordinate has no uniform strict decrease relative to the natural product height. More importantly, no second same-type successor triple and no transported canonical gcd channels have been constructed, so there is no admissible successor on which a Stage35 descent height could be evaluated.

Hence

```text
STRICT_WELL_FOUNDED_SAME_TYPE_HEIGHT_DECREASE_PROVED=false.
INFINITE_DESCENT_PROVED=false.
```

## 5. Exact route boundary

The legal conclusion is

```text
CURRENT_PRODUCT_HYPOTENUSE_SELF_MAP_ROUTE=FROZEN_NO_CANONICAL_SAME_TYPE_SUCCESSOR
PRODUCT_HYPOTENUSE_PRIMITIVE_TRIPLE_RETAINS_EXACT_RECEIVER_VALUE=true
PRODUCT_HYPOTENUSE_CANONICAL_TWO_TRIPLE_RECONSTRUCTION=false
NATURAL_SUCCESSOR_P_T2_REQUIRES_NEW_SQUARE_OBLIGATIONS=true
NATURAL_SUCCESSOR_T1_P_REQUIRES_NEW_SQUARE_OBLIGATIONS=true
STRICT_WELL_FOUNDED_SAME_TYPE_HEIGHT_DECREASE_PROVED=false
ALL_PRODUCT_HYPOTENUSE_DESCENTS_RULED_OUT_IN_PRINCIPLE=false
INFINITE_DESCENT_PROVED=false
```

Reopen only if a new exact construction supplies **both** primitive successor triples, the same-type Master and E1 square conditions, the canonical gcd adapter, and a strictly decreasing well-founded height.

This is `BLOCKED_NO_NEW_INFORMATION` with respect to theorem credit: the receiver triple remains exact, but the attempted self-map does not transport the Stage35 counterexample species.

## 6. Arsenal check

The Research OS canonical route was followed: `docs/arsenal/index.json` first, then the relevant formal card. `S34-W01` is the closest descent-shaped card, but it does not supply the missing same-type successor reconstruction here; its previous Stage35 bridge adapter is already frozen. No Arsenal card currently supplies the two-triple reconstruction plus strict height decrease required by this leaf.

Therefore no Arsenal theorem credit is imported.

## 7. Cycle consequence

35EX-14's fresh breadth audit selected three materially distinct residual candidates. 35EX-15 and 35EX-16 are now frozen, and this leaf freezes the remaining product-hypotenuse descent candidate. Under the Cycle Exploration Safety Protocol, three blocked routes since the last broad audit and an otherwise pending park trigger a fresh `EXHAUSTIVE_VIEW_AUDIT` plus `BLIND_REDISCOVERY`.

Accordingly this leaf does **not** park Stage35 by itself. The immediate next action is a fresh breadth audit on the exact coprime receiver.

## Credit firewall

```text
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
