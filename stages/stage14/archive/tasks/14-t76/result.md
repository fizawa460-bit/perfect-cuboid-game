# Stage14-t76 — clean-kappa primitive cover root line inside the balanced small-angular-gcd block

## Purpose

Merged Stage14-t75 leaves one genuinely two-variable physical block:

```text
SharedUSmallOddKappaFixedTagSmallAngularGcdBalancedShortCoverTypeIIDispersionEnergy.
```

The cover coordinates are

```text
A=b-a,  B=b+a,
r=q-p,  t=q+p,
```

with

```text
gcd(odd(A),odd(B))=1,
gcd(odd(r),odd(t))=1,
g=gcd(odd(A*B),odd(r*t)),
c/odd(h)=R0*T0,
```

and the balanced small-`g` branch retains the t74/t75 short-cover and hyperbola inequalities.

Stage14-t76 connects the fixed squareclass/tag data `(kappa,beta)` directly to this cover pair. The main point is that the part of odd `kappa` on which the cover/direction coordinates fail to be units is not a new bad modulus: it is contained exactly in the already-exposed angular gcd `g`. After removing that support, the entire remaining odd squareclass becomes a primitive projective root-line modulus for `(r,t)`.

No additional whole-family exponent saving is claimed here. The current strongest merged theorem is Stage14-X11:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34.
```

---

## 1. Imported t75 packet

Fix

```text
(U,epsilon,k,h,kappa,beta),
beta=gcd(kappa,v),
alpha=kappa/beta.
```

For one physical state write

```text
A=b-a,
B=b+a,
r=q-p,
t=q+p,
K=oddpart(kappa).
```

Merged t71 gives the Kummer components

```text
L1=A*t-B*r,
L2=B*t-A*r,
L3=A*t+B*r,
L4=B*t+A*r,

s=(L1*L2)/(L3*L4),
kappa=sf(L1*L2*L3*L4).
```

Merged t72/t73 give the fixed-tag signed rule: for every odd prime `p|K`,

```text
p|alpha  => Pplus == +Pminus (mod p),
p|beta   => Pplus == -Pminus (mod p).
```

Merged t75 gives

```text
g=gcd(odd(A*B),odd(r*t))
```

and the exact two-column factorization of `g` and `c`.

---

## 2. All nonunit squareclass support is already inside `g`

Define

```text
K_bad = gcd(K, A*B*r*t).
```

Because `K` is squarefree, it is enough to work primewise. Let an odd prime `p|K`.

If `p|A*B` but `p∤r*t`, then, since the odd parts of `A,B` are coprime, exactly one of `A,B` is zero modulo `p` and both `r,t` are units. Each of `L1,L2,L3,L4` is then nonzero modulo `p`, contradicting `p|sf(L1L2L3L4)`.

Likewise, if `p|r*t` but `p∤A*B`, exactly one of `r,t` is zero modulo `p` and all four Kummer components are nonzero modulo `p`, again a contradiction.

Hence

```text
p|K and p|A*B*r*t
    => p|A*B and p|r*t
    => p|g.
```

The reverse implication on the intersection with `K` is tautological. Therefore

```text
boxed:
K_bad = gcd(K,g).
```

Put

```text
K_clean = K/K_bad.
```

Then exactly

```text
boxed:
gcd(K_clean,A*B*r*t)=1.
```

Moreover

```text
K_bad <= g,
K_clean = K/gcd(K,g) >= K/g.
```

Thus after t75 has placed `g` on a small dyadic scale, any fixed-power squareclass support not already paid for by `g` survives as a unit modulus on the cover chart.

```text
KAPPA_NONUNIT_SUPPORT_EQUALS_KAPPA_INTERSECTION_ANGULAR_GCD=true
CLEAN_KAPPA_COPRIME_TO_DIRECTION_AND_COVER_COORDINATES=true
CLEAN_KAPPA_LOWER_BOUND=K/g
```

---

## 3. Fixed denominator tag determines the sign of the cover root line

Write

```text
alpha_clean = gcd(oddpart(alpha),K_clean),
beta_clean  = gcd(oddpart(beta), K_clean).
```

Then

```text
alpha_clean*beta_clean=K_clean,
gcd(alpha_clean,beta_clean)=1.
```

The exact t74 balance is

```text
h*r*t*Pplus = epsilon*delta*A*B*(Pminus/ell).
```

Using

```text
Pminus=ell*(Pminus/ell),
r^2+t^2=2*k*delta,
h*k=epsilon*m,
A^2+B^2=2*ell*m,
```

and the fixed-tag congruence `Pplus == lambda Pminus (mod p)`, one obtains for every odd `p|K_clean`

```text
A*B*(r^2+t^2) == lambda*(A^2+B^2)*r*t (mod p),
```

where

```text
lambda=+1 for p|alpha_clean,
lambda=-1 for p|beta_clean.
```

Because all four coordinates are units modulo `K_clean`, this factors into actual primitive root lines:

```text
p|alpha_clean:
    (A*t-B*r)(B*t-A*r) == 0 (mod p),

p|beta_clean:
    (A*t+B*r)(B*t+A*r) == 0 (mod p).
```

Equivalently, with `r` invertible modulo `p`,

```text
p|alpha_clean:
    t/r in { B/A, A/B } (mod p),

p|beta_clean:
    t/r in {-B/A,-A/B} (mod p).
