# Stage32 post1648AP — factor-pair birational conductor demand

Scratch-only necessary-condition adapter. This leaf combines the two AM/AO factor maps simultaneously. It proves that any hypothetical integral geometric-genus-1 V6 carrier must map birationally to a very singular bidegree `(81,105)` curve in `P1 x P1`, and records the exact conductor-length demand. It does not construct or exclude such a carrier and grants no MAIN theorem/receiver/route/endpoint credit.

## Parent locks

- AO finalized scratch head: `aa57ac29404bae75f93aadcd4e134cba9eb91563`.
- AO canonical SHA256: `39e217c7223732b1834b7e9b96b4361807227f823a5624842a97eddf71390378`.
- AM canonical SHA256: `184debdb65c679242fadcc1e1ca176faf720c651b67f09368bc45c14dabb44c8`.
- AN canonical SHA256: `fc2568ae2cb6df0c0da319950a7e5b8edb7b9e356812c2f3d86c575593883a29`.

## Source quotient

Primary geometry remains Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), DOI `10.1307/mmj/1480734014`.

Theorem 2.4 and Section 2 source-lock

`C8 = H*/Gamma[8]`,
`G = Gamma[4]/Gamma[8] ~= (Z/2)^3`,
`B = (C8 x C8)/G_diag`.

AO source-locks `Z=C8/G=X(4)` as genus zero. The two factor quotient maps combine to

`Phi : B -> Z x Z`.

Upstairs, `C8 x C8 -> Z x Z` is the quotient by `G x G`, while `B` has already divided by the diagonal copy of `G`. Hence on the generic free locus `Phi` is the residual quotient by

`(G x G)/G_diag ~= G`

and has generic degree 8.

## Birationality of the factor-pair map

Let `C` be a hypothetical integral V6 carrier and let `D=Phi(C)`.

For an irreducible curve under a finite group quotient, the generic degree `delta` of the restriction to its image is the quotient of its component stabilizer by the generic point stabilizer. Therefore `delta` divides the group order, and here

`delta | 8`.

The two coordinate maps factor through `C -> D`. AM/AO give their degrees, unordered, as 81 and 105. Therefore

`delta | gcd(81,105)=3`.

Consequently

`delta | gcd(8,3)=1`,

so

`delta=1`.

Thus the factor-pair map is birational on every hypothetical integral V6 carrier. Equivalently, such a carrier has trivial generic stabilizer under the residual factor group `G`.

## Image arithmetic genus

Since `C -> D` is birational, `D` has bidegree `(81,105)` in `Z x Z ~= P1 x P1` (up to swapping the two factors).

For an integral bidegree `(a,b)` curve in `P1 x P1`,

`p_a=(a-1)(b-1)`.

Hence

`p_a(D)=(81-1)(105-1)=80*104=8320`.

The normalization is the same genus-one curve as the normalization of `C`, so the total delta defect of the image is

`delta(D)=8320-1=8319`.

On the resolved box surface, the V6 class has

`C^2=758`, `K.C=186`,

hence

`p_a(C)=1+(758+186)/2=473`

and the hypothetical genus-one normalization requires

`delta(C)=473-1=472`.

The proper birational restriction from the strict transform of `C` to `D` is finite because no component of the integral V6 curve is exceptional and both factor degrees are positive. For a finite birational morphism of integral projective curves,

`0 -> O_D -> f_* O_C -> Q -> 0`

gives

`length(Q)=p_a(D)-p_a(C)`.

Therefore the factor-pair quotient/contraction must contribute the exact additional conductor length

`8320-473 = 7847`.

Equivalently,

`8319-472 = 7847`

units of image singularity defect are not already present as intrinsic singularity defect of the strict-transform V6 curve.

## Meaning of the new obligation

This is a global necessary condition, not an exclusion. The next load-bearing interface is now concrete:

`residual G action on the retained Picard/V6 class`
`-> intersections C . gC and exceptional contraction data`
`-> upper/lower bound for the conductor length created by Phi`
`-> compare with required 7847`.

AK already showed the full V6 class stabilizer is trivial, which is compatible with the birationality proved here; AP does not count that agreement as additional closure.

## Firewalls

- Scratch only; shared `MAIN-STATE.json` and Stage32 authority remain unchanged.
- `Q602_excluded=false`.
- `O210_excluded=false`.
- `O212_plus_advance_allowed=false`.
- `7847` is a necessary conductor-length demand, not proof that such conductor is attainable or impossible.
- No receiver, route, theorem, endpoint, or perfect-cuboid credit.
