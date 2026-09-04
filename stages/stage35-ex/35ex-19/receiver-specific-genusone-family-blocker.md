# Stage35-EX 35EX-19 — receiver-specific genus-one family blocker

## Scope

Continue from hostile-audited and merged 35EX-18. Work conditionally under a hypothetical full E1 counterexample and retain the primitive Master-Hit source hypotheses.

The active question is exactly whether the full receiver can be sent to one **fixed** quartic/genus-one curve with a source-locked adapter, so that formal Arsenal weapon `S31-W01` can be used as more than routing guidance.

The answer at the present identity level is **no**. A smooth genus-one quartic appears only after fixing one moving source parameter. The resulting fibers form a non-isotrivial one-parameter family. Thus no single fixed elliptic/genus-one model is derived from the current receiver.

The failed fixed-fiber route exposes a new exact source-filtered paired-quartic hook, recorded in Section 7 for the next cycle.

No E1, receiver, Stage35 MAIN, Stage29-parent, or endpoint credit is claimed.

## 1. Source-normalized receiver

Put

```text
r = U1/W1,
t = U2/W2,
s1 = V1/W1,
s2 = V2/W2.
```

For primitive positive Euclid triples,

```text
0 < r,t < 1,
r^2+s1^2=1,
t^2+s2^2=1.
```

Let

```text
mu = sqrt((V1*U2)^2+(U1*V2)^2)/(W1*W2),
nu = sqrt((W1*U2)^2+(U1*V2)^2)/(W1*W2).
```

On a Master-Hit plus full E1 counterexample, `mu,nu` are rational. Direct division by `(W1*W2)^2` gives exactly

```text
mu^2 = r^2 + t^2 - 2*r^2*t^2
     = r^2 + (1-2*r^2)*t^2,                 (M)

nu^2 = r^2 + t^2 - r^2*t^2
     = r^2 + (1-r^2)*t^2.                   (E)
```

Also

```text
nu^2-mu^2 = r^2*t^2,                         (DIFF)
```

which is the normalized form of the already-known product-hypotenuse bridge and is not counted as a new theorem species here.

## 2. Fixing the first source parameter produces a quartic

Fix an admissible rational `r` and define

```text
k = 1-2*r^2.
```

The Master equation `(M)` is the conic

```text
mu^2 = r^2 + k*t^2.
```

Use its rational base point `(t,mu)=(0,r)` and put

```text
u0 = (mu-r)/t.
```

To avoid collision with the E1 coordinate `nu`, rename this slope variable

```text
u0 = u.
```

For every actual source point `t>0`. Moreover `k!=0` for rational admissible `r`, so `u=0` cannot occur on the source image. Expanding `mu=r+u*t` in `(M)` gives

```text
t*(k-u^2)=2*r*u,

t = 2*r*u/(k-u^2),                           (T(u))

mu = r*(k+u^2)/(k-u^2).                      (MU(u))
```

The denominator `k-u^2` cannot vanish on an actual source point, because then `2*r*u=0`, while `r>0` and the preceding paragraph gives `u!=0`.

Now define

```text
Y = nu*(k-u^2)/r.
```

Substituting `(T(u))` into `(E)` gives exactly

```text
Y^2 = (k-u^2)^2 + 4*(1-r^2)*u^2
    = u^4 + 2*u^2 + k^2.                     (Ck)
```

Thus every full-receiver source point with fixed `r` maps to

```text
C_k : Y^2 = u^4 + 2*u^2 + k^2.
```

Conversely, on the open `u*(k-u^2)!=0`, a rational point `(u,Y)` on `C_k` recovers the simultaneous Master/E1 square fiber by

```text
t  = 2*r*u/(k-u^2),
mu = r*(k+u^2)/(k-u^2),
nu = r*Y/(k-u^2).
```

Exact substitution recovers `(M)` and `(E)`. This is the exact fixed-`r` square-fiber adapter. It does **not** yet enforce that the recovered `t` lies on the second source unit circle; that source condition is restored in Section 7.

## 3. Every admissible fiber is smooth genus one

The quartic polynomial is

```text
f_k(u)=u^4+2*u^2+k^2.
```

Its exact polynomial discriminant is

```text
Disc_u(f_k)=256*k^2*(k-1)^2*(k+1)^2.          (DISC)
```

For an admissible primitive first source triple:

- `k=1` would give `r=0`, impossible because `U1>0`;
- `k=-1` would give `r^2=1`, impossible because `V1>0`;
- `k=0` would give rational `r` with `r^2=1/2`, impossible over `Q`.

Therefore `Disc_u(f_k)!=0` for every admissible source fiber. Since `(u,Y)=(0,k)` is a rational point, `C_k` is a smooth genus-one curve with a rational point, hence an elliptic curve after choosing that point as origin.

This is a genuine exact genus-one reduction, but only **fiberwise** after fixing the moving source parameter `r`.

## 4. The genus-one family is non-isotrivial

For the binary quartic

```text
Y^2=u^4+2*u^2+k^2,
```

the standard quartic invariants are

```text
I = 4*(1+3*k^2),
J = 16*(9*k^2-1),
Delta = (4*I^3-J^2)/27
      = 256*k^2*(1-k^2)^2.
```

Hence its elliptic `j`-invariant is

```text
j(k) = 2^8*I^3/Delta
     = 64*(1+3*k^2)^3/(k^2*(1-k^2)^2).       (J)
```

