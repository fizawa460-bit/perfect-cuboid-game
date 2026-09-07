# Stage32EX6 post-1697 — FSM16 modular-tensor multibranch wall

Status: **EXPLORATORY EXACT BOUNDED WALL — NO ENDPOINT CLOSURE CREDIT**.

## Question

Can the modular-tensor degree bound of Freitag–Salvati Manni exclude the hypothetical fixed-V6 genus-one carrier at the endpoint `O=266`?

## External source lock

Freitag–Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), Theorem 3.1; arXiv:1303.6495.

Their Theorem 3.1 states that if an integral curve `C` on the box variety has bijective normalization map `Cbar -> C`, geometric genus `g`, and projective degree `d`, then

`d <= 176 + 16 g`.

The proof constructs, for arbitrary positive integer `k`, a pulled-back symmetric tensor with

`16(2g-2)k = #zeros - #poles`.

The exact proof ingredients used here are:

- the zero divisor contributes at least `2kd` zeros;
- poles occur only above the 48 exceptional curves over the nodes;
- for one normalization branch at a node, the local cusp parameters satisfy
  `a1 ≡ a2 ≡ 0 (mod 4)`, `a1+a2 ≡ 0 (mod 8)`, and `a1,a2>0`;
- hence `a1+a2>=8`;
- `(dzdw)^(8k)` contributes pole order `16k`, while `Delta(z)^k Delta(w)^k` contributes zero order `(a1+a2)k`;
- therefore a branch contributes pole order at most `8k`;
- under bijective normalization there is at most one normalization point over each of the 48 nodes, so the proof obtains `#poles <= 384k`.

This is the only FSM16 result used below. No stronger holomorphic-tensor claim is imported: the paper explicitly remarks that they did not obtain a tensor holomorphic across all exceptional divisors.

## Existing EX6 endpoint lock

From `post1697-o266-endpoint-source-note.md`, at `O=266`:

- geometric genus `g=1`;
- projective degree of the retained V6 class is `d=186`;
- the normalization has `B=266` points over the exceptional divisor;
- all exceptional contacts have multiplicity one;
- the positive node support has size 47, but 38 nodes are multibranch, so the normalization map is not bijective over the image curve.

## First near-miss: the published theorem itself

For `g=1`, FSM16 gives

`d <= 176 + 16 = 192`.

Thus the retained V6 degree

`d=186`

already survives the published unibranch/bijective-normalization theorem, with degree slack `192-186=6`.

So merely importing Theorem 3.1 cannot exclude the V6 carrier even before confronting the actual O266 multibranch profile.

## Sharpening by the exact 47-node support still misses

If, counterfactually, the normalization were bijective and met only the 47 nodes in the retained positive support, the identical proof would improve the pole bound from `48*8k` to `47*8k=376k`.

For genus one,

`0 = #zeros - #poles >= 2kd - 376k`,

so

`d <= 188`.

The V6 degree `186` still survives, now with slack `2`.

This 47-node calculation is only a diagnostic near-miss. It is not applicable to the actual O266 population because that population is multibranch.

## Exact branchwise extension of the proof architecture

Let `B` denote the number of normalization points lying over the exceptional divisor. The local FSM16 cusp estimate is branchwise, so without the bijectivity assumption the same proof architecture gives the safe pole bound

`#poles <= 8k B`.

Combining with `#zeros >= 2kd` gives

`16(2g-2)k >= 2kd - 8kB`,

hence

`d <= 16g - 16 + 4B`.

At the O266 endpoint, `g=1` and `B=266`, therefore

`d <= 4*266 = 1064`.

The retained degree `186` has slack `878`. Thus the direct multibranch extension is extremely nonexcluding.

This extension is a proof-level adaptation of the exact FSM16 pole count; it does not assert a new published theorem and does not identify the FSM16 cusp parameters with the Stage32 AN/FSM local parameters.

## Stronger weighted threshold inside the same tensor architecture

The congruence conditions on the FSM16 cusp parameters make the local pole budget discrete.

Because `a1,a2` are positive multiples of 4 and `a1+a2` is divisible by 8:

- the unique minimal sum is `a1+a2=8`, necessarily `(a1,a2)=(4,4)`, giving pole order at most `8k`;
- every other allowed pair has `a1+a2>=16`, so the tensor has no positive pole order on that branch.

Let

`S_cusp = #{normalization branches with FSM16 cusp pair (4,4)}`.

Then the same proof gives

`#poles <= 8k S_cusp`.

For the V6 target `g=1,d=186`, compatibility requires

`8 S_cusp >= 2d = 372`,

so necessarily

`S_cusp >= 47`.

Equivalently, this modular-tensor route would exclude the V6 genus-one carrier if one could prove the global/member-level bound

`S_cusp <= 46`.

This is the sharp integer threshold available from the FSM16 tensor argument at degree 186.

## Missing adapter / re-entry boundary

No retained source currently identifies the FSM16 modular cusp pair `(a1,a2)` with the Stage32 AN local FSM pair `(A,B)` branch-by-branch. In particular, this note does **not** turn AN's `(1,1)` witness into an FSM16 `(4,4)` count.

A useful continuation through this route therefore needs one of:

1. an exact branch-level adapter from the Stage32 local coordinates to the FSM16 modular cusp parameters, plus a global theorem forcing `S_cusp<=46`;
2. a replacement tensor with a strictly smaller per-branch pole budget;
3. a member-level restriction that forces enough branches into `a1+a2>=16` so that fewer than 47 maximal-pole branches remain;
4. a different global inequality not paid for independently at every normalization branch.

Without such an input, the FSM16 modular-tensor architecture does not exclude O266.

## Decision

`FSM16_MODULAR_TENSOR_O266 = NUMERICALLY_NONEXCLUDING`

`O266_ENDPOINT_EXCLUDED = false`.

No O264 descent or endpoint closure follows from this wall.
