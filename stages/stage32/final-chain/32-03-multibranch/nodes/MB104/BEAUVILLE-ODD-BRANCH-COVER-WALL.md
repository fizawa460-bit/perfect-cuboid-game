# Stage32 MB104 — Beauville odd-branch double-cover wall

Status: **RETAINED GLOBAL COVER WALL / MB104 INCOMPLETE / NO CREDIT**

## Question

Can the canonical two-fold Beauville cover of the box variety convert the multibranch problem into a Riemann--Hurwitz bound strong enough to upper-bound the FSM-minimal count `R8`?

Answer: **the cover gives a clean global constraint, but in the wrong direction**. It forces a lower bound on the number of odd exceptional contacts.

## Source-locked cover geometry

Freitag--Salvati Manni, Section 4 of *Parametrization of the box variety by theta functions* (Michigan Math. J. 65 (2016), arXiv:1303.6495), constructs a two-fold cover

```text
q : X -> B
```

which is locally `C^2 -> C^2/{+/-1}` at each of the 48 nodes. After blowing up the 48 points upstairs and resolving the nodes downstairs, the induced double cover is ramified exactly along the 48 exceptional curves. The same section states that `X` has a finite unramified cover by a product of two curves of genus greater than one.

The retained Stage32 A1 adapter gives, for a normalization branch through a box node,

```text
m = min(A,B),
```

and the resolved Beauville double cover is ramified on that normalization branch exactly when `m` is odd. In particular every FSM-minimal branch `(A,B)=(1,1)` has `m=1` and is an odd branch.

Define

```text
r_odd = number of normalization branches through box nodes with odd m.
```

Then

```text
R8 <= r_odd <= M.
```

Source lock for the branch adapter:
`stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md`, blob `512fcc70afb1acf16956fd4b7a2b9b935a052150`.

## Restricted double cover of the normalization

Let `Cbar` be the normalization of the carrier, of genus `g`, and assume `R8>0`. Then `r_odd>0`, so the restricted degree-two cover is branched and therefore connected. Let `Ybar` be its normalization and let its genus be `h`.

Riemann--Hurwitz gives

```text
2h - 2 = 2(2g - 2) + r_odd
       = 4g - 4 + r_odd.                     (B1)
```

In particular `r_odd` is even.

## Canonical degree upstairs

The local quotient is by `-1` on `C^2`; its determinant is `+1`, so the quotient map is quasi-etale and carries no divisorial canonical ramification. Thus

```text
K_X = q^* K_B
```

in the canonical/Q-Cartier sense. Since the preimage curve has degree two over the downstairs carrier and the canonical degree downstairs is `d`,

```text
K_X . Y = 2d.                                (B2)
```

## Product-cover curve inequality

Take a finite etale cover

```text
P = C1 x C2 -> X
```

with `genus(C1), genus(C2) > 1`, as in Freitag--Salvati Manni Section 4. Let `Z` be a connected component of the normalized pullback of `Y`, of etale degree `e` over `Ybar`.

For the two projections `Z -> C_i`, Riemann--Hurwitz gives, whenever the projection is nonconstant,

```text
deg(proj_i) * (2 genus(C_i)-2) <= 2 genus(Z)-2.
```

A constant projection contributes zero. Therefore

```text
K_P . Z <= 2(2 genus(Z)-2).
```

Etaleness gives

```text
K_P . Z = e (K_X . Y),
2 genus(Z)-2 = e(2h-2),
```

hence

```text
K_X . Y <= 4h - 4.                           (B3)
```

Combining `(B1)`, `(B2)`, `(B3)` yields

```text
2d <= 8g - 8 + 2 r_odd,
d <= 4g - 4 + r_odd,
r_odd >= d - 4g + 4.                         (B4)
```

For the two MB104 genera:

```text
g=0: r_odd >= d + 4,
g=1: r_odd >= d.
```

## Why this does not close MB104

MB104 needs an **upper** bound

```text
R8 <= alpha*d + beta,  alpha < 1/4.
```

The Beauville cover instead supplies a lower bound on the larger quantity `r_odd`. Even under the strongest identification `r_odd=R8`, `(B4)` points in the opposite direction and cannot furnish the required upper slope.

Since `r_odd<=M`, `(B4)` also implies

```text
d <= 4g - 4 + M,
```

which is the same direction as the retained Garcia-Fritz--Urzua exceptional-mass inequality. Thus the canonical double cover does not create a hidden multiplicity upper bound; it explains geometrically why large degree forces more odd contact rather than fewer branches.

## Consequence

The Beauville double-cover/Riemann--Hurwitz route is now closed as a standalone `R8`-upper-bound mechanism. A successful continuation still needs information that upper-bounds integral branch multiplicity: a cuboid-specific conductor/jet inequality, a higher-order differential mechanism that counts repeated branches, or another global restriction not factoring only through odd-contact ramification.

## Firewalls

- No finite `R8` upper bound is proved.
- MB104 remains incomplete.
- Finite Picard enumeration is unreleased.
- No receiver/effectivity/final-milestone/theorem/endpoint/Perfect-Cuboid credit.
- No merge authorization.
