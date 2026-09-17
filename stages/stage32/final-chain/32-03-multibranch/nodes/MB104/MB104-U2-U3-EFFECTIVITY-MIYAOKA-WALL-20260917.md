# Stage32 MB104 — U2/U3 effectivity and Miyaoka wall — 2026-09-17

Status: **DISPLAYED RAY EFFECTIVE FOR EVERY l>=1 / SIMPLE MORI-NEF EXCLUSION IMPOSSIBLE / GENERAL MIYAOKA-YAU-SAKAI CURVE INEQUALITY DOES NOT CUT THE RAY / NO CLOSURE CREDIT**

## Scope

Work only with the retained displayed balanced genus-one ray

```text
D_l = 7l H - 4l sum_(p in Sigma) E_p,
|Sigma|=14,
l>=1,
```

on the smooth minimal resolution `S`, with retained identities

```text
H=K_S,
H^2=K_S^2=16,
H.E_i=0,
E_i^2=-2,
D_l^2=336l^2,
K_S.D_l=112l,
c2(S)=80.
```

No assertion is made here about irreducibility, the prescribed branch packet, normalization genus, or downstream effectivity credit.

## 1. U2: homogeneous cone tests cannot produce a large-l cutoff

The ray is exactly homogeneous:

```text
D_l = l D_1.
```

Therefore every purely numerical cone test of the form

```text
N.D_l < 0
```

for a fixed nef class `N`, or membership/nonmembership in a homogeneous effective/Mori cone, has sign independent of `l`. Such a test can exclude all positive multiples or none of them; it cannot by itself yield an asymptotic threshold `l>L`.

The stronger fact below shows that ordinary effectivity is not an obstruction at all for this displayed ray.

## 2. Exact Riemann–Roch effectivity for every l>=1

Noether's formula gives

```text
chi(O_S)=(K_S^2+c2(S))/12=(16+80)/12=8.
```

For `l>=1`,

```text
H.(K_S-D_l)
 = H.K_S - H.D_l
 = 16 - 112l
 < 0.
```

Since `H=K_S` is nef on the retained minimal surface, an effective divisor cannot have negative intersection with `H`. Hence

```text
H^0(S,O_S(K_S-D_l))=0.
```

By Serre duality,

```text
H^2(S,O_S(D_l))=0.
```

Riemann–Roch then gives

```text
chi(O_S(D_l))
 = chi(O_S) + (D_l.(D_l-K_S))/2
 = 8 + (336l^2-112l)/2
 = 168l^2-56l+8.
```

This is strictly positive for every `l>=1`. Because `h^2=0`,

```text
h^0(O_S(D_l))
 = chi(O_S(D_l)) + h^1(O_S(D_l))
 >= 168l^2-56l+8
 > 0.
```

Therefore

```text
|D_l| != empty   for every l>=1.
```

So the old restart question "is D_l effective for infinitely many l?" is resolved positively, indeed for all positive `l`, for this displayed ray.

This does **not** produce an irreducible carrier or a curve with the MB104 singularity/equality packet. The remaining wall moves strictly to irreducibility plus realization of the prescribed low-genus singular packet inside the nonempty linear system.

## 3. U3: Miyaoka's orbibundle curve inequality is numerically slack

Use Yoichi Miyaoka, *The Orbibundle Miyaoka-Yau-Sakai Inequality and an Effective Bogomolov-McQuillan Theorem*, Publ. RIMS 44 (2008), Theorem 1.3(i). For a surface of non-negative Kodaira dimension and an irreducible curve `C` of geometric genus `g`, for every real `0<=alpha<=1`,

```text
(alpha^2/2)(C^2+3CK-6g+6)
 -2alpha(CK-3g+3)
 +3c2(S)-K_S^2 >= 0.
```

Substitute the hypothetical MB104 genus-one carrier

```text
g=1,
C^2=336l^2,
CK=112l,
K_S^2=16,
c2(S)=80.
```

The inequality becomes

```text
F_l(alpha)
 = 168l(l+1) alpha^2 - 224l alpha + 224
 >= 0.
```

Its minimizing point is

```text
alpha_* = 2/(3(l+1)),
```

which lies in `[0,1]` for all `l>=1`. The exact minimum is

```text
F_l(alpha_*)
 = 224 - (224/3) l/(l+1)
 = 224(2l+3)/(3(l+1))
 > 0.
```

Thus the general Miyaoka-Yau-Sakai irreducible-curve inequality is satisfied with a uniform positive margin and gives no all-`l` contradiction and no finite large-`l` cutoff.

Miyaoka's stronger effective boundedness theorem for fixed geometric genus assumes

```text
K_S^2 > c2(S),
```

whereas here

```text
16 < 80.
```

Hence that boundedness theorem is not available on this surface.

## 4. Consequence for the replacement-theorem search

The following routes are now ruled out as standalone closures for the displayed ray:

```text
U2_FIXED_NEF_NEGATIVITY = BLOCKED_BY_HOMOGENEITY_AND_ACTUAL_EFFECTIVITY
U2_ORDINARY_EFFECTIVE_CONE_NONMEMBERSHIP = FALSE_FOR_THE_DISPLAYED_RAY
U3_GENERAL_MIYAOKA_YAU_SAKAI_CURVE_BOUND = NUMERICALLY_SLACK
```

The useful positive information is sharper than the previous Picard-integrality checkpoint:

```text
integral Picard class  ->  effective divisor class for every l>=1.
```

Accordingly, future MB104 work should not spend cycles trying to prove non-effectivity of `D_l`. It must attack one of the genuinely packet-sensitive statements:

1. no **irreducible** member of `|D_l|` can realize normalization genus one plus the balanced 14-node packet;
2. the packet forces a fixed component/decomposition despite nonemptiness of `|D_l|`;
3. a product-cover / degeneration / incidence invariant excludes the prescribed singularity passport uniformly;
4. a global theorem cuts the packet-specific superabundance, not the divisor class itself.

## Firewalls

- `displayed_ray_effective_for_all_l=true` means only nonemptiness of the complete linear system `|D_l|`.
- No irreducible MB104 carrier is constructed.
- No balanced packet is realized.
- No normalization-genus-one carrier is constructed or excluded.
- No finite degree window is proved.
- No receiver/effectivity-milestone/theorem/endpoint/merge/Perfect-Cuboid credit is granted.
