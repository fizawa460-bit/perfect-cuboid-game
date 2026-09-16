# Stage32 MB104 — size-48 CM inert-7 obstruction

Status: **RETAINED GLOBAL NONREALIZABILITY OF THE UNIFORM MINIMAL-BRANCH PACKET / BOTH SIZE-48 BALANCED ORBITS REMOVED FROM THE MB104 EQUALITY-PACKET FRONTIER / UNIFORM DIVISOR CLASS WITHOUT THE BRANCH PACKET NOT EXCLUDED / MB104 INCOMPLETE / NO CREDIT**

## Scope

This leaf treats the two current size-48 balanced support orbits

```text
0000770000ff,
00007b0000ff.
```

For both masks the exact node-type quotient leaf gives

```text
|Sigma|=14,
all supported nodes have one singular stabilizer type s,
D_l=7lH-4l sum_(p in Sigma)E_p,
d=112l.
```

The present contradiction is conditional on an actual carrier realizing the retained **uniform MB104 minimal-branch packet**

```text
r_i=M_i=8l at every supported node,
all branches have m=1,
r_odd=R8=M=d=112l.
```

It is not a statement that every irreducible divisor in the Picard class `D_l` is impossible if a different exceptional branch partition is allowed.

## 1. Equality rigidity and the one-type quotient

Assume such an integral normalization-genus-one carrier exists. Let

```text
E = normalization of the downstairs carrier.
```

The retained Beauville equality-rigidity leaf gives a connected component

```text
Z subset C8 x C8
```

of the normalized product-cover pullback, with component degree

```text
e in {1,2,4}
```

over the connected Beauville pullback. Its two projections

```text
f1,f2: Z -> C8
```

are finite etale covers of the same degree

```text
n=14*e*l.
```

Let `K<=G` be the stabilizer of `Z`. Then

```text
|K|=2e,
E=Z/K.
```

Because every supported branch has the same singular type `s`, the involution `s` lies in `K` and fixes the product-cover points above every one of the `112l` supported normalization branches.

Each branch point of `E` with inertia `<s>` lifts to

```text
|K|/2=e
```

points of `Z` fixed by `s`. There are no additional `s`-fixed points on `Z`: a fixed point descends to a box node of type `s`, and the uniform packet has no exceptional support outside `Sigma`. Therefore

```text
#Fix_Z(s)=112*e*l.
```

On the other hand equality rigidity gives

```text
2g(Z)-2=e*d=112*e*l.
```

Riemann--Hurwitz for

```text
Z -> B1:=Z/<s>
```

therefore reads

```text
112el = 2(2g(B1)-2)+112el,
```

so

```text
g(B1)=1.
```

## 2. Two equal-degree isogenies to the fixed CM elliptic quotient

For the singular type `s`, the published Beauville/Kummer source adapter identifies the factor quotient

```text
E0=C8/<s_factor>
```

(up to the retained `S3` conjugacy of the three node types) with the elliptic quotient

```text
E0: y^2=x^3-x,
j(E0)=1728,
End^0(E0)=Q(i).
```

Since `f1,f2` are `s`-equivariant, they descend to

```text
phi1,phi2: B1 -> E0.
```

Quotienting source and target by the same order-two involution does not change the degree, hence

```text
deg(phi1)=deg(phi2)=n=14*e*l.
```

Both source and target have genus one, so after choosing origins and translating the target the two maps are isogenies. Translation does not affect degrees or the generic degree of the pair map.

## 3. Inert prime `7` forces a common kernel

Write the translated isogenies as

```text
alpha1,alpha2:B1 -> E0.
```

In the isogeny category put

```text
nu = alpha2 * alpha1^{-1} in End^0(E0)^* = Q(i)^*.
```

Equal degrees give

```text
Norm_Q(i)/Q(nu)=deg(alpha2)/deg(alpha1)=1.
```

The rational prime `7` is inert in `Q(i)`. Therefore the `7`-adic valuation of a norm-one element is zero, and

```text
nu in Z_7[i]^*.
```

Thus `nu` acts invertibly on the `7`-divisible group of `E0`. On `7`-primary torsion,

```text
alpha2 = nu alpha1
```

implies

```text
ker(alpha1)[7^infinity] = ker(alpha2)[7^infinity].
```

But

```text
7 | deg(alpha1)=14el.
```

Hence this common `7`-primary kernel is nontrivial. Let `J` be a subgroup of order `7` in it. The pair homomorphism

```text
Phi=(alpha1,alpha2): B1 -> E0 x E0
```

factors through `B1/J`. Consequently the generic degree of `Phi` onto its image is divisible by `7`.

After composing with the fixed finite quotient

```text
E0 x E0 -> (E0 x E0)/H,
H ~= (Z/2)^2,
```

the generic degree is the generic degree of `Phi` multiplied by the generic degree of its image curve under the quotient. Therefore it remains divisible by `7`.

## 4. The box/Kummer diagram says the same generic degree is a power of two

For the matching coordinate sign involution `sigma` on the box variety, the published source gives

```text
(E0 x E0)/H ~= B/sigma.
```

The map induced by `(phi1,phi2)` is therefore the same modular quotient map as the geometric composition

```text
B1=Z/<s> -> Z/K=E -> C subset B -> B/sigma.
```

The first arrow has degree

```text
[K:<s>]=e.
```

The normalization map `E->C` has generic degree one. For an involution quotient, the restriction

```text
C -> image(C in B/sigma)
```

has generic degree either `1` or `2`: it is `1` when the generic `sigma`-orbit meets `C` once (including the pointwise-fixed case), and `2` only when `sigma` preserves `C` nontrivially.

Therefore the generic degree of

```text
B1 -> B/sigma
```

is exactly one of

```text
e, 2e,
```

hence belongs to

```text
{1,2,4,8}.
```

It is a power of two and is not divisible by `7`.

This contradicts the common inert-`7` kernel conclusion of the previous section.

## Conclusion

No actual normalization-genus-one carrier can realize the retained uniform minimal-branch equality packet on either size-48 balanced support orbit, for any

```text
l>=1.
```

Thus the MB104 equality-packet frontier loses both size-48 orbits:

```text
48+48+768 -> 768.
```

The only current balanced support orbit still compatible with the full uniform minimal-branch packet is

```text
000707000f0f   size 768.
```

This is stronger than the previous size-48 quotient/isogeny classification: the CM field and the inert prime `7` prevent the required pair of factor isogenies from descending through the box/Kummer quotient.

## Important scope firewall

- This leaf excludes the **MB104 dangerous packet** `r_odd=R8=M=d` on the two size-48 supports.
- It does **not** prove that the Picard class `D_l` has no irreducible genus-one member with a different exceptional multiplicity/branch partition.
- Therefore the geometric support population for arbitrary members of `|D_l|` is not silently changed from `864`; only the active MB104 equality-packet population drops to `768`.
- Arbitrary unequal exceptional coefficients remain open.
- `000707000f0f`, genus-one P6, genus-zero P6, MB104, receiver, theorem, endpoint, and Perfect-Cuboid credit remain open/zero.
- No merge authorization.
