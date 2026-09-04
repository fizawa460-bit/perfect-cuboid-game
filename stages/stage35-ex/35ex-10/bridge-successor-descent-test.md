# Stage35-EX 35EX-10A — bridge successor and exact descent obstruction

## Scope

Assume the hostile-audited conditional reductions through 35EX-09. The third primitive bridge triple from 35EX-08 is

```text
U3 = U1*U2/(c*e) = U1*T/e,
V3 = q*H/e,
W3 = p*w/e,
```

with

```text
U3^2 + V3^2 = W3^2,
gcd(U3,V3)=1,
U3,W3 odd,
V3 even.
```

Thus the bridge parameters `(alpha,beta)` do not merely parameterize an auxiliary conic: they give a genuine new primitive Euclid triple

```text
U3=alpha^2-beta^2,
V3=2*alpha*beta,
W3=alpha^2+beta^2.
```

This leaf tests whether that new triple is already a smaller counterexample of the same Stage35-EX type.

## 1. The canonical no-new-choice successor fails to inherit the two squares

The only successor available without inventing a new second Euclid triple is to replace the first primitive triple by `(U3,V3,W3)` and keep the original second triple `(U2,V2,W2)`.

Its two raw square conditions would be

```text
E3 = (W3*U2)^2 + (U3*V2)^2,
M3 = (V3*U2)^2 + (U3*V2)^2.
```

Using `U2=c*T`, the bridge definitions give

```text
E3 = (T/e)^2 * [ (c*p*w)^2 + (U1*V2)^2 ],
M3 = (T/e)^2 * [ (c*q*H)^2 + (U1*V2)^2 ].
```

The old E1-counterexample and Master squares are

```text
(c*p*w)^2 = (W1*U2)^2 + (U1*V2)^2,
(c*q*H)^2 = (V1*U2)^2 + (U1*V2)^2.
```

Therefore the successor obligations are exactly

```text
E3 = (T/e)^2 * [ (W1*U2)^2 + 2*(U1*V2)^2 ],
M3 = (T/e)^2 * [ (V1*U2)^2 + 2*(U1*V2)^2 ].
```

The audited identities through 35EX-09 do not make either bracket a square. They are new quadratic-form conditions of type `X^2+2Y^2=square`.

Consequently the bridge triple does not inherit the simultaneous E1/Master square property when paired with the original second triple.

## 2. No automatic canonical gcd transport

Even if one of the two new norms happened to be square, the Stage35-EX counterexample type requires new canonical quantities

```text
c3 = gcd(U3,U2),
p3 = gcd(W3,V2),
q3 = gcd(V3,V2)
```

and the corresponding reduced E1/Master primitive conditions. The bridge construction determines `(U3,V3,W3)` but supplies no exact identities identifying `c3,p3,q3` with the old `c,p,q,e,T` in a way that reproduces 35EX-02 through 35EX-03.

Thus a same-type successor needs genuinely new arithmetic input; it is not a formal consequence of the third primitive triple.

## 3. No monotone height inequality is supplied by the bridge

The component ratios are

```text
U3/U1 = T/e,
V3/H  = q/e,
W3/w  = p/e.
```

The current exact theory gives

```text
e | c,
gcd(e,p)=gcd(e,q)=gcd(e,T)=1,
```

but no inequality forcing `T<e`, `p<e`, or `q<e`. Hence no componentwise or canonical-hypotenuse height decrease follows from the bridge formulas alone.

This does not prove that some more elaborate descent map cannot exist. It proves that the natural bridge substitution is not a self-map of the full counterexample system and that the present formulas provide no verified decreasing height.

## Exact status

```text
BRIDGE_IS_GENUINE_PRIMITIVE_EUCLID_TRIPLE=true
CANONICAL_KEEP_SECOND_TRIPLE_SUCCESSOR_INHERITS_E1_SQUARE=false
CANONICAL_KEEP_SECOND_TRIPLE_SUCCESSOR_INHERITS_MASTER_SQUARE=false
NEW_SUCCESSOR_GCD_ADAPTER_PROVED=false
UNIFORM_HEIGHT_DECREASE_PROVED=false
INFINITE_DESCENT_PROVED=false
```

The second half of 35EX-10 therefore turns to the alternative authorized route: an odd split-prime valuation obstruction from the complete three-reservoir graph.
