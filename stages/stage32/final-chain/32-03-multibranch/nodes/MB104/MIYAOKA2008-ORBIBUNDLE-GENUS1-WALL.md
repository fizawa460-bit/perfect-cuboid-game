# Stage32 MB104 — Miyaoka 2008 orbibundle genus-one wall

Status: **RETAINED PUBLISHED-INEQUALITY ADAPTER / STANDARD ALL-SINGULARITY ORBIBUNDLE ROUTE DOES NOT BOUND l / NO CLOSURE / MB104 INCOMPLETE / NO CREDIT**

## Purpose

The active balanced16 frontier has exhausted the known zero-quartic fixed-component route on the surviving `864` supports.  A natural next attempt is to use a singular-curve Bogomolov--Miyaoka--Yau inequality directly on a hypothetical integral normalization-genus-one member

```text
C_l in |D_l|,
D_l = 7l H - 4l sum_(p in Sigma) E_p,
l>=1.
```

This note records that the standard one-curve orbibundle inequality of Miyaoka (2008) is **automatically satisfied** on this ray and therefore gives no upper bound on `l`.

## Published source

Yoichi Miyaoka,
*The Orbibundle Miyaoka--Yau--Sakai Inequality and an Effective Bogomolov--McQuillan Theorem*,
Publ. Res. Inst. Math. Sci. **44** (2008), no. 2, 403--417,
DOI `10.2977/PRIMS/1210167331`.

For a minimal smooth complex projective surface `X` of general type, an irreducible curve `C` of geometric genus `g`, and rational `alpha in [0,1]`, Theorem 1.3 gives

```text
(alpha^2/2) * (C^2 + 3 C.K_X - 6g + 6)
 - 2 alpha * (C.K_X - 3g + 3)
 + 3 c2(X) - K_X^2
>= 0.
```

Only this displayed inequality is imported here.

## Cuboid-surface substitution

The retained canonical source adapter gives on the minimal resolution `S`

```text
K_S = H,
K_S^2 = 16,
chi(O_S)=8,
c2(S)=12*8-16=80.
```

For the uniform P5 ray,

```text
C_l^2 = 336 l^2,
K_S.C_l = 112 l,
g=1.
```

Hence Miyaoka's left-hand side becomes

```text
f_l(alpha)
 = 168 l(l+1) alpha^2
   - 224 l alpha
   + 224.
```

## Exact minimization

For every `l>=1`, the quadratic coefficient is positive.  Its unconstrained minimum occurs at

```text
alpha_l = 2 / (3(l+1)).
```

This satisfies

```text
0 < alpha_l <= 1/3 < 1,
```

so it is also the minimum on the allowed interval `[0,1]`.

Substitution gives

```text
min_[0,1] f_l
 = 224 - (224/3) * l/(l+1)
 = 224(2l+3)/(3(l+1))
 > 0.
```

Therefore the Miyaoka 2008 orbibundle inequality is strictly satisfied for every `l>=1`.

## Consequence

The standard single-curve orbibundle BMY route supplies **no** bound on `l` for the displayed uniform genus-one P5 ray.  In particular, it cannot close any of the surviving support orbits

```text
0000770000ff   size 48,
00007b0000ff   size 48,
000707000f0f   size 768.
```

This is compatible with the numerical regime

```text
K_S^2 = 16 < c2(S)=80.
```

Miyaoka's uniform canonical-degree consequence in the same paper requires the opposite strict inequality `K_X^2>c2(X)`, so that corollary is unavailable here.

This negative result does **not** rule out a stronger log-boundary argument involving the fourteen exceptional curves, nor a refinement that charges singularity/conductor data.  Those are genuinely different inputs and remain live.

## Relation to the retained Lu--Miyaoka leaf

The retained Lu--Miyaoka 1995 adapter yields the nontrivial necessary condition

```text
n_ordinary_node_or_triple(C_l) >= max(0,112l-224).
```

The 2008 one-curve orbibundle inequality does not improve this into an `l`-bound.  Any further progress must use additional structure: the exceptional boundary, conductor/branch distribution, fibration data with a global tangent condition, or another source-supported inequality.

## Firewalls

- This is an adapter to a published inequality, not a new BMY theorem.
- No support orbit is closed.
- No bound on `l` is proved.
- No irreducible genus-one carrier is constructed or excluded on the `864` survivors.
- The possible log-boundary route `C_l + sum E_i` is not claimed here.
- MB104, receiver, theorem, endpoint, and Perfect-Cuboid credit remain open/zero.
- No merge authorization.
