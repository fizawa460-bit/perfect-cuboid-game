# Stage32 MB104 — genus-one P5 Beauville equality rigidity

Status: **RETAINED GLOBAL NECESSARY GEOMETRY / FORMAL F1-P5 EQUALITY UPGRADED TO ETALE CORRESPONDENCE / NO CLOSURE / MB104 INCOMPLETE / NO CREDIT**

## Scope

Assume, only for this leaf, that an actual integral normalization-genus-one carrier realizes the retained uniform F1-P5 packet

```text
D_l = 7l H - 4l sum_(p in Sigma) E_p,
|Sigma|=14,
l>=1,
d=112l,
r_odd=R8=M=112l.
```

The equality `r_odd=d` is the key extra input.  This leaf does **not** assume that such a carrier exists.

## Fixed Beauville/product-cover geometry

Let

```text
C8 = H*/Gamma[8],   genus(C8)=5,
P = C8 x C8.
```

Freitag--Salvati Manni give a free diagonal action

```text
G0 = Gamma'[4]/Gamma[8] ~= (Z/2Z)^2
```

with

```text
P -> X=P/G0
```

a finite etale Galois cover of degree `4`, while `X -> B` is the Beauville double cover of the box variety.

The retained Beauville branch adapter says that the pullback of the normalization of a genus-`g` carrier to `X` is a connected double cover whenever `r_odd>0`, with

```text
2h-2 = 4g-4+r_odd.
```

For `g=1` and `r_odd=d`, its genus is therefore

```text
2h-2=d,
h=1+d/2=56l+1.
```

Call this normalized curve `Y`.

## Pull once more to the product cover

Take a connected component `Z` of the normalized pullback of `Y` to `P`.  Since `P->X` is etale of degree four,

```text
e := deg(Z->Y) in {1,2,4},
```

and `Z->Y` is etale.  Hence

```text
2g(Z)-2 = e(2h-2)=e d.                 (E1)
```

The canonical pullback identity from the retained Beauville leaf gives

```text
K_X.Y = 2d.
```

Etaleness of `P->X` therefore gives

```text
K_P.Z = e K_X.Y = 2 e d.               (E2)
```

## Equality forces both product projections to be etale

Write the two projections as

```text
f1: Z -> C8,
f2: Z -> C8,
```

with degrees `n1,n2`.  Since `genus(C8)=5`,

```text
deg K_C8 = 8,
K_P = pr1^*K_C8 + pr2^*K_C8.
```

Thus `(E2)` gives

```text
8(n1+n2)=2ed,
n1+n2=ed/4.                              (E3)
```

For each nonconstant projection, Riemann--Hurwitz and `(E1)` give

```text
8 n_j <= 2g(Z)-2 = ed,
n_j <= ed/8.                              (E4)
```

A constant projection would contribute `n_j=0`, making `(E3)` impossible because the other projection is bounded by `ed/8 < ed/4`.  Hence both projections are nonconstant.

Adding the two inequalities `(E4)` gives

```text
n1+n2 <= ed/4.
```

But `(E3)` is equality.  Therefore both Riemann--Hurwitz inequalities are individually equalities:

```text
n1=n2=ed/8,
Ram(f1)=Ram(f2)=0.
```

So both projections are finite etale covers.

For the retained integral Picard subsequence `d=112l`,

```text
n1=n2=14 e l,
e in {1,2,4}.
```

Thus any actual realization of the uniform F1-P5 packet would produce inside

```text
C8 x C8
```

a connected curve `Z` that is an **etale self-correspondence of equal bidegree**

```text
(14 e l, 14 e l),  e in {1,2,4}.
```

Equivalently, `Z` is a common finite etale cover of the two genus-five factors.

## Why this is new information

The earlier Beauville leaf retained only the inequality

```text
d <= r_odd
```

for genus one and classified it as the wrong-direction lower bound on odd branches.  The formal F1-P5 packet lies exactly on the equality face

```text
r_odd=d.
```

On that equality face the two projection Riemann--Hurwitz inequalities cannot have slack.  The numerical boundary therefore upgrades to a rigid geometric requirement: actual realization must come from an etale correspondence on `X(8)`.

## What remains

This does not yet exclude the packet: genus-five curves can have nontrivial finite etale common covers.  The next useful question is whether an etale correspondence of bidegree `14el` can simultaneously descend through the fixed `(Z/2)^3` modular quotient and realize the selected fourteen box-node stabilizer types with `8l` odd minimal branches at each supported node.

That is now a finite-group/equivariant-correspondence problem rather than an unconstrained local-branch gluing problem.

## Firewalls

- The conclusion is conditional on actual realization of the retained uniform F1-P5 packet.
- No etale correspondence is constructed.
- No surviving balanced support orbit is closed.
- No claim is made yet about which node-stabilizer types occur in the selected support.
- Whole span5, unequal Picard coefficients, P6 sectors, MB104, receiver, theorem, endpoint, and Perfect-Cuboid credit remain open/zero.
- No merge authorization.
