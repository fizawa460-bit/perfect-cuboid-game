# Stage15-6au — targeted literature audit for small-height points on the exact j=1728 twist family

Base: Stage15-6at in the current cycle. Stage15-6ar identified the exact congruent-number twist packet

\[
E_d:y^2=x^3-d^2x,
\qquad d=sf(2k\kappa),
\]

while 6as and 6at showed that a per-twist lower-height theorem and the remembered low-core size inequalities do not by themselves aggregate the norm core.

Stage15-6au asks a narrower question: is there an existing theorem that counts **twist parameters carrying a non-torsion point of unusually small height** with a fixed-power saving?

This is a **literature/theorem-species audit**.

## 1. The relevant theorem species exists

For a fixed elliptic curve

\[
E:y^2=x^3+Ax+B
\]

and squarefree quadratic twists `E_d`, define

\[
\log\eta_d(A,B)
=\min\{\hat h_{E_d}(P):P\in E_d(\mathbf Q)\setminus E_d(\mathbf Q)_{tors}\},
\]

with `eta_d=infinity` when the rank is zero.

Joachim Petit, *On the Number of Quadratic Twists with a Rational Point of Almost Minimal Height*, IMRN 2022, arXiv:2004.02500, studies

\[
\mathcal D_{A,B}(\alpha;X)
=\{d\le X:\ d\text{ squarefree},\ \eta_d(A,B)\le d^{1/8+\alpha}\}.
\]

For

\[
\boxed{0<\alpha<1/120,}
\]

Petit Theorem 1 proves an asymptotic formula for this set. The companion paper on average rank records the size explicitly as

