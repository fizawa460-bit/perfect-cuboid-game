# Stage33-07 elementary index-512 glue: exact structural reduction

This note records the proof behind `certify_elementary_index512_structural_reduction.py`. It is a reduction only; it does not identify the actual endpoint glue and does not release Stage33-08.

Let

`A0 = (Z/8)^10 ⊕ (Z/16)^4`, `V=A0[2] ≅ F2^14`,

and let `H ⊂ V` be an elementary isotropic subgroup of order `2^9`. Put `Q=H^⊥/H`. Write `V=X⊕Y`, where `X=F2^10` comes from the ten `Z/8` coordinates and `Y=F2^4` from the four `Z/16` coordinates. Set

`S=H∩Y`, `s=dim S`, `P=pr_X(H)`, and `r=dim(P∩P^⊥)` for the ordinary binary dot product on `X`.

## 1. Target invariant factors

The annihilator has index `|H|=2^9` in `A0`, so `|Q|=2^(46-9-9)=2^28`.

For `Q[2]`, a class killed by two has a representative `x` with `2x∈H`. Every such half of an order-two element has even residue in every `Z/8` and `Z/16` coordinate, hence lies automatically in `H^⊥`. Multiplication by two has kernel `A0[2]` of order `2^14`; therefore

`|Q[2]| = |H|·2^14 / |H| = 2^14`.

For `Q[4]`, write `h=4x∈H`. In a `Z/8` coordinate, the parity of `x` is exactly the corresponding binary coordinate of `h`; in a `Z/16` coordinate, the parity is zero. Thus `x∈H^⊥` exactly when `pr_X(h)∈P^⊥`. The allowed `h` form the inverse image of `P∩P^⊥` under `H→P`, whose kernel is `S`. Hence there are `2^(s+r)` allowed `h`. Since `|A0[4]|=2^28`,

`log2 |Q[4]| = 28 + s + r - 9 = 19+s+r`.

Finally, for `x∈H^⊥`, multiplication by eight kills all `Z/8` coordinates and records only the parity of the four `Z/16` coordinates. The set of possible `Y` parities of `H^⊥` is `S^⊥`. Hence `8x∈H` for every `x∈H^⊥` iff

`S^⊥ ⊂ S`.

The endpoint group `(Z/2)^4 ⊕ (Z/4)^6 ⊕ (Z/8)^4` has order `2^28`, `|Q[2]|=2^14`, `|Q[4]|=2^24`, and exponent eight. Therefore an elementary H has the endpoint invariant factors iff

1. `S` is coisotropic: `S^⊥⊂S`;
2. `s+r=5`.

The possible cases are exactly `(s,r)=(2,3),(3,2),(4,1)`. In `Y=F2^4` there are exactly 3, 7, and 1 coisotropic subspaces of dimensions 2, 3, and 4 respectively.

## 2. cc stability

On `V`, the extension-independent `cc` action swaps `(0,1)`, `(2,3)`, `(4,5)` and fixes the remaining eight coordinates. On `X`, write `N=cc-I`; then `N^2=0`, `rank N=3`, and `dim ker N=7`.

Every H above is an extension of `P=pr_X(H)` by `S`; after choosing the quotient `Y/S`, it is represented by a graph map `phi:P→Y/S`. cc-stability is equivalent to

- `P` being N-stable;
- `phi∘N=0`.

Thus `phi` factors through `P/N(P)`. The script enumerates N-stable P exactly from the three Jordan blocks, not by sampling arbitrary 9-planes.

After imposing `r=5-s`, the exact counts by `b=dim N(P)` are

- `s=2`, `dim P=7`, `r=3`: `{b=0:1, b=1:146, b=2:1008}`;
- `s=3`, `dim P=6`, `r=2`: `{b=0:112, b=1:6848, b=2:17920}`;
- `s=4`, `dim P=5`, `r=1`: `{b=0:1792, b=1:37376, b=2:27648}`.

Including all graph maps gives exactly 8,597,760 elementary H with the endpoint invariant-factor group and cc stability.

## 3. endpoint ct two-torsion

The retained exact scaled action artifact contains 128 raw global `ct` choices. On the half-lifts of `A0[2]`, all 128 induce the same binary map `L:V→V`:

- coordinates `0..5` map to zero;
- `e6,e7,e8,e9` map to `e10,e11,e12,e13`;
- `e10,e11,e12,e13` map to themselves.

Because ct fixes `A0[2]` pointwise, for `Q[2]` there is an exact sequence

`0 → A0[2]/H → Q[2] → H → 0`.

For `h∈H`, choose any half `x` with `2x=h`. Then `ct(x)-x∈A0[2]`, and its class modulo H is independent of the chosen half. This gives a linear map

`delta_H : H → A0[2]/H`.

Hence

`dim Fix(ct,Q[2]) = 14 - rank(delta_H)`.

The endpoint has `log2 |Fix(ct)[2]|=13`, so `rank(delta_H)=1` is mandatory.

In the graph description, modulo `S` this map is

`delta = ell + phi : P/N(P) → Y/S`,

where `ell` is the fixed map induced by coordinates `6..9`. As `phi` ranges over all cc-stable graph maps, `delta` ranges bijectively over all linear maps `P/N(P)→Y/S`. Thus the number of choices with rank one is elementary linear algebra:

- for `dim(Y/S)=1`: `2^m-1`;
- for `dim(Y/S)=2`: `3(2^m-1)`;
- for `dim(Y/S)=0`: zero,

with `m=dim P-dim N(P)`.

Therefore the entire `s=4` branch is rejected, and the exact survivor census after the endpoint ct two-torsion condition is

- `s=2`: 365,157;
- `s=3`: 3,417,008;
- `s=4`: 0;
- total: **3,782,165**.

These remain candidates only. The next leaf must impose the full ct fixed subgroup, the exact finite quadratic form, the cc/joint fixed types, and simultaneous endpoint V4 conjugacy. Stage33 remains `6/11`; Stage33-08 and Stage33-09 remain unreleased.
