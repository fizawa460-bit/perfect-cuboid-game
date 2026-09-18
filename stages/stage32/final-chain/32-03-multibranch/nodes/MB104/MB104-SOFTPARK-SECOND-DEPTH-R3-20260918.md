# Stage32 MB104 — SOFT-PARK second-depth screening Round 3 — 2026-09-18

Status: **ROUND 3 COMPLETE / NO THIRD-DEPTH ADVANCE / W17,W23 RESERVE / W18,W19,W29 PARK / NO MATHEMATICAL CREDIT**

## Scope

Round 3 revisits the normalization/projective-geometry family:

```
W17  support-stabilizer carrier dichotomy
W18  cuboid-specific secant defect
W19  adaptive Wronskian / forced contact
W23  joint-factor special singularity/grid geometry
W29  cotangent stability on the special elliptic normalization
```

Promotion still requires a source-complete path to either all-`l` exclusion or an explicit large-`l` cutoff.

## W17 — support stabilizer: exact fixed-locus refinement

The nontrivial stabilizer of the active support is

```
sigma:(a1,a2,a3,b1,b2,b3,c)
   ->(a2,a1,a3,b2,b1,b3,c).
```

Use the source-locked cuboid equations

```
a1^2+a2^2=b3^2,
a2^2+a3^2=b1^2,
a1^2+a3^2=b2^2,
a1^2+a2^2+a3^2=c^2.
```

The projective fixed locus has a plus-eigenspace

```
a1=a2, b1=b2.
```

On the surface the first quadric becomes

```
b3^2=2a1^2,
```

so over the retained ground field it splits into the two known genus-one quartics

```
F_+: a1-a2=0, b1-b2=0, b3-sqrt(2)a1=0,
F_-: a1-a2=0, b1-b2=0, b3+sqrt(2)a1=0.
```

These are members of the Stoll--Testa `C3` family, hence

```
H.F_+=H.F_-=4.
```

The minus-eigenspace would require

```
a1=-a2, b1=-b2, a3=b3=c=0,
```

but the first quadric then gives `2a1^2=0`, so it contributes no projective fixed point.

Exact replay of the retained 48-node model gives the four fixed box nodes

```
P16,P19,P20,P23,
```

and none belongs to the active support

```
{P0,P1,P2,P3,P8,P9,P10,P11,P24,P25,P26,P32,P33,P34}.
```

Therefore the active class has

```
D_l.F_+ = D_l.F_- = 7l*4 = 28l,
D_l.(F_++F_-)=56l.
```

This sharpens the invariant branch of W17.  If `sigma(C)=C`, the normalization involution has at most four fixed points.  Hence the geometric intersection `56l` with the pointwise-fixed curves cannot generically be read as `56l` distinct fixed normalization points: almost all of it must be absorbed through invariant singularities whose local normalization branches are exchanged, or through higher contact.

That is useful localization, but it is not yet a cutoff.  Such branch-exchange singularities can consume only a linear amount of the available quadratic genus defect without contradiction.  The non-invariant branch remains as before: `C.sigma(C)=336l^2`, while the current landing data give no positive source-complete local lower bound at the supported exceptionals.

**Disposition: RESERVE.**

Reopen if the fixed-locus singularities can be charged by a source-complete local invariant with quadratic total cost, or if the quotient curve on `S/<sigma>` acquires an independent genus/conductor obstruction.

## W18 — secant/projection center: exact elliptic evaluation saturation

Let

```
E = normalization,
L=nu^*O_S(H),
d=deg L=112l,
B=B_support,
deg B=d,
L ~= O_E(B).
```

Since `g(E)=1`,

```
h0(E,L)=d.
```

The exact sequence

```
0 -> O_E -> L -> L|_B -> 0
```

gives

```
0 -> k -> H0(L) -> H0(L|_B) -> H1(O_E) -> 0,
```

so the restriction image has dimension exactly

```
d-1.
```

Now partition `B` into the fourteen supported node blocks, each of size `8l`.  Requiring all points of one block to have one projective image restricts the evaluation vectors to one line per block.  Before the single elliptic evaluation/Abel relation, the resulting block-value space has dimension 14; intersecting with the codimension-one image of `H0(L)` leaves the generic dimension at least 13.

The ambient canonical system needs only six independent restrictions after removing the unique support-hyperplane section:

```
dim(V/<support section>)=6.
```

Thus the refined secant-center problem still has at least seven dimensions of linear room:

```
13-6=7.
```

The old `O(l)` parameter slack was therefore not the correct final scale, but the exact elliptic restriction sequence still leaves constant positive slack rather than an overload.

