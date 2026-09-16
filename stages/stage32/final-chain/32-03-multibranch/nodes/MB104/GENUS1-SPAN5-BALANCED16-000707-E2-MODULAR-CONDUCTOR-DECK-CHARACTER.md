# Stage32 MB104 — `000707000f0f` e=2 modular conductor residual deck character

Status: **RETAINED V2 CORRECTION CANDIDATE / ACTUAL `G/H` CHARACTER AND EXPLICIT `R=C8/H` COORDINATE / CONDUCTOR TRANSITION ELEMENT STILL MISSING / e=2 OPEN / NO CREDIT**

## Scope and correction

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The previous V1 version of this note used the Beauville free-subgroup character

```text
G -> G/G0,   G0=Gamma'[4]/Gamma[8],
```

as if it were the residual sheet character

```text
G -> G/H
```

for the `000707` support.  These two index-two subgroups are different.  That
identification is withdrawn here.  No V1 conductor sign is consumable.

The retained support has exactly the two singular types

```text
b1=Z1=0,
b2=Z2=0,
```

and omits

```text
b3=Z3=0.
```

Freitag--Salvati Manni's theta action identifies these three types with

```text
b1=0  <->  T',
b2=0  <->  TT'R,
b3=0  <->  T.
```

Hence for this support

```text
G = Gamma[4]/Gamma[8] = <T,T',R> ~= (Z/2)^3,
H = <T',TT'R> = {1,T',TR,TT'R},
```

while the Beauville free subgroup is

```text
G0 = Gamma'[4]/Gamma[8] = <TT',TR>.
```

In particular

```text
T' in H but T' notin G0,
```

so `G/H` and `G/G0` cannot have the same character.

## 1. Correct finite congruence character

Write a class of `Gamma[4]/Gamma[8]` modulo `8` as

```text
M = [[A,B],[C,D]]
  == [[1+4*rho, 4*tau],
      [4*upsilon, 1+4*rho]]        (mod 8),
rho,tau,upsilon in F2.
```

The three bits are respectively the exponents of

```text
R, T, T'.
```

The residual `000707` quotient has kernel `H`, hence its character is

```text
chi_res([M]) = rho + tau  in F2.                 (RES-CHAR)
```

Equivalently,

```text
chi_res([M]) = 0
    <=> A+B == 1 (mod 8).                        (RES-CONG)
```

This is well-defined on the class modulo `Gamma[8]`.

For comparison only, the Beauville character has kernel `G0` and is

```text
chi_B([M]) = rho + tau + upsilon,
chi_B([M])=0 <=> A+B+C == 1 (mod 8).
```

The old V1 evaluator `A+B+C == 1 (mod 8)` therefore tests the Beauville cover,
not the residual `G/H` sheet.  The matrix `T'` is an explicit witness:

```text
chi_res(T')=0,
chi_B(T')=1.
```

## 2. Explicit coordinate on `R=C8/H`

For one level-eight factor use the retained theta coordinates

```text
a=theta00(z),
e=theta10(z),
b=theta01(z),
c=theta00(2z),
d=theta10(2z)
```

with

```text
a^2=c^2+d^2,
b^2=c^2-d^2,
e^2=2*c*d.
```

On the chart `d!=0` put

```text
x=c/d,
r=e/d.
```

Then

```text
r^2=2*x.                                         (R-REL)
```

The two generators of the actual support subgroup `H` act as follows:

- `T'` changes only the sign of `b`, so it fixes `r`;
- `TT'R` changes the signs of `e,c,d` simultaneously (and also `b`), so it
  again fixes `r`.

Thus `r` is `H`-invariant.  Conversely, on this chart the remaining ratios
satisfy

```text
(a/d)^2=x^2+1,
(b/d)^2=x^2-1,
x=r^2/2.
```

For generic `r`, the independent signs of `a/d` and `b/d` give exactly the
four points of one `H`-orbit.  Hence

```text
k(C8)^H = C(r),
R=C8/H ~= P1_r.                                  (R-COORD)
```

The absent singular involution is represented by `T`.  Since `T` changes the
sign of `e` and fixes `d`,

```text
T : r -> -r.                                     (RES-ACT)
```

Therefore the residual quotient is explicitly

```text
q : R=P1_r -> S=C8/G=P1_s,
s=r^2                                             (Q)
```

up to a Möbius rescaling of the base coordinate.  Its two branch points
`r=0,infinity` are exactly the fixed points of the absent type `b3=0`.

Equivalently one may take `x=c/d` on `S`; then `r^2=2x`.  This gives an
explicit choice of the base-cover function in the retained square-root
semantics:

```text
h=2x,
sqrt(h)=r=e/d.                                    (SQRT)
```

## 3. Correct conductor-pair evaluator

Let normalization preimages `u,v` over one singular carrier point have a
source-locked compatible modular transition

```text
[M_(u,v)] in G=Gamma[4]/Gamma[8].
```

Then the residual conductor bit is

```text
epsilon(u)+epsilon(v)
 = chi_res([M_(u,v)]),
```

with `chi_res` from `(RES-CHAR)/(RES-CONG)`, not the Beauville character.

Equivalently, when the explicit quotient coordinate is used and the pair is
away from the absent branch values,

```text
r(v) = (-1)^chi_res([M_(u,v)]) * r(u)
```

after compatible local trivialization over the common base value in `S`.

Thus the active weighted cut becomes

```text
y/2
 = sum_p sum_(i<j) I_p(beta_i,beta_j)
   * chi_res([M_(p;i,j)]).
```

The retained Hodge threshold remains

```text
y/2 >= 84*l^2.
```

## 4. What has and has not advanced

The residual evaluator is now explicit in two equivalent forms:

```text
M_(u,v) -> (A+B mod 8) -> chi_res,
```

or

```text
normalization preimage -> r=e/d in R -> sign under r->-r.
```

This removes the previous ambiguity between the Beauville two-fold cover and
the actual `000707` residual `G/H` cover.

The load-bearing object still missing is the branch-pair transition itself:
the repository does not yet determine `M_(u,v)` (or, equivalently, the two
limiting `r` values) for every conductor identification.

## Sources / retained adapters

- `FREITAG-SALVATI-MANNI-RESIDUAL-KUMMER-COORDINATE-SOURCE-NOTE.md`
- `BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md`
- `GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION.md`
- `GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER.md`

External check: Freitag--Salvati Manni, *Parametrization of the box variety by
theta functions*, especially Lemma 2.3 and Section 4.  The published
`a+b+c == 1 (mod 8)` condition defines `Gamma'[4]`; it is used here only to
distinguish `G0` from the support-specific subgroup `H`.

## Firewalls

- The old V1 Beauville-character evaluator is superseded and non-consumable
  for this active residual-sheet leaf.
- No conductor transition `M_(u,v)` is claimed to be known.
- No individual conductor sign is assigned.
- No weighted-cut upper bound is claimed.
- No `e=2` or `e=4` closure is claimed.
- `000707000f0f` remains open.
- MB104/span5/receiver/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge authorization.
