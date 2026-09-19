# MB104 — 000707 degree-four pair-map restriction-degree reduction — 2026-09-20

Status: PRE-AUDIT NUMERICAL PREFLIGHT / COMMON-VERTICAL CORRECTION OPEN / ZERO CREDIT / NO MERGE

Use the new genus-seven fibration class G and one of the rank-three genus-five fiber classes F with

H.G=12,
P.G=36,
H.F=8,
P.F=40,
G.F=4.

The product map

pi=(f_G,f_F): S -> P1 x P1

is generically finite of degree 4, but not finite on the smooth resolution because common vertical curves are contracted.

Let C be a hypothetical integral MB carrier in |lP| with elliptic normalization, and let D=pi(C).
Write r for the degree of C -> D. Since pi has degree four,

r in {1,2,3,4}.

Let A,B be the two ruling classes on P1 x P1 with

pi^*A=G,
pi^*B=F.

Because the two projections of C have degrees 36l and 40l, the image curve D has bidegree

(40l/r, 36l/r)

with the convention D ~ (40l/r) A + (36l/r) B.

Hence

pi^*D = l[(40/r)G + (36/r)F].

The full inverse image pi^{-1}(D) contains C. Define the residual effective divisor

Q = pi^*D - C.

Numerically,

Q = l[(40/r)G + (36/r)F - P].

Using
G^2=F^2=0,
G.F=4,
P.G=36,
P.F=40,
P^2=336,
H.G=12,
H.F=8,
H.P=112,

one gets

Q.G/l = 144/r - 36,
Q.F/l = 160/r - 40,

Q.H/l = 768/r - 112,

Q^2/l^2 = 11520/r^2 + 336 - 5760/r.

## r=4 is impossible

For r=4,

Q.G=Q.F=0.

Since pi is finite, no positive-dimensional irreducible curve is contracted by both fibrations.
Therefore an effective residual Q with both intersections zero must be zero.

But Q=0 would imply

P = 10G + 9F.

Intersecting with H gives

112 = H.P = 10*12 + 9*8 = 192,

contradiction.

This does not yet exclude r=4: Q may be supported on common vertical curves contracted by the product map.

## r=3 is impossible

For r=3,

Q.H = 144l,
Q^2 = -304 l^2.

Because pi has total degree four and C -> D has degree three, over the generic point of D there is
exactly one remaining point of pi^{-1}(D). In characteristic zero the residual Q therefore has one
horizontal irreducible component mapping birationally to D; there are no vertical components
because pi is finite. Hence Q is an effective integral curve generically reduced along that
component and adjunction applies to its divisor class.

Its arithmetic genus is

p_a(Q)
 = 1 + (Q^2 + H.Q)/2
 = 1 - 152 l^2 + 72 l.

For every l>=1,

1 - 152 l^2 + 72 l < 0,

impossible for an effective integral curve.

This does not yet exclude r=3: Q may contain common vertical components, so the total divisor cannot be treated as one integral curve without a Stein-factor correction.

## Remaining cases

No restriction degree is promoted as excluded until the common-vertical locus is contracted and its correction is bounded.

For reference:

r=2:
Q.H = 272l,
Q^2 = 336 l^2,
Q.G = 36l,
Q.F = 40l.

r=1:
Q.H = 656l,
Q^2 = 6096 l^2,
Q.G = 108l,
Q.F = 120l.

The r=2 case is structurally special: the degree-four cover of D splits generically into two
degree-two pieces, C and Q (or Q may split into two degree-one sheets). This is the natural place
to look for an involution / quadratic intermediate cover / monodromy obstruction.

The r=1 case says C is birational to its image in P1 x P1 and should be attacked by the image
bidegree (40l,36l), conductor/delta, and the ramification divisor of pi.

The ramification divisor of pi is

R_pi = K_S - pi^*K_(P1xP1)
     = H + 2G + 2F.

Thus

P.R_pi = 112 + 2*36 + 2*40 = 264,

so

C.R_pi = 264l.

This is linear in l, while the intrinsic conductor different of C has degree

336l^2 + 112l.

This linear/quadratic separation is the next input for r=1 and r=2.

Decision:

PAIR_MAP_DEGREE = 4
C_TO_IMAGE_DEGREE_R4 = EXCLUDED
C_TO_IMAGE_DEGREE_R3 = EXCLUDED
REMAINING = {1,2}
NEXT = R2_INTERMEDIATE_QUADRATIC_COVER_OR_MONODROMY; R1_BIRATIONAL_IMAGE_CONDUCTOR
MB104_COMPLETE = false
THEOREM_CREDIT = false
ENDPOINT_CREDIT = false
MERGE_AUTHORIZED = false


## Hostile correction

The product map is only generically finite.  All restriction-degree exclusions in this note are
now treated as conditional numerical signals, not conclusions.  Required next step: exact common
vertical locus + Stein-factor correction.