\[
\boxed{\#\mathcal D_{A,B}(\alpha;X)\sim c(\alpha)X^{1/2}\log X.}
\]

This is exactly a half-power twist-family counting species, not merely an almost-all lower-height statement.

Primary sources:

- Joachim Petit, arXiv:2004.02500 / IMRN 2022.
- Joachim Petit, arXiv:2011.13195, Eq. (2.9), which quotes the above asymptotic.

## 2. Base-family match

Stage15 uses the fixed base curve

\[
E:y^2=x^3-x,
\]

so in Petit's notation

\[
A=-1,\qquad B=0.
\]

The cubic `x^3-x` is reducible. Petit's 2020 counting theorem is stated for a general fixed non-singular cubic and tracks the number `lambda_{A,B}` of irreducible factors; the later average-rank paper imposes irreducibility only for its own rank argument.

Thus the **counting theorem species** is structurally targeted at the correct fixed quadratic-twist setup. No sixth-power-free discriminant hypothesis analogous to the blocked Nara Theorem 1.1 is the issue here.

```text
PETIT_SMALL_HEIGHT_TWIST_SPECIES_MATCH=true
```

## 3. Why this theorem would be powerful if the Stage15 adapter succeeds

The Stage15 twist parameter satisfies

\[
d=sf(2k\kappa)\asymp k\kappa
\]

within an absolute factor two. On the small-coordinate-core branch,

\[
\kappa^2<ZW,
\qquad kZW\le2B,
\]

so

\[
k\kappa^2<2B.
\]

In particular the twist parameter remains polynomially bounded by the physical height, and in the crude whole branch one has `d<=B^O(1)`; in fact the exact product gives a natural `d=O(B)` scale.

Therefore a theorem counting relevant twist parameters by `X^(1/2+o(1))` is of the right magnitude to interact with the already-known Stage15 half-power numerator scale.

This observation is **not** yet a proof: the Stage15 quartic points must first be shown to satisfy Petit's small-height hypothesis on `E_d`.

## 4. Four mandatory adapters before application

### Gate A — explicit 2-covering map

For every charged quartic model

\[
C_{K,\kappa}:\ \kappa T^2=F_K(a,b),
\]

construct a rational degree-four covering map

\[
\pi_{K,\kappa}:C_{K,\kappa}\to E_d.
\]

The existence of a Jacobian is not enough; the map and its coefficient height must be controlled.

### Gate B — non-torsion image

Petit counts twists possessing a **non-torsion** rational point. Stage15 must prove that a counted physical quartic point supplies such a point under a fixed counting-compatible map, or isolate and count the torsion-image branch separately.

### Gate C — canonical-height upper bridge

Need an explicit implication of the form

\[
\text{Stage15 physical/product height}
\Longrightarrow
\eta_d\le d^{1/8+\alpha}
\]

for some fixed

\[
\alpha<1/120
\]

on the target residual branch.

A merely polynomial upper bound for the projective quartic height is insufficient. The exponent relative to `d` is the decisive datum.

### Gate D — packet multiplicity / pair count

Petit counts **twist parameters**, whereas Stage15 counts pairs of Gaussian/covering states. After fixing `d`, the split `k*kappa` and finite core/cell decorations cost only `B^o(1)` by 6ar, but the number of rational Stage15 points on those coverings must also be controlled.

Petit's proof itself contains a second-moment treatment of twists with two independent small points, which is relevant guidance, but it cannot be imported without matching the Stage15 covering coordinates and product-height weight.

## 5. AR-027 / measure verdict

This theorem is stronger for Stage15 purposes than an `almost all` statement because it directly counts the exceptional small-height twist family. Nevertheless the Stage15 host is weighted by two covering points and physical masks.

Therefore

```text
AR-027=ADAPTER_REQUIRED_NOT_AUTOMATICALLY_FAILED
```

The theorem is not rejected; its host measure must be matched.

## 6. Audit verdict

```text
AUDIT_STAGE=Stage15-6au
AUDIT_TARGET=SMALL_HEIGHT_QUADRATIC_TWIST_FAMILY_COUNT
AUDIT_VERDICT=NEW_GATE
PETIT_SMALL_HEIGHT_TWIST_SPECIES_MATCH=true
PETIT_ALPHA_RANGE=(0,1/120)
PETIT_TWIST_COUNT_SCALE=X^(1/2)*log(X)
STAGE15_EXACT_TWIST_PARAMETER_AVAILABLE=true
COVERING_MAP_ADAPTER_PROVED=false
NONTORSION_IMAGE_PROVED=false
CANONICAL_HEIGHT_UPPER_BRIDGE_PROVED=false
PACKET_MULTIPLICITY_BRIDGE_PROVED=false
PETIT_THEOREM_APPLIED_TO_STAGE15=false
```

`NEW_GATE` means: the theorem species is now sufficiently well matched that the next work should be an exact adapter, not another broad literature search.

## 7. Cycle stop

This is the natural stop for the current cycle.

The sequence of visible audit decisions was

```text
6ar  exact j=1728 twist identification            PASS
6as  Nara explicit twist-height theorem           BLOCK
6at  low-core size-memory sufficiency             BLOCK
6au  Petit small-height twist-family theorem       NEW_GATE
```

Thus the next substage is unambiguous:

```text
Stage15-6av
= construct/audit the explicit binary-quartic 2-covering map
  and derive the Stage15-projective-height -> canonical-height bridge.
```

No new external theorem should be searched before that adapter is attempted.

## 8. Frozen exit

```text
STAGE15_6_SUBSTAGE=6au
STAGE15_6AU_AUDIT=true
STAGE15_6AU_AUDIT_VERDICT=NEW_GATE
STAGE15_6AU_PETIT_THEOREM_SPECIES_MATCH=true
STAGE15_6AU_PETIT_HALF_POWER_TWIST_COUNT=true
STAGE15_6AU_PETIT_STAGE15_ADAPTER_PROVED=false
STAGE15_6AU_NEXT=Stage15-6av_EXPLICIT_2COVERING_CANONICAL_HEIGHT_ADAPTER
STAGE15_6AU_EXIT=PETIT_HALF_POWER_TWIST_THEOREM_ADAPTER_READY
```