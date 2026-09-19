# MB104 — 000707 degree-four pair-map discriminant exclusion — 2026-09-20

Status: PRE-AUDIT EXACT DISCRIMINANT/RESULTANT EXCLUSION / ZERO CREDIT / NO MERGE

## Setup

Use the new genus-seven fibration class G and a rank-three genus-five fiber F with

H.G=12,
P.G=36,
H.F=8,
P.F=40,
G.F=4.

The product morphism

pi=(f_G,f_F): S -> Y=P1 x P1

is finite of degree four.

Its ramification divisor is

R_pi = K_S - pi^*K_Y
     = H + 2G + 2F.

The discriminant/branch divisor B_pi on Y is the divisorial discriminant of the finite cover.
For a target curve D not contained in B_pi,

deg Disc(pi_D)
 = B_pi.D
 = R_pi.pi^*D

by the discriminant/different description and projection formula.

Let C in |lP| be a hypothetical integral MB carrier and D=pi(C). Let r=deg(C->D).
The previous pair-map reduction excludes r=3,4, so only r=1,2 remain.

The projection degrees of C are

C.G=36l,
C.F=40l.

Hence D has bidegree

(40l/r,36l/r),

and

pi^*D = l[(40/r)G+(36/r)F].

Write the effective residual divisor

Q=pi^*D-C.

The carrier C cannot be a component of the fixed ramification divisor: H.C=112l, while
H.R_pi=56. Thus the generic factor corresponding to C is separable and D is not a branch
component through C. Also the bidegrees below exceed the total branch bidegree in a ruling, so
D itself is not a component of B_pi.

After base change to the normalization of D, the degree-four finite algebra is finite flat.
The factorization into the C-part and the residual Q-part gives the standard discriminant
factorization

disc(fg)=disc(f) disc(g) Res(f,g)^2.

The cross resultant divisor is the scheme-theoretic intersection of the two horizontal factors.
Therefore

2 C.Q <= deg Disc(pi_D).                         (DISC-BOUND)

Internal ramification terms are effective and only increase the discriminant.

## r=2

For r=2,

pi^*D = l(20G+18F).

The residual class is

Q=l(20G+18F-P).

Intersection with C gives

C.Q
 = l^2 P.(20G+18F-P)
 = l^2(20*36+18*40-336)
 = 1104 l^2.

Thus the left side of (DISC-BOUND) is

2C.Q = 2208 l^2.

The discriminant degree is

R_pi.pi^*D
=(H+2G+2F).l(20G+18F)
=688 l.

Hence (DISC-BOUND) would require

2208 l^2 <= 688 l,

which is impossible for every integer l>=1.

Therefore r != 2.

## r=1

For r=1,

pi^*D=l(40G+36F),

Q=l(40G+36F-P).

Then

C.Q
=l^2 P.(40G+36F-P)
=l^2(40*36+36*40-336)
=2544 l^2.

So

2C.Q=5088 l^2.

The discriminant degree is

R_pi.pi^*D
=(H+2G+2F).l(40G+36F)
=1376 l.

Thus one would need

5088 l^2 <= 1376 l,

again impossible for every l>=1.

Therefore r != 1.

## Conclusion

All four possible restriction degrees are excluded:

r=4: finite-map residual orthogonality / H-degree contradiction.
r=3: residual curve has negative arithmetic genus.
r=2: discriminant-resultant cross-intersection contradiction.
r=1: discriminant-resultant cross-intersection contradiction.

Hence no integral carrier C in |lP| can exist on the balanced support orbit

000707000f0f

for any l>=1.

By Aut(S) transport, the entire size-768 orbit is excluded.

Balanced hard core update:

before this route:
  0000770000ff   size 48 survives
  00007b0000ff   size 48 survives
  000707000f0f  size768 survives

after:
  0000770000ff   size48 survives
  00007b0000ff   size48 survives
  000707000f0f   size768 excluded PRE-AUDIT

remaining balanced supports: 96 in two Aut(S) orbits.

## Source gate

The load-bearing external algebra is the classical multiplicativity formula

disc(fg)=disc(f)disc(g)Res(f,g)^2,

applied after normalization/base change of D to the finite flat degree-four cover.
For geometric finite covers, the discriminant divisor is the pushforward of the different /
ramification divisor in characteristic zero, and projection formula gives its degree on D.

This note remains PRE-AUDIT until the finite-flat base-change and resultant/intersection
identification are hostile source-checked in the exact geometric setting.

## Firewalls

excluded_orbit_pre_audit=000707000f0f
excluded_support_count_pre_audit=768
remaining_balanced_support_count_pre_audit=96
whole_MB104_closed=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
