# Stage32 post-1518 O210 Q602 canonical residue 73 trace spectrum

Scope: fixed audited O210/Q602 leaf only, after the hostile-audited marked-gauge compression `{73,97,235} -> 73`. This note derives a new gauge-invariant necessary trace/diagonal-intersection condition. It does not exclude Q602 or O210.

## 1. Audited canonical residue and trace lattice

Use the audited canonical marked-gauge representative `73` in the retained coordinate order

`(t11.a,t11.b,t12.a,t12.b,t21.a,t21.b,t22.a,t22.b)`

for entries `a+b*r` with `r^2=-2`. Little-endian residue 73 therefore gives

`x mod 2 = (1,0,0,1,0,0,1,0)`.

The retained exact Rosati trace lattice has Gram matrix `A` and unimodular column matrix `U` with

`U^t A U = D4 direct-sum D4`.

Writing `x=U*y`, exact reduction mod 2 gives

`y mod 2 = (1,0,0,0 | 1,0,1,0)`.

The rational trace of a matrix over `Q(r)` on the underlying four-dimensional Q-space is

`Tr_Q(T)=2*(t11.a+t22.a)`.

In the retained D4+D4 coordinates this becomes

`Tr_Q(T) = -2*y2 + 4*y4`.

Conjugation by the principal Bolza automorphisms used in the audited gauge compression preserves this rational trace, so this is a gauge-invariant arithmetic condition on the canonical representative.

## 2. Q=602 forces trace 4 mod 8

For one D4 block with coordinates `(a,b,c,d)`, write half the D4 norm as

`m(a,b,c,d)=a^2+b^2+c^2+d^2-b*(a+c+d)`.

Since `Q(T)=602`, the two half-norms satisfy

`m1+m2=301`.

For the second block parity `(1,0,1,0)`, direct reduction gives

`m2 = 2 (mod 4)`.

Hence `m1 = 3 (mod 4)`. For the first block parity `(1,0,0,0)`, write `b=2B`; then

`m1 = 1-2B (mod 4)`.

Therefore `B` is odd, so `y2=b=2 (mod 4)`. Also `y4` is even. Thus

`Tr_Q(T) = -2*y2+4*y4 = 4 (mod 8)`.

This strengthens the initial mod-4 observation.

## 3. Diagonal-intersection bridge

Use Igor Dolgachev and Yuri G. Zarhin, *Endomorphisms of Complex Abelian Varieties*, April 8, 2025, Chapter 10, Section 10.1, equation (10.1). For a correspondence `D` of bidegree `(d1,d2)`,

`t(D)=d1+d2-(D,Delta)=tr((u_D)_r)`.

For the retained correspondence `Gamma` of bidegree `(105,81)`, this gives

`Tr_Q(T)=186-(Gamma,Delta)`.

Therefore every geometric survivor in canonical gauge satisfies

`(Gamma,Delta) = 6 (mod 8)`.

## 4. Exact Q602 trace spectrum

A lightweight exact 4+4 enumeration in the D4+D4 coordinates, with the fixed parity above and `m1+m2=301`, gives exactly `13,674,752` integral matrices in residue 73. Their rational traces are exactly

`{-68,-60,-52,-44,-36,-28,-20,-12,-4,4,12,20,28,36,44,52,60,68}`.

Consequently the diagonal intersection is restricted to exactly

`{118,126,134,142,150,158,166,174,182,190,198,206,214,222,230,238,246,254}`.

This is a necessary finite spectrum only. No geometric realization of any lattice point is inferred.

## Verdict / next leaf

Promote only after hostile audit:

- canonical residue 73 + Q602 forces `Tr_Q(T)=4 mod 8`;
- equivalently `(Gamma,Delta)=6 mod 8`;
- the exact trace spectrum has 18 values and the exact diagonal-intersection spectrum has 18 values;
- Q602 and O210 remain open; O212+ remains blocked.

The next exact leaf is to test the 18-value diagonal-intersection spectrum against retained common-cover / marked-branch geometry, without reopening the already-audited locator search, Rosati-only nonexclusion, or gauge-orbit work.
