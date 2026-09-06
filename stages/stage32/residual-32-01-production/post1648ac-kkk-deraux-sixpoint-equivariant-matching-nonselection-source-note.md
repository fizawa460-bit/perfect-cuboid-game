# Stage32 post1648AC scratch source note — full six-point equivariant matching is exact but W-line balanced

This leaf is scratch-only and grants no MAIN or arithmetic credit.

## Locked inputs

No new semantic identification is assumed.

From post1648Z / Klein–Kokotov–Korotkin §3.2.4, use the named Bolza branch set

`{0, infinity, 1, -1, i, -i}`

with the three explicit curve generators

- `mu1: z -> i*z`,
- `mu2: z -> (z+1)/(z-1)`,
- `mu3: z -> -1/z`.

On the six branch points these generate a permutation group of order 24.

From post1648AA / Deraux §4, use the explicit six-point order-8-isotropy orbit in
`A[2]` with retained coordinate basis `[e1,e2,r*e1,r*e2]`:

- `(0,0,1,0)`,
- `(0,0,1,1)`,
- `(1,0,0,0)`,
- `(1,0,1,1)`,
- `(1,1,0,1)`,
- `(1,1,1,1)`.

The affine `G48` action on this set has permutation image of order 24.

## Exact equivariant matching

Enumerate all `6! = 720` bijections from the named source branch set to the explicit
target six-point set.

A bijection `phi` is retained exactly when it conjugates the full source
six-point permutation group onto the full target six-point permutation image.
This is stronger than matching only the `B9/mu1` cycle type.

Exactly 48 bijections survive.

For every surviving bijection, take the target difference between the images of
source `0` and source `infinity`. The only differences that occur are the three
retained W-line vectors

- `L1=(0,0,1,0)` -> residue 73,
- `L2=(0,0,0,1)` -> residue 97,
- `L3=(0,0,1,1)` -> residue 235,

with multiplicities `16,16,16`.

Thus the complete six-point permutation representation still does not select an
absolute retained W-line.

## Semantic boundary

The 48 surviving bijections are exhaustive equivariant candidates, not 48
source-locked pointwise identifications. No checked source chooses one of them.
Equivariance up to conjugacy of the full `S4` permutation image therefore does
not materialize the missing marked ppav conjugator `g`.

This closes the route “reconstruct the full six-Weierstrass permutation action
and match it exactly to the Deraux six-point action” as a nonselecting finite
adapter search. It does not claim global nonexistence of an explicit `g` in
other external sources.