```

The denominator tag `beta` therefore fixes the sign. The only residual primewise choice is which reciprocal direction root is used.

By CRT, after at most

```text
2^omega(K_clean)=B^o(1)
```

orientation choices, the whole clean squareclass becomes one projective line

```text
boxed:
t == rho*r (mod K_clean),
gcd(r,K_clean)=1.
```

```text
FIXED_BETA_DETERMINES_CLEAN_KAPPA_ROOT_SIGN=true
CLEAN_KAPPA_RECIPROCAL_DIRECTION_CHOICES_PER_PRIME_AT_MOST=2
CLEAN_KAPPA_CRT_PROJECTIVE_ROOT_LINE_PROVED=true
CLEAN_KAPPA_ROOT_ORIENTATION_MULTIPLICITY=Bo1
```

---

## 4. Elementary primitive root-line spacing closes the large clean-`K` cover branch

Fix a direction `(A,B)`, a clean-root orientation `rho`, and dyadic cover ranges

```text
r ~ R,
t ~ T,
gcd(r,t) in {1,2}.
```

Two distinct normalized primitive slopes on the same projective root line satisfy

```text
K_clean | (t1*r2-t2*r1).
```

If the determinant vanishes, the two slopes are equal and the condition `gcd(r,t)<=2` leaves only `O(1)` representatives. Otherwise Farey spacing in the dyadic rectangle gives

```text
#cover pairs
  <= (1 + R*T/K_clean) B^o(1).
```

Since

```text
K_clean >= K/g,
```

one also has the weaker but useful bound

```text
#cover pairs
  <= (1 + g*R*T/K) B^o(1).
```

Therefore the branch

```text
K_clean >= R*T*B^(-o(1))
```

is near-linear after the already-fixed packet/root orientation summations. Equivalently, it is enough that

```text
K >= g*R*T*B^(-o(1)).
```

This is a new use of `kappa`: t72 compared `K` with the Cayley-pair area `Pplus*Pminus`; t76 compares its clean part with the much shorter physical cover rectangle.

```text
LARGE_CLEAN_KAPPA_COVER_BRANCH_CLOSED_BY_ELEMENTARY_ROOTLINE_SPACING=true
ROOTLINE_COVER_COUNT=(1+R*T/K_clean)*Bo1
```

---

## 5. What genuinely remains

After t75 and t76, the genuinely two-variable branch may be assumed to satisfy simultaneously

```text
small angular g,
balanced r,t,
K_bad=gcd(K,g),
K_clean=K/K_bad,
K_clean < R*T*B^o(1),
```

with

```text
gcd(K_clean,A*B*r*t)=1,
t == rho*r (mod K_clean),
```

for one of `B^o(1)` fixed-tag reciprocal root orientations, together with all physical masks

```text
ell canonical prime,
ell^2>4B,
ell*c<2B,
ell*g*c<2B,
r,t<sqrt(ell),
h*ell*(r^2+t^2)<=4B,
ell*delta<=Y_U,
c/odd(h)=R0*T0,
(R0,T0)=1.
```

Because the projective modulus is now explicitly too small to close by spacing, the surviving problem is a genuine balanced Type-II average over canonical directions and short primitive cover pairs, not an unresolved algebraic adapter.

Define the post-t76 receiver

```text
SharedUSmallOddKappaFixedTagSmallAngularGcdBalancedCleanKappaDeficientPrimitiveCoverTypeIIDispersionEnergy.
```

It is not proved here.

---

## 6. Relation to merged tH20 and tH21 decision

Merged tH20 explicitly advised the order

```text
1. exhaust exact angular divisor geometry in g,q-p,q+p;
2. isolate the residual balanced bilinear sum with its exact phase/kernel;
3. only then test bilinear/dispersion technology.
```

Stages t75 and t76 now complete steps 1 and 2 at the arithmetic receiver level. In particular, t76 supplies the missing exact projective root kernel and quantifier order.

Therefore a new auxiliary audit is now justified.

```text
TH21_NEEDED=true
TH21_REQUESTED_OBJECT=SmallAngularGcdBalancedCleanKappaCanonicalPrimePrimitiveCoverTypeIIDispersion
```

The t-route does not block on tH21; t77 should continue exact reduction of the deficient-modulus branch while tH21 independently audits available Type-II/dispersion inputs.

---

## 7. Shared exponent

The current strongest merged whole-family theorem is Stage14-X11:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34
```

Stage14-t76 proves no additional whole-family power saving.

---

## Locked boundary

```text
STAGE14_T76=COMPLETE_CLEAN_KAPPA_COVER_PROJECTIVE_ROOTLINE_AND_DEFICIENT_TYPEII_REDUCTION
MERGED_T75_IMPORTED=true
MERGED_TH20_IMPORTED=true
MERGED_X11_GLOBAL_19_34_LEDGER_IMPORTED=true
KAPPA_NONUNIT_SUPPORT_EQUALS_KAPPA_INTERSECTION_ANGULAR_GCD=true
CLEAN_KAPPA_COPRIME_TO_DIRECTION_AND_COVER_COORDINATES=true
CLEAN_KAPPA_LOWER_BOUND=K/g
FIXED_BETA_DETERMINES_CLEAN_KAPPA_ROOT_SIGN=true
CLEAN_KAPPA_RECIPROCAL_DIRECTION_CHOICES_PER_PRIME_AT_MOST=2
CLEAN_KAPPA_CRT_PROJECTIVE_ROOT_LINE_PROVED=true
LARGE_CLEAN_KAPPA_COVER_BRANCH_CLOSED_BY_ELEMENTARY_ROOTLINE_SPACING=true
SHARED_U_SMALL_ODD_KAPPA_FIXED_TAG_SMALL_ANGULAR_GCD_BALANCED_CLEAN_KAPPA_DEFICIENT_PRIMITIVE_COVER_TYPEII_DISPERSION_ENERGY_PROVED=false
TH21_NEEDED=true
TH21_REQUESTED_OBJECT=SmallAngularGcdBalancedCleanKappaCanonicalPrimePrimitiveCoverTypeIIDispersion
T_ROUTE_BLOCKED_WAITING_FOR_TH21=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34
T76_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t77
```
