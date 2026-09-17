# Stage32 MB104 — U11 GFU equality-face wall — 2026-09-17

Status: **PACKET-SPECIFIC NEGATIVE PREFLIGHT / BASE GFU AT EXACT DEGREE ZERO / ENHANCED GFU STRICTLY POSITIVE / NO CREDIT**

## Scope

Work only on the dangerous balanced equality ray

```text
Sigma = 000707000f0f,
|Sigma|=14,
g=1,
d=112l,
D_l.E_p=8l for p in Sigma,
E.D_l=112l,
l>=1.
```

This note asks whether Garcia-Fritz--Urzua (GFU) can be strengthened on the exact equality face by combining the published cuboid differentials with the retained MB104 packet.

## 1. Published GFU theorem lands exactly on degree zero

GFU Theorem 3.1 uses the section induced by the standard symmetric differential on the base and proves omega-integrality when

```text
-deg(C) + (E.C') + 4g(C) - 4 < 0.
```

For the current balanced genus-one ray,

```text
-deg(C) + (E.C') + 4g(C)-4
= -112l + 112l + 0
= 0.
```

Therefore the published theorem does **not** force omega-integrality on this ray.  Degree zero would become useful only after a separate argument proves that the induced section on the elliptic normalization has at least one zero; a nonzero section of a degree-zero line bundle is nowhere vanishing.

So the candidate re-entry condition is precise:

```text
GFU equality face + one source-locked surplus zero
=> omega-integral carrier.
```

No such surplus zero is present in Theorem 3.1 itself.

## 2. The four enhanced GFU differentials are strictly positive on 000707

GFU Lemma 3.4 introduces four sections omega_i.  Let E_i be the sum of exceptional divisors above the 24 cuboid nodes whose image belongs to the corresponding curve C_i, and E'_i the complementary 24 exceptional divisors.

Under the standard cuboid-coordinate identification

```text
GFU (x0,x1,x2,x3) = Stage32 (a1,a2,a3,c),
```

comparison of the cuboid equations identifies the remaining GFU face-diagonal coordinates with the Stage32 b-coordinates up to the irrelevant permutation.

Replaying the retained canonical 48-node model on

```text
Sigma={P0,P1,P2,P3,P8,P9,P10,P11,P24,P25,P26,P32,P33,P34}
```

gives the exact numbers of supported nodes lying in E_i:

```text
#(Sigma cap E_0) = 7,
#(Sigma cap E_1) = 7,
#(Sigma cap E_2) = 8,
#(Sigma cap E_3) = 6.
```

Hence the complementary supported-node counts are

```text
#(Sigma cap E'_i) = (7,7,6,8).
```

Every supported exceptional contributes `8l`, so

```text
D_l.E'_i = (56l,56l,48l,64l).
```

For genus one, `deg Sym^2 Omega_E^1=0`.  The line bundle in GFU Lemma 3.4 is numerically `O(E'_i)` before restriction to the normalization, so the four enhanced sections have exact restriction degrees

```text
56l, 56l, 48l, 64l.
```

All are strictly positive for every `l>=1`.  Thus the four-differential refinement does not turn the current packet into a negative- or zero-degree automatic-integrality case.

The companion verifier

```text
verify_mb104_u11_gfu_equality_face.py
```

replays the 48-node model, the `000707` support, and these degree coefficients exactly.

## 3. Why the retained finite local-jet data do not supply the missing surplus zero

At an A1 point arising over the crossing of two omega-integral branch fibres, choose base local coordinates `X,Y` so the fibres are `X=0` and `Y=0`.  The standard GFU base differential is locally a unit multiple of the mixed symmetric tensor

```text
dX dY
```

up to terms forced by omega-integrality of the two coordinate axes.

On the standard A1 resolution chart

```text
X=s,
Z=s t,
Y=s t^2,
```

the leading exceptional-direction coefficient of the mixed term is a nonzero polynomial in the landing coordinate `t`; in particular generic finite nonzero landing directions do not force an extra zero after the minimal A1 pole/vanishing balance is accounted for.

This matches the retained MB104 local walls:

- FSM-minimal branches have a free exceptional landing parameter;
- the dangerous packet has `8l` pairwise distinct nonzero landing keys at each supported node;
- any fixed finite order-two principal-part portfolio has only finitely many exceptional directions on which an additional cancellation occurs;
- the geometric field is infinite, so the retained local data alone allow all `8l` directions to avoid any prescribed finite root set.

Therefore the currently retained BTVA/GFU order-two local information does not supply the missing universal surplus zero on the GFU degree-zero section.

This is a **formal local non-forcing statement**, not a construction of a global carrier.

## 4. Route verdict

The following shortcut is not available:

```text
GFU degree = 0
+ balanced 14-node packet
=> omega-integral.
```

Nor do the four GFU enhanced differentials improve the sign: their exact genus-one degrees are all positive.

U11 is therefore classified as

```text
BLOCKED_WITH_CURRENT_ORDER2_DATA.
```

Re-entry requires genuinely new global information that forces a surplus zero of the degree-zero GFU section, for example:

1. a global relation on the exceptional landing directions that forces at least one branch into the GFU cancellation divisor;
2. a higher-order differential whose exceptional valuation is strictly stronger than the current minimal A1 compensation;
3. a packet-sensitive divisor/monodromy identity implying that the degree-zero GFU line on the elliptic normalization is nontrivial or that its section must vanish;
4. a new theorem combining GFU and BTVA beyond the published finite order-two principal-part data.

Without such an input, U11 reduces to the already-retained finite-jet/global-landing wall and should not be restarted as a fresh route.

## Sources

- N. Garcia-Fritz and G. Urzua, *Families of explicit quasi-hyperbolic and hyperbolic surfaces*, Math. Z. 296 (2020), arXiv:1804.07671, especially Theorem 3.1, Lemma 3.4 and Theorem 3.5.
- Retained Stage32 canonical 48-node model and `000707` support decoder from the archived MB104 exact head `ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11`.
- Retained `BTVA-13FORM-PRINCIPAL-PART.md` and `FINITE-JET-MULTIPLICITY-SATURATION-WALL.md` for the finite order-two landing-direction firewall.

## Firewalls

```text
U11_closes_000707=false
GFU_base_degree_negative=false
GFU_base_degree_zero=true
gfu_surplus_zero_proved=false
enhanced_GFU_negative_or_zero=false
MB104_complete=false
finite_degree_window_proved=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