Any further obstruction must use the **specific** node-coordinate ratios/principal parts inside that 14-block value space.  This is precisely the residue/Abel information isolated in W20.

**Disposition: PARK_DOMINATED_BY_W20.**

## W19 — adaptive Wronskian / unbounded contact

For the ambient

```
g^6_(112l)
```

the total Pluecker/Wronskian weight is

```
7*112l=784l.
```

The key obstruction remains structural, not numerical: identifying many distinct points of `E` at one box node does not force ramification of the map at any of those points.  The retained supported branches are individually unramified in the product-factor model.

Hence there is no source-complete positive Wronskian charge attached merely to the `112l` supported preimages.

If extra charge is obtained by forcing equal tangent directions or higher contact, that is no longer a bare Wronskian mechanism; it is W23's tangency problem.

**Disposition: PARK_DOMINATED_BY_W23.**

## W23 — special grid / tangency geometry

The `e=2` joint-factor image has

```
C subset P1 x P1,
[C]=(28l,28l),
g(normalization)=1.
```

Its total delta is

```
delta_total=784l^2-56l.
```

The retained optimal branch-count calculation at the sixteen special grid points gives at most

```
delta_branch_count <=736l^2-56l,
```

leaving a necessary extra-contact gap of

```
48l^2.
```

The archive also gives an exact tangency evaluator: for two smooth branches through the same special point,

```
I(branch_i,branch_j)>=2
iff
A(branch_i)^2=A(branch_j)^2,
```

where `A` is the appropriate Kummer-ratio function.

This is a genuine packet-sensitive evaluator, but there is still no collision theorem.  A degree bound on a rational function does not force the values on a chosen finite set of normalization points to repeat: distinct supported points may map to distinct values of `A`.  In particular, the retained estimate `deg A<=84l` gives no source-complete lower bound on the number of `A^2` collisions.

To close through this route one needs **quadratically many** units of extra intersection beyond the ordinary branch-count contribution—at least `48l^2` in the extremal capacity comparison.  No current monodromy, Nielsen, or modular statement forces that quadratic collision count.

**Disposition: RESERVE.**

It remains mathematically sharper than generic secant/Wronskian counting because the tangent evaluator is exact; promote only if a new source forces a finite value set, large fibers, or another `Omega(l^2)` collision mechanism.

## W29 — cotangent stability is structurally impossible

Let

```
f:E -> S
```

be the normalization map.  Let `R` be its ramification divisor.  The differential has saturated image

```
O_E(-R) subset Omega_E ~= O_E.
```

Thus on the elliptic normalization there is an exact sequence

```
0 -> K_f -> f^*Omega_S -> O_E(-R) -> 0.
```

Since

```
deg f^*Omega_S = K_S.D_l =112l,
```

we have

```
deg K_f =112l+deg R >0.
```

The extension class lies in

```
Ext^1(O_E(-R),K_f)
 = H^1(E,K_f(R)).
```

But

```
deg K_f(R)=112l+2deg R>0,
```

and a positive-degree line bundle on an elliptic curve has `H^1=0`.  Therefore the conormal sequence splits:

```
f^*Omega_S ~= K_f direct_sum O_E(-R).
```

So the hoped-for positive-slope semistability is not merely unproved; it is incompatible with the normalization geometry.  The degree-zero/negative quotient is an explicit direct summand.

**Disposition: PARK_STRUCTURALLY_SPLIT.**

A future cotangent argument would have to exploit this splitting itself, not try to prove semistability.

## Round-3 selection

```
ADVANCE_FOR_THIRD_DEPTH:
  none

RESERVE:
  W17  exact fixed-locus localization, but only linear pressure so far
  W23  exact tangency evaluator, but no quadratic collision theorem

PARK:
  W18  exact secant/evaluation problem reduces to packet Abel data already in W20
  W19  no forced ramification; any useful contact is W23
  W29  pullback cotangent splits on the elliptic normalization
```

Cumulative third-depth candidates remain

```
W4, W16, W20.
```

High reserve remains

```
W5.
```

Additional reserves are

```
W13, W17, W23.
```

No mathematical closure or downstream credit is claimed.

## Next second-depth round

Continue the deformation/obstruction family:

```
W1   smaller canonical Bogomolov--Reider / CB cluster
W21  lower-rank polar/degeneracy construction
W22  stable-map obstruction / negative expected dimension
W24  distributional conductor/different
W27  reduced/cosection semiregularity
W28  multiplier/interpolation variant
```

Do not promote any route unless it gains a source-complete forward adapter and an explicit all-`l` or finite-cutoff closing shape.
