# Stage32 MB104 — wide shallow closure scan Round D — 2026-09-18

Status: **ROUND D COMPLETE / FIVE ROUTES SCREENED / ALL DROP / NO MATHEMATICAL CREDIT**

Archive-semantic precheck was performed before promotion.

## W16 — minimal Cayley--Bacharach conductor subcluster: DROP

Let

```
B_E=sum_(p in Sigma)E_p.
```

For the exact dangerous packet,

```
D_l.B_E=112l,
B_E^2=-28.
```

The most obvious source-complete zero-dimensional cluster is the full landing scheme

```
Z=C intersect B_E,
length Z=112l.
```

It is a complete intersection.  The corresponding Serre construction is therefore tautological: the rank-two bundle can be taken as

```
O_S(D_l) direct_sum O_S(B_E),
```

with

```
c1=D_l+B_E,
c2=112l.
```

Its Bogomolov discriminant is

```
c1^2-4c2
 =336l^2-224l-28 >0
```

for every `l>=1`, but this supplies no new divisor: the bundle is already split and its destabilizing line bundles are exactly the two input factors.

Thus the one canonical linear-size CB cluster loops back to the starting geometry.  A proper smaller CB subcluster could be interesting, but the retained packet does not canonically supply one; constructing it would be new-theorem work.

**DROP.**

## W17 — support-stabilizer carrier dichotomy: DROP

The active support stabilizer has order two. Its nonidentity element is

```
(a1,a2,a3,b1,b2,b3,c)
 -> (a2,a1,a3,b2,b1,b3,c).
```

On the active support it pairs the fourteen nodes as

```
(0,8),(1,9),(2,10),(3,11),
(24,32),(25,33),(26,34),
```

with no fixed supported node.

### If sigma(C)=C

The `112l` supported normalization points can be paired between these seven node pairs. There is no packet parity obstruction. Numerically an involution on a genus-one normalization can have either zero fixed points with genus-one quotient or four fixed points with genus-zero quotient, so Riemann--Hurwitz alone is compatible.

### If sigma(C)!=C

Both curves have class `D_l`, hence

```
C.sigma(C)=336l^2.
```

At a supported node the landing set of `sigma(C)` is transported from the paired node.  The retained A1/static-landing interface does not force any of those landing points to coincide with the landing set of `C`; they can be disjoint at the formal packet level.

Therefore there is no positive source-complete local lower bound, let alone one exceeding `336l^2`.

Both branches of the dichotomy remain numerically compatible.

**DROP.**

## W18 — elliptic projection / secant-center capacity: DROP

Let

```
L=nu^*O_S(H),
deg L=d=112l,
h0(E,L)=112l.
```

The ambient map uses seven sections. At one box node, `m=8l` distinct normalization points all map to one fixed point of `P^6`. Six independent hyperplanes through that target point must vanish at those `m` points.

For an ordered seven-section presentation, this imposes at most

```
6m=48l
```

linear conditions per node. Across fourteen nodes:

```
14*6m=672l.
```

The seven sections live in a vector space of dimension

```
7h0(L)=784l.
```

So even the naive simultaneous collision problem has linear slack

```
784l-672l=112l.
```

After quotienting by the `49` parameters of a basis change in the seven-dimensional target space, the slack is still

```
112l-49>0
```

for every `l>=1`.

Thus the multisecant/projection-center conditions are not dimensionally overdetermined. A special-position theorem stronger than the generic secant count would be required.

**DROP.**

## W19 — adaptive Wronskian / unbounded-jet budget: DROP

For a basepoint-free

```
g^6_(112l)
```

on a genus-one curve, the Wronskian/Pluecker ramification divisor has total weight

```
(r+1)d = 7*112l = 784l.
```

But the MB104 packet does not force ramification at the `112l` supported preimages. Distinct points may map to the same box node while each map germ is unramified; the retained minimal-branch local model explicitly leaves the first tangential jet free.

So the native forced Wronskian charge is zero.

Even under an intentionally stronger fictitious charge of one unit per supported preimage, the cost would be only

```
112l < 784l.
```

There is no Wronskian overload.

**DROP.**

## W20 — support-hyperplane residue / Abel relation: DROP

The unique support hyperplane has zero divisor on the normalization equal to the complete supported branch divisor

```
B_support,
deg B_support=112l.
```

Hence

```
L ~= O_E(B_support),
h0(E,L)=112l.
```

Dividing the other ambient coordinate sections by this hyperplane section gives only six independent meromorphic functions with poles bounded by `B_support`, inside a Riemann--Roch space of dimension `112l`.

The basic Abel condition for `B_support` is exactly the statement that it is the divisor of that hyperplane section, so it contributes no new constraint.  More refined residue/principal-part moments would require fixed local principal parts, but the retained packet leaves exceptional landing values and first tangential jets free.

The archive also already contains a stronger, sheet-selected Abel--Jacobi statement in the e=2 product-cover geometry; even that only reduces one divisor difference to `E[2]` and does not close the frontier.

**DROP.**

## Round D result

```
W16 DROP
W17 DROP
W18 DROP
W19 DROP
W20 DROP
```

No second-scan or DEEP candidate is released.

The wide scan should continue with genuinely new mechanisms only, after archive-semantic precheck.
