# MB104 — 000707 degree-four pair-map restriction-degree reduction — corrected 2026-09-20

Status: PRE-AUDIT NUMERICAL PREFLIGHT / COMMON-VERTICAL CORRECTION OPEN / ZERO EXCLUSION CREDIT / NO MERGE

## Exact retained setup

Let G be the retained genus-seven fibration class and F a retained rank-three genus-five fibration class satisfying

H.G=12,  P.G=36,
H.F=8,   P.F=40,
G.F=4.

The product morphism

pi=(f_G,f_F): S -> P1 x P1

is generically finite of degree four because G.F=4. It is **not finite on the smooth resolution**: common vertical curves are contracted. Every restriction-degree statement below is therefore only a numerical signal until the Stein-factor/common-vertical correction is source-complete.

Let C be a hypothetical integral MB carrier in |lP| with elliptic normalization, let D=pi(C), and let r=deg(C->D). Then r is one of 1,2,3,4. The projection degrees are

C.G=36l,  C.F=40l,

so D has bidegree (40l/r,36l/r) and

pi^*D = l[(40/r)G+(36/r)F].

Write Q=pi^*D-C as a divisor class. Using
G^2=F^2=0, G.F=4, P.G=36, P.F=40, P^2=336,
H.G=12, H.F=8, H.P=112,

Q.G/l = 144/r-36,
Q.F/l = 160/r-40,
Q.H/l = 768/r-112,
Q^2/l^2 = 11520/r^2+336-5760/r.

These identities are exact numerical identities. They do **not** imply that Q has no common-vertical components.

## r=4 conditional signal

For r=4,

Q.G=Q.F=0.

If the product map were finite, an effective residual divisor orthogonal to both rulings would have no horizontal component, and Q=0 would imply

P=10G+9F.

Intersecting H would give 112=192, impossible.

On the actual smooth resolution this is not an exclusion: Q may contain common vertical curves. Therefore

r=4: UNEXCLUDED / CONDITIONAL NUMERICAL SIGNAL ONLY.

## r=3 conditional signal

For r=3,

Q.H=144l,
Q^2=-304l^2.

If Q were exactly one integral horizontal residual curve with no common-vertical correction, adjunction would give

p_a(Q)=1-152l^2+72l<0

for every l>=1.

That hypothesis is not established on the smooth resolution. Therefore

r=3: UNEXCLUDED / CONDITIONAL NUMERICAL SIGNAL ONLY.

## r=2 and r=1

For r=2,

Q.H=272l,
Q^2=336l^2,
Q.G=36l,
Q.F=40l.

For r=1,

Q.H=656l,
Q^2=6096l^2,
Q.G=108l,
Q.F=120l.

The ramification class of the generically finite pair map is numerically

R_pi = H+2G+2F,

so P.R_pi=264 and C.R_pi=264l. This linear quantity is potentially useful against quadratic conductor/intersection terms, but only after passing through the finite Stein factor and accounting for the contracted locus.

## Correct conclusion

No restriction degree is excluded at this retained boundary:

r=1: OPEN
r=2: OPEN
r=3: OPEN
r=4: OPEN

The exact retained gain is the degree-four pair-map numerical package and the identification of the missing adapter:

1. form the Stein factorization S -> X -> P1xP1;
2. identify the complete common vertical exceptional locus;
3. transport the carrier/residual intersections to X;
4. bound all correction terms;
5. only then reconsider restriction-degree exclusion.

No MB104, receiver, theorem, endpoint, or merge credit is granted.
