# MB104 — 000707 degree-four pair-map discriminant preflight — corrected 2026-09-20

Status: PRE-AUDIT NUMERICAL PREFLIGHT / STEIN CORRECTION OPEN / ZERO EXCLUSION CREDIT / NO MERGE

## Setup

Use the retained classes G and F with

H.G=12, P.G=36,
H.F=8,  P.F=40,
G.F=4.

The product map pi=(f_G,f_F):S->P1xP1 is generically degree four, but it contracts common vertical curves on the smooth resolution. Therefore the finite-cover discriminant/resultant argument cannot be applied directly on S.

Numerically,

R_pi = H+2G+2F,
H.R_pi = 56.

For a hypothetical carrier C in |lP| and D=pi(C), put r=deg(C->D). The corrected restriction-degree note keeps all r=1,2,3,4 OPEN.

For r=2,

pi^*D=l(20G+18F),
Q=l(20G+18F-P),
C.Q=1104l^2,
2C.Q=2208l^2.

The naive finite-cover discriminant degree would be 688l.

For r=1,

pi^*D=l(40G+36F),
Q=l(40G+36F-P),
C.Q=2544l^2,
2C.Q=5088l^2,

while the naive finite-cover discriminant degree would be 1376l.

Thus the finite model would have a very large quadratic-versus-linear margin. This is only a **conditional numerical signal**. On S, common contracted curves can alter the horizontal/residual intersection bookkeeping, so neither r=1 nor r=2 is excluded.

The classical identity

disc(fg)=disc(f)disc(g)Res(f,g)^2

remains the intended finite-model mechanism, but the exact geometric adapter is missing.

## Required adapter

Before any exclusion can be promoted:

1. construct the Stein factorization S -> X -> P1xP1;
2. identify every common vertical curve contracted by the pair map;
3. identify the horizontal carrier factor and residual factor on X;
4. prove how C.Q on S differs from the resultant intersection on X;
5. prove the discriminant/different degree on X with all correction terms;
6. show that the corrected upper bound is still smaller than the quadratic cross-intersection.

## Correct retained conclusion

No orbit is excluded.

Remaining balanced orbits:
- 0000770000ff, size 48;
- 00007b0000ff, size 48;
- 000707000f0f, size 768.

Remaining balanced support count: 864.

The size-768 orbit is **not** excluded at this boundary. The pair-map route remains a pre-audit, zero-credit numerical preflight until the Stein/common-vertical adapter is complete.

No MB104, receiver, theorem, endpoint, Perfect-Cuboid, or merge credit is granted.