This rational function is nonconstant. The source parameter

```text
k = 1-2*((a^2-b^2)/(a^2+b^2))^2
```

moves with the primitive first Euclid pair. In particular the already-source-locked genuine Master-Hit witnesses with first pairs `(4,3)` and `(8,5)` give

```text
k_43 = 527/625,
k_85 = 4879/7921,
```

and exact substitution into `(J)` gives distinct rational `j` values.

Therefore the quartics arising from the normalized receiver are not all birational over `Qbar` to one fixed elliptic curve. The receiver exposes a **non-isotrivial genus-one family**, not a single fixed curve.

The witness use here does not claim those Master-Hits are E1 counterexamples. It only regression-locks that the source base parameter is genuinely moving on the admitted Master population. The non-isotriviality statement itself is the exact algebraic dependence `(J)`.

## 5. Why this blocks the current S31-W01 plan

Formal Arsenal card `S31-W01` certifies an explicit rational birational adapter between an already-fixed quartic and elliptic model, including inverse denominators and exceptional loci. It does not collapse a moving family to one fixed elliptic curve and grants no automatic integral-point transfer.

35EX-19 now supplies:

```text
FIXED_R_GENUS_ONE_QUARTIC_DERIVED=true
FIXED_R_SOURCE_TO_SQUARE_FIBER_ADAPTER_PROVED=true
GENUS_ONE_FAMILY_NONISOTRIVIAL=true
GLOBAL_FIXED_GENUS_ONE_MODEL_DERIVED=false
```

Consequently

```text
S31_W01_GLOBAL_35EX19_USE=BLOCKED_NO_FIXED_MODEL,
S31_W01_FIBERWISE_ROUTING_ONLY=true.
```

One may apply the S31-W01 procedure to a **specific fixed `k` fiber** after writing and certifying explicit quartic-to-Weierstrass maps, denominator opens, and exceptional points. That would prove only a theorem for that fiber. It cannot by itself exclude all primitive Master-Hit source parameters.

A uniform family theorem or an exact theorem fixing `k` on every hypothetical counterexample would be a materially new input. Neither is supplied by the present identities.

## 6. Exact route freeze

The original selected candidate was

```text
E1-RECEIVER-SPECIFIC-GENUSONE-ELIMINATION.
```

The intended fixed-curve version is now frozen:

```text
CURRENT_RECEIVER_SPECIFIC_FIXED_GENUSONE_ROUTE
 = FROZEN_NONISOTRIVIAL_MOVING_SOURCE_PARAMETER.
```

This does **not** prove that elliptic-surface, uniform-family, higher-genus, or other global arithmetic methods are impossible. It only rejects promotion from the current receiver to one fixed elliptic curve.

## 7. New exact source-filtered paired-quartic hook

The fixed-fiber derivation omitted one condition when viewing `C_k` as a standalone rational curve: the recovered `t` must come from the second primitive source triple, hence

```text
s2^2 = 1-t^2
```

for rational `s2=V2/W2`.

Using `(T(u))`, define

```text
Z = s2*(k-u^2).
```

Then exactly

```text
Z^2
 = (k-u^2)^2 - 4*r^2*u^2
 = u^4 - 2*u^2 + k^2.                        (Dk)
```

Thus every actual full-receiver source point satisfies the simultaneous pair

```text
Y^2 = u^4 + 2*u^2 + k^2,
Z^2 = u^4 - 2*u^2 + k^2.                     (PAIR)
```

The first source circle supplies one further exact identity. Put

```text
sigma = 2*r*s1 = 2*U1*V1/W1^2.
```

Then

```text
k^2 + sigma^2 = 1.                            (KS)
```

Therefore `(PAIR)` can also be written

```text
Y^2 = (u^2+1)^2 - sigma^2,
Z^2 = (u^2-1)^2 - sigma^2.                    (PAIR-FACT)
```

and in particular

```text
Y^2-Z^2 = 4*u^2.                              (PAIR-DIFF)
```

This paired source-filter structure is not the fixed-curve plan that just failed: it simultaneously retains the second source-circle condition and couples the two quartic square covers. It is the materially new exact pattern exposed by the blocker.

No contradiction is claimed here.

## 8. Route decision and credit boundary

```text
CYCLE_ROUTE_STATUS=BLOCKED_NEW_PATTERN_ISOLATED
CYCLE_ACTIVE_RECEIVER=MASTER_HIT_PLUS_LMINUS_SQUARE_PLUS_LPLUS_SQUARE
FIXED_R_GENUS_ONE_QUARTIC_DERIVED=true
FIXED_R_QUARTIC_SMOOTH_GENUS_ONE=true
FIXED_R_FIBER_ADAPTER_PROVED=true
GENUS_ONE_J_INVARIANT_NONCONSTANT=true
GLOBAL_FIXED_GENUS_ONE_MODEL_DERIVED=false
CURRENT_RECEIVER_SPECIFIC_FIXED_GENUSONE_ROUTE=FROZEN_NONISOTRIVIAL_MOVING_SOURCE_PARAMETER
S31_W01_GLOBAL_35EX19_USE_BLOCKED=true
PAIRED_SOURCE_FILTER_QUARTICS_DERIVED=true
PAIRED_QUARTIC_CONTRADICTION_PROVED=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
